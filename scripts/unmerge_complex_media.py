#!/usr/bin/env python3
"""Unmerge incorrectly merged complex media entries.

This script finds complex media that were incorrectly merged with single ingredients
(e.g., "Oatmeal agar" merged into "Agar") and unmerges them.

Usage:
    python scripts/unmerge_complex_media.py --dry-run
    python scripts/unmerge_complex_media.py --interactive
    python scripts/unmerge_complex_media.py --auto-unmerge
"""

import argparse
import logging
import sys
from pathlib import Path

from rich.console import Console
from rich.panel import Panel
from rich.prompt import Confirm
from rich.table import Table

# Add src to path
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from mediaingredientmech.curation.ingredient_curator import IngredientCurator

# Import detection function
sys.path.insert(0, str(Path(__file__).parent))
from identify_complex_media import detect_complex_medium

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
logger = logging.getLogger(__name__)

console = Console()


def find_incorrectly_merged(curator: IngredientCurator) -> list[dict]:
    """Find complex media that were incorrectly merged.

    Args:
        curator: IngredientCurator instance.

    Returns:
        List of dicts with merged_record, representative_record, reason.
    """
    incorrect_merges = []
    id_to_record = {r.get("id"): r for r in curator.records if r.get("id")}

    for record in curator.records:
        # Only check REJECTED records with representative
        if record.get("mapping_status") != "REJECTED":
            continue

        representative_id = record.get("representative")
        if not representative_id:
            continue

        # Check if this is a complex medium
        preferred_term = record.get("preferred_term", "")
        ontology_id = record.get("ontology_mapping", {}).get("ontology_id")

        is_complex, confidence, reason = detect_complex_medium(preferred_term, ontology_id)

        if is_complex and confidence >= 0.75:
            representative = id_to_record.get(representative_id)
            if representative:
                incorrect_merges.append({
                    "merged_record": record,
                    "representative_record": representative,
                    "confidence": confidence,
                    "reason": reason,
                })

    return incorrect_merges


def unmerge_record(
    merged_record: dict,
    representative_record: dict,
    curator: IngredientCurator,
    dry_run: bool = True
) -> bool:
    """Unmerge a record from its representative.

    Args:
        merged_record: The merged (source) record to unmerge.
        representative_record: The representative (target) record.
        curator: IngredientCurator instance.
        dry_run: If True, don't actually modify records.

    Returns:
        True if unmerged, False if skipped.
    """
    merged_id = merged_record.get("id")
    representative_id = representative_record.get("id")
    merged_name = merged_record.get("preferred_term")
    representative_name = representative_record.get("preferred_term")

    if dry_run:
        logger.info(f"[DRY RUN] Would unmerge: {merged_name} from {representative_name}")
        return False

    # Remove from representative's merged list
    merged_list = representative_record.get("merged") or []
    if merged_id in merged_list:
        merged_list.remove(merged_id)
        if not merged_list:
            representative_record.pop("merged", None)
        else:
            representative_record["merged"] = merged_list

    # Remove representative from merged record
    merged_record.pop("representative", None)

    # Change status back to MAPPED or UNMAPPED
    original_ontology_id = merged_record.get("ontology_mapping", {}).get("ontology_id")
    if original_ontology_id and original_ontology_id.startswith("CHEBI:"):
        # Had a CHEBI mapping, but it's probably wrong for complex media
        curator.change_status(
            merged_record,
            "UNMAPPED",
            notes=f"Unmerged from {representative_name}. Complex media should not be mapped to pure chemical CHEBI terms."
        )
        merged_record["ontology_mapping"] = None
        merged_record["identifier"] = f"UNMAPPED_{merged_id.split(':')[-1]}"
    else:
        curator.change_status(
            merged_record,
            "UNMAPPED",
            notes=f"Unmerged from {representative_name}. Needs proper classification as DEFINED_MEDIUM."
        )

    # Set ingredient_type
    merged_record["ingredient_type"] = "DEFINED_MEDIUM"

    # Add curation event to representative
    from datetime import datetime, timezone
    representative_record.setdefault("curation_history", []).append({
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "curator": curator.curator_name,
        "action": "CORRECTED",
        "changes": f"Unmerged {merged_id} ({merged_name}) - was incorrectly merged complex medium",
    })

    logger.info(f"Unmerged: {merged_name} from {representative_name}")
    curator._dirty = True

    return True


