"""Guards for the CultureMech recipe reference and its matcher (#447).

The matcher used to index 15,877 recipes by lower-cased name in a one-value
dict, then accept substring and two-token-overlap matches as recipe identity and
store the winner as a display string. Measured against the real corpus, that
would have written links into 208 records; 98% of its candidates are ambiguous,
and `PYG` alone matches 56 recipes.
"""

import importlib.util
import sys
from pathlib import Path

import pytest
import yaml

ROOT = Path(__file__).parent.parent
SCRIPT = ROOT / "scripts" / "cross_reference_culturemech.py"


@pytest.fixture(scope="module")
def mod():
    sys.path.insert(0, str(ROOT / "src"))
    spec = importlib.util.spec_from_file_location("cross_reference_culturemech", SCRIPT)
    m = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = m
    spec.loader.exec_module(m)
    return m


def _tree(tmp_path: Path, recipes: list[tuple[str, str]]) -> Path:
    """A minimal normalized_yaml tree of (id, name) recipes."""
    root = tmp_path / "CultureMech" / "data" / "normalized_yaml" / "bacterial"
    root.mkdir(parents=True)
    for i, (medium_id, name) in enumerate(recipes):
        (root / f"r{i}.yaml").write_text(
            yaml.safe_dump({"id": medium_id, "name": name, "ingredients": []}),
            encoding="utf-8")
    return root.parent  # .../normalized_yaml


# --- fail closed, do not fail open ----------------------------------------
def test_a_missing_source_raises_instead_of_indexing_nothing(mod, tmp_path):
    """It used to warn and return, leaving an empty index, so every lookup said
    "no match" -- indistinguishable from "the source could not be read". Its
    default path did not exist, so that was the normal case."""
    with pytest.raises(SystemExit, match="not found"):
        mod.CultureMechMatcher(tmp_path / "nope")


def test_a_source_with_no_stable_ids_raises(mod, tmp_path):
    """An index built from recipes carrying no `CultureMech:` id cannot produce
    a usable link, so reporting "no matches" from it would be a false negative."""
    root = tmp_path / "data" / "normalized_yaml"
    root.mkdir(parents=True)
    (root / "x.yaml").write_text(yaml.safe_dump({"name": "nameless"}), encoding="utf-8")

    with pytest.raises(SystemExit, match="no recipes carrying"):
        mod.CultureMechMatcher(root)


# --- names cannot identify a recipe ---------------------------------------
def test_duplicate_names_do_not_overwrite_one_another(mod, tmp_path):
    """A one-value name index dropped 3190 of 11093 named recipes, keeping
    whichever was indexed last. `defined_freshwater_medium_cocl2` names 29."""
    tree = _tree(tmp_path, [("CultureMech:000001", "shared_name"),
                            ("CultureMech:000002", "shared_name"),
                            ("CultureMech:000003", "unique_name")])

    matcher = mod.CultureMechMatcher(tree)

    assert len(matcher.media_by_id) == 3
    assert len(matcher.media_by_name["shared_name"]) == 2
    assert {r["id"] for r in matcher.media_by_name["shared_name"]} == {
        "CultureMech:000001", "CultureMech:000002"}


def test_an_exact_name_match_can_still_be_several_recipes(mod, tmp_path):
    """The most dangerous case: exact name agreement reads as certainty and is
    not. Both candidates must survive so the caller sees the ambiguity."""
    tree = _tree(tmp_path, [("CultureMech:000001", "pyg_medium"),
                            ("CultureMech:000002", "pyg_medium")])

    matches = mod.CultureMechMatcher(tree).find_medium_matches("pyg_medium")

    assert len(matches) == 2
    assert all(m["match_type"] == "exact_name" for m in matches)


def test_every_candidate_carries_a_stable_id(mod, tmp_path):
    """A display name cannot identify a recipe, so a candidate without an id is
    not actionable."""
    tree = _tree(tmp_path, [("CultureMech:000001", "pyg_medium_b"),
                            ("CultureMech:000002", "pyg_medium_c")])

    matches = mod.CultureMechMatcher(tree).find_medium_matches("pyg")

    assert matches
    assert all(m["medium_id"].startswith("CultureMech:") for m in matches)


# --- the tool proposes; a curator accepts ---------------------------------
def test_report_candidates_modifies_no_record(mod, tmp_path, monkeypatch):
    """The old path took matches[0] -- possibly a substring hit at 0.8 -- and
    wrote it as an accepted link. Acceptance needs a relationship and evidence,
    which is a judgement, so this writes a report and nothing else."""
    monkeypatch.chdir(tmp_path)
    record = {"identifier": "kgmicrobe.ingredient:pyg", "preferred_term": "PYG"}
    before = dict(record)

    class _Curator:
        records = [record]

    results = {0: [{"medium": {"id": "CultureMech:000001", "name": "pyg_medium_b",
                               "_source_path": "x.yaml"},
                    "medium_id": "CultureMech:000001",
                    "match_type": "contains", "confidence": 0.8}]}

    mod.report_candidates(_Curator(), results, confidence_threshold=0.8)

    assert record == before, "the matcher must not write into records"
    assert (tmp_path / "reports" / "culturemech_link_candidates.tsv").exists()


