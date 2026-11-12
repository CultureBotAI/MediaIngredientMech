"""Claw #1189 integration: native diagnostic exclusion is not row approval."""

from __future__ import annotations

import json
import subprocess
from pathlib import Path

import pytest

from mediaingredientmech.curate import stable_sssom_publication as pub
from tests import stable_publication_fixture as fixture_source
from tests.test_stable_id_adoption import api, commit, write
from tests.test_stable_sssom_publication import PublicationFixture, digest, ref, restore

OVERLAY = Path(__file__).parent / "fixtures/claw_registry_retirement1189"
ORIGIN_SHA = "64fdc5943581892351047674a1e422c7cb71072f8785c18385282ac0c4f80c0f"


def patched_producer(root):
    """Apply exact proposed upstream bytes to the original test-only c1 source."""
    origin_raw = (OVERLAY / "ORIGIN.json").read_bytes()
    assert api.sha(origin_raw) == ORIGIN_SHA
    origin = json.loads(origin_raw)
    patch = (OVERLAY / "producer.patch").read_bytes()
    assert api.sha(patch) == origin["patch_sha256"]
    assert origin["upstream_base"] == fixture_source.CLAW_REVISION
    for name, pins in origin["files"].items():
        assert digest(root / name) == pins["before_sha256"]
    subprocess.run(
        ["git", "apply", "--check", "-"], input=patch, cwd=root, check=True, capture_output=True
    )
    subprocess.run(["git", "apply", "-"], input=patch, cwd=root, check=True, capture_output=True)
    for name, pins in origin["files"].items():
        assert digest(root / name) == pins["after_sha256"]
    head = commit(root)
    assert head != fixture_source.CLAW_REVISION


@pytest.fixture(scope="module")
def retirement(tmp_path_factory):
    monkeypatch = pytest.MonkeyPatch()
    original = fixture_source.NativeReviewAdoptionFixture.__init__

    def constructor(self, *args, **kwargs):
        # Synthetic source form is fixed before real native SAVE/adoption.
        kwargs["original_records"][0]["identifier"] = "kgmicrobe.ingredient:Exact_~28Stock~29"
        original(self, *args, **kwargs)

    monkeypatch.setattr(fixture_source.NativeReviewAdoptionFixture, "__init__", constructor)
    try:
        f = PublicationFixture(tmp_path_factory.mktemp("retirement-native"), monkeypatch, None)
        patched_producer(f.producer)
        canonical = f.root / pub.CANONICAL
        metadata, fields, rows = pub.read_sssom(canonical)
        old = dict(rows[0])
        old.update(
            object_id="kgmicrobe.compound:obsolete_exact_stock",
            object_label="Exact",
            object_source="kgm:compound",
            comment="Obsolete generated row: retain all history",
        )
        rows.append(old)
        canonical.write_bytes(pub._render_candidate(canonical.read_bytes(), fields, rows))
        owner = next(
            p for p in (f.root / "data/ingredients/mapped").glob("*.yaml") if p.stem == "Exact"
        )
        import yaml

        f.evidence = f.root / "retirement-evidence.txt"
        f.evidence.write_text(
            "Synthetic original generator defect evidence; not a scientific approval.\n"
        )
        f.proposal = f.root / "retirement-proposal.json"
        proposal = {
            "schema_version": 1,
            "capability": "stable-registry-retirement-proposal-v1",
            "scope": "diagnostic_candidate_only",
            "author": "synthetic-proposal-author",
            "scientific_approval": False,
            "canonical": {"path": pub.CANONICAL, "sha256": digest(canonical)},
            "evidence_inputs": {f.evidence.name: digest(f.evidence)},
            "entries": [
                {
                    "row_position": 2,
                    "row": old,
                    "owner": {
                        "path": str(owner.relative_to(f.root)),
                        "sha256": digest(owner),
                        "mim_id": yaml.safe_load(owner.read_bytes())["mim_id"],
                    },
                    "reason": "Synthetic exact full-row retirement proposal, awaiting independent publication reviews",
                    "evidence": [f.evidence.name],
                }
            ],
        }
        write(f.proposal, proposal)
        before = canonical.read_bytes()
        with pytest.raises(ValueError, match="native generator failed"):
            pub.generate(
                f.root,
                f.producer,
                f.kg,
                f.adoption.stage,
                f.adoption.receipt / "application.json",
                f.root / ".temp/conflict-refusal",
            )
        assert canonical.read_bytes() == before
        assert (f.root / ".temp/conflict-refusal/FAILED.json").is_file()
        f.generation_dir = f.root / ".temp/retirement-generation"
        f.generated = pub.generate(
            f.root,
            f.producer,
            f.kg,
            f.adoption.stage,
            f.adoption.receipt / "application.json",
            f.generation_dir,
            f.proposal,
            digest(f.proposal),
        )
        f.generation_receipt = f.generation_dir / "receipt.json"
        assert canonical.read_bytes() == before
        yield f
    finally:
        monkeypatch.undo()


