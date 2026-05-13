#!/usr/bin/env python3
"""Analyze CultureMech role data from ingredient synonyms.

This script parses role annotations from RAW_TEXT synonyms and generates:
1. Role distribution statistics across all ingredients
2. Top 100 ingredient cross-reference with role assignments
3. Confidence scores based on properties metadata

Input: data/curated/mapped_ingredients.yaml
Outputs:
  - data/analysis/culturemech_role_distribution.csv
  - data/analysis/top100_role_crossref.yaml
"""

import re
import sys
from pathlib import Path
from collections import defaultdict
from dataclasses import dataclass, field
from typing import Optional

import pandas as pd
import yaml

# Add src to path
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from mediaingredientmech.curation.ingredient_curator import IngredientCurator

# Extended mapping from CultureMech role text to IngredientRoleEnum
CULTUREMECH_ROLE_MAPPING = {
    "Mineral source": "MINERAL",
    "Buffer": "BUFFER",
    "Nitrogen source": "NITROGEN_SOURCE",
    "Carbon source": "CARBON_SOURCE",
    "Vitamin source": "VITAMIN_SOURCE",
    "Vitamin": "VITAMIN_SOURCE",
    "Protein source": "PROTEIN_SOURCE",
    "Trace element": "TRACE_ELEMENT",
    "Trace metal": "TRACE_ELEMENT",
    "Solvating media": "SALT",
    "Salt": "SALT",
    "Solidifying agent": "SOLIDIFYING_AGENT",
    "Solidifying component": "SOLIDIFYING_AGENT",
    "Energy source": "ENERGY_SOURCE",
    "Electron acceptor": "ELECTRON_ACCEPTOR",
    "Electron donor": "ELECTRON_DONOR",
    "Cofactor": "COFACTOR_PROVIDER",
    "Cofactor provider": "COFACTOR_PROVIDER",
    "Amino acid source": "AMINO_ACID_SOURCE",
    # New mappings for extended enum
    "pH dependent redox indicator": "REDOX_INDICATOR",
    "Redox indicator": "REDOX_INDICATOR",
    "Reducing agent": "REDOX_INDICATOR",
    "pH indicator": "PH_INDICATOR",
    "Antimicrobial agent": "SELECTIVE_AGENT",
    "Selective agent": "SELECTIVE_AGENT",
    "Surfactant": "SURFACTANT",
    "Detergent": "SURFACTANT",
    # Additional mappings (2026-03-15)
    "Growth factor": "VITAMIN_SOURCE",
    "Nutrient source": "CARBON_SOURCE",
    # Multi-role mappings (take first role for primary)
    "Mineral source, Protective agent": "MINERAL",
    "Protective agent, Mineral source": "MINERAL",
    "pH indicator, Selective agent": "PH_INDICATOR",
    "Selective agent, pH indicator": "SELECTIVE_AGENT",
    "Buffer, Mineral source": "BUFFER",
}

# Pattern to match role text in synonyms
ROLE_PATTERN = re.compile(r"Role:\s*([^;]+);?\s*Properties:\s*(.+)")


@dataclass
class RoleAnnotation:
    """Parsed role annotation from CultureMech synonym."""

    role_text: str  # Original text (e.g., "Mineral source")
    role_enum: Optional[str]  # Mapped enum value (e.g., "MINERAL")
    properties: list[str] = field(default_factory=list)
    is_defined: bool = False
    is_simple: bool = False
    is_inorganic: bool = False


@dataclass
class IngredientRoleSummary:
    """Summary of roles for a single ingredient."""

    id: str
    ontology_id: str
    preferred_term: str
    occurrence_count: int
    roles: list[RoleAnnotation] = field(default_factory=list)
    primary_role: Optional[str] = None  # Most common role enum
    confidence: float = 0.0


def parse_ingredient_notes(synonym_text: str) -> Optional[RoleAnnotation]:
    """Extract role and properties from synonym text.

    Args:
        synonym_text: Text like "Role: Mineral source; Properties: Defined component, ..."

    Returns:
        RoleAnnotation object or None if no match
    """
    match = ROLE_PATTERN.match(synonym_text)
    if not match:
        return None

    role_text = match.group(1).strip()
    properties_text = match.group(2).strip()

    # Map to enum value
    role_enum = CULTUREMECH_ROLE_MAPPING.get(role_text)

    # Parse properties
    properties = [p.strip() for p in properties_text.split(",")]

    # Extract property flags
    is_defined = "Defined component" in properties
    is_simple = "Simple component" in properties
    is_inorganic = "Inorganic compound" in properties

    return RoleAnnotation(
        role_text=role_text,
        role_enum=role_enum,
        properties=properties,
        is_defined=is_defined,
        is_simple=is_simple,
        is_inorganic=is_inorganic,
    )


