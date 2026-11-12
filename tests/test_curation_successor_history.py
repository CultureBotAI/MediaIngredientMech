"""Actual completed-history and live-ledger boundaries (#1378, #1379)."""

from __future__ import annotations

import json

import pytest

from mediaingredientmech.curate import curation_successor as successor
from mediaingredientmech.curate import stable_sssom_publication as pub
from tests.test_curation_successor import SuccessorFixture
from tests.test_curation_successor_publication import corrected, publication
from tests.test_curation_successor_transition import maintained, prepared
from tests.test_stable_id_adoption import api, command


def commit_paths(root, names, message):
    """Commit only the explicitly selected maintained outputs, never fixture evidence."""
    names = tuple(names)
    assert names and not command(root, "diff", "--cached", "--name-only", "-z")
    previous = command(root, "rev-parse", "HEAD").decode().strip()
    command(root, "add", "--", *names)
    staged = set(command(root, "diff", "--cached", "--name-only", "-z").decode().split("\0")) - {""}
    assert staged and staged <= set(names)
    command(root, "commit", "-m", message)
    current = command(root, "rev-parse", "HEAD").decode().strip()
    assert current != previous
    assert command(root, "rev-parse", "HEAD^").decode().strip() == previous
    changed = set(
        command(root, "diff-tree", "--no-commit-id", "--name-only", "-r", "HEAD", "-z")
        .decode()
        .split("\0")
    ) - {""}
    assert changed == staged
    return current


def receipt_evidence(root, stage, receipt_path):
    """Retain actual native manifest, receipt, fit and recovery archive bytes."""
    receipt = json.loads(receipt_path.read_bytes())
    manifest_path = stage / "manifest.json"
    manifest = json.loads(manifest_path.read_bytes())
    paths = {manifest_path, receipt_path, stage / "fit-context.json"}
    paths.add(root / manifest["operational_budget"]["measurement"]["path"])
    paths.add(root / receipt["operational_fit"]["receipt"]["path"])
    for reference in receipt["beforeimages"].values():
        if reference is not None:
            paths.add(root / reference["path"])
    for reference in receipt.get("retired_sources", {}).values():
        paths.add(root / reference["path"])
    return {path: path.read_bytes() for path in paths}


def assert_exact_evidence(snapshot):
    """Keep original native proof and recovery bytes unchanged through commits."""
    assert {path: path.read_bytes() for path in snapshot} == snapshot


def test_completed_source_and_publication_commits_preserve_native_history_and_live_ledgers(
    tmp_path, monkeypatch
):
    """Ordinary output commits retain proof; archived ledgers cannot hide live drift."""
    f, endpoint = corrected(tmp_path, monkeypatch)
    value = json.loads(endpoint.read_bytes())
    source_stage = f.target / value["stage"]
    source_receipt = f.target / value["receipt"]["path"]
    source_manifest = json.loads((source_stage / "manifest.json").read_bytes())
    original_identity = source_manifest["identity"]
    original_evidence = receipt_evidence(f.target, source_stage, source_receipt)
    predecessor_before = maintained(f.predecessor)
    predecessor_receipt_path = f.predecessor / f.endpoint["receipt"]["path"]
    predecessor_receipt = predecessor_receipt_path.read_bytes()
    ledgers = {name: (f.target / name).read_bytes() for name in successor.LEDGERS}

    source_head = commit_paths(
        f.target,
        source_manifest["outputs"],
        "Commit exact synthetic source correction outputs (#1379)",
    )
    checked = successor.verify_completed(f.target, source_stage, source_receipt)
    assert checked["status"] == "COMPLETE_CURRENT_SOURCE_SUCCESSOR"
    assert checked["original_identity"] == original_identity
    assert checked["current_identity"]["head"] == source_head
    assert checked["current_identity"]["head"] != original_identity["head"]
    assert_exact_evidence(original_evidence)
    assert maintained(f.predecessor) == predecessor_before

    p = publication(f, endpoint, tmp_path)
    assert p.generated["curation_successor"]["sha256"] == api.sha(endpoint.read_bytes())
    request = p.request()
    owner_before = {
        str(path.relative_to(f.target)): path.read_bytes()
        for path in (f.target / "data/ingredients").glob("*/*.yaml")
    }
    registry_name, lifecycle_name = successor.LEDGERS
    registry_lines = ledgers[registry_name].decode().splitlines(keepends=True)
    cells = registry_lines[1].rstrip("\r\n").split("\t")
    assert cells[0] == "MIM:0000001"
    cells[1] = "Forbidden replacement mint label"
    registry_lines[1] = "\t".join(cells) + "\n"
    mutations = {
        registry_name: "".join(registry_lines).encode(),
        lifecycle_name: ledgers[lifecycle_name]
        + b"MIM:0000001\tmerged\tMIM:0000002\t2026-11-12T00:00:00Z\tForbidden live transition\n",
    }
    for name, raw in mutations.items():
        path = f.target / name
        assert raw != ledgers[name]
        path.write_bytes(raw)
        try:
            with pytest.raises(ValueError):
                successor.verify_completed(f.target, source_stage, source_receipt)
            with pytest.raises(ValueError):
                pub.inspect(f.target, request.path)
            assert {key: (f.target / key).read_bytes() for key in owner_before} == owner_before
            assert_exact_evidence(original_evidence)
        finally:
            path.write_bytes(ledgers[name])
        assert {key: (f.target / key).read_bytes() for key in ledgers} == ledgers

    request, publication_stage, _ = p.prepare(request)
    acceptance = p.accept(request, publication_stage)
    destination = p.destination(request, "committed")
    result = pub.apply(f.target, publication_stage, acceptance, destination, enabled=True)
    assert result["state"] == "COMPLETE"
    publication_receipt = destination / "application.json"
    publication_bytes = publication_receipt.read_bytes()
    publication_archives = {
        f.target / item["path"]: (f.target / item["path"]).read_bytes()
        for item in result["beforeimages"].values()
        if item is not None
    }
    canonical_head = commit_paths(
        f.target, pub.OUTPUTS, "Commit exact synthetic canonical publication outputs (#1379)"
    )
    proof = pub.verify_completed(f.target, publication_stage, publication_receipt)
    assert proof["status"] == "COMPLETE_CURRENT_CANONICAL_CANDIDATE"
    assert proof["ordinary_release_review_required"] is True
    assert command(f.target, "rev-parse", "HEAD").decode().strip() == canonical_head
    assert publication_receipt.read_bytes() == publication_bytes
    assert_exact_evidence(publication_archives)
    assert_exact_evidence(original_evidence)
    assert {name: (f.target / name).read_bytes() for name in ledgers} == ledgers
    assert maintained(f.predecessor) == predecessor_before
    assert predecessor_receipt_path.read_bytes() == predecessor_receipt


def test_prepared_live_application_still_refuses_a_new_commit(tmp_path, monkeypatch):
    """Historical descendant support does not relax a live prepared-set HEAD guard."""
    f = SuccessorFixture(tmp_path, monkeypatch)
    stage, acceptance, _ = prepared(f)
    before = maintained(f.target)
    assert not command(f.target, "diff", "--cached", "--name-only", "-z")
    previous = command(f.target, "rev-parse", "HEAD").decode().strip()
    command(f.target, "commit", "--allow-empty", "-m", "Synthetic intervening commit (#1379)")
    assert command(f.target, "rev-parse", "HEAD").decode().strip() != previous
    receipt = f.target / ".temp/changed-live-head"
    with pytest.raises(ValueError):
        successor.apply(f.target, stage, acceptance, receipt, enabled=True)
    assert not receipt.exists()
    assert maintained(f.target) == before
