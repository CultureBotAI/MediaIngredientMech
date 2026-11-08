"""Append the bounded #1149/#1151 source receipt to retained policy provenance.

No policy decision, suppression, historical update, or scientific approval is
changed. The typed companion verifier independently replays this transition.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from mediaingredientmech.curate.apply_receipt import reserve_receipt_outputs
from mediaingredientmech.ingredient_bundle_contract import content_sha256, read_json
from mediaingredientmech.source_alias_refresh import (
    ISSUE,
    MANIFEST,
    NOTE_OWNER,
    OWNER,
    SOURCE,
    UPDATE,
)
from mediaingredientmech.validation.mapping_change_receipts import verify_mapping_chain

BEFORE = "6b6fe48246bd43dd70499e82f508a7b7ea0fcd121bccafafa0217aae84a17778"


def prepare(root, generation_path):
    raw = (root / MANIFEST).read_bytes()
    if content_sha256(raw) != BEFORE:
        raise ValueError("Policy baseline differs; review a new transition")
    proof = verify_mapping_chain(root)
    receipt = proof["receipts"][-1]
    if receipt["sequence"] != 27 or receipt["issue"] != ISSUE:
        raise ValueError("Expected the exact scoped native receipt")
    doc = read_json(raw)
    if doc["artifacts"][SOURCE] != receipt["before_sha256"]:
        raise ValueError("Policy checkpoint does not join the new native receipt")
    owners = {x["source_record"]: x for x in receipt["records"]}
    if set(owners) != {OWNER, NOTE_OWNER}:
        raise ValueError("Unexpected receipt owner scope")
    for name, record in owners.items():
        if doc["source_owner_sha256"][name] != record["before_yaml_sha256"]:
            raise ValueError("Historical owner pin differs")
        if content_sha256((root / name).read_bytes()) != record["after_yaml_sha256"]:
            raise ValueError("Current owner differs from native receipt")
        doc["source_owner_sha256"][name] = record["after_yaml_sha256"]
    if content_sha256((root / SOURCE).read_bytes()) != receipt["after_sha256"]:
        raise ValueError("Canonical endpoint differs")
    doc["artifacts"][SOURCE] = receipt["after_sha256"]
    if UPDATE in doc:
        raise ValueError("Scoped update already present")
    generation = read_json((root / generation_path).read_bytes())
    if generation["external_sssom_validation"] != "passed":
        raise ValueError("Generation did not validate")
    receipt_path = proof["receipt_paths"][-1]
    doc[UPDATE] = [
        {
            "issue": ISSUE,
            "approval": "NONE: scientific review is separate",
            "prior_manifest_sha256": BEFORE,
            "mapping_receipt": receipt_path,
            "mapping_receipt_sha256": proof["receipt_inputs"][receipt_path],
            "generation_manifest": generation_path,
            "generation_manifest_sha256": content_sha256((root / generation_path).read_bytes()),
        }
    ]
    return raw, (json.dumps(doc, indent=2, sort_keys=True, ensure_ascii=False) + "\n").encode()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path.cwd())
    parser.add_argument("--generation-manifest", required=True)
    parser.add_argument("--receipt-dir", type=Path, required=True)
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args()
    root = args.root.resolve()
    for name in (MANIFEST, args.generation_manifest):
        p = root / name
        if not p.resolve().is_relative_to(root) or any(x.is_symlink() for x in (p, *p.parents)):
            raise ValueError("Aliased/outside policy input")
    if any(x.is_symlink() for x in (args.receipt_dir, *args.receipt_dir.parents)):
        raise ValueError("Aliased receipt destination")
    before, after = prepare(root, args.generation_manifest)
    print(
        json.dumps(
            {"before": content_sha256(before), "after": content_sha256(after), "approval": "NONE"}
        )
    )
    if args.apply:
        log = args.receipt_dir / "policy-manifest-write.json"
        backup_path = args.receipt_dir / "policy-manifest-before.json"
        with reserve_receipt_outputs(log, backup_paths=(backup_path,)) as (receipt, backup):
            current_before, current_after = prepare(root, args.generation_manifest)
            if (current_before, current_after) != (before, after):
                raise ValueError("Policy inputs changed during preflight")
            backup.write(before)
            backup.flush()
            (root / MANIFEST).write_bytes(after)
            receipt.write(
                json.dumps(
                    {
                        "before_sha256": content_sha256(before),
                        "after_sha256": content_sha256(after),
                        "approval": "NONE",
                    }
                )
                + "\n"
            )


if __name__ == "__main__":
    main()
