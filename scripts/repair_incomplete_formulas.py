#!/usr/bin/env python3
"""Attempt to repair incomplete chemical formulas.

Strategy:
1. Generate possible complete formulas based on chemical patterns
2. Check against existing mapped ingredients
3. Search for candidates in CHEBI
4. Rank by likelihood using context (synonyms, CAS numbers, roles)
"""

import re
from pathlib import Path
from typing import List, Dict, Any
import yaml

# Paths
DATA_DIR = Path(__file__).parent.parent / "data" / "curated"
UNMAPPED_PATH = DATA_DIR / "unmapped_ingredients.yaml"
MAPPED_PATH = DATA_DIR / "mapped_ingredients.yaml"


def load_yaml(path):
    """Load YAML file."""
    with open(path, encoding="utf-8") as f:
        return yaml.safe_load(f)


def generate_formula_candidates(incomplete: str) -> List[Dict[str, str]]:
    """Generate possible complete formulas for an incomplete formula.

    Returns:
        List of dicts with 'formula', 'name', 'chebi_id', 'likelihood'
    """
    candidates = []

    # Known patterns and completions
    completions = {
        # Nitrates and nitrites
        "NaNO": [
            {"formula": "NaNO3", "name": "sodium nitrate", "chebi": "CHEBI:34218", "likelihood": "HIGH",
             "reason": "Nitrate (NO3) more common than nitrite (NO2) in media"},
            {"formula": "NaNO2", "name": "sodium nitrite", "chebi": "CHEBI:78870", "likelihood": "LOW",
             "reason": "Nitrite less common in growth media"},
        ],
        "KNO": [
            {"formula": "KNO3", "name": "potassium nitrate", "chebi": "CHEBI:63043", "likelihood": "HIGH",
             "reason": "Common nitrogen source in minimal media"},
            {"formula": "KNO2", "name": "potassium nitrite", "chebi": "CHEBI:63044", "likelihood": "LOW",
             "reason": "Nitrite rarely used"},
        ],
        "NH4NO": [
            {"formula": "NH4NO3", "name": "ammonium nitrate", "chebi": "CHEBI:63038", "likelihood": "HIGH",
             "reason": "Common nitrogen source"},
        ],

        # Phosphates
        "K2HPO": [
            {"formula": "K2HPO4", "name": "dipotassium hydrogen phosphate", "chebi": "CHEBI:32030", "likelihood": "HIGH",
             "reason": "Common phosphate buffer, K2HPO4 is standard dibasic form"},
        ],
        "KH2PO": [
            {"formula": "KH2PO4", "name": "potassium dihydrogen phosphate", "chebi": "CHEBI:32583", "likelihood": "HIGH",
             "reason": "Common phosphate buffer, monobasic form"},
        ],
        "NH4MgPO": [
            {"formula": "(NH4)MgPO4", "name": "ammonium magnesium phosphate", "chebi": "CHEBI:90884", "likelihood": "MEDIUM",
             "reason": "Struvite, common in some media"},
            {"formula": "NH4MgPO4·6H2O", "name": "ammonium magnesium phosphate hexahydrate", "chebi": "?", "likelihood": "MEDIUM",
             "reason": "Hydrated form"},
        ],

        # Carbonates
        "MgCO": [
            {"formula": "MgCO3", "name": "magnesium carbonate", "chebi": "CHEBI:6611", "likelihood": "HIGH",
             "reason": "Standard carbonate form"},
        ],
        "CaCO": [
            {"formula": "CaCO3", "name": "calcium carbonate", "chebi": "CHEBI:3311", "likelihood": "HIGH",
             "reason": "Most common calcium carbonate form"},
        ],
        "Na2CO": [
            {"formula": "Na2CO3", "name": "sodium carbonate", "chebi": "CHEBI:29377", "likelihood": "HIGH",
             "reason": "Common buffer and pH adjuster"},
        ],

        # Bicarbonates
        "NaHCO": [
            {"formula": "NaHCO3", "name": "sodium bicarbonate", "chebi": "CHEBI:32139", "likelihood": "HIGH",
             "reason": "Common buffer and carbon source"},
        ],

        # Borates
        "H3BO": [
            {"formula": "H3BO3", "name": "boric acid", "chebi": "CHEBI:33118", "likelihood": "HIGH",
             "reason": "Common boron source and buffer"},
        ],

        # Single elements (ambiguous)
        "Ca": [
            {"formula": "CaCl2", "name": "calcium chloride", "chebi": "CHEBI:3312", "likelihood": "HIGH",
             "reason": "Most common calcium salt in media"},
            {"formula": "CaCl2·2H2O", "name": "calcium chloride dihydrate", "chebi": "CHEBI:86158", "likelihood": "HIGH",
             "reason": "Common hydrated form"},
            {"formula": "CaSO4", "name": "calcium sulfate", "chebi": "CHEBI:31346", "likelihood": "MEDIUM",
             "reason": "Alternative calcium source"},
            {"formula": "CaCO3", "name": "calcium carbonate", "chebi": "CHEBI:3311", "likelihood": "MEDIUM",
             "reason": "Buffer and calcium source"},
        ],
        "K": [
            {"formula": "KCl", "name": "potassium chloride", "chebi": "CHEBI:32588", "likelihood": "HIGH",
             "reason": "Most common potassium salt"},
            {"formula": "K2HPO4", "name": "dipotassium hydrogen phosphate", "chebi": "CHEBI:32030", "likelihood": "MEDIUM",
             "reason": "Common buffer"},
        ],
        "Mg": [
            {"formula": "MgSO4", "name": "magnesium sulfate", "chebi": "CHEBI:32599", "likelihood": "HIGH",
             "reason": "Most common magnesium source"},
            {"formula": "MgSO4·7H2O", "name": "magnesium sulfate heptahydrate", "chebi": "CHEBI:86354", "likelihood": "HIGH",
             "reason": "Common hydrated form"},
            {"formula": "MgCl2", "name": "magnesium chloride", "chebi": "CHEBI:6636", "likelihood": "MEDIUM",
             "reason": "Alternative magnesium source"},
        ],
        "Na": [
            {"formula": "NaCl", "name": "sodium chloride", "chebi": "CHEBI:26710", "likelihood": "HIGH",
             "reason": "Most common sodium salt"},
            {"formula": "Na2HPO4", "name": "disodium hydrogen phosphate", "chebi": "CHEBI:34683", "likelihood": "MEDIUM",
             "reason": "Common buffer"},
        ],
        "Fe": [
            {"formula": "FeCl3", "name": "ferric chloride", "chebi": "CHEBI:30808", "likelihood": "MEDIUM",
             "reason": "Common iron source (Fe3+)"},
            {"formula": "FeSO4", "name": "ferrous sulfate", "chebi": "CHEBI:30850", "likelihood": "MEDIUM",
             "reason": "Common iron source (Fe2+)"},
            {"formula": "FeSO4·7H2O", "name": "ferrous sulfate heptahydrate", "chebi": "CHEBI:75832", "likelihood": "MEDIUM",
             "reason": "Hydrated ferrous sulfate"},
        ],
        "Zn": [
            {"formula": "ZnSO4", "name": "zinc sulfate", "chebi": "CHEBI:35176", "likelihood": "HIGH",
             "reason": "Most common zinc source"},
            {"formula": "ZnSO4·7H2O", "name": "zinc sulfate heptahydrate", "chebi": "CHEBI:86469", "likelihood": "HIGH",
             "reason": "Common hydrated form"},
            {"formula": "ZnCl2", "name": "zinc chloride", "chebi": "CHEBI:49976", "likelihood": "MEDIUM",
             "reason": "Alternative zinc source"},
        ],
    }

    return completions.get(incomplete, [])


