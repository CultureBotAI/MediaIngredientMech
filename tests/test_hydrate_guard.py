"""Guards for the hydrate acceptance refusal (#243).

The automated path normalises `MgSO4•7H2O` to `MgSO4`, searches on that, and
used to accept whatever came back — filing a hydrate onto its anhydrous parent
with the original as a `HYDRATE_FORM` synonym. That produced the 32 families of
#218 and the 53 records `just report-hydrate-grounding` lists. #240 fixed the
documentation; this pins the code.
"""

from dataclasses import dataclass, field

import pytest

from mediaingredientmech.curation.hydrate_guard import (
    HydrateMismatch, hydrate_mismatch, is_hydrate_label, term_is_hydrate,
)


@dataclass
class Cand:
    ontology_id: str
    label: str
    synonyms: list = field(default_factory=list)


@pytest.mark.parametrize("label", [
    "MgSO4 x 7 H2O", "MgSO4•7H2O", "CaCl2·2H2O", "Cr2(SO4)3 x n H2O",
    "L-Rhamnose monohydrate", "Cadmium chloride hemipentahydrate",
    "Potassium tellurite hydrate",
])
def test_hydrate_notation_is_detected(label):
    assert is_hydrate_label(label)


@pytest.mark.parametrize("label", [
    "b-Mannan borohydrate reduced carob seed",  # the trap: not a hydrate
    "Sodium hydroxide", "Carbohydrate mix", "Tetrahydrofuran", "Glucose",
])
def test_non_hydrates_are_not_flagged(label):
    assert not is_hydrate_label(label)


def test_refuses_a_hydrate_onto_its_anhydrous_parent():
    """The #218 case, in one assertion."""
    reason = hydrate_mismatch("MgSO4 x 7 H2O", Cand("CHEBI:32599", "magnesium sulfate"))
    assert reason and "CHEBI:32599" in reason
    assert "Section 3" in reason, "the refusal must say what to do instead"


def test_allows_a_hydrate_onto_a_hydrate_term():
    assert hydrate_mismatch(
        "MgSO4 x 7 H2O", Cand("CHEBI:31795", "magnesium sulfate heptahydrate")) is None


def test_allows_when_only_a_synonym_says_hydrate():
    assert hydrate_mismatch(
        "Ceftazidime hydrate",
        Cand("CHEBI:3509", "ceftazidime pentahydrate", ["Ceftazidime hydrate"])) is None


def test_allows_a_non_hydrate_label_onto_anything():
    """The guard is one-directional; the reverse case is #242."""
    assert hydrate_mismatch("MgSO4", Cand("CHEBI:31795", "magnesium sulfate heptahydrate")) is None


def test_formula_lookup_catches_a_hydrate_term_whose_label_is_silent():
    """ChEBI writes some hydrates without saying so: CHEBI:182320
    'Glycocholic acid hydrate' is C26H43NO6."""
    cand = Cand("CHEBI:X", "some salt")
    assert hydrate_mismatch("Foo monohydrate", cand) is not None
    assert hydrate_mismatch("Foo monohydrate", cand, lambda c: "C6H12O6.H2O") is None


def test_formula_water_is_a_component_not_a_substring():
    """`H2O4P` is dihydrogenphosphate — no water at all."""
    cand = Cand("CHEBI:37585", "sodium dihydrogenphosphate")
    assert hydrate_mismatch("NaH2PO4 x 2 H2O", cand, lambda c: "H2O4P.Na") is not None


def test_accept_mapping_raises_and_the_opt_out_works():
    from mediaingredientmech.curation.ingredient_curator import IngredientCurator
    cur = IngredientCurator(curator_name="test")
    rec = {"preferred_term": "MgSO4 x 7 H2O", "mapping_status": "UNMAPPED"}
    cand = Cand("CHEBI:32599", "magnesium sulfate")
    cand.source, cand.score = "CHEBI", 0.99
    with pytest.raises(HydrateMismatch):
        cur.accept_mapping(rec, cand, quality="EXACT_MATCH", auto_enrich=False)
    assert rec["mapping_status"] == "UNMAPPED", "a refused record must be left alone"
    cur.accept_mapping(rec, cand, quality="EXACT_MATCH", auto_enrich=False,
                       allow_hydrate_mismatch=True)
    assert rec["mapping_status"] == "MAPPED"
