"""Genuine bounded adoption → correction → correction with independent inputs (#1373)."""

import copy
import json
import shutil

import pytest
import yaml

from mediaingredientmech.curate import curation_successor as successor
from mediaingredientmech.curate import curation_successor_producer
from tests.test_curation_successor import SuccessorFixture, ref
from tests.test_curation_successor_history import (
    assert_exact_evidence,
    commit_paths,
    receipt_evidence,
)
from tests.test_curation_successor_publication import publication
from tests.test_curation_successor_transition import maintained, prepared
from tests.test_stable_id_adoption import ROOT, api, command, write


class ChainFixture(SuccessorFixture):
    """Keep the actual first endpoint immutable in its own committed real root."""

    def __init__(self, tmp, monkeypatch, *, predecessor_source=None):
        source_name = "src/mediaingredientmech/curate/curation_successor.py"
        super().__init__(
            tmp,
            monkeypatch,
            publication_baseline=True,
            predecessor_sources={source_name: predecessor_source} if predecessor_source else None,
        )
        first_api = successor
        if predecessor_source:
            loader = self.target / "src/mediaingredientmech/curate/curation_successor_producer.py"
            _, first_api = curation_successor_producer.load(self.target, loader.read_bytes())
            self.successor_api = first_api
        hold = {"issue_key": "retained-quantity", "reason": "Source quantity remains unassessed"}
        self.request["operations"][0]["inherited_holds"] = [hold]
        self.request["operations"][0]["residual_holds"] = [copy.deepcopy(hold)]
        write(self.path, self.request)
        stage, acceptance, manifest = prepared(self)
        receipt = self.target / ".temp/first-application"
        first_api.apply(self.target, stage, acceptance, receipt, enabled=True)
        self.first = self.target
        self.first_stage, self.first_receipt = stage, receipt / "application.json"
        self.first_evidence = receipt_evidence(self.first, stage, self.first_receipt)
        commit_paths(self.first, manifest["outputs"], "Commit first actual synthetic correction")
        if predecessor_source:
            # A fresh CLI invocation captures the producer's current Git context
            # after the ordinary commit; the original manifest remains unchanged.
            _, first_api = curation_successor_producer.load(self.first, loader.read_bytes())
        assert first_api.verify_completed(self.first, stage, self.first_receipt)["status"] == (
            "COMPLETE_CURRENT_SOURCE_SUCCESSOR"
        )
        self.first_maintained = maintained(self.first)
        self.adoption = self.predecessor
        self.adoption_maintained = maintained(self.adoption)
        self.predecessor = self.first
        self.endpoint = {
            **copy.deepcopy(self.endpoint),
            "kind": "successor",
            "identity": successor._identity(self.first),
            "stage": str(stage.relative_to(self.first)),
            "manifest": ref(self.first, stage / "manifest.json"),
            "receipt": ref(self.first, self.first_receipt),
            "producer": manifest["producer"],
        }
        self.target = tmp / "second-successor"
        shutil.copytree(self.first, self.target, ignore=shutil.ignore_patterns(".temp"))
        if predecessor_source:
            shutil.copyfile(ROOT / source_name, self.target / source_name)
            commit_paths(
                self.target, [source_name], "Install successor-chain producer in new target"
            )
        self.successor_api = successor
        self.review_prefix = "second-correction-"
        self.path = self.target / "second-correction/request.json"
        self.proposal = self.path.with_name("proposal.yaml")
        self.context_path = self.path.with_name("context.json")
        self.payloads_path = self.path.with_name("payloads.json")
        self.proposal.parent.mkdir()
        self.before = {
            n: raw
            for n, raw in maintained(self.target).items()
            if n.startswith("data/ingredients/")
        }
        owner = self.request["operations"][0]["after_path"]
        before = api.load_yaml(self.before[owner])
        after = copy.deepcopy(before)
        after["notes"] = "Second independently reviewed method documentation; holds retained."
        api.record_curation_event(
            after,
            curator="second-synthetic-primary",
            timestamp=self.stamp,
            action="MANUAL_CURATION",
            changes="Document independently reviewed method evidence.",
            previous_status="MAPPED",
            new_status="MAPPED",
            llm_assisted=True,
            llm_model="synthetic-fixture",
        )
        self.proposal.write_text(yaml.safe_dump(after, sort_keys=False))
        self.request.update(
            identity=successor._identity(self.target),
            predecessor=self.endpoint,
            target_inventory={n: api.sha(raw) for n, raw in self.before.items()},
            target_inputs={
                n: api.sha((self.target / n).read_bytes())
                for n in (*api.AGGREGATES, *successor.LEDGERS)
            },
            context=None,
            payloads=None,
            review_inputs={},
        )
        self.request["operations"][0].update(
            before=ref(self.target, self.target / owner),
            proposal=ref(self.target, self.proposal),
            delta=successor._delta(before, after),
            primary=None,
            skeptic=None,
        )
        write(self.path, self.request)


