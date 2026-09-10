"""Repair same-prefix kg_microbe_node_id drift reported in #554."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
sys.path.insert(0, str(ROOT / "src"))

from audit_kg_microbe_node_ids import (  # noqa: E402
    COLLECTIONS,
    DataProblem,
    load_collection,
    mismatch_type,
)

from mediaingredientmech.utils.yaml_handler import save_yaml  # noqa: E402

STAMP = "2026-09-09T00:00:00+00:00"
CURATOR = "fix_kg_microbe_node_id_drift"
ISSUE = "#554"


def repair(data: dict[str, Any]) -> tuple[list[str], list[str]]:
    changed: list[str] = []
    skipped: list[str] = []

    for record in data.get("ingredients", []):
        identifier = record.get("identifier")
        kg_microbe_node_id = record.get("kg_microbe_node_id")
        if identifier is None or kg_microbe_node_id is None:
            continue
        if str(identifier) == str(kg_microbe_node_id):
            continue

        if mismatch_type(identifier, kg_microbe_node_id) != "same_prefix":
            skipped.append(f"{record.get('preferred_term')}: {kg_microbe_node_id} -> {identifier}")
            continue

        old_node_id = str(kg_microbe_node_id)
        new_node_id = str(identifier)
        record["kg_microbe_node_id"] = new_node_id
        record.setdefault("curation_history", []).append(
            {
                "timestamp": STAMP,
                "curator": CURATOR,
                "action": "CORRECTED",
                "changes": (
                    f"kg_microbe_node_id {old_node_id} -> {new_node_id} ({ISSUE}). "
                    "The compatibility node id lagged a same-prefix identifier "
                    "correction; the downstream node id must match the curated "
                    "identifier unless a record intentionally crosses CURIE prefixes."
                ),
                "llm_assisted": False,
            }
        )
        changed.append(f"{record.get('preferred_term')}: {old_node_id} -> {new_node_id}")

    return changed, skipped


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--apply", action="store_true", help="write repaired collection YAML")
    args = ap.parse_args()

    collections = {}
    try:
        for collection, path in COLLECTIONS.items():
            collections[collection] = (path, load_collection(path))
    except DataProblem as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2

    all_changed: list[str] = []
    all_skipped: list[str] = []
    for collection, (path, data) in collections.items():
        changed, skipped = repair(data)
        all_changed.extend(f"{collection}: {row}" for row in changed)
        all_skipped.extend(f"{collection}: {row}" for row in skipped)
        if args.apply and changed:
            save_yaml(data, path, backup=False)

    print(f"{len(all_changed)} same-prefix kg_microbe_node_id correction(s)")
    for row in all_changed:
        print(f"  {row}")
    print(f"{len(all_skipped)} cross-prefix mismatch(es) left unchanged")
    for row in all_skipped:
        print(f"  {row}")

    if not args.apply and all_changed:
        print("Dry run only; pass --apply to write changes")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
