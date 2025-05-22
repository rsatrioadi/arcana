import time
from collections import OrderedDict
from itertools import combinations
from typing import Any, Dict, List, TextIO

from tqdm.auto import tqdm

from arcana import templates
from arcana.filters import check_stop, layers_to_ordereddict
from arcana.graph_utils import (build_hierarchy, build_triplets, describe_path,
								group_paths_by_endpoints)
from arcana.llm_filter.client import LLMClient
from arcana.llm_filter.processors import ComponentProcessor, InteractionProcessor, ScriptProcessor, StructureProcessor
from arcana.llm_filter.prompt import PromptBuilder
from arcana.utils import (lower_first, remove_java_comments, write_jsonl)
from arcanalib.graph import Edge, Graph, Node
from arcanalib.pipefilter import Filter

def default_layers():
	return OrderedDict([
		('Presentation Layer', "Manages the user interface, defines UI elements and behavior, displays information, responds to user input, and updates views."),
		('Service Layer', "Controls the application flow, orchestrates domain operations, connects UI events with domain logic, and synchronizes domain changes with the UI."),
		('Domain Layer', "Handles business logic, represents domain data and behavior, and performs necessary computations for domain operations."),
		('Data Source Layer', "Interacts with databases, filesystems, hardware, messaging systems, or other data sources, performs CRUD operations, handles data conversion, and ensures data integrity."),
	])

def default_role_stereotypes():
	# **Information Holder** is responsible for knowing facts and providing information to other objects. POJOs, Java Beans, and enumerations are usually information holders. \
	# **Service Provider** is responsible for handling requests and performing specific services. It usually implements a specific interface with a small number of methods. Concrete strategies are service providers. \
	# **Structurer** is responsible for managing relationships and constraints among related things. It is usually a collection or mapping of some sort, i.e., a subclass of a List, Set, Map, etc. \
	# **Controller** is responsible for making decisions, directing the work of others, and handling important events. It directs the flow of the application or business process. \
	# **Coordinator** is responsible for managing the actions of a group of workers and facilitating communication and work of other objects. It delegates requests to other objects. Very abstract classes and interfaces might be coordinators as they delegate the work to subclasses. \
	# **User Interfacer** is responsible for transmitting user requests for action or display/render information that can be updated. It handles interactions with users. \
	# **External Interfacer** is responsible for loading and storing information from/to external services, including database systems, web services, filesystems, hardware, etc. \
	# **Internal Interfacer** is responsible for interfacing between two subsystems. It may bundle together information of requests from a group of objects to be sent to another object. Abstract adapters, bridges, facades, and proxies are internal interfacers."
	return OrderedDict([
        ("Information Holder",    "Knows facts and provides information (POJOs, beans, enums)."),
        ("Service Provider",      "Handles requests, performs services; implements a specific interface with a small number of methods (strategies, handlers)."),
        ("Structurer",            "Manages relationships among things (collections, maps)."),
        ("Controller",            "Makes decisions, directs flow of the program."),
        ("Coordinator",           "Delegates work across workers."),
        ("User Interfacer",       "Handles user input/output."),
        ("External Interfacer",   "Loads/stores from external services."),
        ("Internal Interfacer",   "Bridges subsystems (adapters, bridges, facades, proxies)."),
    ])
  
