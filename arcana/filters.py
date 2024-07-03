import json
import os
import re
import subprocess
import time
from collections import Counter
from typing import Dict, Any

from openai import OpenAI
from tqdm.auto import tqdm

from arcana import templates
from arcanalib.graph import Graph, triplets, invert, lift
from arcanalib.pipefilter import Filter, Seeder


def remove_java_comments(java_source: str) -> str:
	"""
	Remove single-line and multi-line comments from a given Java source code string.

	Args:
		java_source (str): The Java source code as a string.

	Returns:
		str: The Java source code without comments.
	"""
	pattern = r"(//.*?$)|(/\*.*?\*/)"
	return re.sub(pattern, "", java_source, flags=re.MULTILINE | re.DOTALL).strip()


def sentence(s: str) -> str:
	"""
	Capitalize the first letter of a string and ensure it ends with a period.

	Args:
		s (str): The input string.

	Returns:
		str: The formatted string.
	"""
	t = s.strip()
	if t[-1] in '.?!…~–—':
		return f'{t[0].upper()}{t[1:]}'
	return f'{t[0].upper()}{t[1:]}.'


def lower1(s: str) -> str:
	"""
	Lowercase the first character of a string.

	Args:
		s (str): The input string.

	Returns:
		str: The string with the first character lowercased.
	"""
	return s[0].lower() + s[1:] if s else s


def prettify_json(obj: dict) -> str:
	"""
	Convert a dictionary to a pretty-printed JSON string.

	Args:
		obj (dict): The input dictionary.

	Returns:
		str: The pretty-printed JSON string.
	"""
	return json.dumps(obj, indent='\t')


class CLISeeder(Seeder):

	def __init__(self, command) -> None:
		"""
		Initialize the seeder with a command.

		:param command: The command to be executed.
		"""
		self.command = command

	# sys.stderr.write(f"Command: {self.command}\n")

	def generate(self) -> Graph:
		"""
		Execute the command, parse the JSON output into a dict, and pass the dict to the Graph constructor.

		:return: The generated Graph object.
		"""
		# Execute the command
		process = subprocess.run(
			self.command,
			capture_output=True,
			text=True,
   			encoding="utf-8"
		)
		
		# Parse the JSON output into a dict
		if process.returncode == 0:
			output_dict = json.loads(process.stdout)

			# Pass the dict to the Graph constructor and return the Graph object
			return Graph(output_dict)
		else:
			raise "Command execution failed."


class MetricsFilter(Filter):
	def process(self, data: Graph) -> Graph:
		"""
		Process the data to generate dependency profiles and categorize nodes.

		Args:
			data (Graph): The input data.

		Returns:
			Graph: The processed data with dependency profiles.
		"""
		parents = {e['source']: e['target'] for e in invert(data.edges['contains'])}
		dependency_profiles = {}

		calls = data.edges.get('calls', lift(data.edges['hasScript'], data.edges['invokes'], 'calls'))

		for edge in calls:
			source_id, target_id = edge['source'], edge['target']
			dependency_profiles.setdefault(source_id, [])
			dependency_profiles.setdefault(target_id, [])

			if parents[source_id] != parents[target_id]:
				dependency_profiles[source_id].append('out')
				dependency_profiles[target_id].append('in')

		dependency_profiles = {id: Counter(profile) for id, profile in dependency_profiles.items()}

		def dependency_profile_category(inn: int, out: int) -> str:
			if inn == 0 and out > 0:
				return "outbound"
			elif inn > 0 and out == 0:
				return "inbound"
			elif inn > 0 and out > 0:
				return "transit"
			return "hidden"

		for id, profile in dependency_profiles.items():
			data.nodes[id]['properties']['dependencyProfile'] = dependency_profile_category(
				profile['in'],
				profile['out']
			)

		return data


def build_hierarchy(data: Graph) -> dict:
	"""Build a hierarchical structure of packages, classes, and methods."""
	methods = sorted(triplets(data.edges['contains'], data.edges['hasScript']))
	classes = sorted({(pkg, clz) for pkg, clz, _ in methods})
	packages = sorted({pkg for pkg, _ in classes})

	hierarchy = {
		pkg_id: {
			cls_id: [met_id for _, c, met_id in methods if c == cls_id]
			for p, cls_id in classes if p == pkg_id
		} for pkg_id in packages
	}

	return hierarchy


