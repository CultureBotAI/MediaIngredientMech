"""A `MIM:` subject is the record's escaped file stem, and nothing re-derives it (#236).

#236 asked whether `MIM:` slugs are paths or opaque ids. The pipeline had
already answered: claw's publisher emits `MIM:<safe_stem>`, `CurieNormalizer`
resolves subjects against file stems, and `FilenameIndex` never renames a file.
Deriving the subject from the stem makes it both stable and file-backed, so the
trade-off #236 described never had to be made.

What was left was every place that disagreed: a relabel script that rewrote the
subject from the new label (#236's own mechanism), writers that took the right
stem but forgot to escape it, a one-shot that spelled a subject from a label,
five hand-written copies of the escape rule, and a checker that compared
subjects against *unescaped* stems and so reported 18 false alarms.
"""

from __future__ import annotations

import importlib
import re
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
sys.path.insert(0, str(ROOT / "scripts"))

from mediaingredientmech.curie import mim_curie_for_stem  # noqa: E402

HEADER = ("subject_id\tsubject_label\tpredicate_id\tobject_id\tobject_label\n")


# --------------------------------------------------------------------------- #
# The rule itself
# --------------------------------------------------------------------------- #

def test_a_safe_stem_is_its_own_subject():
    assert mim_curie_for_stem("Glucose") == "MIM:Glucose"


def test_unsafe_characters_are_escaped():
    assert mim_curie_for_stem("(R)-lactate") == "MIM:~28R~29-lactate"


# --------------------------------------------------------------------------- #
# The checker: 18 false alarms came from comparing against unescaped stems
# --------------------------------------------------------------------------- #

@pytest.fixture
def checker():
    return importlib.import_module("check_sssom_subject_files")


def _tree(tmp_path, stems):
    mapped = tmp_path / "mapped"
    mapped.mkdir()
    for stem in stems:
        (mapped / f"{stem}.yaml").write_text("identifier: X:1\n", encoding="utf-8")
    return (mapped,)


def _sssom(tmp_path, subjects):
    path = tmp_path / "s.tsv"
    body = "".join(f"{s}\tlabel\tskos:exactMatch\tCHEBI:1\tx\n" for s in subjects)
    path.write_text("# curie_map: {}\n" + HEADER + body, encoding="utf-8")
    return path


def test_an_escaped_subject_resolves_to_its_file(tmp_path, checker):
    """The exact shape of all 18 old false alarms."""
    dirs = _tree(tmp_path, ["(R)-lactate"])
    sssom = _sssom(tmp_path, ["MIM:~28R~29-lactate"])
    assert checker.unresolved_subjects(sssom, dirs) == {}


def test_a_subject_naming_no_file_is_reported(tmp_path, checker):
    dirs = _tree(tmp_path, ["Phenethylamine_Hydrochloride"])
    sssom = _sssom(tmp_path, ["MIM:2-phenylethylamine"])
    assert "MIM:2-phenylethylamine" in checker.unresolved_subjects(sssom, dirs)


def test_the_published_set_passes(checker):
    """Zero genuine mismatches today; the gate pins that."""
    assert checker.unresolved_subjects() == {}


def test_the_checker_is_now_a_gate(tmp_path, checker, monkeypatch):
    dirs = _tree(tmp_path, ["Glucose"])
    sssom = _sssom(tmp_path, ["MIM:Not_A_File"])
    monkeypatch.setattr(checker, "unresolved_subjects",
                        lambda: {"MIM:Not_A_File": "label"})
    assert checker.main() == 1


# --------------------------------------------------------------------------- #
# relabel: the mechanism #236 was filed about
# --------------------------------------------------------------------------- #

