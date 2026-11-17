"""#1431: explicit unknown is evidence-bound, never zero or scientific approval."""

import copy
import hashlib

import pytest
import yaml

from mediaingredientmech.occurrence_coverage import (
    content_sha256,
    load_coverage,
    occurrence_view,
    stored_counts,
)


def write_bundle(tmp_path):
    root = tmp_path / "data" / "ingredients"
    (root / "mapped").mkdir(parents=True)
    record = {
        "mim_id": "MIM:0000001",
        "identifier": "cas:1-00-0",
        "preferred_term": "reviewed material",
        "mapping_status": "MAPPED",
    }
    owner = root / "mapped" / "record.yaml"
    owner.write_text(yaml.safe_dump(record))
    bundle = tmp_path / "mappings" / "occurrence_coverage.yaml"
    bundle.parent.mkdir()
    source = bundle.parent / "source.tsv"
    source.write_text("source_id\tcontext\ns1\tone captured subset\n")
    digest = hashlib.sha256(source.read_bytes()).hexdigest()
    declaration = {
        "mim_id": record["mim_id"],
        "owner_sha256": hashlib.sha256(owner.read_bytes()).hexdigest(),
        "owner_content_sha256": content_sha256(record),
        "state": "UNKNOWN",
        "reason_code": "INCOMPLETE_SOURCE_COVERAGE",
        "reason": "Only a reviewed subset was captured; complete media usage is unknown.",
        "evidence": [{"path": "source.tsv", "sha256": digest, "description": "Frozen subset"}],
        "source_coverage": [
            {
                "source": "example",
                "revision": "v1",
                "evidence_path": "source.tsv",
                "source_sha256": digest,
                "scanned_at": "2026-11-17T00:00:00Z",
                "row_count": 1,
                "scope": "One subset, not the complete media universe",
            }
        ],
    }
    doc = {
        "contract": "mim-occurrence-coverage-v1",
        "created_at": "2026-11-17T00:00:00Z",
        "declarations": [declaration],
    }
    bundle.write_text(yaml.safe_dump(doc))
    return root, record, owner, bundle, doc


def save(bundle, doc):
    bundle.write_text(yaml.safe_dump(doc))


def test_unknown_distinct_from_zero_and_missing(tmp_path):
    root, record, _, bundle, _ = write_bundle(tmp_path)
    coverage = load_coverage(bundle, root)
    view = occurrence_view(record, {"cas:1-00-0": (1, 1)}, coverage)
    assert view["occurrence_statistics_state"] == "UNKNOWN"
    assert view["media_count"] is None and view["total_occurrences"] is None
    assert view["occurrence_statistics_provenance"]["coverage_sha256"] == coverage.sha256
    assert occurrence_view(record)["occurrence_statistics_state"] == "MISSING"
    zero = {**record, "occurrence_statistics": {"media_count": 0, "total_occurrences": 0}}
    assert occurrence_view(zero)["total_occurrences"] == 0
    assert occurrence_view(zero)["occurrence_statistics_state"] == "RECORDED"


@pytest.mark.parametrize(
    "field", ["reason", "evidence", "source_coverage", "owner_sha256", "state"]
)
def test_required_declaration_fields(tmp_path, field):
    root, _, _, bundle, doc = write_bundle(tmp_path)
    del doc["declarations"][0][field]
    save(bundle, doc)
    with pytest.raises(ValueError):
        load_coverage(bundle, root)


@pytest.mark.parametrize(
    "mutation",
    [
        "wrong_id",
        "owner_bytes",
        "owner_content",
        "duplicate",
        "evidence_bytes",
        "blank_reason",
        "extra_count",
        "timezone",
    ],
)
def test_binding_and_closed_shape_failures(tmp_path, mutation):
    root, _, owner, bundle, doc = write_bundle(tmp_path)
    item = doc["declarations"][0]
    if mutation == "wrong_id":
        item["mim_id"] = "MIM:0000002"
    elif mutation == "owner_bytes":
        owner.write_text(owner.read_text() + "# new bytes\n")
    elif mutation == "owner_content":
        item["owner_content_sha256"] = "0" * 64
    elif mutation == "duplicate":
        doc["declarations"].append(copy.deepcopy(item))
    elif mutation == "evidence_bytes":
        (bundle.parent / "source.tsv").write_text("changed")
    elif mutation == "blank_reason":
        item["reason"] = "   "
    elif mutation == "extra_count":
        item["total_occurrences"] = 0
    elif mutation == "timezone":
        doc["created_at"] = "2026-11-17T00:00:00"
    save(bundle, doc)
    with pytest.raises(ValueError):
        load_coverage(bundle, root)


