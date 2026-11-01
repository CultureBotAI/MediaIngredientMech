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
from dataclasses import dataclass
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
POLICY_MANIFEST = "mappings/ingredient_mappings.sssom.tsv.manifest.json"
POLICY_SIDECAR = "mappings/suppressed_aliases.tsv"
POLICY_BASELINE = "mappings/other_cross_record_baseline.tsv"


@dataclass(frozen=True)
class FormProjectionContext:
    """Explicit execution context, never a caller-supplied replay result."""

    root: Path
    baseline: str
    manifest_sha256: str


def _form_require(condition, message):
    if not condition:
        raise ValueError("Form projection: " + message)


def _form_sha(value):
    _form_require(isinstance(value, str) and re.fullmatch(r"[0-9a-f]{64}", value), "invalid SHA256")
    return value


def _form_member(root, name):
    path = safe_member(root, name)
    _form_require(not any(p.is_symlink() for p in (path, *path.parents)), "aliased proof input")
    return path


def verify_form_projection(prior, before, current, context):
    """Verify one typed, caller-pinned form update outside the selected cohort.

    Generation/source-receipt attribution is pinned, not independently replayed.
    Canonical and owner transitions are independently replayed from native receipts.
    The complete proof input inventory is returned for publication-time rechecking.
    """
    from mediaingredientmech.curie import mim_curie_for_stem
    from mediaingredientmech.validation.mapping_change_receipts import verify_mapping_chain

    _form_require(isinstance(context, FormProjectionContext), "explicit context and pin required")
    root = context.root.resolve()
    _form_require(re.fullmatch(r"[0-9a-f]{40}", context.baseline), "durable commit required")
    _form_require(
        content_sha256(current[POLICY_MANIFEST]) == _form_sha(context.manifest_sha256),
        "caller manifest pin differs",
    )
    old, new = (read_json(values[POLICY_MANIFEST]) for values in (before, current))
    fixed = {
        "schema_version",
        "policy_version",
        "approval",
        "scope",
        "decisions",
        "policy_evidence",
        "producer_revision",
        "generation_manifest_sha256",
        "generation_receipt_sha256",
        "source_receipt_sha256",
        "sssom_before_sha256",
        "baseline_before_sha256",
    }
    required = fixed | {"artifacts", "source_owner_sha256"}
    for doc in (old, new):
        _form_require(
            isinstance(doc, dict)
            and set(doc) in (required, required | {"form_projection_updates"}),
            "unknown manifest shape",
        )
        _form_require(
            type(doc["schema_version"]) is int
            and doc["schema_version"] == 1
            and doc["policy_version"] == "owned-name-policy-v1",
            "unknown policy/schema",
        )
    _form_require(all(old[k] == new[k] for k in fixed), "immutable policy/attribution changed")
    prefix, updates = old.get("form_projection_updates", []), new.get("form_projection_updates")
    _form_require(
        isinstance(prefix, list)
        and isinstance(updates, list)
        and len(updates) == len(prefix) + 1
        and updates[:-1] == prefix,
        "expected exactly one append with preserved history",
    )
    update = updates[-1]
    fields = {
        "issue",
        "scope",
        "approval",
        "prior_manifest_sha256",
        "source_record",
        "owner_before_sha256",
        "owner_after_sha256",
        "source_receipt",
        "source_receipt_sha256",
        "generation_manifest_sha256",
        "generation_receipt_sha256",
        "sssom_before_sha256",
        "sssom_after_sha256",
        "sidecar_sha256",
        "baseline_sha256",
    }
    _form_require(isinstance(update, dict) and set(update) == fields, "unknown update shape")
    for name, value in update.items():
        if name.endswith("_sha256"):
            _form_sha(value)
    _form_require(
        type(update["issue"]) is int
        and update["issue"] > 0
        and isinstance(update["scope"], str)
        and bool(update["scope"])
        and isinstance(update["approval"], str)
        and update["approval"].startswith("NONE:")
        and isinstance(update["source_receipt"], str)
        and bool(update["source_receipt"]),
        "invalid attribution fields",
    )
    _form_require(
        update["prior_manifest_sha256"] == content_sha256(before[POLICY_MANIFEST]),
        "prior raw manifest hash differs",
    )
    source = read_json(before[prior["base_review"]])["source_sssom"]
    artifacts = {source, POLICY_SIDECAR, POLICY_BASELINE}
    for doc, values in ((old, before), (new, current)):
        _form_require(
            isinstance(doc["artifacts"], dict) and set(doc["artifacts"]) == artifacts,
            "artifact membership differs",
        )
        _form_require(
            all(doc["artifacts"][p] == content_sha256(values[p]) for p in artifacts),
            "artifact bytes differ",
        )
    for path in artifacts | {POLICY_MANIFEST}:
        _form_require(
            _form_member(root, path).read_bytes() == current[path],
            "context current artifact differs",
        )
    _form_require(
        before[POLICY_SIDECAR] == current[POLICY_SIDECAR]
        and before[POLICY_BASELINE] == current[POLICY_BASELINE],
        "policy sidecar/baseline changed",
    )
    for field, path in (("sidecar_sha256", POLICY_SIDECAR), ("baseline_sha256", POLICY_BASELINE)):
        _form_require(update[field] == content_sha256(current[path]), "update policy hash differs")
    for field, values in (("sssom_before_sha256", before), ("sssom_after_sha256", current)):
        _form_require(update[field] == content_sha256(values[source]), "canonical endpoint differs")
    owner = update["source_record"]
    _form_require(
        isinstance(owner, str)
        and owner.startswith("data/ingredients/mapped/")
        and owner.endswith(".yaml")
        and owner not in prior["record_inputs"],
        "owner is invalid or belongs to companion cohort",
    )
    current_owner = _form_member(root, owner).read_bytes()

    def historical(path):
        _form_member(root, path)
        return subprocess.check_output(["git", "show", context.baseline + ":" + path], cwd=root)

    for path in (source, POLICY_MANIFEST):
        _form_require(historical(path) == before[path], "baseline input bytes differ")
    old_owner = historical(owner)
    _form_require(
        update["owner_before_sha256"] == content_sha256(old_owner)
        and update["owner_after_sha256"] == content_sha256(current_owner),
        "actual owner endpoint differs",
    )
    old_owners, new_owners = old["source_owner_sha256"], new["source_owner_sha256"]
    _form_require(
        isinstance(old_owners, dict)
        and isinstance(new_owners, dict)
        and set(old_owners) == set(new_owners)
        and owner in old_owners,
        "owner inventory differs",
    )
    for values in (old_owners, new_owners):
        for digest in values.values():
            _form_sha(digest)
    expected_owners = dict(old_owners)
    _form_require(expected_owners[owner] == update["owner_before_sha256"], "old owner map differs")
    expected_owners[owner] = update["owner_after_sha256"]
    _form_require(expected_owners == new_owners, "unaccounted owner change")
    proof = verify_mapping_chain(root)
    _form_require(
        proof["reviewed_sha256"] == update["sssom_after_sha256"], "current native chain differs"
    )
    matches = [r for r in proof["receipts"] if r["before_sha256"] == update["sssom_before_sha256"]]
    _form_require(
        len(matches) == 1 and matches[0] == proof["receipts"][-1],
        "update is not the exact final native suffix",
    )
    receipt = matches[0]
    _form_require(
        receipt["after_sha256"] == update["sssom_after_sha256"]
        and receipt["issue"]
        == f"https://github.com/CultureBotAI/MediaIngredientMech/issues/{update['issue']}",
        "native receipt endpoints/issue differ",
    )
    records = receipt["records"]
    _form_require(
        len(records) == 1
        and records[0]["source_record"] == owner
        and records[0]["before_yaml_sha256"] == update["owner_before_sha256"]
        and records[0]["after_yaml_sha256"] == update["owner_after_sha256"]
        and records[0]["shape"] == "hydrate_parent_predicate",
        "native owner transition differs",
    )
    subject = mim_curie_for_stem(Path(owner).stem)
    _form_require(
        receipt["touched_subjects"] == [subject]
        and all(
            row["subject_id"] == subject
            for change in receipt["changes"]
            for row in (change["before"], change["after"])
            if row is not None
        ),
        "unaccounted native subject change",
    )
    inputs = dict(proof["input_hashes"])
    inputs[owner] = content_sha256(current_owner)
    for path in artifacts | {POLICY_MANIFEST}:
        inputs[path] = content_sha256(current[path])
    for path in (
        "src/mediaingredientmech/ingredient_bundle_refresh.py",
        "src/mediaingredientmech/validation/mapping_change_receipts.py",
    ):
        inputs[path] = content_sha256(_form_member(root, path).read_bytes())
    return {
        "manifest_before_sha256": content_sha256(before[POLICY_MANIFEST]),
        "caller_pinned_manifest_sha256": context.manifest_sha256,
        "attribution_contract": "Exact caller-pinned attribution; generation/source receipts are not replayed here.",
        "native_transition_contract": "Full native receipt chain and durable-baseline/current owner bytes verified.",
        "baseline": context.baseline,
        "source_record": owner,
        "appended_update": update,
        "native_receipt": proof["receipt_paths"][-1],
        "native_receipt_sha256": proof["receipt_inputs"][proof["receipt_paths"][-1]],
        "receipt_paths": proof["receipt_paths"],
        "input_sha256": inputs,
        "scientific_approval_added": False,
    }


