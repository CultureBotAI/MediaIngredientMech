#!/usr/bin/env python3
"""Validate component-reference and has-part invariants across the MIM catalog."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "src"))

from mediaingredientmech.validation.component_partonomy import (  # noqa: E402
    load_curated_records,
    validate_component_partonomy,
)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--curated-dir",
        type=Path,
        default=REPO_ROOT / "data" / "curated",
    )
    args = parser.parse_args(argv)

    try:
        records = load_curated_records(args.curated_dir)
    except (OSError, ValueError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2

    violations = validate_component_partonomy(records)
    for violation in violations:
        print(violation, file=sys.stderr)
    component_records = sum(bool(record.get("components")) for record in records)
    component_count = sum(len(record.get("components") or []) for record in records)
    print(
        f"component partonomy: {len(records)} records, {component_records} decompositions, "
        f"{component_count} components, {len(violations)} violation(s)"
    )
    return 2 if violations else 0


if __name__ == "__main__":
    raise SystemExit(main())
