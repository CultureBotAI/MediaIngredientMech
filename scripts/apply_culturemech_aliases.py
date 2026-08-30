#!/usr/bin/env python3
"""Add CultureMech surface forms as synonyms on the MIM records they denote.

`triage_culturemech_residual.py` classifies an unresolved CultureMech label as
ALIAS when it folds onto a label MIM already publishes for a MAPPED record. The
compound is mapped; only the spelling is missing. Adding the raw surface form as
a synonym is therefore a labelling fix, not a grounding claim -- it asserts
nothing about chemical identity that the record does not already assert.

Consequently this tool refuses to invent identity:
  * ALIAS rows only -- RESIDUAL/UNMAPPED/AMBIGUOUS/NOISE are never touched.
  * A label already carried as a REJECTED_LABEL synonym is skipped, never
    promoted. MediaIngredientMech#477 made rejected labels stop resolving as
    synonyms; re-adding one here as RAW_TEXT would quietly undo that.
  * A target identifier held by more than one record file is skipped and
    reported: which record should own the spelling is a merge decision.

Writes per-record files under data/ingredients/. Follow with `just sync-curated`
(per-record wins) -- NOT `just sync-individual`, which projects the collection
back over the tree and would revert these edits.

Usage:
    python scripts/apply_culturemech_aliases.py                 # dry run
    python scripts/apply_culturemech_aliases.py --apply
"""

from __future__ import annotations

import argparse
import csv
import re
import sys
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path

import yaml

_REPO = Path(__file__).resolve().parent.parent
RECORDS = _REPO / "data" / "ingredients"
TRIAGE = _REPO / "reports" / "culturemech_residual_triage.tsv"

CURATOR = "claude_culturemech_alias_backfill"
SOURCE = "culturemech:output/ingredient_occurrences.tsv"

# A surface form carrying a supplier or catalogue tag is a CATALOG_VARIANT; every
# other raw recipe spelling is RAW_TEXT.
_VENDOR = re.compile(
    r"\b(?:difco|bd|bbl|oxoid|sigma|aldrich|gibco|merck|fluka|wako|"
    r"nacalai|kanto|tokyo kasei|mn\s*\d|serva|roth)\b",
    re.IGNORECASE,
)


def record_files() -> list[Path]:
    return sorted(RECORDS.rglob("*.yaml"))


def load_records() -> tuple[dict[str, list[Path]], dict[Path, dict]]:
    """Map identifier -> record files, and cache each parsed record."""
    by_identifier: dict[str, list[Path]] = defaultdict(list)
    cache: dict[Path, dict] = {}
    for path in record_files():
        try:
            data = yaml.safe_load(path.read_text(encoding="utf-8"))
        except yaml.YAMLError as exc:
            raise SystemExit(f"unparseable record {path}: {exc}") from exc
        if not isinstance(data, dict):
            continue
        identifier = data.get("identifier")
        if identifier:
            by_identifier[str(identifier)].append(path)
            cache[path] = data
    if not by_identifier:
        raise SystemExit(f"no ingredient records found under {RECORDS}")
    return by_identifier, cache


def existing_texts(record: dict) -> dict[str, str]:
    """Map casefolded synonym text -> its synonym_type, plus the preferred term."""
    seen: dict[str, str] = {}
    term = record.get("preferred_term")
    if term:
        seen[str(term).casefold()] = "PREFERRED_TERM"
    for syn in record.get("synonyms") or []:
        if isinstance(syn, dict) and syn.get("synonym_text"):
            seen[str(syn["synonym_text"]).casefold()] = str(syn.get("synonym_type") or "")
    return seen


