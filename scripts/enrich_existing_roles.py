#!/usr/bin/env python3
"""Enrich existing role assignments with structured CultureMech metadata.

This script upgrades minimal "Imported from CultureMech pipeline" citations
with structured evidence including occurrence statistics and property details.

Input: data/curated/mapped_ingredients.yaml (with existing roles)
Output: Updated data/curated/mapped_ingredients.yaml
"""

import sys
from pathlib import Path

import yaml

# Add src to path
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from mediaingredientmech.curation.ingredient_curator import IngredientCurator


def load_crossref_lookup(crossref_path: Path) -> dict[str, dict]:
    """Load top 100 cross-reference as a lookup by ingredient ID.

    Args:
        crossref_path: Path to top100_role_crossref.yaml

    Returns:
        Dictionary mapping ingredient_id → ingredient_data
    """
    with open(crossref_path) as f:
        data = yaml.safe_load(f)

    lookup = {}
    for ingredient in data["ingredients"]:
        lookup[ingredient["id"]] = ingredient

    return lookup


def has_generic_citation(role_assignment: dict) -> bool:
    """Check if role has generic CultureMech citation.

    Args:
        role_assignment: Role assignment dict from media_roles

    Returns:
        True if citation is generic and needs enrichment
    """
    for evidence in role_assignment.get("evidence", []):
        ref_text = evidence.get("reference_text", "")
        if "Imported from CultureMech pipeline" in ref_text:
            return True
        # Also check for very short citations without metadata
        if ref_text and len(ref_text) < 50 and "CultureMech" in ref_text:
            return True

    return False


def enrich_role_citation(
    role_assignment: dict,
    ingredient_id: str,
    preferred_term: str,
    occurrence_count: int,
    crossref_data: dict,
) -> bool:
    """Enrich a role assignment with structured CultureMech metadata.

    Args:
        role_assignment: Role assignment dict to update
        ingredient_id: Ingredient ID
        preferred_term: Preferred term
        occurrence_count: Total occurrence count
        crossref_data: Cross-reference data for this ingredient

    Returns:
        True if citation was enriched
    """
    role_enum = role_assignment.get("role")

    # Find role-specific annotations
    role_annotations = [
        ann
        for ann in crossref_data.get("raw_annotations", [])
        if ann["role_enum"] == role_enum
    ]

    if not role_annotations:
        return False

    # Build excerpt from first annotation
    first_ann = role_annotations[0]
    role_text = first_ann["role_text"]
    properties = ", ".join(first_ann["properties"])
    excerpt = f"Role: {role_text}; Properties: {properties}"

    # Determine if "Defined component" is present
    is_defined = "Defined component" in properties

    # Build curator note
    role_display = role_enum.replace("_", " ").title()
    property_note = "High confidence based on 'Defined component' property." if is_defined else "Moderate confidence based on CultureMech annotations."
    curator_note = f"Widespread use in media formulations ({occurrence_count} occurrences). {property_note}"

    # Create new evidence entry
    new_evidence = {
        "reference_text": f"CultureMech database ({occurrence_count} occurrences as '{role_text}')",
        "reference_type": "DATABASE_ENTRY",
        "url": "https://github.com/CultureBotAI/CultureMech",
        "excerpt": excerpt,
        "curator_note": curator_note,
    }

    # Replace or update evidence
    role_assignment["evidence"] = [new_evidence]

    return True


