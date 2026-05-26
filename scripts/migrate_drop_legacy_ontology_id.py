"""One-shot migration: drop the legacy top-level `ontology_id` key from
ingredient records inside the 5 categorized unmapped collections.

Background
----------
`IngredientRecord` was renamed `ontology_id` -> `identifier`. The writer in
`scripts/prepare_unmapped_for_curation.py` emitted both keys for backwards
compatibility; the closed-schema strict validator now flags `ontology_id`
as `unexpected_field` (85 ERROR rows across the 5 files).

This migration scans each categorized file, removes `ontology_id` from
every record where it equals the record's `identifier`, and re-writes the
file through `write_validated_ingredient` so the result is structurally
valid against the schema.

Idempotent: running again is a no-op (the key is already gone).

Usage
-----
    # Preview (default):
    uv run python scripts/migrate_drop_legacy_ontology_id.py

    # Apply:
    uv run python scripts/migrate_drop_legacy_ontology_id.py --apply
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

import yaml

REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT / "src"))

from mediaingredientmech.validation.write_validated import (  # noqa: E402
    ValidationFailedError,
    write_validated_ingredient,
)

CATEGORIZED_FILES = [
    REPO_ROOT / "data" / "curated" / "unmapped_already_mapped.yaml",
    REPO_ROOT / "data" / "curated" / "unmapped_complex_media.yaml",
    REPO_ROOT / "data" / "curated" / "unmapped_incomplete_formula.yaml",
    REPO_ROOT / "data" / "curated" / "unmapped_other.yaml",
    REPO_ROOT / "data" / "curated" / "unmapped_placeholder.yaml",
]


def migrate_file(path: Path, *, apply: bool) -> tuple[int, int]:
    """Return `(records_with_legacy_key, records_dropped)`."""
    with path.open("r", encoding="utf-8") as f:
        data = yaml.safe_load(f)

    if not isinstance(data, dict) or not isinstance(data.get("ingredients"), list):
        print(f"  SKIP {path.name}: not an IngredientCollection")
        return 0, 0

    seen = 0
    dropped = 0
    for record in data["ingredients"]:
        if not isinstance(record, dict):
            continue
        if "ontology_id" not in record:
            continue
        seen += 1
        legacy = record["ontology_id"]
        identifier = record.get("identifier")
        if legacy != identifier:
            print(
                f"  WARN {path.name}: skipping record "
                f"identifier={identifier!r} — legacy ontology_id={legacy!r} "
                "differs from identifier (not a safe rename)."
            )
            continue
        del record["ontology_id"]
        dropped += 1

    if apply and dropped > 0:
        try:
            write_validated_ingredient(
                data, path, target_class="IngredientCollection"
            )
        except ValidationFailedError as exc:
            print(f"  ERROR {path.name}: validation failed after migration")
            print(exc.summary())
            raise

    return seen, dropped


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--apply",
        action="store_true",
        help="Actually write changes (default: dry-run preview only).",
    )
    args = parser.parse_args()

    mode = "APPLY" if args.apply else "DRY-RUN"
    print(f"=== migrate_drop_legacy_ontology_id ({mode}) ===")

    total_seen = 0
    total_dropped = 0
    for path in CATEGORIZED_FILES:
        if not path.exists():
            print(f"  SKIP {path.name}: file not found")
            continue
        seen, dropped = migrate_file(path, apply=args.apply)
        total_seen += seen
        total_dropped += dropped
        verb = "would drop" if not args.apply else "dropped"
        print(f"  {path.name}: {verb} {dropped}/{seen} legacy ontology_id key(s)")

    print(f"--- total: {verb} {total_dropped}/{total_seen} legacy ontology_id key(s) ---")
    if not args.apply and total_seen > 0:
        print("(re-run with --apply to write changes)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
