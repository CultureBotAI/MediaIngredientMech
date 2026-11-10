"""Unit tests for CAS Common Chemistry candidate guard audit in MediaIngredientMech."""

from __future__ import annotations

import sys
from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT / "scripts" / "adhoc"))
sys.path.insert(0, str(REPO_ROOT / "scripts"))

from audit_cas_common_chemistry_candidates import (  # noqa: E402
    audit_cas_rows,
    has_deduplicated_component_smiles,
    normalize_cas_formula,
    select_best_chebi_candidate,
    strip_inchikey_prefix,
    validate_output_path_is_outside_data,
)
from audit_writers import looks_like_yaml_writer  # noqa: E402


def test_audit_script_is_not_classified_as_yaml_writer():
    script_path = REPO_ROOT / "scripts" / "adhoc" / "audit_cas_common_chemistry_candidates.py"
    assert looks_like_yaml_writer(script_path.read_text(encoding="utf-8")) is False


def test_validate_output_path_refuses_data_directory(tmp_path):
    (tmp_path / "data" / "ingredients").mkdir(parents=True)
    (tmp_path / "reports").mkdir(parents=True)

    with pytest.raises(ValueError, match="Refusing to write CC-BY-NC-4.0"):
        validate_output_path_is_outside_data(
            tmp_path / "data" / "ingredients" / "out.tsv", repo_root=tmp_path
        )

    validate_output_path_is_outside_data(
        tmp_path / "reports" / "cas_audit.tsv", repo_root=tmp_path
    )


def test_normalize_cas_formula_prefers_inchi_formula_layer():
    assert (
        normalize_cas_formula(
            "C<sub>18</sub>H<sub>32</sub>O<sub>16</sub>·5H<sub>2</sub>O",
            "InChI=1S/C18H32O16.5H2O/c19-1-5-9(23)12(26)15(29)17(32-5)31-4-8-11(25)14(28)16(30)18(33-8)34-7(3-21)10(24)13(27)6(22)2-20;;;;;/h5-30H,1-4H2;5*1H2",
        )
        == "C18H32O16.5H2O"
    )
    assert strip_inchikey_prefix("InChIKey=RZQXOGQSPBYUKH-UHFFFAOYSA-N") == (
        "RZQXOGQSPBYUKH-UHFFFAOYSA-N"
    )
    assert (
        has_deduplicated_component_smiles(
            "C18H32O16·5H2O",
            "OCC1OC(OC2(CO)OC(CO)C(O)C2O)C(O)C(O)C1OCC3OC(O)C(O)C(O)C3O.O",
            "InChI=1S/C18H32O16.5H2O/c19-1-5-9(23)12(26)15(29)17(32-5)31-4-8-11(25)14(28)16(30)18(33-8)34-7(3-21)10(24)13(27)6(22)2-20;;;;;/h5-30H,1-4H2;5*1H2",
        )
        is True
    )