def calculate_confidence(
    roles: list[RoleAnnotation], occurrence_count: int
) -> float:
    """Calculate confidence score based on CultureMech properties.

    Rules:
    - "Defined component" + occurrence >500 → 1.0
    - "Defined component" + occurrence 100-500 → 0.95
    - "Defined component" + occurrence <100 → 0.9
    - "Undefined component" → 0.8
    - No properties → 0.7

    Args:
        roles: List of role annotations for ingredient
        occurrence_count: Total occurrence count across media

    Returns:
        Confidence score (0.0-1.0)
    """
    if not roles:
        return 0.0

    # Check if any role has "Defined component"
    is_defined = any(r.is_defined for r in roles)

    if not is_defined:
        return 0.8  # Undefined component

    # Use occurrence count for defined components
    if occurrence_count > 500:
        return 1.0
    elif occurrence_count >= 100:
        return 0.95
    else:
        return 0.9


def analyze_all_ingredients(
    curator: IngredientCurator,
) -> tuple[dict[str, int], list[IngredientRoleSummary]]:
    """Analyze all ingredients for role distribution.

    Args:
        curator: IngredientCurator with loaded records

    Returns:
        Tuple of (role_counts, ingredient_summaries)
    """
    role_counts = defaultdict(int)
    role_text_counts = defaultdict(int)
    ingredient_summaries = []

    print(f"\nAnalyzing {len(curator.records)} ingredients...")

    for i, record in enumerate(curator.records, 1):
        if i % 100 == 0:
            print(f"  Processed {i}/{len(curator.records)} ingredients...")

        # Extract basic info
        ingredient_id = record.get("id", "")
        ontology_id = record.get("ontology_id", "")
        preferred_term = record.get("preferred_term", "")
        occurrence_count = record.get("occurrence_statistics", {}).get(
            "total_occurrences", 0
        )

        # Extract role annotations from synonyms
        roles = []
        role_enum_set = set()

        for synonym in record.get("synonyms", []):
            if synonym.get("synonym_type") != "RAW_TEXT":
                continue

            synonym_text = synonym.get("synonym_text", "")
            role_annotation = parse_ingredient_notes(synonym_text)

            if role_annotation:
                roles.append(role_annotation)
                role_text_counts[role_annotation.role_text] += 1

                if role_annotation.role_enum:
                    role_enum_set.add(role_annotation.role_enum)

        # Count unique role enums
        for role_enum in role_enum_set:
            role_counts[role_enum] += 1

        # Create summary if roles found
        if roles:
            # Determine primary role (most common)
            role_enum_occurrences = defaultdict(int)
            for r in roles:
                if r.role_enum:
                    role_enum_occurrences[r.role_enum] += 1

            primary_role = (
                max(role_enum_occurrences.items(), key=lambda x: x[1])[0]
                if role_enum_occurrences
                else None
            )

            confidence = calculate_confidence(roles, occurrence_count)

            summary = IngredientRoleSummary(
                id=ingredient_id,
                ontology_id=ontology_id,
                preferred_term=preferred_term,
                occurrence_count=occurrence_count,
                roles=roles,
                primary_role=primary_role,
                confidence=confidence,
            )

            ingredient_summaries.append(summary)

    print(f"\nFound {len(ingredient_summaries)} ingredients with role annotations")

    # Print unmapped role texts
    unmapped_roles = [
        (text, count)
        for text, count in role_text_counts.items()
        if text not in CULTUREMECH_ROLE_MAPPING
    ]

    if unmapped_roles:
        print("\n⚠️  Unmapped role texts found (not in CULTUREMECH_ROLE_MAPPING):")
        for text, count in sorted(unmapped_roles, key=lambda x: x[1], reverse=True):
            print(f"  '{text}': {count} occurrences")

    return dict(role_counts), ingredient_summaries


