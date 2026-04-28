from abc import ABC, abstractmethod
from collections import OrderedDict
from collections.abc import Iterable
from concurrent.futures import Future, ThreadPoolExecutor, wait as futures_wait
import logging
import re
import threading

from tqdm.auto import tqdm

from arcana.checkpoint import writer
from arcana.filters import check_stop
from arcana.llm_filter.classification import ClassificationScheme
from arcana.llm_filter.client import LLMClient
from arcana.llm_filter.prompt import PromptBuilder, describe
from arcana.utils import lower_first, remove_java_comments
from arcanalib.graph import Graph, Node

logger = logging.getLogger(__name__)


# ---------------------------------------------------------------------------
# Futures-based DAG executor
# ---------------------------------------------------------------------------

class NodeExecutor:
    """Executes graph nodes concurrently while honouring dependency ordering.

    Each node is submitted once. Before running its own processing function a
    worker thread waits for the futures of all direct dependencies to finish.
    This is equivalent to a topological sort but without a global pre-pass and
    with finer-grained parallelism: a node starts as soon as *its own* deps are
    ready rather than waiting for an entire topo-level to drain.

    Starvation note: if max_workers < longest dependency chain length every
    thread could block and make no progress.  Default of 8 is safe for typical
    Java inheritance depths.  Users can raise it in config if needed.
    """

    def __init__(self, max_workers: int = 8):
        self._pool = ThreadPoolExecutor(max_workers=max_workers)
        self._futures: dict[str, Future] = {}
        self._lock = threading.Lock()
        self._completed = 0
        self._completed_lock = threading.Lock()

    def submit(self, node_id: str, dep_ids: list[str], fn) -> Future:
        with self._lock:
            if node_id in self._futures:
                return self._futures[node_id]
            # Snapshot dep futures while holding the lock so they cannot
            # disappear between the check and the submit.
            dep_futures = [self._futures[d] for d in dep_ids if d in self._futures]
            f = self._pool.submit(self._run, dep_futures, fn, node_id)
            self._futures[node_id] = f
            return f

    def wait_all(self):
        with self._lock:
            all_futures = list(self._futures.values())
        futures_wait(all_futures)

    def shutdown(self):
        self._pool.shutdown(wait=True)

    def _run(self, dep_futures: list[Future], fn, node_id: str):
        for df in dep_futures:
            df.result()  # block until dependency is processed
        fn(node_id)
        with self._completed_lock:
            self._completed += 1

    @property
    def completed(self) -> int:
        with self._completed_lock:
            return self._completed


# ---------------------------------------------------------------------------
# Base processor
# ---------------------------------------------------------------------------

class Processor(ABC):
    def __init__(self, client: LLMClient, prompt_builder: PromptBuilder, max_workers: int = 8):
        self.client = client
        self.prompt = prompt_builder
        self.max_workers = max_workers

    @abstractmethod
    def process_all(self, graph: Graph):
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


# ---------------------------------------------------------------------------
# Helper: same-name method family (overloads in same class + overrides in ancestors)
# ---------------------------------------------------------------------------

def collect_same_name_family(
    graph: Graph,
    method: Node,
    enclosing_type: Node,
    type_ancestor_ids: list[str],
) -> dict[str, str]:
    """Return qualifiedName → describe() for related methods sharing the same simpleName.

    Covers:
    - Overloads: same class, same simpleName, different node id.
    - Overrides/hides: any ancestor class method with the same simpleName.

    Only includes methods that already have a description so the context is
    always meaningful.
    """
    name = method.properties.get('simpleName', '')
    family: dict[str, str] = {}

    for op in enclosing_type.targets('encapsulates'):
        if (op.has_label('Operation')
                and op.id != method.id
                and op.properties.get('simpleName') == name
                and 'description' in op.properties):
            family[op.properties['qualifiedName']] = describe(op, 'description', 'returns', 'howItWorks')

    for ancestor_id in type_ancestor_ids:
        ancestor = graph.nodes.get(ancestor_id)
        if not ancestor:
            continue
        for op in ancestor.targets('encapsulates'):
            if (op.has_label('Operation')
                    and op.properties.get('simpleName') == name
                    and 'description' in op.properties):
                family[op.properties['qualifiedName']] = describe(op, 'description', 'returns', 'howItWorks')

    return family


# ---------------------------------------------------------------------------
# ScriptProcessor
# ---------------------------------------------------------------------------

