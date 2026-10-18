"""Published identities must not resurrect a reviewed source mapping rejection."""

import csv
import importlib.util
from pathlib import Path

import pytest

_spec = importlib.util.spec_from_file_location(
    "check_unified_rejections", Path(__file__).parents[1] / "scripts/check_unified_rejections.py"
)
gate = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(gate)


@pytest.fixture
def export(tmp_path):
    ledger = tmp_path / "rejected.tsv"
    ledger.write_text(
        "ingredient_name\trejected_id\tmim_id\treason\n"
        "Trypticase\tCHEBI:78018\tMICRO:0000175\tReviewed detergent mismatch\n"
    )
    row = dict.fromkeys(("ingredient_name", *gate.IDENTITY_COLUMNS), "")
    row.update(ingredient_name="Trypticase", mim_id="MICRO:0000175")
    artifact = tmp_path / "unified.tsv"

    def write(**updates):
        with artifact.open("w", newline="") as handle:
            writer = csv.DictWriter(handle, fieldnames=row, delimiter="\t")
            writer.writeheader()
            writer.writerow(row | updates)
        return artifact, ledger

    return write


@pytest.mark.parametrize("column", gate.IDENTITY_COLUMNS)
def test_rejected_id_is_caught_in_every_identity_column(export, column):
    assert gate.check(*export(**{column: "CHEBI:78018"}))


def test_fixed_row_passes(export):
    assert gate.check(*export()) == []


def test_alias_with_same_identity_is_protected(export):
    assert gate.check(*export(ingredient_name="Trypticase peptone", chebi_id="CHEBI:78018"))


def test_real_detergent_is_not_globally_banned(export):
    assert gate.check(*export(ingredient_name="Dodecylphosphocholine", mim_id="CHEBI:78018", chebi_id="CHEBI:78018")) == []


def test_lost_curated_identity_is_detected(export):
    assert gate.check(*export(mim_id=""))


def test_missing_ledger_fails_closed(export):
    artifact, ledger = export()
    ledger.unlink()
    assert gate.check(artifact, ledger)


def test_ledger_whitespace_cannot_hide_a_rejected_id(export):
    artifact, ledger = export(chebi_id="CHEBI:78018")
    ledger.write_text(ledger.read_text().replace("CHEBI:78018", " CHEBI:78018 "))
    assert gate.check(artifact, ledger)


@pytest.mark.parametrize("text", ["", "ingredient_name\tmim_id\n", "broken\n"])
def test_malformed_ledger_is_not_treated_as_no_rejections(export, text):
    artifact, ledger = export()
    ledger.write_text(text)
    assert gate.check(artifact, ledger)


def test_committed_export_respects_rejections():
    assert gate.check() == []
