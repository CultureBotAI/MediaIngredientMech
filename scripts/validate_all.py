#!/usr/bin/env python3
"""CLI to validate all curated YAML records against the MediaIngredientMech schema.

Supports both collection files and individual ingredient files.

Usage:
    python scripts/validate_all.py [--data-dir data/curated] [--no-oak] [--verbose]
    python scripts/validate_all.py --mode individual [--ingredients-dir data/ingredients]
    python scripts/validate_all.py --mode both
"""

from __future__ import annotations

import sys
from pathlib import Path

import click
from rich.console import Console
from rich.table import Table

# Ensure the src package is importable when running the script directly
_project_root = Path(__file__).resolve().parents[1]
_src = _project_root / "src"
if str(_src) not in sys.path:
    sys.path.insert(0, str(_src))

from mediaingredientmech.validation.schema_validator import SchemaValidationResult, validate_file
from mediaingredientmech.validation.ontology_validator import (
    OntologyValidationResult,
    validate_records,
)

import yaml

console = Console()


def _load_yaml(path: Path) -> dict | None:
    try:
        with open(path) as fh:
            return yaml.safe_load(fh) or {}
    except Exception:
        return None


@click.command()
@click.option(
    "--data-dir",
    type=click.Path(exists=False),
    default=None,
    help="Directory containing collection YAML files (default: data/curated/)",
)
@click.option(
    "--ingredients-dir",
    type=click.Path(exists=False),
    default=None,
    help="Directory containing individual ingredient files (default: data/ingredients/)",
)
@click.option(
    "--mode",
    type=click.Choice(["collection", "individual", "both"]),
    default="both",
    help="Validation mode: collection files, individual files, or both (default: both)",
)
@click.option("--no-oak", is_flag=True, help="Skip OAK ontology lookups (format checks only)")
@click.option("--verbose", "-v", is_flag=True, help="Show all messages, not just summary")
def main(
    data_dir: str | None,
    ingredients_dir: str | None,
    mode: str,
    no_oak: bool,
    verbose: bool
):
    """Validate curated YAML data files (collections and/or individual files)."""
    # Set default paths
    if data_dir is None:
        data_dir_path = _project_root / "data" / "curated"
    else:
        data_dir_path = Path(data_dir)

    if ingredients_dir is None:
        ingredients_dir_path = _project_root / "data" / "ingredients"
    else:
        ingredients_dir_path = Path(ingredients_dir)

    # Collect files to validate based on mode
    yaml_files = []

    if mode in ("collection", "both"):
        if data_dir_path.exists():
            collection_files = sorted(data_dir_path.glob("**/*.yaml")) + sorted(data_dir_path.glob("**/*.yml"))
            yaml_files.extend(collection_files)
            if collection_files:
                console.print(f"[bold]Collection files:[/bold] {len(collection_files)} from {data_dir_path}")
        elif mode == "collection":
            console.print(f"[yellow]Collection directory not found: {data_dir_path}[/yellow]")
            sys.exit(0)

    if mode in ("individual", "both"):
        if ingredients_dir_path.exists():
            individual_files = sorted(ingredients_dir_path.glob("**/*.yaml")) + sorted(ingredients_dir_path.glob("**/*.yml"))
            yaml_files.extend(individual_files)
            if individual_files:
                console.print(f"[bold]Individual files:[/bold] {len(individual_files)} from {ingredients_dir_path}")
        elif mode == "individual":
            console.print(f"[yellow]Ingredients directory not found: {ingredients_dir_path}[/yellow]")
            console.print("[yellow]Run export_individual_records.py first to create individual files.[/yellow]")
            sys.exit(0)

    if not yaml_files:
        console.print(f"[yellow]No YAML files found to validate[/yellow]")
        sys.exit(0)

    console.print(f"\n[bold]Validating {len(yaml_files)} total file(s)[/bold]\n")

    total_errors = 0
    total_warnings = 0
    total_terms = 0
    total_valid_terms = 0
    file_results: list[tuple[str, SchemaValidationResult, OntologyValidationResult]] = []

    for fp in yaml_files:
        # Schema validation
        schema_result = validate_file(fp)

        # Ontology validation
        data = _load_yaml(fp)
        if data is not None:
            onto_result = validate_records(data, source=str(fp), use_oak=not no_oak)
        else:
            onto_result = OntologyValidationResult(file_path=str(fp))

        file_results.append((str(fp), schema_result, onto_result))
        total_errors += len(schema_result.errors) + len(onto_result.errors)
        total_warnings += len(schema_result.warnings) + len(onto_result.warnings)
        total_terms += onto_result.terms_checked
        total_valid_terms += onto_result.terms_valid

    # Detailed output
    if verbose:
        for fp, sr, orr in file_results:
            all_msgs = sr.messages + [
                type("Msg", (), {"level": m.level, "path": m.path, "message": m.message})()
                for m in orr.messages
            ]
            if not all_msgs:
                continue
            console.print(f"\n[bold]{fp}[/bold]")
            for m in all_msgs:
                color = "red" if m.level == "error" else "yellow"
                console.print(f"  [{color}]{m.level.upper()}[/{color}] {m.path}: {m.message}")

    # Summary table
    table = Table(title="Validation Summary")
    table.add_column("File", style="cyan")
    table.add_column("Schema Errors", justify="right")
    table.add_column("Schema Warnings", justify="right")
    table.add_column("Ontology Errors", justify="right")
    table.add_column("Ontology Warnings", justify="right")
    table.add_column("Status", justify="center")

    for fp, sr, orr in file_results:
        name = Path(fp).name
        se = len(sr.errors)
        sw = len(sr.warnings)
        oe = len(orr.errors)
        ow = len(orr.warnings)
        status = "[green]PASS[/green]" if (se + oe) == 0 else "[red]FAIL[/red]"
        table.add_row(name, str(se), str(sw), str(oe), str(ow), status)

    console.print()
    console.print(table)

    # Stats
    console.print(f"\n[bold]Total files:[/bold] {len(yaml_files)}")
    console.print(f"[bold]Total errors:[/bold] {total_errors}")
    console.print(f"[bold]Total warnings:[/bold] {total_warnings}")
    if total_terms > 0:
        console.print(f"[bold]Ontology terms checked:[/bold] {total_terms}")
        console.print(f"[bold]Ontology terms valid:[/bold] {total_valid_terms}")
    oak_used = any(orr.oak_available for _, _, orr in file_results)
    if no_oak:
        console.print("[dim]OAK lookups: skipped (--no-oak)[/dim]")
    elif not oak_used:
        console.print("[dim]OAK lookups: not available (format checks only)[/dim]")
    else:
        console.print("[green]OAK lookups: active[/green]")

    if total_errors > 0:
        console.print("\n[red bold]Validation FAILED[/red bold]")
        sys.exit(1)
    else:
        console.print("\n[green bold]Validation PASSED[/green bold]")
        sys.exit(0)


if __name__ == "__main__":
    main()
