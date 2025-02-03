import json
import os
import re
import subprocess
import sys
import time

from arcana import templates
from arcanalib.graph import Edge, Graph, Node, triplets, invert, lift
from arcanalib.pipefilter import Filter, Seeder
from collections import Counter, defaultdict
from collections.abc import Iterable
from io import TextIOWrapper
from itertools import combinations
from openai import OpenAI
from tqdm.auto import tqdm
from typing import Dict, Any, Tuple, List


def remove_author(s):
	return '\n'.join(t.strip() for t in s.split('\n') if not '@author' in t)


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
	if not s:
		return ""
	t = s.strip()
	if not t:
		return ""
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


def layers_to_list(d):
    result = []
    i = 1
    while True:
        name_key, desc_key = f"layer{i}name", f"layer{i}desc"
        if name_key not in d or desc_key not in d:
            break
        result.append((d[name_key], d[desc_key]))
        i += 1
    return result


class CLISeeder(Seeder):

	def __init__(self, command) -> None:
		"""
		Initialize the seeder with a command.

		:param command: The command to be executed.
		"""
		self.command = command

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

		sys.stderr.write(process.stderr)
		
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
		parents = {e.source: e.target for e in invert(data.edges['contains'])}
		dependency_profiles = {}

		calls = data.edges.get('calls', lift(data.edges['hasScript'], data.edges['invokes'], 'calls'))

		for edge in calls:
			source_id, target_id = edge.source, edge.target
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
			data.nodes[id].properties['dependencyProfile'] = dependency_profile_category(
				profile['in'],
				profile['out']
			)

		return data

def build_triplets(edge_list1, edge_list2) -> dict:
 
	methods = sorted(triplets(edge_list1, edge_list2))
 
	return methods
	
def build_hierarchy(method_triplets) -> dict:
	classes = sorted({(pkg, clz) for pkg, clz, _ in method_triplets})
	packages = sorted({pkg for pkg, _ in classes})

	hierarchy = {
		pkg_id: {
			cls_id: [met_id for _, c, met_id in method_triplets if c == cls_id]
			for p, cls_id in classes if p == pkg_id
		} for pkg_id in packages
	}

	return hierarchy

class CustomJSONEncoder(json.JSONEncoder):
	def default(self, obj):
		if isinstance(obj, set):
			# Convert set to list
			return list(obj)
		# Call the default method for other types
		return super().default(obj)

def group_paths_by_endpoints(paths: List[List[Edge]]) -> Dict[Tuple[str, str], List[List[Edge]]]:
	"""
	Groups paths by the tuple of (first edge's source, last edge's target).

	Args:
		paths (List[List[Edge]]): The list of paths to group.

	Returns:
		Dict[Tuple[str, str], List[List[Edge]]]: A dictionary where keys are 
		tuples (first edge's source, last edge's target), and values are lists of paths.
	"""
	grouped_paths = defaultdict(list)
	for path in paths:
		if path:  # Ensure the path is not empty
			start = path[0].source
			end = path[-1].target
			grouped_paths[(start, end)].append(path)
	return grouped_paths

def format_layers(layers):
    return "\n".join(f"- **{name}**: {desc}" for name, desc in layers)

