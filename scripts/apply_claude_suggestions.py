#!/usr/bin/env python3
"""Apply reviewed LLM curation suggestions to unmapped ingredients.

The input is validated completely before any record is mutated. Each accepted
mapping is built on a copy and committed to the in-memory collection only after
all mapping and enrichment work for that record succeeds.
"""

from __future__ import annotations

import sys
from collections.abc import Callable, Mapping
from copy import deepcopy
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import click
import yaml
from rich.console import Console
from rich.table import Table

# Add src to path
_project_root = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(_project_root / "src"))

from mediaingredientmech.curation.hydrate_guard import HydrateMismatch  # noqa: E402
from mediaingredientmech.curation.ingredient_curator import (  # noqa: E402
    VALID_MATCH_LEVEL,
    VALID_QUALITY,
    IngredientCurator,
)
from mediaingredientmech.utils.chemical_normalizer import normalize_chemical_name  # noqa: E402
from mediaingredientmech.utils.ontology_client import (  # noqa: E402
    OntologyCandidate,
    OntologyClient,
)

console = Console()


class SuggestionValidationError(ValueError):
    """Raised when a suggestion document does not match the importer schema."""


@dataclass(frozen=True)
class MappingSuggestion:
    """Validated, provider-neutral mapping suggestion."""

    identifier: str
    name: str
    ontology_id: str | None
    ontology_label: str | None
    ontology_source: str | None
    confidence: float
    reasoning: str
    quality: str
    match_level: str

    @classmethod
    def from_mapping(cls, raw: Mapping[str, Any], index: int | None = None) -> MappingSuggestion:
        """Validate and normalize one YAML mapping into the typed model."""
        location = f"suggestions[{index}]" if index is not None else "suggestion"

        identifier = raw.get("identifier")
        if not isinstance(identifier, str) or not identifier.strip():
            raise SuggestionValidationError(f"{location}.identifier must be a non-empty string")

        name = raw.get("name", "")
        if not isinstance(name, str):
            raise SuggestionValidationError(f"{location}.name must be a string")

        quality = raw.get("quality", "LLM_ASSISTED")
        if not isinstance(quality, str) or quality not in VALID_QUALITY | {"UNMAPPABLE"}:
            allowed = ", ".join(sorted(VALID_QUALITY | {"UNMAPPABLE"}))
            raise SuggestionValidationError(f"{location}.quality must be one of: {allowed}")

        match_level = raw.get("match_level", "MANUAL")
        if not isinstance(match_level, str) or match_level not in VALID_MATCH_LEVEL:
            allowed = ", ".join(sorted(VALID_MATCH_LEVEL))
            raise SuggestionValidationError(f"{location}.match_level must be one of: {allowed}")

        confidence = raw.get("confidence", 0.0)
        if isinstance(confidence, bool) or not isinstance(confidence, (int, float)):
            raise SuggestionValidationError(f"{location}.confidence must be a number from 0 to 1")
        confidence = float(confidence)
        if not 0.0 <= confidence <= 1.0:
            raise SuggestionValidationError(f"{location}.confidence must be a number from 0 to 1")

        reasoning = raw.get("reasoning", "")
        if not isinstance(reasoning, str):
            raise SuggestionValidationError(f"{location}.reasoning must be a string")

        ontology_id = raw.get("ontology_id")
        ontology_label = raw.get("ontology_label")
        ontology_source = raw.get("ontology_source")
        unmappable = quality == "UNMAPPABLE" or ontology_id is None
        if unmappable:
            if ontology_id is not None and quality == "UNMAPPABLE":
                raise SuggestionValidationError(
                    f"{location}.ontology_id must be null when quality is UNMAPPABLE"
                )
            ontology_id = None
            ontology_label = None
            ontology_source = None
        else:
            for field_name, value in (
                ("ontology_id", ontology_id),
                ("ontology_label", ontology_label),
                ("ontology_source", ontology_source),
            ):
                if not isinstance(value, str) or not value.strip():
                    raise SuggestionValidationError(
                        f"{location}.{field_name} must be a non-empty string for a mapping"
                    )
            ontology_source = ontology_source.upper()
            if ":" not in ontology_id:
                raise SuggestionValidationError(
                    f"{location}.ontology_id must be a CURIE such as CHEBI:26710"
                )
            if ontology_id.split(":", 1)[0].upper() != ontology_source:
                raise SuggestionValidationError(
                    f"{location}.ontology_source must match the ontology_id prefix"
                )

        return cls(
            identifier=identifier.strip(),
            name=name,
            ontology_id=ontology_id,
            ontology_label=ontology_label,
            ontology_source=ontology_source,
            confidence=confidence,
            reasoning=reasoning,
            quality=quality,
            match_level=match_level,
        )