def generate_top_n_crossref(
    summaries: list[IngredientRoleSummary], top_n: int = 100
) -> list[IngredientRoleSummary]:
    """Generate top N ingredient cross-reference by occurrence.

    Args:
        summaries: All ingredient summaries
        top_n: Number of top ingredients to return

    Returns:
        Top N summaries sorted by occurrence count
    """
    # Sort by occurrence count
    sorted_summaries = sorted(
        summaries, key=lambda s: s.occurrence_count, reverse=True
    )

    return sorted_summaries[:top_n]


def save_role_distribution(role_counts: dict[str, int], output_path: Path):
    """Save role distribution statistics to CSV.

    Args:
        role_counts: Dictionary of role enum → count
        output_path: Output CSV path
    """
    # Create DataFrame
    df = pd.DataFrame(
        [
            {"role_enum": role, "ingredient_count": count}
            for role, count in sorted(
                role_counts.items(), key=lambda x: x[1], reverse=True
            )
        ]
    )

    # Save to CSV
    output_path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(output_path, index=False)

    print(f"\n✅ Role distribution saved to: {output_path}")
    print("\nTop 10 roles:")
    for _, row in df.head(10).iterrows():
        print(f"  {row['role_enum']:25s}: {row['ingredient_count']:4d} ingredients")


def save_top_n_crossref(summaries: list[IngredientRoleSummary], output_path: Path):
    """Save top N ingredient cross-reference to YAML.

    Args:
        summaries: List of ingredient summaries
        output_path: Output YAML path
    """
    # Convert to serializable format
    data = {
        "generation_date": pd.Timestamp.now().isoformat(),
        "total_count": len(summaries),
        "average_confidence": sum(s.confidence for s in summaries) / len(summaries)
        if summaries
        else 0.0,
        "ingredients": [
            {
                "id": s.id,
                "ontology_id": s.ontology_id,
                "preferred_term": s.preferred_term,
                "occurrence_count": s.occurrence_count,
                "primary_role": s.primary_role,
                "all_roles": [r.role_enum for r in s.roles if r.role_enum],
                "confidence": s.confidence,
                "properties_summary": {
                    "defined": any(r.is_defined for r in s.roles),
                    "simple": any(r.is_simple for r in s.roles),
                    "inorganic": any(r.is_inorganic for r in s.roles),
                },
                "raw_annotations": [
                    {
                        "role_text": r.role_text,
                        "role_enum": r.role_enum,
                        "properties": r.properties,
                    }
                    for r in s.roles
                ],
            }
            for s in summaries
        ],
    }

    # Save to YAML
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, "w") as f:
        yaml.safe_dump(data, f, default_flow_style=False, sort_keys=False)

    print(f"\n✅ Top {len(summaries)} cross-reference saved to: {output_path}")
    print(f"   Average confidence: {data['average_confidence']:.3f}")


def main():
    """Main analysis workflow."""
    print("=" * 80)
    print("CultureMech Role Analysis")
    print("=" * 80)

    # Load mapped ingredients
    data_path = Path("data/curated/mapped_ingredients.yaml")
    curator = IngredientCurator(
        data_path=data_path, curator_name="analyze_culturemech_roles"
    )

    print(f"\nLoading ingredient records from: {data_path}")
    curator.load()
    print(f"Loaded {len(curator.records)} records")

    # Analyze all ingredients
    role_counts, summaries = analyze_all_ingredients(curator)

    # Save role distribution
    distribution_path = Path("data/analysis/culturemech_role_distribution.csv")
    save_role_distribution(role_counts, distribution_path)

    # Generate and save top 100 cross-reference
    top_100 = generate_top_n_crossref(summaries, top_n=100)
    crossref_path = Path("data/analysis/top100_role_crossref.yaml")
    save_top_n_crossref(top_100, crossref_path)

    # Summary statistics
    print("\n" + "=" * 80)
    print("ANALYSIS SUMMARY")
    print("=" * 80)
    print(f"Total ingredients analyzed: {len(curator.records)}")
    print(f"Ingredients with role annotations: {len(summaries)}")
    print(f"Unique role types found: {len(role_counts)}")
    print(f"Average confidence (top 100): {sum(s.confidence for s in top_100) / len(top_100):.3f}")

    print("\n✅ Analysis complete!")


if __name__ == "__main__":
    main()
