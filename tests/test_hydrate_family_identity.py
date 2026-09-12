"""Identity and CAS within hydrate families (#225, #334).

Two defects with one cause: a hydrate and its anhydrous parent are different
substances, and tooling that treats them as one produced both a wrong identifier
and a wrong CAS. #334's own warning is the reason the CAS half matters --
`7791-20-0` sat on the di- and pentahydrate records while belonging to the
hexahydrate, so any CAS-keyed dedup run at the time would have merged the wrong
records.
"""

import csv
from collections import defaultdict
from pathlib import Path

import pytest
import yaml

ROOT = Path(__file__).parent.parent
CURATED = ROOT / "data" / "curated" / "mapped_ingredients.yaml"
SSSOM = ROOT / "mappings" / "ingredient_mappings.sssom.tsv"
MEMBERSHIP = ROOT / "mappings" / "culturemech_recipe_membership.tsv"

LOCAL_SULFATE_HYDRATES = {
    "FeSO4 x 5 H2O": (
        "kgmicrobe.compound:feso4_x_5_h2o",
        "CHEBI:75832",
        "Fe.O4S.5H2O",
        4,
    ),
    "FeSO4 x 6 H2O": (
        "kgmicrobe.compound:feso4_x_6_h2o",
        "CHEBI:75832",
        "Fe.O4S.6H2O",
        23,
    ),
    "MgSO4 x 6 H2O": (
        "kgmicrobe.compound:mgso4_x_6_h2o",
        "CHEBI:32599",
        "Mg.O4S.6H2O",
        35,
    ),
    "MnSO4 x 7 H2O": (
        "kgmicrobe.compound:mnso4_x_7_h2o",
        "CHEBI:86360",
        "Mn.O4S.7H2O",
        16,
    ),
}


@pytest.fixture(scope="module")
def records() -> list[dict]:
    return yaml.safe_load(CURATED.read_text(encoding="utf-8"))["ingredients"]


def _by_term(records: list[dict], term: str) -> dict:
    hits = [r for r in records if str(r.get("preferred_term") or "") == term]
    assert hits, f"no record named {term!r}"
    return hits[0]


def _cas(record: dict) -> str | None:
    return (record.get("chemical_properties") or {}).get("cas_rn")


@pytest.fixture(scope="module")
def sssom_rows() -> list[dict]:
    with SSSOM.open(newline="", encoding="utf-8") as fh:
        rows = [line for line in fh if not line.startswith("#")]
    return list(csv.DictReader(rows, delimiter="\t"))


@pytest.fixture(scope="module")
def membership_rows() -> list[dict]:
    with MEMBERSHIP.open(newline="", encoding="utf-8") as fh:
        rows = [line for line in fh if not line.startswith("#")]
    return list(csv.DictReader(rows, delimiter="\t"))


# --- #334: the two promotions ---------------------------------------------
@pytest.mark.parametrize(
    ("term", "chebi", "label"),
    [
        ("Na2HPO4 x 2 H2O", "CHEBI:91258", "dihydrate"),
        ("Na2HPO4 x 12 H2O", "CHEBI:91259", "dodecahydrate"),
    ],
)
def test_a_record_that_is_the_chebi_term_carries_its_id(records, term, chebi, label):
    """These were grounded to the right specific hydrate term while keeping a
    registry mint and a CLOSE_MATCH -- understating a record that IS that
    substance. The corpus convention makes the two inseparable: every
    registry-identified record is graded non-exact."""
    record = _by_term(records, term)

    assert record["identifier"] == chebi
    assert record["ontology_mapping"]["ontology_id"] == chebi
    assert record["ontology_mapping"]["mapping_quality"] == "EXACT_MATCH"
    assert label in record["ontology_mapping"]["ontology_label"]


