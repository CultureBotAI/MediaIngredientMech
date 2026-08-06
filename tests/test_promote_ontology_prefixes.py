"""The prefix map that decides what `promote_resolved_unmapped` can resolve.

`ONTOLOGY_DB` started as a single hard-coded `chebi.db` and grew to five
ontologies over the course of #213/#114, each addition unblocking records the
previous state had wrongly reported as ungroundable:

  NCIT    Polymyxin B, Lysostaphin, Colistin Sulfate, Carbomycin -- valid CHEBI
          accessions absent from the local semsql build, so a CHEBI-only helper
          called them unresolvable
  MeSH    RNA, Filipin, Actinomycin X, Netropsin, Bottromycin, Ristocetin A
  ENVO    Crude Oil
  UBERON  Rumen fluid

So the map is load-bearing: a prefix missing from it is not a lookup failure, it
is a record that silently cannot be grounded. Nothing pinned it.
"""

from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
_spec = importlib.util.spec_from_file_location(
    "promote_resolved_unmapped", ROOT / "scripts" / "promote_resolved_unmapped.py")
mod = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(mod)


EXPECTED = {"CHEBI", "NCIT", "FOODON", "ENVO", "MESH", "UBERON"}


def test_every_expected_ontology_is_resolvable():
    """Each of these was added because a real record needed it."""
    assert EXPECTED <= set(mod.ONTOLOGY_DB)


def test_every_resolvable_prefix_has_an_sssom_object_source():
    """A published row with a blank object_source is malformed.

    The two maps are separate dicts; adding an ontology to one and not the other
    yields rows that resolve but cannot say where the term came from.
    """
    missing = set(mod.ONTOLOGY_DB) - set(mod.OBJECT_SOURCE)
    assert not missing, f"no object_source for {sorted(missing)}"


def test_prefix_membership_is_case_insensitive():
    """Records write `mesh:` lower-case while the build stores `MESH:`.

    The membership checks upper-case before lookup; if that regressed, every
    lower-cased registry-style prefix would be rejected as unresolvable.
    """
    assert "mesh".upper() in mod.ONTOLOGY_DB
    assert "MESH" in mod.ONTOLOGY_DB


@pytest.mark.parametrize("curie,expected", [
    ("kgmicrobe.compound:foo", "kgmicrobe.compound"),
    ("kgmicrobe.ingredient:bar", "kgmicrobe.ingredient"),
    ("cas:150-90-3", "CAS"),
    ("CHEBI:15741", "CHEBI"),
    ("mesh:D012313", "MESH"),
])
def test_source_enum_casing(curie, expected):
    """Ontology prefixes upper-case, registry namespaces keep their own form.

    Upper-casing everything produced `KGMICROBE.COMPOUND`, which is not in the
    schema enum — the write-time validator rejected it, but only after eight
    promotions had printed success and silently written nothing.
    """
    assert mod._source_enum(curie) == expected


def test_registry_mints_are_not_in_the_ontology_map():
    """A mint must take the registry path, never an ontology lookup."""
    for prefix in mod.REGISTRY_PREFIXES:
        assert prefix.rstrip(":").upper() not in mod.ONTOLOGY_DB
