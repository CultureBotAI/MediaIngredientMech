#!/usr/bin/env python3
"""Generate comprehensive role assignment statistics report.

This script generates a detailed YAML report of role statistics including:
- Summary metrics (coverage, average confidence, citation types)
- Role distribution by type
- Confidence score distribution
- Citation quality metrics
- Top ingredients by occurrence

Output: data/analysis/role_statistics_report.yaml
"""

import sys
from pathlib import Path
from collections import defaultdict
from datetime import datetime

import yaml

# Add src to path
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from mediaingredientmech.curation.ingredient_curator import IngredientCurator


def analyze_ingredients(curator: IngredientCurator) -> dict:
    """Analyze all ingredients for role statistics.

    Args:
        curator: IngredientCurator with loaded records

    Returns:
        Statistics dictionary
    """
    stats = {
        "total_ingredients": len(curator.records),
        "with_roles": 0,
        "total_roles": 0,
        "unique_role_types": set(),
        "role_counts": defaultdict(int),
        "confidence_distribution": defaultdict(int),
        "citation_types": defaultdict(int),
        "multi_role_ingredients": 0,
        "confidence_scores": [],
        "top_ingredients": [],
    }

    print(f"\nAnalyzing {len(curator.records)} ingredients...")

    for i, record in enumerate(curator.records, 1):
        if i % 200 == 0:
            print(f"  Processed {i}/{len(curator.records)} ingredients...")

        media_roles = record.get("media_roles", [])
        if not media_roles:
            continue

        stats["with_roles"] += 1
        stats["total_roles"] += len(media_roles)

        if len(media_roles) > 1:
            stats["multi_role_ingredients"] += 1

        # Collect ingredient info for top list
        ingredient_info = {
            "id": record.get("id"),
            "ontology_id": record.get("ontology_id"),
            "preferred_term": record.get("preferred_term"),
            "occurrence_count": record.get("occurrence_statistics", {}).get(
                "total_occurrences", 0
            ),
            "role_count": len(media_roles),
            "roles": [],
        }

        for role_assignment in media_roles:
            role = role_assignment.get("role")
            confidence = role_assignment.get("confidence", 0.0)
            evidence = role_assignment.get("evidence", [])

            # Count role types
            if role:
                stats["role_counts"][role] += 1
                stats["unique_role_types"].add(role)
                ingredient_info["roles"].append(role)

            # Confidence distribution (binned)
            if confidence is not None:
                stats["confidence_scores"].append(confidence)
                if confidence == 1.0:
                    stats["confidence_distribution"]["1.0"] += 1
                elif confidence >= 0.95:
                    stats["confidence_distribution"]["0.95-0.99"] += 1
                elif confidence >= 0.9:
                    stats["confidence_distribution"]["0.9-0.94"] += 1
                elif confidence >= 0.8:
                    stats["confidence_distribution"]["0.8-0.89"] += 1
                else:
                    stats["confidence_distribution"]["<0.8"] += 1

            # Citation types
            for ev in evidence:
                ref_type = ev.get("reference_type")
                if ref_type:
                    stats["citation_types"][ref_type] += 1

        stats["top_ingredients"].append(ingredient_info)

    # Sort top ingredients by occurrence
    stats["top_ingredients"] = sorted(
        stats["top_ingredients"], key=lambda x: x["occurrence_count"], reverse=True
    )[:20]  # Keep top 20

    return stats


