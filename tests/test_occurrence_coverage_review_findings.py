"""Independent regressions for #1463 and #1464; real native review contract."""

import copy
import hashlib

import pytest
import yaml

from mediaingredientmech.occurrence_coverage import (
    _review_contract,
    content_sha256,
    load_coverage,
)
from tests.test_occurrence_coverage import add_native_observation_reviews, save, write_bundle


def refresh_evidence(doc, bundle, path):
    relative = str(path.relative_to(bundle.parent))
    for entry in doc["declarations"][0]["evidence"]:
        if entry["path"] == relative:
            entry["sha256"] = hashlib.sha256(path.read_bytes()).hexdigest()


def test_1463_duplicate_reason_cannot_hide_withheld(tmp_path):
    root, _, _, bundle, doc = write_bundle(tmp_path)
    add_native_observation_reviews(bundle, doc)
    raw = bundle.read_text()
    needle = "  reason_code: INCOMPLETE_SOURCE_COVERAGE\n"
    assert raw.count(needle) == 1
    bundle.write_text(raw.replace(needle, "  reason_code: SOURCE_ATTRIBUTION_WITHHELD\n" + needle))
    with pytest.raises(ValueError, match="duplicate"):
        load_coverage(bundle, root)


def test_1463_duplicate_owner_status_cannot_hide_rejection(tmp_path):
    root, record, owner, bundle, doc = write_bundle(tmp_path)
    owner.write_text("mapping_status: REJECTED\n" + owner.read_text())
    assert yaml.safe_load(owner.read_bytes()) == record
    doc["declarations"][0]["owner_sha256"] = hashlib.sha256(owner.read_bytes()).hexdigest()
    save(bundle, doc)
    with pytest.raises(ValueError, match="duplicate"):
        load_coverage(bundle, root)


@pytest.mark.parametrize("kind", ["dot", "symlink", "hardlink"])
def test_1464_physical_evidence_alias_is_not_independent(tmp_path, kind):
    root, _, _, bundle, doc = write_bundle(tmp_path)
    add_native_observation_reviews(bundle, doc)
    item = doc["declarations"][0]
    primary = item["observations"][0]["primary_review_path"]
    if kind == "dot":
        alias = "./" + primary
    else:
        alias = "aliased-review.yaml"
        link = bundle.parent / alias
        if kind == "symlink":
            link.symlink_to(bundle.parent / primary)
        else:
            link.hardlink_to(bundle.parent / primary)
    ev = next(e for e in item["evidence"] if e["path"] == primary)
    item["evidence"].append({**ev, "path": alias})
    item["observations"][0]["skeptical_review_path"] = alias
    save(bundle, doc)
    with pytest.raises(ValueError, match="aliased physical"):
        load_coverage(bundle, root)


def test_1464_source_name_cannot_select_two_revisions(tmp_path):
    root, _, _, bundle, doc = write_bundle(tmp_path)
    item = doc["declarations"][0]
    other = copy.deepcopy(item["source_coverage"][0])
    other["revision"] = "v2"
    item["source_coverage"].append(other)
    save(bundle, doc)
    with pytest.raises(ValueError, match="ambiguous source"):
        load_coverage(bundle, root)


@pytest.mark.parametrize(
    "field,new", [("count", 8), ("unit", "SOURCE_LISTING"), ("scope", "a larger universe")]
)
def test_1464_review_support_is_for_exact_observed_claim(tmp_path, field, new):
    root, _, _, bundle, doc = write_bundle(tmp_path)
    observation = add_native_observation_reviews(bundle, doc)
    observation[field] = new
    save(bundle, doc)
    with pytest.raises(ValueError, match="exact owner/source/count/unit/scope"):
        load_coverage(bundle, root)


def test_1464_version_change_needs_new_scientific_review(tmp_path):
    root, _, _, bundle, doc = write_bundle(tmp_path)
    add_native_observation_reviews(bundle, doc)
    doc["declarations"][0]["source_coverage"][0]["revision"] = "v2"
    save(bundle, doc)
    with pytest.raises(ValueError, match="exact owner/source/count/unit/scope"):
        load_coverage(bundle, root)


def test_1464_rehashing_owner_does_not_reapprove_prior_count_review(tmp_path):
    root, record, owner, bundle, doc = write_bundle(tmp_path)
    add_native_observation_reviews(bundle, doc)
    record["preferred_term"] = "new owner context"
    owner.write_text(yaml.safe_dump(record))
    doc["declarations"][0].update(
        owner_sha256=hashlib.sha256(owner.read_bytes()).hexdigest(),
        owner_content_sha256=content_sha256(record),
    )
    save(bundle, doc)
    with pytest.raises(ValueError, match="review input has changed"):
        load_coverage(bundle, root)


@pytest.mark.parametrize(
    "mutation", ["same_reviewer", "not_independent", "not_science", "wrong_claim"]
)
def test_1464_native_review_decisions_are_checked(tmp_path, mutation):
    root, _, _, bundle, doc = write_bundle(tmp_path)
    obs = add_native_observation_reviews(bundle, doc)
    native = _review_contract()
    path = bundle.parent / obs["skeptical_review_path"]
    review = native.load_document(path.read_bytes())
    if mutation == "same_reviewer":
        review["reviewer"]["identity"] = "primary fixture"
    elif mutation == "not_independent":
        review["reviewer"]["independence"] = "self_review"
    elif mutation == "not_science":
        review["scientific_review"] = False
    else:
        review["assessments"][0]["dimensions"][0]["value"] = "0" * 64
    # Changes are valid generic native reports; the occurrence-specific binding
    # must still reject them instead of merely checking shape or file hashes.
    native.validate_review(review)
    path.write_text(native._dump_document(review))
    path.with_name("review.md").write_text(native.render_markdown(review))
    for p in (path, path.with_name("review.md")):
        refresh_evidence(doc, bundle, p)
    save(bundle, doc)
    with pytest.raises(ValueError):
        load_coverage(bundle, root)


def test_1464_arbitrary_json_is_not_a_native_count_review(tmp_path):
    root, _, _, bundle, doc = write_bundle(tmp_path)
    obs = add_native_observation_reviews(bundle, doc)
    path = bundle.parent / obs["primary_review_path"]
    path.write_text('{"approved": true}')
    refresh_evidence(doc, bundle, path)
    save(bundle, doc)
    with pytest.raises(ValueError):
        load_coverage(bundle, root)
