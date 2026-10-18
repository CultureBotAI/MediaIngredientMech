#!/usr/bin/env python3
"""Write an audit-only section-refresh receipt; changed bytes need fresh approval.

Run after a change confined to one auditable section has been synced to the
per-record files. Every changed record must differ from ``--base`` only in that
section plus one appended curation event. The receipt documents that bounded
change; it does not preserve an approval or advance the reviewed baseline.

Usage:
    python scripts/make_record_refresh_receipt.py --section causal_graphs --batch causal-graphs-YYYYMMDD
    python scripts/make_record_refresh_receipt.py --section occurrence_statistics --batch ... --write
"""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "src"))

from mediaingredientmech.record_refresh import (  # noqa: E402
    RECEIPT_KIND,
    REFRESH_DIR,
    REFRESHABLE_SECTIONS,
    RecordRefreshes,
    peel,
    sha256,
)


def git(*args: str) -> bytes:
    return subprocess.run(["git", "-C", str(ROOT), *args], check=True, capture_output=True).stdout


# Preserve the historical producer exclusion for ingredient-bundle owners
# (#828). All changed records, including other owners, require fresh approval.
BUNDLE_REVIEW = ROOT / "reports/ingredient_bundle_20260924/review.json"


def _paths(raw: bytes) -> list[str]:
    """NUL-separated paths from ``git ... -z`` (no C-quoting of non-ASCII names, #825)."""
    return [p for p in raw.decode("utf-8").split("\0") if p]


def _json_faithful(value):
    """The value exactly as the receipt will store it, or SystemExit if JSON would alter it (#826)."""
    try:
        restored = json.loads(json.dumps(value, ensure_ascii=False))
    except (TypeError, ValueError) as error:
        raise SystemExit(f"error: section value is not JSON-representable: {error}") from error
    if restored != value:
        raise SystemExit("error: JSON would change the section value (non-string keys or typed scalars); quote them in YAML")
    return restored


def build(base: str, batch: str, section: str) -> dict:
    changed = _paths(git("-c", "core.quotePath=false", "diff", "--name-only", "-z", base, "--", "data/ingredients"))
    untracked = _paths(
        git("-c", "core.quotePath=false", "ls-files", "-z", "--others", "--exclude-standard", "--", "data/ingredients")
    )
    bundle_owners = set(json.loads(BUNDLE_REVIEW.read_text()).get("record_inputs", {})) if BUNDLE_REVIEW.is_file() else set()
    blocked = sorted(set(changed) & bundle_owners)
    if blocked:
        raise SystemExit(f"error: ingredient-bundle owners are excluded from section audit receipts (#828): {blocked[:5]}")
    if untracked:
        raise SystemExit(f"error: untracked record files are not refreshes: {untracked[:5]}")
    records = []
    for path in sorted(changed):
        current = ROOT / path
        if not current.is_file():
            raise SystemExit(f"error: {path} was removed; a removal is not a section refresh")
        before = git("show", f"{base}:{path}")
        after = current.read_bytes()
        before_record, after_record = yaml.safe_load(before), yaml.safe_load(after)
        entry = {
            "source_record": path,
            "section": section,
            "before_yaml_sha256": sha256(before),
            "after_yaml_sha256": sha256(after),
            "before_value": _json_faithful(before_record.get(section)),
            "event": (after_record.get("curation_history") or [None])[-1],
        }
        try:
            peel(after, entry)
        except (ValueError, KeyError, TypeError, AttributeError) as error:
            raise SystemExit(f"error: {path} is not a {section} refresh: {error}") from error
        records.append(entry)
    if not records:
        raise SystemExit("error: no record differs from the base; nothing to receipt")
    existing = RecordRefreshes(ROOT).receipts
    return {
        "schema_version": 1,
        "kind": RECEIPT_KIND,
        "batch": batch,
        "sequence": len(existing) + 1,
        "section": section,
        "scope": (
            f"The {section} section and the one curation event appended with it, per record; "
            "no identity, mapping, synonym, role, component or evidence change."
        ),
        "approval": (
            "NONE: this receipt is audit history only. Any changed record bytes require "
            "fresh approval bound to the resulting bytes."
        ),
        "base_commit": git("rev-parse", base).decode().strip(),
        "record_count": len(records),
        "records": records,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--section", required=True, choices=sorted(REFRESHABLE_SECTIONS))
    parser.add_argument("--batch", required=True, help="receipt name, e.g. causal-graphs-20261005")
    parser.add_argument("--base", default="HEAD", help="commit the records are refreshed from")
    parser.add_argument("--write", action="store_true", help="write the receipt (default: preview)")
    args = parser.parse_args()
    receipt = build(args.base, args.batch, args.section)
    target = ROOT / REFRESH_DIR / f"{args.batch}.json"
    print(f"{receipt['record_count']} {args.section} refresh(es) verified; sequence {receipt['sequence']}")
    if not args.write:
        print(f"preview only; re-run with --write to create {target.relative_to(ROOT)}")
        return
    if target.exists():
        raise SystemExit(f"error: {target.relative_to(ROOT)} exists; receipts are append-only")
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(json.dumps(receipt, indent=2, ensure_ascii=False) + "\n")
    print(f"wrote {target.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
