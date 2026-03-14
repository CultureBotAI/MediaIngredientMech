#!/usr/bin/env python3
"""Validate role assignments and generate quality metrics.

This script validates all role assignments across both mapped and unmapped ingredients,
checks for schema compliance, and generates comprehensive statistics.
"""

import sys
from collections import defaultdict
from pathlib import Path

# Add src to path
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from mediaingredientmech.curation.ingredient_curator import IngredientCurator


def validate_file(file_path: Path, label: str) -> dict:
    """Validate role assignments in a file and return statistics.

    Args:
        file_path: Path to YAML file to validate
        label: Label for this file (e.g., "mapped", "unmapped")

    Returns:
        Dictionary of validation statistics
    """
    print(f"\n{'=' * 80}")
    print(f"Validating {label} ingredients: {file_path}")
    print(f"{'=' * 80}")

    curator = IngredientCurator(data_path=file_path, curator_name="validator")
    curator.load()

    stats = {
        "total_ingredients": len(curator.records),
        "with_media_roles": 0,
        "with_cellular_roles": 0,
        "with_solution_type": 0,
        "total_media_roles": 0,
        "total_cellular_roles": 0,
        "roles_with_citations": 0,
        "roles_with_doi": 0,
        "validation_errors": 0,
        "media_role_counts": defaultdict(int),
        "cellular_role_counts": defaultdict(int),
        "solution_type_counts": defaultdict(int),
        "citation_type_counts": defaultdict(int),
        "confidence_scores": [],
        "error_details": [],
    }

    # Validate each record
    for i, record in enumerate(curator.records, 1):
        # Run validation
        errors = curator.validate_role_assignments(record)
        if errors:
            stats["validation_errors"] += len(errors)
            for error in errors:
                stats["error_details"].append(
                    f"{record.get('preferred_term', 'UNKNOWN')} (#{i}): {error}"
                )

        # Count media roles
        media_roles = record.get("media_roles", [])
        if media_roles:
            stats["with_media_roles"] += 1
            stats["total_media_roles"] += len(media_roles)

            for role_assignment in media_roles:
                role = role_assignment.get("role")
                if role:
                    stats["media_role_counts"][role] += 1

                # Confidence tracking
                confidence = role_assignment.get("confidence")
                if confidence is not None:
                    stats["confidence_scores"].append(confidence)

                # Citation tracking
                evidence = role_assignment.get("evidence", [])
                if evidence:
                    stats["roles_with_citations"] += 1

                    for cite in evidence:
                        ref_type = cite.get("reference_type")
                        if ref_type:
                            stats["citation_type_counts"][ref_type] += 1

                        if cite.get("doi"):
                            stats["roles_with_doi"] += 1

        # Count cellular roles
        cellular_roles = record.get("cellular_roles", [])
        if cellular_roles:
            stats["with_cellular_roles"] += 1
            stats["total_cellular_roles"] += len(cellular_roles)

            for role_assignment in cellular_roles:
                role = role_assignment.get("role")
                if role:
                    stats["cellular_role_counts"][role] += 1

                # Confidence tracking
                confidence = role_assignment.get("confidence")
                if confidence is not None:
                    stats["confidence_scores"].append(confidence)

                # Citation tracking
                evidence = role_assignment.get("evidence", [])
                if evidence:
                    stats["roles_with_citations"] += 1

                    for cite in evidence:
                        ref_type = cite.get("reference_type")
                        if ref_type:
                            stats["citation_type_counts"][ref_type] += 1

                        if cite.get("doi"):
                            stats["roles_with_doi"] += 1

        # Count solution types
        solution_type = record.get("solution_type")
        if solution_type:
            stats["with_solution_type"] += 1
            stats["solution_type_counts"][solution_type] += 1

    return stats


