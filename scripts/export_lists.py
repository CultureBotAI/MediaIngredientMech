#!/usr/bin/env python3
"""Export lists of mapped and unmapped ingredients from curated YAML files.

Generates JSON, CSV, and Markdown lists for both mapped and unmapped ingredients.
Uses the curated collection files as source.
"""

from __future__ import annotations

import csv
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

import click
import yaml
from rich.console import Console
from rich.table import Table

console = Console()


def load_ingredients(yaml_path: Path) -> list[dict]:
    """Load ingredients from YAML file."""
    with open(yaml_path) as f:
        data = yaml.safe_load(f)

    # Handle collection format
    if isinstance(data, dict) and "ingredients" in data:
        return data["ingredients"]
    elif isinstance(data, list):
        return data
    return []


def _ontology_id(ing: dict) -> str:
    """ontology_id lives under ontology_mapping (not at the record top level)."""
    return (ing.get("ontology_mapping") or {}).get("ontology_id", "") or ""


# Separator for the CSV synonyms column. `|` is the multi-value separator this
# repo's SSSOM already uses (the `source`, `validation_method` and `other`
# columns), so consumers split on it today.
SYNONYM_SEP = "|"

# Curation strings that live in `synonyms` but are not names anything answers
# to: role/property annotations carried over from the CultureMech import, and
# bare parentheticals like `(sodium salt)` or `(for solid medium, alternative)`
# that are fragments of a name, not a name. 214 distinct strings. Publishing
# them as resolvable labels would make `Role: Carbon source; Properties: ...`
# "resolve" to 44 different CHEBI ids.
_NOT_A_LABEL = re.compile(r"^\s*Role:.*;\s*Properties:|^\s*\([^)]*\)\s*$", re.IGNORECASE)


def _synonyms(ing: dict) -> list[str]:
    """Every raw label this record answers to, minus the preferred_term itself.

    Merging a duplicate folds its raw label in here and deletes its record, and
    merges add no SSSOM row (SSSOM subjects are preferred_terms, never
    synonyms). `docs/data/ingredients.json` has always carried synonyms, but the
    backlog exports here did not -- so after a merge the label stopped resolving
    from the CSV/JSON that consumers join against. Issue #229.
    """
    preferred = ing.get("preferred_term", "")
    seen, out = {preferred}, []
    for s in ing.get("synonyms") or []:
        text = (s or {}).get("synonym_text")
        if not text or text in seen or _NOT_A_LABEL.match(text):
            continue
        seen.add(text)
        out.append(text)
    return out


def _join_synonyms(ing: dict) -> str:
    """Pack synonyms into the CSV cell, refusing rather than corrupting.

    Nothing in the schema forbids `|` in a synonym_text, and no synonym contains
    one today. If one ever does, joining silently would split it into two bogus
    labels on read, so fail here with the record named -- the coverage gate would
    otherwise report it as an unresolvable label and advise re-running the export,
    which loops forever.
    """
    syns = _synonyms(ing)
    bad = [s for s in syns if SYNONYM_SEP in s]
    if bad:
        raise ValueError(
            f"{ing.get('identifier', '?')}: synonym(s) contain the {SYNONYM_SEP!r} "
            f"separator and cannot be packed into the CSV column: {bad}. "
            "Change the separator or escape it before exporting.")
    return SYNONYM_SEP.join(syns)


def export_to_json(ingredients: list[dict], output_path: Path):
    """Export ingredients to JSON format."""
    records = []
    for ing in ingredients:
        record = {
            "identifier": ing.get("identifier", ""),
            "ontology_id": _ontology_id(ing),
            "preferred_term": ing.get("preferred_term", ""),
            "mapping_status": ing.get("mapping_status", ""),
            "synonyms": _synonyms(ing),
        }

        # Add ontology mapping details if mapped
        if ing.get("ontology_mapping"):
            om = ing["ontology_mapping"]
            record.update({
                "ontology_label": om.get("ontology_label", ""),
                "ontology_source": om.get("ontology_source", ""),
                "mapping_quality": om.get("mapping_quality", ""),
            })

        # Add statistics
        if ing.get("occurrence_statistics"):
            stats = ing["occurrence_statistics"]
            record.update({
                "total_occurrences": stats.get("total_occurrences", 0),
                "media_count": stats.get("media_count", 0),
            })

        records.append(record)

    with open(output_path, "w") as f:
        json.dump(records, f, indent=2)

    return len(records)