class ScriptProcessor(Processor):

    def __init__(self, client, prompt_builder, max_workers=8):
        super().__init__(client, prompt_builder, max_workers)
        # Populated by LLMFilter before process_all is called.
        self.type_ancestor_ids: dict[str, list[str]] = {}

    def process_all(self, graph: Graph):
        methods = graph.find_nodes('Operation')
        invokes_edges = graph.find_edges(label='invokes')

        # Build a dep map: method_id → [method_id, ...] of methods it invokes.
        invokes_map: dict[str, list[str]] = {m.id: [] for m in methods}
        for edge in invokes_edges:
            if edge.source in invokes_map:
                invokes_map[edge.source].append(edge.target)

        executor = NodeExecutor(max_workers=self.max_workers)
        total = len(methods)

        def process_fn(met_id: str):
            method = graph.nodes[met_id]
            enclosers = [n for n in method.sources('encapsulates') if n.has_label('Type')]
            if not enclosers:
                return
            clasz = enclosers[0]
            self.process_one(graph, method, clasz)
            check_stop()

        for method in methods:
            executor.submit(method.id, invokes_map.get(method.id, []), process_fn)

        with tqdm(total=total, desc='Processing methods') as pbar:
            last = 0
            while True:
                done = executor.completed
                if done > last:
                    pbar.update(done - last)
                    last = done
                if done >= total:
                    break
                import time; time.sleep(0.1)

        executor.wait_all()
        executor.shutdown()
        writer().flush()

    def process_one(self, graph: Graph, operation: Node, type: Node):
        if (operation.properties.get('description')
                and operation.properties['description'] != "(no description)"):
            return

        op_name = operation.properties['simpleName']
        op_src = remove_java_comments(operation.properties.get('sourceText', ''))
        op_kind = operation.properties.get('kind', 'function')

        typ_name = type.properties['qualifiedName']
        typ_kind = type.properties.get('kind', 'class')
        typ_kind = 'enum' if typ_kind == 'enumeration' else 'abstract class' if typ_kind == 'abstract' else typ_kind

        ancestor_ids = self.type_ancestor_ids.get(type.id, [])
        family = collect_same_name_family(graph, operation, type, ancestor_ids)

        base_instruction = f"Describe the following {op_kind} by using the AnalyzeScript tool.\n\n"
        if family:
            base_instruction = (
                "Related methods sharing the same name are listed below under "
                "\"Related Methods\". If this overrides or hides a parent-class method, "
                "clearly differentiate what this implementation changes or adds. "
                "If this overloads another method in the same class, ensure descriptions "
                "are consistent but distinguish the parameter/use-case differences.\n\n"
                + base_instruction
            )

        op_parameters = OrderedDict()
        op_parameters["Project Name"] = self.prompt.project_name
        op_parameters["Project Description"] = self.prompt.project_desc
        op_parameters[f"{op_kind.title()} to Analyze"] = f"`{op_name}` from the {typ_kind} `{typ_name}`."
        op_parameters[f"{op_kind.title()} Source Code"] = op_src

        invoked_ids = [e.target for e in graph.find_edges(label='invokes') if e.source == operation.id]
        op_parameters["Outgoing Dependencies (Invokes)"] = {
            graph.nodes[nid].properties['qualifiedName']: describe(graph.nodes[nid], 'description', 'returns', 'howToUse', 'docComment')
            for nid in invoked_ids if nid in graph.nodes
        }
        op_parameters["Incoming Dependencies (Invoked By)"] = [
            m.properties['qualifiedName'] for m in operation.sources('invokes')
        ]
        if family:
            op_parameters["Related Methods (same name — overloads / overrides)"] = family

        self.add_classification_options(op_parameters, "operation")

        prompt = self.prompt.compose(base_instruction, **op_parameters)
        logger.debug(prompt)

        description = self.client.generate_json(prompt, "AnalyzeScript")
        self.apply_classifications(graph, operation, description, "operation")
        self.update_method_properties(graph, description, operation)
        writer().write({'data': {'id': operation.id, 'labels': list(operation.labels), 'properties': description}})

    @staticmethod
    def update_method_properties(data: Graph, description: dict, method: Node):
        for key, value in description.items():
            if key.endswith('Reason'):
                continue
            key_lower = lower_first(key)
            if key_lower == 'parameters' and isinstance(value, Iterable):
                param_nodes = [data.nodes[edge.source] for edge in data.find_edges(label='parameterizes')
                               if edge.target == method.id]
                for param in value:
                    if isinstance(param, dict):
                        matching = [n for n in param_nodes if n.properties['simpleName'] == param.get('name')]
                        if matching and matching[0].id in data.nodes:
                            data.nodes[matching[0].id].properties['description'] = param.get('description')
            else:
                data.nodes[method.id].properties[key_lower] = value


# ---------------------------------------------------------------------------
# StructureProcessor
# ---------------------------------------------------------------------------

