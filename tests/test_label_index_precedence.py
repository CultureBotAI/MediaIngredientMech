"""Precedence rules for `docs/data/label_index.csv` (issue #232).

Under the #260 direction CultureMech resolves groundings from this file by
taking the FIRST row for a label, so row order is not presentation — it decides
which identifier a consumer gets. `docs/LABEL_INDEX_CONTRACT.md` states the
rules; these tests pin them, because the two defects below both shipped.

The tests build records in memory rather than reading the published CSV: a test
that asserts against the artifact passes trivially once the artifact is
regenerated, and would not have caught either bug.
"""

import csv
import importlib.util
import sys
from pathlib import Path

ROOT = Path(__file__).parent.parent


def _load():
    spec = importlib.util.spec_from_file_location(
        "export_lists", ROOT / "scripts" / "export_lists.py")
    mod = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = mod
    spec.loader.exec_module(mod)
    return mod


def _record(identifier, preferred_term, status="MAPPED", synonyms=(),
            ontology_label=None):
    return {
        "identifier": identifier,
        "preferred_term": preferred_term,
        "mapping_status": status,
        "synonyms": [{"synonym_text": s} for s in synonyms],
        "ontology_mapping": {"ontology_id": identifier,
                             "ontology_label": ontology_label or preferred_term},
    }


def _resolve(tmp_path, records):
    """label -> the row a take-the-first-row consumer receives."""
    mod = _load()
    tmp_path.mkdir(parents=True, exist_ok=True)
    out = tmp_path / "label_index.csv"
    mod.export_label_index(records, out)
    first = {}
    with out.open() as f:
        for row in csv.DictReader(f):
            first.setdefault(row["label"].strip().lower(), row)
    return first


def test_uppercase_synonym_does_not_outrank_the_owning_record(tmp_path):
    """The raw `label` used to sort second, above every semantic key, so among
    case variants ASCII decided the winner and uppercase won.

    `FRUCTOSE` — a synonym on `Fructooligosaccharides (FOS)` — outranked
    `Fructose`, the record that owns the label, so the consumer received a
    polymer for the sugar. 16 labels resolved to the wrong record this way,
    including `Citric acid` -> trisodium citrate and `Asparagine`/`Cysteine`
    -> the L-enantiomer of a stereo-unspecified label.
    """
    got = _resolve(tmp_path, [
        _record("cas:308066-66-2", "Fructooligosaccharides (FOS)",
                synonyms=["FRUCTOSE"]),
        _record("CHEBI:28757", "Fructose"),
    ])
    assert got["fructose"]["identifier"] == "CHEBI:28757"
    assert got["fructose"]["match_type"] == "preferred_term"


def test_owning_tombstone_beats_another_records_synonym(tmp_path):
    """Ownership outranks MAPPED-ness.

    A record whose own preferred_term IS the label makes a claim about exactly
    that string; a synonym on a different record is a weaker claim about
    something else. A tombstone still resolves — it carries the merge winner's
    identifier — so `LABEL_INDEX_CONTRACT` says REJECTED is not "no answer".

    Without this, `FeSO4 x 7H2O` resolved to CHEBI:75832 `FeSO4 x 5 H2O`: a
    heptahydrate label answered with the pentahydrate.

    The live winner is in the fixture because it is in the real data: the
    tombstone was merged INTO `FeSO4 x 7 H2O` and carries its identifier. That
    is what makes the tombstone resolvable, and the next test covers what
    happens when it is not.
    """
    got = _resolve(tmp_path, [
        _record("CHEBI:75832", "FeSO4 x 5 H2O", synonyms=["FeSO4 x 7H2O"]),
        _record("CHEBI:75836", "FeSO4 x 7H2O", status="REJECTED"),
        _record("CHEBI:75836", "FeSO4 x 7 H2O"),
    ])
    assert got["feso4 x 7h2o"]["identifier"] == "CHEBI:75836"


def test_a_dangling_tombstone_does_not_win_on_ownership(tmp_path):
    """Ownership only jumps the queue when the owner actually resolves.

    A merge tombstone is a legitimate owner because it carries the winner's
    identifier — but nothing gates that invariant, and one left pointing at its
    own dead accession resolves to nothing. `Bacto Soytone` sat on the obsolete
    CHEBI:8150 until #360 repointed it, and while it did, a consumer following
    ownership would have got the obsolete term instead of the live
    FOODON:03315720 that answers to the same label.

    No live record holds CHEBI:8150 here, so the live synonym wins.
    """
    got = _resolve(tmp_path, [
        _record("CHEBI:8150", "Bacto Soytone", status="REJECTED"),
        _record("FOODON:03315720", "Soy peptone", synonyms=["Bacto Soytone"]),
    ])
    assert got["bacto soytone"]["identifier"] == "FOODON:03315720"


def test_among_non_owners_a_live_record_beats_a_tombstone(tmp_path):
    """Ownership jumps the queue, but nothing else does — otherwise promoting
    match_type above status would let a tombstone's SYNONYM beat a live
    record's term label, which sent `EDTA disodium salt (anhydrous)` back to
    the rejected dihydrate. No record owns that label, so status decides.
    """
    got = _resolve(tmp_path, [
        _record("CHEBI:64758", "Na2-EDTA x 2 H2O", status="REJECTED",
                synonyms=["EDTA disodium salt (anhydrous)"]),
        _record("CHEBI:64734", "Na2-EDTA",
                ontology_label="EDTA disodium salt (anhydrous)"),
    ])
    assert got["edta disodium salt (anhydrous)"]["identifier"] == "CHEBI:64734"


def test_preferred_term_beats_synonym_beats_ontology_label(tmp_path):
    """The ranking among match types, all else equal. `ontology_label` is last:
    a term label is the ontology's name for the concept, not a name this record
    claims about itself."""
    got = _resolve(tmp_path, [
        _record("CHEBI:3", "Third", ontology_label="Shared"),
        _record("CHEBI:2", "Second", synonyms=["Shared"]),
        _record("CHEBI:1", "Shared"),
    ])
    assert got["shared"]["identifier"] == "CHEBI:1"
    assert got["shared"]["match_type"] == "preferred_term"


def test_ordering_is_deterministic_regardless_of_record_order(tmp_path):
    """`identifier` is not a unique record key — 46 identifiers are held by 117
    records — so without a full tiebreak the winner is decided by YAML order,
    and a reordering silently changes published answers."""
    a = _record("CHEBI:2", "Second", synonyms=["Shared"])
    b = _record("CHEBI:9", "Ninth", synonyms=["Shared"])
    assert (_resolve(tmp_path / "x", [a, b])["shared"]["identifier"]
            == _resolve(tmp_path / "y", [b, a])["shared"]["identifier"])
