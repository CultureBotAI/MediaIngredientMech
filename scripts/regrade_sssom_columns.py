#!/usr/bin/env python3
"""Align the published SSSOM's `confidence` and `mapping_justification` with the builder.

MIM's promotion helpers and claw's `build_mim_ingredient_sssom.py` used different rules
for these two columns, so whichever ran last won and the values flipped across rebuilds
with nothing gating or reporting it (#519). `mediaingredientmech.sssom_grading` now holds
one rule, mirroring the builder's, so no NEW row diverges -- but rows written before that
still carry the old grades.

This aligns them, using a freshly built working copy as the reference. The builder is the
authority by construction: it regenerates every row from the records, so a value it does
not produce cannot survive the next rebuild anyway.

Only those two columns are touched. Identity -- subject, object, predicate -- is never
modified, so this cannot change what the file claims, only how confidently it says it.

Read-only by default.

Usage:
    python scripts/regrade_sssom_columns.py --rebuild <working-copy>
    python scripts/regrade_sssom_columns.py --rebuild <working-copy> --apply
"""

from __future__ import annotations

import argparse
import collections
import csv
import io
import sys
from pathlib import Path

_REPO = Path(__file__).resolve().parent.parent
PUBLISHED = _REPO / "mappings" / "ingredient_mappings.sssom.tsv"
COLUMNS = ("confidence", "mapping_justification")


def split(path: Path) -> tuple[str, list[str]]:
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines(keepends=True)
    preamble = [line for line in lines if line.startswith("#")]
    body = [line for line in lines if not line.startswith("#")]
    return "".join(preamble), body


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--published", type=Path, default=PUBLISHED)
    parser.add_argument("--rebuild", type=Path, required=True)
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args(argv)

    for path in (args.published, args.rebuild):
        if not path.is_file():
            raise SystemExit(f"not found: {path}")

    preamble, body = split(args.published)
    reader = csv.DictReader(io.StringIO("".join(body)), delimiter="\t")
    rows = list(reader)
    fieldnames = reader.fieldnames or []

    _, ref_body = split(args.rebuild)
    reference = {
        (r["subject_id"], r["object_id"]): r
        for r in csv.DictReader(io.StringIO("".join(ref_body)), delimiter="\t")
    }

    moves: dict[tuple[str, str, str], int] = collections.Counter()
    unmatched = 0
    for row in rows:
        ref = reference.get((row["subject_id"], row["object_id"]))
        if ref is None:
            # A row the builder does not produce -- a stale subject, say. Leaving it
            # alone is right: we have no authority for a new grade.
            unmatched += 1
            continue
        for column in COLUMNS:
            before, after = row.get(column, ""), ref.get(column, "")
            if after and before != after:
                moves[(column, before, after)] += 1
                row[column] = after

    total = sum(moves.values())
    print(f"rows: {len(rows)}   not produced by the builder (left alone): {unmatched}")
    print(f"cells realigned: {total}")
    for (column, before, after), n in sorted(moves.items(), key=lambda kv: -kv[1]):
        print(f"  {column:<22} {before or '(empty)'} -> {after}: {n}")

    if not args.apply:
        print("\nDry run. Re-run with --apply to write.")
        return 0

    out = io.StringIO()
    writer = csv.DictWriter(out, fieldnames=fieldnames, delimiter="\t", lineterminator="\n")
    writer.writeheader()
    writer.writerows(rows)
    args.published.write_text(preamble + out.getvalue(), encoding="utf-8")
    print(f"\nWrote {args.published}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
