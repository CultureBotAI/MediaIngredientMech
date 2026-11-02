"""Source-specific science preservation and native transaction guards for #313/#235."""

import copy
import importlib.util
import json
import shutil
from contextlib import contextmanager
from pathlib import Path

import pytest
import yaml

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location(
    "step7c_source_writer", ROOT / "scripts/curate_step7c_source_labels.py"
)
writer = importlib.util.module_from_spec(spec)
spec.loader.exec_module(writer)
STAMP = "2026-11-02T22:00:00+00:00"


@pytest.fixture
def originals():
    return writer.frozen_owners()


@pytest.fixture
def proposal(originals):
    return writer.propose_sources(originals, timestamp=STAMP)


@pytest.fixture
def native_runtime():
    pytest.importorskip(
        "kg_microbe_write", reason="Native Claw transaction integration is optional"
    )


@pytest.fixture
def case(tmp_path, originals):
    root = tmp_path.resolve()
    before = {p: originals[p] if p in originals else (ROOT / p).read_bytes() for p in writer.BEFORE}
    for path, data in before.items():
        target = root / path
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(data)
    shutil.copytree(ROOT / writer.REPORT, root / writer.REPORT)
    receipts = root / "receipts"
    receipts.mkdir()
    return root, root / writer.EVIDENCE, receipts / "fixture-source-313-235.json", before


def apply(case, *, enabled=True):
    root, evidence, log, _ = case
    return writer.apply_sources(root, evidence, log, apply=enabled)


def assert_unchanged(case):
    root, _, _, before = case
    assert all((root / p).read_bytes() == b for p, b in before.items())
    assert not (root / writer.NEW).exists()


@pytest.mark.parametrize("path", list(writer.TOKENS))
def test_exact_source_labels_retired_preserving_every_other_scientific_field(
    originals, proposal, path
):
    from mediaingredientmech.synonym_policy import is_resolving_synonym

    old = yaml.safe_load(originals[path])
    new = yaml.safe_load(proposal[path])
    assert new["curation_history"][:-1] == old["curation_history"]
    event = new["curation_history"][-1]
    assert event["timestamp"] == STAMP and event["llm_assisted"] is True
    assert event["previous_status"] == event["new_status"] == "MAPPED"
    assert writer.VERIFICATION[path] in event["changes"]
    assert new["ontology_mapping"]["evidence"][:-1] == old["ontology_mapping"]["evidence"]
    for before, after in zip(old["synonyms"], new["synonyms"], strict=True):
        if before["synonym_text"] in writer.TOKENS[path]:
            assert after == {**before, "synonym_type": "REJECTED_LABEL"}
            assert not is_resolving_synonym(after)
        else:
            assert after == before
    restored = copy.deepcopy(new)
    restored["curation_history"].pop()
    restored["ontology_mapping"]["evidence"].pop()
    restored["synonyms"] = old["synonyms"]
    assert restored == old


def test_fragment_boundaries_and_counts_are_not_reinterpreted(proposal):
    butane = yaml.safe_load(proposal[writer.BUTANEDIOL])
    phosphate = yaml.safe_load(proposal[writer.PHOSPHATE])
    mono = yaml.safe_load(proposal[writer.MONOKETO])
    assert (
        next(s for s in butane["synonyms"] if s["synonym_text"] == "Butane-1,4-diol")[
            "synonym_type"
        ]
        == "RAW_TEXT"
    )
    assert (
        phosphate["identifier"]
        == "kgmicrobe.compound:24-diamino-67-di-iso-propylpteridine_phosphate"
    )
    assert phosphate["ontology_mapping"]["ontology_id"] == "CHEBI:73908"
    assert phosphate["ontology_mapping"]["mapping_quality"] == "NARROW_MATCH"
    assert phosphate["occurrence_statistics"]["source_occurrences"][0]["count"] == 1212
    assert mono["identifier"] == "CHEBI:58143"
    assert mono["occurrence_statistics"]["source_occurrences"][0]["count"] == 288
    assert any(
        "same compound (#213)" in h.get("changes", "") for h in mono["curation_history"][:-1]
    )


