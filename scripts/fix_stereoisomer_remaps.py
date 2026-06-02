#!/usr/bin/env python3
"""Re-map stereoisomer records that were auto-collapsed onto an achiral CHEBI parent.

The `resolve_unmapped` auto-upgrade normalized stereo-prefixed names to their
generic form, so distinct enantiomers ended up sharing one achiral CHEBI id
(flagged in notes/duplicate_identifiers_analysis_2026-05-29.md). This re-points
each to its correct stereospecific CHEBI term.

Remaps (verified against the local CHEBI sqlite):
  (R)-3-hydroxybutyrate : CHEBI:37054 (3-hydroxybutyrate)  -> CHEBI:10983
  (S)-3-hydroxybutyrate : CHEBI:37054 (3-hydroxybutyrate)  -> CHEBI:11047
  L-Carnitine           : CHEBI:17126 (carnitine, racemate)-> CHEBI:16347 ((R)-carnitine)

chemical_properties are left untouched (the molecular_formula is identical
across enantiomers; the stereo InChI/SMILES refinement is out of scope).

Usage:
    python scripts/fix_stereoisomer_remaps.py [--dry-run]
"""

import argparse
import sys
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from mediaingredientmech.curation.ingredient_curator import IngredientCurator

# (preferred_term, current identifier, corrected identifier)
REMAPS = [
    ("(R)-3-hydroxybutyrate", "CHEBI:37054", "CHEBI:10983"),
    ("(S)-3-hydroxybutyrate", "CHEBI:37054", "CHEBI:11047"),
    ("L-Carnitine", "CHEBI:17126", "CHEBI:16347"),
]
CHEBI_DB = f"sqlite:///{Path.home() / '.data' / 'oaklib' / 'chebi.db'}"


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    from oaklib import get_adapter

    adapter = get_adapter(CHEBI_DB)
    curator = IngredientCurator(
        data_path=Path("data/curated/mapped_ingredients.yaml"),
        curator_name="fix_stereoisomer_remaps",
    )
    curator.load()
    ts = datetime.now(timezone.utc).isoformat()

    by_pt = {(r.get("preferred_term"), r.get("identifier")): r for r in curator.records}
    n = 0
    for pt, old_id, new_id in REMAPS:
        record = by_pt.get((pt, old_id))
        if record is None:
            print(f"  SKIP: no record {pt!r} with identifier {old_id}")
            continue
        new_label = adapter.label(new_id) or ""
        om = record.get("ontology_mapping") or {}
        record["identifier"] = new_id
        om["ontology_id"] = new_id
        om["ontology_label"] = new_label
        om["mapping_quality"] = "EXACT_MATCH"
        om.setdefault("evidence", []).append(
            {
                "evidence_type": "CURATOR_JUDGMENT",
                "source": "fix_stereoisomer_remaps",
                "notes": (
                    f"Re-mapped from achiral {old_id} to stereospecific {new_id} "
                    f"({new_label}); the prior auto-upgrade collapsed the stereo "
                    f"prefix to the generic parent."
                ),
            }
        )
        record["ontology_mapping"] = om
        if record.get("kg_microbe_node_id") == old_id:
            record["kg_microbe_node_id"] = new_id
        record.setdefault("curation_history", []).append(
            {
                "timestamp": ts,
                "curator": "fix_stereoisomer_remaps",
                "action": "CORRECTED",
                "changes": (
                    f"identifier {old_id} -> {new_id}: enantiomer was sharing an "
                    f"achiral CHEBI parent with its mirror image."
                ),
                "llm_assisted": False,
            }
        )
        print(f"  {pt}: {old_id} -> {new_id} ({new_label})")
        n += 1

    if not args.dry_run:
        curator.save()
        print(f"\nSaved {n} remaps.")
    else:
        print(f"\n[dry-run] would remap {n} records.")


if __name__ == "__main__":
    main()
