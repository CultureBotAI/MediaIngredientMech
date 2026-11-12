"""Real synthetic native correction transitions, without campaign approvals (#1373)."""

from __future__ import annotations

import json

import pytest

from mediaingredientmech.curate import curation_successor as successor
from tests.test_curation_successor import SuccessorFixture, ref
from tests.test_stable_id_adoption import api, write


def maintained(root):
    """Capture complete owner bytes and every maintained non-owner beforeimage."""
    owners = {
        str(path.relative_to(root)): path.read_bytes()
        for path in (root / "data/ingredients").glob("*/*.yaml")
    }
    names = (*api.AGGREGATES, *successor.LEDGERS, *successor.PUBLICATION, successor.MARKER)
    return {
        **owners,
        **{name: (root / name).read_bytes() if (root / name).exists() else None for name in names},
    }


def prepared(f):
    """Save genuine synthetic technical acceptance for the native prepared delta."""
    f.seal()
    stage = f.target / ".temp/correction-stage"
    manifest = successor.prepare(f.target, f.path, stage)
    path = stage / "manifest.json"
    relative = str(path.relative_to(f.target))
    target = {
        "target_id": "prepared",
        "kind": "snapshot_row",
        "path": relative,
        "selector": "prepared",
        "label": "Synthetic exact source correction",
        "semantic_digest": {
            "algorithm": "sha256",
            "sha256": api.sha(path.read_bytes()),
            "description": "Exact prepared curation successor manifest bytes",
        },
        "owner_paths": [
            {
                "repository": api.REPOSITORY,
                "path": relative,
                "role": "prepared source correction",
            }
        ],
    }
    inputs = {relative, "primary.txt"}
    for op in f.request["operations"]:
        for role in ("primary", "skeptic"):
            pair = f.target / op[role]["path"]
            report = api.load_yaml(pair.read_bytes())
            inputs.update(item["path"] for item in report["source"]["inputs"])
            inputs.update(str(p.relative_to(f.target)) for p in (pair, pair.with_name("review.md")))
    original = f.original
    previous_root = original.root
    original.root = f.target
    try:
        report = original.report("correction-technical", [target], sorted(inputs), scientific=False)
        budget = manifest["operational_budget"]
        context = json.loads(f.context_path.read_bytes())
        dimensions = {
            "curation_action": "apply_exact_prepared_set",
            "operational_budget_sha256": api.digest(budget),
            "lease_seconds": str(budget["policy_value"]["lease_seconds"]),
            "lease_namespace_sha256": api.digest(budget["lease_namespace"]),
            "lease_scheduling": "mediaingredientmech_and_global_conflict_reviewed",
            "historical_obligations_sha256": api.digest(context["historical_obligations"]),
        }
        report["assessments"] = [
            {
                "assessment_id": "apply",
                "area": "completeness",
                "topic": "Exact synthetic prepared source correction",
                "outcome": "supported",
                "summary": "Independent synthetic technical acceptance, no release approval",
                "target_ids": ["prepared"],
                "evidence_ids": ["primary"],
                "dimensions": [
                    {
                        "name": key,
                        "value": value,
                        "definition": "Explicit synthetic technical scope",
                        "evidence_ids": ["primary"],
                    }
                    for key, value in dimensions.items()
                ],
            }
        ]
        pair = original.save_report(report)
    finally:
        original.root = previous_root
    acceptance = f.target / "correction/acceptance.json"
    write(
        acceptance,
        {
            "manifest_sha256": api.sha(path.read_bytes()),
            "review": {
                **ref(f.target, pair),
                "markdown_sha256": api.sha(pair.with_name("review.md").read_bytes()),
                "target_id": "prepared",
                "assessment_id": "apply",
            },
        },
    )
    return stage, acceptance, manifest


def test_exact_native_correction_apply_and_verify_preserve_identity_and_history(
    tmp_path, monkeypatch
):
    """A real correction verifies through its unchanged real adoption predecessor."""
    f = SuccessorFixture(tmp_path, monkeypatch)
    stage, acceptance, manifest = prepared(f)
    before = maintained(f.target)
    predecessor = maintained(f.predecessor)
    source_context = f.target / f.request["source_context"]["path"]
    source_before = source_context.read_bytes()
    receipt = f.target / ".temp/correction-application"
    dry = successor.apply(f.target, stage, acceptance, receipt, enabled=False)
    assert dry["applied"] is False and not receipt.exists()
    assert maintained(f.target) == before

    result = successor.apply(f.target, stage, acceptance, receipt, enabled=True)
    assert result["state"] == "COMPLETE"
    assert result["recovery_required"] is False and result["release_approval_added"] is False
    checked = successor.verify_completed(f.target, stage, receipt / "application.json")
    assert checked["status"] == "COMPLETE_CURRENT_SOURCE_SUCCESSOR"
    assert checked["release_approval_added"] is False
    assert maintained(f.predecessor) == predecessor
    assert source_context.read_bytes() == source_before

    after = maintained(f.target)
    selected = f.request["operations"][0]["after_path"]
    for name, raw in before.items():
        if name not in {selected, *api.AGGREGATES, successor.MARKER}:
            assert after[name] == raw
    before_owners = {name: api.load_yaml(raw) for name, raw in f.before.items()}
    after_owners = {name: api.load_yaml((f.target / name).read_bytes()) for name in f.before}
    assert {name: record["mim_id"] for name, record in before_owners.items()} == {
        name: record["mim_id"] for name, record in after_owners.items()
    }
    assert after_owners[selected] == api.load_yaml(f.proposal.read_bytes())
    assert (
        after_owners[selected]["curation_history"][:-1]
        == before_owners[selected]["curation_history"]
    )
    assert result["publication_beforeimages"] == manifest["publication_beforeimages"]
    assert {name: after[name] for name in successor.PUBLICATION} == {
        name: before[name] for name in successor.PUBLICATION
    }
    assert set(result["beforeimages"]) == set(before)
    for name, archived in result["beforeimages"].items():
        if before[name] is None:
            assert archived is None
        else:
            assert (f.target / archived["path"]).read_bytes() == before[name]
    assert (
        api.verify_completed(
            f.predecessor, f.original.stage, f.original.receipt / "application.json"
        )["status"]
        == "COMPLETE_CURRENT_CANDIDATE"
    )


