"""Author only the sealed W01 #1226 typing lane; never write maintained files."""
from __future__ import annotations

import copy
import hashlib
import importlib.util
import json
import re
import subprocess
import sys
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path

import yaml

W = Path.cwd().resolve()
C = W.parents[2]
D = W / "reports/all_unmatched_20261107/worker-01/successor-1226-1237-v1"
T = D / "typing"
PACKET = C / "preflight/w01-w09-author-task-planning-v1"
I = C / "preflight/final-intake-candidate-v1"
HEAD = "26445f23b5a905ac26d864acfbd658570c88769c"
sys.path.insert(0, str(W / "src"))
from mediaingredientmech.curate.curation_event import record_curation_event
from mediaingredientmech.curate.publication_guard import FrozenFile, no_alias
from mediaingredientmech.ingredient_bundle_refresh import publish_new_files
from mediaingredientmech.synonym_policy import is_resolving_synonym
from mediaingredientmech.validation.component_partonomy import validate_component_partonomy
from mediaingredientmech.validation.write_validated import validate_ingredient, write_validated_ingredient


def sha(data):
    return hashlib.sha256(data).hexdigest()


def canonical(value):
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False, allow_nan=False).encode()


def digest(value):
    return sha(canonical(value))


def bind(path):
    path = Path(path).absolute()
    return {"path": str(path), "sha256": sha(path.read_bytes())}


def save(name, value):
    with (T / name).open("x", encoding="utf-8") as out:
        json.dump(value, out, indent=2, ensure_ascii=False)
        out.write("\n")


frozen = {}


def capture(path, expected=None):
    path = Path(path).absolute()
    if path not in frozen:
        frozen[path] = FrozenFile.capture(path)
    f = frozen[path]
    if expected is not None:
        assert sha(f.content) == expected, (str(path), "input hash mismatch")
    return f.content


def load(path, expected=None):
    return json.loads(capture(path, expected))


def git(*args):
    return subprocess.check_output(["git", *args], cwd=W, text=True).strip()


def verify_inputs():
    assert git("rev-parse", "HEAD") == HEAD
    for f in frozen.values():
        f.verify()


def evidence_index(row):
    m = re.fullmatch(r"ontology_mapping\.evidence\[(\d+)\]", row["field"])
    assert m, "Only exact ordinary MappingEvidence selectors are allowed"
    return int(m.group(1))


def check_rows(rows, expected):
    assert canonical(rows) == canonical(expected), "Closed allowlist differs"
    assert len({r["field"] for r in rows}) == len(rows), "Repeated selector"
    for r in rows:
        assert not r["also_science_scope"] and r["proposed_typing_only"]
        assert r["classification"] == "new_agent_record"
        assert r["suggested_native_type"] == "LLM_SUGGESTION"
        assert r["full_value"]["evidence_type"] == "MANUAL_CURATION"
        assert digest(r["full_value"]) == r["full_value_sha256"]
        evidence_index(r)


def check_before(record, rows):
    for r in rows:
        actual = record["ontology_mapping"]["evidence"][evidence_index(r)]
        assert actual == r["full_value"], "Stale complete evidence object"
        assert digest(actual) == r["full_value_sha256"]


def check_delta(before, after, rows):
    restored = copy.deepcopy(after)
    old_history = before.get("curation_history", [])
    history = restored.get("curation_history", [])
    assert len(history) == len(old_history) + 1, "Exactly one new history event required"
    assert history[:-1] == old_history, "Prior history prefix changed"
    event = history.pop()
    assert event["curator"] == "Codex /root/issue_context (worker01)"
    assert event["llm_assisted"] is True and event["action"] == "CORRECTED"
    assert "#1226" in event["changes"]
    if "curation_history" not in before:
        del restored["curation_history"]
    for r in rows:
        obj = restored["ontology_mapping"]["evidence"][evidence_index(r)]
        assert obj == {**r["full_value"], "evidence_type": "LLM_SUGGESTION"}
        obj["evidence_type"] = "MANUAL_CURATION"
    assert restored == before, "Unlisted semantic change (includes components and inherited evidence)"
    return event


