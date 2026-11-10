#!/usr/bin/env python3
"""Audit CAS Common Chemistry hits against MediaIngredientMech chemical_properties_guard.

Purpose:
  Evaluate CAS Common Chemistry lookup hits (`mim_cas_fallbacks`,
  `mim_missing_structure`, `mim_unmapped_single`) against MediaIngredientMech's
  `chemical_properties_guard` (`_structure_consistency` and `_label_consistency`)
  without modifying any SHA-256-locked ingredient files or redistributing
  CC BY-NC 4.0 data into the BSD-3-Clause corpus.

  In particular, this audit detects and flags the 25 polysalt/polyhydrate
  records where CAS Common Chemistry's `canonicalSmile` field deduplicates
  disconnected counterions or waters of hydration (e.g. emitting a single `[Na]`
  or `.O` for disodium/trisodium/tetrasodium salts or pentahydrates/heptahydrates)
  and triggers `STRUCTURE_COMPOSITION_MISMATCH` under `_structure_consistency`.

Inputs:
  - Enriched CAS Common Chemistry TSV (`--cas-tsv`)
  - MediaIngredientMech ingredient records (`data/ingredients/{mapped,unmapped}/*.yaml`)

Outputs:
  - Guard-classification summary to stdout and optional TSV report (`--output-tsv`
    outside `data/`).

Date: 2026-11-09
"""

from __future__ import annotations

import argparse
import csv
import re
import sys
from collections import Counter
from pathlib import Path

import yaml

REPO_ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(REPO_ROOT / "src"))

from mediaingredientmech.curation.chemical_properties_guard import (  # noqa: E402
    _label_consistency,
    _structure_consistency,
)

INGREDIENTS_DIR = REPO_ROOT / "data" / "ingredients"
DEFAULT_CAS_TSV = (
    REPO_ROOT.parent
    / "XMechBay"
    / ".temp"
    / "mech-chemicals-and-acs-dois"
    / "cas_common_chemistry_enriched.tsv"
)

CAS_LICENSE = "CC-BY-NC-4.0"
CORPUS_LICENSE = "BSD-3-Clause"
INCHIKEY_PREFIX_RE = re.compile(r"^InChIKey=", re.IGNORECASE)


def strip_inchikey_prefix(value: str) -> str:
    """Normalize `InChIKey=XXXX-YYYY-Z` to standard 27-character `XXXX-YYYY-Z`."""
    return INCHIKEY_PREFIX_RE.sub("", (value or "").strip())


def normalize_cas_formula(raw_formula: str, inchi: str) -> str:
    """Return a dot-separated formula suitable for `_structure_consistency`.

    CAS Common Chemistry `molecularFormula` uses middle dots (`·`) or HTML tags;
    when `inchi` is a standard `InChI=1S/<formula>/...`, its formula layer
    already uses `.` for disconnected components.
    """
    inchi_clean = (inchi or "").strip()
    if inchi_clean.startswith("InChI=1S/"):
        layers = inchi_clean.split("/")
        if len(layers) >= 2 and layers[1]:
            return layers[1]
    cleaned = re.sub(r"<[^>]+>", "", (raw_formula or "").strip())
    return cleaned.replace("·", ".")


def validate_output_path_is_outside_data(output_path: Path, repo_root: Path = REPO_ROOT) -> None:
    """Refuse to write CC BY-NC 4.0 audit output inside `data/`."""
    resolved = output_path.resolve()
    forbidden = (repo_root / "data").resolve()
    if resolved == forbidden or resolved.is_relative_to(forbidden):
        raise ValueError(
            f"Refusing to write {CAS_LICENSE} audit output inside {forbidden}: "
            f"MediaIngredientMech is licensed under {CORPUS_LICENSE} and ingredient "
            "records are SHA-256-locked by semantic and SSSOM review gates."
        )


def load_ingredients_by_id(ingredients_dir: Path = INGREDIENTS_DIR) -> dict[str, dict]:
    """Load MediaIngredientMech ingredient files keyed by `identifier` and file stem."""
    by_id: dict[str, dict] = {}
    if not ingredients_dir.exists():
        return by_id
    for yaml_path in sorted(ingredients_dir.rglob("*.yaml")):
        with yaml_path.open(encoding="utf-8") as fh:
            doc = yaml.safe_load(fh) or {}
        identifier = (doc.get("identifier") or "").strip()
        if identifier:
            by_id[identifier] = doc
        by_id.setdefault(yaml_path.stem, doc)
    return by_id


