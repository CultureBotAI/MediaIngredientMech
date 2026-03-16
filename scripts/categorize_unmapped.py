#!/usr/bin/env python3
"""Categorize unmapped ingredients and generate reports by category."""

import re
from pathlib import Path
import yaml

# Paths
DATA_DIR = Path(__file__).parent.parent / "data" / "curated"
UNMAPPED_PATH = DATA_DIR / "unmapped_ingredients.yaml"
OUTPUT_DIR = DATA_DIR


def load_yaml(path):
    """Load YAML file."""
    with open(path, encoding="utf-8") as f:
        return yaml.safe_load(f)


def save_yaml(data, path):
    """Save YAML file."""
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        yaml.dump(data, f, default_flow_style=False, sort_keys=False, allow_unicode=True)


def save_text(content, path):
    """Save text file."""
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)


def categorize_ingredient(record):
    """Categorize an unmapped ingredient.

    Returns:
        Category: PLACEHOLDER, COMPLEX_MEDIA, INCOMPLETE_FORMULA, ALREADY_MAPPED, or OTHER
    """
    notes = record.get("notes", "")
    term = record["preferred_term"]

    # Check notes first
    if "Placeholder" in notes:
        return "PLACEHOLDER"
    if "Complex media" in notes:
        return "COMPLEX_MEDIA"
    if "Incomplete" in notes:
        return "INCOMPLETE_FORMULA"

    # Check for merge artifacts
    if term.startswith("[Merged") and "duplicates" in term:
        return "PLACEHOLDER"

    # Check for already mapped (different encoding variants)
    already_mapped = [
        "Sterile dH2O",  # Mapped as "sterile dH2O"
        "Na2Glycerophosphate.5H2O",  # Mapped as Na2glycerophosphate•5H2O
        "Na2Glycerophosphate•5H2O",  # Mapped as Na2glycerophosphate•5H2O
    ]
    if term in already_mapped:
        return "ALREADY_MAPPED"

    # Stock solutions and generic mixtures
    stock_patterns = ["Stock", "stock", "Nutrients", "nutrients"]
    if any(p in term for p in stock_patterns):
        return "COMPLEX_MEDIA"

    # Pattern-based categorization for incomplete formulas
    # Known incomplete formulas with corrections
    known_incomplete = {
        "NaNO", "K2HPO", "MgCO", "KH2PO", "CaCO", "KNO", "NaHCO",
        "NH4NO", "Na2CO", "H3BO", "NH4MgPO",
        "Ca", "K", "Mg", "Na", "Fe", "Zn"
    }
    if term in known_incomplete:
        return "INCOMPLETE_FORMULA"

    # Single element symbols (incomplete)
    if re.match(r"^[A-Z][a-z]?$", term) and len(term) <= 2:
        return "INCOMPLETE_FORMULA"

    return "OTHER"


def generate_category_report(category_name, ingredients):
    """Generate a text report for a category."""
    lines = []
    lines.append(f"# {category_name}")
    lines.append(f"**Count**: {len(ingredients)} ingredients")
    lines.append("")
    lines.append("| Preferred Term | Ontology ID | Occurrences | Notes |")
    lines.append("|----------------|-------------|-------------|-------|")

    for ing in ingredients:
        term = ing["preferred_term"]
        ont_id = ing["ontology_id"]
        occ = ing["occurrence_statistics"]["total_occurrences"]
        notes = ing.get("notes", "")[:50]  # Truncate long notes
        lines.append(f"| {term} | {ont_id} | {occ} | {notes} |")

    lines.append("")
    return "\n".join(lines)


def generate_incomplete_formula_report(ingredients):
    """Generate detailed report for incomplete formulas."""
    lines = []
    lines.append("# INCOMPLETE FORMULAS - Report to CultureMech")
    lines.append(f"**Count**: {len(ingredients)} ingredients")
    lines.append("")
    lines.append("These are malformed chemical formulas in the source data that should be corrected.")
    lines.append("")
    lines.append("| Ingredient | Occurrences | Likely Correct Formula | Expected CHEBI ID |")
    lines.append("|------------|-------------|------------------------|-------------------|")

    # Known corrections
    corrections = {
        "NaNO": ("NaNO₃", "CHEBI:34218", "sodium nitrate"),
        "K2HPO": ("K₂HPO₄", "CHEBI:32030", "dipotassium phosphate"),
        "MgCO": ("MgCO₃", "CHEBI:6611", "magnesium carbonate"),
        "KH2PO": ("KH₂PO₄", "CHEBI:32583", "potassium dihydrogen phosphate"),
        "CaCO": ("CaCO₃", "CHEBI:3311", "calcium carbonate"),
        "KNO": ("KNO₃", "CHEBI:63043", "potassium nitrate"),
        "NaHCO": ("NaHCO₃", "CHEBI:32139", "sodium bicarbonate"),
        "NH4NO": ("NH₄NO₃", "CHEBI:63038", "ammonium nitrate"),
        "Na2CO": ("Na₂CO₃", "CHEBI:29377", "sodium carbonate"),
        "NH4MgPO": ("(NH₄)MgPO₄", "?", "ammonium magnesium phosphate"),
        "H3BO": ("H₃BO₃", "CHEBI:33118", "boric acid"),
    }

    for ing in ingredients:
        term = ing["preferred_term"]
        occ = ing["occurrence_statistics"]["total_occurrences"]

        if term in corrections:
            correct, chebi, name = corrections[term]
            lines.append(f"| {term} | {occ} | {correct} ({name}) | {chebi} |")
        else:
            lines.append(f"| {term} | {occ} | ? | ? |")

    lines.append("")
    lines.append("## Action Required")
    lines.append("Report these to CultureMech maintainers for source data correction.")
    lines.append("")

    return "\n".join(lines)