def search_in_mapped(formula: str, mapped_ingredients: List[Dict]) -> List[Dict]:
    """Search for formula in existing mapped ingredients.

    Returns matching records with similarity scores.
    """
    matches = []

    # Normalize formula for matching
    formula_normalized = formula.lower().replace(" ", "")

    for ing in mapped_ingredients:
        # Check preferred term
        term = ing.get("preferred_term", "").lower()

        # Check if formula appears in term
        if formula_normalized in term.replace(" ", ""):
            matches.append({
                "preferred_term": ing["preferred_term"],
                "ontology_id": ing.get("ontology_id"),
                "match_type": "formula_in_term",
                "confidence": "HIGH",
            })
            continue

        # Check synonyms for formula
        for syn in ing.get("synonyms", []):
            syn_text = syn.get("synonym_text", "").lower()
            if formula_normalized in syn_text.replace(" ", ""):
                matches.append({
                    "preferred_term": ing["preferred_term"],
                    "ontology_id": ing.get("ontology_id"),
                    "match_type": "formula_in_synonym",
                    "confidence": "MEDIUM",
                })
                break

    return matches


def extract_context_clues(unmapped_record: Dict) -> Dict[str, Any]:
    """Extract context clues from unmapped record (CAS, catalog, roles)."""
    clues = {
        "cas_numbers": [],
        "catalog_codes": [],
        "roles": [],
        "properties": [],
    }

    # Extract from synonyms
    for syn in unmapped_record.get("synonyms", []):
        text = syn.get("synonym_text", "")

        # CAS numbers
        cas_match = re.search(r"CAS:\s*(\d+-\d+-\d+)", text)
        if cas_match:
            clues["cas_numbers"].append(cas_match.group(1))

        # Catalog codes
        catalog_match = re.search(r"\((Fisher|Sigma|BD|Difco)\s+([A-Z0-9\-]+)\)", text)
        if catalog_match:
            clues["catalog_codes"].append(f"{catalog_match.group(1)} {catalog_match.group(2)}")

        # Roles
        role_match = re.search(r"Role:\s*([^;]+)", text)
        if role_match:
            clues["roles"].append(role_match.group(1).strip())

        # Properties
        prop_match = re.search(r"Properties:\s*([^;]+)", text)
        if prop_match:
            props = prop_match.group(1).strip()
            clues["properties"].extend([p.strip() for p in props.split(",")])

    return clues


