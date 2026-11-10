"""Filesystem regressions extracted from the guarded campaign writers.

Synthetic bytes exercise filesystem boundaries, not native schema/science
validation or complete adoption. All files belong to pytest's private fixture.
"""

import json
import os
from pathlib import Path

import pytest

from mediaingredientmech.curate import adoption_filesystem as files
from mediaingredientmech.curate import publication_guard as guard
from mediaingredientmech.curate.apply_receipt import reserve_receipt_outputs


@pytest.fixture
def root(tmp_path):
    # macOS pytest temp paths can pass through /var or /tmp aliases.
    return tmp_path.resolve()


def put(root, name, raw=b"original"):
    path = root / name
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(raw)
    return path


def unchanged():
    pass


def test_capture_rechecks_bytes_and_inode(root):
    path = put(root, "owner.yaml")
    frozen = guard.FrozenFile.capture(path)
    frozen.verify()
    path.write_bytes(b"changed")
    with pytest.raises(ValueError, match="Captured input changed"):
        frozen.verify()
    path.write_bytes(frozen.content)
    frozen.verify()
    replacement = put(root, "replacement", frozen.content)
    os.replace(replacement, path)
    with pytest.raises(ValueError, match="identity changed"):
        frozen.verify()


@pytest.mark.parametrize("kind", ["leaf-symlink", "parent-symlink", "hardlink", "directory"])
def test_capture_refuses_aliases_and_nonregular_entries(root, kind):
    path = put(root, "owners/owner.yaml")
    if kind == "leaf-symlink":
        selected = root / "alias.yaml"
        selected.symlink_to(path)
    elif kind == "parent-symlink":
        (root / "alias").symlink_to(path.parent, target_is_directory=True)
        selected = root / "alias/owner.yaml"
    elif kind == "hardlink":
        os.link(path, root / "alias.yaml")
        selected = path
    else:
        selected = path.parent
    with pytest.raises(ValueError, match="alias|Nonregular"):
        guard.FrozenFile.capture(selected)
    assert path.read_bytes() == b"original"


def test_capture_refuses_parent_replacement_even_with_same_file_inode(root):
    path = put(root, "owners/owner.yaml")
    frozen = guard.FrozenFile.capture(path)
    saved = root / "saved"
    path.parent.rename(saved)
    path.parent.mkdir()
    (saved / path.name).rename(path)
    assert path.stat().st_ino == frozen.identity[1]
    with pytest.raises(ValueError, match="parent changed"):
        frozen.verify()


def test_exclusive_create_returns_single_link_captured_file(root):
    (root / "owners").mkdir()
    calls = []
    result = files._new_owner(root, "owners/new.yaml", b"validated", lambda: calls.append(1))
    result.verify()
    assert result.content == b"validated" and result.path.stat().st_nlink == 1
    assert calls == [1]
    assert list(result.path.parent.iterdir()) == [result.path]


@pytest.mark.parametrize("kind", ["file", "directory", "dangling-symlink"])
def test_exclusive_create_refuses_existing_destination(root, kind):
    target = root / "new.yaml"
    if kind == "file":
        target.write_bytes(b"competitor")
    elif kind == "directory":
        target.mkdir()
    else:
        target.symlink_to(root / "missing")
    with pytest.raises(ValueError, match="exists|alias"):
        files._new_owner(root, target.name, b"validated", unchanged)
    if kind == "file":
        assert target.read_bytes() == b"competitor"
    else:
        assert target.is_dir() if kind == "directory" else target.is_symlink()


def test_exclusive_create_race_preserves_competitor(root, monkeypatch):
    target = root / "new.yaml"
    link = files.os.link

    def race(*args, **kwargs):
        target.write_bytes(b"competitor")
        return link(*args, **kwargs)

    monkeypatch.setattr(files.os, "link", race)
    with pytest.raises(FileExistsError):
        files._new_owner(root, target.name, b"validated", unchanged)
    assert target.read_bytes() == b"competitor"


