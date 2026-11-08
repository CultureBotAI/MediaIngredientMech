"""2026-11-07 private coordinator accounting; no integration or scientific approval.

Read exact frozen queue/shards and explicitly selected active worker bundles.
Reuse the unchanged worker outcome auditor. Write a new coordinator report only.
Partial worker files remain incomplete; historical evidence is not another claim.
"""

from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import re
from collections import Counter, defaultdict
from pathlib import Path

AUDITOR_SHA256 = "3bde4d7fa3aca41c6962a7c61b15f9709b98acdbbe936cdb498b3bca68600fad"
CASE_COUNT = 1879
SLOTS = set(range(1, 11))
OWNER_PATTERN = r"data/ingredients/(?:mapped|unmapped)/[^/]+\.yaml"


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def require(condition, message):
    if not condition:
        raise ValueError(message)


def load_auditor():
    path = Path(__file__).with_name("audit_worker_outcomes_v1.py")
    require(digest(path) == AUDITOR_SHA256, "existing worker auditor pin differs")
    spec = importlib.util.spec_from_file_location("unchanged_worker_auditor", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module, path


def declared_path_roles(bundle, decisions, evidence, proposals):
    """#1161: retain declared roots/relative roles before native consumption."""
    roles = []

    def remember(role, reference, root_key, relative, sha256):
        declared = Path(bundle[root_key]).absolute()
        roles.append(
            {
                "bundle_id": bundle["bundle_id"],
                "role": role,
                "reference_id": reference,
                "declared_root": str(declared),
                "resolved_root": str(declared.resolve(strict=True)),
                "relative_path": relative,
                "sha256": sha256,
            }
        )

    def remember_capture(role, reference, capture):
        root_key = {"artifact": "artifact_root", "source": "source_root"}[capture["root"]]
        remember(role, reference, root_key, capture["path"], capture["sha256"])

    for row in evidence["evidence"]:
        remember_capture("evidence", row["evidence_id"], row["capture"])
    for row in proposals:
        remember_capture("proposal", row["proposal_id"], row["after_capture"])
    for row in decisions["decisions"]:
        for owner in row["owner_records"]:
            remember("worker_owner", row["case_id"], "mim_root", owner["path"], owner["sha256"])
    return roles


def account(baseline_path, baseline_sha256, bundles_path, current_mim_root):
    native, auditor_path = load_auditor()
    helper_path = Path(__file__).resolve()
    inputs = {auditor_path.resolve(): AUDITOR_SHA256, helper_path: digest(helper_path)}

    def read(path, expected=None):
        path = Path(path).resolve(strict=True)
        raw = path.read_bytes()
        actual = hashlib.sha256(raw).hexdigest()
        require(expected is None or actual == expected, "input hash differs: " + str(path))
        require(path not in inputs or inputs[path] == actual, "input changed during reads")
        inputs[path] = actual
        return json.loads(raw, object_pairs_hook=native.reject_duplicate_keys)

    baseline = read(baseline_path, baseline_sha256)
    config = read(bundles_path)
    require(
        config.get("schema_version") == 1 and isinstance(config.get("bundles"), list),
        "explicit bundles configuration required",
    )
    queue = baseline["queue"]
    cases = read(Path(queue["root"]) / "union-ledger.json", queue["union_sha256"])
    require(isinstance(cases, list) and len(cases) == CASE_COUNT, "full 1879-case queue required")
    case_by_id = {row["case_id"]: row for row in cases}
    require(len(case_by_id) == len(cases), "duplicate immutable queue case_id")
    require(set(queue["shards"]) == {str(slot) for slot in SLOTS}, "all ten shard pins required")
    assigned = {}
    shard_paths = {}
    shard_cases = {}
    for slot in sorted(SLOTS):
        pin = queue["shards"][str(slot)]
        shard_paths[slot] = Path(pin["path"]).resolve(strict=True)
        shard = read(shard_paths[slot], pin["sha256"])
        require(shard.get("worker_slot") == slot, "shard slot differs")
        shard_cases[slot] = set()
        for case in shard["cases"]:
            key = case["case_id"]
            require(key in case_by_id and case == case_by_id[key], "shard/union payload differs")
            require(key not in assigned, "immutable shards overlap")
            assigned[key] = slot
            shard_cases[slot].add(key)
    require(set(assigned) == set(case_by_id), "immutable shards omit cases")
    current_root = Path(current_mim_root).resolve(strict=True)
    require(current_root.is_dir(), "current MIM root is not a directory")
    observations = []
    consumed_path_roles = []
    claims = defaultdict(list)
    cross_shard = []
    unknown = []
    source_errors = []
    owner_claims = defaultdict(list)
    proposal_claims = defaultdict(list)
    malformed_owner_claims = []
    validated = set()
    complete_slots = set()
    seen_bundle_ids = set()
    review_states = Counter()
    for bundle in config["bundles"]:
        key = native.string(bundle.get("bundle_id"), "bundle_id")
        require(key not in seen_bundle_ids, "duplicate bundle_id")
        seen_bundle_ids.add(key)
        slot = bundle.get("worker_slot")
        require(type(slot) is int and slot in SLOTS, "bundle worker slot invalid")
        result = {
            "bundle_id": key,
            "worker_slot": slot,
            "strict_audit": "NOT_RUN",
            "state": "INCOMPLETE",
            "claimed_case_ids": [],
        }
        observations.append(result)
        missing = [
            name
            for name in ["decisions", "evidence", "proposals"]
            if not Path(bundle[name]).is_file()
        ]
        if missing:
            result["missing_outputs"] = missing
        if "decisions" in missing:
            continue
        try:
            decisions = read(bundle["decisions"])
            if "evidence" not in missing:
                evidence = read(bundle["evidence"])
            proposal_rows = []
            if "proposals" not in missing:
                proposals = read(bundle["proposals"])
                require(isinstance(proposals.get("proposals"), list), "proposal list missing")
                proposal_rows = proposals["proposals"]
            require(isinstance(decisions.get("decisions"), list), "decision list missing")
        except (OSError, ValueError, TypeError, KeyError) as exc:
            result.update(state="INVALID", error=str(exc))
            continue
        result["phase"] = decisions.get("phase")
        result["envelope_matches_slot_and_shard"] = (
            decisions.get("worker_slot") == slot
            and decisions.get("shard_sha256") == queue["shards"][str(slot)]["sha256"]
        )
        for row in decisions["decisions"]:
            if not isinstance(row, dict) or not isinstance(row.get("case_id"), str):
                source_errors.append({"bundle_id": key, "error": "malformed decision case_id"})
                continue
            case_id = row["case_id"]
            claim = {"bundle_id": key, "worker_slot": slot, "case_id": case_id}
            claims[case_id].append(claim)
            result["claimed_case_ids"].append(case_id)
            if case_id not in case_by_id:
                unknown.append(claim)
                continue
            if assigned[case_id] != slot:
                cross_shard.append({**claim, "assigned_worker_slot": assigned[case_id]})
            original = case_by_id[case_id]
            expected_source = {
                field: original[field]
                for field in ["source", "source_case_id", "source_label", "raw_source_label"]
            }
            expected_occurrences = {
                item["occurrence_id"] for item in original.get("occurrences", [])
            }
            raw_occurrences = row.get("occurrence_ids")
            occurrence_ok = (
                isinstance(raw_occurrences, list)
                and all(isinstance(x, str) for x in raw_occurrences)
                and len(raw_occurrences) == len(set(raw_occurrences))
                and set(raw_occurrences) == expected_occurrences
            )
            if (
                row.get("case_input_sha256") != native.case_digest(original)
                or row.get("source") != expected_source
                or not occurrence_ok
            ):
                source_errors.append(
                    {**claim, "error": "case digest/source fields/occurrence references differ"}
                )
            for owner in (
                row.get("owner_records", []) if isinstance(row.get("owner_records"), list) else []
            ):
                if isinstance(owner, dict):
                    if isinstance(owner.get("path"), str):
                        owner_claims[owner["path"]].append(
                            {**claim, "before_sha256": owner.get("sha256")}
                        )
                    else:
                        malformed_owner_claims.append(
                            {**claim, "owner_path": owner.get("path"), "kind": "INVALID_OWNER_PATH"}
                        )
        for proposal in proposal_rows:
            if isinstance(proposal, dict):
                if not isinstance(proposal.get("owner_path"), str):
                    malformed_owner_claims.append(
                        {
                            "bundle_id": key,
                            "owner_path": proposal.get("owner_path"),
                            "kind": "INVALID_OWNER_PATH",
                        }
                    )
                    continue
                capture = proposal.get("after_capture")
                proposal_claims[proposal.get("owner_path")].append(
                    {
                        "bundle_id": key,
                        "worker_slot": slot,
                        "proposal_id": proposal.get("proposal_id"),
                        "case_ids": proposal.get("case_ids"),
                        "kind": proposal.get("kind"),
                        "before_sha256": proposal.get("before_sha256"),
                        "declared_after_sha256": (
                            capture.get("sha256") if isinstance(capture, dict) else None
                        ),
                    }
                )
        if missing:
            # Available decisions are raw claims only; absent outputs never enter
            # the native auditor and are never replaced with synthetic payloads.
            continue
        try:
            roles = declared_path_roles(bundle, decisions, evidence, proposal_rows)
            audit = native.audit(
                shard_paths[slot],
                bundle["decisions"],
                bundle["evidence"],
                bundle["proposals"],
                bundle["artifact_root"],
                bundle["source_root"],
                canary_case=bundle.get("canary_case"),
                mim_root=bundle.get("mim_root"),
            )
            for path, value in audit["input_hashes"].items():
                path = Path(path)
                require(
                    path not in inputs or inputs[path] == value,
                    "worker input changed between accounting and strict audit",
                )
                inputs[path] = value
            for role in roles:
                path = Path(role["resolved_root"]) / role["relative_path"]
                require(
                    audit["input_hashes"].get(str(path)) == role["sha256"],
                    "declared input role differs from native consumption",
                )
            consumed_path_roles.extend(roles)
            result.update(
                strict_audit="PASS",
                state="CANARY_ONLY" if audit["phase"] == "canary" else "FULL_SHARD_STRUCTURAL_PASS",
                audit=audit,
            )
            validated.update(audit["accounted_case_ids"])
            review_states.update(audit["independent_review_status_counts"])
            if audit["phase"] == "shard":
                complete_slots.add(slot)
        except (OSError, ValueError, TypeError, KeyError, AttributeError) as exc:
            result.update(strict_audit="FAIL", error=str(exc))
            if not set(result["claimed_case_ids"]) < shard_cases[slot]:
                result["state"] = "INVALID"

    owner_conflicts = list(malformed_owner_claims)
    current_owners = {}
    current_missing = set()
    for path in sorted(set(owner_claims) | set(proposal_claims), key=str):
        refs = owner_claims.get(path, [])
        proposals_for_owner = proposal_claims.get(path, [])
        if not isinstance(path, str) or re.fullmatch(OWNER_PATTERN, path) is None:
            owner_conflicts.append({"owner_path": path, "kind": "INVALID_OWNER_PATH"})
            continue
        current_path = current_root / path
        current_sha = None
        if current_path.exists() or current_path.is_symlink():
            try:
                current_path = native.safe_file(current_root, path, "coordinator current owner")
                current_sha = digest(current_path)
                if current_path in inputs and inputs[current_path] != current_sha:
                    owner_conflicts.append(
                        {"owner_path": path, "kind": "OWNER_CHANGED_DURING_ACCOUNTING"}
                    )
                else:
                    inputs[current_path] = current_sha
            except (OSError, ValueError) as exc:
                owner_conflicts.append(
                    {"owner_path": path, "kind": "UNSAFE_CURRENT_OWNER", "error": str(exc)}
                )
        else:
            current_missing.add(current_path)
        current_owners[path] = current_sha
        hashes = {
            entry["before_sha256"] for entry in refs if isinstance(entry["before_sha256"], str)
        }
        hashes.update(
            entry["before_sha256"]
            for entry in proposals_for_owner
            if entry["kind"] == "edit_existing_owner" and isinstance(entry["before_sha256"], str)
        )
        if len(hashes) > 1:
            owner_conflicts.append(
                {
                    "owner_path": path,
                    "kind": "CONFLICTING_BEFORE_HASHES",
                    "claimed_hashes": sorted(hashes),
                }
            )
        for value in sorted(hashes):
            if value != current_sha:
                owner_conflicts.append(
                    {
                        "owner_path": path,
                        "kind": "STALE_OR_MISSING_CURRENT_OWNER",
                        "claimed_before_sha256": value,
                        "current_sha256": current_sha,
                    }
                )
        if current_sha is not None and any(
            entry["kind"] == "new_owner" for entry in proposals_for_owner
        ):
            owner_conflicts.append({"owner_path": path, "kind": "NEW_OWNER_PATH_ALREADY_EXISTS"})
        after = {
            entry["declared_after_sha256"]
            for entry in proposals_for_owner
            if isinstance(entry["declared_after_sha256"], str)
        }
        if len(after) > 1:
            owner_conflicts.append(
                {
                    "owner_path": path,
                    "kind": "DIVERGENT_PROPOSED_BYTES_REQUIRE_COORDINATION",
                    "declared_after_sha256": sorted(after),
                }
            )
    duplicates = {key: values for key, values in claims.items() if len(values) > 1}
    validated -= set(duplicates)
    changed_inputs = [
        str(path) for path, value in inputs.items() if not path.is_file() or digest(path) != value
    ]
    changed_inputs.extend(
        str(path) for path in current_missing if path.exists() or path.is_symlink()
    )
    path_role_errors = []
    for role in consumed_path_roles:
        root = Path(role["resolved_root"])
        path = root / role["relative_path"]
        try:
            require(
                Path(role["declared_root"]).resolve(strict=True) == root,
                "declared root binding changed after native audit",
            )
            checked = native.safe_file(root, role["relative_path"], role["role"] + " final check")
            require(digest(checked) == role["sha256"], "role bytes changed after native audit")
        except (OSError, ValueError, RuntimeError) as exc:
            path_role_errors.append({**role, "error": str(exc)})
            changed_inputs.append(str(path))
    for path, value in current_owners.items():
        if value is not None:
            try:
                native.safe_file(current_root, path, "coordinator current owner final check")
            except (OSError, ValueError):
                changed_inputs.append(str(current_root / path))
    changed_inputs = sorted(set(changed_inputs))
    structural_complete = (
        complete_slots == SLOTS
        and validated == set(case_by_id)
        and not duplicates
        and not unknown
        and not cross_shard
        and not source_errors
        and not owner_conflicts
        and not changed_inputs
        and all(row["strict_audit"] == "PASS" for row in observations)
    )
    literal_names = {row["source_label"] for row in cases}
    return {
        "schema_version": 1,
        "scope": {
            "baseline_path": str(Path(baseline_path).resolve()),
            "baseline_sha256": baseline_sha256,
            "bundles_path": str(Path(bundles_path).resolve()),
            "current_mim_root": str(current_root),
            "owner_comparison": "pre-integration acceptance against explicitly selected current bytes",
        },
        "structural_inventory_complete": structural_complete,
        "campaign_complete_or_scientific_approval": False,
        "counts": {
            "source_cases": len(cases),
            "distinct_literal_source_labels_including_blank": len(literal_names),
            "blank_source_label_cases": sum(not row["source_label"] for row in cases),
            "observed_claims": sum(map(len, claims.values())),
            "unique_claimed_known_cases": len(set(claims) & set(case_by_id)),
            "fully_audited_unique_cases_without_duplicates": len(validated),
            "full_shards_passing_strict_audit": len(complete_slots),
            "distinct_referenced_owner_paths": len(owner_claims),
            "distinct_proposed_owner_paths": len(proposal_claims),
        },
        "source_case_counts": dict(Counter(row["source"] for row in cases)),
        "missing_case_ids": sorted(set(case_by_id) - set(claims)),
        "not_fully_audited_case_ids": sorted(set(case_by_id) - validated),
        "workers_without_full_shard_pass": sorted(SLOTS - complete_slots),
        "duplicate_case_claims": duplicates,
        "cross_shard_claims": cross_shard,
        "unknown_case_claims": unknown,
        "source_binding_errors": source_errors,
        "owner_conflicts": owner_conflicts,
        "owner_claims": dict(owner_claims),
        "proposal_claims": dict(proposal_claims),
        "current_owner_hashes": current_owners,
        "reported_independent_review_states_from_strictly_valid_bundles": dict(review_states),
        "bundles": observations,
        "consumed_path_roles": consumed_path_roles,
        "path_role_errors": path_role_errors,
        "inputs_changed_during_audit": changed_inputs,
        "input_sha256": {str(path): value for path, value in sorted(inputs.items())},
        "auditor_sha256": AUDITOR_SHA256,
        "coordinator_helper_sha256": inputs[helper_path],
        "limitations": [
            "Names and owner paths are not counts of distinct chemical identities.",
            "Strict structural PASS does not establish scientific review or approval.",
            "Partial shards are never relabeled as canaries or counted complete.",
            "Owner conflicts require coordinator review; no winner or merged payload is selected.",
            "This is a read-only observation of explicitly supplied active bundles, not a worker ledger update.",
        ],
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    for name in ["baseline", "bundles", "current-mim-root", "output"]:
        parser.add_argument("--" + name, type=Path, required=True)
    parser.add_argument("--baseline-sha256", required=True)
    args = parser.parse_args()
    allowed = Path(__file__).resolve().parents[1] / "preflight/campaign-accounting-v1"
    require(
        args.output.resolve().is_relative_to(allowed),
        "output must stay in coordinator private accounting directory",
    )
    require(not args.output.exists(), "new immutable report path required")
    result = account(args.baseline, args.baseline_sha256, args.bundles, args.current_mim_root)
    with args.output.open("x") as stream:
        json.dump(result, stream, indent=2, sort_keys=True)
        stream.write("\n")
    print(
        json.dumps(
            {
                "structural_inventory_complete": result["structural_inventory_complete"],
                "campaign_complete_or_scientific_approval": False,
                "counts": result["counts"],
            }
        )
    )


if __name__ == "__main__":
    main()
