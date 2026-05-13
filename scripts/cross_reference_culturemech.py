#!/usr/bin/env python3
"""Cross-reference MediaIngredientMech entries with CultureMech media recipes.

This script searches CultureMech for media recipes that match ingredient names,
particularly useful for identifying defined media entries that should link to
their full recipe formulations.

Usage:
    python scripts/cross_reference_culturemech.py --complex-media-only
    python scripts/cross_reference_culturemech.py --ingredient "R2A agar"
    python scripts/cross_reference_culturemech.py --update-links
"""

import argparse
import sys
from pathlib import Path
from typing import Any, Optional

import yaml
from rich.console import Console
from rich.table import Table
from rich.panel import Panel

# Add src to path
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from mediaingredientmech.curation.ingredient_curator import IngredientCurator

console = Console()


class CultureMechMatcher:
    """Match MediaIngredientMech entries to CultureMech media."""

    def __init__(self, culturemech_path: Path):
        """Initialize with path to CultureMech data.

        Args:
            culturemech_path: Path to CultureMech media YAML file.
        """
        self.culturemech_path = culturemech_path
        self.media_data = None
        self.media_by_name = {}
        self._load_culturemech()

    def _load_culturemech(self) -> None:
        """Load CultureMech media data."""
        if not self.culturemech_path.exists():
            console.print(f"[yellow]Warning: CultureMech file not found at {self.culturemech_path}[/yellow]")
            return

        try:
            with open(self.culturemech_path) as f:
                self.media_data = yaml.safe_load(f)

            # Index by medium name
            media_list = self.media_data.get("media", [])
            for medium in media_list:
                name = medium.get("medium_name", "").lower().strip()
                if name:
                    self.media_by_name[name] = medium

            console.print(f"[green]Loaded {len(self.media_by_name)} media from CultureMech[/green]")

        except Exception as e:
            console.print(f"[red]Error loading CultureMech data: {e}[/red]")

    def find_medium_matches(self, ingredient_name: str) -> list[dict[str, Any]]:
        """Find CultureMech media that match an ingredient name.

        Args:
            ingredient_name: Ingredient name to search for.

        Returns:
            List of matching media records with match scores.
        """
        if not self.media_by_name:
            return []

        matches = []
        search_name = ingredient_name.lower().strip()

        # Exact match
        if search_name in self.media_by_name:
            matches.append({
                "medium": self.media_by_name[search_name],
                "match_type": "exact",
                "confidence": 1.0,
            })
            return matches

        # Partial matches
        for name, medium in self.media_by_name.items():
            # Check if search term is in medium name
            if search_name in name:
                matches.append({
                    "medium": medium,
                    "match_type": "contains",
                    "confidence": 0.8,
                })
            # Check if medium name is in search term
            elif name in search_name:
                matches.append({
                    "medium": medium,
                    "match_type": "contained_by",
                    "confidence": 0.7,
                })

        # Fuzzy matching (token overlap)
        if not matches:
            search_tokens = set(search_name.split())
            for name, medium in self.media_by_name.items():
                name_tokens = set(name.split())
                overlap = search_tokens & name_tokens
                if overlap and len(overlap) >= 2:  # At least 2 words match
                    confidence = len(overlap) / max(len(search_tokens), len(name_tokens))
                    matches.append({
                        "medium": medium,
                        "match_type": "fuzzy",
                        "confidence": confidence,
                    })

        # Sort by confidence descending
        matches.sort(key=lambda x: x["confidence"], reverse=True)
        return matches

    def get_medium_ingredients(self, medium: dict) -> list[str]:
        """Extract ingredient list from a CultureMech medium record.

        Args:
            medium: CultureMech medium record.

        Returns:
            List of ingredient names.
        """
        ingredients = []

        # Get ingredients from components
        for component in medium.get("components", []):
            ing_name = component.get("ingredient_name", "")
            if ing_name:
                ingredients.append(ing_name)

        return ingredients