def enrich_existing_roles(
    curator: IngredientCurator,
    crossref_lookup: dict[str, dict],
    dry_run: bool = False,
) -> tuple[int, int, int]:
    """Enrich existing role assignments with structured metadata.

    Args:
        curator: IngredientCurator instance
        crossref_lookup: Lookup from ingredient_id → crossref_data
        dry_run: If True, preview changes without saving

    Returns:
        Tuple of (ingredients_checked, roles_enriched, roles_skipped)
    """
    ingredients_checked = 0
    roles_enriched = 0
    roles_skipped = 0

    print(f"\nProcessing {len(curator.records)} ingredient records...")

    for i, record in enumerate(curator.records, 1):
        if i % 100 == 0:
            print(f"  Processed {i}/{len(curator.records)} ingredients...")

        # Skip if no roles
        if not record.get("media_roles"):
            continue

        ingredients_checked += 1

        ingredient_id = record.get("id")
        preferred_term = record.get("preferred_term", "Unknown")
        occurrence_count = record.get("occurrence_statistics", {}).get(
            "total_occurrences", 0
        )

        # Get cross-reference data if available
        crossref_data = crossref_lookup.get(ingredient_id)

        # Process each role assignment
        for role_assignment in record["media_roles"]:
            role_enum = role_assignment.get("role")

            # Check if needs enrichment
            if not has_generic_citation(role_assignment):
                roles_skipped += 1
                continue

            # Try to enrich
            if crossref_data:
                if dry_run:
                    print(
                        f"  [DRY RUN] Would enrich {role_enum} for {ingredient_id} ({preferred_term})"
                    )
                    enriched = True
                else:
                    enriched = enrich_role_citation(
                        role_assignment,
                        ingredient_id,
                        preferred_term,
                        occurrence_count,
                        crossref_data,
                    )

                if enriched:
                    roles_enriched += 1
                else:
                    roles_skipped += 1
            else:
                # No crossref data available, skip
                roles_skipped += 1

    return ingredients_checked, roles_enriched, roles_skipped


def main():
    """Main enrichment workflow."""
    import argparse

    parser = argparse.ArgumentParser(
        description="Enrich existing role citations with CultureMech metadata"
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Preview changes without saving",
    )
    parser.add_argument(
        "--crossref",
        type=Path,
        default=Path("data/analysis/top100_role_crossref.yaml"),
        help="Path to top100_role_crossref.yaml",
    )
    args = parser.parse_args()

    print("=" * 80)
    print("Enrich Existing Role Citations")
    print("=" * 80)

    if args.dry_run:
        print("\n⚠️  DRY RUN MODE - No changes will be saved\n")

    # Load cross-reference lookup
    print(f"\nLoading cross-reference from: {args.crossref}")
    crossref_lookup = load_crossref_lookup(args.crossref)
    print(f"Loaded cross-reference data for {len(crossref_lookup)} ingredients")

    # Load mapped ingredients
    data_path = Path("data/curated/mapped_ingredients.yaml")
    curator = IngredientCurator(
        data_path=data_path, curator_name="enrich_existing_roles"
    )

    print(f"\nLoading ingredient records from: {data_path}")
    curator.load()
    print(f"Loaded {len(curator.records)} records")

    # Count existing roles
    total_existing_roles = sum(
        len(r.get("media_roles", [])) for r in curator.records
    )
    print(f"Found {total_existing_roles} existing role assignments")

    # Enrich roles
    ingredients_checked, roles_enriched, roles_skipped = enrich_existing_roles(
        curator, crossref_lookup, dry_run=args.dry_run
    )

    # Save results
    if not args.dry_run:
        print("\nSaving updated records...")
        curator.save()
        print(f"✅ Saved to {data_path}")
    else:
        print("\n⚠️  DRY RUN - No changes saved")

    # Summary statistics
    print("\n" + "=" * 80)
    print("ENRICHMENT SUMMARY")
    print("=" * 80)
    print(f"Ingredients with roles: {ingredients_checked}")
    print(f"Total existing roles: {total_existing_roles}")
    print(f"Roles enriched: {roles_enriched}")
    print(f"Roles skipped (already proper or no data): {roles_skipped}")

    if roles_enriched > 0:
        enrichment_rate = (
            roles_enriched / total_existing_roles * 100 if total_existing_roles > 0 else 0
        )
        print(f"Enrichment rate: {enrichment_rate:.1f}%")

    if not args.dry_run:
        print("\n✅ Role enrichment complete!")
    else:
        print("\n✅ Dry run complete! Re-run without --dry-run to apply changes.")


if __name__ == "__main__":
    main()
