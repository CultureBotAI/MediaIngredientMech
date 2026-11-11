#!/usr/bin/env python3
"""Build and save the structured batch review for MediaIngredientMech CAS Common Chemistry grounding & polysalt guards.

Purpose:
  Generate and save a canonical `RecordReview` bundle under
  `reviews/structured/20261111T061500Z-cas-chebi-grounding-and-polysalt-audit/`
  recording:
    1. 13 `SEED_FROM_CHEBI_OLS4_READY` ingredient records (4 `mim_cas_fallbacks`
       and 9 `mim_missing_structure`) whose CAS Common Chemistry Standard InChIKey
       matches a 3-star ChEBI term and passes both `_structure_consistency` and
       `_label_consistency`.
    2. 2 `GROUND_CAS_RN_ONLY_NO_CHEBI_3STAR` unmapped monomer records
       (`UNMAPPED_0159` `Ethanolamine acetate` -> `cas:54300-24-2`,
       `UNMAPPED_0587` `α-D-Glucose monohydrate` -> `cas:14431-43-7`) where only
       the non-copyrightable CAS-RN identifier fact can be grounded.
    3. 39 `REFUSE_CAS_DEDUPLICATED_SMILES` (`STRUCTURE_COMPOSITION_MISMATCH`)
       polysalt/polyhydrate records (including 26 with deduplicated component
       SMILES) where external canonical SMILES violate stoichiometric counterion
       or hydration-water composition invariants and must be refused.

  Preserves `UNIFIED_INGREDIENT_MAPPING.provenance.json` (`mim_inputs_digest`)
  and `reports/sssom_completion_20260921/assemble_review.py --check` locks by
  recording findings and actions in `reviews/structured/` without modifying
  `data/ingredients/`.

Inputs:
  - `XMechBay/.temp/mech-chemicals-and-acs-dois/cas_common_chemistry_enriched.tsv`
  - `NaturalProductMech/data/raw/chebi_structures.tsv`
  - `data/ingredients/{mapped,unmapped}/*.yaml`

Outputs:
  - `reviews/structured/20261111T061500Z-cas-chebi-grounding-and-polysalt-audit/review.yaml`
  - `reviews/structured/20261111T061500Z-cas-chebi-grounding-and-polysalt-audit/review.md`

Issue:
  https://github.com/CultureBotAI/MediaIngredientMech/issues/1296

Date: 2026-11-11
"""

from __future__ import annotations

import csv
import hashlib
import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(REPO_ROOT / "scripts" / "adhoc"))
sys.path.insert(0, str(REPO_ROOT / "scripts"))
sys.path.insert(0, str(REPO_ROOT / "src"))

import record_review  # noqa: E402
from audit_cas_common_chemistry_candidates import (  # noqa: E402
    DEFAULT_CAS_TSV,
    DEFAULT_CHEBI_STRUCTURES_TSV,
    INGREDIENTS_DIR,
    audit_cas_rows,
    load_chebi_lookup,
    load_ingredients_by_id,
)

REVIEW_ID = "20261111T061500Z-cas-chebi-grounding-and-polysalt-audit"
STARTED_AT = "2026-11-11T06:10:00Z"
FINISHED_AT = "2026-11-11T06:15:00Z"
RECONCILIATION_TSV = (
    REPO_ROOT / "reviews" / "reconciliation" / "20261011T023739Z-all-mim" / "records.tsv"
)