class LLMFilter(Filter):
	def __init__(self, config: Dict[str, Dict[str, Any]]):
		super().__init__(config)
		self.project_name = None
		self.project_desc = None
		self.openai_client_args = None

	def process(self, data: Graph) -> Graph:
		"""
		Process the data using a language model to generate descriptions.

		Args:
			data (Graph): The input data.

		Returns:
			Graph: The processed data with generated descriptions.
		"""
		self.project_name, self.project_desc, self.openai_client_args, model, client = self.setup()

		hierarchy = build_hierarchy(data)
		timestr = time.strftime("%Y%m%d-%H%M%S")

		with open(f'arcana-{timestr}.jsonl', 'a', encoding="utf-8") as file:
			try:
				self.process_hierarchy(data, hierarchy, client, model, file)
			except StopIteration:
				pass

		return data

	def setup(self):
		"""Setup necessary configuration and client."""
		project_name = self.config['project']['name']
		project_desc = self.config['project']['desc']

		openai_client_args = {
			'api_key': self.config['llm'].get('apikey'),
			'base_url': self.config['llm'].get('apibase')
		}
		model = self.config['llm'].get('model', "gpt-3.5-turbo")

		client = OpenAI(**openai_client_args)

		return project_name, project_desc, openai_client_args, model, client

	def describe(self, node: dict) -> str:
		"""Generate a description for a given node."""
		keys = ['description', 'reason', 'howToUse', 'howItWorks', 'assertions', 'roleStereotype', 'layer']
		return ' '.join(f"**{key}**: {str(node['properties'][key])}. " for key in keys if key in node['properties'])

	def process_hierarchy(self, data: Graph, hierarchy: dict, client: OpenAI, model: str, file):
		"""Process each package, class, and method in the hierarchy."""
		for pkg_id, pkg_data in tqdm(hierarchy.items(), desc="Processing packages"):
			package = data.nodes[pkg_id]

			for cls_id, cls_data in tqdm(pkg_data.items(), desc="Processing classes", position=1, leave=False):
				clasz = data.nodes[cls_id]

				class_name = clasz['properties']['qualifiedName']
				class_kind = clasz['properties']['kind']
				class_kind = 'enum' if class_kind == 'enumeration' else 'abstract class' if class_kind == 'abstract' else class_kind

				for met_id in tqdm(cls_data, desc='Processing methods', position=2, leave=False):
					self.process_method(data, client, model, file, met_id, class_name, class_kind)

					if os.path.exists('stop'):
						raise StopIteration

				self.process_class(data, client, model, file, cls_id, clasz, class_name, class_kind, cls_data)

				if os.path.exists('stop'):
					raise StopIteration

			self.process_package(data, client, model, file, pkg_id, package, pkg_data)

			if os.path.exists('stop'):
				raise StopIteration

	def process_method(self, data: Graph, client: OpenAI, model: str, file, met_id: str, class_name: str,
	                   class_kind: str):
		"""Process a single method and generate its description."""
		method = data.nodes[met_id]

		if 'description' not in method['properties'] or not method['properties']['description']:
			method_name = method['properties']['simpleName']
			method_src = remove_java_comments(method['properties']['sourceText'])

			prompt = templates.script_analysis.format(
				op_name=method_name,
				struct_kind=class_kind,
				struct_name=class_name,
				op_src=method_src,
				project_name=self.project_name,
				project_desc=self.project_desc
			)

			description = self.generate_description(client, model, prompt)
			self.update_method_properties(data, description, method)

			file.write(json.dumps({
				'data': {
					'id': method['id'],
					'labels': method['labels'],
					'properties': description
				}
			}))
			file.write('\n')

	def process_class(self, data: Graph, client: OpenAI, model: str, file, cls_id: str, clasz: dict, class_name: str,
	                  class_kind: str, cls_data: list):
		"""Process a single class and generate its description."""
		ancestors, fields = self.get_class_relations(data, cls_id)
		methods_descriptions = self.get_methods_descriptions(data, cls_data)

		prompt = templates.structure_analysis.format(
			struct_type=class_kind,
			struct_name=class_name,
			ancestors="\n".join([f"- `{ancestor}`" for ancestor in ancestors]) if ancestors else "(none)",
			fields="\n".join([f"- `{field}`" for field in fields]) if fields else "(none)",
			methods="\n".join(methods_descriptions) if methods_descriptions else "(none)",
			project_name=self.project_name,
			project_desc=self.project_desc
		)

		description = self.generate_description(client, model, prompt)
		self.update_class_properties(data, description, clasz)

		file.write(json.dumps({
			'data': {
				'id': clasz['id'],
				'labels': clasz['labels'],
				'properties': description
			}
		}))
		file.write('\n')

	def process_package(self, data: Graph, client: OpenAI, model: str, file, pkg_id: str, package: dict,
	                    pkg_data: dict):
		"""Process a single package and generate its description."""
		classes_descriptions = self.get_classes_descriptions(data, pkg_data)

		prompt = templates.component_analysis.format(
			pkg_name=package['properties']['qualifiedName'],
			classes="\n".join(classes_descriptions),
			project_name=self.project_name,
			project_desc=self.project_desc
		)

		description = self.generate_description(client, model, prompt)
		self.update_package_properties(data, description, package)

		file.write(json.dumps({
			'data': {
				'id': package['id'],
				'labels': package['labels'],
				'properties': description}}))
		file.write('\n')

	def generate_description(self, client: OpenAI, model: str, prompt: str) -> dict:
		"""Generate a description using the OpenAI client."""
		try:
			response = client.chat.completions.create(
				model=model,
				response_format={"type": "json_object"},
				messages=[{"role": "user", "content": prompt}],
				max_tokens=1024,
				temperature=0
			)
			description = response.choices[0].message.content
		except:
			description = '{}'

		try:
			description = json.loads(description)
		except:
			description = dict()

		return description

	def update_method_properties(self, data: Graph, description: dict, method: dict):
		"""Update method properties with the generated description."""
		for key in description:
			if key.endswith('Reason'):
				continue
			elif lower1(key) == 'parameters':
				for parameter in description[key]:
					param_id = method['id'] + '.' + parameter['name']
					if param_id in data.nodes:
						data.nodes[param_id]['properties']['description'] = parameter.get('description')
			else:
				method['properties'][lower1(key)] = description[key]

	def update_class_properties(self, data: Graph, description: dict, clasz: dict):
		"""Update class properties with the generated description."""
		for key in description:
			if not key.endswith('Reason'):
				clasz['properties'][lower1(key)] = description[key]

	def update_package_properties(self, data: Graph, description: dict, package: dict):
		"""Update package properties with the generated description."""
		for key in description:
			if not key.endswith('Reason'):
				package['properties'][lower1(key)] = description[key]

	def get_class_relations(self, data: Graph, cls_id: str) -> tuple:
		"""Retrieve class ancestors and fields."""
		ancestors = {
			edge['target']
			for edge in data.edges['specializes']
			if edge['source'] == cls_id
		}
		fields = {
			edge['target']
			for edge in data.edges['hasVariable']
			if edge['source'] == cls_id
		}
		fields = [
			' '.join(remove_java_comments(data.nodes[field]['properties']['sourceText']).split())
			for field in fields
		]
		return ancestors, fields

	def get_methods_descriptions(self, data: Graph, cls_data: list) -> list:
		"""Generate descriptions for methods."""
		return [
			f"- `{data.nodes[met_id]['properties']['simpleName']}`: {self.describe(data.nodes[met_id])}"
			for met_id in cls_data
		]

	def get_classes_descriptions(self, data: Graph, pkg_data: dict) -> list:
		"""Generate descriptions for classes."""
		return [
			f"- {data.nodes[cls_id]['properties']['kind']} `{data.nodes[cls_id]['properties']['qualifiedName']}`: {self.describe(data.nodes[cls_id])}"
			for cls_id, _ in pkg_data.items()
		]


