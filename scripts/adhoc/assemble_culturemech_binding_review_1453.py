#!/usr/bin/env python3
"""Assemble explicitly authored #1453 source-binding proof, 2026-11-16.

Inputs: pinned prepared intake and complete independent eligible-case decisions.
Outputs: new review/evidence JSON and unchanged author decisions for native finalization.
Only an absent native supported canonical row produces a mechanical WITHHOLD;
eligible cases require an explicit payload-bound scientific disposition. No sends.
"""

import argparse
import json
from collections import Counter
from pathlib import Path

from mediaingredientmech.intake import culturemech as intake

ROOT = Path(__file__).resolve().parents[2]


def validate_coverage(decision, case):
    """Require exhaustive support review or actual blocking witnesses (#1465)."""
    payloads = {
        "descriptor": case["descriptors"],
        "change": case.get("change_payloads", {}),
        "held": case.get("held_payloads", {}),
    }
    inspected = {}
    for kind, members in payloads.items():
        values = decision[f"inspected_{kind}_sha256"]
        intake.require(
            isinstance(values, list)
            and all(isinstance(value, str) for value in values)
            and len(set(values)) == len(values)
            and set(values) <= set(members),
            "Inspected payload is not a unique case member",
        )
        inspected[kind] = set(values)
    if decision["disposition"] == "SUPPORTED":
        intake.require(
            all(inspected[kind] == set(members) for kind, members in payloads.items()),
            "Supported author payload review is incomplete",
        )
        return
    witnesses = decision.get("blocking_witnesses")
    intake.require(isinstance(witnesses, list) and witnesses, "WITHHOLD needs blocking witnesses")
    for witness in witnesses:
        intake.require(isinstance(witness, dict), "Invalid blocking witness")
        kind, sha = witness.get("payload_kind"), witness.get("sha256")
        intake.require(
            isinstance(kind, str)
            and isinstance(sha, str)
            and kind in payloads
            and sha in inspected[kind]
            and sha in payloads[kind],
            "Blocking witness is not an inspected case member",
        )
        payload = payloads[kind][sha]
        intake.require(intake.payload_sha256(payload) == sha, "Stale blocking witness hash")
        pointer, reason = witness.get("field_path"), witness.get("reason")
        intake.require(
            isinstance(pointer, str)
            and pointer.startswith("/")
            and isinstance(reason, str)
            and reason.strip(),
            "Blocking witness needs an exact field and concrete reason",
        )
        value = payload
        try:
            for token in pointer[1:].split("/"):
                if "~" in token.replace("~1", "").replace("~0", ""):
                    raise ValueError("Invalid JSON pointer escape")
                token = token.replace("~1", "/").replace("~0", "~")
                if isinstance(value, list):
                    if not token.isdecimal() or (len(token) > 1 and token.startswith("0")):
                        raise ValueError("Invalid JSON array index")
                    value = value[int(token)]
                else:
                    value = value[token]
        except (KeyError, TypeError, ValueError, IndexError) as exc:
            raise ValueError("Blocking witness field is absent") from exc


