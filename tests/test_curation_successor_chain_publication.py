"""A published successor can precede another correction only through native proof."""

import copy
import json
import shutil

import pytest

from mediaingredientmech.curate import curation_successor as successor
from mediaingredientmech.curate import stable_sssom_publication as publication_api
from tests.test_curation_successor import ref
from tests.test_curation_successor_publication import corrected, publication
from tests.test_curation_successor_transition import maintained


def test_published_successor_predecessor_requires_native_publication_and_history(
    tmp_path, monkeypatch
):
    f, endpoint_path = corrected(tmp_path, monkeypatch)
    endpoint = json.loads(endpoint_path.read_bytes())
    p = publication(f, endpoint_path, tmp_path)
    request, stage, manifest = p.prepare()
    acceptance = p.accept(request, stage)
    # These are genuine pre-installation report inputs at a distinct real root;
    # installed canonical maps cannot replace their original scientific context.
    history = tmp_path / "frozen-publication-history"
    shutil.copytree(f.target, history)
    reviews = copy.deepcopy(f.endpoint["historical_reviews"])
    for reference in request.request["reviews"]:
        path = history / reference["path"]
        reviews.append(
            {
                "identity": successor._identity(history),
                "review": reference,
                "markdown_sha256": successor.native().sha(path.with_name("review.md").read_bytes()),
            }
        )
    destination = p.destination(request, "published-predecessor")
    publication_api.apply(f.target, stage, acceptance, destination, enabled=True)
    assert (
        publication_api.verify_completed(f.target, stage, destination / "application.json")[
            "status"
        ]
        == "COMPLETE_CURRENT_CANONICAL_CANDIDATE"
    )
    reference = {
        "kind": "successor",
        "identity": successor._identity(f.target),
        **{key: endpoint[key] for key in ("stage", "manifest", "receipt", "producer")},
        "publication_beforeimages": successor._optional_hashes(
            successor._optional(f.target, successor.PUBLICATION)
        ),
        "publication_proof": {
            "stage": str(stage.relative_to(f.target)),
            "manifest": ref(f.target, stage / "manifest.json"),
            "receipt": ref(f.target, destination / "application.json"),
            "producer": manifest["producer"],
        },
        "historical_reviews": reviews,
    }
    target = tmp_path / "next-target"
    shutil.copytree(f.target, target, ignore=shutil.ignore_patterns(".temp"))
    before = maintained(f.target)
    captured = successor.Predecessor(target, reference)
    assert captured.verify_native()["status"] == "COMPLETE_CURRENT_CANONICAL_CANDIDATE"
    assert maintained(f.target) == before
    for change in ("omit-publication", "omit-review"):
        wrong = copy.deepcopy(reference)
        if change == "omit-publication":
            wrong["publication_proof"] = None
        else:
            wrong["historical_reviews"].pop()
        with pytest.raises(ValueError):
            successor.Predecessor(target, wrong)
    assert maintained(f.target) == before
