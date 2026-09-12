"""Grade metadata drifts independently of the predicate (#623).

`_sync_quality_columns` has always written predicate, justification and
confidence together, so all three are what "in sync" has to mean. The drift
detector keyed on the predicate alone, which let a row keep the right predicate
with stale justification or confidence and still be reported clean:

    PREDICATE (current ontology row, wrong predicate): 0
    OK: SSSOM is in sync with the curated data.

The published set measures zero on both counts today, so these tests pin a
verified-clean property rather than turning CI red.
"""

from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import pytest
import yaml

_REPO = Path(__file__).parent.parent
sys.path.insert(0, str(_REPO / "src"))
sys.path.insert(0, str(_REPO / "scripts"))
_spec = importlib.util.spec_from_file_location("rec", _REPO / "scripts" / "reconcile_sssom.py")
rec = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(rec)

from mediaingredientmech.sssom_grading import CONFIDENCE, PREDICATE, justification_for  # noqa: E402


def _row(term="Sugars", oid="CHEBI:16646", quality="NARROW_MATCH", **overrides):
    predicate, justification, confidence = rec.expected_grade(quality)
    row = {
        "subject_id": f"MIM:{term}",
        "subject_label": term,
        "object_id": oid,
        "predicate_id": predicate,
        "mapping_justification": justification,
        "confidence": confidence,
    }
    row.update(overrides)
    return row


def _curated(term="Sugars", oid="CHEBI:16646", quality="NARROW_MATCH", identifier="MIM:Sugars"):
    return {
        "ingredients": [
            {
                "preferred_term": term,
                "identifier": identifier,
                "mapping_status": "MAPPED",
                "ontology_mapping": {"ontology_id": oid, "mapping_quality": quality},
            }
        ]
    }


def test_expected_grade_is_the_triple_the_writer_sets():
    """The projection must match _sync_quality_columns or the gate is fiction."""
    for quality in ("EXACT_MATCH", "NARROW_MATCH", "CLOSE_MATCH"):
        assert rec.expected_grade(quality) == (
            PREDICATE[quality], justification_for(quality), str(CONFIDENCE[quality])
        )


def test_a_clean_row_reports_no_drift():
    drift = rec.find_drift(_curated(), [_row()])
    assert drift["predicate"] == [] and drift["grade"] == []


def test_stale_confidence_alone_is_caught():
    """The exact case that was invisible: predicate right, confidence stale."""
    drift = rec.find_drift(_curated(), [_row(confidence="0.123")])
    assert drift["predicate"] == []
    assert len(drift["grade"]) == 1
    assert "confidence" in drift["grade"][0][3]


def test_stale_justification_alone_is_caught():
    drift = rec.find_drift(_curated(), [_row(mapping_justification="semapv:Bogus")])
    assert drift["predicate"] == []
    assert drift["grade"] and "mapping_justification" in drift["grade"][0][3]


def test_both_stale_fields_are_named():
    drift = rec.find_drift(
        _curated(), [_row(confidence="0.1", mapping_justification="semapv:Bogus")]
    )
    assert set(drift["grade"][0][3]) == {"mapping_justification", "confidence"}


def test_a_wrong_predicate_is_still_predicate_drift_not_grade():
    """The categories must stay disjoint or the counts double-report."""
    drift = rec.find_drift(_curated(), [_row(predicate_id="skos:exactMatch")])
    assert len(drift["predicate"]) == 1
    assert drift["grade"] == []


def test_the_primary_identifier_row_is_out_of_scope():
    """A record's own identity row is not graded against its parent mapping."""
    curated = _curated(identifier="CHEBI:16646")
    drift = rec.find_drift(curated, [_row(confidence="0.123")])
    assert drift["grade"] == []


def test_the_published_set_has_no_grade_drift():
    """Pins the verified-clean state this rule was added on."""
    curated = yaml.safe_load((_REPO / "data" / "curated" / "mapped_ingredients.yaml").read_text())
    _, _, _, rows = rec._read_sssom()
    drift = rec.find_drift(curated, rows)
    assert drift["grade"] == [], drift["grade"][:3]
    assert drift["predicate"] == []