def assemble(source, pin, authors, output, *, root=ROOT):
    source, output, root = source.resolve(), output.resolve(), root.resolve()
    authors = [path.resolve() for path in authors]
    intake.require(output.is_relative_to(root), "Review output must remain in the repository")
    intake.output_preflight(output, [source, root / "data", root / "mappings", *authors])
    manifest, cases, _ = intake.verify_intake(source, pin, root)
    packet_pin = manifest["files"]["review-packet.json"]["sha256"]
    packet, _ = intake.read_json(source / "review-packet.json", packet_pin)
    intake.require(
        {case["case_id"]: case for case in packet["cases"]} == cases,
        "Packet changed during verification",
    )
    supplied, author_inputs = {}, {}
    for path in authors:
        review, actual = intake.read_json(path)
        intake.require(review["intake_sha256"] == pin, "Author reviewed another intake")
        author_inputs[path] = actual
        for decision in review["decisions"]:
            key = decision["case_id"]
            intake.require(key in cases and key not in supplied, "Unexpected/duplicate author case")
            case = cases[key]
            intake.require(
                bool(case["candidate"]["supported_canonical_rows"]),
                "Author case lacks native canonical eligibility",
            )
            intake.require(
                decision["row_sha256"] == intake.payload_sha256(case), "Stale author case"
            )
            intake.require(
                decision["disposition"] in {"SUPPORTED", "WITHHOLD"}
                and isinstance(decision["review_reason"], str)
                and decision["review_reason"].strip()
                and decision["evidence_locators"],
                "Missing explicit scientific disposition/evidence",
            )
            validate_coverage(decision, case)
            supplied[key] = decision
    eligible = {key for key, case in cases.items() if case["candidate"]["supported_canonical_rows"]}
    intake.require(set(supplied) == eligible, "Every eligible case needs an authored review")
    evidence_name = (output.relative_to(root) / "binding-evidence.json").as_posix()
    decisions, entries = [], {}
    for key, case in sorted(cases.items()):
        candidate = case["candidate"]
        owner = candidate.get("owner_record", "source/bundle/manifest.json")
        owner_sha = candidate.get("owner_record_sha256", manifest["source_manifest_sha256"])
        if key in supplied:
            authored = supplied[key]
            disposition, reason = authored["disposition"], authored["review_reason"]
            canonical = authored.get("canonical_row_sha256", "")
            if disposition == "SUPPORTED":
                intake.require(
                    not set(case["context"].get("held_fields", []))
                    & {"SOURCE_CLAIM", "IDENTITY_FORM"},
                    "Source identity/source-claim hold cannot be supported",
                )
                intake.require(
                    canonical
                    in {row["row_sha256"] for row in candidate["supported_canonical_rows"]},
                    "Authored support lacks a supported canonical row",
                )
            else:
                intake.require(not canonical, "Withheld author decision asserts a canonical row")
            locators = authored["evidence_locators"]
        else:
            disposition, canonical = "WITHHOLD", ""
            reason = (
                "Canonical eligibility gate: the pinned native review "
                + manifest["canonical_review_sha256"]
                + " contains no SUPPORTED exact own-identifier row for this source case's "
                + (
                    "unique candidate owner."
                    if len(candidate["owners"]) == 1
                    else "owner resolution."
                )
                + " Source-binding approval is therefore withheld; this does not assert ingredient absence, "
                "invalidate source quantities, or approve a different identity. Candidate classification: "
                + candidate["classification"]
                + "."
            )
            locators = [
                "review-packet.json case_id=" + key + " candidate.supported_canonical_rows",
                "intake.json#/canonical_review_sha256",
            ]
        decision = {
            "case_id": key,
            "row_sha256": intake.payload_sha256(case),
            "owner_record": owner,
            "disposition": disposition,
            "review_reason": reason,
            "review_evidence": evidence_name,
            "evidence_key": key,
        }
        if canonical:
            decision["canonical_row_sha256"] = canonical
        entries[key] = {
            **{
                field: decision[field]
                for field in ("row_sha256", "owner_record", "disposition", "review_reason")
            },
            "owner_record_sha256": owner_sha,
            "evidence_locators": locators,
            "intake_sha256": pin,
            "review_packet_sha256": packet_pin,
            "review_coverage": (
                {
                    field: supplied[key].get(field, [])
                    for field in (
                        "inspected_descriptor_sha256",
                        "inspected_change_sha256",
                        "inspected_held_sha256",
                        "blocking_witnesses",
                    )
                }
                if key in supplied
                else {"kind": "native_canonical_eligibility_gate"}
            ),
        }
        decisions.append(decision)
    output.parent.mkdir(parents=True, exist_ok=True)
    with intake.staging(output) as stage:
        inputs = {}
        for index, (path, expected) in enumerate(author_inputs.items()):
            data = path.read_bytes()
            intake.require(
                intake.hashlib.sha256(data).hexdigest() == expected["sha256"], "Author changed"
            )
            name = f"author-{index + 1}.json"
            (stage / name).write_bytes(data)
            inputs[(output.relative_to(root) / name).as_posix()] = expected["sha256"]
        intake.write_json(stage / "binding-evidence.json", {"entries": entries})
        inputs[evidence_name] = intake.fingerprint(stage / "binding-evidence.json")["sha256"]
        review = {
            "schema_version": 1,
            "intake_sha256": pin,
            "inputs": inputs,
            "decisions": decisions,
        }
        intake.write_json(stage / "binding-review.json", review)
        intake.write_json(
            stage / "summary.json",
            {
                "status": "ASSEMBLED_PENDING_NATIVE_FINALIZATION_AND_INDEPENDENT_REVIEW",
                "intake_sha256": pin,
                "review_packet_sha256": packet_pin,
                "canonical_review_sha256": manifest["canonical_review_sha256"],
                "authored_cases": len(supplied),
                "canonical_gate_withheld_cases": len(cases) - len(supplied),
                "dispositions": dict(Counter(item["disposition"] for item in decisions)),
                "helper_sha256": intake.fingerprint(Path(__file__))["sha256"],
                "files": {path.name: intake.fingerprint(path) for path in sorted(stage.iterdir())},
            },
        )
        final_manifest, final_cases, _ = intake.verify_intake(source, pin, root)
        intake.require(final_manifest == manifest and final_cases == cases, "Intake changed")
        intake.read_json(source / "review-packet.json", packet_pin)
        for path, expected in author_inputs.items():
            intake.require(
                intake.fingerprint(path) == expected, "Author changed before publication"
            )
    return review


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--intake", type=Path, required=True)
    parser.add_argument("--expected-intake-sha256", required=True)
    parser.add_argument("--author-review", type=Path, action="append", required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    assemble(args.intake, args.expected_intake_sha256, args.author_review, args.output)
    print(
        json.dumps(
            {"review_sha256": intake.fingerprint(args.output / "binding-review.json")["sha256"]}
        )
    )


if __name__ == "__main__":
    main()
