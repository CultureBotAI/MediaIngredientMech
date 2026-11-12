"""Native tracked-source publication handoff and protected-closure controls (#1401)."""

from __future__ import annotations

import json
import shutil

import pytest

from mediaingredientmech.curate import curation_successor as successor
from mediaingredientmech.curate import stable_sssom_publication as pub
from mediaingredientmech.validation import semantic_transition as transition
from mediaingredientmech.validation.current_semantic_release import Inputs
from tests.test_curation_successor import SuccessorFixture, ref
from tests.test_curation_successor_publication import publication
from tests.test_curation_successor_transition import prepared
from tests.test_semantic_publication_transition import run as reconstruct_transition
from tests.test_stable_id_adoption import api, write
from tests.test_stable_sssom_publication import current_outputs, restore


@pytest.fixture(scope="module")
def tracked_publication(tmp_path_factory):
    """Actual native source proof with clean tracked publication beforeimages."""
    tmp = tmp_path_factory.mktemp("publication-handoff1401")
    with pytest.MonkeyPatch.context() as monkeypatch:
        f = SuccessorFixture(tmp, monkeypatch, publication_baseline=True)
        (f.target / "unrelated-tracked.txt").write_text("unchanged unrelated content\n")
        publisher_name = "src/mediaingredientmech/curate/stable_sssom_publication.py"
        publisher_path = f.target / publisher_name
        current_publisher = publisher_path.read_bytes()
        # Source qualification must not depend on this independent publisher.
        publisher_path.write_bytes(b"# Synthetic prior publisher for #1401\n")
        api.git(
            f.target,
            "add",
            "--",
            pub.CANONICAL,
            pub.SUPPRESSIONS,
            "unrelated-tracked.txt",
            publisher_name,
        )
        api.git(f.target, "commit", "-m", "Synthetic tracked publication baseline for #1401")
        f.request["identity"] = successor._identity(f.target)
        write(f.path, f.request)
        for name in (pub.CANONICAL, pub.SUPPRESSIONS):
            assert api.git(f.target, "show", "HEAD:" + name) == (f.target / name).read_bytes()
            assert api.git(f.target, "diff", "HEAD", "--", name) == b""
        stage, acceptance, manifest = prepared(f)
        source_receipt = f.target / ".temp/source-correction-application"
        result = successor.apply(f.target, stage, acceptance, source_receipt, enabled=True)
        assert result["state"] == "COMPLETE"
        assert (
            successor.verify_completed(f.target, stage, source_receipt / "application.json")[
                "status"
            ]
            == "COMPLETE_CURRENT_SOURCE_SUCCESSOR"
        )
        source_manifest = (stage / "manifest.json").read_bytes()
        source_application = (source_receipt / "application.json").read_bytes()
        assert publisher_name not in manifest["producer"]["files"]
        assert publisher_name not in manifest["inputs"]
        source_head = api.git(f.target, "rev-parse", "HEAD").strip()
        publisher_path.write_bytes(current_publisher)
        api.git(f.target, "add", "--", publisher_name)
        api.git(f.target, "commit", "-m", "Synthetic publisher-only descendant adoption #1401")
        assert api.git(f.target, "rev-parse", "HEAD^").strip() == source_head
        assert api.git(
            f.target, "diff-tree", "--no-commit-id", "--name-only", "-r", "HEAD"
        ).decode().splitlines() == [publisher_name]
        assert (
            successor.verify_completed(f.target, stage, source_receipt / "application.json")[
                "status"
            ]
            == "COMPLETE_CURRENT_SOURCE_SUCCESSOR"
        )
        assert (stage / "manifest.json").read_bytes() == source_manifest
        assert (source_receipt / "application.json").read_bytes() == source_application
        endpoint = f.target / "correction/endpoint.json"
        write(
            endpoint,
            {
                "schema_version": 1,
                "capability": successor.CAPABILITY,
                "root": str(f.target),
                "stage": str(stage.relative_to(f.target)),
                "manifest": ref(f.target, stage / "manifest.json"),
                "receipt": ref(f.target, source_receipt / "application.json"),
                "producer": manifest["producer"],
            },
        )
        p = publication(f, endpoint, tmp)
        request, publication_stage, _ = p.prepare()
        publication_acceptance = p.accept(request, publication_stage)
        yield f, p, request, publication_stage, publication_acceptance, source_receipt


