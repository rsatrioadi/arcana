import json
from collections import defaultdict
from collections.abc import Iterable
from typing import Optional, List, Dict, Union, Set, Tuple


class Node:
	def __init__(self, _id, *labels, **properties):
		self.id = _id
		self.labels = set(labels)
		self.properties = properties

		# Meta/cache references
		self._graph = None  # The parent Graph, for on-demand lookups
		self._sources_cache = {}  # edge_label -> List[Node]
		self._targets_cache = {}  # edge_label -> List[Node]

	def set_graph(self, graph):
		self._graph = graph
		self._invalidate_cache()

	def _invalidate_cache(self):
		self._sources_cache.clear()
		self._targets_cache.clear()

	def has_label(self, label: str) -> bool:
		return label in self.labels

	def add_label(self, label: str):
		self.labels.add(label)
		return self

	def remove_label(self, label: str):
		self.labels.discard(label)
		return self

	def replace_label(self, old_label: str, new_label: str):
		if old_label in self.labels:
			self.labels.remove(old_label)
			self.labels.add(new_label)
		return self

	def has_property(self, key: str) -> bool:
		return key in self.properties

	def property(self, key: str, value=None):
		if value is None and value is not False:
			return self.properties.get(key)
		elif value is None:  # allow explicit removal if value is None
			self.properties.pop(key, None)
		else:
			self.properties[key] = value
		return self

	def sources(self, edge_label: str):
		if edge_label not in self._sources_cache:
			if not self._graph:
				return []
			es = self._graph.edges.get(edge_label, [])
			self._sources_cache[edge_label] = [self._graph.nodes[e.source] for e in es if e.target == self.id]
		return self._sources_cache[edge_label]

	def targets(self, edge_label: str):
		if edge_label not in self._targets_cache:
			if not self._graph:
				return []
			es = self._graph.edges.get(edge_label, [])
			self._targets_cache[edge_label] = [self._graph.nodes[e.target] for e in es if e.source == self.id]
		return self._targets_cache[edge_label]

	def to_dict(self):
		return {'data': {'id': self.id, 'labels': list(self.labels), 'properties': self.properties}}

	def __repr__(self):
		return json.dumps(self.to_dict())


class Edge:
	def __init__(self, source, target, label, **properties):
		self.id = f'{source}-{label}-{target}'
		self.source = source
		self.target = target
		self.label_val = label
		self.properties = properties

		# Meta/cache references
		self._graph = None
		self._cached_source_node = None
		self._cached_target_node = None

	def set_graph(self, graph):
		self._graph = graph
		self._cached_source_node = None
		self._cached_target_node = None

	def label(self, new_label=None):
		if new_label is None:
			return self.label_val
		else:
			self.label_val = new_label
			self.id = f'{self.source}-{self.label_val}-{self.target}'
			return self

	def property(self, key: str, value=None):
		if value is None and value is not False:
			return self.properties.get(key)
		elif value is None:  # remove
			self.properties.pop(key, None)
		else:
			self.properties[key] = value
		return self

	def source_node(self):
		if self._cached_source_node is None and self._graph is not None:
			self._cached_source_node = self._graph.nodes.get(self.source, None)
		return self._cached_source_node

	def target_node(self):
		if self._cached_target_node is None and self._graph is not None:
			self._cached_target_node = self._graph.nodes.get(self.target, None)
		return self._cached_target_node

	def to_dict(self):
		return {'data': {'id': self.id, 'source': self.source, 'target': self.target, 'label': self.label_val,
			'properties': self.properties}}

	def __repr__(self):
		return json.dumps(self.to_dict())


def invert(edge_list: List[Edge], new_label: Optional[str] = None) -> List[Edge]:
	aggregated = []
	for edge in edge_list:
		lbl = new_label if new_label else f"inv_{edge.label_val}"
		e = Edge(source=edge.target, target=edge.source, label=lbl, **edge.properties)
		aggregated.append(e)
	return aggregated


