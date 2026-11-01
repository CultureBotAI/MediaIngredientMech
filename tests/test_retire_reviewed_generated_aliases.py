"""Byte-preserving, fail-closed scope guards for seven reviewed alias retirements."""

import importlib.util
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "generated_alias_retirement", ROOT / "scripts/retire_reviewed_generated_aliases.py")
mod = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(mod)


def mapping_fixture(*, candidate=False):
    lines = ["# preserved metadata\r\n", "subject_id\tpredicate_id\tobject_id\tother\tcomment\r\n"]
    for plan in mod.PLANS:
        other = "keep-one|keep-two" if candidate else f"keep-one|{plan['token']}|keep-two"
        lines.append(f"{plan['subject_id']}\t{plan['predicate_id']}\t{plan['object_id']}\t{other}\tunchanged\r\n")
    lines.append("MIM:unrelated\tskos:exactMatch\tCHEBI:1\tretain|all\tquoted \"detail\"\r\n")
    return "".join(lines).encode()


def baseline_fixture():
    lines = ["subject_id\ttoken\towned_by\tdisposition\n"]
    for plan in mod.PLANS:
        lines.append("\t".join(plan[k] for k in ["subject_id", "token", "owned_by", "baseline_disposition"]) + "\n")
    lines += [f"MIM:policy{i}\tuntouched{i}\tMIM:owner{i}\tUNREVIEWED\n" for i in range(38)]
    return "".join(lines).encode()


def test_removes_only_reviewed_tokens_preserving_every_other_byte():
    before, candidate = mapping_fixture(), mapping_fixture(candidate=True)
    after = mod.transform_sssom(before, candidate)
    assert after == candidate
    assert before.endswith(b'quoted "detail"\r\n')
    assert after.endswith(b'quoted "detail"\r\n')
    assert after.count(b"\r\n") == before.count(b"\r\n")


def test_exactly_seven_baseline_entries_retire_and_other_38_are_untouched():
    before = baseline_fixture()
    after = mod.transform_baseline(before)
    assert after.splitlines(keepends=True) == before.splitlines(keepends=True)[:1] + before.splitlines(keepends=True)[8:]


@pytest.mark.parametrize("fault", ["still_generated", "case_variant_generated", "missing_generated",
                                  "missing_canonical", "duplicate_canonical", "changed_token",
                                  "wrong_predicate", "case_variant_canonical"])
def test_refuses_unreviewed_or_nonreproducing_payload(fault):
    before, candidate = mapping_fixture(), mapping_fixture(candidate=True)
    first = mod.PLANS[0]
    token = first["token"].encode()
    if fault == "still_generated":
        candidate = before
    elif fault == "case_variant_generated":
        candidate = candidate.replace(b"keep-one", token.upper(), 1)
    elif fault == "missing_generated":
        candidate = candidate.replace(first["subject_id"].encode(), b"MIM:wrong", 1)
    elif fault == "missing_canonical":
        before = before.replace(first["subject_id"].encode(), b"MIM:wrong", 1)
    elif fault == "duplicate_canonical":
        before += before.splitlines(keepends=True)[2]
    elif fault == "changed_token":
        before = before.replace(token, b"different-token", 1)
    elif fault == "wrong_predicate":
        before = before.replace(first["predicate_id"].encode(), b"skos:relatedMatch", 1)
    else:
        before = before.replace(token, token + b"|" + token.upper(), 1)
    with pytest.raises(ValueError):
        mod.transform_sssom(before, candidate)


@pytest.mark.parametrize("fault", ["entry_count", "owner", "disposition", "token"])
def test_refuses_changed_baseline_obligations(fault):
    before = baseline_fixture()
    if fault == "entry_count":
        before += b"MIM:extra\talias\tMIM:owner\tUNREVIEWED\n"
    elif fault == "owner":
        before = before.replace(mod.PLANS[0]["owned_by"].encode(), b"MIM:different", 1)
    elif fault == "disposition":
        before = before.replace(mod.PLANS[0]["baseline_disposition"].encode(), b"DIFFERENT_RULING", 1)
    else:
        before = before.replace(mod.PLANS[0]["token"].encode(), b"different", 1)
    with pytest.raises(ValueError):
        mod.transform_baseline(before)


def test_refuses_changed_owner_and_never_writes_it(tmp_path, monkeypatch):
    owner = tmp_path / "record.yaml"
    owner.write_bytes(b"reviewed owner bytes\n")
    plan = {**mod.PLANS[0], "source_record": "record.yaml", "owner_sha256": mod.digest(owner.read_bytes())}
    monkeypatch.setattr(mod, "PLANS", [plan])
    entry = mod.verified_owners(tmp_path)[0]
    assert entry["before_yaml_sha256"] == entry["after_yaml_sha256"]
    assert owner.read_bytes() == b"reviewed owner bytes\n"
    owner.write_bytes(b"concurrent curation\n")
    with pytest.raises(ValueError, match="Owner bytes changed"):
        mod.verified_owners(tmp_path)
    assert owner.read_bytes() == b"concurrent curation\n"