def test_phenethylamine_freebase_and_true_beta_alias_survive(proposal):
    new = yaml.safe_load(proposal[writer.PHENETHYLAMINE])
    assert new["identifier"] == new["ontology_mapping"]["ontology_id"] == "CHEBI:18397"
    assert new["chemical_properties"]["cas_rn"] == "64-04-0"
    assert new["chemical_properties"]["molecular_formula"] == "C8H11N"
    assert (
        next(s for s in new["synonyms"] if s["synonym_text"] == "Beta-phenylethylamine")[
            "synonym_type"
        ]
        == "RAW_TEXT"
    )
    assert new["occurrence_statistics"] == {"total_occurrences": 0, "media_count": 0}
    assert (
        "Separate salt-record re-ingestion remains open" in new["curation_history"][-1]["changes"]
    )


def test_new_diketo_has_exact_identity_and_only_two_production_field_occurrences(proposal):
    new = yaml.safe_load(proposal[writer.NEW])
    assert new["identifier"] == new["ontology_mapping"]["ontology_id"] == "CHEBI:11449"
    assert (
        new["preferred_term"]
        == new["ontology_mapping"]["ontology_label"]
        == "2,5-didehydro-D-gluconate"
    )
    assert new["ontology_mapping"]["mapping_quality"] == "EXACT_MATCH"
    assert new["occurrence_statistics"] == {
        "total_occurrences": 0,
        "media_count": 0,
        "source_occurrences": [
            {
                "source": "microbedecoder",
                "count": 2,
                "source_columns": "BacDive_Metabolite_production",
            }
        ],
    }
    assert not any(k in new for k in ("roles", "chemical_properties", "supplied_form"))
    assert new["synonyms"] == [
        {
            "synonym_text": "5-didehydro-D-gluconate",
            "synonym_type": "RAW_TEXT",
            "source": "microbedecoder",
        }
    ]
    assert "blank" in new["ontology_mapping"]["evidence"][0]["notes"]
    assert new["curation_history"][0]["llm_assisted"] is True


def test_recovered_fragment_resolves_only_to_new_diketo_owner(proposal):
    from mediaingredientmech.synonym_policy import is_resolving_synonym

    owners = [yaml.safe_load(proposal[p]) for p in (writer.MONOKETO, writer.NEW)]
    resolving = [
        r["identifier"]
        for r in owners
        for s in r.get("synonyms", [])
        if s["synonym_text"] == "5-didehydro-D-gluconate" and is_resolving_synonym(s)
    ]
    assert resolving == ["CHEBI:11449"]
    assert "damaged-label exception" in owners[1]["curation_history"][-1]["changes"]


def test_saved_independent_sources_count_diketo_separately_without_subtraction():
    directory = ROOT / writer.REPORT / "sources"
    counted = json.loads((directory / "recomputed-gluconate-counts.json").read_bytes())
    expected = {
        ("BacDive_Metabolite_production", "2,5-didehydro-D-gluconate"): 2,
        ("BacDive_Metabolite_production", "5-dehydro-D-gluconate"): 11,
        ("BacDive_Metabolite_utilization", "5-dehydro-D-gluconate"): 277,
    }
    assert len(counted) == 2
    for source in counted:
        assert source["split_delimiter"] == ";"
        assert {(r["column"], r["label"]): r["count"] for r in source["counts"]} == expected
    for filename in ("original-zip-source-extracts.json", "kgmicrobe-raw-source-extracts.json"):
        data = json.loads((directory / filename).read_bytes())
        selected = [
            r for r in data["rows"] if any(m["label"] == writer.NEW_NAME for m in r["matches"])
        ]
        assert {r["BacDive_ID"] for r in selected} == {"34", "58"}
        assert all(
            "5-dehydro-D-gluconate" in r["full_relevant_cells"]["BacDive_Metabolite_production"]
            for r in selected
        )