def generate_report(stats: dict, output_path: Path):
    """Generate and save YAML report.

    Args:
        stats: Statistics dictionary
        output_path: Output YAML path
    """
    # Calculate derived metrics
    total_ingredients = stats["total_ingredients"]
    with_roles = stats["with_roles"]
    total_roles = stats["total_roles"]

    avg_confidence = (
        sum(stats["confidence_scores"]) / len(stats["confidence_scores"])
        if stats["confidence_scores"]
        else 0.0
    )

    avg_roles_per_ingredient = total_roles / with_roles if with_roles > 0 else 0.0

    # Build report structure
    report = {
        "generation_date": datetime.now().isoformat(),
        "summary": {
            "total_ingredients": total_ingredients,
            "with_roles": with_roles,
            "coverage_percentage": round(with_roles / total_ingredients * 100, 1)
            if total_ingredients > 0
            else 0.0,
            "total_roles": total_roles,
            "average_roles_per_ingredient": round(avg_roles_per_ingredient, 2),
            "unique_role_types": len(stats["unique_role_types"]),
            "multi_role_ingredients": stats["multi_role_ingredients"],
            "average_confidence": round(avg_confidence, 3),
        },
        "role_distribution": dict(
            sorted(stats["role_counts"].items(), key=lambda x: x[1], reverse=True)
        ),
        "confidence_distribution": dict(
            sorted(
                stats["confidence_distribution"].items(),
                key=lambda x: {
                    "1.0": 5,
                    "0.95-0.99": 4,
                    "0.9-0.94": 3,
                    "0.8-0.89": 2,
                    "<0.8": 1,
                }.get(x[0], 0),
                reverse=True,
            )
        ),
        "citation_types": dict(
            sorted(stats["citation_types"].items(), key=lambda x: x[1], reverse=True)
        ),
        "top_20_ingredients": stats["top_ingredients"],
    }

    # Save report
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, "w") as f:
        yaml.safe_dump(report, f, default_flow_style=False, sort_keys=False)

    print(f"\n✅ Report saved to: {output_path}")


def print_summary(report: dict):
    """Print summary of report.

    Args:
        report: Report dictionary
    """
    print("\n" + "=" * 80)
    print("ROLE STATISTICS SUMMARY")
    print("=" * 80)

    summary = report["summary"]
    print(f"\nCOVERAGE:")
    print(f"  Total ingredients: {summary['total_ingredients']}")
    print(
        f"  With roles: {summary['with_roles']} ({summary['coverage_percentage']}%)"
    )
    print(f"  Multi-role ingredients: {summary['multi_role_ingredients']}")

    print(f"\nROLE METRICS:")
    print(f"  Total roles assigned: {summary['total_roles']}")
    print(f"  Unique role types: {summary['unique_role_types']}")
    print(f"  Average roles per ingredient: {summary['average_roles_per_ingredient']}")

    print(f"\nQUALITY METRICS:")
    print(f"  Average confidence: {summary['average_confidence']}")

    print(f"\nTOP 5 ROLE TYPES:")
    for i, (role, count) in enumerate(
        list(report["role_distribution"].items())[:5], 1
    ):
        print(f"  {i}. {role:25s}: {count:4d}")

    print(f"\nCONFIDENCE DISTRIBUTION:")
    for conf_range, count in report["confidence_distribution"].items():
        print(f"  {conf_range:15s}: {count:4d}")

    print(f"\nCITATION TYPES:")
    for cite_type, count in report["citation_types"].items():
        print(f"  {cite_type:25s}: {count:4d}")

    print(f"\nTOP 5 INGREDIENTS (by occurrence):")
    for i, ing in enumerate(report["top_20_ingredients"][:5], 1):
        roles_str = ", ".join(ing["roles"])
        print(
            f"  {i}. {ing['preferred_term']:30s} ({ing['occurrence_count']:5d} occ, {ing['role_count']} roles: {roles_str})"
        )


def main():
    """Main statistics generation workflow."""
    print("=" * 80)
    print("Generate Role Statistics Report")
    print("=" * 80)

    # Load mapped ingredients
    data_path = Path("data/curated/mapped_ingredients.yaml")
    curator = IngredientCurator(
        data_path=data_path, curator_name="generate_role_statistics"
    )

    print(f"\nLoading ingredient records from: {data_path}")
    curator.load()
    print(f"Loaded {len(curator.records)} records")

    # Analyze ingredients
    stats = analyze_ingredients(curator)

    # Generate report
    output_path = Path("data/analysis/role_statistics_report.yaml")
    generate_report(stats, output_path)

    # Print summary
    with open(output_path) as f:
        report = yaml.safe_load(f)

    print_summary(report)

    print("\n" + "=" * 80)
    print("✅ Statistics generation complete!")
    print("=" * 80)


if __name__ == "__main__":
    main()
