"""Independent bounded successor-delta audit; not a scientific approval.

Reads complete predecessor/successor objects, checks the closed authority and
retained objects, and writes one exclusive receipt inside this review directory.
No candidate, maintained input, Git state, or earlier receipt is changed.
"""
import argparse
import copy
import datetime
import hashlib
import json
from pathlib import Path
import re

import yaml

HERE = Path(__file__).resolve().parent
D = HERE.parent.parent
W = D.parents[3]
OLD = W / "reports/all_unmatched_20261107/worker-01"


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def diff(a, b, loc=""):
    if type(a) is not type(b):
        return [{"field": loc, "before": a, "after": b}]
    if isinstance(a, dict):
        out = []
        for k in sorted(a.keys() | b.keys()):
            if k not in a or k not in b:
                out.append({"field": loc + "/" + k, "before_present": k in a,
                            "after_present": k in b, "before": a.get(k), "after": b.get(k)})
            else:
                out.extend(diff(a[k], b[k], loc + "/" + k))
        return out
    if isinstance(a, list):
        out = []
        for i in range(max(len(a), len(b))):
            if i >= len(a) or i >= len(b):
                out.append({"field": loc + "/" + str(i), "before_present": i < len(a),
                            "after_present": i < len(b), "before": a[i] if i < len(a) else None,
                            "after": b[i] if i < len(b) else None})
            else:
                out.extend(diff(a[i], b[i], loc + "/" + str(i)))
        return out
    return [] if a == b else [{"field": loc, "before": a, "after": b}]


def expected_typed(old, rows):
    obj = copy.deepcopy(old)
    for row in rows:
        i = int(re.fullmatch(r"ontology_mapping\.evidence\[(\d+)\]", row["field"])[1])
        assert old["ontology_mapping"]["evidence"][i] == row["full_value"], "stale complete evidence object"
        assert row["suggested_native_type"] == "LLM_SUGGESTION"
        assert row["classification"] == "new_agent_record"
        obj["ontology_mapping"]["evidence"][i]["evidence_type"] = "LLM_SUGGESTION"
    return obj


