"""Capture the explicit curation successor without changing adoption's loader."""

import types
from pathlib import Path
from typing import Any

ENTRY = "mediaingredientmech.curate.curation_successor"
LOADER = "src/mediaingredientmech/curate/curation_successor_producer.py"
BASE = "src/mediaingredientmech/curate/adoption_producer.py"


def load(root: Path, loader_bytes: bytes):
    """Compile only the captured native dependency closure in a private namespace."""
    raw = (root / BASE).read_bytes()
    helper: Any = types.ModuleType("_curation_successor_capture")
    helper.__file__ = str(root / BASE)
    exec(compile(raw, helper.__file__, "exec"), helper.__dict__)
    helper.ENTRY, helper.LOADER = ENTRY, LOADER
    helper.MODULES = (ENTRY, *helper.MODULES)
    helper.SCRIPTS = (*helper.SCRIPTS, BASE, "docs/CURATION_SUCCESSOR.md")
    capture, implementation = helper.load(root, loader_bytes)
    if capture.files[BASE][0] != raw:
        raise ValueError("Curation successor capture helper changed")
    return capture, implementation
