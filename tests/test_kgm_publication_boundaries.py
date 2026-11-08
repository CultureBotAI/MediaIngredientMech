"""#1153/#1154: four real writers refuse aliases and late evidence drift."""

import contextlib
import importlib.util
import json
import os
import sys
from pathlib import Path

import pytest

from mediaingredientmech.curate import publication_guard as guard
from mediaingredientmech.validation.mapping_change_receipts import verify_mapping_chain

ROOT = Path(__file__).resolve().parents[1]
REPORT = ROOT / "reports/kgm_unmapped_chemicals_20261107"
WRITERS = {
    "owner": "curate_mediadive_acetate_alias.py",
    "canonical": "publish_mediadive_acetate_alias.py",
    "policy": "refresh_kgm_source_policy_manifest.py",
    "note": "correct_microbedecoder_methylacetate_provenance.py",
}


def load(name):
    spec = importlib.util.spec_from_file_location(name, ROOT / "scripts" / WRITERS[name])
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def copy(source, destination):
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_bytes(source.read_bytes())
    return destination


@pytest.fixture(scope="module")
def native_proof():
    # Replay the native receipt chain, not a hand-built mocked proof.
    return verify_mapping_chain(ROOT)


def setup(name, root, native_proof):
    mod = load(name)
    args = ["writer", "--root", str(root), "--receipt-dir", str(root / "receipts")]
    if name == "owner":
        target = copy(REPORT / "sodium-acetate/write/owner-before.yaml", root / mod.OWNER)
        evidence = root / "primary"
        for filename in mod.EVIDENCE:
            copy(REPORT / "sodium-acetate/sources" / filename, evidence / filename)
        inputs = {"evidence": evidence / "mediadive-1315.json"}
        args += ["--evidence", str(evidence)]
        log = root / "receipts/apply-log.json"
    elif name == "note":
        target = copy(REPORT / "methylacetate/write/owner-before.yaml", root / mod.OWNER)
        evidence = copy(
            REPORT / "methylacetate/sources/microbedecoder-raw-record19685.csv", root / "raw.csv"
        )
        inputs = {"evidence": evidence}
        args += ["--source-record", str(evidence)]
        log = root / "receipts/apply-log.json"
    elif name == "canonical":
        target = copy(REPORT / "sodium-acetate/publication/canonical-before.tsv", root / mod.SOURCE)
        owner = copy(ROOT / mod.OWNER, root / mod.OWNER)
        candidate = copy(
            REPORT / "native-generation/native-candidate.sssom.tsv", root / "candidate.tsv"
        )
        manifest = root / "generation.json"
        doc = json.loads(
            (REPORT / "native-generation/native-candidate.sssom.tsv.manifest.json").read_bytes()
        )
        for item in doc["source_inputs"]:
            if item["path"].endswith("/" + mod.OWNER):
                item["path"] = str(owner)
        manifest.write_text(json.dumps(doc))
        inputs = {"owner": owner, "candidate": candidate, "manifest": manifest}
        args += ["--candidate", str(candidate), "--manifest", str(manifest)]
        log = root / "receipts/projection.json"
    else:
        for path in native_proof["input_hashes"]:
            copy(ROOT / path, root / path)
        target = copy(REPORT / "policy-write/policy-manifest-before.json", root / mod.MANIFEST)
        for path in (mod.OWNER, mod.NOTE_OWNER):
            copy(ROOT / path, root / path)
        generation = copy(
            REPORT / "native-generation/native-candidate.sssom.tsv.manifest.json",
            root / "generation.json",
        )
        inputs = {
            "manifest": generation,
            "owner": root / mod.OWNER,
            "canonical": root / mod.SOURCE,
            "receipt": root / native_proof["receipt_paths"][-1],
        }
        args += ["--generation-manifest", "generation.json"]
        log = root / "receipts/policy-manifest-write.json"
    return mod, target, inputs, args, log


def invoke(mod, args, monkeypatch, apply=True):
    monkeypatch.setattr(sys, "argv", args + (["--apply"] if apply else []))
    mod.main()


def no_success(log):
    assert not log.exists() or log.read_bytes() == b""


@pytest.mark.parametrize("name", WRITERS)
def test_1153_real_writers_dry_run_then_publish_unaliased_files(
    tmp_path, monkeypatch, native_proof, name
):
    mod, target, inputs, args, log = setup(name, tmp_path, native_proof)
    before = target.read_bytes()
    evidence = {p: p.read_bytes() for p in inputs.values()}
    invoke(mod, args, monkeypatch, apply=False)
    assert target.read_bytes() == before and not log.exists()
    invoke(mod, args, monkeypatch)
    assert target.read_bytes() != before
    assert all(p.read_bytes() == raw for p, raw in evidence.items())
    receipt = json.loads(log.read_bytes())
    if name == "canonical":
        assert receipt["native_manifest_sha256"] == mod.content_sha256(evidence[inputs["manifest"]])
        assert receipt["native_candidate_sha256"] == mod.content_sha256(
            evidence[inputs["candidate"]]
        )
    elif name in {"owner", "note"}:
        assert len(receipt["records"]) == 1
    else:
        assert receipt["approval"] == "NONE"


@pytest.mark.parametrize("name", WRITERS)
@pytest.mark.parametrize("late", [False, True])
def test_1153_target_hardlinks_initial_or_after_reservation(
    tmp_path, monkeypatch, native_proof, name, late
):
    mod, target, _, args, log = setup(name, tmp_path, native_proof)
    before = target.read_bytes()
    alias = tmp_path / "unrelated-link"
    if late:
        reserve = mod.reserve_receipt_outputs

        @contextlib.contextmanager
        def intercepted(*args, **kwargs):
            with reserve(*args, **kwargs) as handles:
                os.link(target, alias)
                yield handles

        monkeypatch.setattr(mod, "reserve_receipt_outputs", intercepted)
    else:
        os.link(target, alias)
    with pytest.raises(ValueError, match="alias"):
        invoke(mod, args, monkeypatch)
    assert target.read_bytes() == alias.read_bytes() == before
    no_success(log)