def test_relabelling_changes_the_label_and_not_the_subject(tmp_path, monkeypatch):
    relabel = importlib.import_module("relabel_mapped_record")
    sssom = tmp_path / "s.tsv"
    sssom.write_text(
        "# curie_map: {}\n" + HEADER +
        "MIM:Phenethylamine_Hydrochloride\tPhenethylamine Hydrochloride\t"
        "skos:exactMatch\tCHEBI:18397\t2-phenylethylamine\n",
        encoding="utf-8",
    )
    monkeypatch.setattr(relabel, "SSSOM", sssom)

    text, _ = relabel.plan_sssom_move("Phenethylamine Hydrochloride", "2-phenylethylamine")
    row = next(ln for ln in text.splitlines() if ln.startswith("MIM:"))
    subject, label = row.split("\t")[:2]

    assert label == "2-phenylethylamine"
    assert subject == "MIM:Phenethylamine_Hydrochloride", (
        "a relabel must not rewrite the subject -- the file stem does not move"
    )


# --------------------------------------------------------------------------- #
# merge: capture the loser's stem before it is given the winner's identifier
# --------------------------------------------------------------------------- #

def test_filenameindex_follows_the_identifier_first(tmp_path):
    """Why ordering matters in merge_salt_label_duplicates: after the loser is
    rewritten to carry the winner's identifier, the index answers with the
    WINNER's stem, and the rows dropped would be the winner's."""
    from export_individual_records import collect_existing_filenames

    mapped = tmp_path / "ingredients" / "mapped"
    mapped.mkdir(parents=True)
    (mapped / "Ca-pantothenate.yaml").write_text(
        "identifier: CHEBI:29032\npreferred_term: Ca-pantothenate\n", encoding="utf-8")
    (mapped / "Calcium_pantothenate.yaml").write_text(
        "identifier: CHEBI:31345\npreferred_term: Calcium pantothenate\n", encoding="utf-8")
    index = collect_existing_filenames(tmp_path / "ingredients")

    loser = {"identifier": "CHEBI:29032", "preferred_term": "Ca-pantothenate"}
    assert index.for_record(loser) == "Ca-pantothenate"
    loser["identifier"] = "CHEBI:31345"                     # the merge's rewrite
    assert index.for_record(loser) == "Calcium_pantothenate"  # the trap


def test_merge_captures_the_stem_before_the_rewrite():
    source = (ROOT / "scripts" / "merge_salt_label_duplicates.py").read_text(encoding="utf-8")
    capture = source.index("lose_stem = stems.for_record(lose)")
    rewrite = source.index('lose["identifier"] = win_id')
    assert capture < rewrite
    # The code form, not the phrase: the fix's own comment quotes the old spelling.
    assert 'drop_subjects.append(f"MIM:{lose_label' not in source


# --------------------------------------------------------------------------- #
# One home for the rule
# --------------------------------------------------------------------------- #

@pytest.mark.parametrize("module,function", [
    ("backfill_sssom_surface_forms", "mim_curie"),
])
def test_former_copies_of_the_escape_rule_delegate(module, function):
    mod = importlib.import_module(module)
    for stem in ("Glucose", "(R)-lactate", "α1-Acid Glycoprotein"):
        assert getattr(mod, function)(stem) == mim_curie_for_stem(stem)


def test_the_alias_map_delegates():
    mod = importlib.import_module("build_curie_alias_map")
    for stem in ("Glucose", "(R)-lactate"):
        assert mod.mim_curie(f"data/ingredients/mapped/{stem}.yaml") == mim_curie_for_stem(stem)


def test_no_second_copy_of_the_escape_regex():
    """Five copies existed; three independently rediscovered the raw-stem bug.

    Matches the implementing idiom, not the text: the validator's docstring still
    quotes the escape to explain why it cannot be decoded."""
    pattern = re.compile(r'lambda m: f"~\{ord\(')
    copies = [
        str(path.relative_to(ROOT))
        for directory in ("scripts", "src")
        for path in (ROOT / directory).rglob("*.py")
        if pattern.search(path.read_text(encoding="utf-8"))
    ]
    assert copies == ["src/mediaingredientmech/curie.py"], copies


