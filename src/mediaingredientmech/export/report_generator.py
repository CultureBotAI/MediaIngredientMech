"""Generate statistics and quality metrics reports from curated ingredient data."""

import json
from collections import Counter
from datetime import datetime
from pathlib import Path
from typing import Any

import yaml


DEFAULT_DATA_DIR = Path(__file__).resolve().parents[3] / "data" / "curated"


def load_yaml(path: Path) -> dict | None:
    """Load a YAML file, returning None if it doesn't exist or is empty."""
    if not path.exists():
        return None
    with open(path) as f:
        return yaml.safe_load(f)


def load_curated_data(
    data_dir: Path | None = None,
) -> tuple[dict | None, dict | None]:
    """Load mapped and unmapped ingredient YAML files.

    Returns (mapped_data, unmapped_data) tuple.
    """
    data_dir = data_dir or DEFAULT_DATA_DIR
    mapped = load_yaml(data_dir / "mapped_ingredients.yaml")
    unmapped = load_yaml(data_dir / "unmapped_ingredients.yaml")
    return mapped, unmapped


def compute_statistics(
    mapped_data: dict | None, unmapped_data: dict | None
) -> dict[str, Any]:
    """Compute overview statistics from mapped/unmapped data."""
    mapped_ingredients = []
    unmapped_ingredients = []

    if mapped_data:
        mapped_ingredients = mapped_data.get("mapped_ingredients", [])
    if unmapped_data:
        unmapped_ingredients = unmapped_data.get("unmapped_ingredients", [])

    total_mapped = len(mapped_ingredients)
    total_unmapped = len(unmapped_ingredients)
    total = total_mapped + total_unmapped

    # Ontology distribution from mapped ingredients
    ontology_dist: Counter = Counter()
    quality_dist: Counter = Counter()
    for ing in mapped_ingredients:
        src = ing.get("ontology_source", "UNKNOWN")
        ontology_dist[src] += 1
        quality = ing.get("mapping_quality", "UNKNOWN")
        quality_dist[quality] += 1

    # Mapping status distribution from unmapped
    status_dist: Counter = Counter()
    for ing in unmapped_ingredients:
        status = ing.get("mapping_status", "UNMAPPED")
        status_dist[status] += 1

    # Category distributions
    mapped_category_dist: Counter = Counter()
    if mapped_data:
        for summary in mapped_data.get("summary_by_category", []):
            cat = summary.get("category", "UNKNOWN")
            count = summary.get("unique_mapped_count", 0)
            mapped_category_dist[cat] = count

    unmapped_category_dist: Counter = Counter()
    if unmapped_data:
        for summary in unmapped_data.get("summary_by_category", []):
            cat = summary.get("category", "UNKNOWN")
            count = summary.get("unique_unmapped_count", 0)
            unmapped_category_dist[cat] = count

    return {
        "total_ingredients": total,
        "total_mapped": total_mapped,
        "total_unmapped": total_unmapped,
        "mapping_percentage": (total_mapped / total * 100) if total > 0 else 0.0,
        "ontology_distribution": dict(ontology_dist.most_common()),
        "quality_distribution": dict(quality_dist.most_common()),
        "unmapped_status_distribution": dict(status_dist.most_common()),
        "mapped_category_distribution": dict(mapped_category_dist),
        "unmapped_category_distribution": dict(unmapped_category_dist),
        "mapped_total_instances": (
            mapped_data.get("total_instances", 0) if mapped_data else 0
        ),
        "unmapped_media_count": (
            unmapped_data.get("media_count", 0) if unmapped_data else 0
        ),
    }


def collect_curation_history(
    mapped_data: dict | None, limit: int = 20
) -> list[dict[str, Any]]:
    """Collect recent curation events from mapped ingredient records.

    The main schema (mediaingredientmech.yaml) has curation_history on IngredientRecord.
    The mapped_ingredients YAML may or may not include these fields depending on
    the data pipeline. We look for curation_history on each ingredient.
    """
    events = []
    if not mapped_data:
        return events

    for ing in mapped_data.get("mapped_ingredients", []):
        for event in ing.get("curation_history", []):
            event_copy = dict(event)
            event_copy["ingredient"] = ing.get("preferred_term", "unknown")
            events.append(event_copy)

    # Sort by timestamp descending
    events.sort(key=lambda e: e.get("timestamp", ""), reverse=True)
    return events[:limit]