def test_a_registry_identifier_still_implies_a_non_exact_grounding(records):
    """The invariant the promotions were reasoned from, asserted so it cannot
    erode: a record kept on a `kgmicrobe.` mint is one that is NOT the ontology
    term, so grading it exact would make the mint meaningless."""
    offenders = [
        (
            r.get("preferred_term"),
            r["identifier"],
            (r.get("ontology_mapping") or {}).get("mapping_quality"),
        )
        for r in records
        if str(r.get("identifier") or "").startswith("kgmicrobe.")
        and (r.get("ontology_mapping") or {}).get("mapping_quality")
        in {"EXACT_MATCH", "SYNONYM_MATCH"}
    ]

    assert not offenders, f"registry mint with an exact grounding: {offenders[:3]}"


# --- #334: CAS within a hydrate family ------------------------------------
@pytest.mark.parametrize(
    ("term", "cas", "chebi"),
    [("CoCl2 x 6 H2O", "7791-13-1", "CHEBI:53503"), ("NiCl2 x 6 H2O", "7791-20-0", "CHEBI:53542")],
)
def test_a_hexahydrate_carries_its_own_cas_not_the_anhydrous_one(records, term, cas, chebi):
    """Both carried the ANHYDROUS parent's CAS. ChEBI's dbxref on the term the
    record is grounded to is the authority."""
    record = _by_term(records, term)

    assert record["identifier"] == chebi
    assert _cas(record) == cas


@pytest.mark.parametrize(
    "term", ["CoCl2 x 2 H2O", "CoCl2 x 4 H2O", "Na2HPO4 x 3 H2O", "Na2HPO4 x 6 H2O"]
)
def test_a_hydrate_with_no_chebi_term_carries_no_borrowed_cas(records, term):
    """These held a CAS belonging to a different substance -- the anhydrous
    parent, or the heptahydrate. ChEBI has no term for these hydration states,
    so there is no authoritative value to substitute and inventing one is how
    wrong CAS numbers spread. Absent is recoverable; wrong is not."""
    assert _cas(_by_term(records, term)) is None


def test_no_hydrate_carries_its_anhydrous_parents_cas(records):
    """The defect in general form, and the reason it is dangerous: #334 warned
    that `7791-20-0` sat on the di- and pentahydrate while belonging to the
    hexahydrate, so a CAS-keyed join run then would have merged the WRONG
    records.

    Stated as "no hydrate carries the CAS of its own anhydrous sibling" rather
    than "no two hydration states share a CAS". The looser form also fires on
    records whose CAS faithfully reflects a wrong GROUNDING -- a hydrate sitting
    on the anhydrous term is #321's defect, not this one, and a test that
    conflates them cannot be satisfied by fixing either.
    """
    anhydrous = {
        str(r.get("preferred_term") or ""): (r.get("chemical_properties") or {}).get("cas_rn")
        for r in records
        if " x " not in str(r.get("preferred_term") or "")
    }

    offenders = []
    for record in records:
        term = str(record.get("preferred_term") or "")
        cas = _cas(record)
        if not cas or " x " not in term:
            continue
        parent = term.split(" x ")[0].strip()
        if anhydrous.get(parent) and anhydrous[parent] == cas:
            offenders.append((term, cas, parent))

    assert not offenders, f"hydrate carrying its anhydrous parent's CAS: {offenders}"


@pytest.mark.parametrize(
    ("term", "cas", "chebi"),
    [("FeSO4 x 7H2O", "7782-63-0", "CHEBI:75836"), ("MnSO4 x 1 H2O", "10034-96-5", "CHEBI:86364")],
)
def test_hydrate_specific_groundings_carry_their_own_cas(records, term, cas, chebi):
    """Found by the general check above, not by #334's enumerated list: both are
    grounded to a hydrate-SPECIFIC ChEBI term while carrying the anhydrous CAS,
    so ChEBI's dbxref settles them."""
    record = _by_term(records, term)

    assert record["ontology_mapping"]["ontology_id"] == chebi
    assert _cas(record) == cas


