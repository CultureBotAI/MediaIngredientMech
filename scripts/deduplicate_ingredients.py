#!/usr/bin/env python3
"""Standalone script for automated ingredient deduplication.

This script implements a comprehensive deduplication workflow:
1. CHEBI ID deduplication (primary merge rule)
2. Name-based matching for solutions/buffers/stocks
3. KG-Microbe reconciliation (optional)

Usage:
    python scripts/deduplicate_ingredients.py --dry-run
    python scripts/deduplicate_ingredients.py --chebi-only
    python scripts/deduplicate_ingredients.py --auto-merge-threshold 0.9
    python scripts/deduplicate_ingredients.py --search-kg-microbe
"""

from __future__ import annotations

import argparse
import logging
import sys
from pathlib import Path
from typing import Any

from rich.console import Console
from rich.panel import Panel
from rich.table import Table

# Add src to path
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from mediaingredientmech.curation.chebi_deduplicator import CHEBIDeduplicator
from mediaingredientmech.curation.ingredient_curator import IngredientCurator
from mediaingredientmech.curation.solution_matcher import SolutionMatcher
from mediaingredientmech.utils.kg_microbe_searcher import KGMicrobeSearcher

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
logger = logging.getLogger(__name__)

console = Console()


def display_chebi_results(results: dict[str, Any], curator: IngredientCurator) -> None:
    """Display CHEBI deduplication results in a formatted table."""
    merged = results.get("merged", [])
    flagged = results.get("flagged", [])
    total_removed = results.get("total_removed", 0)
    dry_run = results.get("dry_run", True)

    # Summary panel
    mode_str = "DRY RUN" if dry_run else "EXECUTED"
    console.print(
        Panel(
            f"[bold]CHEBI Deduplication Results ({mode_str})[/bold]\n"
            f"Merged groups: {len(merged)}\n"
            f"Records removed: {total_removed}\n"
            f"Flagged for review: {len(flagged)}",
            title="Phase 1: CHEBI ID Deduplication",
            border_style="green" if len(merged) > 0 else "yellow",
        )
    )

    # Merged records table
    if merged:
        table = Table(title="Merged Records", show_header=True, header_style="bold cyan")
        table.add_column("CHEBI ID", style="cyan")
        table.add_column("Target", style="green")
        table.add_column("Merged From", style="yellow")
        table.add_column("Count", justify="right")

        for target_idx, source_indices, chebi_id in merged:
            target_name = curator.records[target_idx].get("preferred_term", "")
            source_names = [
                curator.records[i].get("preferred_term", "") for i in source_indices
            ]
            table.add_row(
                chebi_id, target_name, "\n".join(source_names), str(len(source_indices))
            )

        console.print(table)

    # Flagged records table
    if flagged:
        table = Table(
            title="Flagged for Manual Review", show_header=True, header_style="bold yellow"
        )
        table.add_column("CHEBI ID", style="cyan")
        table.add_column("Record Count", justify="right")
        table.add_column("Reason", style="yellow")

        for chebi_id, indices, reason in flagged:
            table.add_row(chebi_id, str(len(indices)), reason)

        console.print(table)


def display_solution_results(
    duplicates: list[tuple[int, int, float]], curator: IngredientCurator, threshold: float
) -> None:
    """Display solution/buffer/stock matching results."""
    console.print(
        Panel(
            f"[bold]Solution/Buffer/Stock Matching Results[/bold]\n"
            f"Potential duplicates found: {len(duplicates)}\n"
            f"Threshold: {threshold:.2f}",
            title="Phase 2: Name-Based Matching",
            border_style="blue",
        )
    )

    if duplicates:
        table = Table(
            title="Potential Name-Based Duplicates", show_header=True, header_style="bold blue"
        )
        table.add_column("Confidence", justify="right", style="cyan")
        table.add_column("Name 1", style="green")
        table.add_column("Name 2", style="yellow")
        table.add_column("Occurrences", justify="right")

        # Sort by confidence descending
        sorted_dups = sorted(duplicates, key=lambda x: x[2], reverse=True)

        for idx1, idx2, confidence in sorted_dups[:20]:  # Show top 20
            name1 = curator.records[idx1].get("preferred_term", "")
            name2 = curator.records[idx2].get("preferred_term", "")
            occ1 = (
                curator.records[idx1].get("occurrence_statistics", {}).get("total_occurrences", 0)
            )
            occ2 = (
                curator.records[idx2].get("occurrence_statistics", {}).get("total_occurrences", 0)
            )
            table.add_row(f"{confidence:.2f}", name1, name2, f"{occ1} + {occ2}")

        console.print(table)

        if len(sorted_dups) > 20:
            console.print(f"[dim]... and {len(sorted_dups) - 20} more[/dim]")


def display_kg_microbe_results(matches: dict[int, dict], curator: IngredientCurator) -> None:
    """Display KG-Microbe search results."""
    total_with_matches = sum(
        1
        for m in matches.values()
        if m.get("chebi_matches") or m.get("name_matches")
    )

    console.print(
        Panel(
            f"[bold]KG-Microbe Reconciliation Results[/bold]\n"
            f"Records with CultureMech matches: {total_with_matches}/{len(matches)}",
            title="Phase 3: KG-Microbe Search",
            border_style="magenta",
        )
    )

    # Show sample matches
    table = Table(
        title="Sample CultureMech Matches (Top 10)",
        show_header=True,
        header_style="bold magenta",
    )
    table.add_column("MediaIngredientMech", style="green")
    table.add_column("Match Type", style="cyan")
    table.add_column("CultureMech Records", justify="right")

    count = 0
    for idx, match_data in matches.items():
        if count >= 10:
            break

        chebi_matches = match_data.get("chebi_matches", [])
        name_matches = match_data.get("name_matches", [])

        if chebi_matches or name_matches:
            name = curator.records[idx].get("preferred_term", "")
            match_type = "CHEBI ID" if chebi_matches else "Name"
            match_count = len(chebi_matches) + len(name_matches)
            table.add_row(name, match_type, str(match_count))
            count += 1

    if count > 0:
        console.print(table)


