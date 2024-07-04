# ![Arcana](arcana.svg)

**arcana** (*noun*):

1. Secret or arcane knowledge, acquired or understood by only a few.
2. Software **arc**hitecture **ana**lyses.

Arcana performs various analyses on a software architectural knowledge base represented in a knowledge graph.

## Directions for Use

### Installing Requirements

```bash
pip install -r requirements.txt
```

### Commands

To run Arcana, use the following command:

```bash
python -m arcana [--config CONFIG] [--use-seeder] command
```

(It is recommended to redirect stderr to a log file by adding `2> log.txt` at the end of the command line.)

`CONFIG` specifies the path to the configuration file. The default path is `config.ini`. See `config.ini.example` and read further for more information about the configuration.

The `command` can be any of the following, and they can be executed in a pipeline by specifying the command names in succession, separated by a dash (`-`). For example, `python -m arcana metrics-llm` will first execute the `metrics` command on the input graph, and then the `llm` command on the graph produced by the `metrics` command.

- `metrics`: Computes metrics for the graph nodes and adds the computed metrics to the node's properties. Currently, the only supported metric is the [*dependency profile*](https://doi.org/10.1109/ICSM.2011.6080827).
- `llm`: Uses a large language model API (specified in the `llm` section of the configuration file) to add properties to the graph nodes, including:

	- `description`: A one-sentence summary of *packages*, *classes*, and *methods*/*constructors*.
	- `roleStereotype`: A classification of *classes* into one of [Wirfs-Brock's role stereotypes](https://wirfs-brock.com/PDFs/Characterizing%20Classes.pdf).
	- `layer`: A classification of *packages*, *classes*, and *methods*/*constructors* into one of the following architectural layers: `Presentation Layer`, `Service Layer`, `Domain Layer`, or `Data Source Layer`.

### Input

The canonical input for Arcana is a knowledge graph as described in [this paper](https://doi.org/10.1109/MSR59073.2023.00029), in a specific JSON format. This input is specified in the configuration file.

```ini
[project]
name=<project name here>
desc=<project description here>
input=<specify input here>
...
```

`input` can either be a path to a JSON file containing the graph data, or `stdin` to read the JSON text from standard input. This is useful, for example, when you want to use the output of another program that produces the graph data.

#### Using a Seeder

If you don’t have a graph ready and want to specify a source directory as an input, you can use a seeder by passing `--use-seeder` as a command line argument to Arcana. Currently, the only supported seeder is [javapers](https://github.com/rsatrioadi/javapers). The configuration for javapers can be found in the `seeder` section of the configuration file. Make sure to specify the correct path to the Java executable and javapers JAR file:

```ini
[seeder]
command={javaexe} -jar {jarfile} -i {input} -a -n {name} -f json
javaexe=./javapers/jdk-17.0.11+9-jre/bin/java.exe
jarfile=./javapers/javapers-1.1.2-jar-with-dependencies.jar
```

In this case, the `input` field in the `project` section is a directory that contains the Java source files. You can specify several directories by separating each directory with a plus sign (`+`), for example:

```ini
[project]
input=/path/to/src1/+/path/to/src2/
...
```

### Output

Similar to input, the output can be written to a file or standard output (`stdout`), based on the `output` configuration in the `project` section.

```ini
[project]
output=<specify output here>
...
```

The resulting output, in the same format as the input graph (i.e., a specific JSON format), can be visualized in [ClassViz](https://rsatrioadi.github.io/classviz/). This visualizer is exploratory in nature and therefore unstable. A more mature visualizer is in development.
