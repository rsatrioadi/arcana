
from arcanalib.graph import Graph, triplets, invert, lift
from arcanalib.pipefilter import Filter, Seeder

class Arvisaninator(Filter):
	def process(self, data: Graph) -> Graph:

		domain_name = f"{self.config['project']['name']}"
		domain_node = {
			"id:ID": domain_name,
			":LABEL": "Domain",
			"fullName": domain_name,
			"simpleName": domain_name,
			"color": "#666666",
			"dependencyProfileCategory": None,
			"cohesion": None
		}

		def extract_top_level_packages(data):
			# Remove the last element from each tuple and convert to set for uniqueness
			unique_prefixes = set(tuple(item[:-1]) for item in data)

			# Sort unique_prefixes by length of tuples in ascending order
			sorted_prefixes = sorted(unique_prefixes, key=len)

			results = []

			for prefix in sorted_prefixes:
				# Check if the prefix is already a prefix of any result
				if not any(prefix[:len(result)] == result for result in results):
					results.append(prefix)

			return results

		def find_path_from_root(tree, target_node):
			# Step 1: Build a dictionary to map each node to its parent
			parent_map = {}
			for edge in tree:
				parent_map[edge['target']] = edge['source']

			# Step 2: Trace the path from target_node to the root
			path = []
			current_node = target_node
			while current_node in parent_map:
				path.append(current_node)
				current_node = parent_map[current_node]

			# Step 3: Append the root node to the path
			if current_node is not None:
				path.append(current_node)

			# Step 4: Reverse the path to get root to target_node order
			path.reverse()

			return tuple(path)

		pkg_with_classes = {
			edge['source']
			for edge in data.edges['contains']
			if 'Container' in data.nodes[edge['source']]['labels']
			   and 'Structure' in data.nodes[edge['target']]['labels']
		}

		pkg_paths = [
			find_path_from_root(data.edges['contains'], pkg_id)
			for pkg_id in pkg_with_classes
		]

		top_level_packages = extract_top_level_packages(pkg_paths)

		def create_mapping(list1, list2):
			mapping = dict()
			for tup in list1:
				key = tup[-1]  # Last element of the tuple as the key
				for tup2 in list2:
					if tuple(tup[:len(tup2)]) == tup2:  # Match the prefix part in list1 with list2
						mapping[key] = tup2[-1]
						break
			return mapping

		sublayer_to_component = create_mapping(pkg_paths, top_level_packages)
		components = [pkg[-1] for pkg in top_level_packages]

		contains = []
		component_nodes = []
		for component in components:
			component_props = data.nodes[component]['properties']
			component_node = {
				"id:ID": component,
				":LABEL": "Component",
				"fullName": component_props['qualifiedName'],
				"simpleName": component_props['qualifiedName'],
				"color": "#666666",
				"dependencyProfileCategory": None,
				"cohesion": None
			}
			component_nodes.append(component_node)
			contains.append({
				"id": f"{domain_name}-contains-{component}",
				":TYPE": 'CONTAINS',
				":START_ID": domain_name,
				":END_ID": component,
				"references": "{}",
				"dependencyTypes": None,
				"nrDependencies:INT": None,
				"nrCalls:INT": None
			})

		layer_colors = {
			'Presentation Layer': '#ee3239',
			'Service Layer': '#fece00',
			'Domain Layer': '#5eaa5f',
			'Data Source Layer': '#6a6dba',
			'Unknown': '#666666'
		}

		# packages that directly contain classes
		sublayers = list(set(
			{
				"id:ID": pkg,
				":LABEL": 'Sublayer',
				"fullName": pkg,
				"simpleName": pkg,
				"color": layer_colors[data.nodes[pkg]['properties'].get('layer', 'Unknown')],
				"dependencyProfileCategory": None,
				"cohesion": None
			}
			for pkg in pkg_with_classes
		))

		# ("id",":TYPE",":START_ID",":END_ID","references","dependencyTypes","nrDependencies:INT","nrCalls:INT")
		contains += [
			{
				"id": f'{sublayer_to_component[_id]}-contains-{_id}',
				":TYPE": 'CONTAINS',
				":START_ID": sublayer_to_component[_id],
				":END_ID": _id,
				"references": "{}",
				"dependencyTypes": None,
				"nrDependencies:INT": None,
				"nrCalls:INT": None
			}
			for _id, label, fullName, simpleName, color, depProfileCat, cohesion in sublayers
		]
		contains += [
			{
				"id": edge['id'],
				":TYPE": 'CONTAINS',
				":START_ID": edge['source'],
				":END_ID": edge['target'],
				"references": "{}",
				"dependencyTypes": None,
				"nrDependencies:INT": None,
				"nrCalls:INT": None
			}
			for edge in data.edges['contains']
			if 'Container' in data.nodes[edge['source']]['labels'] and 'Structure' in data.nodes[edge['target']]['labels']
		]

		edges_calls = data.edges['calls'] if 'calls' in data.edges else lift(data.edges['hasScript'], data.edges['invokes'])

		calls = [
			{
				"id": f'{edge["source"]}-calls-{edge["target"]}',
				":TYPE": 'CALLS',
				":START_ID": edge['source'],
				":END_ID": edge['target'],
				"references": "{}",
				"dependencyTypes": "compile_time",
				"nrDependencies:INT": edge['properties']['weight'],
				"nrCalls:INT": None
			}
			for edge in edges_calls
			if edge['source'] != edge['target']
		]

		role_stereotype_colors = {
			"Unknown": "#cccccc",
			"Controller": "#decbe4",
			"Coordinator": "#ccebc5",
			"Information Holder": "#fbb4ae",
			"Interfacer": "#fed9a6",
			"User Interfacer": "#fed9a6",
			"Internal Interfacer": "#fed9a6",
			"External Interfacer": "#fed9a6",
			"Service Provider": "#b3cde3",
			"Structurer": "#fddaec",
		}

		modules = [
			{
				"id:ID": _id,
				":LABEL": 'Module',
				"fullName": node['properties']['qualifiedName'],
				"simpleName": node['properties']['simpleName'],
				"color": role_stereotype_colors[node['properties'].get('roleStereotype', 'Unknown')],
				"dependencyProfileCategory": node['properties'].get('dependencyProfile', None),
				"cohesion": None
			}
			for _id, node in data.nodes.items()
			if 'Structure' in node['labels'] and _id != 'java.lang.String']
