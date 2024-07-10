# The Architecture of Arcana

Arcana is a _pipe-and-filter_ application.
Each command available in the command line is a _filter_, i.e., it extends from the `arcanalib.pipefilter.Filter` class.
Each filter takes graph data as an input (an instance of `arcanalib.graph.Graph`) and outputs the same type of data, except for filters that are subclasses of `arcanalib.pipefiler.EndFilter`.
These filters are meant to be the end of the pipeline, i.e., if the pipeline encounters an `EndFilter`, it will ignore any subsequent filters. End filters are useful if you want to convert the final graph data into another format, e.g., one that is required by a particular visualization tool.

A _pipeline_ (an instance of `arcanalib.pipefilter.Pipeline`) composes these filters, receives an input, and pass the input through the filters in succession.
The input for a pipeline can either be a `Graph` or a seeder (an instance of `arcanalib.pipefilter.Seeder`).
When the input is a seeder, the pipeline will first use the seeder to generate the graph data that will then be passed through the filters.

## Available Seeders and Filters

### Seeder: `CLISeeder`

This basically takes a command that one would execute from a command-line shell, runs it from within the application, and uses the output of that command as the graph data.

### Filter: `MetricsFilter`

This filter computes metrics for the graph nodes and adds the computed metrics to the node's properties. 
Currently, the only supported metric is the [*dependency profile*](https://doi.org/10.1109/ICSM.2011.6080827), which applies to classes.
Dependency profile describes whether a class depends on classes from another package, is being used by classes in another package, both, or none.
This metrics is stored in the property `dependencyProfile` of class nodes.

### Filter: `LLMFilter`

This command uses a large language model API (specified in the `llm` section of the configuration file) to analyze and add properties to the graph nodes.
The additional properties added are described below.

#### Descriptions

These are summaries generated for methods, method parameters, classes, and packages.
The method summaries are generated with consideration of [“intents”](https://doi.org/10.1145/3597503.3608134), i.e, they describe what the paper defines as the “what” (`description`), “why” (`reason`), “how-to-use” (`howToUse`), “how-it-is-done” (`howItWorks`), and “property” (`assertions`).
Additionally, the filter also generates description of the method's return value in the property `returns`.

The summaries for classes and packages are generated using the “summary of summaries” or [hierarchical summarization approach](https://doi.org/10.1109/ICoDSE59534.2023.10292037).

#### Class Role Stereotypes

This is a classification of *classes* into one of [Wirfs-Brock's role stereotypes](https://wirfs-brock.com/PDFs/Characterizing%20Classes.pdf).
The role stereotypes were introduced as design-time concept, but [classifying implementation classes into stereotypes can help in making sense of the structure of the software system](https://doi.org/10.1016/j.jss.2022.111296).

This information is stored in the `roleStereotype` property of class nodes, and has the following possible values:

- `Information Holder`
- `Service Provider`
- `Structurer`
- `Controller`
- `Coordinator`
- `User Interfacer`
- `External Interfacer`
- `Internal Interfacer`

#### Architectural Layers

The filter takes the descriptions of *packages*, *classes*, and *methods*/*constructors* and matches them with the purported functionalities of the following architectural layers: `Presentation Layer`, `Service Layer`, `Domain Layer`, or `Data Source Layer`.
The classification method is based on the [_deductive software architecture recovery_ approach](https://doi.org/10.1145/3639476.3639776).

This information is stored in the `layer` property of the nodes in question.