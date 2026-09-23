"""A follow-up review cannot silently approve changed claims or evidence (#752)."""

import importlib.util
from pathlib import Path

import pytest

from mediaingredientmech.export.reviewed_sssom import digest, row_sha256

_PATH = Path(__file__).resolve().parents[1] / "reports/sssom_completion_20260921/assemble_review.py"
_SPEC = importlib.util.spec_from_file_location("mapping_followup_assembler", _PATH)
assembler = importlib.util.module_from_spec(_SPEC)
_SPEC.loader.exec_module(assembler)


@pytest.fixture
def reviewed(tmp_path):
    """Provide a claim whose prior alias objection was explicitly reconsidered."""
    (tmp_path / "evidence.md").write_text("Reviewed structure and complete alias scope.\n")
    row = {
        "subject_id": "MIM:A",
        "predicate_id": "skos:exactMatch",
        "object_id": "CHEBI:1",
        "other": "alias",
    }
    negative = [
        {"reason": "Alias scope previously unreviewed", "evidence": "prior.json", "detail": "A"}
    ]
    entry = {
        "mapping": dict(row),
        "row_sha256": row_sha256(row),
        "owner_record": "A.yaml",
        "owner_record_sha256": "owner-digest",
        "disposition": "SUPPORTED",
        "reason": "Same structure and alias verified",
        "identity_review": "Specific chemical form reviewed",
        "token_reviews": {"alias": "Same structure"},
        "evidence_inputs": {"evidence.md": digest(tmp_path / "evidence.md")},
        "resolved_negative_reviews": negative,
    }
    return entry, row, negative, tmp_path


def apply(reviewed, **kwargs):
    entry, row, negative, root = reviewed
    return assembler.apply_followup(entry, row, "A.yaml", "owner-digest", negative, root, **kwargs)


def test_exact_review_can_resolve_its_specific_prior_objection(reviewed):
    assert apply(reviewed)[0] == "SUPPORTED"


@pytest.mark.parametrize("field,value", [("other", "alias|unreviewed"), ("object_id", "CHEBI:2")])
def test_changed_claim_does_not_inherit_approval(reviewed, field, value):
    reviewed[1][field] = value
    with pytest.raises(ValueError, match="stale row or owner"):
        apply(reviewed)


def test_changed_owner_does_not_inherit_approval(reviewed):
    reviewed[0]["owner_record_sha256"] = "old-owner"
    with pytest.raises(ValueError, match="stale row or owner"):
        apply(reviewed)


def test_changed_evidence_cannot_be_reused(reviewed):
    (reviewed[3] / "evidence.md").write_text("Now contradicts the original decision.")
    with pytest.raises(ValueError, match="evidence changed"):
        apply(reviewed)


def test_all_exported_aliases_need_an_individual_review(reviewed):
    reviewed[0]["token_reviews"] = {}
    with pytest.raises(ValueError, match="every synonym token"):
        apply(reviewed)


def test_new_negative_finding_cannot_be_overridden_by_old_followup(reviewed):
    reviewed[0]["resolved_negative_reviews"] = []
    with pytest.raises(ValueError, match="exact prior negative reviews"):
        apply(reviewed)


def test_existing_grade_and_preparation_safeguards_still_apply(reviewed):
    with pytest.raises(ValueError, match="cannot override"):
        apply(reviewed, safeguards=["Preparation token requires separate source correction"])


def test_followup_does_not_approve_a_parent_relation(reviewed):
    entry, row, _, _ = reviewed
    row["predicate_id"] = "skos:broadMatch"
    entry.update(mapping=dict(row), row_sha256=row_sha256(row))
    with pytest.raises(ValueError, match="does not approve non-exact"):
        apply(reviewed)


@pytest.mark.parametrize("path", ["../evidence.md", "/evidence.md"])
def test_evidence_path_must_be_repository_relative(reviewed, path):
    reviewed[0]["evidence_inputs"] = {path: "digest"}
    with pytest.raises(ValueError, match="within repository"):
        apply(reviewed)


@pytest.mark.parametrize("mutation", [None, "external", "wrong_owner", "alias", "parent"])
def test_added_local_identity_requires_its_own_complete_review(reviewed, mutation):
    entry, row, _, root = reviewed
    row.update(object_id="kgmicrobe.ingredient:a", subject_label="A", object_label="A", other="")
    record = {"identifier": row["object_id"], "preferred_term": "A"}
    if mutation == "external":
        row["object_id"] = record["identifier"] = "NCIT:C1"
    elif mutation == "wrong_owner":
        record["identifier"] = "kgmicrobe.ingredient:b"
    elif mutation == "alias":
        row["other"] = "unreviewed mixture"
    elif mutation == "parent":
        row["predicate_id"] = "skos:broadMatch"
    entry.update(
        mapping=dict(row),
        row_sha256=row_sha256(row),
        token_reviews={},
        resolved_negative_reviews=[],
    )
    args = (entry, row, "A.yaml", "owner-digest", record, root)
    if mutation:
        with pytest.raises(ValueError):
            assembler.apply_added_identity_followup(*args)
    else:
        assert assembler.apply_added_identity_followup(*args)[0] == "SUPPORTED"
