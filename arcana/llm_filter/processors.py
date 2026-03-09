from abc import ABC, abstractmethod
from collections import OrderedDict
from collections.abc import Iterable
import logging
import re

from tqdm.auto import tqdm

from arcana.checkpoint import writer
from arcana.filters import check_stop
from arcana.llm_filter.classification import ClassificationScheme
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

	def add_classification_options(self, parameters: OrderedDict, element_kind: str):
		for scheme in self.prompt.classification_schemes(element_kind):
			parameters[scheme.prompt_label] = scheme.options_with_undetermined()

	def apply_classifications(self, graph: Graph, element: Node, description: dict, element_kind: str):
		for scheme in self.prompt.classification_schemes(element_kind):
			self._apply_classification(graph, element, description, scheme)

	@staticmethod
	def _apply_classification(graph: Graph, element: Node, description: dict, scheme: ClassificationScheme):
		if scheme.allow_multi_label:
			classifications = description.get(scheme.response_key, None)
		else:
			classifications = description.pop(scheme.response_key, None)
		if not classifications:
			return

		if isinstance(classifications, str):
			classifications = [classifications]
		elif isinstance(classifications, (list, tuple, set)):
			classifications = list(classifications)
		else:
			classifications = []

		if not scheme.allow_multi_label and classifications:
			classifications = classifications[:1]
		elif scheme.allow_multi_label and classifications and "primarySecdfdType" not in description:
			description["primarySecdfdType"] = classifications[0]

		seen = set()
		for classification in classifications:
			if not classification or classification in seen:
				continue
			seen.add(classification)
			target = graph.find_node(label="Category", where=lambda n: n.id == scheme.category_id(classification))
			if target:
				impl_edge = graph.add_edge(
					element.id,
					target.id,
					"implements",
					weight=1,
					reason=description.get(scheme.response_reason_key),
				)
				if impl_edge:
					writer().write(impl_edge.to_dict())

class ScriptProcessor(Processor):
  
	def process_all(self, graph: Graph):
		sorted_method_ids, method_deps = Graph.toposorted_nodes(graph.find_edges(label='invokes'), graph.find_nodes('Operation'))
		counter = 0
		# logger.debug(sorted_method_ids)
		# logger.debug(method_deps)

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
			self.add_classification_options(op_parameters, "operation")

			prompt = self.prompt.compose(prompt, **op_parameters)

			logger.debug(prompt)

			description = self.client.generate_json(prompt, "AnalyzeScript")

			self.apply_classifications(graph, operation, description, "operation")

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
				param_nodes = [data.nodes[edge.source] for edge in data.find_edges(label='parameterizes') if
							   edge.target == method.id]
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
			enclosers = [n for n in clasz.sources('encloses') if n.has_label('Scope')]
			package: Node = enclosers[0] if enclosers else None
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
  
		prompt = f"Describe the following {typ_kind} using the AnalyzeStructure tool.\n\n"
		typ_parameters = OrderedDict()
		typ_parameters["Project Name"] = self.prompt.project_name
		typ_parameters["Project Description"] = self.prompt.project_desc
  
		if scope:
			scope_name = scope.properties['qualifiedName']
			scope_kind = scope.properties.get('kind', "scope")
			typ_parameters[f"{typ_kind.title()} to Analyze"] = f"`{typ_kind} {typ_name}` from the {scope_kind} `{scope_name}`."
		else:
			typ_parameters[f"{typ_kind.title()} to Analyze"] = f"`{typ_kind} {typ_name}`."
   
		typ_parameters[f"{typ_kind.title()} Inhertis From"] = {graph.nodes[node_id].properties[
																	  'qualifiedName']: f"{describe(graph.nodes[node_id], 'description', 'docComment')}"
																  for node_id in type_deps[type.id]}
		typ_parameters["Inherited By"] = [f"{t.properties['kind']} {t.properties['qualifiedName']}" for t in type.sources('specializes')]
		typ_parameters[f"Enclosed Variables/Fields"] = vars
		typ_parameters[f"Enclosed Functions/Methods"] = op_descriptions
		self.add_classification_options(typ_parameters, "type")

		prompt = self.prompt.compose(prompt, **typ_parameters)

		logger.debug(prompt)

		description = self.client.generate_json(prompt, "AnalyzeStructure")

		self.apply_classifications(graph, type, description, "type")

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
		self.add_classification_options(scp_parameters, "scope")

		prompt = self.prompt.compose(prompt, **scp_parameters)

		logger.debug(prompt)

		description = self.client.generate_json(prompt, "AnalyzeComponent")

		self.apply_classifications(graph, scope, description, "scope")

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


