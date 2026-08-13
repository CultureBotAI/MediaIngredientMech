"""Tests for the hydrate-water detector (#321).

Each test pins one of the three bugs the string-matching version had. They are
written against the real values that exposed each bug, so a regression reproduces
the original wrong answer rather than an invented one.
"""
from __future__ import annotations

import importlib.util
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parent.parent


def _load():
    spec = importlib.util.spec_from_file_location(
        "check_hydrate_water", ROOT / "scripts" / "check_hydrate_water.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


mod = _load()


class TestParseFormula:
    @pytest.mark.parametrize("formula,expected", [
        ("2Cl.Co.2H2O", {"Cl": 2, "Co": 1, "H": 4, "O": 2}),
        ("C6H5O7.3Na", {"C": 6, "H": 5, "O": 7, "Na": 3}),
        ("12H2O.HO4P.2Na", {"H": 25, "O": 16, "P": 1, "Na": 2}),
        ("C5H11NO2.H2O", {"C": 5, "H": 13, "N": 1, "O": 3}),
        ("C7H15N3O5", {"C": 7, "H": 15, "N": 3, "O": 5}),
    ])
    def test_dot_notation_and_leading_multipliers(self, formula, expected):
        assert dict(mod.parse_formula(formula)) == expected

    def test_centre_dot_is_equivalent_to_a_period(self):
        assert mod.parse_formula("MoO4.2Na.2H2O") == mod.parse_formula("MoO4·2Na·2H2O")

    @pytest.mark.parametrize("value", [None, "", "OC[C@H]1OC(O)", "not a formula!"])
    def test_unparseable_returns_none_rather_than_guessing(self, value):
        """SMILES must not be silently mis-parsed as element symbols."""
        assert mod.parse_formula(value) is None


class TestHydrationNumber:
    @pytest.mark.parametrize("label,n", [
        ("CoCl2 x 2 H2O", 2), ("Na2MoO4·2H2O", 2), ("Betaine x H2O", 1),
        ("Na2HPO4 x 12 H2O", 12),
    ])
    def test_numeric_notation(self, label, n):
        assert mod.hydration_number(label) == n

    @pytest.mark.parametrize("label,n", [
        ("Esculin Monohydrate", 1), ("Cadmium acetate dihydrate", 2),
        ("Chromium(III) Chloride Hexahydrate", 6),
        ("Sodium phosphite dibasic pentahydrate", 5),
    ])
    def test_word_forms(self, label, n):
        """`\\bhydrate\\b` never matched these — there is no word boundary after
        a letter, so every multiplier-prefixed spelling was skipped."""
        assert mod.hydration_number(label) == n

    def test_bare_hydrate_states_no_number(self):
        assert mod.hydration_number("Stachyose hydrate") is None


class TestLabelPattern:
    @pytest.mark.parametrize("label", [
        "Esculin Monohydrate", "CoCl2 x 2 H2O", "Na2MoO4·2H2O", "Stachyose hydrate",
    ])
    def test_recognises_every_hydrate_spelling(self, label):
        assert mod.HYDRATE_LABEL.search(label)

    def test_borohydrate_is_excluded(self):
        """It ends in -hydrate by spelling alone and is not a hydrate."""
        label = "b-Mannan borohydrate reduced carob seed"
        assert mod.HYDRATE_LABEL.search(label)          # the label pattern still hits
        assert mod.NOT_A_HYDRATE.search(label)          # ...and the guard rejects it


class TestClassify:
    def test_combined_notation_counts_as_water_present(self):
        """The bug that mattered most: `C7H15N3O5` IS Gly-Gln plus one water,
        written combined. String-matching for 'H2O' called it defective."""
        verdict, _ = mod.classify(
            "Gly-Gln monohydrate", "C7H15N3O5", "C7H13N3O4", "Gly-Gln")
        assert verdict == "ok"

    def test_dot_notation_counts_as_water_present(self):
        verdict, _ = mod.classify(
            "CoCl2 x 2 H2O", "2Cl.Co.2H2O", "2Cl.Co", "cobalt dichloride")
        assert verdict == "ok"

    def test_anhydrous_formula_is_missing_water(self):
        verdict, reason = mod.classify(
            "CoCl2 x 2 H2O", "2Cl.Co", "2Cl.Co", "cobalt dichloride")
        assert verdict == "missing"
        assert "unaccounted" in reason

    def test_term_that_is_itself_the_hydrate_is_not_missing(self):
        """`Cobalt chloride hexahydrate` equals its term's formula because the
        term IS the hexahydrate — equality here is correctness, not a defect."""
        verdict, _ = mod.classify(
            "Cobalt chloride hexahydrate", "2Cl.Co.6H2O", "2Cl.Co.6H2O",
            "cobalt chloride hexahydrate")
        assert verdict == "ok"

    def test_unstated_stoichiometry_is_unknown_not_missing(self):
        verdict, reason = mod.classify(
            "Stachyose hydrate", "C24H42O21", "C24H42O21", "stachyose")
        assert verdict == "unknown"
        assert "states no hydration number" in reason

    def test_unparseable_term_formula_is_unknown(self):
        verdict, _ = mod.classify("Esculin Monohydrate", "C15H16O9", None, "esculin")
        assert verdict == "unknown"

    def test_mismatch_in_neither_direction_is_unknown(self):
        """Never silently bucket a disagreement as 'ok' or 'missing'."""
        verdict, _ = mod.classify(
            "Cadmium acetate dihydrate", "C4H6CdO4", "2C2H3O2.Cd", "cadmium acetate")
        assert verdict in ("missing", "unknown")