@pytest.mark.parametrize(
    ("term", "chebi", "label", "formula", "cas", "data_source"),
    [
        (
            "Esculin Monohydrate",
            "CHEBI:73111",
            "esculin hydrate",
            "C15H16O9.H2O",
            None,
            "OAK/CHEBI exact hydrate term CHEBI:73111",
        ),
        (
            "Betaine x H2O",
            "CHEBI:91242",
            "glycine betaine hydrate",
            "C5H11NO2.H2O",
            "590-47-6",
            "OAK/CHEBI exact hydrate term CHEBI:91242",
        ),
    ],
)
def test_late_specific_hydrates_use_the_exact_chebi_term(
    records, term, chebi, label, formula, cas, data_source
):
    record = _by_term(records, term)

    assert record["identifier"] == chebi
    assert record["ontology_mapping"]["ontology_id"] == chebi
    assert record["ontology_mapping"]["ontology_label"] == label
    assert record["ontology_mapping"]["mapping_quality"] == "EXACT_MATCH"
    assert record["chemical_properties"]["molecular_formula"] == formula
    assert _cas(record) == cas
    assert record["chemical_properties"]["data_source"] == data_source
    if "kg_microbe_node_id" in record:
        assert record["kg_microbe_node_id"] == chebi


@pytest.mark.parametrize(
    ("term", "required", "forbidden"),
    [
        (
            "Esculin Monohydrate",
            {"7-hydroxy-2-oxo-2H-chromen-6-yl " "beta-D-glucopyranoside--water (1/1)"},
            {"7-hydroxy-2-oxo-2H-chromen-6-yl beta-D-glucopyranoside"},
        ),
        (
            "Betaine x H2O",
            {
                "(trimethylazaniumyl)acetate--water (1/1)",
                "carboxy-N,N,N-trimethylmethanaminium hydroxide",
            },
            {"Betaine", "Glycine betaine", "Trimethylglycine"},
        ),
    ],
)
def test_late_specific_hydrates_do_not_publish_anhydrous_exact_synonyms(
    records, term, required, forbidden
):
    exact = {
        synonym["synonym_text"]
        for synonym in _by_term(records, term).get("synonyms") or []
        if synonym.get("synonym_type") == "EXACT_SYNONYM"
    }

    assert required <= exact
    assert exact.isdisjoint(forbidden)


def test_esculin_ferric_citrate_keeps_anhydrous_component_as_external_term(records):
    record = _by_term(records, "Esculin Ferric Citrate")
    esculin = [
        component for component in record["components"] if component["component_name"] == "esculin"
    ]

    assert esculin == [
        {
            "component_name": "esculin",
            "component_id": "CHEBI:4853",
            "reference_scope": "EXTERNAL_TERM",
            "source": "MIM curation (#213/#308)",
        }
    ]


@pytest.mark.parametrize(
    ("term", "chebi", "other"),
    [
        (
            "Esculin Monohydrate",
            "CHEBI:73111",
            [
                "hydrolysis: esculin",
                ("7-hydroxy-2-oxo-2H-chromen-6-yl " "beta-D-glucopyranoside--water (1/1)"),
            ],
        ),
        (
            "Betaine x H2O",
            "CHEBI:91242",
            [
                "(trimethylazaniumyl)acetate--water (1/1)",
                "carboxy-N,N,N-trimethylmethanaminium hydroxide",
                "CAS:590-47-6",
            ],
        ),
    ],
)
def test_late_specific_hydrates_have_single_sssom_exact_rows(sssom_rows, term, chebi, other):
    rows = [row for row in sssom_rows if row["subject_label"] == term]

    assert len(rows) == 1
    assert rows[0]["predicate_id"] == "skos:exactMatch"
    assert rows[0]["object_id"] == chebi
    assert rows[0]["mapping_date"] == "2026-09-10"
    assert rows[0]["other"].split("|") == other


