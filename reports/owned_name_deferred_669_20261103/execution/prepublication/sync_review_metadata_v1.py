"""Exact native endpoint/selector synchronization after verified receipt26."""
from __future__ import annotations

import argparse
import hashlib
import json
import stat
from pathlib import Path
import subprocess
import sys

D = Path(__file__).resolve().parent
W = D.parent / "step8-aliases"
REPORT = "reports/owned_name_deferred_669_20261103"
BASE = "0ee56c11a2894ed50a476b331d56297be0a3ee12"
CANONICAL = "mappings/ingredient_mappings.sssom.tsv"
OLD = "d3030e6385a2659a0dbd2c64ad5581568eecd9c10023f4a58de667e8050f20ef"
NEW = "d5f76fc404967477903fafc79eaba86ecfef9e2c391926ec08c3c1af4a5220b6"
RECEIPT = "reports/sssom_completion_20260921/mapping_changes/issue669-deferred-owned-aliases.json"
RECEIPT_SHA = "121b8d6026d6af9a6692966b024398706eb518dbd30506d10a44364c8f8a24b6"
PRIOR = "reports/step7d_mapping_901_20261103/refresh-v2/companion-review.json"
SUCCESSOR = REPORT + "/companion-review.json"
ASSEMBLER = "reports/sssom_completion_20260921/assemble_review.py"
SELECTORS = ("tests/test_ingredient_bundle.py", ".github/workflows/qc-reviewed-sssom.yaml")
SELF = Path(__file__).read_bytes()


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def require(ok, message):
    if not ok:
        raise ValueError(message)


def regular(path):
    path = Path(path).absolute()
    require(path == path.resolve(), "aliased input: " + str(path))
    info = path.lstat()
    require(stat.S_ISREG(info.st_mode) and info.st_nlink == 1, "nonregular input")
    return path.read_bytes()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("phase", choices=("assembler", "selectors"))
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args()
    sys.path[:0] = [str(W), str(W / "src")]
    from scripts import step7a_guarded_publication as publisher
    from mediaingredientmech.owned_name_suppression_refresh import source_inventory
    from mediaingredientmech.validation.mapping_change_receipts import verify_mapping_chain
    from plugins.lock_manager import LockManager
    from plugins.repository_settings import RepositorySettings

    target = RepositorySettings.from_environment().get_target("mediaingredientmech")
    require(target.path.resolve() == W, "configured root differs")
    target.open()
    with LockManager().lock("mediaingredientmech", "deferred23 exact review metadata synchronization"):
        inputs = {Path(__file__): SELF}

        def read(name):
            path = W / name
            raw = regular(path)
            require(path not in inputs or inputs[path] == raw, "conflicting input bytes")
            inputs[path] = raw
            return raw

        inventory = json.loads(read(REPORT + "/unchanged-inventory.json"))
        membership = source_inventory(W)
        for folder, key in (("data/ingredients", "ingredient_sha256"), ("data/curated", "aggregate_sha256")):
            require(membership[folder] == sorted(inventory[key]), "source membership differs")
            for name, expected in inventory[key].items():
                require(sha(read(name)) == expected, "source changed: " + name)
        for name, expected in inventory["protected_sha256"].items():
            require(sha(read(name)) == expected, "protected input changed: " + name)
        require(sha(read(CANONICAL)) == NEW, "approved canonical endpoint missing")
        require(sha(read(RECEIPT)) == RECEIPT_SHA, "approved receipt26 missing")
        require(json.loads(read(REPORT + "/application/publication.json"))["state"] == "complete", "publication incomplete")
        proof = verify_mapping_chain(W)
        require(len(proof["receipt_paths"]) == 26 and proof["receipt_paths"][-1] == RECEIPT and proof["reviewed_sha256"] == NEW, "native chain differs")
        for name, expected in proof["input_hashes"].items():
            require(sha(read(name)) == expected, "native chain input changed")
        before = {}
        outputs = {}
        names = (ASSEMBLER,) if args.phase == "assembler" else SELECTORS
        old, new = ((f'REVIEWED_SOURCE = "{OLD}"', f'REVIEWED_SOURCE = "{NEW}"')
                    if args.phase == "assembler" else (PRIOR, SUCCESSOR))
        for name in names:
            raw = read(name)
            baseline = subprocess.check_output(["git", "-C", str(W), "show", BASE + ":" + name])
            require(raw == baseline and raw.count(old.encode()) == 1 and new.encode() not in raw,
                    "not an exact unchanged selector/endpoint: " + name)
            before[Path(name)] = raw
            outputs[Path(name)] = raw.replace(old.encode(), new.encode())
        if args.phase == "selectors":
            from mediaingredientmech.ingredient_bundle_contract import read_json, reviewed_products
            review = read_json(read(SUCCESSOR))
            source_names = {review["claims_file"], review["base_review"], *review["inputs"], *review["record_inputs"]}
            reviewed_products(review, {name: read(name) for name in source_names})
            refresh = json.loads(read(REPORT + "/companion-refresh-receipt.json"))
            require(refresh["scientific_approval_added"] is False, "companion approval changed")
            require(read(REPORT + "/prior-companion-review.json") == read(PRIOR), "prior companion differs")
        read("scripts/step7a_guarded_publication.py")
        read("scripts/promote_heptahydrate_ncit.py")

        def recheck():
            require(source_inventory(W) == membership, "source membership changed")
            for path, raw in inputs.items():
                require(regular(path) == raw, "captured input changed: " + str(path))

        recheck()
        log = D / ("metadata-" + args.phase + "-v1.json")
        backups = {log.with_name(log.stem + ".before-" + name.name): raw for name, raw in before.items()}
        result = {"operation": "deferred23-exact-review-metadata", "phase": args.phase,
                  "issue": "https://github.com/CultureBotAI/MediaIngredientMech/issues/669",
                  "approval": "NONE: exact endpoint/selector synchronization only",
                  "scientific_approval_added": False, "supervisor_binding": None,
                  "input_sha256": {str(p): sha(b) for p, b in inputs.items()},
                  "output_sha256": {str(p): sha(b) for p, b in outputs.items()}}
        answer = publisher.publish(W, outputs, inputs, log, backups, result,
                                   apply=args.apply, validate_scope=recheck)
        if args.apply:
            saved = json.loads(regular(log))
            publisher.completed_journal(W, log, saved, previous=before)
            for name, raw in outputs.items():
                require(regular(W / name) == raw, "written bytes differ")
                inputs[W / name] = raw
            recheck()
        print(json.dumps({"phase": args.phase, "applied": args.apply,
                          "state": answer.get("state"), "outputs": result["output_sha256"]}, indent=2))


if __name__ == "__main__":
    main()
