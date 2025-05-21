import os
from typing import Any, Dict, List, Tuple

def layers_to_list(d: Dict[str, Any]) -> List[Tuple[str, str]]:
	result = []
	i = 1
	while True:
		name_key, desc_key = f"layer{i}name", f"layer{i}desc"
		if name_key not in d or desc_key not in d:
			break
		result.append((d[name_key], d[desc_key]))
		i += 1
	return result

from collections import OrderedDict
from typing import Any, Dict, OrderedDict as OD

def layers_to_ordereddict(d: Dict[str, Any]) -> OD[str, str]:
    layers: OD[str, str] = OrderedDict()
    i = 1
    while True:
        name_key = f"layer{i}name"
        desc_key = f"layer{i}desc"
        if name_key not in d or desc_key not in d:
            break
        layers[d[name_key]] = d[desc_key]
        i += 1
    return layers


class StopProcessing(Exception):
	"""Raised when a stop signal is detected."""
	pass

def check_stop() -> None:
	if os.path.exists('stop'):
		raise StopProcessing("Stop file detected, halting processing.")
