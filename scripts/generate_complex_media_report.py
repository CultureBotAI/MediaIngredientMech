#!/usr/bin/env python3
"""Generate comprehensive report of suspected complex media entries.

This script analyzes all ingredients and generates a detailed report of entries
that may be complex media rather than single ingredients, organized by CHEBI ID
and confidence level.

Usage:
    python scripts/generate_complex_media_report.py
    python scripts/generate_complex_media_report.py --output-format markdown
    python scripts/generate_complex_media_report.py --output analysis/complex_media_report.md
"""

import argparse
import sys
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import yaml

# Add src to path
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from mediaingredientmech.curation.ingredient_curator import IngredientCurator

# Import detection functions from identify_complex_media
sys.path.insert(0, str(Path(__file__).parent))
from identify_complex_media import detect_complex_medium


def group_by_chebi_id(entries: list[dict]) -> dict[str, list[dict]]:
    """Group entries by their CHEBI ID.

    Args:
        entries: List of detected complex media entries.

    Returns:
        Dict mapping CHEBI ID to list of entries.
    """
    grouped = defaultdict(list)

    for entry in entries:
        ontology_id = entry["record"].get("ontology_mapping", {}).get("ontology_id", "UNMAPPED")
        grouped[ontology_id].append(entry)

    return dict(grouped)


def generate_markdown_report(
    curator: IngredientCurator,
    results: dict[str, list[dict]],
    output_path: Path
) -> None:
    """Generate Markdown format report.

    Args:
        curator: IngredientCurator instance.
        results: Analysis results from identify_complex_media.
        output_path: Path to output file.
    """
    lines = []

    # Header
    lines.append("# Complex Media Detection Report")
    lines.append(f"\n**Generated**: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    lines.append(f"**Data source**: {curator.data_path}")
    lines.append(f"**Total records analyzed**: {len(curator.records)}\n")

    # Summary
    lines.append("## Summary\n")
    total_complex = len(results["complex_media_high"]) + len(results["complex_media_medium"])
    lines.append(f"- **High confidence complex media**: {len(results['complex_media_high'])}")
    lines.append(f"- **Medium confidence complex media**: {len(results['complex_media_medium'])}")
    lines.append(f"- **Total suspected complex media**: {total_complex}")
    lines.append(f"- **Single ingredients**: {len(results['single_ingredients'])}")
    lines.append(f"- **Uncertain**: {len(results['uncertain'])}\n")

    # High confidence - grouped by CHEBI ID
    if results["complex_media_high"]:
        lines.append("## High Confidence Complex Media\n")
        lines.append("These entries are very likely complete media formulations, not single ingredients.\n")

        grouped = group_by_chebi_id(results["complex_media_high"])

        for chebi_id in sorted(grouped.keys()):
            entries = grouped[chebi_id]
            lines.append(f"### {chebi_id} ({len(entries)} entries)\n")

            # Get CHEBI label from first entry
            first_entry = entries[0]
            chebi_label = first_entry["record"].get("ontology_mapping", {}).get("ontology_label", "N/A")
            lines.append(f"**Ontology label**: {chebi_label}\n")

            lines.append("| Name | Confidence | Reason | Occurrences |")
            lines.append("|------|------------|--------|-------------|")

            for entry in sorted(entries, key=lambda x: x["confidence"], reverse=True):
                record = entry["record"]
                name = record.get("preferred_term", "")
                confidence = entry["confidence"]
                reason = entry["reason"].replace("|", "\\|")  # Escape pipes
                occurrences = record.get("occurrence_statistics", {}).get("total_occurrences", 0)

                lines.append(f"| {name} | {confidence:.2f} | {reason} | {occurrences} |")

            lines.append("")

    # Medium confidence
    if results["complex_media_medium"]:
        lines.append("## Medium Confidence Complex Media\n")
        lines.append("These entries may be complex media. Manual review recommended.\n")

        grouped = group_by_chebi_id(results["complex_media_medium"])

        for chebi_id in sorted(grouped.keys()):
            entries = grouped[chebi_id]
            lines.append(f"### {chebi_id} ({len(entries)} entries)\n")

            lines.append("| Name | Confidence | Reason |")
            lines.append("|------|------------|--------|")

            for entry in sorted(entries, key=lambda x: x["confidence"], reverse=True):
                record = entry["record"]
                name = record.get("preferred_term", "")
                confidence = entry["confidence"]
                reason = entry["reason"].replace("|", "\\|")

                lines.append(f"| {name} | {confidence:.2f} | {reason} |")

            lines.append("")

    # Recommendations
    lines.append("## Recommendations\n")
    lines.append("### Immediate Actions\n")
    lines.append("1. **Review high-confidence entries** - These should likely be reclassified as `DEFINED_MEDIUM`")
    lines.append("2. **Check CHEBI mappings** - Complex media should not be mapped to pure chemical CHEBI terms")
    lines.append("3. **Cross-reference CultureMech** - Find full recipe formulations for these media\n")

    lines.append("### Reclassification Steps\n")
    lines.append("```bash")
    lines.append("# Interactive review")
    lines.append("python scripts/identify_complex_media.py --interactive")
    lines.append("")
    lines.append("# Auto-reclassify high confidence (dry run first)")
    lines.append("python scripts/identify_complex_media.py --auto-reclassify --dry-run")
    lines.append("")
    lines.append("# Cross-reference with CultureMech")
    lines.append("python scripts/cross_reference_culturemech.py --complex-media-only")
    lines.append("```\n")

    # Specific cases
    lines.append("## Special Cases Requiring Expert Review\n")

    # Find agar cases
    agar_entries = []
    for entry in results["complex_media_high"]:
        if entry["record"].get("ontology_mapping", {}).get("ontology_id") == "CHEBI:2509":
            agar_entries.append(entry)

    if agar_entries:
        lines.append(f"### Agar Variants (CHEBI:2509) - {len(agar_entries)} entries\n")
        lines.append("These entries are mapped to agar but appear to be complete agar-based media:\n")
        for entry in sorted(agar_entries, key=lambda x: x["record"].get("preferred_term", "")):
            name = entry["record"].get("preferred_term", "")
            lines.append(f"- **{name}**")

            # Note if it's a known complex medium
            if any(keyword in name.lower() for keyword in ["marine", "r2a", "corn meal", "oatmeal", "broth"]):
                lines.append(f"  - Contains additional ingredients beyond agar")
                lines.append(f"  - Should cross-reference to CultureMech for full recipe")

        lines.append("")

    # Write to file
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, "w") as f:
        f.write("\n".join(lines))

    print(f"Report written to: {output_path}")


