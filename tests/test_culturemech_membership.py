"""Guards for the CultureMech membership edge list (#449).

MIM stored two aggregate counts and nothing else, so "which recipes use this
ingredient?" was unanswerable from this repo -- and when the counts were wrong
(39 records pinned at exactly 50 by a truncated example list) there was nothing
to check them against. These pin the artifact that closes that.
"""

import csv
import importlib.util
import subprocess
import sys
from collections import defaultdict
from pathlib import Path

import pytest
import yaml

ROOT = Path(__file__).parent.parent
SCRIPT = ROOT / "scripts" / "build_culturemech_membership.py"
ARTIFACT = ROOT / "mappings" / "culturemech_recipe_membership.tsv"


@pytest.fixture(scope="module")
def mod():
    spec = importlib.util.spec_from_file_location("build_culturemech_membership", SCRIPT)
    m = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = m
    spec.loader.exec_module(m)
    return m


@pytest.fixture(scope="module")
def edges() -> list[dict]:
    with ARTIFACT.open(newline="", encoding="utf-8") as fh:
        rows = [line for line in fh if not line.startswith("#")]
    return list(csv.DictReader(rows, delimiter="\t"))


@pytest.fixture(scope="module")
def records() -> list[dict]:
    data = yaml.safe_load(
        (ROOT / "data/curated/mapped_ingredients.yaml").read_text(encoding="utf-8"))
    return data["ingredients"]


def test_the_counts_are_reproducible_from_the_edges(edges, records):
    """The documented definition the issue asks for: counting a record's edges
    reproduces `media_count`, and summing their `occurrences` reproduces
    `total_occurrences`.

    REJECTED records are excluded because curation deliberately zeroes them and
    transfers their counts to the representative they were merged into, while
    CultureMech still resolves that identifier -- so the two disagree by design
    (48 of them do).
    """
    by_id = defaultdict(lambda: [0, 0])
    for row in edges:
        by_id[row["mim_identifier"]][0] += 1
        by_id[row["mim_identifier"]][1] += int(row["occurrences"])

    disagree = []
    for record in records:
        identifier = str(record.get("identifier") or "")
        if identifier not in by_id or record.get("mapping_status") == "REJECTED":
            continue
        stats = record.get("occurrence_statistics") or {}
        media, occurrences = by_id[identifier]
        if (stats.get("media_count"), stats.get("total_occurrences")) != (media, occurrences):
            disagree.append((record.get("preferred_term"), stats, media, occurrences))

    assert not disagree, f"{len(disagree)} active record(s) disagree: {disagree[:3]}"


def test_an_ingredient_in_more_than_fifty_recipes_is_represented(edges):
    """The explicit acceptance criterion, and the defect's signature: the old
    importer capped at 50 because CultureMech truncated its example list, so
    anything above 50 was exactly what could not be represented."""
    counts = defaultdict(int)
    for row in edges:
        counts[row["mim_identifier"]] += 1

    over = {k: v for k, v in counts.items() if v > 50}

    assert over, "no ingredient has more than 50 memberships"
    assert max(over.values()) > 1000, (
        f"largest membership is {max(over.values())}; the corpus has one at 7695")


def test_edges_are_unique_so_a_rebuild_cannot_duplicate_them(edges):
    """`(mim_identifier, recipe_id)` is the key. A repeated listing inside one
    recipe belongs in `occurrences`, not in a second row."""
    keys = [(r["mim_identifier"], r["recipe_id"]) for r in edges]

    assert len(keys) == len(set(keys)), f"{len(keys) - len(set(keys))} duplicate edge(s)"


def test_the_artifact_is_sorted_so_rebuilds_diff_cleanly(edges):
    """Dict order would make every rebuild look like a full rewrite, which is
    how a real change gets lost in the noise."""
    keys = [(r["mim_identifier"], r["recipe_id"]) for r in edges]

    assert keys == sorted(keys)


def test_no_display_names_are_stored_on_either_side(edges):
    """Names are not identity. CultureMech has 2291 shared names, one naming 29
    recipes, and 4784 recipes with none -- #447 removed name-keyed linking, and
    an edge table is the easiest place to reintroduce it."""
    assert set(edges[0]) == {"mim_identifier", "recipe_id", "occurrences"}


def test_both_sides_are_stable_ids(edges):
    sample = edges[:2000]

    assert all(r["recipe_id"].startswith("CultureMech:") for r in sample)
    assert all(":" in r["mim_identifier"] for r in sample)


def test_the_artifact_carries_provenance():
    """Recipe ids are stable but the SET of recipes is not, so an edge list read
    later cannot be checked against the tree that produced it (#486)."""
    first = ARTIFACT.read_text(encoding="utf-8").splitlines()[0]

    assert first.startswith("# ")
    assert "culturemech_rev=" in first and "edges=" in first


def test_an_identifier_mim_does_not_hold_is_reported_not_published(mod, tmp_path):
    """CultureMech resolves 28 identifiers MIM has no record for. Publishing
    them would put edges in the artifact that no record can answer to; dropping
    them silently would hide a real gap between the two repos."""
    source = tmp_path / "occ.tsv"
    with source.open("w", newline="", encoding="utf-8") as fh:
        w = csv.writer(fh, delimiter="\t", lineterminator="\n")
        w.writerow(["recipe_id", "resolved_identifier"])
        w.writerow(["CultureMech:000001", "CHEBI:known"])
        w.writerow(["CultureMech:000002", "CHEBI:absent"])

    collected, unknown = mod.collect(source, {"CHEBI:known"})

    assert list(collected) == [("CHEBI:known", "CultureMech:000001")]
    assert unknown == ["CHEBI:absent"]


def test_repeated_listings_in_one_recipe_become_a_count_not_a_row(mod, tmp_path):
    source = tmp_path / "occ.tsv"
    with source.open("w", newline="", encoding="utf-8") as fh:
        w = csv.writer(fh, delimiter="\t", lineterminator="\n")
        w.writerow(["recipe_id", "resolved_identifier"])
        w.writerow(["CultureMech:000001", "CHEBI:x"])
        w.writerow(["CultureMech:000001", "CHEBI:x"])

    collected, _ = mod.collect(source, {"CHEBI:x"})

    assert collected == {("CHEBI:x", "CultureMech:000001"): 2}


def test_a_pre_337_table_is_refused(mod, tmp_path):
    source = tmp_path / "old.tsv"
    source.write_text("preferred_term\tmedium_name\nNaCl\tR2A\n", encoding="utf-8")

    with pytest.raises(SystemExit, match="resolved_identifier|recipe_id"):
        mod.collect(source, set())


def test_the_artifact_is_tracked_not_a_local_leftover():
    """It is a published artifact, not a report -- the point is that a consumer
    can read it without a CultureMech checkout."""
    tracked = subprocess.run(
        ["git", "-C", str(ROOT), "ls-files", "--error-unmatch",
         str(ARTIFACT.relative_to(ROOT))],
        capture_output=True, text=True)

    assert tracked.returncode == 0, f"{ARTIFACT.name} is not tracked by git"