@pytest.fixture
def alias_apply_case(tmp_path, monkeypatch):
    mappings = tmp_path / "mappings"
    mappings.mkdir()
    canonical = mappings / "ingredient_mappings.sssom.tsv"
    baseline = mappings / "other_cross_record_baseline.tsv"
    candidate = tmp_path / "candidate.tsv"
    canonical.write_bytes(mapping_fixture())
    baseline.write_bytes(baseline_fixture())
    candidate.write_bytes(mapping_fixture(candidate=True))
    plans = []
    for i, plan in enumerate(mod.PLANS):
        owner = tmp_path / plan["source_record"]
        owner.parent.mkdir(parents=True, exist_ok=True)
        owner.write_bytes(f"reviewed fixture owner {i}\n".encode())
        plans.append({**plan, "owner_sha256": mod.digest(owner.read_bytes())})
    monkeypatch.setattr(mod, "PLANS", plans)
    monkeypatch.setattr(mod, "ROOT", tmp_path)
    receipt = tmp_path / "apply.json"
    monkeypatch.setattr(sys, "argv", ["script", "--apply", "--candidate", str(candidate), "--log", str(receipt)])
    outputs = {"receipt": receipt, "canonical_backup": receipt.with_suffix(".before.tsv"),
               "baseline_backup": receipt.with_suffix(".baseline-before.tsv")}
    sources = {p: p.read_bytes() for p in tmp_path.rglob("*") if p.is_file()}
    return outputs, sources, canonical, baseline


@pytest.mark.parametrize("collision", ["receipt", "canonical_backup", "baseline_backup"])
@pytest.mark.parametrize("kind", ["file", "directory", "symlink", "dangling_symlink"])
def test_cli_refuses_evidence_collision_before_any_source_write(
    alias_apply_case, tmp_path, monkeypatch, collision, kind,
):
    outputs, sources, _, _ = alias_apply_case
    path = outputs[collision]
    marker = b"preserved earlier evidence\n"
    target = tmp_path / "other-evidence"
    if kind == "file":
        path.write_bytes(marker)
    elif kind == "directory":
        path.mkdir()
    else:
        if kind == "symlink":
            target.write_bytes(marker)
        path.symlink_to(target)
    writes = []
    original_write = Path.write_bytes

    def observe_write(self, data):
        if self in sources:
            writes.append(self)
        return original_write(self, data)

    monkeypatch.setattr(Path, "write_bytes", observe_write)
    with pytest.raises(FileExistsError):
        mod.main()
    assert writes == []
    assert {p: p.read_bytes() for p in sources} == sources
    assert all(not p.exists() for p in outputs.values() if p != path)
    if kind == "file":
        assert path.read_bytes() == marker
    elif kind == "directory":
        assert path.is_dir()
    else:
        assert path.is_symlink()
        assert path.readlink() == target
        if kind == "symlink":
            assert target.read_bytes() == marker
        else:
            assert not target.exists()


@pytest.mark.parametrize("collision", ["receipt", "canonical_backup", "baseline_backup"])
def test_concurrent_evidence_creation_cannot_be_overwritten(alias_apply_case, monkeypatch, collision):
    outputs, sources, _, _ = alias_apply_case
    path = outputs[collision]
    original_open = Path.open
    injected = False

    def racing_open(self, mode="r", *args, **kwargs):
        nonlocal injected
        if self == path and not injected and any(flag in mode for flag in "wxa"):
            injected = True
            with original_open(path, "xb") as handle:
                handle.write(b"another writer won the reservation\n")
        return original_open(self, mode, *args, **kwargs)

    monkeypatch.setattr(Path, "open", racing_open)
    with pytest.raises(FileExistsError):
        mod.main()
    assert injected
    assert path.read_bytes() == b"another writer won the reservation\n"
    assert {p: p.read_bytes() for p in sources} == sources
    assert all(not p.exists() for p in outputs.values() if p != path)


def test_late_reservation_failure_cleans_only_new_reservations(alias_apply_case, monkeypatch):
    outputs, sources, _, _ = alias_apply_case
    original_open = Path.open

    def denied_open(self, mode="r", *args, **kwargs):
        if self == outputs["baseline_backup"] and any(flag in mode for flag in "wxa"):
            raise PermissionError("simulated third reservation failure")
        return original_open(self, mode, *args, **kwargs)

    monkeypatch.setattr(Path, "open", denied_open)
    with pytest.raises(PermissionError, match="third reservation"):
        mod.main()
    assert {p: p.read_bytes() for p in sources} == sources
    assert all(not path.exists() for path in outputs.values())


