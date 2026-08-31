"""Pin the near-match review report's risk assessment.

The similarity score is the least useful thing this report produces. The `risks`
column is the point: in this domain the *small* differences are the ones that change
the compound, so a report that surfaces a close candidate without naming what differs
is worse than no report -- it invites exactly the wrong grounding the exact-match pass
is careful to avoid.
"""

from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import pytest

_REPO = Path(__file__).resolve().parent.parent


def _load(name: str):
    spec = importlib.util.spec_from_file_location(name, _REPO / "scripts" / f"{name}.py")
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


report = _load("report_residual_near_matches")


class TestHydrationStateIsAlwaysFlagged:
    """MAPPING_SEMANTICS Section 3: a different hydration state is a different compound."""

    @pytest.mark.parametrize(
        "surface,candidate",
        [
            ("MgSO4 x 7 H2O", "magnesium sulfate"),
            ("Na2S·9H2O", "sodium sulfide"),
            ("CaCl2 (anhydrous)", "calcium chloride dihydrate"),
            ("Copper sulfate pentahydrate", "copper sulfate"),
        ],
    )
    def test_a_hydrate_against_its_parent_is_flagged(self, surface, candidate):
        assert "HYDRATION_STATE" in report.assess_risks(surface, candidate)

    def test_matching_hydration_is_not_flagged(self):
        assert "HYDRATION_STATE" not in report.assess_risks("MgSO4 x 7 H2O", "MgSO4 x 7 H2O")


class TestFormulaDigitsAreFlagged:
    """`H3BO4` against `H3BO3` is one character and a different species.

    No similarity score separates these -- they are 0.9+ similar -- so the only thing
    that can protect a curator is naming the difference.
    """

    def test_a_differing_formula_digit_is_flagged(self):
        assert "FORMULA_DIGITS" in report.assess_risks("H3BO4", "H3BO3")

    def test_an_identical_formula_is_not_flagged(self):
        assert "FORMULA_DIGITS" not in report.assess_risks("H3BO3", "H3BO3")


class TestStereochemistryIsFlagged:
    @pytest.mark.parametrize(
        "surface,candidate",
        [
            ("DL-Serine", "serine"),
            ("DL-Serine", "L-serine"),
            ("D-Glucose", "L-glucose"),
        ],
    )
    def test_a_stereo_difference_is_flagged(self, surface, candidate):
        assert "STEREOCHEMISTRY" in report.assess_risks(surface, candidate)

    def test_matching_stereo_is_not_flagged(self):
        assert "STEREOCHEMISTRY" not in report.assess_risks("D-Glucose", "D-glucose")


class TestSaltAndPhysicalStateAreFlagged:
    def test_a_salt_form_difference_is_flagged(self):
        assert "SALT_OR_ION_FORM" in report.assess_risks(
            "Sodium glycerophosphate", "sn-glycero-3-monophosphate(2-)"
        )

    def test_a_physical_state_difference_is_flagged(self):
        assert "PHYSICAL_STATE" in report.assess_risks("Oxygen gas", "dioxygen")

    def test_a_surviving_concentration_is_flagged(self):
        assert "CONCENTRATION" in report.assess_risks("5% Na2S solution", "sodium sulfide")


class TestTheSafestRowsAreMarkedSo:
    def test_an_identical_name_carries_no_risk(self):
        assert report.assess_risks("Sodium Glycerophosphate", "Sodium Glycerophosphate") == []

    def test_a_word_order_difference_only_carries_no_risk(self):
        """Token set equality means nothing chemical differs."""
        assert report.assess_risks("acid citric", "citric acid") == []

    def test_a_plain_extra_word_is_the_residual_category(self):
        assert report.assess_risks("DI Water", "water") == ["TOKEN_DIFFERENCE"]


class TestQueryGeneration:
    """The full label is rarely a substring of any ontology label."""

    def test_uninformative_words_are_not_searched(self):
        queries = report.search_queries("Trace vitamins solution", "trace vitamins solution",
                                        "trace vitamins solution", lambda t: None)
        assert "solution" not in queries, "searching `solution` returns thousands of terms"
        assert "vitamins" in queries

    def test_formula_expansion_reaches_names_no_string_measure_would(self):
        """`N2 gas` and `dinitrogen` share almost no characters."""
        queries = report.search_queries(
            "N2 gas", "n2 gas", "n2 gas", lambda t: "nitrogen" if t == "N2" else None
        )
        assert "nitrogen" in queries

    def test_the_full_key_is_searched_first(self):
        queries = report.search_queries("citric acid", "citric acid", "citric acid", lambda t: None)
        assert queries[0] == "citric acid"


class TestFormulaTableEntriesReachRealTerms:
    """A formula->name entry is only useful if the name is an actual ontology label.

    These exist so `N2 gas` can reach `dinitrogen`, which shares almost no characters
    with it. An entry naming something no ontology calls it is dead weight that looks
    like coverage -- `N2O` was first written as `nitrous oxide`, which CHEBI does not
    use (it labels CHEBI:17045 `dinitrogen oxide`).
    """

    GASES = {
        "N2": "dinitrogen",
        "O2": "dioxygen",
        "H2": "dihydrogen",
        "CO2": "carbon dioxide",
        "CO": "carbon monoxide",
        "CH4": "methane",
        "H2S": "hydrogen sulfide",
        "NH3": "ammonia",
        "H2O": "water",
        "N2O": "dinitrogen oxide",
        "SO2": "sulfur dioxide",
    }

    @pytest.mark.parametrize("formula,name", sorted(GASES.items()))
    def test_the_gas_expands_to_its_chebi_label(self, formula, name):
        sys.path.insert(0, str(_REPO / "src"))
        from mediaingredientmech.utils.chemical_normalizer import formula_to_common_name

        assert formula_to_common_name(formula) == name