def load_alias_rows(path: Path) -> list[dict[str, str]]:
    if not path.is_file():
        raise SystemExit(
            f"triage report not found: {path}\n"
            "Run: python scripts/triage_culturemech_residual.py"
        )
    with path.open(encoding="utf-8", newline="") as handle:
        rows = [r for r in csv.DictReader(handle, delimiter="\t") if r["bucket"] == "ALIAS"]
    if not rows:
        raise SystemExit(f"no ALIAS rows in {path}")
    return rows


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--triage", type=Path, default=TRIAGE)
    parser.add_argument("--apply", action="store_true", help="write changes (default: dry run)")
    parser.add_argument("--only", action="append", help="restrict to these labels (canary mode)")
    # CurationEvent.timestamp is `date-time`, not `date`: a bare YYYY-MM-DD fails
    # validate-strict with format_mismatch on every record written.
    parser.add_argument("--date", default=datetime.now(timezone.utc).isoformat())
    args = parser.parse_args(argv)

    rows = load_alias_rows(args.triage)
    if args.only:
        wanted = {label.casefold() for label in args.only}
        rows = [r for r in rows if r["label"].casefold() in wanted]
        if not rows:
            raise SystemExit("--only matched no ALIAS rows")

    by_identifier, cache = load_records()

    planned: dict[Path, list[dict]] = defaultdict(list)
    counts: dict[str, int] = {}
    skipped: list[tuple[str, str]] = []
    for row in rows:
        identifier, label = row["mim_identifier"], row["label"]
        paths = by_identifier.get(identifier)
        if not paths:
            skipped.append((label, f"no record holds {identifier}"))
            continue
        if len(paths) > 1:
            skipped.append((label, f"{identifier} held by {len(paths)} records; merge first"))
            continue
        path = paths[0]
        seen = existing_texts(cache[path])
        current = seen.get(label.casefold())
        if current == "REJECTED_LABEL":
            skipped.append((label, f"carried as REJECTED_LABEL on {path.name} (#477)"))
            continue
        if current is not None:
            skipped.append((label, f"already present on {path.name} as {current}"))
            continue
        # No `occurrence_count`: not one of the corpus's ~7k synonyms carries it, and
        # MIM's counts are over MIM's own ingest while these are over CultureMech's
        # corpus. Mixing the two silently double-counts (the rule set by #260's pass in
        # add_culturemech_gap_labels.py). The count is audit detail, so it goes in the
        # curation_history note where its corpus is named.
        if any(s["synonym_text"].casefold() == label.casefold() for s in planned[path]):
            # A case variant of a spelling already planned for this record. The index
            # lookup is case-insensitive, so a second row would add no reach.
            counts[label] = int(row["occurrences"])
            for planned_syn in planned[path]:
                if planned_syn["synonym_text"].casefold() == label.casefold():
                    counts[planned_syn["synonym_text"]] += int(row["occurrences"])
            continue
        planned[path].append(
            {
                "synonym_text": label,
                "synonym_type": "CATALOG_VARIANT" if _VENDOR.search(label) else "RAW_TEXT",
                "source": SOURCE,
            }
        )
        counts[label] = int(row["occurrences"])

    owners: dict[str, set[Path]] = defaultdict(set)
    for path, syns in planned.items():
        for syn in syns:
            owners[syn["synonym_text"].casefold()].add(path)
    contested = {text: paths for text, paths in owners.items() if len(paths) > 1}
    if contested:
        # Two records claiming one spelling would publish an ambiguous label_index row,
        # on which CultureMech fails closed -- a net loss over the current miss.
        for text, paths in contested.items():
            skipped.append((text, f"claimed by {len(paths)} records; ambiguous"))
        for path in list(planned):
            planned[path] = [s for s in planned[path] if s["synonym_text"].casefold() not in contested]
            if not planned[path]:
                del planned[path]

    # A spelling already published for a different record is equally ambiguous.
    published: dict[str, set[str]] = defaultdict(set)
    for identifier, paths in by_identifier.items():
        for path in paths:
            for text in existing_texts(cache[path]):
                published[text].add(identifier)
    for path in list(planned):
        own = str(cache[path].get("identifier"))
        keep = []
        for syn in planned[path]:
            holders = published.get(syn["synonym_text"].casefold(), set()) - {own}
            if holders:
                skipped.append((syn["synonym_text"], f"already published for {sorted(holders)[0]}"))
            else:
                keep.append(syn)
        if keep:
            planned[path] = keep
        else:
            del planned[path]

    total = sum(len(v) for v in planned.values())
    print(f"ALIAS rows considered: {len(rows)}")
    print(f"  synonyms to add:  {total} across {len(planned)} records")
    print(f"  skipped:          {len(skipped)}")
    for label, why in skipped[:15]:
        print(f"      - {label!r}: {why}")
    if len(skipped) > 15:
        print(f"      ... and {len(skipped) - 15} more")

    if not args.apply:
        for path, syns in sorted(planned.items())[:10]:
            print(f"\n  {path.relative_to(_REPO)}")
            for syn in syns:
                print(f"      + [{syn['synonym_type']}] {syn['synonym_text']!r} (x{syn['occurrence_count']})")
        if len(planned) > 10:
            print(f"\n  ... and {len(planned) - 10} more records")
        print("\nDry run. Re-run with --apply to write.")
        return 0

    for path, syns in sorted(planned.items()):
        record = cache[path]
        record.setdefault("synonyms", [])
        record["synonyms"].extend(syns)
        record.setdefault("curation_history", []).append(
            {
                "timestamp": args.date,
                "curator": CURATOR,
                "action": "ADDED_SYNONYMS",
                "changes": (
                    f"Added {len(syns)} CultureMech recipe surface form(s) that folded onto this "
                    f"record's published label but were absent from MIM's label index, so "
                    f"CultureMech could not resolve them: "
                    + "; ".join(
                        f"{s['synonym_text']!r} (x{counts[s['synonym_text']]} CultureMech mentions)"
                        for s in syns
                    )
                    + f". Source: {SOURCE}."
                ),
                "llm_assisted": False,
            }
        )
        # No `width=`: the corpus canonical format is PyYAML's default wrap. Widening it
        # reflows every long string in the file, burying two added lines under dozens of
        # spurious ones and making the batch diff unreviewable.
        path.write_text(
            yaml.dump(record, sort_keys=False, allow_unicode=True, default_flow_style=False),
            encoding="utf-8",
        )
    print(f"\nWrote {total} synonyms across {len(planned)} records.")
    print("Next: `just sync-curated` (per-record wins), then regenerate docs/data/label_index.csv.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