def test_success_reserves_all_outputs_and_flushes_both_backups_before_mutation(
    alias_apply_case, monkeypatch,
):
    outputs, sources, canonical, baseline = alias_apply_case
    original_open, original_write = Path.open, Path.write_bytes
    reservations = []
    writes = []

    def observe_open(self, mode="r", *args, **kwargs):
        if self in outputs.values() and any(flag in mode for flag in "wxa"):
            reservations.append((self, mode))
        return original_open(self, mode, *args, **kwargs)

    def guarded_write(self, data):
        if self in {canonical, baseline}:
            assert reservations == [(outputs["receipt"], "x"),
                                    (outputs["canonical_backup"], "xb"),
                                    (outputs["baseline_backup"], "xb")]
            assert outputs["canonical_backup"].read_bytes() == sources[canonical]
            assert outputs["baseline_backup"].read_bytes() == sources[baseline]
            writes.append(self)
        return original_write(self, data)

    monkeypatch.setattr(Path, "open", observe_open)
    monkeypatch.setattr(Path, "write_bytes", guarded_write)
    assert mod.main() == 0
    assert writes == [canonical, baseline]
    assert canonical.read_bytes() == mapping_fixture(candidate=True)
    assert baseline.read_bytes() == mod.transform_baseline(sources[baseline])
    assert outputs["receipt"].read_text().endswith("\n")
    assert {p: p.read_bytes() for p in sources if p not in {canonical, baseline}} == {
        p: data for p, data in sources.items() if p not in {canonical, baseline}
    }


@pytest.mark.parametrize("replaced", ["receipt", "canonical_backup"])
@pytest.mark.parametrize("replacement", ["file", "symlink", "removed"])
@pytest.mark.parametrize("late_open", ["failure", "success"])
def test_reservation_replacement_preserves_competitor_and_refuses_source_writes(
    alias_apply_case, tmp_path, monkeypatch, replaced, replacement, late_open,
):
    outputs, sources, _, _ = alias_apply_case
    path = outputs[replaced]
    immutable = tmp_path / "historical-review.yaml"
    immutable.write_bytes(b"historical review must not change\n")
    original_open, original_write = Path.open, Path.write_bytes
    injected = False
    writes = []

    def racing_open(self, mode="r", *args, **kwargs):
        nonlocal injected
        if self == outputs["baseline_backup"] and mode == "xb" and not injected:
            injected = True
            path.unlink()
            if replacement == "file":
                with original_open(path, "xb") as handle:
                    handle.write(b"competing writer's evidence\n")
            elif replacement == "symlink":
                path.symlink_to(immutable)
            if late_open == "failure":
                raise PermissionError("later backup reservation failed")
        return original_open(self, mode, *args, **kwargs)

    def observe_write(self, data):
        if self in sources:
            writes.append(self)
        return original_write(self, data)

    monkeypatch.setattr(Path, "open", racing_open)
    monkeypatch.setattr(Path, "write_bytes", observe_write)
    error = PermissionError if late_open == "failure" else ValueError
    with pytest.raises(error):
        mod.main()
    assert injected
    assert writes == []
    assert {p: p.read_bytes() for p in sources} == sources
    assert immutable.read_bytes() == b"historical review must not change\n"
    if replacement == "file":
        assert path.read_bytes() == b"competing writer's evidence\n"
    elif replacement == "symlink":
        assert path.is_symlink() and path.readlink() == immutable
    else:
        assert not path.exists()
    assert all(not p.exists() for p in outputs.values() if p != path)


def test_owned_cleanup_runs_while_exclusive_handles_remain_open(alias_apply_case, monkeypatch):
    outputs, sources, _, _ = alias_apply_case
    original_open, original_unlink = Path.open, Path.unlink
    handles = []
    cleaned = []

    def fail_last_open(self, mode="r", *args, **kwargs):
        if self == outputs["baseline_backup"] and mode == "xb":
            raise PermissionError("last reservation denied")
        handle = original_open(self, mode, *args, **kwargs)
        if self in outputs.values() and mode in {"x", "xb"}:
            handles.append(handle)
        return handle

    def observe_cleanup(self, *args, **kwargs):
        if self in outputs.values():
            assert handles and all(not handle.closed for handle in handles)
            cleaned.append(self)
        return original_unlink(self, *args, **kwargs)

    monkeypatch.setattr(Path, "open", fail_last_open)
    monkeypatch.setattr(Path, "unlink", observe_cleanup)
    with pytest.raises(PermissionError, match="last reservation denied"):
        mod.main()
    assert set(cleaned) == {outputs["receipt"], outputs["canonical_backup"]}
    assert all(handle.closed for handle in handles)
    assert {p: p.read_bytes() for p in sources} == sources
