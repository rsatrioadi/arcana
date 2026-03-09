from dataclasses import dataclass
from collections import OrderedDict
from collections.abc import Iterable


def default_layers():
	return OrderedDict([
		('Presentation Layer', "Manages the user interface, defines UI elements and behavior, displays information, responds to user input, and updates views."),
		('Service Layer', "Controls the application flow, orchestrates domain operations, connects UI events with domain logic, and synchronizes domain changes with the UI."),
		('Domain Layer', "Handles business logic, represents domain data and behavior, and performs necessary computations for domain operations."),
		('Data Source Layer', "Interacts with databases, filesystems, hardware, messaging systems, or other data sources, performs CRUD operations, handles data conversion, and ensures data integrity."),
	])


def default_role_stereotypes():
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


@dataclass
class ClassificationScheme:
	name: str
	dimension_id: str
	dimension_name: str
	dimension_kind: str
	category_prefix: str
	category_kind: str
	prompt_label: str
	response_key: str
	response_reason_key: str
	options: OrderedDict
	undetermined_description: str
	ordered: bool = False
	applies_to: tuple = ()
	allow_multi_label: bool = False

	def options_with_undetermined(self) -> OrderedDict:
		result = OrderedDict(self.options or OrderedDict())
		result['Undetermined'] = self.undetermined_description
		return result

	def ordered_options(self) -> OrderedDict:
		result = self.options_with_undetermined()
		result.move_to_end('Undetermined', False)
		return result

	def category_id(self, category_name: str) -> str:
		return f"{self.category_prefix}:{category_name}"


def ordered_dict_from_mapping(mapping) -> OrderedDict:
	if not mapping:
		return OrderedDict()
	if isinstance(mapping, OrderedDict):
		return mapping
	if isinstance(mapping, dict):
		return OrderedDict(mapping)
	if isinstance(mapping, Iterable):
		return OrderedDict(mapping)
	return OrderedDict()


def default_secdfd_types():
	return OrderedDict([
		("External Entity", "Represents an external actor or system that interacts with the software."),
		("DataStore", "Represents persisted storage or a data access boundary."),
		("Process", "Represents non-trivial computation or orchestration logic."),
		("Asset", "Represents data objects with business or security value."),
		("Flow", "Represents data transfer across operations or boundaries."),
	])


def default_classification_schemes(layers_cfg=None, role_stereotypes_cfg=None, secdfd_enabled=False):
	layers = ordered_dict_from_mapping(layers_cfg) or default_layers()
	role_stereotypes = ordered_dict_from_mapping(role_stereotypes_cfg) or default_role_stereotypes()

	layer_scheme = ClassificationScheme(
		name="layer",
		dimension_id="Architectural Layer",
		dimension_name="Architectural Layer",
		dimension_kind="categorical-ordered",
		category_prefix="layer",
		category_kind="architectural layer",
		prompt_label="Possible Architectural Layers",
		response_key="layer",
		response_reason_key="layerReason",
		options=layers,
		undetermined_description="Architectural layer cannot be determined for this element.",
		ordered=True,
		applies_to=("operation", "type", "scope")
	)

	role_scheme = ClassificationScheme(
		name="roleStereotype",
		dimension_id="Role Stereotype",
		dimension_name="Role Stereotype",
		dimension_kind="categorical-nominal",
		category_prefix="rs",
		category_kind="role stereotype",
		prompt_label="Possible Role Stereotypes",
		response_key="roleStereotype",
		response_reason_key="roleStereotypeReason",
		options=role_stereotypes,
		undetermined_description="Role stereotype cannot be determined for this element.",
		ordered=False,
		applies_to=("type",)
	)
	schemes = OrderedDict([
		(layer_scheme.name, layer_scheme),
		(role_scheme.name, role_scheme),
	])

	if secdfd_enabled:
		secdfd_scheme = ClassificationScheme(
			name="secdfd",
			dimension_id="SecDFD Type",
			dimension_name="SecDFD Type",
			dimension_kind="categorical-nominal",
			category_prefix="secdfd",
			category_kind="secdfd type",
			prompt_label="Possible SecDFD Types",
			response_key="secdfdTypes",
			response_reason_key="secdfdEvidence",
			options=default_secdfd_types(),
			undetermined_description="SecDFD type cannot be determined for this element.",
			ordered=False,
			applies_to=("operation", "type", "variable"),
			allow_multi_label=True,
		)
		schemes[secdfd_scheme.name] = secdfd_scheme

	return schemes
