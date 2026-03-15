#!/usr/bin/env python3
"""Analyze merge patterns from merged vs pre-merge data.

Compares data/curated/mapped_ingredients_WITH_MERGES.yaml with
data/curated/mapped_ingredients.yaml to identify:
1. What was merged (clusters)
2. Why it was merged (CHEBI ID, quality, occurrence)
3. Whether it should have been merged (complex media detection)
4. Pattern classification (good vs bad merges)
"""

import argparse
import sys
from pathlib import Path
from typing import Any

import yaml
from rich.console import Console
from rich.table import Table

# Add src to path
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

# Import detect_complex_medium from identify_complex_media
import importlib.util
spec = importlib.util.spec_from_file_location(
    "identify_complex_media",
    Path(__file__).parent / "identify_complex_media.py"
)
identify_complex_media = importlib.util.module_from_spec(spec)
spec.loader.exec_module(identify_complex_media)
detect_complex_medium = identify_complex_media.detect_complex_medium

console = Console()


def load_yaml(filepath: str) -> dict[str, Any]:
    """Load YAML file."""
    with open(filepath) as f:
        return yaml.safe_load(f)


def save_yaml(data: dict[str, Any], filepath: str) -> None:
    """Save YAML file."""
    with open(filepath, "w") as f:
        yaml.dump(data, f, default_flow_style=False, sort_keys=False, allow_unicode=True)


def save_markdown(content: str, filepath: str) -> None:
    """Save markdown file."""
    with open(filepath, "w") as f:
        f.write(content)


def extract_merge_clusters(merged_data: dict) -> dict[str, dict]:
    """Extract all merge clusters from merged data.

    Returns:
        Dict mapping representative ID to cluster info:
        {
            'rep_id': {
                'representative': record,
                'merged': [list of merged records]
            }
        }
    """
    clusters = {}

    # Build index by ID
    by_id = {r["id"]: r for r in merged_data["ingredients"]}

    # Find all representative records (those with 'merged' field)
    for record in merged_data["ingredients"]:
        if "merged" in record:
            rep_id = record["id"]
            merged_ids = record["merged"]

            # Get merged records
            merged_records = []
            for merged_id in merged_ids:
                if merged_id in by_id:
                    merged_records.append(by_id[merged_id])
                else:
                    console.print(f"[yellow]Warning: merged ID {merged_id} not found[/yellow]")

            clusters[rep_id] = {
                "representative": record,
                "merged": merged_records
            }

    return clusters