@pytest.mark.parametrize("alias", [False, True])
def test_late_create_parent_swap_does_not_write_into_replacement(root, monkeypatch, alias):
    parent = root / "owners"
    parent.mkdir()
    saved = root / "saved"
    link = files.os.link

    def swap(*args, **kwargs):
        parent.rename(saved)
        if alias:
            parent.symlink_to(saved, target_is_directory=True)
        else:
            parent.mkdir()
            (parent / "competitor").write_bytes(b"keep")
        return link(*args, **kwargs)

    monkeypatch.setattr(files.os, "link", swap)
    with pytest.raises((ValueError, FileNotFoundError)):
        files._new_owner(root, "owners/new.yaml", b"validated", unchanged)
    if not alias:
        assert not (parent / "new.yaml").exists()
        assert (parent / "competitor").read_bytes() == b"keep"
    else:
        # A late alias can leave real bytes in the original held directory;
        # the helper refuses success and does not roll that partial state back.
        assert parent.is_symlink()
        assert (saved / "new.yaml").read_bytes() == b"validated"


def test_create_recheck_failure_precedes_installation(root):
    def refuse():
        raise ValueError("review changed")

    with pytest.raises(ValueError, match="review changed"):
        files._new_owner(root, "new.yaml", b"validated", refuse)
    assert not (root / "new.yaml").exists()


def test_retirement_preserves_original_inode_and_bytes(root):
    source = guard.FrozenFile.capture(put(root, "owners/old.yaml"))
    recovery = root / "recovery"
    recovery.mkdir()
    retired = files._retire(source, recovery, unchanged)
    assert not os.path.lexists(source.path)
    retired.verify()
    assert retired.identity == source.identity and retired.content == source.content
    assert retired.path == recovery / "retired-owner.yaml"


@pytest.mark.parametrize("kind", ["occupied", "symlink"])
def test_retirement_requires_fresh_unaliased_recovery(root, kind):
    source = guard.FrozenFile.capture(put(root, "old.yaml"))
    real = root / "real-recovery"
    real.mkdir()
    recovery = root / "recovery"
    if kind == "occupied":
        recovery.mkdir()
        (recovery / "competitor").write_bytes(b"keep")
    else:
        recovery.symlink_to(real, target_is_directory=True)
    with pytest.raises(ValueError, match="fresh|alias"):
        files._retire(source, recovery, unchanged)
    source.verify()
    assert list(real.iterdir()) == []


def test_retirement_exclusive_race_preserves_source_and_competitor(root, monkeypatch):
    source = guard.FrozenFile.capture(put(root, "old.yaml"))
    recovery = root / "recovery"
    recovery.mkdir()
    rename = files._rename_exclusive

    def race(*args):
        (recovery / "retired-owner.yaml").write_bytes(b"competitor")
        return rename(*args)

    monkeypatch.setattr(files, "_rename_exclusive", race)
    with pytest.raises(FileExistsError):
        files._retire(source, recovery, unchanged)
    source.verify()
    assert (recovery / "retired-owner.yaml").read_bytes() == b"competitor"


def test_retirement_wrong_inode_is_retained_but_never_accepted(root, monkeypatch):
    source = guard.FrozenFile.capture(put(root, "old.yaml"))
    authentic = root / "authentic.yaml"
    recovery = root / "recovery"
    recovery.mkdir()
    rename = files._rename_exclusive

    def race(*args):
        source.path.rename(authentic)
        source.path.write_bytes(source.content)
        return rename(*args)

    monkeypatch.setattr(files, "_rename_exclusive", race)
    with pytest.raises(ValueError, match="retired a changed entry; retained for recovery"):
        files._retire(source, recovery, unchanged)
    assert guard.FrozenFile.capture(authentic).identity == source.identity
    retired = guard.FrozenFile.capture(recovery / "retired-owner.yaml")
    assert retired.content == source.content and retired.identity != source.identity


def test_retirement_reappearing_source_preserves_both_entries(root, monkeypatch):
    source = guard.FrozenFile.capture(put(root, "old.yaml"))
    recovery = root / "recovery"
    recovery.mkdir()
    rename = files._rename_exclusive

    def race(*args):
        rename(*args)
        source.path.write_bytes(b"competitor")

    monkeypatch.setattr(files, "_rename_exclusive", race)
    with pytest.raises(ValueError, match="source reappeared"):
        files._retire(source, recovery, unchanged)
    assert source.path.read_bytes() == b"competitor"
    assert guard.FrozenFile.capture(recovery / "retired-owner.yaml").identity == source.identity


