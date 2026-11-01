"""Exact source-label holds reject false identities without inventing owners (#1025)."""

import csv
import importlib.util
from pathlib import Path

import pytest

ROOT = Path(__file__).parents[1]
SPEC = importlib.util.spec_from_file_location("source_hold_gate", ROOT / "scripts/check_unified_rejections.py")
gate = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(gate)

HEADER = "ingredient_name\trejected_id\tmim_id\treason\n"
REVIEWED_PAIRS = {
    "1 M K2HPO4": "CHEBI:131527",
    "1 M KH2PO4": "CHEBI:63036",
    "1 M Sodium acetate solution": "CHEBI:32954",
    "1 M Tris base (pH 8)": "CHEBI:9754",
    "1 N NaOH": "CHEBI:32145",
    "10% Glucose solution": "CHEBI:17234",
    "25% HCl (7.7 M)": "CHEBI:17883",
    "5% L-Cysteine·HCl·H2O solution": "CHEBI:91248",
    "5% Na2S·9H2O solution": "CHEBI:76209",
    "8% NaHCO3 solution": "CHEBI:32139",
    "Cyanocobalamin (Vitamin B12)": "CHEBI:176843",
    "MnSO4·xH2O": "CHEBI:86360",
    "1 M CaCl2 solution": "CHEBI:3312",
    "1 M K2HPO4 solution": "CHEBI:131527",
    "1 M MgCl2 solution": "CHEBI:6636",
    "1 M Sodium fumarate solution": "CHEBI:115156",
    "1 N KOH": "CHEBI:32035",
    "2 M NH4Cl solution": "CHEBI:31206",
    "3% L-Cysteine HCl x H2O solution": "CHEBI:91248",
    "3% Na2S x 9 H2O solution": "CHEBI:76209",
    "4 M NH4Cl solution": "CHEBI:31206",
    "5% Na2S x 9 H2O solution": "CHEBI:76209",
    "Ethanol (95 %)": "CHEBI:16236",
    "FeSO4 x 7 H2O (0.1% w/v in 0.1 N H2SO4)": "CHEBI:75836",
    "HEPES buffer pH 7.8": "CHEBI:42334",
    "KOH solution": "CHEBI:32035",
    "NaOH (1 N)": "CHEBI:32145",
    "Sulfuric acid (concentrated)": "CHEBI:26836",
    "Tricine (pH 8)": "CHEBI:46760",
    "MnSO4 x xH2O": "CHEBI:86360",
    "MnSO4.xH2O": "CHEBI:86360",
    "Cyanocobalamin (B12)": "CHEBI:176843",
    "Vitamin B12 (Cobalamin)": "CHEBI:176843",
}


@pytest.fixture
def export(tmp_path):
    ledger = tmp_path / "holds.tsv"
    artifact = tmp_path / "unified.tsv"

    def write(*rows, ledger_rows="Held preparation\tCHEBI:9\t\tReviewed scope\n"):
        ledger.write_text(HEADER + ledger_rows)
        fields = ("ingredient_name", *gate.IDENTITY_COLUMNS)
        with artifact.open("w", newline="") as stream:
            writer = csv.DictWriter(stream, fieldnames=fields, delimiter="\t")
            writer.writeheader()
            for row in rows or ({"ingredient_name": "Held preparation"},):
                writer.writerow(dict.fromkeys(fields, "") | row)
        return artifact, ledger

    return write


def test_explicit_empty_replacement_is_valid(export):
    assert gate.check(*export()) == []


@pytest.mark.parametrize("column", gate.IDENTITY_COLUMNS)
def test_source_hold_catches_leak_in_every_identity_column(export, column):
    problems = gate.check(*export({"ingredient_name": "Held preparation", column: "CHEBI:9"}))
    assert any(f"republishes rejected CHEBI:9 in {column}" in problem for problem in problems)


def test_source_hold_allows_different_independent_identity(export):
    assert gate.check(*export({"ingredient_name": "Held preparation", "mim_id": "CHEBI:10", "chebi_id": "CHEBI:10"})) == []


def test_source_hold_never_matches_other_empty_identity_rows(export):
    assert gate.check(*export(
        {"ingredient_name": "Held preparation"},
        {"ingredient_name": "Unrelated source label", "culturemech_term_id": "CHEBI:9"},
    )) == []


def test_source_hold_never_globally_bans_same_id(export):
    assert gate.check(*export({"ingredient_name": "Reagent", "mim_id": "CHEBI:9", "chebi_id": "CHEBI:9"})) == []