def compose(edges1: List[Edge], edges2: List[Edge], new_label: Optional[str] = None) -> List[Edge]:
	mapping = defaultdict(list)
	for edge in edges2:
		w = edge.properties.get('weight', 1)
		mapping[edge.source].append({'target': edge.target, 'label': edge.label_val, 'weight': w})

	aggregated = {}
	for edge in edges1:
		w1 = edge.properties.get('weight', 1)
		if edge.target in mapping:
			for m in mapping[edge.target]:
				new_w = w1 * m['weight']
				key = f"{edge.source}-{m['target']}"
				if key not in aggregated:
					lbl = new_label if new_label else f"{edge.label_val}-{m['label']}"
					e = Edge(source=edge.source, target=m['target'], label=lbl, weight=new_w)
					aggregated[key] = e
				else:
					aggregated[key].properties['weight'] += new_w
	return list(aggregated.values())


def lift(edges1: List[Edge], edges2: List[Edge], new_label: Optional[str] = None) -> List[Edge]:
	return compose(compose(edges1, edges2), invert(edges1), new_label)


def triplets(edge_list1: List[Edge], edge_list2: List[Edge]) -> Set[Tuple[str, str, str]]:
	source_mapping = defaultdict(list)
	for edge in edge_list1:
		source_mapping[edge.target].append(edge.source)

	paths = set()
	for edge in edge_list2:
		if edge.source in source_mapping:
			sources = source_mapping[edge.source]
			for source1 in sources:
				paths.add((source1, edge.source, edge.target))
	return paths


