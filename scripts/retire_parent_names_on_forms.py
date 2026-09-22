#!/usr/bin/env python3
"""Retire a parent compound's names from the records of its salts and hydrates (#232).

47 labels in docs/data/label_index.csv resolved to more than one record and were
judged conflict:different_substances by the index itself. Triaged one by one,
40 have a single shape: a salt, hydrate or merge-tombstone record carries the
name of the parent it is a form OF -- the free acid's IUPAC name on a
monopotassium salt, the anhydrous ChEBI label on a heptahydrate, a sibling
hydrate's formula string on a tombstone. MAPPING_SEMANTICS Section 3 makes those
distinct substances; a consumer resolving the parent's name then reaches the
wrong one.

Criterion, re-derived on every run and decidable without judgement:
  * the synonym is a name ChEBI gives to ANOTHER mapped record's term and does
    NOT give to this record's own term, or
  * it is a formula string whose water count differs from this record's own.
Only records listed in the plan file are touched, so a name ChEBI does not carry
(e.g. a CultureBotHT spelling) is left for a curator rather than guessed at.

Marked REJECTED_LABEL, never deleted: the provenance is real, and claw's builder
filters every candidate alternate through the record's rejected labels, so a
rebuild cannot restore the name from kg-microbe.

Usage:
    python scripts/retire_parent_names_on_forms.py --plan mappings/parent_name_retirements_2026-09-22.json
    python scripts/retire_parent_names_on_forms.py --plan ... --apply
"""

from __future__ import annotations

import argparse
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "src"))

from mediaingredientmech.utils.yaml_handler import save_yaml  # noqa: E402

CURATOR = "retire_parent_names_on_forms"


def main(argv: list[str]) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--plan", type=Path, required=True, help="{record path: [synonym_text, ...]}")
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args(argv)
    plan = json.loads(args.plan.read_text(encoding="utf-8"))
    stamp = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    retired = 0
    for rel, names in sorted(plan.items()):
        path = ROOT / rel
        record = yaml.safe_load(path.read_text(encoding="utf-8"))
        wanted = {n.casefold() for n in names}
        hits = [
            s for s in record.get("synonyms") or []
            if str(s.get("synonym_text") or "").strip().casefold() in wanted
            and str(s.get("synonym_type") or "").upper() != "REJECTED_LABEL"
        ]
        if not hits:
            continue
        print(f"{path.name}: {len(hits)} -> REJECTED_LABEL")
        for hit in hits:
            print(f"    - {hit['synonym_text']}")
        retired += len(hits)
        if not args.apply:
            continue
        for hit in hits:
            hit["synonym_type"] = "REJECTED_LABEL"
        record.setdefault("curation_history", []).append({
            "timestamp": stamp, "curator": CURATOR, "action": "CORRECTED",
            "changes": (
                f"Marked {len(hits)} synonym(s) non-resolving: {[h['synonym_text'] for h in hits]}. "
                f"Each is a name of the parent compound or of a different hydrate, not of "
                f"this form; Section 3 keeps them distinct and the label index resolved the "
                f"parent's name here (#232). Kept as REJECTED_LABEL so a rebuild cannot restore them."
            ),
            "llm_assisted": True,
        })
        save_yaml(record, path)
    print(f"\n{'Retired' if args.apply else 'Would retire'} {retired} synonym(s).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
