import json
import subprocess
import sys

from arcanalib.graph import Graph
from arcanalib.pipefilter import Seeder


class CLISeeder(Seeder):

	def __init__(self, command) -> None:
		"""
		Initialize the seeder with a command.

		:param command: The command to be executed.
		"""
		self.command = command

	def generate(self) -> Graph:
		"""
		Execute the command, parse the JSON output into a dict, and pass the dict to the Graph constructor.

		:return: The generated Graph object.
		"""
		process = subprocess.run(self.command, capture_output=True, text=True, encoding="utf-8", check=True)
		if process.stderr:
			sys.stderr.write(process.stderr)
		output_dict = json.loads(process.stdout)
		return Graph(output_dict)