def only_typed_and_history(old, new, rows):
    exp = expected_typed(old, rows)
    actual = copy.deepcopy(new)
    history = actual.pop("curation_history", [])
    prior = exp.pop("curation_history", [])
    return actual == exp and history[:len(prior)] == prior and len(history) == len(prior) + 1


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", required=True)
    args = parser.parse_args()
    out = HERE / args.output
    assert out.parent == HERE and not out.exists(), "exclusive output in reviewer area only"
    original = json.loads((OLD / "shard/proposals.json").read_text())["proposals"]
    authority_path = D / "inputs/w01-full-provenance-allowlist-v2.json"
    authority = json.loads(authority_path.read_text())
    grouped = {}
    for row in authority["rows"]:
        grouped.setdefault(row["proposal_id"], []).append(row)
    science = {r["proposal_id"] for r in authority["rows"] if r["also_science_scope"]}
    traces, failures, old_objects, new_objects = [], [], {}, {}
    for p in original:
        pid = p["proposal_id"]
        before_path = OLD / p["after_capture"]["path"]
        after_path = D / "payloads" / (pid + ".yaml")
        assert sha(before_path) == p["after_capture"]["sha256"]
        old = yaml.safe_load(before_path.read_text())
        new = yaml.safe_load(after_path.read_text())
        old_objects[pid], new_objects[pid] = old, new
        rows = grouped.get(pid, [])
        expected = expected_typed(old, rows)
        old_history = old.get("curation_history", [])
        new_history = new.get("curation_history", [])
        prefix = new_history[:len(old_history)] == old_history
        trace = {"proposal_id": pid, "scope": "science_and_typing" if pid in science else
                 ("typing_only" if rows else "unchanged"), "before": {"path": str(before_path), "sha256": sha(before_path)},
                 "after": {"path": str(after_path), "sha256": sha(after_path)},
                 "authorized_fields": [r["field"] for r in rows], "complete_before_object_bindings": True,
                 "entire_prior_history_prefix": prefix, "history_events_added": len(new_history)-len(old_history),
                 "full_object_differences": diff(old, new)}
        if not rows:
            trace["byte_identical"] = sha(before_path) == sha(after_path)
            if not trace["byte_identical"]:
                failures.append({"proposal_id": pid, "failure": "unselected payload changed"})
        else:
            if not prefix or len(new_history) != len(old_history) + 1:
                failures.append({"proposal_id": pid, "failure": "history is not exact prefix plus one deliberate event"})
            added = new_history[-1]
            trace["appended_event"] = added
            if added.get("llm_assisted") is not True or not added.get("curator"):
                failures.append({"proposal_id": pid, "failure": "missing actual author/LLM assistance"})
            for row in rows:
                i = int(re.fullmatch(r"ontology_mapping\.evidence\[(\d+)\]", row["field"])[1])
                if new["ontology_mapping"]["evidence"][i]["evidence_type"] != "LLM_SUGGESTION":
                    failures.append({"proposal_id": pid, "failure": "authorized field not corrected", "field": row["field"]})
            if pid not in science:
                ok = only_typed_and_history(old, new, rows)
                trace["whole_scientific_object_and_other_evidence_unchanged"] = ok
                if not ok:
                    failures.append({"proposal_id": pid, "failure": "typing-only unauthorized full-object difference"})
            else:
                baseline = copy.deepcopy(expected)
                baseline["curation_history"] = copy.deepcopy(new_history)
                trace["science_delta_requiring_manual_review"] = diff(baseline, new)
                # These invariants are explicitly outside all four science deltas.
                for key in ["identifier", "preferred_term", "components", "mapping_status", "ingredient_type", "solution_type"]:
                    if old.get(key) != new.get(key):
                        failures.append({"proposal_id": pid, "failure": "protected science object changed", "field": key})
        traces.append(trace)
    controls = []
    sample = next(pid for pid in grouped if pid not in science)
    old, new, rows = old_objects[sample], new_objects[sample], grouped[sample]
    mutations = {}
    q = copy.deepcopy(new); q["ontology_mapping"]["evidence"][0]["notes"] += " invented"; mutations["changed_claim_notes"] = q
    q = copy.deepcopy(new); q["preferred_term"] += " invented"; mutations["changed_identity_label"] = q
    q = copy.deepcopy(new); q["ontology_mapping"]["evidence"].append({"evidence_type": "LLM_SUGGESTION", "source": "invented"}); mutations["unlisted_new_evidence"] = q
    q = copy.deepcopy(new); q["curation_history"][0]["curator"] = "invented human"; mutations["rewritten_history"] = q
    q = copy.deepcopy(new); q["component_assertion"]["evidence"][0]["evidence_type"] = "MANUAL_CURATION"; mutations["component_enum_edit"] = q
    for name, mutated in mutations.items():
        rejected = not only_typed_and_history(old, mutated, rows)
        controls.append({"name": name, "fixture": sample, "in_memory_only": True, "rejected": rejected})
        if not rejected:
            failures.append({"failure": "negative control accepted", "name": name})
    stale_rows = copy.deepcopy(rows); stale_rows[0]["full_value"]["notes"] += " stale"
    try:
        expected_typed(old, stale_rows)
        stale_rejected = False
    except AssertionError:
        stale_rejected = True
    controls.append({"name": "stale_complete_authority_object", "fixture": sample, "in_memory_only": True, "rejected": stale_rejected})
    if not stale_rejected:
        failures.append({"failure": "stale object accepted"})
    counts = {"selected": len(traces), "changed": sum(t["before"]["sha256"] != t["after"]["sha256"] for t in traces),
              "science_and_typing": sum(t["scope"] == "science_and_typing" for t in traces),
              "typing_only": sum(t["scope"] == "typing_only" for t in traces), "unchanged": sum(t["scope"] == "unchanged" for t in traces),
              "authorized_evidence_entries": len(authority["rows"])}
    if counts != {"selected": 76, "changed": 66, "science_and_typing": 4, "typing_only": 62, "unchanged": 10, "authorized_evidence_entries": 76}:
        failures.append({"failure": "closed cohort counts differ", "actual": counts})
    receipt = {"reviewer": "/root/skeptical_review", "at": datetime.datetime.now(datetime.timezone.utc).isoformat(),
               "result": "PASS" if not failures else "FAIL", "counts": counts, "authority": {"path": str(authority_path), "sha256": sha(authority_path)},
               "script": {"path": str(Path(__file__).resolve()), "sha256": sha(Path(__file__).resolve())},
               "proposals": traces, "negative_controls": controls, "failures": failures,
               "limits": ["Complete parsed-object comparison and closed provenance audit, not source truth renewal of62 typing-only candidates.",
                          "Four scientific deltas are itemized for separate independent primary-source/manual review; this receipt alone does not approve them.",
                          "Native schema/partonomy/projection and complete188-case/76-proposal ledger review are separate required evidence."],
               "scientific_approval": False, "release_approval": False}
    with out.open("x") as f:
        json.dump(receipt, f, indent=2, ensure_ascii=False); f.write("\n")
    print(json.dumps({"path": str(out), "sha256": sha(out), "result": receipt["result"], "counts": counts, "failures": failures}, indent=2))
    return bool(failures)


if __name__ == "__main__":
    raise SystemExit(main())
