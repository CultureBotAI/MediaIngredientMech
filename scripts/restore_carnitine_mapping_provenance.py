#!/usr/bin/env python3
"""Restore historical carnitine mapping provenance without changing claims (#1014).

The immutable #669/#1003 receipt supplies both the exact preimage and the
original source/comment cells. Dry-run is the default. A new mapping-change
receipt must subsequently append this correction to the native review chain.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

from mediaingredientmech.curate.apply_receipt import reserve_receipt_outputs

ROOT = Path(__file__).resolve().parents[1]
SOURCE = Path("mappings/ingredient_mappings.sssom.tsv")
PRIOR = Path(
    "reports/sssom_completion_20260921/mapping_changes/issue669-1003-scoped-alias-corrections.json"
)
OWNER = "data/ingredients/mapped/Carnitine_Hydrochloride.yaml"
SUBJECT = "MIM:Carnitine_Hydrochloride"
OBJECTS = {"CHEBI:17126", "kgmicrobe.compound:carnitine_hydrochloride"}


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def restore_provenance(data: bytes, prior: dict) -> bytes:
    """Restore only the two historical source/comment cells, preserving bytes."""
    if digest(data) != prior["after_sha256"]:
        raise ValueError("Canonical bytes differ from the reviewed correction receipt")
    selected = [c for c in prior["changes"] if c["after"]["subject_id"] == SUBJECT]
    if (
        len(selected) != 2
        or {c["after"]["object_id"] for c in selected} != OBJECTS
        or any(c["kind"] != "changed" or c["before_position"] != c["after_position"]
               for c in selected)
    ):
        raise ValueError("Expected exactly the two unchanged carnitine mapping slots")
    expected = {c["after_position"]: c for c in selected}
    lines = data.decode("utf-8").splitlines(keepends=True)
    header = None
    position = 0
    restored = set()
    for index, line in enumerate(lines):
        if line.startswith("#") or not line.strip():
            continue
        ending = "\r\n" if line.endswith("\r\n") else "\n" if line.endswith("\n") else ""
        cells = (line[:-len(ending)] if ending else line).split("\t")
        if header is None:
            header = cells
            if len(set(header)) != len(header) or not {"source", "comment"} <= set(header):
                raise ValueError("Invalid SSSOM columns")
            continue
        position += 1
        if len(cells) != len(header):
            raise ValueError("Ambiguous SSSOM cell count")
        if position not in expected:
            continue
        change = expected[position]
        row = dict(zip(header, cells, strict=True))
        if row != change["after"]:
            raise ValueError("Carnitine row differs from receipt preimage")
        if row["object_id"] == "CHEBI:17126" and "[#390 " not in change["before"]["comment"]:
            raise ValueError("Historical predicate-reconciliation comment is missing")
        for field in ("source", "comment"):
            cells[header.index(field)] = change["before"][field]
        lines[index] = "\t".join(cells) + ending
        restored.add(position)
    if restored != set(expected) or position != prior["after_row_count"]:
        raise ValueError("Incomplete carnitine restoration or row count drift")
    return "".join(lines).encode("utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=ROOT)
    parser.add_argument("--log", type=Path, required=True)
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args()
    root = args.root.resolve()
    prior_bytes = (root / PRIOR).read_bytes()
    prior = json.loads(prior_bytes)
    source = root / SOURCE
    before = source.read_bytes()
    after = restore_provenance(before, prior)
    owner = (root / OWNER).read_bytes()
    owner_sha = digest(owner)
    prior_owner = next(r for r in prior["records"] if r["source_record"] == OWNER)
    if owner_sha != prior_owner["after_yaml_sha256"]:
        raise ValueError("Carnitine owner changed after the reviewed alias correction")
    record = {
        "source_record": OWNER,
        "shape": "mapping_provenance_restoration",
        "before_yaml_sha256": owner_sha,
        "after_yaml_sha256": owner_sha,
        "change": "Restore both original source cells and the #390 predicate-reconciliation comment; preserve corrected aliases, dates, identifiers, predicates and all other rows (#1014).",
        "verification": "Exact before/after rows in immutable issue669-1003-scoped-alias-corrections.json establish the original provenance. This restoration makes no new scientific assertion and grants no approval.",
    }
    result = {
        "issue": "#1014", "records": [record],
        "prior_receipt": str(PRIOR), "prior_receipt_sha256": digest(prior_bytes),
        "sssom_before_sha256": digest(before), "sssom_after_sha256": digest(after),
        "changed_rows": 2, "allowed_fields": ["source", "comment"],
        "approval": "NONE; existing WITHHOLD decisions remain withheld",
    }
    if args.apply:
        backup_path = args.log.with_suffix(".before.tsv")
        with reserve_receipt_outputs(args.log, backup_paths=(backup_path,)) as (receipt, backup):
            if source.read_bytes() != before or (root / OWNER).read_bytes() != owner or (root / PRIOR).read_bytes() != prior_bytes:
                raise ValueError("Input changed during provenance verification")
            backup.write(before)
            backup.flush()
            receipt.write(json.dumps(result, indent=2) + "\n")
            receipt.flush()
            source.write_bytes(after)
    print(json.dumps({"applied": args.apply, **result}, indent=2))


if __name__ == "__main__":
    main()
