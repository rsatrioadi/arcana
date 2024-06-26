from typing import Any, Dict, List

from arcanalib import Graph

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

class Pipeline:
	def __init__(self, *args: Filter) -> None:
		"""
		Initialize the pipeline with an optional sequence of filters.

		:param args: Filters to be added to the pipeline.
		"""
		self.filters: List[Filter] = list(args)

	def add_filter(self, filter: Filter) -> None:
		"""
		Add a filter to the pipeline.

		:param filter: The filter to be added.
		"""
		self.filters.append(filter)

	def process(self, data: Graph) -> Any:
		"""
		Process the data through the sequence of filters in the pipeline.

		:param data: The input data to be processed.
		:return: The processed data.
		"""
		for filter in self.filters:
			data = filter.process(data)
			if isinstance(filter, EndFilter):
				break
		return data