def cross_reference_all(
    curator: IngredientCurator,
    matcher: CultureMechMatcher,
    complex_media_only: bool = True
) -> dict[int, list[dict]]:
    """Cross-reference all ingredients with CultureMech.

    Args:
        curator: IngredientCurator instance.
        matcher: CultureMechMatcher instance.
        complex_media_only: If True, only check DEFINED_MEDIUM entries.

    Returns:
        Dict mapping ingredient index to list of CultureMech matches.
    """
    results = {}

    for idx, record in enumerate(curator.records):
        # Skip rejected
        if record.get("mapping_status") == "REJECTED":
            continue

        # Filter by type if requested
        if complex_media_only and record.get("ingredient_type") != "DEFINED_MEDIUM":
            continue

        ingredient_name = record.get("preferred_term", "")
        matches = matcher.find_medium_matches(ingredient_name)

        if matches:
            results[idx] = matches

    return results


def display_cross_reference_results(
    curator: IngredientCurator,
    results: dict[int, list[dict]],
    matcher: CultureMechMatcher,
    max_display: int = 50
) -> None:
    """Display cross-reference results.

    Args:
        curator: IngredientCurator instance.
        results: Cross-reference results.
        matcher: CultureMechMatcher instance.
        max_display: Maximum number of results to display.
    """
    console.print(f"\n[bold]Cross-Reference Results[/bold]")
    console.print(f"Found CultureMech matches for {len(results)} ingredients\n")

    table = Table(show_header=True, header_style="bold cyan")
    table.add_column("MediaIngredientMech", style="green", width=40)
    table.add_column("CultureMech Medium", style="cyan", width=40)
    table.add_column("Match", style="yellow")
    table.add_column("Ingredients", justify="right")

    count = 0
    for idx in sorted(results.keys()):
        if count >= max_display:
            break

        record = curator.records[idx]
        ingredient_name = record.get("preferred_term", "")

        # Show best match
        best_match = results[idx][0]
        medium = best_match["medium"]
        medium_name = medium.get("medium_name", "N/A")
        match_type = best_match["match_type"]
        confidence = best_match["confidence"]

        # Get ingredient count
        ingredients = matcher.get_medium_ingredients(medium)
        ing_count = len(ingredients)

        table.add_row(
            ingredient_name,
            medium_name,
            f"{match_type} ({confidence:.2f})",
            str(ing_count) if ing_count > 0 else "N/A"
        )

        count += 1

    console.print(table)

    if len(results) > max_display:
        console.print(f"\n[dim]... and {len(results) - max_display} more matches[/dim]")


def display_medium_details(medium: dict, matcher: CultureMechMatcher) -> None:
    """Display detailed information about a CultureMech medium.

    Args:
        medium: CultureMech medium record.
        matcher: CultureMechMatcher instance.
    """
    medium_name = medium.get("medium_name", "Unknown")
    medium_id = medium.get("medium_id", "N/A")

    ingredients = matcher.get_medium_ingredients(medium)

    panel_content = f"[bold]Medium ID:[/bold] {medium_id}\n\n"
    panel_content += f"[bold]Ingredients ({len(ingredients)}):[/bold]\n"

    if ingredients:
        for ing in ingredients[:20]:  # Show first 20
            panel_content += f"  • {ing}\n"
        if len(ingredients) > 20:
            panel_content += f"  ... and {len(ingredients) - 20} more\n"
    else:
        panel_content += "  [dim]No ingredients listed[/dim]\n"

    console.print(Panel(panel_content, title=medium_name, border_style="cyan"))


