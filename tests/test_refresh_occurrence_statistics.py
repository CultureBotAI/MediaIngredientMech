"""Guards for the occurrence-statistics refresh (#449).

The values this replaces were wrong in a way that looked authoritative: 39
records read exactly 50 because CultureMech's pre-#337 aggregator truncated its
occurrence list to 50 examples and the retired importer (#453) counted the
truncated list. `ZnCl2` claimed 1579 occurrences across "50" media.
"""

import csv
import importlib.util
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).parent.parent
SCRIPT = ROOT / "scripts" / "refresh_occurrence_statistics.py"


@pytest.fixture(scope="module")
def mod():
    spec = importlib.util.spec_from_file_location("refresh_occurrence_statistics", SCRIPT)
    m = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = m
    spec.loader.exec_module(m)
    return m


def _table(tmp_path: Path, rows: list[tuple[str, str]]) -> Path:
    path = tmp_path / "occurrences.tsv"
    with path.open("w", newline="", encoding="utf-8") as fh:
        w = csv.writer(fh, delimiter="\t", lineterminator="\n")
        w.writerow(["recipe_id", "resolved_identifier", "ingredient_json"])
        for recipe_id, identifier in rows:
            w.writerow([recipe_id, identifier, "{}"])
    return path


def test_media_count_is_distinct_recipes_not_rows(mod, tmp_path):
    """The whole defect: counting occurrence rows rather than distinct media.
    An ingredient listed twice in one recipe is in ONE medium."""
    path = _table(tmp_path, [
        ("CultureMech:1", "CHEBI:1"),
        ("CultureMech:1", "CHEBI:1"),   # same medium, second listing
        ("CultureMech:2", "CHEBI:1"),
    ])

    fresh, total_rows, total_recipes = mod.read_occurrences(path)

    assert (total_rows, total_recipes) == (3, 2)
    assert fresh["CHEBI:1"] == (2, 3), "expected (2 distinct media, 3 rows)"


def test_no_cap_at_fifty(mod, tmp_path):
    """The pre-#337 aggregator truncated to 50 examples; nothing here may."""
    path = _table(tmp_path, [(f"CultureMech:{i}", "CHEBI:1") for i in range(120)])

    assert mod.read_occurrences(path)[0]["CHEBI:1"] == (120, 120)


def test_a_pre_337_table_is_refused_rather_than_misread(mod, tmp_path):
    """Without recipe_id there is no stable key, and silently falling back to
    names would reintroduce the identity problem this fix exists to avoid."""
    path = tmp_path / "old.tsv"
    path.write_text("preferred_term\tmedium_name\nNaCl\tR2A\n", encoding="utf-8")

    with pytest.raises(SystemExit, match="resolved_identifier|recipe_id"):
        mod.read_occurrences(path)


def test_unmatched_records_are_left_alone_not_zeroed(mod):
    """Absence from a scan can mean the ingredient is gone OR that upstream
    resolution changed. Those are different facts; zeroing asserts the first."""
    records = [{"identifier": "CHEBI:absent", "preferred_term": "X",
                "occurrence_statistics": {"media_count": 7, "total_occurrences": 9}}]

    changes, stranded, _ = mod.plan(records, {"CHEBI:other": (1, 1)})

    assert changes == []
    assert [r["identifier"] for r, _ in stranded] == ["CHEBI:absent"]
    assert records[0]["occurrence_statistics"]["media_count"] == 7


def test_records_already_correct_are_not_rewritten(mod):
    """Keeps re-runs from churning the corpus and its curation history."""
    records = [{"identifier": "CHEBI:1", "preferred_term": "X",
                "occurrence_statistics": {"media_count": 3, "total_occurrences": 4}}]

    changes, _, _ = mod.plan(records, {"CHEBI:1": (3, 4)})

    assert changes == []


def test_shared_identifiers_are_detected(mod):
    """`MgSO4 x 7 H2O` and `MgSO4·H2O` share one identifier, so both take the
    same count -- the #225/#334 duplicate cohort. Must be reported, because it
    means media_count cannot be summed across records."""
    records = [{"identifier": "CHEBI:1"}, {"identifier": "CHEBI:1"},
               {"identifier": "CHEBI:2"}, {"identifier": ""}, {"identifier": ""}]

    assert mod.shared_identifiers(records) == {"CHEBI:1"}


def test_apply_never_lets_media_count_exceed_total_occurrences(mod):
    """`audit_occurrence_stats` calls that combination impossible, and updating
    media_count alone would have produced it on 821 records."""
    records = [{"identifier": "CHEBI:1", "preferred_term": "X",
                "occurrence_statistics": {"media_count": 50, "total_occurrences": 1579}}]
    changes, _, _ = mod.plan(records, {"CHEBI:1": (1839, 1839)})

    mod.apply(changes, "test-provenance")

    stats = records[0]["occurrence_statistics"]
    assert stats["media_count"] <= stats["total_occurrences"]
    assert (stats["media_count"], stats["total_occurrences"]) == (1839, 1839)


def test_apply_records_a_curation_event(mod):
    records = [{"identifier": "CHEBI:1", "preferred_term": "X",
                "occurrence_statistics": {"media_count": 50, "total_occurrences": 100}}]
    changes, _, _ = mod.plan(records, {"CHEBI:1": (7, 9)})

    mod.apply(changes, "test-provenance")

    history = records[0].get("curation_history") or []
    assert history, "a data correction must leave an audit trail"
    assert "50/100 -> 7/9" in history[-1]["changes"]


def test_the_corpus_no_longer_carries_the_truncation_signature():
    """End state, not mechanism: 39 records read exactly 50 before this. A
    natural distribution has no reason to pile up on a slice bound."""
    import yaml

    data = yaml.safe_load(
        (ROOT / "data/curated/mapped_ingredients.yaml").read_text(encoding="utf-8"))
    counts = [(r.get("occurrence_statistics") or {}).get("media_count")
              for r in data["ingredients"]]
    at_fifty = sum(1 for c in counts if c == 50)
    neighbours = sum(1 for c in counts if isinstance(c, int) and 45 <= c <= 55 and c != 50)

    assert at_fifty <= max(3, neighbours), (
        f"{at_fifty} records at exactly 50 against {neighbours} in 45-55: "
        "the truncation signature is back")


def test_rejected_records_are_skipped_not_resurrected(mod):
    """A REJECTED record was merged and its counts moved to the representative.
    Refreshing one puts back a number curation deliberately zeroed --
    `audit_occurrence_stats` calls that combination an inconsistency, and it is
    a small version of the overwrite-curation failure that retired the importer
    in #453. This actually happened: the first run resurrected 48 of them."""
    records = [{"identifier": "CHEBI:1", "preferred_term": "merged away",
                "mapping_status": "REJECTED",
                "occurrence_statistics": {"media_count": 0, "total_occurrences": 0}}]

    changes, _, rejected = mod.plan(records, {"CHEBI:1": (4665, 4665)})

    assert changes == []
    assert len(rejected) == 1
    assert records[0]["occurrence_statistics"]["total_occurrences"] == 0