def test_two_native_corrections_commit_verify_and_generate(tmp_path, monkeypatch):
    two_native_corrections(tmp_path, monkeypatch)


def two_native_corrections(tmp_path, monkeypatch, *, predecessor_source=None):
    """Also reusable for a separately retained, actual historical producer source."""
    f = ChainFixture(tmp_path, monkeypatch, predecessor_source=predecessor_source)
    identity = successor._identity(f.first)
    command(f.first, "checkout", "--detach", identity["head"])
    assert successor._identity(f.first) == identity
    stage, acceptance, manifest = prepared(f)
    before = maintained(f.target)
    receipt = f.target / ".temp/second-application"
    dry = successor.apply(f.target, stage, acceptance, receipt)
    assert dry["applied"] is False and not receipt.exists()
    assert maintained(f.target) == before
    result = successor.apply(f.target, stage, acceptance, receipt, enabled=True)
    assert result["state"] == "COMPLETE"
    assert (f.target / result["beforeimages"][successor.MARKER]["path"]).read_bytes() == (
        f.first_maintained[successor.MARKER]
    )
    second_evidence = receipt_evidence(f.target, stage, receipt / "application.json")
    head = commit_paths(f.target, manifest["outputs"], "Commit second actual synthetic correction")
    checked = successor.verify_completed(f.target, stage, receipt / "application.json")
    assert checked["status"] == "COMPLETE_CURRENT_SOURCE_SUCCESSOR"
    assert checked["current_identity"]["head"] == head
    endpoint = f.path.with_name("endpoint.json")
    write(
        endpoint,
        {
            "schema_version": 1,
            "capability": successor.CAPABILITY,
            "root": str(f.target),
            "stage": str(stage.relative_to(f.target)),
            "manifest": ref(f.target, stage / "manifest.json"),
            "receipt": ref(f.target, receipt / "application.json"),
            "producer": manifest["producer"],
        },
    )
    p = publication(f, endpoint, tmp_path)
    assert p.generated["curation_successor"] == ref(f.target, endpoint)
    assert_exact_evidence(f.first_evidence)
    assert_exact_evidence(second_evidence)
    assert maintained(f.first) == f.first_maintained
    assert maintained(f.adoption) == f.adoption_maintained
    selected = f.request["operations"][0]["after_path"]
    after = api.load_yaml((f.target / selected).read_bytes())
    assert after["curation_history"][:-1] == api.load_yaml(f.before[selected])["curation_history"]
    for name, raw in before.items():
        if name not in {selected, *api.AGGREGATES, successor.MARKER}:
            assert maintained(f.target)[name] == raw
    captured = successor.Endpoint(f.target, json.loads(endpoint.read_bytes()))
    adoption_marker = f.adoption / successor.MARKER
    assert not adoption_marker.exists()
    adoption_marker.write_bytes(b"unexpected late lineage")
    try:
        with pytest.raises(ValueError, match="lineage"):
            captured.check()
    finally:
        adoption_marker.unlink()
    captured.check()
    # Every qualified root remains live after endpoint admission, including
    # ancestor evidence/ledgers and unselected owners, not just the latest delta.
    ancestor_manifest = json.loads((f.first_stage / "manifest.json").read_bytes())
    ancestor_request = json.loads((f.first / ancestor_manifest["request"]["path"]).read_bytes())
    for path in (
        f.first / successor.LEDGERS[0],
        f.first / successor.LEDGERS[1],
        f.adoption / next(iter(f.before)),
        f.target / next(n for n in f.before if n != selected),
        f.first / ancestor_request["operations"][0]["primary"]["path"],
        f.first_receipt,
        f.first_stage / "manifest.json",
    ):
        raw = path.read_bytes()
        path.write_bytes(raw + b"\n")
        try:
            with pytest.raises(ValueError):
                captured.check()
        finally:
            path.write_bytes(raw)
        captured.check()


