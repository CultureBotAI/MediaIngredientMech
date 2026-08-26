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


# --- the script paths (PR #246 review: nothing reached them, which is why the
#     batch refusal handler shipped referencing a non-existent self.stats) -----

import importlib.util
import sys as _sys
from pathlib import Path as _Path

_ROOT = _Path(__file__).parent.parent


def _load_script(name):
    _sys.path.insert(0, str(_ROOT / "scripts"))
    _sys.path.insert(0, str(_ROOT / "src"))
    spec = importlib.util.spec_from_file_location(name, _ROOT / "scripts" / f"{name}.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def test_batch_session_defines_the_counter_its_handler_increments():
    """The handler referenced self.stats, which BatchCurationSession never had —
    so the first refusal aborted the whole batch with an AttributeError."""
    mod = _load_script("batch_curate_unmapped")
    sess = mod.BatchCurationSession.__new__(mod.BatchCurationSession)
    src = (_ROOT / "scripts" / "batch_curate_unmapped.py").read_text()
    assert "self.hydrate_refused = 0" in src, "counter must be initialised"
    assert "self.stats[" not in src, "self.stats does not exist on this class"


def test_every_accept_mapping_caller_handles_the_refusal():
    """`just curate` runs curate_unmapped.py; an uncaught raise ended the session."""
    callers = ["curate_unmapped", "batch_curate", "batch_curate_unmapped",
               "llm_curate_unmapped", "apply_claude_suggestions"]
    missing = []
    for name in callers:
        src = (_ROOT / "scripts" / f"{name}.py").read_text()
        if "accept_mapping(" in src and "HydrateMismatch" not in src:
            missing.append(name)
    assert not missing, f"these call accept_mapping without handling refusal: {missing}"


def test_refusal_is_visible_in_the_batch_report():
    """A refusal that is counted nowhere and printed nowhere is indistinguishable
    from a record that was never seen."""
    src = (_ROOT / "scripts" / "batch_curate_unmapped.py").read_text()
    assert "self.hydrate_refused += 1" in src
    assert "session.hydrate_refused" in src, "must appear in the final report"
    assert "refused_hydrate_on_non_hydrate_term" in src, "must emit a decision row"


def test_llm_curate_callers_do_not_report_a_refusal_as_mapped():
    src = (_ROOT / "scripts" / "llm_curate_unmapped.py").read_text()
    assert "return accept_llm_mapping(" in src, "the caller must honour the return value"


@pytest.mark.parametrize("label", [
    "NiCl2・H2O", "MnSO4 ⋅ H2O", "Cysteine-HCl∙H2O", "Na2MoO4 × H2O",
    "FeSO4.H2O", "MgSO4 . H2O", "VOSO4.nH2O", "VOSO4(H2O)n",
])
def test_separators_this_corpus_actually_uses(label):
    """These are real strings from data/curated. The first version missed all of
    them, so an ingredient ingested as `NiCl2・H2O` was #243 recurring."""
    assert is_hydrate_label(label)


def test_h2o2_is_not_water_of_crystallisation():
    from mediaingredientmech.curation.hydrate_guard import FORMULA_WATER
    assert not FORMULA_WATER.search("H2O2")
    assert FORMULA_WATER.search("Al.12H2O.H4N.2O4S")


def test_formula_lookup_is_reachable_from_the_curator():
    """It was read via getattr(self, ...) and never assigned — dead code."""
    from mediaingredientmech.curation.ingredient_curator import IngredientCurator
    cur = IngredientCurator(curator_name="t", formula_lookup=lambda c: "Al.12H2O.H4N.2O4S")
    rec = {"preferred_term": "Ammonium alum hydrate", "mapping_status": "UNMAPPED"}
    cand = Cand("CHEBI:185255", "Ammonium alum")
    cand.source, cand.score = "CHEBI", 0.99
    cur.accept_mapping(rec, cand, quality="EXACT_MATCH", auto_enrich=False)
    assert rec["mapping_status"] == "MAPPED", "formula water must allow the mapping"


# --- water_multiplicity (#254) ----------------------------------------------
# Two earlier attempts at this shipped wrong, so each trap is pinned.

from mediaingredientmech.curation.hydrate_guard import water_multiplicity  # noqa: E402


@pytest.mark.parametrize("label,expected", [
    # the trap that made `AlCl3.6H2O` read as "3.6": a formula subscript sits
    # immediately before the separator
    ("AlCl3.6H2O", "6"),
    ("(NH4)2Ni(SO4)2.6H2O", "6"),
    ("Ca(NO3)2.4H2O", "4"),
    ("Al2(SO4)3 x 18 H2O", "18"),
    # every separator this corpus uses
    ("(NH4)2Ni(SO4)2・6H2O", "6"),
    ("CoCl2 ∙ 6 H2O", "6"),
    ("MgSO4 × 7 H2O", "7"),
    ("MgSO4 x 6 H2O", "6"),
    # hyphen-separated forms present in the corpus (#256)
    ("ZnSO4-7H2O", "7"),
    ("CuCl2-2H2O", "2"),
    ("Na2MoO4-2H2O", "2"),
    # word forms must equal their digit equivalents
    ("magnesium sulfate hexahydrate", "6"),
    ("sodium citrate dihydrate", "2"),
    ("...;dihydrate", "2"),
    # compound prefix: hemi x penta
    ("Cadmium chloride hemipentahydrate", "2.5"),
    ("something sesquihydrate", "1.5"),
    # a word multiplier wins over unrelated digits in the name
    ("dihydrochloride pentahydrate", "5"),
])
def test_water_multiplicity_reads_the_stated_count(label, expected):
    assert water_multiplicity(label) == expected


@pytest.mark.parametrize("label", [
    "CaCl22H2O",                 # ambiguous: subscript or multiplier?
    "MgSO4 x n H2O",             # explicitly variable
    "VOSO4(H2O)n",
    "Potassium tellurite hydrate",   # unspecified
    "L-Cysteine HCl x H2O",
    "b-Mannan borohydrate reduced carob seed",   # not a hydrate at all
    "Glucose",
])
def test_unstated_or_ambiguous_returns_none_not_one(label):
    """None means 'the label does not say'. Treating it as monohydrate invents
    mismatches against records that genuinely say 6."""
    assert water_multiplicity(label) is None


def test_hexahydrate_and_6H2O_are_the_same_state():
    """Comparing raw tokens reported 96 records as mismatched when almost all
    were respellings (#254)."""
    assert water_multiplicity("CoCl2 x 6 H2O") == water_multiplicity("cobalt chloride hexahydrate")


# --- #257: a digit run above MAX_PLAUSIBLE_WATERS is parse damage -----------
@pytest.mark.parametrize(
    "label",
    ["MgCl2 x 76 H2O", "FeSO43 x 999 H2O", "CoCl2·31H2O"],
)
def test_an_implausible_water_count_reads_as_unstated(label):
    """Reporting 76 does not merely lose information -- it manufactures a
    confident mismatch against every sibling stating a real count."""
    assert water_multiplicity(label) is None


@pytest.mark.parametrize("label", ["Al2(SO4)3 x 18 H2O", "AlK(SO4)2 x 12 H2O",
                                   "Na2SO4 x 10 H2O", "CoCl2·30H2O"])
def test_real_hydration_states_are_not_capped(label):
    """The corpus tops out at 18; the ceiling must clear everything real."""
    assert water_multiplicity(label) is not None


def test_word_forms_are_not_subject_to_the_ceiling():
    """`_COUNT` already bounds them, and `dodecahydrate` cannot be a typo."""
    assert water_multiplicity("magnesium chloride dodecahydrate") == "12"


# --- #256 regression: hyphen-separated hydrates ----------------------------
@pytest.mark.parametrize(
    ("label", "expected"),
    [("MgCl2-6H2O", "6"), ("Na2HPO4-12H2O", "12"), ("MgCl2 - 6 H2O", "6")],
)
def test_hyphen_separated_hydrates_are_read(label, expected):
    """Filed as broken in #256; verified fixed 2026-08-24. Pinned so the
    separator class cannot lose `-` again."""
    assert water_multiplicity(label) == expected


# --- #475: an implausible match is skipped, not fatal ----------------------
@pytest.mark.parametrize(
    ("label", "expected"),
    [
        ("MgSO4 x 76 H2O and MgSO4 x 7 H2O", "7"),
        ("MgCl2  x 76 H2O | MgCl2 x 6 H2O", "6"),
        ("MgCl2 x 76 H2O", None),  # nothing real to fall through to
    ],
)
def test_a_corrupt_count_does_not_swallow_a_real_one_beside_it(label, expected):
    """The digit path used to `search` and give up on the first match, so a
    rejected count abandoned a real one later in the same string. The word path
    has always stepped over a bare `hydrate` to reach an informative form."""
    assert water_multiplicity(label) == expected


def test_both_paths_step_over_an_uninformative_match():
    """Pins the symmetry itself, so the two halves cannot diverge again."""
    assert water_multiplicity("hydrate, specifically the hexahydrate") == "6"
    assert water_multiplicity("x 99 H2O, corrected to x 9 H2O") == "9"
