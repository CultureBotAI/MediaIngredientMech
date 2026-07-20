"""Tests for utils/role_iteration.py — the shared role-slot iterator."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from mediaingredientmech.utils.role_iteration import (
    ALL_ROLE_SLOTS,
    FACET_ROLE_SLOTS,
    iter_role_assignments,
)


def _record_with_one_of_each() -> dict:
    """Fixture: an IngredientRecord dict with one assignment in every role slot."""
    return {
        "identifier": "TEST:001",
        "preferred_term": "test compound",
        "mapping_status": "MAPPED",
        "community_organism_roles": [{"role": "PRIMARY_DEGRADER", "confidence": 0.8}],
        "nutritional_roles": [{"role": "CARBON_SOURCE", "confidence": 0.95}],
        "physicochemical_roles": [{"role": "BUFFER", "confidence": 0.99}],
        "cellular_metabolic_roles": [{"role": "SUBSTRATE", "confidence": 0.9}],
    }


def test_all_role_slots_covered():
    """The exported ALL_ROLE_SLOTS tuple names all four role slots."""
    assert ALL_ROLE_SLOTS == (
        "community_organism_roles",
        "nutritional_roles",
        "physicochemical_roles",
        "cellular_metabolic_roles",
    )
    assert set(FACET_ROLE_SLOTS).issubset(set(ALL_ROLE_SLOTS))


def test_default_yields_every_assignment_across_all_slots():
    record = _record_with_one_of_each()
    yielded = list(iter_role_assignments(record))
    assert len(yielded) == 4
    slot_names = [slot for slot, _ in yielded]
    assert slot_names == list(ALL_ROLE_SLOTS)
    # Values are the exact assignment dicts.
    for slot, assignment in yielded:
        assert assignment is record[slot][0]


def test_slots_filter_restricts_to_facet_slots_only():
    record = _record_with_one_of_each()
    yielded = list(iter_role_assignments(record, slots=FACET_ROLE_SLOTS))
    assert [slot for slot, _ in yielded] == list(FACET_ROLE_SLOTS)
    assert len(yielded) == 3


def test_record_with_no_role_slots_yields_nothing():
    record = {"identifier": "TEST:002", "preferred_term": "empty", "mapping_status": "UNMAPPED"}
    assert list(iter_role_assignments(record)) == []


def test_slot_set_to_none_or_empty_list_yields_nothing():
    record = {
        "identifier": "TEST:003",
        "community_organism_roles": [],
        "physicochemical_roles": None,
        "nutritional_roles": [{"role": "SULFUR_SOURCE"}],
    }
    yielded = list(iter_role_assignments(record))
    assert yielded == [("nutritional_roles", {"role": "SULFUR_SOURCE"})]


def test_unknown_slot_names_in_filter_are_silently_skipped():
    """A caller passing a slot name that isn't a role slot must not raise."""
    record = _record_with_one_of_each()
    yielded = list(
        iter_role_assignments(
            record, slots=("nutritional_roles", "not_a_real_slot", "physicochemical_roles")
        )
    )
    assert [slot for slot, _ in yielded] == ["nutritional_roles", "physicochemical_roles"]


def test_multivalued_slot_yields_each_assignment_in_order():
    record = {
        "identifier": "TEST:004",
        "nutritional_roles": [
            {"role": "AMINO_ACID_SOURCE"},
            {"role": "SULFUR_SOURCE"},
        ],
    }
    yielded = list(iter_role_assignments(record))
    assert [a["role"] for _, a in yielded] == ["AMINO_ACID_SOURCE", "SULFUR_SOURCE"]
