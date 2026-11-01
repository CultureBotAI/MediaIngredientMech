"""The #882 hydrate split must not reuse retired placeholders (#1021)."""

import copy
import importlib.util
import sys
from pathlib import Path

import pytest
import yaml

ROOT = Path(__file__).parents[1]
SCRIPT = ROOT / "scripts/fix_merge_tombstone_resolution.py"
ALLOCATIONS = {
    "Na2moo4_X_H2o": ("UNMAPPED_0851", "UNMAPPED_0819"),
    "Trisodium_Citrate_X_3_H2o": ("UNMAPPED_0852", "UNMAPPED_0820"),
}


@pytest.fixture
def producer(monkeypatch):
    spec = importlib.util.spec_from_file_location("tombstone_repair_1021", SCRIPT)
    module = importlib.util.module_from_spec(spec)
    monkeypatch.setitem(sys.modules, spec.name, module)
    spec.loader.exec_module(module)
    return module


@pytest.mark.parametrize("slug,allocation", ALLOCATIONS.items())
def test_persisted_split_preserves_history_and_avoids_retired_id(slug, allocation):
    allocated, retired = allocation
    record = yaml.safe_load((ROOT / "data/ingredients/unmapped" / f"{slug}.yaml").read_text())
    assert record["identifier"] == allocated
    assert record["mapping_status"] == "UNMAPPED"
    assert "ontology_mapping" not in record
    assert record["curation_history"][0]["action"] == "CREATED_AS_UNMAPPED"
    correction = next(
        event for event in record["curation_history"]
        if event["action"] == "CORRECTED_IDENTIFIER" and "#1021" in event["changes"]
    )
    assert retired in correction["changes"] and allocated in correction["changes"]
    assert "#1021" in correction["changes"]


def test_producer_recreation_uses_fresh_placeholders(producer, tmp_path, monkeypatch):
    monkeypatch.setattr(producer, "TARGETS", ())
    monkeypatch.setattr(producer, "UNMAPPED_DIR", tmp_path)
    assert producer.main(["--apply"]) == 0
    for slug, (allocated, retired) in ALLOCATIONS.items():
        record = yaml.safe_load((tmp_path / f"{slug}.yaml").read_text())
        assert record["identifier"] == allocated, f"{slug} must not recreate retired {retired}"
        assert record["mapping_status"] == "UNMAPPED"
        assert "ontology_mapping" not in record


def test_second_required_repair_preserves_history_and_then_is_idempotent(producer, tmp_path, monkeypatch):
    """A later repair adds evidence instead of deleting the earlier repair (#1022)."""
    repair = producer.TARGETS[0]
    record_path = ROOT / "data/ingredients/mapped" / f"{repair.slug}.yaml"
    record = yaml.safe_load(record_path.read_text())
    assert record["curation_history"][-1]["action"] == "REPAIRED_TOMBSTONE_RESOLUTION"
    history = copy.deepcopy(record["curation_history"])
    record.pop("representative")
    source = tmp_path / f"{repair.slug}.yaml"
    source.write_text(yaml.safe_dump(record, sort_keys=False))
    target = tmp_path / f"{repair.target_slug}.yaml"
    target.write_bytes((ROOT / "data/ingredients/mapped" / target.name).read_bytes())
    monkeypatch.setattr(producer, "MAPPED_DIR", tmp_path)
    monkeypatch.setattr(producer, "TARGETS", (repair,))
    monkeypatch.setattr(producer, "UNMAPPED_HYDRATE_SPECS", ())

    assert producer.main(["--apply"]) == 0
    repaired = yaml.safe_load(source.read_text())
    assert repaired["curation_history"][:-1] == history
    assert repaired["curation_history"][-1]["action"] == "REPAIRED_TOMBSTONE_RESOLUTION"
    assert repaired["representative"] == repair.representative

    after = source.read_bytes()
    assert producer.main(["--apply"]) == 0
    assert source.read_bytes() == after


@pytest.mark.parametrize("slug,wrong_id", [("Na-glutamate", "CHEBI:29984"), ("Sodium_Citrate", "CHEBI:63041")])
def test_future_repair_uses_corrected_synonym_rationale(producer, tmp_path, monkeypatch, slug, wrong_id):
    """A future necessary repair must not repeat the false ontology citations (#1023)."""
    repair = next(spec for spec in producer.TARGETS if spec.slug == slug)
    record = yaml.safe_load((ROOT / "data/ingredients/mapped" / f"{slug}.yaml").read_text())
    history = copy.deepcopy(record["curation_history"])
    record.pop("representative")
    source = tmp_path / f"{slug}.yaml"
    source.write_text(yaml.safe_dump(record, sort_keys=False))
    target = tmp_path / f"{repair.target_slug}.yaml"
    target.write_bytes((ROOT / "data/ingredients/mapped" / target.name).read_bytes())
    monkeypatch.setattr(producer, "MAPPED_DIR", tmp_path)
    monkeypatch.setattr(producer, "TARGETS", (repair,))
    monkeypatch.setattr(producer, "UNMAPPED_HYDRATE_SPECS", ())

    assert producer.main(["--apply"]) == 0
    repaired = yaml.safe_load(source.read_text())
    assert repaired["curation_history"][:-1] == history
    changes = repaired["curation_history"][-1]["changes"]
    assert wrong_id not in changes
    if slug == "Na-glutamate":
        assert "CHEBI:29988" in changes and "L-glutamate(2-)" in changes
    else:
        assert "stoichiometry" in changes and "Na2citrate" in changes


@pytest.mark.parametrize("slug,wrong_id,representative", [
    ("Na-glutamate", "CHEBI:29984", "CHEBI:64243"),
    ("Sodium_Citrate", "CHEBI:63041", "CHEBI:32142"),
])
def test_provenance_correction_retains_original_repair(slug, wrong_id, representative):
    record = yaml.safe_load((ROOT / "data/ingredients/mapped" / f"{slug}.yaml").read_text())
    history = record["curation_history"]
    original = next(event for event in history if event["action"] == "REPAIRED_TOMBSTONE_RESOLUTION"
                    and wrong_id in event["changes"])
    correction = next(event for event in history if event["action"] == "CORRECTED_PROVENANCE"
                      and "#1023" in event["changes"])
    assert history.index(original) < history.index(correction)
    assert "https://www.ebi.ac.uk/chebi/" in correction["changes"]
    assert "new_status" not in correction
    assert record["identifier"] == record["representative"] == representative
    assert record["mapping_status"] == "REJECTED"
    retired = {synonym["synonym_text"] for synonym in record["synonyms"]
               if synonym["synonym_type"] == "REJECTED_LABEL"}
    if slug == "Na-glutamate":
        assert {"(2S)-2-aminopentanedioate", "L-glutamic acid dianion"} <= retired
        assert "CHEBI:29988" in correction["changes"]
    else:
        assert "Na2citrate" in retired
        assert "manganese(II) chloride" in correction["changes"]
