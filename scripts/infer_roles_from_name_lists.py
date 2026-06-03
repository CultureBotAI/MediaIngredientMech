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

# Ordered (role, include pattern, exclude pattern). First include-match whose
# exclude pattern does NOT also match wins. Order encodes precedence.
_ANTIBIOTIC = (
    r"(cillin\b|mycin\b|micin\b|cycline\b|floxacin\b|oxacin\b|^cef|^ceph|penem\b|"
    r"bactam\b|chloramphenicol|rifam|vancomycin|teicoplanin|bacitracin|polymyxin|"
    r"colistin|nystatin|amphotericin|nalidixic|trimethoprim|sulfamethox|"
    r"metronidazole|\bnisin\b|novobiocin|fusidic|puromycin|geneticin|hygromycin|"
    r"blasticidin|carbenicillin|cycloheximide|fosfomycin|aztreonam|linezolid|"
    r"daptomycin|tylosin|thiostrepton|actinomycin|antimycin|bleomycin|apramycin|"
    r"spectinomycin|tetracycline|erythromycin|clindamycin|nourseothricin|"
    r"carbamyl.{0,2}serine)"
)
_CHELATOR = (
    r"(\bEDTA\b|ethylenediaminetetraacetic|nitrilotriacetic acid|\bNTA\b|"
    r"\bEGTA\b|\bDTPA\b|desferrioxamine|deferoxamine)"
)
# Metal-chelate complexes are iron/trace sources, not chelators.
_CHELATE_COMPLEX = r"(Fe|ferric|ferrous|Mg-|Ca-|Zn-|Cu-|Co-|Ni-|sodium ferric)"
_REDUCING = (
    r"(dithionite|dithiothreitol|\bDTT\b|2-mercaptoethanol|thioglycol|"
    r"\bTCEP\b|sodium sulfide|hydrogen sulfide|ammonium sulfide|\bNa2S\b|"
    r"sodium sulfite|titanium.{0,4}citrate)"
)
# Good's buffers + named buffer solutions / Tris.
_BUFFER = (
    r"(\bHEPES\b|\bMOPS\b|\bMOPSO\b|\bMES\b|\bPIPES\b|\bTRICINE\b|\bBICINE\b|"
    r"\bTAPS\b|\bTAPSO\b|\bCAPS\b|\bTES\b|\bEPPS\b|\bHEPPS\b|Bis-Tris|\bTris\b|"
    r"\bACES\b|buffer\b)"
)
# Gelling agents. Restricted to pure agar forms (whole name) + named gels, so
# agar-containing complete media ("Brucella agar", "Malt Extract Agar") are NOT
# caught — those are defined media, not a single gelling-agent ingredient.
_SOLIDIFYING = (
    r"(agarose|gellan|gelrite|gelzan|phytagel|"
    r"^(bacto[ -]|noble[ -]|granulated[ -]|purified[ -])?agar([ -]agar)?$)"
)
# Protein/nitrogen-rich complex sources. Bare "extract" is avoided (malt extract
# is a carbon source); only protein-bearing extracts are listed explicitly.
# "liver" is start-anchored so "Glycogen from bovine liver" (a carbon source) is
# not caught; complete media (broth/agar) are excluded as defined media.
_PROTEIN = (
    r"(peptone|tryptone|tryptose|trypticase|casitone|casamino|casein|"
    r"hydrolysate|\bdigest\b|yeast extract|beef extract|meat extract|"
    r"brain heart infusion|\bBHI\b|^liver|gelatin|proteose|lysate|\bbeef\b|"
    r"baker.?s yeast|tryptic soy)"
)
_PROTEIN_EXCL = r"(broth|\bagar\b)"
# Amino acids: name must START with the (optionally L/D/DL-prefixed) amino acid,
# so conjugates ("Fructose-asparagine"), acyl-homoserine lactones, polymers and
# modified residues ("4-benzoyl-L-phenylalanine") are not caught.
_AMINO_ACID = (
    r"^(L-|D-|DL-)?(alanine|arginine|asparagine|aspartic acid|aspartate|"
    r"cysteine|cystine|glutamic acid|glutamate|glutamine|glycine|histidine|"
    r"isoleucine|leucine|lysine|methionine|phenylalanine|proline|serine|"
    r"threonine|tryptophan|tyrosine|valine|ornithine|citrulline)\b"
)
_AMINO_ACID_EXCL = r"(lactone|\bpoly|peptide|imidazolium|hydroxamate|hydroxamic)"
_VITAMIN = (
    r"(\bbiotin\b|thiamine|thiamin\b|riboflavin|niacin|nicotinamide|"
    r"nicotinic acid|pyridoxine|pyridoxal|pyridoxamine|cobalamin|folic acid|"
    r"\bfolate\b|folinic|pantothenate|pantothenic|lipoic acid|thioctic|"
    r"menaquinone|menadione|aminobenzoic|\bPABA\b|inositol|vitamin)"
)
# Antivitamins / oxidized derivatives / antagonists / phospholipids that merely
# contain "inositol" are not vitamin sources.
_VITAMIN_EXCL = r"(deoxy|N-oxide|\banti|phosphatidyl)"
# Inorganic salts of nutrient metals, matched by formula prefix (avoids the
# azide/dithionite/oxidizer false positives of a broad "inorganic salt" rule).
_MINERAL = (
    r"^(MgSO4|MgCl2|MnSO4|MnCl2|CuSO4|CuCl|FeSO4|FeCl2|FeCl3|CoCl2|CoSO4|"
    r"NiCl2|NiSO4|ZnSO4|ZnCl2|CaCl2|CaSO4|K2SO4|KCl\b|Na2SO4|Na2MoO4|Na2WO4|"
    r"H3BO3|boric acid)"
)
# Carbohydrate carbon sources (sugars + polysaccharides).
_CARBON = (
    r"(ose\b|oligosaccharide|polysaccharide|dextrin|dextran|starch|glycogen|"
    r"cellulose|inulin|\bpectin|glucan|mannan|xylan|chitin|chitosan|"
    r"maltodextrin|glycerol|\bmalt\b|fructo-?oligo|galacto-?oligo|\bFOS\b|\bGOS\b)"
)
# Not metabolic carbon-source ingredients despite matching a sugar/polysaccharide
# token: endotoxin (lipopolysaccharide), glycerol fatty-acid esters (emulsifiers),
# and complete media ("malt extract agar/broth").
_CARBON_EXCL = r"(lipopolysaccharide|oleate|stearate|palmitate|broth|\bagar\b)"