def check_candidate_label_consistency(preferred_term: str, cas_name: str, synonyms_sample: str) -> str:
    """Check whether `preferred_term` passes `_label_consistency` against CAS name or synonyms."""
    candidates = [c.strip() for c in [cas_name, *(synonyms_sample or "").split(";")] if c.strip()]
    if not candidates:
        return "MISSING_CAS_LABEL"
    reasons = [_label_consistency(preferred_term, cand) for cand in candidates]
    if any(r is None for r in reasons):
        return "PASS"
    return reasons[0] or "NAME_SCOPE_UNRESOLVED"


def audit_cas_rows(
    cas_rows: list[dict[str, str]],
    ingredients_by_id: dict[str, dict],
) -> list[dict[str, str]]:
    """Audit MediaIngredientMech CAS Common Chemistry rows with `chemical_properties_guard`."""
    results: list[dict[str, str]] = []
    for row in cas_rows:
        if row.get("mech") != "MediaIngredientMech":
            continue
        identifier = (row.get("identifier") or "").strip()
        rec = ingredients_by_id.get(identifier, {})
        preferred_term = (rec.get("preferred_term") or row.get("query_name") or "").strip()
        cas_name = (row.get("cas_name") or "").strip()
        synonyms_sample = (row.get("synonyms_sample") or "").strip()
        inchi = (row.get("inchi") or "").strip()
        smiles = (row.get("canonical_smiles") or "").strip()
        raw_formula = (row.get("molecular_formula") or "").strip()
        norm_formula = normalize_cas_formula(raw_formula, inchi)

        props = {
            "molecular_formula": norm_formula,
            "inchi": inchi,
            "smiles": smiles,
        }
        struct_reason = _structure_consistency(preferred_term, props)
        struct_verdict = "PASS" if struct_reason is None else struct_reason
        label_verdict = check_candidate_label_consistency(preferred_term, cas_name, synonyms_sample)

        results.append(
            {
                "group": (row.get("group") or "").strip(),
                "identifier": identifier,
                "preferred_term": preferred_term,
                "cas_rn": (row.get("cas_rn") or "").strip(),
                "cas_name": cas_name,
                "normalized_formula": norm_formula,
                "canonical_smiles": smiles,
                "inchikey": strip_inchikey_prefix(row.get("inchikey") or ""),
                "structure_guard": struct_verdict,
                "label_guard": label_verdict,
            }
        )
    return results


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--cas-tsv",
        type=Path,
        default=DEFAULT_CAS_TSV,
        help="Path to cas_common_chemistry_enriched.tsv",
    )
    parser.add_argument(
        "--output-tsv",
        type=Path,
        default=None,
        help="Optional output TSV path (must be outside data/)",
    )
    args = parser.parse_args(argv)

    if not args.cas_tsv.exists():
        print(f"missing {args.cas_tsv}; run query_cas_common_chemistry.py first", file=sys.stderr)
        return 1

    if args.output_tsv is not None:
        validate_output_path_is_outside_data(args.output_tsv)

    with args.cas_tsv.open(newline="", encoding="utf-8") as fh:
        cas_rows = list(csv.DictReader(fh, delimiter="\t"))

    ingredients_by_id = load_ingredients_by_id(INGREDIENTS_DIR)
    audited = audit_cas_rows(cas_rows, ingredients_by_id)

    print(f"CAS Common Chemistry license                : {CAS_LICENSE}")
    print(f"MediaIngredientMech corpus license          : {CORPUS_LICENSE}")
    print(f"MediaIngredientMech CAS hits audited        : {len(audited)}")
    print()

    for group in sorted({r["group"] for r in audited}):
        subset = [r for r in audited if r["group"] == group]
        struct_counts = Counter(r["structure_guard"] for r in subset)
        both_pass = sum(
            1 for r in subset if r["structure_guard"] == "PASS" and r["label_guard"] == "PASS"
        )
        print(f"Group {group} (total={len(subset)}, structure+label PASS={both_pass}):")
        for verdict, count in sorted(struct_counts.items()):
            print(f"  {verdict:<38} : {count}")
        print()

    print("NOT WRITTEN TO DATA/INGREDIENTS. Ingredient records are SHA-256-locked by")
    print("SSSOM and semantic release gates and require defining ChEBI OLS4 properties.")

    if args.output_tsv is not None:
        args.output_tsv.parent.mkdir(parents=True, exist_ok=True)
        fieldnames = [
            "group",
            "identifier",
            "preferred_term",
            "cas_rn",
            "cas_name",
            "normalized_formula",
            "canonical_smiles",
            "inchikey",
            "structure_guard",
            "label_guard",
        ]
        with args.output_tsv.open("w", newline="", encoding="utf-8") as fh:
            writer = csv.DictWriter(
                fh, fieldnames=fieldnames, delimiter="\t", lineterminator="\n"
            )
            writer.writeheader()
            writer.writerows(audited)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
