"""Independent complete source-case/proposal successor assembly audit."""
import copy
import datetime
import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
D = HERE.parent.parent
W = D.parents[3]
ART = W / "reports/all_unmatched_20261107/worker-01"
OLD = ART / "shard"
NEW = D / "cores/pre-review"

def load(p):
    return json.loads(p.read_text())

def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()

def rowsha(r):
    return hashlib.sha256(json.dumps(r, sort_keys=True, separators=(",", ":"), ensure_ascii=False, allow_nan=False).encode()).hexdigest()

def unchanged_scientific_core(old, new, update, metadata):
    expected = copy.deepcopy(old)
    expected.update(copy.deepcopy(update))
    actual = copy.deepcopy(new)
    for key in metadata:
        expected.pop(key, None)
        actual.pop(key, None)
    return expected == actual

pins = {"SELECTION.json": "aa03ac6c0abd551edeb5b8ae3f6b109753a985b820cbb7a83fa83d456197d3c7",
        "decisions.json": "9d9c86c17923b400813bff317778160d3cefa3bc8623c5c4360bd5ccaf0cfac1",
        "proposals.json": "75e0a4346f1f155b5baf547ef99cbda9d51a11eab2472d45f1f134555405f1b6",
        "evidence.json": "8c4a8604b9d96404cdf078f0081b01a4c651bdc40cd9de77cbc4039102ddd442"}
assert all(sha(NEW/n) == expected for n, expected in pins.items())
updates = load(D / "science/assembly-deltas-v1.json")
cu = {x["case_id"]: x for x in updates["case_updates"]}
pu = {x["proposal_id"]: x for x in updates["proposal_updates"]}
before_d, after_d = load(OLD/"decisions.json")["decisions"], load(NEW/"decisions.json")["decisions"]
before_p, after_p = load(OLD/"proposals.json")["proposals"], load(NEW/"proposals.json")["proposals"]
before_e, after_e = load(OLD/"evidence.json")["evidence"], load(NEW/"evidence.json")["evidence"]
selection = load(NEW/"SELECTION.json")
assert len(before_d) == len(after_d) == len({x["case_id"] for x in after_d}) == 188
assert len(before_p) == len(after_p) == len({x["proposal_id"] for x in after_p}) == 76
assert [x["case_id"] for x in before_d] == [x["case_id"] for x in after_d]
assert [x["proposal_id"] for x in before_p] == [x["proposal_id"] for x in after_p]
assert after_e[:len(before_e)] == before_e
assert len({x["evidence_id"] for x in after_e}) == len(after_e)
eids = {x["evidence_id"] for x in after_e}
pids = {x["proposal_id"] for x in after_p}
case_rows = []
cmeta = {"evidence_ids", "issue_refs", "independent_review", "successor_lineage"}
for old, new in zip(before_d, after_d):
    cid = old["case_id"]
    update = cu.get(cid, {}).get("updates", {})
    if cid in cu:
        assert cu[cid]["predecessor"]["row_sha256_canonical_json"] == rowsha(old)
        assert cu[cid]["predecessor"]["file_sha256"] == sha(OLD/"decisions.json")
    assert unchanged_scientific_core(old, new, update, cmeta), cid
    assert new["successor_lineage"]["predecessor_row_sha256"] == rowsha(old), cid
    assert new["successor_lineage"]["original_independent_review"] == old["independent_review"]
    assert new["successor_lineage"]["scientific_rationale_changed"] == (cid in cu)
    assert new["evidence_ids"][:len(old["evidence_ids"])] == old["evidence_ids"]
    assert set(old["issue_refs"]) <= set(new["issue_refs"])
    assert set(new["evidence_ids"]) <= eids and set(new["proposal_ids"]) <= pids
    assert new["independent_review"] == {"status": "pending", "evidence_ids": []}
    case_rows.append({"case_id": cid, "before_row_sha256": rowsha(old), "successor_row_sha256": rowsha(new),
                      "case_input_sha256": new["case_input_sha256"], "source_and_all_occurrences_unchanged": True,
                      "scientific_delta": sorted(update), "only_authorized_science_and_metadata_changed": True})