@pytest.mark.parametrize(
    "stamp", ["2026-11-02T19:00:00+00:00", "2026-11-02T23:00:00", "2026-11-02T23:00:00+01:00"]
)
def test_history_must_follow_evidence_and_explicitly_use_utc(originals, stamp):
    with pytest.raises(ValueError, match="Timestamp"):
        writer.propose_sources(originals, timestamp=stamp)


@pytest.mark.parametrize("path", list(writer.TOKENS))
def test_changed_reviewed_preimages_refused(originals, path):
    originals[path] += b"# unreviewed change\n"
    with pytest.raises(ValueError, match="Reviewed owner changed"):
        writer.propose_sources(originals, timestamp=STAMP)


@pytest.mark.usefixtures("native_runtime")
def test_dry_run_then_complete_native_receipt_with_new_owner_and_exact_noop(case):
    root, _, log, before = case
    result = apply(case, enabled=False)
    assert result["applied"] is False and not log.exists()
    assert not writer.publication._journal_path(log).exists()
    assert_unchanged(case)
    result = apply(case)
    assert result["transaction"]["created"] == [str(root / writer.NEW)]
    saved = json.loads(log.read_bytes())
    assert saved["state"] == "complete" and saved["approval"] == writer.APPROVAL
    assert len(saved["records"]) == 5
    added = next(r for r in saved["records"] if r["shape"] == "new_record")
    assert added["before_yaml_sha256"] is None
    assert added["after_yaml_sha256"] == writer.digest((root / writer.NEW).read_bytes())
    for path, backup in writer.backups(log).items():
        assert backup.read_bytes() == before[path]
    outputs = {p: (root / p).read_bytes() for p in (*writer.TOKENS, writer.NEW)}
    assert apply(case)["changed"] is False
    assert outputs == {p: (root / p).read_bytes() for p in outputs}


@pytest.mark.parametrize("collision", ["log", "backup", "journal", "source_alias"])
@pytest.mark.usefixtures("native_runtime")
def test_reservations_and_aliases_refused_before_any_source_write(case, collision):
    root, _, log, before = case
    occupied = log if collision == "log" else next(iter(writer.backups(log).values()))
    if collision == "journal":
        occupied = writer.publication._journal_path(log)
        occupied.mkdir()
        (occupied / "preserve").write_bytes(b"prior evidence")
    elif collision == "source_alias":
        occupied = log
        occupied.symlink_to(root / writer.BUTANEDIOL)
    else:
        occupied.write_bytes(b"prior evidence")
    with pytest.raises((ValueError, FileExistsError)):
        apply(case)
    assert_unchanged(case)
    if collision in {"log", "backup"}:
        assert occupied.read_bytes() == b"prior evidence"


@pytest.mark.parametrize("corrupt", ["evidence", "manifest", "canonical"])
def test_changed_evidence_and_canonical_anchors_refused_before_writes(case, corrupt):
    root, evidence, _, before = case
    path = (
        root / writer.REPORT / "sources/pubchem-9075-properties.json"
        if corrupt == "evidence"
        else evidence if corrupt == "manifest" else root / writer.SSSOM
    )
    altered = path.read_bytes() + b"\n"
    path.write_bytes(altered)
    with pytest.raises(ValueError, match="changed|differs"):
        apply(case, enabled=False)
    assert all((root / p).read_bytes() == b for p, b in before.items() if root / p != path)
    assert not (root / writer.NEW).exists()


