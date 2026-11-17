#!/usr/bin/env python3
"""Materialize explicit first-slice source reviews for #1453, 2026-11-17.

Inputs: pinned final v3 owner packets and a manually authored case decision table.
Output: a new full-payload-bound reviewer JSON; no inferred scientific approvals.
Every case of owner indices 0 through 108 must have an explicit current decision.
"""

import argparse
import hashlib
import json
from collections import Counter
from pathlib import Path

from assemble_culturemech_binding_review_1453 import validate_coverage
from review_culturemech_intake_second_1453 import read_pinned

INTAKE = "6bcc92540daba081d8180346d135c2ae40471c9fb0a7005b46aa5c9902d684f7"
PARTITIONS = "c166a20a7874dab2fe7c4812ed733d5065008a75a89841aae0e92a6e6811451b"


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--partitions", required=True, type=Path)
    parser.add_argument("--manual", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()
    summary = read_pinned(args.partitions / "summary.json", PARTITIONS)
    manual_bytes = args.manual.read_bytes()
    manual = json.loads(manual_bytes)
    if manual["intake_sha256"] != INTAKE:
        raise ValueError("Manual decisions name another intake")
    supplied = {entry["case_id"]: entry for entry in manual["decisions"]}
    if len(supplied) != len(manual["decisions"]):
        raise ValueError("Duplicate manual case")
    cases = {}
    for index in range(109):
        name = f"owner-{index:04d}.json"
        packet = read_pinned(args.partitions / name, summary["files"][name]["sha256"])
        for case in packet["cases"]:
            key = case["case_id"]
            cases[key] = (case, packet["case_payload_sha256"][key])
    if set(supplied) != set(cases):
        raise ValueError("Explicit decisions must cover every assigned case exactly once")
    output = []
    for key, (case, pin) in sorted(cases.items()):
        decision = dict(supplied[key])
        # The global partition pin fixes all case bytes. Explicit author choices
        # may omit copied digests; this only materializes their provenance, never
        # chooses a case, disposition or scientific reason from matching flags.
        decision.setdefault("row_sha256", pin)
        if decision["row_sha256"] != pin:
            raise ValueError("Manual review is stale")
        if decision["disposition"] == "SUPPORTED" and "canonical_row_sha256" not in decision:
            canonical = case["candidate"]["supported_canonical_rows"]
            if len(canonical) != 1:
                raise ValueError("Author must select the exact supported canonical row")
            decision["canonical_row_sha256"] = canonical[0]["row_sha256"]
        if not decision["review_reason"].strip() or not decision["evidence_locators"]:
            raise ValueError("Missing explicit reason/evidence")
        bound = {
            **decision,
            **(
                {
                    "inspected_descriptor_sha256": sorted(case["descriptors"]),
                    "inspected_change_sha256": sorted(case.get("change_payloads", {})),
                    "inspected_held_sha256": sorted(case.get("held_payloads", {})),
                }
                if decision["disposition"] == "SUPPORTED"
                else {
                    field: decision[field]
                    for field in (
                        "inspected_descriptor_sha256",
                        "inspected_change_sha256",
                        "inspected_held_sha256",
                        "blocking_witnesses",
                    )
                }
            ),
        }
        validate_coverage(bound, case)
        output.append(bound)
    if args.manual.read_bytes() != manual_bytes:
        raise ValueError("Manual decisions changed")
    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open("x") as stream:
        json.dump(
            {
                "intake_sha256": INTAKE,
                "partition": "owner indices 0 through 108 inclusive",
                "partition_summary_sha256": PARTITIONS,
                "manual_decisions_sha256": hashlib.sha256(manual_bytes).hexdigest(),
                "decisions": output,
            },
            stream,
            indent=2,
            sort_keys=True,
        )
        stream.write("\n")
    print(
        json.dumps(
            {
                "cases": len(output),
                "dispositions": dict(Counter(row["disposition"] for row in output)),
                "sha256": hashlib.sha256(args.output.read_bytes()).hexdigest(),
            },
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
