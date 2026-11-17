#!/usr/bin/env python3
"""Preserve bounded independent intake cross-review, #1453, 2026-11-17.

Inputs: unchanged root decision snapshots, packet pins and authored scope below.
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
    "root-tail": {
        "sha256": "949977d4c83b91933fdd15b816087f117a2d2861331edf05a59728dbb0b5d5d4",
        "reason_count": 67,
        "summary": "All67 reasons independently read. Complete scientific source payloads and current owners inspected for SL-10 cases3f38be/f41cd2, vitamin-solution casesbf9a6e/da7569, Vitox16c3f3, Jamarin32838c and Zeikus9cf4af. Exact10-input SL-10 and12-input Zeikus formulations corroborated by primary collection recipes; Vitox named supplement and Jamarin named10x material corroborated without inferring dose or interchangeability. No new material binding finding in these seven complete-case samples.",
        "owners": [402, 423, 424, 428, 433],
    },
    "root-water": {
        "sha256": "edea0f109e4c8d7d02252f9da2c472000a7fe000defaf7b0782148b0ff7cc0f3",
        "reason_count": 18,
        "summary": "All18 reasons independently read. Complete owner118 history470 and complete cases4f275d (one descriptor/two ADD changes) and c71e5c (four descriptors) inspected. One complete blocking witness2281413d from cf881d inspected; the other3030-pool payloads were not independently read. The owner retains generic molecular Water/H2O but excludes supplied sterile/deionized/demineralized forms. Water input followed by autoclaving differs from a supplied autoclaved-water preparation. No new material finding in this bounded sample.",
        "owners": [118],
    },
    "root-upper": {
        "sha256": "5f0660e3f828a2001e8def16a0cf3c7096a4ecc2e41f4e4baf713ecd1611e24d",
        "reason_count": 76,
        "summary": "All76 reasons independently read. Complete Table wine case7115a6 and both Thallium(I) acetate cases930e5f/c6f666 inspected with current owners. Sulfur owner history368 and complete atom-grounded witness6652b30f inspected; no claim to the other39 powder descriptors. Glycerophosphate witness77304abb and its Sigma gradeII note inspected alongside earlier primary NCI/FDA/current Sigma scope checks; a historical hydration state is not inferred from current products. These checks support the existing1520/1522/1526 holds and bounded named-solute supports; no new material finding in the sample.",
        "owners": [357, 380, 384, 394],
    },
}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--decisions-dir", type=Path, required=True)
    parser.add_argument("--partitions", type=Path, required=True)
    parser.add_argument("--root-first-cross-review", type=Path, required=True)
    parser.add_argument("--root-middle-cross-review", type=Path, required=True)
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
                "support": "supports",
                "summary": scope["summary"],
                "snapshot_sha256": hashlib.sha256(raw).hexdigest(),
            }
        )
        assessments.append(
            {
                "assessment_id": name,
                "area": "identity",
                "topic": "Bounded independent source-binding cross-review",
                "outcome": "supported",
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
    root_raw = args.root_first_cross_review.read_bytes()
    root_copy = output / "root-first-cross-review.md"
    root_copy.write_bytes(root_raw)
    contexts.add(root_copy.relative_to(ROOT).as_posix())
    middle_raw = args.root_middle_cross_review.read_bytes()
    middle_copy = output / "root-middle-cross-review.md"
    middle_copy.write_bytes(middle_raw)
    contexts.add(middle_copy.relative_to(ROOT).as_posix())
    inspection = inspect_source(ROOT, targets, sorted(contexts))
    (output / "inspection.json").write_text(json.dumps(inspection, indent=2) + "\n")
    review = {
        "schema_version": "1.0.0",
        "review_id": now.replace("-", "").replace(":", "")
        + "-culturemech-intake-bounded-cross-review",
        "kind": "batch",
        "repository": "CultureBotAI/MediaIngredientMech",
        "title": "Bounded independent cross-review of root CultureMech binding decisions",
        "started_at": now,
        "finished_at": now,
        "reviewer": {
            "identity": "Codex bundle_impl",
            "kind": "agent",
            "independence": "independent",
            "independence_basis": "Did not author these three root decision snapshots. Authored the intake implementation and a disjoint first scientific slice; contributed some upstream CultureMech curation. This report claims only the explicitly listed independent decision/payload samples.",
        },
        "skill": "lbnl-mech-record-review; native docs/record-reviews.md and MAPPING_SEMANTICS.md",
        "completion": "completed",
        "verdict": "pass_with_limitations",
        "scientific_review": True,
        "summary": "Read all161 root decision reasons across67tail/18water/76upper cases, then inspected the explicitly listed complete cases and blocking witnesses. No new material issue found in this bounded sample. Existing scientific holds remain in place; this is not approval of withheld chemistry or all161payloads.",
        "source": inspection["source"],
        "targets": targets,
        "scope": {
            "description": "All decision reasons, sampled complete scientific payloads and precise blocking witnesses.",
            "selection": "Risk-based sample declared per target; no statistical representativeness claimed.",
            "coverage": "sampled",
            "sampling_method": "Purposive exact preparation, supplied-form, stale-ID and gas/quantity boundary cases; all reasons read, scientific payloads only as explicitly listed.",
            "population_size": 161,
            "reviewed_target_ids": [t["target_id"] for t in targets],
        },
        "checks": checks,
        "evidence": evidence,
        "assessments": assessments,
        "findings": [],
        "actions": [],
        "limitations": [
            "Not an independent double-review of every scientific payload, source coordinate or original publication. Exact sample sizes and witnesses are declared per target.",
            "Root's separate first-slice review is retained byte-for-byte as attributed context, not claimed as this reviewer's independent inspection of their own decisions.",
            "Current product data cannot prove historical Sigma gradeII hydration; unresolved supplied forms remain withheld. Quantity, growth, release adoption and global canonical publication are outside this identity cross-review.",
            "Native finalization, exact product replay, complete author-case coverage and final PR review remain required. Timestamps record consolidation of the preceding read-only inspection.",
        ],
        "links": [
            "https://github.com/CultureBotAI/MediaIngredientMech/issues/1453",
            "https://github.com/CultureBotAI/MediaIngredientMech/pull/1460",
        ],
    }
    assert_current_source(ROOT, review)
    if (
        any(path.read_bytes() != raw for path, raw in frozen.items())
        or args.root_first_cross_review.read_bytes() != root_raw
        or args.root_middle_cross_review.read_bytes() != middle_raw
    ):
        raise ValueError("Cross-review source changed")
    validate_review(review, ROOT / "schema/record_review.yaml")
    draft = output / "review-draft.json"
    draft.write_text(json.dumps(review, indent=2) + "\n")
    print(draft.relative_to(ROOT))


if __name__ == "__main__":
    main()
