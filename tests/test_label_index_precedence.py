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
            ontology_label=None, formula=None):
    r = {
        "identifier": identifier,
        "preferred_term": preferred_term,
        "mapping_status": status,
        "synonyms": [{"synonym_text": s} for s in synonyms],
        "ontology_mapping": {"ontology_id": identifier,
                             "ontology_label": ontology_label or preferred_term},
    }
    if formula:
        r["chemical_properties"] = {"molecular_formula": formula}
    return r


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


# --- ambiguity verdicts (#232) ---------------------------------------------
#
# `take the first row` cannot be honoured for every label: 167 are carried as a
# synonym by records that are not the same substance, so an arbitrary first row
# hands over the wrong compound. These pin the vocabulary a consumer branches on.


def test_conflicting_formulas_are_published_as_a_conflict(tmp_path):
    """The salt-inheritance case: a free acid's systematic name is carried by
    its salts, whose formulas differ by a counterion. Real instance —
    `(2S)-2-aminobutanedioic acid` resolves to L-aspartic acid AND its potassium
    salt AND its sodium salt monohydrate."""
    got = _resolve(tmp_path, [
        _record("CHEBI:17053", "L-Aspartic acid", formula="C4H7NO4",
                synonyms=["(2S)-2-aminobutanedioic acid"]),
        _record("cas:1115-63-5", "L-Aspartic acid potassium salt", formula="C4H6KNO4",
                synonyms=["(2S)-2-aminobutanedioic acid"]),
    ])
    assert got["(2s)-2-aminobutanedioic acid"]["ambiguity"] == "conflict:different_substances"


def test_matching_formulas_are_not_a_conflict(tmp_path):
    """ChEBI models the neutral species and the zwitterion separately and both
    legitimately carry the name. Nothing is wrong and either pick is correct, so
    flagging it would cry wolf."""
    got = _resolve(tmp_path, [
        _record("CHEBI:17561", "L-Cysteine", formula="C3H7NO2S",
                synonyms=["(2R)-2-ammonio-3-sulfanylpropanoate"]),
        _record("CHEBI:35235", "L-cysteine zwitterion", formula="C3H7NO2S",
                synonyms=["(2R)-2-ammonio-3-sulfanylpropanoate"]),
    ])
    assert got["(2r)-2-ammonio-3-sulfanylpropanoate"]["ambiguity"] == "agree:same_substance"


def test_an_owned_label_is_never_flagged_ambiguous(tmp_path):
    """Ownership short-circuits the formula check. Without this the prototype
    flagged `Citric acid` — which CHEBI:30769 owns and precedence already
    resolves — as a conflict, marking 97 correct answers untrustworthy."""
    got = _resolve(tmp_path, [
        _record("CHEBI:53258", "Trisodium citrate", formula="C6H5O7.3Na",
                synonyms=["Citric acid"]),
        _record("CHEBI:30769", "Citric acid", formula="C6H8O7"),
    ])
    assert got["citric acid"]["ambiguity"] == "resolved:owned"
    assert got["citric acid"]["identifier"] == "CHEBI:30769"


def test_missing_chemistry_is_unresolved_not_agreement(tmp_path):
    """Absent formulas must not read as 'the same substance'. A third of records
    carry no formula, so defaulting to agreement would silently bless the very
    collisions this column exists to expose."""
    got = _resolve(tmp_path, [
        _record("CHEBI:39005", "MES", formula="C6H13NO4S", synonyms=["shared"]),
        _record("cas:145224-94-8", "MES Hydrat", synonyms=["shared"]),
    ])
    assert got["shared"]["ambiguity"] == "unresolved:partial_chemistry"

    got = _resolve(tmp_path / "b", [
        _record("ENVO:00003031", "Dry cow-manure", synonyms=["animal manure"]),
        _record("UNMAPPED_0367", "Cow manure", status="UNMAPPED",
                synonyms=["animal manure"]),
    ])
    assert got["animal manure"]["ambiguity"] == "unresolved:no_chemistry"


def test_an_unambiguous_label_says_unique(tmp_path):
    got = _resolve(tmp_path, [_record("CHEBI:17234", "Glucose", formula="C6H12O6")])
    assert got["glucose"]["ambiguity"] == "unique"


def test_ambiguity_is_the_last_column(tmp_path):
    """Appended, not inserted: a consumer indexing positionally keeps working."""
    mod = _load()
    tmp_path.mkdir(parents=True, exist_ok=True)
    out = tmp_path / "label_index.csv"
    mod.export_label_index([_record("CHEBI:1", "X")], out)
    assert out.read_text().splitlines()[0].split(",")[-1] == "ambiguity"


def test_dot_notation_formulas_are_not_a_false_conflict(tmp_path):
    """ChEBI writes salts in dot notation and other sources collapse them, so a
    raw-string comparison called potassium tellurite two substances (#389).
    `2K.O3Te` and `K2O3Te` are the same compound."""
    got = _resolve(tmp_path, [
        _record("CHEBI:75248", "K2TeO3", formula="2K.O3Te",
                synonyms=["potassium tellurite"]),
        # NOT named "Potassium tellurite": that would OWN the label and return
        # resolved:owned, testing the wrong branch entirely.
        _record("cas:123333-66-4", "K2TeO3 (Sigma)", formula="K2O3Te",
                synonyms=["potassium tellurite"]),
    ])
    assert got["potassium tellurite"]["ambiguity"] == "agree:same_substance"


def test_hydrate_and_anhydrous_still_conflict(tmp_path):
    """The dot-notation fix must not collapse a hydrate into its anhydrous form:
    `2Cl.Co` and `2Cl.Co.6H2O` differ by six waters and are different
    substances. Real case — `CoCl2 x 6 H2O` resolves to both."""
    got = _resolve(tmp_path, [
        _record("CHEBI:35696", "CoCl2", formula="2Cl.Co", synonyms=["CoCl2 x 6 H2O"]),
        _record("CHEBI:53503", "CoCl2 hexahydrate", formula="2Cl.Co.6H2O",
                synonyms=["CoCl2 x 6 H2O"]),
    ])
    assert got["cocl2 x 6 h2o"]["ambiguity"] == "conflict:different_substances"


def test_formula_lookup_ignores_record_order_for_a_shared_identifier(tmp_path):
    """`identifier` is not unique — a merge tombstone carries the winner's — and
    28 shared identifiers disagree on formula. A last-wins lookup let YAML order
    decide the published verdict (#388). The first NON-EMPTY formula wins, so
    both orderings agree."""
    tomb = _record("CHEBI:41189", "Butane-1,4-diol", status="REJECTED")
    live = _record("CHEBI:41189", "1,4-Butanediol", formula="C4H10O2",
                   synonyms=["shared name"])
    other = _record("CHEBI:99999", "Something else", formula="C9H9N9",
                    synonyms=["shared name"])
    a = _resolve(tmp_path / "a", [tomb, live, other])["shared name"]["ambiguity"]
    b = _resolve(tmp_path / "b", [live, tomb, other])["shared name"]["ambiguity"]
    assert a == b == "conflict:different_substances"


def test_an_unparseable_formula_is_unknown_not_disagreement(tmp_path):
    """Guessing either way is worse than saying it could not be checked."""
    got = _resolve(tmp_path, [
        _record("CHEBI:1", "Real", formula="C6H12O6", synonyms=["shared"]),
        _record("CHEBI:2", "Junk", formula="???", synonyms=["shared"]),
    ])
    assert got["shared"]["ambiguity"] == "unresolved:partial_chemistry"