def rank_candidates(candidates: List[Dict], context: Dict, mapped_matches: List[Dict]) -> List[Dict]:
    """Rank candidates by likelihood using context clues and existing mappings."""

    for candidate in candidates:
        score = 0
        evidence = []

        # Base score from likelihood
        if candidate["likelihood"] == "HIGH":
            score += 10
        elif candidate["likelihood"] == "MEDIUM":
            score += 5
        elif candidate["likelihood"] == "LOW":
            score += 1

        # Bonus if found in mapped ingredients
        for match in mapped_matches:
            if candidate["chebi"] in match.get("ontology_id", ""):
                score += 20
                evidence.append(f"Already mapped: {match['preferred_term']}")

        # Bonus for context clues
        if context["cas_numbers"]:
            evidence.append(f"Has CAS: {', '.join(context['cas_numbers'])}")
            score += 5

        if context["roles"]:
            # Check if role matches expected usage
            roles_str = ", ".join(context["roles"])
            evidence.append(f"Roles: {roles_str}")

            # Role-specific bonuses
            if "Nitrogen source" in roles_str:
                if "nitrate" in candidate["name"] or "ammonium" in candidate["name"]:
                    score += 5
            if "Phosphate" in roles_str or "Buffer" in roles_str:
                if "phosphate" in candidate["name"]:
                    score += 5
            if "Mineral" in roles_str:
                score += 3

        candidate["score"] = score
        candidate["evidence"] = evidence

    # Sort by score (highest first)
    candidates.sort(key=lambda x: x["score"], reverse=True)

    return candidates


