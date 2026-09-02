"""Pin the surface-form backfill's selection logic.

Every case here failed at least once. The costly one was a variable-shadowing bug that
produced no error and no wrong data -- only silent under-application: the loop's
`(subject_id, object_id)` tuple was rebound to a token string inside the token loop, so
`records.get(key[0])` looked up the token's first CHARACTER for every later token in the
same row. Each row migrated its first surface form and counted the rest as "no matching
record". It cost 187 surface forms and was invisible except as an implausible statistic.
"""

from __future__ import annotations

import importlib.util
import re
import sys
from pathlib import Path

import pytest

_REPO = Path(__file__).resolve().parent.parent


def _load(name: str):
    spec = importlib.util.spec_from_file_location(name, _REPO / "scripts" / f"{name}.py")
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


bf = _load("backfill_sssom_surface_forms")


class TestTheLoopVariableIsNotRebound:
    """The shadowing bug, pinned as a property of the source.

    A behavioural test would need the full corpus plus a kg-microbe checkout; the defect
    is a one-line rebinding, and asserting it cannot come back is both cheaper and more
    direct than reconstructing the conditions that expose it.
    """

    def test_no_assignment_to_the_loop_key_inside_the_token_loop(self):
        source = (_REPO / "scripts" / "backfill_sssom_surface_forms.py").read_text(encoding="utf-8")
        body = source.split("for key, pub_row in published.items():", 1)
        assert len(body) == 2, "the main loop was renamed; update this guard"
        assert not re.search(r"^\s+key = ", body[1], re.M), (
            "rebinding `key` inside the loop makes records.get(key[0]) index a string"
        )

    def test_the_subject_is_read_from_a_stable_name(self):
        source = (_REPO / "scripts" / "backfill_sssom_surface_forms.py").read_text(encoding="utf-8")
        assert "key_subject = key[0]" in source


class TestCurieRoundTrip:
    """Subjects are the record filename with non-URL-safe characters `~HEX`-escaped.

    Matching on the raw stem alone misses every record whose filename has a parenthesis
    or a Greek letter.
    """

    @pytest.mark.parametrize(
        "stem,curie",
        [
            ("(R)-lactate", "MIM:~28R~29-lactate"),
            ("Calcium(2)", "MIM:Calcium~282~29"),
            ("plain_name", "MIM:plain_name"),
            ("with.dot-and_underscore", "MIM:with.dot-and_underscore"),
        ],
    )
    def test_escaping_matches_the_builder(self, stem, curie):
        assert bf.mim_curie(stem) == curie

    def test_records_are_reachable_under_both_spellings(self):
        by_subject = bf.records_by_subject()
        assert by_subject, "no records found"
        sample = next(p for p in (_REPO / "data" / "ingredients").rglob("*.yaml"))
        assert f"MIM:{sample.stem}" in by_subject
        assert bf.mim_curie(sample.stem) in by_subject


class TestDamageTriage:
    def test_chebi_hydrate_notation_is_not_damage(self):
        """ChEBI writes hydrates as `<compound>--water (1/n)`."""
        assert not bf.is_damaged("cobalt(2+) sulfate--water (1/7)")

    def test_cas_inverted_nomenclature_is_not_damage(self):
        """CAS index names invert and end on the substituent's hyphen."""
        assert not bf.is_damaged("beta-D-glucopyranose, 4-O-beta-D-galactopyranosyl-")

    @pytest.mark.parametrize("token", ["2--Mercaptoethanol", "DL--Mevalonic acid"])
    def test_a_doubled_hyphen_in_a_name_is_damage(self, token):
        assert bf.is_damaged(token)

    def test_a_doubled_hyphen_repairs(self):
        assert bf.repair("2--Mercaptoethanol") == "2-Mercaptoethanol"

    def test_a_trailing_comma_repairs(self):
        assert bf.repair("Ethylenediamintetraacetic acid (EDTA),") == (
            "Ethylenediamintetraacetic acid (EDTA)"
        )

    def test_truncation_inside_a_parenthetical_is_unrepairable(self):
        """The lost text cannot be recovered and guessing it would fabricate a synonym."""
        assert bf.repair("Methyl alpha-D-mannopyranoside (methyl alpha-") is None

    @pytest.mark.parametrize(
        "token", ["utilizes: 1,2-propandiol", "carbon source: acetate", "Role: buffer"]
    )
    def test_role_text_is_recognised(self, token):
        assert bf._ROLE_TEXT.match(token)
