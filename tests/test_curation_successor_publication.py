"""Actual offline source correction to native stable publication (#1373)."""

import gzip
import json

import pytest

from mediaingredientmech.curate import curation_successor as successor
from mediaingredientmech.curate import stable_sssom_publication as pub
from tests.stable_publication_fixture import materialize_producer
from tests.test_curation_successor import SuccessorFixture, ref
from tests.test_curation_successor_transition import maintained, prepared
from tests.test_stable_id_adoption import api, commit, initialize, write
from tests.test_stable_sssom_publication import PublicationFixture


def corrected(tmp_path, monkeypatch):
    """Build a genuine corrected native endpoint with real unchanged predecessor."""
    f = SuccessorFixture(tmp_path, monkeypatch, publication_baseline=True)
    stage, acceptance, manifest = prepared(f)
    receipt = f.target / ".temp/source-correction-application"
    successor.apply(f.target, stage, acceptance, receipt, enabled=True)
    assert (
        successor.verify_completed(f.target, stage, receipt / "application.json")["status"]
        == "COMPLETE_CURRENT_SOURCE_SUCCESSOR"
    )
    endpoint = f.target / "correction/endpoint.json"
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
    return f, endpoint


def publication(f, endpoint, tmp_path):
    """Reuse the existing real producer and paired publication-review fixture."""
    p = PublicationFixture.__new__(PublicationFixture)
    p.root, p.adoption, p.counter = f.target, f.original, 0
    p.adoption.root = f.target
    p.adoption.policy = f.target / "operational-policy.json"
    p.histories = [
        {
            "root": r["identity"]["root"],
            "head": r["identity"]["head"],
            "review": r["review"],
            "markdown_sha256": r["markdown_sha256"],
        }
        for r in f.endpoint["historical_reviews"]
    ]
    p.history = p.histories[0]
    p.producer = tmp_path / "producer"
    materialize_producer(p.producer)
    p.kg = tmp_path / "kg"
    initialize(p.kg)
    mapping = p.kg / "mappings/kgmicrobe_unified_entity_mappings.sssom.tsv.gz"
    mapping.parent.mkdir()
    mapping.write_bytes(
        gzip.compress(
            b"subject_id\tsubject_label\tpredicate_id\tobject_id\tobject_label\tsource\n", mtime=0
        )
    )
    commit(p.kg)
    p.generation_dir = f.target / ".temp/successor-generation"
    p.generated = pub.generate(
        f.target,
        p.producer,
        p.kg,
        None,
        None,
        p.generation_dir,
        curation_successor=endpoint,
        curation_successor_sha256=api.sha(endpoint.read_bytes()),
    )
    p.generation_receipt = p.generation_dir / "receipt.json"
    return p


def test_real_corrected_endpoint_native_generation_publication_and_archived_verification(
    tmp_path, monkeypatch
):
    """Full native chain retains all four beforeimages and separate reviewed science."""
    f, endpoint = corrected(tmp_path, monkeypatch)
    original = maintained(f.predecessor)
    p = publication(f, endpoint, tmp_path)
    assert p.generated["adoption"] is None
    assert p.generated["curation_successor"] == ref(f.target, endpoint)
    request, stage, _ = p.prepare()
    acceptance = p.accept(request, stage)
    destination = p.destination(request, "applied")
    result = pub.apply(f.target, stage, acceptance, destination, enabled=True)
    assert result["state"] == "COMPLETE" and result["scientific_approval_added"] is False
    proof = pub.verify_completed(f.target, stage, destination / "application.json")
    assert proof["status"] == "COMPLETE_CURRENT_CANONICAL_CANDIDATE"
    assert proof["ordinary_release_review_required"] is True
    assert maintained(f.predecessor) == original
    # A standalone old source-completion verifier may not silently pretend the
    # installed canonical table is its historical beforeimage.
    value = json.loads(endpoint.read_bytes())
    with pytest.raises(ValueError):
        successor.verify_completed(
            f.target, f.target / value["stage"], f.target / value["receipt"]["path"]
        )
    # Nor may a caller authorize historical verification by passing a raw map.
    with pytest.raises(ValueError, match="naked publication"):
        successor.Endpoint(f.target, value, publication=dict.fromkeys(successor.PUBLICATION))
    assert maintained(f.predecessor) == original
