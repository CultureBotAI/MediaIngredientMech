#!/usr/bin/env python3
"""
Generate index files for all MediaIngredientMech records.

Creates JSON, CSV, and Markdown exports for easy reference.
"""

import csv
import json
from pathlib import Path

import yaml


def load_records(path: Path) -> list[dict]:
    """Load the aggregate collection that drives one curated index."""
    doc = yaml.safe_load(path.read_text(encoding='utf-8')) or {}
    records = doc.get('ingredients')
    if not isinstance(records, list):
        raise ValueError(f"{path} does not contain an ingredients list")
    return records


def generate_json_index(records: list[dict], output_path: Path) -> None:
    """Generate JSON index with key fields."""
    index = []

    for record in records:
        entry = {
            'identifier': record.get('identifier'),
            'preferred_term': record.get('preferred_term'),
            'mapping_status': record.get('mapping_status'),
            'occurrences': record.get('occurrence_statistics', {}).get('total_occurrences', 0),
        }

        # Add ontology mapping if exists
        om = record.get('ontology_mapping')
        if isinstance(om, dict):
            entry['ontology_id'] = om.get('ontology_id')
            entry['ontology_source'] = om.get('ontology_source')
            entry['mapping_quality'] = om.get('mapping_quality')

        index.append(entry)

    with open(output_path, 'w') as f:
        json.dump(index, f, indent=2)

    print(f"✓ Created {output_path} ({len(index)} records)")


def generate_csv_index(records: list[dict], output_path: Path) -> None:
    """Generate CSV index with key fields."""
    with open(output_path, 'w', newline='') as f:
        # Use repository-stable LF endings so changed rows pass `git diff --check`
        # on every platform.
        writer = csv.writer(f, lineterminator='\n')

        # Header
        writer.writerow([
            'identifier',
            'preferred_term',
            'mapping_status',
            'ontology_id',
            'ontology_source',
            'mapping_quality',
            'occurrences',
        ])

        # Rows
        for record in records:
            om = record.get('ontology_mapping') or {}
            writer.writerow([
                record.get('identifier', ''),
                record.get('preferred_term', ''),
                record.get('mapping_status', ''),
                om.get('ontology_id', ''),
                om.get('ontology_source', ''),
                om.get('mapping_quality', ''),
                record.get('occurrence_statistics', {}).get('total_occurrences', 0),
            ])

    print(f"✓ Created {output_path} ({len(records)} records)")


