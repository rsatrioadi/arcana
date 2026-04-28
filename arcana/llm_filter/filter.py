import os
from collections import OrderedDict
from itertools import combinations
from typing import Any, Dict, List, TextIO
import logging

from tqdm.auto import tqdm

from arcana import templates
from arcana.checkpoint import configure_writer, load_checkpoint, writer
from arcana.filters import check_stop, layers_to_ordereddict
from arcana.graph_utils import (build_hierarchy, build_triplets, describe_path,
                                group_paths_by_endpoints)
from arcana.llm_filter.classification import default_classification_schemes
from arcana.llm_filter.client import LLMClient
from arcana.llm_filter.processors import (ComponentProcessor, InteractionProcessor,
                                           ScriptProcessor, StructureProcessor, VariableProcessor)
from arcana.llm_filter.prompt import PromptBuilder
from arcana.utils import lower_first, remove_java_comments, write_jsonl
from arcanalib.graph import Edge, Graph, Node
from arcanalib.pipefilter import Filter

logger = logging.getLogger(__name__)


class LLMFilter(Filter):
    def __init__(self, config: Dict[str, Dict[str, Any]]):
        super().__init__(config)
        self.client = LLMClient(config['llm'], config['project'])

        llm_cfg = config.get('llm', {})
        self.max_workers = int(llm_cfg.get('workers', 8))

        # Checkpoint / resume config
        self.checkpoint_file = llm_cfg.get('checkpoint_file', 'checkpoints.jsonl')
        self.resume = str(llm_cfg.get('resume', 'false')).strip().lower() in {'1', 'true', 'yes', 'on'}
        configure_writer(self.checkpoint_file, append=self.resume)

        layer_cfg = config.get('layers')
        self.layers = layers_to_ordereddict(layer_cfg) if layer_cfg else OrderedDict()

        stereo_cfg = config.get('stereotypes')
        self.role_stereotypes = OrderedDict(stereo_cfg) if stereo_cfg else OrderedDict()

        self.secdfd_cfg = config.get('secdfd', {})
        self.secdfd_enabled = str(self.secdfd_cfg.get("enabled", "false")).strip().lower() in {"1", "true", "yes", "on"}

        stereocode_cfg = config.get('stereocode', {})
        self.stereocode_enabled = str(stereocode_cfg.get("enabled", "false")).strip().lower() in {"1", "true", "yes", "on"}

        classifications = default_classification_schemes(
            self.layers,
            self.role_stereotypes,
            secdfd_enabled=self.secdfd_enabled,
            stereocode_enabled=self.stereocode_enabled,
        )
        self.prompt_builder = PromptBuilder(config['project'], classifications)
        self.script_processor = ScriptProcessor(self.client, self.prompt_builder, self.max_workers)
        self.structure_processor = StructureProcessor(self.client, self.prompt_builder, self.max_workers)
        self.variable_processor = VariableProcessor(self.client, self.prompt_builder, self.secdfd_cfg, self.max_workers)
        self.component_processor = ComponentProcessor(self.client, self.prompt_builder, self.max_workers)
        self.interaction_processor = InteractionProcessor(self.client, self.prompt_builder, self.max_workers)

    def process(self, graph: Graph) -> Graph:
        # 0. Resume: pre-load previous checkpoint so processors skip done nodes.
        if self.resume and os.path.exists(self.checkpoint_file):
            logger.info("Resuming from checkpoint: %s", self.checkpoint_file)
            load_checkpoint(self.checkpoint_file, graph)

        # 1. Initialize classification dimension/category nodes.
        self.prompt_builder.initialize_layers(graph)

        # 2. Build ancestor map for ScriptProcessor (same-name family / override context).
        #    Maps type_id → [all ancestor type_ids] via specializes edges.
        type_ancestor_ids = self._build_type_ancestor_map(graph)
        self.script_processor.type_ancestor_ids = type_ancestor_ids

        # 3. Process methods.
        self.script_processor.process_all(graph)

        # 4. Process classes.
        self.structure_processor.process_all(graph)

        # 5. Process variables (SecDFD).
        if self.secdfd_enabled:
            self.variable_processor.process_all(graph)

        # 6. Process packages.
        self.component_processor.process_all(graph)

        # 7. Process interactions (stub).
        self.interaction_processor.process_all(graph)

        return graph

    @staticmethod
    def _build_type_ancestor_map(graph: Graph) -> dict[str, list[str]]:
        """Return type_id → ordered list of ancestor type ids (parents first) via specializes."""
        specializes_edges = graph.find_edges(label='specializes')
        # Build direct parent map: child_id → [parent_id, ...]
        parents: dict[str, list[str]] = {}
        for edge in specializes_edges:
            parents.setdefault(edge.source, []).append(edge.target)

        # BFS from each type to collect all ancestors in order.
        result: dict[str, list[str]] = {}
        for t in graph.find_nodes('Type'):
            visited: list[str] = []
            seen: set[str] = set()
            queue = list(parents.get(t.id, []))
            while queue:
                pid = queue.pop(0)
                if pid in seen:
                    continue
                seen.add(pid)
                visited.append(pid)
                queue.extend(parents.get(pid, []))
            result[t.id] = visited
        return result

    # ------------------------------------------------------------------
    # Legacy interaction processing (kept from original, not currently
    # wired into process() but available for future use)
    # ------------------------------------------------------------------

    def process_hierarchy(self, graph: Graph, jsonl_file, log_file):
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
                    self.process_interactions(graph, pkg1, pkg2, path_groups[(pkg1_id, pkg2_id)], hierarchy, jsonl_file, log_file)
                if path_groups[(pkg2_id, pkg1_id)]:
                    self.process_interactions(graph, pkg2, pkg1, path_groups[(pkg2_id, pkg1_id)], hierarchy, jsonl_file, log_file)

    def process_interactions(self, graph: Graph, c1: Node, c2: Node, path_groups: List[List[Edge]], hierarchy,
                             jsonl_file: TextIO, log_file: TextIO):
        c1_name = c1.properties["qualifiedName"]
        c2_name = c2.properties["qualifiedName"]
        c1_desc = c1.properties.get("description", "")
        c2_desc = c2.properties.get("description", "")

        c1_contents = hierarchy.get(c1.id, dict())
        c2_contents = hierarchy.get(c2.id, dict())

        c1_structure_info = "\n".join(
            f"        - `{graph.nodes[c_id].properties['simpleName']}`: {graph.nodes[c_id].properties.get('description', '')}"
            for c_id, _ in c1_contents.items())
        c2_structure_info = "\n".join(
            f"        - `{graph.nodes[c_id].properties['simpleName']}`: {graph.nodes[c_id].properties.get('description', '')}"
            for c_id, _ in c2_contents.items())

        dep_info = f"    - Dependencies from `{c1_name}` to `{c2_name}`:\n" + "\n".join(
            f"        - {describe_path(graph, path)}" for path in path_groups) if path_groups else ""

        prompt = templates.interaction_analysis.format(
            project_name=self.prompt_builder.project_name,
            project_desc=self.prompt_builder.project_desc,
            pkg1_name=c1_name, pkg2_name=c2_name,
            pkg1_desc=c1_desc, pkg2_desc=c2_desc,
            cls1_info=c1_structure_info, cls2_info=c2_structure_info,
            dep_info=dep_info,
        )

        log_file.write(prompt)
        log_file.write('\n\n======\n\n')

        description = self.client.generate_text(prompt)
        pkg1_edge = Edge(source=c1.id, target=c2.id, label="dependsOn", description=description) if dep_info else None

        if pkg1_edge:
            if "dependsOn" not in graph.edges:
                graph.edges["dependsOn"] = []
            graph.edges["dependsOn"].append(pkg1_edge)
            write_jsonl(jsonl_file, pkg1_edge.to_dict())
