#!/usr/bin/env python3
"""Analyze batch1 ingredients and generate YAML suggestions."""

import sys
from pathlib import Path

# Add src to path
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from mediaingredientmech.utils.chemical_normalizer import normalize_chemical_name, generate_search_variants
from mediaingredientmech.utils.ontology_client import OntologyClient

def analyze_ingredient(name: str, synonyms: list = None):
    """Analyze a single ingredient and return mapping suggestion."""
    client = OntologyClient()

    # Try normalization
    result = normalize_chemical_name(name)

    # Generate search variants
    variants = generate_search_variants(result.normalized, name)

    # Search CHEBI first (all are SIMPLE_CHEMICAL category)
    matches = client.search_with_variants(variants, sources=["CHEBI"], max_results=5)

    if matches:
        top_match = matches[0]
        quality = "EXACT_MATCH" if top_match.score >= 0.95 else "SYNONYM_MATCH"

        return {
            "ingredient_id": None,  # Will be filled in
            "ontology_id": top_match.ontology_id,
            "ontology_label": top_match.label,
            "ontology_source": "CHEBI",
            "confidence": round(top_match.score, 2),
            "quality": quality,
            "reasoning": f"Normalized from '{name}' to '{result.normalized}'. Search variants: {variants[:3]}. Top CHEBI match.",
            "applied_rules": result.applied_rules
        }
    else:
        return {
            "ingredient_id": None,
            "ontology_id": None,
            "ontology_label": None,
            "ontology_source": None,
            "confidence": 0.0,
            "quality": "NEEDS_EXPERT",
            "reasoning": f"No matches found for '{name}'. Variants tried: {variants}",
            "applied_rules": result.applied_rules
        }

# Ingredients from batch1_simple_chemicals.md
ingredients = [
    ("UNMAPPED_0003", "MgSO4•7H2O"),
    ("UNMAPPED_0004", "NaNO"),  # Has synonym NaNO3
    ("UNMAPPED_0006", "dH2O"),
    ("UNMAPPED_0007", "CaCl2•2H2O"),
    ("UNMAPPED_0010", "K2HPO"),  # Has synonym K2HPO4
    ("UNMAPPED_0011", "P-IV Metal Solution"),
    ("UNMAPPED_0015", "NaCl"),
    ("UNMAPPED_0016", "Na2SiO3•9H2O"),
    ("UNMAPPED_0017", "MgCO"),  # Has synonym MgCO3
    ("UNMAPPED_0018", "KH2PO"),  # Has synonym KH2PO4
    ("UNMAPPED_0020", "KCl"),
    ("UNMAPPED_0021", "CaCO"),  # Has synonym CaCO3
    ("UNMAPPED_0026", "KNO"),  # Has synonym KNO3
    ("UNMAPPED_0028", "NaH2PO4•H2O"),
    ("UNMAPPED_0030", "Na2glycerophosphate•5H2O"),
    ("UNMAPPED_0032", "sterile dH2O"),
    ("UNMAPPED_0034", "NH4Cl"),
    ("UNMAPPED_0035", "NaHCO"),  # Has synonym NaHCO3
    ("UNMAPPED_0036", "Original amount: (NH4)2HPO4(Fisher A686)"),
    ("UNMAPPED_0037", "NH4NO"),  # Has synonym NH4NO3
]

print("Analyzing ingredients...")
print()

suggestions = []
for ing_id, name in ingredients:
    print(f"Analyzing {ing_id}: {name}")
    suggestion = analyze_ingredient(name)
    suggestion["ingredient_id"] = ing_id
    suggestions.append(suggestion)

    if suggestion["ontology_id"]:
        print(f"  ✓ {suggestion['ontology_id']}: {suggestion['ontology_label']} (confidence: {suggestion['confidence']})")
    else:
        print(f"  ✗ No match found")
    print()

# Generate YAML output
print("\n" + "="*80)
print("YAML Output:")
print("="*80)
print()

print("# Batch 1 Ontology Mapping Suggestions")
print("# Generated using map-media-ingredients skill")
print("# Total: 20 ingredients")
print()
print("suggestions:")

for s in suggestions:
    if s["ontology_id"] is None:
        # Skip unmappable
        continue

    print(f"  - ingredient_id: {s['ingredient_id']}")
    print(f"    ontology_id: {s['ontology_id']}")
    print(f"    ontology_label: {s['ontology_label']}")
    print(f"    ontology_source: {s['ontology_source']}")
    print(f"    confidence: {s['confidence']}")
    print(f"    quality: {s['quality']}")
    print(f"    reasoning: |")
    print(f"      {s['reasoning']}")
    print()

# Summary
mapped = [s for s in suggestions if s["ontology_id"] is not None]
high_conf = [s for s in mapped if s["confidence"] >= 0.9]
medium_conf = [s for s in mapped if 0.7 <= s["confidence"] < 0.9]
unmappable = [s for s in suggestions if s["ontology_id"] is None]

print()
print("# Summary")
print(f"# Total: {len(suggestions)}")
print(f"# Mapped: {len(mapped)}")
print(f"# High confidence (≥0.9): {len(high_conf)}")
print(f"# Medium confidence (0.7-0.89): {len(medium_conf)}")
print(f"# Unmappable: {len(unmappable)}")
if unmappable:
    print(f"# Unmappable IDs: {', '.join([s['ingredient_id'] for s in unmappable])}")
