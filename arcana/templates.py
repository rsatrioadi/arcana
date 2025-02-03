script_analysis = '''Consider a project {project_name}, {project_desc}. This is method `{op_name}` of {struct_kind} `{struct_name}`:

```java
{op_src}
```

The method may use the following other methods:

{other_ops}

Explain the above method on the following aspects:

{{ description: "Describe the functionality of the method in one sentence.",
  parameters: [ {{ name:..., type:..., description:... }}, ... ], // empty list if there is no parameter
  returns: "Describe the returned object/value in one sentence. (In case of a constructor, consider the newly created instance as the return value.)"
  reason: "Explain the reason why the method is provided or the design rationale of the method, in one sentence.",
  howToUse: "Describe the usage or the expected set-up of using the method, in less than 3 sentences.",
  howItWorks: "Describe the implementation details of the method, in less than 5 sentences.",
  assertions: {{ preConditions: ["pre-conditions of the method", ...], postConditions: ["pre-conditions of the method", ...] }},
  stereotype: one of "Accessor", "Mutator", "Creational", "Collaborational", or "Other",
  stereotypeReason: "Explain the rationale of the stereotype choice",
  layer:...,
  layerReason:...
}}

For the `layer`, fill the value with one of the following architectural layer which functionality is exhibited by the method source code:

{layers}

In `layerReason`, explain why this method fits your layer of choice but not the other layers.

Respond with a well-formatted JSON object. Do not use any quote marks ("'`) within the JSON values.'''

structure_analysis = '''Consider a project {project_name}, {project_desc}. A {struct_type} `{struct_name}` specializes the following class(es) or interface(s):

{ancestors}

This {struct_type} contains the following field(s) and method(s):

Fields:

{fields}

Methods:

{methods}

Explain the above {struct_type} on the following aspects:

{{ description: "Describe the key responsibilities of the {struct_type} in up to three sentences.", 
  keywords: ["list", "of", "keywords", "relevant", "to", "the", "{struct_type}"], // try to have nouns as well as verb keywords
  roleStereotype:..., 
  roleStereotypeReason:... }}

When describing the responsibilities, consider that a responsibility can be fulfilled by a group of methods within the {struct_type}. In other words, an intermediate step for describing the {struct_type} is to cluster its methods into a few method responsibility-type.

For the `roleStereotype`, fill the value with one of the following role stereotypes which responsibility is exhibited by the {struct_type}:

- **Information Holder** is responsible for knowing facts and providing information to other objects. POJOs and Java Beans are usually information holders.
- **Service Provider** is responsible for handling requests and performing specific services. It usually implements a specific interface with a small number of methods. Concrete strategies are service providers.
- **Structurer** is responsible for managing relationships and constraints among related things. It is usually a collection or mapping of some sort.
- **Controller** is responsible for making decisions, directing the work of others, and handling important events. It directs the flow of the application or business process.
- **Coordinator** is responsible for managing the actions of a group of workers and facilitating communication and work of other objects. It delegates requests to other objects. Very abstract classes and interfaces might be coordinators as they delegate the work to subclasses.
- **User Interfacer** is responsible for transmitting user requests for action or display/render information that can be updated. It handles interactions with users.
- **External Interfacer** is responsible for loading and storing information from/to external services, including database systems, web services, filesystems, hardware, etc.
- **Internal Interfacer** is responsible for interfacing between two subsystems. It may bundle together information of requests from a group of objects to be sent to another object. Abstract adapters, bridges, facades, and proxies are internal interfacers.

In `roleStereotypeReason`, explain why this {struct_type} fits your stereotype of choice but not the other stereotypes.

Respond with a well-formatted JSON object. Do not use any quote marks ("'`) within the JSON values. In the `description`, do not mention the name of the role stereotype or layer.'''

component_analysis = '''Consider a project {project_name}, {project_desc}. Given a package `{pkg_name}` containing the following classes:

{classes}

and the following subpackages:

{packages}

Explain the above package on the following aspects:

{{ description: "Describe the functionality of the package in up to five sentences.",
  title: "A Noun Phrase that Describes the Package",
  keywords: ["list", "of", "keywords", "relevant", "to", "the", "package"], // try to have nouns as well as verb keywords
  layer:...,
  layerReason:... }}

For the `layer`, consider the functionalities of architectural layers below:

{layers}

In `layerReason`, explain why this package fits your layer of choice but not the other layers.

Respond with a well-formatted JSON object. Do not use any quote marks ("'`) within the JSON values. In the `description`, do not mention the name of the layer.'''

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
