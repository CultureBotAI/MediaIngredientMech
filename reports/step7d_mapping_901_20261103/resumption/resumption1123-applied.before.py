"""Receipt24 qualifies superseded concern text without renewing approval (#1112)."""

import copy
import importlib.util
import json
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
PATH = ROOT / "reports/sssom_completion_20260921/assemble_review.py"
SPEC = importlib.util.spec_from_file_location("source_concern_assembler", PATH)
assembler = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(assembler)
BATCH = "issue751-313-235-stock-and-source-labels"
STEMS = ("14-Butanediol", "5-dehydro-D-gluconate", "Phenethylamine_Hydrochloride",
         "Wc_Trace_Elements_Solution")


@pytest.fixture(scope="module")
def native_context():
    here = PATH.parent
    return {
        "chain": assembler.verify_mapping_chain(ROOT),
        "baseline": json.loads((here / "baseline-mapping-review.json").read_bytes()),
        "concerns": json.loads((here / "mapping_review/concern_cohorts.json").read_bytes())["rows"],
    }


def arguments(context, stem="14-Butanediol"):
    owner = f"data/ingredients/mapped/{stem}.yaml"
    entry = next(item for item in context["concerns"] if item["source_record"] == owner)
    proof = context["chain"]
    position = proof["forward"][entry["source_position"] - 1]
    return {
        "entry": copy.deepcopy(entry),
        "mapping": copy.deepcopy(proof["state"][position - 1]),
        "owner": owner,
        "owner_hash": assembler.digest(ROOT / owner),
        "chain": copy.deepcopy(proof),
        "baseline": copy.deepcopy(context["baseline"]),
        "current_position": position,
    }


@pytest.mark.parametrize("stem", STEMS)
def test_actual_corrected_concern_keeps_quote_and_proved_owner_row_lineage(native_context, stem):
    args = arguments(native_context, stem)
    before = copy.deepcopy(args)
    reason, proof = assembler.qualify_source_mapping_concern(**args)
    assert args == before
    assert reason.startswith("Historical concern recorded before the verified source/mapping correction")
    assert args["entry"]["reason"] in reason
    assert "not the current corrected payload" in reason
    assert "remains WITHHOLD pending fresh mapping-specific review" in reason
    assert "role and component concerns remain" in reason
    assert "no provisional role is approved" in reason
    assert "retires no historical finding and adds no scientific approval" in reason
    assert proof["owner_supersession"]["owner_record"] == args["owner"]
    assert proof["owner_supersession"]["current_sha256"] == args["owner_hash"]
    assert proof["historical_row_sha256"] == assembler.row_sha256(args["entry"]["mapping"])
    assert proof["current_row_sha256"] == assembler.row_sha256(args["mapping"])
    assert proof["mapping_correction"]["batch"] == BATCH
    assert proof["mapping_correction"]["after_row_sha256"] == proof["current_row_sha256"]


def test_unchanged_owner_retains_original_reason(native_context):
    args = arguments(native_context)
    args["owner_hash"] = args["entry"]["source_record_sha256"]
    assert assembler.qualify_source_mapping_concern(**args) == (args["entry"]["reason"], None)


def test_other_concerns_in_same_receipt_keep_original_basis(native_context):
    args = arguments(native_context, "24-diamino-67-di-iso-propylpteridine_phosphate")
    assert assembler.qualify_source_mapping_concern(**args) == (args["entry"]["reason"], None)


@pytest.mark.parametrize("changed", ["shape", "batch"])
def test_unrelated_correction_cannot_qualify_a_concern(native_context, changed):
    args = arguments(native_context)
    receipt = next(r for r in args["chain"]["receipts"] if r["batch"] == BATCH)
    if changed == "batch":
        receipt["batch"] = "unrelated-batch"
    else:
        record = next(r for r in receipt["records"] if r["source_record"] == args["owner"])
        record["shape"] = "unrelated_change"
    assert assembler.qualify_source_mapping_concern(**args) == (args["entry"]["reason"], None)


