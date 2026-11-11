#!/usr/bin/env python3
"""Audit CAS Common Chemistry hits against MediaIngredientMech chemical_properties_guard.

Purpose:
  Evaluate CAS Common Chemistry lookup hits (`mim_cas_fallbacks`,
  `mim_missing_structure`, `mim_unmapped_single`) against MediaIngredientMech's
  `chemical_properties_guard` (`_structure_consistency` and `_label_consistency`)
  and 3-star ChEBI (`chebi_structures.tsv`) without modifying any SHA-256-locked
  ingredient files or redistributing CC BY-NC 4.0 data into the BSD-3-Clause corpus.

  In particular, this audit:
    1. Detects and refuses the 26 polysalt/polyhydrate records
       (`REFUSE_CAS_DEDUPLICATED_SMILES`) where CAS Common Chemistry's
       `canonicalSmile` field deduplicates disconnected counterions or waters of
       hydration (e.g. emitting a single `[Na]` or `.O` for disodium/trisodium/
       tetrasodium salts or pentahydrates/heptahydrates) and triggers
       `STRUCTURE_COMPOSITION_MISMATCH` under `_structure_consistency`.
    2. Cross-references passing records' `Standard InChIKey` values against
       3-star ChEBI (`--chebi-structures-tsv`) to identify candidates ready to
       be seeded from CC BY 4.0 ChEBI OLS4 (`SEED_FROM_CHEBI_OLS4_READY`) vs
       connectivity-only salt/hydrate form matches
       (`CHEBI_3STAR_CONNECTIVITY_ONLY_REVIEW_FORM`).
    3. Flags `mim_unmapped_single` monomer groundings (`UNMAPPED_0159`
       `Ethanolamine acetate` -> `CAS-RN:54300-24-2`, `UNMAPPED_0587`
       `α-D-Glucose monohydrate` -> `CAS-RN:14431-43-7`) where only the
       non-copyrightable `CAS-RN` identifier fact can be grounded because
       3-star ChEBI lacks those salt/hydrate forms
       (`GROUND_CAS_RN_ONLY_NO_CHEBI_3STAR`).

Inputs:
  - Enriched CAS Common Chemistry TSV (`--cas-tsv`)
  - MediaIngredientMech ingredient records (`data/ingredients/{mapped,unmapped}/*.yaml`)
  - Optional 3-star ChEBI structures TSV (`--chebi-structures-tsv`)

Outputs:
  - Guard and curation-disposition summary to stdout and optional TSV report
    (`--output-tsv` outside `data/`).

Issue:
  https://github.com/CultureBotAI/MediaIngredientMech/issues/1296

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
DEFAULT_CHEBI_STRUCTURES_TSV = (
    REPO_ROOT.parent / "NaturalProductMech" / "data" / "raw" / "chebi_structures.tsv"
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


def _component_count(formula_expr: str) -> int:
    parts = [p.strip() for p in re.split(r"[.·]", formula_expr) if p.strip()]
    total = 0
    for part in parts:
        m = re.match(r"^(\d+)\s*[A-Za-z(\[]", part)
        total += int(m.group(1)) if m else 1
    return total


def has_deduplicated_component_smiles(
    molecular_formula: str,
    canonical_smiles: str,
    inchi: str,
) -> bool:
    """Detect CAS Common Chemistry `canonicalSmile` component deduplication on polysalts/hydrates."""
    norm_formula = normalize_cas_formula(molecular_formula, inchi)
    smiles = (canonical_smiles or "").strip()
    if not smiles or not norm_formula:
        return False
    smiles_parts = [p for p in smiles.split(".") if p]
    if "." in norm_formula and len(smiles_parts) < _component_count(norm_formula):
        return True
    return False


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


def load_chebi_lookup(
    path: Path | None,
) -> tuple[dict[str, list[tuple[str, str]]], dict[str, list[tuple[str, str]]]]:
    """Return `(exact_by_inchikey, connectivity_by_14char)` candidate lists from a 3-star ChEBI TSV."""
    if path is None or not path.exists():
        return {}, {}
    exact: dict[str, list[tuple[str, str]]] = {}
    conn14: dict[str, list[tuple[str, str]]] = {}
    with path.open(newline="", encoding="utf-8") as fh:
        for row in csv.DictReader(fh, delimiter="\t"):
            ik = (row.get("standard_inchi_key") or "").strip()
            cid = (row.get("chebi_id") or "").strip()
            name = (row.get("name") or row.get("label") or "").strip()
            if ik and cid:
                pair = (cid, name)
                if pair not in exact.setdefault(ik, []):
                    exact[ik].append(pair)
                if pair not in conn14.setdefault(ik[:14], []):
                    conn14[ik[:14]].append(pair)
    return exact, conn14


def _coerce_candidate_list(
    entry: list[tuple[str, str]] | tuple[str, str] | None,
) -> list[tuple[str, str]]:
    """Normalize either a single `(chebi_id, name)` tuple or a list of tuples into a list."""
    if not entry:
        return []
    if isinstance(entry, tuple) and len(entry) == 2 and isinstance(entry[0], str):
        return [entry]
    return list(entry)


def select_best_chebi_candidate(
    preferred_term: str,
    candidates: list[tuple[str, str]] | tuple[str, str] | None,
) -> tuple[str, str, str]:
    """Select `(best_chebi_id, best_name, all_candidate_ids_pipe_joined)` ranked against `preferred_term`.

    Candidates whose name matches `preferred_term` case-insensitively rank first,
    followed by candidates that pass `_label_consistency(preferred_term, name) is None`,
    and finally the first candidate in file order.
    """
    cand_list = _coerce_candidate_list(candidates)
    if not cand_list:
        return "", "", ""
    all_ids = "|".join(cid for cid, _ in cand_list)
    pref_cf = (preferred_term or "").strip().casefold()
    pref_tokens = set(re.findall(r"[a-z0-9]+", pref_cf))
    pref_stem_tokens = {t for t in pref_tokens if len(t) >= 2 and not t.isdigit()}

    def _rank_key(idx_and_pair: tuple[int, tuple[str, str]]) -> tuple[int, int, int, int]:
        idx, (_cid, cname) = idx_and_pair
        cname_cf = (cname or "").strip().casefold()
        cand_tokens = set(re.findall(r"[a-z0-9]+", cname_cf))
        cand_stem_tokens = {t for t in cand_tokens if len(t) >= 2 and not t.isdigit()}
        shared_stems = len(pref_stem_tokens & cand_stem_tokens)
        shared_tokens = len(pref_tokens & cand_tokens)
        if pref_cf and cname_cf == pref_cf:
            return (0, -shared_stems, -shared_tokens, idx)
        if pref_cf and _label_consistency(preferred_term, cname) is None:
            return (1, -shared_stems, -shared_tokens, idx)
        return (2, -shared_stems, -shared_tokens, idx)

    _, (best_id, best_name) = min(enumerate(cand_list), key=_rank_key)
    return best_id, best_name, all_ids


_IDENTIFIER_RE = re.compile(r"^identifier:\s*(.+?)\s*$", re.MULTILINE)
_PREFERRED_TERM_RE = re.compile(r"^preferred_term:\s*(.+?)\s*$", re.MULTILINE)


def _strip_yaml_scalar(raw: str) -> str:
    val = raw.strip()
    if len(val) >= 2 and val[0] == val[-1] and val[0] in {"'", '"'}:
        return val[1:-1]
    return val


def load_ingredients_by_id(ingredients_dir: Path = INGREDIENTS_DIR) -> dict[str, dict]:
    """Load MediaIngredientMech ingredient files keyed by `identifier` and file stem."""
    by_id: dict[str, dict] = {}
    if not ingredients_dir.exists():
        return by_id
    for yaml_path in sorted(ingredients_dir.rglob("*.yaml")):
        head = yaml_path.read_text(encoding="utf-8")[:1024]
        id_m = _IDENTIFIER_RE.search(head)
        pt_m = _PREFERRED_TERM_RE.search(head)
        if id_m and pt_m:
            doc = {
                "identifier": _strip_yaml_scalar(id_m.group(1)),
                "preferred_term": _strip_yaml_scalar(pt_m.group(1)),
                "_rel_path": yaml_path.relative_to(REPO_ROOT).as_posix()
                if yaml_path.is_relative_to(REPO_ROOT)
                else str(yaml_path),
            }
        else:
            doc = yaml.safe_load(yaml_path.read_text(encoding="utf-8")) or {}
            doc["_rel_path"] = (
                yaml_path.relative_to(REPO_ROOT).as_posix()
                if yaml_path.is_relative_to(REPO_ROOT)
                else str(yaml_path)
            )
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


def _classify_curation_disposition(
    *,
    group: str,
    cas_rn: str = "",
    dedup_smiles: bool,
    struct_verdict: str,
    label_verdict: str,
    chebi_match_type: str,
) -> str:
    """Classify the actionable curation disposition for a MediaIngredientMech CAS row."""
    if dedup_smiles or struct_verdict == "STRUCTURE_COMPOSITION_MISMATCH":
        return "REFUSE_CAS_DEDUPLICATED_SMILES"
    if struct_verdict != "PASS" or label_verdict != "PASS":
        return "HOLD_GUARD_REJECTION"
    if chebi_match_type == "EXACT_INCHIKEY":
        return "SEED_FROM_CHEBI_OLS4_READY"
    if chebi_match_type == "CONNECTIVITY_14":
        return "CHEBI_3STAR_CONNECTIVITY_ONLY_REVIEW_FORM"
    if group == "mim_unmapped_single" and cas_rn.strip():
        return "GROUND_CAS_RN_ONLY_NO_CHEBI_3STAR"
    return "CAS_RESOLVED_NO_CHEBI_3STAR"


def audit_cas_rows(
    cas_rows: list[dict[str, str]],
    ingredients_by_id: dict[str, dict],
    chebi_exact: dict[str, list[tuple[str, str]] | tuple[str, str]] | None = None,
    chebi_conn14: dict[str, list[tuple[str, str]] | tuple[str, str]] | None = None,
) -> list[dict[str, str]]:
    """Audit MediaIngredientMech CAS Common Chemistry rows with `chemical_properties_guard` and ChEBI."""
    exact_map = chebi_exact or {}
    conn14_map = chebi_conn14 or {}
    results: list[dict[str, str]] = []
    for row in cas_rows:
        if row.get("mech") != "MediaIngredientMech":
            continue
        group = (row.get("group") or "").strip()
        identifier = (row.get("identifier") or "").strip()
        rec = ingredients_by_id.get(identifier, {})
        preferred_term = (rec.get("preferred_term") or row.get("query_name") or "").strip()
        cas_name = (row.get("cas_name") or "").strip()
        synonyms_sample = (row.get("synonyms_sample") or "").strip()
        inchi = (row.get("inchi") or "").strip()
        smiles = (row.get("canonical_smiles") or "").strip()
        raw_formula = (row.get("molecular_formula") or "").strip()
        norm_formula = normalize_cas_formula(raw_formula, inchi)
        ik = strip_inchikey_prefix(row.get("inchikey") or "")
        dedup_smiles = has_deduplicated_component_smiles(raw_formula, smiles, inchi)

        props = {
            "molecular_formula": norm_formula,
            "inchi": inchi,
            "smiles": smiles,
        }
        struct_reason = _structure_consistency(preferred_term, props)
        struct_verdict = "PASS" if struct_reason is None else struct_reason
        label_verdict = check_candidate_label_consistency(preferred_term, cas_name, synonyms_sample)

        if ik and ik in exact_map:
            chebi_id, chebi_name, all_chebi_ids = select_best_chebi_candidate(
                preferred_term, exact_map[ik]
            )
            chebi_match_type = "EXACT_INCHIKEY"
        elif ik and ik[:14] in conn14_map:
            chebi_id, chebi_name, all_chebi_ids = select_best_chebi_candidate(
                preferred_term, conn14_map[ik[:14]]
            )
            chebi_match_type = "CONNECTIVITY_14"
        else:
            chebi_id, chebi_name, all_chebi_ids = "", "", ""
            chebi_match_type = "NONE"

        disposition = _classify_curation_disposition(
            group=group,
            cas_rn=(row.get("cas_rn") or "").strip(),
            dedup_smiles=dedup_smiles,
            struct_verdict=struct_verdict,
            label_verdict=label_verdict,
            chebi_match_type=chebi_match_type,
        )

        results.append(
            {
                "group": group,
                "identifier": identifier,
                "preferred_term": preferred_term,
                "cas_rn": (row.get("cas_rn") or "").strip(),
                "cas_name": cas_name,
                "normalized_formula": norm_formula,
                "canonical_smiles": smiles,
                "inchikey": ik,
                "deduplicated_component_smiles": "true" if dedup_smiles else "false",
                "structure_guard": struct_verdict,
                "label_guard": label_verdict,
                "candidate_chebi_id": chebi_id,
                "candidate_chebi_name": chebi_name,
                "all_candidate_chebi_ids": all_chebi_ids,
                "chebi_match_type": chebi_match_type,
                "curation_disposition": disposition,
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
        "--chebi-structures-tsv",
        type=Path,
        default=DEFAULT_CHEBI_STRUCTURES_TSV,
        help="Optional path to 3-star ChEBI structures TSV",
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
    chebi_exact, chebi_conn14 = load_chebi_lookup(args.chebi_structures_tsv)
    audited = audit_cas_rows(cas_rows, ingredients_by_id, chebi_exact, chebi_conn14)

    dedup_total = sum(1 for r in audited if r["deduplicated_component_smiles"] == "true")
    print(f"CAS Common Chemistry license                : {CAS_LICENSE}")
    print(f"MediaIngredientMech corpus license          : {CORPUS_LICENSE}")
    print(f"MediaIngredientMech CAS hits audited        : {len(audited)}")
    print(f"Refused deduplicated component SMILES       : {dedup_total}")
    print()

    for group in sorted({r["group"] for r in audited}):
        subset = [r for r in audited if r["group"] == group]
        struct_counts = Counter(r["structure_guard"] for r in subset)
        disp_counts = Counter(r["curation_disposition"] for r in subset)
        both_pass = sum(
            1 for r in subset if r["structure_guard"] == "PASS" and r["label_guard"] == "PASS"
        )
        print(f"Group {group} (total={len(subset)}, structure+label PASS={both_pass}):")
        for verdict, count in sorted(struct_counts.items()):
            print(f"  structure_guard {verdict:<30} : {count}")
        for disp, count in sorted(disp_counts.items()):
            print(f"  disposition     {disp:<30} : {count}")
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
            "deduplicated_component_smiles",
            "structure_guard",
            "label_guard",
            "candidate_chebi_id",
            "candidate_chebi_name",
            "all_candidate_chebi_ids",
            "chebi_match_type",
            "curation_disposition",
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
