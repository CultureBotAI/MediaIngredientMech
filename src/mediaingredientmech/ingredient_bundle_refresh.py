"""Create an immutable companion successor after proving the cohort unchanged.

The caller selects the historical Git commit and prior review explicitly. This
operation supplies no scientific approval and refuses cohort, contract, evidence
or semantic changes. It never updates a release selector automatically.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
from collections import Counter
from contextlib import ExitStack
from copy import deepcopy
from datetime import date
from pathlib import Path
from typing import BinaryIO

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
    safe_member,
)

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
    old_meta, old_fields, old_rows = _base_table(before[source])
    new_meta, new_fields, new_rows = _base_table(current[source])
    claims = read_json(before[prior["claims_file"]])["claims"]
    selected_old_decisions = []
    for claim in claims:
        if claim["kind"] != "mapping":
            continue
        row = {field: claim["payload"][field] for field in old_fields}
        if old_rows.count(row) != 1:
            raise ValueError("Selected original row is ambiguous")
        position = old_rows.index(row) + 1
        selected_old_decisions.append(
            next(d for d in old_base["decisions"] if d["source_position"] == position)
        )
    # Only the selected base decisions identify global evidence containers.
    # Other scope/claim evidence and every owner remain byte-immutable.
    evidence_containers = {d["review_evidence"] for d in selected_old_decisions}
    allowed = {prior["base_review"], source, *evidence_containers}
    changed = {p for p in before if before[p] != current[p]}
    if changed - allowed:
        raise ValueError(
            "Non-global input or owner changed: " + ", ".join(sorted(changed - allowed))
        )
    for decision in prior["decisions"]:
        entries = [
            read_json(sources[decision["review_evidence"]])["entries"][decision["evidence_key"]]
            for sources in (before, current)
        ]
        if entries[0] != entries[1]:
            raise ValueError("Companion scientific evidence changed")
    mutable_base = {"source_sha256", "inputs", "record_inputs", "decisions"}
    if {k: v for k, v in old_base.items() if k not in mutable_base} != {
        k: v for k, v in new_base.items() if k not in mutable_base
    }:
        raise ValueError("Original review scope or contract changed")
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
        "operation": "refresh_unchanged_companion_cohort",
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
    """Retain exclusive handles and refuse replaced output reservations."""
    validate_destinations([p for p, _ in outputs])
    with ExitStack() as stack:
        reserved: list[tuple[Path, BinaryIO, tuple[int, int]]] = []

        def still_owned(path, identity):
            try:
                actual = path.lstat()
            except FileNotFoundError:
                return False
            return (actual.st_dev, actual.st_ino) == identity

        def verify_reservations():
            for path, _, identity in reserved:
                if not still_owned(path, identity):
                    raise ValueError("Output reservation changed: " + str(path))

        try:
            for path, _ in outputs:
                handle = stack.enter_context(path.open("xb"))
                status = os.fstat(handle.fileno())
                reserved.append((path, handle, (status.st_dev, status.st_ino)))
            verify_snapshot()
            verify_reservations()
            for (_, handle, _), (_, content) in zip(reserved, outputs, strict=True):
                # Never reopen a pathname after reservation: even a concurrent
                # replacement cannot redirect this write to another inode.
                verify_reservations()
                handle.write(content)
                handle.flush()
            verify_reservations()
        except BaseException:
            # Keep handles open until cleanup finishes, so their inode identities
            # cannot be recycled. Preserve another writer's replacement paths.
            for path, _, identity in reserved:
                if still_owned(path, identity):
                    path.unlink()
            raise


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path.cwd())
    parser.add_argument(
        "--baseline", required=True, help="Git commit containing the prior review and its inputs"
    )
    parser.add_argument(
        "--prior-review",
        type=Path,
        required=True,
        help="Repository-relative preserved prior review",
    )
    parser.add_argument("--output", type=Path, required=True, help="New successor review path")
    parser.add_argument("--receipt", type=Path, required=True, help="New verification receipt path")
    parser.add_argument(
        "--prior-copy", type=Path, required=True, help="New exact prior-review copy path"
    )
    args = parser.parse_args(argv)
    root = args.root.resolve()
    destinations = [root / args.output, root / args.receipt, root / args.prior_copy]
    validate_destinations(destinations)
    prior_path = args.prior_review.as_posix()
    old_bytes = safe_member(root, prior_path).read_bytes()
    prior = read_json(old_bytes)
    baseline = (
        subprocess.check_output(
            ["git", "rev-parse", "--verify", "--end-of-options", args.baseline + "^{commit}"],
            cwd=root,
        )
        .decode()
        .strip()
    )

    def historical(name):
        safe_member(root, name)
        return subprocess.check_output(["git", "show", baseline + ":" + name], cwd=root)

    if historical(prior_path) != old_bytes:
        raise ValueError("Historical companion review changed")
    # Validate the entire current base review before considering the selected cohort.
    loaded = load_review(root, Path(prior["base_review"]))
    before = {name: historical(name) for name in source_names(prior)}
    current = {name: safe_member(root, name).read_bytes() for name in before}
    old_contracts = {name: historical(name) for name in CONTRACTS}
    new_contracts = {name: (root / name).read_bytes() for name in CONTRACTS}
    for name in (PROFILE_NAME, SCHEMA_NAME):
        if contract_resource(name) != new_contracts["src/mediaingredientmech/profiles/" + name]:
            raise ValueError("Loaded package differs from current schema/profile")
    successor, audit = verify_unchanged_cohort(prior, before, current, old_contracts, new_contracts)
    new_bytes = encode(successor)
    audit.update(
        {
            "historical_commit": baseline,
            "requested_baseline": args.baseline,
            "execution_head": subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=root)
            .decode()
            .strip(),
            "producer_sha256": content_sha256(Path(__file__).read_bytes()),
            "prior_review": prior_path,
            "prior_review_sha256": content_sha256(old_bytes),
            "successor_review": str(args.output),
            "successor_review_sha256": content_sha256(new_bytes),
            "current_full_base_review_validation": "PASS",
        }
    )
    snapshots = {root / p: content_sha256(b) for p, b in (current | new_contracts).items()}
    snapshots[root / prior_path] = content_sha256(old_bytes)
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
