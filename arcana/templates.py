script_analysis = '''This is method `{op_name}` of {struct_kind} `{struct_name}`:

```java
{op_src}
```

Explain the above method on the following aspects:

{{ description: "Describe the functionality of the method in one sentence.",
  parameters: [ {{ name:..., type:..., description:... }}, ... ],
  returns: {{ type:..., description: ... }}, // In case of a constructor, consider the constructed class as the return type.
  reason: "Explain, in one sentence, the reason why the method is provided or the design rationale of the method.",
  howToUse: "Describe the usage or the expected set-up of using the method in less than 3 sentences.",
  howItWorks: "Describe the implementation details of the method in less than 5 sentences.",
  assertions: {{ preConditions: ["pre-conditions of the method", ...], postConditions: ["pre-conditions of the method", ...] }},
  layer:...,
  layerReason:...
}}

For the `layer`, fill the value with one of the following architectural layer which functionality is exhibited by the method source code:

- **Presentation Layer**: Manages the user interface, defines UI elements and behavior, displays information, responds to user input, and updates views.

- **Service Layer**: Controls the application flow, orchestrates domain operations, connects UI events with domain logic, and synchronizes domain changes with the UI.

- **Domain Layer**: Handles business logic, represents domain data and behavior, and performs necessary computations for domain operations.

- **Data Source Layer**: Interacts with databases, filesystems, hardware, messaging systems, or other data sources, performs CRUD operations, handles data conversion, and ensures data integrity.

In `layerReason`, explain why this method fits your layer of choice but not the other layers.

Respond with a well-formatted JSON object. Do not use any quote marks ("'`) within the JSON values.'''

structure_analysis = '''A Java {struct_type} `{struct_name}` specializes the following class(es) or interface(s):

{ancestors}

This {struct_type} contains the following field(s) and method(s):

Fields:

{fields}

Methods:

{methods}

Explain the above {struct_type} on the following aspects:

{{ description: "Describe the responsibility of the {struct_type} in one sentence.", 
  roleStereotype:..., 
  roleStereotypeReason:...,
  layer:...,
  layerReason:... }}

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

For the `layer`, consider the functionalities of architectural layers below:

- **Presentation Layer**: Manages the user interface, defines UI elements and behavior, displays information, responds to user input, and updates views. Typically (but not only) contains User Interfacers.

- **Service Layer**: Controls the application flow, orchestrates domain operations, connects UI events with domain logic, and synchronizes domain changes with the UI. Typically (but not only) contains Coordinators and (Application) Controllers.

- **Domain Layer**: Handles business logic, represents domain data and behavior, and performs necessary computations for domain operations. Typically (but not only) contains Information Holders, Service Providers, Structurers, Coordinators, and (Domain) Controllers.

- **Data Source Layer**: Interacts with databases, filesystems, hardware, messaging systems, or other data sources, performs CRUD operations, handles data conversion, and ensures data integrity. Typically (but not only) contains External Interfacers.

In `layerReason`, explain why this {struct_type} fits your layer of choice but not the other layers.

Respond with a well-formatted JSON object. Do not use any quote marks ("'`) within the JSON values. In the `description`, do not mention the name of the role stereotype or layer.'''

component_analysis = '''Given a Java package `{pkg_name}` containing the following classes:

{classes}

Explain the above package on the following aspects:

{{ description: "Describe the purpose of the package in one sentence.", 
  layer:...,
  layerReason:... }}

For the `layer`, consider the functionalities of architectural layers below:

- **Presentation Layer**: Manages the user interface, defines UI elements and behavior, displays information, responds to user input, and updates views. Typically (but not only) contains User Interfacers.

- **Service Layer**: Controls the application flow, orchestrates domain operations, connects UI events with domain logic, and synchronizes domain changes with the UI. Typically (but not only) contains Coordinators and (Application) Controllers.

- **Domain Layer**: Handles business logic, represents domain data and behavior, and performs necessary computations for domain operations. Typically (but not only) contains Information Holders, Service Providers, Structurers, Coordinators, and (Domain) Controllers.

- **Data Source Layer**: Interacts with databases, filesystems, hardware, messaging systems, or other data sources, performs CRUD operations, handles data conversion, and ensures data integrity. Typically (but not only) contains External Interfacers.

In `layerReason`, explain why this package fits your layer of choice but not the other layers.

Respond with a well-formatted JSON object. Do not use any quote marks ("'`) within the JSON values. In the `description`, do not mention the name of the layer.'''