def test_l_cysteine_solution_keeps_local_identity_on_the_hydrate_parent(records, sssom_rows):
    record = _by_term(records, "L-Cysteine x HCl x H2O solution")

    assert record["identifier"] == ("kgmicrobe.ingredient:l-cysteine_x_hcl_x_h2o_solution")
    assert record["ontology_mapping"]["ontology_id"] == "CHEBI:91248"
    assert record["ontology_mapping"]["mapping_quality"] == "CLOSE_MATCH"

    rows = {
        row["object_id"]: row
        for row in sssom_rows
        if row["subject_label"] == "L-Cysteine x HCl x H2O solution"
    }
    assert set(rows) == {
        "CHEBI:91248",
        "kgmicrobe.ingredient:l-cysteine_x_hcl_x_h2o_solution",
    }
    assert rows["CHEBI:91248"]["predicate_id"] == "skos:closeMatch"
    assert rows["CHEBI:91248"]["mapping_date"] == "2026-09-10"
    assert rows["CHEBI:91248"]["other"] == "QSY9 succinimidyl ester(1+)"
    assert (
        rows["kgmicrobe.ingredient:l-cysteine_x_hcl_x_h2o_solution"]["mapping_date"] == "2026-09-10"
    )
    assert "CHEBI:91248" in rows["kgmicrobe.ingredient:l-cysteine_x_hcl_x_h2o_solution"]["comment"]


def test_variable_ferric_sulfate_hydrate_is_not_moved_to_the_monohydrate(records, sssom_rows):
    """`Fe2(SO4)3 x n H2O` needs a variable-hydrate identity.

    CHEBI:131387 is labelled "iron(3+) sulfate hydrate", but its formula and
    exact synonym state a 1:1 monohydrate. Exact-matching the variable `n`
    record to it would collapse two hydration states.
    """
    record = _by_term(records, "Fe2(SO4)3 x n H2O")
    rows = [row for row in sssom_rows if row["subject_label"] == "Fe2(SO4)3 x n H2O"]

    assert rows
    assert record["identifier"] != "CHEBI:131387"
    assert record["ontology_mapping"]["ontology_id"] != "CHEBI:131387"
    assert record.get("chemical_properties", {}).get("cas_rn") != "43059-01-4"
    assert all(row["object_id"] != "CHEBI:131387" for row in rows)


@pytest.mark.parametrize(
    ("term", "identifier", "parent", "parent_label"),
    [
        (
            "Cr2(SO4)3 x n H2O",
            "kgmicrobe.compound:cr2_so43_x_n_h2o",
            "CHEBI:53471",
            "chromium(III) sulfate",
        ),
        (
            "Fe2(SO4)3 x n H2O",
            "kgmicrobe.compound:fe2_so43_x_n_h2o",
            "CHEBI:53438",
            "iron(3+) sulfate",
        ),
    ],
)
def test_variable_sulfate_hydrates_are_locally_identified(
    records, term, identifier, parent, parent_label
):
    record = _by_term(records, term)

    assert record["identifier"] == identifier
    assert record["ontology_mapping"]["ontology_id"] == parent
    assert record["ontology_mapping"]["ontology_label"] == parent_label
    assert record["ontology_mapping"]["mapping_quality"] == "NARROW_MATCH"
    assert record.get("chemical_properties") == {}
    assert record.get("kg_microbe_node_id") != parent

    kg_microbe_exact = [
        synonym
        for synonym in record.get("synonyms") or []
        if synonym.get("synonym_type") == "EXACT_SYNONYM" and synonym.get("source") == "kg_microbe"
    ]

    assert kg_microbe_exact == []