def update_culturemech_links(
    curator: IngredientCurator,
    results: dict[int, list[dict]],
    confidence_threshold: float = 0.8,
    dry_run: bool = True
) -> int:
    """Update records with CultureMech cross-references.

    Args:
        curator: IngredientCurator instance.
        results: Cross-reference results.
        confidence_threshold: Minimum confidence for auto-linking.
        dry_run: If True, don't actually update records.

    Returns:
        Number of records updated.
    """
    updated = 0

    for idx, matches in results.items():
        best_match = matches[0]
        if best_match["confidence"] < confidence_threshold:
            continue

        record = curator.records[idx]
        medium = best_match["medium"]
        medium_name = medium.get("medium_name", "")

        if dry_run:
            console.print(f"[DRY RUN] Would link: {record.get('preferred_term')} → {medium_name}")
        else:
            record["culturemech_medium_name"] = medium_name
            curator.add_note(
                record,
                f"Cross-referenced to CultureMech medium: {medium_name} "
                f"(confidence: {best_match['confidence']:.2f})"
            )
            console.print(f"Linked: {record.get('preferred_term')} → {medium_name}")

        updated += 1

    return updated


def main():
    """Main workflow."""
    parser = argparse.ArgumentParser(
        description="Cross-reference MediaIngredientMech with CultureMech"
    )
    parser.add_argument(
        "--data-path",
        type=Path,
        default=Path("data/curated/mapped_ingredients.yaml"),
        help="Path to MediaIngredientMech data file",
    )
    parser.add_argument(
        "--culturemech-path",
        type=Path,
        default=Path("../CultureMech/output/media.yaml"),
        help="Path to CultureMech media file",
    )
    parser.add_argument(
        "--complex-media-only",
        action="store_true",
        help="Only search for DEFINED_MEDIUM entries",
    )
    parser.add_argument(
        "--ingredient",
        type=str,
        help="Search for specific ingredient name",
    )
    parser.add_argument(
        "--update-links",
        action="store_true",
        help="Update records with CultureMech links",
    )
    parser.add_argument(
        "--confidence-threshold",
        type=float,
        default=0.8,
        help="Minimum confidence for auto-linking (default: 0.8)",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Preview changes without saving",
    )
    parser.add_argument(
        "--show-details",
        action="store_true",
        help="Show detailed medium information",
    )

    args = parser.parse_args()

    # Load MediaIngredientMech
    console.print(f"\n[bold]Loading MediaIngredientMech from {args.data_path}[/bold]")
    curator = IngredientCurator(data_path=args.data_path)
    curator.load()
    console.print(f"Loaded {len(curator.records)} ingredient records\n")

    # Load CultureMech
    console.print(f"[bold]Loading CultureMech from {args.culturemech_path}[/bold]")
    matcher = CultureMechMatcher(args.culturemech_path)

    if not matcher.media_by_name:
        console.print("[red]No CultureMech data loaded. Exiting.[/red]")
        return 1

    # Single ingredient search
    if args.ingredient:
        console.print(f"\n[bold]Searching for: {args.ingredient}[/bold]\n")
        matches = matcher.find_medium_matches(args.ingredient)

        if matches:
            console.print(f"Found {len(matches)} matches:\n")
            for match in matches:
                medium = match["medium"]
                medium_name = medium.get("medium_name", "N/A")
                console.print(
                    f"  • {medium_name} ({match['match_type']}, "
                    f"confidence: {match['confidence']:.2f})"
                )

                if args.show_details:
                    console.print()
                    display_medium_details(medium, matcher)
                    console.print()
        else:
            console.print("[yellow]No matches found[/yellow]")

        return 0

    # Cross-reference all
    console.print("\n[bold cyan]Cross-referencing all ingredients...[/bold cyan]")
    results = cross_reference_all(curator, matcher, args.complex_media_only)

    # Display results
    display_cross_reference_results(curator, results, matcher)

    # Update links
    if args.update_links:
        console.print(f"\n[bold]Updating CultureMech links (threshold: {args.confidence_threshold})[/bold]")
        updated = update_culturemech_links(curator, results, args.confidence_threshold, args.dry_run)

        console.print(f"\n{'[DRY RUN] Would update' if args.dry_run else 'Updated'}: {updated} records")

        if not args.dry_run and updated > 0:
            console.print(f"\n[bold green]Saving changes to {args.data_path}[/bold green]")
            curator.save()
            console.print("[green]✓ Saved successfully[/green]")

    return 0


if __name__ == "__main__":
    sys.exit(main())
