"""The former filename-slug report checks permanent record identity (#1265)."""

import importlib.util
from pathlib import Path

import pytest
import yaml

from mediaingredientmech.stable_ids import (
    LIFECYCLE_PATH, REGISTRY_PATH, Lifecycle, Mint, Registry,
    dump_lifecycle, dump_registry,
)

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "subject_records", ROOT / "scripts/check_sssom_subject_files.py"
)
subject_records = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(subject_records)


@pytest.fixture
def corpus(tmp_path):
    registry = Registry((Mint("MIM:0000001", "Original", "2026-11-08"),))
    (tmp_path / REGISTRY_PATH).parent.mkdir(parents=True)
    (tmp_path / REGISTRY_PATH).write_bytes(dump_registry(registry))
    (tmp_path / LIFECYCLE_PATH).write_bytes(dump_lifecycle(registry))
    record = tmp_path / "data/ingredients/unmapped/Renamed.yaml"
    record.parent.mkdir(parents=True)
    record.write_text(yaml.safe_dump({"mim_id": "MIM:0000001",
                                     "preferred_term": "Corrected label",
                                     "legacy_identifiers": ["MIM:Original"]}))
    sssom = tmp_path / "mappings/ingredient_mappings.sssom.tsv"
    sssom.parent.mkdir()
    return tmp_path, registry, record, sssom


def write_subjects(sssom, *subjects):
    sssom.write_text("subject_id\tobject_id\tpredicate_id\n" + "".join(
        f"{subject}\tCHEBI:1\tskos:exactMatch\n" for subject in subjects
    ))


def test_numeric_subject_survives_filename_and_label_change(corpus, capsys):
    root, _, _, sssom = corpus
    write_subjects(sssom, "MIM:0000001", "MIM:Original")
    assert subject_records.check_subjects(root, sssom) == (
        {"MIM:0000001": "MIM:0000001", "MIM:Original": "MIM:0000001"}, {}
    )
    assert subject_records.main(["--root", str(root)]) == 0
    assert "Resolved through registry and current records: 2" in capsys.readouterr().out


def test_unknown_subject_exits_nonzero_even_with_matching_filename(corpus, capsys):
    root, _, record, sssom = corpus
    record.rename(record.with_name("9999999.yaml"))
    write_subjects(sssom, "MIM:9999999")
    assert subject_records.main(["--root", str(root)]) == 1
    assert "UNKNOWN_SUBJECT" in capsys.readouterr().out


def test_invalid_duplicate_ids_fail_before_subject_resolution(corpus, capsys):
    root, _, record, sssom = corpus
    record.with_name("Duplicate.yaml").write_bytes(record.read_bytes())
    write_subjects(sssom, "MIM:0000001")
    assert subject_records.main(["--root", str(root)]) == 1
    assert "Duplicate MIM ID" in capsys.readouterr().err


def test_retired_subject_follows_registered_replacement(corpus):
    root, registry, record, sssom = corpus
    replacement = Mint("MIM:0000002", "Replacement", "2026-11-08")
    event = Lifecycle("MIM:0000001", "merged", "MIM:0000002",
                      "2026-11-08T01:00:00Z", "Reviewed duplicate")
    registry = Registry((*registry.entries, replacement), (event,))
    (root / REGISTRY_PATH).write_bytes(dump_registry(registry))
    (root / LIFECYCLE_PATH).write_bytes(dump_lifecycle(registry))
    record.write_text(yaml.safe_dump({"mim_id": "MIM:0000002",
                                     "preferred_term": "Replacement"}))
    write_subjects(sssom, "MIM:0000001")
    assert subject_records.check_subjects(root, sssom) == (
        {"MIM:0000001": "MIM:0000002"}, {}
    )


def test_missing_registry_does_not_fall_back_to_filenames(corpus, capsys):
    root, _, _, sssom = corpus
    (root / REGISTRY_PATH).unlink()
    write_subjects(sssom, "MIM:Renamed")
    assert subject_records.main(["--root", str(root)]) == 1
    assert "MIM subject check failed" in capsys.readouterr().err
