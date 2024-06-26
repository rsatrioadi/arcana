import argparse
import configparser
import json
import sys

from arcana import cli
from arcanalib import Pipeline, Graph

def main():
	parser = argparse.ArgumentParser(description="Perform architectural analyses on software knowledge graphs.")
	parser.add_argument('--version', '-v', action='version', version='arcana 0.1')

	parser.add_argument('command', choices=['llm', 'metrics'], help='Command to execute -- join with a dash to make a pipeline')
	parser.add_argument('--config', '-c', type=str, default='config.ini',
						help='Path to the configuration file (default: config.ini)')
	parser.add_argument('--verbose', action='store_true', help='Enable verbose output')
	parser.add_argument('--dry-run', action='store_true', help='Do not actually call the LLM API, only print prompts')

	args = parser.parse_args()

	config_parser = configparser.ConfigParser()
	config_parser.read(args.config)
	config = {section: dict(config_parser.items(section))
			  for section in config_parser.sections()}

	if 'input' not in config['project'] or config['project']['input'] == 'stdin':
		data = sys.stdin.read()
	else:
		with open(config['project']['input'], 'r', encoding="utf-8") as file:
			data = json.load(file)

	filters = {
		'llm': cli.LLMFilter,
		'metrics': cli.MetricsFilter,
	}
 
	commands = args.command.split('-')
	graph = Graph(data)

	# Dispatch the command
	if commands:
		pipeline = Pipeline(*[
			filters[command](config)
   			for command in commands 
			if command in filters]
		)
		result = pipeline.process(graph)
		if 'output' not in config['project'] or config['project']['output'] == 'stdout':
			# TODO write the graph to stdout
			pass
		else:
			# TODO write the graph to a file at config['project']['output']
			pass

	else:
		parser.print_help()
		sys.exit(1)


if __name__ == "__main__":
	main()
