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
    collect_visualization_exclusions,
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
        "MIM:Dry": {
            "identifier": "CHEBI:1",
            "name": "salt",
            "mapping_status": "MAPPED",
            "ontology_source": "CHEBI",
            "ontology_id": "CHEBI:1",
            "ontology_label": "salt",
            "mapping_quality": "EXACT_MATCH",
            "total_occurrences": 0,
            "media_count": 0,
            "num_synonyms": 0,
            "molecular_formula": "",
            "cas_rn": "",
            "category": "mapped",
        },
        "MIM:Wet": {
            "identifier": "CHEBI:1",
            "name": "salt hydrate",
            "mapping_status": "MAPPED",
            "ontology_source": "CHEBI",
            "ontology_id": "CHEBI:1",
            "ontology_label": "salt hydrate",
            "mapping_quality": "EXACT_MATCH",
            "total_occurrences": 0,
            "media_count": 0,
            "num_synonyms": 0,
            "molecular_formula": "",
            "cas_rn": "",
            "category": "mapped",
        },
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


def test_currency_audit_rejects_stale_metadata():
    defects = audit_entries(
        [
            {
                "id": "MIM:Dry",
                "identifier": "CHEBI:1",
                "ontology_id": "CHEBI:old",
            }
        ],
        {
            "MIM:Dry": {
                "identifier": "CHEBI:1",
                "ontology_id": "CHEBI:2",
            }
        },
    )

    assert defects["metadata_mismatches"] == [
        ("MIM:Dry", {"ontology_id": ("CHEBI:old", "CHEBI:2")})
    ]


def test_num_synonyms_excludes_rejected_label_and_curation_notes(tmp_path):
    from scripts.browser_export import extract_ingredient_for_browser

    ingredients = tmp_path / "ingredients"
    path = ingredients / "mapped" / "Salt.yaml"
    path.parent.mkdir(parents=True, exist_ok=True)
    record = {
        "identifier": "CHEBI:1",
        "preferred_term": "salt",
        "mapping_status": "MAPPED",
        "ontology_mapping": {
            "ontology_id": "CHEBI:1",
            "ontology_label": "salt",
            "ontology_source": "CHEBI",
            "mapping_quality": "EXACT_MATCH",
        },
        "synonyms": [
            {"synonym_text": "table salt", "synonym_type": "EXACT_SYNONYM"},
            {"synonym_text": "table salt", "synonym_type": "RELATED_SYNONYM"},
            {"synonym_text": "salt monohydrate", "synonym_type": "REJECTED_LABEL"},
            {"synonym_text": "Role: mineral source", "synonym_type": "RAW_TEXT"},
        ],
    }
    path.write_text(yaml.safe_dump(record), encoding="utf-8")

    coordinates = pd.DataFrame(
        [{"ingredient_id": "MIM:Salt", "umap_x": 1.0, "umap_y": 2.0}]
    )
    nodes = build_visualization_data(coordinates, ingredients)
    live = live_records(ingredients)
    browser = extract_ingredient_for_browser(record, "mapped/Salt.yaml")

    assert nodes[0]["num_synonyms"] == 1
    assert live["MIM:Salt"]["num_synonyms"] == 1
    assert browser["synonyms"] == ["table salt"]
    assert browser["synonym_count"] == 1
    assert "salt monohydrate" not in browser["searchable"]


def test_currency_audit_detects_missing_live_records_and_invalid_exclusions():
    entries = [
        {
            "id": "MIM:Dry",
            "identifier": "CHEBI:1",
            "ontology_id": "CHEBI:1",
        }
    ]
    live = {
        "MIM:Dry": {
            "identifier": "CHEBI:1",
            "ontology_id": "CHEBI:1",
            "mapping_status": "MAPPED",
            "category": "mapped",
        },
        "MIM:Rifamycin": {
            "identifier": "CHEBI:28077",
            "ontology_id": "CHEBI:28077",
            "mapping_status": "MAPPED",
            "category": "mapped",
        },
        "MIM:Local_Compound": {
            "identifier": "kgmicrobe.compound:local_1",
            "ontology_id": "kgmicrobe.compound:local_1",
            "mapping_status": "MAPPED",
            "category": "mapped",
        },
        "MIM:Regrounded": {
            "identifier": "CHEBI:999",
            "ontology_id": "CHEBI:999",
            "mapping_status": "MAPPED",
            "category": "mapped",
        },
        "MIM:Forged_Embedded": {
            "identifier": "CHEBI:1",
            "ontology_id": "CHEBI:1",
            "mapping_status": "MAPPED",
            "category": "mapped",
        },
        "MIM:Unmapped_Foo": {
            "identifier": "UNMAPPED_0001",
            "ontology_id": "",
            "mapping_status": "UNMAPPED",
            "category": "unmapped",
        },
    }
    exclusions = {
        "MIM:Local_Compound": {
            "identifier": "kgmicrobe.compound:local_1",
            "ontology_id": "kgmicrobe.compound:local_1",
            "ontology_source": "kgmicrobe.compound",
            "reason": "no_kg_microbe_embedding",
        },
        "MIM:Regrounded": {
            "identifier": "cas:123-45-6",
            "ontology_id": "cas:123-45-6",
            "ontology_source": "CAS",
            "reason": "no_kg_microbe_embedding",
        },
        "MIM:Forged_Embedded": {
            "identifier": "CHEBI:1",
            "ontology_id": "CHEBI:1",
            "ontology_source": "CHEBI",
            "reason": "no_kg_microbe_embedding",
        },
        "MIM:Unmapped_Foo": {
            "identifier": "UNMAPPED_0001",
            "ontology_id": "",
            "ontology_source": "",
            "reason": "no_kg_microbe_embedding",
        },
        "MIM:Dry": {
            "identifier": "CHEBI:1",
            "ontology_id": "CHEBI:1",
            "ontology_source": "CHEBI",
            "reason": "no_kg_microbe_embedding",
        },
        "MIM:Retired": {
            "identifier": "cas:000-00-0",
            "ontology_id": "cas:000-00-0",
            "ontology_source": "CAS",
            "reason": "no_kg_microbe_embedding",
        },
    }

    defects = audit_entries(entries, live, exclusions)

    assert defects["missing"] == [
        "MIM:Forged_Embedded",
        "MIM:Regrounded",
        "MIM:Rifamycin",
        "MIM:Unmapped_Foo",
    ]
    assert defects["invalid_exclusions"] == ["MIM:Dry", "MIM:Retired"]


def test_collect_visualization_exclusions_records_unembedded_mapped_only(tmp_path):
    ingredients = tmp_path / "ingredients"
    _write(ingredients / "mapped" / "Embedded.yaml", "CHEBI:1", "salt")
    _write(
        ingredients / "mapped" / "Local.yaml",
        "kgmicrobe.compound:local_1",
        "local compound",
    )
    _write(
        ingredients / "mapped" / "Tombstone.yaml",
        "kgmicrobe.compound:dead",
        "retired",
        status="REJECTED",
    )
    _write(
        ingredients / "unmapped" / "Unmapped_1.yaml",
        "UNMAPPED_0001",
        "unknown",
        status="UNMAPPED",
    )

    exclusions = collect_visualization_exclusions(ingredients, {"CHEBI:1": [0.1, 0.2]})

    assert exclusions == {
        "MIM:Local": {
            "identifier": "kgmicrobe.compound:local_1",
            "ontology_id": "kgmicrobe.compound:local_1",
            "ontology_source": "CHEBI",
            "reason": "no_kg_microbe_embedding",
        }
    }