def test_1189_real_generation_replay_retains_unapproved_full_retirement(retirement):
    f = retirement
    manifest = json.loads((f.generation_dir / "generation.json").read_bytes())
    assert manifest["registry_retirement_proposal"]["content"] == json.loads(
        f.proposal.read_bytes()
    )
    assert manifest["registry_retirement_proposal"]["scientific_approval_added"] is False
    assert f.generated["registry_retirement_proposal"] == ref(f.root, f.proposal)
    request = f.request(assessed=False)
    removed = [r for r in request.selection["rows"] if r["candidate_position"] is None]
    assert len(removed) == 1
    assert removed[0]["disposition"] is None and removed[0]["reason"] is None
    assert "Obsolete generated row" in json.dumps(removed[0])
    before = (f.root / pub.CANONICAL).read_bytes()
    with pytest.raises(ValueError):
        pub.prepare(f.root, request.path, f.root / ".temp/unreviewed-retirement-stage")
    assert (f.root / pub.CANONICAL).read_bytes() == before


@pytest.mark.parametrize("change", ["proposal", "evidence", "omit_proposal", "omit_evidence"])
def test_1189_native_replay_refuses_changed_or_omitted_retirement_closure(retirement, change):
    f = retirement
    request = f.request(assessed=False)
    manifest_path = f.generation_dir / "generation.json"
    with restore([f.proposal, f.evidence, manifest_path, f.generation_receipt]):
        if change in {"proposal", "evidence"}:
            path = f.proposal if change == "proposal" else f.evidence
            path.write_bytes(path.read_bytes() + b" ")
        else:
            excluded = f.proposal if change == "omit_proposal" else f.evidence
            manifest = json.loads(manifest_path.read_bytes())
            manifest["source_inputs"] = [
                r for r in manifest["source_inputs"] if r["path"] != str(excluded)
            ]
            write(manifest_path, manifest)
            receipt = json.loads(f.generation_receipt.read_bytes())
            receipt["outputs"]["manifest"] = ref(f.root, manifest_path)
            write(f.generation_receipt, receipt)
            request.request["generation"] = ref(f.root, f.generation_receipt)
            write(request.path, request.request)
        with pytest.raises(ValueError, match="changed|digest|input hash differs|replay failed"):
            pub.inspect(f.root, request.path)


def test_1189_paired_native_removal_reviews_can_prepare_but_never_imply_release(retirement):
    f = retirement
    request = f.request()
    stage = f.root / ".temp/reviewed-retirement-stage"
    before = (f.root / pub.CANONICAL).read_bytes()
    manifest = pub.prepare(f.root, request.path, stage)
    assert manifest["scientific_approval_added"] is False
    assert (f.root / pub.CANONICAL).read_bytes() == before
    selection = request.selection
    removed = [r for r in selection["rows"] if r["candidate_position"] is None]
    assert len(removed) == 1 and removed[0]["disposition"] == "REMOVE_WITH_HISTORY"
    assert all(
        r["disposition"] == "INSTALL_WITHHOLD" for r in selection["rows"] if r["candidate_position"]
    )
    assert not (request.directory / "application.json").exists()
