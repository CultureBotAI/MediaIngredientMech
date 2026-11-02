"""Exact six-owner scope and native transaction regressions for #870."""

import copy
import importlib.util
import json
import os
import shutil
from contextlib import contextmanager
from pathlib import Path

import pytest
import yaml

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "remove_stale_nodes", ROOT / "scripts/remove_stale_kg_microbe_nodes.py"
)
mod = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(mod)
STAMP = "2030-01-02T00:00:00+00:00"


@pytest.fixture
def native_runtime():
    """Only actual publication/recovery cases need the optional Claw package (#1085)."""
    return pytest.importorskip("kg_microbe_write", reason="Real native transaction required")


@pytest.fixture
def before():
    return {p: mod.frozen(p) for p in mod.OWNERS}


@pytest.fixture
def case(tmp_path, before):
    root = tmp_path.resolve() / "mim"
    root.mkdir()
    shutil.copytree(ROOT / mod.REPORT, root / mod.REPORT)
    originals = before | {p: (ROOT / p).read_bytes() for p in mod.ANCHORS}
    for p, data in originals.items():
        (root / p).parent.mkdir(parents=True, exist_ok=True)
        (root / p).write_bytes(data)
    log = tmp_path.resolve() / "receipts/source.json"
    log.parent.mkdir()
    return root, log, originals


def assert_owners_unchanged(case):
    root, _, originals = case
    assert all((root / p).read_bytes() == originals[p] for p in mod.OWNERS)


def test_exact_six_proposals_preserve_all_other_fields_and_history(before):
    originals = copy.deepcopy(before)
    proposed = mod.propose_sources(before, timestamp=STAMP)
    assert before == originals and set(proposed) == set(before)
    for p, data in proposed.items():
        old, new = yaml.safe_load(before[p]), yaml.safe_load(data)
        assert "kg_microbe_node_id" not in new
        assert new["curation_history"][:-1] == old["curation_history"]
        assert len(new["curation_history"]) == len(old["curation_history"]) + 1
        for key in old.keys() - {"kg_microbe_node_id", "curation_history"}:
            assert new[key] == old[key]
        assert set(new) == set(old) - {"kg_microbe_node_id"}
        event = new["curation_history"][-1]
        assert event["previous_status"] == event["new_status"] == old["mapping_status"]
        assert event["action"] == mod.ACTION and event["llm_assisted"] is True
        assert event["llm_model"] == "gpt-6" and event["curator"] == "Codex"
        assert mod.MANIFEST_SHA in event["changes"]
    fish = next(p for p in proposed if p.name.startswith("Deoxyribonucleic"))
    assert "representative" not in yaml.safe_load(proposed[fish])
    soy = next(p for p in proposed if p.name == "Bacto_Soytone.yaml")
    assert yaml.safe_load(proposed[soy])["representative"] == "FOODON:03315720"
    assert mod.verify_complete(proposed) == STAMP


@pytest.mark.parametrize(
    "kind", ["missing", "extra", "wrong-node", "history", "identifier", "alias"]
)
def test_preimage_or_owner_membership_change_refused(before, kind):
    p = mod.OWNERS[0]
    if kind == "missing":
        before.pop(p)
    elif kind == "extra":
        before[Path("data/ingredients/mapped/Extra.yaml")] = before[p]
    else:
        doc = yaml.safe_load(before[p])
        if kind == "wrong-node":
            doc["kg_microbe_node_id"] = "CHEBI:1"
        elif kind == "history":
            doc["curation_history"][0]["changes"] = "changed history"
        elif kind == "identifier":
            doc["identifier"] = "CHEBI:1"
        else:
            doc["synonyms"] = []
        before[p] = yaml.safe_dump(doc).encode()
    with pytest.raises(ValueError):
        mod.propose_sources(before, timestamp=STAMP)


