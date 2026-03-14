#!/usr/bin/env python3
"""Apply Claude Code curation suggestions to unmapped ingredients.

Reads a YAML file containing Claude's mapping suggestions and applies them
to the unmapped ingredients database with full audit trail.
"""

from __future__ import annotations

import sys
from datetime import datetime
from pathlib import Path

import click
import yaml
from rich.console import Console
from rich.table import Table

# Add src to path
_project_root = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(_project_root / "src"))

from mediaingredientmech.curation.ingredient_curator import IngredientCurator
from mediaingredientmech.utils.chemical_normalizer import normalize_chemical_name
from mediaingredientmech.utils.ontology_client import OntologyCandidate, OntologyClient

console = Console()


def load_suggestions(suggestions_file: Path) -> list[dict]:
    """Load Claude's suggestions from YAML file."""
    with open(suggestions_file) as f:
        data = yaml.safe_load(f)

    return data.get("suggestions", [])


def apply_suggestion(
    suggestion: dict,
    curator: IngredientCurator,
    ontology_client: OntologyClient,
    validate: bool = True,
) -> tuple[bool, str]:
    """Apply a single suggestion.

    Returns:
        Tuple of (success, message)
    """
    identifier = suggestion.get("ontology_id")
    ontology_id = suggestion.get("ontology_id")
    ontology_label = suggestion.get("ontology_label")
    ontology_source = suggestion.get("ontology_source")
    confidence = suggestion.get("confidence", 0.0)
    reasoning = suggestion.get("reasoning", "")
    quality = suggestion.get("quality", "LLM_ASSISTED")
    match_level = suggestion.get("match_level", "MANUAL")

    # Skip unmappable ingredients
    if ontology_id is None or quality == "UNMAPPABLE":
        return False, "Unmappable (skipped)"

    # Find the record
    record = None
    for rec in curator.records:
        if rec.get("ontology_id") == identifier:
            record = rec
            break

    if not record:
        return False, f"Record {identifier} not found"

    # Validate ontology term if requested
    if validate:
        try:
            from oaklib import get_adapter

            resource_map = {
                "CHEBI": "sqlite:obo:chebi",
                "FOODON": "sqlite:obo:foodon",
                "ENVO": "sqlite:obo:envo",
            }
            resource = resource_map.get(ontology_source)
            if not resource:
                return False, f"Unknown ontology source: {ontology_source}"

            adapter = get_adapter(resource)
            label = adapter.label(ontology_id)

            if not label:
                return False, f"Term {ontology_id} not found in {ontology_source}"

            # Update label if different
            if label.lower() != ontology_label.lower():
                console.print(
                    f"[yellow]Label mismatch for {ontology_id}: "
                    f"suggested '{ontology_label}', actual '{label}'[/yellow]"
                )
                ontology_label = label

        except Exception as e:
            return False, f"Validation error: {e}"

    # Create candidate
    candidate = OntologyCandidate(
        ontology_id=ontology_id,
        label=ontology_label,
        source=ontology_source,
        score=confidence,
        synonyms=[],
        definition=None,
    )

    # Apply mapping
    try:
        curator.accept_mapping(
            record,
            candidate,
            quality=quality,
            match_level=match_level,
            llm_assisted=True,
            llm_model="claude-code-interactive",
            notes=f"Claude Code reasoning: {reasoning}",
        )

        # Add original form as synonym if normalized
        original_name = record.get("preferred_term", "")
        norm_result = normalize_chemical_name(original_name)

        if norm_result.applied_rules and norm_result.normalized != original_name:
            if "synonyms" not in record or record["synonyms"] is None:
                record["synonyms"] = []

            # Determine synonym type
            if "stripped_hydrate" in norm_result.applied_rules:
                synonym_type = "HYDRATE_FORM"
            elif "stripped_catalog" in norm_result.applied_rules:
                synonym_type = "CATALOG_VARIANT"
            elif "fixed_incomplete_formula" in norm_result.applied_rules:
                synonym_type = "INCOMPLETE_FORMULA"
            else:
                synonym_type = "ALTERNATE_FORM"

            record["synonyms"].append(
                {
                    "synonym_text": original_name.strip(),
                    "synonym_type": synonym_type,
                    "source": "claude_code_curation",
                    "notes": f"Original form before normalization: {', '.join(norm_result.applied_rules)}",
                }
            )

        return True, f"Mapped to {ontology_id} ({ontology_label})"

    except Exception as e:
        return False, f"Error applying mapping: {e}"


