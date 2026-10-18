#!/usr/bin/env python3
"""Reject reviewed bad identities in the unified export, without external deps."""

from __future__ import annotations

import argparse
import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LEDGER = ROOT / "mappings/unified_mapping_rejections.tsv"
ARTIFACT = ROOT / "UNIFIED_INGREDIENT_MAPPING.tsv"
IDENTITY_COLUMNS = ("chebi_id", "culturemech_term_id", "mim_id", "kg_microbe_node_id", "cas_rn")


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
            if None in row or any(not (row.get(c) or "").strip() for c in columns):
                return [f"{ledger}: incomplete rejection"]
            row = {key: value.strip() for key, value in row.items()}
            key = (row["mim_id"], row["rejected_id"])
            if key in seen or ":" not in row["rejected_id"]:
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
                    same_label = row["ingredient_name"].strip().casefold() == rejected["ingredient_name"].strip().casefold()
                    same_identity = row["mim_id"] == rejected["mim_id"]
                    if not (same_label or same_identity):
                        continue
                    if same_label and not same_identity:
                        problems.append(f"{artifact}:{line}: {row['ingredient_name']} lost its curated identity {rejected['mim_id']}")
                    for column in IDENTITY_COLUMNS:
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