def test_repeat_correction_refuses_rehashed_or_omitted_obligations(tmp_path, monkeypatch):
    f = ChainFixture(tmp_path, monkeypatch)
    original = copy.deepcopy(f.request)
    before = maintained(f.target)

    def refuse(change, match):
        f.request = copy.deepcopy(original)
        change(f.request)
        write(f.path, f.request)
        with pytest.raises((ValueError, KeyError), match=match):
            successor.inspect(f.target, f.path)
        assert maintained(f.target) == before

    refuse(lambda r: r["target_inventory"].pop(next(iter(r["target_inventory"]))), "inventory")
    refuse(lambda r: r["predecessor"]["historical_reviews"].pop(), "obligations")
    refuse(lambda r: r["operations"][0].update(inherited_holds=[], residual_holds=[]), "holds")
    refuse(lambda r: r["predecessor"].update(producer={}), "producer")
    refuse(lambda r: r["predecessor"]["identity"].update(root=str(f.target)), "overlap")
    refuse(lambda r: r["predecessor"].update(kind="adoption"), "lineage")
    f.request = original
    write(f.path, original)
    # A marker naming a sibling stage cannot make copied current owner bytes its endpoint.
    marker = f.target / successor.MARKER
    raw = marker.read_bytes()
    value = json.loads(raw)
    value["request"]["sha256"] = "f" * 64
    write(marker, value)
    with pytest.raises(ValueError, match="marker differs"):
        successor.inspect(f.target, f.path)
    marker.write_bytes(raw)
    # Self-rehashed target bytes cannot replace the native predecessor's owner/ID state.
    for name in (next(iter(f.before)), *api.AGGREGATES, *successor.LEDGERS):
        path = f.target / name
        raw = path.read_bytes()
        path.write_bytes(raw + b"\n")
        request = copy.deepcopy(original)
        collection = "target_inventory" if name in f.before else "target_inputs"
        request[collection][name] = api.sha(path.read_bytes())
        write(f.path, request)
        with pytest.raises(ValueError):
            successor.inspect(f.target, f.path)
        path.write_bytes(raw)
    write(f.path, original)
    assert maintained(f.target) == before
    assert_exact_evidence(f.first_evidence)
    # Rehashing a caller-visible reference cannot authorize a changed native
    # manifest or an omitted recovery owner in the real ancestor receipt.
    for path, change in (
        (
            f.first_stage / "manifest.json",
            lambda value: value["after_inventory"].pop(next(iter(f.before))),
        ),
        (f.first_receipt, lambda value: value["beforeimages"].pop(next(iter(f.before)))),
    ):
        raw = path.read_bytes()
        value = json.loads(raw)
        change(value)
        write(path, value)
        request = copy.deepcopy(original)
        key = "manifest" if path.name == "manifest.json" else "receipt"
        request["predecessor"][key] = ref(f.first, path)
        write(f.path, request)
        try:
            with pytest.raises(ValueError):
                successor.inspect(f.target, f.path)
        finally:
            path.write_bytes(raw)
    write(f.path, original)
    assert_exact_evidence(f.first_evidence)
    cloned = tmp_path / "unverified-copy-of-first"
    shutil.copytree(f.first, cloned)
    request = copy.deepcopy(original)
    request["predecessor"]["identity"] = successor._identity(cloned)
    write(f.path, request)
    with pytest.raises(ValueError, match="ancestry|root|foreign"):
        successor.inspect(f.target, f.path)


def test_ancestry_precheck_refuses_cycles_before_native_recursion(tmp_path, monkeypatch):
    f = ChainFixture(tmp_path, monkeypatch)
    reference = copy.deepcopy(f.endpoint)
    # Rehashed ancestry with a back-edge is rejected structurally, even before
    # its unchanged technical acceptance would reject the altered manifest.
    stage = f.first_stage
    manifest_path = stage / "manifest.json"
    manifest = json.loads(manifest_path.read_bytes())
    receipt = json.loads(f.first_receipt.read_bytes())
    request_path = f.first / manifest["request"]["path"]
    request = json.loads(request_path.read_bytes())
    request["predecessor"] = copy.deepcopy(reference)
    write(request_path, request)
    manifest["request"] = ref(f.first, request_path)
    manifest["predecessor"] = request["predecessor"]
    receipt["predecessor"] = request["predecessor"]
    write(manifest_path, manifest)
    write(f.first_receipt, receipt)
    marker = json.loads((f.first / successor.MARKER).read_bytes())
    marker.update(request=manifest["request"], predecessor=request["predecessor"])
    write(f.first / successor.MARKER, marker)
    reference.update(manifest=ref(f.first, manifest_path), receipt=ref(f.first, f.first_receipt))
    with pytest.raises(ValueError, match="overlap"):
        successor._ancestry(f.target, reference)


