"""Read the shared skill revision without changing its timestamp."""
import json
from pathlib import Path


def metadata():
    return json.loads((Path(__file__).resolve().parents[1] / 'version.json').read_text())