def generate_markdown_index(records: list[dict], output_path: Path, title: str) -> None:
    """Generate Markdown index with formatted tables."""
    lines = [f"# {title}\n"]

    # Summary stats
    total = len(records)
    mapped = sum(1 for r in records if r.get('mapping_status') == 'MAPPED')
    unmapped = sum(1 for r in records if r.get('mapping_status') == 'UNMAPPED')
    other = total - mapped - unmapped
    total_occurrences = sum(r.get('occurrence_statistics', {}).get('total_occurrences', 0) for r in records)

    lines.append(f"**Total Records**: {total}\n")
    lines.append(f"**Mapped**: {mapped} ({mapped/total*100:.1f}%)\n")
    lines.append(f"**Unmapped**: {unmapped} ({unmapped/total*100:.1f}%)\n")
    if other:
        lines.append(f"**Other statuses**: {other} ({other/total*100:.1f}%) — REJECTED, NEEDS_EXPERT, PENDING_REVIEW, IN_PROGRESS, AMBIGUOUS\n")
    lines.append(f"**Total Occurrences**: {total_occurrences:,}\n")
    lines.append("\n---\n\n")

    # Mapped ingredients table
    if mapped > 0:
        lines.append("## Mapped Ingredients\n\n")
        lines.append("| Identifier | Preferred Term | Ontology ID | Source | Quality | Occurrences |\n")
        lines.append("|---|---|---|---|---|---|\n")

        for record in records:
            if record.get('mapping_status') != 'MAPPED':
                continue

            om = record.get('ontology_mapping') or {}
            lines.append(
                f"| {record.get('identifier', '')} "
                f"| {record.get('preferred_term', '')} "
                f"| {om.get('ontology_id', '')} "
                f"| {om.get('ontology_source', '')} "
                f"| {om.get('mapping_quality', '')} "
                f"| {record.get('occurrence_statistics', {}).get('total_occurrences', 0)} |\n"
            )

        lines.append("\n")

    # Unmapped ingredients table
    if unmapped > 0:
        lines.append("## Unmapped Ingredients\n\n")
        lines.append("| Identifier | Preferred Term | Status | Occurrences |\n")
        lines.append("|---|---|---|---|\n")

        for record in records:
            if record.get('mapping_status') != 'UNMAPPED':
                continue

            lines.append(
                f"| {record.get('identifier', '')} "
                f"| {record.get('preferred_term', '')} "
                f"| {record.get('mapping_status', '')} "
                f"| {record.get('occurrence_statistics', {}).get('total_occurrences', 0)} |\n"
            )

        lines.append("\n")

    # Other-status ingredients table (REJECTED, NEEDS_EXPERT, PENDING_REVIEW,
    # IN_PROGRESS, AMBIGUOUS — anything that isn't MAPPED or UNMAPPED).
    # Keeps the digest self-consistent: every record in `records` appears in
    # exactly one of the three sections so the summary counts add up.
    if other > 0:
        lines.append("## Other Statuses\n\n")
        lines.append("| Identifier | Preferred Term | Status | Ontology ID | Representative | Occurrences |\n")
        lines.append("|---|---|---|---|---|---|\n")

        for record in records:
            status = record.get('mapping_status')
            if status in ('MAPPED', 'UNMAPPED'):
                continue
            om = record.get('ontology_mapping') or {}
            lines.append(
                f"| {record.get('identifier', '')} "
                f"| {record.get('preferred_term', '')} "
                f"| {status or ''} "
                f"| {om.get('ontology_id', '')} "
                f"| {record.get('representative', '')} "
                f"| {record.get('occurrence_statistics', {}).get('total_occurrences', 0)} |\n"
            )

        lines.append("\n")

    with open(output_path, 'w') as f:
        f.writelines(lines)

    print(f"✓ Created {output_path}")


def main():
    """Generate all index files."""
    print("=" * 80)
    print("GENERATING INDEX FILES")
    print("=" * 80)
    print()

    mapped_records = load_records(Path('data/curated/mapped_ingredients.yaml'))
    print(f"Loaded {len(mapped_records)} mapped ingredients")

    unmapped_records = load_records(Path('data/curated/unmapped_ingredients.yaml'))
    print(f"Loaded {len(unmapped_records)} unmapped ingredients")
    print()

    all_records = mapped_records + unmapped_records
    print(f"Total: {len(all_records)} ingredients")
    print()

    output_dir = Path('data/curated')

    # Generate JSON
    print("Generating JSON indexes...")
    generate_json_index(mapped_records, output_dir / 'mapped_ingredients_index.json')
    generate_json_index(unmapped_records, output_dir / 'unmapped_ingredients_index.json')
    generate_json_index(all_records, output_dir / 'all_ingredients_index.json')
    print()

    # Generate CSV
    print("Generating CSV indexes...")
    generate_csv_index(mapped_records, output_dir / 'mapped_ingredients_index.csv')
    generate_csv_index(unmapped_records, output_dir / 'unmapped_ingredients_index.csv')
    generate_csv_index(all_records, output_dir / 'all_ingredients_index.csv')
    print()

    # Generate Markdown
    print("Generating Markdown indexes...")
    generate_markdown_index(mapped_records, output_dir / 'MAPPED_INGREDIENTS.md', 'Mapped Ingredients Index')
    generate_markdown_index(unmapped_records, output_dir / 'UNMAPPED_INGREDIENTS.md', 'Unmapped Ingredients Index')
    generate_markdown_index(all_records, output_dir / 'ALL_INGREDIENTS.md', 'Complete Ingredients Index')
    print()

    print("=" * 80)
    print("✓ ALL INDEX FILES GENERATED")
    print("=" * 80)
    print()
    print("Files created in data/curated/:")
    print("  JSON: *_index.json (machine-readable)")
    print("  CSV:  *_index.csv (spreadsheet-compatible)")
    print("  MD:   *.md (human-readable)")


if __name__ == '__main__':
    main()