def source_names(review):
    return {
        review["base_review"],
        review["claims_file"],
        *review["inputs"],
        *review["record_inputs"],
    }


def encode(value):
    return (json.dumps(value, indent=2, sort_keys=True, ensure_ascii=False) + "\n").encode()


def verify_unchanged_cohort(
    prior, before, current, old_contracts, new_contracts, *, form_projection=None
):
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
    projection = None
    if form_projection is not None and POLICY_MANIFEST not in changed:
        raise ValueError("Form projection requested without a changed policy manifest")
    if POLICY_MANIFEST in changed and form_projection is not None:
        projection = verify_form_projection(prior, before, current, form_projection)
        allowed.add(POLICY_MANIFEST)
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
        # A source insertion/removal/reorder can move an unchanged selected row
        # and its evidence entry. Compare the scientific decision separately
        # from those locators, then resolve each locator in its own snapshot.
        location_fields = {"source_position", "evidence_key"}
        scientific_decisions = [
            {key: value for key, value in decision.items() if key not in location_fields}
            for decision in decisions
        ]
        if (
            scientific_decisions[0] != scientific_decisions[1]
            or decisions[1]["disposition"] != "SUPPORTED"
        ):
            raise ValueError("Selected original scientific decision changed")
        entries = [
            read_json(sources[decision["review_evidence"]])["entries"][decision["evidence_key"]]
            for sources, decision in zip((before, current), decisions, strict=True)
        ]
        if entries[0] != entries[1]:
            raise ValueError("Selected original scientific evidence changed")
        selected.append(
            {
                "claim_id": claim["claim_id"],
                "original_row": row,
                "base_decision": decisions[0],
                "base_decision_locations": {
                    name: {key: decision[key] for key in sorted(location_fields)}
                    for name, decision in zip(("before", "after"), decisions, strict=True)
                },
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
    if projection is not None:
        audit["form_projection"] = projection
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
    parser.add_argument(
        "--form-projection-manifest-sha256",
        help="Explicit reviewed successor manifest pin; native owner/receipt checks still apply",
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
    form_projection = (
        FormProjectionContext(root, baseline, args.form_projection_manifest_sha256)
        if args.form_projection_manifest_sha256 is not None
        else None
    )
    successor, audit = verify_unchanged_cohort(
        prior, before, current, old_contracts, new_contracts, form_projection=form_projection
    )
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
    if "form_projection" in audit:
        for path, expected in audit["form_projection"]["input_sha256"].items():
            member = _form_member(root, path)
            if member in snapshots and snapshots[member] != expected:
                raise ValueError("Projection proof conflicts with captured input: " + path)
            snapshots[member] = expected
    outputs = list(zip(destinations, (new_bytes, encode(audit), old_bytes), strict=True))
    if any(p.resolve() in {s.resolve() for s in snapshots} for p, _ in outputs):
        raise ValueError("Output collides with a source input")

    def verify_snapshot():
        if "form_projection" in audit:
            from mediaingredientmech.validation.mapping_change_receipts import receipt_paths

            if receipt_paths(root) != audit["form_projection"]["receipt_paths"]:
                raise ValueError("Projection receipt inventory changed during verification")
            for name in audit["form_projection"]["input_sha256"]:
                _form_member(root, name)
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
