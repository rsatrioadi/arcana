from typing import Any, Dict, List, Union

from arcanalib.graph import Graph


class Filter:
	def __init__(self, config: Dict[str, Dict[str, Any]]) -> None:
		"""
		Initialize the filter with a configuration.

		:param config: Configuration for the filter.
		"""
		self.config = config

	def process(self, data: Graph) -> Any:
		"""
		Process the data. This method should be implemented by subclasses.

		:param data: The input data to be processed.
		:return: The processed data.
		"""
		raise NotImplementedError("Subclasses must implement this method")


class EndFilter(Filter):
	"""
	A special type of filter that marks the end of the pipeline processing.
	"""
	pass


class Seeder:
	"""
	A class that generates graph data.
	"""

	def generate(self) -> Graph:
		"""
		Generate graph data. This method should be implemented by subclasses.
		"""
		raise NotImplementedError("Subclasses must implement this method")


class Pipeline:
	def __init__(self, *args: Filter) -> None:
		self.filters: List[Filter] = list(args)

	def add_filter(self, filter: Filter) -> None:
		self.filters.append(filter)

	def process(self, data: Union[Graph, Seeder]) -> Any:
		"""
		Process the data through the sequence of filters in the pipeline.
		If a seeder is provided instead of graph data, use the seeder to generate the graph data.

		:param data: The input data to be processed or a seeder to generate the data.
		:return: The processed data.
		"""
		# If a seeder is provided, use it to generate the graph data
		if isinstance(data, Seeder):
			data = data.generate()

		# sys.stderr.write(f"Graph stats: {len(data.nodes)} nodes, {len(data.edges)} edge types.")
		for filter in self.filters:
			data = filter.process(data)
			if isinstance(filter, EndFilter):
				break
		return data
