import argparse
import configparser
import json
import sys

from arcana.filters import CLISeeder, MetricsFilter, LLMFilter, MergeFilter
from arcanalib.graph import Graph
from arcanalib.pipefilter import Pipeline


def main():
	parser = argparse.ArgumentParser(description="Perform architectural analyses on software knowledge graphs.")
	parser.add_argument('--version', '-v', action='version', version='arcana 0.1')

	parser.add_argument(
		'command', type=str,
		help='Command to execute: metrics, llm, merge -- join with a dash to make a pipeline'
	)
	parser.add_argument(
		'--config', '-c', type=str, default='config.ini',
		help='Path to the configuration file (default: config.ini)'
	)
	parser.add_argument(
		'--use-seeder', '-s', action='store_true',
		help='Get graph data from seeder instead of file or stdin'
	)
	# parser.add_argument('--verbose', action='store_true', help='Enable verbose output')
	# parser.add_argument('--dry-run', action='store_true', help='Do not actually call the LLM API, only print prompts')

	args = parser.parse_args()

	config_parser = configparser.ConfigParser()
	config_parser.read(args.config)
	config = {
		section: dict(config_parser.items(section))
		for section in config_parser.sections()
	}

	config['args'] = vars(args)

	if args.use_seeder:
		data = CLISeeder(config['seeder']['command'].format(**{**config['project'], **config['seeder']}))
	elif ('input' not in config['project']) or (config['project']['input'] == 'stdin'):
		data = Graph(json.loads(sys.stdin.read()))
	else:
		with open(config['project']['input'], 'r', encoding="utf-8") as file:
			data = Graph(json.load(file))

	filters = {
		'llm': LLMFilter,
		'metrics': MetricsFilter,
		'merge': MergeFilter
	}

	commands = args.command.split('-')

	if commands:
		pipeline = Pipeline(*[
			filters[command](config)
			for command in commands
			if command in filters]
		)
		result = pipeline.process(data)
		if ('output' not in config['project']) or (config['project']['output'] == 'stdout'):
			print(str(result))
		else:
			with open(config['project']['output'], 'w') as json_file:
				json_file.write(str(result))
	else:
		parser.print_help()
		sys.exit(1)


if __name__ == "__main__":
	main()
