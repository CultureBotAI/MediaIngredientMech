"""#1111 reads archived result icons and supersedes only the active false note."""

import copy
import importlib.util
import json
from contextlib import contextmanager
from pathlib import Path

import pytest
import yaml

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location(
    "diketo_evidence_correction", ROOT / "scripts/correct_diketo_bacdive_evidence.py"
)
writer = importlib.util.module_from_spec(spec)
spec.loader.exec_module(writer)
STAMP = "2026-11-02T22:30:00+00:00"


@pytest.mark.parametrize(
    "cell,value",
    [
        ('<i class="ph ph-x text-danger" alt="No" title="No"></i>', "No"),
        ('<i class="ph ph-check text-success" alt="Yes" title="Yes"></i>', "Yes"),
        ("", None),
        (" &nbsp; ", None),
        ("No", "No"),
        ("Yes", "Yes"),
    ],
)
def test_result_icons_distinguish_no_yes_and_genuinely_absent_information(cell, value):
    assert writer.production_result(cell) == value


@pytest.mark.parametrize(
    "cell",
    [
        '<i class="ph ph-x text-danger" alt="No" title="Yes"></i>',
        '<i class="ph ph-x text-danger" alt="No"></i>',
        '<i class="ph ph-check text-success" alt="No" title="No"></i>',
        '<i class="ph ph-x text-danger" alt="No" title="No"></i>Yes',
        '<i class="ph ph-x text-danger" alt="No" title="No"></i><i></i>',
        "uninterpreted result",
    ],
)
def test_ambiguous_or_conflicting_result_information_is_not_called_absent(cell):
    with pytest.raises(ValueError):
        writer.production_result(cell)


@pytest.mark.parametrize("sid", [34, 58])
def test_archived_primary_table_headers_bind_diketo_no_and_monoketo_yes(sid):
    raw = (ROOT / writer.SOURCE_DIRECTORY / f"bacdive-{sid}.html").read_bytes()
    assert writer.production_rows(raw) == {writer.NAME: "No", writer.CONTROL: "Yes"}
    with pytest.raises(ValueError, match="headers changed"):
        writer.production_rows(raw.replace(b"<th>Production</th>", b"<th>Utilization</th>"))
    with pytest.raises(ValueError, match="ChEBI identity"):
        writer.production_rows(raw.replace(b"chebiId=CHEBI:11449", b"chebiId=CHEBI:99999"))


def test_active_note_is_corrected_and_original_history_and_all_science_are_preserved():
    original = writer.frozen()
    before = yaml.safe_load(original)
    output = writer.propose_sources({writer.OWNER: original}, timestamp=STAMP)
    after = yaml.safe_load(output[writer.OWNER])
    old_note = before["ontology_mapping"]["evidence"][0]["notes"]
    new_note = after["ontology_mapping"]["evidence"][0]["notes"]
    assert writer.OLD_SENTENCE in old_note
    assert writer.OLD_SENTENCE not in new_note
    assert "explicitly No" in new_note
    assert after["curation_history"][:-1] == before["curation_history"]
    assert "values are blank" in after["curation_history"][0]["changes"]
    event = after["curation_history"][-1]
    assert event["action"] == "CORRECTED_SOURCE_EVIDENCE_NOTE"
    assert "incorrect and is superseded" in event["changes"]
    assert event["llm_assisted"] is True and event["timestamp"] == STAMP
    restored = copy.deepcopy(after)
    restored["ontology_mapping"]["evidence"][0]["notes"] = old_note
    restored["curation_history"].pop()
    assert restored == before
    assert after["identifier"] == "CHEBI:11449"
    assert after["occurrence_statistics"]["source_occurrences"] == [
        {"source": "microbedecoder", "count": 2, "source_columns": "BacDive_Metabolite_production"}
    ]
    assert after["synonyms"] == [
        {
            "synonym_text": "5-didehydro-D-gluconate",
            "synonym_type": "RAW_TEXT",
            "source": "microbedecoder",
        }
    ]
    assert "roles" not in after
    assert writer.verify_complete(output) == STAMP


