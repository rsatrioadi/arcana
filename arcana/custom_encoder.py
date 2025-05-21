import json

class CustomJSONEncoder(json.JSONEncoder):
	def default(self, obj):
		if isinstance(obj, set):
			# Convert set to list
			return list(obj)
		# Call the default method for other types
		return super().default(obj)