def main():
    """Categorize unmapped ingredients and generate reports."""
    print("=" * 80)
    print("CATEGORIZE UNMAPPED INGREDIENTS")
    print("=" * 80)
    print()

    # Load unmapped
    print("Loading unmapped_ingredients.yaml...")
    data = load_yaml(UNMAPPED_PATH)
    ingredients = data["ingredients"]
    print(f"  Loaded {len(ingredients)} unmapped ingredients")
    print()

    # Categorize
    print("Categorizing ingredients...")
    categories = {
        "PLACEHOLDER": [],
        "COMPLEX_MEDIA": [],
        "INCOMPLETE_FORMULA": [],
        "ALREADY_MAPPED": [],
        "OTHER": [],
    }

    for ing in ingredients:
        category = categorize_ingredient(ing)
        categories[category].append(ing)

    # Sort each category by occurrence (descending)
    for cat in categories:
        categories[cat].sort(
            key=lambda x: x["occurrence_statistics"]["total_occurrences"],
            reverse=True
        )

    # Print summary
    print("\nCategorization Summary:")
    print("-" * 80)
    for cat, ings in categories.items():
        print(f"  {cat:20s}: {len(ings):3d} ingredients")
    print("-" * 80)
    print(f"  {'TOTAL':20s}: {len(ingredients):3d} ingredients")
    print()

    # Generate category YAML files
    print("Generating category files...")
    for cat, ings in categories.items():
        if not ings:
            continue

        cat_data = {
            "category": cat,
            "count": len(ings),
            "ingredients": ings,
        }

        output_path = OUTPUT_DIR / f"unmapped_{cat.lower()}.yaml"
        save_yaml(cat_data, output_path)
        print(f"  ✓ Saved {output_path.name} ({len(ings)} ingredients)")

    print()

    # Generate markdown reports
    print("Generating markdown reports...")

    # Summary report
    summary_lines = []
    summary_lines.append("# Unmapped Ingredients by Category")
    summary_lines.append("")
    summary_lines.append(f"**Total Unmapped**: {len(ingredients)} ingredients")
    summary_lines.append("")
    summary_lines.append("## Category Breakdown")
    summary_lines.append("")

    for cat, ings in categories.items():
        summary_lines.append(f"### {cat.replace('_', ' ').title()}")
        summary_lines.append(f"**Count**: {len(ings)}")
        summary_lines.append("")

        # Top 5 by occurrence
        if ings:
            summary_lines.append("Top 5 by occurrence:")
            for i, ing in enumerate(ings[:5], 1):
                term = ing["preferred_term"]
                occ = ing["occurrence_statistics"]["total_occurrences"]
                summary_lines.append(f"{i}. {term} ({occ} occurrences)")
            summary_lines.append("")

    summary_path = OUTPUT_DIR / "UNMAPPED_CATEGORIES_SUMMARY.md"
    save_text("\n".join(summary_lines), summary_path)
    print(f"  ✓ Saved {summary_path.name}")

    # Detailed category reports
    for cat, ings in categories.items():
        if not ings:
            continue

        if cat == "INCOMPLETE_FORMULA":
            report = generate_incomplete_formula_report(ings)
        else:
            report = generate_category_report(cat.replace("_", " ").title(), ings)

        report_path = OUTPUT_DIR / f"UNMAPPED_{cat}.md"
        save_text(report, report_path)
        print(f"  ✓ Saved {report_path.name}")

    print()
    print("=" * 80)
    print("CATEGORIZATION COMPLETE")
    print("=" * 80)
    print()
    print("Generated files:")
    print(f"  - {len(categories)} category YAML files (unmapped_*.yaml)")
    print(f"  - {len(categories) + 1} markdown reports (UNMAPPED_*.md)")
    print()


if __name__ == "__main__":
    main()
