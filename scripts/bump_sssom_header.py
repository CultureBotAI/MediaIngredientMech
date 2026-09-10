#!/usr/bin/env python3
"""Set the SSSOM header's version and date to the newest row `mapping_date`.

Rule G in `validate_sssom_invariants` requires the header to describe the rows
underneath it, which is what stops `mapping_set_version` going quietly stale
while the set changes (#301). Nothing bumped it, so satisfying a now-blocking
gate meant hand-editing the header -- the very thing that made it unreliable.

Every MIM-side row writer appends without touching the header, and
`reconcile_sssom --apply --date D` stamps whatever date the operator passes,
which can itself disagree with the newest row. This computes the value Rule G
actually wants and writes exactly that (#602).

Usage:
    python scripts/bump_sssom_header.py            # report what would change
    python scripts/bump_sssom_header.py --apply
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

_REPO = Path(__file__).resolve().parent.parent
SSSOM = _REPO / "mappings" / "ingredient_mappings.sssom.tsv"
_DATE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
_FIELDS = ("mapping_set_version", "mapping_date")


def newest_row_date(lines: list[str]) -> str | None:
    """
    Return the newest parseable `mapping_date` among the data rows.

    :param lines: Every line of the mapping set, header block included.
    :return: The newest date, or None when no row carries one.
    """
    body = [ln for ln in lines if not ln.startswith("#")]
    if not body:
        return None
    columns = body[0].rstrip("\n").split("\t")
    if "mapping_date" not in columns:
        return None
    index = columns.index("mapping_date")
    dates = [
        value
        for row in body[1:]
        if len(cells := row.rstrip("\n").split("\t")) > index
        and _DATE.match(value := cells[index].strip())
    ]
    return max(dates) if dates else None


def rewrite(lines: list[str], date: str) -> tuple[list[str], dict[str, str]]:
    """
    Return the lines with both header fields set to `date`, and what changed.

    :param lines: Every line of the mapping set.
    :param date: The value to stamp.
    :return: (new lines, {field: old value} for fields that actually moved).
    """
    changed: dict[str, str] = {}
    out: list[str] = []
    for line in lines:
        for field in _FIELDS:
            marker = f"# {field}:"
            if line.startswith(marker):
                old = line[len(marker) :].strip().strip('"')
                if old != date:
                    changed[field] = old
                line = f'# {field}: "{date}"\n'
                break
        out.append(line)
    return out, changed


def main(argv: list[str]) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--apply", action="store_true", help="Write the change")
    parser.add_argument("--sssom", type=Path, default=SSSOM)
    args = parser.parse_args(argv)

    lines = args.sssom.read_text(encoding="utf-8").splitlines(keepends=True)
    date = newest_row_date(lines)
    if date is None:
        print("No row carries a parseable mapping_date; nothing to bump.")
        return 1

    _, changed = rewrite(lines, date)
    if not changed:
        print(f"Header already matches the newest row mapping_date ({date}).")
        return 0
    for field, old in sorted(changed.items()):
        print(f"  {field}: {old} -> {date}")
    if not args.apply:
        print("Dry run. Re-run with --apply to write it.")
        return 0
    new_lines, _ = rewrite(lines, date)
    args.sssom.write_text("".join(new_lines), encoding="utf-8")
    print(f"Wrote {args.sssom}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
