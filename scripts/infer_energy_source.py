#!/usr/bin/env python3
"""Add an ENERGY_SOURCE dimension to canonical energy substrates.

media_roles currently carry a single functional axis; most catabolic substrates
are tagged only CARBON_SOURCE. This adds ENERGY_SOURCE as a SECOND role to the
textbook fermentable/respirable energy substrates that already hold CARBON_SOURCE
— glycolytic/TCA organic acids, common fermentable sugars, and ethanol/glycerol.

Deliberately conservative: only substrates microbiologists routinely describe as
energy sources are included, so ENERGY_SOURCE stays meaningful rather than being
stamped on every carbon-bearing compound. Records are required to already have a
CARBON_SOURCE role (so we only add the second axis to confirmed carbon sources).
Idempotent: a record already carrying ENERGY_SOURCE is skipped.

Usage:
    python scripts/infer_energy_source.py [--dry-run]
"""

import argparse
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from mediaingredientmech.curation.ingredient_curator import IngredientCurator

# Canonical energy substrates (word-boundaried). Acids match -ate/-ic forms.
ENERGY = re.compile(
    r"\b("
    # glycolytic / TCA / fermentation acids
    r"acet(ate|ic)|lact(ate|ic)|pyruv(ate|ic)|succin(ate|ic)|fumar(ate|ic)|"
    r"mal(ate|ic)|citr(ate|ic)|propion(ate|ic)|butyr(ate|ic)|form(ate|ic)|"
    r"glucon(ate|ic)|oxoglutar(ate|ic)|ketoglutar(ate|ic)|"
    # common fermentable sugars
    r"glucose|fructose|galactose|mannose|sucrose|maltose|lactose|trehalose|"
    r"cellobiose|xylose|arabinose|ribose|"
    # alcohols
    r"ethanol|glycerol"
    r")\b",
    re.I,
)
# Don't treat non-metabolizable analogs / esters as energy substrates:
# sugar phosphates, fatty-acid esters, and non-metabolizable glucose analogs
# (2-deoxyglucose, 3-O-methylglucose — transport tracers, not catabolized).
ENERGY_EXCL = re.compile(
    r"(phosphate|oleate|stearate|palmitate|monostearate|deoxy|o-methyl)", re.I
)


def is_energy_substrate(name: str) -> bool:
    return bool(ENERGY.search(name)) and not ENERGY_EXCL.search(name)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    curator = IngredientCurator(
        data_path=Path("data/curated/mapped_ingredients.yaml"),
        curator_name="infer_energy_source",
    )
    curator.load()

    added = []
    for record in curator.records:
        roles = {m.get("role") for m in record.get("media_roles", [])}
        if "CARBON_SOURCE" not in roles or "ENERGY_SOURCE" in roles:
            continue
        if not is_energy_substrate(record.get("preferred_term", "")):
            continue
        added.append(record["preferred_term"])
        if not args.dry_run:
            curator.add_media_role(
                record,
                role="ENERGY_SOURCE",
                confidence=0.7,
                reference_text="Canonical energy substrate (catabolised for energy)",
                reference_type="COMPUTATIONAL_PREDICTION",
                curator_note="Provisional ENERGY_SOURCE added alongside CARBON_SOURCE; review recommended.",
            )

    if not args.dry_run:
        curator.save()

    print(f"ENERGY_SOURCE added to {len(added)} records" + (" (DRY RUN)" if args.dry_run else ""))
    for x in sorted(added):
        print("  ", x)


if __name__ == "__main__":
    main()
