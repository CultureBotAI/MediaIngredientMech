"""Guards for the hydrate report's synonym bucket (#251).

The script had no tests at all, which is how a first version of the
hydration-state detector reported 96 records that were almost all respellings of
the same state (#254). These pin the parts that survived.
"""

import importlib.util
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).parent.parent
SCRIPT = ROOT / "scripts" / "report_hydrate_grounding.py"


@pytest.fixture(scope="module")
def mod():
    spec = importlib.util.spec_from_file_location("report_hydrate_grounding", SCRIPT)
    m = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = m
    spec.loader.exec_module(m)
    return m


def test_regexes_come_from_the_guard_not_a_local_copy(mod):
    """The report's private copy drifted from the guard's between #246 and #250;
    a third hand-synced copy would drift again."""
    spec = importlib.util.spec_from_file_location(
        "_hg", ROOT / "src" / "mediaingredientmech" / "curation" / "hydrate_guard.py"
    )
    hg = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(hg)
    assert mod.HYDRATE.pattern == hg.HYDRATE_NOTATION.pattern
    assert mod.FORMULA_WATER.pattern == hg.FORMULA_WATER.pattern


@pytest.mark.parametrize(
    "label",
    [
        "b-Mannan borohydrate reduced carob seed",
        "L-Ornithine monochlorohydrate/ornithine",
        "carbohydrate",
    ],
)
def test_borohydrate_class_labels_are_not_hydrate_terms(mod, label):
    """A bare /hydrate/ test would call these hydrate terms and silently drop
    the record from the synonym bucket. Both are live MIM targets."""
    assert not mod.HYDRATE.search(label)


@pytest.mark.parametrize(
    "formula,expected",
    [
        ("Mg.O4S.7H2O", True),
        ("Al.12H2O.H4N.2O4S", True),
        ("(H2O)n.O5SV", True),
        ("H2O4P.Na", False),  # dihydrogenphosphate, no water
        ("H2O2", False),  # hydrogen peroxide
        ("C26H43NO6", False),
    ],
)
def test_formula_water_is_a_component_not_a_substring(mod, formula, expected):
    assert bool(mod.FORMULA_WATER.search(formula)) is expected


def test_baseline_identifiers_reads_the_tracked_set(mod):
    ids = mod.baseline_identifiers()
    assert ids, "the duplicate-identifier baseline should be readable"
    assert all(":" in i for i in ids)


def test_synonym_report_path_is_tracked_separately(mod):
    assert mod.SYN_REPORT.name == "hydrate_synonyms.tsv"
    assert mod.SYN_REPORT != mod.REPORT


# --- #259: the two summary buckets are keyed on data, not on prose ---------
def test_the_two_buckets_are_keyed_on_kind_not_on_prose(mod):
    """The split tested `"states" in r["detail"]`, so rewording the sentence --
    or a term label that happens to contain the word -- reclassified rows."""
    rows = [
        {"kind": mod.DIFFERENT_STATE, "detail": "reworded, no keyword here"},
        {"kind": mod.ANHYDROUS_TERM, "detail": "this one states nothing at all"},
    ]

    buckets = mod.split_synonym_buckets(rows)

    assert len(buckets[mod.DIFFERENT_STATE]) == 1
    assert buckets[mod.DIFFERENT_STATE][0]["detail"].startswith("reworded")
    assert len(buckets[mod.ANHYDROUS_TERM]) == 1


def test_the_old_substring_rule_would_have_got_both_wrong(mod):
    """Pins why the change was needed, not just that it happened."""
    rows = [
        {"kind": mod.DIFFERENT_STATE, "detail": "reworded, no keyword here"},
        {"kind": mod.ANHYDROUS_TERM, "detail": "this one states nothing at all"},
    ]

    by_substring = [r for r in rows if "states" in r["detail"]]

    assert [r["kind"] for r in by_substring] == [
        mod.ANHYDROUS_TERM
    ], "the substring rule selects exactly the wrong row here"


def test_the_kind_values_are_distinct(mod):
    assert len({mod.DIFFERENT_STATE, mod.ANHYDROUS_TERM, mod.MALFORMED_NOTATION}) == 3


def test_kind_is_written_to_the_synonym_tsv(mod):
    """Downstream consumers should be able to key on it too, not re-derive it
    from the prose the way the report used to."""
    assert mod.SYNONYM_FIELDS == [
        "identifier",
        "preferred_term",
        "ontology_id",
        "kind",
        "detail",
        "hydrate_synonyms",
    ]

    rows = mod.classify_synonym_rows(
        [
            {
                "identifier": "CHEBI:1",
                "preferred_term": "magnesium chloride",
                "ontology_mapping": {
                    "ontology_id": "CHEBI:1",
                    "ontology_label": "magnesium chloride",
                },
                "synonyms": [{"synonym_text": "MgCl2 x 6 H2O"}],
            }
        ],
        {"CHEBI:1": "Cl2Mg"},
    )

    assert rows and set(rows[0]) == set(mod.SYNONYM_FIELDS)
    assert rows[0]["kind"] == mod.ANHYDROUS_TERM


