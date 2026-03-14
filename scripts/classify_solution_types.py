#!/usr/bin/env python3
"""Classify ingredients as solution types (vitamin mixes, trace metal solutions, etc.).

This script identifies ingredients that are pre-mixed solutions or stock solutions
rather than individual pure chemicals, and assigns appropriate SolutionTypeEnum values.
"""

import sys
from pathlib import Path

# Add src to path
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from mediaingredientmech.curation.ingredient_curator import IngredientCurator


def classify_solution_type(preferred_term: str, synonyms: list[dict]) -> str | None:
    """Classify an ingredient as a solution type based on its name and synonyms.

    Args:
        preferred_term: The preferred term for the ingredient
        synonyms: List of synonym dictionaries

    Returns:
        SolutionTypeEnum value or None if not a solution/mixture
    """
    # Combine all text for analysis
    all_text = preferred_term.lower()
    for syn in synonyms:
        all_text += " " + syn.get("synonym_text", "").lower()

    # Vitamin mixes
    vitamin_keywords = [
        "vitamin",
        "b12",
        "biotin",
        "thiamin",
        "riboflavin",
        "niacin",
        "pantothenic",
        "pyridoxine",
        "folate",
        "cobalamin",
    ]
    if any(kw in all_text for kw in vitamin_keywords) and (
        "solution" in all_text or "mix" in all_text or "supplement" in all_text
    ):
        return "VITAMIN_MIX"

    # Trace metal/element mixes
    trace_keywords = ["trace element", "trace metal", "micronutrient", "metal solution"]
    if any(kw in all_text for kw in trace_keywords):
        return "TRACE_METAL_MIX"

    # Amino acid mixes
    aa_keywords = ["amino acid"]
    if any(kw in all_text for kw in aa_keywords) and (
        "solution" in all_text or "mix" in all_text
    ):
        return "AMINO_ACID_MIX"

    # Buffer solutions
    buffer_keywords = [
        "buffer solution",
        "phosphate buffer",
        "hepes buffer",
        "tris buffer",
        "bicarbonate buffer",
    ]
    if any(kw in all_text for kw in buffer_keywords):
        return "BUFFER_SOLUTION"

    # Mineral stock solutions
    if "stock" in all_text and any(
        kw in all_text for kw in ["mineral", "salt", "solution", "phosphate", "sulfate"]
    ):
        return "MINERAL_STOCK"

    # Cofactor mixes
    cofactor_keywords = ["cofactor", "coenzyme"]
    if any(kw in all_text for kw in cofactor_keywords) and (
        "solution" in all_text or "mix" in all_text
    ):
        return "COFACTOR_MIX"

    # Complex undefined media components
    complex_keywords = [
        "yeast extract",
        "peptone",
        "tryptone",
        "casein",
        "beef extract",
        "malt extract",
        "soil extract",
        "rumen fluid",
    ]
    if any(kw in all_text for kw in complex_keywords):
        return "COMPLEX_UNDEFINED"

    # Generic solution/mix indicators (only if not a pure chemical)
    if (
        ("solution" in preferred_term.lower() or "mix" in preferred_term.lower())
        and not any(
            pure in all_text
            for pure in ["nacl", "kcl", "mgso4", "cacl2", "h2o", "glucose", "sucrose"]
        )
        and len(preferred_term.split()) > 2
    ):  # Multi-word names more likely to be mixes
        return "OTHER"

    return None


def should_classify_ingredient(record: dict) -> bool:
    """Check if ingredient should be classified."""
    # Skip if already has solution_type
    if record.get("solution_type"):
        return False

    # Only classify mapped ingredients
    if record.get("mapping_status") != "MAPPED":
        return False

    return True


def main():
    """Main classification workflow."""
    print("=" * 80)
    print("PHASE 3: Classify Solution Types")
    print("=" * 80)

    # Process both mapped and unmapped ingredients
    for data_file, label in [
        ("data/curated/mapped_ingredients.yaml", "mapped"),
        ("data/curated/unmapped_ingredients.yaml", "unmapped"),
    ]:
        print(f"\n{'=' * 80}")
        print(f"Processing {label} ingredients...")
        print(f"{'=' * 80}")

        curator = IngredientCurator(
            data_path=Path(data_file), curator_name="classify_solution_types"
        )

        print(f"\nLoading ingredient records from {data_file}...")
        curator.load()
        total_records = len(curator.records)
        print(f"Loaded {total_records} records")

        # Classify solution types
        print("\nClassifying solution types...")
        classified_count = 0
        solution_type_counts = {}

        for i, record in enumerate(curator.records, 1):
            if i % 100 == 0:
                print(f"  Processed {i}/{total_records} ingredients...")

            if not should_classify_ingredient(record):
                continue

            preferred_term = record.get("preferred_term", "")
            synonyms = record.get("synonyms", [])

            solution_type = classify_solution_type(preferred_term, synonyms)
            if solution_type:
                curator.set_solution_type(record, solution_type)
                classified_count += 1
                solution_type_counts[solution_type] = solution_type_counts.get(solution_type, 0) + 1

        # Save results
        if curator.is_dirty:
            print(f"\nSaving updated {label} records...")
            curator.save()

        # Summary for this file
        print(f"\n{label.upper()} SUMMARY:")
        print(f"  Ingredients classified: {classified_count} ({classified_count/total_records*100:.1f}%)")

        if solution_type_counts:
            print(f"\n  Solution type distribution:")
            for sol_type, count in sorted(
                solution_type_counts.items(), key=lambda x: x[1], reverse=True
            ):
                print(f"    {sol_type:25s}: {count:4d}")

    print("\n" + "=" * 80)
    print("✅ Phase 3 complete! Solution types classified.")
    print("=" * 80)


if __name__ == "__main__":
    main()
