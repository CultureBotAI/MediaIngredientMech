"""Focused regression tests for the #317 synonym-grade regrader.

The production audit uses the local ChEBI semsql database. These tests use a
minimal in-memory ``statements`` table, so they are deterministic and CI-safe.
"""

from __future__ import annotations

import copy
import importlib.util
import sqlite3
from pathlib import Path

import pytest

_SPEC = importlib.util.spec_from_file_location(
    "regrade_synonym_matches",
    Path(__file__).parent.parent / "scripts" / "regrade_synonym_matches.py",
)
assert _SPEC is not None and _SPEC.loader is not None
mod = importlib.util.module_from_spec(_SPEC)
_SPEC.loader.exec_module(mod)


def _record(
    preferred_term: str,
    ontology_label: str = "canonical name",
    *,
    curie: str = "CHEBI:1",
    status: str = "MAPPED",
    quality: str = "EXACT_MATCH",
    cas_rn: str | None = None,
    cas_created: bool = False,
    synonyms: list[tuple[str, str]] | None = None,
) -> dict:
    record = {
        "identifier": curie,
        "preferred_term": preferred_term,
        "mapping_status": status,
        "ontology_mapping": {
            "ontology_id": curie,
            "ontology_label": ontology_label,
            "ontology_source": "CHEBI",
            "mapping_quality": quality,
        },
        "synonyms": [
            {
                "synonym_text": text,
                "synonym_type": "EXACT_SYNONYM",
                "source": source,
            }
            for text, source in (synonyms or [])
        ],
        "curation_history": [],
    }
    if cas_rn:
        record["chemical_properties"] = {"cas_rn": cas_rn}
    if cas_created:
        record["curation_history"].append(
            {"action": "CREATED_FROM_CAS_LOOKUP", "changes": "test fixture"}
        )
    return record


def _cursor(
    *,
    synonyms: dict[str, list[str]],
    structured: set[str] | None = None,
    cas_xrefs: dict[str, list[str]] | None = None,
):
    db = sqlite3.connect(":memory:")
    db.execute("CREATE TABLE statements (subject TEXT, predicate TEXT, value TEXT)")
    for curie, values in synonyms.items():
        for value in values:
            db.execute(
                "INSERT INTO statements VALUES (?, 'oio:hasExactSynonym', ?)",
                (curie, value),
            )
    for curie in structured if structured is not None else set(synonyms):
        db.execute(
            "INSERT INTO statements VALUES (?, 'chebi:formula', 'C1')",
            (curie,),
        )
    for curie, values in (cas_xrefs or {}).items():
        for value in values:
            db.execute(
                "INSERT INTO statements VALUES (?, 'oio:hasDbXref', ?)",
                (curie, f"cas:{value}"),
            )
    db.commit()
    return db, db.cursor()


def _plan(records: list[dict], synonyms: dict[str, list[str]], **kwargs):
    db, cursor = _cursor(synonyms=synonyms, **kwargs)
    try:
        return mod.plan({"ingredients": records}, cursor)
    finally:
        db.close()


def test_explicit_matching_cas_provenance_takes_priority_over_lexical_grade():
    rec = _record("alias", cas_rn="123-45-6", cas_created=True)
    todo, tally = _plan(
        [rec],
        {"CHEBI:1": ["alias"]},
        cas_xrefs={"CHEBI:1": ["123-45-6"]},
    )
    assert len(todo) == 1
    assert todo[0]["target_quality"] == "CAS_RN_LOOKUP"
    assert tally["cas_rn_lookup_regrade"] == 1
    assert tally["synonym_regrade"] == 0


def test_prior_synonym_regrade_is_repaired_when_mapping_was_created_by_cas():
    rec = _record(
        "alias",
        quality="SYNONYM_MATCH",
        cas_rn="123-45-6",
        cas_created=True,
    )
    todo, _ = _plan(
        [rec],
        {"CHEBI:1": ["alias"]},
        cas_xrefs={"CHEBI:1": ["123-45-6"]},
    )
    assert todo[0]["old_quality"] == "SYNONYM_MATCH"
    assert todo[0]["target_quality"] == "CAS_RN_LOOKUP"


def test_cas_presence_without_creation_provenance_does_not_override_synonym():
    rec = _record("alias", cas_rn="123-45-6")
    todo, tally = _plan(
        [rec],
        {"CHEBI:1": ["alias"]},
        cas_xrefs={"CHEBI:1": ["123-45-6"]},
    )
    assert todo[0]["target_quality"] == "SYNONYM_MATCH"
    assert tally["synonym_regrade"] == 1


