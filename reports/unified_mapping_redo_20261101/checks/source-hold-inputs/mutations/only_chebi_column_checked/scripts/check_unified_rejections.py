#!/usr/bin/env python3
"""Reject reviewed bad identities in the unified export, without external deps.

See docs/UNIFIED_MAPPING_REJECTIONS.md for identity and exact-label scopes.
"""

from __future__ import annotations

import argparse
import csv
from pathlib import Path
import re
import unicodedata

ROOT = Path(__file__).resolve().parents[1]
LEDGER = ROOT / "mappings/unified_mapping_rejections.tsv"
ARTIFACT = ROOT / "UNIFIED_INGREDIENT_MAPPING.tsv"
IDENTITY_COLUMNS = ("chebi_id", "culturemech_term_id", "mim_id", "kg_microbe_node_id", "cas_rn")
REJECTION_ID = re.compile(r"[A-Za-z][A-Za-z0-9.]*:[A-Za-z0-9][A-Za-z0-9._~-]*\Z")


def _label_key(name: str) -> str:
    return unicodedata.normalize("NFC", name).strip().casefold()


def check(artifact: Path = ARTIFACT, ledger: Path = LEDGER) -> list[str]:
    """Verify rejections even when a stale producer regenerates and stamps a TSV."""
    problems = []
    try:
        with ledger.open(encoding="utf-8", newline="") as handle:
            reader = csv.DictReader(handle, delimiter="\t")
            columns = ["ingredient_name", "rejected_id", "mim_id", "reason"]
            if reader.fieldnames != columns:
                return [f"{ledger}: invalid rejection-ledger columns"]
            raw_rejections = list(reader)
        rejections = []
        seen = set()
        for row in raw_rejections:
            if (
                None in row
                or any(row.get(c) is None for c in columns)
                or any(not row[c].strip() for c in columns if c != "mim_id")
            ):
                return [f"{ledger}: incomplete rejection"]
            row = {key: value.strip() for key, value in row.items()}
            key = (
                (row["mim_id"], row["rejected_id"])
                if row["mim_id"]
                else ("source_label", _label_key(row["ingredient_name"]), row["rejected_id"])
            )
            if key in seen or not REJECTION_ID.fullmatch(row["rejected_id"]) or row["mim_id"].startswith("UNMAPPED"):
                return [f"{ledger}: duplicate or invalid rejection"]
            if row["rejected_id"] == row["mim_id"]:
                return [f"{ledger}: rejected ID equals corrected identity"]
            seen.add(key)
            rejections.append(row)
        with artifact.open(encoding="utf-8", newline="") as handle:
            reader = csv.DictReader(handle, delimiter="\t")
            if not {"ingredient_name", *IDENTITY_COLUMNS}.issubset(reader.fieldnames or []):
                return [f"{artifact}: missing identity columns"]
            for line, row in enumerate(reader, 2):
                if None in row or any(row[c] is None for c in ("ingredient_name", *IDENTITY_COLUMNS)):
                    return [f"{artifact}:{line}: malformed export row"]
                for rejected in rejections:
                    same_label = _label_key(row["ingredient_name"]) == _label_key(rejected["ingredient_name"])
                    same_identity = bool(rejected["mim_id"]) and row["mim_id"] == rejected["mim_id"]
                    if not (same_label or same_identity):
                        continue
                    if same_label and rejected["mim_id"] and not same_identity:
                        problems.append(f"{artifact}:{line}: {row['ingredient_name']} lost its curated identity {rejected['mim_id']}")
                    for column in ("chebi_id",):
                        if row[column] == rejected["rejected_id"]:
                            problems.append(f"{artifact}:{line}: {row['ingredient_name']} republishes rejected {row[column]} in {column}")
    except (OSError, UnicodeError, csv.Error) as error:
        problems.append(str(error))
    return problems


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--artifact", type=Path, default=ARTIFACT)
    parser.add_argument("--ledger", type=Path, default=LEDGER)
    args = parser.parse_args()
    problems = check(args.artifact, args.ledger)
    if problems:
        print("\n".join(problems))
        return 1
    print("Unified export respects reviewed identity rejections.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
