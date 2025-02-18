analyze_script_tool = {
    "type": "function",
    "function": {
        "name": "AnalyzeScript",
        "description": "Analyzes a program script given its source code and context. Returns an explanation covering functionality, parameters, return value, design rationale, usage, implementation details, assertions, stereotype, and architectural layer classification.",
        "parameters": {
            "type": "object",
            "properties": {
                "description": {
                    "type": "string",
                    "description": "One-sentence description of the script functionality."
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
                    "description": "List of pre-conditions for the method."
                },
                "postConditions": {
                    "type": "array",
                    "items": {
                        "type": "string"
                    },
                    "description": "List of post-conditions for the method."
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
                    "description": "Design stereotype of the method."
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
                    "description": "Explanation why the method fits the chosen architectural layer but not others."
                }
            },
            "required": [
                "description",
                "parameters",
                "returns",
                "howToUse",
                "howItWorks",
                "preConditions",
                "postConditions",
                "stereotype",
                "stereotypeReason",
                "layer",
                "layerReason"
            ]
        }
    }
}

analyze_structure_tool = {
    "type": "function",
    "function": {
        "name": "AnalyzeStructure",
        "description": "Analyzes a software structure based on its inheritance, fields, and methods. Returns an explanation covering the key responsibilities of the structure, relevant keywords, role stereotype, and rationale for the chosen stereotype.",
        "parameters": {
            "type": "object",
            "properties": {
                "description": {
                    "type": "string",
                    "description": "Up to three sentences describing the key responsibilities of the structure."
                },
                "keywords": {
                    "type": "array",
                    "items": {
                        "type": "string"
                    },
                    "description": "List of keywords relevant to the structure."
                },
                "roleStereotype": {
                    "type": "string",
                    "enum": [
                        "Information Holder",
                        "Service Provider",
                        "Structurer",
                        "Controller",
                        "Coordinator",
                        "User Interfacer",
                        "External Interfacer",
                        "Internal Interfacer"
                    ],
                    "description": "The role stereotype of the structure: \
                      **Information Holder** is responsible for knowing facts and providing information to other objects. POJOs, Java Beans, and enumerations are usually information holders. \
                      **Service Provider** is responsible for handling requests and performing specific services. It usually implements a specific interface with a small number of methods. Concrete strategies are service providers. \
                      **Structurer** is responsible for managing relationships and constraints among related things. It is usually a collection or mapping of some sort, i.e., a subclass of a List, Set, Map, etc. \
                      **Controller** is responsible for making decisions, directing the work of others, and handling important events. It directs the flow of the application or business process. \
                      **Coordinator** is responsible for managing the actions of a group of workers and facilitating communication and work of other objects. It delegates requests to other objects. Very abstract classes and interfaces might be coordinators as they delegate the work to subclasses. \
                      **User Interfacer** is responsible for transmitting user requests for action or display/render information that can be updated. It handles interactions with users. \
                      **External Interfacer** is responsible for loading and storing information from/to external services, including database systems, web services, filesystems, hardware, etc. \
                      **Internal Interfacer** is responsible for interfacing between two subsystems. It may bundle together information of requests from a group of objects to be sent to another object. Abstract adapters, bridges, facades, and proxies are internal interfacers."
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
    }
}

analyze_component_tool = {
    "type": "function",
    "function": {
        "name": "AnalyzeComponent",
        "description": "Analyzes a software component by examining its contents. Returns an explanation including a description of component functionality, a descriptive title, a list of keywords, the selected architectural layer, and the rationale for that layer.",
        "parameters": {
            "type": "object",
            "properties": {
                "description": {
                    "type": "string",
                    "description": "Describe the functionality of the package in up to five sentences (do not mention the layer name)."
                },
                "title": {
                    "type": "string",
                    "description": "A noun phrase that describes the package."
                },
                "keywords": {
                    "type": "array",
                    "items": {
                        "type": "string"
                    },
                    "description": "List of keywords relevant to the package."
                },
                "layer": {
                    "type": "string",
                    "description": "Architectural layer classification selected from the provided options."
                },
                "layerReason": {
                    "type": "string",
                    "description": "Explanation why the package fits the chosen layer but not others."
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
