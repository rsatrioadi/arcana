from collections import OrderedDict
from arcana.checkpoint import writer
from arcana.utils import remove_author, sentence
from arcana.llm_filter.classification import ClassificationScheme
from arcanalib.graph import Graph, Node


class PromptBuilder:
	def __init__(self, project_cfg, classifications=None):
		self.project_name = project_cfg['name']
		self.project_desc = project_cfg['desc']
		self.classifications = classifications or OrderedDict()
		self.layers = self.classification_options('layer')
		self.role_stereotypes = self.classification_options('roleStereotype')

	def classification_options(self, classification_name: str) -> OrderedDict:
		scheme: ClassificationScheme = self.classifications.get(classification_name)
		if not scheme:
			return OrderedDict()
		return scheme.options_with_undetermined()

	def classification_schemes(self, element_kind: str = None):
		schemes = list(self.classifications.values())
		if not element_kind:
			return schemes
		return [scheme for scheme in schemes if element_kind in scheme.applies_to]

	def initialize_classifications(self, graph: Graph):
		for scheme in self.classification_schemes():
			dimension = graph.add_node(
				scheme.dimension_id,
				"Dimension",
				kind=scheme.dimension_kind,
				simpleName=scheme.dimension_name,
				qualifiedName=scheme.dimension_name,
			)
			writer().write(dimension.to_dict())

			categories = scheme.ordered_options()
			category_names = list(categories.keys())
			for i, (name, desc) in enumerate(categories.items()):
				cat_kwargs = dict(
					kind=scheme.category_kind,
					simpleName=name,
					qualifiedName=name,
					description=desc,
				)
				if scheme.ordered:
					cat_kwargs["order"] = i - 1
				cat = graph.add_node(
					scheme.category_id(name), "Category", **cat_kwargs
				)
				writer().write(cat.to_dict())
				e = graph.add_edge(cat.id, dimension.id, "composes", weight=1)
				writer().write(e.to_dict())

			if scheme.ordered:
				for i in range(1, len(category_names) - 1):
					src = category_names[i]
					tgt = category_names[i + 1]
					e = graph.add_edge(
						scheme.category_id(src), scheme.category_id(tgt), "succeeds", weight=1
					)
					writer().write(e.to_dict())

	def initialize_layers(self, graph: Graph):
		# Backward-compatible alias.
		self.initialize_classifications(graph)

	def compose(self, base_prompt, **parameters):
		
		prompt = base_prompt
		for k, v in parameters.items():
			if isinstance(v, dict) and len(v):
				prompt += f"## {k}\n\n"
				for k1, v1 in v.items():
					if v1:
						prompt += f"* {k1}: {str(v1)}\n"
				prompt += "\n\n"
			elif isinstance(v, list) and len(v):
				prompt += f"## {k}\n\n"
				for v1 in v:
					if v1:
						prompt += f"* {str(v1)}\n"
				prompt += "\n\n"
			elif v:
				prompt += f"## {k}\n\n{str(v)}\n\n"
		return prompt.strip()


def describe(node: Node, *keys) -> str:
	"""Generate a description for a given node."""
	sr, sn = '\r', '\n'
	if not keys:
		keys = ['description', 'docComment', 'returns', 'reason', 'howToUse', 'howItWorks', 'assertions',
				'roleStereotype', 'layer']

	lines = {key: f"**{key}**: {sentence(str(node.properties[key]).replace(sr, '').replace(sn, ' '))}" for key in
				keys if key in node.properties and key != 'docComment' and node.properties[key]}
	if 'docComment' in keys and 'docComment' in node.properties and node.properties['docComment']:
		lines[
			'docComment'] = f"**docComment**: {sentence(remove_author(str(node.properties['docComment'])).replace(sr, '').replace(sn, ' '))} "

	return ' '.join(lines[key] for key in keys if key in lines).strip()
