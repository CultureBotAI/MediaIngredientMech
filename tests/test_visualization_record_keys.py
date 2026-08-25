"""Visualization nodes use file-backed record keys, not semantic identifiers."""

from __future__ import annotations

from pathlib import Path

import pandas as pd
import pytest
import yaml

from scripts.check_visualization_currency import audit_entries, live_records
from scripts.generate_ingredient_umap import (
    _require_unique_record_keys,
    build_visualization_data,
)


def _write(path: Path, identifier: str, term: str, status: str = "MAPPED") -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        yaml.safe_dump(
            {
                "identifier": identifier,
                "preferred_term": term,
                "mapping_status": status,
                "ontology_mapping": {
                    "ontology_id": identifier,
                    "ontology_label": term,
                    "ontology_source": "CHEBI",
                    "mapping_quality": "EXACT_MATCH",
                },
            }
        ),
        encoding="utf-8",
    )


def test_visualization_preserves_live_siblings_with_one_semantic_identifier(tmp_path):
    ingredients = tmp_path / "ingredients"
    _write(ingredients / "mapped" / "Dry.yaml", "CHEBI:1", "salt")
    _write(ingredients / "mapped" / "Wet.yaml", "CHEBI:1", "salt hydrate")
    _write(
        ingredients / "mapped" / "Merged_label.yaml",
        "CHEBI:1",
        "old spelling",
        status="REJECTED",
    )
    coordinates = pd.DataFrame(
        [
            {"ingredient_id": "MIM:Dry", "umap_x": 1.0, "umap_y": 2.0},
            {"ingredient_id": "MIM:Wet", "umap_x": 1.0, "umap_y": 2.0},
        ]
    )

    nodes = build_visualization_data(coordinates, ingredients)

    assert {node["id"] for node in nodes} == {"MIM:Dry", "MIM:Wet"}
    assert {node["name"] for node in nodes} == {"salt", "salt hydrate"}
    assert {node["identifier"] for node in nodes} == {"CHEBI:1"}


def test_currency_index_uses_record_keys_and_excludes_tombstones(tmp_path):
    ingredients = tmp_path / "ingredients"
    _write(ingredients / "mapped" / "Dry.yaml", "CHEBI:1", "salt")
    _write(ingredients / "mapped" / "Wet.yaml", "CHEBI:1", "salt hydrate")
    _write(
        ingredients / "mapped" / "Merged_label.yaml",
        "CHEBI:1",
        "old spelling",
        status="REJECTED",
    )

    assert live_records(ingredients) == {
        "MIM:Dry": "CHEBI:1",
        "MIM:Wet": "CHEBI:1",
    }


def test_duplicate_record_keys_are_rejected_not_collapsed():
    with pytest.raises(ValueError, match="Duplicate visualization record key"):
        _require_unique_record_keys([{"id": "MIM:Same"}, {"id": "MIM:Same"}])


def test_currency_audit_rejects_blank_keys_and_non_object_entries():
    defects = audit_entries(
        [{"id": "", "identifier": "CHEBI:1"}, "not a node"],
        {"MIM:Dry": "CHEBI:1"},
    )

    assert defects["blank_ids"] == [0]
    assert defects["invalid_entries"] == [1]
