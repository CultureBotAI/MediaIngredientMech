"""Bounded #1265 migration preserves scientific facts and refuses partial minting."""
import importlib.util
import subprocess
import sys
from pathlib import Path
from types import SimpleNamespace

import pytest
import yaml

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("mint_1265", ROOT / "scripts/adhoc/mint_stable_ids_1265.py")
migration = importlib.util.module_from_spec(spec)
spec.loader.exec_module(migration)
STAMP = "2026-11-08T22:01:42+00:00"


def freeze_source(root, monkeypatch):
    """Give bounded migration fixtures a real immutable Git inventory."""
    subprocess.run(["git", "init", "--quiet", str(root)], check=True)
    subprocess.run(["git", "add", "."], cwd=root, check=True)
    subprocess.run(
        ["git", "-c", "user.name=Migration Test", "-c", "user.email=test@example.invalid",
         "-c", "commit.gpgsign=false", "commit", "--quiet", "-m", "Frozen synthetic source"],
        cwd=root, check=True,
    )
    commit = subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=root, text=True).strip()
    monkeypatch.setattr(migration, "SOURCE_COMMIT", commit)


@pytest.fixture
def frozen_corpus(tmp_path, monkeypatch):
    for group, name, identifier, status in [
        ("mapped", "A", "CHEBI:1", "MAPPED"),
        ("unmapped", "Z", "UNMAPPED_43", "UNMAPPED"),
    ]:
        folder = tmp_path / "data/ingredients" / group
        folder.mkdir(parents=True)
        (folder / f"{name}.yaml").write_text(yaml.safe_dump({
            "identifier": identifier, "preferred_term": name, "mapping_status": status,
        }))
    sssom = tmp_path / migration.SSSOM
    sssom.parent.mkdir(parents=True)
    # The unmapped owner has no SSSOM row: SSSOM alone cannot detect its omission.
    sssom.write_bytes(b'# curie_map:\n#   MIM: "https://old/"\nsubject_id\tobject_id\nMIM:A\tCHEBI:1\n')
    freeze_source(tmp_path, monkeypatch)
    return tmp_path


def alter_inventory(root, change):
    owner = root / "data/ingredients/unmapped/Z.yaml"
    if change == "missing":
        owner.unlink()
    else:
        (owner.parent / "Extra.yaml").write_bytes(owner.read_bytes())


@pytest.mark.parametrize("change", ["missing", "extra"])
def test_inventory_mismatch_refused_before_any_staging_write(frozen_corpus, monkeypatch, change):
    root = frozen_corpus
    alter_inventory(root, change)
    calls = []
    writer = migration.write_validated_ingredient

    def observe(*args, **kwargs):
        calls.append(args[1])
        return writer(*args, **kwargs)

    monkeypatch.setattr(migration, "write_validated_ingredient", observe)
    stage = root / ".temp/stage"
    with pytest.raises(ValueError, match="Complete record inventory differs"):
        migration.prepare(root, stage, STAMP)
    assert calls == []
    assert not stage.exists()
    assert not (root / migration.REGISTRY_PATH).exists()


@pytest.mark.parametrize("change", ["missing", "extra"])
def test_inventory_change_after_prepare_refused_before_transaction(frozen_corpus, monkeypatch, change):
    root = frozen_corpus
    stage = root / ".temp/stage"
    inputs, outputs, manifest = migration.prepare(root, stage, STAMP)
    assert len(manifest["records"]) == 2
    alter_inventory(root, change)
    calls = []

    def forbidden_transaction(*args, **kwargs):
        calls.append((args, kwargs))
        pytest.fail("Inventory refusal must precede the publication transaction")

    monkeypatch.setitem(sys.modules, "kg_microbe_write", SimpleNamespace(
        ValidatedWriteTransaction=forbidden_transaction,
    ))
    with pytest.raises(ValueError, match="Complete record inventory differs"):
        migration.publish(root, stage, inputs, outputs, apply=False)
    assert calls == []
    assert not (root / migration.REGISTRY_PATH).exists()


def test_complete_direct_inventory_prepares_every_owner(frozen_corpus, monkeypatch):
    root = frozen_corpus
    auxiliary = root / "data/ingredients/mapped/notes/not-an-owner.yaml"
    auxiliary.parent.mkdir()
    auxiliary.write_text("note: retained auxiliary data\n")
    freeze_source(root, monkeypatch)
    originals = {
        path.relative_to(root).as_posix(): path.read_bytes()
        for group in ("mapped", "unmapped")
        for path in (root / "data/ingredients" / group).glob("*.yaml")
    }
    inputs, outputs, manifest = migration.prepare(root, root / ".temp/stage", STAMP)
    assert {row["path"] for row in manifest["records"]} == set(originals)
    assert len(manifest["records"]) == 2
    assert all(inputs[name] == raw == (root / name).read_bytes() for name, raw in originals.items())
    assert all(name in outputs for name in originals)
    assert not (root / migration.REGISTRY_PATH).exists()


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


def test_invalid_last_record_never_writes_live_corpus(tmp_path, monkeypatch):
    folder = tmp_path / "data/ingredients/mapped"
    folder.mkdir(parents=True)
    for name, status in [("A", "MAPPED"), ("Z", "BOGUS")]:
        (folder / f"{name}.yaml").write_text(yaml.safe_dump({
            "identifier": "CHEBI:1", "preferred_term": name, "mapping_status": status,
        }))
    originals = {p: p.read_bytes() for p in folder.glob("*.yaml")}
    freeze_source(tmp_path, monkeypatch)
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