class Graph:
	def __init__(self, graph_data: dict = None) -> None:
		if not graph_data:
			self.nodes: Dict[str, Node] = {}
			self.edges: Dict[str, List[Edge]] = {}
			return

		self.nodes: Dict[str, Node] = {}
		for node_data in graph_data['elements']['nodes']:
			n = Node(node_data['data']['id'], *node_data['data']['labels'], **node_data['data']['properties'])
			self.nodes[n.id] = n

		self.edges: Dict[str, List[Edge]] = {}
		for edge_data in graph_data['elements']['edges']:
			d = edge_data['data']
			e = Edge(d['source'], d['target'], d['label'], **d['properties'])
			if e.label_val not in self.edges:
				self.edges[e.label_val] = []
			self.edges[e.label_val].append(e)

		self._set_graph_refs()

	def _set_graph_refs(self):
		for node in self.nodes.values():
			node.set_graph(self)
		for elist in self.edges.values():
			for edge in elist:
				edge.set_graph(self)

	def add_node(self, _id: str, *labels, **properties) -> Optional[Node]:
		if _id in self.nodes:
			return None
		n = Node(_id, *(labels or []), **(properties or {}))
		self.nodes[_id] = n
		n.set_graph(self)
		return n

	def add_edge(self, source_id: str, target_id: str, edge_label: str, **properties) -> Optional[Edge]:
		if source_id not in self.nodes or target_id not in self.nodes:
			return None
		if self.find_edges(label=edge_label, where_source=lambda n: n.id == source_id,
		                   where_target=lambda n: n.id == target_id):
			return None

		e = Edge(source_id, target_id, edge_label, **(properties or {}))
		if edge_label not in self.edges:
			self.edges[edge_label] = []
		self.edges[edge_label].append(e)
		e.set_graph(self)

		# Invalidate caching for the involved nodes
		self.nodes[source_id]._invalidate_cache()
		self.nodes[target_id]._invalidate_cache()

		return e

	def invert_edges(self, edge_label: str, new_label: Optional[str] = None) -> None:
		if edge_label in self.edges:
			inverted = invert(self.edges.get(edge_label, []), new_label)
			nlabel = new_label or f"inv_{edge_label}"
			self.edges[nlabel] = inverted
		self._set_graph_refs()

	def compose_edges(self, edge_label1: str, edge_label2: str, new_label: Optional[str] = None) -> None:
		if (edge_label1 in self.edges) and (edge_label2 in self.edges):
			nlabel = new_label or f"{edge_label1}_{edge_label2}"
			composed_list = compose(self.edges.get(edge_label1, []), self.edges.get(edge_label2, []), nlabel)
			self.edges[nlabel] = composed_list
		self._set_graph_refs()

	def lift_edges(self, edge_label1: str, edge_label2: str, new_label: Optional[str] = None) -> None:
		if (edge_label1 in self.edges) and (edge_label2 in self.edges):
			lifted_list = lift(self.edges.get(edge_label1, []), self.edges.get(edge_label2, []), new_label)
			nlabel = new_label or f"lifted_{edge_label1}_{edge_label2}"
			self.edges[nlabel] = lifted_list
		self._set_graph_refs()

	def filter_nodes_by_labels(self, labels: Union[List[str], Set[str]]) -> Dict[str, Node]:
		return {k: v for k, v in self.nodes.items() if any(label in v.labels for label in labels)}

	def get_all_node_labels(self) -> Set[str]:
		return {label for node in self.nodes.values() for label in node.labels}

	def get_all_edge_labels(self) -> Set[str]:
		return set(self.edges.keys())

	def get_edges_with_node_labels(self, edge_label: str, node_label: str) -> List[Edge]:
		if edge_label in self.edges:
			return [edge for edge in self.edges.get(edge_label, []) if
				node_label in self.nodes.get(edge.source, Node(None)).labels and node_label in self.nodes.get(
					edge.target, Node(None)).labels]
		return []

	def get_edge_node_labels(self, edge: Edge) -> List[Tuple[str, str]]:
		source_labels = self.nodes.get(edge.source, Node(None)).labels
		target_labels = self.nodes.get(edge.target, Node(None)).labels
		return [(sl, tl) for sl in source_labels for tl in target_labels]

	def get_source_and_target_labels(self, edge_label: str) -> Set[Tuple[str, str]]:
		if edge_label not in self.edges:
			return set()
		return {(sl, tl) for e in self.edges.get(edge_label, []) for (sl, tl) in self.get_edge_node_labels(e)}

	def generate_ontology(self) -> 'Graph':
		ontology_map = {label: self.get_source_and_target_labels(label) for label in self.edges}
		onto_graph = Graph()
		onto_graph.edges = {lbl: [Edge(src, tgt, lbl) for (src, tgt) in ontology_map[lbl]] for lbl in ontology_map}
		sources = {src for lbl in ontology_map for (src, _) in ontology_map[lbl]}
		targets = {tgt for lbl in ontology_map for (_, tgt) in ontology_map[lbl]}
		all_ids = sources.union(targets)
		onto_graph.nodes = {i: Node(i, i) for i in all_ids}
		onto_graph._set_graph_refs()
		return onto_graph

	def find_nodes(self, label=None, where=None) -> List[Node]:
		return [node for node in self.nodes.values() if
			(not label or label in node.labels) and (not where or where(node))]

	def find_node(self, label=None, where=None) -> Optional[Node]:
		nodes = self.find_nodes(label, where)
		if nodes:
			return nodes[0]
		return None

	def find_edge(self, label=None, source_label=None, target_label=None, where_edge=None, where_source=None,
	              where_target=None):
		edges = self.find_edges(label, source_label, target_label, where_edge, where_source, where_target)
		if edges:
			return edges[0]
		return None

	def find_edges(self, label=None, source_label=None, target_label=None, where_edge=None, where_source=None,
	               where_target=None):
		if label:
			edge_list = self.edges.get(label, [])
		else:
			edge_list = [e for edges in self.edges.values() for e in edges]

		return [e for e in edge_list if (not source_label or source_label in self.nodes[e.source].labels) and (
					not target_label or target_label in self.nodes[e.target].labels) and (
					                                not where_edge or where_edge(e)) and (
					                                not where_source or where_source(self.nodes[e.source])) and (
					                                not where_target or where_target(self.nodes[e.target]))]

	def find_source(self, edge_list: List[Edge], start_node: Node, predicate, default: Node = None):
		predecessors = defaultdict(list)
		for e in edge_list:
			predecessors[e.target].append(e.source)
		visited = set()
		stack = [start_node.id]

		while stack:
			current = stack.pop()
			if current in visited:
				continue
			visited.add(current)
			if predicate(self.nodes[current]):
				return self.nodes[current]
			stack.extend(predecessors[current])
		return default

	@staticmethod
	def _adj_list(edge_list: List[Edge]):
		adj_list = {}
		outdegree = {}
		for e in edge_list:
			s, t = e.source, e.target
			if s not in adj_list:
				adj_list[s] = []
			if s not in outdegree:
				outdegree[s] = 0
			if t not in adj_list:
				adj_list[t] = []
			if t not in outdegree:
				outdegree[t] = 0
			adj_list[s].append(t)
			outdegree[s] += 1
		return adj_list, outdegree

	@staticmethod
	def _outdeg_leaf_nodes(outdegree):
		return [n for n, c in outdegree.items() if c == 0]

	def process_nodes(self, edges: List[Edge], node_processor):
		adj_list, outdegree = Graph._adj_list(edges)
		results = {}
		queue = Graph._outdeg_leaf_nodes(outdegree)
		while queue:
			next_queue = []
			for n_id in queue:
				dependencies = adj_list.get(n_id, [])
				resolved = {dep: results[dep] for dep in dependencies if dep in results}
				results[n_id] = node_processor(self.nodes[n_id], resolved)
				for caller, targets in adj_list.items():
					if n_id in targets:
						outdegree[caller] -= 1
						if outdegree[caller] == 0:
							next_queue.append(caller)
			queue = next_queue
		for n_id, deg in outdegree.items():
			if deg > 0 and n_id not in results:
				dependencies = adj_list.get(n_id, [])
				resolved = {dep: results[dep] for dep in dependencies if dep in results}
				results[n_id] = node_processor(self.nodes[n_id], resolved)
		return results

	@staticmethod
	def toposorted_nodes(edges: List[Edge], nodes: List[Node] = None):
		adj_list, outdegree = Graph._adj_list(edges)
		sorted_nodes = []
		node_deps = {}
		queue = Graph._outdeg_leaf_nodes(outdegree)

		while queue:
			next_queue = []
			for n_id in queue:
				dependencies = adj_list.get(n_id, [])
				sorted_nodes.append(n_id)
				node_deps[n_id] = dependencies
				for caller, targets in adj_list.items():
					if n_id in targets:
						outdegree[caller] -= 1
						if outdegree[caller] == 0:
							next_queue.append(caller)
			queue = next_queue

		for n_id, deg in outdegree.items():
			if deg > 0 and n_id not in sorted_nodes:
				dependencies = adj_list.get(n_id, [])
				sorted_nodes.append(n_id)
				node_deps[n_id] = dependencies
    
		for node in nodes:
			if node.id not in sorted_nodes:
				sorted_nodes.insert(0, node.id)
				node_deps[node.id] = []
    
		return sorted_nodes, node_deps

	def clean_up(self):
		for edge_type in list(self.edges.keys()):
			self.edges[edge_type] = [e for e in self.edges.get(edge_type, []) if
				e.source in self.nodes and e.target in self.nodes]

	def find_paths(self, *edge_sequence: str) -> List[List[Edge]]:
		def get_edges(label: str) -> List[Edge]:
			if label.startswith('-'):
				base_label = label[1:]
				if base_label in self.edges:
					return invert(self.edges.get(base_label, []))
				return []
			return self.edges.get(label, [])

		def find_next(current_paths: List[List[Edge]], label: str) -> List[List[Edge]]:
			result = []
			for path in current_paths:
				last_node = path[-1].target if path else None
				for candidate in get_edges(label):
					if not path or candidate.source == last_node:
						result.append(path + [candidate])
			return result

		paths = [[]]
		for lbl in edge_sequence:
			paths = find_next(paths, lbl)
		return paths

	def __repr__(self):
		return json.dumps(self.to_dict())

	def to_dict(self, *args: str, node_labels: Optional[Union[str, Iterable[str]]] = None) -> dict:
		included_edge_labels = list(args) if args else list(self.edges.keys())
		if node_labels == 'all':
			included_node_labels = self.get_all_node_labels()
		else:
			included_node_labels: Set[str] = {nlbl for elbl in included_edge_labels for nlbl_pair in
				self.get_source_and_target_labels(elbl) for nlbl in nlbl_pair}
			if isinstance(node_labels, str):
				included_node_labels.add(node_labels)
			elif isinstance(node_labels, Iterable):
				included_node_labels.update(node_labels)

		included_nodes = {k: v for k, v in self.filter_nodes_by_labels(included_node_labels).items()}
		included_edges = {lbl: eds for lbl, eds in self.edges.items() if lbl in included_edge_labels}
		return {"elements": {"nodes": [{"data": n.to_dict()['data']} for n in included_nodes.values()],
			"edges": [{"data": e.to_dict()['data']} for e in sum(included_edges.values(), [])]}}
