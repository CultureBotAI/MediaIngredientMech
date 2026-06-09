"""Tests for the ontology_label canonicalization logic.

`scripts/correct_stale_ontology_labels.py` rewrites stale/empty
`ontology_mapping.ontology_label` values to the canonical OBO label. These pin
the decision logic (`needs_correction`) with a stub resolver so it stays
CI-safe (no OAK sqlite needed) and can't silently regress its guards.
"""

import importlib.util
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

_spec = importlib.util.spec_from_file_location(
    "correct_stale_ontology_labels",
    Path(__file__).parent.parent / "scripts" / "correct_stale_ontology_labels.py",
)
mod = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(mod)

# stub canonical-label resolver: only CHEBI:1 and CHEBI:2 "exist".
CANON = {"CHEBI:1": "coenzyme M", "CHEBI:2": "acetate"}


def resolve(oid):
    return CANON.get(oid)


def test_stale_label_corrected():
    om = {"ontology_id": "CHEBI:1", "ontology_label": "2-Mercaptoethanesulfonate", "ontology_source": "CHEBI"}
    assert mod.needs_correction(om, resolve) == "coenzyme M"


def test_casing_only_corrected():
    # exact (byte) comparison: a casing-only difference IS corrected to canonical.
    om = {"ontology_id": "CHEBI:2", "ontology_label": "Acetate", "ontology_source": "CHEBI"}
    assert mod.needs_correction(om, resolve) == "acetate"


def test_already_canonical_skipped():
    om = {"ontology_id": "CHEBI:1", "ontology_label": "coenzyme M", "ontology_source": "CHEBI"}
    assert mod.needs_correction(om, resolve) is None


def test_empty_label_filled():
    om = {"ontology_id": "CHEBI:2", "ontology_label": "", "ontology_source": "CHEBI"}
    assert mod.needs_correction(om, resolve) == "acetate"


def test_id_source_mismatch_skipped():
    # CHEBI id tagged with a non-CHEBI source = the documented mismatch class; skip.
    om = {"ontology_id": "CHEBI:1", "ontology_label": "x", "ontology_source": "NCIT"}
    assert mod.needs_correction(om, resolve) is None


def test_unresolvable_id_skipped():
    # resolver returns None (obsolete/junk/absent) -> never blank a label.
    om = {"ontology_id": "CHEBI:999", "ontology_label": "keep me", "ontology_source": "CHEBI"}
    assert mod.needs_correction(om, resolve) is None


def test_no_adapter_prefix_skipped():
    # cas:/registry prefixes have no trusted adapter -> untouched.
    om = {"ontology_id": "cas:7647-14-5", "ontology_label": "NaCl", "ontology_source": "cas"}
    assert mod.needs_correction(om, resolve) is None