def test_retirement_late_source_parent_alias_refuses_before_move(root):
    source = guard.FrozenFile.capture(put(root, "owners/old.yaml"))
    saved = root / "saved"
    recovery = root / "recovery"
    recovery.mkdir()

    def swap():
        source.path.parent.rename(saved)
        source.path.parent.symlink_to(saved, target_is_directory=True)

    with pytest.raises((ValueError, OSError)):
        files._retire(source, recovery, swap)
    assert (saved / "old.yaml").read_bytes() == source.content
    assert list(recovery.iterdir()) == []


@pytest.mark.parametrize("platform", ["unsupported", "darwin", "linux"])
def test_retirement_has_no_overwriting_fallback(root, monkeypatch, platform):
    source = put(root, "source")
    target = put(root, "target", b"keep")
    with monkeypatch.context() as patch:
        patch.setattr(files.sys, "platform", platform)
        patch.setattr(files.ctypes, "CDLL", lambda *a, **k: object())
        with pytest.raises(ValueError, match="No exclusive owner-retirement primitive"):
            files._rename_exclusive(-1, str(source), -1, str(target))
    assert source.read_bytes() == b"original" and target.read_bytes() == b"keep"


def test_validated_publication_replaces_only_held_entry(root):
    target = guard.FrozenFile.capture(put(root, "owner.yaml"))
    evidence = guard.FrozenFile.capture(put(root, "evidence"))
    result = guard.publish_validated(target, lambda p: p.write_bytes(b"validated"), evidence.verify)
    result.verify()
    evidence.verify()
    assert result.content == b"validated" and result.identity != target.identity


def test_render_failure_leaves_original_owner_and_no_candidate(root):
    target = guard.FrozenFile.capture(put(root, "owner.yaml"))

    def invalid(path):
        path.write_bytes(b"invalid partial render")
        raise ValueError("native validator refused")

    with pytest.raises(ValueError, match="native validator refused"):
        guard.publish_validated(target, invalid, unchanged)
    target.verify()
    assert list(root.iterdir()) == [target.path]


def test_publication_parent_swap_refuses_and_preserves_competitor(root, monkeypatch):
    target = guard.FrozenFile.capture(put(root, "owners/owner.yaml"))
    parent, saved = target.path.parent, root / "saved"
    replace = guard.os.replace

    def swap(staged, destination, **kwargs):
        # The destination fd still names the old parent. Supply the real
        # moved staged source so the test reaches the post-replace check.
        relative = staged.relative_to(parent)
        parent.rename(saved)
        parent.mkdir()
        target.path.write_bytes(b"competitor")
        return replace(saved / relative, destination, **kwargs)

    monkeypatch.setattr(guard.os, "replace", swap)
    with pytest.raises(ValueError, match="Published output or parent differs"):
        guard.publish_validated(target, lambda p: p.write_bytes(b"validated"), unchanged)
    assert target.path.read_bytes() == b"competitor"
    assert (saved / target.path.name).read_bytes() == b"validated"


@pytest.mark.parametrize("when", ["render", "after-replace"])
def test_publication_input_drift_never_returns_success(root, monkeypatch, when):
    target = guard.FrozenFile.capture(put(root, "owner.yaml"))
    evidence = guard.FrozenFile.capture(put(root, "evidence"))

    def render(path):
        path.write_bytes(b"validated")
        if when == "render":
            evidence.path.write_bytes(b"changed")

    replace = guard.os.replace

    def late(*args, **kwargs):
        replace(*args, **kwargs)
        evidence.path.write_bytes(b"changed")

    if when == "after-replace":
        monkeypatch.setattr(guard.os, "replace", late)
    with pytest.raises(ValueError, match="Captured input changed"):
        guard.publish_validated(target, render, evidence.verify)
    assert target.path.read_bytes() == (b"original" if when == "render" else b"validated")


def test_last_instant_hardlink_keeps_original_bytes_without_success(root, monkeypatch):
    target = guard.FrozenFile.capture(put(root, "owner.yaml"))
    alias = root / "alias"
    replace = guard.os.replace

    def race(*args, **kwargs):
        os.link(target.path, alias)
        return replace(*args, **kwargs)

    monkeypatch.setattr(guard.os, "replace", race)
    with pytest.raises(ValueError, match="hardlink appeared"):
        guard.publish_validated(target, lambda p: p.write_bytes(b"validated"), unchanged)
    assert alias.read_bytes() == target.content
    assert target.path.read_bytes() == b"validated"


