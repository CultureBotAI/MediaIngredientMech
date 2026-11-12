"""Append the bounded #1149/#1151 source receipt to retained policy provenance.

No policy decision, suppression, historical update, or scientific approval is
changed. The typed companion verifier independently replays this transition.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from mediaingredientmech.curate.apply_receipt import reserve_receipt_outputs
from mediaingredientmech.curate.publication_guard import (
    FrozenFile,
    check_reserved,
    finish_receipt,
    no_alias,
    publish_validated,
)
from mediaingredientmech.ingredient_bundle_contract import content_sha256, read_json
from mediaingredientmech.registry_correction_refresh import receipt_inventory
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


def prepare(root, generation_path, *, captured=None):
    if captured is None:
        captured = {}

    def read(name):
        path = root / name
        no_alias(path)
        if not path.resolve().is_relative_to(root):
            raise ValueError("Outside policy input")
        item = FrozenFile.capture(path)
        if name in captured and item != captured[name]:
            raise ValueError("Policy input changed during preparation")
        captured[name] = item
        return item.content

    raw = read(MANIFEST)
    if content_sha256(raw) != BEFORE:
        raise ValueError("Policy baseline differs; review a new transition")
    proof = verify_mapping_chain(root)
    for name, digest in proof["input_hashes"].items():
        if content_sha256(read(name)) != digest:
            raise ValueError("Native receipt evidence changed during preparation")
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
        if content_sha256(read(name)) != record["after_yaml_sha256"]:
            raise ValueError("Current owner differs from native receipt")
        doc["source_owner_sha256"][name] = record["after_yaml_sha256"]
    if content_sha256(read(SOURCE)) != receipt["after_sha256"]:
        raise ValueError("Canonical endpoint differs")
    doc["artifacts"][SOURCE] = receipt["after_sha256"]
    if UPDATE in doc:
        raise ValueError("Scoped update already present")
    generation_bytes = read(generation_path)
    generation = read_json(generation_bytes)
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
            "generation_manifest_sha256": content_sha256(generation_bytes),
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
    no_alias(args.root)
    no_alias(args.receipt_dir)
    root = args.root.absolute()
    captured = {}
    inventory = receipt_inventory(root)
    before, after = prepare(root, args.generation_manifest, captured=captured)
    target = captured.pop(MANIFEST)

    def recheck_inputs():
        if receipt_inventory(root) != inventory:
            raise ValueError("Native receipt inventory changed")
        for item in captured.values():
            item.verify()

    target.verify()
    recheck_inputs()
    print(
        json.dumps(
            {"before": content_sha256(before), "after": content_sha256(after), "approval": "NONE"}
        )
    )
    if args.apply:
        log = args.receipt_dir / "policy-manifest-write.json"
        backup_path = args.receipt_dir / "policy-manifest-before.json"
        with reserve_receipt_outputs(log, backup_paths=(backup_path,)) as (receipt, backup):

            def recheck():
                recheck_inputs()
                check_reserved(receipt, log)
                check_reserved(backup, backup_path)

            target.verify()
            recheck()
            backup.write(before)
            backup.flush()
            published = publish_validated(target, lambda staged: staged.write_bytes(after), recheck)

            def final_check():
                published.verify()
                recheck()

            finish_receipt(
                receipt,
                log,
                {
                    "before_sha256": content_sha256(before),
                    "after_sha256": content_sha256(after),
                    "approval": "NONE",
                },
                final_check,
            )


if __name__ == "__main__":
    main()
