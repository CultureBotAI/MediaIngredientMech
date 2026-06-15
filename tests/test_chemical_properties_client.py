"""Tests for ChemicalPropertiesClient's OLS4 response parsing.

Regression: OLS4 renamed its chemical-property annotation keys
(formula -> generalized_empirical_formula; SMILES/InChI -> *_string) and dropped
the legacy `formula` key, which silently broke formula/SMILES/InChI enrichment
(every fetch returned None). These pin the current keys, the legacy fallback, and
the formula-less ceiling. `requests.get` is monkeypatched — CI-safe, no network.
"""

import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).parent.parent / "src"))
from mediaingredientmech.utils import chemical_properties_client as mod  # noqa: E402


class _FakeResp:
    def __init__(self, payload, status=200):
        self._p, self.status_code = payload, status
        self.ok = status == 200

    def json(self):
        return self._p

    def raise_for_status(self):
        if not self.ok:
            raise mod.requests.HTTPError(str(self.status_code))


def _patch(monkeypatch, ols_payload, ols_status=200):
    """Route OLS4 calls to ols_payload; make every PubChem call a clean miss."""
    def fake_get(url, timeout=10, **kw):
        if "ols4" in url:
            return _FakeResp(ols_payload, ols_status)
        return _FakeResp({}, 404)  # PubChem fallback returns nothing
    monkeypatch.setattr(mod.requests, "get", fake_get)
    return mod.ChemicalPropertiesClient(cache_enabled=False)


CURRENT_KEYS = {
    "annotation": {
        "generalized_empirical_formula": ["C6H12O6"],
        "mass": ["180.156"],
        "smiles_string": ["OC[C@H]1OC(O)[C@H](O)[C@@H](O)[C@@H]1O"],
        "inchi_string": ["InChI=1S/C6H12O6/c7-1-2-3(8)4(9)5(10)6(11)12-2/h2-11H,1H2"],
    }
}


def test_parses_current_ols4_keys(monkeypatch):
    c = _patch(monkeypatch, CURRENT_KEYS)
    p = c.get_properties("CHEBI:17234", "glucose", "CHEBI")
    assert p is not None
    assert p.molecular_formula == "C6H12O6"
    assert p.smiles.startswith("OC[C@H]")
    assert p.inchi.startswith("InChI=1S/C6H12O6")
    assert abs(p.molecular_weight - 180.156) < 0.01


def test_legacy_formula_key_still_works(monkeypatch):
    # resilience: if OLS4 ever serves the old `formula` key again, still parse it
    c = _patch(monkeypatch, {"annotation": {"formula": ["NaCl"], "mass": ["58.44"]}})
    p = c.get_properties("CHEBI:26710", "sodium chloride", "CHEBI")
    assert p is not None and p.molecular_formula == "NaCl"


def test_no_chem_keys_returns_none(monkeypatch):
    # abstract class / polymer: no formula/smiles/inchi/mass -> None (the ceiling,
    # not a failure). This is what kept the 75 class/polymer targets unenriched.
    c = _patch(monkeypatch, {"annotation": {"has_obo_namespace": ["chebi_ontology"], "id": ["CHEBI:33655"]}})
    assert c.get_properties("CHEBI:33655", "aromatic compound", "CHEBI") is None


def test_non_chebi_source_skipped(monkeypatch):
    c = _patch(monkeypatch, CURRENT_KEYS)
    assert c.get_properties("FOODON:03411448", "yeast extract", "FOODON") is None