@pytest.mark.parametrize("changed", ["scientific-input", "predecessor-owner"])
def test_changed_real_proof_input_refuses_before_writes(tmp_path, monkeypatch, changed):
    """A fresh application must reject changed science or predecessor owner bytes."""
    f = SuccessorFixture(tmp_path, monkeypatch)
    stage, acceptance, _ = prepared(f)
    before = maintained(f.target)
    path = (
        f.target / "primary.txt"
        if changed == "scientific-input"
        else f.predecessor / "data/ingredients/mapped/Exact.yaml"
    )
    path.write_bytes(path.read_bytes() + b"\n# altered after review\n")
    receipt = f.target / ".temp/rejected-application"
    with pytest.raises(ValueError):
        successor.apply(f.target, stage, acceptance, receipt, enabled=True)
    assert maintained(f.target) == before
    assert not receipt.exists()


def test_insufficient_reviewed_policy_refuses_preparation_without_maintained_writes(
    tmp_path, monkeypatch
):
    """A genuinely selected insufficient policy cannot become a prepared candidate."""
    f = SuccessorFixture(tmp_path, monkeypatch)
    policy = f.target / f.request["operational_policy"]["path"]
    value = json.loads(policy.read_bytes())
    value["lease_seconds"] = 1
    write(policy, value)
    f.request["operational_policy"] = ref(f.target, policy)
    write(f.path, f.request)
    f.seal()
    before = maintained(f.target)
    stage = f.target / ".temp/insufficient-policy"
    with pytest.raises(ValueError):
        successor.prepare(f.target, f.path, stage)
    assert maintained(f.target) == before
    assert not (stage / "manifest.json").exists()
    if (stage / "FAILED.json").exists():
        assert json.loads((stage / "FAILED.json").read_bytes())["state"] == "FAILED_PREPARATION"


def test_lost_native_lease_cannot_install_or_claim_completion(tmp_path, monkeypatch):
    """Real acquired native lease ownership is checked again before installation."""
    f = SuccessorFixture(tmp_path, monkeypatch)
    stage, acceptance, _ = prepared(f)
    original = successor.native().Claw.__init__
    seen = []

    def selected(instance, root):
        original(instance, root)
        manager = instance.modules["locks"].LockManager
        check = manager.check_lock

        def lost(self, resource):
            value = check(self, resource)
            if value and resource == "mediaingredientmech" and resource in self._leases:
                seen.append(resource)
                if len(seen) > 1:
                    return {**value, "lease_token": "synthetic-other-writer"}
            return value

        manager.check_lock = lost

    monkeypatch.setattr(successor.native().Claw, "__init__", selected)
    before = maintained(f.target)
    receipt = f.target / ".temp/lost-native-lease"
    with pytest.raises(ValueError):
        successor.apply(f.target, stage, acceptance, receipt, enabled=True)
    assert len(seen) > 1
    assert maintained(f.target) == before
    if (receipt / "application.json").exists():
        assert json.loads((receipt / "application.json").read_bytes())["state"] != "COMPLETE"


def test_failure_after_real_first_write_preserves_honest_recovery_receipt(tmp_path, monkeypatch):
    """A real installed first owner cannot be concealed behind a success receipt."""
    f = SuccessorFixture(tmp_path, monkeypatch)
    stage, acceptance, manifest = prepared(f)
    before = maintained(f.target)
    globals_ = successor.apply.__globals__
    original = globals_["publish_validated"]
    installed = []

    def fail_after_write(*args, **kwargs):
        result = original(*args, **kwargs)
        installed.append(result.path)
        raise OSError("Synthetic failure after actual guarded owner installation")

    monkeypatch.setitem(globals_, "publish_validated", fail_after_write)
    receipt = f.target / ".temp/partial-application"
    with pytest.raises(OSError, match="Synthetic failure"):
        successor.apply(f.target, stage, acceptance, receipt, enabled=True)
    selected = f.request["operations"][0]["after_path"]
    assert installed == [f.target / selected]
    assert api.sha((f.target / selected).read_bytes()) == manifest["outputs"][selected]
    assert (f.target / selected).read_bytes() != before[selected]
    result = json.loads((receipt / "application.json").read_bytes())
    assert result["state"] == "FAILED" and result["recovery_required"] is True
    assert result["observed_outputs"][selected]["sha256"] == manifest["outputs"][selected]
    assert (f.target / result["beforeimages"][selected]["path"]).read_bytes() == before[selected]
    assert not (f.target / successor.MARKER).exists()
    assert {name: maintained(f.target)[name] for name in successor.PUBLICATION} == {
        name: before[name] for name in successor.PUBLICATION
    }
    with pytest.raises(ValueError):
        successor.verify_completed(f.target, stage, receipt / "application.json")
    with pytest.raises(ValueError):
        successor.apply(f.target, stage, acceptance, receipt, enabled=True)