def test_distinct_holds_can_share_a_rejected_id(export):
    rows = "Held preparation\tCHEBI:9\t\tScope\nOther preparation\tCHEBI:9\t\tScope\n"
    assert gate.check(*export({"ingredient_name": "Held preparation"}, {"ingredient_name": "Other preparation"}, ledger_rows=rows)) == []
    assert any("republishes rejected" in problem for problem in gate.check(*export(
        {"ingredient_name": "Other preparation", "chebi_id": "CHEBI:9"}, ledger_rows=rows)))


def test_one_label_can_hold_two_distinct_ids(export):
    rows = "Held preparation\tCHEBI:9\t\tScope\nHeld preparation\tCHEBI:10\t\tScope\n"
    assert gate.check(*export(ledger_rows=rows)) == []


def test_source_hold_keys_use_nfc_trim_and_casefold(export):
    problems = gate.check(*export(
        {"ingredient_name": "  RE\u0301AGENT  ", "chebi_id": "CHEBI:9"},
        ledger_rows="réagent\tCHEBI:9\t\tScope\n"))
    assert any("republishes rejected" in problem for problem in problems)


@pytest.mark.parametrize("held,other", [
    ("1 M reagent", "2 M reagent"), ("Reagent·H2O", "Reagent"),
    ("D-Reagent", "L-Reagent"), ("Reagent (stock)", "Reagent"),
    ("Reagent x H2O", "Reagent·H2O"), ("1 M reagent", "1  M reagent"),
])
def test_source_hold_does_not_discard_qualifiers(export, held, other):
    assert gate.check(*export({"ingredient_name": other, "chebi_id": "CHEBI:9"},
                             ledger_rows=f"{held}\tCHEBI:9\t\tScope\n")) == []


@pytest.mark.parametrize("rows", [
    "Name\tCHEBI:9\t\n", "Name\tCHEBI:9\tReason\n", "Name\tCHEBI:9\n",
    "\tCHEBI:9\t\tReason\n", "Name\t\t\tReason\n", "Name\tCHEBI:9\t\t \n",
    "Name\tCHEBI:9\t\tReason\textra\n", "Name\tCHEBI\t\tReason\n",
    "Name\tCHEBI:\t\tReason\n", "Name\t:9\t\tReason\n", "Name\tCHEBI:9 10\t\tReason\n",
    "Name\tCHEBI:9\t\tReason\n name \tCHEBI:9\t\tOther reason\n",
    "réagent\tCHEBI:9\t\tReason\nre\u0301agent\tCHEBI:9\t\tOther reason\n",
])
def test_source_hold_malformed_rows_fail_closed(export, rows):
    assert gate.check(*export(ledger_rows=rows))


def test_source_hold_extra_header_column_fails_closed(export):
    artifact, ledger = export()
    ledger.write_text(ledger.read_text().replace("reason\n", "reason\textra\n"))
    assert gate.check(artifact, ledger) == [f"{ledger}: invalid rejection-ledger columns"]


def test_identity_wide_and_exact_label_scopes_coexist(export):
    ledger_rows = "Reviewed reagent\tCHEBI:9\tCHEBI:10\tIdentity review\nHeld preparation\tCHEBI:9\t\tScope review\n"
    assert gate.check(*export({"ingredient_name": "Owned alias", "mim_id": "CHEBI:10"}, ledger_rows=ledger_rows)) == []
    problems = gate.check(*export({"ingredient_name": "Owned alias", "mim_id": "CHEBI:10", "chebi_id": "CHEBI:9"}, ledger_rows=ledger_rows))
    assert any("republishes rejected" in problem for problem in problems)
    problems = gate.check(*export({"ingredient_name": "Reviewed reagent"}, ledger_rows=ledger_rows))
    assert any("lost its curated identity CHEBI:10" in problem for problem in problems)


def test_reviewed_source_hold_cohort_is_unmapped_without_borrowed_metadata():
    """These 33 reviewed labels had no independent MIM owner before ID lookup."""
    with gate.LEDGER.open() as stream:
        holds = [row for row in csv.DictReader(stream, delimiter="\t") if not row["mim_id"]]
    assert {(row["ingredient_name"], row["rejected_id"]) for row in holds} == set(REVIEWED_PAIRS.items())
    assert len(holds) == len(REVIEWED_PAIRS) == 33
    with gate.ARTIFACT.open() as stream:
        rows = list(csv.DictReader(stream, delimiter="\t"))
    for name in REVIEWED_PAIRS:
        matches = [row for row in rows if row["ingredient_name"] == name]
        assert len(matches) == 1, name
        row = matches[0]
        assert row["mapping_status"] == "UNMAPPED", name
        assert all(row[field] == "" for field in (*gate.IDENTITY_COLUMNS, "synonyms")), name
        assert int(row["occurrence_count"]) > 0 and row["example_media"], name
