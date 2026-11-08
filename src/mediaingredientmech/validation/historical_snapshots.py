"""Validate the five immutable pre-ID backlog subsets without minting new records.

These 85 historical entries are not the 2,956 current records. Neither their old
placeholder strings nor their old labels establish current identity. The exact
snapshot bytes retain their exact old schema; changed/new files require review.
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path

SCHEMA_DIR = Path(__file__).resolve().parents[1] / "schema" / "historical"


def historical_schema(path: Path, root: Path) -> Path | None:
    """Return the frozen schema only for an unchanged, explicitly inventoried file."""
    try:
        name = path.resolve().relative_to(root.resolve()).as_posix()
    except ValueError:
        return None
    inventory = json.loads((SCHEMA_DIR / "pre_mint_snapshot_inventory.json").read_text())
    expected = inventory["files"].get(name)
    if expected is None:
        return None
    if path.is_symlink() or hashlib.sha256(path.read_bytes()).hexdigest() != expected:
        raise ValueError(f"Historical ingredient snapshot was modified: {name}")
    schema = SCHEMA_DIR / "pre_mint_ingredient_snapshot.yaml"
    for candidate, digest in [
        (schema, inventory["schema_sha256"]),
        (SCHEMA_DIR / "mech_shared.yaml", inventory["shared_schema_sha256"]),
    ]:
        if hashlib.sha256(candidate.read_bytes()).hexdigest() != digest:
            raise ValueError("Historical snapshot schema differs from its pinned source")
    return schema