class VariableProcessor(Processor):
	def __init__(self, client, prompt_builder, secdfd_cfg=None):
		super().__init__(client, prompt_builder)
		cfg = secdfd_cfg or {}
		self.label_score_threshold = float(cfg.get("label_score_threshold", 0.60))
		self.process_min_out_invokes = int(cfg.get("process_min_out_invokes", 2))
		self.process_min_in_invokes = int(cfg.get("process_min_in_invokes", 2))
		self.asset_sensitive_term_hit_min = int(cfg.get("asset_sensitive_term_hit_min", 1))
		self.datastore_crud_hit_min = int(cfg.get("datastore_crud_hit_min", 1))
		self.external_entity_max_participation = int(cfg.get("external_entity_max_participation", 2))
		self.external_keywords = set("client rest entity user customer bank".split())
		self.datastore_keywords = set("db database dao repository storage cache data record table".split())
		self.asset_keywords = set("password secret policy user document card money balance account pin token key".split())
		self.flow_keywords = set("request response payload dto input output transfer amount source target".split())

	def process_all(self, graph: Graph):
		counter = 0
		signature_counts = self.build_signature_counts(graph)
		for var in tqdm(graph.find_nodes("Variable"), desc="Processing variables"):
			self.process_one(graph, var, signature_counts)
			check_stop()
			counter += 1
			if counter == 50:
				writer().flush()
				counter = 0

	def process_one(self, graph: Graph, var: Node, signature_counts: dict):
		description = self.infer_secdfd(graph, var, signature_counts)
		if not description:
			return
		self.apply_classifications(graph, var, description, "variable")
		for k, v in description.items():
			if not k.endswith("Reason"):
				graph.nodes[var.id].properties[lower_first(k)] = v
		writer().write({"data": {"id": var.id, "labels": list(var.labels), "properties": description}})

	def infer_secdfd(self, graph: Graph, var: Node, signature_counts: dict) -> dict:
		var_name = str(var.properties.get("simpleName", "")).strip()
		name_tokens = self.tokenize(var_name)
		signature = self.variable_signature(var)
		participation = len(var.targets("parameterizes")) + len(var.sources("encapsulates"))
		owners = [n for n in var.sources("encapsulates") if n.has_label("Type")]
		ops = [n for n in var.targets("parameterizes") if n.has_label("Operation")]
		scores = {
			"External Entity": 0.0,
			"DataStore": 0.0,
			"Process": 0.0,
			"Asset": 0.0,
			"Flow": 0.0,
		}
		evidence = []

		external_hits = self.keyword_hits(name_tokens, self.external_keywords)
		if external_hits:
			scores["External Entity"] += 0.7
			evidence.append(f"external_keywords={','.join(sorted(external_hits))}")
		if participation <= self.external_entity_max_participation and (ops or owners):
			scores["External Entity"] += 0.2
			evidence.append("low_participation")

		datastore_hits = self.keyword_hits(name_tokens, self.datastore_keywords)
		if len(datastore_hits) >= self.datastore_crud_hit_min:
			scores["DataStore"] += 0.7
			evidence.append(f"datastore_keywords={','.join(sorted(datastore_hits))}")
		if any(any(v in self.tokenize(op.properties.get("simpleName", "")) for v in {"save", "find", "delete", "create", "read", "update"}) for op in ops):
			scores["DataStore"] += 0.2
			evidence.append("crud_related_operation")

		asset_hits = self.keyword_hits(name_tokens, self.asset_keywords)
		if len(asset_hits) >= self.asset_sensitive_term_hit_min:
			scores["Asset"] += 0.8
			evidence.append(f"asset_keywords={','.join(sorted(asset_hits))}")
		if owners and not ops:
			scores["Asset"] += 0.1
			evidence.append("field_like_variable")

		flow_hits = self.keyword_hits(name_tokens, self.flow_keywords)
		if flow_hits:
			scores["Flow"] += 0.4
			evidence.append(f"flow_keywords={','.join(sorted(flow_hits))}")
		if ops:
			scores["Flow"] += 0.2
			evidence.append("parameterizes_operation")
		if signature_counts.get(signature, 0) > 1:
			scores["Flow"] += 0.3
			evidence.append("shared_signature")

		# Variables are not typically processes, keep score near-zero unless explicitly verb-named.
		if self.looks_like_verb(var_name):
			scores["Process"] += 0.2
			evidence.append("verb_like_name")
		if any(len(op.targets("invokes")) >= self.process_min_out_invokes or len(op.sources("invokes")) >= self.process_min_in_invokes for op in ops):
			scores["Process"] += 0.3
			evidence.append("connected_to_high_interaction_operation")

		selected = [label for label, score in sorted(scores.items(), key=lambda x: x[1], reverse=True) if score >= self.label_score_threshold][:3]
		if not selected:
			selected = ["Undetermined"]
			primary = "Undetermined"
		else:
			primary = selected[0]

		return {
			"secdfdTypes": selected,
			"primarySecdfdType": primary,
			"secdfdConfidence": {k: round(v, 3) for k, v in scores.items() if v > 0},
			"secdfdEvidence": "; ".join(evidence) if evidence else "No strong SecDFD evidence found.",
		}

	@staticmethod
	def keyword_hits(tokens: set, keywords: set) -> set:
		return {t for t in tokens if t in keywords}

	@staticmethod
	def tokenize(text: str) -> set:
		text = re.sub(r"([a-z0-9])([A-Z])", r"\1 \2", text or "")
		text = text.replace("_", " ").replace("-", " ").lower()
		return {t for t in re.findall(r"[a-z0-9]+", text)}

	@staticmethod
	def looks_like_verb(name: str) -> bool:
		l = (name or "").lower()
		return l.startswith(("get", "set", "create", "save", "find", "load", "send", "fetch", "verify"))

	@staticmethod
	def variable_signature(var: Node):
		name = str(var.properties.get("simpleName", "")).strip().lower()
		types = tuple(sorted(t.id for t in var.targets("type")))
		return name, types

	def build_signature_counts(self, graph: Graph):
		counts = {}
		for var in graph.find_nodes("Variable"):
			sig = self.variable_signature(var)
			counts[sig] = counts.get(sig, 0) + 1
		return counts