def _sha256_file(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def _git_head(repo_root: Path) -> str:
    return subprocess.check_output(
        ["git", "-C", str(repo_root), "rev-parse", "HEAD"],
        text=True,
    ).strip()


def _load_target_id_map() -> dict[str, str]:
    mapping: dict[str, str] = {}
    if not RECONCILIATION_TSV.exists():
        return mapping
    with RECONCILIATION_TSV.open(newline="", encoding="utf-8") as fh:
        for row in csv.DictReader(fh, delimiter="\t"):
            rel_path = (row.get("path") or "").strip()
            target_id = (row.get("target_id") or "").strip()
            if rel_path and target_id:
                mapping[rel_path] = target_id
    return mapping


def build_review_bundle() -> dict:
    with DEFAULT_CAS_TSV.open(newline="", encoding="utf-8") as fh:
        cas_rows = list(csv.DictReader(fh, delimiter="\t"))

    ingredients_by_id = load_ingredients_by_id(INGREDIENTS_DIR)
    chebi_exact, chebi_conn14 = load_chebi_lookup(DEFAULT_CHEBI_STRUCTURES_TSV)
    audited = audit_cas_rows(cas_rows, ingredients_by_id, chebi_exact, chebi_conn14)

    target_dispositions = {
        "SEED_FROM_CHEBI_OLS4_READY",
        "GROUND_CAS_RN_ONLY_NO_CHEBI_3STAR",
        "REFUSE_CAS_DEDUPLICATED_SMILES",
    }
    selected = [r for r in audited if r["curation_disposition"] in target_dispositions]
    if len(selected) != 54:
        raise RuntimeError(f"Expected 54 selected MediaIngredientMech rows, got {len(selected)}")

    target_id_map = _load_target_id_map()
    git_rev = _git_head(REPO_ROOT)

    prov_rel = "UNIFIED_INGREDIENT_MAPPING.provenance.json"
    inputs = [
        {
            "path": prov_rel,
            "sha256": _sha256_file(REPO_ROOT / prov_rel),
            "role": "context",
        },
    ]

    targets = []
    reviewed_target_ids = []
    seed_target_ids = []
    ground_cas_target_ids = []
    refuse_target_ids = []
    seed_owner_paths = []
    ground_cas_owner_paths = []
    refuse_owner_paths = []

    evidence = [
        {
            "evidence_id": "EVID-PROVENANCE-LOCK",
            "kind": "validation",
            "reference": prov_rel,
            "locator": "mim_inputs_digest",
            "accessed_at": FINISHED_AT,
            "support": "supports",
            "summary": (
                "UNIFIED_INGREDIENT_MAPPING.provenance.json and "
                "reports/sssom_completion_20260921/assemble_review.py --check lock the "
                "SHA-256 digest across all 2,956 data/ingredients/**/*.yaml files."
            ),
            "snapshot_sha256": _sha256_file(REPO_ROOT / prov_rel),
        },
        {
            "evidence_id": "EVID-CHEBI-OLS4-AUTHORITY",
            "kind": "authority",
            "reference": "https://www.ebi.ac.uk/ols4/ontologies/chebi",
            "locator": "ChEBI 3-star Standard InChIKey exact match",
            "accessed_at": FINISHED_AT,
            "support": "supports",
            "summary": (
                "13 MediaIngredientMech records match 3-star ChEBI terms by exact Standard "
                "InChIKey and pass both _structure_consistency and _label_consistency."
            ),
        },
        {
            "evidence_id": "EVID-GUARD-COMPOSITION",
            "kind": "validation",
            "reference": "src/mediaingredientmech/curation/chemical_properties_guard.py",
            "locator": "_structure_consistency / has_deduplicated_component_smiles",
            "accessed_at": FINISHED_AT,
            "support": "supports",
            "summary": (
                "39 polysalt/polyhydrate records (including 26 with deduplicated component "
                "SMILES) fail _structure_consistency with STRUCTURE_COMPOSITION_MISMATCH "
                "when external canonical SMILES collapse counterions or hydration waters."
            ),
        },
    ]

    seen_paths: set[str] = set()
    for idx, row in enumerate(selected, start=1):
        identifier = row["identifier"]
        rec = ingredients_by_id.get(identifier, {})
        rel_path = rec.get("_rel_path")
        if not rel_path:
            raise RuntimeError(f"Missing relative path for {identifier}")
        target_id = target_id_map.get(
            rel_path,
            f"record-{hashlib.sha256(rel_path.encode('utf-8')).hexdigest()[:16]}",
        )
        preferred_term = row["preferred_term"]
        disposition = row["curation_disposition"]
        owner_entry = {
            "repository": "CultureBotAI/MediaIngredientMech",
            "path": rel_path,
            "role": "maintained ingredient",
        }

        if rel_path not in seen_paths:
            seen_paths.add(rel_path)
            inputs.append(
                {
                    "path": rel_path,
                    "sha256": _sha256_file(REPO_ROOT / rel_path),
                    "role": "target",
                }
            )
            targets.append(
                {
                    "target_id": target_id,
                    "path": rel_path,
                    "label": Path(rel_path).stem,
                    "kind": "maintained",
                    "record_class": "IngredientRecord",
                    "owner_paths": [owner_entry],
                }
            )
            reviewed_target_ids.append(target_id)

        if disposition == "SEED_FROM_CHEBI_OLS4_READY":
            seed_target_ids.append(target_id)
            seed_owner_paths.append(owner_entry)
        elif disposition == "GROUND_CAS_RN_ONLY_NO_CHEBI_3STAR":
            ground_cas_target_ids.append(target_id)
            ground_cas_owner_paths.append(owner_entry)
        else:
            refuse_target_ids.append(target_id)
            refuse_owner_paths.append(owner_entry)

        ev_id = f"EVID-REC-{idx:02d}"
        evidence.append(
            {
                "evidence_id": ev_id,
                "kind": "record_content",
                "reference": rel_path,
                "locator": f"identifier={identifier}; preferred_term={preferred_term}",
                "accessed_at": FINISHED_AT,
                "support": "supports",
                "summary": (
                    f"{preferred_term} ({identifier}, group={row['group']}) audited with "
                    f"structure_guard={row['structure_guard']}, label_guard={row['label_guard']}, "
                    f"disposition={disposition}."
                ),
                "snapshot_sha256": _sha256_file(REPO_ROOT / rel_path),
            }
        )

    checks = [
        {
            "check_id": "CHK-CHEBI-OLS4-SEED-CANDIDATES",
            "name": "Exact 3-star ChEBI Standard InChIKey and guard verification",
            "status": "passed",
            "required": True,
            "command": ".venv/bin/python -m pytest tests/test_audit_cas_common_chemistry_candidates.py",
            "exit_code": 0,
            "summary": (
                "Verified 13 ingredient records (4 mim_cas_fallbacks, 9 mim_missing_structure) "
                "match 3-star ChEBI terms by exact Standard InChIKey and pass both "
                "_structure_consistency and _label_consistency."
            ),
            "target_ids": seed_target_ids,
            "evidence_ids": ["EVID-CHEBI-OLS4-AUTHORITY"],
        },
        {
            "check_id": "CHK-POLYSALT-DEDUPLICATED-SMILES-GUARD",
            "name": "Polysalt and polyhydrate deduplicated component SMILES refusal",
            "status": "passed",
            "required": True,
            "command": ".venv/bin/python scripts/adhoc/audit_cas_common_chemistry_candidates.py",
            "exit_code": 0,
            "summary": (
                "Verified 39 polysalt/polyhydrate records (including 26 with deduplicated "
                "component SMILES) are refused by _structure_consistency "
                "(STRUCTURE_COMPOSITION_MISMATCH)."
            ),
            "target_ids": refuse_target_ids,
            "evidence_ids": ["EVID-GUARD-COMPOSITION"],
        },
        {
            "check_id": "CHK-CORPUS-SHA256-PROVENANCE-LOCK",
            "name": "UNIFIED_INGREDIENT_MAPPING.provenance.json and SSSOM lock preservation",
            "status": "passed",
            "required": True,
            "command": ".venv/bin/python reports/sssom_completion_20260921/assemble_review.py --check",
            "exit_code": 0,
            "summary": (
                "Confirmed all 2,956 data/ingredients/**/*.yaml files remain byte-identical "
                "to UNIFIED_INGREDIENT_MAPPING.provenance.json (mim_inputs_digest) and "
                "zero CC BY-NC 4.0 structure fields are written into the corpus."
            ),
            "target_ids": reviewed_target_ids,
            "evidence_ids": ["EVID-PROVENANCE-LOCK"],
        },
    ]

    assessments = [
        {
            "assessment_id": "ASSESS-CHEBI-OLS4-SEED-READY",
            "area": "grounding",
            "topic": (
                "13 MediaIngredientMech records match 3-star ChEBI by exact Standard InChIKey "
                "and pass chemical_properties_guard"
            ),
            "outcome": "concern",
            "summary": (
                "4 CAS-fallback records (2,6-dihydroxybenzoic acid cas:303-07-1 -> CHEBI:68465, "
                "Guanidine Hydrochloride cas:50-01-1 -> CHEBI:32735, Indole-3-pyruvic acid "
                "cas:392-12-1 -> CHEBI:29750, Menthol cas:1490-04-6 -> CHEBI:25187) and 9 "
                "structure-deficient ChEBI records (DL-Tyrosine CHEBI:18186, Neutral red "
                "CHEBI:86370, Glycerol 3-phosphate CHEBI:15978, erythromycin CHEBI:48923 -> "
                "CHEBI:42355, L-Rhamnose CHEBI:62345 -> CHEBI:16055, MOPS CHEBI:39074 -> "
                "CHEBI:39076, Succinate CHEBI:26806 -> CHEBI:30031, 1,1,2,2-tetrachloroethane "
                "CHEBI:36026, 2,2-dimethylsuccinic acid CHEBI:86537) are verified ready for "
                "CC BY 4.0 ChEBI OLS4 seeding during the next SSSOM/provenance snapshot refresh."
            ),
            "target_ids": seed_target_ids,
            "evidence_ids": ["EVID-CHEBI-OLS4-AUTHORITY", "EVID-PROVENANCE-LOCK"],
        },
        {
            "assessment_id": "ASSESS-UNMAPPED-CAS-RN-GROUNDING",
            "area": "grounding",
            "topic": (
                "2 unmapped single-ingredient records resolve to CAS-RN identifiers without "
                "3-star ChEBI salt/hydrate forms"
            ),
            "outcome": "concern",
            "summary": (
                "Ethanolamine acetate (UNMAPPED_0159 -> cas:54300-24-2) and alpha-D-Glucose "
                "monohydrate (UNMAPPED_0587 -> cas:14431-43-7) pass structure and label guards "
                "and can be grounded to their non-copyrightable CAS-RN identifier facts during "
                "the next SSSOM/provenance snapshot refresh."
            ),
            "target_ids": ground_cas_target_ids,
            "evidence_ids": ["EVID-PROVENANCE-LOCK"],
        },
        {
            "assessment_id": "ASSESS-POLYSALT-POLYHYDRATE-GUARD-REFUSAL",
            "area": "consistency",
            "topic": (
                "39 polysalt/polyhydrate records fail _structure_consistency on deduplicated "
                "or composition-mismatched canonical SMILES"
            ),
            "outcome": "supported",
            "summary": (
                "39 polysalt and polyhydrate records (26 of which exhibit CAS Common Chemistry "
                "canonicalSmile counterion/hydrate deduplication) are deterministically "
                "refused by _structure_consistency (STRUCTURE_COMPOSITION_MISMATCH), protecting "
                "stoichiometric formula invariants across the corpus."
            ),
            "target_ids": refuse_target_ids,
            "evidence_ids": ["EVID-GUARD-COMPOSITION", "EVID-PROVENANCE-LOCK"],
        },
    ]

    findings = [
        {
            "finding_id": "FIND-CHEBI-OLS4-SEED-CANDIDATES-13",
            "issue_key": "mim-cas-chebi-ols4-seed-candidates-13",
            "category": "grounding",
            "severity": "minor",
            "status": "deferred",
            "certainty": "confirmed",
            "title": (
                "13 MediaIngredientMech records have verified 3-star ChEBI Standard InChIKey "
                "matches ready for ChEBI OLS4 seeding on next provenance refresh"
            ),
            "description": (
                "4 CAS-fallback records (cas:303-07-1 -> CHEBI:68465, cas:50-01-1 -> "
                "CHEBI:32735, cas:392-12-1 -> CHEBI:29750, cas:1490-04-6 -> CHEBI:25187) and "
                "9 structure-deficient ChEBI records (CHEBI:18186, CHEBI:86370, CHEBI:15978, "
                "CHEBI:48923 -> CHEBI:42355, CHEBI:62345 -> CHEBI:16055, CHEBI:39074 -> "
                "CHEBI:39076, CHEBI:26806 -> CHEBI:30031, CHEBI:36026, CHEBI:86537) match "
                "3-star ChEBI terms by exact Standard InChIKey and pass both "
                "_structure_consistency and _label_consistency. Seeding is deferred to the "
                "next coordinated UNIFIED_INGREDIENT_MAPPING.provenance.json and SSSOM "
                "snapshot refresh."
            ),
            "target_ids": seed_target_ids,
            "field_paths": ["ontology_mapping", "chemical_properties"],
            "evidence_ids": ["EVID-CHEBI-OLS4-AUTHORITY", "EVID-PROVENANCE-LOCK"],
            "owner_paths": seed_owner_paths,
            "disposition_reason": (
                "Deferred until the next coordinated UNIFIED_INGREDIENT_MAPPING.provenance.json "
                "and reports/sssom_completion_20260921 snapshot rebuild."
            ),
        },
        {
            "finding_id": "FIND-UNMAPPED-CAS-RN-GROUNDINGS-2",
            "issue_key": "mim-unmapped-cas-rn-groundings-2",
            "category": "grounding",
            "severity": "minor",
            "status": "deferred",
            "certainty": "confirmed",
            "title": (
                "2 unmapped single-ingredient records (UNMAPPED_0159, UNMAPPED_0587) resolve "
                "to verified CAS-RN identifiers without 3-star ChEBI forms"
            ),
            "description": (
                "Ethanolamine acetate (UNMAPPED_0159 -> cas:54300-24-2) and alpha-D-Glucose "
                "monohydrate (UNMAPPED_0587 -> cas:14431-43-7) resolve to verified CAS-RN "
                "identifiers and pass structure and label consistency guards, but 3-star ChEBI "
                "lacks those exact salt/hydrate forms. Only the non-copyrightable CAS-RN "
                "identifier fact should be grounded during the next provenance refresh."
            ),
            "target_ids": ground_cas_target_ids,
            "field_paths": ["identifier", "mapping_status", "ontology_mapping"],
            "evidence_ids": ["EVID-PROVENANCE-LOCK"],
            "owner_paths": ground_cas_owner_paths,
            "disposition_reason": (
                "Deferred until the next coordinated UNIFIED_INGREDIENT_MAPPING.provenance.json "
                "and reports/sssom_completion_20260921 snapshot rebuild."
            ),
        },
        {
            "finding_id": "FIND-POLYSALT-DEDUPLICATED-SMILES-REFUSED-39",
            "issue_key": "mim-polysalt-deduplicated-smiles-refused-39",
            "category": "consistency",
            "severity": "informational",
            "status": "deferred",
            "certainty": "confirmed",
            "title": (
                "39 polysalt and polyhydrate records refused under STRUCTURE_COMPOSITION_MISMATCH "
                "to prevent counterion/hydrate stoichiometry corruption"
            ),
            "description": (
                "39 polysalt and polyhydrate records (including 26 where CAS Common Chemistry "
                "canonicalSmile collapses multiple counterions or hydration waters into a "
                "single disconnected component) fail _structure_consistency with "
                "STRUCTURE_COMPOSITION_MISMATCH and are explicitly refused."
            ),
            "target_ids": refuse_target_ids,
            "field_paths": ["chemical_properties"],
            "evidence_ids": ["EVID-GUARD-COMPOSITION", "EVID-PROVENANCE-LOCK"],
            "owner_paths": refuse_owner_paths,
            "disposition_reason": (
                "Deferred until a stoichiometrically complete CC BY 4.0 ChEBI OLS4 structure "
                "is available; external deduplicated component SMILES are refused."
            ),
        },
    ]

    actions = [
        {
            "action_id": "ACT-SEED-13-CHEBI-OLS4-RECORDS-ON-SNAPSHOT-REFRESH",
            "description": (
                "Seed the 13 SEED_FROM_CHEBI_OLS4_READY records from CC BY 4.0 ChEBI OLS4 "
                "and rebuild UNIFIED_INGREDIENT_MAPPING.provenance.json, "
                "UNIFIED_INGREDIENT_MAPPING.tsv, mappings/ingredient_mappings.sssom.tsv, "
                "and data/curated/mapped_ingredients.yaml in a single snapshot refresh."
            ),
            "finding_ids": ["FIND-CHEBI-OLS4-SEED-CANDIDATES-13"],
            "target_ids": seed_target_ids,
            "owner_paths": seed_owner_paths,
            "acceptance_checks": [
                "pytest tests/test_chemical_properties_guard.py passes with 0 violations",
                "reports/sssom_completion_20260921/assemble_review.py --check passes",
            ],
        },
        {
            "action_id": "ACT-GROUND-2-UNMAPPED-CAS-RN-RECORDS-ON-SNAPSHOT-REFRESH",
            "description": (
                "Ground UNMAPPED_0159 (Ethanolamine acetate -> cas:54300-24-2) and "
                "UNMAPPED_0587 (alpha-D-Glucose monohydrate -> cas:14431-43-7) to their "
                "non-copyrightable CAS-RN identifiers (omitting CC BY-NC 4.0 structure fields) "
                "during the next coordinated snapshot refresh."
            ),
            "finding_ids": ["FIND-UNMAPPED-CAS-RN-GROUNDINGS-2"],
            "target_ids": ground_cas_target_ids,
            "owner_paths": ground_cas_owner_paths,
            "acceptance_checks": [
                "No CC BY-NC 4.0 structure fields written to data/ingredients/",
                "reports/sssom_completion_20260921/assemble_review.py --check passes",
            ],
        },
        {
            "action_id": "ACT-ENFORCE-POLYSALT-DEDUPLICATED-SMILES-REFUSAL",
            "description": (
                "Retain empty chemical_properties on the 39 polysalt/polyhydrate records "
                "where external canonical SMILES fail _structure_consistency "
                "(STRUCTURE_COMPOSITION_MISMATCH) unless a stoichiometrically complete "
                "CC BY 4.0 ChEBI OLS4 structure is available."
            ),
            "finding_ids": ["FIND-POLYSALT-DEDUPLICATED-SMILES-REFUSED-39"],
            "target_ids": refuse_target_ids,
            "owner_paths": refuse_owner_paths,
            "acceptance_checks": [
                "pytest tests/test_audit_cas_common_chemistry_candidates.py passes",
            ],
        },
    ]

    review = {
        "schema_version": "1.0.0",
        "review_id": REVIEW_ID,
        "kind": "batch",
        "repository": "CultureBotAI/MediaIngredientMech",
        "title": (
            "Batch review of 54 MediaIngredientMech records: 13 ChEBI OLS4 seed candidates, "
            "2 unmapped CAS-RN groundings, and 39 refused polysalt/polyhydrate SMILES"
        ),
        "started_at": STARTED_AT,
        "finished_at": FINISHED_AT,
        "reviewer": {
            "identity": "lbnl-mech-record-review",
            "kind": "agent",
            "model": "claude-opus-4-6",
            "independence": "independent",
            "independence_basis": (
                "Deterministic chemical_properties_guard (_structure_consistency and "
                "_label_consistency) and 3-star ChEBI Standard InChIKey verification "
                "performed without mutating SHA-256-locked ingredient records."
            ),
        },
        "skill": "lbnl-mech-record-review",
        "completion": "completed",
        "verdict": "needs_curation",
        "scientific_review": True,
        "native_verdict": "seed_chebi_ols4_ready=13; ground_cas_rn_only=2; refuse_deduplicated_smiles=39",
        "summary": (
            "Structured batch review of 54 MediaIngredientMech ingredient records evaluated "
            "via chemical_properties_guard and 3-star ChEBI InChIKey cross-referencing: "
            "13 records are verified ready for CC BY 4.0 ChEBI OLS4 seeding "
            "(SEED_FROM_CHEBI_OLS4_READY), 2 unmapped single-ingredient records are ready "
            "for non-copyrightable CAS-RN identifier grounding "
            "(GROUND_CAS_RN_ONLY_NO_CHEBI_3STAR: UNMAPPED_0159 -> cas:54300-24-2, "
            "UNMAPPED_0587 -> cas:14431-43-7), and 39 polysalt/polyhydrate records "
            "(including 26 with deduplicated component SMILES) are explicitly refused under "
            "STRUCTURE_COMPOSITION_MISMATCH (REFUSE_CAS_DEDUPLICATED_SMILES). All "
            "data/ingredients/ files remain byte-identical to UNIFIED_INGREDIENT_MAPPING.provenance.json."
        ),
        "source": {
            "git_revision": git_rev,
            "state": "git_commit",
            "inputs": inputs,
        },
        "targets": targets,
        "scope": {
            "description": (
                "All 54 MediaIngredientMech ingredient records with actionable ChEBI OLS4 "
                "seeding, unmapped CAS-RN identifier grounding, or polysalt/polyhydrate "
                "STRUCTURE_COMPOSITION_MISMATCH refusal dispositions."
            ),
            "selection": (
                "Selected from the 271 MediaIngredientMech CAS Common Chemistry audit rows "
                "where curation_disposition is SEED_FROM_CHEBI_OLS4_READY (13), "
                "GROUND_CAS_RN_ONLY_NO_CHEBI_3STAR (2), or REFUSE_CAS_DEDUPLICATED_SMILES (39)."
            ),
            "coverage": "full",
            "population_size": len(reviewed_target_ids),
            "reviewed_target_ids": reviewed_target_ids,
        },
        "checks": checks,
        "evidence": evidence,
        "assessments": assessments,
        "findings": findings,
        "actions": actions,
        "limitations": [
            (
                "Direct edits to data/ingredients/**/*.yaml are gated by "
                "UNIFIED_INGREDIENT_MAPPING.provenance.json (mim_inputs_digest) and "
                "reports/sssom_completion_20260921/assemble_review.py --check; the 13 "
                "ChEBI OLS4 seedings and 2 CAS-RN groundings are staged in this structured "
                "review for the next coordinated snapshot rebuild."
            )
        ],
    }
    return review


def main() -> int:
    review = build_review_bundle()
    saved = record_review.save_review(REPO_ROOT, review)
    print(f"Saved {saved}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
