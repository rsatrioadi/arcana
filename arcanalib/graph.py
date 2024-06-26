from collections.abc import Iterable
import json
from typing import Optional, List, Dict, Union, Set, Tuple


def invert(edge_list: List[Dict], new_label: Optional[str] = None) -> List[Dict]:
	"""
	Inverts the direction of edges in the given edge list.

	Args:
		edge_list (list): A list of edges to invert.
		new_label (str, optional): A new label for the inverted edges. Defaults to None.

	Returns:
		list: A list of inverted edges with updated labels.
	"""
	return [
		{
			**edge,
			'source': edge['target'],
			'target': edge['source'],
			'label': new_label if new_label else f"inv_{edge.get('label', 'edge')}",
		}
		for edge in edge_list
	]


def compose(edges1: List[Dict], edges2: List[Dict], new_label: Optional[str] = None) -> List[Dict]:
	"""
	Composes two lists of edges.

	Args:
		edges1 (list): The first list of edges.
		edges2 (list): The second list of edges.
		new_label (str, optional): A new label for the composed edges. Defaults to None.

	Returns:
		list: A list of composed edges.
	"""
	mapping: Dict[str, Dict[str, str]] = {
		edge['source']: {
			'target': edge['target'],
			'label': edge['label']
		} for edge in edges2
	}
	composed_edges: List[Dict] = []
	for edge in edges1:
		if edge['target'] in mapping:
			composed_edges.append({
				'source': edge['source'],
				'target': mapping[edge['target']]['target'],
				'label': new_label if new_label else f"{edge['label']},{mapping[edge['target']]['label']}"
			})
	return composed_edges


def lift(edges1: List[Dict], edges2: List[Dict], new_label: Optional[str] = None) -> List[Dict]:
	"""
	Lifts relations by composing two lists of edges and their inverses.

	Args:
		edges1 (list): The first list of edges.
		edges2 (list): The second list of edges.
		new_label (str, optional): A new label for the lifted edges. Defaults to None.

	Returns:
		list: A list of lifted edges.
	"""
	return compose(compose(edges1, edges2), invert(edges1), new_label)


def triplets(edgeList1, edgeList2):
	source_mapping = {}
	for edge in edgeList1:
		source_mapping[edge['target']] = edge['source']

	paths = set()
	for edge in edgeList2:
		if edge['source'] in source_mapping:
			source1 = source_mapping[edge['source']]
			triplet = (source1, edge['source'], edge['target'])
			paths.add(triplet)

	return paths


