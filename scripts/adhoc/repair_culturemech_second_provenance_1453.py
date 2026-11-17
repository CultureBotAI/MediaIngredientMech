#!/usr/bin/env python3
"""Correct two reviewed narrative fields for #1535/#1536, 2026-11-17.

Input: immutable second-slice decisions pinned below. Output: exclusive successor
JSON and exact field-delta receipt. Scientific decisions and payload pins unchanged.
"""

import argparse
import copy
import hashlib
import json
from pathlib import Path

PIN = "a309fe8b6a841afea0d0b4463a205fe322a2722fced2797930bd0cbfe815791b"


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--receipt", type=Path, required=True)
    args = parser.parse_args()
    raw = args.source.read_bytes()
    if hashlib.sha256(raw).hexdigest() != PIN:
        raise ValueError("Unexpected reviewed predecessor")
    if args.output.exists() or args.receipt.exists():
        raise ValueError("Successor paths must be new")
    original = json.loads(raw)
    successor = copy.deepcopy(original)
    changes = []
    for decision in successor["decisions"]:
        key = decision["case_id"]
        if key.startswith("b198a7c5"):
            before = decision["evidence_locators"][0]
            bad = "d300b6526d61bfef904b8c9ca20b96a7c4c020a0bb686b85b9f007dc74079a07f8"
            good = "d300b6526d61bfef904b8c9ca20b96a7c020a0bb686b85b9f007dc74079a07f8"
            if before.count(bad) != 1:
                raise ValueError("Unexpected locator beforeimage")
            after = before.replace(bad, good)
            decision["evidence_locators"][0] = after
            field = "/evidence_locators/0"
        elif key.startswith("d0c8d3"):
            before = decision["blocking_witnesses"][0]["reason"]
            expected = (
                "The literal KOMODO source calls the material sodium sulfide hydrate, "
                "while its term and MIM-derived term assert anhydrous CHEBI:76208."
            )
            if before != expected:
                raise ValueError("Unexpected witness beforeimage")
            after = (
                "The literal KOMODO source calls the material sodium sulfide hydrate, "
                "while the selected candidate owner denotes anhydrous CHEBI:76208; "
                "this witness itself contains no term or MIM-derived term field."
            )
            decision["blocking_witnesses"][0]["reason"] = after
            field = "/blocking_witnesses/0/reason"
        else:
            continue
        changes.append({"case_id": key, "field": field, "before": before, "after": after})
    if len(changes) != 2:
        raise ValueError("Expected exactly two corrections")
    encoded = (json.dumps(successor, indent=2, sort_keys=True) + "\n").encode()
    receipt = {
        "predecessor_sha256": PIN,
        "successor_sha256": hashlib.sha256(encoded).hexdigest(),
        "changes": changes,
        "scientific_dispositions_and_machine_pins": "UNCHANGED",
    }
    if args.source.read_bytes() != raw:
        raise ValueError("Predecessor changed")
    with args.output.open("xb") as stream:
        stream.write(encoded)
    with args.receipt.open("x") as stream:
        stream.write(json.dumps(receipt, indent=2, sort_keys=True) + "\n")
    print(json.dumps(receipt, sort_keys=True))


if __name__ == "__main__":
    main()
