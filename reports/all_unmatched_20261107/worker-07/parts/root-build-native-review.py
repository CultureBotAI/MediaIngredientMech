"""Author a scoped native owner observation from inspected final campaign inputs.

The source-only cases remain in the campaign contract. This is a bounded owner
comparison, not whole-record scientific approval or a publication selector.
"""
import argparse
import datetime
import hashlib
import json
from pathlib import Path

import yaml

OUT = Path("reports/all_unmatched_20261107/worker-07")


class NoAliasDumper(yaml.SafeDumper):
    def ignore_aliases(self, data):
        return True


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def utc(value):
    return datetime.datetime.fromisoformat(value.replace("Z", "+00:00")).astimezone(datetime.timezone.utc).isoformat().replace("+00:00", "Z")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--inspection", default="logs/root-owner-inspect-final.json")
    parser.add_argument("--predecessor")
    args = parser.parse_args()
    inspected = json.loads((OUT / args.inspection).read_text())
    decisions = json.loads((OUT / "parts/root-native-input-decisions.json").read_text())["decisions"]
    sources = json.loads((OUT / "parts/root-native-input-evidence.json").read_text())["evidence"]
    proposals = json.loads((OUT / "parts/root-native-input-proposals.json").read_text())["proposals"]
    now = datetime.datetime.now(datetime.timezone.utc)
    timestamp = now.isoformat().replace("+00:00", "Z")
    targets = inspected["targets"]
    tids = [t["target_id"] for t in targets]
    evidence = [{"evidence_id": "campaign-evidence", "kind": "prior_review", "reference": str(OUT / "parts/root-native-input-evidence.json"), "locator": "Hash-bound primary, source snapshot, unsuccessful pursuit and separate skeptical-review evidence entries", "accessed_at": timestamp, "support": "context_only", "summary": "Frozen final campaign evidence catalog. Per-case applicability remains in the paired decision snapshot; shared captures do not grant owner-wide approval.", "snapshot_sha256": sha(OUT / "parts/root-native-input-evidence.json")}]
    for i, decision in enumerate(decisions):
        if decision["owner_records"]:
            evidence.append({"evidence_id": f"case-{i:03}", "kind": "prior_review", "reference": str(OUT / "parts/root-native-input-decisions.json"), "locator": f"decisions[{i}] case_id={decision['case_id']}", "accessed_at": timestamp, "support": "partial", "summary": decision["reasoning"] + " Scope: " + decision["applicability"], "snapshot_sha256": sha(OUT / "parts/root-native-input-decisions.json")})
    proof_ids = []
    wanted = ("61278", "66870", "232798", "31345", "3374", "52891", "91261")
    for index, item in enumerate(sources):
        if item["kind"] == "ontology" and any(term in (item.get("url") or "") for term in wanted):
            eid = f"authority-{index:04}"
            evidence.append({"evidence_id": eid, "kind": "authority", "reference": item["url"], "locator": item["locator"] + "; exact local capture " + item["capture"]["path"], "accessed_at": utc(item["accessed_at"]), "support": "refutes", "summary": item["supports_or_contradicts"], "snapshot_sha256": item["capture"]["sha256"]})
            proof_ids.append(eid)
    checks = []
    check_specs = [
        ("owner-schema", "Strict closed schema for selected current owners", "logs/final-owner-schema-command.json", "logs/final-owner-schema.log"),
        ("proposal-schema-partonomy", "Isolated proposal schema, identifiers, history and full catalogue partonomy", "logs/final-proposal-validation-command.json", "logs/final-proposal-validation.json"),
        ("campaign-structure", "Whole-shard contract integrity before native attachment", "logs/structural-audit-reviewed-command.json", "structural-audit-reviewed.json"),
    ]
    for key, name, command_path, log_path in check_specs:
        command = json.loads((OUT / command_path).read_text())
        assert command["returncode"] == 0
        eid = "check-" + key
        evidence.append({"evidence_id": eid, "kind": "validation", "reference": str(OUT / log_path), "accessed_at": timestamp, "support": "supports", "summary": name + "; no scientific or release approval follows from structural validation.", "snapshot_sha256": sha(OUT / log_path)})
        checks.append({"check_id": key, "name": name, "status": "passed", "required": True, "summary": name + " passed on pinned inputs.", "target_ids": tids, "command": command["command"], "exit_code": 0, "expected_exit_code": 0, "evidence_ids": [eid]})
    checks.append({"check_id": "native-export-gates", "name": "Generated export and publication gates", "status": "not_applicable", "required": False, "summary": "This branch proposes isolated payloads only. User forbids downstream rebuilds and maintained data edits; coordinator must apply guarded writes, synchronize and run native export/publication gates after integration.", "target_ids": tids})
    assessments = []
    defects = {
        "data/ingredients/mapped/Sodium_Dithionite.yaml": ("dithionite-foreign-scutellarin-aliases", "Scutellarin aliases resolve a chemically different sodium dithionite owner", "Six active scutellarin-derived aliases contradict CHEBI:61278 versus CHEBI:66870. The isolated proposal rejects the six strings while preserving their provenance and adds only the independently supported source alias.", "https://github.com/CultureBotAI/MediaIngredientMech/issues/1169"),
        "data/ingredients/mapped/Na-l-lactate.yaml": ("l-lactate-dl-synonym-conflict", "Racemic sodium lactate alias resolves an L-specific owner", "The active Sodium D,L-Lactate synonym conflicts with this L-specific CHEBI:232798 owner. The proposed rejection and explicit L source spelling do not authorize racemic or unknown-stereo source cases.", "https://github.com/CultureBotAI/MediaIngredientMech/issues/1170"),
        "data/ingredients/mapped/Calcium_Pantothenate.yaml": ("calcium-pantothenate-capsaicin-aliases", "Capsaicin names contaminate the calcium pantothenate owner", "Four vanillylamide, capsaicin and Zostrix strings belong to CHEBI:3374, not CHEBI:31345. Their rejection does not settle all D versus DL source cases or inherited supplier assertions.", "https://github.com/CultureBotAI/MediaIngredientMech/issues/1157"),
        "data/ingredients/mapped/L-Cysteine_X_HCl_X_H2O_Solution.yaml": ("cysteine-stock-qsy9-alias", "QSY9 dye and preparation instruction are resolving stock synonyms", "CHEBI:52891 denotes QSY9 succinimidyl ester, a different substance. Reject the dye string and preparation instruction while keeping the solution separate from pure cysteine hydrochloride and retaining unresolved concentration/form relations.", "https://github.com/CultureBotAI/MediaIngredientMech/issues/702"),
        "data/ingredients/mapped/Sodium_Malate.yaml": ("s-malate-racemate-synonyms", "Five racemic malate aliases resolve an S-specific disodium owner", "Current CHEBI:91261 is disodium (S)-malate. Five active DL/racemate synonyms conflict with that stereospecific identity: DL-Na-malate, Na-DL-malate, Na2-DL-malate, Sodium DL-malate and DL-Sodium malate. The isolated proposal rejects those five strings while preserving provenance. Remaining source uncertainty about sodium stoichiometry and hydration is separate and does not negate this confirmed owner defect.", "https://github.com/CultureBotAI/MediaIngredientMech/issues/811"),
    }
    for index, target in enumerate(targets):
        path = target["path"]
        related = [(i, d) for i, d in enumerate(decisions) if any(o["path"] == path for o in d["owner_records"])]
        eid = f"owner-{index:03}"
        record = yaml.safe_load(Path(path).read_text())
        evidence.append({"evidence_id": eid, "kind": "record_content", "reference": path, "locator": target["selector"], "accessed_at": timestamp, "support": "context_only", "summary": f"Read maintained owner identity {record['identifier']}, mapping, supplied form, synonyms and source notes as a comparison for assigned cases; roles and other claims excluded.", "snapshot_sha256": sha(Path(path))})
        outcome = "concern" if path in defects else "unknown" if any(d["disposition"] == "unresolved" for _, d in related) else "supported"
        changes = [p["proposal_id"] for p in proposals if p["owner_path"] == path]
        assessments.append({"assessment_id": f"owner-assessment-{index:03}", "area": "identity", "topic": "Assigned source-label, supplied-form and synonym comparison", "outcome": outcome, "summary": f"Compared {record['preferred_term']} ({record['identifier']}) to {len(related)} assigned source cases. " + ("Bounded isolated owner changes proposed: " + ", ".join(changes) + ". " if changes else "No owner-byte change is proposed by these cases. ") + "Support is limited to the explicit case relation or contrast; no complete owner approval.", "target_ids": [path], "evidence_ids": [eid, "campaign-evidence"] + [f"case-{i:03}" for i, _ in related], "details": "\n\n".join(d["source"]["source_case_id"] + ": " + d["reasoning"] + " Remaining requirement: " + str(d["missing_requirement"]) for _, d in related), "dimensions": [{"name": "claim_scope", "value": "source identity/form/alias only", "definition": "No roles, unrelated source identities, full chemical properties or content-bound publication support approved.", "evidence_ids": [eid, "campaign-evidence"]}]})
    findings, actions = [], []
    for index, (path, (key, title, detail, issue)) in enumerate(defects.items()):
        assert path in tids
        case_ids = [f"case-{i:03}" for i, d in enumerate(decisions) if any(o["path"] == path for o in d["owner_records"])]
        fid = f"F{index+1}"
        findings.append({"finding_id": fid, "issue_key": key, "category": "identity", "severity": "blocker", "status": "open", "certainty": "confirmed", "title": title, "description": detail, "target_ids": [path], "field_paths": ["synonyms"], "evidence_ids": case_ids + proof_ids, "rule_id": "MAPPING_SEMANTICS source identity and resolving synonym invariants", "native_severity": "P1", "normalization_reason": "Resolving foreign-substance or stereochemically incompatible names can denote the wrong substance; P1 maps to blocker within this bounded claim scope.", "owner_paths": target_owner(path), "external_issues": [issue]})
        if args.predecessor and index < 4:
            findings[-1]["previous_occurrences"] = [{"repository": "CultureBotAI/MediaIngredientMech", "review_id": args.predecessor, "finding_id": fid}]
        actions.append({"action_id": f"A{index+1}", "description": "Reconcile the exact isolated synonym proposal against other shards and the original owner hash, then apply through native guarded integration.", "finding_ids": [fid], "target_ids": [path], "owner_paths": target_owner(path), "acceptance_checks": ["Foreign strings retained only as non-resolving provenance; unrelated claims remain withheld.", "Withdraw old content-bound support after any owner-byte change; synchronize individual/aggregate/SSSOM and validate new complete published payload.", "Compare cross-shard dependencies and existing duplicate owners; no automatic merge or release from this review."]})
    review = {"schema_version": "1.0.0", "review_id": now.strftime("%Y%m%dT%H%M%SZ") + "-worker07-source-owner-comparison", "kind": "batch", "repository": "CultureBotAI/MediaIngredientMech", "title": "Worker07 assigned source-to-owner identity and synonym comparison", "started_at": "2026-11-08T05:06:41.928427Z", "finished_at": timestamp,
              "reviewer": {"identity": "/root, worker07 source-review campaign", "kind": "agent", "independence": "self_review", "independence_basis": "Root authors the compilation and integration proposals. Independent source-case reviews by primary_c of A70, primary_a of B70 and primary_b of C48, plus integration_reviewer of root deltas, are separate hash-bound artifacts. This native wrapper is not falsely labelled an independent whole-owner review."},
              "skill": ".claude/skills/review-ingredients/SKILL.md", "completion": "completed", "verdict": "needs_curation", "scientific_review": True,
              "summary": f"Bounded comparison of {len(targets)} actual maintained owners referenced by the 188 assigned source decisions. {len(defects)} confirmed resolving-synonym defects remain open in maintained bytes; exact isolated proposals and source-specific unresolved requirements are preserved. All source-only cases stay in the campaign contract without invented native owners.",
              "source": inspected["source"], "scope": {"description": "Existing owner identity, supplied form and relevant resolving synonyms compared only to assigned source contexts; not full ingredient-record review.", "selection": "Every actual existing owner named in final worker07 owner_records; target paths resolved and inspected before assessment. Proposed new owners are not maintained targets.", "coverage": "full", "population_size": len(targets), "reviewed_target_ids": tids, "exclusions": [{"target": "Source-only cases and proposed new owners", "reason": "No maintained owner exists to review; full source-case and isolated-payload assessment is in the campaign outcomes."}, {"target": "Roles, unrelated synonyms, properties, native selector and export approval", "reason": "Outside this bounded identity comparison; all existing source-specific holds remain effective."}]},
              "targets": targets, "checks": checks, "evidence": evidence, "assessments": assessments, "findings": findings, "actions": actions,
              "limitations": ["Completion means completion of this declared comparison scope, not resolution of every source identity or approval of all owner assertions.", "Native current owners remain unchanged; proposed new records and baseline-relative edits are isolated artifact bytes.", "Live primary sources can differ from frozen source snapshots; differing recipe contexts are retained explicitly, never substituted silently.", "Required downstream integration, synchronizations and publication gates belong to the coordinator and were not executed in this worker."], "links": [str(OUT / "decisions.json"), str(OUT / "proposals.json"), str(OUT / "subagent-scopes.json")], "tags": ["worker07", "source-review", "bounded-owner-comparison"]}
    if args.predecessor:
        review["related_reviews"] = [{"repository": "CultureBotAI/MediaIngredientMech", "review_id": args.predecessor, "relationship": "Successor observation preserves all 77 targets and four prior open findings, and adds the previously omitted fifth malate-synonym finding; no prior artifact or maintained source was rewritten."}]
        review["notes"] = ["The earlier native wrapper omitted a confirmed malate synonym defect already represented in the unchanged source decisions and proposal. Independent integration review identified the inventory omission. This successor fixes the native finding inventory; it does not alter or newly approve the source-case/proposal science."]
    destination = OUT / "parts/root-native-review-input.yaml"
    destination.write_text(yaml.dump(review, Dumper=NoAliasDumper, sort_keys=False, allow_unicode=True, width=100))
    print(json.dumps({"review_id": review["review_id"], "target_count": len(targets), "findings": len(findings), "path": str(destination)}))


def target_owner(path):
    return [{"repository": "CultureBotAI/MediaIngredientMech", "path": path, "role": "maintained ingredient owner; synchronize aggregate and mappings after guarded integration"}]


if __name__ == "__main__":
    main()
