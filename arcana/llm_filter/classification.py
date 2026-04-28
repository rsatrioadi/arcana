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


def stereocode_method_stereotypes():
	return OrderedDict([
		# Structural Accessors
		("get",           "Returns a data member directly."),
		("predicate",     "Returns a Boolean value that is not itself a data member."),
		("property",      "Returns information derived from or about data members (non-Boolean)."),
		("void-accessor", "Returns information about data members through method parameters (out/ref params) rather than the return value."),
		# Structural Mutators
		("set",              "Modifies a single data member."),
		("command",          "Performs a complex change to the object's state (e.g., modifies multiple data members); returns void."),
		("non-void-command", "Like command but also returns a value."),
		# Creational
		("constructor",      "Creates (or initialises) a new object instance."),
		("copy-constructor", "Creates a new object by copying an existing one."),
		("destructor",       "Destroys or cleans up an object."),
		("factory",          "Creates and returns an instance of another class."),
		# Collaborational
		("collaborator", "Works primarily with objects belonging to classes other than itself (passed as parameter, stored as local/data member, or returned)."),
		("controller",   "Changes only the state of an external object, not 'this'."),
		("wrapper",      "Does not change the object's state but delegates to at least one free function call."),
		# Degenerate
		("incidental", "Does not read or change the object's state and makes no calls to other class methods or free functions."),
		("stateless",  "Does not read or change the object's state but has at least one call to other class methods or free functions."),
		("empty",      "Has no statements at all."),
	])


def stereocode_class_stereotypes():
	return OrderedDict([
		("entity",          "Encapsulates both data and behaviour; keeper of the data model and/or business logic."),
		("minimal-entity",  "Special case of entity consisting only of get, set, and command methods."),
		("data-provider",   "Encapsulates data and consists mainly of accessors (get/property/predicate)."),
		("commander",       "Encapsulates behaviour and consists mainly of mutators (set/command)."),
		("boundary",        "Communicator with a large percentage of collaborational methods and a low percentage of controller methods; few factory methods."),
		("factory",         "Creator of objects; has mostly factory methods."),
		("controller",      "Provides functionality to control external objects; consists mostly of controller and factory methods."),
		("pure-controller", "Special case of controller consisting only of controller and factory methods."),
		("large-class",     "Contains a large number of methods combining multiple roles such as data-provider, commander, controller, and factory."),
		("lazy-class",      "Consists mostly of get, set, and degenerate methods; occurrence of other methods is low."),
		("degenerate",      "Consists mostly of degenerate methods that do not read or write to the object's state."),
		("data-class",      "Consists only of get and set methods."),
		("small-class",     "Consists of only one or two methods."),
		("empty",           "Has no methods."),
	])


def default_classification_schemes(layers_cfg=None, role_stereotypes_cfg=None, secdfd_enabled=False, stereocode_enabled=False):
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

	if stereocode_enabled:
		stereocode_method_scheme = ClassificationScheme(
			name="stereocodeMethod",
			dimension_id="Stereocode Method Stereotype",
			dimension_name="Stereocode Method Stereotype",
			dimension_kind="categorical-nominal",
			category_prefix="scm",
			category_kind="stereocode method stereotype",
			prompt_label="Possible Stereocode Method Stereotypes",
			response_key="stereocodeStereotype",
			response_reason_key="stereocodeStereotypeReason",
			options=stereocode_method_stereotypes(),
			undetermined_description="Stereocode method stereotype cannot be determined.",
			ordered=False,
			applies_to=("operation",),
			allow_multi_label=True,
		)
		stereocode_class_scheme = ClassificationScheme(
			name="stereocodeClass",
			dimension_id="Stereocode Class Stereotype",
			dimension_name="Stereocode Class Stereotype",
			dimension_kind="categorical-nominal",
			category_prefix="scc",
			category_kind="stereocode class stereotype",
			prompt_label="Possible Stereocode Class Stereotypes",
			response_key="stereocodeClassStereotype",
			response_reason_key="stereocodeClassStereotypeReason",
			options=stereocode_class_stereotypes(),
			undetermined_description="Stereocode class stereotype cannot be determined.",
			ordered=False,
			applies_to=("type",),
			allow_multi_label=False,
		)
		schemes[stereocode_method_scheme.name] = stereocode_method_scheme
		schemes[stereocode_class_scheme.name] = stereocode_class_scheme

	return schemes