@pytest.mark.parametrize(
    ("term", "identifier", "parent", "expected_other"),
    [
        ("Cr2(SO4)3 x n H2O", "kgmicrobe.compound:cr2_so43_x_n_h2o", "CHEBI:53471", ""),
        (
            "Fe2(SO4)3 x n H2O",
            "kgmicrobe.compound:fe2_so43_x_n_h2o",
            "CHEBI:53438",
            "Fe(SO4)3 x n H2O",
        ),
    ],
)
def test_variable_sulfate_hydrates_publish_parent_and_registry_rows(
    sssom_rows, term, identifier, parent, expected_other
):
    rows = {row["object_id"]: row for row in sssom_rows if row["subject_label"] == term}

    assert set(rows) == {parent, identifier}
    assert rows[parent]["predicate_id"] == "skos:narrowMatch"
    assert rows[parent]["confidence"] == "0.9"
    assert rows[parent]["other"] == expected_other
    assert rows[identifier]["predicate_id"] == "skos:exactMatch"
    assert rows[identifier]["object_label"] == term
    assert rows[identifier]["object_source"] == "kgm:compound"
    assert rows[identifier]["confidence"] == "0.99"
    assert rows[identifier]["other"] == expected_other


@pytest.mark.parametrize(
    ("term", "old", "new"),
    [
        ("Cr2(SO4)3 x n H2O", "CHEBI:53471", "kgmicrobe.compound:cr2_so43_x_n_h2o"),
        ("Fe2(SO4)3 x n H2O", "CHEBI:53438", "kgmicrobe.compound:fe2_so43_x_n_h2o"),
    ],
)
def test_variable_sulfate_membership_rows_move_to_local_identity(
    records, membership_rows, term, old, new
):
    expected = _by_term(records, term)["occurrence_statistics"]["media_count"]
    new_recipes = {row["recipe_id"] for row in membership_rows if row["mim_identifier"] == new}
    stale_old_recipes = {
        row["recipe_id"] for row in membership_rows if row["mim_identifier"] == old
    }

    assert len(new_recipes) == expected
    assert not stale_old_recipes


@pytest.mark.parametrize("term", sorted(LOCAL_SULFATE_HYDRATES))
def test_formula_supported_sulfates_have_local_identities(records, term):
    identifier, parent, formula, _ = LOCAL_SULFATE_HYDRATES[term]
    record = _by_term(records, term)
    properties = record.get("chemical_properties") or {}

    assert record["identifier"] == identifier
    assert record["ontology_mapping"]["ontology_id"] == parent
    assert record["ontology_mapping"]["mapping_quality"] == "NARROW_MATCH"
    assert properties == {
        "molecular_formula": formula,
        "data_source": "MIM curation (#652)",
    }
    assert record.get("kg_microbe_node_id") not in {identifier, parent}


@pytest.mark.parametrize("term", sorted(LOCAL_SULFATE_HYDRATES))
def test_formula_supported_sulfate_sssom_has_parent_and_registry_rows(
    sssom_rows,
    term,
):
    identifier, parent, _, _ = LOCAL_SULFATE_HYDRATES[term]
    rows = {row["object_id"]: row for row in sssom_rows if row["subject_label"] == term}

    assert set(rows) == {parent, identifier}
    assert rows[parent]["predicate_id"] == "skos:narrowMatch"
    assert rows[parent]["confidence"] == "0.9"
    assert rows[identifier]["predicate_id"] == "skos:exactMatch"
    assert rows[identifier]["confidence"] == "0.99"
    assert rows[identifier]["object_source"] == "kgm:compound"
    assert "CAS:" not in rows[parent]["other"]
    assert "CAS:" not in rows[identifier]["other"]


def test_mgso4_middle_dot_hexahydrate_publishes_on_local_identity(sssom_rows):
    rows = {row["object_id"]: row for row in sssom_rows if row["subject_id"] == "MIM:Mgso4_X_6_H2o"}

    assert "MgSO4·6H2O" in rows["CHEBI:32599"]["other"].split("|")
    assert "MgSO4·6H2O" in rows["kgmicrobe.compound:mgso4_x_6_h2o"]["other"].split("|")


