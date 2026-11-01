"""#1004 routes two reviewed salt labels without freezing future recipe counts."""

import csv
import hashlib
import importlib.util
import json
from pathlib import Path

import pytest

from mediaingredientmech.utils.culturemech_occurrences import (
    effective_occurrence_statistics,
    membership_counts,
    mim_identifier_for_occurrence,
)

ROOT = Path(__file__).resolve().parents[1]
FIXTURES = ROOT / "tests/fixtures"
OLD = "kgmicrobe.compound:carnitine_hydrochloride"
NEW = "NCIT:C216679"
NAMES = ("Carnitine Hydrochloride", "Carnitine (Dl) Hydrochloride")


@pytest.fixture
def producer():
    spec = importlib.util.spec_from_file_location("carnitine_membership_producer", ROOT / "scripts/build_culturemech_membership.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


@pytest.fixture
def frozen_occurrences():
    path = FIXTURES / "issue1004-routing-occurrences.tsv"
    assert hashlib.sha256(path.read_bytes()).hexdigest() == "e7fdbba52261189a462da2e4ada8f80f99c5b047dbb3d2627c29b545478f2c35"
    with path.open() as stream:
        return list(csv.DictReader(stream, delimiter="\t"))


def write_occurrences(path, rows):
    with path.open("w", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=list(rows[0]), delimiter="\t", lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)
    return path


@pytest.mark.parametrize("name", [*NAMES, " carnitine  HYDROCHLORIDE ", "CARNITINE (dl)  HYDROCHLORIDE"])
@pytest.mark.parametrize("upstream", [OLD, "cas:461-06-3", "CHEBI:91318", "CHEBI:48601", "", NEW])
def test_only_reviewed_source_labels_follow_exact_salt_identity(name, upstream):
    assert mim_identifier_for_occurrence({"preferred_term": name, "resolved_identifier": upstream}) == NEW


@pytest.mark.parametrize("name,upstream", [
    ("DL-carnitine", "CHEBI:17126"), ("L-Carnitine", "CHEBI:16347"),
    ("L-Carnitine hydrochloride", "CHEBI:91318"),
    ("carnitinamide chloride", "CHEBI:48601"),
    ("Carnitine", OLD), ("Carnitine (D) Hydrochloride", OLD),
    ("DL-Carnitine Hydrochloride", OLD), ("Carnitine Hydrochloride stock", OLD),
    ("", OLD),
])
def test_other_source_routes_keep_their_incoming_identity(name, upstream):
    # Preservation is not new scientific approval of a sibling's upstream ID.
    assert mim_identifier_for_occurrence({"preferred_term": name, "resolved_identifier": upstream}) == upstream


def test_native_historical_slice_routes_all_fourteen_pairs_and_free_controls(producer, frozen_occurrences, tmp_path):
    path = write_occurrences(tmp_path / "occurrences.tsv", frozen_occurrences)
    edges, unknown = producer.collect(path, {NEW, "CHEBI:17126"})
    expected = {(NEW if row["preferred_term"] in NAMES else row["resolved_identifier"], row["recipe_id"]): 1
                for row in frozen_occurrences}
    assert edges == expected and unknown == {}
    assert len([key for key in edges if key[0] == NEW]) == 14  # frozen historical application only
    assert len([key for key in edges if key[0] == "CHEBI:17126"]) == 2
    assert all(identity != OLD for identity, recipe in edges)


@pytest.mark.parametrize("growth,expected", [("new_recipe", (15, 15)), ("extra_listing", (14, 15))])
def test_native_future_membership_growth_is_counted_not_refused(producer, frozen_occurrences, tmp_path, monkeypatch, growth, expected):
    salt = next(row for row in frozen_occurrences if row["preferred_term"] == NAMES[0])
    extra = {**salt, "preferred_term": NAMES[1], "resolved_identifier": "cas:461-06-3"}
    if growth == "new_recipe":
        extra["recipe_id"] = "CultureMech:999999"
    path = write_occurrences(tmp_path / "occurrences.tsv", [*frozen_occurrences, extra])
    edges, unknown = producer.collect(path, {NEW, "CHEBI:17126"})
    assert unknown == {} and all(identity != OLD for identity, _ in edges)
    membership = tmp_path / "membership.tsv"
    monkeypatch.setattr(producer, "OUTPUT", membership)
    producer.write(edges, "synthetic future cohort based on frozen #1004 source excerpt")
    counts = membership_counts(membership)
    assert counts[NEW] == expected
    active = {"identifier": NEW, "mapping_status": "MAPPED", "occurrence_statistics": {"media_count": 14, "total_occurrences": 14}}
    tombstone = {"identifier": NEW, "mapping_status": "REJECTED", "occurrence_statistics": {"media_count": 0, "total_occurrences": 0}}
    assert effective_occurrence_statistics(active, counts) == expected
    assert effective_occurrence_statistics(tombstone, counts) == (0, 0)


def test_missing_active_salt_owner_stays_unknown_in_native_collect(producer, frozen_occurrences, tmp_path):
    path = write_occurrences(tmp_path / "occurrences.tsv", frozen_occurrences)
    edges, unknown = producer.collect(path, {OLD, "CHEBI:17126"})
    assert unknown == {NEW: 14}  # exact immutable source excerpt, not the live corpus
    assert all(identity == "CHEBI:17126" for identity, _ in edges)


def test_routing_fixture_manifest_matches_the_retained_source_bytes():
    manifest = json.loads((FIXTURES / "issue1004-routing-manifest.json").read_text())
    assert manifest["base_revision"] == "99fe4b44d78126d78041a69eeb366c52bedf0caa"
    for name, entry in manifest["fixtures"].items():
        assert hashlib.sha256((FIXTURES / name).read_bytes()).hexdigest() == entry["sha256"]