def print_stats(stats: dict, label: str):
    """Print formatted statistics."""
    print(f"\n{label.upper()} STATISTICS:")
    print("=" * 80)

    total = stats["total_ingredients"]
    print(f"\nCOVERAGE:")
    print(f"  Total ingredients: {total}")
    print(
        f"  With media roles: {stats['with_media_roles']} ({stats['with_media_roles']/total*100:.1f}%)"
    )
    print(
        f"  With cellular roles: {stats['with_cellular_roles']} ({stats['with_cellular_roles']/total*100:.1f}%)"
    )
    print(
        f"  With solution type: {stats['with_solution_type']} ({stats['with_solution_type']/total*100:.1f}%)"
    )

    print(f"\nROLE COUNTS:")
    print(f"  Total media roles: {stats['total_media_roles']}")
    print(f"  Total cellular roles: {stats['total_cellular_roles']}")

    if stats["total_media_roles"] > 0:
        print(f"\nMEDIA ROLE DISTRIBUTION:")
        for role, count in sorted(
            stats["media_role_counts"].items(), key=lambda x: x[1], reverse=True
        ):
            print(f"  {role:25s}: {count:4d}")

    if stats["total_cellular_roles"] > 0:
        print(f"\nCELLULAR ROLE DISTRIBUTION:")
        for role, count in sorted(
            stats["cellular_role_counts"].items(), key=lambda x: x[1], reverse=True
        ):
            print(f"  {role:25s}: {count:4d}")

    if stats["with_solution_type"] > 0:
        print(f"\nSOLUTION TYPE DISTRIBUTION:")
        for sol_type, count in sorted(
            stats["solution_type_counts"].items(), key=lambda x: x[1], reverse=True
        ):
            print(f"  {sol_type:25s}: {count:4d}")

    total_roles = stats["total_media_roles"] + stats["total_cellular_roles"]
    if total_roles > 0:
        print(f"\nCITATION STATISTICS:")
        print(
            f"  Roles with citations: {stats['roles_with_citations']}/{total_roles} ({stats['roles_with_citations']/total_roles*100:.1f}%)"
        )
        print(
            f"  Roles with DOI: {stats['roles_with_doi']}/{total_roles} ({stats['roles_with_doi']/total_roles*100:.1f}%)"
        )

        if stats["citation_type_counts"]:
            print(f"\n  Citation type breakdown:")
            for cite_type, count in sorted(
                stats["citation_type_counts"].items(), key=lambda x: x[1], reverse=True
            ):
                print(f"    {cite_type:30s}: {count:4d}")

    if stats["confidence_scores"]:
        avg_confidence = sum(stats["confidence_scores"]) / len(stats["confidence_scores"])
        min_confidence = min(stats["confidence_scores"])
        max_confidence = max(stats["confidence_scores"])
        print(f"\nCONFIDENCE SCORES:")
        print(f"  Average: {avg_confidence:.3f}")
        print(f"  Range: {min_confidence:.3f} - {max_confidence:.3f}")

    print(f"\nVALIDATION:")
    if stats["validation_errors"] == 0:
        print(f"  ✅ No validation errors detected")
    else:
        print(f"  ❌ {stats['validation_errors']} validation errors detected")
        print(f"\n  Error details:")
        for error in stats["error_details"][:10]:  # Show first 10 errors
            print(f"    • {error}")
        if len(stats["error_details"]) > 10:
            print(f"    ... and {len(stats['error_details']) - 10} more")


def main():
    """Main validation workflow."""
    print("=" * 80)
    print("ROLE ASSIGNMENT VALIDATION")
    print("=" * 80)

    # Validate both files
    mapped_stats = validate_file(Path("data/curated/mapped_ingredients.yaml"), "mapped")
    unmapped_stats = validate_file(Path("data/curated/unmapped_ingredients.yaml"), "unmapped")

    # Print statistics
    print_stats(mapped_stats, "mapped")
    print_stats(unmapped_stats, "unmapped")

    # Combined statistics
    print(f"\n{'=' * 80}")
    print("COMBINED STATISTICS")
    print("=" * 80)

    total_ingredients = mapped_stats["total_ingredients"] + unmapped_stats["total_ingredients"]
    total_with_media = mapped_stats["with_media_roles"] + unmapped_stats["with_media_roles"]
    total_with_cellular = (
        mapped_stats["with_cellular_roles"] + unmapped_stats["with_cellular_roles"]
    )
    total_with_solution = (
        mapped_stats["with_solution_type"] + unmapped_stats["with_solution_type"]
    )
    total_media_roles = mapped_stats["total_media_roles"] + unmapped_stats["total_media_roles"]
    total_cellular_roles = (
        mapped_stats["total_cellular_roles"] + unmapped_stats["total_cellular_roles"]
    )
    total_roles_with_citations = (
        mapped_stats["roles_with_citations"] + unmapped_stats["roles_with_citations"]
    )
    total_roles_with_doi = mapped_stats["roles_with_doi"] + unmapped_stats["roles_with_doi"]
    total_errors = mapped_stats["validation_errors"] + unmapped_stats["validation_errors"]

    print(f"\nTotal ingredients: {total_ingredients}")
    print(f"With media roles: {total_with_media} ({total_with_media/total_ingredients*100:.1f}%)")
    print(
        f"With cellular roles: {total_with_cellular} ({total_with_cellular/total_ingredients*100:.1f}%)"
    )
    print(
        f"With solution type: {total_with_solution} ({total_with_solution/total_ingredients*100:.1f}%)"
    )
    print(f"\nTotal media roles assigned: {total_media_roles}")
    print(f"Total cellular roles assigned: {total_cellular_roles}")

    total_roles = total_media_roles + total_cellular_roles
    if total_roles > 0:
        print(
            f"\nRoles with citations: {total_roles_with_citations}/{total_roles} ({total_roles_with_citations/total_roles*100:.1f}%)"
        )
        print(
            f"Roles with DOI: {total_roles_with_doi}/{total_roles} ({total_roles_with_doi/total_roles*100:.1f}%)"
        )

        all_confidence = mapped_stats["confidence_scores"] + unmapped_stats["confidence_scores"]
        if all_confidence:
            avg_conf = sum(all_confidence) / len(all_confidence)
            print(f"\nAverage confidence: {avg_conf:.3f}")

    print(f"\nValidation errors: {total_errors}")
    if total_errors == 0:
        print("✅ All role assignments are valid!")
    else:
        print(f"⚠️  Some validation errors detected - review error details above")

    print("\n" + "=" * 80)
    print("✅ Validation complete!")
    print("=" * 80)


if __name__ == "__main__":
    main()
