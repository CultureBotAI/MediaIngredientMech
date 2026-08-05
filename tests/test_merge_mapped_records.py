"""Guards for MAPPED-to-MAPPED merging (#226).

This is the case no other script could do — and every one of the 61 groups in
`duplicate_identifier_baseline.tsv` is `collection=mapped`, so it is the case
that actually blocks the backlog. The semantics are the repo's own:
`audit_occurrence_stats.py` documents that a REJECTED merged record must have
had its counts "transferred to its representative", so these tests pin transfer
plus tombstone, not deletion.
"""

import importlib.util
import sys
from pathlib import Path

import pytest
import yaml

ROOT = Path(__file__).parent.parent
SCRIPT = ROOT / "scripts" / "merge_mapped_records.py"


def _load():
    spec = importlib.util.spec_from_file_location("merge_mapped_records", SCRIPT)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = mod
    spec.loader.exec_module(mod)
    return mod


@pytest.fixture(scope="module")
def mod():
    return _load()


def rec(curie, term, occ=(0, 0), syns=(), status="MAPPED", roles=None):
    r = {"identifier": curie, "preferred_term": term, "mapping_status": status,
         "synonyms": [{"synonym_text": s, "synonym_type": "RAW_TEXT"} for s in syns],
         "occurrence_statistics": {"total_occurrences": occ[0], "media_count": occ[1]}}
    if roles:
        r["nutritional_roles"] = roles
    return r


def test_one_refuses_an_ambiguous_curie(mod):
    recs = [rec("CHEBI:1", "A"), rec("CHEBI:1", "B")]
    with pytest.raises(SystemExit, match="expected exactly 1"):
        mod.one(recs, "CHEBI:1", None, "--from")
    assert mod.one(recs, "CHEBI:1", "B", "--from")["preferred_term"] == "B"


def test_source_id_is_scraped_from_notes(mod):
    assert mod.source_id({"notes": "Imported (source_id=kgmicrobe.trait:x); ..."}) \
        == "kgmicrobe.trait:x"
    assert mod.source_id({"notes": None}) is None


def test_dropped_sssom_rows_are_the_sources_only(mod, tmp_path, monkeypatch):
    tsv = tmp_path / "s.tsv"
    tsv.write_text("subject_id\tsubject_label\tp\n"
                   "MIM:A\tA\tx\nMIM:B\tB\tx\nMIM:B\tB\ty\n")
    monkeypatch.setattr(mod, "SSSOM", tsv)
    text, dropped = mod.drop_sssom_rows("B", apply=False)
    assert dropped == 2
    assert "MIM:A\tA" in text and "MIM:B" not in text
    assert tsv.read_text().count("MIM:B") == 2, "dry-run must not write"


def test_occurrences_transfer_and_source_is_tombstoned(mod, tmp_path, monkeypatch):
    """The repo's semantics: counts move to the representative, the source
    becomes a REJECTED tombstone reporting zero — not a deletion."""
    coll = {"total_count": 2, "mapped_count": 2,
            "ingredients": [rec("CHEBI:1", "Winner", (10, 4)),
                            rec("CHEBI:1", "Loser", (6, 3), syns=("alt",),
                                roles=[{"role": "CARBON_SOURCE"}])]}
    src = tmp_path / "mapped.yaml"
    src.write_text(yaml.safe_dump(coll))
    tsv = tmp_path / "s.tsv"
    tsv.write_text("subject_id\tsubject_label\tp\nMIM:Loser\tLoser\tx\n")
    monkeypatch.setattr(mod, "MAPPED", src)
    monkeypatch.setattr(mod, "SSSOM", tsv)
    monkeypatch.setattr(sys, "argv", ["x", "--from", "CHEBI:1", "--from-term", "Loser",
                                      "--into", "CHEBI:1", "--into-term", "Winner",
                                      "--reason", "same substance", "--apply"])
    mod.main()

    out = yaml.safe_load(src.read_text())
    winner = [r for r in out["ingredients"] if r["preferred_term"] == "Winner"][0]
    loser = [r for r in out["ingredients"] if r["preferred_term"] == "Loser"][0]

    assert winner["occurrence_statistics"] == {"total_occurrences": 16, "media_count": 7}
    assert loser["mapping_status"] == "REJECTED", "tombstone, not delete"
    assert loser["occurrence_statistics"] == {"total_occurrences": 0, "media_count": 0}, \
        "audit_occurrence_stats flags a REJECTED record still reporting occurrences"
    syns = {s["synonym_text"] for s in winner["synonyms"]}
    assert {"Loser", "alt"} <= syns, "the source's name and synonyms must survive"
    assert winner.get("nutritional_roles"), "role facets union onto the survivor"
    assert out["mapped_count"] == 1
    assert "MIM:Loser" not in tsv.read_text(), "a row pointing at a REJECTED record is ORPHAN"


def test_refuses_when_either_record_is_not_mapped(mod, tmp_path, monkeypatch):
    coll = {"ingredients": [rec("CHEBI:1", "A"), rec("CHEBI:2", "B", status="REJECTED")]}
    src = tmp_path / "m.yaml"; src.write_text(yaml.safe_dump(coll))
    monkeypatch.setattr(mod, "MAPPED", src)
    monkeypatch.setattr(sys, "argv", ["x", "--from", "CHEBI:2", "--into", "CHEBI:1",
                                      "--reason", "r"])
    with pytest.raises(SystemExit, match="not MAPPED"):
        mod.main()