class LLMFilter(Filter):
	def __init__(self, config: Dict[str, Dict[str, Any]]):
		super().__init__(config)
		self.project_name = None
		self.project_desc = None
		self.openai_client_args = None
		
		layers = layers_to_list(config["layers"]) if "layers" in config else None
		if not layers:
			layers = [
				("Presentation Layer", "Manages the user interface, defines UI elements and behavior, displays information, responds to user input, and updates views."),
				("Service Layer", "Controls the application flow, orchestrates domain operations, connects UI events with domain logic, and synchronizes domain changes with the UI."),
				("Domain Layer", "Handles business logic, represents domain data and behavior, and performs necessary computations for domain operations."),
				("Data Source Layer", "Interacts with databases, filesystems, hardware, messaging systems, or other data sources, performs CRUD operations, handles data conversion, and ensures data integrity."),
			]
		self.layers = layers
		self.layers_text = format_layers(layers)
  
		

	def process(self, data: Graph) -> Graph:
		"""
		Process the data using a language model to generate descriptions.

		Args:
			data (Graph): The input data.

		Returns:
			Graph: The processed data with generated descriptions.
		"""
		self.project_name, self.project_desc, self.openai_client_args, model, client = self.setup()
		timestr = time.strftime("%Y%m%d-%H%M%S")
  
		for i,(name,desc) in enumerate(self.layers):
			data.add_node(f"layer:{name}", "Grouping", kind="architectural layer", simpleName=name, qualifiedName=name, description=desc, layerOrder=i)
   
		for i in range(len(self.layers)-1):
			src = self.layers[i][0]
			tgt = self.layers[i+1][0]
			data.add_edge(f"layer:{src}", f"layer:{tgt}", "allowedDependency", weight=1)

		with open(f'arcana-{timestr}.jsonl', 'a', encoding="utf-8") as jsonl_file:
			with open(f'arcana-{timestr}.log', 'a', encoding="utf-8") as log_file:
				try:
					self.process_hierarchy(data, client, model, jsonl_file, log_file)
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
		model = self.config['llm'].get('model', "gpt-4o-mini")

		client = OpenAI(**openai_client_args)

		return project_name, project_desc, openai_client_args, model, client

	def describe(self, node: dict, *keys) -> str:
		"""Generate a description for a given node."""
		sr, sn = '\r', '\n'
		if not keys:
			keys = ['description', 'docComment', 'returns', 'reason', 'howToUse', 'howItWorks', 'assertions', 'stereotype', 'roleStereotype', 'layer']

		lines = {key:f"**{key}**: {sentence(str(node.properties[key]).replace(sr,'').replace(sn,' '))} " for key in keys if key in node.properties and key != 'docComment' and node.properties[key]}
		if 'docComment' in keys and 'docComment' in node.properties and node.properties['docComment']:
			lines['docComment'] = f"**docComment**: {sentence(remove_author(str(node.properties['docComment'])).replace(sr,'').replace(sn,' '))} "

		return ' '.join(lines[key] for key in keys if key in lines)

	def process_hierarchy(self, data: Graph, client: OpenAI, model: str, jsonl_file, log_file):
		"""Process each package, class, and method in the hierarchy."""
  
		st_contains_st = data.find_edges(label='contains',source_label='Structure',target_label='Structure')
		ct_contains_st = data.find_edges(label='contains',target_label='Structure', where_source=lambda node: 'Container' in node.labels and 'Structure' not in node.labels)
		new_ct_sources = {edge.target:data.find_source(data.edges['contains'],data.nodes[edge.target],lambda node:'Structure' not in node.labels,data.nodes[edge.source]).id for edge in st_contains_st}
		ct_contains_st.extend([Edge(source=source, target=target, label='contains') for target, source in new_ct_sources.items()])
  
		triplets = build_triplets(ct_contains_st, data.edges['hasScript'])
		met_to_cls_pkg = {met_id: (cls_id, pkg_id) for pkg_id, cls_id, met_id in triplets}
		# print(met_to_cls_pkg)
		# print('######################################################################')
		sorted_method_ids, method_deps = data.toposorted_nodes(data.edges['invokes'])
		# print(sorted_method_ids)
  
		counter = 0
  
		for met_id in tqdm(sorted_method_ids, desc='Processing methods', position=0, leave=False):
			cls_id, pkg_id = met_to_cls_pkg[met_id]
			clasz = data.nodes[cls_id]

			class_name = clasz.properties['qualifiedName']
			class_kind = clasz.properties['kind']
			class_kind = 'enum' if class_kind == 'enumeration' else 'abstract class' if class_kind == 'abstract' else class_kind
			self.process_method(data, client, model, jsonl_file, log_file, met_id, class_name, class_kind, method_deps)

			if os.path.exists('stop'):
				raise StopIteration

			counter += 1
			if counter==10:
				log_file.flush()
				jsonl_file.flush()
				counter %= 10

  
		hierarchy = build_hierarchy(triplets)
		# print(hierarchy)
		# print('==========')
  
		sorted_pkg_ids, pkg_deps = data.toposorted_nodes(data.find_edges(label='contains',where_source=lambda node: 'Structure' not in node.labels,where_target=lambda node: 'Structure' not in node.labels))
		# print(sorted_pkg_ids)
		# print('==========')
  
		# print(pkg_deps)
		# print('==========')
  
		for pkg_id in tqdm(sorted_pkg_ids, desc="Processing packages", position=1):
			pkg_data = hierarchy.get(pkg_id, dict())
			package = data.nodes[pkg_id]

			for cls_id, cls_data in tqdm(pkg_data.items(), desc="Processing classes", position=2, leave=False):
				clasz = data.nodes[cls_id]

				class_name = clasz.properties['qualifiedName']
				class_kind = clasz.properties['kind']
				class_kind = 'enum' if class_kind == 'enumeration' else 'abstract class' if class_kind == 'abstract' else class_kind

				self.process_class(data, client, model, jsonl_file, log_file, cls_id, clasz, class_name, class_kind, cls_data)

				if os.path.exists('stop'):
					raise StopIteration

			self.process_package(data, client, model, jsonl_file, log_file, pkg_id, package, pkg_data, pkg_deps)


			log_file.flush()
			jsonl_file.flush()

			if os.path.exists('stop'):
				raise StopIteration

		paths = data.find_paths("contains", "hasScript", "invokes", "-hasScript", "-contains")
		path_groups = group_paths_by_endpoints(paths)
  
		pkg_pairs = list(combinations(sorted_pkg_ids,2))
		for pkg2_id, pkg1_id in tqdm(pkg_pairs, desc='Processing package interactions', position=0, leave=False):
			pkg1 = data.nodes[pkg1_id]
			pkg2 = data.nodes[pkg2_id]
			if ('Structure' not in pkg1.labels) and ('Structure' not in pkg2.labels):
				if path_groups[(pkg1_id,pkg2_id)]:
					self.process_interactions(data, client, model, pkg1, pkg2, path_groups[(pkg1_id,pkg2_id)], hierarchy, jsonl_file, log_file)
				if path_groups[(pkg2_id,pkg1_id)]:
					self.process_interactions(data, client, model, pkg2, pkg1, path_groups[(pkg2_id,pkg1_id)], hierarchy, jsonl_file, log_file)

	def process_method(self, data: Graph, client: OpenAI, model: str, jsonl_file: TextIOWrapper, log_file: TextIOWrapper, met_id: str, class_name: str,
						class_kind: str, node_deps: dict):
		"""Process a single method and generate its description."""
		method = data.nodes[met_id]

		if 'description' not in method.properties or not method.properties['description']:
			method_name = method.properties['simpleName']
			method_src = remove_java_comments(method.properties['sourceText'])

			prompt = templates.script_analysis.format(
				op_name=method_name,
				struct_kind=class_kind,
				struct_name=class_name,
				op_src=method_src,
				other_ops="(none)" if not node_deps[met_id] else "\n".join(f"- `{data.nodes[node_id].properties['simpleName']}`: {self.describe(data.nodes[node_id], 'description', 'returns', 'docComment')}" for node_id in node_deps[met_id]),
				project_name=self.project_name,
				project_desc=self.project_desc,
				layers=self.layers_text
			)
   
			log_file.write(prompt)
			log_file.write('\n\n======\n\n')

			description = self.generate_json_description(client, model, prompt)
			self.update_method_properties(data, description, method)

			layer_id = None
			if method.has_property("layer") and \
   					method.property("layer") in [name for name, _ in self.layers]:
				layer_id = f"layer:{method.property('layer')}"
			layer_node = data.find_node(label="Grouping", where=lambda node: node.id == layer_id)
			if layer_node:
				data.add_edge(method.id, layer_node.id, "implements", weight=1)

			jsonl_file.write(json.dumps({
				'data': {
					'id': method.id,
					'labels': method.labels,
					'properties': description
				}
			}, cls=CustomJSONEncoder))
			jsonl_file.write('\n')
   
	def process_class(self, data: Graph, client: OpenAI, model: str, jsonl_file, log_file, cls_id: str, clasz: dict, class_name: str,
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
  
		log_file.write(prompt)
		log_file.write('\n\n======\n\n')

		description = self.generate_json_description(client, model, prompt)
		self.update_class_properties(data, description, clasz)

		jsonl_file.write(json.dumps({
			'data': {
				'id': clasz.id,
				'labels': list(clasz.labels),
				'properties': description
			}
		}))
		jsonl_file.write('\n')

	def process_package(self, data: Graph, client: OpenAI, model: str, jsonl_file, log_file, pkg_id: str, package: dict,
						pkg_data: dict, pkg_deps: dict):
		"""Process a single package and generate its description."""
		classes_descriptions = self.get_classes_descriptions(data, pkg_data)
		package_descriptions = self.get_packages_descriptions(data, pkg_deps[pkg_id])

		prompt = templates.component_analysis.format(
			pkg_name=package.properties['qualifiedName'],
			classes="(none)" if not classes_descriptions else "\n".join(classes_descriptions),
			packages="(none)" if not package_descriptions else "\n".join(package_descriptions),
			project_name=self.project_name,
			project_desc=self.project_desc,
			layers=self.layers_text
		)

		log_file.write(prompt)
		log_file.write('\n\n======\n\n')

		description = self.generate_json_description(client, model, prompt)
		self.update_package_properties(data, description, package)

		layer_id = None
		if package.has_property("layer") and \
				package.property("layer") in [name for name, _ in self.layers]:
			layer_id = f"layer:{package.property('layer')}"
		layer_node = data.find_node(label="Grouping", where=lambda node: node.id == layer_id)
		if layer_node:
			data.add_edge(package.id, layer_node.id, "implements", weight=1)

		jsonl_file.write(json.dumps({
			'data': {
				'id': package.id,
				'labels': list(package.labels),
				'properties': description}}))
		jsonl_file.write('\n')

	def process_interactions(self, data: Graph, client: OpenAI, model: str, pkg1: Node, pkg2: Node, path_groups: List[Edge], hierarchy, jsonl_file: TextIOWrapper, log_file: TextIOWrapper):
		pkg1_name = pkg1.properties["qualifiedName"]
		pkg2_name = pkg2.properties["qualifiedName"]
		pkg1_desc = pkg1.properties["description"]
		pkg2_desc = pkg2.properties["description"]
  
		pkg1_data = hierarchy.get(pkg1.id, dict())
		pkg2_data = hierarchy.get(pkg2.id, dict())
  
		cls1_info = "\n".join(f"        - `{data.nodes[c_id].properties['simpleName']}`: {data.nodes[c_id].properties['description']}" for c_id, _ in pkg1_data.items())
		cls2_info = "\n".join(f"        - `{data.nodes[c_id].properties['simpleName']}`: {data.nodes[c_id].properties['description']}" for c_id, _ in pkg2_data.items())
  
		def describe_path(path):
			src_cls = data.nodes[path[1].source]
			src_mth = data.nodes[path[1].target]
			tgt_mth = data.nodes[path[-2].source]
			tgt_cls = data.nodes[path[-2].target]
			return f"Method `{src_mth.properties['simpleName']}` ({src_mth.properties['description']}) of class `{src_cls.properties['qualifiedName']}` invokes method `{tgt_mth.properties['simpleName']}` ({tgt_mth.properties['description']}) of class `{tgt_cls.properties['qualifiedName']}`."
  
		dep_info = f"    - Dependencies from `{pkg1_name}` to `{pkg2_name}`:\n" + "\n".join(f"        - {describe_path(path)}" for path in path_groups) if path_groups else ""
  
		prompt = templates.interaction_analysis.format(
			project_name=self.project_name,
			project_desc=self.project_desc,
			pkg1_name=pkg1_name,
			pkg2_name=pkg2_name,
			pkg1_desc=pkg1_desc,
			pkg2_desc=pkg2_desc,
			cls1_info=cls1_info,
			cls2_info=cls2_info,
			dep_info=dep_info
		)

		log_file.write(prompt)
		log_file.write('\n\n======\n\n')

		description = self.generate_text_description(client, model, prompt)
		pkg1_edge = Edge(source=pkg1.id, target=pkg2.id, label="dependsOn", description=description) if dep_info else None

		if pkg1_edge:
			if "dependsOn" not in data.edges:
				data.edges["dependsOn"] = []
			data.edges["dependsOn"].append(pkg1_edge)
			jsonl_file.write(json.dumps(pkg1_edge.to_dict(), cls=CustomJSONEncoder))
			jsonl_file.write('\n')

	def generate_json_description(self, client: OpenAI, model: str, prompt: str) -> dict:
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

		if 'description' not in description:
			description['description'] = "(no description)"
		return description

	def generate_text_description(self, client: OpenAI, model: str, prompt: str) -> dict:
		"""Generate a description using the OpenAI client."""
		try:
			response = client.chat.completions.create(
				model=model,
				messages=[{"role": "user", "content": prompt}],
				max_tokens=4096,
				temperature=0
			)
			description = response.choices[0].message.content
		except:
			description = "(no description)"

		return description

	def update_method_properties(self, data: Graph, description: dict, method: Node):
		"""Update method properties with the generated description."""
		

		for key, value in description.items():
			if key.endswith('Reason'):
				continue
			key_lower = lower1(key)
			if key_lower == 'parameters' and isinstance(value, Iterable):
				param_nodes = [
						data.nodes[edge.target]
						for edge in data.edges['hasParameter']
						if edge.source == method.id
					]
				for param in value:
					matching_params = [
						node
						for node in param_nodes
						if node.properties['simpleName'] == param['name']
					]
					if matching_params:
						param_node_id = matching_params[0].id
						if param_node_id in data.nodes:
							data.nodes[param_node_id].properties['description'] = param.get('description')
			# elif key_lower == 'returns':
			# 	method.properties['returns'] = value.get('description', None) if value and hasattr(value, 'get') else None
			else:
				method.properties[key_lower] = value

	def update_class_properties(self, data: Graph, description: dict, clasz: Node):
		"""Update class properties with the generated description."""
		for key in description:
			if not key.endswith('Reason'):
				clasz.properties[lower1(key)] = description[key]

	def update_package_properties(self, data: Graph, description: dict, package: Node):
		"""Update package properties with the generated description."""
		for key in description:
			if not key.endswith('Reason'):
				package.properties[lower1(key)] = description[key]

	def get_class_relations(self, data: Graph, cls_id: str) -> tuple:
		"""Retrieve class ancestors and fields."""
		ancestors = {
			edge.target
			for edge in data.edges['specializes']
			if edge.source == cls_id
		}
		fields = {
			edge.target
			for edge in data.edges['hasVariable']
			if edge.source == cls_id
		}
		fields = [
			' '.join(remove_java_comments(data.nodes[field].properties['sourceText']).split())
			for field in fields
		]
		return ancestors, fields

	def get_methods_descriptions(self, data: Graph, cls_data: list) -> list:
		"""Generate descriptions for methods."""
		return [
			f"- `{data.nodes[met_id].properties['simpleName']}`: {self.describe(data.nodes[met_id])}"
			for met_id in cls_data
		]

	def get_classes_descriptions(self, data: Graph, pkg_data: dict) -> list:
		"""Generate descriptions for classes."""
		return [
			f"- {data.nodes[cls_id].properties['kind']} `{data.nodes[cls_id].properties['qualifiedName']}`: {self.describe(data.nodes[cls_id])}"
			for cls_id, _ in pkg_data.items()
		]

	def get_packages_descriptions(self, data: Graph, package_ids: list) -> list:
		"""Generate descriptions for packages."""
		return [
			f"- `{data.nodes[pkg_id].properties['qualifiedName']}`: {self.describe(data.nodes[pkg_id])}"
			for pkg_id in package_ids
		]


def merge_node_properties(dict1: Dict[str, Node], dict2: Dict[str, Node], simplify_names=False):
	for id2, obj2 in dict2.items():

		matched_obj: Node = None
		if id2 in dict1 and set(dict1[id2].labels) & set(obj2.labels):
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
				if {'Script', 'Operation', 'Constructor'} & set(dict1[key].labels)
			}

			if id2 in dict1_name_remap and set(dict1[dict1_name_remap[id2]].labels) & set(obj2.labels):
				matched_obj = dict1[dict1_name_remap[id2]]

		if matched_obj:
			# sys.stderr.write(f"{id2}->{matched_obj['id']}\n")
			# Merge properties from obj2 into matched_obj
			matched_obj.properties.update(obj2.properties)
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
		merge_node_properties(data.nodes, self.node_dict_to_merge, True)
		return data
