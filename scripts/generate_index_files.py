#!/usr/bin/env python3
"""
Generate index files for all MediaIngredientMech records.

Creates JSON, CSV, and Markdown exports for easy reference.
"""

import sys
import json
import csv
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from mediaingredientmech.curation.ingredient_curator import IngredientCurator


def generate_json_index(records: list[dict], output_path: Path) -> None:
    """Generate JSON index with key fields."""
    index = []

    for record in records:
        entry = {
            'id': record.get('id'),
            'preferred_term': record.get('preferred_term'),
            'identifier': record.get('identifier'),
            'mapping_status': record.get('mapping_status'),
            'occurrences': record.get('occurrence_statistics', {}).get('total_occurrences', 0),
        }

        # Add ontology mapping if exists
        if 'ontology_mapping' in record:
            om = record['ontology_mapping']
            entry['ontology_id'] = om.get('ontology_id')
            entry['ontology_source'] = om.get('ontology_source')
            entry['mapping_quality'] = om.get('mapping_quality')

        # Add hierarchy info if exists
        if 'parent_ingredient' in record:
            entry['parent_ingredient'] = record['parent_ingredient']
        if 'variant_type' in record:
            entry['variant_type'] = record['variant_type']

        index.append(entry)

    with open(output_path, 'w') as f:
        json.dump(index, f, indent=2)

    print(f"✓ Created {output_path} ({len(index)} records)")


def generate_csv_index(records: list[dict], output_path: Path) -> None:
    """Generate CSV index with key fields."""
    with open(output_path, 'w', newline='') as f:
        writer = csv.writer(f)

        # Header
        writer.writerow([
            'id',
            'preferred_term',
            'identifier',
            'mapping_status',
            'ontology_id',
            'ontology_source',
            'mapping_quality',
            'occurrences',
            'parent_ingredient',
            'variant_type',
        ])

        # Rows
        for record in records:
            om = record.get('ontology_mapping', {})
            writer.writerow([
                record.get('id', ''),
                record.get('preferred_term', ''),
                record.get('identifier', ''),
                record.get('mapping_status', ''),
                om.get('ontology_id', ''),
                om.get('ontology_source', ''),
                om.get('mapping_quality', ''),
                record.get('occurrence_statistics', {}).get('total_occurrences', 0),
                record.get('parent_ingredient', ''),
                record.get('variant_type', ''),
            ])

    print(f"✓ Created {output_path} ({len(records)} records)")


def generate_markdown_index(records: list[dict], output_path: Path, title: str) -> None:
    """Generate Markdown index with formatted tables."""
    lines = [f"# {title}\n"]

    # Summary stats
    total = len(records)
    mapped = sum(1 for r in records if r.get('mapping_status') == 'MAPPED')
    unmapped = sum(1 for r in records if r.get('mapping_status') == 'UNMAPPED')
    total_occurrences = sum(r.get('occurrence_statistics', {}).get('total_occurrences', 0) for r in records)

    lines.append(f"**Total Records**: {total}\n")
    lines.append(f"**Mapped**: {mapped} ({mapped/total*100:.1f}%)\n")
    lines.append(f"**Unmapped**: {unmapped} ({unmapped/total*100:.1f}%)\n")
    lines.append(f"**Total Occurrences**: {total_occurrences:,}\n")
    lines.append("\n---\n\n")

    # Mapped ingredients table
    if mapped > 0:
        lines.append("## Mapped Ingredients\n\n")
        lines.append("| ID | Preferred Term | Ontology ID | Source | Quality | Occurrences |\n")
        lines.append("|---|---|---|---|---|---|\n")

        for record in records:
            if record.get('mapping_status') != 'MAPPED':
                continue

            om = record.get('ontology_mapping', {})
            lines.append(
                f"| {record.get('id', '')} "
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
        lines.append("| ID | Preferred Term | Identifier | Status | Occurrences |\n")
        lines.append("|---|---|---|---|---|\n")

        for record in records:
            if record.get('mapping_status') != 'UNMAPPED':
                continue

            lines.append(
                f"| {record.get('id', '')} "
                f"| {record.get('preferred_term', '')} "
                f"| {record.get('identifier', '')} "
                f"| {record.get('mapping_status', '')} "
                f"| {record.get('occurrence_statistics', {}).get('total_occurrences', 0)} |\n"
            )

        lines.append("\n")

    # Hierarchy parents
    hierarchy_parents = [r for r in records if r.get('child_ingredients')]
    if hierarchy_parents:
        lines.append("## Hierarchy Parents\n\n")
        for parent in hierarchy_parents:
            lines.append(f"### {parent.get('preferred_term')} ({parent.get('id')})\n\n")
            lines.append(f"**Variant Type**: {parent.get('variant_type', 'N/A')}\n\n")
            lines.append(f"**Children**: {len(parent.get('child_ingredients', []))}\n\n")

            children_ids = parent.get('child_ingredients', [])
            for child_id in children_ids:
                child = next((r for r in records if r.get('id') == child_id), None)
                if child:
                    lines.append(f"- {child.get('preferred_term')} ({child_id}) - {child.get('variant_type', 'N/A')}\n")
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

    # Load mapped ingredients
    mapped_curator = IngredientCurator(data_path='data/curated/mapped_ingredients.yaml')
    mapped_curator.load()
    print(f"Loaded {len(mapped_curator.records)} mapped ingredients")

    # Load unmapped ingredients
    unmapped_curator = IngredientCurator(data_path='data/curated/unmapped_ingredients.yaml')
    unmapped_curator.load()
    print(f"Loaded {len(unmapped_curator.records)} unmapped ingredients")
    print()

    # Combine all records
    all_records = mapped_curator.records + unmapped_curator.records
    print(f"Total: {len(all_records)} ingredients")
    print()

    output_dir = Path('data/curated')

    # Generate JSON
    print("Generating JSON indexes...")
    generate_json_index(mapped_curator.records, output_dir / 'mapped_ingredients_index.json')
    generate_json_index(unmapped_curator.records, output_dir / 'unmapped_ingredients_index.json')
    generate_json_index(all_records, output_dir / 'all_ingredients_index.json')
    print()

    # Generate CSV
    print("Generating CSV indexes...")
    generate_csv_index(mapped_curator.records, output_dir / 'mapped_ingredients_index.csv')
    generate_csv_index(unmapped_curator.records, output_dir / 'unmapped_ingredients_index.csv')
    generate_csv_index(all_records, output_dir / 'all_ingredients_index.csv')
    print()

    # Generate Markdown
    print("Generating Markdown indexes...")
    generate_markdown_index(mapped_curator.records, output_dir / 'MAPPED_INGREDIENTS.md', 'Mapped Ingredients Index')
    generate_markdown_index(unmapped_curator.records, output_dir / 'UNMAPPED_INGREDIENTS.md', 'Unmapped Ingredients Index')
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
