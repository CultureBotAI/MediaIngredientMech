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


@pytest.mark.parametrize("collision", ["receipt", "canonical_backup", "baseline_backup"])
def test_cli_refuses_evidence_collision_before_any_maintained_write(tmp_path, monkeypatch, collision):
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
    path = {"receipt": receipt, "canonical_backup": receipt.with_suffix(".before.tsv"),
            "baseline_backup": receipt.with_suffix(".baseline-before.tsv")}[collision]
    path.write_bytes(b"preserved earlier evidence\n")
    before = {p: p.read_bytes() for p in tmp_path.rglob("*") if p.is_file()}
    monkeypatch.setattr(sys, "argv", ["script", "--apply", "--candidate", str(candidate), "--log", str(receipt)])
    with pytest.raises(ValueError, match="Refusing to overwrite"):
        mod.main()
    assert {p: p.read_bytes() for p in tmp_path.rglob("*") if p.is_file()} == before