def test_1401_clean_tracked_native_apply_and_completed_reconstruction(tracked_publication):
    f, p, request, stage, acceptance, source_receipt = tracked_publication
    before = current_outputs(f.target)
    original_source = (source_receipt / "application.json").read_bytes()
    original_manifest = (f.target / "correction/endpoint.json").read_bytes()
    proof = json.loads((stage / "manifest.json").read_bytes())["source_publication_handoff"]
    assert proof["capability"] == pub.SOURCE_HANDOFF
    assert proof["delegated_outputs"] == list(pub.OUTPUTS)
    assert proof["source_sha256"] == pub.SOURCE_HANDOFF_SOURCE_SHA
    for name in (pub.CANONICAL, pub.SUPPRESSIONS):
        assert api.git(f.target, "diff", "HEAD", "--", name) == b""
    with restore([f.target / name for name in pub.OUTPUTS]):
        receipt = p.destination(request, "tracked-applied")
        result = pub.apply(f.target, stage, acceptance, receipt, enabled=True)
        assert result["state"] == "COMPLETE" and result["recovery_required"] is False
        assert result["scientific_approval_added"] is False
        verified = pub.verify_completed(f.target, stage, receipt / "application.json")
        assert verified["status"] == "COMPLETE_CURRENT_CANONICAL_CANDIDATE"
        assert verified["ordinary_release_review_required"] is True
        assert current_outputs(f.target) != before
        assert (source_receipt / "application.json").read_bytes() == original_source
        assert (f.target / "correction/endpoint.json").read_bytes() == original_manifest
        # Genuine native capture reconstructs the newly versioned publication
        # through the current semantic route without original transaction roots.
        reference = transition.capture(
            f.target, stage, receipt / "application.json", ".temp/handoff-semantic-evidence"
        )
        evidence = transition.Evidence(Inputs(f.target), reference)
        first = evidence.packet["sources"][0]
        adopted = evidence.document(first["root"], first["receipt"])
        baseline = {
            name: evidence.read(first["root"], ref) for name, ref in adopted["beforeimages"].items()
        }
        application = json.loads((receipt / "application.json").read_bytes())
        baseline[pub.CANONICAL] = evidence.read(
            str(f.target), application["beforeimages"][pub.CANONICAL]
        )
        original_root = f.target.parent
        portable = original_root.with_name(original_root.name + "-portable")
        unavailable = original_root.with_name(original_root.name + "-unavailable")
        shutil.copytree(f.target, portable)
        original_root.rename(unavailable)
        try:
            reconstructed = reconstruct_transition((portable, reference, baseline))
        finally:
            unavailable.rename(original_root)
        assert reconstructed["scope"] == "semantic_reconstruction_not_transaction_reexecution"
        assert reconstructed["provenance"]["scientific_approval_added"] is False
        assert reconstructed["provenance"]["ordinary_release_review_required"] is True
        assert len(reconstructed["source"]["operations"]) == 1
        retained = reconstructed["source"]["retained_contexts"][-1]["original_native_reviews"]
        assert retained["references"][0]["primary"]
        assert retained["references"][0]["skeptic"]
        assert len(retained["context"]["historical_obligations"]) == 2
        # The original standalone source verifier must still refuse current
        # canonical bytes as its historical beforeimage.
        selected = json.loads(original_manifest)
        with pytest.raises(ValueError):
            successor.verify_completed(
                f.target,
                f.target / selected["stage"],
                f.target / selected["receipt"]["path"],
            )
    assert current_outputs(f.target) == before