# A subject spelled by hand is how #236 keeps coming back. These are the exact
# lines that build something other than a subject, or that are the rule's own
# home. Exempting lines rather than files means a second, genuinely wrong site
# added to one of these files is still caught (#691).
_NOT_A_SUBJECT = {
    ("src/mediaingredientmech/curie.py", 'return f"MIM:{safe}"'),           # the rule itself
    ("scripts/backfill_sssom_surface_forms.py", 'out[f"MIM:{path.stem}"] = path'),  # lenient alias
    ("scripts/restore_culturemech_grounding_evidence.py", 'f"MIM:{EVIDENCE_SOURCE}'),  # provenance
    ("scripts/reground_mapped_record.py", 'f"MIM:{subject_slug}.'),         # error message text
}


def test_no_writer_spells_a_subject_by_hand():
    offenders = []
    for directory in ("scripts", "src"):
        for path in (ROOT / directory).rglob("*.py"):
            rel = str(path.relative_to(ROOT))
            for number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
                if any(rel == f and marker in line for f, marker in _NOT_A_SUBJECT):
                    continue
                # Provenance strings ("MIM:<source>|MIM:curator=...") are not subjects.
                if "curator=" in line:
                    continue
                if re.search(r'''f["']MIM:\{''', line):
                    offenders.append(f"{rel}:{number}")
    assert not offenders, f"build these with mim_curie_for_stem(<file stem>): {offenders}"


def test_every_exemption_still_matches_a_real_line():
    """An exemption that no longer matches anything is dead, and hides nothing
    it claims to — but a stale one is how the list quietly grows."""
    for rel, marker in _NOT_A_SUBJECT:
        assert marker in (ROOT / rel).read_text(encoding="utf-8"), f"{rel}: {marker!r}"


# --------------------------------------------------------------------------- #
# merge: "nothing to drop" must be checked, not assumed (#690)
# --------------------------------------------------------------------------- #

def _merge_fixture(tmp_path, monkeypatch, *, published_label):
    """One loser/winner pair whose loser the stem index cannot find."""
    import yaml
    from export_individual_records import FilenameIndex

    merge = importlib.import_module("merge_salt_label_duplicates")
    collection = tmp_path / "mapped_ingredients.yaml"
    collection.write_text(yaml.safe_dump({"ingredients": [
        {"identifier": "CHEBI:1", "preferred_term": "Na-thing", "mapping_status": "MAPPED",
         "synonyms": [], "occurrence_statistics": {"total_occurrences": 1}},
        {"identifier": "CHEBI:2", "preferred_term": "Sodium thing", "mapping_status": "MAPPED",
         "synonyms": [], "occurrence_statistics": {"total_occurrences": 1}},
    ]}), encoding="utf-8")
    sssom = tmp_path / "s.tsv"
    body = "" if published_label is None else (
        f"MIM:Some_Drifted_Stem\t{published_label}\tskos:exactMatch\tCHEBI:1\tx\n")
    sssom.write_text("# curie_map: {}\n" + HEADER + body, encoding="utf-8")

    monkeypatch.setattr(merge, "COLLECTION", collection)
    monkeypatch.setattr(merge, "SSSOM", sssom)
    monkeypatch.setattr(merge, "MERGES", [("Na-thing", "CHEBI:1", "CHEBI:2", "Sodium thing")])
    # The miss this guards against: an unsynced collection the index cannot match.
    monkeypatch.setattr(merge, "collect_existing_filenames", lambda root: FilenameIndex())
    return merge


def test_merge_refuses_when_an_unmatched_loser_still_has_a_row(tmp_path, monkeypatch):
    """Skipping the drop would leave the row as an ORPHAN while reporting success."""
    merge = _merge_fixture(tmp_path, monkeypatch, published_label="Na-thing")
    with pytest.raises(SystemExit) as excinfo:
        merge.main([])
    assert "refusing to leave them as orphans" in str(excinfo.value)
    assert "MIM:Some_Drifted_Stem" in str(excinfo.value)


def test_merge_says_nothing_to_drop_only_when_that_is_true(tmp_path, monkeypatch, capsys):
    merge = _merge_fixture(tmp_path, monkeypatch, published_label=None)
    merge.main([])
    assert "no published row, so there is nothing to drop" in capsys.readouterr().out
