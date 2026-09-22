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
    with pytest.raises(ValueError, match="mapping identities"):
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


def two_supported_rows(fixture):
    root, path, output = fixture
    review = json.loads(path.read_text())
    evidence = root / "evidence.json"
    proof = json.loads(evidence.read_text())
    review["decisions"][1]["disposition"] = "SUPPORTED"
    proof["entries"]["2"]["disposition"] = "SUPPORTED"
    fixture_support.write_json(evidence, proof)
    review["inputs"]["evidence.json"] = reviewed.digest(evidence)
    source = root / "source.sssom.tsv"
    _, fields, rows = reviewed.read_sssom(source)
    header = "".join(
        line for line in source.read_text().splitlines(keepends=True) if line.startswith("#")
    )
    source.write_bytes(header.encode() + reviewed._tsv(fields, list(reversed(rows))))
    review["source_sha256"] = reviewed.digest(source)
    for decision in review["decisions"]:
        decision["source_position"] = 3 - decision["source_position"]
    fixture_support.write_json(path, review)
    reviewed.export_reviewed(root, path, output)


def test_real_native_sorting_preserves_mapping_multiset(reviewed_fixture):
    _, _, output = reviewed_fixture
    two_supported_rows(reviewed_fixture)
    table = output / "ingredient_mappings.sssom.tsv"
    _, _, raw = reviewed.read_sssom(table)
    native = native_gate.parse_sssom_table(table, strict=True)
    assert [row["subject_id"] for row in raw] == ["MIM:Beta", "MIM:Alpha"]
    assert native.df.subject_id.tolist() == ["MIM:Alpha", "MIM:Beta"]
    assert native_gate.validate_native(output)["status"] == "PASS"


def test_multiset_preserves_duplicate_multiplicity_and_bound_confidence():
    alpha = {"subject_id": "MIM:Alpha", "subject_label": "Alpha", "confidence": "0.80"}
    beta = {"subject_id": "MIM:Beta", "subject_label": "Beta", "confidence": "0.99"}
    assert native_gate._mapping_multiset([alpha, alpha, beta]) != native_gate._mapping_multiset(
        [alpha, beta, beta]
    )
    assert native_gate._mapping_multiset([alpha, beta]) == native_gate._mapping_multiset(
        [{**beta, "confidence": 0.99}, {**alpha, "confidence": 0.8}], native=True
    )
    assert native_gate._mapping_multiset([alpha, beta]) != native_gate._mapping_multiset(
        [{**beta, "confidence": 0.8}, {**alpha, "confidence": 0.99}], native=True
    )


def test_native_reordering_cannot_hide_substituted_mapping(reviewed_fixture, monkeypatch):
    _, _, output = reviewed_fixture
    two_supported_rows(reviewed_fixture)
    parse = native_gate.parse_sssom_table

    def substitute(*args, **kwargs):
        native = parse(*args, **kwargs)
        if len(native.df) == 2:
            native.df.iloc[1] = native.df.iloc[0]
        return native

    monkeypatch.setattr(native_gate, "parse_sssom_table", substitute)
    with pytest.raises(ValueError, match="mapping identities"):
        native_gate.validate_native(output)
