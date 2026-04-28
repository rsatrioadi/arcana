import json
import logging
from threading import Lock

from arcana.custom_encoder import CustomJSONEncoder

logger = logging.getLogger(__name__)


class JSONLWriter:
    _instance = None
    _lock = Lock()

    def __new__(cls, path: str, append: bool = False):
        with cls._lock:
            if cls._instance is None:
                inst = super().__new__(cls)
                mode = "a" if append else "w"
                inst._file = open(path, mode, buffering=1)
                cls._instance = inst
            return cls._instance

    def write(self, data: dict):
        with self._lock:
            self._file.write(json.dumps(data, cls=CustomJSONEncoder) + "\n")

    def flush(self):
        with self._lock:
            try:
                self._file.flush()
            except Exception:
                pass


_writer_path: str = "checkpoints.jsonl"
_writer_append: bool = False


def configure_writer(path: str, append: bool = False):
    """Call once before the first writer() use to set path and open mode."""
    global _writer_path, _writer_append
    _writer_path = path
    _writer_append = append


def writer(path=None):
    effective = path or _writer_path
    return JSONLWriter(effective, _writer_append)


# ---------------------------------------------------------------------------
# Checkpoint loading (for resume)
# ---------------------------------------------------------------------------

def load_checkpoint(path: str, graph):
    """Load a JSONL checkpoint file into *graph*, applying node properties and edges.

    Handles both node entries  {"data": {"id": ..., "labels": [...], "properties": {...}}}
    and edge entries           {"data": {"id": ..., "source": ..., "target": ..., "label": ..., "properties": {...}}}.
    """
    loaded_nodes = 0
    loaded_edges = 0
    try:
        with open(path, encoding="utf-8") as f:
            for lineno, line in enumerate(f, 1):
                line = line.strip()
                if not line:
                    continue
                try:
                    entry = json.loads(line).get('data', {})
                except json.JSONDecodeError as e:
                    logger.warning("Skipping malformed checkpoint line %d: %s", lineno, e)
                    continue

                eid = entry.get('id')
                if not eid:
                    continue

                if 'source' in entry and 'target' in entry and 'label' in entry:
                    # Edge entry
                    graph.add_edge(
                        entry['source'],
                        entry['target'],
                        entry['label'],
                        **entry.get('properties', {}),
                    )
                    loaded_edges += 1
                else:
                    # Node entry
                    props = entry.get('properties', {})
                    if eid in graph.nodes:
                        graph.nodes[eid].properties.update(props)
                    else:
                        graph.add_node(eid, *entry.get('labels', []), **props)
                    loaded_nodes += 1

    except FileNotFoundError:
        logger.warning("Checkpoint file not found: %s", path)
        return

    logger.info("Loaded checkpoint %s: %d nodes, %d edges.", path, loaded_nodes, loaded_edges)