class StructureProcessor(Processor):

    def process_all(self, graph: Graph):
        types = graph.find_nodes('Type')
        specializes_edges = graph.find_edges(label='specializes')

        # Build dep map: class_id → [parent_id, ...] (parents = classes it specializes)
        spec_map: dict[str, list[str]] = {t.id: [] for t in types}
        for edge in specializes_edges:
            if edge.source in spec_map:
                spec_map[edge.source].append(edge.target)

        executor = NodeExecutor(max_workers=self.max_workers)
        total = len(types)

        def process_fn(cls_id: str):
            clasz = graph.nodes[cls_id]
            enclosers = [n for n in clasz.sources('encloses') if n.has_label('Scope')]
            package = enclosers[0] if enclosers else None
            self.process_one(graph, clasz, package, spec_map)
            check_stop()

        for t in types:
            executor.submit(t.id, spec_map.get(t.id, []), process_fn)

        with tqdm(total=total, desc='Processing classes') as pbar:
            last = 0
            while True:
                done = executor.completed
                if done > last:
                    pbar.update(done - last)
                    last = done
                if done >= total:
                    break
                import time; time.sleep(0.1)

        executor.wait_all()
        executor.shutdown()
        writer().flush()

    def process_one(self, graph: Graph, type: Node, scope: Node, spec_map: dict[str, list[str]]):
        vars_list = StructureProcessor.get_type_relations(graph, type.id)
        op_descriptions = {
            method.properties['qualifiedName']: describe(method)
            for method in type.targets('encapsulates') if method.has_label('Operation')
        }

        typ_name = type.properties['qualifiedName']
        typ_kind = type.properties.get('kind', 'type')
        typ_kind = 'enum' if typ_kind == 'enumeration' else 'abstract class' if typ_kind == 'abstract' else typ_kind

        parent_ids = spec_map.get(type.id, [])
        siblings = self._already_processed_siblings(graph, type, parent_ids)

        base_instruction = f"Describe the following {typ_kind} using the AnalyzeStructure tool.\n\n"
        if siblings or parent_ids:
            base_instruction = (
                "The parent class description is provided below under \"Inherits From\". "
                "Build on the parent's context and maintain consistent layer/stereotype "
                "choices unless there is a clear reason to differ. "
                + (
                    "Sibling classes (sharing the same parent, already analysed) are also "
                    "provided — your description should be consistent in terminology with "
                    "them but must clearly differentiate this class's specific responsibilities. "
                    if siblings else ""
                )
                + "\n\n" + base_instruction
            )

        typ_parameters = OrderedDict()
        typ_parameters["Project Name"] = self.prompt.project_name
        typ_parameters["Project Description"] = self.prompt.project_desc

        if scope:
            scope_name = scope.properties['qualifiedName']
            scope_kind = scope.properties.get('kind', 'scope')
            typ_parameters[f"{typ_kind.title()} to Analyze"] = f"`{typ_kind} {typ_name}` from the {scope_kind} `{scope_name}`."
        else:
            typ_parameters[f"{typ_kind.title()} to Analyze"] = f"`{typ_kind} {typ_name}`."

        typ_parameters[f"{typ_kind.title()} Inherits From"] = {
            graph.nodes[pid].properties['qualifiedName']: describe(graph.nodes[pid], 'description', 'docComment')
            for pid in parent_ids if pid in graph.nodes
        }
        typ_parameters["Inherited By"] = [
            f"{t.properties['kind']} {t.properties['qualifiedName']}"
            for t in type.sources('specializes')
        ]
        if siblings:
            typ_parameters["Sibling Classes (already analysed, same parent)"] = siblings
        typ_parameters["Enclosed Variables/Fields"] = vars_list
        typ_parameters["Enclosed Functions/Methods"] = op_descriptions
        self.add_classification_options(typ_parameters, "type")

        prompt = self.prompt.compose(base_instruction, **typ_parameters)
        logger.debug(prompt)

        description = self.client.generate_json(prompt, "AnalyzeStructure")
        self.apply_classifications(graph, type, description, "type")

        for k, v in description.items():
            if not k.endswith('Reason'):
                graph.nodes[type.id].properties[lower_first(k)] = v

        writer().write({'data': {'id': type.id, 'labels': list(type.labels), 'properties': description}})

    @staticmethod
    def _already_processed_siblings(graph: Graph, type_node: Node, parent_ids: list[str]) -> dict[str, str]:
        result = {}
        for parent_id in parent_ids:
            parent = graph.nodes.get(parent_id)
            if not parent:
                continue
            for sibling in parent.sources('specializes'):
                if sibling.id != type_node.id and 'description' in sibling.properties:
                    result[sibling.properties['qualifiedName']] = describe(sibling, 'description', 'roleStereotype')
        return result

    @staticmethod
    def get_type_relations(data: Graph, cls_id: str) -> list:
        fields = {data.nodes[edge.target] for edge in data.find_edges(label='encapsulates') if edge.source == cls_id}
        return [' '.join(remove_java_comments(f.properties['sourceText']).split())
                for f in fields if f.has_label('Variable')]