def test_audit_cas_rows_classifies_deduplicated_smiles_chebi_ready_and_unmapped_cas_rn():
    cas_rows = [
        {
            "group": "mim_cas_fallbacks",
            "mech": "MediaIngredientMech",
            "identifier": "CAS-RN:68399-81-5",
            "query_name": "TAPSO",
            "cas_rn": "68399-81-5",
            "cas_name": "1-Propanesulfonic acid, 2-hydroxy-3-[[2-hydroxy-1,1-bis(hydroxymethyl)ethyl]amino]-",
            "molecular_formula": "C7H17NO7S",
            "canonical_smiles": "O=S(=O)(O)CC(O)CNC(CO)(CO)CO",
            "inchi": "InChI=1S/C7H17NO7S/c9-2-7(3-10,4-11)8-1-6(12)5-16(13,14)15/h6,8-12H,1-5H2,(H,13,14,15)",
            "inchikey": "InChIKey=RZQXOGQSPBYUKH-UHFFFAOYSA-N",
            "synonyms_sample": "TAPSO; 3-[N-Tris(hydroxymethyl)methylamino]-2-hydroxypropanesulfonic acid",
        },
        {
            "group": "mim_cas_fallbacks",
            "mech": "MediaIngredientMech",
            "identifier": "CAS-RN:17629-30-0",
            "query_name": "D-Raffinose pentahydrate",
            "cas_rn": "17629-30-0",
            "cas_name": "α-D-Galactopyranoside, β-D-fructofuranosyl O-α-D-glucopyranosyl-(1→6)-, hydrate (1:5)",
            "molecular_formula": "C18H32O16·5H2O",
            # CAS canonicalSmile collapses 5H2O into a single `.O`!
            "canonical_smiles": "OCC1OC(OC2(CO)OC(CO)C(O)C2O)C(O)C(O)C1OCC3OC(O)C(O)C(O)C3O.O",
            "inchi": "InChI=1S/C18H32O16.5H2O/c19-1-5-9(23)12(26)15(29)17(32-5)31-4-8-11(25)14(28)16(30)18(33-8)34-7(3-21)10(24)13(27)6(22)2-20;;;;;/h5-30H,1-4H2;5*1H2",
            "inchikey": "InChIKey=KJXSIXMJHQSKOD-UHFFFAOYSA-N",
            "synonyms_sample": "D-Raffinose pentahydrate",
        },
        {
            "group": "mim_unmapped_single",
            "mech": "MediaIngredientMech",
            "identifier": "UNMAPPED_0159",
            "query_name": "Ethanolamine acetate",
            "cas_rn": "54300-24-2",
            "cas_name": "Acetic acid, compd. with 2-aminoethanol (1:1)",
            "molecular_formula": "C2H7NO·C2H4O2",
            "canonical_smiles": "CC(=O)O.NCCO",
            "inchi": "InChI=1S/C2H7NO.C2H4O2/c3-1-2-4;1-2(3)4/h4H,1-3H2;1H3,(H,3,4)",
            "inchikey": "InChIKey=VVLAIYIMMFWRFW-UHFFFAOYSA-N",
            "synonyms_sample": "Ethanolamine acetate; 2-Aminoethanol acetate",
        },
    ]
    ingredients_by_id = {
        "CAS-RN:68399-81-5": {
            "identifier": "CAS-RN:68399-81-5",
            "preferred_term": "TAPSO",
        },
        "CAS-RN:17629-30-0": {
            "identifier": "CAS-RN:17629-30-0",
            "preferred_term": "D-Raffinose pentahydrate",
        },
        "UNMAPPED_0159": {
            "identifier": "UNMAPPED_0159",
            "preferred_term": "Ethanolamine acetate",
        },
    }
    chebi_exact = {
        "RZQXOGQSPBYUKH-UHFFFAOYSA-N": ("CHEBI:46761", "TAPSO"),
    }

    audited = audit_cas_rows(cas_rows, ingredients_by_id, chebi_exact=chebi_exact)
    by_id = {r["identifier"]: r for r in audited}

    assert by_id["CAS-RN:68399-81-5"]["structure_guard"] == "PASS"
    assert by_id["CAS-RN:68399-81-5"]["label_guard"] == "PASS"
    assert by_id["CAS-RN:68399-81-5"]["candidate_chebi_id"] == "CHEBI:46761"
    assert by_id["CAS-RN:68399-81-5"]["curation_disposition"] == "SEED_FROM_CHEBI_OLS4_READY"

    assert (
        by_id["CAS-RN:17629-30-0"]["structure_guard"]
        == "STRUCTURE_COMPOSITION_MISMATCH"
    )
    assert by_id["CAS-RN:17629-30-0"]["deduplicated_component_smiles"] == "true"
    assert (
        by_id["CAS-RN:17629-30-0"]["curation_disposition"]
        == "REFUSE_CAS_DEDUPLICATED_SMILES"
    )

    assert by_id["UNMAPPED_0159"]["structure_guard"] == "PASS"
    assert by_id["UNMAPPED_0159"]["label_guard"] == "PASS"
    assert (
        by_id["UNMAPPED_0159"]["curation_disposition"]
        == "GROUND_CAS_RN_ONLY_NO_CHEBI_3STAR"
    )


def test_select_best_chebi_candidate_ranks_multiple_conn14_candidates_by_label_consistency():
    candidates = [
        ("CHEBI:4167", "D-glucopyranose"),
        ("CHEBI:17634", "D-glucose"),
        ("CHEBI:42758", "aldehydo-D-glucose"),
    ]
    best_id, best_name, all_ids = select_best_chebi_candidate("D-Glucose", candidates)
    assert best_id == "CHEBI:17634"
    assert best_name == "D-glucose"
    assert all_ids == "CHEBI:4167|CHEBI:17634|CHEBI:42758"

    # Also test hydrate / stereoisomer ranking when exact match is absent
    hydrate_candidates = [
        ("CHEBI:10001", "raffinose"),
        ("CHEBI:10002", "raffinose pentahydrate"),
    ]
    best_h_id, best_h_name, all_h_ids = select_best_chebi_candidate(
        "D-Raffinose pentahydrate", hydrate_candidates
    )
    assert best_h_id == "CHEBI:10002"
    assert best_h_name == "raffinose pentahydrate"
    assert all_h_ids == "CHEBI:10001|CHEBI:10002"
