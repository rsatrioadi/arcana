# ![Arcana](arcana.svg)

**arcana** (*noun*):

1. secret or arcane knowledge, acquired or understood by only a few.
2. software **arc**hitecture **ana**lyses.

Arcana performs various analyses on a software architectural knowledge base represented in a knowledge graph.

## Directions of use

### Installing requirements

```bash
pip install -r requirements.txt
```

### The commands

To run Arcana, type in:

```bash
python -m arcana [--config CONFIG] [--use-seeder] command
```

(It is recommended to redirect stderr to a log file by adding `2> log.txt` at the end of the command line.)

`CONFIG` specifies the path to the configuration file. The default path is `config.ini`.  See `config.ini.example` and read further for more information about the configuration.

The `command` can be any of the following list, and they can be executed in a pipeline by specifying the command names in succession, separated by a dash (`-`), e.g., `python -m arcana metrics-llm` will first execute the `metrics` command on the input graph, and then the `llm` command on the graph produced by the `metrics` command.

- `metrics`: computes metrics for the graph nodes and add the computed metrics into the node's properties. Currently, the only supported metrics is [*dependency profile*](https://doi.org/10.1109/ICSM.2011.6080827).
- `llm`: uses a large language model API (specified in the `llm` section of the configuration file) to add properties to the graph nodes, including:

	- `description`: a one-sentence summary of *packages*, *classes*, and *methods*/*constructors*.
	- `roleStereotype`: a classification of *classes* into one of [Wirfs-Brock's role stereotypes](https://wirfs-brock.com/PDFs/Characterizing%20Classes.pdf).
	- `layer`: a classification of *packages*, *classes*, and *methods*/*constructors* into one of the following architectural layers: `Presentation Layer`, `Service Layer`, `Domain Layer`, or `Data Source Layer`.

### Input

The “normal” input for Arcana is a knowledge graph as described in [this paper](https://doi.org/10.1109/MSR59073.2023.00029), in a particular JSON format. This input is specified in the configuration file.

```ini
[project]
name=<project name here>
desc=<project description here>
input=<specify input here>
...
```

`input` can either be a path to a JSON file containing the graph data, or `stdin` to read the JSON text from standard input. This is useful, e.g., for when you want to use the output of another program that produces the graph data.

#### Using a seeder

If you don’t have a graph ready, i.e., you want to specify a source directory as an input, you can use a seeder by passing `--use-seeder` as a command line argument to Arcana. At this time, the only seeder supported is [javapers](https://github.com/rsatrioadi/javapers), the configuration for which can be seen in the `seeder` section of the configuration file (make sure to specify the correct path to the java executable and javapers JAR file):

```ini
[seeder]
command={javaexe} -jar {jarfile} -i {input} -a -n {name} -f json
javaexe=./javapers/jdk-17.0.11+9-jre/bin/java.exe
jarfile=./javapers/javapers-1.1.2-jar-with-dependencies.jar
```

In such case, the `input` field in the `project` section is a directory that contains the Java source files. You can specify several directories by separating each directory with a plus sign (`+`), e.g.:

```ini
[project]
input=/path/to/src1/+/path/to/src2/
...
```

### Output

Similar to input, output can be written to a file or standard output (`stdout`), based on the `output` configuration in the `project` section.

```ini
[project]
output=<specify output here>
...
```

The resulting output, in the same format as the input graph (i.e., a particular JSON format), can be visualized in [ClassViz](https://rsatrioadi.github.io/classviz/). This visualizer is exploratory in nature and therefore unstable. A more mature visualizer is in the works.
