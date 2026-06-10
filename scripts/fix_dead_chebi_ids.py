#!/usr/bin/env python3
"""Re-map three curated records pointing at CHEBI ids that no longer exist.

The id↔label correspondence checker found three MAPPED records whose
`ontology_id` is absent from current ChEBI (HTTP 404 on OLS4 — not merely
missing from the local sqlite, and not flagged obsolete: the ids were removed):

  Diaminopimelic acid  CHEBI:23674 -> CHEBI:23673 (2,6-diaminopimelic acid)
        the current generic ChEBI term for the unspecified-stereo acid.
  Catalase             CHEBI:3463  -> NCIT:C61062 (Catalase)
        catalase is an enzyme, not a ChEBI small molecule — ChEBI only has
        "catalase inhibitor"; NCIT is the correct ontology.
  Sodium L-lactate     CHEBI:867561 -> merge into CHEBI:232798 (sodium L-lactate)
        the correct current id already exists as a record (preferred_term
        "Na-L-lactate"), so this is a duplicate to merge, not a bare remap.

Targets verified against OLS4 (current ChEBI/NCIT). Remaps change the record's
primary key (`identifier`); the merge marks the dead-id record REJECTED and
folds its name/synonyms/occurrence stats into the survivor. Each leaves a
CORRECTED / merge curation event. Idempotent.

Usage:
    python scripts/fix_dead_chebi_ids.py [--dry-run]
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

import yaml

sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from mediaingredientmech.curate.curation_event import record_curation_event
from mediaingredientmech.utils.yaml_handler import save_yaml

DATA = Path("data/curated/mapped_ingredients.yaml")

# (preferred_term, old_id, new_id, new_source, new_label)
REMAPS = [
    ("Diaminopimelic acid", "CHEBI:23674", "CHEBI:23673", "CHEBI", "2,6-diaminopimelic acid"),
    ("Catalase", "CHEBI:3463", "NCIT:C61062", "NCIT", "Catalase"),
]
# (source preferred_term, source dead id) -> (target id)
MERGE = ("Sodium L-lactate", "CHEBI:867561", "CHEBI:232798")


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    data = yaml.safe_load(DATA.read_text())
    by_id = {(r.get("preferred_term"), r.get("identifier")): r for r in data["ingredients"]}
    by_oid = {(r.get("ontology_mapping") or {}).get("ontology_id"): r for r in data["ingredients"]}
    changed = 0

    for pt, old_id, new_id, new_source, new_label in REMAPS:
        rec = by_id.get((pt, old_id))
        if rec is None:
            print(f"  SKIP remap: no record {pt!r} @ {old_id} (already fixed?)")
            continue
        om = rec.get("ontology_mapping") or {}
        rec["identifier"] = new_id
        om["ontology_id"] = new_id
        om["ontology_label"] = new_label
        om["ontology_source"] = new_source
        om["mapping_quality"] = "EXACT_MATCH"
        rec["ontology_mapping"] = om
        record_curation_event(
            rec,
            curator="fix_dead_chebi_ids.py",
            action="CORRECTED",
            changes=(
                f"identifier {old_id} -> {new_id} ({new_label}, source {new_source}): "
                f"{old_id} is absent from current ChEBI (OLS4 404)."
            ),
        )
        print(f"  remap {pt!r}: {old_id} -> {new_id} ({new_label})")
        changed += 1

    # --- merge dead-id duplicate into the survivor ---
    src_pt, src_id, tgt_id = MERGE
    src = by_id.get((src_pt, src_id))
    tgt = by_oid.get(tgt_id)
    if src is None:
        print(f"  SKIP merge: no record {src_pt!r} @ {src_id} (already merged?)")
    elif tgt is None:
        print(f"  SKIP merge: survivor {tgt_id} not found")
    elif src.get("mapping_status") == "REJECTED":
        print(f"  SKIP merge: {src_id} already REJECTED")
    else:
        # fold source name + synonyms into the survivor
        tgt_syn_texts = {
            (s.get("synonym_text") if isinstance(s, dict) else str(s)).strip().lower()
            for s in (tgt.get("synonyms") or [])
        }
        to_add = [src.get("preferred_term")] + [
            (s.get("synonym_text") if isinstance(s, dict) else str(s))
            for s in (src.get("synonyms") or [])
        ]
        for text in to_add:
            if text and text.strip().lower() not in tgt_syn_texts:
                tgt.setdefault("synonyms", []).append(
                    {"synonym_text": text, "synonym_type": "EXACT_SYNONYM", "source": "merge"}
                )
                tgt_syn_texts.add(text.strip().lower())
        # combine occurrence stats (approximate: media lists not tracked per-record)
        ts, ss = tgt.get("occurrence_statistics") or {}, src.get("occurrence_statistics") or {}
        if ss:
            ts["total_occurrences"] = ts.get("total_occurrences", 0) + ss.get("total_occurrences", 0)
            ts["media_count"] = ts.get("media_count", 0) + ss.get("media_count", 0)
            tgt["occurrence_statistics"] = ts
            # zero the source's stats: they now live on the survivor (a REJECTED
            # record must carry no occurrences — test_occurrence_stats_consistent).
            ss["total_occurrences"] = 0
            ss["media_count"] = 0
            if "sample_media" in ss:
                ss["sample_media"] = []
            src["occurrence_statistics"] = ss
        src["mapping_status"] = "REJECTED"
        record_curation_event(
            tgt, curator="fix_dead_chebi_ids.py", action="MERGED",
            changes=f"Merged dead-id duplicate {src_id} ({src_pt!r}) into this record.",
        )
        record_curation_event(
            src, curator="fix_dead_chebi_ids.py", action="REJECTED",
            changes=f"Dead id {src_id} (OLS4 404); same substance as {tgt_id}; merged there.",
        )
        print(f"  merge {src_pt!r} {src_id} -> {tgt_id} (REJECTED source)")
        changed += 1

    print(f"\n{'[dry-run] would change' if args.dry_run else 'Changed'} {changed} record(s).")
    if changed and not args.dry_run:
        save_yaml(data, DATA, backup=False, validate=True, target_class="IngredientCollection")
        print(f"Saved {DATA}")


if __name__ == "__main__":
    main()