@pytest.mark.parametrize(
    "stamp", ["2000-01-01T00:00:00+00:00", "2030-01-02T00:00:00", "2030-01-02T00:00:00+01:00"]
)
def test_requires_utc_timestamp_after_source_evidence(before, stamp):
    with pytest.raises(ValueError, match="Timestamp"):
        mod.propose_sources(before, timestamp=stamp)


@pytest.mark.parametrize(
    "kind", ["role", "representative", "history", "partial", "duplicate-event"]
)
def test_completed_verification_refuses_unreviewed_or_partial_changes(before, kind):
    current = mod.propose_sources(before, timestamp=STAMP)
    p = next(p for p in current if p.name.startswith("Deoxyribonucleic"))
    doc = yaml.safe_load(current[p])
    if kind == "role":
        doc["nutritional_roles"] = [{"role": "CARBON_SOURCE"}]
    elif kind == "representative":
        doc["representative"] = "kgmicrobe.ingredient:fish-sperm_dna"
    elif kind == "history":
        doc["curation_history"][0]["changes"] = "edited"
    elif kind == "duplicate-event":
        doc["curation_history"].append(doc["curation_history"][-1])
    else:
        doc = yaml.safe_load(before[p])
    current[p] = yaml.safe_dump(doc).encode()
    with pytest.raises(ValueError):
        mod.verify_complete(current)


def test_native_dry_run_apply_and_completed_receipt(native_runtime, case):
    root, log, originals = case
    result = mod.apply_sources(root, log)
    assert not result["applied"] and not log.exists()
    assert_owners_unchanged(case)
    result = mod.apply_sources(root, log, apply=True)
    assert result["applied"] and len(result["records"]) == 6
    assert set(result["transaction"]["changed"]) == {str(root / p) for p in mod.OWNERS}
    assert result["transaction"]["created"] == []
    for p in mod.ANCHORS:
        assert (root / p).read_bytes() == originals[p]
    for p, backup in mod.backups(log).items():
        assert backup.read_bytes() == originals[p]
    _, receipt = mod.source_receipt(root, log)
    assert all(
        "No mapping" in row["change"] and "source-evidence.json" in row["verification"]
        for row in receipt["records"]
    )
    assert receipt["approval"].startswith("NONE")
    assert mod.apply_sources(root, log, apply=True)["changed"] is False


@pytest.mark.parametrize(
    "kind", ["owner", "evidence", "manifest", "canonical", "unified", "ledger", "source-symlink"]
)
def test_changed_or_aliased_input_refuses_before_owner_write(case, kind):
    root, log, _ = case
    paths = {
        "owner": root / mod.OWNERS[-1],
        "evidence": root / mod.REPORT / "sources/ols-78020.json",
        "manifest": root / mod.MANIFEST,
        "canonical": root / "mappings/ingredient_mappings.sssom.tsv",
        "unified": root / "UNIFIED_INGREDIENT_MAPPING.tsv",
        "ledger": root / "mappings/unified_mapping_rejections.tsv",
        "source-symlink": root / mod.REPORT / "sources/ols-78020.json",
    }
    path = paths[kind]
    if kind == "source-symlink":
        saved = path.with_suffix(".original")
        path.rename(saved)
        path.symlink_to(saved)
    else:
        path.write_bytes(path.read_bytes() + b"\n")
    snapshots = {p: (root / p).read_bytes() for p in mod.OWNERS}
    with pytest.raises(ValueError):
        mod.apply_sources(root, log, apply=True)
    assert not log.exists()
    assert all((root / p).read_bytes() == data for p, data in snapshots.items())


@pytest.mark.parametrize("kind", ["receipt", "backup", "receipt-symlink"])
def test_all_receipt_outputs_reserved_before_publication(native_runtime, case, kind):
    root, log, _ = case
    path = next(iter(mod.backups(log).values())) if kind == "backup" else log
    if kind == "receipt-symlink":
        original = log.parent / "other.json"
        original.write_bytes(b"do not overwrite")
        path.symlink_to(original)
    else:
        path.write_bytes(b"do not overwrite")
    with pytest.raises((ValueError, FileExistsError)):
        mod.apply_sources(root, log, apply=True)
    assert path.read_bytes() == b"do not overwrite"
    assert_owners_unchanged(case)