@pytest.mark.parametrize(
    "family",
    [
        "owner",
        "extra_owner",
        "ledger",
        "aggregate",
        "marker",
        "input",
        "archive",
        "receipt",
        "predecessor",
        "source_code",
        "unrelated",
        "git_index",
    ],
)
def test_1401_every_original_guard_family_stays_live(tracked_publication, family):
    f, _, request, _, _, _ = tracked_publication
    loaded = pub.Loaded(f.target, request.path)
    handoff = loaded.adopted
    handoff.check()
    initial_dirty = set(handoff.source.initial_dirty)
    root = f.target
    if family == "owner":
        path = root / next(iter(handoff.owners))
    elif family == "extra_owner":
        path = root / "data/ingredients/unmapped/Unexpected.yaml"
    elif family == "ledger":
        path = handoff.ledgers[0].path
    elif family == "aggregate":
        path = root / api.AGGREGATES[0]
    elif family == "marker":
        path = root / successor.MARKER
    elif family == "input":
        path = root / "primary.txt"
    elif family == "archive":
        path = handoff.archives[0].path
    elif family == "receipt":
        path = handoff.endpoint.receipt_file.path
    elif family == "predecessor":
        path = handoff.source.predecessor.root / "primary.txt"
    elif family == "source_code":
        path = root / pub.SOURCE_HANDOFF_SOURCE
    elif family == "unrelated":
        path = root / "unrelated-tracked.txt"
    else:
        index = root / ".git/index"
        with restore([index]):
            original_index = api.git(root, "ls-files", "--stage", "-z")
            api.git(root, "update-index", "--force-remove", "unrelated-tracked.txt")
            assert api.git(root, "ls-files", "--stage", "-z") != original_index
            with pytest.raises(ValueError, match="Git context"):

                handoff.check()
        assert handoff.source.initial_dirty == initial_dirty
        return
    with restore([path]):
        raw = path.read_bytes() if path.exists() else b""
        path.write_bytes(raw + b"\n# actual guarded drift for #1401\n")
        with pytest.raises((ValueError, KeyError)):
            handoff.check()
    assert handoff.source.initial_dirty == initial_dirty


def test_1401_unsupported_source_revision_and_changed_context_are_refused(tracked_publication):
    f, _, request, _, _, _ = tracked_publication
    loaded = pub.Loaded(f.target, request.path)
    handoff = loaded.adopted
    original = dict(handoff.producer)
    handoff.producer = {**original, "source_sha256": "0" * 64}
    with pytest.raises(ValueError, match="unsupported source handoff"):
        handoff.check()
    handoff.producer = original
    initial = set(handoff.source.initial_dirty)
    handoff.source.initial_dirty.add("unrelated-tracked.txt")
    with pytest.raises(ValueError, match="captured context"):
        handoff.check()
    handoff.source.initial_dirty = initial
    handoff.check()


@pytest.mark.parametrize("attack", ["wrong_bytes", "alias"])
def test_1401_output_mutation_during_legitimate_write_is_not_delegated(
    tracked_publication, monkeypatch, attack
):
    f, p, request, stage, acceptance, _ = tracked_publication
    globals_ = pub.apply.__globals__
    original = globals_["publish_validated"]
    writes = []
    outside = request.directory / ("outside-output-" + attack)
    outside.write_bytes(b"must not change this file\n")

    def corrupt(*args, **kwargs):
        result = original(*args, **kwargs)
        writes.append(result.path)
        if len(writes) == 1:
            if attack == "alias":
                result.path.unlink()
                result.path.symlink_to(outside)
            else:
                result.path.write_bytes(b"wrong canonical bytes\n")
        return result

    with restore([f.target / name for name in pub.OUTPUTS]):
        monkeypatch.setitem(globals_, "publish_validated", corrupt)
        receipt = p.destination(request, "output-drift-" + attack)
        with pytest.raises(ValueError):
            pub.apply(f.target, stage, acceptance, receipt, enabled=True)
        report = json.loads((receipt / "application.json").read_bytes())
        assert writes == [f.target / pub.CANONICAL]
        assert report["state"] == "FAILED" and report["recovery_required"] is True
        assert outside.read_bytes() == b"must not change this file\n"
        if attack == "alias":
            (f.target / pub.CANONICAL).unlink()


def test_1401_missing_or_tampered_handoff_proof_cannot_reuse_acceptance(tracked_publication):
    f, _, _, stage, acceptance, _ = tracked_publication
    path = stage / "manifest.json"
    original = json.loads(path.read_bytes())
    for changed in ({}, {"capability": pub.SOURCE_HANDOFF, "delegated_outputs": [pub.CANONICAL]}):
        with restore([path]):
            manifest = dict(original)
            manifest["source_publication_handoff"] = changed
            write(path, manifest)
            with pytest.raises(ValueError, match="source publication handoff"):
                pub.apply(f.target, stage, acceptance, stage / "never-applied", enabled=False)