def generate_yaml_report(
    curator: IngredientCurator,
    results: dict[str, list[dict]],
    output_path: Path
) -> None:
    """Generate YAML format report.

    Args:
        curator: IngredientCurator instance.
        results: Analysis results.
        output_path: Path to output file.
    """
    report = {
        "generation_date": datetime.now(timezone.utc).isoformat(),
        "data_source": str(curator.data_path),
        "total_records": len(curator.records),
        "summary": {
            "high_confidence_complex_media": len(results["complex_media_high"]),
            "medium_confidence_complex_media": len(results["complex_media_medium"]),
            "single_ingredients": len(results["single_ingredients"]),
            "uncertain": len(results["uncertain"]),
        },
        "high_confidence_by_chebi": {},
        "medium_confidence_by_chebi": {},
    }

    # Group high confidence by CHEBI
    grouped_high = group_by_chebi_id(results["complex_media_high"])
    for chebi_id, entries in grouped_high.items():
        report["high_confidence_by_chebi"][chebi_id] = [
            {
                "name": e["record"].get("preferred_term", ""),
                "confidence": e["confidence"],
                "reason": e["reason"],
                "occurrences": e["record"].get("occurrence_statistics", {}).get("total_occurrences", 0),
            }
            for e in entries
        ]

    # Group medium confidence by CHEBI
    grouped_medium = group_by_chebi_id(results["complex_media_medium"])
    for chebi_id, entries in grouped_medium.items():
        report["medium_confidence_by_chebi"][chebi_id] = [
            {
                "name": e["record"].get("preferred_term", ""),
                "confidence": e["confidence"],
                "reason": e["reason"],
            }
            for e in entries
        ]

    # Write to file
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, "w") as f:
        yaml.dump(report, f, default_flow_style=False, sort_keys=False)

    print(f"Report written to: {output_path}")


def main():
    """Main workflow."""
    parser = argparse.ArgumentParser(
        description="Generate comprehensive complex media detection report"
    )
    parser.add_argument(
        "--data-path",
        type=Path,
        default=Path("data/curated/mapped_ingredients.yaml"),
        help="Path to ingredient data file",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=Path("analysis/complex_media_report.md"),
        help="Path to output report file",
    )
    parser.add_argument(
        "--output-format",
        choices=["markdown", "yaml"],
        default="markdown",
        help="Output format (default: markdown)",
    )

    args = parser.parse_args()

    # Load data
    print(f"\nLoading ingredients from {args.data_path}...")
    curator = IngredientCurator(data_path=args.data_path)
    curator.load()
    print(f"Loaded {len(curator.records)} ingredient records\n")

    # Analyze (use function from identify_complex_media)
    print("Analyzing ingredients...")
    from identify_complex_media import analyze_ingredients
    results = analyze_ingredients(curator)

    # Generate report
    print(f"Generating {args.output_format} report...\n")

    if args.output_format == "markdown":
        generate_markdown_report(curator, results, args.output)
    else:
        generate_yaml_report(curator, results, args.output)

    # Print summary
    print("\n" + "="*60)
    print("Summary:")
    print(f"  High confidence: {len(results['complex_media_high'])}")
    print(f"  Medium confidence: {len(results['complex_media_medium'])}")
    print(f"  Single ingredients: {len(results['single_ingredients'])}")
    print(f"  Uncertain: {len(results['uncertain'])}")
    print("="*60 + "\n")

    return 0


if __name__ == "__main__":
    sys.exit(main())
