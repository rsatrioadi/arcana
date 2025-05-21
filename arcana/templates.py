script_description = {
	"$schema": "http://json-schema.org/draft-07/schema#",
	"title": "ScriptDescription",
	"type": "object",
	"properties": {
		"description": {
			"type": "string",
			"description": "One-sentence description of the method/constructor/function functionality."
		},
		"parameters": {
			"type": "array",
			"items": {
				"type": "object",
				"properties": {
					"name": {
						"type": "string",
						"description": "Parameter name."
					},
					"type": {
						"type": "string",
						"description": "Parameter type."
					},
					"description": {
						"type": "string",
						"description": "Brief description of the parameter."
					}
				},
				"required": [
					"name",
					"description"
				]
			},
			"description": "List of script parameters. Empty if none."
		},
		"returns": {
			"type": "string",
			"description": "One-sentence description of the returned object or value. For constructors, consider the newly created instance as the return."
		},
		"howToUse": {
			"type": "string",
			"description": "Usage instructions in less than three sentences."
		},
		"howItWorks": {
			"type": "string",
			"description": "Implementation details in less than five sentences."
		},
		"preConditions": {
			"type": "array",
			"items": {
				"type": "string"
			},
			"description": "List of pre-conditions for the script."
		},
		"postConditions": {
			"type": "array",
			"items": {
				"type": "string"
			},
			"description": "List of post-conditions for the script."
		},
		"stereotype": {
			"type": "string",
			"enum": [
				"Accessor",
				"Mutator",
				"Creational",
				"Collaborational",
				"Other"
			],
			"description": "Design stereotype of the script."
		},
		"stereotypeReason": {
			"type": "string",
			"description": "One-sentence explanation for the chosen stereotype."
		},
		"layer": {
			"type": "string",
			"description": "Architectural layer classification selected from the provided options."
		},
		"layerReason": {
			"type": "string",
			"description": "Explanation why the script fits the chosen architectural layer but not others."
		}
	},
	"required": [
		"description",
		"howItWorks",
		"howToUse",
		"layer",
		"layerReason",
		"parameters",
		"postConditions",
		"preConditions",
		"returns",
		"stereotype",
		"stereotypeReason"
	],
	"additionalProperties": False
}

analyze_script_tool = {
	"type": "function",
	"function": {
		"name": "AnalyzeScript",
		"description": "Analyzes a program method/constructor/function given its source code and context. Returns an explanation covering functionality, parameters, return value, design rationale, usage, implementation details, assertions, stereotype, and architectural layer classification.",
		"parameters": script_description
	}
}

structure_description = {
	"$schema": "http://json-schema.org/draft-07/schema#",
	"title": "StructureDescription",
	"type": "object",
	"properties": {
		"description": {
			"type": "string",
			"description": "Up to three sentences describing the key responsibilities of the class/struct/type."
		},
		"keywords": {
			"type": "array",
			"items": {
				"type": "string"
			},
			"description": "List of important keywords related to the key responsibilities of the class/struct/type."
		},
		"roleStereotype": {
			"type": "string",
			"description": "Role stereotype of the class/struct/type; options are supplied at runtime."
		},
		"roleStereotypeReason": {
			"type": "string",
			"description": "One-sentence explanation for the chosen role stereotype."
		}
	},
	"required": [
		"description",
		"keywords",
		"roleStereotype",
		"roleStereotypeReason"
	]
}

analyze_structure_tool = {
	"type": "function",
	"function": {
		"name": "AnalyzeStructure",
		"description": "Analyzes a software class/struct/type based on its inheritance, fields, and methods. Returns an explanation covering the key responsibilities of the structure, relevant keywords, role stereotype, and rationale for the chosen stereotype.",
		"parameters": structure_description
	}
}

component_description = {
	"$schema": "http://json-schema.org/draft-07/schema#",
	"title": "ComponentDescription",
	"type": "object",
	"properties": {
		"description": {
			"type": "string",
			"description": "Describe the functionality of the component/package in up to five sentences."
		},
		"title": {
			"type": "string",
			"description": "A noun phrase that describes the component/package."
		},
		"keywords": {
			"type": "array",
			"items": {
				"type": "string"
			},
			"description": "List of important keywords related to the core functionalities of the component/package."
		},
		"layer": {
			"type": "string",
			"description": "Architectural layer classification selected from the provided options."
		},
		"layerReason": {
			"type": "string",
			"description": "Explanation why the component/package fits the chosen layer but not others."
		}
	},
	"required": [
		"description",
		"title",
		"keywords",
		"layer",
		"layerReason"
	]
}

analyze_component_tool = {
	"type": "function",
	"function": {
		"name": "AnalyzeComponent",
		"description": "Analyzes a software component/package by examining its contents. Returns an explanation including a description of component/package responsibility, a descriptive title, a list of keywords, the selected architectural layer, and the rationale for that layer.",
		"parameters": component_description
	}
}

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
