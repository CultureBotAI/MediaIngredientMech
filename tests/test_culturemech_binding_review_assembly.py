"""An authored proof must cover exact cases before native finalization (#1453)."""

import importlib.util
import json
from pathlib import Path

import pytest

from mediaingredientmech.intake import culturemech as intake
from tests.test_culturemech_intake import handoff, prepared  # noqa: F401
from tests.test_reviewed_sssom import reviewed_fixture  # noqa: F401

HELPER = Path(__file__).parents[1] / "scripts/adhoc/assemble_culturemech_binding_review_1453.py"
SPEC = importlib.util.spec_from_file_location("binding_review_assembly", HELPER)
helper = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(helper)


def author_review(source, pin):
    cases = json.loads((source / "review-packet.json").read_text())["cases"]
    return {
        "intake_sha256": pin,
        "decisions": [
            {
                "case_id": case["case_id"],
                "row_sha256": intake.payload_sha256(case),
                "disposition": "SUPPORTED",
                "review_reason": "Synthetic Alpha is explicitly the exact synthetic owner; context is retained.",
                "canonical_row_sha256": case["candidate"]["supported_canonical_rows"][0][
                    "row_sha256"
                ],
                "inspected_descriptor_sha256": list(case["descriptors"]),
                "inspected_change_sha256": list(case.get("change_payloads", {})),
                "inspected_held_sha256": list(case.get("held_payloads", {})),
                "evidence_locators": [
                    "Synthetic fixture source descriptor and exact owner payload"
                ],
            }
            for case in cases
            if case["candidate"]["supported_canonical_rows"]
        ],
    }


def test_complete_authored_proof_passes_native_finalization(handoff):  # noqa: F811
    root, source, _manifest, pin = prepared(handoff)
    author = root / "author.json"
    intake.write_json(author, author_review(source, pin))
    output = root / "reports/binding-review"
    helper.assemble(source, pin, [author], output, root=root)
    final = intake.finalize(
        source, pin, "reports/binding-review/binding-review.json", root / "reviewed", root=root
    )
    assert final["counts"] == {"SUPPORTED": 3, "WITHHOLD": 3}
    review = json.loads((output / "binding-review.json").read_text())
    gated = [row for row in review["decisions"] if row["disposition"] == "WITHHOLD"]
    assert all("Canonical eligibility gate" in row["review_reason"] for row in gated)
    assert all("canonical_row_sha256" not in row for row in gated)
    assert (output / "author-1.json").read_bytes() == author.read_bytes()


@pytest.mark.parametrize("defect", ["missing_case", "stale_case", "omitted_descriptor"])
def test_incomplete_or_stale_author_review_cannot_publish(handoff, defect):  # noqa: F811
    root, source, _manifest, pin = prepared(handoff)
    review = author_review(source, pin)
    if defect == "missing_case":
        review["decisions"].pop()
    elif defect == "stale_case":
        review["decisions"][0]["row_sha256"] = "0" * 64
    else:
        review["decisions"][0]["inspected_descriptor_sha256"] = []
    author, output = root / "author.json", root / "reports/binding-review"
    intake.write_json(author, review)
    with pytest.raises(ValueError, match="needs an authored|Stale author|incomplete"):
        helper.assemble(source, pin, [author], output, root=root)
    assert not output.exists()


def witness_decision(case):
    sha = next(iter(case["descriptors"]))
    return {
        "disposition": "WITHHOLD",
        "inspected_descriptor_sha256": [sha],
        "inspected_change_sha256": [],
        "inspected_held_sha256": [],
        "blocking_witnesses": [
            {
                "payload_kind": "descriptor",
                "sha256": sha,
                "field_path": "/preferred_term",
                "reason": "Synthetic label lacks the specific form required by this hypothetical binding.",
            }
        ],
    }


def test_one_real_blocking_witness_does_not_attest_unread_payloads():
    descriptors = [{"preferred_term": "Unspecified salt"}, {"preferred_term": "Other form"}]
    case = {"descriptors": {intake.payload_sha256(value): value for value in descriptors}}
    decision = witness_decision(case)
    helper.validate_coverage(decision, case)
    assert len(decision["inspected_descriptor_sha256"]) == 1
    decision["disposition"] = "SUPPORTED"
    with pytest.raises(ValueError, match="incomplete"):
        helper.validate_coverage(decision, case)


@pytest.mark.parametrize("defect", ["empty", "nonmember", "stale", "missing_field"])
def test_bad_withhold_witness_cannot_publish(handoff, defect):  # noqa: F811
    root, source, _manifest, pin = prepared(handoff)
    review = author_review(source, pin)
    packet = json.loads((source / "review-packet.json").read_text())
    cases = {case["case_id"]: case for case in packet["cases"]}
    decision = review["decisions"][0]
    case = cases[decision["case_id"]]
    decision.update(witness_decision(case))
    decision.pop("canonical_row_sha256")
    if defect == "empty":
        decision["blocking_witnesses"] = []
    elif defect == "nonmember":
        decision["blocking_witnesses"][0]["sha256"] = "f" * 64
    elif defect == "stale":
        decision["inspected_descriptor_sha256"] = ["0" * 64]
        decision["blocking_witnesses"][0]["sha256"] = "0" * 64
    else:
        decision["blocking_witnesses"][0]["field_path"] = "/missing"
    author, output = root / "author.json", root / "reports/binding-review"
    intake.write_json(author, review)
    with pytest.raises(ValueError, match="witness|case member"):
        helper.assemble(source, pin, [author], output, root=root)
    assert not output.exists()


def test_stale_witness_digest_rejects_changed_payload():
    value = {"preferred_term": "Unspecified salt"}
    sha = intake.payload_sha256(value)
    case = {"descriptors": {sha: value}}
    decision = witness_decision(case)
    value["preferred_term"] = "Different salt"
    with pytest.raises(ValueError, match="Stale blocking"):
        helper.validate_coverage(decision, case)


def test_explicit_witness_survives_native_withhold_finalization(handoff):  # noqa: F811
    root, source, _manifest, pin = prepared(handoff)
    review = author_review(source, pin)
    packet = json.loads((source / "review-packet.json").read_text())
    cases = {case["case_id"]: case for case in packet["cases"]}
    decision = review["decisions"][0]
    decision.update(witness_decision(cases[decision["case_id"]]))
    decision.pop("canonical_row_sha256")
    decision["review_reason"] = (
        "Synthetic source form is unspecified; owner specificity is unsupported."
    )
    author, output = root / "author.json", root / "reports/binding-review"
    intake.write_json(author, review)
    helper.assemble(source, pin, [author], output, root=root)
    proof = json.loads((output / "binding-evidence.json").read_text())["entries"][
        decision["case_id"]
    ]
    assert proof["review_coverage"]["blocking_witnesses"] == decision["blocking_witnesses"]
    final = intake.finalize(
        source, pin, "reports/binding-review/binding-review.json", root / "reviewed", root=root
    )
    assert final["counts"] == {"SUPPORTED": 2, "WITHHOLD": 4}
