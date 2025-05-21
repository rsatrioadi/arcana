from collections import OrderedDict, defaultdict
from typing import Dict, List, Tuple

from arcanalib.graph import Edge, triplets


def dependency_profile_category(inn: int, out: int) -> str:
	if inn == 0 and out > 0:
		return "outbound"
	elif inn > 0 and out == 0:
		return "inbound"
	elif inn > 0 and out > 0:
		return "transit"
	return "hidden"

def build_triplets(edge_list1, edge_list2) -> list:
	methods = sorted(triplets(edge_list1, edge_list2))

	return methods

def build_hierarchy(method_triplets) -> dict:
	classes = sorted({(pkg, clz) for pkg, clz, _ in method_triplets})
	packages = sorted({pkg for pkg, _ in classes})

	hierarchy = {
		pkg_id: {cls_id: [met_id for _, c, met_id in method_triplets if c == cls_id] for p, cls_id in classes if
				 p == pkg_id} for pkg_id in packages}

	return hierarchy

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

def format_layers(layers: OrderedDict):
	return "\n".join(f"- **{name}**: {desc}" for name, desc in layers.items())

def describe_path(graph, path):
	src_structure = graph.nodes[path[1].source]
	src_method = graph.nodes[path[1].target]
	tgt_method = graph.nodes[path[-2].source]
	tgt_structure = graph.nodes[path[-2].target]
	return f"{src_method.properties['kind'].capitalize()} `{src_method.properties['simpleName']}` ({src_method.properties['description']}) of {src_structure.properties['kind']} `{src_structure.properties['qualifiedName']}` invokes {tgt_method.properties['kind']} `{tgt_method.properties['simpleName']}` ({tgt_method.properties['description']}) of {tgt_structure.properties['kind']} `{tgt_structure.properties['qualifiedName']}`."