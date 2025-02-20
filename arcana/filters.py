import json
import os
import re
import subprocess
import sys
import time

from arcana import templates
from arcanalib.graph import Edge, Graph, Node, triplets, invert, lift
from arcanalib.pipefilter import Filter, Seeder
from collections import Counter, defaultdict, OrderedDict
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
			shell=True,
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
		parents = {e.source: e.target for e in invert(data.find_edges(label='contains'))}
		dependency_profiles = {}

		calls = data.edges.get('calls', lift(data.find_edges(label='hasScript'), data.find_edges(label='invokes'), 'calls'))

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

		with open(f'arcana-{timestr}.jsonl', 'a', encoding="utf-8") as jsonl_file:
		
			for i,(name,desc) in enumerate(self.layers):
				n = data.add_node(f"layer:{name}", "Grouping", kind="architectural layer", simpleName=name, qualifiedName=name, description=desc, layerOrder=i)
				jsonl_file.write(json.dumps(n.to_dict(), cls=CustomJSONEncoder))
				jsonl_file.write('\n')
		

			for i in range(len(self.layers)-1):
				src = self.layers[i][0]
				tgt = self.layers[i+1][0]
				e = data.add_edge(f"layer:{src}", f"layer:{tgt}", "allowedDependency", weight=1)
				jsonl_file.write(json.dumps(e.to_dict(), cls=CustomJSONEncoder))
				jsonl_file.write('\n')

			with open(f'arcana-{timestr}.log', 'a', encoding="utf-8") as log_file:
				try:
					self.process_hierarchy(data, client, model, jsonl_file, log_file)
				except StopIteration:
					pass

		return data

	def setup(self):
		"""Setup necessary configuration and client."""
		project_name = self.config['project']['name']
		project_desc = sentence(self.config['project']['desc'])

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

		lines = {key:f"**{key}**: {sentence(str(node.properties[key]).replace(sr,'').replace(sn,' '))}" for key in keys if key in node.properties and key != 'docComment' and node.properties[key]}
		if 'docComment' in keys and 'docComment' in node.properties and node.properties['docComment']:
			lines['docComment'] = f"**docComment**: {sentence(remove_author(str(node.properties['docComment'])).replace(sr,'').replace(sn,' '))} "

		return ' '.join(lines[key] for key in keys if key in lines).strip()

	def process_hierarchy(self, data: Graph, client: OpenAI, model: str, jsonl_file, log_file):
		"""Process each package, class, and method in the hierarchy."""
  
		st_contains_st = data.find_edges(label='contains',source_label='Structure',target_label='Structure')
		ct_contains_st = data.find_edges(label='contains',target_label='Structure', where_source=lambda node: 'Container' in node.labels and 'Structure' not in node.labels)
		new_ct_sources = {edge.target:data.find_source(data.find_edges(label='contains'),data.nodes[edge.target],lambda node:'Structure' not in node.labels,data.nodes[edge.source]).id for edge in st_contains_st}
		ct_contains_st.extend([Edge(source=source, target=target, label='contains') for target, source in new_ct_sources.items()])
  
		triplets = build_triplets(ct_contains_st, data.find_edges(label='hasScript'))
		met_to_cls_pkg = {met_id: (cls_id, pkg_id) for pkg_id, cls_id, met_id in triplets}
		# print(met_to_cls_pkg)
		# print('######################################################################')
		sorted_method_ids, method_deps = data.toposorted_nodes(data.find_edges(label='invokes'))
		# print(sorted_method_ids)
		
		counter = 0
  
		for met_id in tqdm(sorted_method_ids, desc='Processing methods', position=0, leave=False):
			cls_id, pkg_id = met_to_cls_pkg[met_id]
			method = data.nodes[met_id]
			clasz = data.nodes[cls_id]

			self.process_script(data, client, model, jsonl_file, log_file, method, clasz, method_deps)

			if os.path.exists('stop'):
				raise StopIteration

			counter += 1
			if counter==10:
				log_file.flush()
				jsonl_file.flush()
				counter %= 10

		hierarchy = build_hierarchy(triplets)
		sorted_pkg_ids, pkg_deps = data.toposorted_nodes(data.find_edges(label='contains',where_source=lambda node: 'Structure' not in node.labels,where_target=lambda node: 'Structure' not in node.labels))
		
		for pkg_id in tqdm(sorted_pkg_ids, desc="Processing packages", position=1):
			pkg_data = hierarchy.get(pkg_id, dict())
			package = data.nodes[pkg_id]

			for cls_id, cls_data in tqdm(pkg_data.items(), desc="Processing classes", position=2, leave=False):
				clasz = data.nodes[cls_id]

				self.process_structure(data, client, model, jsonl_file, log_file, clasz, cls_data)

				if os.path.exists('stop'):
					raise StopIteration

			self.process_component(data, client, model, jsonl_file, log_file, package, pkg_data, pkg_deps)

			log_file.flush()
			jsonl_file.flush()

			if os.path.exists('stop'):
				raise StopIteration

		paths = data.find_paths("contains", "hasScript", "invokes", "-hasScript", "-contains")
		path_groups = group_paths_by_endpoints(paths)
  
		pkg_pairs = list(combinations(sorted_pkg_ids,2))
		for pkg2_id, pkg1_id in tqdm(pkg_pairs, desc='Processing package interactions', position=0, leave=False):
      
			if os.path.exists('stop'):
				raise StopIteration

			pkg1 = data.nodes[pkg1_id]
			pkg2 = data.nodes[pkg2_id]
			if ('Structure' not in pkg1.labels) and ('Structure' not in pkg2.labels):
				if path_groups[(pkg1_id,pkg2_id)]:
					self.process_interactions(data, client, model, pkg1, pkg2, path_groups[(pkg1_id,pkg2_id)], hierarchy, jsonl_file, log_file)
				if path_groups[(pkg2_id,pkg1_id)]:
					self.process_interactions(data, client, model, pkg2, pkg1, path_groups[(pkg2_id,pkg1_id)], hierarchy, jsonl_file, log_file)

	def compose_prompt(self, p, function_parameters):
		prompt = p
		for k,v in function_parameters.items():
			if isinstance(v, dict) and len(v):
				prompt += f"## {k}\n\n"
				for k1,v1 in v.items():
					if v1:
						prompt += f"* {k1}: {str(v1)}\n"
				prompt += "\n\n"
			elif isinstance(v, list) and len(v):
				prompt += f"## {k}\n\n"
				for v1 in v:
					if v1:
						prompt += f"* {str(v1)}\n"
				prompt += "\n\n"
			elif v:
				prompt += f"## {k}\n\n{str(v)}\n\n"
		return prompt.strip()
    
	def process_script(self, graph: Graph, client: OpenAI, model: str, jsonl_file: TextIOWrapper, log_file: TextIOWrapper, script: Node, structure: Node, node_deps: dict):
		"""Process a single method and generate its description."""

		if 'description' not in script.properties or not script.properties['description'] or script.properties['description'] == "(no description)":
			script_name = script.properties['simpleName']
			script_src = remove_java_comments(script.properties['sourceText'])
			script_kind = script.properties.get('kind', 'function')
   
			structure_name = structure.properties['qualifiedName']
			structure_kind = structure.properties['kind']
			structure_kind = 'enum' if structure_kind == 'enumeration' else 'abstract class' if structure_kind == 'abstract' else structure_kind

			prompt = f"Describe the following {script_kind} by using the AnalyzeScript tool.\n\n"
			script_parameters = OrderedDict()
			script_parameters["Project Name"] = self.project_name
			script_parameters["Project Description"] = self.project_desc
			script_parameters[f"{script_kind.title()} Declaration"] = f"The {script_kind} {script_name} is declared within the {structure_kind} {structure_name}."
			script_parameters[f"{script_kind.title()} Source Code"] = script_src
			script_parameters[f"Other Functions/Methods Used"] = {
					graph.nodes[node_id].properties['qualifiedName']: f"{self.describe(graph.nodes[node_id], 'description', 'returns', 'howToUse', 'docComment')}" 
					for node_id in node_deps[script.id]
				}
			script_parameters["Possible Architectural Layers"] = dict(self.layers)

			prompt = self.compose_prompt(prompt, script_parameters)
   
			log_file.write(prompt)
			log_file.write('\n\n======\n\n')

			description = self.generate_json_description(client, model, prompt, "AnalyzeScript")
			self.update_method_properties(graph, description, script)

			layer_id = None
			if script.has_property("layer") and \
   					script.property("layer") in [name for name, _ in self.layers]:
				layer_id = f"layer:{script.property('layer')}"
			layer_node = graph.find_node(label="Grouping", where=lambda node: node.id == layer_id)
			if layer_node:
				e = graph.add_edge(script.id, layer_node.id, "implements", weight=1)
				jsonl_file.write(str(e), cls=CustomJSONEncoder)
				jsonl_file.write('\n')

			jsonl_file.write(json.dumps({
				'data': {
					'id': script.id,
					'labels': script.labels,
					'properties': description
				}
			}, cls=CustomJSONEncoder))
			jsonl_file.write('\n')
   
	def process_structure(self, graph: Graph, client: OpenAI, model: str, jsonl_file, log_file, structure: Node, structure_scripts: list):
		"""Process a single class and generate its description."""
  
		# if 'description' not in structure.properties or not structure.properties['description'] or structure.properties['description'] == "(no description)":
		ancestors, variables = self.get_structure_relations(graph, structure.id)
		script_descriptions = self.get_script_descriptions(graph, structure_scripts)

		structure_name = structure.properties['qualifiedName']
		structure_kind = structure.properties['kind']
		structure_kind = 'enum' if structure_kind == 'enumeration' else 'abstract class' if structure_kind == 'abstract' else structure_kind

		prompt = f"Describe the following {structure_kind} using the AnalyzeStructure tool.\n\n"
		structure_parameters = OrderedDict()
		structure_parameters["Project Name"] = self.project_name
		structure_parameters["Project Description"] = self.project_desc
		structure_parameters[f"{structure_kind.title()} Name"] = structure_name
		structure_parameters[f"{structure_kind.title()} Inhertis From"] = ancestors
		structure_parameters[f"Enclosed Variables/Fields"] = variables
		structure_parameters[f"Enclosed Functions/Methods"] = script_descriptions

		prompt = self.compose_prompt(prompt, structure_parameters)

		log_file.write(prompt)
		log_file.write('\n\n======\n\n')

		description = self.generate_json_description(client, model, prompt, "AnalyzeStructure")
		self.update_class_properties(graph, description, structure)

		jsonl_file.write(json.dumps({
			'data': {
				'id': structure.id,
				'labels': list(structure.labels),
				'properties': description
			}
		}))
		jsonl_file.write('\n')

	def process_component(self, graph: Graph, client: OpenAI, model: str, jsonl_file, log_file, component: Node,
						component_contents: dict, component_deps: dict):
		"""Process a single package and generate its description."""
  
		# if 'description' not in component.properties or not component.properties['description'] or component.properties['description'] == "(no description)":
		structure_descriptions = self.get_structure_descriptions(graph, component_contents)
		subcomponent_descriptions = self.get_component_descriptions(graph, component_deps[component.id])
		component_kind = component.properties.get('kind', "component")

		prompt = f"Describe the following {component_kind} using the AnalyzeComponent tool.\n\n"
		component_parameters = OrderedDict()
		component_parameters["Project Name"] = self.project_name
		component_parameters["Project Description"] = self.project_desc
		component_parameters["Component Type"] = component_kind
		component_parameters["Component Name"] = component.properties['qualifiedName']
		component_parameters["Enclosed Sub-components"] = subcomponent_descriptions
		component_parameters["Enclosed Classes"] = structure_descriptions
		component_parameters["Possible Architectural Layers"] = dict(self.layers)

		prompt = self.compose_prompt(prompt, component_parameters)

		log_file.write(prompt)
		log_file.write('\n\n======\n\n')

		description = self.generate_json_description(client, model, prompt, "AnalyzeComponent")
		self.update_package_properties(graph, description, component)

		layer_id = None
		if component.has_property("layer") and \
				component.property("layer") in [name for name, _ in self.layers]:
			layer_id = f"layer:{component.property('layer')}"
		layer_node = graph.find_node(label="Grouping", where=lambda node: node.id == layer_id)
		if layer_node:
			graph.add_edge(component.id, layer_node.id, "implements", weight=1)

		jsonl_file.write(json.dumps({
			'data': {
				'id': component.id,
				'labels': list(component.labels),
				'properties': description}}))
		jsonl_file.write('\n')

	def process_interactions(self, graph: Graph, client: OpenAI, model: str, c1: Node, c2: Node, path_groups: List[Edge], hierarchy, jsonl_file: TextIOWrapper, log_file: TextIOWrapper):
		c1_name = c1.properties["qualifiedName"]
		c2_name = c2.properties["qualifiedName"]
		c1_desc = c1.properties["description"]
		c2_desc = c2.properties["description"]
  
		c1_contents = hierarchy.get(c1.id, dict())
		c2_contents = hierarchy.get(c2.id, dict())
  
		c1_structure_info = "\n".join(f"        - `{graph.nodes[c_id].properties['simpleName']}`: {graph.nodes[c_id].properties['description']}" for c_id, _ in c1_contents.items())
		c2_structure_info = "\n".join(f"        - `{graph.nodes[c_id].properties['simpleName']}`: {graph.nodes[c_id].properties['description']}" for c_id, _ in c2_contents.items())
  
		def describe_path(path):
			src_structure = graph.nodes[path[1].source]
			src_method = graph.nodes[path[1].target]
			tgt_method = graph.nodes[path[-2].source]
			tgt_structure = graph.nodes[path[-2].target]
			return f"{src_method.properties['kind'].capitalize()} `{src_method.properties['simpleName']}` ({src_method.properties['description']}) of {src_structure.properties['kind']} `{src_structure.properties['qualifiedName']}` invokes {tgt_method.properties['kind']} `{tgt_method.properties['simpleName']}` ({tgt_method.properties['description']}) of {tgt_structure.properties['kind']} `{tgt_structure.properties['qualifiedName']}`."
  
		dep_info = f"    - Dependencies from `{c1_name}` to `{c2_name}`:\n" + "\n".join(f"        - {describe_path(path)}" for path in path_groups) if path_groups else ""
  
		prompt = templates.interaction_analysis.format(
			project_name=self.project_name,
			project_desc=self.project_desc,
			pkg1_name=c1_name,
			pkg2_name=c2_name,
			pkg1_desc=c1_desc,
			pkg2_desc=c2_desc,
			cls1_info=c1_structure_info,
			cls2_info=c2_structure_info,
			dep_info=dep_info
		)

		log_file.write(prompt)
		log_file.write('\n\n======\n\n')

		description = self.generate_text_description(client, model, prompt)
		pkg1_edge = Edge(source=c1.id, target=c2.id, label="dependsOn", description=description) if dep_info else None

		if pkg1_edge:
			if "dependsOn" not in graph.edges:
				graph.edges["dependsOn"] = []
			graph.edges["dependsOn"].append(pkg1_edge)
			jsonl_file.write(json.dumps(pkg1_edge.to_dict(), cls=CustomJSONEncoder))
			jsonl_file.write('\n')

	def generate_json_description(self, client: OpenAI, model: str, prompt: str = None, tool: str = None) -> dict:
		"""Generate a description using the OpenAI client."""
		try:
			if tool:
				print(prompt)
				response = client.chat.completions.create(
					model=model,
					messages=[
						{"role": "system", "content": "You are a software architecture analysis tool."},
						{"role": "user", "content": prompt}
					],
					tools=[templates.analyze_script_tool, templates.analyze_structure_tool, templates.analyze_component_tool],
					tool_choice={"name": tool},
					temperature=0,
					seed=42,
					timeout=float(self.config['llm'].get('timeout', 300))
				)
				print(response)
    
				tool_calls = response.choices[0].message.tool_calls
    
				if tool_calls:
					args_str = tool_calls[0].function.arguments
					description = json.loads(args_str)
				else:
					content = response.choices[0].message.content
					json_content = find_first_valid_json(content)
					if json_content:
						description = json.loads(json_content)
					else:
						description = dict()

			else:
				response = client.chat.completions.create(
					model=model,
					response_format={"type": "json_object"},
					messages=[{"role": "user", "content": prompt}],
					max_tokens=4096,
					temperature=0,
					seed=42,
					timeout=float(self.config['llm'].get('timeout', 300))
				)
    
				content = response.choices[0].message.content
				description = json.loads(content)
		except:
			description = {}

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
				temperature=0,
				seed=42,
				timeout=float(self.config['llm'].get('timeout', 300))
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
						for edge in data.find_edges(label='hasParameter')
						if edge.source == method.id
					]
				for param in value:
					if isinstance(param, dict):
						matching_params = [
							node
							for node in param_nodes
							if node.properties['simpleName'] == param.get('name')
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

	def get_structure_relations(self, data: Graph, cls_id: str) -> tuple:
		"""Retrieve class ancestors and fields."""
		ancestors = list({
			data.nodes[edge.target].property("qualifiedName")
			for edge in data.find_edges(label='specializes')
			if edge.source == cls_id
		})
		fields = {
			data.nodes[edge.target]
			for edge in data.find_edges(label='hasVariable')
			if edge.source == cls_id
		}
		fields = [
			' '.join(remove_java_comments(field.properties['sourceText']).split())
			for field in fields
		]
		return ancestors, fields

	def get_script_descriptions(self, data: Graph, cls_data: list) -> dict:
		"""Generate descriptions for methods."""
		return {
			data.nodes[met_id].properties['simpleName']: self.describe(data.nodes[met_id])
			for met_id in cls_data
		}

	def get_structure_descriptions(self, data: Graph, pkg_data: dict) -> list:
		"""Generate descriptions for classes."""
		return {
			f"{data.nodes[cls_id].properties['kind']} {data.nodes[cls_id].properties['qualifiedName']}": self.describe(data.nodes[cls_id])
			for cls_id, _ in pkg_data.items()
		}

	def get_component_descriptions(self, data: Graph, package_ids: list) -> list:
		"""Generate descriptions for packages."""
		return {
			data.nodes[pkg_id].properties['qualifiedName']: self.describe(data.nodes[pkg_id])
			for pkg_id in package_ids
		}

def find_first_valid_json(text: str) -> str:
    """
    Finds the first valid JSON substring in the given text using a stack-based approach.
    
    It scans the text from left to right, and when it encounters a '{', it tracks the balanced
    braces until a complete JSON object is formed. Once a candidate is found, it attempts to parse
    it with json.loads(). If parsing succeeds, that candidate is returned immediately.
    
    Args:
        text (str): The input string that may contain a JSON object.
    
    Returns:
        str: The first valid JSON substring found, or an empty string if none is found.
    """
    n = len(text)
    for i in range(n):
        if text[i] == '{':
            stack = 0
            for j in range(i, n):
                if text[j] == '{':
                    stack += 1
                elif text[j] == '}':
                    stack -= 1
                    if stack == 0:
                        candidate = text[i:j+1]
                        try:
                            json.loads(candidate)
                            return candidate
                        except json.JSONDecodeError:
                            # If this candidate isn't valid JSON, break and continue scanning.
                            break
    return ""

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