@pytest.mark.parametrize("kind", ["symlink", "hardlink", "replacement"])
def test_late_reserved_output_identity_is_checked(root, kind):
    log = root / "receipt.json"
    with reserve_receipt_outputs(log) as (receipt, backup):
        backup.write(b"before")
        backup.flush()
        if kind == "hardlink":
            os.link(log, root / "alias")
        else:
            log.rename(root / "reserved")
            if kind == "symlink":
                log.symlink_to(root / "reserved")
            else:
                log.write_bytes(b"competitor")
        with pytest.raises(ValueError, match="alias|Reserved output changed"):
            guard.finish_receipt(receipt, log, {"state": "complete"}, unchanged)
        assert log.with_suffix(".before.yaml").read_bytes() == b"before"
        if kind == "replacement":
            assert log.read_bytes() == b"competitor"
        else:
            assert log.read_bytes() == b""


def test_receipt_postwrite_input_drift_clears_success_keeps_backup(root):
    log = root / "receipt.json"
    evidence = guard.FrozenFile.capture(put(root, "evidence"))
    calls = 0

    def check():
        nonlocal calls
        calls += 1
        if calls == 2:
            evidence.path.write_bytes(b"changed")
        evidence.verify()

    with reserve_receipt_outputs(log) as (receipt, backup):
        backup.write(b"original")
        backup.flush()
        with pytest.raises(ValueError, match="Captured input changed"):
            guard.finish_receipt(receipt, log, {"state": "complete"}, check)
    assert log.read_bytes() == b""
    assert log.with_suffix(".before.yaml").read_bytes() == b"original"


def test_successful_receipt_checks_real_reserved_handle_and_inputs_twice(root):
    log = root / "receipt.json"
    evidence = guard.FrozenFile.capture(put(root, "evidence"))
    calls = []

    def check():
        evidence.verify()
        calls.append(1)

    with reserve_receipt_outputs(log) as (receipt, backup):
        backup.write(b"original")
        backup.flush()
        guard.check_reserved(backup, log.with_suffix(".before.yaml"))
        guard.finish_receipt(receipt, log, {"state": "complete"}, check)
    assert json.loads(log.read_bytes()) == {"state": "complete"}
    assert calls == [1, 1]
    assert log.with_suffix(".before.yaml").read_bytes() == b"original"


def test_late_backup_hardlink_refused_before_publication(root):
    log = root / "receipt.json"
    owner = guard.FrozenFile.capture(put(root, "owner.yaml"))
    with reserve_receipt_outputs(log) as (_, backup):
        backup.write(owner.content)
        backup.flush()
        os.link(log.with_suffix(".before.yaml"), root / "backup-alias")
        with pytest.raises(ValueError, match="hardlink alias"):
            guard.check_reserved(backup, log.with_suffix(".before.yaml"))
    owner.verify()
    assert log.read_bytes() == b""
    assert (root / "backup-alias").read_bytes() == owner.content


def test_all_backups_reserved_before_any_mutation(root):
    log = root / "receipt.json"
    first, second = root / "first.backup", put(root, "second.backup", b"competitor")
    owner = put(root, "owner.yaml")
    with pytest.raises(FileExistsError):
        with reserve_receipt_outputs(log, backup_paths=(first, second)):
            pytest.fail("reservation must fail before yielding to any mutator")
    assert owner.read_bytes() == b"original" and second.read_bytes() == b"competitor"
    assert not log.exists() and not first.exists()


def test_late_failure_keeps_partial_write_and_reserved_recovery_evidence(root):
    log = root / "receipt.json"
    owner = guard.FrozenFile.capture(put(root, "owner.yaml"))
    with pytest.raises(RuntimeError, match="second operation failed"):
        with reserve_receipt_outputs(log) as (receipt, backup):
            backup.write(owner.content)
            backup.flush()
            assert log.exists() and log.with_suffix(".before.yaml").read_bytes() == owner.content
            guard.check_reserved(receipt, log)
            guard.publish_validated(owner, lambda p: p.write_bytes(b"validated"), unchanged)
            raise RuntimeError("second operation failed")
    assert owner.path.read_bytes() == b"validated"
    assert log.read_bytes() == b""
    assert log.with_suffix(".before.yaml").read_bytes() == owner.content