def test_cas_xref_conflict_is_reported_and_not_used_as_provenance():
    rec = _record(
        "canonical name",
        cas_rn="999-99-9",
        cas_created=True,
    )
    todo, tally = _plan(
        [rec],
        {"CHEBI:1": []},
        cas_xrefs={"CHEBI:1": ["123-45-6"]},
    )
    assert todo == []
    assert tally["cas_xref_mismatch"] == 1
    assert tally["label_matches"] == 0


def test_cas_xref_conflict_cannot_fall_through_to_synonym_grade():
    rec = _record(
        "alias",
        cas_rn="999-99-9",
        cas_created=True,
    )
    todo, tally = _plan(
        [rec],
        {"CHEBI:1": ["alias"]},
        cas_xrefs={"CHEBI:1": ["123-45-6"]},
    )
    assert todo == []
    assert tally["cas_xref_mismatch"] == 1
    assert tally["synonym_regrade"] == 0


def test_cas_shared_by_multiple_chebi_terms_is_left_for_review():
    rec = _record("alias", cas_rn="123-45-6", cas_created=True)
    todo, tally = _plan(
        [rec],
        {"CHEBI:1": ["alias"], "CHEBI:2": []},
        cas_xrefs={"CHEBI:1": ["123-45-6"], "CHEBI:2": ["123-45-6"]},
    )
    assert todo == []
    assert tally["cas_ambiguous_skipped"] == 1
    assert tally["cas_rn_lookup_regrade"] == 0


def test_cas_provenance_does_not_override_preparation_identity_conflict():
    rec = _record("Stachyose - 70%", cas_rn="470-55-3", cas_created=True)
    todo, tally = _plan(
        [rec],
        {"CHEBI:1": ["stachyose"]},
        cas_xrefs={"CHEBI:1": ["470-55-3"]},
    )
    assert todo == []
    assert tally["preparation_skipped"] == 1
    assert tally["cas_rn_lookup_regrade"] == 0


def test_cas_provenance_does_not_override_hydrate_identity_conflict():
    rec = _record(
        "Esculin monohydrate",
        "esculin",
        cas_rn="531-75-9",
        cas_created=True,
    )
    todo, tally = _plan(
        [rec],
        {"CHEBI:1": ["esculin"]},
        cas_xrefs={"CHEBI:1": ["531-75-9"]},
    )
    assert todo == []
    assert tally["hydrate_mismatch_skipped"] == 1
    assert tally["cas_rn_lookup_regrade"] == 0


def test_parenthetical_hemiheptahydrate_is_same_as_contracted_form():
    rec = _record(
        "Ceftriaxone disodium salt hemi(heptahydrate)",
        "ceftriaxone disodium hemiheptahydrate",
        cas_rn="104376-79-6",
        cas_created=True,
    )
    todo, tally = _plan(
        [rec],
        {"CHEBI:1": []},
        cas_xrefs={"CHEBI:1": ["104376-79-6"]},
    )
    assert len(todo) == 1
    assert todo[0]["target_quality"] == "CAS_RN_LOOKUP"
    assert tally["hydrate_mismatch_skipped"] == 0
    assert mod.hydration_state(rec["preferred_term"]) == (True, 3.5)
    assert mod.hydration_state(rec["ontology_mapping"]["ontology_label"]) == (
        True,
        3.5,
    )


@pytest.mark.parametrize(
    ("preferred", "curie", "cas_rn"),
    sorted(mod.REVIEWED_IDENTITY_CONFLICTS),
)
def test_reviewed_cas_identity_conflicts_are_not_merely_regraded(preferred, curie, cas_rn):
    rec = _record(preferred, curie=curie, cas_rn=cas_rn, cas_created=True)
    todo, tally = _plan(
        [rec],
        {curie: []},
        cas_xrefs={curie: [cas_rn]},
    )
    assert todo == []
    assert tally["identity_conflict_skipped"] == 1
    assert tally["cas_rn_lookup_regrade"] == 0


def test_reviewed_identity_skip_does_not_survive_a_corrected_source_label():
    rec = _record(
        "glycyrrhizinic acid",
        "glycyrrhizinic acid",
        curie="CHEBI:15939",
        cas_rn="1405-86-3",
        cas_created=True,
    )
    todo, tally = _plan(
        [rec],
        {"CHEBI:15939": []},
        cas_xrefs={"CHEBI:15939": ["1405-86-3"]},
    )
    assert len(todo) == 1
    assert todo[0]["target_quality"] == "CAS_RN_LOOKUP"
    assert tally["identity_conflict_skipped"] == 0