def compute_curator_progress(mapped_data: dict | None) -> dict[str, int]:
    """Count curation events per curator."""
    curator_counts: Counter = Counter()
    if not mapped_data:
        return {}

    for ing in mapped_data.get("mapped_ingredients", []):
        for event in ing.get("curation_history", []):
            curator = event.get("curator", "unknown")
            curator_counts[curator] += 1

    return dict(curator_counts.most_common())


def generate_report(data_dir: Path | None = None) -> dict[str, Any]:
    """Generate a full report dictionary."""
    mapped_data, unmapped_data = load_curated_data(data_dir)

    stats = compute_statistics(mapped_data, unmapped_data)
    curation_history = collect_curation_history(mapped_data)
    curator_progress = compute_curator_progress(mapped_data)

    return {
        "generated_at": datetime.now().isoformat(),
        "statistics": stats,
        "curation_history": curation_history,
        "curator_progress": curator_progress,
        "data_files": {
            "mapped_exists": mapped_data is not None,
            "unmapped_exists": unmapped_data is not None,
        },
    }


def report_to_markdown(report: dict[str, Any]) -> str:
    """Convert report dict to Markdown string."""
    lines = []
    lines.append("# MediaIngredientMech Curation Report")
    lines.append(f"\nGenerated: {report['generated_at']}\n")

    stats = report["statistics"]

    lines.append("## Overview\n")
    lines.append(f"| Metric | Value |")
    lines.append(f"|--------|-------|")
    lines.append(f"| Total ingredients | {stats['total_ingredients']} |")
    lines.append(f"| Mapped | {stats['total_mapped']} |")
    lines.append(f"| Unmapped | {stats['total_unmapped']} |")
    lines.append(f"| Mapping % | {stats['mapping_percentage']:.1f}% |")
    lines.append(f"| Mapped instances | {stats['mapped_total_instances']} |")
    lines.append("")

    if stats["ontology_distribution"]:
        lines.append("## Ontology Distribution\n")
        lines.append("| Ontology | Count |")
        lines.append("|----------|-------|")
        for ont, count in stats["ontology_distribution"].items():
            lines.append(f"| {ont} | {count} |")
        lines.append("")

    if stats["quality_distribution"]:
        lines.append("## Mapping Quality Distribution\n")
        lines.append("| Quality | Count |")
        lines.append("|---------|-------|")
        for qual, count in stats["quality_distribution"].items():
            lines.append(f"| {qual} | {count} |")
        lines.append("")

    if stats["unmapped_status_distribution"]:
        lines.append("## Unmapped Status Distribution\n")
        lines.append("| Status | Count |")
        lines.append("|--------|-------|")
        for status, count in stats["unmapped_status_distribution"].items():
            lines.append(f"| {status} | {count} |")
        lines.append("")

    if report["curator_progress"]:
        lines.append("## Curator Progress\n")
        lines.append("| Curator | Actions |")
        lines.append("|---------|---------|")
        for curator, count in report["curator_progress"].items():
            lines.append(f"| {curator} | {count} |")
        lines.append("")

    if report["curation_history"]:
        lines.append("## Recent Curation Activity\n")
        lines.append("| Timestamp | Curator | Action | Ingredient |")
        lines.append("|-----------|---------|--------|------------|")
        for event in report["curation_history"]:
            ts = event.get("timestamp", "N/A")
            curator = event.get("curator", "N/A")
            action = event.get("action", "N/A")
            ingredient = event.get("ingredient", "N/A")
            lines.append(f"| {ts} | {curator} | {action} | {ingredient} |")
        lines.append("")

    return "\n".join(lines)


def report_to_json(report: dict[str, Any]) -> str:
    """Convert report dict to JSON string."""
    return json.dumps(report, indent=2, default=str)
