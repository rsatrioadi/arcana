from abc import ABC, abstractmethod
from collections import OrderedDict
from collections.abc import Iterable
import logging

from tqdm.auto import tqdm

from arcana.checkpoint import writer
from arcana.filters import check_stop
from arcana.llm_filter.client import LLMClient
from arcana.llm_filter.prompt import PromptBuilder, describe
from arcana.utils import lower_first, remove_java_comments
from arcanalib.graph import Graph, Node

logger = logging.getLogger(__name__)

class Processor(ABC):
	def __init__(self, client, prompt_builder):
		self.client: LLMClient = client
		self.prompt: PromptBuilder = prompt_builder
  
	@abstractmethod
	def process_all(self, graph):
		raise NotImplementedError

class ScriptProcessor(Processor):
  
	def process_all(self, graph: Graph):
		sorted_method_ids, method_deps = Graph.toposorted_nodes(graph.find_edges(label='invokes'), graph.find_nodes('Operation'))
		counter = 0
		logger.debug(sorted_method_ids)
		logger.debug(method_deps)

		for met_id in tqdm(sorted_method_ids, desc='Processing methods', position=0, leave=False):
			method: Node = graph.nodes[met_id]
			clasz: Node = [n for n in method.sources('encapsulates') if n.has_label('Type')][0]
			self.process_one(graph, method, clasz, method_deps)

			check_stop()

			counter += 1
			if counter == 10:
				writer().flush()
				counter %= 10

	def process_one(self, graph: Graph, method: Node, clasz: Node, method_deps):
		if 'description' not in method.properties or not method.properties['description'] or method.properties[
			'description'] == "(no description)":
			script_name = method.properties['simpleName']
			script_src = remove_java_comments(method.properties['sourceText'])
			script_kind = method.properties.get('kind', 'function')

			structure_name = clasz.properties['qualifiedName']
			structure_kind = clasz.properties['kind']
			structure_kind = 'enum' if structure_kind == 'enumeration' else 'abstract class' if structure_kind == 'abstract' else structure_kind

			prompt = f"Describe the following {script_kind} by using the AnalyzeScript tool.\n\n"
			script_parameters = OrderedDict()
			script_parameters["Project Name"] = self.prompt.project_name
			script_parameters["Project Description"] = self.prompt.project_desc
			script_parameters[f"{script_kind.title()} Declaration"] = f"The {script_kind} {script_name} is declared within the {structure_kind} {structure_name}."
			script_parameters[f"{script_kind.title()} Source Code"] = script_src
			script_parameters["Outgoing Dependencies (Invokes)"] = {graph.nodes[node_id].properties[
																	  'qualifiedName']: f"{describe(graph.nodes[node_id], 'description', 'returns', 'howToUse', 'docComment')}"
																  for node_id in method_deps[method.id]}
			script_parameters["Incoming Dependencies (Invoked By)"] = [m.properties['qualifiedName'] for m in method.sources('invokes')]
			script_parameters["Possible Architectural Layers"] = dict(self.prompt.layers)

			prompt = self.prompt.compose(prompt, **script_parameters)

			logger.debug(prompt)

			description = self.client.generate_json(prompt, "AnalyzeScript")
	
			layer = description.pop('layer', None)
			if layer:
				node_id = f"layer:{layer}"
				target = graph.find_node(label="Category", where=lambda n: n.id == node_id)
				if target:
					impl_edge = graph.add_edge(clasz.id, target.id, "implements", weight=1, reason=description.get('layerReason'))
					writer().write(impl_edge.to_dict())

			self.update_method_properties(graph, description, method)

			writer().write({'data': {'id': method.id, 'labels': method.labels, 'properties': description}})

	@staticmethod
	def update_method_properties(data: Graph, description: dict, method: Node):
		"""Update method properties with the generated description."""

		for key, value in description.items():
			if key.endswith('Reason'):
				continue
			key_lower = lower_first(key)
			if key_lower == 'parameters' and isinstance(value, Iterable):
				param_nodes = [data.nodes[edge.target] for edge in data.find_edges(label='hasParameter') if
							   edge.source == method.id]
				for param in value:
					if isinstance(param, dict):
						matching_params = [node for node in param_nodes if
										   node.properties['simpleName'] == param.get('name')]
						if matching_params:
							param_node_id = matching_params[0].id
							if param_node_id in data.nodes:
								data.nodes[param_node_id].properties['description'] = param.get('description')
			# elif key_lower == 'returns':
			# 	method.properties['returns'] = value.get('description', None) if value and hasattr(value, 'get') else None
			else:
				data.nodes[method.id].properties[key_lower] = value