def analyze_incomplete_formulas():
    """Main analysis function."""
    print("=" * 80)
    print("INCOMPLETE FORMULA REPAIR ANALYSIS")
    print("=" * 80)
    print()

    # Load data
    print("Loading data...")
    unmapped_data = load_yaml(UNMAPPED_PATH)
    mapped_data = load_yaml(MAPPED_PATH)

    unmapped_ingredients = unmapped_data["ingredients"]
    mapped_ingredients = mapped_data["ingredients"]

    print(f"  Loaded {len(mapped_ingredients)} mapped ingredients")
    print(f"  Loaded {len(unmapped_ingredients)} unmapped ingredients")
    print()

    # Find incomplete formulas
    incomplete_formulas = []
    for ing in unmapped_ingredients:
        term = ing["preferred_term"]

        # Check if it's an incomplete formula
        # Pattern: short chemical formula or single element
        if (re.match(r"^[A-Z][a-z]?[0-9]?[A-Z][a-z]?[A-Z]?[a-z]?$", term) or
            re.match(r"^[A-Z][a-z]?$", term) or
            re.match(r"^NH4[A-Z]", term)):
            incomplete_formulas.append(ing)

    print(f"Found {len(incomplete_formulas)} incomplete formulas")
    print()

    # Analyze each
    results = []

    for ing in incomplete_formulas:
        incomplete = ing["preferred_term"]
        print("=" * 80)
        print(f"ANALYZING: {incomplete}")
        print("=" * 80)

        # Generate candidates
        candidates = generate_formula_candidates(incomplete)

        if not candidates:
            print(f"  ⚠️  No completion patterns defined for '{incomplete}'")
            print()
            continue

        print(f"\nGenerated {len(candidates)} candidate completions:")
        for i, cand in enumerate(candidates, 1):
            print(f"  {i}. {cand['formula']} → {cand['name']}")
            print(f"     CHEBI: {cand['chebi']}")
            print(f"     Likelihood: {cand['likelihood']}")
            print(f"     Reason: {cand['reason']}")
        print()

        # Extract context
        context = extract_context_clues(ing)

        if any(context.values()):
            print("Context clues:")
            if context["cas_numbers"]:
                print(f"  CAS: {', '.join(context['cas_numbers'])}")
            if context["catalog_codes"]:
                print(f"  Catalog: {', '.join(context['catalog_codes'])}")
            if context["roles"]:
                print(f"  Roles: {', '.join(set(context['roles']))}")
            if context["properties"]:
                print(f"  Properties: {', '.join(set(context['properties']))}")
            print()

        # Search in mapped ingredients
        mapped_matches_all = []
        for cand in candidates:
            matches = search_in_mapped(cand["formula"], mapped_ingredients)
            mapped_matches_all.extend(matches)

        if mapped_matches_all:
            print("Found in existing mapped ingredients:")
            for match in mapped_matches_all:
                print(f"  ✓ {match['preferred_term']} ({match['ontology_id']})")
                print(f"    Match type: {match['match_type']}, Confidence: {match['confidence']}")
            print()

        # Rank candidates
        ranked = rank_candidates(candidates, context, mapped_matches_all)

        print("RANKED CANDIDATES (by likelihood):")
        print()
        for i, cand in enumerate(ranked, 1):
            print(f"{i}. {cand['formula']} → {cand['name']}")
            print(f"   CHEBI: {cand['chebi']}")
            print(f"   Score: {cand['score']}")
            if cand['evidence']:
                print(f"   Evidence:")
                for ev in cand['evidence']:
                    print(f"     - {ev}")
            print()

        # Store result
        results.append({
            "incomplete": incomplete,
            "occurrences": ing["occurrence_statistics"]["total_occurrences"],
            "candidates": ranked,
            "context": context,
            "top_recommendation": ranked[0] if ranked else None,
        })

        print()

    # Generate summary report
    print("=" * 80)
    print("REPAIR RECOMMENDATIONS SUMMARY")
    print("=" * 80)
    print()

    for result in results:
        print(f"{result['incomplete']} ({result['occurrences']} occurrences)")

        if result["top_recommendation"]:
            rec = result["top_recommendation"]
            print(f"  ✓ RECOMMENDED: {rec['formula']} → {rec['name']}")
            print(f"    CHEBI: {rec['chebi']}")
            print(f"    Confidence: {rec['likelihood']} (score: {rec['score']})")
            if rec['evidence']:
                print(f"    Evidence: {'; '.join(rec['evidence'])}")
        else:
            print(f"  ⚠️  No recommendations available")

        print()

    # Save detailed report
    output_path = Path(__file__).parent.parent / "reports" / "FORMULA_REPAIR_ANALYSIS.yaml"
    with open(output_path, "w") as f:
        yaml.dump({
            "analysis_date": "2026-03-15",
            "total_incomplete": len(incomplete_formulas),
            "results": results,
        }, f, default_flow_style=False, sort_keys=False, allow_unicode=True)

    print(f"✓ Detailed analysis saved to: {output_path}")
    print()


if __name__ == "__main__":
    analyze_incomplete_formulas()