def test_ancestry_precheck_enforces_actual_bound_without_native_recursion(tmp_path):
    """Synthetic structural links exceed the real bound; none claim native approval."""
    target, adoption = tmp_path / "target", tmp_path / "adoption"
    target.mkdir()
    adoption.mkdir()
    reference = {"kind": "adoption", "identity": {"root": str(adoption)}}
    for number in range(successor.MAX_SUCCESSOR_ANCESTRY + 1):
        root = tmp_path / str(number)
        root.mkdir()
        write(root / "request.json", {"predecessor": reference})
        request = ref(root, root / "request.json")
        write(root / "manifest.json", {"request": request, "predecessor": reference})
        write(root / "receipt.json", {"predecessor": reference})
        write(
            root / successor.MARKER,
            {
                "root": str(root),
                "request": request,
                "predecessor": reference,
            },
        )
        reference = {
            "kind": "successor",
            "identity": {"root": str(root)},
            "manifest": ref(root, root / "manifest.json"),
            "receipt": ref(root, root / "receipt.json"),
        }
    with pytest.raises(ValueError, match="ancestry limit"):
        successor._ancestry(target, reference)


def test_chain_native_failure_controls_preserve_honest_partial_receipt(tmp_path, monkeypatch):
    f = ChainFixture(tmp_path, monkeypatch)
    stage, acceptance, manifest = prepared(f)
    before = maintained(f.target)
    for path in (f.target / "primary.txt", acceptance):
        raw = path.read_bytes()
        if path == acceptance:
            value = json.loads(raw)
            value["manifest_sha256"] = "f" * 64
            write(path, value)
        else:
            path.write_bytes(raw + b"changed science\n")
        destination = f.target / ".temp/stale-input"
        try:
            with pytest.raises(ValueError):
                successor.apply(f.target, stage, acceptance, destination, enabled=True)
            assert not destination.exists()
            assert maintained(f.target) == before
        finally:
            path.write_bytes(raw)
    alias = f.target / ".temp/aliased-receipt"
    alias.symlink_to(f.first_stage, target_is_directory=True)
    with pytest.raises(ValueError):
        successor.apply(f.target, stage, acceptance, alias, enabled=True)
    assert maintained(f.target) == before

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
                    return {**value, "lease_token": "another-native-writer"}
            return value

        manager.check_lock = lost

    with monkeypatch.context() as patch:
        patch.setattr(successor.native().Claw, "__init__", selected)
        destination = f.target / ".temp/lost-lease"
        with pytest.raises(ValueError):
            successor.apply(f.target, stage, acceptance, destination, enabled=True)
        assert len(seen) > 1
        assert maintained(f.target) == before

    publish = successor.apply.__globals__["publish_validated"]
    prior = f.first / next(iter(f.before))
    prior_bytes = prior.read_bytes()
    installed = []

    def drift_after_actual_write(*args, **kwargs):
        result = publish(*args, **kwargs)
        installed.append(result.path)
        prior.write_bytes(prior_bytes + b"\n")
        return result

    destination = f.target / ".temp/partial-chain-application"
    with monkeypatch.context() as patch:
        patch.setitem(successor.apply.__globals__, "publish_validated", drift_after_actual_write)
        try:
            with pytest.raises(ValueError):
                successor.apply(f.target, stage, acceptance, destination, enabled=True)
        finally:
            prior.write_bytes(prior_bytes)
    selected = f.request["operations"][0]["after_path"]
    assert installed == [f.target / selected]
    result = json.loads((destination / "application.json").read_bytes())
    assert result["state"] == "FAILED" and result["recovery_required"] is True
    assert result["observed_outputs"][selected]["sha256"] == manifest["outputs"][selected]
    assert (f.target / successor.MARKER).read_bytes() == before[successor.MARKER]
    assert (f.target / result["beforeimages"][selected]["path"]).read_bytes() == before[selected]
    with pytest.raises(ValueError):
        successor.verify_completed(f.target, stage, destination / "application.json")
    with pytest.raises(ValueError):
        successor.apply(f.target, stage, acceptance, destination, enabled=True)
    assert maintained(f.first) == f.first_maintained
    assert_exact_evidence(f.first_evidence)