def load_suggestions(suggestions_file: Path) -> list[MappingSuggestion]:
    """Load and validate the complete suggestion document before mutation."""
    with open(suggestions_file, encoding="utf-8") as stream:
        data = yaml.safe_load(stream)

    if not isinstance(data, Mapping):
        raise SuggestionValidationError("suggestion document must be a YAML mapping")
    raw_suggestions = data.get("suggestions")
    if not isinstance(raw_suggestions, list):
        raise SuggestionValidationError("suggestion document must contain a suggestions list")

    suggestions: list[MappingSuggestion] = []
    for index, raw in enumerate(raw_suggestions):
        if not isinstance(raw, Mapping):
            raise SuggestionValidationError(f"suggestions[{index}] must be a mapping")
        suggestions.append(MappingSuggestion.from_mapping(raw, index))
    return suggestions


def _validated_suggestion(suggestion: MappingSuggestion | Mapping[str, Any]) -> MappingSuggestion:
    if isinstance(suggestion, MappingSuggestion):
        return suggestion
    return MappingSuggestion.from_mapping(suggestion)


def _validate_ontology_term(ontology_source: str, ontology_id: str) -> str | None:
    """Return the authoritative ontology label, or None when the term is absent."""
    from oaklib import get_adapter

    resource_map = {
        "CHEBI": "sqlite:obo:chebi",
        "FOODON": "sqlite:obo:foodon",
        "ENVO": "sqlite:obo:envo",
    }
    resource = resource_map.get(ontology_source)
    if not resource:
        raise ValueError(f"Unknown ontology source: {ontology_source}")
    return get_adapter(resource).label(ontology_id)


def _deduplicate_synonyms(record: dict[str, Any]) -> None:
    """Keep the first synonym for each case-insensitive synonym text."""
    synonyms = record.get("synonyms") or []
    unique: list[Any] = []
    seen: set[str] = set()
    for synonym in synonyms:
        if not isinstance(synonym, Mapping):
            unique.append(synonym)
            continue
        text = synonym.get("synonym_text")
        if not isinstance(text, str):
            unique.append(synonym)
            continue
        key = text.strip().casefold()
        if key in seen:
            continue
        seen.add(key)
        unique.append(synonym)
    if unique or "synonyms" in record:
        record["synonyms"] = unique


def _print_post_save_guidance(data_path: Path) -> None:
    """Explain collection promotion, SSSOM publication, and synchronization."""
    canonical_unmapped = _project_root / "data" / "curated" / "unmapped_ingredients.yaml"
    if data_path.resolve() == canonical_unmapped.resolve():
        console.print(
            "[yellow]Newly mapped records are still in the unmapped collection. "
            "`just sync-individual` alone would preserve that wrong placement and does not "
            "publish their SSSOM rows. Run this sequence:[/yellow]\n"
            "  1. `python scripts/move_mapped_out_of_unmapped_collection.py` (preview)\n"
            "  2. `python scripts/move_mapped_out_of_unmapped_collection.py --apply`\n"
            "  3. `just sync-individual`\n"
            "  4. `just qc`"
        )
        return

    console.print(
        "[yellow]This command edited a non-default collection. Verify mapped/unmapped "
        "placement and update SSSOM before running `just sync-individual`, then run "
        "`just qc`.[/yellow]"
    )


