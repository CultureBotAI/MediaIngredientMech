#!/usr/bin/env python3
"""Example queries demonstrating role tracking capabilities.

This script shows various ways to query ingredients by their roles,
demonstrating the power of the new role tracking system.
"""

import sys
from pathlib import Path

# Add src to path
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from mediaingredientmech.curation.ingredient_curator import IngredientCurator


def query_by_role(ingredients: list[dict], role: str) -> list[dict]:
    """Find all ingredients with a specific media role."""
    return [
        ing
        for ing in ingredients
        if any(r.get("role") == role for r in ing.get("media_roles", []))
    ]


def query_by_solution_type(ingredients: list[dict], solution_type: str) -> list[dict]:
    """Find all ingredients of a specific solution type."""
    return [ing for ing in ingredients if ing.get("solution_type") == solution_type]


def query_with_doi(ingredients: list[dict]) -> list[dict]:
    """Find ingredients with DOI-backed citations."""
    return [
        ing
        for ing in ingredients
        if any(
            any(e.get("doi") for e in r.get("evidence", []))
            for r in ing.get("media_roles", []) + ing.get("cellular_roles", [])
        )
    ]


def query_high_confidence(ingredients: list[dict], threshold: float = 0.95) -> list[dict]:
    """Find ingredients with high-confidence role assignments."""
    result = []
    for ing in ingredients:
        for role_list in [ing.get("media_roles", []), ing.get("cellular_roles", [])]:
            if any(r.get("confidence", 0) >= threshold for r in role_list):
                result.append(ing)
                break
    return result


def query_multiple_roles(ingredients: list[dict]) -> list[dict]:
    """Find ingredients with multiple roles."""
    return [
        ing
        for ing in ingredients
        if len(ing.get("media_roles", [])) + len(ing.get("cellular_roles", [])) > 1
    ]


def main():
    """Demonstrate various role-based queries."""
    print("=" * 80)
    print("EXAMPLE ROLE QUERIES")
    print("=" * 80)

    # Load data
    curator = IngredientCurator(
        data_path=Path("data/curated/mapped_ingredients.yaml"), curator_name="query_example"
    )
    curator.load()
    ingredients = curator.records

    print(f"\nTotal ingredients: {len(ingredients)}")

    # Query 1: Find all nitrogen sources
    print("\n" + "=" * 80)
    print("Query 1: Find all NITROGEN_SOURCE ingredients")
    print("=" * 80)
    nitrogen_sources = query_by_role(ingredients, "NITROGEN_SOURCE")
    print(f"Found {len(nitrogen_sources)} nitrogen sources:")
    for ing in nitrogen_sources[:10]:  # Show first 10
        name = ing.get("preferred_term")
        conf = ing.get("media_roles", [{}])[0].get("confidence", "N/A")
        print(f"  • {name} (confidence: {conf})")
    if len(nitrogen_sources) > 10:
        print(f"  ... and {len(nitrogen_sources) - 10} more")

    # Query 2: Find all carbon sources
    print("\n" + "=" * 80)
    print("Query 2: Find all CARBON_SOURCE ingredients")
    print("=" * 80)
    carbon_sources = query_by_role(ingredients, "CARBON_SOURCE")
    print(f"Found {len(carbon_sources)} carbon sources:")
    for ing in carbon_sources[:10]:
        name = ing.get("preferred_term")
        occurrences = ing.get("occurrence_statistics", {}).get("total_occurrences", 0)
        print(f"  • {name} (occurrences: {occurrences})")
    if len(carbon_sources) > 10:
        print(f"  ... and {len(carbon_sources) - 10} more")

    # Query 3: Find all buffers
    print("\n" + "=" * 80)
    print("Query 3: Find all BUFFER ingredients")
    print("=" * 80)
    buffers = query_by_role(ingredients, "BUFFER")
    print(f"Found {len(buffers)} buffers:")
    for ing in buffers[:10]:
        name = ing.get("preferred_term")
        chebi = ing.get("ontology_mapping", {}).get("ontology_id", "N/A")
        print(f"  • {name} ({chebi})")
    if len(buffers) > 10:
        print(f"  ... and {len(buffers) - 10} more")

    # Query 4: Find vitamin mixes
    print("\n" + "=" * 80)
    print("Query 4: Find all VITAMIN_MIX solution types")
    print("=" * 80)
    vitamin_mixes = query_by_solution_type(ingredients, "VITAMIN_MIX")
    print(f"Found {len(vitamin_mixes)} vitamin mixes:")
    for ing in vitamin_mixes:
        name = ing.get("preferred_term")
        status = ing.get("mapping_status")
        print(f"  • {name} (status: {status})")

    # Query 5: Find ingredients with DOI citations
    print("\n" + "=" * 80)
    print("Query 5: Find ingredients with DOI-backed citations")
    print("=" * 80)
    with_doi = query_with_doi(ingredients)
    print(f"Found {len(with_doi)} ingredients with DOI citations")
    if with_doi:
        for ing in with_doi[:5]:
            name = ing.get("preferred_term")
            # Extract DOI
            for role in ing.get("media_roles", []) + ing.get("cellular_roles", []):
                for evidence in role.get("evidence", []):
                    doi = evidence.get("doi")
                    if doi:
                        print(f"  • {name}: {doi}")
                        break

    # Query 6: Find high-confidence assignments
    print("\n" + "=" * 80)
    print("Query 6: Find ingredients with confidence ≥ 0.95")
    print("=" * 80)
    high_conf = query_high_confidence(ingredients, threshold=0.95)
    print(f"Found {len(high_conf)} ingredients with high-confidence roles")
    # Count by role
    role_counts = {}
    for ing in high_conf:
        for role_assignment in ing.get("media_roles", []):
            if role_assignment.get("confidence", 0) >= 0.95:
                role = role_assignment.get("role")
                role_counts[role] = role_counts.get(role, 0) + 1
    print("\nHigh-confidence role distribution:")
    for role, count in sorted(role_counts.items(), key=lambda x: x[1], reverse=True):
        print(f"  {role:25s}: {count:4d}")

    # Query 7: Find ingredients with multiple roles
    print("\n" + "=" * 80)
    print("Query 7: Find ingredients with multiple roles")
    print("=" * 80)
    multi_role = query_multiple_roles(ingredients)
    print(f"Found {len(multi_role)} ingredients with multiple roles:")
    for ing in multi_role[:10]:
        name = ing.get("preferred_term")
        roles = [r.get("role") for r in ing.get("media_roles", [])]
        print(f"  • {name}: {', '.join(roles)}")
    if len(multi_role) > 10:
        print(f"  ... and {len(multi_role) - 10} more")

    # Query 8: Find minerals by occurrence
    print("\n" + "=" * 80)
    print("Query 8: Top 10 MINERAL ingredients by occurrence")
    print("=" * 80)
    minerals = query_by_role(ingredients, "MINERAL")
    minerals_sorted = sorted(
        minerals,
        key=lambda x: x.get("occurrence_statistics", {}).get("total_occurrences", 0),
        reverse=True,
    )
    print(f"Top minerals (out of {len(minerals)} total):")
    for ing in minerals_sorted[:10]:
        name = ing.get("preferred_term")
        occurrences = ing.get("occurrence_statistics", {}).get("total_occurrences", 0)
        media_count = ing.get("occurrence_statistics", {}).get("media_count", 0)
        print(f"  • {name}: {occurrences} occurrences in {media_count} media")

    print("\n" + "=" * 80)
    print("✅ Query examples complete!")
    print("=" * 80)


if __name__ == "__main__":
    main()