@click.command()
@click.option(
    "--suggestions",
    type=click.Path(path_type=Path),
    required=True,
    help="YAML file with Claude's suggestions",
)
@click.option(
    "--data-path",
    type=click.Path(path_type=Path),
    default=Path("data/curated/unmapped_ingredients.yaml"),
    help="Path to unmapped ingredients YAML",
)
@click.option(
    "--curator",
    default="claude_code",
    help="Curator name for audit trail",
)
@click.option(
    "--skip-validation",
    is_flag=True,
    help="Skip ontology validation (faster but less safe)",
)
@click.option(
    "--dry-run",
    is_flag=True,
    help="Show what would be done without saving",
)
def main(
    suggestions: Path,
    data_path: Path,
    curator: str,
    skip_validation: bool,
    dry_run: bool,
) -> None:
    """Apply Claude Code suggestions to unmapped ingredients."""
    console.print("[bold]Applying Claude Code suggestions...[/bold]\n")

    if dry_run:
        console.print("[yellow]DRY RUN MODE - No changes will be saved[/yellow]\n")

    # Load suggestions
    try:
        suggestions_list = load_suggestions(suggestions)
    except Exception as e:
        console.print(f"[red]Error loading suggestions: {e}[/red]")
        sys.exit(1)

    console.print(f"Loaded {len(suggestions_list)} suggestions\n")

    # Initialize curator
    ontology_client = OntologyClient(sources=["CHEBI", "FOODON", "ENVO"])
    ingredient_curator = IngredientCurator(
        data_path=data_path,
        curator_name=curator,
        ontology_client=ontology_client,
    )

    ingredient_curator.load()

    # Apply suggestions
    results_table = Table(title="Application Results")
    results_table.add_column("Identifier", style="bold")
    results_table.add_column("Name")
    results_table.add_column("Mapping")
    results_table.add_column("Status", style="bold")

    success_count = 0
    fail_count = 0

    for suggestion in suggestions_list:
        identifier = suggestion.get("ontology_id", "?")
        name = suggestion.get("name", "?")
        ontology_id = suggestion.get("ontology_id", "?")
        ontology_label = suggestion.get("ontology_label", "?")

        success, message = apply_suggestion(
            suggestion,
            ingredient_curator,
            ontology_client,
            validate=not skip_validation,
        )

        if success:
            success_count += 1
            status = "[green]✓ Success[/green]"
        else:
            fail_count += 1
            status = f"[red]✗ {message}[/red]"

        # Handle null ontology_label for unmappable ingredients
        if ontology_label is None or ontology_id is None:
            mapping_display = "UNMAPPABLE"
        elif len(ontology_label) > 20:
            mapping_display = f"{ontology_id} ({ontology_label[:20]}...)"
        else:
            mapping_display = f"{ontology_id} ({ontology_label})"

        results_table.add_row(
            identifier,
            name[:30] + "..." if len(name) > 30 else name,
            mapping_display,
            status,
        )

    console.print(results_table)

    # Summary
    console.print(
        f"\n[bold]Summary:[/bold]\n"
        f"  Success: [green]{success_count}[/green]\n"
        f"  Failed: [red]{fail_count}[/red]\n"
        f"  Total: {len(suggestions_list)}"
    )

    # Save
    if not dry_run and success_count > 0:
        ingredient_curator.save()
        console.print(f"\n[green]✓ Saved {success_count} mappings to {data_path}[/green]")
    elif dry_run:
        console.print("\n[dim]Dry run - no changes saved[/dim]")


if __name__ == "__main__":
    main()