def apply_suggestion(
    suggestion: MappingSuggestion | Mapping[str, Any],
    curator: IngredientCurator,
    ontology_client: OntologyClient,
    validate: bool = True,
    auto_enrich: bool = True,
    provider: str = "llm",
    model: str | None = None,
    term_validator: Callable[[str, str], str | None] = _validate_ontology_term,
) -> tuple[bool, str]:
    """Apply a single suggestion.

    Returns:
        Tuple of (success, message)
    """
    try:
        suggestion = _validated_suggestion(suggestion)
    except SuggestionValidationError as exc:
        return False, f"Invalid suggestion: {exc}"

    # `identifier` here is the EXISTING unmapped record's primary key
    # (e.g. `UNMAPPED_0001`), used to find the record below. `ontology_id`
    # is the PROPOSED mapping target (e.g. `CHEBI:26710`). These are two
    # different fields on the suggestion document.
    identifier = suggestion.identifier
    ontology_id = suggestion.ontology_id
    ontology_label = suggestion.ontology_label
    ontology_source = suggestion.ontology_source

    # Skip unmappable ingredients
    if ontology_id is None or suggestion.quality == "UNMAPPABLE":
        return False, "Unmappable (skipped)"

    # Find the record
    record_index = None
    for index, rec in enumerate(curator.records):
        if (rec.get("identifier") or rec.get("ontology_id")) == identifier:
            record_index = index
            break

    if record_index is None:
        return False, f"Record {identifier} not found"

    # Validate ontology term if requested
    if validate:
        try:
            label = term_validator(ontology_source, ontology_id)

            if not label:
                return False, f"Term {ontology_id} not found in {ontology_source}"

            # Update label if different
            if label.casefold() != ontology_label.casefold():
                console.print(
                    f"[yellow]Label mismatch for {ontology_id}: "
                    f"suggested '{ontology_label}', actual '{label}'[/yellow]"
                )
                ontology_label = label

        except Exception as e:
            return False, f"Validation error: {e}"

    # Build and mutate a private copy. Nothing in the collection is changed
    # until the complete per-record operation succeeds.
    original_record = curator.records[record_index]
    record = deepcopy(original_record)
    dirty_before = curator.is_dirty
    candidate = OntologyCandidate(
        ontology_id=ontology_id,
        label=ontology_label,
        source=ontology_source,
        score=suggestion.confidence,
        synonyms=[],
        definition=None,
    )

    # Apply mapping
    try:
        curator.accept_mapping(
            record,
            candidate,
            quality=suggestion.quality,
            match_level=suggestion.match_level,
            llm_assisted=True,
            llm_model=f"{provider}:{model}" if model else provider,
            notes=f"{provider} reasoning: {suggestion.reasoning}",
            auto_enrich=auto_enrich,
        )

        # Add original form as synonym if normalized
        original_name = record.get("preferred_term", "")
        norm_result = normalize_chemical_name(original_name)

        if norm_result.applied_rules and norm_result.normalized != original_name:
            if not isinstance(record.get("synonyms"), list):
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
                    "source": f"{provider}_curation",
                    "notes": f"Original form before normalization: {', '.join(norm_result.applied_rules)}",
                }
            )

        _deduplicate_synonyms(record)
        curator.records[record_index] = record

        return True, f"Mapped to {ontology_id} ({ontology_label})"

    except HydrateMismatch as exc:
        curator._dirty = dirty_before
        # #243: a refusal is a decision, not an error — say so distinctly.
        return False, f"REFUSED (hydrate label onto a non-hydrate term): {exc}"
    except Exception as e:
        curator._dirty = dirty_before
        return False, f"Error applying mapping: {e}"


@click.command()
@click.option(
    "--suggestions",
    type=click.Path(path_type=Path),
    required=True,
    help="YAML file with reviewed mapping suggestions",
)
@click.option(
    "--data-path",
    type=click.Path(path_type=Path),
    default=Path("data/curated/unmapped_ingredients.yaml"),
    help="Path to unmapped ingredients YAML",
)
@click.option(
    "--curator",
    default="llm_assisted",
    help="Curator name for audit trail",
)
@click.option(
    "--provider",
    default="llm",
    show_default=True,
    help="Suggestion provider recorded in provenance (for example openai or anthropic)",
)
@click.option(
    "--model",
    default=None,
    help="Optional model identifier recorded in provenance",
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
    provider: str,
    model: str | None,
    skip_validation: bool,
    dry_run: bool,
) -> None:
    """Apply reviewed LLM suggestions to unmapped ingredients."""
    provider = provider.strip()
    if not provider:
        raise click.UsageError("--provider must be a non-empty string")
    console.print("[bold]Applying reviewed LLM suggestions...[/bold]\n")

    if dry_run:
        console.print(
            "[yellow]DRY RUN MODE - no files, ontology downloads, or enrichment caches "
            "will be changed[/yellow]\n"
        )

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
        identifier = suggestion.identifier
        name = suggestion.name or "?"
        ontology_id = suggestion.ontology_id
        ontology_label = suggestion.ontology_label

        success, message = apply_suggestion(
            suggestion,
            ingredient_curator,
            ontology_client,
            validate=not skip_validation and not dry_run,
            auto_enrich=not dry_run,
            provider=provider,
            model=model,
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
        _print_post_save_guidance(data_path)
    elif dry_run:
        console.print("\n[dim]Dry run - no changes saved[/dim]")


if __name__ == "__main__":
    main()
