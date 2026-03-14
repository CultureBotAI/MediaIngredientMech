#!/usr/bin/env python3
"""Prepare unmapped ingredients for Claude Code curation.

Generates a formatted analysis of unmapped ingredients that Claude Code
can use to provide intelligent mapping suggestions in an interactive session.
"""

from __future__ import annotations

import sys
from pathlib import Path

import click
import yaml
from rich.console import Console

# Add src to path
_project_root = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(_project_root / "src"))

from mediaingredientmech.utils.chemical_normalizer import (
    categorize_unmapped_name,
    normalize_chemical_name,
)

console = Console()


def format_ingredient_for_claude(record: dict, index: int) -> str:
    """Format an ingredient record for Claude Code analysis."""
    identifier = record.get("ontology_id", "")
    name = record.get("preferred_term", "")
    stats = record.get("occurrence_statistics", {})
    synonyms = record.get("synonyms", []) or []

    # Get normalization
    norm_result = normalize_chemical_name(name)
    category = categorize_unmapped_name(name)

    # Extract synonym texts
    syn_texts = []
    for syn in synonyms[:5]:
        if isinstance(syn, dict):
            syn_texts.append(syn.get("synonym_text", ""))
        else:
            syn_texts.append(str(syn))

    # Build formatted text
    text = f"""
## Ingredient {index}: {identifier}

**Name:** {name}
**Category:** {category}
**Occurrences:** {stats.get('total_occurrences', 0)} across {stats.get('media_count', 0)} media
"""

    if norm_result.applied_rules:
        text += f"**Normalized:** {norm_result.normalized} (rules: {', '.join(norm_result.applied_rules)})\n"
        text += f"**Search variants:** {', '.join(norm_result.variants[:3])}\n"

    if syn_texts:
        text += f"**Synonyms:** {', '.join(syn_texts[:3])}\n"

    return text


@click.command()
@click.option(
    "--data-path",
    type=click.Path(path_type=Path),
    default=Path("data/curated/unmapped_ingredients.yaml"),
    help="Path to unmapped ingredients YAML",
)
@click.option(
    "--category",
    help="Filter by category (SIMPLE_CHEMICAL, etc.)",
)
@click.option(
    "--output",
    type=click.Path(path_type=Path),
    default=Path("notes/unmapped_for_claude.md"),
    help="Output markdown file",
)
@click.option(
    "--limit",
    type=int,
    help="Limit number of ingredients",
)
def main(
    data_path: Path,
    category: str | None,
    output: Path,
    limit: int | None,
) -> None:
    """Prepare unmapped ingredients for Claude Code curation."""
    console.print("[bold]Preparing ingredients for Claude Code curation...[/bold]\n")

    # Load data
    with open(data_path) as f:
        data = yaml.safe_load(f)

    ingredients = data.get("ingredients", [])
    unmapped = [ing for ing in ingredients if ing.get("mapping_status") == "UNMAPPED"]

    # Filter by category
    if category:
        unmapped = [
            ing
            for ing in unmapped
            if categorize_unmapped_name(ing.get("preferred_term", "")) == category
        ]

    # Sort by occurrence
    unmapped.sort(
        key=lambda r: r.get("occurrence_statistics", {}).get("total_occurrences", 0),
        reverse=True,
    )

    # Limit
    if limit:
        unmapped = unmapped[:limit]

    console.print(f"Found {len(unmapped)} unmapped ingredients\n")

    # Generate markdown
    lines = [
        "# Unmapped Ingredients for Claude Code Curation",
        "",
        f"**Total:** {len(unmapped)} ingredients",
        f"**Category filter:** {category or 'All'}",
        "",
        "## Instructions for Claude Code",
        "",
        "For each ingredient below, suggest the most appropriate ontology mapping:",
        "",
        "1. **Ontology selection:**",
        "   - CHEBI - Simple chemicals, salts, compounds",
        "   - FOODON - Biological materials, extracts, complex mixtures",
        "   - ENVO - Environmental samples (soil, seawater, etc.)",
        "",
        "2. **For each ingredient provide:**",
        "   - Ontology ID (e.g., CHEBI:32599)",
        "   - Ontology label (e.g., magnesium sulfate)",
        "   - Ontology source (CHEBI/FOODON/ENVO)",
        "   - Confidence (0.0-1.0)",
        "   - Reasoning (why this mapping is correct)",
        "   - Quality rating (EXACT_MATCH, SYNONYM_MATCH, CLOSE_MATCH, or LLM_ASSISTED)",
        "",
        "3. **Special cases:**",
        "   - Hydrates → base chemical (MgSO4•7H2O → magnesium sulfate)",
        "   - Catalog variants → base chemical (NaCl (Fisher X) → sodium chloride)",
        "   - Incomplete formulas → corrected (K2HPO → dipotassium phosphate)",
        "   - Complex mixtures → may be UNMAPPABLE if no appropriate term exists",
        "",
        "4. **Format your response as:**",
        "   ```",
        "   Ingredient X: IDENTIFIER",
        "   Suggested mapping: ONTOLOGY_ID (label)",
        "   Source: ONTOLOGY_SOURCE",
        "   Confidence: 0.XX",
        "   Quality: QUALITY_RATING",
        "   Reasoning: [explanation]",
        "   ```",
        "",
        "---",
        "",
    ]

    # Add ingredient details
    for i, ing in enumerate(unmapped, 1):
        lines.append(format_ingredient_for_claude(ing, i))

    # Add summary section
    lines.extend([
        "",
        "---",
        "",
        "## Summary",
        "",
        "After reviewing all ingredients, provide a summary:",
        "- Total suggested mappings",
        "- High confidence (≥0.9) mappings",
        "- Medium confidence (0.7-0.89) mappings",
        "- Low confidence or unmappable items",
        "- Any patterns or insights noticed",
    ])

    # Write output
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text("\n".join(lines))

    console.print(f"[green]✓ Prepared file: {output}[/green]")
    console.print(f"\n[bold cyan]Next steps:[/bold cyan]")
    console.print(f"1. Review the file: {output}")
    console.print(f"2. Ask Claude Code to analyze and suggest mappings")
    console.print(f"3. Use apply_claude_suggestions.py to apply accepted mappings")


if __name__ == "__main__":
    main()
