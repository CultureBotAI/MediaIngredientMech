"""Native schema validation must not pass after silently dropping bad rows (#730)."""

import importlib.util
import json
from pathlib import Path

import pytest

from mediaingredientmech.export import reviewed_sssom as reviewed
from tests import test_reviewed_sssom as fixture_support

SPEC = importlib.util.spec_from_file_location(
    "validate_reviewed_sssom_schema",
    Path(__file__).parents[1] / "scripts/validate_reviewed_sssom_schema.py",
)
native_gate = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(native_gate)


@pytest.fixture
def reviewed_fixture(tmp_path):
    return fixture_support.reviewed_fixture.__wrapped__(tmp_path)


def test_both_partitions_pass_native_schema_and_preserve_rows(reviewed_fixture):
    _, _, output = reviewed_fixture
    reviewed.export_reviewed(*reviewed_fixture)
    result = native_gate.validate_native(output)
    assert result["status"] == "PASS"
    assert all(
        item["raw_rows"] == item["native_rows"] == item["linkml_rows"] == 1
        for item in result["partitions"].values()
    )


def test_parser_dropped_malformed_row_cannot_produce_false_pass(reviewed_fixture):
    _, _, output = reviewed_fixture
    reviewed.export_reviewed(*reviewed_fixture)
    table = output / "ingredient_mappings.sssom.tsv"
    table.write_text(table.read_text().replace("\t0.8\t", "\tnot-a-number\t"))
    with pytest.raises(ValueError, match="parser dropped or added rows"):
        native_gate.validate_native(output)


def test_native_counts_must_equal_manifest(reviewed_fixture):
    _, _, output = reviewed_fixture
    reviewed.export_reviewed(*reviewed_fixture)
    manifest_path = output / "manifest.json"
    manifest = json.loads(manifest_path.read_text())
    manifest["counts"]["supported"] += 1
    manifest_path.write_text(json.dumps(manifest))
    with pytest.raises(ValueError, match="manifest row count"):
        native_gate.validate_native(output)


def test_native_mapping_identity_changes_rejected(reviewed_fixture, monkeypatch):
    _, _, output = reviewed_fixture
    reviewed.export_reviewed(*reviewed_fixture)
    parse = native_gate.parse_sssom_table

    def changed_label(*args, **kwargs):
        result = parse(*args, **kwargs)
        result.df.loc[0, "object_label"] = "Wrong native label"
        return result

    monkeypatch.setattr(native_gate, "parse_sssom_table", changed_label)
    with pytest.raises(ValueError, match="ordered mapping identity"):
        native_gate.validate_native(output)


def test_native_linkml_document_cannot_drop_rows(reviewed_fixture, monkeypatch):
    _, _, output = reviewed_fixture
    reviewed.export_reviewed(*reviewed_fixture)
    convert = native_gate.to_mapping_set_document

    def dropped_document(*args, **kwargs):
        document = convert(*args, **kwargs)
        document.mapping_set.mappings = []
        return document

    monkeypatch.setattr(native_gate, "to_mapping_set_document", dropped_document)
    with pytest.raises(ValueError, match="LinkML conversion dropped"):
        native_gate.validate_native(output)


def test_empty_supported_partition_is_valid_when_all_source_rows_withheld(reviewed_fixture):
    _, _, output = reviewed_fixture
    fixture_support.prepare_new_generation(reviewed_fixture)
    reviewed.export_reviewed(*reviewed_fixture)
    result = native_gate.validate_native(output)
    assert result["partitions"]["ingredient_mappings.sssom.tsv"]["raw_rows"] == 0
    assert result["partitions"]["withheld_mappings.sssom.tsv"]["raw_rows"] == 2
