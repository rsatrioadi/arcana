import json
import re
from typing import Any, Dict, TextIO

from arcana.custom_encoder import CustomJSONEncoder
from arcanalib.graph import Node

def remove_author(s: str) -> str:
	return "\n".join(line.strip() for line in s.splitlines() if '@author' not in line)

_JAVA_COMMENT_RE = re.compile(r"(//.*?$)|(/\*.*?\*/)", flags=re.MULTILINE | re.DOTALL)

def remove_java_comments(java_source: str) -> str:
	return _JAVA_COMMENT_RE.sub("", java_source).strip()

def sentence(s: str) -> str:
	"""
	Capitalize the first letter of a string and ensure it ends with a period.

	Args:
		s (str): The input string.

	Returns:
		str: The formatted string.
	"""
	if not s:
		return ""
	t = s.strip()
	if not t:
		return ""
	if t[-1] in '.?!…~–—':
		return f'{t[0].upper()}{t[1:]}'
	return f'{t[0].upper()}{t[1:]}.'

def lower_first(s: str) -> str:
	"""
	Lowercase the first character of a string.

	Args:
		s (str): The input string.

	Returns:
		str: The string with the first character lowercased.
	"""
	return s[0].lower() + s[1:] if s else s

def prettify_json(obj: dict) -> str:
	"""
	Convert a dictionary to a pretty-printed JSON string.

	Args:
		obj (dict): The input dictionary.

	Returns:
		str: The pretty-printed JSON string.
	"""
	return json.dumps(obj, indent=2)

def write_jsonl(file: TextIO, obj: Any) -> None:
	file.write(json.dumps(obj, cls=CustomJSONEncoder) + '\n')

def find_first_valid_json(text: str) -> str:
	"""
	Finds the first valid JSON substring in the given text using a stack-based approach.

	It scans the text from left to right, and when it encounters a '{', it tracks the balanced
	braces until a complete JSON object is formed. Once a candidate is found, it attempts to parse
	it with json.loads(). If parsing succeeds, that candidate is returned immediately.

	Args:
		text (str): The input string that may contain a JSON object.

	Returns:
		str: The first valid JSON substring found, or an empty string if none is found.
	"""
	n = len(text)
	for i in range(n):
		if text[i] == '{':
			stack = 0
			for j in range(i, n):
				if text[j] == '{':
					stack += 1
				elif text[j] == '}':
					stack -= 1
					if stack == 0:
						candidate = text[i:j + 1]
						try:
							json.loads(candidate)
							return candidate
						except json.JSONDecodeError:
							# If this candidate isn't valid JSON, break and continue scanning.
							break
	return ""

def simplify_name(name):
	if '(' in name and name.endswith(')'):
		prefix, params = name.split('(', 2)
		params = [param.split('.')[-1].split('$')[-1] for param in params.split(')', 1)[0].split(',')]
		return prefix + '(' + ','.join(params) + ')'
	else:
		return name

def merge_node_properties(dict1: Dict[str, Node], dict2: Dict[str, Node], simplify_names=False):
	for id2, obj2 in dict2.items():

		matched_obj = None
		if id2 in dict1 and set(dict1[id2].labels) & set(obj2.labels):
			matched_obj = dict1[id2]

		elif simplify_names:

			dict1_name_remap = {simplify_name(key): key for key in dict1 if
								{'Script', 'Operation', 'Constructor'} & set(dict1[key].labels)}

			if id2 in dict1_name_remap and set(dict1[dict1_name_remap[id2]].labels) & set(obj2.labels):
				matched_obj = dict1[dict1_name_remap[id2]]

		if matched_obj:
			# sys.stderr.write(f"{id2}->{matched_obj['id']}\n")
			# Merge properties from obj2 into matched_obj
			matched_obj.properties.update(obj2.properties)
		else:
			# sys.stderr.write(f"{id2}->None\n")
			pass