def classify_merge_pattern(cluster: dict) -> dict[str, Any]:
    """Classify a merge cluster as good, bad, or needs review.

    Args:
        cluster: Dict with 'representative' and 'merged' keys

    Returns:
        Dict with classification info:
        {
            'classification': 'GOOD_MERGE' | 'BAD_MERGE' | 'NEEDS_REVIEW',
            'pattern': str (description of pattern),
            'confidence': float (0-1),
            'reasons': [list of reasons],
            'issues': [list of issues if bad]
        }
    """
    rep = cluster["representative"]
    merged = cluster["merged"]

    all_records = [rep] + merged

    reasons = []
    issues = []
    pattern = "unknown"

    # Get basic info
    rep_name = rep.get("preferred_term", "")
    merged_names = [r.get("preferred_term", "") for r in merged]
    all_names = [rep_name] + merged_names

    rep_chebi = rep.get("ontology_mapping", {}).get("ontology_id", "")

    # Check for complex media in any record
    complex_detected = []
    for i, record in enumerate(all_records):
        name = record.get("preferred_term", "")
        chebi = record.get("ontology_mapping", {}).get("ontology_id", "")
        is_complex, conf, reason = detect_complex_medium(name, chebi)
        if is_complex and conf >= 0.75:
            record_type = "representative" if i == 0 else f"merged[{i-1}]"
            complex_detected.append({
                "record": record_type,
                "name": name,
                "confidence": conf,
                "reason": reason
            })

    # Check ingredient_type consistency
    ingredient_types = [r.get("ingredient_type") for r in all_records if r.get("ingredient_type")]
    unique_types = set(ingredient_types)

    # BAD: Complex media detected
    if complex_detected:
        issues.append(f"Complex media detected in {len(complex_detected)} record(s)")
        for item in complex_detected:
            issues.append(f"  • {item['record']}: {item['name']} - {item['reason']}")
        return {
            "classification": "BAD_MERGE",
            "pattern": "complex_media_mixed_with_ingredient",
            "confidence": max(item["confidence"] for item in complex_detected),
            "reasons": reasons,
            "issues": issues,
            "complex_media": complex_detected
        }

    # BAD: Different ingredient types
    if len(unique_types) > 1:
        issues.append(f"Different ingredient_type values: {unique_types}")
        return {
            "classification": "BAD_MERGE",
            "pattern": "inconsistent_ingredient_type",
            "confidence": 1.0,
            "reasons": reasons,
            "issues": issues
        }

    # Now check for good patterns

    # Pattern 1: Case variation only
    normalized_names = [n.lower().strip() for n in all_names]
    if len(set(normalized_names)) == 1:
        pattern = "case_variation"
        reasons.append(f"All names are case variations: {all_names}")
        return {
            "classification": "GOOD_MERGE",
            "pattern": pattern,
            "confidence": 1.0,
            "reasons": reasons,
            "issues": []
        }

    # Pattern 2: Chemical synonyms (same CHEBI, different names)
    if rep_chebi and rep_chebi.startswith("CHEBI:"):
        # Check if names are reasonable synonyms
        # Simple heuristic: if they share significant words or one is abbreviation
        rep_words = set(rep_name.lower().split())

        is_synonym = True
        synonym_reasons = []

        for merged_name in merged_names:
            merged_words = set(merged_name.lower().split())

            # Check for common words
            common = rep_words & merged_words
            if len(common) > 0:
                synonym_reasons.append(f"{rep_name} / {merged_name}: shared words {common}")
            # Check for abbreviation (one much shorter)
            elif len(merged_name) < len(rep_name) * 0.3 or len(rep_name) < len(merged_name) * 0.3:
                synonym_reasons.append(f"{rep_name} / {merged_name}: possible abbreviation")
            # Check for chemical formula patterns
            elif any(c.isdigit() for c in rep_name) or any(c.isdigit() for c in merged_name):
                synonym_reasons.append(f"{rep_name} / {merged_name}: chemical formula variants")
            else:
                is_synonym = False
                break

        if is_synonym:
            pattern = "chemical_synonym"
            reasons.extend(synonym_reasons)
            return {
                "classification": "GOOD_MERGE",
                "pattern": pattern,
                "confidence": 0.9,
                "reasons": reasons,
                "issues": []
            }

    # Pattern 3: Hydrate variants
    hydrate_keywords = ["hydrate", "·", "•", "H2O", "anhydrous"]
    has_hydrate = any(any(kw in name for kw in hydrate_keywords) for name in all_names)

    if has_hydrate:
        pattern = "hydrate_variant"
        reasons.append(f"Hydrate form detected in: {all_names}")
        # This is GOOD but with caution (might want hierarchy instead)
        return {
            "classification": "NEEDS_REVIEW",
            "pattern": pattern,
            "confidence": 0.7,
            "reasons": reasons,
            "issues": ["Hydrate forms might benefit from hierarchy instead of merge"]
        }

    # Default: needs review
    reasons.append(f"No clear pattern detected for: {all_names}")
    return {
        "classification": "NEEDS_REVIEW",
        "pattern": "unclear",
        "confidence": 0.5,
        "reasons": reasons,
        "issues": ["Unable to determine if merge is valid"]
    }


def generate_analysis_report(clusters: dict, original_data: dict) -> dict:
    """Generate comprehensive analysis report.

    Args:
        clusters: Dict of merge clusters
        original_data: Pre-merge data for reference

    Returns:
        Dict with analysis results
    """
    report = {
        "summary": {
            "total_clusters": len(clusters),
            "total_merged_records": sum(len(c["merged"]) for c in clusters.values()),
            "classifications": {
                "GOOD_MERGE": 0,
                "BAD_MERGE": 0,
                "NEEDS_REVIEW": 0
            },
            "patterns": {}
        },
        "clusters_by_classification": {
            "GOOD_MERGE": [],
            "BAD_MERGE": [],
            "NEEDS_REVIEW": []
        }
    }

    # Classify all clusters
    for rep_id, cluster in clusters.items():
        classification = classify_merge_pattern(cluster)

        cluster_info = {
            "representative_id": rep_id,
            "representative_name": cluster["representative"].get("preferred_term"),
            "merged_count": len(cluster["merged"]),
            "merged_names": [r.get("preferred_term") for r in cluster["merged"]],
            "classification": classification["classification"],
            "pattern": classification["pattern"],
            "confidence": classification["confidence"],
            "reasons": classification["reasons"],
            "issues": classification["issues"]
        }

        # Update summary
        cls = classification["classification"]
        report["summary"]["classifications"][cls] += 1

        pattern = classification["pattern"]
        if pattern not in report["summary"]["patterns"]:
            report["summary"]["patterns"][pattern] = 0
        report["summary"]["patterns"][pattern] += 1

        # Add to appropriate list
        report["clusters_by_classification"][cls].append(cluster_info)

    return report