def test_fresh_source_added_after_validation_refuses_before_any_write(
    native_runtime, case, monkeypatch
):
    root, log, _ = case
    reserve = mod.guarded.reserve_receipt_outputs

    @contextmanager
    def changed(*args, **kwargs):
        with reserve(*args, **kwargs) as handles:
            extra = root / "data/ingredients/mapped/Unexpected.yaml"
            extra.write_bytes(mod.frozen(mod.OWNERS[0]))
            yield handles

    monkeypatch.setattr(mod.guarded, "reserve_receipt_outputs", changed)
    with pytest.raises(native_runtime.ValidationFailed, match="path set"):
        mod.apply_sources(root, log, apply=True)
    assert_owners_unchanged(case)
    receipt = json.loads(log.read_bytes())
    assert receipt["state"] == "failed" and receipt["recovery_required"] is True
    assert receipt["journal_directory"] == str(log.parent / (log.stem + "-journal"))


def test_native_partial_io_failure_retains_exact_six_owner_recovery(
    native_runtime, case, monkeypatch
):
    native_transaction = importlib.import_module("kg_microbe_write.transaction")
    root, log, originals = case
    replace = native_transaction._atomic_replace
    written = []

    def fail_second_owner(path, text):
        if path in {root / p for p in mod.OWNERS}:
            if written:
                raise OSError("injected source write failure")
            written.append(path)
        return replace(path, text)

    monkeypatch.setattr(native_transaction, "_atomic_replace", fail_second_owner)
    with pytest.raises(native_runtime.WriteError, match="write failed after 1"):
        mod.apply_sources(root, log, apply=True)
    receipt = json.loads(log.read_bytes())
    assert receipt["state"] == "failed" and receipt["recovery_required"] is True
    journals = list(Path(receipt["journal_directory"]).glob("write-*.json"))
    assert len(journals) == 1
    previous = native_runtime.recover(journals[0])
    assert set(previous) == {str(root / p) for p in mod.OWNERS}
    assert all(previous[str(root / p)].encode() == originals[p] for p in mod.OWNERS)
    assert len(written) == 1
    monkeypatch.setattr(native_transaction, "_atomic_replace", replace)

    def validate(path, text):
        assert text.encode() == originals[path.relative_to(root)]

    recovery = native_runtime.ValidatedWriteTransaction(root, validator=validate)
    for path, text in previous.items():
        recovery.stage(Path(path).relative_to(root), text)
    recovery.commit(apply=True)
    assert_owners_unchanged(case)


def test_protected_anchor_changed_during_reservation_refuses_all_six(
    native_runtime, case, monkeypatch
):
    root, log, _ = case
    reserve = mod.guarded.reserve_receipt_outputs

    @contextmanager
    def changed(*args, **kwargs):
        with reserve(*args, **kwargs) as handles:
            anchor = root / "UNIFIED_INGREDIENT_MAPPING.tsv"
            anchor.write_bytes(anchor.read_bytes() + b"\n")
            yield handles

    monkeypatch.setattr(mod.guarded, "reserve_receipt_outputs", changed)
    with pytest.raises(ValueError, match="frozen input"):
        mod.apply_sources(root, log, apply=True)
    assert_owners_unchanged(case)
    assert json.loads(log.read_bytes())["state"] == "failed"


def test_completed_receipt_cannot_fabricate_authority(native_runtime, case):
    root, log, _ = case
    mod.apply_sources(root, log, apply=True)
    receipt = json.loads(log.read_bytes())
    receipt["approval"] = "APPROVED"
    log.write_text(json.dumps(receipt))
    with pytest.raises(ValueError, match="exact execution"):
        mod.source_receipt(root, log)


