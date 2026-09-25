"""Corpus checks for source-scoped ontology promotion and CAS containment."""

import csv
import json
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
EVIDENCE = ROOT / "reports/sssom_completion_20260921/mapping_review/identity-review-20260924"


def record(slug):
    return yaml.safe_load((ROOT / f"data/ingredients/mapped/{slug}.yaml").read_text())


def rows(path):
    with path.open() as handle:
        return list(csv.DictReader((s for s in handle if not s.startswith("#")), delimiter="\t"))


def test_ncit_current_cas_evidence_agrees_with_promoted_records():
    native = json.loads((EVIDENCE / "native-authorities.json").read_text())["ncit"]
    before = json.loads((EVIDENCE / "source-records.json").read_text())["before_records"]
    for slug, item in before.items():
        target = item["record"]["ontology_mapping"]["ontology_id"]
        if target not in native:
            continue
        current = record(slug)
        assert current["identifier"] == current["ontology_mapping"]["ontology_id"] == target
        assert current["ontology_mapping"]["mapping_quality"] == "EXACT_MATCH"
        cas = [value for predicate, _, value in native[target] if predicate == "NCIT:P210"]
        assert cas == [current["chemical_properties"]["cas_rn"]]


def test_stereospecific_structures_keep_the_independently_verified_form():
    authority = {
        p["CID"]: p
        for p in json.loads((EVIDENCE / "pubchem-structures.json").read_text())["properties"]
    }
    for slug in [
        "Anabasine_Hydrochloride",
        "Pretomanid",
        "Sutezolid",
        "Sodium_Adipate",
        "Acriflavine",
    ]:
        props = record(slug)["chemical_properties"]
        expected = authority[props["pubchem_cid"]]
        assert props["inchi"] == expected["InChI"]
        assert props["smiles"] == expected["SMILES"]
        assert props["molecular_formula"] == expected["MolecularFormula"]


def test_bsa_recipe_membership_and_supplier_preparations_stay_separate():
    occurrences = json.loads((EVIDENCE / "bsa-recipe-occurrences.json").read_text())["occurrences"]
    expected = {item["recipe_id"] for item in occurrences}
    members = rows(ROOT / "mappings/culturemech_recipe_membership.tsv")
    actual = [r for r in members if r["mim_identifier"] == "NCIT:C85253"]
    assert len(actual) == 7
    assert {r["recipe_id"] for r in actual} == expected
    assert not any(r["mim_identifier"] == "cas:9048-46-8" for r in members)
    forms = {f["catalog_number"]: f for f in record("Bovine_Serum_Albumin")["supplied_form"]}
    assert set(forms) == {"A7030", "A9647", "A7409"}
    assert "CultureMech:015191" in forms["A9647"]["notes"]
    assert "CultureMech:015191" in forms["A7409"]["notes"]
    assert "fatty acid free" in forms["A7030"]["form"]


def test_product_preparation_text_does_not_become_an_exact_synonym():
    gum = record("Locust_Bean_Gum")
    assert gum["identifier"] == "FOODON:03413132"
    assert gum["supplied_form"][0]["catalog_number"] == "G0753"
    assert "autoclaved" in gum["supplied_form"][0]["notes"]
    assert not any("autoclaved" in s["synonym_text"].lower() for s in gum["synonyms"])
    assert record("Tara_Gum")["supplied_form"][0]["catalog_number"] == "YT58656"


def test_historical_acriflavine_cas_does_not_escape_into_active_mappings():
    fda = json.loads((EVIDENCE / "fda-gsrs.json").read_text())["1T3A50395T"]
    statuses = {c["code"]: c["type"] for c in fda["codes"] if c["codeSystem"] == "CAS"}
    assert statuses["8048-52-0"] == "SUPERSEDED"
    assert statuses["65589-70-0"] == "PRIMARY"
    current = record("Acriflavine")
    assert current["chemical_properties"]["cas_rn"] == "65589-70-0"
    assert "8048-52-0" in current["notes"]
    active = [
        r
        for r in rows(ROOT / "mappings/ingredient_mappings.sssom.tsv")
        if r["subject_id"] == "MIM:Acriflavine"
    ]
    assert len(active) == 1 and active[0]["object_id"] == "NCIT:C76253"
    assert active[0]["other"] == ""


def test_lysozyme_keeps_local_identity_without_inventing_a_replacement_cas():
    current = record("Lysozyme")
    local = "kgmicrobe.ingredient:lysozyme"
    assert current["identifier"] == current["ontology_mapping"]["ontology_id"] == local
    assert not current["chemical_properties"].get("cas_rn")
    active = [
        r
        for r in rows(ROOT / "mappings/ingredient_mappings.sssom.tsv")
        if r["subject_id"] == "MIM:Lysozyme"
    ]
    assert len(active) == 1
    assert active[0]["object_id"] == local and active[0]["other"] == ""
    original = json.loads((EVIDENCE / "source-records.json").read_text())
    source = next(r for r in original["rows"] if r["Compound"] == "Lysozyme")
    assert source["CAS"] == "2650-88-3" and not source["Company"] and not source["CatalogNumber"]
