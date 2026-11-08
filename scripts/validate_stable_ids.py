#!/usr/bin/env python3
"""Read-only current-inventory and trusted-base registry validation (#1265)."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

import yaml

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
from mediaingredientmech.stable_ids import (  # noqa: E402
    StableIdError,
    build_record_index,
    load_registry,
    validate_history,
    validate_records,
)


class UniqueKeyLoader(yaml.SafeLoader):
    """Do not hide duplicate mim_id fields while checking exactly one ID."""


def _mapping(loader, node, deep=False):
    result = {}
    for key_node, value_node in node.value:
        key = loader.construct_object(key_node, deep=deep)
        if key in result:
            raise StableIdError(f"Duplicate YAML key: {key}")
        result[key] = loader.construct_object(value_node, deep=deep)
    return result


UniqueKeyLoader.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, _mapping)


def check(root: Path, base: str | None = None) -> dict:
    registry = load_registry(root)
    records = {}
    for kind in ("mapped", "unmapped"):
        directory = root / "data/ingredients" / kind
        if not directory.is_dir():
            raise StableIdError(f"Missing record directory: {kind}")
        for path in sorted(directory.glob("*.yaml")):
            record = yaml.load(path.read_text(encoding="utf-8"), Loader=UniqueKeyLoader)
            if not isinstance(record, dict):
                raise StableIdError(f"Record is not a mapping: {path.name}")
            records[path.relative_to(root).as_posix()] = record
    validate_records(registry, records)
    if base is not None:
        validate_history(root, base)
    index = build_record_index(records)
    return {
        "records": len(records),
        "minted_ids": len(registry.entries),
        "lifecycle_events": len(registry.events),
        "ambiguous_legacy_aliases": index.ambiguous_aliases,
        "history_base": base,
        "history_checked": base is not None,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--base", help="Trusted full ancestor commit SHA for append-only history")
    parser.add_argument("--require-history", action="store_true")
    args = parser.parse_args()
    if args.require_history and not args.base:
        parser.error("--require-history needs --base")
    try:
        print(json.dumps(check(args.root.resolve(), args.base), indent=2))
    except (StableIdError, OSError, yaml.YAMLError) as exc:
        print(f"Stable ID validation failed: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