pmeta = {"evidence_ids", "after_capture", "successor_lineage", "successor_review_status"}
proposal_rows = []
selected = {x["proposal_id"]: x for x in selection["selected_entries"]}
assert len(selected) == 76
for old, new in zip(before_p, after_p):
    pid = old["proposal_id"]
    update = pu.get(pid, {}).get("updates", {})
    if pid in pu:
        assert pu[pid]["predecessor"]["row_sha256_canonical_json"] == rowsha(old)
        assert pu[pid]["predecessor"]["file_sha256"] == sha(OLD/"proposals.json")
    assert unchanged_scientific_core(old, new, update, pmeta), pid
    assert new["successor_lineage"]["predecessor_row_sha256"] == rowsha(old)
    assert new["successor_lineage"]["inherited_whole_owner_support"] is False
    assert new["successor_review_status"] == "pending"
    assert new["evidence_ids"][:len(old["evidence_ids"])] == old["evidence_ids"]
    assert set(new["evidence_ids"]) <= eids and set(new.get("depends_on_proposals", [])) <= pids
    cp = ART / new["after_capture"]["path"]
    assert sha(cp) == new["after_capture"]["sha256"]
    assert selected[pid]["selected_capture"] == new["after_capture"]
    assert selected[pid]["old_capture"] == old["after_capture"]
    assert selected[pid]["case_ids"] == old["case_ids"]
    assert selected[pid]["applicable_occurrence_ids"] == old.get("applicable_occurrence_ids", [])
    assert selected[pid]["inherited_whole_owner_support"] is False
    proposal_rows.append({"proposal_id": pid, "before_row_sha256": rowsha(old), "successor_row_sha256": rowsha(new),
                          "selected_payload_sha256": sha(cp), "relation": selected[pid]["relation"],
                          "scope": selected[pid]["change_scope"], "original_identity_case_occurrence_dependencies_retained": True})
for x in selection["case_bindings"]:
    row = next(r for r in after_d if r["case_id"] == x["case_id"])
    assert all(row[k] == v for k, v in x.items())
for name, cap in selection["core_paths"].items():
    assert sha(ART/cap["path"]) == cap["sha256"] == pins[name+".json"]
assert selection["scientific_owner_role_export_approval"] is False
assert selection["coordinator_37_composed_candidates_changed"] is False

# In-memory counterexamples exercise the independent whole-object boundary.
sample_old, sample_new = before_d[0], after_d[0]
controls = []
for field, value in [("case_input_sha256", "0"*64), ("source", {"raw_source_label": "invented"}), ("occurrence_ids", [])]:
    altered = copy.deepcopy(sample_new)
    altered[field] = value
    rejected = not unchanged_scientific_core(sample_old, altered, {}, cmeta)
    assert rejected
    controls.append({"mutation": field, "in_memory_only": True, "rejected": rejected})
counts = {"source_cases": len(after_d), "unique_occurrence_ids": len({y for x in after_d for y in x["occurrence_ids"]}),
          "proposals": len(after_p), "original_evidence_unchanged": len(before_e), "new_evidence_entries": len(after_e)-len(before_e),
          "scientific_case_deltas": len(cu), "scientific_proposal_deltas": len(pu)}
out = {"reviewer": "/root/skeptical_review", "at": datetime.datetime.now(datetime.timezone.utc).isoformat(),
       "result": "PASS", "exact_pre_review_core_hashes": pins, "counts": counts, "case_rows": case_rows,
       "proposal_rows": proposal_rows, "negative_controls": controls,
       "case110_limit": "The retained new_distinct_ingredient_proposal category is explicitly historical workflow metadata; current reasoning/missing_requirement and proposal integration obligations withhold merging or proved-distinct co-installation. No identity approval is inferred from the enum.",
       "scope": "Full188-case and76-proposal retention/bridge review, no sampling. Scientific reevaluation is exactlyfive cases linked tofour payloads. Other source outcomes are preserved, not scientifically renewed.",
       "scientific_approval": False, "release_approval": False,
       "script": {"path": str(Path(__file__).resolve()), "sha256": sha(Path(__file__).resolve())}}
q = HERE / "pre-review-core-independent-v2.json"
with q.open("x") as f:
    json.dump(out, f, indent=2, ensure_ascii=False); f.write("\n")
print(json.dumps({"path": str(q), "sha256": sha(q), "result": "PASS", "counts": counts}, indent=2))