@pytest.mark.parametrize("term", sorted(LOCAL_SULFATE_HYDRATES))
def test_formula_supported_sulfates_have_no_resolving_anhydrous_aliases(records, term):
    forbidden = {
        "CAS:7487-88-9",
        "CAS:7720-78-7",
        "CAS:7785-87-7",
        "FeSO .7H O",
        "Mg2SO4",
        "MgSO .7H O",
        "Manganese sulfate anhydrous",
        "ferrous sulfate (anhydrous)",
        "ferrous sulfate anhydrous",
        "iron(2+) sulfate",
        "iron(2+) sulfate (anhydrous)",
        "manganese(2+) sulfate",
    }
    resolving = {
        synonym["synonym_text"]
        for synonym in _by_term(records, term).get("synonyms") or []
        if synonym.get("synonym_type") != "REJECTED_LABEL"
    }

    assert resolving.isdisjoint(forbidden)


def test_reviewed_hydrate_memberships_are_split_from_anhydrous_parents(
    membership_rows,
):
    stats = defaultdict(lambda: [0, 0])
    for row in membership_rows:
        identifier = row["mim_identifier"]
        stats[identifier][0] += 1
        stats[identifier][1] += int(row["occurrences"])

    for identifier, _, _, count in LOCAL_SULFATE_HYDRATES.values():
        assert tuple(stats[identifier]) == (count, count)

    assert tuple(stats["CHEBI:31404"]) == (8, 8)
    assert tuple(stats["CHEBI:30769"]) == (110, 113)


def test_citric_bullet_duplicate_is_merged_into_monohydrate(records, sssom_rows):
    duplicate = _by_term(records, "Citric Acid•H2O")
    monohydrate = _by_term(records, "Citric acid x H2O")
    row = [row for row in sssom_rows if row["subject_id"] == "MIM:Citric_Acid_X_H2o"][0]
    synonyms = {
        synonym["synonym_text"]
        for synonym in monohydrate.get("synonyms") or []
        if synonym.get("synonym_type") != "REJECTED_LABEL"
    }
    sssom_other = row["other"].split("|")

    assert duplicate["identifier"] == "CHEBI:31404"
    assert duplicate["mapping_status"] == "REJECTED"
    assert duplicate["ontology_mapping"]["ontology_id"] == "CHEBI:31404"
    assert duplicate["ontology_mapping"]["ontology_label"] == "Citric acid monohydrate"
    assert duplicate["occurrence_statistics"] == {
        "total_occurrences": 0,
        "media_count": 0,
    }
    assert monohydrate["identifier"] == "CHEBI:31404"
    assert monohydrate["occurrence_statistics"] == {
        "media_count": 8,
        "total_occurrences": 8,
    }
    assert {"Citric Acid•H2O", "Citric Acid•H2O(Fisher A 104)"} <= synonyms
    assert "Citric Acid•H2O" not in sssom_other
    assert "Citric Acid•H2O(Fisher A 104)" in sssom_other
    assert not any(row["subject_id"] == "MIM:Citric_Acidh2o" for row in sssom_rows)


def test_reviewed_hydrate_aliases_do_not_leak_to_parent_sssom_rows(sssom_rows):
    leaks = []
    for row in sssom_rows:
        if row["subject_label"] in {
            "Citric acid x H2O",
            *LOCAL_SULFATE_HYDRATES,
        }:
            continue
        other = set((row.get("other") or "").split("|"))
        for token in {
            "Citric Acid•H2O",
            "Citric Acid•H2O(Fisher A 104)",
            "FeSO4 x 5 H2O",
            "FeSO4 x 6 H2O",
            "FeSO4 x 6H2O",
            "FeSO4·6H2O",
            "FeSO4・6H2O",
            "MgSO4 x 6 H2O",
            "MgSO4 x 6H2O",
            "MgSO4·6H2O",
            "MnSO4 . 7H2O",
            "MnSO4 x 7 H2O",
            "MnSO4 x 7H2O",
            "MnSO4.7H2O",
            "MnSO4·7H2O",
        } & other:
            leaks.append((row["subject_label"], token))

    assert leaks == []