def test_apply_then_replan_is_idempotent_for_both_output_grades():
    cas_record = _record(
        "CAS-grounded alias",
        curie="CHEBI:1",
        cas_rn="123-45-6",
        cas_created=True,
    )
    synonym_record = _record("lexical alias", curie="CHEBI:2")
    db, cursor = _cursor(
        synonyms={"CHEBI:1": [], "CHEBI:2": ["lexical alias"]},
        cas_xrefs={"CHEBI:1": ["123-45-6"]},
    )
    collection = {"ingredients": [cas_record, synonym_record]}
    try:
        first, _ = mod.plan(collection, cursor)
        assert {item["target_quality"] for item in first} == {
            "CAS_RN_LOOKUP",
            "SYNONYM_MATCH",
        }
        for item in first:
            mod.apply_one(item)

        second, tally = mod.plan(collection, cursor)
        assert second == []
        assert tally["regrade"] == 0
    finally:
        db.close()


def test_all_surfaces_are_evaluated_deterministically():
    """A circular hit encountered first must not hide independent evidence."""
    base = _record(
        "source label",
        synonyms=[
            ("A circular alias", "chebi_synonym_review"),
            ("Z curator alias", "manual_curator"),
        ],
    )
    chebi = {"CHEBI:1": ["Z curator alias", "A circular alias"]}

    first, first_tally = _plan([copy.deepcopy(base)], chebi)
    reversed_record = copy.deepcopy(base)
    reversed_record["synonyms"].reverse()
    second, second_tally = _plan([reversed_record], {"CHEBI:1": list(reversed(chebi["CHEBI:1"]))})

    assert first_tally == second_tally
    assert first_tally["regrade"] == 1
    assert len(first) == len(second) == 1
    for item in (first[0], second[0]):
        assert item["surface_kind"] == "synonym"
        assert item["surface_text"] == "Z curator alias"
        assert item["surface_source"] == "manual_curator"
        assert item["matched_synonym"] == "Z curator alias"


def test_synonym_shared_by_another_chebi_term_is_not_auto_regraded():
    rec = _record("ambiguous alias")
    todo, tally = _plan(
        [rec],
        {"CHEBI:1": ["ambiguous alias"], "CHEBI:2": ["Ambiguous Alias"]},
    )
    assert todo == []
    assert tally["ambiguous_synonym_skipped"] == 1
    assert tally["regrade"] == 0


def test_punctuation_equivalent_synonym_on_another_term_is_ambiguous():
    rec = _record("ambiguous alias")
    todo, tally = _plan(
        [rec],
        {"CHEBI:1": ["ambiguous-alias"], "CHEBI:2": ["Ambiguous Alias"]},
    )
    assert todo == []
    assert tally["ambiguous_synonym_skipped"] == 1
    assert tally["regrade"] == 0


@pytest.mark.parametrize(
    "source",
    ["kg_microbe", "kg_microbe_via_hydration_routing", "chebi_synonym_review", "OLS"],
)
def test_ontology_and_kg_microbe_enrichment_is_circular(source):
    rec = _record("source label", synonyms=[("database alias", source)])
    todo, tally = _plan([rec], {"CHEBI:1": ["database alias"]})
    assert todo == []
    assert tally["circular_evidence_only"] == 1
    assert tally["regrade"] == 0


def test_only_live_mapped_records_are_considered():
    mapped = _record("live alias")
    rejected = _record("dead alias", curie="CHEBI:2", status="REJECTED")
    todo, tally = _plan(
        [mapped, rejected],
        {"CHEBI:1": ["live alias"], "CHEBI:2": ["dead alias"]},
    )
    assert [item["rec"]["preferred_term"] for item in todo] == ["live alias"]
    assert tally["not_mapped"] == 1
    assert tally["regrade"] == 1


def test_concentration_preparation_is_not_regraded():
    rec = _record("0.5 M Nitrilotriacetic acid, disodium salt")
    todo, tally = _plan([rec], {"CHEBI:1": ["0.5 M Nitrilotriacetic acid, disodium salt"]})
    assert todo == []
    assert tally["preparation_skipped"] == 1


@pytest.mark.parametrize(
    "preferred_term",
    ["MOPS_2M_pH7", "example compound (1 M)", "buffer, 25 mM", "reagent 3%"],
)
def test_concentration_preparation_is_detected_anywhere(preferred_term):
    rec = _record(preferred_term)
    todo, tally = _plan([rec], {"CHEBI:1": [preferred_term]})
    assert todo == []
    assert tally["preparation_skipped"] == 1


def test_normalisation_preserves_identity_bearing_punctuation():
    assert mod.norm("(+)-carvone") != mod.norm("(-)-carvone")
    assert mod.norm("5'-deoxyadenosine") != mod.norm("5-deoxyadenosine")
    assert mod.norm("Fe2+") != mod.norm("Fe2−")
    assert mod.norm("Na2S x 9 H2O") == mod.norm("Na2S.9H2O")


