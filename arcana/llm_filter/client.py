import json
import sys
import time
import logging

from pydantic import BaseModel

from arcana import templates
from arcana.utils import find_first_valid_json

logger = logging.getLogger(__name__)

_RETRY_DELAYS = (2, 4, 8)


class LLMClient:
    def __init__(self, llm_cfg, project_cfg):
        from openai import OpenAI
        self.client = OpenAI(api_key=llm_cfg['apikey'], base_url=llm_cfg.get('apibase'))
        self.model = llm_cfg.get('model', 'gpt-4o-mini')
        self.timeout = float(llm_cfg.get('timeout', 300))
        self.use_structured_output = str(llm_cfg.get('use_structured_output', 'true')).strip().lower() in {'1', 'true', 'yes', 'on'}

    # ------------------------------------------------------------------
    # Public interface
    # ------------------------------------------------------------------

    def generate_json(self, prompt: str, tool: str) -> dict:
        """Generate a structured description.

        `tool` is the tool name string (e.g. "AnalyzeScript"). The method tries
        the modern structured-output path first (if enabled) and falls back to
        the legacy tool-calling path on failure or when disabled.
        """
        model_class = templates.TOOL_MODELS.get(tool)

        if self.use_structured_output and model_class:
            result = self._generate_structured(prompt, tool, model_class)
        else:
            result = self._generate_tool_call(prompt)

        if 'description' not in result:
            result['description'] = "(no description)"
        return result

    def generate_text(self, prompt: str) -> str:
        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[{"role": "user", "content": prompt}],
                max_tokens=4096, temperature=0, seed=42,
                timeout=self.timeout,
            )
            return response.choices[0].message.content
        except Exception as e:
            sys.stderr.write(f"Generate text error: {e}\n")
            return "(no description)"

    # ------------------------------------------------------------------
    # Private helpers
    # ------------------------------------------------------------------

    def _generate_structured(self, prompt: str, tool_name: str, model_class: type[BaseModel]) -> dict:
        """Use OpenAI structured outputs (json_schema strict mode)."""
        schema = model_class.model_json_schema()
        # Remove $schema key if present — not accepted by the API
        schema.pop("$schema", None)

        for attempt, delay in enumerate((*_RETRY_DELAYS, None)):
            try:
                response = self.client.chat.completions.create(
                    model=self.model,
                    messages=[
                        {"role": "system", "content": "You are a tool for analyzing software architecture of code implementations."},
                        {"role": "user", "content": prompt},
                    ],
                    response_format={
                        "type": "json_schema",
                        "json_schema": {
                            "name": tool_name,
                            "schema": schema,
                            "strict": True,
                        },
                    },
                    temperature=0, seed=42,
                    timeout=self.timeout,
                )
                content = response.choices[0].message.content
                instance = model_class.model_validate_json(content)
                return instance.model_dump()
            except Exception as e:
                if delay is None:
                    logger.warning("Structured output failed after retries (%s); falling back to tool-calling.", e)
                    return self._generate_tool_call(prompt)
                logger.warning("Structured output attempt %d failed (%s); retrying in %ds.", attempt + 1, e, delay)
                time.sleep(delay)

        return {}  # unreachable

    def _generate_tool_call(self, prompt: str) -> dict:
        """Legacy path: OpenAI tool-calling to constrain output format."""
        for attempt, delay in enumerate((*_RETRY_DELAYS, None)):
            try:
                response = self.client.chat.completions.create(
                    model=self.model,
                    messages=[
                        {"role": "system", "content": "You are a tool for analyzing software architecture of code implementations."},
                        {"role": "user", "content": prompt},
                    ],
                    tools=[
                        templates.analyze_script_tool,
                        templates.analyze_structure_tool,
                        templates.analyze_component_tool,
                    ],
                    tool_choice="required",
                    temperature=0, seed=42,
                    timeout=self.timeout,
                )

                tool_calls = response.choices[0].message.tool_calls
                if tool_calls:
                    return json.loads(tool_calls[0].function.arguments)

                content = response.choices[0].message.content
                json_content = find_first_valid_json(content)
                if json_content:
                    return json.loads(json_content)
                return {}

            except Exception as e:
                if delay is None:
                    sys.stderr.write(f"Generate JSON (tool-call) error: {e}\n")
                    return {}
                logger.warning("Tool-call attempt %d failed (%s); retrying in %ds.", attempt + 1, e, delay)
                time.sleep(delay)

        return {}  # unreachable
