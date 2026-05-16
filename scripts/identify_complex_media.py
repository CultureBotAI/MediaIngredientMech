#!/usr/bin/env python3
"""Identify and reclassify complex media entries that are actually medium formulations.

This script detects ingredients that are likely complete media recipes rather than
single chemical ingredients, particularly focusing on entries mapped to CHEBI:2509 (agar)
that are actually complex agar-based media.

Usage:
    python scripts/identify_complex_media.py --dry-run
    python scripts/identify_complex_media.py --interactive
    python scripts/identify_complex_media.py --auto-reclassify --confidence-threshold 0.9
"""

import argparse
import logging
import re
import sys
from pathlib import Path
from typing import Any, Optional

from rich.console import Console
from rich.panel import Panel
from rich.prompt import Confirm, Prompt
from rich.table import Table

# Add src to path
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from mediaingredientmech.curation.ingredient_curator import IngredientCurator

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
logger = logging.getLogger(__name__)

console = Console()

# Patterns that strongly suggest a defined medium (not a single ingredient)
MEDIUM_NAME_PATTERNS = [
    # Agar-based media (most common issue)
    r"(?i)\b(marine|r2a|corn meal|oatmeal|brucella|fastidious|mueller hinton|columbia|brewer)\s+agar\b",
    r"(?i)\b(malt extract|glycerol-asparagine|inorganic salts-starch)\s+agar\b",
    r"(?i)\b(middlebrook|bcye|gam|czapek dox)\s+agar\b",
    r"(?i)\blegionella\s+agar\s+enrichment\b",
    r"(?i)\b(blood|chocolate)\s+agar\b",

    # Broth-based media
    r"(?i)\b(lb|luria|nutrient|tryptic soy|brain heart infusion)\s+broth\b",
    r"(?i)\b(mueller hinton|thioglycollate)\s+broth\b",

    # Named media with numbers/codes
    r"(?i)\b(marine|nutrient|tryptic soy)\s+agar\s+\d+\b",  # e.g., "Marine agar 2216"
    r"(?i)\b(middlebrook|m|r)\s*\d{1,2}(h)?\d{0,2}\b",  # e.g., "Middlebrook 7H10"

    # Medium types
    r"(?i)\b(minimal|selective|differential|enrichment)\s+(medium|media|agar)\b",

    # Base/powder indicators (less certain)
    r"(?i)\b(agar|broth)\s+(base|powder|mix)\b",
]

# Specific known medium names
KNOWN_MEDIA = {
    "R2A agar", "Marine agar 2216", "LB agar", "TSA", "Nutrient agar",
    "Middlebrook 7H10 agar", "Middlebrook 7H11 agar", "BCYE agar",
    "Mueller Hinton agar", "MacConkey agar", "EMB agar",
    "Corn meal agar", "Oatmeal agar", "Malt extract agar",
    "Blood agar", "Chocolate agar", "Columbia blood agar",
    "Brucella agar", "Fastidious Anaerobe Agar", "GAM agar",
    "Brewer anaerobic agar", "Czapek Dox agar",
}

# Patterns that suggest single ingredient (to avoid false positives)
SINGLE_INGREDIENT_PATTERNS = [
    r"^agar$",  # Just "agar"
    r"^agar\s*$",
    r"^purified agar$",
    r"^bacteriological agar$",
]


def detect_complex_medium(preferred_term: str, ontology_id: Optional[str] = None) -> tuple[bool, float, str]:
    """Detect if an ingredient is likely a complex defined medium.

    Args:
        preferred_term: The ingredient name.
        ontology_id: Optional ontology ID (e.g., CHEBI:2509).

    Returns:
        Tuple of (is_complex_medium, confidence, reason).
    """
    term_lower = preferred_term.lower().strip()

    # First check if it's definitely a single ingredient
    for pattern in SINGLE_INGREDIENT_PATTERNS:
        if re.match(pattern, term_lower):
            return False, 1.0, "Single ingredient pattern match"

    # Check known media names (high confidence)
    if preferred_term in KNOWN_MEDIA or term_lower in {m.lower() for m in KNOWN_MEDIA}:
        return True, 0.95, f"Known medium name: {preferred_term}"

    # Check patterns (medium confidence)
    for pattern in MEDIUM_NAME_PATTERNS:
        if re.search(pattern, preferred_term):
            return True, 0.85, f"Medium pattern match: {pattern}"

    # Special case: anything containing "agar" + another word (but not just "agar")
    if ontology_id == "CHEBI:2509":  # Agar
        words = term_lower.split()
        if "agar" in words and len(words) > 1:
            # Check if other words suggest a medium
            other_words = [w for w in words if w not in ("agar", "bacto", "bacteriological", "purified")]
            if other_words:
                return True, 0.75, f"CHEBI:2509 (agar) with additional terms: {other_words}"

    return False, 0.0, "No complex medium indicators"


