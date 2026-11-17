#!/usr/bin/env python3
"""Prepare diagnostic owner groups for independent #1453 source review, 2026-11-16.

Inputs: immutable prepared intake plus its externally supplied manifest digest.
Outputs: new diagnostic cases TSV, owner groups JSON and provenance/count summary.
This helper does not decide SUPPORTED/WITHHOLD, mutate ingredients, or send data.
Embedded identifiers and owner-label differences are review flags, not chemistry.
"""

import argparse
import json
from collections import Counter, defaultdict
from pathlib import Path

import yaml

from mediaingredientmech.intake import culturemech as intake

ROOT = Path(__file__).resolve().parents[2]


def identifiers(value, path=""):
    """Retain every explicit nested identifier and its payload coordinate."""
    found = []
    if isinstance(value, dict):
        for key, item in value.items():
            pointer = path + "/" + key.replace("~", "~0").replace("/", "~1")
            if key in {"id", "identifier"} and isinstance(item, str):
                found.append({"path": pointer, "value": item})
            found.extend(identifiers(item, pointer))
    elif isinstance(value, list):
        for index, item in enumerate(value):
            found.extend(identifiers(item, path + "/" + str(index)))
    return found


def prepare(source, pin, output, *, root=ROOT):
    """Build navigation from one pinned snapshot; refuse drift before acceptance (#1461)."""
    source, output = source.resolve(), output.resolve()
    intake.output_preflight(output, [source, root / "data", root / "reports"])
    manifest, cases, _native = intake.verify_intake(source, pin, root)
    packet_pin = manifest["files"]["review-packet.json"]["sha256"]
    packet, _ = intake.read_json(source / "review-packet.json", packet_pin)
    intake.require(
        {case["case_id"]: case for case in packet["cases"]} == cases,
        "Review packet changed during initial verification",
    )
    rows, groups, flags = [], defaultdict(list), Counter()
    identity_profiles = {}
    for key, case in sorted(cases.items()):
        candidate = case["candidate"]
        owner = candidate.get("owner_record")
        owner_record = {}
        if owner:
            path = intake.relative(root, owner)
            raw = path.read_bytes()
            intake.require(
                intake.hashlib.sha256(raw).hexdigest() == candidate["owner_record_sha256"],
                "Candidate owner changed",
            )
            owner_record = yaml.load(raw, Loader=yaml.CSafeLoader)
        owner_id = candidate.get("mim_identifier", "")
        embedded = {
            digest: identifiers(descriptor)
            for digest, descriptor in case.get("descriptors", {}).items()
        }
        explicit_ids = {item["value"] for values in embedded.values() for item in values}
        namespace = owner_id.partition(":")[0] + ":" if ":" in owner_id else ""
        disagreements = sorted(
            value
            for value in explicit_ids
            if namespace and value.startswith(namespace) and value != owner_id
        )
        reasons = []
        if not candidate["supported_canonical_rows"]:
            reasons.append("NO_SUPPORTED_CANONICAL_ROW")
        if disagreements:
            reasons.append("EMBEDDED_IDENTIFIER_DISAGREEMENT")
        if len(candidate["owners"]) != 1:
            reasons.append("NO_UNIQUE_ACTIVE_OWNER")
        if (
            owner
            and case["context"]["preferred_term"].casefold()
            != str(owner_record.get("preferred_term", "")).casefold()
        ):
            reasons.append("OWNER_LABEL_DIFFERS")
        if candidate["classification"] == "SOURCE_IDENTIFIER_CONFLICT":
            reasons.append("SOURCE_RESOLVED_IDENTIFIER_CONFLICT")
        if set(case["context"].get("held_fields", [])) & {"SOURCE_CLAIM", "IDENTITY_FORM"}:
            reasons.append("HELD_IDENTITY_OR_SOURCE_CLAIM")
        if not reasons:
            reasons.append("MANUAL_PAYLOAD_FORM_REVIEW_REQUIRED")
        flags.update(reasons)
        row = {
            "case_id": key,
            "case_payload_sha256": intake.payload_sha256(case),
            "source_label": case["context"]["preferred_term"],
            "owner_record": owner or "",
            "owner_label": owner_record.get("preferred_term", ""),
            "owner_identifier": owner_id,
            "classification": candidate["classification"],
            "review_flags_json": json.dumps(reasons),
            "embedded_identifiers_json": json.dumps(sorted(explicit_ids)),
            "disagreeing_identifiers_json": json.dumps(disagreements),
            "positive_occurrences": case["positive_occurrences"],
            "context_only_mentions": case["context_only_mentions"],
            "held_source_mentions": case.get("held_source_mentions", 0),
        }
        rows.append(row)
        groups[owner or "UNRESOLVED"].append(
            {
                **row,
                "context": case["context"],
                "supported_canonical_rows": candidate["supported_canonical_rows"],
                "descriptor_identifiers": embedded,
                "descriptors": case.get("descriptors", {}),
                "change_payloads": case.get("change_payloads", {}),
                "held_payloads": case.get("held_payloads", {}),
                "source_coordinates": "Complete coordinates retained in the pinned intake review-packet.json case",
            }
        )
        if candidate["supported_canonical_rows"]:
            for descriptor_sha, descriptor in case.get("descriptors", {}).items():
                # Navigation only: concentration-qualified preparations can affect
                # identity. Final review must inspect the complete pinned descriptor.
                identity = {
                    field: value for field, value in descriptor.items() if field != "concentration"
                }
                profile_key = intake.payload_sha256({"owner": owner, "descriptor": identity})
                profile = identity_profiles.setdefault(
                    profile_key,
                    {
                        "owner_record": owner,
                        "owner_label": owner_record.get("preferred_term", ""),
                        "owner_identifier": owner_id,
                        "identity_descriptor": identity,
                        "case_bindings": [],
                    },
                )
                profile["case_bindings"].append(
                    {
                        "case_id": key,
                        "case_payload_sha256": row["case_payload_sha256"],
                        "complete_descriptor_sha256": descriptor_sha,
                        "review_flags": reasons,
                        "context": case["context"],
                    }
                )
    output.parent.mkdir(parents=True, exist_ok=True)
    with intake.staging(output) as stage:
        intake.write_tsv(stage / "cases.tsv", list(rows[0]), rows)
        intake.write_json(stage / "owner-groups.json", dict(sorted(groups.items())))
        intake.write_json(stage / "identity-review.json", identity_profiles)
        summary = {
            "status": "DIAGNOSTIC_REVIEW_PREPARATION_ONLY",
            "intake_sha256": pin,
            "review_packet_sha256": packet_pin,
            "source_manifest_sha256": manifest["source_manifest_sha256"],
            "canonical_review_sha256": manifest["canonical_review_sha256"],
            "cases": len(rows),
            "owner_groups": len(groups),
            "supported_canonical_identity_profiles": len(identity_profiles),
            "supported_canonical_owner_groups": len(
                {profile["owner_record"] for profile in identity_profiles.values()}
            ),
            "review_flags": dict(sorted(flags.items())),
            "limitations": [
                "No scientific decision or approval is generated.",
                "Matching namespace comparisons flag explicit identifier conflicts; other namespaces are retained for manual review.",
                "Absence of a diagnostic flag does not establish exact salt, hydrate, stereochemical, mixture or stock identity.",
                "Concentration-stripped profiles are navigation only; review complete descriptors and their preparation context before any identity decision.",
                "Current input may be a historical v2 planning canary; only the exact final intake pin can support final dispositions.",
            ],
            "products": {
                name: intake.fingerprint(stage / name)
                for name in ("cases.tsv", "owner-groups.json", "identity-review.json")
            },
            "helper_sha256": intake.fingerprint(Path(__file__))["sha256"],
        }
        intake.write_json(stage / "summary.json", summary)
        final_manifest, final_cases, _ = intake.verify_intake(source, pin, root)
        intake.require(
            final_manifest == manifest and final_cases == cases,
            "Intake changed during review preparation",
        )
        intake.read_json(source / "review-packet.json", packet_pin)
    return summary


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--intake", type=Path, required=True)
    parser.add_argument("--expected-intake-sha256", required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    summary = prepare(args.intake, args.expected_intake_sha256, args.output)
    print(
        json.dumps(
            {
                "output": str(args.output.resolve()),
                "summary_sha256": intake.fingerprint(args.output / "summary.json")["sha256"],
                "cases": summary["cases"],
                "review_flags": summary["review_flags"],
            }
        )
    )


if __name__ == "__main__":
    main()
