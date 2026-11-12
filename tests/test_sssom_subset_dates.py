"""Subset dates describe emitted rows, independently of the full source version (#1090)."""

import copy
import csv
import importlib.util
import json
from datetime import date
from pathlib import Path

import pytest
import yaml

from mediaingredientmech.export import reviewed_sssom as reviewed
from mediaingredientmech.export.ingredient_bundle import export_bundle
from mediaingredientmech.export.supported_kgx import _supported_sssom, export_supported
from mediaingredientmech.ingredient_bundle_contract import (
    ARTIFACTS,
    _base_table,
    content_sha256,
    read_json,
    reviewed_products,
    validate_bundle,
)


def _test_module(name):
    path = Path(__file__).with_name(name + ".py")
    spec = importlib.util.spec_from_file_location(name + "_date_fixture", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def _parse(content):
    lines = content.decode().splitlines(keepends=True)
    metadata = yaml.safe_load("".join(line[1:] for line in lines if line.startswith("#")))
    rows = list(
        csv.DictReader((line for line in lines if not line.startswith("#")), delimiter="\t")
    )
    return metadata, rows


def _table(metadata, rows, fields=None):
    header = "".join("# " + line + "\n" for line in yaml.safe_dump(metadata).splitlines())
    return header.encode() + reviewed._tsv(fields or list(rows[0]), rows)


def _reviewed_fixture(tmp_path, dates, supported=(True, False)):
    """A complete synthetic review; every modified test row is rebound to its proof."""
    module = _test_module("test_reviewed_sssom")
    root, review_path, output = module.reviewed_fixture.__wrapped__(tmp_path)
    source = root / "source.sssom.tsv"
    metadata, fields, rows = reviewed.read_sssom(source)
    metadata.update(mapping_date="2024-12-31", mapping_set_version="2024-12-31")
    review = json.loads(review_path.read_bytes())
    evidence = json.loads((root / "evidence.json").read_bytes())
    for row, decision, value, approved in zip(
        rows, review["decisions"], dates, supported, strict=True
    ):
        row["mapping_date"] = value
        decision["row_sha256"] = reviewed.row_sha256(row)
        decision["disposition"] = "SUPPORTED" if approved else "WITHHOLD"
        evidence["entries"][decision["evidence_key"]].update(
            row_sha256=decision["row_sha256"], disposition=decision["disposition"]
        )
    source.write_bytes(_table(metadata, rows, fields + ["mapping_date"]))
    module.write_json(root / "evidence.json", evidence)
    review["source_sha256"] = reviewed.digest(source)
    review["inputs"]["evidence.json"] = reviewed.digest(root / "evidence.json")
    module.write_json(review_path, review)
    return root, review_path, output, rows


def test_reviewed_partitions_derive_their_own_dates_and_preserve_proofs(tmp_path):
    root, path, output, source_rows = _reviewed_fixture(tmp_path, ("2024-03-02", "2024-12-31"))
    source_bytes, proof_bytes = (root / "source.sssom.tsv").read_bytes(), path.read_bytes()
    manifest = reviewed.export_reviewed(root, path, output)
    original_meta, _ = _parse(source_bytes)
    for index, filename in enumerate(reviewed.PRODUCTS[:2]):
        metadata, rows = _parse((output / filename).read_bytes())
        assert rows == [source_rows[index]]
        assert (
            metadata["mapping_date"] == metadata["mapping_set_version"] == rows[0]["mapping_date"]
        )
        for key in original_meta.keys() - {
            "mapping_date",
            "mapping_set_version",
            "mapping_set_id",
            "mapping_set_description",
        }:
            assert metadata[key] == original_meta[key]
    assert reviewed.validate_reviewed(root, path, output) == manifest
    assert manifest["source_sha256"] == reviewed.digest(root / "source.sssom.tsv")
    assert manifest["review_sha256"] == reviewed.digest(path)
    assert (root / "source.sssom.tsv").read_bytes() == source_bytes
    assert path.read_bytes() == proof_bytes


@pytest.mark.parametrize("dates", [("", ""), ("2024-03-02", "2024-12-31")])
def test_empty_and_wholly_dateless_reviewed_subsets_omit_dates(tmp_path, dates):
    root, path, output, source_rows = _reviewed_fixture(tmp_path, dates, supported=(False, False))
    reviewed.export_reviewed(root, path, output)
    supported_meta, supported_rows = _parse((output / reviewed.PRODUCTS[0]).read_bytes())
    assert supported_rows == []
    assert "mapping_date" not in supported_meta and "mapping_set_version" not in supported_meta
    withheld_meta, withheld_rows = _parse((output / reviewed.PRODUCTS[1]).read_bytes())
    assert withheld_rows == source_rows
    if not any(dates):
        assert "mapping_date" not in withheld_meta and "mapping_set_version" not in withheld_meta


@pytest.mark.parametrize("selected_dates", [[], [""], ["2024-01-05", "2024-03-02"]])
def test_supported_kgx_dates_use_only_its_selected_rows(tmp_path, selected_dates):
    rows = [
        {"subject_id": f"MIM:Selected{index}", "object_id": f"CHEBI:{index}", "mapping_date": value}
        for index, value in enumerate(selected_dates, 1)
    ]
    newest = {"subject_id": "MIM:Withheld", "object_id": "CHEBI:999", "mapping_date": "2024-12-31"}
    metadata = {
        "mapping_set_id": "https://example.org/source",
        "mapping_date": "2024-12-31",
        "mapping_set_version": "2024-12-31",
        "predicate_semantics": "skos",
        "license": "https://example.org/license",
    }
    source = tmp_path / "mappings/ingredient_mappings.sssom.tsv"
    source.parent.mkdir()
    source.write_bytes(_table(metadata, [*rows, newest]))
    before = source.read_bytes()
    selected = [
        {
            "assertion_type": "mapping",
            "source_position": str(index),
            "assertion_json": json.dumps(row),
        }
        for index, row in enumerate(rows, 1)
    ]
    selected_before = copy.deepcopy(selected)
    content, count, set_id = _supported_sssom(tmp_path, selected)
    actual_meta, actual_rows = _parse(content)
    assert actual_rows == rows and count == len(rows)
    assert set_id == "https://example.org/source/supported"
    assert actual_meta["predicate_semantics"] == "skos"
    assert actual_meta["license"] == metadata["license"]
    if any(selected_dates):
        expected = max(date.fromisoformat(value) for value in selected_dates).isoformat()
        assert actual_meta["mapping_date"] == actual_meta["mapping_set_version"] == expected
    else:
        assert "mapping_date" not in actual_meta and "mapping_set_version" not in actual_meta
    assert source.read_bytes() == before and selected == selected_before


def test_companion_date_is_stable_when_unselected_source_date_advances(tmp_path, pre_mint_schema_case):
    module = _test_module("test_ingredient_bundle_dependency_refresh")
    fixture = module.cohort.__wrapped__(pre_mint_schema_case)
    prior, before, current, _ = fixture
    before_copy, current_copy, review_copy = (
        copy.deepcopy(before),
        copy.deepcopy(current),
        copy.deepcopy(prior),
    )
    successor, receipt = module.verify(fixture)
    old_artifacts, old_loaded = reviewed_products(prior, before)
    new_artifacts, new_loaded = reviewed_products(successor, current)
    old_meta, old_rows = _parse(old_artifacts[ARTIFACTS["mappings"]])
    new_meta, new_rows = _parse(new_artifacts[ARTIFACTS["mappings"]])
    expected = max(date.fromisoformat(row["mapping_date"]) for row in old_rows).isoformat()
    assert old_meta["mapping_date"] == old_meta["mapping_set_version"] == expected
    assert new_meta["mapping_date"] == new_meta["mapping_set_version"] == expected
    assert old_artifacts == new_artifacts and old_loaded == new_loaded
    assert old_rows == new_rows
    base = read_json(current[prior["base_review"]])
    source_meta, _, _ = _base_table(current[base["source_sssom"]])
    assert date.fromisoformat(source_meta["mapping_date"]) > date.fromisoformat(expected)
    assert successor["decisions"] == prior["decisions"]
    assert successor["record_inputs"] == prior["record_inputs"]
    assert receipt["scientific_approval_added"] is False
    assert (before, current, prior) == (before_copy, current_copy, review_copy)
    for name, content in before.items():
        target = tmp_path / name
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(content)
    review_path = tmp_path / "companion.json"
    review_path.write_bytes(json.dumps(prior).encode())
    output = tmp_path / "exported"
    result = export_bundle(tmp_path, review_path, output)
    loaded = validate_bundle(output, expected_manifest_sha256=result["manifest_sha256"])
    assert loaded["mappings"] == old_rows
    helper = Path(__file__).parents[1] / "src/mediaingredientmech/sssom_metadata.py"
    assert loaded["manifest"]["provenance"]["sssom_metadata_sha256"] == content_sha256(
        helper.read_bytes()
    )
    assert loaded["manifest"]["provenance"]["base_review_sha256"] == prior["base_review_sha256"]


def test_supported_manifest_attributes_subset_date_implementation(tmp_path):
    fixture = _test_module("test_supported_kgx").full_failed_review.__wrapped__(tmp_path)
    root, report = fixture
    manifest = export_supported(root, report, root / "supported")
    helper = Path(__file__).parents[1] / "src/mediaingredientmech/sssom_metadata.py"
    assert manifest["implementation"]["sssom_metadata.py"] == content_sha256(helper.read_bytes())


def test_registry_refresh_binds_date_helper_and_rejects_late_change(tmp_path, monkeypatch, pre_mint_schema_case):
    from mediaingredientmech import ingredient_bundle_refresh as refresh

    module = _test_module("test_ingredient_bundle_dependency_refresh")
    fixture = module.registry_correction.__wrapped__(module.cohort.__wrapped__(pre_mint_schema_case), tmp_path)
    _, audit = module.verify_registry(fixture)
    name = "src/mediaingredientmech/sssom_metadata.py"
    helper = tmp_path / name
    assert audit["registry_correction"]["input_sha256"][name] == content_sha256(helper.read_bytes())
    publish_new_files = refresh.publish_new_files

    def publish_with_late_change(outputs, check):
        def changed():
            helper.write_bytes(helper.read_bytes() + b"\n# changed after proof capture\n")
            check()

        return publish_new_files(outputs, changed)

    monkeypatch.setattr(refresh, "publish_new_files", publish_with_late_change)
    with pytest.raises(ValueError, match="Input changed during verification"):
        refresh.main(module.registry_argv(fixture))
    assert not any(
        (tmp_path / "history" / member).exists()
        for member in ("successor.json", "audit.json", "copy.json")
    )


@pytest.mark.parametrize(
    "invalid",
    ["２０２４-０３-０２", "2024-02-30", "2024-3-02", "2024-03-02T00:00:00", "not a date"],
)
def test_invalid_nonblank_dates_are_not_used_as_subset_versions(tmp_path, invalid):
    root, path, output, _ = _reviewed_fixture(tmp_path, (invalid, "2024-12-31"))
    with pytest.raises(ValueError, match="mapping_date"):
        reviewed.export_reviewed(root, path, output)
    assert not output.exists()
