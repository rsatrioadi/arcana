from collections import Counter, OrderedDict
import logging

from arcana.graph_utils import dependency_profile_category
from arcanalib.graph import Graph, invert, lift
from arcanalib.pipefilter import Filter


logger = logging.getLogger(__name__)

class MetricsFilter(Filter):
	def process(self, data: Graph) -> Graph:
		"""
		Process the data to generate dependency profiles and categorize nodes.

		Args:
			data (Graph): The input data.

		Returns:
			Graph: The processed data with dependency profiles.
		"""
		# 1. Create a Dependency Profile dimension with its 4 categories
		dim = data.add_node(
			"Dependency Profile", "Dimension",
			kind="categorical",
			simpleName="Dependency Profile",
			qualifiedName="Dependency Profile"
		)
		categories = OrderedDict([
			("outbound", "Calls leaving the module"),
			("inbound",  "Calls entering the module"),
			("transit",  "Both inbound and outbound"),
			("hidden",   "Neither inbound nor outbound"),
		])
		cat_ids = {}
		for idx, (key, desc) in enumerate(categories.items()):
			cat = data.add_node(
				f"dp:{key}", "Category",
				kind="dependency profile",
				simpleName=key,
				qualifiedName=key,
				description=desc,
				order=idx
			)
			cat_ids[key] = cat.id
			data.add_edge(cat.id, dim.id, "composes", weight=1)
		
		# 2. Compute raw in/out counts
		parents = {e.source: e.target for e in invert(data.find_edges(label='encloses'))}
		dependency_profiles = {node.id:list() for node in data.find_nodes('Type')}

		calls = data.edges.get('calls',
							   lift(data.find_edges(label='encapsulates'), data.find_edges(label='invokes'), 'calls'))

		for edge in calls:
			source_id, target_id = edge.source, edge.target
			if parents.get(source_id) != parents.get(target_id):
				dependency_profiles[source_id].append('out')
				dependency_profiles[target_id].append('in')

		dependency_profiles = {node_id: Counter(prof) for node_id, prof in dependency_profiles.items()}
		logger.debug(dependency_profiles)

		# 3. Attach classification edges instead of setting a string property
		for node_id, profile in dependency_profiles.items():
			cat_key = dependency_profile_category(profile['in'], profile['out'])
			target_id = cat_ids.get(cat_key)
			if target_id:
				data.add_edge(node_id, target_id, "implements", weight=1)

		return data