class Graph:
	"""
	A class to represent a graph with nodes and edges.

	Attributes:
		nodes (dict): A dictionary of nodes.
		edges (dict): A dictionary of edges categorized by labels.
	"""

	def __init__(self, graph_data: dict) -> None:
		"""
		Initializes the Graph with nodes and edges from the provided data.

		Args:
			graph_data (dict): A dictionary containing graph data with nodes and edges.
		"""
		self.nodes: Dict[str, dict] = {
			node['data']['id']: node['data']
			for node in graph_data['elements']['nodes']
		}
		self.edges: Dict[str, List[dict]] = {}
		for edge in graph_data['elements']['edges']:
			if 'label' in edge['data']:
				label = edge['data']['label']
			else:
				label = ','.join(edge['data']['labels'])
				edge['data']['label'] = label

			if label not in self.edges:
				self.edges[label] = []
			self.edges[label].append(edge['data'])

	def invert_edges(self, edge_label: str, new_label: Optional[str] = None) -> None:
		"""
		Inverts the edges with the specified label and saves them under a new label.

		Args:
			edge_label (str): The label of the edges to invert.
			new_label (str, optional): The label for the inverted edges. Defaults to None.
		"""
		if edge_label in self.edges:
			inverted = invert(self.edges[edge_label], new_label)
			new_label = new_label or f"inv_{edge_label}"
			self.edges[new_label] = inverted

	def compose_edges(self, edge_label1: str, edge_label2: str, new_label: Optional[str] = None) -> None:
		"""
		Composes edges with the specified labels and saves them under a new label.

		Args:
			edge_label1 (str): The label of the first list of edges.
			edge_label2 (str): The label of the second list of edges.
			new_label (str, optional): The label for the composed edges. Defaults to None.
		"""
		if (edge_label1 in self.edges) and (edge_label2 in self.edges):
			new_label = new_label or f"{edge_label1}_{edge_label2}"
			composed = compose(self.edges[edge_label1], self.edges[edge_label2], new_label)
			self.edges[new_label] = composed

	def lift_edges(self, edge_label1: str, edge_label2: str, new_label: Optional[str] = None) -> None:
		"""
		Lifts relations by composing edges with the specified labels and their inverses, then saves them under a new label.

		Args:
			edge_label1 (str): The label of the first list of edges.
			edge_label2 (str): The label of the second list of edges.
			new_label (str, optional): The label for the lifted edges. Defaults to None.
		"""
		if (edge_label1 in self.edges) and (edge_label2 in self.edges):
			lifted = lift(self.edges[edge_label1], self.edges[edge_label2], new_label)
			new_label = new_label or f"lifted_{edge_label1}_{edge_label2}"
			self.edges[new_label] = lifted

	def filter_nodes_by_labels(self, labels: Union[List[str], Set[str]]) -> Dict[str, dict]:
		"""
		Filters nodes by the specified labels.

		Args:
			labels (list or set): A list of labels to filter nodes by.

		Returns:
			dict: A dictionary of filtered nodes.
		"""
		return {
			key: node
			for key, node in self.nodes.items()
			if any(label in labels for label in node.get('labels', []))
		}

	def get_all_node_labels(self) -> Set[str]:
		"""
		Retrieves all unique node labels present in the graph.

		Returns:
			set: A set of all node labels.
		"""
		return {
			label
			for _, node in self.nodes.items()
			for label in node.get('labels', [])
		}

	def get_all_edge_labels(self) -> Set[str]:
		"""
		Retrieves all unique edge labels present in the graph.

		Returns:
			set: A set of all edge labels.
		"""
		return set(self.edges.keys())

	def get_edges_with_node_labels(self, edge_label: str, node_label: str) -> List[Dict]:
		"""
		Retrieves edges whose source and target nodes have the specified labels.

		Args:
			edge_label (str): The label of the edges to retrieve.
			node_label (str): The label of the nodes to filter by.

		Returns:
			list: A list of edges that match the criteria.
		"""
		if edge_label in self.edges:
			return [
				edge
				for edge in self.edges[edge_label]
				if (node_label in self.nodes[edge['source']].get('labels', []))
				and (node_label in self.nodes[edge['target']].get('labels', []))
			]
		return []

	def get_edge_node_labels(self, edge: dict) -> List[Tuple[str, str]]:
		"""
		Retrieves the labels of the source and target nodes for a given edge.

		Args:
			edge (dict): The edge to retrieve node labels for.

		Returns:
			list: A list of tuples containing source and target node labels.
		"""
		source_labels = self.nodes.get(edge['source'], {}).get('labels', [])
		target_labels = self.nodes.get(edge['target'], {}).get('labels', [])
		return [
			(source_label, target_label)
			for source_label in source_labels
			for target_label in target_labels
		]

	def get_source_and_target_labels(self, edge_label: str) -> Set[str]:
		"""
		Retrieves the set of source and target labels for a given list of edges.

		Args:
			edge_label (str): The label of the edges to retrieve labels for.

		Returns:
			set: A set of source and target labels.
		"""
		edge_node_labels: Set[str] = {
			label
			for edge in self.edges[edge_label]
			for label in self.get_edge_node_labels(edge)
		}
		return edge_node_labels

	def generate_ontology(self) -> Dict[str, Set[str]]:
		"""
		Generates an ontology from the graph's edges and nodes.

		Returns:
			dict: A dictionary representing the ontology.
		"""
		return {
			label: self.get_source_and_target_labels(label)
			for label in self.edges
		}

	def __str__(self):
		return json.dumps(self.to_dict())

	def to_dict(self, *args: str, node_labels: Optional[Union[str, Iterable[str]]] = None) -> dict:
		"""
		Converts the graph into a dictionary format with specified edge and node labels.

		Args:
			*args: Variable length argument list of edge labels to include.
			node_labels (str or iterable, optional): Labels of nodes to include. Defaults to None.

		Returns:
			dict: A dictionary representation of the graph with specified elements.
		"""
		included_edge_labels = list(args) if args else list(self.edges.keys())

		if node_labels == 'all':
			included_node_labels = self.get_all_node_labels()
		else:
			included_node_labels: Set[str] = {
				node_label
				for edge_label in included_edge_labels
				for node_label_pair in self.get_source_and_target_labels(edge_label)
				for node_label in node_label_pair
			}
			if isinstance(node_labels, str):
				included_node_labels.add(node_labels)
			elif isinstance(node_labels, Iterable):
				included_node_labels.update(node_labels)

		included_nodes: Dict[str, dict] = self.filter_nodes_by_labels(included_node_labels)

		included_edges: Dict[str, List[dict]] = {
			label: edge_list
			for label, edge_list in self.edges.items()
			if label in included_edge_labels
		}

		return {
			"elements": {
				"nodes": [{"data": node} for node in list(included_nodes.values())],
				"edges": [{"data": edge} for edge in sum(list(included_edges.values()), [])]
			}
		}
