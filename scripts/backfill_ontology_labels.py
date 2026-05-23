#!/usr/bin/env python3
"""Backfill missing ``ontology_label`` values in mapped ingredient records.

Schema flag: ``OntologyMapping.ontology_label`` is ``required: true`` but
``linkml-validate`` accepts empty strings as "present". Several hundred
records were imported (mostly from the CultureBotHT CAS→CHEBI bridge)
with ``ontology_label: ''`` and never had the label backfilled. This
script fetches the canonical label from the OLS4 ChEBI endpoint and
writes it back. Only touches records whose ``ontology_label`` is the
empty string; non-empty labels are left alone.

Usage::

    python scripts/backfill_ontology_labels.py            # writes in place
    python scripts/backfill_ontology_labels.py --dry-run  # report only
"""

from __future__ import annotations

import sys
import time
import urllib.parse
from pathlib import Path

import click
import requests
import yaml
from rich.console import Console
from rich.progress import Progress

console = Console()

OLS_API = "https://www.ebi.ac.uk/ols4/api/ontologies"

ONTOLOGY_TO_IRI_BASE = {
    "CHEBI": "http://purl.obolibrary.org/obo/CHEBI_",
    "FOODON": "http://purl.obolibrary.org/obo/FOODON_",
    "ENVO": "http://purl.obolibrary.org/obo/ENVO_",
    "UBERON": "http://purl.obolibrary.org/obo/UBERON_",
    "NCIT": "http://purl.obolibrary.org/obo/NCIT_",
    "BTO": "http://purl.obolibrary.org/obo/BTO_",
}
ONTOLOGY_TO_OLS = {
    "CHEBI": "chebi",
    "FOODON": "foodon",
    "ENVO": "envo",
    "UBERON": "uberon",
    "NCIT": "ncit",
    "BTO": "bto",
}


def fetch_label(curie: str, source: str) -> str | None:
    """Fetch the canonical label for an ontology term from OLS4.

    Rejects "junk" labels: obsolete CHEBI terms return the IRI fragment
    (e.g. "CHEBI_1", "CHEBI_8150") as the label, which is not a real
    canonical label and would silently overwrite an empty string with
    garbage. We also skip obsolete terms entirely.
    """
    prefix, _, local = curie.partition(":")
    iri_base = ONTOLOGY_TO_IRI_BASE.get(prefix.upper())
    ols_ontology = ONTOLOGY_TO_OLS.get(prefix.upper())
    if not iri_base or not ols_ontology:
        return None
    iri = f"{iri_base}{local}"
    encoded = urllib.parse.quote(urllib.parse.quote(iri, safe=""), safe="")
    url = f"{OLS_API}/{ols_ontology}/terms/{encoded}"
    try:
        resp = requests.get(url, timeout=10)
        if resp.status_code != 200:
            return None
        data = resp.json()
        label = data.get("label")
        if not label:
            return None
        if data.get("is_obsolete"):
            return None
        # IRI-fragment fallback (e.g. "CHEBI_8150") = obsolete or stub term
        # with no real label. Treat as no-label-available.
        if label.replace("_", ":") == curie or label == f"{prefix}_{local}":
            return None
        return label
    except (requests.RequestException, ValueError):
        return None


def iter_records(data: dict):
    if isinstance(data, dict) and "ingredients" in data:
        yield from data["ingredients"]
    elif isinstance(data, list):
        yield from data


@click.command()
@click.option(
    "--input",
    "-i",
    "input_path",
    type=click.Path(exists=True, path_type=Path),
    default=Path("data/curated/mapped_ingredients.yaml"),
)
@click.option("--dry-run", is_flag=True, help="Report only, do not write.")
@click.option(
    "--sleep",
    type=float,
    default=0.05,
    help="Seconds between OLS requests (rate-limit politeness).",
)
def main(input_path: Path, dry_run: bool, sleep: float):
    console.print(f"\n[bold]Backfilling missing ontology_label[/bold]")
    console.print(f"Input: {input_path}")

    with open(input_path) as f:
        data = yaml.safe_load(f)

    candidates = []
    for record in iter_records(data):
        mapping = record.get("ontology_mapping") or {}
        label = mapping.get("ontology_label")
        if label != "":
            continue
        ontology_id = mapping.get("ontology_id")
        if not ontology_id:
            continue
        candidates.append(record)

    console.print(f"Found {len(candidates)} records with empty ontology_label")
    if not candidates:
        return

    if dry_run:
        for r in candidates[:10]:
            console.print(
                f"  {r['ontology_mapping']['ontology_id']:<20} ({r.get('preferred_term', 'N/A')})"
            )
        if len(candidates) > 10:
            console.print(f"  ... and {len(candidates) - 10} more")
        return

    filled, missing = 0, 0
    miss_list: list[str] = []
    with Progress() as progress:
        task = progress.add_task("[cyan]Fetching labels...", total=len(candidates))
        for record in candidates:
            mapping = record["ontology_mapping"]
            curie = mapping["ontology_id"]
            source = mapping.get("ontology_source", "")
            label = fetch_label(curie, source)
            if label:
                mapping["ontology_label"] = label
                filled += 1
            else:
                missing += 1
                miss_list.append(curie)
            progress.update(task, advance=1)
            if sleep:
                time.sleep(sleep)

    console.print(f"\nFilled: [green]{filled}[/green]")
    console.print(f"Unresolved: [yellow]{missing}[/yellow]")
    if miss_list[:10]:
        console.print(f"Unresolved sample: {', '.join(miss_list[:10])}")

    if filled:
        # Match IngredientCurator.save() yaml.dump settings (default width=80)
        # so this script's writes don't reformat unrelated lines.
        with open(input_path, "w") as f:
            yaml.dump(
                data, f, default_flow_style=False, sort_keys=False,
                allow_unicode=True,
            )
        console.print(f"[bold green]Saved to {input_path}[/bold green]")


if __name__ == "__main__":
    main()
