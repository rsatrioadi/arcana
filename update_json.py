#!/usr/bin/env python3
import sys
import json

if len(sys.argv) != 3:
    sys.exit(f"Usage: {sys.argv[0]} <input_json_file> <input_jsonl_file>")

json_file = sys.argv[1]
jsonl_file = sys.argv[2]

with open(json_file, "r") as f:
    data = json.load(f)

elements = data.get("elements", {})
nodes = elements.get("nodes", [])
edges = elements.get("edges", [])

node_map = {node["data"]["id"]: node for node in nodes if "data" in node and "id" in node["data"]}
edge_map = {}
for edge in edges:
    edata = edge.get("data", {})
    if all(k in edata for k in ("source", "target", "label")):
        key = (edata["source"], edata["target"], edata["label"])
        edge_map[key] = edge

with open(jsonl_file, "r") as f:
    for line in f:
        line = line.strip()
        if not line:
            continue
        entry = json.loads(line)
        edata = entry.get("data", {})
        if all(k in edata for k in ("source", "target", "label")):
            key = (edata["source"], edata["target"], edata["label"])
            new_props = edata.get("properties", {})
            if key in edge_map:
                curr_props = edge_map[key]["data"].get("properties", {})
                curr_props.update(new_props)
                edge_map[key]["data"]["properties"] = curr_props
            else:
                edges.append(entry)
                edge_map[key] = entry
        elif "id" in edata:
            node_id = edata["id"]
            new_props = edata.get("properties", {})
            if node_id in node_map:
                curr_props = node_map[node_id]["data"].get("properties", {})
                curr_props.update(new_props)
                node_map[node_id]["data"]["properties"] = curr_props
            else:
                nodes.append(entry)
                node_map[node_id] = entry

print(json.dumps(data, indent=4))
