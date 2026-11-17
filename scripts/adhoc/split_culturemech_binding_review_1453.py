#!/usr/bin/env python3
"""Make complete owner packets for independent #1453 review, 2026-11-16.

Inputs: independently pinned intake and diagnostic summary, current MIM owners.
Outputs: immutable owner packets, navigation and a deterministic two-part split.
No scientific decisions, ingredient edits, provider calls or approval generation.
"""

import argparse
import json
from collections import defaultdict
from pathlib import Path

import yaml

from mediaingredientmech.intake import culturemech as intake

ROOT = Path(__file__).resolve().parents[2]


def prepare(source, pin, profiles, profile_pin, output, *, root=ROOT):
    intake.output_preflight(output, [source, profiles, root / "data", root / "reports"])
    manifest, _ = intake.read_json(source / "intake.json", pin)
    summary, _ = intake.read_json(profiles / "summary.json", profile_pin)
    packet_pin = manifest["files"]["review-packet.json"]["sha256"]
    intake.require(
        summary["intake_sha256"] == pin and summary["review_packet_sha256"] == packet_pin,
        "Diagnostic summary belongs to another intake",
    )
    packet, _ = intake.read_json(source / "review-packet.json", packet_pin)
    groups = defaultdict(list)
    gated = []
    for case in packet["cases"]:
        if case["candidate"]["supported_canonical_rows"]:
            groups[case["candidate"]["owner_record"]].append(case)
        else:
            gated.append(
                {"case_id": case["case_id"], "payload_sha256": intake.payload_sha256(case)}
            )
    owners = sorted(groups)
    split = (len(owners) + 1) // 2
    nav, snapshots = [], {}
    output.parent.mkdir(parents=True, exist_ok=True)
    with intake.staging(output) as stage:
        for index, owner in enumerate(owners):
            raw = intake.relative(root, owner).read_bytes()
            sha = intake.hashlib.sha256(raw).hexdigest()
            intake.require(
                all(case["candidate"]["owner_record_sha256"] == sha for case in groups[owner]),
                "Owner changed since intake",
            )
            snapshots[owner] = {"sha256": sha, "bytes": len(raw)}
            record = yaml.load(raw, Loader=yaml.CSafeLoader)
            name = f"owner-{index:04d}.json"
            selected = sorted(groups[owner], key=lambda item: item["case_id"])
            intake.write_json(
                stage / name,
                {
                    "owner_record": owner,
                    "owner_record_sha256": sha,
                    "owner_payload": record,
                    "intake_sha256": pin,
                    "review_packet_sha256": packet_pin,
                    "cases": selected,
                    "case_payload_sha256": {
                        case["case_id"]: intake.payload_sha256(case) for case in selected
                    },
                },
            )
            nav.append(
                {
                    "owner_index": index,
                    "review_partition": "first" if index < split else "second",
                    "packet": name,
                    "owner_record": owner,
                    "owner_identifier": record.get("identifier", ""),
                    "owner_label": record.get("preferred_term", ""),
                    "cases": len(selected),
                    "source_labels_json": json.dumps(
                        sorted({case["context"]["preferred_term"] for case in selected})
                    ),
                }
            )
        intake.write_tsv(stage / "owners.tsv", list(nav[0]), nav)
        intake.write_json(stage / "canonical-gated-cases.json", gated)
        result = {
            "status": "PENDING_INDEPENDENT_SOURCE_BINDING_REVIEW",
            "intake_sha256": pin,
            "diagnostic_summary_sha256": profile_pin,
            "review_packet_sha256": packet_pin,
            "canonical_review_sha256": manifest["canonical_review_sha256"],
            "eligible_cases": sum(len(cases) for cases in groups.values()),
            "canonical_gated_cases": len(gated),
            "eligible_owners": len(owners),
            "split_rule": "Lexically sorted owner paths; ceil(N/2) owners first, remaining second.",
            "first_owner_count": split,
            "second_owner_count": len(owners) - split,
            "owner_inputs": snapshots,
            "files": {path.name: intake.fingerprint(path) for path in sorted(stage.iterdir())},
            "helper_sha256": intake.fingerprint(Path(__file__))["sha256"],
            "limitations": "Navigation does not approve cases. Read complete descriptors, preparation context and owner payload; canonical support alone cannot approve source identity.",
        }
        intake.write_json(stage / "summary.json", result)
        intake.read_json(source / "intake.json", pin)
        intake.read_json(source / "review-packet.json", packet_pin)
        intake.read_json(profiles / "summary.json", profile_pin)
        intake.check_snapshot(root, snapshots)
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--intake", required=True, type=Path)
    parser.add_argument("--expected-intake-sha256", required=True)
    parser.add_argument("--profiles", required=True, type=Path)
    parser.add_argument("--expected-profile-sha256", required=True)
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()
    result = prepare(
        args.intake.resolve(),
        args.expected_intake_sha256,
        args.profiles.resolve(),
        args.expected_profile_sha256,
        args.output.resolve(),
    )
    print(
        json.dumps(
            {
                "summary_sha256": intake.fingerprint(args.output / "summary.json")["sha256"],
                **{
                    key: result[key]
                    for key in ("eligible_cases", "canonical_gated_cases", "eligible_owners")
                },
            }
        )
    )


if __name__ == "__main__":
    main()
