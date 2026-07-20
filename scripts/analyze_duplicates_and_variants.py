#!/usr/bin/env python3
"""Analyze ingredient data for duplicates and variant relationships.

Finds:
1. True duplicates (same chemical, same form) - candidates for merging
2. Variant relationships (hydrates, salts, stereoisomers) - candidates for hierarchy
3. Role patterns across variants

Conservative approach: Don't merge variants, propose hierarchy instead.
"""

from __future__ import annotations

import re
import sys
from collections import defaultdict
from pathlib import Path

import click
import yaml
from rich.console import Console
from rich.table import Table
from rich.tree import Tree

console = Console()

# Add src to path
_project_root = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(_project_root / "src"))

from mediaingredientmech.utils.chemical_normalizer import normalize_chemical_name
from mediaingredientmech.utils.role_iteration import FACET_ROLE_SLOTS, iter_role_assignments


def ingredient_role_names(ing: dict) -> list[str]:
    """Role names assigned to an ingredient across the three role facets."""
    return [
        r.get("role") for _, r in iter_role_assignments(ing, slots=FACET_ROLE_SLOTS)
    ]


def load_ingredients(yaml_path: Path) -> list[dict]:
    """Load ingredients from YAML file."""
    with open(yaml_path) as f:
        data = yaml.safe_load(f)
    if isinstance(data, dict) and "ingredients" in data:
        return data["ingredients"]
    return data if isinstance(data, list) else []


def is_hydrate(name: str) -> tuple[bool, str | None]:
    """Check if ingredient is a hydrate. Returns (is_hydrate, base_form)."""
    # Pattern: anything with ·nH2O, xH2O, * n H2O, etc.
    patterns = [
        r'(.+?)\s*[·•×x]\s*(\d+)\s*H2O',  # MgSO4·7H2O
        r'(.+?)\s+(\d+)\s*H2O',            # MgSO4 7H2O
        r'(.+?)\s*\(\s*(\d+)\s*H2O\s*\)',  # MgSO4 (7H2O)
    ]

    for pattern in patterns:
        match = re.search(pattern, name, re.IGNORECASE)
        if match:
            base = match.group(1).strip()
            return True, base

    return False, None


def is_salt_form(name: str) -> tuple[bool, str | None]:
    """Check if ingredient is a salt form. Returns (is_salt, base_form)."""
    # Pattern: compound name + HCl, Na, K, etc.
    salt_patterns = [
        r'(.+?)\s+HCl',
        r'(.+?)\s+hydrochloride',
        r'(.+?)\s+sodium\s+salt',
        r'(.+?)\s+potassium\s+salt',
        r'(.+?)\s+Na\+?',
        r'(.+?)\s+K\+?',
    ]

    for pattern in salt_patterns:
        match = re.search(pattern, name, re.IGNORECASE)
        if match:
            base = match.group(1).strip()
            return True, base

    return False, None


def is_stereoisomer(name: str) -> tuple[bool, str | None]:
    """Check if ingredient is a stereoisomer. Returns (is_stereo, base_form)."""
    # Pattern: D-, L-, (+)-, (-)-, R-, S- prefix
    patterns = [
        r'^([DL])-(.+)',
        r'^\(([+-])\)-(.+)',
        r'^([RS])-(.+)',
    ]

    for pattern in patterns:
        match = re.search(pattern, name)
        if match:
            if len(match.groups()) == 2:
                base = match.group(2).strip()
            else:
                base = match.group(3).strip() if len(match.groups()) > 2 else name
            return True, base

    return False, None


def detect_variant_type(name: str) -> tuple[str, str | None]:
    """Detect variant type and base form.

    Returns: (variant_type, base_form)
    """
    is_hyd, base = is_hydrate(name)
    if is_hyd:
        return "HYDRATE", base

    is_sal, base = is_salt_form(name)
    if is_sal:
        return "SALT", base

    is_ster, base = is_stereoisomer(name)
    if is_ster:
        return "STEREOISOMER", base

    return "BASE_CHEMICAL", None


def group_by_chebi(ingredients: list[dict]) -> dict[str, list[dict]]:
    """Group ingredients by CHEBI ID."""
    groups = defaultdict(list)

    for ing in ingredients:
        ont_id = ing.get("ontology_id", "")
        if ont_id.startswith("CHEBI:"):
            groups[ont_id].append(ing)

    return dict(groups)