def expect_refusal(name, callback):
    try:
        callback()
    except (AssertionError, ValueError, FileExistsError) as e:
        return {"control": name, "rejected": True, "exception_type": type(e).__name__, "message": str(e)}
    raise AssertionError("Negative control unexpectedly passed: " + name)


def main():
    T.mkdir(exist_ok=True)
    staged = T / "validated-staging-v1"
    staged.mkdir(exist_ok=False)
    (D / "payloads").mkdir(exist_ok=True)
    no_alias(D)
    assert git("rev-parse", "HEAD") == HEAD
    tracked_status = git("status", "--short", "--untracked-files=no")
    assert not tracked_status
    manifest = load(D / "inputs/MANIFEST.json", "2c1545756990cdd5c109e82acdb8d206f304a4587cb6ec3d60cf5cabd49afb52")
    for member in manifest["files"]:
        capture(PACKET / member["path"], member["sha256"])
    assert len(manifest["files"]) == 135
    preflight = load(D / "checks/preflight-v1.json")
    for item in preflight["input_copies"]:
        capture(D / item["path"], item["sha256"])
    allow = load(D / "inputs/w01-full-provenance-allowlist-v2.json", "49e57ca367db15a15e38c0d2f7139a6e05994e64fe1fb6ce7dee7991244ed91e")
    assert allow["source_head"] == HEAD
    selected = [r for r in allow["rows"] if not r["also_science_scope"]]
    assert len(selected) == 71 and len({r["proposal_id"] for r in selected}) == 62
    by_id = defaultdict(list)
    for row in selected:
        by_id[row["proposal_id"]].append(row)
    worker = load(D / "inputs/current-worker-bindings.json")["workers"][0]
    assert worker["head"] == HEAD
    for item in [*worker["core"].values(), *worker["all_selected_payloads"]]:
        data = capture(item["path"], item["sha256"])
        rel = Path(item["path"]).relative_to(W).as_posix()
        assert sha(subprocess.check_output(["git", "show", HEAD + ":" + rel], cwd=W)) == sha(data)
    props = {p["proposal_id"]: p for p in load(worker["core"]["proposals.json"]["path"])["proposals"]}
    decisions = load(worker["core"]["decisions.json"]["path"])["decisions"]
    cases = {c["case_id"]: c for c in decisions}
    assert len(cases) == len(decisions) == 188 and len(props) == 76
    bundle = next(b for b in load(I / "active-bundles-frozen-v1.json")["bundles"] if b["worker_slot"] == 1)
    roots = {"artifact": Path(bundle["artifact_root"]), "source": Path(bundle["source_root"]), "mim": Path(bundle["mim_root"])}
    native_paths = ["src/mediaingredientmech/validation/write_validated.py", "src/mediaingredientmech/curate/curation_event.py", "src/mediaingredientmech/curate/publication_guard.py", "src/mediaingredientmech/ingredient_bundle_refresh.py", "src/mediaingredientmech/schema/mediaingredientmech.yaml", "src/mediaingredientmech/validation/component_partonomy.py", "src/mediaingredientmech/synonym_policy.py", "MAPPING_SEMANTICS.md"]
    for n in native_paths:
        capture(W / n)
    producer = C.parent / "kgm-unmapped-20261107/claw/scripts/build_mim_ingredient_sssom.py"
    capture(producer)
    spec = importlib.util.spec_from_file_location("typing_native_producer", producer)
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    records, candidates, receipts, projections, before_bindings = {}, {}, [], [], []
    for pid, rows in by_id.items():
        check_rows(rows, by_id[pid])
        row = rows[0]
        before = yaml.safe_load(capture(row["current_payload_path"], row["payload_sha256"]))
        assert before == row["origin"]["record"]
        check_before(before, rows)
        proposal = props[pid]
        assert proposal["after_capture"]["sha256"] == row["payload_sha256"]
        assert proposal["before_sha256"] == row["origin"]["before_sha256"]
        assert set(proposal["case_ids"]) == set(row["origin"]["case_ids"])
        case_bindings = []
        for b in row["origin"]["case_bindings"]:
            case = cases[b["case_id"]]
            assert b["input_sha256"] == case["case_input_sha256"]
            assert set(b["occurrence_ids"]) == set(case["occurrence_ids"])
            case_bindings.append({"original_binding": b, "complete_unchanged_decision": case, "decision_semantic_sha256": digest(case)})
        capture_bindings = []
        for ev in row["origin"]["evidence"]:
            cap = ev.get("capture")
            if cap:
                source = roots[cap["root"]] / cap["path"]
                capture(source, cap["sha256"])
                capture_bindings.append({"evidence": ev, "verified_capture": bind(source)})
        owner_before = None
        if row["baseline_path"]:
            raw = capture(row["baseline_path"], row["baseline_sha256"])
            owner_before = bind(row["baseline_path"])
            assert row["baseline_sha256"] == proposal["before_sha256"]
            baseline = yaml.safe_load(raw)
            for r in rows:
                assert r["full_value"] not in baseline.get("ontology_mapping", {}).get("evidence", [])
            before_bindings.append({"proposal_id": pid, "authentic_owner_before": owner_before})
        after = copy.deepcopy(before)
        for r in rows:
            after["ontology_mapping"]["evidence"][evidence_index(r)]["evidence_type"] = "LLM_SUGGESTION"
        fields = ", ".join(r["field"] for r in rows)
        event = record_curation_event(after, curator="Codex /root/issue_context (worker01)", action="CORRECTED", changes=f"#1226 authorized provenance-only successor: change {fields} from MANUAL_CURATION to LLM_SUGGESTION because these exact new-agent MappingEvidence judgments were LLM-authored. Preserve all evidence sources, citations, notes, scientific assertions, component evidence, aliases, case applicability, status and prior history. Isolated proposal only; no maintained integration or new scientific approval.", previous_status=before.get("mapping_status"), new_status=before.get("mapping_status"), llm_assisted=True, llm_model="gpt-6")
        check_delta(before, after, rows)
        path = staged / (pid + ".yaml")
        assert not path.exists()
        write_validated_ingredient(after, path)
        reread = yaml.safe_load(path.read_bytes())
        assert reread == after and not validate_ingredient(reread)
        check_delta(before, reread, rows)
        records[pid], candidates[pid] = before, reread
        old_alias = [is_resolving_synonym(s) for s in before.get("synonyms", [])]
        assert old_alias == [is_resolving_synonym(s) for s in after.get("synonyms", [])]
        args = (Path(row["owner_path"]).name, {}, {}, {}, {})
        old_sssom = module._row_from_yaml(Path(args[0]), *args[1:], record=before, owners={})
        new_sssom = module._row_from_yaml(Path(args[0]), *args[1:], record=after, owners={})
        def scientific_rows(rs):
            return [{k: v for k, v in r.items() if k not in {"source", "mapping_date", "mapping_justification"}} for r in rs]
        assert scientific_rows(old_sssom) == scientific_rows(new_sssom)
        projections.append({"proposal_id": pid, "resolver_flags": old_alias, "before_sssom": old_sssom, "after_sssom": new_sssom, "scientific_projection_equal": True, "projection_limits": "Actual native in-memory producer with empty ancillary maps; attribution/date/justification may reflect the honest new history. No canonical output or release approval."})
        receipts.append({"proposal_id": pid, "entry_id": row["entry_id"], "source_head": HEAD, "source_kind": row["proposal_kind"], "owner_path": row["owner_path"], "predecessor": bind(row["current_payload_path"]), "authentic_owner_before": owner_before, "original_proposal": proposal, "after": {"path": str(D / "payloads" / (pid + ".yaml")), "sha256": sha(path.read_bytes())}, "staged": bind(path), "source_case_bindings": case_bindings, "original_evidence_captures": capture_bindings, "changes": [{"audit_row_id": r["audit_row_id"], "selector": r["field"], "before_full_value": r["full_value"], "after_full_value": {**r["full_value"], "evidence_type": "LLM_SUGGESTION"}, "before_sha256": r["full_value_sha256"], "after_sha256": digest({**r["full_value"], "evidence_type": "LLM_SUGGESTION"})} for r in rows], "new_history_event": event, "old_history_prefix_sha256": digest(before.get("curation_history", [])), "old_history_prefix_length": len(before.get("curation_history", [])), "before_semantic_sha256": digest(before), "after_restored_semantic_sha256": digest(before), "proof": "Reverting only the 1/2 listed evidence_type fields and removing exactly one appended event reproduces the entire predecessor object exactly. Every other original field, component enum, source, citation, note, quantity, alias and old event is unchanged.", "independent_review": "pending exact successor bytes; predecessor approval does not transfer"})
    assert len(before_bindings) == 8
    # Focused negative controls use real predecessor/successor objects and the same author gate.
    pid = next(iter(by_id)); rows = by_id[pid]; before = records[pid]; after = candidates[pid]
    negatives = [expect_refusal("omitted allowlist row", lambda: check_rows([], rows))]
    badrows = copy.deepcopy(rows); badrows[0]["field"] = "component_assertion.evidence[0]"
    negatives.append(expect_refusal("component selector cannot enter the closed ordinary-evidence allowlist", lambda: check_rows(badrows, rows)))
    stale = copy.deepcopy(before); stale["ontology_mapping"]["evidence"][0]["notes"] += " stale"
    negatives.append(expect_refusal("stale complete evidence object", lambda: check_before(stale, rows)))
    bad = copy.deepcopy(after); bad["curation_history"][0]["changes"] += " changed"
    negatives.append(expect_refusal("prior history mutation", lambda: check_delta(before, bad, rows)))
    bad = copy.deepcopy(after); bad["component_assertion"]["evidence"][0]["evidence_type"] = "MANUAL_CURATION"
    negatives.append(expect_refusal("unlisted component evidence enum mutation", lambda: check_delta(before, bad, rows)))
    bad = copy.deepcopy(after); bad["ontology_mapping"]["evidence"].append({"evidence_type": "LLM_SUGGESTION", "source": "unlisted inherited assertion"})
    negatives.append(expect_refusal("unlisted ordinary evidence addition", lambda: check_delta(before, bad, rows)))
    unknown = copy.deepcopy(after); unknown["not_a_schema_field"] = "reject"
    errors = validate_ingredient(unknown); assert errors
    negatives.append({"control": "closed native schema rejects unknown field", "rejected": True, "errors": [e.message for e in errors]})
    control = T / "negative-controls-v1"; control.mkdir(exist_ok=False)
    changed = control / "stale-input.txt"; changed.write_text("before\n")
    held = FrozenFile.capture(changed); changed.write_text("after\n")
    negatives.append(expect_refusal("native stale FrozenFile input", held.verify))
    occupied = control / "occupied-output.txt"; occupied.write_text("preserved\n")
    negatives.append(expect_refusal("native exclusive output collision", lambda: publish_new_files([(occupied, b"forbidden\n")], lambda: None)))
    assert occupied.read_bytes() == b"preserved\n"
    # Full authentic maintained catalog plus all 76 predecessor proposals; replace only this lane's 62.
    baseline = {}
    for path in sorted((W / "data/ingredients").rglob("*.yaml")):
        baseline[path.relative_to(W).as_posix()] = yaml.safe_load(capture(path))
    old_catalog = copy.deepcopy(baseline); new_catalog = copy.deepcopy(baseline)
    for pid, prop in props.items():
        path = W / "reports/all_unmatched_20261107/worker-01" / prop["after_capture"]["path"]
        rec = yaml.safe_load(capture(path, prop["after_capture"]["sha256"]))
        old_catalog[prop["owner_path"]] = rec
        new_catalog[prop["owner_path"]] = candidates.get(pid, rec)
    old_errors = [str(x) for x in validate_component_partonomy(old_catalog.values())]
    new_errors = [str(x) for x in validate_component_partonomy(new_catalog.values())]
    assert old_errors == new_errors, "Typing changes must not change native partonomy"
    verify_inputs()
    outputs = [(D / "payloads" / (pid + ".yaml"), (staged / (pid + ".yaml")).read_bytes()) for pid in by_id]
    publish_new_files(outputs, verify_inputs)
    verify_inputs()
    for r in receipts:
        assert sha(Path(r["after"]["path"]).read_bytes()) == r["after"]["sha256"]
    save("payload-deltas-v1.json", {"scope": "62 typing-only payloads; 71 exact MappingEvidence types and 62 appended events", "payloads": receipts})
    save("negative-controls-v1.json", {"controls": negatives, "limitations": "Private real-object/API controls; no Git fixture, maintained writes or broad suite."})
    save("native-projections-v1.json", {"producer": bind(producer), "projections": projections, "partonomy": {"overlay": "All 76 original selected proposals; after projection substitutes exactly the 62 typing-only successors. Four science candidates remain originals in this scoped check.", "maintained_count": len(baseline), "projected_count": len(old_catalog), "before_errors": old_errors, "after_errors": new_errors, "introduced_errors": [], "scientific_approval": False}})
    save("input-bindings-v1.json", {"checked_at": datetime.now(timezone.utc).isoformat(), "source_head": HEAD, "inputs": [bind(p) for p in sorted(frozen)], "authoritative_allowlist": bind(D / "inputs/w01-full-provenance-allowlist-v2.json"), "authentic_existing_owner_beforeimages": before_bindings, "maintained_before_after_equal": True, "scope": "Every captured input verified unchanged before and after exclusive publication; all maintained record bytes are included. No main/upstream freshness claim beyond separately recorded root preflight."})
    save("HANDOFF-v1.json", {"finished_at": datetime.now(timezone.utc).isoformat(), "author": "Codex /root/issue_context (worker01)", "source_head": HEAD, "assignment": bind(D / "inputs/w01-author-task-DRAFT-v2.md"), "allowlist": bind(D / "inputs/w01-full-provenance-allowlist-v2.json"), "program": bind(__file__), "native_sources": [bind(W / p) for p in native_paths], "payload_count": 62, "evidence_object_count": 71, "events_appended": 62, "authentic_beforeimage_count": 8, "closed_schema_passes": 62, "negative_controls_pass": len(negatives), "unrelated_semantic_changes": 0, "source_case_count": len({b["case_id"] for rs in by_id.values() for b in rs[0]["origin"]["case_bindings"]}), "distinct_occurrence_count": len({o for rs in by_id.values() for b in rs[0]["origin"]["case_bindings"] for o in b["occurrence_ids"]}), "receipts": [bind(T / n) for n in ["payload-deltas-v1.json", "negative-controls-v1.json", "native-projections-v1.json", "input-bindings-v1.json"]], "payloads": [{"proposal_id": r["proposal_id"], **r["after"]} for r in receipts], "remaining": "Independent exact-byte review and root assembly with four separately authored science payloads and ten unchanged originals. No inherited whole-owner approval, maintained integration, export approval, Git commit or GitHub action."})
    print(json.dumps({"handoff": bind(T / "HANDOFF-v1.json"), "payloads": len(receipts), "entries": sum(len(r["changes"]) for r in receipts), "native_partonomy_before_errors": len(old_errors), "native_partonomy_after_errors": len(new_errors), "negative_controls": len(negatives)}))


if __name__ == "__main__":
    main()