def search_kg_microbe_matches(
    records: list[dict], kg_searcher: KGMicrobeSearcher
) -> dict[int, dict]:
    """Search KG-Microbe for matches to each ingredient record.

    Args:
        records: List of ingredient records.
        kg_searcher: KGMicrobeSearcher instance.

    Returns:
        Dict mapping record index to match results.
    """
    matches = {}

    for idx, record in enumerate(records):
        if record.get("mapping_status") == "REJECTED":
            continue

        match_data = kg_searcher.find_matches(record)
        matches[idx] = match_data

    return matches


def main():
    """Main deduplication workflow."""
    parser = argparse.ArgumentParser(
        description="Deduplicate MediaIngredientMech ingredients"
    )
    parser.add_argument(
        "--data-path",
        type=Path,
        default=Path("data/curated/unmapped_ingredients.yaml"),
        help="Path to ingredient data file",
    )
    parser.add_argument(
        "--culturemech-path",
        type=Path,
        default=Path("/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/CultureMech/output/mapped_ingredients.yaml"),
        help="Path to CultureMech mapped ingredients",
    )
    parser.add_argument(
        "--dry-run", action="store_true", help="Preview changes without saving"
    )
    parser.add_argument(
        "--chebi-only", action="store_true", help="Only perform CHEBI ID deduplication"
    )
    parser.add_argument(
        "--include-name-matches",
        action="store_true",
        help="Include solution/buffer/stock name matching",
    )
    parser.add_argument(
        "--search-kg-microbe",
        action="store_true",
        help="Search CultureMech for additional matches",
    )
    parser.add_argument(
        "--auto-merge-threshold",
        type=float,
        default=1.0,
        help="Auto-merge above this confidence (0.0-1.0)",
    )
    parser.add_argument(
        "--name-match-threshold",
        type=float,
        default=0.9,
        help="Minimum confidence for name-based matching (0.0-1.0)",
    )

    args = parser.parse_args()

    # Load ingredients
    console.print(f"[bold]Loading ingredients from {args.data_path}[/bold]")
    curator = IngredientCurator(data_path=args.data_path)
    curator.load()

    initial_count = len(curator.records)
    console.print(f"Loaded {initial_count} ingredient records")

    # Phase 1: CHEBI ID deduplication
    console.print("\n[bold cyan]Phase 1: CHEBI ID Deduplication[/bold cyan]")
    chebi_dedup = CHEBIDeduplicator(curator)
    auto_merge = not args.dry_run and args.auto_merge_threshold < 1.0
    chebi_results = chebi_dedup.merge_duplicates(dry_run=args.dry_run, auto_merge=auto_merge)
    display_chebi_results(chebi_results, curator)

    # Phase 2: Name-based matching (optional)
    if not args.chebi_only and args.include_name_matches:
        console.print("\n[bold blue]Phase 2: Solution/Buffer/Stock Matching[/bold blue]")
        solution_matcher = SolutionMatcher()
        solution_duplicates = solution_matcher.find_solution_duplicates(
            curator.records, threshold=args.name_match_threshold
        )
        display_solution_results(solution_duplicates, curator, args.name_match_threshold)

        # Note: Name-based merging not auto-executed, flagged for manual review
        if solution_duplicates:
            console.print(
                "[yellow]Note: Name-based matches require manual review before merging[/yellow]"
            )

    # Phase 3: KG-Microbe reconciliation (optional)
    if args.search_kg_microbe:
        console.print("\n[bold magenta]Phase 3: KG-Microbe Reconciliation[/bold magenta]")
        if args.culturemech_path.exists():
            kg_searcher = KGMicrobeSearcher(args.culturemech_path)
            kg_matches = search_kg_microbe_matches(curator.records, kg_searcher)
            display_kg_microbe_results(kg_matches, curator)

            # Display KG-Microbe statistics
            stats = kg_searcher.get_statistics()
            console.print(
                f"\n[dim]CultureMech: {stats['total_records']} total, "
                f"{stats['unique_chebi_ids']} unique CHEBI IDs[/dim]"
            )
        else:
            console.print(
                f"[yellow]CultureMech file not found: {args.culturemech_path}[/yellow]"
            )

    # Summary
    final_count = len([r for r in curator.records if r.get("mapping_status") != "REJECTED"])
    console.print(
        Panel(
            f"[bold]Deduplication Summary[/bold]\n"
            f"Initial records: {initial_count}\n"
            f"Final records: {final_count}\n"
            f"Reduction: {initial_count - final_count} ({(initial_count - final_count) / initial_count * 100:.1f}%)",
            title="Summary",
            border_style="green" if not args.dry_run else "yellow",
        )
    )

    # Save if not dry run
    if not args.dry_run:
        console.print(f"\n[bold green]Saving changes to {args.data_path}[/bold green]")
        curator.save()
        console.print("[green]✓ Saved successfully[/green]")

        # Validate
        is_valid, errors = chebi_dedup.validate_no_chebi_duplicates()
        if is_valid:
            console.print("[green]✓ Validation passed: No CHEBI duplicates remain[/green]")
        else:
            console.print("[red]✗ Validation failed:[/red]")
            for error in errors:
                console.print(f"  [red]- {error}[/red]")
    else:
        console.print("\n[yellow]DRY RUN: No changes saved[/yellow]")


if __name__ == "__main__":
    main()
