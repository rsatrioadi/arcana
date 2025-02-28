from abc import ABC, abstractmethod
from typing import Any, Dict, List, Union

from arcanalib.graph import Graph


class Filter(ABC):
	def __init__(self, config: Dict[str, Dict[str, Any]]) -> None:
		"""
		Initialize the filter with a configuration.

		:param config: Configuration for the filter.
		"""
		self.config = config

	@abstractmethod
	def process(self, data: Graph) -> Any:
		"""
		Process the data. This method should be implemented by subclasses.

		:param data: The input data to be processed.
		:return: The processed data.
		"""
		raise NotImplementedError


class EndFilter(Filter):
	"""A special filter that marks the end of pipeline processing."""
	pass


class Seeder(ABC):
	"""
	A class that generates graph data.
	"""

	@abstractmethod
	def generate(self) -> Graph:
		"""
		Generate graph data. This method should be implemented by subclasses.
		"""
		raise NotImplementedError


class Pipeline:
	def __init__(self, *filters: Filter) -> None:
		self.filters: List[Filter] = list(filters)

	def add_filter(self, filt: Filter) -> None:
		self.filters.append(filt)

	def process(self, data: Union[Graph,Seeder]) -> Any:
		"""
		Process the data through the sequence of filters in the pipeline.
		If a seeder is provided instead of graph data, use the seeder to generate the graph data.

		:param data: The input data to be processed or a seeder to generate the data.
		:return: The processed data.
		"""
		d = data.generate() if isinstance(data, Seeder) else data

		for filt in self.filters:
			d = filt.process(d)
			if isinstance(filt, EndFilter):
				break
		return d
