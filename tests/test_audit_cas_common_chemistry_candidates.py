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
    normalize_cas_formula,
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


def test_audit_cas_rows_catches_deduplicated_component_smiles_and_passes_valid_monomer():
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
    }

    audited = audit_cas_rows(cas_rows, ingredients_by_id)
    by_id = {r["identifier"]: r for r in audited}

    assert by_id["CAS-RN:68399-81-5"]["structure_guard"] == "PASS"
    assert by_id["CAS-RN:68399-81-5"]["label_guard"] == "PASS"

    assert (
        by_id["CAS-RN:17629-30-0"]["structure_guard"]
        == "STRUCTURE_COMPOSITION_MISMATCH"
    )