@pytest.mark.parametrize("occupied", [False, True])
def test_1314_recovery_replaced_before_open_refuses_before_retirement(root, monkeypatch, occupied):
    source = guard.FrozenFile.capture(put(root, "owners/old.yaml"))
    recovery = root / "recovery"
    recovery.mkdir()
    initial = recovery.stat().st_ino
    opened = files.os.open
    swapped = False

    def race(path, *args, **kwargs):
        nonlocal swapped
        if Path(path) == recovery and not swapped:
            swapped = True
            recovery.rename(root / "reserved-recovery")
            recovery.mkdir()
            if occupied:
                (recovery / "sentinel").write_bytes(b"keep")
        return opened(path, *args, **kwargs)

    monkeypatch.setattr(files.os, "open", race)
    with pytest.raises(ValueError, match="Relocation recovery"):
        files._retire(source, recovery, unchanged)
    source.verify()
    assert (root / "reserved-recovery").stat().st_ino == initial
    assert list((root / "reserved-recovery").iterdir()) == []
    assert not (recovery / "retired-owner.yaml").exists()
    if occupied:
        assert (recovery / "sentinel").read_bytes() == b"keep"


def test_1314_same_recovery_contaminated_before_open_refuses_before_retirement(root, monkeypatch):
    source = guard.FrozenFile.capture(put(root, "owners/old.yaml"))
    recovery = root / "recovery"
    recovery.mkdir()
    initial = recovery.stat().st_ino
    opened = files.os.open

    def race(path, *args, **kwargs):
        if Path(path) == recovery:
            (recovery / "sentinel").write_bytes(b"keep")
        return opened(path, *args, **kwargs)

    monkeypatch.setattr(files.os, "open", race)
    with pytest.raises(ValueError, match="recovery directory is not fresh"):
        files._retire(source, recovery, unchanged)
    source.verify()
    assert recovery.stat().st_ino == initial
    assert (recovery / "sentinel").read_bytes() == b"keep"
    assert not (recovery / "retired-owner.yaml").exists()


def test_1314_recovery_opened_descriptor_must_match_bound_directory(root, monkeypatch):
    source = guard.FrozenFile.capture(put(root, "owners/old.yaml"))
    recovery, other = root / "recovery", root / "other"
    recovery.mkdir()
    other.mkdir()
    opened = files.os.open

    def redirect(path, *args, **kwargs):
        return opened(other if Path(path) == recovery else path, *args, **kwargs)

    monkeypatch.setattr(files.os, "open", redirect)
    with pytest.raises(ValueError, match="recovery descriptor changed"):
        files._retire(source, recovery, unchanged)
    source.verify()
    assert list(recovery.iterdir()) == list(other.iterdir()) == []


def test_1314_same_recovery_inode_under_replaced_ancestor_is_refused(root, monkeypatch):
    source = guard.FrozenFile.capture(put(root, "owners/old.yaml"))
    parent = root / "evidence"
    recovery = parent / "recovery"
    recovery.mkdir(parents=True)
    initial = recovery.stat().st_ino
    opened = files.os.open
    swapped = False

    def race(path, *args, **kwargs):
        nonlocal swapped
        if Path(path) == recovery and not swapped:
            swapped = True
            parent.rename(root / "original-parent")
            parent.mkdir()
            (root / "original-parent/recovery").rename(recovery)
        return opened(path, *args, **kwargs)

    monkeypatch.setattr(files.os, "open", race)
    with pytest.raises(ValueError, match="recovery ancestor changed"):
        files._retire(source, recovery, unchanged)
    source.verify()
    assert recovery.stat().st_ino == initial
    assert list(recovery.iterdir()) == []


