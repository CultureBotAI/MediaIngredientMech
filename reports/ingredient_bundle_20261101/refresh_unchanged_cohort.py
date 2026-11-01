"""Issue #1008: create a successor only when the reviewed cohort is unchanged.

This bounded migration preserves the historical review. It supplies no scientific
approval and deliberately refuses cohort, contract, evidence or semantic changes.
"""

from __future__ import annotations

import argparse
import json
import re
import subprocess
from collections import Counter
from copy import deepcopy
from datetime import date
from pathlib import Path

from mediaingredientmech.export.reviewed_sssom import load_review
from mediaingredientmech.ingredient_bundle_contract import (
    PROFILE_NAME,
    SCHEMA_NAME,
    _base_table,
    canonical_json,
    content_sha256,
    contract_resource,
    read_json,
    reviewed_products,
)

BASELINE = "4625afd492b6cf43e3b499d1425d2453d490009d"
PRIOR_REVIEW = "reports/ingredient_bundle_20260924/review.json"
SUCCESSOR = "reports/ingredient_bundle_20261101/review.json"
EVIDENCE = "reports/sssom_completion_20260921/mapping-evidence.json"
CONTRACTS = tuple("src/mediaingredientmech/profiles/" + n for n in (PROFILE_NAME, SCHEMA_NAME))
DATE_FIELDS = {"mapping_date", "mapping_set_version"}


def source_names(review):
    return {
        review["base_review"],
        review["claims_file"],
        *review["inputs"],
        *review["record_inputs"],
    }


def encode(value):
    return (json.dumps(value, indent=2, sort_keys=True, ensure_ascii=False) + "\n").encode()


def verify_unchanged_cohort(prior, before, current, old_contracts, new_contracts):
    """Return a dependency-only successor and complete selected-claim evidence."""
    if set(old_contracts) != set(CONTRACTS) or old_contracts != new_contracts:
        raise ValueError("Packaged schema/profile contract changed")
    if set(before) != source_names(prior) or set(current) != set(before):
        raise ValueError("Companion source coverage changed")
    _, old_loaded = reviewed_products(prior, before)
    old_base = read_json(before[prior["base_review"]])
    new_base = read_json(current[prior["base_review"]])
    source = old_base["source_sssom"]
    if new_base["source_sssom"] != source:
        raise ValueError("Original SSSOM source path changed")
    allowed = {prior["base_review"], source, EVIDENCE}
    changed = {p for p in before if before[p] != current[p]}
    if changed - allowed:
        raise ValueError(
            "Non-global input or owner changed: " + ", ".join(sorted(changed - allowed))
        )
    old_meta, old_fields, old_rows = _base_table(before[source])
    new_meta, new_fields, new_rows = _base_table(current[source])
    if old_fields != new_fields:
        raise ValueError("Original SSSOM column definitions changed")
    if {k: v for k, v in old_meta.items() if k not in DATE_FIELDS} != {
        k: v for k, v in new_meta.items() if k not in DATE_FIELDS
    }:
        raise ValueError("Original SSSOM semantic metadata changed")
    for metadata, rows in ((old_meta, old_rows), (new_meta, new_rows)):
        for key in DATE_FIELDS:
            value = str(metadata.get(key, ""))
            if not re.fullmatch(r"[0-9]{4}-[0-9]{2}-[0-9]{2}", value):
                raise ValueError("Invalid SSSOM date/version")
            date.fromisoformat(value)
        if metadata["mapping_date"] != metadata["mapping_set_version"]:
            raise ValueError("SSSOM date/version disagree")
        row_dates = []
        for row in rows:
            value = row.get("mapping_date", "")
            if not re.fullmatch(r"[0-9]{4}-[0-9]{2}-[0-9]{2}", value):
                raise ValueError("Invalid original row mapping_date")
            row_dates.append(date.fromisoformat(value))
        if date.fromisoformat(str(metadata["mapping_date"])) != max(row_dates):
            raise ValueError("SSSOM header date differs from newest row date (Rule G)")
    selected = []
    claims = read_json(before[prior["claims_file"]])["claims"]
    for claim in claims:
        if claim["kind"] != "mapping":
            continue
        row = {field: claim["payload"][field] for field in old_fields}
        if old_rows.count(row) != 1 or new_rows.count(row) != 1:
            raise ValueError("Selected complete original row changed or became ambiguous")
        positions = [old_rows.index(row) + 1, new_rows.index(row) + 1]
        decisions = [
            next(d for d in base["decisions"] if d["source_position"] == position)
            for base, position in zip((old_base, new_base), positions, strict=True)
        ]
        if decisions[0] != decisions[1] or decisions[1]["disposition"] != "SUPPORTED":
            raise ValueError("Selected original scientific decision changed")
        decision = decisions[0]
        entries = [
            read_json(sources[decision["review_evidence"]])["entries"][decision["evidence_key"]]
            for sources in (before, current)
        ]
        if entries[0] != entries[1]:
            raise ValueError("Selected original scientific evidence changed")
        selected.append(
            {
                "claim_id": claim["claim_id"],
                "original_row": row,
                "base_decision": decision,
                "base_evidence": entries[0],
            }
        )
    successor = deepcopy(prior)
    successor["base_review_sha256"] = content_sha256(current[prior["base_review"]])
    for name in allowed - {prior["base_review"]}:
        successor["inputs"][name] = content_sha256(current[name])
    _, new_loaded = reviewed_products(successor, current)
    if {k: v for k, v in old_loaded.items() if k != "metadata"} != {
        k: v for k, v in new_loaded.items() if k != "metadata"
    }:
        raise ValueError("Reconstructed companion payloads changed")
    audit = {
        "issue": "https://github.com/CultureBotAI/MediaIngredientMech/issues/1008",
        "scientific_approval_added": False,
        "claim_counts": dict(sorted(Counter(c["kind"] for c in claims).items())),
        "owner_hashes_unchanged": prior["record_inputs"],
        "claims_sha256_unchanged": prior["claims_sha256"],
        "companion_decisions_sha256_unchanged": content_sha256(canonical_json(prior["decisions"])),
        "selected_mapping_evidence_unchanged": selected,
        "semantic_metadata_unchanged": {k: v for k, v in old_meta.items() if k not in DATE_FIELDS},
        "columns_unchanged": old_fields,
        "header_date_changes": {
            k: {"before": str(old_meta[k]), "after": str(new_meta[k])} for k in sorted(DATE_FIELDS)
        },
        "contract_sha256_unchanged": {p: content_sha256(b) for p, b in old_contracts.items()},
        "dependency_changes": {
            p: {"before": content_sha256(before[p]), "after": content_sha256(current[p])}
            for p in sorted(changed)
        },
        "unchanged_input_sha256": {
            p: content_sha256(before[p]) for p in sorted(before.keys() - changed)
        },
        "native_historical_and_successor_payload_replay": "PASS; all claim payloads equal; only validated header dates differ",
    }
    return successor, audit