@pytest.mark.parametrize(
    ("record", "chebi_synonyms"),
    [
        (
            _record(
                "CuSO4 x 4 H2O",
                "copper(II) sulfate",
                synonyms=[("cupric sulfate anhydrous", "kg_microbe")],
            ),
            ["cupric sulfate anhydrous"],
        ),
        (
            _record(
                "MgSO4·H2O",
                "magnesium sulfate heptahydrate",
                synonyms=[("MgSO4.7H2O", "kg_microbe")],
            ),
            ["MgSO4.7H2O"],
        ),
        (
            _record(
                "Ciprofloxacin Hydrochloride",
                "ciprofloxacin hydrochloride hydrate",
            ),
            ["ciprofloxacin hydrochloride"],
        ),
        (
            _record("Example monohydrate", "example dihydrate"),
            ["Example monohydrate"],
        ),
    ],
)
def test_hydrate_identity_mismatches_are_not_regraded(record, chebi_synonyms):
    todo, tally = _plan([record], {"CHEBI:1": chebi_synonyms})
    assert todo == []
    assert tally["hydrate_mismatch_skipped"] == 1


def test_hydrate_separator_normalisation_retains_a_valid_preferred_term_match():
    rec = _record("Na2S x 9 H2O", "sodium sulfide nonahydrate")
    todo, tally = _plan([rec], {"CHEBI:1": ["Na2S.9H2O"]})
    assert tally["regrade"] == 1
    assert todo[0]["surface_kind"] == "preferred_term"
    assert todo[0]["matched_synonym"] == "Na2S.9H2O"
    assert mod.norm("xanthine") == "xanthine"


@pytest.mark.parametrize(
    ("preferred", "target"),
    [
        ("ferric citrate monohydrate", "iron(III) citrate monohydrate"),
        (
            "spectinomycin dihydrochloride pentahydrate",
            "spectinomycin hydrochloride hydrate",
        ),
    ],
)
def test_compatible_hydrate_states_can_be_regraded(preferred, target):
    rec = _record(preferred, target)
    todo, tally = _plan([rec], {"CHEBI:1": [preferred]})
    assert len(todo) == 1
    assert tally["regrade"] == 1
    assert tally["hydrate_mismatch_skipped"] == 0


def test_apply_history_names_the_actual_matching_surface_and_preserves_identity():
    rec = _record(
        "source label",
        synonyms=[("curated alias", "manual_review")],
    )
    todo, _ = _plan([rec], {"CHEBI:1": ["curated alias"]})
    old_identifier = rec["identifier"]
    old_ontology_id = rec["ontology_mapping"]["ontology_id"]

    mod.apply_one(todo[0])

    assert rec["identifier"] == old_identifier
    assert rec["ontology_mapping"]["ontology_id"] == old_ontology_id
    assert rec["ontology_mapping"]["mapping_quality"] == "SYNONYM_MATCH"
    event = rec["curation_history"][-1]
    assert event["action"] == "REGRADED_EXACT_TO_SYNONYM"
    assert "independently sourced synonym 'curated alias'" in event["changes"]
    assert "source 'manual_review'" in event["changes"]
    assert "ChEBI synonym 'curated alias'" in event["changes"]


def test_apply_history_names_preferred_term_when_it_is_the_match():
    rec = _record("direct synonym")
    todo, _ = _plan([rec], {"CHEBI:1": ["direct synonym"]})
    mod.apply_one(todo[0])
    changes = rec["curation_history"][-1]["changes"]
    assert "preferred_term 'direct synonym'" in changes
    assert "ChEBI synonym 'direct synonym'" in changes


def test_apply_cas_grade_records_method_and_preserves_identity():
    rec = _record("source label", cas_rn="123-45-6", cas_created=True)
    todo, _ = _plan(
        [rec],
        {"CHEBI:1": []},
        cas_xrefs={"CHEBI:1": ["123-45-6"]},
    )
    old_identifier = rec["identifier"]
    old_ontology_id = rec["ontology_mapping"]["ontology_id"]

    mod.apply_one(todo[0])

    assert rec["identifier"] == old_identifier
    assert rec["ontology_mapping"]["ontology_id"] == old_ontology_id
    assert rec["ontology_mapping"]["mapping_quality"] == "CAS_RN_LOOKUP"
    event = rec["curation_history"][-1]
    assert event["action"] == "REGRADED_TO_CAS_RN_LOOKUP"
    assert "current CAS RN 123-45-6 uniquely resolves by ChEBI xref to CHEBI:1" in event["changes"]
    assert "own-identifier SSSOM predicate remains skos:exactMatch" in event["changes"]
