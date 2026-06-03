#!/usr/bin/env python3
"""Re-map casein-peptone trade products from the coarse FOODON parent to precise MICRO terms.

`FOODON:03315719` ("mammalian milk protein (hydrolyzed)") was shared by three
distinct casein-peptone products (Casein peptone / Trypticase / Tryptone) — a
valid but coarse mapping (flagged in notes/duplicate_identifiers_analysis_2026-05-29.md).
The Microbial growth media ontology (MICRO) has exact terms for two of them, so
this re-points them for a more precise mapping (verified against MICRO via OLS4):

  Tryptone   FOODON:03315719 -> MICRO:0000182 ("tryptone")            EXACT
  Trypticase FOODON:03315719 -> MICRO:0000175 ("Trypticase peptone")  CLOSE (trade name)

The resulting shared identifiers (Tryptone≡Bacto-tryptone on MICRO:0000182;
Trypticase≡"Trypticase peptone" on MICRO:0000175) are legitimate same-substance
variant collisions, not errors. Generic "Casein peptone" (occ=0) has no exact
MICRO term and stays on FOODON:03315719 (now its sole holder — collision resolved).

Usage:
    python scripts/remap_peptones_to_micro.py [--dry-run]
"""

import argparse
import sys
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from mediaingredientmech.curation.ingredient_curator import IngredientCurator

# (preferred_term, old_id, new_id, new_label, mapping_quality)
REMAPS = [
    ("Tryptone", "FOODON:03315719", "MICRO:0000182", "tryptone", "EXACT_MATCH"),
    ("Trypticase", "FOODON:03315719", "MICRO:0000175", "Trypticase peptone", "CLOSE_MATCH"),
]


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    curator = IngredientCurator(
        data_path=Path("data/curated/mapped_ingredients.yaml"),
        curator_name="remap_peptones_to_micro",
    )
    curator.load()
    ts = datetime.now(timezone.utc).isoformat()
    by_pt = {(r.get("preferred_term"), r.get("identifier")): r for r in curator.records}

    n = 0
    for pt, old_id, new_id, new_label, quality in REMAPS:
        record = by_pt.get((pt, old_id))
        if record is None:
            print(f"  SKIP: no record {pt!r} with identifier {old_id}")
            continue
        om = record.get("ontology_mapping") or {}
        record["identifier"] = new_id
        om["ontology_id"] = new_id
        om["ontology_label"] = new_label
        om["ontology_source"] = "MICRO"
        om["mapping_quality"] = quality
        om.setdefault("evidence", []).append(
            {
                "evidence_type": "CURATOR_JUDGMENT",
                "source": "remap_peptones_to_micro",
                "notes": (
                    f"Re-mapped from the coarse {old_id} (mammalian milk protein, "
                    f"hydrolyzed) to the precise MICRO term {new_id} ({new_label})."
                ),
            }
        )
        record["ontology_mapping"] = om
        record.setdefault("curation_history", []).append(
            {
                "timestamp": ts,
                "curator": "remap_peptones_to_micro",
                "action": "CORRECTED",
                "changes": (
                    f"identifier {old_id} -> {new_id}: disambiguated casein-peptone "
                    f"product from the shared coarse FOODON term to its precise MICRO term."
                ),
                "llm_assisted": False,
            }
        )
        print(f"  {pt}: {old_id} -> {new_id} ({new_label}) [{quality}]")
        n += 1

    if not args.dry_run:
        curator.save()
        print(f"\nSaved {n} remaps.")
    else:
        print(f"\n[dry-run] would remap {n} records.")


if __name__ == "__main__":
    main()
