"""Independent read-only worker07 integration inspection, 2026-11-08.

Inputs: frozen shard, author bundles, final bundles, and current Git index.
Output: a new explicitly named capture; this script does not approve science.
"""
import argparse
import hashlib
import json
import subprocess
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path


ROOT = Path.cwd()
ARTIFACT = ROOT / "reports/all_unmatched_20261107/worker-07"
SOURCE = Path("/Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech/.temp/all-unmatched-20261107/queue/preliminary-v5")
BASE = "e000d66dd26ab053e9b17ce7bf8d3c873c3dde99"


def digest(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False, allow_nan=False).encode()).hexdigest()


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def read(path):
    return json.loads(path.read_text())


def git(*args):
    return subprocess.check_output(["git", *args], cwd=ROOT)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", required=True)
    args = parser.parse_args()
    output = ARTIFACT / args.output
    assert output.parent == ARTIFACT / "captures" and output.name.startswith("integration-") and not output.exists()
    original = read(SOURCE / "shards/shard-07.json")["cases"]
    decisions = read(ARTIFACT / "decisions.json")["decisions"]
    evidence = read(ARTIFACT / "evidence.json")["evidence"]
    proposals = read(ARTIFACT / "proposals.json")["proposals"]
    author_cases, author_evidence, author_proposals = {}, {}, {}
    for part in "abc":
        author_cases.update({x["case_id"]: x for x in read(ARTIFACT / f"parts/{part}-decisions.json")["decisions"]})
        author_evidence.update({x["evidence_id"]: x for x in read(ARTIFACT / f"parts/{part}-evidence.json")["evidence"]})
        author_proposals.update({x["proposal_id"]: x for x in read(ARTIFACT / f"parts/{part}-proposals.json")["proposals"]})
    errors, case_results = [], []
    if len(decisions) != 188 or [d["case_id"] for d in decisions] != [c["case_id"] for c in original]:
        errors.append("Final membership/order differs from exact188-case shard")
    evidence_by_id = {x["evidence_id"]: x for x in evidence}
    for index, (case, decision) in enumerate(zip(original, decisions)):
        problems = []
        if decision["case_input_sha256"] != digest(case):
            problems.append("complete frozen case digest differs")
        if decision["source"] != {key: case[key] for key in ("source", "source_case_id", "source_label", "raw_source_label")}:
            problems.append("source tuple differs")
        if set(decision["occurrence_ids"]) != {o["occurrence_id"] for o in case.get("occurrences", [])}:
            problems.append("occurrences differ")
        author = author_cases[case["case_id"]]
        changed_fields = [key for key in set(author) | set(decision) if author.get(key) != decision.get(key)]
        substantive_changes = [key for key in changed_fields if key not in {"independent_review", "evidence_ids", "proposal_ids", "issue_refs"}]
        if substantive_changes and index not in {11, 23, 45, 46}:
            problems.append(f"Unreviewed root semantic delta: {substantive_changes}")
        if decision["independent_review"]["status"] != "complete":
            problems.append("independent review not complete")
        if not decision["independent_review"]["evidence_ids"] or any(evidence_by_id.get(eid, {}).get("kind") != "independent_review" for eid in decision["independent_review"]["evidence_ids"]):
            problems.append("missing independent review capture reference")
        for owner in decision["owner_records"]:
            blob = git("show", f"{BASE}:{owner['path']}")
            if hashlib.sha256(blob).hexdigest() != owner["sha256"] or sha(ROOT / owner["path"]) != owner["sha256"]:
                problems.append(f"owner baseline changed: {owner['path']}")
        if problems:
            errors.append({"case_id": case["case_id"], "problems": problems})
        case_results.append({"case_index": index, "case_id": case["case_id"], "final_decision_sha256": digest(decision), "author_decision_sha256": digest(author), "changed_fields": sorted(changed_fields), "source_case_and_owner_integrity": "PASS" if not problems else "FAIL"})
    for eid, item in author_evidence.items():
        if evidence_by_id.get(eid) != item:
            errors.append(f"Author evidence metadata changed or removed: {eid}")
    checked_captures = {}
    for item in evidence:
        capture = item["capture"]
        root = ARTIFACT if capture["root"] == "artifact" else SOURCE
        path = root / capture["path"]
        if path.is_symlink() or not path.is_file() or sha(path) != capture["sha256"]:
            errors.append(f"Evidence capture mismatch: {item['evidence_id']}")
        checked_captures[f"{capture['root']}:{capture['path']}"] = capture["sha256"]
    for proposal in proposals:
        path = ARTIFACT / proposal["after_capture"]["path"]
        if sha(path) != proposal["after_capture"]["sha256"]:
            errors.append(f"Proposed payload changed: {proposal['proposal_id']}")
        if proposal["proposal_id"] in author_proposals and proposal["after_capture"] != author_proposals[proposal["proposal_id"]]["after_capture"]:
            errors.append(f"Author payload replaced without explicit composition: {proposal['proposal_id']}")
        for capture in proposal.get("original_author_payloads", []):
            if sha(ARTIFACT / capture["path"]) != capture["sha256"]:
                errors.append(f"Original composition input changed: {capture['path']}")
    staged = git("diff", "--cached", "--name-status", BASE).decode().splitlines()
    tracked_worktree_changes = git("diff", "--name-only").decode().splitlines()
    for row in staged:
        status, path = row.split("\t", 1)
        if status != "A" or not (path.startswith("reports/all_unmatched_20261107/worker-07/") or path.startswith("reviews/structured/")):
            errors.append(f"Unexpected staged change: {row}")
    for path in tracked_worktree_changes:
        if not (path.startswith("reports/all_unmatched_20261107/worker-07/") or path.startswith("reviews/structured/")):
            errors.append(f"Unexpected tracked worktree change: {path}")
    inputs = ["decisions.json", "evidence.json", "proposals.json", "parts/root-assemble.py", "parts/root-decision-deltas.json", "parts/root-validate-proposals.py"]
    result = {"reviewer": "/root/integration_reviewer", "checked_at": datetime.now(timezone.utc).isoformat(), "status": "PASS" if not errors else "FAIL", "scientific_approval": False, "scope": "All188 final case accounting and author-to-final changed fields; original evidence metadata/capture integrity; baseline owner bytes checked against git object; proposed payload/original composition captures; all staged paths against allowed artifact/native-review additions.", "input_hashes": {p: sha(ARTIFACT / p) for p in inputs}, "case_count": len(decisions), "proposal_count": len(proposals), "evidence_entry_count": len(evidence), "unique_checked_evidence_capture_count": len(checked_captures), "independent_status_counts": dict(Counter(x["independent_review"]["status"] for x in decisions)), "cases": case_results, "staged_name_status": staged, "tracked_unstaged_paths": tracked_worktree_changes, "errors": errors}
    output.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps({key: result[key] for key in ("status", "case_count", "proposal_count", "evidence_entry_count", "unique_checked_evidence_capture_count", "independent_status_counts", "errors")}))
    return 0 if not errors else 1


if __name__ == "__main__":
    raise SystemExit(main())
