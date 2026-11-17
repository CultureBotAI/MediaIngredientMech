#!/usr/bin/env python3
"""Preserve bounded independent intake cross-review, #1453, 2026-11-17.

Inputs: unchanged second-slice decisions, packet pins and authored scope below.
Outputs: exact durable copies and native review draft; no inferred decisions/sends.
This records completed inspection, not a fresh full-payload review of all cases.
"""

import argparse
import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path

from record_review import assert_current_source, inspect_source, validate_review
from review_culturemech_intake_second_1453 import read_pinned

ROOT = Path(__file__).resolve().parents[2]
PARTITION_PIN = "c166a20a7874dab2fe7c4812ed733d5065008a75a89841aae0e92a6e6811451b"
SCOPES = {
    "second-219-284": {
        "sha256": "a309fe8b6a841afea0d0b4463a205fe322a2722fced2797930bd0cbfe815791b",
        "reason_count": 143,
        "summary": "Independently read all 143 decision reasons. Read complete owner266 plus its two descriptors and exact local canonical row; approval correctly excludes the external parent CHEBI:15978. Read complete owner268 history plus full Pinchuk old-side REPLACE case 1d009355 (zero positive occurrences) and its separate monobasic-conflict witness 013d738a. Read complete owner281 and exact ammonium-salt versus anion witness 81424774. Read complete owner270 and hydrate witness c51054. The selected identity boundaries and context-only replacement membership are preserved. Narrative provenance errors were independently confirmed and filed as issues 1535 and 1536; they do not change these dispositions.",
        "owners": [266, 268, 270, 273, 281],
    },
}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--decisions-dir", type=Path, required=True)
    parser.add_argument("--partitions", type=Path, required=True)
    parser.add_argument("--output-dir", type=Path, required=True)
    args = parser.parse_args()
    summary = read_pinned(args.partitions / "summary.json", PARTITION_PIN)
    output = args.output_dir.resolve()
    output.relative_to(ROOT / "reports")
    output.mkdir(parents=True, exist_ok=False)
    targets, assessments, evidence, checks = [], [], [], []
    contexts = {"MAPPING_SEMANTICS.md", "reports/sssom_completion_20260921/review.json"}
    frozen = {}
    now = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    for name, scope in SCOPES.items():
        source = args.decisions_dir / (name + ".json")
        raw = source.read_bytes()
        if hashlib.sha256(raw).hexdigest() != scope["sha256"]:
            raise ValueError("Unexpected independently reviewed decision snapshot")
        snapshot = json.loads(raw)
        if len(snapshot["decisions"]) != scope["reason_count"]:
            raise ValueError("Unexpected reviewed decision count")
        frozen[source] = raw
        dest = output / source.name
        dest.write_bytes(raw)
        rel = dest.relative_to(ROOT).as_posix()
        targets.append(
            {
                "target_id": name,
                "path": rel,
                "kind": "source",
                "label": name,
                "ownership_note": "Frozen review decisions; maintained candidate owners and exact source cases remain in the bound owner packets. This report does not mutate those scientific owners.",
            }
        )
        evidence.append(
            {
                "evidence_id": name,
                "kind": "record_content",
                "reference": rel,
                "accessed_at": now,
                "support": "partial",
                "summary": scope["summary"],
                "snapshot_sha256": hashlib.sha256(raw).hexdigest(),
            }
        )
        assessments.append(
            {
                "assessment_id": name,
                "area": "identity",
                "topic": "Bounded independent source-binding cross-review",
                "outcome": "concern",
                "summary": scope["summary"],
                "target_ids": [name],
                "evidence_ids": [name],
            }
        )
        checks.append(
            {
                "check_id": name,
                "name": "Explicit bounded cross-review",
                "status": "passed",
                "required": True,
                "summary": scope["summary"],
                "target_ids": [name],
            }
        )
        for index in scope["owners"]:
            name = f"owner-{index:04d}.json"
            path = args.partitions / name
            packet = read_pinned(path, summary["files"][name]["sha256"])
            contexts.update([path.resolve().relative_to(ROOT).as_posix(), packet["owner_record"]])
    inspection = inspect_source(ROOT, targets, sorted(contexts))
    (output / "inspection.json").write_text(json.dumps(inspection, indent=2) + "\n")
    review = {
        "schema_version": "1.0.0",
        "review_id": now.replace("-", "").replace(":", "")
        + "-culturemech-intake-second-cross-review",
        "kind": "batch",
        "repository": "CultureBotAI/MediaIngredientMech",
        "title": "Bounded independent cross-review of CultureMech intake owners 219–284",
        "started_at": now,
        "finished_at": now,
        "reviewer": {
            "identity": "Codex release687_current",
            "kind": "agent",
            "independence": "independent",
            "independence_basis": "Did not author these second-slice decisions. Authored disjoint middle binding decisions and contributed upstream CultureMech schema, provenance and some curation, including the Pinchuk variant. This report claims independence from the reviewed binding judgments, not all upstream curation, and only the explicitly listed payload sample.",
        },
        "skill": "lbnl-mech-record-review; native docs/record-reviews.md and MAPPING_SEMANTICS.md",
        "completion": "completed",
        "verdict": "needs_curation",
        "scientific_review": True,
        "summary": "Read all 143 decision reasons and the declared complete-case/witness sample. Two minor textual provenance findings require a successor snapshot; no new substantive identity defect was found within this bounded sample. Existing scientific holds remain in place; this is not approval of withheld chemistry or all 143 scientific payloads.",
        "source": inspection["source"],
        "targets": targets,
        "scope": {
            "description": "All decision reasons, sampled complete scientific payloads and precise blocking witnesses.",
            "selection": "Risk-based sample declared per target; no statistical representativeness claimed.",
            "coverage": "sampled",
            "sampling_method": "Purposive exact preparation, supplied-form, stale-ID and gas/quantity boundary cases; all reasons read, scientific payloads only as explicitly listed.",
            "population_size": 143,
            "reviewed_target_ids": [t["target_id"] for t in targets],
        },
        "checks": checks,
        "evidence": evidence,
        "assessments": assessments,
        "findings": [
            {
                "finding_id": "chlorate-locator",
                "issue_key": "culturemech-intake-second-chlorate-locator-1535",
                "category": "provenance", "severity": "minor", "status": "open",
                "certainty": "confirmed", "title": "Incorrect narrative descriptor digest",
                "ownership_note": "Owned by the second-slice review author; correct only a successor decision snapshot, not source ingredients or canonical rows.",
                "description": "Case b198a7c5e3164e5112e16cb10007008ceb321feeff7a7c4bc2f2dcad109d6e3d evidence_locators[0] contains an extra 4c in descriptor digest d300b6526d61bfef904b8c9ca20b96a7c020a0bb686b85b9f007dc74079a07f8. The author disclosed this before this reviewer independently verified it. The machine-readable inspected hash and complete case pin are correct.",
                "target_ids": ["second-219-284"], "evidence_ids": ["second-219-284"],
                "field_paths": ["decisions[case_id=b198a7c5e3164e5112e16cb10007008ceb321feeff7a7c4bc2f2dcad109d6e3d].evidence_locators[0]"],
                "external_issues": ["https://github.com/CultureBotAI/MediaIngredientMech/issues/1535"],
            },
            {
                "finding_id": "sulfide-witness-wording",
                "issue_key": "culturemech-intake-second-sulfide-witness-1536",
                "category": "provenance", "severity": "minor", "status": "open",
                "certainty": "confirmed", "title": "Witness explanation asserts absent embedded fields",
                "ownership_note": "Owned by the second-slice review author; correct only a successor decision snapshot, not source ingredients or canonical rows.",
                "description": "Case d0c8d3c8ab968b81703d7291e78c7bbb018c735fd3e2cd11b342b18b11d1be20 witness c51054cca36e6a38a39f35805ff8a40060d922a22aa5f7b78988ff6d6906217c has no term or mediaingredientmech_chebi_term. Its explanation incorrectly says those fields assert anhydrous CHEBI76208. The selected candidate/owner, rather than this descriptor, is anhydrous. Literal sodium sulfide hydrate evidence still justifies WITHHOLD against that owner.",
                "target_ids": ["second-219-284"], "evidence_ids": ["second-219-284"],
                "field_paths": ["decisions[case_id=d0c8d3c8ab968b81703d7291e78c7bbb018c735fd3e2cd11b342b18b11d1be20].blocking_witnesses[0].reason"],
                "external_issues": ["https://github.com/CultureBotAI/MediaIngredientMech/issues/1536"],
            },
        ],
        "actions": [{
            "action_id": "preserve-and-correct-narrative",
            "ownership_note": "Second-slice review author owns the decision successor; independent reviewer checks the exact delta.",
            "description": "Retain the original snapshot and emit an independently checked successor with only the two narrative corrections; retain every scientific decision and source hash.",
            "finding_ids": ["chlorate-locator", "sulfide-witness-wording"],
            "target_ids": ["second-219-284"],
            "acceptance_checks": ["Exact two-field diff; complete case membership and pins unchanged; new native review and final assembly use successor bytes."],
        }],
        "limitations": [
            "Not an independent double-review of every scientific payload, source coordinate or original publication. Exact sample sizes and witnesses are declared per target.",
            "The sampled packet claims and maintained owners were reread; underlying primary publications were not re-retrieved during this second-pass cross-review. Quantity, growth, release adoption and global canonical publication are outside its scope.",
            "Native finalization, exact product replay, complete author-case coverage and final PR review remain required. Timestamps record consolidation of the preceding read-only inspection.",
        ],
        "links": [
            "https://github.com/CultureBotAI/MediaIngredientMech/issues/1453",
            "https://github.com/CultureBotAI/MediaIngredientMech/pull/1460",
        ],
    }
    assert_current_source(ROOT, review)
    if any(path.read_bytes() != raw for path, raw in frozen.items()):
        raise ValueError("Cross-review source changed")
    validate_review(review, ROOT / "schema/record_review.yaml")
    draft = output / "review-draft.json"
    draft.write_text(json.dumps(review, indent=2) + "\n")
    print(draft.relative_to(ROOT))


if __name__ == "__main__":
    main()