def validate_destinations(paths):
    """Validate ordered paths before any mapping can discard duplicate keys."""
    if len({p.resolve() for p in paths}) != len(paths):
        raise ValueError("Output paths collide")


def publish_new_files(outputs, verify_snapshot):
    """Reserve every output exclusively; never overwrite a prior review/receipt."""
    validate_destinations([p for p, _ in outputs])
    reserved = []
    try:
        for path, _ in outputs:
            with path.open("xb"):
                pass
            reserved.append(path)
        verify_snapshot()
        for path, content in outputs:
            path.write_bytes(content)
    except BaseException:
        for path in reserved:
            path.unlink()
        raise


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[2])
    parser.add_argument("--output", type=Path, default=Path(SUCCESSOR))
    parser.add_argument(
        "--receipt", type=Path, default=Path(SUCCESSOR).with_name("dependency-refresh.json")
    )
    parser.add_argument(
        "--prior-copy", type=Path, default=Path(SUCCESSOR).with_name("prior-review.json")
    )
    args = parser.parse_args()
    root = args.root.resolve()
    destinations = [root / args.output, root / args.receipt, root / args.prior_copy]
    validate_destinations(destinations)
    old_bytes = (root / PRIOR_REVIEW).read_bytes()
    prior = read_json(old_bytes)

    def historical(name):
        return subprocess.check_output(["git", "show", BASELINE + ":" + name], cwd=root)

    if historical(PRIOR_REVIEW) != old_bytes:
        raise ValueError("Historical companion review changed")
    # Validate the entire current base review before considering the selected cohort.
    loaded = load_review(root, Path(prior["base_review"]))
    before = {name: historical(name) for name in source_names(prior)}
    current = {name: (root / name).read_bytes() for name in before}
    old_contracts = {name: historical(name) for name in CONTRACTS}
    new_contracts = {name: (root / name).read_bytes() for name in CONTRACTS}
    for name in (PROFILE_NAME, SCHEMA_NAME):
        if contract_resource(name) != new_contracts["src/mediaingredientmech/profiles/" + name]:
            raise ValueError("Loaded package differs from current schema/profile")
    successor, audit = verify_unchanged_cohort(prior, before, current, old_contracts, new_contracts)
    new_bytes = encode(successor)
    audit.update(
        {
            "historical_commit": BASELINE,
            "execution_head": subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=root)
            .decode()
            .strip(),
            "prior_review": PRIOR_REVIEW,
            "prior_review_sha256": content_sha256(old_bytes),
            "successor_review": str(args.output),
            "successor_review_sha256": content_sha256(new_bytes),
            "current_full_base_review_validation": "PASS",
        }
    )
    snapshots = {root / p: content_sha256(b) for p, b in (current | new_contracts).items()}
    snapshots[root / PRIOR_REVIEW] = content_sha256(old_bytes)
    snapshots.update(loaded["input_snapshot"])
    outputs = list(zip(destinations, (new_bytes, encode(audit), old_bytes), strict=True))
    if any(p.resolve() in {s.resolve() for s in snapshots} for p, _ in outputs):
        raise ValueError("Output collides with a source input")

    def verify_snapshot():
        for path, expected in snapshots.items():
            if content_sha256(path.read_bytes()) != expected:
                raise ValueError("Input changed during verification: " + str(path))

    publish_new_files(outputs, verify_snapshot)
    print(
        json.dumps(
            {
                "successor": str(args.output),
                "sha256": content_sha256(new_bytes),
                "claim_counts": audit["claim_counts"],
                "owners": len(prior["record_inputs"]),
            }
        )
    )


if __name__ == "__main__":
    main()