@pytest.mark.parametrize("kind", ["directory", "file", "symlink"])
def test_existing_journal_entry_refuses_without_overwrite(native_runtime, case, kind):
    root, log, _ = case
    journal = log.parent / (log.stem + "-journal")
    foreign = log.parent / "foreign"
    foreign.mkdir()
    marker = foreign / "keep.txt"
    marker.write_bytes(b"competitor")
    if kind == "directory":
        journal.mkdir()
    elif kind == "file":
        journal.write_bytes(b"competitor")
    else:
        journal.symlink_to(foreign, target_is_directory=True)
    with pytest.raises(ValueError, match="Journal"):
        mod.apply_sources(root, log, apply=True)
    assert_owners_unchanged(case)
    assert not log.exists()
    assert marker.read_bytes() == b"competitor"
    assert list(foreign.iterdir()) == [marker]
    assert journal.exists()


@pytest.mark.parametrize("kind", ["leaf-symlink", "leaf-replacement", "parent-symlink"])
def test_late_journal_alias_at_reservation_preserves_competitors(
    native_runtime, case, monkeypatch, kind
):
    root, log, _ = case
    foreign = log.parent.parent / "foreign-journal-target"
    foreign.mkdir()
    marker = foreign / "keep.txt"
    marker.write_bytes(b"competitor")
    journal = log.parent / (log.stem + "-journal")
    retained = (
        log.parent.with_name("retained-receipts")
        if kind == "parent-symlink"
        else log.parent / "retained-journal"
    )
    reserve = mod.guarded.reserve_receipt_outputs

    @contextmanager
    def replace_after_reservation(*args, **kwargs):
        with reserve(*args, **kwargs) as handles:
            if kind == "parent-symlink":
                log.parent.rename(retained)
                log.parent.symlink_to(foreign, target_is_directory=True)
            else:
                journal.rename(retained)
                if kind == "leaf-symlink":
                    journal.symlink_to(foreign, target_is_directory=True)
                else:
                    journal.mkdir()
            yield handles

    monkeypatch.setattr(mod.guarded, "reserve_receipt_outputs", replace_after_reservation)
    with pytest.raises((ValueError, native_runtime.ValidationFailed)):
        mod.apply_sources(root, log, apply=True)
    assert_owners_unchanged(case)
    assert list(foreign.iterdir()) == [marker]
    assert marker.read_bytes() == b"competitor"
    assert retained.is_dir()
    if kind == "parent-symlink":
        assert log.parent.is_symlink()
        failure = retained / log.name
    else:
        assert journal.exists()
        failure = log
    assert json.loads(failure.read_bytes())["state"] == "failed"


@pytest.mark.parametrize("kind", ["leaf", "parent"])
def test_fd_bound_journal_blocks_alias_during_native_write(native_runtime, case, monkeypatch, kind):
    root, log, _ = case
    foreign = log.parent.parent / "foreign-native-target"
    foreign.mkdir()
    marker = foreign / "keep.txt"
    marker.write_bytes(b"competitor")
    journal = log.parent / (log.stem + "-journal")
    retained = (
        log.parent / "retained-journal"
        if kind == "leaf"
        else log.parent.with_name("retained-receipts")
    )
    write_at = mod.publication._write_at
    intercepted = []

    def swap_then_write(fd, name, payload, *, replacing=False):
        assert not replacing and not intercepted
        intercepted.append(name)
        if kind == "leaf":
            journal.rename(retained)
            journal.symlink_to(foreign, target_is_directory=True)
        else:
            log.parent.rename(retained)
            log.parent.symlink_to(foreign, target_is_directory=True)
        return write_at(fd, name, payload, replacing=replacing)

    monkeypatch.setattr(mod.publication, "_write_at", swap_then_write)
    with pytest.raises(ValueError, match="aliased"):
        mod.apply_sources(root, log, apply=True)
    assert len(intercepted) == 1
    assert_owners_unchanged(case)
    assert list(foreign.iterdir()) == [marker]
    owned_journal = retained if kind == "leaf" else retained / journal.name
    journals = list(owned_journal.glob("write-*.json"))
    assert len(journals) == 1
    assert json.loads(journals[0].read_bytes())["status"] == "in_progress"
    failure = log if kind == "leaf" else retained / log.name
    assert json.loads(failure.read_bytes())["state"] == "failed"


