"""Compare the strict-port outputs without conferring scientific approval.

The baseline receipt is an explicitly hash-bound input. The caller must select
the current companion review; there is no fallback to a historical review.
Only its base-review dependency hash may advance, and that hash must describe
the actual current mapping review. Native export validation remains required.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import io
import json
from collections import Counter
from pathlib import Path

MAPPING = "reports/sssom_completion_20260921/review.json"
SEMANTIC = "reports/semantic_review_20260921/resolution"
POSITIVE = {"SUPPORTED", "APPROVED", "RESOLVED"}


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def member(root, name):
    path = Path(name)
    if path.is_absolute() or ".." in path.parts:
        raise ValueError(f"Expected a repository-relative path: {name}")
    result = root / path
    if not result.resolve().is_relative_to(root.resolve()):
        raise ValueError(f"Input escapes its declared root: {name}")
    return result


def read(path):
    return json.loads(path.read_bytes())


def rows(path):
    with path.open(newline="") as stream:
        return list(csv.DictReader(stream, delimiter="\t"))


class Snapshot:
    """Hash and parse the same bytes, then refuse changes during comparison."""

    def __init__(self):
        self.inputs = {}

    def payload(self, path):
        path = path.absolute()
        if path not in self.inputs:
            target = path.resolve()
            content = path.read_bytes()
            if path.resolve() != target:
                raise ValueError(f"Input target changed during capture: {path}")
            self.inputs[path] = (target, content)
        return self.inputs[path][1]

    def digest(self, path):
        return hashlib.sha256(self.payload(path)).hexdigest()

    def read(self, path):
        return json.loads(self.payload(path))

    def rows(self, path):
        return list(csv.DictReader(io.StringIO(self.payload(path).decode()), delimiter="\t"))

    def verify(self):
        for path, (target, content) in self.inputs.items():
            if path.resolve() != target or path.read_bytes() != content:
                raise ValueError(f"Input changed during comparison: {path}")


def indexed(items, key):
    result = {str(row[key]): row for row in items}
    if len(result) != len(items):
        raise ValueError(f"Duplicate disposition key: {key}")
    return result


def compare(before, after, key, status):
    old, new = indexed(before, key), indexed(after, key)
    return {
        "before_count": len(old),
        "after_count": len(new),
        "before_status": dict(Counter(row[status] for row in old.values())),
        "after_status": dict(Counter(row[status] for row in new.values())),
        "added": {key: new[key] for key in sorted(new.keys() - old.keys())},
        "removed": {key: old[key] for key in sorted(old.keys() - new.keys())},
        "changed": {
            key: {"before": old[key], "after": new[key]}
            for key in sorted(old.keys() & new.keys())
            if old[key] != new[key]
        },
    }


def positive_changes(comparison):
    def positive(row):
        return row.get("disposition", row.get("resolution_status")) in POSITIVE

    return any(positive(row) for row in comparison["added"].values()) or any(
        positive(change["after"]) for change in comparison["changed"].values()
    )


def assess(root, baseline, baseline_sha256, prior_companion, companion_review):
    snapshot = Snapshot()
    digest, read, rows = snapshot.digest, snapshot.read, snapshot.rows
    baseline_receipt = baseline / "receipt.json"
    if digest(baseline_receipt) != baseline_sha256:
        raise ValueError("Baseline receipt hash mismatch")
    metadata = read(baseline_receipt)
    expected_outputs = {
        MAPPING,
        SEMANTIC + "/current-review.json",
        SEMANTIC + "/assertion-dispositions.tsv",
        SEMANTIC + "/finding-dispositions.tsv",
        prior_companion,
    }
    if set(metadata["comparison_outputs"]) != expected_outputs:
        raise ValueError("Baseline must bind exactly the five compared outputs")
    for path, expected in metadata["comparison_outputs"].items():
        if digest(member(baseline, path)) != expected:
            raise ValueError(f"Archived comparison output changed: {path}")
    if prior_companion not in metadata["comparison_outputs"]:
        raise ValueError("Prior companion is not in the captured baseline")
    preservation_failures = {}
    for path, expected in metadata["preserve_bytes"].items():
        current = member(root, path)
        actual = digest(current) if current.is_file() else None
        if actual != expected:
            preservation_failures[path] = {"expected": expected, "actual": actual}

    old_mapping, new_mapping = read(baseline / MAPPING), read(root / MAPPING)
    old_semantic = read(baseline / SEMANTIC / "current-review.json")
    new_semantic = read(root / SEMANTIC / "current-review.json")
    old_companion = read(member(baseline, prior_companion))
    current_companion_path = member(root, companion_review)
    new_companion = read(current_companion_path)
    if old_companion["base_review"] != MAPPING or new_companion["base_review"] != MAPPING:
        raise ValueError("Companion must bind the compared mapping review")
    if old_companion["base_review_sha256"] != digest(baseline / MAPPING):
        raise ValueError("Prior companion does not bind the archived mapping review")
    if new_companion["base_review_sha256"] != digest(root / MAPPING):
        raise ValueError("Selected companion does not bind the current mapping review")
    # Verify each declared input separately, so an overlapping key cannot hide
    # a conflicting owner or claim hash through a dictionary merge.
    bindings = [
        new_companion["inputs"],
        new_companion["record_inputs"],
        {
            new_companion["claims_file"]: new_companion["claims_sha256"],
        },
    ]
    for group in bindings:
        for path, expected in group.items():
            if digest(member(root, path)) != expected:
                raise ValueError(f"Current companion input hash mismatch: {path}")

    comparisons = {
        "mapping": compare(
            old_mapping["decisions"], new_mapping["decisions"], "source_position", "disposition"
        ),
        "assertions": compare(
            rows(baseline / SEMANTIC / "assertion-dispositions.tsv"),
            rows(root / SEMANTIC / "assertion-dispositions.tsv"),
            "assertion_id",
            "resolution_status",
        ),
        "findings": compare(
            rows(baseline / SEMANTIC / "finding-dispositions.tsv"),
            rows(root / SEMANTIC / "finding-dispositions.tsv"),
            "finding_id",
            "resolution_status",
        ),
        "companion": compare(
            old_companion["decisions"], new_companion["decisions"], "claim_id", "disposition"
        ),
    }
    # This infrastructure-only run has no evidence-locator migration. Any such
    # future change requires a separate review, not an expanded ignore list.
    contract_keys = (old_companion.keys() | new_companion.keys()) - {
        "decisions",
        "base_review_sha256",
    }
    contract_changes = {
        key: {"before": old_companion.get(key), "after": new_companion.get(key)}
        for key in sorted(contract_keys)
        if key not in old_companion
        or key not in new_companion
        or old_companion[key] != new_companion[key]
    }
    summary_changes = {
        key: {"before": old_semantic[key], "after": new_semantic[key]}
        for key in (
            "release_verdict",
            "blocking_finding_ids",
            "blocking_assertion_ids",
            "evidence_gaps",
            "record_inputs",
        )
        if old_semantic[key] != new_semantic[key]
    }
    changed = bool(preservation_failures or contract_changes or summary_changes) or any(
        entry["added"] or entry["removed"] or entry["changed"] for entry in comparisons.values()
    )
    positive_changed = any(positive_changes(entry) for entry in comparisons.values())
    positive_changed |= bool(contract_changes) and any(
        row["disposition"] in POSITIVE for row in new_companion["decisions"]
    )
    result = {
        "status": "REQUIRES_REVIEW" if changed else "EXACT_DISPOSITION_AND_SOURCE_PRESERVATION",
        "scope": "All mapping, assertion, finding and explicitly selected companion decisions; captured source bytes",
        "baseline": metadata["base"],
        "baseline_receipt_sha256": baseline_sha256,
        "protected_files": len(metadata["preserve_bytes"]),
        "preservation_failures": preservation_failures,
        "comparisons": comparisons,
        "release_summary_changes": summary_changes,
        "companion_contract_changes": contract_changes,
        "current_companion": {"path": companion_review, "sha256": digest(current_companion_path)},
        "prior_companion": {
            "path": prior_companion,
            "sha256": digest(member(baseline, prior_companion)),
        },
        "verified_companion_dependency": {
            "path": MAPPING,
            "before_sha256": old_companion["base_review_sha256"],
            "after_sha256": new_companion["base_review_sha256"],
        },
        "scientific_approval_added": positive_changed,
        "approval_detection": "New or modified positive decisions, or changed companion contracts carrying positive decisions, require review",
        "native_companion_validation": "Required separately; this comparison does not confer scientific approval",
        "current_output_sha256": {
            path: digest(member(root, path))
            for path in metadata["comparison_outputs"]
            if path != prior_companion
        },
    }
    snapshot.verify()
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", required=True, type=Path)
    parser.add_argument("--baseline", required=True, type=Path)
    parser.add_argument("--baseline-receipt-sha256", required=True)
    parser.add_argument("--prior-companion", required=True)
    parser.add_argument("--companion-review", required=True)
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()
    try:
        result = assess(
            args.root,
            args.baseline,
            args.baseline_receipt_sha256,
            args.prior_companion,
            args.companion_review,
        )
        with args.output.open("x") as stream:
            json.dump(result, stream, indent=2)
            stream.write("\n")
    except (OSError, ValueError, KeyError, TypeError) as error:
        parser.exit(2, f"Comparison refused: {error}\n")
    print(
        json.dumps(
            {
                "status": result["status"],
                "scientific_approval_added": result["scientific_approval_added"],
                "current_companion": result["current_companion"],
                "output": str(args.output),
            },
            indent=2,
        )
    )
    return 1 if result["status"] == "REQUIRES_REVIEW" else 0


if __name__ == "__main__":
    raise SystemExit(main())
