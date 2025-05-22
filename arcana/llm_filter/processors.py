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

		for met_id in tqdm(sorted_method_ids, desc='Processing methods'):
			method: Node = graph.nodes[met_id]
			clasz: Node = [n for n in method.sources('encapsulates') if n.has_label('Type')][0]
			self.process_one(graph, method, clasz, method_deps)

			check_stop()

			counter += 1
			if counter == 10:
				writer().flush()
				counter %= 10

	def process_one(self, graph: Graph, operation: Node, type: Node, operation_deps):
		if 'description' not in operation.properties or not operation.properties['description'] or operation.properties[
			'description'] == "(no description)":
			op_name = operation.properties['simpleName']
			op_src = remove_java_comments(operation.properties['sourceText'])
			op_kind = operation.properties.get('kind', 'function')

			typ_name = type.properties['qualifiedName']
			typ_kind = type.properties['kind']
			typ_kind = 'enum' if typ_kind == 'enumeration' else 'abstract class' if typ_kind == 'abstract' else typ_kind

			prompt = f"Describe the following {op_kind} by using the AnalyzeScript tool.\n\n"
			op_parameters = OrderedDict()
			op_parameters["Project Name"] = self.prompt.project_name
			op_parameters["Project Description"] = self.prompt.project_desc
			op_parameters[f"{op_kind.title()} to Analyze"] = f"`{op_name}` from the {typ_kind} `{typ_name}`."
			op_parameters[f"{op_kind.title()} Source Code"] = op_src
			op_parameters["Outgoing Dependencies (Invokes)"] = {graph.nodes[node_id].properties[
																	  'qualifiedName']: f"{describe(graph.nodes[node_id], 'description', 'returns', 'howToUse', 'docComment')}"
																  for node_id in operation_deps[operation.id]}
			op_parameters["Incoming Dependencies (Invoked By)"] = [m.properties['qualifiedName'] for m in operation.sources('invokes')]
			op_parameters["Possible Architectural Layers"] = dict(self.prompt.layers)

			prompt = self.prompt.compose(prompt, **op_parameters)

			logger.debug(prompt)

			description = self.client.generate_json(prompt, "AnalyzeScript")
	
			layer = description.pop('layer', None)
			if layer:
				node_id = f"layer:{layer}"
				target = graph.find_node(label="Category", where=lambda n: n.id == node_id)
				if target:
					impl_edge = graph.add_edge(operation.id, target.id, "implements", weight=1, reason=description.get('layerReason'))
					writer().write(impl_edge.to_dict())

			self.update_method_properties(graph, description, operation)

			writer().write({'data': {'id': operation.id, 'labels': operation.labels, 'properties': description}})

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

		for cls_id in tqdm(sorted_class_ids, desc='Processing classes'):
			clasz: Node = graph.nodes[cls_id]
			package: Node = [n for n in clasz.sources('encloses') if n.has_label('Scope')][0]
			self.process_one(graph, clasz, package, class_deps)

			check_stop()

			counter += 1
			if counter == 10:
				writer().flush()
				counter %= 10
    
	def process_one(self, graph: Graph, type: Node, scope: Node, type_deps):
		vars = StructureProcessor.get_type_relations(graph, type.id)
		op_descriptions = { method.properties['qualifiedName']: describe(method) for method in type.targets('encapsulates') if method.has_label('Operation') }

		typ_name = type.properties['qualifiedName']
		typ_kind = type.properties.get('kind', "type")
		typ_kind = 'enum' if typ_kind == 'enumeration' else 'abstract class' if typ_kind == 'abstract' else typ_kind
  
		scope_name = scope.properties['qualifiedName']
		scope_kind = scope.properties.get('kind', "scope")

		prompt = f"Describe the following {typ_kind} using the AnalyzeStructure tool.\n\n"
		typ_parameters = OrderedDict()
		typ_parameters["Project Name"] = self.prompt.project_name
		typ_parameters["Project Description"] = self.prompt.project_desc
		typ_parameters[f"{typ_kind.title()} to Analyze"] = f"`{typ_kind} {typ_name}` from the {scope_kind} `{scope_name}`."
		typ_parameters[f"{typ_kind.title()} Inhertis From"] = {graph.nodes[node_id].properties[
																	  'qualifiedName']: f"{describe(graph.nodes[node_id], 'description', 'docComment')}"
																  for node_id in type_deps[type.id]}
		typ_parameters[f"Enclosed Variables/Fields"] = vars
		typ_parameters[f"Enclosed Functions/Methods"] = op_descriptions
		typ_parameters['Possible Role Stereotypes'] = dict(self.prompt.role_stereotypes)
		typ_parameters["Possible Architectural Layers"] = dict(self.prompt.layers)

		prompt = self.prompt.compose(prompt, **typ_parameters)

		logger.debug(prompt)

		description = self.client.generate_json(prompt, "AnalyzeStructure")
  
		rs = description.pop('roleStereotype', None)
		if rs:
			node_id = f"rs:{rs}"
			target = graph.find_node(label="Category", where=lambda n: n.id == node_id)
			if target:
				impl_edge = graph.add_edge(type.id, target.id, "implements", weight=1, reason=description.get('roleStereotypeReason'))
				writer().write(impl_edge.to_dict())
     
		layer = description.pop('layer', None)
		if layer:
			node_id = f"layer:{layer}"
			target = graph.find_node(label="Category", where=lambda n: n.id == node_id)
			if target:
				impl_edge = graph.add_edge(type.id, target.id, "implements", weight=1, reason=description.get('layerReason'))
				writer().write(impl_edge.to_dict())

		for k, v in description.items():
			if not k.endswith('Reason'):
				graph.nodes[type.id].properties[lower_first(k)] = v

		writer().write({'data': {'id': type.id, 'labels': list(type.labels), 'properties': description}})

	@staticmethod
	def get_type_relations(data: Graph, cls_id: str) -> tuple:
		"""Retrieve class fields."""
		fields = {data.nodes[edge.target] for edge in data.find_edges(label='encapsulates') if edge.source == cls_id}
		fields = [' '.join(remove_java_comments(field.properties['sourceText']).split()) for field in fields if field.has_label('Variable')]
		return fields


