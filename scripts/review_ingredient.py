#!/usr/bin/env python3
"""
Interactive single-ingredient review with Rich UI.

Usage:
    python scripts/review_ingredient.py "sodium chloride"
    python scripts/review_ingredient.py --id CHEBI:26710
    python scripts/review_ingredient.py "glucose" --suggest-fixes
"""

import argparse
import sys
from pathlib import Path

from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich import box
from rich.text import Text

# Add src to path
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from mediaingredientmech.curation.ingredient_curator import IngredientCurator
from mediaingredientmech.validation.ingredient_reviewer import IngredientReviewer

console = Console()


def display_ingredient_info(ingredient: dict):
    """Display ingredient information in a panel."""
    info_text = Text()
    info_text.append(f"Status: {ingredient.get('mapping_status', 'N/A')}\n")

    ontology_mapping = ingredient.get("ontology_mapping") or {}
    if ontology_mapping:
        info_text.append(f"Ontology ID: {ontology_mapping.get('ontology_id', 'N/A')}\n")
        # Schema names: `mapping_quality`. Confidence lives per-evidence-row,
        # so we surface the best confidence_score across evidence entries.
        quality = ontology_mapping.get("mapping_quality", "N/A")
        evidence = ontology_mapping.get("evidence") or []
        confidence_scores = [
            ev.get("confidence_score")
            for ev in evidence
            if isinstance(ev, dict) and ev.get("confidence_score") is not None
        ]
        confidence = max(confidence_scores) if confidence_scores else "N/A"
        info_text.append(f"Quality: {quality} (confidence: {confidence})\n")
        info_text.append(f"Match Level: {ontology_mapping.get('match_level', 'N/A')}\n")

    panel = Panel(
        info_text,
        title=f"[bold]Ingredient: {ingredient.get('preferred_term', 'N/A')}[/bold]",
        border_style="blue",
    )
    console.print(panel)


def display_validation_results(result):
    """Display validation results in a table."""
    if result.status == "PASS" and not result.issues:
        console.print("[green]✓ PASS - No issues found[/green]\n")
        return

    status_color = {
        "PASS": "green",
        "WARNING": "yellow",
        "ERROR": "red",
    }

    console.print(
        f"\nValidation Results: [{status_color[result.status]}]{result.status}[/{status_color[result.status]}] "
        f"({len(result.issues)} {'issue' if len(result.issues) == 1 else 'issues'})\n"
    )

    # Group issues by priority
    priority_groups = {}
    for issue in result.issues:
        if issue.priority not in priority_groups:
            priority_groups[issue.priority] = []
        priority_groups[issue.priority].append(issue)

    # Display each priority group
    for priority in ["P1", "P2", "P3", "P4"]:
        if priority not in priority_groups:
            continue

        issues = priority_groups[priority]
        priority_colors = {
            "P1": "red",
            "P2": "yellow",
            "P3": "blue",
            "P4": "green",
        }

        table = Table(
            title=f"[{priority_colors[priority]}]{priority} {len(issues)} issue(s)[/{priority_colors[priority]}]",
            box=box.ROUNDED,
            show_header=True,
        )
        table.add_column("Rule", style="cyan")
        table.add_column("Category", style="magenta")
        table.add_column("Message", style="white")

        for issue in issues:
            table.add_row(issue.rule_id, issue.category, issue.message)

        console.print(table)
        console.print()


def display_suggestions(suggestions):
    """Display correction suggestions."""
    if not suggestions:
        return

    console.print(f"\n[bold]Correction Suggestions ({len(suggestions)}):[/bold]\n")

    for i, suggestion in enumerate(suggestions, 1):
        auto_label = "[green]✓ Auto-correctable[/green]" if suggestion.auto_correctable else "[yellow]⚠ Manual review[/yellow]"

        console.print(f"{i}. {suggestion.action} - {auto_label}")
        console.print(f"   Field: {suggestion.field_path}")
        console.print(f"   Current: {suggestion.current_value}")
        console.print(f"   Suggested: {suggestion.suggested_value}")
        console.print(f"   Confidence: {suggestion.confidence:.2f}")
        console.print(f"   Rationale: {suggestion.rationale}\n")


def apply_corrections_interactive(
    curator: IngredientCurator, ingredient: dict, suggestions: list
):
    """Interactively apply corrections."""
    console.print("\n[bold]Apply Corrections:[/bold]\n")

    auto_suggestions = [s for s in suggestions if s.auto_correctable]
    if not auto_suggestions:
        console.print("[yellow]No auto-correctable suggestions available[/yellow]")
        return

    console.print(f"Found {len(auto_suggestions)} auto-correctable suggestions:\n")
    for i, suggestion in enumerate(auto_suggestions, 1):
        console.print(f"{i}. {suggestion.action}: {suggestion.rationale}")

    response = console.input("\nApply all auto-corrections? [y/N]: ")
    if response.lower() != "y":
        console.print("Skipped corrections")
        return

    # Apply corrections
    reviewer = IngredientReviewer()
    corrected = reviewer.auto_correct(ingredient)

    # IngredientCurator has no `update_ingredient`. Replace the matching
    # record in-place inside `curator.records` and rely on `curator.save()`
    # to persist.
    for idx, existing in enumerate(curator.records):
        if existing is ingredient:
            curator.records[idx] = corrected
            break
    curator.save()

    console.print("[green]✓ Corrections applied and saved[/green]")


def main():
    parser = argparse.ArgumentParser(description="Review a single ingredient")
    parser.add_argument(
        "term",
        nargs="?",
        help="Ingredient preferred term to review",
    )
    parser.add_argument(
        "--id",
        help="Review by ontology ID instead",
    )
    parser.add_argument(
        "--suggest-fixes",
        action="store_true",
        help="Show correction suggestions",
    )
    parser.add_argument(
        "--interactive",
        action="store_true",
        help="Apply corrections interactively",
    )

    args = parser.parse_args()

    if not args.term and not args.id:
        parser.error("Either term or --id must be provided")

    # Initialize
    curator = IngredientCurator()
    reviewer = IngredientReviewer()

    # Find ingredient
    if args.id:
        # Find by ontology ID
        all_ingredients = curator.get_by_status("MAPPED")
        ingredient = None
        for ing in all_ingredients:
            if ing.get("ontology_mapping", {}).get("ontology_id") == args.id:
                ingredient = ing
                break

        if not ingredient:
            console.print(f"[red]✗ Ingredient with ontology ID {args.id} not found[/red]")
            return 1
    else:
        # Find by preferred term
        ingredient = curator.get_by_preferred_term(args.term)
        if not ingredient:
            console.print(f"[red]✗ Ingredient '{args.term}' not found[/red]")
            return 1

    # Display ingredient info
    display_ingredient_info(ingredient)

    # Run validation
    console.print("[cyan]Running validation...[/cyan]\n")
    result = reviewer.review_ingredient(ingredient)

    # Display results
    display_validation_results(result)

    # Display suggestions if requested
    if args.suggest_fixes and result.suggestions:
        display_suggestions(result.suggestions)

    # Interactive correction
    if args.interactive and result.suggestions:
        apply_corrections_interactive(curator, ingredient, result.suggestions)

    # Show metadata
    console.print(f"\n[dim]Validation completed in {result.metadata.get('duration_ms', 0)}ms[/dim]")

    return 0 if result.status != "ERROR" else 1


if __name__ == "__main__":
    sys.exit(main())