@pytest.mark.parametrize(
    "mutation",
    ["archived-owner", "current-owner", "owner-path", "archived-source", "archived-row",
     "current-position", "current-row", "forward-position", "receipt-before", "receipt-after",
     "receipt-hash", "receipt-mapping", "unsupported-disposition"],
)
def test_unverified_owner_or_row_transition_is_rejected(native_context, mutation):
    args = arguments(native_context)
    receipt = next(r for r in args["chain"]["receipts"] if r["batch"] == BATCH)
    record = next(r for r in receipt["records"] if r["source_record"] == args["owner"])
    if mutation == "archived-owner":
        args["entry"]["source_record_sha256"] = "0" * 64
    elif mutation == "current-owner":
        args["owner_hash"] = "0" * 64
    elif mutation == "owner-path":
        args["entry"]["source_record"] = "data/ingredients/mapped/Water.yaml"
    elif mutation == "archived-source":
        args["entry"]["sssom_source_sha256"] = "0" * 64
    elif mutation == "archived-row":
        args["entry"]["mapping"]["other"] = "unreviewed"
    elif mutation == "current-position":
        args["current_position"] += 1
    elif mutation == "current-row":
        args["mapping"]["other"] = "unreviewed"
    elif mutation == "forward-position":
        args["chain"]["forward"][args["entry"]["source_position"] - 1] += 1
    elif mutation in {"receipt-before", "receipt-after"}:
        field = "before_yaml_sha256" if mutation == "receipt-before" else "after_yaml_sha256"
        record[field] = "0" * 64
    elif mutation == "receipt-hash":
        index = args["chain"]["receipts"].index(receipt)
        args["chain"]["receipt_inputs"][args["chain"]["receipt_paths"][index]] = "0" * 64
    elif mutation == "receipt-mapping":
        change = next(c for c in receipt["changes"] if c["after"] == args["mapping"])
        change["after"]["other"] = "unreviewed"
    else:
        args["entry"]["disposition"] = "SUPPORTED"
    with pytest.raises(ValueError):
        assembler.qualify_source_mapping_concern(**args)


def test_native_assembly_keeps_all_holds_and_exact_negative_evidence(native_context):
    """Compute native output in memory; never overwrite archived/current files."""
    here = PATH.parent
    preserved = {path: path.read_bytes() for path in (
        here / "mapping_review/concern_cohorts.json",
        here / "mapping_review/issue-intersections.json",
        here / "review.json",
        here / "mapping-evidence.json",
    )}
    previous = json.loads(preserved[here / "review.json"])
    previous_evidence = json.loads(preserved[here / "mapping-evidence.json"])
    result = assembler.assemble()
    review = json.loads(result["review.json"])
    evidence = json.loads(result["mapping-evidence.json"])
    old_decisions = {item["source_position"]: item for item in previous["decisions"]}
    decisions = {item["source_position"]: item for item in review["decisions"]}
    changed = set()
    for stem in STEMS:
        args = arguments(native_context, stem)
        position = args["current_position"]
        changed.add(position)
        item = evidence["entries"][str(position)]
        reason, proof = assembler.qualify_source_mapping_concern(**args)
        assert decisions[position]["disposition"] == item["disposition"] == "WITHHOLD"
        assert reason in decisions[position]["review_reason"] == item["review_reason"]
        assert item["basis"]["historical_concern"] == proof
        old_item = previous_evidence["entries"][str(position)]
        assert item["basis"].get("negative_reviews") == old_item["basis"].get("negative_reviews")
        assert item["basis"]["mapping_change"] == BATCH
        if stem == "Wc_Trace_Elements_Solution":
            assert "TRACE_ELEMENT" in item["review_reason"]
            assert "non-exact relation" in item["review_reason"]
            assert item["basis"]["policy"] == old_item["basis"]["policy"]
        if stem == "5-dehydro-D-gluconate":
            assert args["mapping"]["other"] == ""
            assert item["basis"]["negative_reviews"][0]["reason"] == args["entry"]["reason"]
    receipt = next(r for r in native_context["chain"]["receipts"] if r["batch"] == BATCH)
    touched = {c["after_position"] for c in receipt["changes"]}
    assert len(touched) == 8
    assert all(decisions[p]["disposition"] == "WITHHOLD" for p in touched)
    for position, decision in decisions.items():
        if position not in changed:
            assert decision == old_decisions[position]
            assert evidence["entries"][str(position)] == previous_evidence["entries"][str(position)]
    assert all(path.read_bytes() == raw for path, raw in preserved.items())

