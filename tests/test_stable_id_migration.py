"""Bounded #1265 migration preserves scientific facts and refuses partial minting."""
import importlib.util
from pathlib import Path

import pytest
import yaml

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("mint_1265", ROOT / "scripts/adhoc/mint_stable_ids_1265.py")
migration = importlib.util.module_from_spec(spec)
spec.loader.exec_module(migration)
STAMP = "2026-11-08T22:01:42+00:00"


def test_record_retains_mapping_status_and_history():
    old = {"identifier": "UNMAPPED_43", "preferred_term": "A mixture",
           "mapping_status": "UNMAPPED", "curation_history": [{"action": "OLD"}],
           "discussions": [{"note": "keep"}]}
    new = migration.migrate_record(old, "data/ingredients/unmapped/A.yaml", "MIM:0000001", STAMP)
    assert new["identifier"] == "UNMAPPED_43"
    assert new["legacy_identifiers"] == ["MIM:A", "UNMAPPED_43"]
    assert new["mapping_status"] == "UNMAPPED"
    assert new["curation_history"][:-1] == old["curation_history"]
    assert new["curation_history"][-1]["action"] == "ASSIGNED_MIM_ID"
    assert list(new)[-1] == "discussions"
    assert "mim_id" not in old and len(old["curation_history"]) == 1
    with pytest.raises(ValueError, match="already identified"):
        migration.migrate_record(new, "A.yaml", "MIM:0000002", STAMP)


def test_sssom_changes_only_subject_and_prefix():
    before = b'# curie_map:\n#   MIM: "https://old/"\nsubject_id\tobject_id\tnote\nMIM:A\tCHEBI:1\tMIM:A is evidence\n'
    after = migration.migrate_sssom(before, {"MIM:A": "MIM:0000001"})
    assert after.splitlines()[-1] == b'MIM:0000001\tCHEBI:1\tMIM:A is evidence'
    with pytest.raises(KeyError):
        migration.migrate_sssom(before, {})


def test_invalid_last_record_never_writes_live_corpus(tmp_path):
    folder = tmp_path / "data/ingredients/mapped"
    folder.mkdir(parents=True)
    for name, status in [("A", "MAPPED"), ("Z", "BOGUS")]:
        (folder / f"{name}.yaml").write_text(yaml.safe_dump({
            "identifier": "CHEBI:1", "preferred_term": name, "mapping_status": status,
        }))
    originals = {p: p.read_bytes() for p in folder.glob("*.yaml")}
    with pytest.raises(Exception, match="validation failed"):
        migration.prepare(tmp_path, tmp_path / ".temp/stage", STAMP)
    assert all(p.read_bytes() == raw for p, raw in originals.items())
    assert not (tmp_path / migration.REGISTRY_PATH).exists()


def test_staging_refuses_nondurable_and_existing_paths(tmp_path):
    with pytest.raises(ValueError, match="Durable"):
        migration.prepare(tmp_path, tmp_path / "scratch", STAMP)
    stage = tmp_path / ".temp/stage"
    stage.mkdir(parents=True)
    with pytest.raises(ValueError, match="already exists"):
        migration.prepare(tmp_path, stage, STAMP)