@pytest.mark.parametrize("name", WRITERS)
def test_1153_atomic_replace_never_writes_a_link_added_at_replace(
    tmp_path, monkeypatch, native_proof, name
):
    mod, target, _, args, log = setup(name, tmp_path, native_proof)
    before = target.read_bytes()
    alias = tmp_path / "last-instant-link"
    replace = guard.os.replace

    def intercepted(*args, **kwargs):
        os.link(target, alias)
        return replace(*args, **kwargs)

    monkeypatch.setattr(guard.os, "replace", intercepted)
    with pytest.raises(ValueError, match="hardlink appeared"):
        invoke(mod, args, monkeypatch)
    assert alias.read_bytes() == before
    no_success(log)


DRIFT = [
    ("canonical", "manifest"),
    ("canonical", "candidate"),
    ("canonical", "owner"),
    ("owner", "evidence"),
    ("note", "evidence"),
    ("policy", "manifest"),
    ("policy", "owner"),
    ("policy", "canonical"),
    ("policy", "receipt"),
]


@pytest.mark.parametrize("name,input_name", DRIFT)
@pytest.mark.parametrize("boundary", ["reservation", "after_publication", "receipt"])
def test_1154_all_consumed_inputs_stay_bound_until_receipt(
    tmp_path, monkeypatch, native_proof, name, input_name, boundary
):
    mod, target, inputs, args, log = setup(name, tmp_path, native_proof)
    before = target.read_bytes()
    changed = inputs[input_name]

    def mutate():
        changed.write_bytes(changed.read_bytes() + b"\n")

    if boundary == "reservation":
        reserve = mod.reserve_receipt_outputs

        @contextlib.contextmanager
        def intercepted(*args, **kwargs):
            with reserve(*args, **kwargs) as handles:
                mutate()
                yield handles

        monkeypatch.setattr(mod, "reserve_receipt_outputs", intercepted)
    elif boundary == "after_publication":
        replace = guard.os.replace

        def intercepted(*args, **kwargs):
            result = replace(*args, **kwargs)
            mutate()
            return result

        monkeypatch.setattr(guard.os, "replace", intercepted)
    else:
        finish = mod.finish_receipt

        def intercepted(receipt, path, payload, recheck):
            calls = 0

            def late():
                nonlocal calls
                calls += 1
                if calls == 2:
                    mutate()
                recheck()

            return finish(receipt, path, payload, late)

        monkeypatch.setattr(mod, "finish_receipt", intercepted)
    with pytest.raises(ValueError, match="changed"):
        invoke(mod, args, monkeypatch)
    if boundary == "reservation":
        assert target.read_bytes() == before
    no_success(log)


@pytest.mark.parametrize("name", WRITERS)
@pytest.mark.parametrize("role", ["input", "receipt", "backup"])
def test_1153_late_evidence_and_reservation_aliases_are_refused(
    tmp_path, monkeypatch, native_proof, name, role
):
    mod, target, inputs, args, log = setup(name, tmp_path, native_proof)
    before = target.read_bytes()
    reserve = mod.reserve_receipt_outputs

    @contextlib.contextmanager
    def intercepted(*args, **kwargs):
        with reserve(*args, **kwargs) as handles:
            if role == "input":
                victim = next(iter(inputs.values()))
            else:
                victim = Path(handles[0 if role == "receipt" else 1].name)
            os.link(victim, tmp_path / "unrelated-link")
            yield handles

    monkeypatch.setattr(mod, "reserve_receipt_outputs", intercepted)
    with pytest.raises(ValueError, match="alias"):
        invoke(mod, args, monkeypatch)
    assert target.read_bytes() == before
    no_success(log)


def test_1154_policy_receipt_inventory_cannot_grow_after_validation(
    tmp_path, monkeypatch, native_proof
):
    mod, target, _, args, log = setup("policy", tmp_path, native_proof)
    before = target.read_bytes()
    reserve = mod.reserve_receipt_outputs

    @contextlib.contextmanager
    def intercepted(*args, **kwargs):
        with reserve(*args, **kwargs) as handles:
            (tmp_path / native_proof["receipt_paths"][-1]).with_name("extra.json").write_text("{}")
            yield handles

    monkeypatch.setattr(mod, "reserve_receipt_outputs", intercepted)
    with pytest.raises(ValueError, match="Unsupported mapping receipt schema"):
        invoke(mod, args, monkeypatch)
    assert target.read_bytes() == before
    no_success(log)


@pytest.mark.parametrize("name", WRITERS)
@pytest.mark.parametrize("replacement", ["symlink", "same_bytes_new_inode"])
def test_1153_late_target_replacement_refused_even_when_bytes_agree(
    tmp_path, monkeypatch, native_proof, name, replacement
):
    mod, target, _, args, log = setup(name, tmp_path, native_proof)
    before = target.read_bytes()
    reserve = mod.reserve_receipt_outputs
    original = tmp_path / "original-target"

    @contextlib.contextmanager
    def intercepted(*args, **kwargs):
        with reserve(*args, **kwargs) as handles:
            target.rename(original)
            if replacement == "symlink":
                target.symlink_to(original)
            else:
                target.write_bytes(before)
            yield handles

    monkeypatch.setattr(mod, "reserve_receipt_outputs", intercepted)
    with pytest.raises(ValueError, match="alias|identity changed"):
        invoke(mod, args, monkeypatch)
    assert target.read_bytes() == original.read_bytes() == before
    no_success(log)