def merge_properties(dict1, dict2, simplify_names=False):
	for id2, obj2 in dict2.items():

		matched_obj = None
		if id2 in dict1 and set(dict1[id2]['labels']) & set(obj2['labels']):
			matched_obj = dict1[id2]

		elif simplify_names:

			def simplify_name(name):
				if '(' in name and name.endswith(')'):
					prefix, params = name.split('(', 2)
					params = [param.split('.')[-1].split('$')[-1] for param in params.split(')', 1)[0].split(',')]
					return prefix + '(' + ','.join(params) + ')'
				else:
					return name

			dict1_name_remap = {
				simplify_name(key): key
				for key in dict1
				if {'Script', 'Operation', 'Constructor'} & set(dict1[key]['labels'])
			}

			if id2 in dict1_name_remap and set(dict1[dict1_name_remap[id2]]['labels']) & set(obj2['labels']):
				matched_obj = dict1[dict1_name_remap[id2]]

		if matched_obj:
			# sys.stderr.write(f"{id2}->{matched_obj['id']}\n")
			# Merge properties from obj2 into matched_obj
			matched_obj['properties'].update(obj2['properties'])
		else:
			# sys.stderr.write(f"{id2}->None\n")
			pass


# Note: dict1 is updated in place, no need to return anything

class MergeFilter(Filter):
	def __init__(self, config: Dict[str, Dict[str, Any]]):
		super().__init__(config)

		with open(config['merge']['input'], 'r', encoding="utf-8") as file:
			data = json.load(file)
		self.node_dict_to_merge = data

	def process(self, data: Graph) -> Any:
		merge_properties(data.nodes, self.node_dict_to_merge, True)
		return data
