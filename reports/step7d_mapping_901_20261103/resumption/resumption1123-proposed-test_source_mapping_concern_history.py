"""Receipt24 qualifies superseded concern text without renewing approval (#1112)."""

import copy
import hashlib
import importlib.util
import json
from pathlib import Path

import pytest

from mediaingredientmech.validation.mapping_change_receipts import walk_mapping_changes

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


def receipt_current_rows(chain):
    """Follow receipt24 row identities through the complete verified suffix."""
    matches = [(i, r) for i, r in enumerate(chain["receipts"]) if r["batch"] == BATCH]
    assert len(matches) == 1, "Expected one source-correction receipt"
    index, receipt = matches[0]
    touched = {}
    for change in receipt["changes"]:
        position, payload = change["after_position"], change["after"]
        assert position is not None and payload is not None, "Corrected endpoint was removed"
        assert chain["states_after_sequence"][receipt["sequence"]][position - 1] == payload
        for following in chain["receipts"][index + 1:]:
            assert not any(c.get("before_position") == position for c in following["changes"]), (
                "Later receipt changed or removed a source-correction endpoint"
            )
            position = following["position_map"][position - 1]
            assert position is not None, "Later receipt removed a source-correction endpoint"
            assert chain["states_after_sequence"][following["sequence"]][position - 1] == payload, (
                "Later receipt position does not retain the corrected row payload"
            )
        assert chain["state"][position - 1] == payload, "Current corrected row payload differs"
        assert position not in touched, "Corrected row lineages collided"
        touched[position] = payload
    return touched


def assert_receipt_rows_withheld(chain, decisions):
    touched = receipt_current_rows(chain)
    assert len(touched) == 8
    assert all(decisions[p]["disposition"] == "WITHHOLD" for p in touched)
    return touched


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
    assert_receipt_rows_withheld(native_context["chain"], decisions)
    for position, decision in decisions.items():
        if position not in changed:
            assert decision == old_decisions[position]
            assert evidence["entries"][str(position)] == previous_evidence["entries"][str(position)]
    assert all(path.read_bytes() == raw for path, raw in preserved.items())



def append_verified_suffix(chain, operations):
    """Build native-validated in-memory insert/remove receipts, without file writes."""
    result = copy.deepcopy(chain)
    for offset, operation in enumerate(operations, 1):
        before = result["state"]
        after = copy.deepcopy(before)
        sequence = result["receipts"][-1]["sequence"] + 1
        if operation == "insert":
            added = dict(before[0], subject_id=f"MIM:Later_receipt_insert_{offset}")
            after.insert(0, added)
            positions = list(range(2, len(before) + 2))
            changes = [{"kind": "added", "before_position": None, "after_position": 1,
                        "before": None, "after": added}]
        elif operation == "remove":
            assert 1 not in receipt_current_rows(result), "Fixture must remove an unrelated row"
            removed = after.pop(0)
            positions = [None, *range(1, len(before))]
            changes = [{"kind": "removed", "before_position": 1, "after_position": None,
                        "before": removed, "after": None}]
        elif operation == "remove-and-readd-held":
            position = min(receipt_current_rows(result))
            removed = after.pop(position - 1)
            after.append(removed)
            positions = [p if p < position else p - 1 if p > position else None
                         for p in range(1, len(before) + 1)]
            changes = [
                {"kind": "removed", "before_position": position, "after_position": None,
                 "before": removed, "after": None},
                {"kind": "added", "before_position": None, "after_position": len(after),
                 "before": None, "after": removed},
            ]
        else:
            raise AssertionError("Unknown fixture operation")
        endpoint = hashlib.sha256(json.dumps(after, sort_keys=True).encode()).hexdigest()
        receipt = {
            "schema_version": 1, "batch": f"later-position-fixture-{sequence}",
            "sequence": sequence, "issue": "fixture", "scope": "Position-lineage regression",
            "approval": "NONE: synthetic test receipt adds no approval",
            "before_sha256": result["reviewed_sha256"], "after_sha256": endpoint,
            "before_row_count": len(before), "after_row_count": len(after),
            "records": [], "changes": changes, "position_map": positions,
            "changed_rows": 0, "added_rows": sum(c["kind"] == "added" for c in changes),
            "removed_rows": sum(c["kind"] == "removed" for c in changes),
        }
        result["receipts"].append(receipt)
        forward, last, state = walk_mapping_changes(
            result["receipts"], start_sha256=result["start_sha256"],
            reviewed_sha256=endpoint, baseline_rows=result["baseline_rows"],
            refreshed_rows=result["refreshed_rows"],
        )
        assert state == after
        result.update(forward=forward, last=last, state=state, reviewed_sha256=endpoint)
        result["states_after_sequence"][sequence] = copy.deepcopy(state)
    return result


@pytest.mark.parametrize(
    "operations,shift", [(("insert",), 1), (("remove",), -1),
                         (("insert", "remove", "insert"), 1)],
)
def test_receipt24_positions_follow_every_verified_insertion_and_removal(native_context, operations, shift):
    original = native_context["chain"]
    before = receipt_current_rows(original)
    shifted = append_verified_suffix(original, operations)
    after = receipt_current_rows(shifted)
    assert after == {position + shift: payload for position, payload in before.items()}
    assert len(after) == 8
    assert original == native_context["chain"]


@pytest.mark.parametrize("mutation", ["wrong-map", "wrong-current-payload", "remove-and-readd-held"])
def test_wrong_receipt24_row_lineage_fails(native_context, mutation):
    chain = append_verified_suffix(native_context["chain"], ("insert",))
    if mutation == "remove-and-readd-held":
        chain = append_verified_suffix(chain, ("remove-and-readd-held",))
    elif mutation == "wrong-map":
        current = min(receipt_current_rows(chain))
        chain["receipts"][-1]["position_map"][current - 2] = 1
    else:
        current = min(receipt_current_rows(chain))
        chain["state"][current - 1] = dict(chain["state"][0])
    with pytest.raises(AssertionError):
        receipt_current_rows(chain)


@pytest.mark.parametrize("touched_index", range(8))
def test_actually_supported_corrected_row_still_fails(native_context, touched_index):
    decisions = {item["source_position"]: item for item in
                 json.loads((PATH.parent / "review.json").read_bytes())["decisions"]}
    touched = assert_receipt_rows_withheld(native_context["chain"], decisions)
    position = sorted(touched)[touched_index]
    decisions[position]["disposition"] = "SUPPORTED"
    with pytest.raises(AssertionError):
        assert_receipt_rows_withheld(native_context["chain"], decisions)
