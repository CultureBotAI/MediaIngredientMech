#!/usr/bin/env python3
"""Infer media_roles for role-less MAPPED ingredients from curated name patterns.

Complements the structural CHEBI-ancestry pass (``infer_roles_from_chebi.py``),
which deliberately skips SELECTIVE_AGENT / MINERAL / REDUCING_AGENT / CHELATOR
because CHEBI's structural class does not determine the media role. Here we use
hand-curated, high-precision name patterns instead — each chosen so a match is
overwhelmingly likely to play that exact role in a growth medium.

Precision choices:
  * SELECTIVE_AGENT: antibiotic-class name patterns (-cillin/-mycin/-cycline/
    cef-/-floxacin/-penem/... + explicit names). Antibiotics in a medium are
    selective agents.
  * CHELATOR: only FREE chelators (EDTA / NTA / EGTA / DTPA / desferrioxamine).
    Metal-chelate complexes (Fe-EDTA, ferric citrate) are excluded — their media
    role is an iron/trace source, not chelation. Citrate is excluded (ambiguous:
    carbon source / buffer / chelator).
  * REDUCING_AGENT: specific anaerobic reductants (dithionite, dithiothreitol,
    2-mercaptoethanol, thioglycolate, sodium/hydrogen/ammonium sulfide, TCEP).
    Cysteine and volatile organosulfides are excluded (ambiguous / not reductant
    additives).
  * MINERAL: inorganic salts of nutrient metals, matched by formula prefix
    (MgSO4, MnCl2, CuSO4, FeSO4, CoCl2, NiSO4, ZnSO4, CaCl2, K2SO4, Na2MoO4, ...).
    Anchoring on the metal-salt formula avoids the azide/dithionite/oxidizer
    false positives that the broad "inorganic salt" CHEBI class would catch.

One role per record (first match by the precedence below). Idempotent: records
that already carry any media_role are skipped. Assignments are provisional —
confidence 0.8, reference_type COMPUTATIONAL_PREDICTION, curator
``infer_roles_from_name_lists``.

Usage:
    python scripts/infer_roles_from_name_lists.py [--dry-run]
"""

import argparse
import re
import sys
from collections import Counter
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from mediaingredientmech.curation.ingredient_curator import IngredientCurator

# Ordered (role, compiled pattern). First match wins.
_ANTIBIOTIC = (
    r"(cillin\b|mycin\b|micin\b|cycline\b|floxacin\b|oxacin\b|^cef|^ceph|penem\b|"
    r"bactam\b|chloramphenicol|rifam|vancomycin|teicoplanin|bacitracin|polymyxin|"
    r"colistin|nystatin|amphotericin|nalidixic|trimethoprim|sulfamethox|"
    r"metronidazole|\bnisin\b|novobiocin|fusidic|puromycin|geneticin|hygromycin|"
    r"blasticidin|carbenicillin|cycloheximide|fosfomycin|aztreonam|linezolid|"
    r"daptomycin|tylosin|thiostrepton|actinomycin|antimycin|bleomycin|apramycin|"
    r"spectinomycin|tetracycline|erythromycin|clindamycin|nourseothricin)"
)
_CHELATOR = (
    r"(\bEDTA\b|ethylenediaminetetraacetic|nitrilotriacetic acid|\bNTA\b|"
    r"\bEGTA\b|\bDTPA\b|desferrioxamine|deferoxamine)"
)
# Exclude metal-chelate complexes from CHELATOR (iron/trace sources, not chelators).
_CHELATE_COMPLEX = r"(Fe|ferric|ferrous|Mg-|Ca-|Zn-|Cu-|Co-|Ni-|sodium ferric)"
_REDUCING = (
    r"(dithionite|dithiothreitol|\bDTT\b|2-mercaptoethanol|thioglycol|"
    r"\bTCEP\b|sodium sulfide|hydrogen sulfide|ammonium sulfide|\bNa2S\b|"
    r"sodium sulfite|titanium.{0,4}citrate)"
)
_MINERAL = (
    r"^(MgSO4|MgCl2|MnSO4|MnCl2|CuSO4|CuCl|FeSO4|FeCl2|FeCl3|CoCl2|CoSO4|"
    r"NiCl2|NiSO4|ZnSO4|ZnCl2|CaCl2|CaSO4|K2SO4|KCl\b|Na2SO4|Na2MoO4|Na2WO4|"
    r"H3BO3|boric acid)"
)

RULES = [
    ("SELECTIVE_AGENT", re.compile(_ANTIBIOTIC, re.I)),
    ("CHELATOR", re.compile(_CHELATOR, re.I)),
    ("REDUCING_AGENT", re.compile(_REDUCING, re.I)),
    ("MINERAL", re.compile(_MINERAL, re.I)),
]
_CHELATE_RX = re.compile(_CHELATE_COMPLEX, re.I)


def infer_role(name: str) -> str | None:
    for role, rx in RULES:
        if not rx.search(name):
            continue
        if role == "CHELATOR" and _CHELATE_RX.search(name):
            return None  # metal-chelate complex: iron/trace source, not a chelator
        return role
    return None


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    curator = IngredientCurator(
        data_path=Path("data/curated/mapped_ingredients.yaml"),
        curator_name="infer_roles_from_name_lists",
    )
    curator.load()

    dist = Counter()
    examples: dict[str, list[str]] = {}
    for record in curator.records:
        if record.get("mapping_status") != "MAPPED" or record.get("media_roles"):
            continue
        role = infer_role(record.get("preferred_term", ""))
        if not role:
            continue
        dist[role] += 1
        examples.setdefault(role, []).append(record["preferred_term"])
        if not args.dry_run:
            curator.add_media_role(
                record,
                role=role,
                confidence=0.8,
                reference_text="Inferred from curated media-role name pattern",
                reference_type="COMPUTATIONAL_PREDICTION",
                curator_note="Provisional role from a curated name-pattern rule; review recommended.",
            )

    if not args.dry_run:
        curator.save()

    print("NAME-LIST ROLE INFERENCE" + (" (DRY RUN)" if args.dry_run else ""))
    print(f"assigned: {sum(dist.values())}")
    for role, n in dist.most_common():
        print(f"  {role:18s} {n}  e.g. {examples[role][:5]}")


if __name__ == "__main__":
    main()