def analyze_ingredients(curator: IngredientCurator) -> dict[str, list[dict]]:
    """Analyze all ingredients and categorize them.

    Returns:
        Dict with categories:
        - complex_media_high: High confidence complex media
        - complex_media_medium: Medium confidence
        - single_ingredients: Likely single ingredients
        - uncertain: Unclear classification
    """
    results = {
        "complex_media_high": [],
        "complex_media_medium": [],
        "single_ingredients": [],
        "uncertain": [],
    }

    for idx, record in enumerate(curator.records):
        # Skip already rejected
        if record.get("mapping_status") == "REJECTED":
            continue

        # Skip if already classified
        if record.get("ingredient_type"):
            continue

        preferred_term = record.get("preferred_term", "")
        ontology_id = record.get("ontology_mapping", {}).get("ontology_id")

        is_complex, confidence, reason = detect_complex_medium(preferred_term, ontology_id)

        entry = {
            "index": idx,
            "record": record,
            "confidence": confidence,
            "reason": reason,
        }

        if is_complex and confidence >= 0.85:
            results["complex_media_high"].append(entry)
        elif is_complex and confidence >= 0.70:
            results["complex_media_medium"].append(entry)
        elif not is_complex and confidence >= 0.9:
            results["single_ingredients"].append(entry)
        else:
            results["uncertain"].append(entry)

    return results


def display_analysis_summary(results: dict[str, list[dict]]) -> None:
    """Display summary of analysis results."""
    console.print("\n[bold]Complex Media Detection Summary[/bold]\n")

    table = Table(title="Classification Results")
    table.add_column("Category", style="cyan")
    table.add_column("Count", justify="right", style="magenta")
    table.add_column("Action", style="yellow")

    table.add_row(
        "Complex Media (High Confidence)",
        str(len(results["complex_media_high"])),
        "Auto-reclassify or review"
    )
    table.add_row(
        "Complex Media (Medium Confidence)",
        str(len(results["complex_media_medium"])),
        "Manual review recommended"
    )
    table.add_row(
        "Single Ingredients",
        str(len(results["single_ingredients"])),
        "No action needed"
    )
    table.add_row(
        "Uncertain",
        str(len(results["uncertain"])),
        "Manual review"
    )

    console.print(table)


def display_complex_media_details(entries: list[dict], max_display: int = 50) -> None:
    """Display detailed list of detected complex media."""
    if not entries:
        return

    console.print(f"\n[bold]Detected Complex Media ({len(entries)} total)[/bold]\n")

    table = Table(show_header=True, header_style="bold cyan")
    table.add_column("Name", style="green", width=50)
    table.add_column("CHEBI ID", style="cyan")
    table.add_column("Confidence", justify="right")
    table.add_column("Reason", style="yellow", width=40)

    # Sort by confidence descending
    sorted_entries = sorted(entries, key=lambda x: x["confidence"], reverse=True)

    for entry in sorted_entries[:max_display]:
        record = entry["record"]
        name = record.get("preferred_term", "")
        ontology_id = record.get("ontology_mapping", {}).get("ontology_id", "N/A")
        confidence = entry["confidence"]
        reason = entry["reason"]

        table.add_row(
            name,
            ontology_id,
            f"{confidence:.2f}",
            reason[:40] + "..." if len(reason) > 40 else reason
        )

    console.print(table)

    if len(sorted_entries) > max_display:
        console.print(f"\n[dim]... and {len(sorted_entries) - max_display} more[/dim]")