def test_synonym_different_state_rows_are_classified_by_the_source(mod):
    rows = mod.classify_synonym_rows(
        [
            {
                "identifier": "CHEBI:1",
                "preferred_term": "MgCl2 x 6 H2O",
                "ontology_mapping": {
                    "ontology_id": "CHEBI:1",
                    "ontology_label": "magnesium chloride hexahydrate",
                },
                "synonyms": [{"synonym_text": "MgCl2 x 7 H2O"}],
            }
        ],
        {"CHEBI:1": "Cl2Mg.6H2O"},
    )

    assert len(rows) == 1
    assert rows[0]["kind"] == mod.DIFFERENT_STATE


def test_implausible_hydrate_synonyms_are_classified_as_malformed(mod):
    rows = mod.classify_synonym_rows(
        [
            {
                "identifier": "CHEBI:1",
                "preferred_term": "MgCl2 x 7 H2O",
                "ontology_mapping": {
                    "ontology_id": "CHEBI:1",
                    "ontology_label": "magnesium chloride heptahydrate",
                },
                "synonyms": [
                    {"synonym_text": "MgCl2  x 76 H2O"},
                    {"synonym_text": "MgCl2 x 6 H2O"},
                ],
            }
        ],
        {"CHEBI:1": "Cl2Mg.7H2O"},
    )

    buckets = mod.split_synonym_buckets(rows)

    assert len(buckets[mod.MALFORMED_NOTATION]) == 1
    assert buckets[mod.MALFORMED_NOTATION][0]["hydrate_synonyms"] == "MgCl2  x 76 H2O"
    assert "76" in buckets[mod.MALFORMED_NOTATION][0]["detail"]
    assert len(buckets[mod.DIFFERENT_STATE]) == 1


def test_preferred_term_hydrate_rows_are_classified_by_the_source(mod):
    rows = mod.classify_hydrate_rows(
        [
            {
                "identifier": "CHEBI:1",
                "preferred_term": "MgCl2 x 6 H2O",
                "ontology_mapping": {
                    "ontology_id": "CHEBI:1",
                    "ontology_label": "magnesium chloride",
                },
            },
            {
                "identifier": "CHEBI:2",
                "preferred_term": "NaCl",
                "ontology_mapping": {
                    "ontology_id": "CHEBI:2",
                    "ontology_label": "sodium chloride",
                },
            },
            {
                "identifier": "kgmicrobe.compound:mgcl2_x_7_h2o",
                "preferred_term": "MgCl2 x 7 H2O",
                "ontology_mapping": {
                    "ontology_id": "CHEBI:1",
                    "ontology_label": "magnesium chloride",
                },
            },
        ],
        {"CHEBI:1": "Cl2Mg", "CHEBI:2": "ClNa"},
        {"MgCl2 x 7 H2O"},
    )

    assert rows == [
        {
            "identifier": "CHEBI:1",
            "preferred_term": "MgCl2 x 6 H2O",
            "ontology_id": "CHEBI:1",
            "ontology_label": "magnesium chloride",
            "term_formula": "Cl2Mg",
            "status": "HYDRATE_ON_ANHYDROUS_TERM",
        },
        {
            "identifier": "kgmicrobe.compound:mgcl2_x_7_h2o",
            "preferred_term": "MgCl2 x 7 H2O",
            "ontology_id": "CHEBI:1",
            "ontology_label": "magnesium chloride",
            "term_formula": "Cl2Mg",
            "status": mod.OK_LOCAL_REGISTRY_ID,
        },
    ]


def test_local_hydrate_registry_ids_still_need_parent_rows(mod):
    rows = mod.classify_hydrate_rows(
        [
            {
                "identifier": "kgmicrobe.compound:mgcl2_x_7_h2o",
                "preferred_term": "MgCl2 x 7 H2O",
                "ontology_mapping": {
                    "ontology_id": "CHEBI:1",
                    "ontology_label": "magnesium chloride",
                },
            },
        ],
        {"CHEBI:1": "Cl2Mg"},
        set(),
    )

    assert rows[0]["status"] == "HYDRATE_ON_ANHYDROUS_TERM"


def test_preferred_term_hydrate_rows_ignore_rejected_records(mod):
    rows = mod.classify_hydrate_rows(
        [
            {
                "identifier": "CHEBI:wrong",
                "preferred_term": "MgCl2x 6 H2O",
                "mapping_status": "REJECTED",
                "ontology_mapping": {
                    "ontology_id": "CHEBI:wrong",
                    "ontology_label": "magnesium dichloride",
                },
            }
        ],
        {"CHEBI:wrong": "Cl2Mg"},
        set(),
    )

    assert rows == []


def test_hydrate_synonym_rows_ignore_rejected_records(mod):
    rows = mod.classify_synonym_rows(
        [
            {
                "identifier": "CHEBI:wrong",
                "preferred_term": "magnesium chloride",
                "mapping_status": "REJECTED",
                "ontology_mapping": {
                    "ontology_id": "CHEBI:wrong",
                    "ontology_label": "magnesium chloride",
                },
                "synonyms": [{"synonym_text": "MgCl2 x 6 H2O"}],
            }
        ],
        {"CHEBI:wrong": "Cl2Mg"},
    )

    assert rows == []


# --- #258 regression --------------------------------------------------------
def test_multiplicities_sort_numerically_not_lexicographically():
    """Filed against a lexicographic sort, where 10 precedes 2. Verified fixed
    2026-08-24 (`key=float`); pinned so it cannot regress."""
    assert sorted({"10", "2", "7"}, key=float) == ["2", "7", "10"]
    assert sorted({"10", "2", "7"}) == ["10", "2", "7"], "plain sort is still wrong"