def generate_markdown_report(report: dict) -> str:
    """Generate markdown report from analysis."""

    lines = [
        "# MediaIngredientMech Merge Pattern Analysis",
        "",
        f"**Analysis Date:** {Path.cwd()}",
        "",
        "## Summary Statistics",
        "",
        f"- **Total merge clusters:** {report['summary']['total_clusters']}",
        f"- **Total merged records:** {report['summary']['total_merged_records']}",
        "",
        "### Classifications",
        "",
    ]

    for cls, count in report["summary"]["classifications"].items():
        pct = count / report["summary"]["total_clusters"] * 100 if report["summary"]["total_clusters"] > 0 else 0
        emoji = "✅" if cls == "GOOD_MERGE" else "❌" if cls == "BAD_MERGE" else "⚠️"
        lines.append(f"- {emoji} **{cls}:** {count} ({pct:.1f}%)")

    lines.extend([
        "",
        "### Patterns Detected",
        "",
    ])

    for pattern, count in sorted(report["summary"]["patterns"].items(), key=lambda x: -x[1]):
        lines.append(f"- **{pattern}:** {count}")

    lines.extend([
        "",
        "---",
        "",
        "## Good Merges (Safe Patterns)",
        "",
    ])

    good_merges = report["clusters_by_classification"]["GOOD_MERGE"]
    if good_merges:
        # Group by pattern
        by_pattern = {}
        for cluster in good_merges:
            pattern = cluster["pattern"]
            if pattern not in by_pattern:
                by_pattern[pattern] = []
            by_pattern[pattern].append(cluster)

        for pattern, clusters in by_pattern.items():
            lines.extend([
                f"### Pattern: {pattern}",
                "",
                f"**Count:** {len(clusters)} clusters",
                "",
                "**Examples:**",
                "",
            ])

            # Show first 5 examples
            for cluster in clusters[:5]:
                all_names = [cluster["representative_name"]] + cluster["merged_names"]
                lines.append(f"- **{cluster['representative_name']}** ← {cluster['merged_names']}")
                if cluster["reasons"]:
                    lines.append(f"  - *Reason:* {cluster['reasons'][0]}")

            if len(clusters) > 5:
                lines.append(f"  - *...and {len(clusters) - 5} more*")

            lines.append("")
    else:
        lines.append("*No good merges found*")

    lines.extend([
        "",
        "---",
        "",
        "## Bad Merges (Dangerous Patterns)",
        "",
    ])

    bad_merges = report["clusters_by_classification"]["BAD_MERGE"]
    if bad_merges:
        lines.append(f"**Count:** {len(bad_merges)} clusters")
        lines.append("")

        for i, cluster in enumerate(bad_merges, 1):
            lines.extend([
                f"### {i}. {cluster['representative_name']}",
                "",
                f"- **Merged records:** {len(cluster['merged_names'])}",
                f"- **Pattern:** {cluster['pattern']}",
                f"- **Confidence:** {cluster['confidence']:.2f}",
                "",
                "**Merged names:**",
                "",
            ])

            for name in cluster["merged_names"]:
                lines.append(f"- {name}")

            lines.extend([
                "",
                "**Issues:**",
                "",
            ])

            for issue in cluster["issues"]:
                lines.append(f"- {issue}")

            lines.append("")
    else:
        lines.append("*No bad merges found*")

    lines.extend([
        "",
        "---",
        "",
        "## Needs Review",
        "",
    ])

    review_merges = report["clusters_by_classification"]["NEEDS_REVIEW"]
    if review_merges:
        lines.append(f"**Count:** {len(review_merges)} clusters")
        lines.append("")

        # Group by pattern
        by_pattern = {}
        for cluster in review_merges:
            pattern = cluster["pattern"]
            if pattern not in by_pattern:
                by_pattern[pattern] = []
            by_pattern[pattern].append(cluster)

        for pattern, clusters in by_pattern.items():
            lines.extend([
                f"### Pattern: {pattern}",
                "",
                f"**Count:** {len(clusters)} clusters",
                "",
                "**Examples (first 3):**",
                "",
            ])

            for cluster in clusters[:3]:
                lines.append(f"- **{cluster['representative_name']}** ← {cluster['merged_names']}")
                if cluster["issues"]:
                    lines.append(f"  - *Issues:* {'; '.join(cluster['issues'])}")

            if len(clusters) > 3:
                lines.append(f"  - *...and {len(clusters) - 3} more*")

            lines.append("")
    else:
        lines.append("*No merges need review*")

    lines.extend([
        "",
        "---",
        "",
        "## Recommendations",
        "",
        "### Pre-Merge Validation Rules",
        "",
        "Based on this analysis, implement these safety checks before merging:",
        "",
        "1. **Complex Media Detection**",
        "   - Run `detect_complex_medium()` on all records",
        "   - Block merge if confidence >= 0.75",
        "   - Rationale: Prevents recipes from merging into ingredients",
        "",
        "2. **Ingredient Type Consistency**",
        "   - Verify all records have same `ingredient_type`",
        "   - Block merge if types differ",
        "   - Rationale: Different types indicate different semantic categories",
        "",
        "3. **Pattern Matching**",
        "   - Prefer merges with clear patterns (case, synonym, abbreviation)",
        "   - Flag unclear patterns for manual review",
        "   - Rationale: Ambiguous merges risk data corruption",
        "",
        "4. **Hydrate Handling**",
        "   - Consider hierarchy instead of merge for hydrate variants",
        "   - Flag for expert review",
        "   - Rationale: Different hydration states may have different properties",
        "",
        "### Implementation in CHEBIDeduplicator",
        "",
        "Update `should_auto_merge()` method to include:",
        "",
        "```python",
        "# Check ingredient_type",
        "if target_type != source_type:",
        "    return False, 'Different ingredient types'",
        "",
        "# Check complex media",
        "is_complex, conf, reason = detect_complex_medium(name, chebi)",
        "if is_complex and conf >= 0.75:",
        "    return False, f'Complex media: {reason}'",
        "```",
        "",
    ])

    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(description="Analyze merge patterns")
    parser.add_argument(
        "--merged-file",
        default="data/curated/mapped_ingredients_WITH_MERGES.yaml",
        help="Path to merged data file"
    )
    parser.add_argument(
        "--original-file",
        default="data/curated/mapped_ingredients.yaml",
        help="Path to pre-merge data file"
    )
    parser.add_argument(
        "--output-yaml",
        default="analysis/merge_pattern_analysis.yaml",
        help="Path to output YAML report"
    )
    parser.add_argument(
        "--output-md",
        default="analysis/merge_pattern_analysis.md",
        help="Path to output markdown report"
    )

    args = parser.parse_args()

    # Create output directory
    Path(args.output_yaml).parent.mkdir(exist_ok=True)

    # Load data
    console.print(f"[cyan]Loading merged data from {args.merged_file}...[/cyan]")
    merged_data = load_yaml(args.merged_file)

    console.print(f"[cyan]Loading original data from {args.original_file}...[/cyan]")
    original_data = load_yaml(args.original_file)

    # Extract clusters
    console.print("[cyan]Extracting merge clusters...[/cyan]")
    clusters = extract_merge_clusters(merged_data)
    console.print(f"[green]Found {len(clusters)} merge clusters[/green]")

    # Generate analysis
    console.print("[cyan]Analyzing merge patterns...[/cyan]")
    report = generate_analysis_report(clusters, original_data)

    # Display summary
    console.print("\n[bold]Analysis Summary:[/bold]")
    table = Table(show_header=True)
    table.add_column("Classification")
    table.add_column("Count", justify="right")
    table.add_column("Percentage", justify="right")

    total = report["summary"]["total_clusters"]
    for cls, count in report["summary"]["classifications"].items():
        pct = count / total * 100 if total > 0 else 0
        emoji = "✅" if cls == "GOOD_MERGE" else "❌" if cls == "BAD_MERGE" else "⚠️"
        table.add_row(f"{emoji} {cls}", str(count), f"{pct:.1f}%")

    console.print(table)

    # Save YAML report
    console.print(f"\n[cyan]Saving YAML report to {args.output_yaml}...[/cyan]")
    save_yaml(report, args.output_yaml)

    # Generate and save markdown report
    console.print(f"[cyan]Generating markdown report...[/cyan]")
    md_content = generate_markdown_report(report)
    save_markdown(md_content, args.output_md)
    console.print(f"[green]Saved markdown report to {args.output_md}[/green]")

    console.print("\n[bold green]✓ Analysis complete![/bold green]")


if __name__ == "__main__":
    main()
