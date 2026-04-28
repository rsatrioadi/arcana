from typing import Literal
from pydantic import BaseModel, Field


# ---------------------------------------------------------------------------
# Output models
# ---------------------------------------------------------------------------

class Parameter(BaseModel):
    name: str
    type: str = ""
    description: str


class ScriptDescription(BaseModel):
    description: str = Field(description="One-sentence description of the method/constructor/function functionality, in imperative mood.")
    parameters: list[Parameter] = Field(default_factory=list, description="List of parameters. Empty if none.")
    returns: str = Field(description="One-sentence description of the returned value. For constructors, describe the created instance.")
    howToUse: str = Field(description="Usage instructions in less than three sentences.")
    howItWorks: str = Field(description="Implementation details in less than five sentences.")
    preConditions: list[str] = Field(default_factory=list, description="Pre-conditions for the script.")
    postConditions: list[str] = Field(default_factory=list, description="Post-conditions for the script.")
    stereotype: Literal["Accessor", "Mutator", "Creational", "Collaborational", "Other"] = Field(description="Design stereotype.")
    stereotypeReason: str = Field(description="One-sentence explanation for the chosen stereotype.")
    layer: str = Field(description="Architectural layer selected from the provided options.")
    layerReason: str = Field(description="Explanation why this fits the chosen layer but not others.")
    secdfdTypes: list[str] = Field(default_factory=list, description="One or more SecDFD classifications from the provided options.")
    secdfdEvidence: str = Field(default="", description="Short evidence summary for the SecDFD classifications.")


class StructureDescription(BaseModel):
    description: str = Field(description="Up to three sentences describing the key responsibilities of the class/struct/type.")
    keywords: list[str] = Field(default_factory=list, description="Important keywords related to key responsibilities.")
    roleStereotype: str = Field(description="Role stereotype; options are supplied at runtime.")
    roleStereotypeReason: str = Field(description="One-sentence explanation for the chosen role stereotype.")
    layer: str = Field(description="Architectural layer selected from the provided options.")
    layerReason: str = Field(description="Explanation why this fits the chosen layer but not others.")
    secdfdTypes: list[str] = Field(default_factory=list, description="One or more SecDFD classifications from the provided options.")
    secdfdEvidence: str = Field(default="", description="Short evidence summary for the SecDFD classifications.")


class ComponentDescription(BaseModel):
    description: str = Field(description="Describe the functionality of the component/package in up to five sentences.")
    title: str = Field(description="A noun phrase describing the component/package.")
    keywords: list[str] = Field(default_factory=list, description="Important keywords related to the core functionalities.")
    layer: str = Field(description="Architectural layer selected from the provided options.")
    layerReason: str = Field(description="Explanation why this fits the chosen layer but not others.")


# ---------------------------------------------------------------------------
# Tool dicts (OpenAI function-calling format, derived from Pydantic schemas)
# Used as fallback when use_structured_output = false.
# ---------------------------------------------------------------------------

def _tool(name: str, description: str, model: type[BaseModel]) -> dict:
    schema = model.model_json_schema()
    # Pydantic v2 may emit $defs for nested models; OpenAI function-calling
    # accepts these inline definitions without issue.
    return {
        "type": "function",
        "function": {
            "name": name,
            "description": description,
            "parameters": schema,
        },
    }


analyze_script_tool = _tool(
    "AnalyzeScript",
    "Analyzes a program method/constructor/function given its source code and context.",
    ScriptDescription,
)

analyze_structure_tool = _tool(
    "AnalyzeStructure",
    "Analyzes a software class/struct/type based on its inheritance, fields, and methods.",
    StructureDescription,
)

analyze_component_tool = _tool(
    "AnalyzeComponent",
    "Analyzes a software component/package by examining its contents.",
    ComponentDescription,
)

# Map tool name → Pydantic model (used by the structured-output client path).
TOOL_MODELS: dict[str, type[BaseModel]] = {
    "AnalyzeScript": ScriptDescription,
    "AnalyzeStructure": StructureDescription,
    "AnalyzeComponent": ComponentDescription,
}


# ---------------------------------------------------------------------------
# Interaction analysis prompt template (unchanged)
# ---------------------------------------------------------------------------

interaction_analysis = '''## Input:

Consider a project {project_name}, {project_desc}.

- Package Information:
	- `{pkg1_name}`: {pkg1_desc}
	- `{pkg2_name}`: {pkg2_desc}

- Class Information:
	- `{pkg1_name}`:
{cls1_info}
	- `{pkg2_name}`:
{cls2_info}

- Inter-Package Dependencies:
{dep_info}

## Task:

Using the provided information, describe the interaction between the {pkg1_name} and {pkg2_name} packages, focusing on:

- The purpose and nature of their dependency in terms of design.
- An abstract, high-level description of the relationship without referencing specific classes or methods.

## Output:

Provide a cohesive explanation of the interaction in one to two sentences. Keep the response plain text.'''