def test_ambiguous_candidates_are_marked_ambiguous(mod, tmp_path, monkeypatch):
    """`PYG` matches 56 recipes. The report has to say so, or a reader takes the
    first row -- which is exactly what the old code did."""
    monkeypatch.chdir(tmp_path)

    class _Curator:
        records = [{"identifier": "x", "preferred_term": "PYG"}]

    results = {0: [
        {"medium": {"id": f"CultureMech:00000{i}", "name": "pyg_medium", "_source_path": ""},
         "medium_id": f"CultureMech:00000{i}", "match_type": "contains", "confidence": 0.9}
        for i in (1, 2)]}

    rows = mod.report_candidates(_Curator(), results, confidence_threshold=0.8)

    text = (tmp_path / "reports" / "culturemech_link_candidates.tsv").read_text()
    assert rows == 2
    assert text.count("\tYES\t") == 2


# --- the corpus ------------------------------------------------------------
def test_no_record_carries_the_retired_name_only_field():
    """Checks the parsed KEY, not the raw text. Curation history legitimately
    names the retired field -- an event log records what was done at the time,
    and the migration event itself says `culturemech_medium_name=... ->
    culturemech_reference ...`. A substring test would fail on its own audit
    trail."""
    root = ROOT / "data" / "ingredients"
    stale = [p.name for p in root.rglob("*.yaml")
             if "culturemech_medium_name" in (
                 yaml.safe_load(p.read_text(encoding="utf-8")) or {})]

    assert not stale, f"name-only CultureMech links remain: {stale}"


@pytest.mark.parametrize(
    ("stem", "medium_id", "relationship"),
    [("BHI", "CultureMech:015492", "EXACT_FORMULATION"),
     ("GYPS", "CultureMech:002799", "SIMILAR_COMPOSITION")],
)
def test_the_two_links_are_typed_and_id_bearing(stem, medium_id, relationship):
    """GYPS is the one that matters: its name matches `gyps_medium` exactly and
    it is NOT the same formulation, so it must not be EXACT_FORMULATION."""
    record = yaml.safe_load(
        (ROOT / "data" / "ingredients" / "mapped" / f"{stem}.yaml").read_text(encoding="utf-8"))
    reference = record["culturemech_reference"]

    assert reference["medium_id"] == medium_id
    assert reference["relationship"] == relationship
    assert reference["evidence"].strip(), "a link may not rest on a name match alone"


def test_gyps_keeps_its_compositional_caveat():
    """The migration must not quietly strengthen the claim."""
    record = yaml.safe_load(
        (ROOT / "data/ingredients/mapped/GYPS.yaml").read_text(encoding="utf-8"))

    evidence = record["culturemech_reference"]["evidence"]

    assert "not identical" in evidence.lower()
    assert "mes" in evidence.lower() and "starch" in evidence.lower()


def test_the_whole_medium_filter_admits_records_that_actually_have_links(mod):
    """`--complex-media-only` filtered on NAMED_MEDIUM alone, and BOTH records
    carrying a CultureMech link are UNDEFINED_MIXTURE -- so it excluded 100% of
    its target population and returned a confident 0 candidates (#490). The enum
    mixes granularity with composition (#478), so a whole medium can legitimately
    be filed under either."""
    linked_types = {
        yaml.safe_load(
            (ROOT / "data/ingredients/mapped" / f"{stem}.yaml").read_text(encoding="utf-8")
        )["ingredient_type"]
        for stem in ("BHI", "GYPS")
    }

    assert linked_types <= mod.WHOLE_MEDIUM_TYPES, (
        f"records with links are typed {linked_types}, which the filter excludes")


def test_the_candidate_report_carries_provenance(mod, tmp_path, monkeypatch):
    """Ids are stable but the SET of recipes is not, so a candidate list read
    later cannot be checked against the tree that produced it (#491, cf. #486)."""
    monkeypatch.chdir(tmp_path)

    class _Curator:
        records = [{"identifier": "x", "preferred_term": "PYG"}]

    results = {0: [{"medium": {"id": "CultureMech:000001", "name": "p", "_source_path": ""},
                    "medium_id": "CultureMech:000001",
                    "match_type": "contains", "confidence": 0.9}]}

    mod.report_candidates(_Curator(), results, 0.8, provenance="culturemech_rev=abc123")

    first = (tmp_path / "reports/culturemech_link_candidates.tsv").read_text().splitlines()[0]
    assert first.startswith("# ") and "culturemech_rev=abc123" in first