# ---------------------------------------------------------------------------
# ComponentProcessor
# ---------------------------------------------------------------------------

class ComponentProcessor(Processor):

    def process_all(self, graph: Graph):
        scopes = graph.find_nodes('Scope', where=lambda n: not n.has_label('Type'))
        encloses_edges = graph.find_edges(
            label='encloses',
            where_source=lambda n: n.has_label('Scope') and not n.has_label('Type'),
            where_target=lambda n: n.has_label('Scope') and not n.has_label('Type'),
        )

        enc_map: dict[str, list[str]] = {s.id: [] for s in scopes}
        for edge in encloses_edges:
            if edge.source in enc_map:
                enc_map[edge.source].append(edge.target)

        # A package depends on its sub-packages: reverse — sub-pkg must be done first.
        dep_map: dict[str, list[str]] = {s.id: [] for s in scopes}
        for parent_id, child_ids in enc_map.items():
            for child_id in child_ids:
                if child_id in dep_map:
                    dep_map[child_id]  # ensure key exists
            # parent depends on children being done
            dep_map[parent_id] = list(child_ids)

        executor = NodeExecutor(max_workers=self.max_workers)
        total = len(scopes)

        def process_fn(pkg_id: str):
            scope = graph.nodes[pkg_id]
            self.process_one(graph, scope, enc_map)
            check_stop()

        for s in scopes:
            executor.submit(s.id, dep_map.get(s.id, []), process_fn)

        with tqdm(total=total, desc='Processing packages') as pbar:
            last = 0
            while True:
                done = executor.completed
                if done > last:
                    pbar.update(done - last)
                    last = done
                if done >= total:
                    break
                import time; time.sleep(0.1)

        executor.wait_all()
        executor.shutdown()
        writer().flush()

    def process_one(self, graph: Graph, scope: Node, enc_map: dict[str, list[str]]):
        typ_descriptions = {
            f"{t.properties['kind']} {t.properties['qualifiedName']}": describe(t)
            for t in scope.targets('encloses') if t.has_label('Type')
        }
        sub_ids = enc_map.get(scope.id, [])
        subscp_descriptions = {
            graph.nodes[nid].properties['qualifiedName']: describe(graph.nodes[nid], 'description', 'returns', 'howToUse', 'docComment')
            for nid in sub_ids if nid in graph.nodes
        }
        scp_kind = scope.properties.get('kind', 'component')

        prompt_base = f"Describe the following {scp_kind} using the AnalyzeComponent tool.\n\n"
        scp_parameters = OrderedDict()
        scp_parameters["Project Name"] = self.prompt.project_name
        scp_parameters["Project Description"] = self.prompt.project_desc
        scp_parameters[f"{scp_kind.title()} to Analyze"] = scope.properties['qualifiedName']
        scp_parameters[f"Enclosed Sub-{scp_kind}s"] = subscp_descriptions
        scp_parameters["Enclosed Classes"] = typ_descriptions
        self.add_classification_options(scp_parameters, "scope")

        prompt = self.prompt.compose(prompt_base, **scp_parameters)
        logger.debug(prompt)

        description = self.client.generate_json(prompt, "AnalyzeComponent")
        self.apply_classifications(graph, scope, description, "scope")
        ComponentProcessor.update_package_properties(graph, description, scope)
        writer().write({'data': {'id': scope.id, 'labels': list(scope.labels), 'properties': description}})

    @staticmethod
    def update_package_properties(data: Graph, description: dict, package: Node):
        for key in description:
            if not key.endswith('Reason'):
                data.nodes[package.id].properties[lower_first(key)] = description[key]


# ---------------------------------------------------------------------------
# InteractionProcessor (stub)
# ---------------------------------------------------------------------------

class InteractionProcessor(Processor):
    def process_all(self, graph: Graph):
        pass


# ---------------------------------------------------------------------------
# VariableProcessor (SecDFD heuristic — unchanged logic)
# ---------------------------------------------------------------------------

class VariableProcessor(Processor):
    def __init__(self, client, prompt_builder, secdfd_cfg=None, max_workers=8):
        super().__init__(client, prompt_builder, max_workers)
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
        scores = {"External Entity": 0.0, "DataStore": 0.0, "Process": 0.0, "Asset": 0.0, "Flow": 0.0}
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
