#!/usr/bin/env python3
"""Prepare the completed first-slice native review, #1453, 2026-11-17.

Inputs: exact manually authored first-v2 decisions and pinned owner packets.
Outputs: new durable decision bytes, native inspection and review draft; no sends.
This records existing case judgments; it does not infer scientific approvals.
Run with PYTHONPATH=src:scripts; save the draft through record_review.py save.
"""

import argparse
import hashlib
import json
import re
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path

from assemble_culturemech_binding_review_1453 import validate_coverage
from record_review import assert_current_source, inspect_source, validate_review
from review_culturemech_intake_second_1453 import read_pinned

ROOT = Path(__file__).resolve().parents[2]
DECISION_PIN = "b11e5881c85c3df0e920d66e38ad35819df92046629ed4bc4a8403a7011f4022"
PARTITION_PIN = "c166a20a7874dab2fe7c4812ed733d5065008a75a89841aae0e92a6e6811451b"


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--decisions", type=Path, required=True)
    parser.add_argument("--partitions", type=Path, required=True)
    parser.add_argument("--output-dir", type=Path, required=True)
    args = parser.parse_args()
    started = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    raw = args.decisions.read_bytes()
    if hashlib.sha256(raw).hexdigest() != DECISION_PIN:
        raise ValueError("Unexpected manually reviewed decision snapshot")
    decisions = json.loads(raw)
    summary = read_pinned(args.partitions / "summary.json", PARTITION_PIN)
    cases, contexts = {}, {"MAPPING_SEMANTICS.md", "reports/sssom_completion_20260921/review.json"}
    for index in range(109):
        name = f"owner-{index:04d}.json"
        path = args.partitions / name
        packet = read_pinned(path, summary["files"][name]["sha256"])
        contexts.add(path.resolve().relative_to(ROOT).as_posix())
        contexts.add(packet["owner_record"])
        for case in packet["cases"]:
            cases[case["case_id"]] = case
    entries = decisions["decisions"]
    if len(entries) != len(cases) or {d["case_id"] for d in entries} != set(cases):
        raise ValueError("Incomplete or duplicate explicit decisions")
    for decision in entries:
        validate_coverage(decision, cases[decision["case_id"]])
        if decision["disposition"] == "SUPPORTED" and set(
            cases[decision["case_id"]]["context"].get("held_fields", [])
        ) & {"SOURCE_CLAIM", "IDENTITY_FORM"}:
            raise ValueError("Source/identity hold cannot support binding")
    output = args.output_dir.resolve()
    output.relative_to(ROOT / "reports")
    output.mkdir(parents=True, exist_ok=False)
    decision_file = output / "decisions.json"
    decision_file.write_bytes(raw)
    rel = decision_file.relative_to(ROOT).as_posix()
    targets, evidence, assessments, findings = [], [], [], []
    for decision in entries:
        key = decision["case_id"]
        case = cases[key]
        tid, eid = "case-" + key[:16], "evidence-" + key[:16]
        owner = {
            "repository": "CultureBotAI/MediaIngredientMech",
            "path": case["candidate"]["owner_record"],
            "role": "Maintained candidate identity; frozen source corrections belong in CultureMech",
        }
        targets.append(
            {
                "target_id": tid,
                "path": rel,
                "selector": "decisions[case_id=" + key + "]",
                "label": case["context"]["preferred_term"],
                "kind": "snapshot_row",
                "owner_paths": [owner],
            }
        )
        evidence.append(
            {
                "evidence_id": eid,
                "kind": "record_content",
                "reference": rel,
                "locator": "decisions[case_id="
                + key
                + "]; full payload SHA256 "
                + decision["row_sha256"],
                "accessed_at": started,
                "support": "supports" if decision["disposition"] == "SUPPORTED" else "partial",
                "summary": decision["review_reason"],
                "snapshot_sha256": DECISION_PIN,
            }
        )
        assessments.append(
            {
                "assessment_id": "assessment-" + key[:16],
                "area": "identity",
                "topic": "Exact source binding to the native canonical-eligible owner",
                "outcome": "supported" if decision["disposition"] == "SUPPORTED" else "concern",
                "summary": decision["review_reason"],
                "target_ids": [tid],
                "evidence_ids": [eid],
                "details": "Source/evidence locators: "
                + json.dumps(decision["evidence_locators"], ensure_ascii=False),
            }
        )
        if decision["disposition"] == "WITHHOLD":
            issues = sorted(
                set(
                    re.findall(
                        r"https://github\.com/CultureBotAI/[A-Za-z]+/issues/\d+",
                        " ".join(decision["evidence_locators"]),
                    )
                )
            )
            finding = {
                "finding_id": "withhold-" + key[:16],
                "issue_key": "culturemech-intake-binding-" + key[:16],
                "category": "identity",
                "severity": "major",
                "status": "open",
                "certainty": "confirmed",
                "title": "Source binding withheld: " + case["context"]["preferred_term"],
                "description": decision["review_reason"],
                "target_ids": [tid],
                "evidence_ids": [eid],
                "owner_paths": [owner],
                "field_paths": [w["field_path"] for w in decision["blocking_witnesses"]],
                "disposition_reason": "The complete unchanged case is quarantined; inspected member hashes and actual blocking witnesses remain in the durable decision JSON.",
            }
            if issues:
                finding["external_issues"] = issues
            findings.append(finding)
    inspection = inspect_source(ROOT, targets, sorted(contexts))
    (output / "inspection.json").write_text(json.dumps(inspection, indent=2) + "\n")
    counts = Counter(row["disposition"] for row in entries)
    finished = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    review = {
        "schema_version": "1.0.0",
        "review_id": finished.replace("-", "").replace(":", "")
        + "-culturemech-intake-first-source-bindings",
        "kind": "batch",
        "repository": "CultureBotAI/MediaIngredientMech",
        "title": "CultureMech v3 intake source bindings, owner indices 0 through 108",
        "started_at": started,
        "finished_at": finished,
        "reviewer": {
            "identity": "Codex bundle_impl",
            "kind": "agent",
            "independence": "self_review",
            "independence_basis": "Author of these binding decisions and intake implementation, and contributor to some upstream CultureMech curation. The frozen maintained MIM owners were not changed. Independent sampled cross-review is separately recorded; no independent double-review of all cases is claimed.",
        },
        "skill": "lbnl-mech-record-review; native docs/record-reviews.md and MAPPING_SEMANTICS.md",
        "completion": "completed",
        "verdict": "needs_curation",
        "native_verdict": f"{counts['SUPPORTED']} SUPPORTED; {counts['WITHHOLD']} WITHHOLD; identity-only source binding",
        "scientific_review": True,
        "summary": "Explicit source-binding decisions for all161 canonical-eligible cases in109 assigned owner groups. Every supported case received complete distinct descriptor/change/held scientific-payload inspection. Holds retain concrete inspected blocking witnesses and quarantine the full unchanged case. No owner, canonical row, source quantity or growth claim is repaired or promoted.",
        "source": inspection["source"],
        "targets": targets,
        "scope": {
            "description": "Complete assigned-case disposition coverage, with exact per-case evidence and bounded payload-read declarations.",
            "selection": "Pinned final v3 partition owner indices0 through108 inclusive; no selection by flags or matching label alone.",
            "coverage": "full",
            "population_size": len(entries),
            "reviewed_target_ids": [t["target_id"] for t in targets],
        },
        "checks": [
            {
                "check_id": "payload-membership",
                "name": "Native full-support and actual blocking-witness membership",
                "status": "passed",
                "required": True,
                "summary": "The assembler validate_coverage function accepted every exact case: all scientific payload hashes for support, nonempty recomputed member/field witnesses for holds.",
                "target_ids": [t["target_id"] for t in targets],
            }
        ],
        "evidence": evidence,
        "assessments": assessments,
        "findings": findings,
        "actions": [
            {
                "action_id": "reconcile-" + finding["finding_id"],
                "description": "Reconcile the exact source-to-owner identity discrepancy before replacing this WITHHOLD disposition; preserve the frozen intake.",
                "finding_ids": [finding["finding_id"]],
                "target_ids": finding["target_ids"],
                "owner_paths": finding["owner_paths"],
                "acceptance_checks": [
                    "Inspect the exact blocking witness and its primary source; do not infer salt, hydrate, stereochemistry or preparation equivalence from label matching.",
                    "Any corrected source/owner must receive a new payload-bound review and regenerated native supported/withheld products; preserve this observation unchanged.",
                ],
            }
            for finding in findings
        ],
        "limitations": [
            "Report-consolidation timestamps are recorded here; the case-level scientific inspection occurred during the preceding2026-11-16/17 session and is preserved in the explicit decisions and source locators.",
            "Canonical eligibility is the separately pinned native2026-09-21 mapping review; this review does not create a new global SSSOM release or adopt the active campaign.",
            "Identity support excludes dose, growth, whole-stock equivalence and unspecified supplied forms except where the individual reason explicitly establishes the scoped material correspondence.",
            "Per-case WITHHOLD inspected hashes are the authoritative minimum coverage; a blocking witness may quarantine an aggregate without claiming unread payloads were reviewed.",
            "Prepared intake, full owner packets and original producer remain immutable ignored evidence; the durable decisions retain their exact hashes and source pins. Final native intake finalization and independent product/QC verification remain required.",
        ],
        "links": [
            "https://github.com/CultureBotAI/MediaIngredientMech/issues/1453",
            "https://github.com/CultureBotAI/MediaIngredientMech/pull/1460",
        ],
    }
    assert_current_source(ROOT, review)
    if args.decisions.read_bytes() != raw:
        raise ValueError("Manual review drift")
    validate_review(review, ROOT / "schema/record_review.yaml")
    draft = output / "review-draft.json"
    draft.write_text(json.dumps(review, indent=2, ensure_ascii=False) + "\n")
    print(
        json.dumps(
            {
                "draft": str(draft.relative_to(ROOT)),
                "decisions_sha256": DECISION_PIN,
                "cases": len(entries),
                "counts": dict(counts),
            },
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