@pytest.mark.parametrize("path_kind", ["absolute", "traversal", "symlink"])
def test_evidence_containment(tmp_path, path_kind):
    root, _, _, bundle, doc = write_bundle(tmp_path)
    outside = tmp_path / "outside.tsv"
    outside.write_text((bundle.parent / "source.tsv").read_text())
    if path_kind == "absolute":
        name = str(outside)
    elif path_kind == "traversal":
        name = "../outside.tsv"
    else:
        (bundle.parent / "escape.tsv").symlink_to(outside)
        name = "escape.tsv"
    doc["declarations"][0]["evidence"][0]["path"] = name
    save(bundle, doc)
    with pytest.raises(ValueError):
        load_coverage(bundle, root)


@pytest.mark.parametrize(
    "stats",
    [
        None,
        {},
        {"media_count": 0},
        {"media_count": 0, "total_occurrences": None},
        {"media_count": 0, "total_occurrences": -1},
        {"media_count": -1, "total_occurrences": 1},
        {"media_count": True, "total_occurrences": 1},
        {"media_count": 0, "total_occurrences": "1"},
        {"media_count": 0, "total_occurrences": 1.0},
        {"media_count": 2, "total_occurrences": 1},
    ],
)
def test_invalid_counts_cannot_be_unknown(stats):
    with pytest.raises(ValueError):
        stored_counts({"occurrence_statistics": stats})


def test_rejected_nonzero_separate_from_negative_or_order_errors():
    with pytest.raises(ValueError, match="REJECTED"):
        stored_counts(
            {
                "mapping_status": "REJECTED",
                "occurrence_statistics": {"media_count": 1, "total_occurrences": 2},
            }
        )
    assert stored_counts(
        {
            "mapping_status": "REJECTED",
            "occurrence_statistics": {"media_count": 0, "total_occurrences": 0},
        }
    ) == (0, 0)


@pytest.mark.parametrize(
    "stats", [None, {"media_count": 0}, {"media_count": 0, "total_occurrences": 0}]
)
def test_unknown_cannot_hide_present_statistics(tmp_path, stats):
    root, record, owner, bundle, doc = write_bundle(tmp_path)
    record["occurrence_statistics"] = stats
    owner.write_text(yaml.safe_dump(record))
    doc["declarations"][0].update(
        owner_sha256=hashlib.sha256(owner.read_bytes()).hexdigest(),
        owner_content_sha256=content_sha256(record),
    )
    save(bundle, doc)
    with pytest.raises(ValueError):
        load_coverage(bundle, root)


def test_changed_aggregate_does_not_reuse_owner_declaration(tmp_path):
    root, record, _, bundle, _ = write_bundle(tmp_path)
    coverage = load_coverage(bundle, root)
    with pytest.raises(ValueError, match="stale owner content"):
        occurrence_view({**record, "preferred_term": "another concept"}, coverage=coverage)


