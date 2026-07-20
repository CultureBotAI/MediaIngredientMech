#!/usr/bin/env python3
"""Audit ingredient role facets for chemically-implausible assignments.

Most roles come from precise inference (synonym `Role:` text, CHEBI ancestry, or
curated name lists) and are self-consistent. The exception is roles imported from
CultureMech `Role:` synonym annotations, which occasionally carry source errors
(e.g. MgSO4 tagged BUFFER). This flags any assignment whose ingredient name matches
NONE of the plausible-name tokens for its assigned role — candidates for review.

It is a heuristic flagger for humans, not an auto-fixer. Run after role changes.

Usage:
    python scripts/audit_role_plausibility.py
"""

import re
import sys
from pathlib import Path

import yaml

sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from mediaingredientmech.utils.role_iteration import FACET_ROLE_SLOTS, iter_role_assignments

DATA = Path("data/curated/mapped_ingredients.yaml")

# Per-role plausible-name tokens, matched by role name across all three role
# facets. Only NARROW-definition roles are audited: their chemistry is specific
# enough that a name matching none of these tokens is a real red flag.
# CARBON_SOURCE / MINERAL_SOURCE / NITROGEN_SOURCE / ENERGY_SOURCE
# are intentionally NOT audited — they span too many chemical classes (sugars,
# acids, alcohols, hydrocarbons, amines, polysaccharides, salts, ...) for a
# name-token rule to be meaningful.
PLAUSIBLE = {
    # acetate/citrate/succinate/glycine are legitimate buffer systems.
    "BUFFER": r"(HEPES|MOPS|MES|PIPES|TRICINE|BICINE|TAPS|CAPS|\bTES\b|EPPS|ACES|"
              r"\bTris\b|morpholino|piperazine|buffer|bicarbonate|carbonate|"
              r"phosphate|HCO3|CO3|PO4|citrate|acet(ate|ic)|succin|glycine|"
              r"glycylglycine|borate|barbital|cacodylate|imidazole|maleate|"
              r"aminoethanesulfonic|tetraborate|B4O7|\bMOPSO\b)",
    "SOLIDIFYING_AGENT": r"(agar|agarose|gellan|gelrite|gelzan|phytagel|carrageenan|"
                         r"alginate|gelatin)",
    "REDUCING_AGENT": r"(sulfide|sulphide|dithionite|dithiothreitol|\bDTT\b|mercapto|"
                      r"thioglycol|\bTCEP\b|cysteine|sulfite|sulphite|ascorb|"
                      r"titanium|thiosulf|\bNa2S\b|SO3|S2O3|S2O4|S2O5)",
    # `nitrilotriacet` (not `...acetic`) so the anion form `Nitrilotriacetate`
    # matches alongside `Nitrilotriacetic acid`.
    "CHELATOR": r"(EDTA|EGTA|DTPA|nitrilotriacet|\bNTA\b|desferri|deferox|chelat|"
                r"dipyrid|bipyrid|phenanthroline|enterobactin|siderophore|"
                r"pyrophosphate|tetrakis|pyridylmethyl)",
    "VITAMIN_SOURCE": r"(vitamin|biotin|thiamin|riboflavin|niacin|nicotin|pyridox|"
                      r"cobalamin|folic|folate|folin|pantothen|lipoic|thioctic|"
                      r"menaquinone|menadione|aminobenzo|\bPABA\b|inositol|ascorb|"
                      r"tocopherol|retinol|calciferol|hemin|haemin|protoporphyrin|"
                      r"carnitin|\bFAD\b|\bNAD\b|coenzyme|cobamide|pteroyl)",
    # standard 20 + common non-proteinogenic amino acids (CHEBI's "amino acid"
    # class, which the ancestry rule uses, is broader than the proteinogenic set).
    "AMINO_ACID_SOURCE": r"(alanine|arginine|asparagin|aspart|cysteine|cystine|"
                         r"glutam|glycine|histidine|isoleucine|leucine|lysine|"
                         r"methionine|phenylalanine|proline|serine|threonine|"
                         r"tryptophan|tyrosine|valine|ornithine|citrulline|"
                         r"amino.*acid|amino.*caproic|aminobutyr|aminovaleric|"
                         r"aminolevulinic|aminosalicylic|sarcosine|anthranil|"
                         r"alliin|levodopa|\bdopa\b|homoserine|homocysteine|"
                         r"canavanine|ergothioneine|aminocyclopropane|carboxylate)",
    "PROTEIN_SOURCE": r"(peptone|tryptone|tryptose|trypticase|casitone|casamino|"
                      r"casein|hydrolysate|digest|extract|infusion|\bbeef\b|yeast|"
                      r"liver|gelatin|proteose|lysate|albumin|mucin|collagen|serum|"
                      r"protein|brain heart|\bBHI\b)",
}


def find_implausible(data: dict) -> list[tuple[str, str, str, str, list[str]]]:
    """Return (role, slot, name, identifier, sources) for assignments whose name matches
    none of the plausible-name tokens for the assigned (narrow-definition) role."""
    flagged = []
    for r in data["ingredients"]:
        name = r.get("preferred_term", "")
        for slot, m in iter_role_assignments(r, slots=FACET_ROLE_SLOTS):
            role = m.get("role")
            pat = PLAUSIBLE.get(role)
            if pat and not re.search(pat, name, re.I):
                srcs = sorted(
                    {
                        e.get("source") or e.get("reference_text", "")[:40]
                        for e in m.get("evidence", [])
                    }
                )
                flagged.append((role, slot, name, r["identifier"], srcs))
    return flagged


def main() -> int:
    data = yaml.safe_load(DATA.read_text())
    flagged = find_implausible(data)

    print(f"Audited roles with plausibility rules: {sorted(PLAUSIBLE)}")
    print(f"Flagged (name matches no plausible token for its role): {len(flagged)}\n")
    for role, slot, name, ident, srcs in sorted(flagged):
        print(f"  [{role} in {slot}] {name!r} ({ident})  <= {srcs}")
    return 1 if flagged else 0


if __name__ == "__main__":
    sys.exit(main())
