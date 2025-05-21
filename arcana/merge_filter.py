import json
from typing import Any, Dict

from arcana.utils import merge_node_properties
from arcanalib.graph import Graph
from arcanalib.pipefilter import Filter


class MergeFilter(Filter):
	def __init__(self, config: Dict[str, Dict[str, Any]]):
		super().__init__(config)

		with open(config['merge']['input'], 'r', encoding="utf-8") as file:
			data = json.load(file)
		self.node_dict_to_merge = data

	def process(self, data: Graph) -> Any:
		merge_node_properties(data.nodes, self.node_dict_to_merge, True)
		return data