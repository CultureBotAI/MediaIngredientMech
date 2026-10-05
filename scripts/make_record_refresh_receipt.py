#!/usr/bin/env python3
"""Write a section-refresh receipt for the review chain.

Run after a change confined to one refreshable section (see
``mediaingredientmech.record_refresh.REFRESHABLE_SECTIONS``) has been synced to
the per-record files, before committing. Every per-record file that differs
from ``--base`` must differ only in that section plus one appended curation
event, or nothing is written: a receipt that covered other edits would carry
reviews past changes nobody reviewed.

Each entry is verified with the same ``record_refresh.peel`` the assemblers
use, so a receipt this writes is one they accept.

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


def build(base: str, batch: str, section: str) -> dict:
    changed = git("diff", "--name-only", base, "--", "data/ingredients").decode().split()
    untracked = git("ls-files", "--others", "--exclude-standard", "--", "data/ingredients").decode().split()
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
            "before_value": before_record.get(section),
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
            "NONE: this receipt approves nothing. It lets a review bound to a record's "
            "before bytes keep applying only after the section-only difference is verified."
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
