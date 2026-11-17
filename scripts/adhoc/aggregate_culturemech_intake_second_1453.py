#!/usr/bin/env python3
"""Combine explicit reviewer decisions for intake #1453, 2026-11-17.

Inputs: pinned partition summary, inclusive owner range, selected partial JSON files.
Output: one new JSON containing unchanged decisions and input hashes.
No new decisions, source edits, network calls or overwriting existing artifacts.
"""

import argparse
import hashlib
import json
from collections import Counter
from pathlib import Path

from review_culturemech_intake_second_1453 import read_pinned


def combine(partitions, summary_pin, first, last, inputs, output):
    """Require exact case coverage and retain each explicit decision unchanged."""
    if first > last or not inputs:
        raise ValueError("An inclusive owner range and input files are required")
    summary = read_pinned(partitions / "summary.json", summary_pin)
    expected = {}
    snapshots = {}
    for index in range(first, last + 1):
        name = f"owner-{index:04d}.json"
        pin = summary["files"][name]["sha256"]
        packet = read_pinned(partitions / name, pin)
        for case_id, row_pin in packet["case_payload_sha256"].items():
            if case_id in expected:
                raise ValueError("Repeated partition case")
            expected[case_id] = row_pin
    decisions = {}
    for path in inputs:
        raw = path.read_bytes()
        if path in snapshots:
            raise ValueError("Repeated author input")
        snapshots[path] = raw
        partial = json.loads(raw)
        if partial["intake_sha256"] != summary["intake_sha256"]:
            raise ValueError("Author input belongs to a different intake")
        # Earliest explicit notes bind intake + every complete case, without a
        # summary field. Still check every case digest against the pinned range.
        if partial.get("partition_summary_sha256", summary_pin) != summary_pin:
            raise ValueError("Author input belongs to a different partition snapshot")
        for decision in partial["decisions"]:
            case_id = decision["case_id"]
            if case_id in decisions:
                raise ValueError("Repeated authored case")
            if expected.get(case_id) != decision["row_sha256"]:
                raise ValueError("Unexpected or stale authored case")
            decisions[case_id] = decision
    if set(decisions) != set(expected):
        raise ValueError("Incomplete owner-range coverage")
    result = {
        "intake_sha256": summary["intake_sha256"],
        "partition": "second",
        "owner_index_range": [first, last],
        "partition_summary_sha256": summary_pin,
        "author_inputs": {
            str(path): hashlib.sha256(raw).hexdigest() for path, raw in snapshots.items()
        },
        "decisions": [decisions[key] for key in sorted(decisions)],
    }
    encoded = json.dumps(result, indent=2, sort_keys=True) + "\n"
    read_pinned(partitions / "summary.json", summary_pin)
    for index in range(first, last + 1):
        name = f"owner-{index:04d}.json"
        read_pinned(partitions / name, summary["files"][name]["sha256"])
    for path, raw in snapshots.items():
        if path.read_bytes() != raw:
            raise ValueError("Author input changed")
    with output.open("x") as stream:
        stream.write(encoded)
    return {
        "cases": len(decisions),
        "dispositions": dict(Counter(item["disposition"] for item in decisions.values())),
        "sha256": hashlib.sha256(encoded.encode()).hexdigest(),
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--partitions", required=True, type=Path)
    parser.add_argument("--summary-sha256", required=True)
    parser.add_argument("--first", required=True, type=int)
    parser.add_argument("--last", required=True, type=int)
    parser.add_argument("--input", required=True, action="append", type=Path)
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()
    result = combine(
        args.partitions, args.summary_sha256, args.first, args.last, args.input, args.output
    )
    print(json.dumps(result, sort_keys=True))


if __name__ == "__main__":
    main()
