#!/usr/bin/env python3
"""Infer ingredient role facets for CHEBI-mapped ingredients from CHEBI ancestry.

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
      - MINERAL_SOURCE (CHEBI:24839 inorganic salt): captures functional non-minerals —
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

The CHEBI adapter URI defaults to the standard OAK semsql cache
(``~/.data/oaklib/chebi.db``), resolved portably via ``Path.home()`` so it
works for any user who has that cache. Override with ``--chebi-db`` or the
``CHEBI_DB`` environment variable; pass ``--chebi-db sqlite:obo:chebi`` to let
OAK download CHEBI if you do not already have the local copy.

Usage:
    python scripts/infer_roles_from_chebi.py --dry-run
    python scripts/infer_roles_from_chebi.py
    python scripts/infer_roles_from_chebi.py --chebi-db sqlite:obo:chebi
"""

import argparse
import os
import sys
from collections import Counter
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from mediaingredientmech.curation.ingredient_curator import IngredientCurator
from mediaingredientmech.utils.role_facets import add_role
from mediaingredientmech.utils.role_iteration import FACET_ROLE_SLOTS, iter_role_assignments

# Default to the standard OAK semsql cache location, resolved portably from the
# user's home dir (reuses an existing local copy without re-downloading).
# Overridable via --chebi-db or $CHEBI_DB; use sqlite:obo:chebi to download.
DEFAULT_CHEBI_DB = os.environ.get(
    "CHEBI_DB", f"sqlite:///{Path.home() / '.data' / 'oaklib' / 'chebi.db'}"
)
HAS_ROLE = "RO:0000087"

# (role, ancestor CHEBI class) in precedence order — first match wins.
# The first three are STRUCTURAL is_a classes (what the molecule is); the last
# three are CHEBI has_role functional annotations (what it does). has_role buffer/
# chelator/surfactant are precise, curator-meaningful media roles — unlike the
# broad has_role classes that stay EXCLUDED (antimicrobial agent CHEBI:33281
# captures short-chain alcohols; antioxidant CHEBI:22586 captures non-reductant
# polyphenols; food additive is not a media role). Structural rules take
# precedence so a carbohydrate that also chelates stays CARBON_SOURCE.
RULES = [
    ("VITAMIN_SOURCE", "CHEBI:33229"),     # vitamin (role)
    ("AMINO_ACID_SOURCE", "CHEBI:33709"),  # amino acid
    ("CARBON_SOURCE", "CHEBI:16646"),      # carbohydrate
    ("BUFFER", "CHEBI:35225"),             # buffer (has_role)
    ("CHELATOR", "CHEBI:38161"),           # chelator (has_role)
    ("SURFACTANT", "CHEBI:35195"),         # surfactant (has_role)
]
ANCESTOR_LABELS = {
    "CHEBI:33229": "vitamin (role)",
    "CHEBI:33709": "amino acid",
    "CHEBI:16646": "carbohydrate",
    "CHEBI:35225": "buffer (role)",
    "CHEBI:38161": "chelator (role)",
    "CHEBI:35195": "surfactant (role)",
}
# Inorganic salt class used only for the unambiguous ammonium -> NITROGEN_SOURCE case.
INORGANIC_SALT = "CHEBI:24839"

# CHEBI has_role chelator is authoritative for in-vitro metal binding but is not a
# reliable MEDIA role for these: flavonoid/polyphenol antioxidants (curcumin,
# quercetin, theaflavin) chelate in vitro yet are used as substrates/antimicrobials,
# and TEMED is a polymerisation catalyst. Excluded so CHELATOR stays media-precise
# (mirrors the script's existing exclusion of the broad antimicrobial/inorganic
# classes). Keyed by role -> CHEBI ids to drop even when the has_role rule matches.
HAS_ROLE_EXCLUDE = {
    "CHELATOR": {"CHEBI:3962", "CHEBI:16243", "CHEBI:136609", "CHEBI:32850"},
}


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
    parser.add_argument(
        "--chebi-db",
        default=DEFAULT_CHEBI_DB,
        help=f"OAK adapter URI for CHEBI (default: {DEFAULT_CHEBI_DB!r}; "
        "or set $CHEBI_DB). Use e.g. sqlite:///path/to/chebi.db for a local copy.",
    )
    args = parser.parse_args()

    from oaklib import get_adapter
    from oaklib.datamodels.vocabulary import IS_A

    print(f"Loading CHEBI adapter ({args.chebi_db})...")
    adapter = get_adapter(args.chebi_db)

    curator = IngredientCurator(
        data_path=Path("data/curated/mapped_ingredients.yaml"),
        curator_name="infer_roles_from_chebi_ancestry",
    )
    curator.load()

    targets = [
        r
        for r in curator.records
        if r.get("mapping_status") == "MAPPED"
        and not any(iter_role_assignments(r, slots=FACET_ROLE_SLOTS))
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
        if cid in HAS_ROLE_EXCLUDE.get(role, ()):
            continue  # has_role matches but this id is a curated media false-positive
        assigned += 1
        dist[role] += 1
        if not args.dry_run:
            add_role(
                curator,
                record,
                role,
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
