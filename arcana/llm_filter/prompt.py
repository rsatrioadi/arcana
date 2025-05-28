from collections import OrderedDict
from arcana.checkpoint import writer
from arcana.utils import remove_author, sentence
from arcanalib.graph import Graph, Node


class PromptBuilder:
	def __init__(self, project_cfg, layers_cfg=None, stereotypes_cfg=None):
		self.project_name = project_cfg['name']
		self.project_desc = project_cfg['desc']
		self.layers      = layers_cfg or OrderedDict()
		self.layers.update({
			'Undetermined': "Architectural layer cannot be determined for this element."
		})
		# self.layers.move_to_end('Undetermined', False)
		self.role_stereotypes = stereotypes_cfg or OrderedDict()
		self.role_stereotypes.update({
			'Undetermined': "Role stereotype cannot be determined for this element."
		})
		# self.role_stereotypes.move_to_end('Undetermined', False)
		# self.layers_str = format_layers(layers_cfg)

	def initialize_layers(self, graph: Graph):
		layer_dimension = graph.add_node(
      		f"Architectural Layer", 
        	"Dimension", 
			kind="categorical-ordered", 
			simpleName="Architectural Layer",
			qualifiedName="Architectural Layer")
		writer().write(layer_dimension.to_dict())

		layers = self.layers.copy()
		layers.move_to_end('Undetermined', False)
		for i, (name, desc) in enumerate(layers.items()):
			cat = graph.add_node(
				f"layer:{name}", "Category",
				kind="architectural layer",
				simpleName=name,
				qualifiedName=name,
				description=desc,
				order=i-1
			)
			writer().write(cat.to_dict())
			e = graph.add_edge(cat.id, layer_dimension.id, "composes", weight=1)
			writer().write(e.to_dict())

		t_layers = list(layers.items())
		for i in range(1, len(t_layers) - 1):
			src = t_layers[i][0]
			tgt = t_layers[i + 1][0]
			e = graph.add_edge(f"layer:{src}", f"layer:{tgt}", "succeeds", weight=1)
			writer().write(e.to_dict())
   
   
		stereo_dimension = graph.add_node(
			"Role Stereotype",
			"Dimension",
			kind="categorical-nominal",
			simpleName="Role Stereotype",
			qualifiedName="Role Stereotype"
		)
		writer().write(stereo_dimension.to_dict())

		role_stereotypes = self.role_stereotypes.copy()
		role_stereotypes.move_to_end('Undetermined', False)
		for i, (name, desc) in enumerate(role_stereotypes.items()):
			cat = graph.add_node(
				f"rs:{name}", "Category",
				kind="role stereotype",
				simpleName=name,
				qualifiedName=name,
				description=desc
			)
			writer().write(cat.to_dict())
			e = graph.add_edge(cat.id, stereo_dimension.id, "composes", weight=1)
			writer().write(e.to_dict())

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