def export_to_csv(ingredients: list[dict], output_path: Path):
    """Export ingredients to CSV format."""
    fieldnames = [
        "identifier",
        "ontology_id",
        "preferred_term",
        "mapping_status",
        "ontology_label",
        "ontology_source",
        "mapping_quality",
        "total_occurrences",
        "media_count",
        # appended, not inserted: a consumer indexing columns positionally keeps
        # working, and one reading by header name picks it up. Issue #229.
        "synonyms",
    ]

    with open(output_path, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()

        for ing in ingredients:
            row = {
                "identifier": ing.get("identifier", ""),
                "ontology_id": _ontology_id(ing),
                "preferred_term": ing.get("preferred_term", ""),
                "mapping_status": ing.get("mapping_status", ""),
                "synonyms": _join_synonyms(ing),
            }

            # Add ontology mapping details
            if ing.get("ontology_mapping"):
                om = ing["ontology_mapping"]
                row.update({
                    "ontology_label": om.get("ontology_label", ""),
                    "ontology_source": om.get("ontology_source", ""),
                    "mapping_quality": om.get("mapping_quality", ""),
                })

            # Add statistics
            if ing.get("occurrence_statistics"):
                stats = ing["occurrence_statistics"]
                row.update({
                    "total_occurrences": stats.get("total_occurrences", 0),
                    "media_count": stats.get("media_count", 0),
                })

            writer.writerow(row)

    return len(ingredients)


def export_label_index(ingredients: list[dict], output_path: Path):
    """One row per (label, record) with how the label matched — #232.

    Publishing synonyms (#229) made 83 labels resolve to more than one
    identifier, and a consumer joining a raw ingredient string had no way to
    choose: `Vitamin B12` is the preferred_term of CHEBI:176843 and a synonym of
    two other records. The record-shaped exports cannot express this, because a
    row has one preferred_term and many synonyms — the ambiguity is per LABEL.

    So the precedence is made machine-readable instead of documented in prose:
    resolve to the row with match_type `preferred_term`; fall back to `synonym`
    only when no preferred_term matches. Rows are sorted so a label's
    preferred_term row sorts before its synonym rows.
    """
    rows = []
    for ing in ingredients:
        ident = ing.get("identifier", "")
        preferred = ing.get("preferred_term", "")
        status = ing.get("mapping_status", "")
        ont = _ontology_id(ing)
        if preferred:
            rows.append({"label": preferred, "match_type": "preferred_term",
                         "identifier": ident, "preferred_term": preferred,
                         "ontology_id": ont, "mapping_status": status})
        for syn in _synonyms(ing):
            rows.append({"label": syn, "match_type": "synonym",
                         "identifier": ident, "preferred_term": preferred,
                         "ontology_id": ont, "mapping_status": status})
    # preferred_term before synonym for the same label, then stable by identifier
    rows.sort(key=lambda r: (r["label"].lower(), r["match_type"] != "preferred_term",
                             r["identifier"]))
    fieldnames = ["label", "match_type", "identifier", "preferred_term",
                  "ontology_id", "mapping_status"]
    with open(output_path, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames)
        w.writeheader()
        w.writerows(rows)
    return len(rows)


def export_to_markdown(ingredients: list[dict], output_path: Path, title: str):
    """Export ingredients to Markdown table format.

    Deliberately carries NO synonyms column, unlike the CSV and JSON exports
    (#229): the pipe-joined list would collide with the table's own cell
    separator, and this artifact is for reading rather than for resolving raw
    strings. Consumers doing lookups should use the CSV or JSON.
    """
    lines = [
        f"# {title}",
        "",
        f"Generated: {datetime.now(timezone.utc).isoformat()}",
        f"Total: {len(ingredients)} ingredients",
        "",
        "| Identifier | Ontology ID | Preferred Term | Status | Source | Quality | Occurrences |",
        "|---|---|---|---|---|---|---|",
    ]

    for ing in ingredients:
        id_val = ing.get("identifier", "")
        ont_id = _ontology_id(ing)
        term = ing.get("preferred_term", "")
        status = ing.get("mapping_status", "")

        source = ""
        quality = ""
        if ing.get("ontology_mapping"):
            om = ing["ontology_mapping"]
            source = om.get("ontology_source", "")
            quality = om.get("mapping_quality", "")

        occurrences = ""
        if ing.get("occurrence_statistics"):
            occurrences = str(ing["occurrence_statistics"].get("total_occurrences", 0))

        lines.append(f"| {id_val} | {ont_id} | {term} | {status} | {source} | {quality} | {occurrences} |")

    with open(output_path, "w") as f:
        f.write("\n".join(lines))

    return len(ingredients)


@click.command()
@click.option(
    "--mapped-input",
    type=click.Path(exists=True, path_type=Path),
    default=Path("data/curated/mapped_ingredients.yaml"),
    help="Input YAML file with mapped ingredients",
)
@click.option(
    "--unmapped-input",
    type=click.Path(exists=True, path_type=Path),
    default=Path("data/curated/unmapped_ingredients.yaml"),
    help="Input YAML file with unmapped ingredients",
)
@click.option(
    "--output-dir",
    type=click.Path(path_type=Path),
    default=Path("docs/data"),
    help="Output directory for exported files",
)
@click.option(
    "--format",
    type=click.Choice(["json", "csv", "markdown", "all"]),
    default="all",
    help="Output format",
)
def main(
    mapped_input: Path,
    unmapped_input: Path,
    output_dir: Path,
    format: str,
):
    """Export lists of mapped and unmapped ingredients."""
    console.print("\n[bold]Ingredient List Exporter[/bold]")

    # Create output directory
    output_dir.mkdir(parents=True, exist_ok=True)

    # Load ingredients
    console.print(f"\nLoading mapped ingredients from {mapped_input}...")
    mapped = load_ingredients(mapped_input)
    console.print(f"  Found {len(mapped)} mapped ingredients")

    console.print(f"\nLoading unmapped ingredients from {unmapped_input}...")
    unmapped = load_ingredients(unmapped_input)
    console.print(f"  Found {len(unmapped)} unmapped ingredients")

    all_ingredients = mapped + unmapped
    console.print(f"\n[bold]Total: {len(all_ingredients)} ingredients[/bold]")

    # Export in requested formats
    formats_to_export = ["json", "csv", "markdown"] if format == "all" else [format]

    for fmt in formats_to_export:
        console.print(f"\n[cyan]Exporting {fmt.upper()} files...[/cyan]")

        if fmt == "json":
            # Mapped JSON
            mapped_json = output_dir / "mapped_ingredients.json"
            count = export_to_json(mapped, mapped_json)
            console.print(f"  ✓ {mapped_json} ({count} records)")

            # Unmapped JSON
            unmapped_json = output_dir / "unmapped_ingredients.json"
            count = export_to_json(unmapped, unmapped_json)
            console.print(f"  ✓ {unmapped_json} ({count} records)")

            # All JSON
            all_json = output_dir / "all_ingredients.json"
            count = export_to_json(all_ingredients, all_json)
            console.print(f"  ✓ {all_json} ({count} records)")

        elif fmt == "csv":
            # Mapped CSV
            mapped_csv = output_dir / "mapped_ingredients.csv"
            count = export_to_csv(mapped, mapped_csv)
            console.print(f"  ✓ {mapped_csv} ({count} records)")

            # Unmapped CSV
            unmapped_csv = output_dir / "unmapped_ingredients.csv"
            count = export_to_csv(unmapped, unmapped_csv)
            console.print(f"  ✓ {unmapped_csv} ({count} records)")

            # All CSV
            all_csv = output_dir / "all_ingredients.csv"
            count = export_to_csv(all_ingredients, all_csv)
            console.print(f"  ✓ {all_csv} ({count} records)")

            # per-LABEL resolution with explicit precedence (#232)
            label_csv = output_dir / "label_index.csv"
            count = export_label_index(all_ingredients, label_csv)
            console.print(f"  ✓ {label_csv} ({count} labels)")

        elif fmt == "markdown":
            # Mapped MD
            mapped_md = output_dir / "mapped_ingredients.md"
            count = export_to_markdown(mapped, mapped_md, "Mapped Ingredients")
            console.print(f"  ✓ {mapped_md} ({count} records)")

            # Unmapped MD
            unmapped_md = output_dir / "unmapped_ingredients.md"
            count = export_to_markdown(unmapped, unmapped_md, "Unmapped Ingredients")
            console.print(f"  ✓ {unmapped_md} ({count} records)")

            # All MD
            all_md = output_dir / "all_ingredients.md"
            count = export_to_markdown(all_ingredients, all_md, "All Ingredients")
            console.print(f"  ✓ {all_md} ({count} records)")

    # Summary
    console.print("\n[bold green]✅ Export complete![/bold green]")
    console.print(f"\nFiles saved to: {output_dir}")

    # Show sample
    console.print("\n[bold]Sample Records:[/bold]")
    table = Table(show_header=True, header_style="bold cyan")
    table.add_column("Identifier", style="yellow")
    table.add_column("Ontology ID", style="green")
    table.add_column("Preferred Term", style="white")
    table.add_column("Status", style="magenta")

    for ing in all_ingredients[:5]:
        table.add_row(
            ing.get("identifier", "")[:25],
            _ontology_id(ing)[:25],
            ing.get("preferred_term", "")[:40],
            ing.get("mapping_status", ""),
        )

    console.print(table)
    console.print(f"\n... and {len(all_ingredients) - 5} more")


if __name__ == "__main__":
    main()