def display_incorrect_merges(incorrect_merges: list[dict]) -> None:
    """Display table of incorrectly merged records.

    Args:
        incorrect_merges: List of incorrect merge dicts.
    """
    console.print(f"\n[bold]Found {len(incorrect_merges)} Incorrectly Merged Complex Media[/bold]\n")

    table = Table(show_header=True, header_style="bold red")
    table.add_column("Complex Medium (Merged)", style="red", width=40)
    table.add_column("→ Representative", style="green", width=30)
    table.add_column("Confidence", justify="right")
    table.add_column("Reason", style="yellow", width=40)

    # Sort by representative, then by name
    sorted_merges = sorted(
        incorrect_merges,
        key=lambda x: (
            x["representative_record"].get("preferred_term", ""),
            x["merged_record"].get("preferred_term", "")
        )
    )

    for item in sorted_merges[:50]:  # Limit display
        merged_name = item["merged_record"].get("preferred_term", "")
        rep_name = item["representative_record"].get("preferred_term", "")
        confidence = item["confidence"]
        reason = item["reason"]

        table.add_row(
            merged_name,
            rep_name,
            f"{confidence:.2f}",
            reason[:40] + "..." if len(reason) > 40 else reason
        )

    console.print(table)

    if len(sorted_merges) > 50:
        console.print(f"\n[dim]... and {len(sorted_merges) - 50} more[/dim]")


def main():
    """Main workflow."""
    parser = argparse.ArgumentParser(
        description="Unmerge incorrectly merged complex media"
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
        "--auto-unmerge",
        action="store_true",
        help="Automatically unmerge all detected incorrect merges"
    )
    parser.add_argument(
        "--confidence-threshold",
        type=float,
        default=0.85,
        help="Minimum confidence for auto-unmerge (default: 0.85)"
    )

    args = parser.parse_args()

    # Load data
    console.print(f"\n[bold]Loading ingredients from {args.data_path}[/bold]")
    curator = IngredientCurator(data_path=args.data_path)
    curator.load()
    console.print(f"Loaded {len(curator.records)} ingredient records\n")

    # Find incorrect merges
    console.print("[bold cyan]Searching for incorrectly merged complex media...[/bold cyan]")
    incorrect_merges = find_incorrectly_merged(curator)

    if not incorrect_merges:
        console.print("[green]✓ No incorrectly merged complex media found![/green]")
        return 0

    # Display findings
    display_incorrect_merges(incorrect_merges)

    # Auto-unmerge mode
    if args.auto_unmerge:
        console.print(f"\n[bold]Auto-unmerging entries with confidence >= {args.confidence_threshold}[/bold]")

        unmerged = 0
        for item in incorrect_merges:
            if item["confidence"] >= args.confidence_threshold:
                if unmerge_record(
                    item["merged_record"],
                    item["representative_record"],
                    curator,
                    args.dry_run
                ):
                    unmerged += 1

        console.print(f"\n{'[DRY RUN] Would unmerge' if args.dry_run else 'Unmerged'}: {unmerged} records")

    # Interactive mode
    elif args.interactive:
        console.print("\n[bold]Interactive Review Mode[/bold]")
        console.print("Review and unmerge incorrectly merged complex media\n")

        unmerged = 0
        for item in incorrect_merges[:30]:  # Limit to first 30
            merged_rec = item["merged_record"]
            rep_rec = item["representative_record"]

            console.print(Panel(
                f"[bold red]{merged_rec.get('preferred_term')}[/bold red]\n"
                f"  Currently merged into: [green]{rep_rec.get('preferred_term')}[/green]\n"
                f"  Confidence: {item['confidence']:.2f}\n"
                f"  Reason: {item['reason']}",
                title="Incorrect Merge",
                border_style="red"
            ))

            if Confirm.ask("Unmerge this complex medium?"):
                if unmerge_record(merged_rec, rep_rec, curator, args.dry_run):
                    unmerged += 1

            if not Confirm.ask("Continue to next?"):
                break

        console.print(f"\n{'[DRY RUN] Would unmerge' if args.dry_run else 'Unmerged'}: {unmerged} records")

    # Save if not dry run
    if not args.dry_run and (args.auto_unmerge or args.interactive):
        if curator.is_dirty:
            console.print(f"\n[bold green]Saving changes to {args.data_path}[/bold green]")
            curator.save()
            console.print("[green]✓ Saved successfully[/green]")

            # Validate merge integrity
            is_valid, errors = curator.validate_merge_integrity()
            if is_valid:
                console.print("[green]✓ Merge integrity validation passed[/green]")
            else:
                console.print(f"[yellow]⚠ {len(errors)} merge integrity warnings:[/yellow]")
                for error in errors[:5]:
                    console.print(f"  • {error}")
        else:
            console.print("\n[yellow]No changes to save[/yellow]")
    elif args.dry_run:
        console.print("\n[yellow]DRY RUN: No changes saved[/yellow]")
    else:
        console.print("\n[yellow]Use --auto-unmerge or --interactive to unmerge records[/yellow]")

    return 0


if __name__ == "__main__":
    sys.exit(main())
