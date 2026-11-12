#!/usr/bin/env python3
"""Correct one unsupported source-origin explanation without grounding it (#1151).

Dry run by default. Preserve REJECTED status, raw label and all prior history.
Only active notes and one appended event change; this grants no export approval.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import io
import json
from copy import deepcopy
from pathlib import Path

import yaml

from mediaingredientmech.curate.apply_receipt import reserve_receipt_outputs
from mediaingredientmech.curate.curation_event import record_curation_event
from mediaingredientmech.curate.publication_guard import (
    FrozenFile,
    check_reserved,
    finish_receipt,
    no_alias,
    publish_validated,
)
from mediaingredientmech.validation.write_validated import write_validated_ingredient

OWNER = "data/ingredients/unmapped/3-methylacetate.yaml"
BEFORE = "98d0af6ac0a86e2ae354ffeb39933840658bfec5550a0b2e81a1f59246eb604a"
SOURCE_CSV = "b60fee13501d1ddba9d53688462f86055a9c1d6c6a470157e336a00ca93e7360"
RAW_ROW = "f96206bc73f8fa93d7a144e6f4f586e8e464d23b31d8093a0d510bc5d272302a"
RAW_DATABASE = "0c6ff730a108720a5d6972400f2bccf2eca8621713b62736abdf5df0fb188c95"
SOURCE = "https://doi.org/10.1002/9781118960608.gbm01426"
NEW_NOTES = (
    "Imported from MicrobeDecoder (source_id=kgmicrobe.compound:3_methylacetate). "
    "The literal 3-methylacetate is present in both the raw Bergey_Text_for_end_products "
    "and Bergey_Minor_end_products fields for Telmatobacter bradus, LPSN 789679, "
    "database.csv record 19685 (source citation " + SOURCE + "). "
    "This is reported minor-product provenance, not an established chemical identity "
    "or growth-medium ingredient. The prior importer-fragment explanation and proposed "
    "3-methyl mercaptopropionate reconstruction are unsupported by this source and are "
    "superseded; their original wording remains in curation history and the archived "
    "preimage. Retain REJECTED status and no ontology mapping until identity and "
    "ingredient/product scope are resolved. No replacement compound is inferred. "
    "Evidence and exact source hashes: reports/kgm_unmapped_chemicals_20261107/"
    "methylacetate/sources/manifest.json; issue #1151."
)
VERIFICATION = (
    "Correct active source-origin notes only (#1151): raw database.csv SHA256="
    + RAW_DATABASE
    + ", record19685 canonical SHA256="
    + RAW_ROW
    + ", contains 3-methylacetate in original prose and structured minor-product field. "
    "Retain unresolved identity, REJECTED status, all raw synonyms, counts and prior "
    "history; add no ontology mapping, replacement identity, role or release approval. "
    "The original primary paper was not independently re-read in this provenance check."
)


def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def prepare(data: bytes, source: bytes, timestamp: str | None = None) -> dict:
    """Require exact reviewed bytes and native whole-row provenance before editing."""
    if sha(data) != BEFORE:
        raise ValueError("Owner differs from the reviewed preimage")
    if sha(source) != SOURCE_CSV:
        raise ValueError("Source extract differs from the reviewed bytes")
    rows = list(csv.DictReader(io.StringIO(source.decode("utf-8"))))
    if len(rows) != 1:
        raise ValueError("Expected exactly one complete source record")
    row = rows[0]
    # KG-Microbe chemical_curation.canonical_raw_row_sha256: every literal field.
    literal = json.dumps(
        row, ensure_ascii=False, sort_keys=True, separators=(",", ":"), allow_nan=False
    )
    if sha(literal.encode("utf-8", errors="surrogateescape")) != RAW_ROW:
        raise ValueError("Source record differs from the bound native record")
    if (
        row["LPSN_ID"] != "789679"
        or row["Bergey_Text_for_end_products"]
        != "acetate and hydrogen, plus traces of 2-methylbutyrate and 3-methylacetate"
        or row["Bergey_Minor_end_products"] != "2-methylbutyrate;3-methylacetate"
    ):
        raise ValueError("Wrong source organism or asserted product wording")
    record = yaml.safe_load(data)
    if (record["identifier"], record["preferred_term"], record["mapping_status"]) != (
        "UNMAPPED_0736",
        "3-methylacetate",
        "REJECTED",
    ) or record.get("ontology_mapping"):
        raise ValueError("Wrong owner, status or mapping boundary")
    result = deepcopy(record)
    result["notes"] = NEW_NOTES
    record_curation_event(
        result,
        curator="claude",
        action="CORRECTED_SOURCE_PROVENANCE",
        changes=VERIFICATION,
        previous_status="REJECTED",
        new_status="REJECTED",
        llm_assisted=True,
        timestamp=timestamp,
    )
    return result


def publish(root: Path, source_path: Path, receipt_dir: Path, *, apply: bool = False) -> dict:
    """Reserve evidence and atomically publish validated bytes (#1151, #1153)."""
    owner = root / OWNER
    no_alias(root)
    no_alias(receipt_dir)
    target, evidence = FrozenFile.capture(owner), FrozenFile.capture(source_path)
    before, source = target.content, evidence.content
    record = prepare(before, source)
    summary = {
        "owner": OWNER,
        "shape": "source_provenance_note",
        "approval": "NONE",
        "apply": apply,
    }
    if not apply:
        return summary
    backup_path, log_path = receipt_dir / "owner-before.yaml", receipt_dir / "apply-log.json"
    if any(
        p.resolve() in (owner.resolve(), source_path.resolve()) for p in (backup_path, log_path)
    ):
        raise ValueError("Receipt/source collision")
    with reserve_receipt_outputs(log_path, backup_paths=(backup_path,)) as (receipt, backup):

        def recheck():
            evidence.verify()
            check_reserved(receipt, log_path)
            check_reserved(backup, backup_path)

        target.verify()
        recheck()
        backup.write(before)
        backup.flush()
        published = publish_validated(
            target, lambda staged: write_validated_ingredient(record, staged), recheck
        )
        after = published.content
        if yaml.safe_load(after) != record:
            raise ValueError("Owner readback or source evidence changed during write")
        entry = {
            "source_record": OWNER,
            "shape": "source_provenance_note",
            "before_yaml_sha256": sha(before),
            "after_yaml_sha256": sha(after),
            "change": "Correct active source-provenance notes; append one event; preserve REJECTED status.",
            "verification": VERIFICATION,
        }

        def final_check():
            published.verify()
            recheck()

        finish_receipt(receipt, log_path, {"records": [entry]}, final_check)
    return summary


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path.cwd())
    parser.add_argument("--source-record", type=Path, required=True)
    parser.add_argument("--receipt-dir", type=Path, required=True)
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args()
    print(json.dumps(publish(args.root, args.source_record, args.receipt_dir, apply=args.apply)))


if __name__ == "__main__":
    main()
