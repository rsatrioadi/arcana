from openai import OpenAI
import json, sys

from arcana import templates
from arcana.utils import find_first_valid_json

class LLMClient:
	def __init__(self, llm_cfg, project_cfg):
		self.client = OpenAI(api_key=llm_cfg['apikey'], base_url=llm_cfg.get('apibase'))
		self.model = llm_cfg.get('model', 'gpt-4o-mini')
		self.timeout = float(llm_cfg.get('timeout', 300))

	def generate_json(self, prompt, tool):
		"""Generate a description using the OpenAI client."""
		try:
			if tool:
				response = self.client.chat.completions.create(model=self.model, messages=[
					{"role": "system", "content": "You are a software architecture analysis tool."},
					{"role": "user", "content": prompt}], tools=[templates.analyze_script_tool,
																 templates.analyze_structure_tool,
																 templates.analyze_component_tool],
															   tool_choice="required", temperature=0, seed=42,
															   timeout=self.timeout)

				tool_calls = response.choices[0].message.tool_calls

				if tool_calls:
					args_str = tool_calls[0].function.arguments
					description = json.loads(args_str)
				else:
					content = response.choices[0].message.content
					json_content = find_first_valid_json(content)
					if json_content:
						description = json.loads(json_content)
					else:
						description = dict()

			else:
				response = self.client.chat.completions.create(model=self.model,
															   response_format={"type": "json_object"},
															   messages=[{"role": "user", "content": prompt}],
															   max_tokens=4096, temperature=0, seed=42,
															   timeout=self.timeout)

				content = response.choices[0].message.content
				description = json.loads(content)
		except Exception as e:
			sys.stderr.write(f"Generate JSON description error: {e}")
			description = {}

		if 'description' not in description:
			description['description'] = "(no description)"
		return description

	def generate_text(self, prompt):
		try:
			response = self.client.chat.completions.create(model=self.model,
														   messages=[{"role": "user", "content": prompt}],
														   max_tokens=4096, temperature=0, seed=42,
														   timeout=float(self.config['llm'].get('timeout', 300)))
			description = response.choices[0].message.content
		except Exception as e:
			sys.stderr.write(f"Generate text description error: {e}")
			description = "(no description)"

		return description