"""#1149: exact source spelling cannot widen identity or bypass receipt preflight."""

import importlib.util
import sys
from pathlib import Path

import pytest
import yaml

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "acetate_alias", ROOT / "scripts/curate_mediadive_acetate_alias.py"
)
writer = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(writer)
EVIDENCE = ROOT / "reports/kgm_unmapped_chemicals_20261107/sodium-acetate/sources"
BEFORE = ROOT / "reports/kgm_unmapped_chemicals_20261107/sodium-acetate/write/owner-before.yaml"


def sources():
    return {name: (EVIDENCE / name).read_bytes() for name in writer.EVIDENCE}


def test_only_source_alias_and_one_history_event_change():
    before = yaml.safe_load(BEFORE.read_bytes())
    after = writer.prepare(BEFORE.read_bytes(), sources(), "2026-11-08T00:00:00+00:00")
    assert after.pop("synonyms") == before.pop("synonyms") + [
        {
            "synonym_text": "Na acetate x 3 H2O",
            "synonym_type": "HYDRATE_FORM",
            "source": writer.SOURCE,
        }
    ]
    new_history = after.pop("curation_history")
    old_history = before.pop("curation_history")
    assert new_history[:-1] == old_history
    assert new_history[-1]["llm_assisted"] is True
    assert new_history[-1]["previous_status"] == new_history[-1]["new_status"] == "MAPPED"
    assert after == before  # all chemistry, identity, roles and measured counts stay exact


def test_changed_owner_or_primary_capture_refused():
    with pytest.raises(ValueError, match="Owner differs"):
        writer.prepare(BEFORE.read_bytes().replace(b"CHEBI:32138", b"CHEBI:32954"), sources())
    changed = sources()
    changed["mediadive-1315.json"] = changed["mediadive-1315.json"].replace(
        b"6131-90-4", b"127-09-3"
    )
    with pytest.raises(ValueError, match="Primary evidence differs"):
        writer.prepare(BEFORE.read_bytes(), changed)


@pytest.mark.parametrize("collision", ["owner-before.yaml", "apply-log.json"])
def test_receipt_collision_prevents_owner_write(tmp_path, monkeypatch, collision):
    owner = tmp_path / writer.OWNER
    owner.parent.mkdir(parents=True)
    owner.write_bytes(BEFORE.read_bytes())
    receipts = tmp_path / "receipts"
    receipts.mkdir()
    (receipts / collision).write_text("unrelated evidence")
    monkeypatch.setattr(
        sys,
        "argv",
        [
            "writer",
            "--root",
            str(tmp_path),
            "--evidence",
            str(EVIDENCE),
            "--receipt-dir",
            str(receipts),
            "--apply",
        ],
    )
    with pytest.raises(FileExistsError):
        writer.main()
    assert owner.read_bytes() == BEFORE.read_bytes()
    assert (receipts / collision).read_text() == "unrelated evidence"


def test_symlink_receipt_parent_prevents_owner_write(tmp_path, monkeypatch):
    owner = tmp_path / writer.OWNER
    owner.parent.mkdir(parents=True)
    owner.write_bytes(BEFORE.read_bytes())
    actual = tmp_path / "actual"
    actual.mkdir()
    alias = tmp_path / "alias"
    alias.symlink_to(actual, target_is_directory=True)
    monkeypatch.setattr(
        sys,
        "argv",
        [
            "writer",
            "--root",
            str(tmp_path),
            "--evidence",
            str(EVIDENCE),
            "--receipt-dir",
            str(alias / "receipts"),
            "--apply",
        ],
    )
    with pytest.raises(ValueError, match="alias refused"):
        writer.main()
    assert owner.read_bytes() == BEFORE.read_bytes()
    assert not list(actual.iterdir())
