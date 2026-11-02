"""Node cleanup qualifies historical concerns without renewing approval (#902)."""

import copy
import importlib.util
import json
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
PATH = ROOT / "reports/sssom_completion_20260921/assemble_review.py"
SPEC = importlib.util.spec_from_file_location("node_concern_assembler", PATH)
assembler = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(assembler)


@pytest.fixture(scope="module")
def native_context():
    here = PATH.parent
    return {
        "chain": assembler.verify_mapping_chain(ROOT),
        "baseline": json.loads((here / "baseline-mapping-review.json").read_bytes()),
        "concerns": json.loads((here / "mapping_review/concern_cohorts.json").read_bytes())["rows"],
    }


def arguments(context, stem="Casein"):
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


@pytest.mark.parametrize("stem", ["02_Thiamine_Pyrophosphate", "Casamino_Acids", "Casein"])
def test_actual_concern_and_exact_owner_correction_remain_withheld(native_context, stem):
    args = arguments(native_context, stem)
    original = copy.deepcopy(args)
    reason, proof = assembler.qualify_node_correction_concern(**args)
    assert args == original
    assert reason.startswith("Historical concern recorded before")
    assert args["entry"]["reason"] in reason
    assert "remains WITHHOLD" in reason
    assert "retires no historical finding and adds no scientific approval" in reason
    assert proof["owner_supersession"]["owner_record"] == args["owner"]
    assert proof["owner_supersession"]["current_sha256"] == args["owner_hash"]
    assert proof["historical_row_sha256"] == assembler.row_sha256(args["entry"]["mapping"])
    assert proof["current_row_sha256"] == assembler.row_sha256(args["mapping"])
    assert proof["node_corrections"][0]["batch"] == "issue753-870-registry-and-node-corrections"


def test_unchanged_owner_keeps_original_concern(native_context):
    args = arguments(native_context)
    args["owner_hash"] = args["entry"]["source_record_sha256"]
    assert assembler.qualify_node_correction_concern(**args) == (args["entry"]["reason"], None)


def test_unrelated_owner_change_does_not_qualify_a_node_correction(native_context):
    args = arguments(native_context)
    for receipt in args["chain"]["receipts"]:
        for item in receipt["records"]:
            if item["source_record"] == args["owner"]:
                item["shape"] = "unrelated_change"
    assert assembler.qualify_node_correction_concern(**args) == (args["entry"]["reason"], None)


def test_other_concerns_of_a_corrected_owner_keep_their_existing_wording(native_context):
    args = arguments(native_context, "Fish-sperm_Dna")
    assert "kg_microbe_node_id" not in args["entry"]["reason"]
    assert assembler.qualify_node_correction_concern(**args) == (args["entry"]["reason"], None)


@pytest.mark.parametrize(
    "mutation",
    [
        "archived-owner",
        "current-owner",
        "owner-path",
        "source-hash",
        "archived-row",
        "archived-position",
        "current-position",
        "current-row",
        "forward-position",
        "receipt-before",
        "receipt-after",
        "receipt-hash",
        "unsupported-disposition",
        "later-owner-drift",
    ],
)
def test_unproved_historical_qualification_is_rejected(native_context, mutation):
    args = arguments(native_context)
    if mutation == "archived-owner":
        args["entry"]["source_record_sha256"] = "0" * 64
    elif mutation in {"current-owner", "later-owner-drift"}:
        args["owner_hash"] = "0" * 64
    elif mutation == "owner-path":
        args["entry"]["source_record"] = "data/ingredients/mapped/Water.yaml"
    elif mutation == "source-hash":
        args["entry"]["sssom_source_sha256"] = "0" * 64
    elif mutation == "archived-row":
        args["entry"]["mapping"]["other"] = "unreviewed"
    elif mutation == "archived-position":
        args["entry"]["source_position"] += 1
    elif mutation == "current-position":
        args["current_position"] += 1
    elif mutation == "current-row":
        args["mapping"]["other"] = "unreviewed"
    elif mutation == "forward-position":
        args["chain"]["forward"][args["entry"]["source_position"] - 1] += 1
    elif mutation.startswith("receipt-"):
        index, receipt = next(
            (i, value)
            for i, value in enumerate(args["chain"]["receipts"])
            if value["batch"] == "issue753-870-registry-and-node-corrections"
        )
        record = next(item for item in receipt["records"] if item["source_record"] == args["owner"])
        if mutation == "receipt-hash":
            args["chain"]["receipt_inputs"][args["chain"]["receipt_paths"][index]] = "0" * 64
        else:
            record[
                "before_yaml_sha256" if mutation == "receipt-before" else "after_yaml_sha256"
            ] = ("0" * 64)
    else:
        args["entry"]["disposition"] = "SUPPORTED"
    with pytest.raises(ValueError):
        assembler.qualify_node_correction_concern(**args)


def test_current_safeguards_are_added_outside_the_historical_quotation(native_context):
    """Exercise native assembly: the qualifier must not erase the existing holds."""
    result = assembler.assemble()
    review = json.loads(result["review.json"])
    evidence = json.loads(result["mapping-evidence.json"])
    decisions = {item["source_position"]: item for item in review["decisions"]}
    for stem in ("02_Thiamine_Pyrophosphate", "Casamino_Acids", "Casein"):
        args = arguments(native_context, stem)
        position = args["current_position"]
        decision = decisions[position]
        item = evidence["entries"][str(position)]
        reason, proof = assembler.qualify_node_correction_concern(**args)
        assert decision["disposition"] == item["disposition"] == "WITHHOLD"
        assert reason in decision["review_reason"] == item["review_reason"]
        assert item["basis"]["historical_concern"] == proof
        if stem == "Casamino_Acids":
            assert (
                "Preparation/concentration/instruction tokens remain" in decision["review_reason"]
            )
            assert "The source grounding grade is CLOSE_MATCH" in decision["review_reason"]
            assert item["basis"]["policy"] and item["basis"]["preparation_tokens"]
