"""2026-11-07 read-only structural accounting of frozen campaign outcomes.

Input: exact shard plus decisions/evidence/proposals and explicit capture roots.
Output: one new receipt. This auditor never supplies decisions, starts workers,
edits sources, contacts providers, or judges scientific adequacy. A single-case
canary is allowed only through an explicit --canary-case argument.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
from collections import Counter
from pathlib import Path, PurePosixPath


class InvalidOutcome(ValueError):
    """A structural accounting or immutable-reference failure."""


def require(value, message):
    if not value:
        raise InvalidOutcome(message)


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def case_digest(value):
    """Portable case hash: UTF-8, sorted keys, compact separators, no newline."""
    return hashlib.sha256(
        json.dumps(
            value, sort_keys=True, separators=(",", ":"), ensure_ascii=False, allow_nan=False
        ).encode("utf-8")
    ).hexdigest()


def reject_duplicate_keys(pairs):
    result = {}
    for key, value in pairs:
        require(key not in result, f"duplicate JSON key: {key}")
        result[key] = value
    return result


def read_json(path):
    return json.loads(path.read_text(encoding="utf-8"), object_pairs_hook=reject_duplicate_keys)


def string(value, label):
    require(isinstance(value, str) and value.strip(), f"{label}: nonempty string required")
    return value


def sha_string(value, label):
    require(
        isinstance(value, str) and re.fullmatch(r"[0-9a-f]{64}", value),
        f"{label}: lowercase SHA256 required",
    )
    return value


def unique_strings(value, label):
    require(isinstance(value, list), f"{label}: list required")
    for entry in value:
        string(entry, label)
    require(len(set(value)) == len(value), f"{label}: duplicate reference")
    return value


def safe_file(root, relative, label):
    string(relative, label)
    path = PurePosixPath(relative)
    require(
        not path.is_absolute() and ".." not in path.parts and "\\" not in relative,
        f"{label}: safe relative POSIX path required",
    )
    require(
        str(path) == relative and relative not in {"", "."},
        f"{label}: normalized relative path required",
    )
    current = root
    for part in path.parts:
        current = current / part
        require(not current.is_symlink(), f"{label}: symlink references are not admitted")
    require(
        current.is_file() and current.resolve().is_relative_to(root),
        f"{label}: regular file under the declared root required",
    )
    return current


def capture(value, roots, label, inputs):
    require(isinstance(value, dict), f"{label}: capture object required")
    require(value.get("root") in roots, f"{label}: unknown capture root")
    path = safe_file(roots[value["root"]], value.get("path"), label)
    expected = sha_string(value.get("sha256"), label)
    require(digest(path) == expected, f"{label}: capture hash differs")
    inputs[path] = expected
    return path


def audit(
    shard_path,
    decisions_path,
    evidence_path,
    proposals_path,
    artifact_root,
    source_root,
    *,
    canary_case=None,
    mim_root=None,
):
    paths = [
        Path(p).resolve(strict=True)
        for p in [shard_path, decisions_path, evidence_path, proposals_path]
    ]
    inputs = {path: digest(path) for path in paths}
    shard, decisions, evidence, proposals = map(read_json, paths)
    require(
        all(
            isinstance(value, dict) and value.get("schema_version") == 1
            for value in [shard, decisions, evidence, proposals]
        ),
        "schema_version 1 required",
    )
    roots = {
        "artifact": Path(artifact_root).resolve(strict=True),
        "source": Path(source_root).resolve(strict=True),
    }
    require(all(root.is_dir() for root in roots.values()), "capture roots must be directories")
    cases = shard.get("cases")
    require(isinstance(cases, list) and cases, "shard cases missing")
    case_by_id = {}
    for case in cases:
        require(isinstance(case, dict), "invalid shard case")
        key = string(case.get("case_id"), "input case_id")
        require(key not in case_by_id, "duplicate input case_id")
        case_by_id[key] = case
    expected = set(case_by_id)
    if canary_case is not None:
        require(canary_case in expected, "canary case is not assigned to shard")
        expected = {canary_case}
    phase = "canary" if canary_case is not None else "shard"
    require(decisions.get("phase") == phase, "phase must match explicit audit scope")
    require(decisions.get("shard_sha256") == inputs[paths[0]], "wrong shard hash")
    require(decisions.get("worker_slot") == shard.get("worker_slot"), "wrong worker slot")
    outcomes = decisions.get("decisions")
    require(isinstance(outcomes, list), "decisions list required")
    counts = Counter(string(row.get("case_id"), "decision case_id") for row in outcomes)
    require(set(counts) == expected, "missing or out-of-scope decision case_id")
    require(all(count == 1 for count in counts.values()), "duplicate decision case_id")

    evidence_rows = evidence.get("evidence")
    require(isinstance(evidence_rows, list), "evidence list required")
    evidence_by_id = {}
    evidence_kinds = {
        "primary_source",
        "source_snapshot",
        "ontology",
        "native_record_review",
        "independent_review",
        "unsuccessful_search",
        "local_validation",
    }
    for row in evidence_rows:
        require(isinstance(row, dict), "invalid evidence entry")
        key = string(row.get("evidence_id"), "evidence_id")
        require(key not in evidence_by_id, "duplicate evidence_id")
        require(row.get("kind") in evidence_kinds, "unknown evidence kind")
        if "case_ids" in row:
            claims = unique_strings(row["case_ids"], "evidence case_ids")
            require(set(claims) <= expected, "evidence claims an unassigned case")
        string(row.get("locator"), "evidence locator")
        string(row.get("supports_or_contradicts"), "evidence applicability")
        capture(row.get("capture"), roots, "evidence " + key, inputs)
        url = row.get("url")
        require(
            url is None or isinstance(url, str) and url.startswith(("https://", "http://")),
            "evidence URL must be HTTP(S) or null",
        )
        if url is not None:
            string(row.get("accessed_at"), "evidence access timestamp")
        if row.get("kind") in {"primary_source", "ontology"}:
            require(url is not None, "primary/ontology evidence URL required")
        evidence_by_id[key] = row

    def evidence_refs(value, label, required=True):
        refs = unique_strings(value, label)
        require(not required or refs, f"{label}: at least one evidence reference required")
        require(set(refs) <= set(evidence_by_id), f"{label}: dangling evidence reference")
        return refs

    proposal_rows = proposals.get("proposals")
    require(isinstance(proposal_rows, list), "proposals list required")
    proposal_by_id = {}
    for row in proposal_rows:
        require(isinstance(row, dict), "invalid proposal")
        key = string(row.get("proposal_id"), "proposal_id")
        require(key not in proposal_by_id, "duplicate proposal_id")
        case_ids = unique_strings(row.get("case_ids"), "proposal case_ids")
        require(case_ids and set(case_ids) <= expected, "proposal claims an unassigned case")
        string(row.get("description"), "proposal description")
        require(
            isinstance(row.get("owner_path"), str)
            and re.fullmatch(
                r"data/ingredients/(?:mapped|unmapped)/[^/]+\.yaml", row["owner_path"]
            ),
            "proposal owner path must be a native direct-child record",
        )
        require(row.get("kind") in {"edit_existing_owner", "new_owner"}, "invalid proposal kind")
        if row["kind"] == "new_owner":
            require(row.get("before_sha256") is None, "new owner has a before hash")
        else:
            sha_string(row.get("before_sha256"), "proposal before owner hash")
        capture(row.get("after_capture"), roots, "proposed owner payload " + key, inputs)
        evidence_refs(row.get("evidence_ids"), "proposal evidence")
        proposal_by_id[key] = row

    dispositions = {
        "existing_identity_or_alias",
        "new_distinct_ingredient_proposal",
        "supplied_form_correction",
        "broad_parent_relation_only",
        "stock_product_mixture_context",
        "malformed_or_nonchemical_token",
        "unresolved",
    }
    review_counts = Counter()
    proposal_backlinks = {key: set() for key in proposal_by_id}
    owner_refs_seen = {}
    for row in outcomes:
        key = row["case_id"]
        case = case_by_id[key]
        require(
            row.get("case_input_sha256") == case_digest(case), "input case hash differs: " + key
        )
        expected_source = {
            field: case[field]
            for field in ["source", "source_case_id", "source_label", "raw_source_label"]
        }
        require(row.get("source") == expected_source, "source identity/name differs: " + key)
        occurrence_ids = unique_strings(row.get("occurrence_ids"), "occurrence_ids")
        original_ids = [entry["occurrence_id"] for entry in case.get("occurrences", [])]
        require(
            set(occurrence_ids) == set(original_ids), "missing/changed occurrence reference: " + key
        )
        require(row.get("disposition") in dispositions, "invalid disposition")
        string(row.get("reasoning"), "case scientific reasoning")
        string(row.get("applicability"), "case evidence applicability")
        evidence_refs(row.get("evidence_ids"), "case evidence")
        missing = row.get("missing_requirement")
        if row["disposition"] == "unresolved":
            string(missing, "unresolved missing requirement")
        else:
            require(missing is None or isinstance(missing, str), "invalid missing requirement")
        refs = unique_strings(row.get("proposal_ids"), "case proposal_ids")
        require(set(refs) <= set(proposal_by_id), "dangling proposal reference")
        if refs:
            require(row.get("no_change_reason") is None, "proposal and no-change conflict")
        else:
            string(row.get("no_change_reason"), "explicit no-change reason")
        for proposal_id in refs:
            require(key in proposal_by_id[proposal_id]["case_ids"], "proposal backlink differs")
            proposal_backlinks[proposal_id].add(key)
        owners = row.get("owner_records")
        require(isinstance(owners, list), "owner_records list required")
        owner_paths = set()
        for owner in owners:
            require(isinstance(owner, dict), "invalid owner reference")
            require(mim_root is not None, "--mim-root required to verify owner references")
            relative = owner.get("path")
            require(
                isinstance(relative, str)
                and re.fullmatch(r"data/ingredients/(?:mapped|unmapped)/[^/]+\.yaml", relative),
                "owner path must be a native direct-child record",
            )
            require(relative not in owner_paths, "duplicate owner reference")
            owner_paths.add(relative)
            path = safe_file(Path(mim_root).resolve(strict=True), relative, "owner record")
            expected_sha = sha_string(owner.get("sha256"), "owner SHA256")
            require(digest(path) == expected_sha, "owner bytes differ")
            require(
                relative not in owner_refs_seen or owner_refs_seen[relative] == expected_sha,
                "conflicting owner hashes",
            )
            owner_refs_seen[relative] = expected_sha
            inputs[path] = expected_sha
        issues = unique_strings(row.get("issue_refs"), "issue_refs")
        require(
            all(
                re.fullmatch(
                    r"https://github\.com/[^/]+/[^/]+/issues/[0-9]+(?:#[-a-zA-Z0-9]+)?", url
                )
                for url in issues
            ),
            "invalid issue reference",
        )
        review = row.get("independent_review")
        require(
            isinstance(review, dict)
            and review.get("status") in {"pending", "findings_open", "complete"},
            "independent review state required",
        )
        review_refs = evidence_refs(
            review.get("evidence_ids"),
            "independent review evidence",
            required=review["status"] != "pending",
        )
        require(
            all(evidence_by_id[ref]["kind"] == "independent_review" for ref in review_refs),
            "independent review reference has wrong evidence kind",
        )
        review_counts[review["status"]] += 1
    for key, row in proposal_by_id.items():
        require(
            proposal_backlinks[key] == set(row["case_ids"]), "proposal has missing case backlinks"
        )
        if row["kind"] == "edit_existing_owner":
            require(
                owner_refs_seen.get(row["owner_path"]) == row["before_sha256"],
                "existing-owner proposal is not bound to verified owner bytes",
            )
    for path, expected_sha in inputs.items():
        require(
            path.is_file() and not path.is_symlink() and digest(path) == expected_sha,
            "input changed during audit: " + str(path),
        )
    return {
        "schema_version": 1,
        "structural_accounting": "PASS",
        "phase": phase,
        "worker_slot": shard["worker_slot"],
        "shard_sha256": inputs[paths[0]],
        "assigned_shard_case_count": len(case_by_id),
        "accounted_case_count": len(outcomes),
        "accounted_case_ids": sorted(expected),
        "out_of_scope_shard_case_ids": sorted(set(case_by_id) - expected),
        "proposal_count": len(proposal_by_id),
        "evidence_count": len(evidence_by_id),
        "independent_review_status_counts": dict(review_counts),
        "scientific_adequacy_or_approval_established": False,
        "limitations": [
            "Checks structure, references and exact case accounting only.",
            "Does not judge evidence quality, scientific reasoning, precise applicability or reviewer independence.",
            "Does not grant scientific mapping, role or publication approval.",
        ],
        "input_hashes": {str(path): value for path, value in sorted(inputs.items())},
        "auditor_sha256": digest(Path(__file__)),
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    for name in [
        "shard",
        "decisions",
        "evidence",
        "proposals",
        "artifact-root",
        "source-root",
        "output",
    ]:
        parser.add_argument("--" + name, type=Path, required=True)
    parser.add_argument("--canary-case")
    parser.add_argument("--mim-root", type=Path)
    args = parser.parse_args()
    require(not args.output.exists(), "new output receipt required")
    require(
        args.output.resolve().is_relative_to(args.artifact_root.resolve(strict=True)),
        "receipt must stay inside the explicit worker artifact root",
    )
    result = audit(
        args.shard,
        args.decisions,
        args.evidence,
        args.proposals,
        args.artifact_root,
        args.source_root,
        canary_case=args.canary_case,
        mim_root=args.mim_root,
    )
    with args.output.open("x", encoding="utf-8") as stream:
        json.dump(result, stream, indent=2, sort_keys=True)
        stream.write("\n")
    print(
        json.dumps(
            {
                key: result[key]
                for key in [
                    "structural_accounting",
                    "phase",
                    "accounted_case_count",
                    "assigned_shard_case_count",
                    "scientific_adequacy_or_approval_established",
                ]
            }
        )
    )


if __name__ == "__main__":
    main()
