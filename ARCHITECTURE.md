# The Architecture of Arcana

Arcana is a _pipe-and-filter_ application.
Each command available in the command line is a _filter_, i.e., it extends from the `arcanalib.pipefilter.Filter` class.
Each filter takes graph data as an input (an instance of `arcanalib.graph.Graph`) and outputs the same type of data, except for filters that are subclasses of `arcanalib.pipefiler.EndFilter`.
These filters are meant to be the end of the pipeline, i.e., if the pipeline encounters an `EndFilter`, it will ignore any subsequent filters. End filters are useful if you want to convert the final graph data into another format, e.g., one that is required by a particular visualization tool.

A _pipeline_ (an instance of `arcanalib.pipefilter.Pipeline`) composes this filters, receives an input, and pass the input through the filters in succession.
The input for a pipeline can either be a `Graph` or a seeder (an instance of `arcanalib.pipefilter.Seeder`).
When the input is a seeder, the pipeline will first use the seeder to generate the graph data that will then be passed through the filters.

## Available Seeders and Filters

### Seeder: `CLISeeder`

### Filter: `MetricsFilter`

This filter computes metrics for the graph nodes and adds the computed metrics to the node's properties. 
Currently, the only supported metric is the [*dependency profile*](https://doi.org/10.1109/ICSM.2011.6080827), which applies to classes.

### Filter: `LLMFilter`