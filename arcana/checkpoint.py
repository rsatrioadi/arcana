# checkpoint.py
import json
from threading import Lock

from arcana.custom_encoder import CustomJSONEncoder

class JSONLWriter:
	_instance = None
	_lock = Lock()

	def __new__(cls, path):
		with cls._lock:
			if cls._instance is None:
				inst = super().__new__(cls)
				inst._file = open(path, "a", buffering=1)
				cls._instance = inst
			return cls._instance

	def write(self, data: dict):
		self._file.write(json.dumps(data, cls=CustomJSONEncoder) + "\n")
		
	def flush(self):
		try:
			self._file.flush()
		finally:
			pass

def writer(path=None):
	"""
	If path is provided and writer not yet instantiated, uses it.
	Otherwise, falls back to default.
	"""
	effective = path or "checkpoints.jsonl"
	return JSONLWriter(effective)
