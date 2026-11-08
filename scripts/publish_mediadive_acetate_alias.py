#!/usr/bin/env python3
"""Project only the independently reviewed #1149 spelling from a native candidate.

The full regeneration changes unrelated historical provenance and row membership.
This bounded writer preserves all other canonical bytes, including confidence,
validation stamps and historical sources. Native receipts/review remain required.
"""

from __future__ import annotations

import argparse
import csv
import io
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
from mediaingredientmech.ingredient_bundle_contract import content_sha256
from mediaingredientmech.source_alias_refresh import ADDED_SOURCE, ALIAS, OWNER, SOURCE, SUBJECT

CANONICAL_BEFORE = "d5f76fc404967477903fafc79eaba86ecfef9e2c391926ec08c3c1af4a5220b6"
PRODUCER = "76c1ebeea3fc7f80bf1abe044688f298f390cfac"


def rows(raw):
    return list(
        csv.DictReader(
            (s for s in raw.decode().splitlines() if not s.startswith("#")), delimiter="\t"
        )
    )


def project(before: bytes, candidate: bytes) -> tuple[bytes, dict]:
    if content_sha256(before) != CANONICAL_BEFORE:
        raise ValueError("Canonical baseline differs")
    selected = [r for r in rows(candidate) if r["subject_id"] == SUBJECT]
    old = [r for r in rows(before) if r["subject_id"] == SUBJECT]
    if len(selected) != 1 or len(old) != 1:
        raise ValueError("Ambiguous/missing subject rows")
    new, old = selected[0], old[0]
    allowed_native = {"other", "mapping_date", "source", "confidence"}
    if {k: v for k, v in old.items() if k not in allowed_native} != {
        k: v for k, v in new.items() if k not in allowed_native
    }:
        raise ValueError("Native candidate changes scoped identity or retained metadata")
    expected_tokens = old["other"].split("|") + [ALIAS]
    if len(set(expected_tokens)) != len(expected_tokens) or sorted(
        new["other"].split("|")
    ) != sorted(expected_tokens):
        raise ValueError("Native candidate changes more than the reviewed spelling")
    result = dict(old)
    result["other"] = "|".join(expected_tokens)
    result["mapping_date"] = new["mapping_date"]
    result["source"] += "|" + ADDED_SOURCE
    lines = before.decode().splitlines(keepends=True)
    header = next(s for s in lines if not s.startswith("#")).rstrip("\r\n").split("\t")
    replacements = 0
    for i, line in enumerate(lines):
        if line.startswith(SUBJECT + "\t"):
            output = io.StringIO(newline="")
            csv.DictWriter(output, fieldnames=header, delimiter="\t", lineterminator="\n").writerow(
                result
            )
            lines[i] = output.getvalue()
            replacements += 1
    if replacements != 1:
        raise ValueError("Physical source row is ambiguous")
    return "".join(lines).encode(), {"before": old, "native_candidate": new, "after": result}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path.cwd())
    parser.add_argument("--candidate", type=Path, required=True)
    parser.add_argument("--manifest", type=Path, required=True)
    parser.add_argument("--receipt-dir", type=Path, required=True)
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args()
    no_alias(args.root)
    no_alias(args.receipt_dir)
    root = args.root.absolute()
    canonical = FrozenFile.capture(root / SOURCE)
    captured = [FrozenFile.capture(p) for p in (root / OWNER, args.candidate, args.manifest)]
    owner, candidate_file, manifest_file = captured
    manifest = json.loads(manifest_file.content)
    candidate = candidate_file.content
    before = canonical.content
    owner_hash = content_sha256(owner.content)
    if (
        manifest["source_revisions"]["claw"] != PRODUCER
        or manifest["external_sssom_validation"] != "passed"
    ):
        raise ValueError("Unverified native producer")
    if not any(
        a["role"] == "sssom" and a["sha256"] == content_sha256(candidate)
        for a in manifest["artifacts"]
    ):
        raise ValueError("Candidate is not bound to native manifest")
    if not any(
        a["path"] == str(root / OWNER) and a["sha256"] == owner_hash
        for a in manifest["source_inputs"]
    ):
        raise ValueError("Generation does not bind current owner")
    after, audit = project(before, candidate)
    print(json.dumps({"subject": SUBJECT, "changed_rows": 1, "apply": args.apply}))
    if not args.apply:
        return
    log, backup_path = (
        args.receipt_dir / "projection.json",
        args.receipt_dir / "canonical-before.tsv",
    )
    with reserve_receipt_outputs(log, backup_paths=(backup_path,)) as (receipt, backup):

        def recheck():
            for item in captured:
                item.verify()
            check_reserved(receipt, log)
            check_reserved(backup, backup_path)

        canonical.verify()
        recheck()
        backup.write(before)
        backup.flush()
        published = publish_validated(canonical, lambda staged: staged.write_bytes(after), recheck)

        def final_check():
            published.verify()
            recheck()

        finish_receipt(
            receipt,
            log,
            {
                "issue": 1149,
                "approval": "NONE",
                "owner_sha256": owner_hash,
                "native_manifest_sha256": content_sha256(manifest_file.content),
                "native_candidate_sha256": content_sha256(candidate),
                "before_sha256": content_sha256(before),
                "after_before_header_sha256": content_sha256(after),
                "canonical_source": SOURCE,
                "row_projection": audit,
                "preservation": "Historical confidence, source vocabulary and validation stamp retained; no unrelated row adopted.",
            },
            final_check,
        )


if __name__ == "__main__":
    main()