def find_duplicates(ingredients: list[dict]) -> list[list[dict]]:
    """Find true duplicates (same chemical, same form)."""
    duplicates = []

    # Group by CHEBI ID
    chebi_groups = group_by_chebi(ingredients)

    for chebi_id, group in chebi_groups.items():
        if len(group) > 1:
            # Multiple ingredients with same CHEBI ID
            # Check if they're variants or true duplicates

            # Subgroup by variant type
            by_variant = defaultdict(list)
            for ing in group:
                variant_type, _ = detect_variant_type(ing.get("preferred_term", ""))
                by_variant[variant_type].append(ing)

            # If multiple with same variant type, likely duplicates
            for variant_type, subgroup in by_variant.items():
                if len(subgroup) > 1:
                    duplicates.append(subgroup)

    return duplicates


def find_variants(ingredients: list[dict]) -> dict[str, list[dict]]:
    """Find variant relationships (different forms of same chemical)."""
    variants = defaultdict(list)

    # Group by CHEBI ID
    chebi_groups = group_by_chebi(ingredients)

    for chebi_id, group in chebi_groups.items():
        if len(group) > 1:
            # Check variant types
            variant_types = set()
            for ing in group:
                variant_type, _ = detect_variant_type(ing.get("preferred_term", ""))
                variant_types.add(variant_type)

            # If multiple variant types, it's a variant family
            if len(variant_types) > 1:
                variants[chebi_id] = group

    return dict(variants)


def analyze_roles_in_variants(variant_group: list[dict]) -> dict:
    """Analyze role patterns within variant group."""
    role_analysis = {
        "has_roles": False,
        "common_roles": set(),
        "unique_roles": {},
        "role_inheritance_candidate": False
    }

    all_roles = []
    for ing in variant_group:
        role_names = ingredient_role_names(ing)
        if role_names:
            role_analysis["has_roles"] = True
            all_roles.append((ing.get("preferred_term"), set(role_names)))

    if all_roles:
        # Find common roles
        role_analysis["common_roles"] = set.intersection(*[roles for _, roles in all_roles])

        # Find unique roles per ingredient
        for name, roles in all_roles:
            unique = roles - role_analysis["common_roles"]
            if unique:
                role_analysis["unique_roles"][name] = unique

        # If there are common roles, inheritance makes sense
        if role_analysis["common_roles"]:
            role_analysis["role_inheritance_candidate"] = True

    return role_analysis