# (role, include_rx, exclude_rx | None) in precedence order.
RULES = [
    ("SELECTIVE_AGENT", re.compile(_ANTIBIOTIC, re.I), None),
    ("CHELATOR", re.compile(_CHELATOR, re.I), re.compile(_CHELATE_COMPLEX, re.I)),
    ("REDUCING_AGENT", re.compile(_REDUCING, re.I), None),
    ("BUFFER", re.compile(_BUFFER, re.I), None),
    ("SOLIDIFYING_AGENT", re.compile(_SOLIDIFYING, re.I), None),
    ("PROTEIN_SOURCE", re.compile(_PROTEIN, re.I), re.compile(_PROTEIN_EXCL, re.I)),
    ("AMINO_ACID_SOURCE", re.compile(_AMINO_ACID, re.I), re.compile(_AMINO_ACID_EXCL, re.I)),
    ("VITAMIN_SOURCE", re.compile(_VITAMIN, re.I), re.compile(_VITAMIN_EXCL, re.I)),
    ("MINERAL", re.compile(_MINERAL, re.I), None),
    ("CARBON_SOURCE", re.compile(_CARBON, re.I), re.compile(_CARBON_EXCL, re.I)),
]


def infer_role(name: str) -> str | None:
    for role, include_rx, exclude_rx in RULES:
        if not include_rx.search(name):
            continue
        if exclude_rx is not None and exclude_rx.search(name):
            return None  # matched the category but hit its exclusion guard
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
