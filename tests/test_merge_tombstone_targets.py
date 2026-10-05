"""Merge tombstones must resolve to a live record (#799).

`docs/LABEL_INDEX_CONTRACT.md` tells consumers to follow REJECTED rows, because
a merged record's `identifier` points at its merge target. Four tombstones from
the 2026-09-21 review kept the identity the review had rejected instead, so
`NaNO` resolved to the nano unit prefix. CultureMech refuses such a label index
outright, which blocked its pin refresh; these tests make MIM refuse it first.
"""

from __future__ import annotations

import csv
import importlib.util
from pathlib import Path

import pytest
import yaml

ROOT = Path(__file__).resolve().parents[1]
LOADER = getattr(yaml, "CSafeLoader", yaml.SafeLoader)


@pytest.fixture(scope="module")
def records() -> list[dict]:
    return [
        yaml.load(path.read_text(encoding="utf-8"), Loader=LOADER)
        for group in ("mapped", "unmapped")
        for path in sorted((ROOT / "data/ingredients" / group).glob("*.yaml"))
    ]


def test_every_merge_tombstone_points_at_a_live_record(records):
    live = {r["identifier"] for r in records if r.get("mapping_status") == "MAPPED"}
    dangling = sorted(
        (r["preferred_term"], r["identifier"])
        for r in records
        if r.get("mapping_status") == "REJECTED"
        and any(e.get("action") == "MERGED_INTO" for e in r.get("curation_history") or [])
        and not str(r["identifier"]).startswith("UNMAPPED_")
        and r["identifier"] not in live
    )
    assert not dangling, f"merge tombstones on an identity no live record holds: {dangling}"


def test_published_rejected_rows_resolve_to_a_live_identifier():
    """The consumer-side check CultureMech applies to every pin (#260)."""
    with (ROOT / "docs/data/label_index.csv").open(newline="", encoding="utf-8") as handle:
        rows = list(csv.DictReader(handle))
    live = {row["identifier"] for row in rows if row["mapping_status"] == "MAPPED"}
    dangling = sorted(
        {
            row["identifier"]
            for row in rows
            if row["mapping_status"] == "REJECTED"
            and not row["identifier"].startswith("UNMAPPED_")
            and row["identifier"] not in live
        }
    )
    assert not dangling


@pytest.mark.parametrize(
    ("term", "target"),
    [
        ("NaNO", "CHEBI:63005"),
        ("Atrazin", "CHEBI:15930"),
        ("EDTA (chelating agent)", "CHEBI:4735"),
        ("Sodium phosphate dibasic", "CHEBI:34683"),
    ],
)
def test_the_799_tombstones_keep_their_provenance(records, term, target):
    record = next(r for r in records if r["preferred_term"] == term)
    assert record["identifier"] == target
    assert record["mapping_status"] == "REJECTED"
    # The rejected identity is provenance, not deleted.
    assert record["ontology_mapping"]["ontology_id"] != target
    assert record["curation_history"][-1]["curator"] == "fix_799_tombstone_identifiers"


def test_fix_script_is_idempotent():
    spec = importlib.util.spec_from_file_location(
        "fix_799", ROOT / "scripts/fix_799_tombstone_identifiers.py"
    )
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    data = yaml.load(
        (ROOT / "data/curated/mapped_ingredients.yaml").read_text(encoding="utf-8"), Loader=LOADER
    )
    assert module.plan(data["ingredients"]) == []
