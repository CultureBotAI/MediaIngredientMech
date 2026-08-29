"""Identity and CAS within hydrate families (#225, #334).

Two defects with one cause: a hydrate and its anhydrous parent are different
substances, and tooling that treats them as one produced both a wrong identifier
and a wrong CAS. #334's own warning is the reason the CAS half matters --
`7791-20-0` sat on the di- and pentahydrate records while belonging to the
hexahydrate, so any CAS-keyed dedup run at the time would have merged the wrong
records.
"""

from pathlib import Path

import pytest
import yaml

ROOT = Path(__file__).parent.parent
CURATED = ROOT / "data" / "curated" / "mapped_ingredients.yaml"


@pytest.fixture(scope="module")
def records() -> list[dict]:
    return yaml.safe_load(CURATED.read_text(encoding="utf-8"))["ingredients"]


def _by_term(records: list[dict], term: str) -> dict:
    hits = [r for r in records if str(r.get("preferred_term") or "") == term]
    assert hits, f"no record named {term!r}"
    return hits[0]


def _cas(record: dict) -> str | None:
    return (record.get("chemical_properties") or {}).get("cas_rn")


# --- #334: the two promotions ---------------------------------------------
@pytest.mark.parametrize(
    ("term", "chebi", "label"),
    [("Na2HPO4 x 2 H2O", "CHEBI:91258", "dihydrate"),
     ("Na2HPO4 x 12 H2O", "CHEBI:91259", "dodecahydrate")],
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
        (r.get("preferred_term"), r["identifier"],
         (r.get("ontology_mapping") or {}).get("mapping_quality"))
        for r in records
        if str(r.get("identifier") or "").startswith("kgmicrobe.")
        and (r.get("ontology_mapping") or {}).get("mapping_quality")
        in {"EXACT_MATCH", "SYNONYM_MATCH"}
    ]

    assert not offenders, f"registry mint with an exact grounding: {offenders[:3]}"


# --- #334: CAS within a hydrate family ------------------------------------
@pytest.mark.parametrize(
    ("term", "cas", "chebi"),
    [("CoCl2 x 6 H2O", "7791-13-1", "CHEBI:53503"),
     ("NiCl2 x 6 H2O", "7791-20-0", "CHEBI:53542")],
)
def test_a_hexahydrate_carries_its_own_cas_not_the_anhydrous_one(records, term, cas, chebi):
    """Both carried the ANHYDROUS parent's CAS. ChEBI's dbxref on the term the
    record is grounded to is the authority."""
    record = _by_term(records, term)

    assert record["identifier"] == chebi
    assert _cas(record) == cas


@pytest.mark.parametrize(
    "term", ["CoCl2 x 2 H2O", "CoCl2 x 4 H2O", "Na2HPO4 x 3 H2O", "Na2HPO4 x 6 H2O"])
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

    assert not offenders, (
        f"hydrate carrying its anhydrous parent's CAS: {offenders}")


@pytest.mark.parametrize(
    ("term", "cas", "chebi"),
    [("FeSO4 x 7H2O", "7782-63-0", "CHEBI:75836"),
     ("MnSO4 x 1 H2O", "10034-96-5", "CHEBI:86364")],
)
def test_hydrate_specific_groundings_carry_their_own_cas(records, term, cas, chebi):
    """Found by the general check above, not by #334's enumerated list: both are
    grounded to a hydrate-SPECIFIC ChEBI term while carrying the anhydrous CAS,
    so ChEBI's dbxref settles them."""
    record = _by_term(records, term)

    assert record["ontology_mapping"]["ontology_id"] == chebi
    assert _cas(record) == cas