class LLMFilter(Filter):
	def __init__(self, config: Dict[str, Dict[str, Any]]):
		super().__init__(config)
		self.client = LLMClient(config['llm'], config['project'])

		layer_cfg = config.get('layers')
		self.layers = layers_to_ordereddict(layer_cfg) if layer_cfg else default_layers()

		stereo_cfg = config.get('stereotypes')
		self.role_stereotypes = OrderedDict(stereo_cfg) if stereo_cfg else default_role_stereotypes()

		self.prompt_builder = PromptBuilder(config['project'], self.layers, self.role_stereotypes)
		self.script_processor = ScriptProcessor(self.client, self.prompt_builder)
		self.structure_processor = StructureProcessor(self.client, self.prompt_builder)
		self.component_processor = ComponentProcessor(self.client, self.prompt_builder)
		self.interaction_processor = InteractionProcessor(self.client, self.prompt_builder)

	def process(self, graph):
		# 1. initialize layers and write baseline nodes/edges
		self.prompt_builder.initialize_layers(graph)

		# 2. process methods
		self.script_processor.process_all(graph)

		# 3. process classes
		self.structure_processor.process_all(graph)

		# 4. process packages
		self.component_processor.process_all(graph)

		# 5. process interactions
		self.interaction_processor.process_all(graph)

		return graph

	def process_hierarchy(self, graph: Graph, jsonl_file, log_file):
		"""Process each package, class, and method in the hierarchy."""

		st_contains_st = graph.find_edges(label='contains', source_label='Structure', target_label='Structure')
		ct_contains_st = graph.find_edges(label='contains', target_label='Structure', where_source=lambda
			node: 'Container' in node.labels and 'Structure' not in node.labels)
		new_ct_sources = {edge.target: graph.find_source(graph.find_edges(label='contains'), graph.nodes[edge.target],
														 lambda node: 'Structure' not in node.labels,
														 graph.nodes[edge.source]).id for edge in st_contains_st}
		ct_contains_st.extend(
			[Edge(source=source, target=target, label='contains') for target, source in new_ct_sources.items()])

		trips = build_triplets(ct_contains_st, graph.find_edges(label='hasScript'))
		hierarchy = build_hierarchy(trips)
		sorted_pkg_ids, pkg_deps = graph.toposorted_nodes(
			graph.find_edges(label='contains', where_source=lambda node: 'Structure' not in node.labels,
							 where_target=lambda node: 'Structure' not in node.labels))

		paths = graph.find_paths("contains", "hasScript", "invokes", "-hasScript", "-contains")
		path_groups = group_paths_by_endpoints(paths)

		pkg_pairs = list(combinations(sorted_pkg_ids, 2))
		for pkg2_id, pkg1_id in tqdm(pkg_pairs, desc='Processing package interactions', position=0, leave=False):

			check_stop()

			pkg1 = graph.nodes[pkg1_id]
			pkg2 = graph.nodes[pkg2_id]
			if ('Structure' not in pkg1.labels) and ('Structure' not in pkg2.labels):
				if path_groups[(pkg1_id, pkg2_id)]:
					self.process_interactions(graph, pkg1, pkg2, path_groups[(pkg1_id, pkg2_id)], hierarchy, jsonl_file,
											  log_file)
				if path_groups[(pkg2_id, pkg1_id)]:
					self.process_interactions(graph, pkg2, pkg1, path_groups[(pkg2_id, pkg1_id)], hierarchy, jsonl_file,
											  log_file)

	def process_interactions(self, graph: Graph, c1: Node, c2: Node, path_groups: List[List[Edge]], hierarchy,
							 jsonl_file: TextIO, log_file: TextIO):
		c1_name = c1.properties["qualifiedName"]
		c2_name = c2.properties["qualifiedName"]
		c1_desc = c1.properties["description"]
		c2_desc = c2.properties["description"]

		c1_contents = hierarchy.get(c1.id, dict())
		c2_contents = hierarchy.get(c2.id, dict())

		c1_structure_info = "\n".join(
			f"        - `{graph.nodes[c_id].properties['simpleName']}`: {graph.nodes[c_id].properties['description']}"
			for c_id, _ in c1_contents.items())
		c2_structure_info = "\n".join(
			f"        - `{graph.nodes[c_id].properties['simpleName']}`: {graph.nodes[c_id].properties['description']}"
			for c_id, _ in c2_contents.items())

		dep_info = f"    - Dependencies from `{c1_name}` to `{c2_name}`:\n" + "\n".join(
			f"        - {describe_path(graph, path)}" for path in path_groups) if path_groups else ""

		prompt = templates.interaction_analysis.format(project_name=self.project_name, project_desc=self.project_desc,
													   pkg1_name=c1_name, pkg2_name=c2_name, pkg1_desc=c1_desc,
													   pkg2_desc=c2_desc, cls1_info=c1_structure_info,
													   cls2_info=c2_structure_info, dep_info=dep_info)

		log_file.write(prompt)
		log_file.write('\n\n======\n\n')

		description = generate_text(prompt)
		pkg1_edge = Edge(source=c1.id, target=c2.id, label="dependsOn", description=description) if dep_info else None

		if pkg1_edge:
			if "dependsOn" not in graph.edges:
				graph.edges["dependsOn"] = []
			graph.edges["dependsOn"].append(pkg1_edge)

			write_jsonl(jsonl_file, pkg1_edge.to_dict())

	@staticmethod
	def update_package_properties(data: Graph, description: dict, package: Node):
		"""Update package properties with the generated description."""
		for key in description:
			if not key.endswith('Reason'):
				data.nodes[package.id].properties[lower_first(key)] = description[key]

	def get_script_descriptions(self, data: Graph, cls_data: list) -> dict[str,str]:
		"""Generate descriptions for methods."""
		return {data.nodes[met_id].properties['simpleName']: self.describe(data.nodes[met_id]) for met_id in cls_data}

	def get_structure_descriptions(self, data: Graph, pkg_data: dict) -> dict[str,str]:
		"""Generate descriptions for classes."""
		return {
			f"{data.nodes[cls_id].properties['kind']} {data.nodes[cls_id].properties['qualifiedName']}": self.describe(
				data.nodes[cls_id]) for cls_id, _ in pkg_data.items()}

	def get_component_descriptions(self, data: Graph, package_ids: list) -> dict[str,str]:
		"""Generate descriptions for packages."""
		return {data.nodes[pkg_id].properties['qualifiedName']: self.describe(data.nodes[pkg_id]) for pkg_id in
				package_ids}