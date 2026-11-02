#!/usr/bin/env python3
"""Fill mechanically eligible empty chemistry blocks from exact ChEBI OLS terms.

Existing chemistry, mapping grades, ingredient types and identities are preserved.
No automatic cache/PubChem fallback or partial-block gap filling is permitted.
"""

from __future__ import annotations

import sys
from pathlib import Path

import click
import yaml
from rich.console import Console

_project_root = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(_project_root / "src"))

from mediaingredientmech.curate.curation_event import record_curation_event  # noqa: E402
from mediaingredientmech.curation.chemical_properties_guard import (  # noqa: E402
    chemistry_preflight,
    prepare_chemical_properties,
)
from mediaingredientmech.utils.yaml_handler import save_yaml  # noqa: E402
from mediaingredientmech.validation.write_validated import ValidationFailedError  # noqa: E402

console = Console()


def load_ingredients(yaml_path: Path) -> dict:
    """Load the collection without discarding its metadata."""
    with open(yaml_path) as stream:
        return yaml.safe_load(stream)


def filter_chebi_without_properties(data: dict | list) -> list[dict]:
    """Pure scope filter; grades do not grant or prohibit eligibility.

    All nonempty blocks, including CAS-only or provenance-only blocks, require
    explicit curation rather than adding fields under their existing provenance.
    """
    records = data.get("ingredients", []) if isinstance(data, dict) else data
    return [
        record
        for record in records
        if record.get("chemical_properties") in (None, {}) and chemistry_preflight(record) is None
    ]


@click.command()
@click.option(
    "--input",
    "-i",
    "input_path",
    type=click.Path(exists=True, path_type=Path),
    default=Path("data/curated/mapped_ingredients.yaml"),
)
@click.option("--output", "-o", "output_path", type=click.Path(path_type=Path), default=None)
@click.option("--dry-run", is_flag=True, help="Inspect the same guarded proposals without writing")
@click.option("--limit", type=int, default=None)
def main(input_path: Path, output_path: Path | None, dry_run: bool, limit: int | None):
    """Propose exact OLS chemistry only for explicitly eligible empty blocks."""
    data = load_ingredients(input_path)
    records = filter_chebi_without_properties(data)
    if limit is not None:
        records = records[:limit]
    enriched = skipped = failed = 0
    for record in records:
        proposal, explanation = prepare_chemical_properties(record)
        if proposal:
            enriched += 1
            console.print(
                f"{'Would enrich' if dry_run else 'Enriched'} {record.get('preferred_term')}: {explanation}"
            )
            if not dry_run:
                record["chemical_properties"] = proposal
                record_curation_event(
                    record,
                    curator="enrich_chemical_properties.py",
                    action="AUTO_BACKFILL_CHEBI_CHEMISTRY",
                    changes=explanation,
                )
        elif explanation == "PROVIDER_FAILURE":
            failed += 1
            console.print(f"Provider failure: {record.get('preferred_term')}")
        else:
            skipped += 1
            console.print(f"Skipped {record.get('preferred_term')}: {explanation}")
    console.print(f"Enriched: {enriched}; Skipped: {skipped}; Failed: {failed}")
    if enriched and not dry_run:
        try:
            save_yaml(
                data, output_path or input_path, validate=True, target_class="IngredientCollection"
            )
        except ValidationFailedError as exc:
            print(exc.summary(), file=sys.stderr)
            raise
    if failed:
        raise click.ClickException(f"{failed} chemical property provider failures")


if __name__ == "__main__":
    main()
