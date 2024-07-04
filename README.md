# ![Arcana](arcana.svg)

**arcana** (*noun*):

1. secret or arcane knowledge, acquired or understood by only a few.
2. software **arc**hitecture **ana**lyses.

Arcana performs various analyses on a software architectural knowledge base represented in a knowledge graph.

## Usage Instructions

### Installing Dependencies

To install the necessary dependencies, run the following command:

```bash
pip install -r requirements.txt
```

### Running Arcana

To execute Arcana, use the following command:

```bash
python -m arcana [--config CONFIG] [--use-seeder] command
```

We recommend redirecting stderr to a log file by appending `2> log.txt` to the end of the command line.

`CONFIG` is an optional argument that specifies the path to the configuration file. If not provided, the default path `config.ini` is used. Refer to `config.ini.example` for more information about the configuration.

The `command` argument can be one of the following:

- `metrics`: This command computes metrics for the graph nodes and adds the computed metrics to the node's properties. Currently, the only supported metric is the [*dependency profile*](https://doi.org/10.1109/ICSM.2011.6080827).
- `llm`: This command uses a large language model API (specified in the `llm` section of the configuration file) to add properties to the graph nodes, including:

	- `description`: A one-sentence summary of *packages*, *classes*, and *methods*/*constructors*.
	- `roleStereotype`: A classification of *classes* into one of [Wirfs-Brock's role stereotypes](https://wirfs-brock.com/PDFs/Characterizing%20Classes.pdf).
	- `layer`: A classification of *packages*, *classes*, and *methods*/*constructors* into one of the following architectural layers: `Presentation Layer`, `Service Layer`, `Domain Layer`, or `Data Source Layer`.

Commands can be chained together in a pipeline by specifying them in succession, separated by a dash (`-`). For example, `python -m arcana metrics-llm` will first execute the `metrics` command on the input graph, and then the `llm` command on the graph produced by the `metrics` command.

### Input

Arcana typically takes as input a knowledge graph as described in [this paper](https://doi.org/10.1109/MSR59073.2023.00029), in a specific JSON format. This input is specified in the configuration file.

```ini
[project]
name=<project name here>
desc=<project description here>
input=<specify input here>
...
```

The `input` field can either be a path to a JSON file containing the graph data, or `stdin` to read the JSON text from standard input. This is useful when you want to use the output of another program that produces the graph data.

#### Using a Seeder

If you don’t have a graph ready and want to specify a source directory as an input, you can use a seeder by passing `--use-seeder` as a command line argument to Arcana. Currently, the only supported seeder is [javapers](https://github.com/rsatrioadi/javapers). The configuration for javapers can be found in the `seeder` section of the configuration file. Ensure that you specify the correct path to the Java executable and the javapers JAR file:

```ini
[seeder]
command={javaexe} -jar {jarfile} -i {input} -a -n {name} -f json
javaexe=./javapers/jdk-17.0.11+9-jre/bin/java.exe
jarfile=./javapers/javapers-1.1.2-jar-with-dependencies.jar
```

In this case, the `input` field in the `project` section should be a directory that contains the Java source files. You can specify multiple directories by separating each directory with a plus sign (`+`), like so:

```ini
[project]
input=/path/to/src1/+/path/to/src2/
...
```

### Output

Similar to the input, the output can be written to a file or to standard output (`stdout`), based on the `output` configuration in the `project` section.

```ini
[project]
output=<specify output here>
...
```

The resulting output, in the same format as the input graph (i.e., a specific JSON format), can be visualized in [ClassViz](https://rsatrioadi.github.io/classviz/). Please note that ClassViz is exploratory in nature and may be unstable. A more mature visualizer is currently under development.