@pytest.mark.parametrize("kind", ["identity", "count", "alias", "history", "note"])
def test_partial_or_modified_completion_is_refused(kind):
    current = writer.propose_sources({writer.OWNER: writer.frozen()}, timestamp=STAMP)
    value = yaml.safe_load(current[writer.OWNER])
    if kind == "identity":
        value["identifier"] = "CHEBI:58143"
    elif kind == "count":
        value["occurrence_statistics"]["source_occurrences"][0]["count"] = 6
    elif kind == "alias":
        value["synonyms"][0]["synonym_type"] = "REJECTED_LABEL"
    elif kind == "history":
        value["curation_history"][0]["changes"] = "rewritten history"
    else:
        value["ontology_mapping"]["evidence"][0]["notes"] = "No"
    with pytest.raises(ValueError, match="Partial or changed"):
        writer.verify_complete({writer.OWNER: yaml.safe_dump(value).encode()})


@pytest.fixture
def native_runtime():
    pytest.importorskip(
        "kg_microbe_write", reason="Native Claw transaction integration is optional"
    )


@pytest.fixture
def case(tmp_path):
    root = tmp_path.resolve()
    for name in [str(writer.MANIFEST), *writer.META["files"], *writer.META["protected_anchors"]]:
        target = root / name
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes((ROOT / name).read_bytes())
    owner = root / writer.OWNER
    owner.parent.mkdir(parents=True, exist_ok=True)
    owner.write_bytes(writer.frozen())
    receipts = root / "receipts"
    receipts.mkdir()
    return root, receipts / "fixture-diketo-correction-1111.json"


@pytest.mark.usefixtures("native_runtime")
def test_native_dry_run_reserved_source_receipt_and_exact_completed_replay(case):
    root, log = case
    before = (root / writer.OWNER).read_bytes()
    assert writer.apply_sources(root, log)["applied"] is False
    assert not log.exists() and (root / writer.OWNER).read_bytes() == before
    writer.apply_sources(root, log, apply=True)
    saved = json.loads(log.read_bytes())
    assert saved["state"] == "complete" and saved["approval"] == writer.APPROVAL
    assert saved["records"][0]["shape"] == "source_evidence_note_correction"
    assert saved["records"][0]["before_yaml_sha256"] == writer.META["owner_sha256"]
    assert writer.backups(log)[writer.OWNER].read_bytes() == before
    assert writer.apply_sources(root, log, apply=True)["changed"] is False
    writer.source_receipt(root, log)


@pytest.mark.parametrize("occupied", ["log", "backup", "journal", "alias"])
@pytest.mark.usefixtures("native_runtime")
def test_existing_evidence_or_alias_refuses_before_owner_mutation(case, occupied):
    root, log = case
    path = log if occupied in {"log", "alias"} else writer.backups(log)[writer.OWNER]
    if occupied == "journal":
        path = writer.publication._journal_path(log)
        path.mkdir()
    elif occupied == "alias":
        path.symlink_to(root / writer.OWNER)
    else:
        path.write_bytes(b"preserve existing evidence")
    with pytest.raises((ValueError, FileExistsError)):
        writer.apply_sources(root, log, apply=True)
    assert (root / writer.OWNER).read_bytes() == writer.frozen()
    if occupied in {"log", "backup"}:
        assert path.read_bytes() == b"preserve existing evidence"


@pytest.mark.parametrize("changed", ["owner", "capture", "historical_writer", "anchor"])
def test_modified_preconditions_never_write_owner(case, changed):
    root, log = case
    paths = {
        "owner": root / writer.OWNER,
        "capture": root / writer.SOURCE_DIRECTORY / "bacdive-34.html",
        "historical_writer": root / "scripts/curate_step7c_source_labels.py",
        "anchor": root / "UNIFIED_INGREDIENT_MAPPING.tsv",
    }
    path = paths[changed]
    path.write_bytes(path.read_bytes() + b"\n")
    owner = (root / writer.OWNER).read_bytes()
    with pytest.raises((ValueError, FileNotFoundError)):
        writer.apply_sources(root, log)
    assert (root / writer.OWNER).read_bytes() == owner and not log.exists()


@pytest.mark.usefixtures("native_runtime")
def test_race_after_receipt_reservation_preserves_competing_owner(case, monkeypatch):
    root, log = case
    reserve = writer.guarded.reserve_receipt_outputs
    competing = writer.frozen() + b"# competing owner edit\n"

    @contextmanager
    def raced(*args, **kwargs):
        with reserve(*args, **kwargs) as handles:
            (root / writer.OWNER).write_bytes(competing)
            yield handles

    monkeypatch.setattr(writer.guarded, "reserve_receipt_outputs", raced)
    with pytest.raises(ValueError, match="frozen input changed"):
        writer.apply_sources(root, log, apply=True)
    assert (root / writer.OWNER).read_bytes() == competing