@pytest.mark.parametrize("failed_open", ["source", "recovery"])
def test_1314_descriptor_acquisition_failure_closes_every_acquired_fd(
    root, monkeypatch, failed_open
):
    source = guard.FrozenFile.capture(put(root, "owners/old.yaml"))
    recovery = root / "recovery"
    recovery.mkdir()
    opened = files.os.open
    acquired = []

    def fail(path, flags, *args, **kwargs):
        if flags & os.O_DIRECTORY:
            role = "source" if Path(path) == source.path.parent else "recovery"
            if role == failed_open:
                raise PermissionError("injected directory acquisition failure")
            descriptor = opened(path, flags, *args, **kwargs)
            acquired.append(descriptor)
            return descriptor
        return opened(path, flags, *args, **kwargs)

    monkeypatch.setattr(files.os, "open", fail)
    with pytest.raises(PermissionError, match="acquisition failure"):
        files._retire(source, recovery, unchanged)
    assert len(acquired) == (0 if failed_open == "source" else 1)
    for descriptor in acquired:
        with pytest.raises(OSError):
            os.fstat(descriptor)
    source.verify()
    assert list(recovery.iterdir()) == []


@pytest.mark.parametrize("outcome", ["success", "pre-move-refusal", "rename-failure"])
def test_1314_both_descriptors_closed_after_acquisition(root, monkeypatch, outcome):
    source = guard.FrozenFile.capture(put(root, "owners/old.yaml"))
    recovery = root / "recovery"
    recovery.mkdir()
    opened = files.os.open
    acquired = []

    def track(path, flags, *args, **kwargs):
        descriptor = opened(path, flags, *args, **kwargs)
        if flags & os.O_DIRECTORY:
            acquired.append(descriptor)
            if Path(path) == recovery and outcome == "pre-move-refusal":
                (recovery / "sentinel").write_bytes(b"keep")
        return descriptor

    def refuse(*args):
        raise OSError("injected rename failure")

    monkeypatch.setattr(files.os, "open", track)
    if outcome == "rename-failure":
        monkeypatch.setattr(files, "_rename_exclusive", refuse)
    if outcome == "success":
        result = files._retire(source, recovery, unchanged)
        assert result.identity == source.identity
    else:
        with pytest.raises((ValueError, OSError)):
            files._retire(source, recovery, unchanged)
        source.verify()
    assert len(acquired) == 2
    for descriptor in acquired:
        with pytest.raises(OSError):
            os.fstat(descriptor)


@pytest.mark.parametrize("alias", [False, True])
def test_1314_later_recovery_swap_retains_partial_evidence_without_success(
    root, monkeypatch, alias
):
    source = guard.FrozenFile.capture(put(root, "owners/old.yaml"))
    recovery, saved = root / "recovery", root / "reserved-recovery"
    recovery.mkdir()
    initial = recovery.stat().st_ino
    rename = files._rename_exclusive

    def race(*args):
        recovery.rename(saved)
        if alias:
            recovery.symlink_to(saved, target_is_directory=True)
        else:
            recovery.mkdir()
            (recovery / "sentinel").write_bytes(b"keep")
        return rename(*args)

    monkeypatch.setattr(files, "_rename_exclusive", race)
    with pytest.raises(ValueError, match="recovery|alias"):
        files._retire(source, recovery, unchanged)
    assert not source.path.exists()
    assert saved.stat().st_ino == initial
    retired = guard.FrozenFile.capture(saved / "retired-owner.yaml")
    assert retired.identity == source.identity and retired.content == source.content
    if not alias:
        assert (recovery / "sentinel").read_bytes() == b"keep"
        assert not (recovery / "retired-owner.yaml").exists()


def test_1314_later_contamination_retains_both_files_without_success(root, monkeypatch):
    source = guard.FrozenFile.capture(put(root, "owners/old.yaml"))
    recovery = root / "recovery"
    recovery.mkdir()
    rename = files._rename_exclusive

    def race(*args):
        (recovery / "sentinel").write_bytes(b"keep")
        return rename(*args)

    monkeypatch.setattr(files, "_rename_exclusive", race)
    with pytest.raises(ValueError, match="recovery directory is not fresh"):
        files._retire(source, recovery, unchanged)
    assert not source.path.exists()
    assert (recovery / "sentinel").read_bytes() == b"keep"
    retired = guard.FrozenFile.capture(recovery / "retired-owner.yaml")
    assert retired.identity == source.identity and retired.content == source.content
