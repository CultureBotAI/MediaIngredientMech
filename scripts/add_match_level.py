#!/usr/bin/env python3
"""Infer and add match_level field to batch suggestion YAML files.

Analyzes the reasoning text in suggestion records to automatically determine
the match_level (EXACT, NORMALIZED, FUZZY, MANUAL, UNMAPPABLE) based on
pattern matching.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path
from typing import Any

import click
import yaml
from rich.console import Console
from rich.table import Table

console = Console()

# Pattern matching rules for inferring match_level
MATCH_LEVEL_PATTERNS = {
    "NORMALIZED": [
        r"[Hh]ydrate notation stripped",
        r"[Ii]ncomplete formula (fixed|inferred)",
        r"[Cc]atalog stripped",
        r"[Pp]refix removed",
        r"\"Original amount:\"",
    ],
    "EXACT": [
        r"[Dd]irect exact match",
        r"[Nn]o normalization needed",
        r"[Ss]imple chemical formula",
    ],
    "FUZZY": [
        r"[Ss]ynonym confirms",
        r"[Ss]emantically close",
        r"[Bb]ritish spelling",
        r"[Aa]bbreviation expanded",
    ],
}


def infer_match_level(suggestion: dict[str, Any]) -> str:
    """Infer match_level from suggestion record.

    Args:
        suggestion: Suggestion dict with quality and reasoning fields.

    Returns:
        Inferred match_level value.
    """
    quality = suggestion.get("quality", "")
    reasoning = suggestion.get("reasoning", "")

    # UNMAPPABLE quality always maps to UNMAPPABLE level
    if quality == "UNMAPPABLE":
        return "UNMAPPABLE"

    # Check patterns in order of specificity
    for level, patterns in MATCH_LEVEL_PATTERNS.items():
        for pattern in patterns:
            if re.search(pattern, reasoning):
                return level

    # Default to MANUAL if no patterns match
    return "MANUAL"


def process_batch_file(
    file_path: Path, dry_run: bool = True
) -> tuple[int, dict[str, int]]:
    """Process a single batch suggestion file.

    Args:
        file_path: Path to batch YAML file.
        dry_run: If True, don't save changes.

    Returns:
        Tuple of (total_count, level_distribution)
    """
    with open(file_path) as f:
        data = yaml.safe_load(f)

    suggestions = data.get("suggestions", [])
    level_counts: dict[str, int] = {}

    for suggestion in suggestions:
        # Skip if already has match_level
        if "match_level" in suggestion:
            existing_level = suggestion["match_level"]
            level_counts[existing_level] = level_counts.get(existing_level, 0) + 1
            console.print(
                f"  [dim]Skipping {suggestion.get('identifier', '?')} "
                f"(already has match_level: {existing_level})[/dim]"
            )
            continue

        # Infer match_level
        match_level = infer_match_level(suggestion)
        suggestion["match_level"] = match_level
        level_counts[match_level] = level_counts.get(match_level, 0) + 1

        identifier = suggestion.get("identifier", "?")
        name = suggestion.get("name", "?")[:30]
        console.print(f"  {identifier:15s} {name:32s} → [bold]{match_level}[/bold]")

    # Save if not dry run
    if not dry_run and suggestions:
        with open(file_path, "w") as f:
            yaml.dump(data, f, default_flow_style=False, sort_keys=False, allow_unicode=True)
        console.print(f"  [green]✓ Saved {len(suggestions)} suggestions[/green]")
    elif dry_run:
        console.print(f"  [dim](Dry run - not saved)[/dim]")

    return len(suggestions), level_counts


@click.command()
@click.option(
    "--batch-files",
    "-b",
    multiple=True,
    type=click.Path(exists=True, path_type=Path),
    help="Specific batch files to process (can be repeated)",
)
@click.option(
    "--all-batches",
    "-a",
    is_flag=True,
    help="Process all batch*.yaml files in notes/ directory",
)
@click.option(
    "--dry-run",
    "-d",
    is_flag=True,
    help="Show what would be done without saving",
)
@click.option(
    "--notes-dir",
    type=click.Path(path_type=Path),
    default=Path("notes"),
    help="Directory containing batch files (default: notes/)",
)
def main(
    batch_files: tuple[Path, ...],
    all_batches: bool,
    dry_run: bool,
    notes_dir: Path,
) -> None:
    """Infer and add match_level to batch suggestion files."""
    console.print("[bold]Match Level Inference Tool[/bold]\n")

    if dry_run:
        console.print("[yellow]DRY RUN MODE - No changes will be saved[/yellow]\n")

    # Determine files to process
    files_to_process: list[Path] = []

    if all_batches:
        # Find all batch files in notes directory
        files_to_process = sorted(notes_dir.glob("batch*.yaml"))
        if not files_to_process:
            console.print(f"[red]No batch*.yaml files found in {notes_dir}[/red]")
            sys.exit(1)
        console.print(f"Found {len(files_to_process)} batch files in {notes_dir}\n")

    elif batch_files:
        files_to_process = list(batch_files)

    else:
        console.print("[red]Error: Must specify --batch-files or --all-batches[/red]")
        sys.exit(1)

    # Process each file
    total_suggestions = 0
    overall_distribution: dict[str, int] = {}

    for file_path in files_to_process:
        console.print(f"\n[bold cyan]Processing {file_path.name}[/bold cyan]")

        try:
            count, distribution = process_batch_file(file_path, dry_run=dry_run)
            total_suggestions += count

            # Aggregate distributions
            for level, cnt in distribution.items():
                overall_distribution[level] = overall_distribution.get(level, 0) + cnt

        except Exception as e:
            console.print(f"[red]Error processing {file_path}: {e}[/red]")
            continue

    # Summary table
    console.print("\n[bold]Overall Distribution:[/bold]")
    summary_table = Table()
    summary_table.add_column("Match Level", style="bold")
    summary_table.add_column("Count", justify="right")
    summary_table.add_column("Percentage", justify="right")

    for level in ["NORMALIZED", "EXACT", "FUZZY", "MANUAL", "UNMAPPABLE", "UNKNOWN"]:
        count = overall_distribution.get(level, 0)
        percentage = (count / total_suggestions * 100) if total_suggestions > 0 else 0.0
        summary_table.add_row(level, str(count), f"{percentage:.1f}%")

    console.print(summary_table)

    console.print(f"\n[bold]Total suggestions processed: {total_suggestions}[/bold]")

    if dry_run:
        console.print(
            "\n[yellow]This was a dry run. Run without --dry-run to save changes.[/yellow]"
        )


if __name__ == "__main__":
    main()