@click.command()
@click.option(
    "--mapped",
    type=click.Path(exists=True, path_type=Path),
    default=Path("data/curated/mapped_ingredients.yaml"),
    help="Mapped ingredients YAML",
)
@click.option(
    "--output",
    type=click.Path(path_type=Path),
    default=Path("analysis/duplicates_and_variants.yaml"),
    help="Output analysis YAML",
)
def main(mapped: Path, output: Path):
    """Analyze ingredients for duplicates and variant relationships."""
    console.print("\n[bold]Ingredient Duplicate & Variant Analysis[/bold]\n")

    # Load ingredients
    console.print(f"Loading ingredients from {mapped}...")
    ingredients = load_ingredients(mapped)
    console.print(f"Loaded {len(ingredients)} ingredients\n")

    # Find duplicates
    console.print("[cyan]Finding true duplicates...[/cyan]")
    duplicates = find_duplicates(ingredients)
    console.print(f"Found {len(duplicates)} duplicate groups\n")

    # Find variants
    console.print("[cyan]Finding variant relationships...[/cyan]")
    variants = find_variants(ingredients)
    console.print(f"Found {len(variants)} variant families\n")

    # Display duplicates
    if duplicates:
        console.print("\n[bold red]═══ TRUE DUPLICATES (Merge Candidates) ═══[/bold red]\n")

        for i, dup_group in enumerate(duplicates[:10], 1):
            console.print(f"[yellow]Duplicate Group {i}:[/yellow]")
            table = Table(show_header=True, header_style="bold cyan")
            table.add_column("ID", style="yellow")
            table.add_column("Ontology ID", style="green")
            table.add_column("Preferred Term", style="white")
            table.add_column("Occurrences", style="magenta")

            for ing in dup_group:
                stats = ing.get("occurrence_statistics", {})
                table.add_row(
                    ing.get("id", "")[:30],
                    ing.get("ontology_id", ""),
                    ing.get("preferred_term", ""),
                    str(stats.get("total_occurrences", 0))
                )

            console.print(table)
            console.print()

        if len(duplicates) > 10:
            console.print(f"... and {len(duplicates) - 10} more duplicate groups\n")

    # Display variants
    if variants:
        console.print("\n[bold green]═══ VARIANT FAMILIES (Hierarchy Candidates) ═══[/bold green]\n")

        for i, (chebi_id, variant_group) in enumerate(list(variants.items())[:10], 1):
            console.print(f"[yellow]Variant Family {i}: {chebi_id}[/yellow]")

            # Create tree
            tree = Tree(f"[bold]{chebi_id}[/bold]")

            for ing in variant_group:
                variant_type, base = detect_variant_type(ing.get("preferred_term", ""))
                label = ing.get("preferred_term", "")
                id_str = ing.get("id", "")

                node_text = f"[cyan]{label}[/cyan] ({variant_type})"
                roles = ingredient_role_names(ing)
                if roles:
                    node_text += f" [dim]Roles: {', '.join(roles[:2])}[/dim]"

                tree.add(f"{node_text} - {id_str[:30]}")

            console.print(tree)

            # Analyze roles
            role_analysis = analyze_roles_in_variants(variant_group)
            if role_analysis["has_roles"]:
                console.print(f"  [dim]Common roles: {', '.join(role_analysis['common_roles']) or 'None'}[/dim]")
                console.print(f"  [dim]Role inheritance candidate: {role_analysis['role_inheritance_candidate']}[/dim]")

            console.print()

        if len(variants) > 10:
            console.print(f"... and {len(variants) - 10} more variant families\n")

    # Summary statistics
    console.print("\n[bold]═══ SUMMARY STATISTICS ═══[/bold]\n")

    summary_table = Table(show_header=True, header_style="bold cyan")
    summary_table.add_column("Metric", style="bold")
    summary_table.add_column("Count", justify="right", style="yellow")

    summary_table.add_row("Total ingredients", str(len(ingredients)))
    summary_table.add_row("Duplicate groups (merge candidates)", str(len(duplicates)))
    summary_table.add_row("Variant families (hierarchy candidates)", str(len(variants)))

    # Count ingredients in variants
    ingredients_in_variants = sum(len(v) for v in variants.values())
    summary_table.add_row("Ingredients in variant families", str(ingredients_in_variants))

    # Count by variant type
    variant_types = defaultdict(int)
    for ing in ingredients:
        variant_type, _ = detect_variant_type(ing.get("preferred_term", ""))
        variant_types[variant_type] += 1

    summary_table.add_row("", "")
    summary_table.add_row("[bold]By Variant Type:[/bold]", "")
    for vtype, count in sorted(variant_types.items()):
        summary_table.add_row(f"  {vtype}", str(count))

    console.print(summary_table)

    # Save analysis
    output.parent.mkdir(parents=True, exist_ok=True)

    analysis_data = {
        "summary": {
            "total_ingredients": len(ingredients),
            "duplicate_groups": len(duplicates),
            "variant_families": len(variants),
            "ingredients_in_variants": ingredients_in_variants,
        },
        "duplicates": [
            {
                "chebi_id": dup_group[0].get("ontology_id"),
                "count": len(dup_group),
                "ingredients": [
                    {
                        "id": ing.get("id"),
                        "ontology_id": ing.get("ontology_id"),
                        "preferred_term": ing.get("preferred_term"),
                        "occurrences": ing.get("occurrence_statistics", {}).get("total_occurrences", 0)
                    }
                    for ing in dup_group
                ]
            }
            for dup_group in duplicates
        ],
        "variants": {
            chebi_id: {
                "count": len(variant_group),
                "ingredients": [
                    {
                        "id": ing.get("id"),
                        "ontology_id": ing.get("ontology_id"),
                        "preferred_term": ing.get("preferred_term"),
                        "variant_type": detect_variant_type(ing.get("preferred_term", ""))[0],
                        "roles": ingredient_role_names(ing),
                    }
                    for ing in variant_group
                ],
                "role_analysis": analyze_roles_in_variants(variant_group)
            }
            for chebi_id, variant_group in variants.items()
        }
    }

    with open(output, "w") as f:
        yaml.dump(analysis_data, f, default_flow_style=False, sort_keys=False, allow_unicode=True)

    console.print(f"\n[bold green]✅ Analysis saved to {output}[/bold green]\n")


if __name__ == "__main__":
    main()
