"""Semantic adapter behavior, corpus boundaries, identity and atomic refusal."""
import copy
import hashlib
import json
from pathlib import Path

import pytest
import yaml

from mediaingredientmech import text_map_inputs as adapter

SOURCE = 'data/ingredients/mapped/salt+hydrate.yaml'
RECORD = {'identifier': 'CHEBI:1', 'preferred_term': 'Hydrated salt', 'ingredient_type': 'SINGLE_INGREDIENT', 'mapping_status': 'MAPPED', 'synonyms': [{'synonym_text': 'legitimate synonym'}, {'synonym_text': 'REJECTED_SENTINEL', 'synonym_type': 'REJECTED_LABEL'}]}
LABEL_FIELD = 'preferred_term'
PAGE = 'browser.html#record=mapped%2Fsalt%2Bhydrate.yaml'


def fixture_tree(root):
    for directory in adapter.RECORD_ROOTS:
        (root / directory).mkdir(parents=True, exist_ok=True)
    path = root / SOURCE
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(yaml.safe_dump(RECORD))
    if adapter.ADAPTER_VERSION.startswith("traitmech-"):
        parent = path.with_name("parent.yaml")
        parent.write_text(yaml.safe_dump({"identifier": "METPO:parent", "label": "Resolved parent", "trait_category": "ECOLOGY"}))
    return path


def test_exact_contract_and_semantic_digest_ignores_provenance(tmp_path):
    path = fixture_tree(tmp_path)
    row = next(adapter.iter_inputs(tmp_path, records=[SOURCE]))
    assert set(row) == {"identifier", "label", "category", "page", "source_path", "text", "text_sha256", "adapter_version"}
    assert row["page"] == PAGE
    assert row["source_path"] == SOURCE
    assert row["text_sha256"] == hashlib.sha256(row["text"].encode("utf-8")).hexdigest()
    assert "REJECTED_SENTINEL" not in row["text"]
    record = copy.deepcopy(RECORD)
    record.update({"curation_history": [{"notes": "PRIVATE_PROVENANCE_SENTINEL"}],
                   "references": [{"reference": "PMID:999999"}],
                   "evidence": [{"snippet": "PRIVATE_PROVENANCE_SENTINEL"}],
                   "notes": "PRIVATE_PROVENANCE_SENTINEL"})
    path.write_text(yaml.safe_dump(record))
    unchanged = next(adapter.iter_inputs(tmp_path, records=[SOURCE]))
    assert unchanged["text_sha256"] == row["text_sha256"]
    assert "PRIVATE_PROVENANCE_SENTINEL" not in unchanged["text"]
    record[LABEL_FIELD] = "A different biological entity"
    path.write_text(yaml.safe_dump(record))
    changed = next(adapter.iter_inputs(tmp_path, records=[SOURCE]))
    assert changed["text_sha256"] != row["text_sha256"]


def test_canary_and_full_keep_identical_semantics(tmp_path):
    fixture_tree(tmp_path)
    full = list(adapter.iter_inputs(tmp_path))
    subset = list(adapter.iter_inputs(tmp_path, records=[SOURCE]))
    assert subset[0] == next(row for row in full if row["source_path"] == SOURCE)
    if adapter.ADAPTER_VERSION.startswith("traitmech-"):
        assert "Resolved parent" in subset[0]["text"]
        assert "METPO:parent" not in subset[0]["text"]
    result = adapter.export_inputs(tmp_path, tmp_path / "records.jsonl", limit=1)
    assert result["records"] == 1 and result["scope"] == "subset"
    result = adapter.export_inputs(tmp_path, None)
    assert result["records"] == len(full) and result["scope"] == "full"


def test_atomic_failure_preserves_previous_output(tmp_path):
    path = fixture_tree(tmp_path)
    output = tmp_path / "records.jsonl"
    output.write_text("previous output")
    broken = path.with_name("zz_broken.yaml")
    broken.write_text("not: [valid YAML")
    with pytest.raises(yaml.YAMLError):
        adapter.export_inputs(tmp_path, output)
    assert output.read_text() == "previous output"
    assert not list(tmp_path.glob(".text-map-*"))


def test_selection_cannot_escape_or_repeat(tmp_path):
    fixture_tree(tmp_path)
    for selection in (["../outside.yaml"], [SOURCE, SOURCE]):
        with pytest.raises(ValueError):
            list(adapter.iter_inputs(tmp_path, records=selection))
    with pytest.raises(ValueError, match="positive"):
        list(adapter.iter_inputs(tmp_path, limit=0))


def test_symlinked_yaml_is_refused(tmp_path):
    path = fixture_tree(tmp_path)
    alias = path.with_name("alias.yaml")
    alias.symlink_to(path)
    with pytest.raises(ValueError, match="symlink"):
        list(adapter.iter_inputs(tmp_path))


def test_distinct_files_can_share_ontology_id_and_tombstones_are_excluded(tmp_path):
    path = fixture_tree(tmp_path)
    sibling = copy.deepcopy(RECORD)
    sibling["preferred_term"] = "Different hydrate"
    path.with_name("other.yaml").write_text(yaml.safe_dump(sibling))
    rejected = copy.deepcopy(RECORD)
    rejected["mapping_status"] = "REJECTED"
    path.with_name("retired.yaml").write_text(yaml.safe_dump(rejected))
    rows = list(adapter.iter_inputs(tmp_path))
    assert len(rows) == 2
    assert len({row["identifier"] for row in rows}) == 2
    assert {row["identifier"] for row in rows} == {"MIM:salt~2Bhydrate", "MIM:other"}



def test_export_round_trip_and_map_sibling_route(tmp_path):
    from urllib.parse import urljoin

    fixture_tree(tmp_path)
    output = tmp_path / "output.jsonl"
    receipt = adapter.export_inputs(tmp_path, output, records=[SOURCE])
    row = json.loads(output.read_text())
    assert receipt["jsonl_sha256"] == hashlib.sha256(output.read_bytes()).hexdigest()
    assert Path(row["source_path"]).suffix == ".yaml"
    assert urljoin("https://example.test/deployment/text-map/index.html", "../" + row["page"]) == "https://example.test/deployment/" + PAGE
