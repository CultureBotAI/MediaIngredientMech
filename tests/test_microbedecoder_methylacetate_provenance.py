"""#1151: correct disproven origin speculation without inventing a chemical identity."""

import importlib.util
from pathlib import Path

import pytest
import yaml

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "methylacetate_provenance", ROOT / "scripts/correct_microbedecoder_methylacetate_provenance.py"
)
writer = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(writer)
EVIDENCE = ROOT / "reports/kgm_unmapped_chemicals_20261107/methylacetate/sources"
BEFORE = EVIDENCE / "owner-reviewed-before.yaml"
SOURCE = EVIDENCE / "microbedecoder-raw-record19685.csv"


def test_1151_only_active_notes_and_one_history_event_change():
    before = yaml.safe_load(BEFORE.read_bytes())
    after = writer.prepare(BEFORE.read_bytes(), SOURCE.read_bytes(), "2026-11-08T00:00:00+00:00")
    assert after.pop("notes") == writer.NEW_NOTES
    assert "likely original" in before.pop("notes")
    history = after.pop("curation_history")
    assert history[:-1] == before.pop("curation_history")
    assert history[-1]["previous_status"] == history[-1]["new_status"] == "REJECTED"
    assert history[-1]["llm_assisted"] is True
    assert after == before
    assert "ontology_mapping" not in after
    assert "3-methyl mercaptopropionate reconstruction are unsupported" in writer.NEW_NOTES


@pytest.mark.parametrize("target", ["owner", "source"])
def test_1151_changed_source_or_owner_refused(target):
    owner, source = BEFORE.read_bytes(), SOURCE.read_bytes()
    if target == "owner":
        owner = owner.replace(b"REJECTED", b"UNMAPPED")
    else:
        source = source.replace(b"3-methylacetate", b"3-methyl mercaptopropionate")
    with pytest.raises(ValueError, match="differs"):
        writer.prepare(owner, source)


def fixture_owner(root):
    owner = root / writer.OWNER
    owner.parent.mkdir(parents=True)
    owner.write_bytes(BEFORE.read_bytes())
    return owner


@pytest.mark.parametrize("collision", ["owner-before.yaml", "apply-log.json"])
def test_1151_occupied_receipt_outputs_refuse_before_write(tmp_path, collision):
    owner = fixture_owner(tmp_path)
    receipts = tmp_path / "receipts"
    receipts.mkdir()
    (receipts / collision).write_text("unrelated evidence")
    with pytest.raises(FileExistsError):
        writer.publish(tmp_path, SOURCE, receipts, apply=True)
    assert owner.read_bytes() == BEFORE.read_bytes()
    assert (receipts / collision).read_text() == "unrelated evidence"


@pytest.mark.parametrize("kind", ["source_symlink", "source_hardlink", "receipt_parent_symlink"])
def test_1151_aliases_refuse_before_write(tmp_path, kind):
    owner = fixture_owner(tmp_path)
    receipts = tmp_path / "receipts"
    source = tmp_path / "source.csv"
    if kind == "source_symlink":
        source.symlink_to(SOURCE)
    elif kind == "source_hardlink":
        original = tmp_path / "original.csv"
        original.write_bytes(SOURCE.read_bytes())
        source.hardlink_to(original)
    else:
        source.write_bytes(SOURCE.read_bytes())
        actual = tmp_path / "actual"
        actual.mkdir()
        receipts.symlink_to(actual, target_is_directory=True)
    with pytest.raises(ValueError, match="alias"):
        writer.publish(tmp_path, source, receipts, apply=True)
    assert owner.read_bytes() == BEFORE.read_bytes()


def test_1151_dry_run_is_noop_and_native_apply_records_exact_preimage(tmp_path):
    owner = fixture_owner(tmp_path)
    receipts = tmp_path / "receipts"
    assert writer.publish(tmp_path, SOURCE, receipts)["apply"] is False
    assert not receipts.exists()
    assert owner.read_bytes() == BEFORE.read_bytes()
    writer.publish(tmp_path, SOURCE, receipts, apply=True)
    assert (receipts / "owner-before.yaml").read_bytes() == BEFORE.read_bytes()
    after = yaml.safe_load(owner.read_bytes())
    assert after["notes"] == writer.NEW_NOTES
    assert after["mapping_status"] == "REJECTED"
    import json

    log = json.loads((receipts / "apply-log.json").read_text())["records"]
    assert len(log) == 1 and log[0]["shape"] == "source_provenance_note"
    assert log[0]["before_yaml_sha256"] == writer.BEFORE
    assert log[0]["after_yaml_sha256"] == writer.sha(owner.read_bytes())
    with pytest.raises(ValueError, match="Owner differs"):
        writer.publish(tmp_path, SOURCE, tmp_path / "repeat", apply=True)
