"""Regression contract for retirement of the dormant hierarchy API (#448)."""

from __future__ import annotations

import csv
import json
from copy import deepcopy
from pathlib import Path

import yaml

from mediaingredientmech.validation.write_validated import validate_ingredient
from scripts.generate_index_files import (
    generate_csv_index,
    generate_json_index,
    generate_markdown_index,
    load_records,
)

ROOT = Path(__file__).resolve().parent.parent
SCHEMA = ROOT / "src" / "mediaingredientmech" / "schema" / "mediaingredientmech.yaml"
RETIRED_FIELDS = {
    "parent_ingredient": "CHEBI:15377",
    "child_ingredients": ["CHEBI:15377"],
    "variant_type": "PURIFIED",
    "variant_notes": "legacy prototype value",
    "role_inheritance": True,
}
BASE_RECORD = {
    "identifier": "CHEBI:15377",
    "preferred_term": "water",
    "mapping_status": "MAPPED",
    "ontology_mapping": {
        "ontology_id": "CHEBI:15377",
        "ontology_label": "water",
        "ontology_source": "CHEBI",
        "mapping_quality": "EXACT_MATCH",
    },
}


def test_schema_no_longer_exposes_hierarchy_surface():
    schema = yaml.safe_load(SCHEMA.read_text(encoding="utf-8"))
    attributes = schema["classes"]["IngredientRecord"]["attributes"]

    assert RETIRED_FIELDS.keys().isdisjoint(attributes)
    assert "VariantTypeEnum" not in schema["enums"]
    assert "BACKFILL_PARENT_CHEBI" in schema["enums"]["CurationActionEnum"]["permissible_values"]


def test_closed_schema_rejects_each_retired_field():
    assert validate_ingredient(BASE_RECORD, target_class="IngredientRecord") == []

    for field, value in RETIRED_FIELDS.items():
        record = deepcopy(BASE_RECORD)
        record[field] = value
        errors = validate_ingredient(record, target_class="IngredientRecord")
        assert errors, f"closed-schema validation accepted retired field {field}"


def test_canonical_collections_have_no_retired_fields():
    for name in ("mapped_ingredients.yaml", "unmapped_ingredients.yaml"):
        collection = yaml.safe_load((ROOT / "data" / "curated" / name).read_text(encoding="utf-8"))
        for record in collection["ingredients"]:
            assert RETIRED_FIELDS.keys().isdisjoint(record), record.get("preferred_term")


def test_index_exports_do_not_restore_legacy_hierarchy(tmp_path):
    record = {
        **BASE_RECORD,
        **RETIRED_FIELDS,
        "occurrence_statistics": {"total_occurrences": 1},
    }
    csv_path = tmp_path / "index.csv"
    json_path = tmp_path / "index.json"
    markdown_path = tmp_path / "index.md"

    generate_csv_index([record], csv_path)
    generate_json_index([record], json_path)
    generate_markdown_index([record], markdown_path, "Test index")

    with csv_path.open(newline="", encoding="utf-8") as stream:
        header = next(csv.reader(stream))
    assert RETIRED_FIELDS.keys().isdisjoint(header)

    exported = json.loads(json_path.read_text(encoding="utf-8"))[0]
    assert RETIRED_FIELDS.keys().isdisjoint(exported)
    assert "Hierarchy Parents" not in markdown_path.read_text(encoding="utf-8")


def test_index_record_loader_reads_aggregate_ingredients(tmp_path):
    path = tmp_path / "collection.yaml"
    path.write_text(yaml.safe_dump({"ingredients": [BASE_RECORD]}), encoding="utf-8")

    assert load_records(path) == [BASE_RECORD]


def test_index_record_loader_rejects_malformed_collections(tmp_path):
    path = tmp_path / "collection.yaml"
    path.write_text(yaml.safe_dump({"records": []}), encoding="utf-8")

    try:
        load_records(path)
    except ValueError as exc:
        assert "does not contain an ingredients list" in str(exc)
    else:
        raise AssertionError("malformed collection was accepted")


def test_prototype_is_archived_not_maintained():
    for relative_path in (
        "src/mediaingredientmech/utils/hierarchy_utils.py",
        "src/mediaingredientmech/utils/hierarchy_validator.py",
        "src/mediaingredientmech/utils/id_utils.py",
        "scripts/build_water_hierarchy.py",
        "scripts/analyze_duplicates_and_variants.py",
        "scripts/apply_corrections.py",
        "scripts/unmerge_complex_media.py",
        "scripts/reconcile_unmapped.py",
        "scripts/merge_identifier_collisions.py",
        "analysis/duplicates_and_variants.yaml",
        "analysis/good_merge_examples.md",
        "analysis/bad_merge_examples.md",
        "analysis/merge_pattern_analysis.md",
        "analysis/merge_pattern_analysis.yaml",
        "docs/WATER_VARIANT_CURATION.md",
        ".claude/skills/manage-identifiers/reference",
    ):
        assert not (ROOT / relative_path).exists()

    for relative_path in (
        "ATTIC/HIERARCHY_GUIDE_RETIRED.md",
        "ATTIC/WATER_VARIANT_CURATION_RETIRED.md",
        "ATTIC/build_water_hierarchy.py",
        "ATTIC/id_utils.py",
        "ATTIC/manage_identifiers_sequential_id_reference",
        "ATTIC/analyze_duplicates_and_variants.py",
        "ATTIC/apply_corrections.py",
        "ATTIC/unmerge_complex_media.py",
        "ATTIC/reconcile_unmapped.py",
        "ATTIC/merge_identifier_collisions.py",
        "ATTIC/duplicates_and_variants.yaml",
        "ATTIC/good_merge_examples.md",
        "ATTIC/bad_merge_examples.md",
        "ATTIC/merge_pattern_analysis.md",
        "ATTIC/merge_pattern_analysis.yaml",
    ):
        assert (ROOT / relative_path).exists()

    maintained_guide = (ROOT / "docs" / "HIERARCHY_GUIDE.md").read_text(encoding="utf-8")
    assert "does not currently encode" in maintained_guide
    assert "CultureMech is authoritative" in maintained_guide
