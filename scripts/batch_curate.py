#!/usr/bin/env python3
"""
Batch Ingredient Curation - Non-Interactive Mode

Programmatically curates unmapped ingredients using LLMCurator with
auto-acceptance based on confidence threshold.

This script enables automated pipeline integration while using the same
proven LLMCurator logic as the interactive CLI.
"""

import sys
import os
from pathlib import Path
import click
import yaml
from datetime import datetime
from typing import List, Dict, Any, Optional

# Add src to path
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from mediaingredientmech.utils.llm_curator import LLMCurator, LLMSuggestion, validate_llm_suggestion
from mediaingredientmech.utils.ontology_client import OntologyCandidate
from mediaingredientmech.curation.ingredient_curator import IngredientCurator

# Try to import OntologyClient (may not be available)
try:
    from mediaingredientmech.utils.ontology_client import OntologyClient
    OAK_AVAILABLE = True
except Exception:
    OAK_AVAILABLE = False
    OntologyClient = None


@click.command()
@click.option(
    "--batch-size",
    type=int,
    default=10,
    help="Maximum number of ingredients to process",
)
@click.option(
    "--auto-accept-threshold",
    type=float,
    default=0.9,
    help="Confidence threshold for auto-acceptance (0.0-1.0)",
)
@click.option(
    "--min-occurrences",
    type=int,
    default=1,
    help="Only process ingredients with >= this many occurrences",
)
@click.option(
    "--dry-run",
    is_flag=True,
    help="Simulate execution without saving changes",
)
@click.option(
    "--data-path",
    type=click.Path(exists=True),
    default=None,
    help="Path to unmapped ingredients YAML file",
)
@click.option(
    "--curator",
    type=str,
    default="batch_curator_automated",
    help="Curator name for audit trail",
)
@click.option(
    "--sources",
    type=str,
    default="CHEBI,FOODON,ENVO,NCIT,MESH,UBERON",
    help="Comma-separated ontology sources",
)
@click.option(
    "--verbose",
    is_flag=True,
    help="Show detailed output",
)
def batch_curate(
    batch_size: int,
    auto_accept_threshold: float,
    min_occurrences: int,
    dry_run: bool,
    data_path: Optional[str],
    curator: str,
    sources: str,
    verbose: bool,
):
    """
    Batch curate unmapped ingredients with LLM assistance.

    This script processes unmapped ingredients in batch mode, automatically
    accepting high-confidence mappings and skipping low-confidence ones.

    Example:
        python batch_curate.py --batch-size 10 --auto-accept-threshold 0.9
    """
    click.echo("=" * 70)
    click.echo("Batch Ingredient Curation - Non-Interactive Mode")
    click.echo("=" * 70)
    click.echo(f"Batch size: {batch_size}")
    click.echo(f"Auto-accept threshold: {auto_accept_threshold}")
    click.echo(f"Min occurrences: {min_occurrences}")
    click.echo(f"Dry run: {dry_run}")
    click.echo(f"Curator: {curator}")
    click.echo(f"OAK available: {OAK_AVAILABLE}")
    click.echo()

    # Initialize curator
    if not data_path:
        data_path = Path(__file__).parent.parent / "data" / "curated" / "unmapped_ingredients.yaml"

    ingredient_curator = IngredientCurator(data_path=data_path)
    ingredient_curator.load()

    # Initialize LLM curator
    llm_curator = LLMCurator(
        model="claude-sonnet-4-20250514",
    )

    # Initialize OntologyClient if available
    ontology_client = None
    if OAK_AVAILABLE:
        try:
            ontology_sources = sources.split(",")
            ontology_client = OntologyClient(sources=ontology_sources)
            click.echo(f"✓ OntologyClient initialized with sources: {', '.join(ontology_sources)}")
        except Exception as e:
            click.echo(f"⚠ Failed to initialize OntologyClient: {e}")
            click.echo("  Continuing without real-time ontology validation")
    else:
        click.echo("⚠ OAK not available, skipping real-time ontology validation")

    click.echo()

    # Get unmapped ingredients
    unmapped = ingredient_curator.get_unmapped()

    # Filter by occurrences
    if min_occurrences > 1:
        unmapped = [
            record for record in unmapped
            if record.get("occurrence_statistics", {}).get("total_occurrences", 0) >= min_occurrences
        ]
        click.echo(f"Filtered to {len(unmapped)} ingredients with >= {min_occurrences} occurrences")

    # Limit batch size
    total_available = len(unmapped)
    unmapped = unmapped[:batch_size]

    click.echo(f"Processing {len(unmapped)} of {total_available} unmapped ingredients")
    click.echo()

    # Process each ingredient
    results = {
        "processed": 0,
        "auto_accepted": 0,
        "skipped_low_confidence": 0,
        "skipped_no_suggestion": 0,
        "failed": 0,
        "total_cost": 0.0,
        "suggestions": [],
    }

    for idx, record in enumerate(unmapped, 1):
        ingredient_name = record.get("preferred_term", "Unknown")
        occurrences = record.get("occurrence_statistics", {}).get("total_occurrences", 0)

        click.echo(f"[{idx}/{len(unmapped)}] {ingredient_name} ({occurrences} occurrences)")

        try:
            # Build context
            context = {
                "occurrences": occurrences,
                "media_count": record.get("occurrence_statistics", {}).get("media_count", 0),
                "synonyms": [s.get("synonym_text", "") for s in record.get("synonyms", [])[:3]],
            }

            # Get LLM suggestion
            if verbose:
                click.echo(f"  Requesting LLM suggestion...")

            suggestion: LLMSuggestion = llm_curator.suggest_mapping(ingredient_name, context)

            if suggestion is None:
                click.echo(f"  ⊘ No suggestion from LLM")
                results["skipped_no_suggestion"] += 1
                results["processed"] += 1
                continue

            # Track cost
            if hasattr(suggestion, 'cost_usd'):
                results["total_cost"] += suggestion.cost_usd

            confidence = suggestion.confidence
            ontology_id = suggestion.ontology_id
            label = suggestion.label
            reasoning = suggestion.reasoning

            if verbose:
                click.echo(f"  Suggestion: {ontology_id} - {label}")
                click.echo(f"  Confidence: {confidence:.2f}")
                click.echo(f"  Reasoning: {reasoning[:100]}...")

            # Validate if OntologyClient available
            is_valid = True
            validation_error = None

            if ontology_client:
                is_valid, validation_error = validate_llm_suggestion(suggestion, ontology_client)
                if not is_valid:
                    click.echo(f"  ⚠ Validation failed: {validation_error}")
                    results["failed"] += 1
                    results["processed"] += 1
                    continue

            # Auto-accept if above threshold
            if confidence >= auto_accept_threshold:
                click.echo(f"  ✓ AUTO-ACCEPTED: {ontology_id} ({confidence:.2f} >= {auto_accept_threshold:.2f})")

                if not dry_run:
                    # Create mapping candidate (OntologyCandidate dataclass —
                    # this is what accept_mapping expects, not a dict).
                    candidate = OntologyCandidate(
                        ontology_id=ontology_id,
                        label=label,
                        source=suggestion.source,
                        score=confidence,
                    )

                    # Accept the mapping. accept_mapping's signature has no
                    # `curator_id` parameter; the curator identity is set on
                    # the IngredientCurator instance itself. Reasoning is
                    # captured via `notes`.
                    ingredient_curator.accept_mapping(
                        record,
                        candidate,
                        quality="LLM_ASSISTED",
                        match_level="MANUAL",
                        llm_assisted=True,
                        notes=(
                            f"Auto-accepted by {curator}: confidence "
                            f"{confidence:.2f} >= threshold {auto_accept_threshold:.2f}"
                            + (f". Reasoning: {reasoning}" if reasoning else "")
                        ),
                    )

                results["auto_accepted"] += 1

                # Store suggestion details
                results["suggestions"].append({
                    "ingredient": ingredient_name,
                    "ontology_id": ontology_id,
                    "label": label,
                    "confidence": confidence,
                    "action": "auto_accepted",
                })

            else:
                click.echo(f"  ⊘ SKIPPED: Confidence {confidence:.2f} < {auto_accept_threshold:.2f}")
                results["skipped_low_confidence"] += 1

                # Store suggestion for potential manual review
                results["suggestions"].append({
                    "ingredient": ingredient_name,
                    "ontology_id": ontology_id,
                    "label": label,
                    "confidence": confidence,
                    "action": "skipped_low_confidence",
                })

            results["processed"] += 1

        except Exception as e:
            click.echo(f"  ✗ ERROR: {e}")
            results["failed"] += 1
            results["processed"] += 1

        click.echo()

    # Save if not dry run
    if not dry_run and results["auto_accepted"] > 0:
        click.echo("Saving changes...")
        ingredient_curator.save()
        click.echo(f"✓ Saved {results['auto_accepted']} accepted mappings")
    elif dry_run:
        click.echo("DRY RUN: No changes saved")

    click.echo()
    click.echo("=" * 70)
    click.echo("Batch Curation Complete")
    click.echo("=" * 70)
    click.echo(f"Processed: {results['processed']}/{len(unmapped)}")
    click.echo(f"Auto-accepted: {results['auto_accepted']}")
    click.echo(f"Skipped (low confidence): {results['skipped_low_confidence']}")
    click.echo(f"Skipped (no suggestion): {results['skipped_no_suggestion']}")
    click.echo(f"Failed: {results['failed']}")
    click.echo(f"Total cost: ${results['total_cost']:.4f}")
    click.echo()

    # Write report
    report_dir = Path(__file__).parent.parent / "reports" / "batch_curation"
    report_dir.mkdir(parents=True, exist_ok=True)

    report_file = report_dir / f"batch_curation_{datetime.now().strftime('%Y%m%d_%H%M%S')}.yaml"

    report = {
        "timestamp": datetime.now().isoformat(),
        "parameters": {
            "batch_size": batch_size,
            "auto_accept_threshold": auto_accept_threshold,
            "min_occurrences": min_occurrences,
            "dry_run": dry_run,
            "curator": curator,
            "sources": sources,
        },
        "results": results,
    }

    with open(report_file, 'w') as f:
        yaml.dump(report, f, default_flow_style=False, sort_keys=False)

    click.echo(f"Report saved: {report_file}")
    click.echo()

    # Exit code based on success
    if results["failed"] > 0:
        sys.exit(1)
    else:
        sys.exit(0)


if __name__ == "__main__":
    batch_curate()