class ComponentProcessor(Processor):

	def process_all(self, graph: Graph):
		sorted_pkg_ids, pkg_deps = graph.toposorted_nodes(
			graph.find_edges(label='encloses', where_source=lambda node: node.has_label('Scope') and not node.has_label('Type'),
							 where_target=lambda node: node.has_label('Scope') and not node.has_label('Type')), graph.find_nodes('Scope', where=lambda node: not node.has_label('Type')))
		counter = 0

		for pkg_id in tqdm(sorted_pkg_ids, desc='Processing packages'):
			package: Node = graph.nodes[pkg_id]
			self.process_one(graph, package, pkg_deps)

			check_stop()

			counter += 1
			if counter == 10:
				writer().flush()
				counter %= 10
    
	def process_one(self, graph: Graph, scope: Node, scope_deps):
		typ_descriptions = { f"{type.properties['kind']} {type.properties['qualifiedName']}": describe(type) for type in scope.targets('encloses') if type.has_label('Type') }
		subscp_descriptions = {graph.nodes[node_id].properties['qualifiedName']: f"{describe(graph.nodes[node_id], 'description', 'returns', 'howToUse', 'docComment')}"
																  for node_id in scope_deps[scope.id]}
		scp_kind = scope.properties.get('kind', "component")

		prompt = f"Describe the following {scp_kind} using the AnalyzeComponent tool.\n\n"
		scp_parameters = OrderedDict()
		scp_parameters["Project Name"] = self.prompt.project_name
		scp_parameters["Project Description"] = self.prompt.project_desc
		scp_parameters[f"{scp_kind.title()} to Analyze"] = scope.properties['qualifiedName']
		scp_parameters[f"Enclosed Sub-{scp_kind}s"] = subscp_descriptions
		scp_parameters["Enclosed Classes"] = typ_descriptions
		scp_parameters["Possible Architectural Layers"] = dict(self.prompt.layers)

		prompt = self.prompt.compose(prompt, **scp_parameters)

		logger.debug(prompt)

		description = self.client.generate_json(prompt, "AnalyzeComponent")

		layer = description.pop('layer', None)
		if layer:
			node_id = f"layer:{layer}"
			target = graph.find_node(label="Category", where=lambda n: n.id == node_id)
			if target:
				impl_edge = graph.add_edge(scope.id, target.id, "implements", weight=1, reason=description.get('layerReason'))
				writer().write(impl_edge.to_dict())

		ComponentProcessor.update_package_properties(graph, description, scope)

		writer().write({'data': {'id': scope.id, 'labels': list(scope.labels), 'properties': description}})

	@staticmethod
	def update_package_properties(data: Graph, description: dict, package: Node):
		"""Update package properties with the generated description."""
		for key in description:
			if not key.endswith('Reason'):
				data.nodes[package.id].properties[lower_first(key)] = description[key]

class InteractionProcessor(Processor):

	def process_all(self, graph):
		# compute and describe interactions between packages
		pass