def add_native_observation_reviews(bundle, doc):
    """Synthetic fixture uses the real shared review schema and pair renderer."""
    import subprocess

    from mediaingredientmech.occurrence_coverage import _review_contract, observation_claim

    native = _review_contract()
    repo = bundle.parent.parent
    for argv in (
        ["init"],
        ["config", "user.name", "Occurrence test fixture"],
        ["config", "user.email", "fixture@example.invalid"],
        ["add", "."],
        ["commit", "-m", "Synthetic occurrence fixture"],
    ):
        subprocess.run(["git", "-C", str(repo), *argv], capture_output=True, check=True)
    head = subprocess.check_output(["git", "-C", str(repo), "rev-parse", "HEAD"], text=True).strip()
    item = doc["declarations"][0]
    obs = {
        "source": "example",
        "unit": "NONMEDIA_OBSERVATION",
        "count": 7,
        "scope": "source graph observation, not media usage",
        "evidence_path": "source.tsv",
        "primary_review_path": "reviews/structured/20260101T000000Z-primary/review.yaml",
        "skeptical_review_path": "reviews/structured/20260101T000000Z-skeptic/review.yaml",
        "attribution": "REVIEWED_SOURCE_SCOPE",
    }
    item["observations"] = [obs]
    claim = observation_claim(item, item["source_coverage"][0], obs)
    owner_path = "data/ingredients/mapped/record.yaml"
    for role in ("primary", "skeptical"):
        name = obs[f"{role}_review_path"]
        review = {
            "schema_version": "1.0.0",
            "review_id": name.split("/")[-2],
            "kind": "record",
            "repository": "CultureBotAI/MediaIngredientMech",
            "title": "Synthetic source-scoped observation review",
            "started_at": "2026-01-01T00:00:00Z",
            "finished_at": "2026-01-01T00:00:00Z",
            "reviewer": {
                "identity": role + " fixture",
                "kind": "agent",
                "independence": "independent",
                "independence_basis": "Separate synthetic reviewer fixture",
            },
            "skill": "review-yaml-record",
            "completion": "completed",
            "verdict": "pass",
            "scientific_review": True,
            "summary": "Synthetic count claim only; no source identity approval.",
            "source": {
                "git_revision": head,
                "state": "working_tree",
                "inputs": [
                    {"path": owner_path, "sha256": item["owner_sha256"], "role": "owner"},
                    {
                        "path": "mappings/source.tsv",
                        "sha256": item["source_coverage"][0]["source_sha256"],
                        "role": "source subset",
                    },
                ],
            },
            "targets": [
                {
                    "target_id": item["mim_id"],
                    "path": owner_path,
                    "label": "synthetic owner",
                    "kind": "maintained",
                    "ownership_note": "Synthetic test, not a real scientific assessment",
                }
            ],
            "scope": {
                "description": "Only the exact synthetic observation",
                "selection": "Fixture",
                "coverage": "full",
                "population_size": 1,
                "reviewed_target_ids": [item["mim_id"]],
            },
            "checks": [
                {
                    "check_id": "count",
                    "name": "Synthetic claim",
                    "required": True,
                    "status": "passed",
                    "summary": "Fixture count inspected",
                    "target_ids": [item["mim_id"]],
                    "evidence_ids": ["source"],
                }
            ],
            "evidence": [
                {
                    "evidence_id": "source",
                    "kind": "primary_source",
                    "reference": "mappings/source.tsv",
                    "accessed_at": "2026-01-01T00:00:00Z",
                    "support": "supports",
                    "summary": "Synthetic source-scoped example",
                }
            ],
            "assessments": [
                {
                    "assessment_id": "count",
                    "area": "quantity",
                    "topic": "Source-scoped count",
                    "outcome": "supported",
                    "summary": "Exact fixture count, not complete media usage",
                    "target_ids": [item["mim_id"]],
                    "evidence_ids": ["source"],
                    "dimensions": [
                        {
                            "name": "occurrence_claim_sha256",
                            "value": claim,
                            "definition": "Exact owner/source/count/unit/scope claim digest",
                            "evidence_ids": ["source"],
                        }
                    ],
                }
            ],
            "findings": [],
            "actions": [],
            "limitations": [],
        }
        native.validate_review(review)
        path = bundle.parent / name
        path.parent.mkdir(parents=True)
        path.write_text(native._dump_document(review))
        path.with_name("review.md").write_text(native.render_markdown(review))
        for ev_path in (path, path.with_name("review.md")):
            item["evidence"].append(
                {
                    "path": str(ev_path.relative_to(bundle.parent)),
                    "sha256": hashlib.sha256(ev_path.read_bytes()).hexdigest(),
                    "description": "Native synthetic review fixture",
                }
            )
    save(bundle, doc)
    return obs


def test_observation_is_not_complete_media_usage(tmp_path):
    root, record, _, bundle, doc = write_bundle(tmp_path)
    add_native_observation_reviews(bundle, doc)
    coverage = load_coverage(bundle, root)
    result = occurrence_view(record, coverage=coverage)
    assert result["total_occurrences"] is None and result["media_count"] is None
    assert result["occurrence_statistics_provenance"]["observations"][0]["count"] == 7
    doc["declarations"][0]["reason_code"] = "SOURCE_ATTRIBUTION_WITHHELD"
    save(bundle, doc)
    with pytest.raises(ValueError, match="unsettled attribution"):
        load_coverage(bundle, root)


def test_known_membership_route_and_rejected_tombstone_preserved():
    rec = {
        "identifier": "CHEBI:1",
        "mapping_status": "MAPPED",
        "occurrence_statistics": {"media_count": 2, "total_occurrences": 3},
    }
    view = occurrence_view(rec, {"CHEBI:1": (4, 5)})
    assert (view["media_count"], view["total_occurrences"]) == (4, 5)
    rec.update(
        mapping_status="REJECTED", occurrence_statistics={"media_count": 0, "total_occurrences": 0}
    )
    assert occurrence_view(rec, {"CHEBI:1": (4, 5)})["total_occurrences"] == 0
