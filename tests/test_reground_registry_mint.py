"""Re-grounding a record onto a registry mint (#273).

MAPPING_SEMANTICS.md Section 3: a substance with no exact ontology term takes its
registry CURIE (`cas:` / `kgmicrobe.compound:`) as identifier AND asserts a
narrowMatch to the nearest ontology parent. 248 records already hold `cas:`
identifiers in that shape, but until #273 no tool could MOVE an existing mapped
record into it — the destination was validated against an ontology adapter, which
a mint never resolves in, so the script refused.

The Rule B1 pairing is the part that matters: a narrowMatch from a MIM subject
with no sibling registry exactMatch row fails validate_sssom_invariants, which is
how PR #275's Sodium succinate dibasic broke CI.
"""

from __future__ import annotations

import importlib.util
from pathlib import Path

import pytest

_spec = importlib.util.spec_from_file_location(
    "reground_mapped_record",
    Path(__file__).resolve().parent.parent / "scripts" / "reground_mapped_record.py",
)
mod = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(mod)


@pytest.mark.parametrize("curie", [
    "cas:150-90-3",
    "kgmicrobe.compound:sodium_succinate_dibasic",
    "kgmicrobe.ingredient:rumen_fluid",
])
def test_registry_mints_are_recognised(curie):
    assert mod.is_registry_mint(curie)


@pytest.mark.parametrize("curie", [
    "CHEBI:15741", "FOODON:03315719", "MICRO:0000520", "UBERON:0010228",
])
def test_ontology_terms_are_not_mints(curie):
    """An ontology term must keep taking the resolve-and-validate path."""
    assert not mod.is_registry_mint(curie)


def test_every_mint_prefix_maps_to_an_sssom_object_source():
    """A registry row with a blank object_source is malformed.

    The prefix list and the source map are separate constants; if one grows
    without the other, the emitted Rule B1 row silently loses its source column.
    """
    for prefix in mod.REGISTRY_PREFIXES:
        assert prefix.rstrip(":") in mod.REGISTRY_SOURCE


# --- the SSSOM half -----------------------------------------------------------

HEADER = ("subject_id\tsubject_label\tpredicate_id\tobject_id\tobject_label\t"
          "object_source\tmapping_justification\tmapping_source\tmapping_date\t"
          "confidence\tcomment\tsee_also\treview\n")
ROW = ("MIM:Widget\tWidget\tskos:exactMatch\tCHEBI:111\told label\tobo:chebi.owl\t"
       "semapv:ManualMappingCuration\tMIM:x\t2026-08-06\t0.95\t\t\t\n")


def _write(tmp_path, monkeypatch):
    p = tmp_path / "m.sssom.tsv"
    p.write_text(HEADER + ROW)
    monkeypatch.setattr(mod, "SSSOM", p)
    return p


def test_ontology_reground_rewrites_object_and_keeps_one_row(tmp_path, monkeypatch):
    _write(tmp_path, monkeypatch)
    text, _ = mod.plan_sssom("Widget", "CHEBI:111", "CHEBI:222", "new label")
    rows = [ln for ln in text.splitlines() if ln.startswith("MIM:")]
    assert len(rows) == 1, "an ordinary re-ground must not add a row"
    cols = rows[0].split("\t")
    assert cols[2] == "skos:exactMatch", "predicate is unchanged without a mint"
    assert (cols[3], cols[4]) == ("CHEBI:222", "new label")


def test_mint_reground_emits_the_rule_b1_pair(tmp_path, monkeypatch):
    _write(tmp_path, monkeypatch)
    text, note = mod.plan_sssom("Widget", "CHEBI:111", "CHEBI:222", "parent label",
                                mint="cas:150-90-3")
    rows = [ln.split("\t") for ln in text.splitlines() if ln.startswith("MIM:")]
    assert len(rows) == 2, "Rule B1 needs the narrowMatch AND its registry sibling"

    narrow, registry = rows
    assert narrow[2] == "skos:narrowMatch"
    assert (narrow[3], narrow[4]) == ("CHEBI:222", "parent label")

    assert registry[2] == "skos:exactMatch"
    assert registry[3] == "cas:150-90-3"
    assert registry[4] == "Widget", "the registry row's object_label is the subject"
    assert registry[5] == "registry:cas", "object_source must name the registry"
    assert "Rule B1" in note


def test_mint_reground_keeps_the_subject_so_the_row_need_not_re_sort(tmp_path, monkeypatch):
    _write(tmp_path, monkeypatch)
    text, _ = mod.plan_sssom("Widget", "CHEBI:111", "CHEBI:222", "p",
                             mint="kgmicrobe.compound:widget")
    for ln in [l for l in text.splitlines() if l.startswith("MIM:")]:
        assert ln.split("\t")[:2] == ["MIM:Widget", "Widget"]


def test_a_stale_object_id_is_refused(tmp_path, monkeypatch):
    """Guards against rewriting a row that has already moved."""
    _write(tmp_path, monkeypatch)
    with pytest.raises(SystemExit):
        mod.plan_sssom("Widget", "CHEBI:999", "CHEBI:222", "p")


# --- Rule B1 slug conformance (#279) ------------------------------------------
# Rule B1 does not just want *a* registry row: _has_registry_row matches
# kgmicrobe.(ingredient|compound):<subject slug lowercased> exactly. A mint spelled
# differently produces a row that looks right and satisfies nothing — caught only
# after the write, as CI failing on an already-published row.


def test_mint_local_part_is_derived_from_the_subject_slug():
    got = mod.check_registry_mint("kgmicrobe.compound:", "Potassium_5-ketogluconate")
    assert got == "kgmicrobe.compound:potassium_5-ketogluconate"


def test_a_mismatched_mint_is_refused_and_the_message_names_the_right_one():
    """This exact spelling passed the tool and then failed Rule B1 in practice."""
    with pytest.raises(SystemExit) as e:
        mod.check_registry_mint("kgmicrobe.compound:potassium_5_ketogluconate",
                                "Potassium_5-ketogluconate")
    assert "kgmicrobe.compound:potassium_5-ketogluconate" in str(e.value)


def test_a_correctly_spelled_mint_passes_through():
    curie = "kgmicrobe.compound:maltose_hydrate"
    assert mod.check_registry_mint(curie, "Maltose_Hydrate") == curie


def test_cas_mints_are_exempt_from_slug_conformance():
    """Rule B1's registry regex covers the kgmicrobe namespaces; a CAS number has
    no relationship to the subject slug and must not be rewritten into one."""
    assert mod.check_registry_mint("cas:150-90-3", "Sodium_Succinate_Dibasic") == "cas:150-90-3"
