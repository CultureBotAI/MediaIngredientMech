#!/usr/bin/env python3
"""Drop specific chemically-implausible media_role assignments (with audit trail).

Some roles were imported from CultureMech `Role:` synonym annotations that carry
source errors (surfaced by scripts/audit_role_plausibility.py). This removes the
listed (preferred_term, identifier, role) assignments and records a CORRECTED
curation_history event. Idempotent: a role already absent is skipped.

Usage:
    python scripts/drop_implausible_roles.py [--dry-run]
"""

import argparse
import sys
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from mediaingredientmech.curation.ingredient_curator import IngredientCurator

# (preferred_term, identifier, role, reason)
DROPS = [
    (
        "MgSO4·7H2O",
        "CHEBI:32599",
        "BUFFER",
        "MgSO4 is a magnesium-sulfate mineral salt, not a pH buffer; the BUFFER role "
        "came from an erroneous CultureMech source synonym. MINERAL role retained.",
    ),
    (
        "EDTA (acid form)",
        "CHEBI:4735",
        "AMINO_ACID_SOURCE",
        "EDTA is a polyamino-polycarboxylic chelator, not an amino-acid nutrient "
        "source; the CHEBI 'amino acid' ancestry rule over-matched it. After this "
        "drop the name-list pass re-tags it CHELATOR.",
    ),
]


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    curator = IngredientCurator(
        data_path=Path("data/curated/mapped_ingredients.yaml"),
        curator_name="drop_implausible_roles",
    )
    curator.load()
    ts = datetime.now(timezone.utc).isoformat()
    by_key = {(r.get("preferred_term"), r.get("identifier")): r for r in curator.records}

    n = 0
    for pt, ident, role, reason in DROPS:
        record = by_key.get((pt, ident))
        if record is None:
            print(f"  SKIP: no record {pt!r} ({ident})")
            continue
        roles = record.get("media_roles", [])
        kept = [m for m in roles if m.get("role") != role]
        if len(kept) == len(roles):
            print(f"  SKIP: {pt!r} has no {role} role")
            continue
        record["media_roles"] = kept
        record.setdefault("curation_history", []).append(
            {
                "timestamp": ts,
                "curator": "drop_implausible_roles",
                "action": "CORRECTED",
                "changes": f"Removed implausible media_role {role}: {reason}",
                "llm_assisted": False,
            }
        )
        print(f"  {pt}: dropped {role}")
        n += 1

    if not args.dry_run:
        curator.save()
        print(f"\nSaved; dropped {n} role(s).")
    else:
        print(f"\n[dry-run] would drop {n} role(s).")


if __name__ == "__main__":
    main()