@pytest.mark.parametrize(
    "kind", ["outside-path", "symlink", "rehash-wrong-preimage", "extra-member"]
)
def test_completed_source_requires_exact_owned_native_journal(native_runtime, case, kind):
    root, log, _ = case
    mod.apply_sources(root, log, apply=True)
    saved = json.loads(log.read_bytes())
    journal = Path(saved["transaction"]["journal"])
    if kind == "outside-path":
        other = log.parent / "foreign.json"
        other.write_bytes(journal.read_bytes())
        saved["transaction"]["journal"] = str(other)
        log.write_text(json.dumps(saved))
    elif kind == "symlink":
        other = log.parent / "foreign.json"
        journal.rename(other)
        journal.symlink_to(other)
    elif kind == "extra-member":
        (journal.parent / "extra.json").write_text("{}")
    else:
        payload = json.loads(journal.read_bytes())
        payload["previous"][str(root / mod.OWNERS[0])] = "forged preimage"
        journal.write_text(json.dumps(payload))
        saved["journal_sha256"] = mod.guarded.digest(journal.read_bytes())
        log.write_text(json.dumps(saved))
    with pytest.raises((ValueError, OSError)):
        mod.source_receipt(root, log)


def test_parent_acquisition_rejects_nonleaf_alias_before_directory_mutation(
    native_runtime, case, monkeypatch
):
    root, old_log, _ = case
    anchor = old_log.parent / "anchor"
    parent = anchor / "nested"
    parent.mkdir(parents=True)
    foreign = old_log.parent / "foreign"
    (foreign / "nested").mkdir(parents=True)
    retained = old_log.parent / "retained"
    opened = os.open
    intercepted = []

    def swap_before_open(path, flags, *args, **kwargs):
        if Path(path) == parent and kwargs.get("dir_fd") is None:
            assert not intercepted
            intercepted.append(path)
            anchor.rename(retained)
            anchor.symlink_to(foreign, target_is_directory=True)
        return opened(path, flags, *args, **kwargs)

    monkeypatch.setattr(os, "open", swap_before_open)
    with pytest.raises(ValueError, match="Receipt parent changed during acquisition"):
        mod.apply_sources(root, parent / "source.json", apply=True)
    assert intercepted == [parent]
    assert list((foreign / "nested").iterdir()) == []
    assert list((retained / "nested").iterdir()) == []
    assert anchor.is_symlink()
    assert_owners_unchanged(case)


@pytest.mark.parametrize("apply_mode", [False, True])
def test_missing_receipt_parent_never_uses_racy_pathname_mkdir(
    native_runtime, case, monkeypatch, apply_mode
):
    root, old_log, _ = case
    anchor = old_log.parent / "anchor"
    anchor.mkdir()
    parent = anchor / "nested"
    foreign = old_log.parent / "foreign"
    foreign.mkdir()
    retained = old_log.parent / "retained"
    mkdir = Path.mkdir
    intercepted = []

    def swap_before_mkdir(path, *args, **kwargs):
        if path == parent:
            intercepted.append(path)
            anchor.rename(retained)
            anchor.symlink_to(foreign, target_is_directory=True)
        return mkdir(path, *args, **kwargs)

    monkeypatch.setattr(Path, "mkdir", swap_before_mkdir)
    with pytest.raises(ValueError, match="Receipt parent must already exist"):
        mod.apply_sources(root, parent / "source.json", apply=apply_mode)
    assert not intercepted and not parent.exists()
    assert list(foreign.iterdir()) == []
    assert not retained.exists() and not anchor.is_symlink()
    assert_owners_unchanged(case)
