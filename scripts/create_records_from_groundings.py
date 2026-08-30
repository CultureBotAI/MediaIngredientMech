#!/usr/bin/env python3
"""Create MIM records for CultureMech ingredients with an exact ontology match.

`propose_residual_groundings.py` marks a proposal NEW_RECORD when a CultureMech surface
form matches an ontology term exactly and no MIM record holds that CURIE yet. This tool
turns those proposals into records.

In MIM the record `identifier` IS the ontology CURIE, so creating a record on a CURIE
another record already holds is a duplicate by construction. The proposer routes those to
SYNONYM_ONTO_EXISTING instead, and this tool re-checks the invariant at write time --
the corpus may have moved since the proposal was generated.

Grading follows what actually matched:
    EXACT_MATCH     the surface form equals the term's canonical label
    SYNONYM_MATCH   it equals one of the term's exact synonyms
`ontology_label` always carries the canonical OBO label, never the surface form; the
surface form is `preferred_term`. Conflating them is the defect PR #49 had to repair
across 413 records.

Writes per-record files under data/ingredients/mapped/. Follow with `just sync-curated`.

Usage:
    python scripts/create_records_from_groundings.py --groundings reports/x.tsv
    python scripts/create_records_from_groundings.py --groundings reports/x.tsv --apply
"""

from __future__ import annotations

import argparse
import csv
import importlib.util
import sys
from datetime import datetime, timezone
from pathlib import Path

import yaml

_REPO = Path(__file__).resolve().parent.parent
MAPPED = _REPO / "data" / "ingredients" / "mapped"
CURATOR = "claude_culturemech_residual_grounding"
SOURCE = "culturemech:output/ingredient_occurrences.tsv"


def _load(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    # Register before executing: the exporter defines dataclasses, and dataclasses
    # resolves annotations through sys.modules[cls.__module__], which is None otherwise.
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


def held_identifiers() -> dict[str, str]:
    held: dict[str, str] = {}
    for path in (_REPO / "data" / "ingredients").rglob("*.yaml"):
        data = yaml.safe_load(path.read_text(encoding="utf-8"))
        if isinstance(data, dict) and data.get("identifier"):
            held[str(data["identifier"])] = path.name
    return held


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--groundings", type=Path, action="append", required=True)
    parser.add_argument("--apply", action="store_true")
    parser.add_argument("--date", default=datetime.now(timezone.utc).isoformat())
    args = parser.parse_args(argv)

    proposer = _load("proposer", _REPO / "scripts" / "propose_residual_groundings.py")
    exporter = _load("exporter", _REPO / "scripts" / "export_individual_records.py")

    rows: list[dict[str, str]] = []
    for path in args.groundings:
        if not path.is_file():
            raise SystemExit(f"groundings report not found: {path}")
        with path.open(encoding="utf-8", newline="") as handle:
            rows.extend(r for r in csv.DictReader(handle, delimiter="\t") if r["verdict"] == "NEW_RECORD")
    if not rows:
        raise SystemExit("no NEW_RECORD proposals in the given reports")

    held = held_identifiers()
    existing_stems = {p.stem for p in (_REPO / "data" / "ingredients").rglob("*.yaml")}
    # A surface form MIM already has as an UNMAPPED record is not a creation at all --
    # it is a promotion of that record, which carries its synonyms, occurrence statistics
    # and curation history with it. Creating a second record would strand all of that.
    unmapped_by_term: dict[str, str] = {}
    for path in (_REPO / "data" / "ingredients" / "unmapped").glob("*.yaml"):
        data = yaml.safe_load(path.read_text(encoding="utf-8"))
        if isinstance(data, dict) and data.get("mapping_status") == "UNMAPPED":
            term = str(data.get("preferred_term") or "").casefold()
            if term:
                unmapped_by_term[term] = str(data.get("identifier") or "")

    planned: list[tuple[Path, dict]] = []
    promotions: list[tuple[str, str, str, str]] = []
    skipped: list[tuple[str, str]] = []
    claimed: dict[str, str] = {}
    for row in sorted(rows, key=lambda r: (-int(r["occurrences"]), r["label"])):
        label, curie = row["label"], row["curie"]
        if curie in held:
            # The corpus moved since the proposal, or two reports proposed the same CURIE.
            skipped.append((label, f"{curie} already held by {held[curie]}"))
            continue
        if curie in claimed:
            skipped.append((label, f"{curie} already claimed this run by {claimed[curie]!r}"))
            continue
        promote_target = unmapped_by_term.get(label.casefold())
        if promote_target:
            promotions.append((promote_target, label, curie, row["term_label"]))
            continue
        stem = exporter.sanitize_filename(label)
        if not stem or stem in existing_stems:
            skipped.append((label, f"filename stem {stem!r} collides"))
            continue
        exact = proposer.comparison_key(label) == proposer.comparison_key(row["term_label"])
        record = {
            "identifier": curie,
            "preferred_term": label,
            "ontology_mapping": {
                "ontology_id": curie,
                # The canonical OBO label, never the surface form (PR #49).
                "ontology_label": row["term_label"],
                "ontology_source": curie.split(":")[0],
                "mapping_quality": "EXACT_MATCH" if exact else "SYNONYM_MATCH",
                "match_level": "EXACT" if exact else "NORMALIZED",
            },
            "mapping_status": "MAPPED",
            "curation_history": [
                {
                    "timestamp": args.date,
                    "curator": CURATOR,
                    "action": "CREATED_FROM_CULTUREMECH_RESIDUAL",
                    "changes": (
                        f"Created from a CultureMech recipe ingredient MIM held no record for "
                        f"({row['occurrences']} mentions across {row['recipes']} recipes). "
                        f"Grounded to {curie} ({row['term_label']!r}) on an exact match of "
                        f"{'the canonical label' if exact else 'an exact synonym'} to the query "
                        f"{row['matched_query']!r}. Source: {SOURCE}."
                    ),
                    "new_status": "MAPPED",
                    "llm_assisted": False,
                }
            ],
        }
        claimed[curie] = label
        existing_stems.add(stem)
        planned.append((MAPPED / f"{stem}.yaml", record))

    print(f"NEW_RECORD proposals: {len(rows)}")
    print(f"  records to create:    {len(planned)}")
    print(f"  promote instead:      {len(promotions)}")
    print(f"  skipped:              {len(skipped)}")
    for identifier, label, curie, term_label in promotions[:12]:
        print(f"      ! {label!r} is {identifier}; promote it rather than creating a record:")
        print(f"          scripts/promote_resolved_unmapped.py --identifier {identifier} "
              f"--to {curie} --quality <EXACT_MATCH|SYNONYM_MATCH> --apply")
    if len(promotions) > 12:
        print(f"      ... and {len(promotions) - 12} more promotions")
    for label, why in skipped[:12]:
        print(f"      - {label!r}: {why}")

    if not args.apply:
        for path, record in planned[:15]:
            om = record["ontology_mapping"]
            print(f"    {path.name:<48} {om['ontology_id']:<16} {om['mapping_quality']}")
        if len(planned) > 15:
            print(f"    ... and {len(planned) - 15} more")
        print("\nDry run. Re-run with --apply to write.")
        return 0

    MAPPED.mkdir(parents=True, exist_ok=True)
    for path, record in planned:
        path.write_text(
            yaml.dump(record, sort_keys=False, allow_unicode=True, default_flow_style=False),
            encoding="utf-8",
        )
    print(f"\nCreated {len(planned)} records. Next: `just sync-curated`.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