@pytest.mark.parametrize("kind", ["identity", "mapping", "symlink"])
def test_ignored_nested_duplicate_or_alias_cannot_hide_from_preflight(case, kind):
    root, _, _, _ = case
    path = root / "data/ingredients/mapped/.ignored/duplicate.yaml"
    path.parent.mkdir()
    if kind == "symlink":
        path.symlink_to(root / writer.MONOKETO)
    else:
        duplicate = {
            "identifier": writer.NEW_ID if kind == "identity" else "UNMAPPED_9999",
            "mapping_status": "MAPPED",
            "preferred_term": "duplicate",
            "ontology_mapping": {"ontology_id": writer.NEW_ID},
        }
        path.write_text(yaml.safe_dump(duplicate))
    with pytest.raises(ValueError, match="Destination identity|aliased"):
        apply(case, enabled=False)
    assert_unchanged(case)


@pytest.mark.usefixtures("native_runtime")
def test_owner_race_after_receipt_reservation_preserves_competing_content(case, monkeypatch):
    root, _, _, before = case
    reserve = writer.guarded.reserve_receipt_outputs
    competing = before[writer.MONOKETO] + b"# another owner changed this\n"

    @contextmanager
    def raced(*args, **kwargs):
        with reserve(*args, **kwargs) as handles:
            (root / writer.MONOKETO).write_bytes(competing)
            yield handles

    monkeypatch.setattr(writer.guarded, "reserve_receipt_outputs", raced)
    with pytest.raises(ValueError, match="frozen input changed"):
        apply(case)
    assert (root / writer.MONOKETO).read_bytes() == competing
    assert all((root / p).read_bytes() == b for p, b in before.items() if p != writer.MONOKETO)
    assert not (root / writer.NEW).exists()


@pytest.mark.usefixtures("native_runtime")
def test_partial_io_failure_preserves_exact_rollback_evidence_and_refuses_partial_replay(
    case, monkeypatch
):
    from kg_microbe_write import transaction

    root, _, log, before = case
    replace = transaction._atomic_replace

    def fail_after_created_record(path, text):
        if path == root / writer.MONOKETO:
            raise OSError("injected fourth-output failure")
        return replace(path, text)

    monkeypatch.setattr(transaction, "_atomic_replace", fail_after_created_record)
    with pytest.raises(Exception, match="write failed after"):
        apply(case)
    saved = json.loads(log.read_bytes())
    assert saved["state"] == "failed" and saved["recovery_required"] is True
    journal = next(Path(saved["journal_directory"]).glob("write-*.json"))
    payload = json.loads(journal.read_bytes())
    assert payload["status"] == "in_progress"
    assert payload["created"] == [str(root / writer.NEW)]
    assert transaction.recover(journal) == {
        str(root / p): before[p].decode() for p in writer.TOKENS
    }
    with pytest.raises(ValueError, match="Partial or changed"):
        apply(case)
    # Exercise recovery only on isolated fixtures, using the journal's exact prior
    # bytes and created-path list. Production recovery needs separate ownership review.
    for path, content in transaction.recover(journal).items():
        Path(path).write_text(content)
    for path in payload["created"]:
        Path(path).unlink(missing_ok=True)
    assert_unchanged(case)


@pytest.mark.parametrize("corrupt", ["new_owner", "receipt", "journal", "backup"])
@pytest.mark.usefixtures("native_runtime")
def test_completed_noop_requires_full_receipt_preimages_and_creation_journal(case, corrupt):
    root, _, log, _ = case
    apply(case)
    saved = json.loads(log.read_bytes())
    if corrupt == "new_owner":
        path = root / writer.NEW
        data = yaml.safe_load(path.read_bytes())
        data["occurrence_statistics"]["source_occurrences"][0]["count"] = 6
        path.write_text(yaml.safe_dump(data))
    elif corrupt == "receipt":
        saved["transaction"]["created"] = []
        log.write_text(json.dumps(saved))
    elif corrupt == "journal":
        path = Path(saved["transaction"]["journal"])
        data = json.loads(path.read_bytes())
        data["created"] = []
        path.write_text(json.dumps(data))
    else:
        next(iter(writer.backups(log).values())).write_bytes(b"changed preimage")
    with pytest.raises(ValueError):
        apply(case)