class StructureProcessor(Processor):

	def process_all(self, graph: Graph):
		sorted_class_ids, class_deps = Graph.toposorted_nodes(graph.find_edges(label='specializes'), graph.find_nodes('Type'))
		counter = 0

		for cls_id in tqdm(sorted_class_ids, desc='Processing classes', position=1, leave=False):
			clasz: Node = graph.nodes[cls_id]
			package: Node = [n for n in clasz.sources('encloses') if n.has_label('Scope')][0]
			self.process_one(graph, clasz, package, class_deps)

			check_stop()

			counter += 1
			if counter == 10:
				writer().flush()
				counter %= 10
    
	def process_one(self, graph: Graph, clasz: Node, package: Node, class_deps):
		_, variables = StructureProcessor.get_structure_relations(graph, clasz.id)
		script_descriptions = { method.properties['qualifiedName']: describe(method) for method in clasz.targets('encapsulates') if method.has_label('Operation') }

		structure_name = clasz.properties['qualifiedName']
		structure_kind = clasz.properties['kind']
		structure_kind = 'enum' if structure_kind == 'enumeration' else 'abstract class' if structure_kind == 'abstract' else structure_kind

		prompt = f"Describe the following {structure_kind} using the AnalyzeStructure tool.\n\n"
		structure_parameters = OrderedDict()
		structure_parameters["Project Name"] = self.prompt.project_name
		structure_parameters["Project Description"] = self.prompt.project_desc
		structure_parameters[f"{structure_kind.title()} Name"] = structure_name
		structure_parameters[f"{structure_kind.title()} Inhertis From"] = {graph.nodes[node_id].properties[
																	  'qualifiedName']: f"{describe(graph.nodes[node_id], 'description', 'docComment')}"
																  for node_id in class_deps[clasz.id]}
		structure_parameters[f"Enclosed Variables/Fields"] = variables
		structure_parameters[f"Enclosed Functions/Methods"] = script_descriptions
		structure_parameters['Possible Role Stereotypes'] = dict(self.prompt.role_stereotypes)

		prompt = self.prompt.compose(prompt, **structure_parameters)

		logger.debug(prompt)

		description = self.client.generate_json(prompt, "AnalyzeStructure")
  
		st = description.pop('roleStereotype', None)
		if st:
			node_id = f"rs:{st}"
			target = graph.find_node(label="Category", where=lambda n: n.id == node_id)
			if target:
				impl_edge = graph.add_edge(clasz.id, target.id, "implements", weight=1, reason=description.get('roleStereotypeReason'))
				writer().write(impl_edge.to_dict())
     
		for k, v in description.items():
			if not k.endswith('Reason'):
				graph.nodes[clasz.id].properties[lower_first(k)] = v

		writer().write({'data': {'id': clasz.id, 'labels': list(clasz.labels), 'properties': description}})

	@staticmethod
	def get_structure_relations(data: Graph, cls_id: str) -> tuple:
		"""Retrieve class ancestors and fields."""
		ancestors = list(
			{data.nodes[edge.target] for edge in data.find_edges(label='specializes') if
			 edge.source == cls_id})
		fields = {data.nodes[edge.target] for edge in data.find_edges(label='encapsulates') if edge.source == cls_id}
		fields = [' '.join(remove_java_comments(field.properties['sourceText']).split()) for field in fields if field.has_label('Variable')]
		return ancestors, fields


class ComponentProcessor(Processor):

	def process_all(self, graph):
		# iterate and describe each package
		pass

class InteractionProcessor(Processor):

	def process_all(self, graph):
		# compute and describe interactions between packages
		pass
