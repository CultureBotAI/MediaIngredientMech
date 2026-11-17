#!/usr/bin/env python3
"""Count reviewed source membership without changing it, #1453, 2026-11-17.

Inputs: externally pinned intake and reviewed receipts plus native dispositions.
Output: new compact JSON accounting; no identity decisions, conversions or sends.
This supplements native replay; matching counts do not prove scientific approval.
"""

import argparse
import json
from collections import Counter
from pathlib import Path

from mediaingredientmech.intake import culturemech as native


def summarize(source, source_pin, reviewed, reviewed_pin):
    original, _ = native.read_json(source / "intake.json", source_pin)
    receipt, _ = native.read_json(reviewed / "reviewed-intake.json", reviewed_pin)
    native.require(receipt["intake_sha256"] == source_pin, "Different source intake")
    native.check_snapshot(reviewed, receipt["files"])
    counts, scopes, holds = Counter(), {}, {}
    fields = ("positive_occurrences", "context_only_mentions", "held_source_mentions")
    with native.csv_reader(reviewed / "binding-dispositions.tsv") as reader:
        for row in reader:
            native.checked_row(row)
            status = row["disposition"]
            native.require(status in {"SUPPORTED", "WITHHOLD"}, "Unknown disposition")
            counts[status] += 1
            scope = scopes.setdefault(status, Counter())
            for field in fields:
                number = int(row[field])
                native.require(number >= 0, "Negative membership count")
                scope[field] += number
            for dimension in json.loads(row["held_fields_json"]):
                holds.setdefault(status, Counter())[dimension] += int(row["held_source_mentions"])
    native.require(dict(counts) == receipt["counts"], "Disposition count mismatch")
    native.require(sum(counts.values()) == original["counts"]["cases"], "Case coverage mismatch")
    for field, original_field in zip(
        fields, ("source_occurrences", "context_only_mentions", "held_source_mentions"), strict=True
    ):
        native.require(
            sum(scope[field] for scope in scopes.values()) == original["counts"][original_field],
            "Source membership mismatch",
        )
    native.read_json(source / "intake.json", source_pin)
    native.read_json(reviewed / "reviewed-intake.json", reviewed_pin)
    native.check_snapshot(reviewed, receipt["files"])
    return {
        "status": "ACCOUNTED_REVIEWED_SOURCE_MEMBERSHIP",
        "intake_sha256": source_pin,
        "reviewed_sha256": reviewed_pin,
        "source_contract": original["source_contract"],
        "source_manifest_sha256": original["source_manifest_sha256"],
        "cases_by_disposition": dict(counts),
        "mentions_by_disposition": scopes,
        "held_mentions_by_disposition_and_dimension": holds,
        "canonical_sssom": receipt["canonical_sssom"],
        "reviewed_files": receipt["files"],
        "limitations": "Identity binding support does not change source presence or clear quantity, operation or stage holds. Held mentions remain zero presence even when their scoped material identity is supported. Held dimensions overlap and must not be summed as distinct mentions. No new canonical release or KGM installation is asserted.",
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--intake", type=Path, required=True)
    parser.add_argument("--intake-sha256", required=True)
    parser.add_argument("--reviewed", type=Path, required=True)
    parser.add_argument("--reviewed-sha256", required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    result = summarize(args.intake, args.intake_sha256, args.reviewed, args.reviewed_sha256)
    native.write_json(args.output, result)
    print(json.dumps(native.fingerprint(args.output)))


if __name__ == "__main__":
    main()
