#!/usr/bin/env python3
"""Infer media_roles for CHEBI-mapped ingredients from CHEBI ancestry.

Synonym-based extraction (``extract_roles_from_synonyms.py``) only covers
ingredients carrying a CultureMech ``Role:`` annotation (~15%). This script
broadens coverage for the remaining CHEBI-mapped chemicals by walking the
CHEBI is_a + has_role ancestor closure (via the local OAK sqlite adapter) and
assigning a single, high-precision role per ingredient.

Design choices for precision (the goal is zero mis-tags, not max coverage):
  * Only authoritative, unambiguous structural ancestor classes are used:
    carbohydrate -> CARBON_SOURCE, amino acid -> AMINO_ACID_SOURCE,
    vitamin (role) -> VITAMIN_SOURCE. These map cleanly from CHEBI structure to
    media role with no observed functional false positives.
  * Exactly one role is assigned per record (first match by precedence).
  * Several tempting rules are intentionally NOT inferred because CHEBI's
    structural/role class does not determine the media role:
      - SELECTIVE_AGENT (CHEBI:33281 antimicrobial agent): captures non-selective
        compounds like short-chain alcohols. Use a curated antibiotic name list.
      - MINERAL (CHEBI:24839 inorganic salt): captures functional non-minerals —
        sodium azide (selective agent), dithionite/sulfite/thiosulfate (reducing
        agents / electron donors), hypochlorite/arsenite/chromate (toxic inhibitors).
      - COFACTOR_PROVIDER (CHEBI:23357 cofactor): captures hydrogen peroxide,
        hydroquinone, pyruvate.
  * The one inorganic-salt case kept is the unambiguous ammonium-salt ->
    NITROGEN_SOURCE mapping (ammonium is always a nitrogen source).

Assignments are written with confidence 0.7 and reference_type
COMPUTATIONAL_PREDICTION under curator ``infer_roles_from_chebi_ancestry`` so
they are easy to review and reverse, and clearly distinct from the higher-
confidence synonym-derived roles.

Usage:
    python scripts/infer_roles_from_chebi.py --dry-run
    python scripts/infer_roles_from_chebi.py
"""

import argparse
import sys
from collections import Counter
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from mediaingredientmech.curation.ingredient_curator import IngredientCurator

CHEBI_DB = "sqlite:///Users/marcin/.data/oaklib/chebi.db"
HAS_ROLE = "RO:0000087"

# (role, ancestor CHEBI class) in precedence order — first match wins.
RULES = [
    ("VITAMIN_SOURCE", "CHEBI:33229"),     # vitamin (role)
    ("AMINO_ACID_SOURCE", "CHEBI:33709"),  # amino acid
    ("CARBON_SOURCE", "CHEBI:16646"),      # carbohydrate
]
ANCESTOR_LABELS = {
    "CHEBI:33229": "vitamin (role)",
    "CHEBI:33709": "amino acid",
    "CHEBI:16646": "carbohydrate",
}
# Inorganic salt class used only for the unambiguous ammonium -> NITROGEN_SOURCE case.
INORGANIC_SALT = "CHEBI:24839"


def infer_role(ancestors: set[str], name: str) -> tuple[str | None, str | None]:
    """Return (role, justifying_ancestor) for a CHEBI ancestor set, or (None, None)."""
    for role, anc in RULES:
        if anc in ancestors:
            return role, f"{anc} ({ANCESTOR_LABELS[anc]})"
    # Ammonium salts are unambiguously nitrogen sources.
    if INORGANIC_SALT in ancestors and "ammonium" in name.lower():
        return "NITROGEN_SOURCE", f"{INORGANIC_SALT} (inorganic ammonium salt)"
    return None, None


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dry-run", action="store_true", help="Preview without saving")
    args = parser.parse_args()

    from oaklib import get_adapter
    from oaklib.datamodels.vocabulary import IS_A

    print("Loading CHEBI adapter...")
    adapter = get_adapter(CHEBI_DB)

    curator = IngredientCurator(
        data_path=Path("data/curated/mapped_ingredients.yaml"),
        curator_name="infer_roles_from_chebi_ancestry",
    )
    curator.load()

    targets = [
        r
        for r in curator.records
        if r.get("mapping_status") == "MAPPED"
        and not r.get("media_roles")
        and (r.get("ontology_mapping") or {}).get("ontology_source") == "CHEBI"
        and str(r["identifier"]).startswith("CHEBI:")
    ]
    print(f"CHEBI role-less targets: {len(targets)}")

    dist = Counter()
    assigned = 0
    errors = 0
    for i, record in enumerate(targets, 1):
        if i % 200 == 0:
            print(f"  processed {i}/{len(targets)}...")
        cid = record["identifier"]
        try:
            ancestors = set(adapter.ancestors(cid, predicates=[IS_A, HAS_ROLE]))
        except Exception:
            errors += 1
            continue
        role, justification = infer_role(ancestors, record.get("preferred_term", ""))
        if not role:
            continue
        assigned += 1
        dist[role] += 1
        if not args.dry_run:
            curator.add_media_role(
                record,
                role=role,
                confidence=0.7,
                reference_text=f"Inferred from CHEBI ancestry: subclass/has_role of {justification}",
                reference_type="COMPUTATIONAL_PREDICTION",
                curator_note=(
                    "Provisional role inferred from CHEBI is_a/has_role closure; "
                    "review recommended."
                ),
            )

    if not args.dry_run:
        print("\nSaving updated records...")
        curator.save()

    print("\n" + "=" * 60)
    print("CHEBI ANCESTRY ROLE INFERENCE" + (" (DRY RUN)" if args.dry_run else ""))
    print("=" * 60)
    print(f"Targets: {len(targets)} | assigned: {assigned} | lookup errors: {errors}")
    for role, n in dist.most_common():
        print(f"  {role:20s} {n}")


if __name__ == "__main__":
    main()