def reclassify_record(
    record: dict,
    curator: IngredientCurator,
    reason: str,
    dry_run: bool = True
) -> bool:
    """Reclassify a record as DEFINED_MEDIUM.

    Returns:
        True if reclassified, False if skipped.
    """
    if dry_run:
        logger.info(f"[DRY RUN] Would reclassify: {record.get('preferred_term')}")
        return False

    # Set ingredient_type
    record["ingredient_type"] = "DEFINED_MEDIUM"

    # Change status to UNMAPPED if currently mapped to wrong ontology
    current_status = record.get("mapping_status")
    ontology_id = record.get("ontology_mapping", {}).get("ontology_id")

    if ontology_id and ontology_id.startswith("CHEBI:"):
        # Complex media should not have CHEBI mappings (unless it's a specific case)
        curator.change_status(
            record,
            "UNMAPPED",
            notes=f"Reclassified as DEFINED_MEDIUM: {reason}. "
                  f"Previous CHEBI mapping inappropriate for complex medium."
        )
        # Clear ontology mapping
        record["ontology_mapping"] = None
        record["identifier"] = f"UNMAPPED_{record.get('id', 'UNKNOWN').split(':')[-1]}"
    else:
        # Just add note
        curator.add_note(
            record,
            f"Classified as DEFINED_MEDIUM: {reason}"
        )

    logger.info(f"Reclassified: {record.get('preferred_term')} → DEFINED_MEDIUM")
    return True


def main():
    """Main workflow."""
    parser = argparse.ArgumentParser(
        description="Identify and reclassify complex media ingredients"
    )
    parser.add_argument(
        "--data-path",
        type=Path,
        default=Path("data/curated/mapped_ingredients.yaml"),
        help="Path to ingredient data file",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Preview changes without saving"
    )
    parser.add_argument(
        "--interactive",
        action="store_true",
        help="Interactive review mode"
    )
    parser.add_argument(
        "--auto-reclassify",
        action="store_true",
        help="Automatically reclassify high-confidence complex media"
    )
    parser.add_argument(
        "--confidence-threshold",
        type=float,
        default=0.85,
        help="Minimum confidence for auto-reclassification (default: 0.85)"
    )
    parser.add_argument(
        "--report-only",
        action="store_true",
        help="Generate report without any reclassification"
    )

    args = parser.parse_args()

    # Load data
    console.print(f"\n[bold]Loading ingredients from {args.data_path}[/bold]")
    curator = IngredientCurator(data_path=args.data_path)
    curator.load()

    console.print(f"Loaded {len(curator.records)} ingredient records\n")

    # Analyze
    console.print("[bold cyan]Analyzing ingredients...[/bold cyan]")
    results = analyze_ingredients(curator)

    # Display summary
    display_analysis_summary(results)

    # Display high-confidence complex media
    if results["complex_media_high"]:
        display_complex_media_details(results["complex_media_high"])

    # Report only mode
    if args.report_only:
        console.print("\n[yellow]Report-only mode: No reclassification performed[/yellow]")
        return 0

    # Auto-reclassify mode
    if args.auto_reclassify:
        console.print(f"\n[bold]Auto-reclassifying entries with confidence >= {args.confidence_threshold}[/bold]")

        reclassified = 0
        for entry in results["complex_media_high"]:
            if entry["confidence"] >= args.confidence_threshold:
                if reclassify_record(entry["record"], curator, entry["reason"], args.dry_run):
                    reclassified += 1

        console.print(f"\n{'[DRY RUN] Would reclassify' if args.dry_run else 'Reclassified'}: {reclassified} records")

    # Interactive mode
    elif args.interactive:
        console.print("\n[bold]Interactive Review Mode[/bold]")
        console.print("Review high-confidence complex media detections\n")

        reclassified = 0
        for entry in results["complex_media_high"][:20]:  # Limit to first 20 in interactive
            record = entry["record"]
            console.print(Panel(
                f"[bold]{record.get('preferred_term')}[/bold]\n"
                f"CHEBI ID: {record.get('ontology_mapping', {}).get('ontology_id', 'N/A')}\n"
                f"Confidence: {entry['confidence']:.2f}\n"
                f"Reason: {entry['reason']}",
                title=f"Record {entry['index'] + 1}",
                border_style="cyan"
            ))

            if Confirm.ask("Reclassify as DEFINED_MEDIUM?"):
                if reclassify_record(entry["record"], curator, entry["reason"], args.dry_run):
                    reclassified += 1

            if not Confirm.ask("Continue to next?"):
                break

        console.print(f"\n{'[DRY RUN] Would reclassify' if args.dry_run else 'Reclassified'}: {reclassified} records")

    # Save if not dry run
    if not args.dry_run and (args.auto_reclassify or args.interactive):
        if curator.is_dirty:
            console.print(f"\n[bold green]Saving changes to {args.data_path}[/bold green]")
            curator.save()
            console.print("[green]✓ Saved successfully[/green]")
        else:
            console.print("\n[yellow]No changes to save[/yellow]")
    elif args.dry_run:
        console.print("\n[yellow]DRY RUN: No changes saved[/yellow]")

    return 0


if __name__ == "__main__":
    sys.exit(main())
