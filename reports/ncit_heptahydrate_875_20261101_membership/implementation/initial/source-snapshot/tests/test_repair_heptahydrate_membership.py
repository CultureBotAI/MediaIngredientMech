"""#1031 restores an existing membership cohort without changing its source."""

import csv
import importlib.util
import io
import json
from contextlib import contextmanager
from pathlib import Path

import pytest
import yaml

from mediaingredientmech.utils.culturemech_occurrences import (
    effective_occurrence_statistics,
    membership_counts,
    mim_identifier_for_occurrence,
)

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("membership_repair", ROOT / "scripts/repair_heptahydrate_membership.py")
writer = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(writer)
guarded = writer.guarded


def table(rows):
    return ("# source=frozen-test-snapshot unchanged=true\n"
            "mim_identifier\trecipe_id\toccurrences\n"
            + "".join("\t".join(row) + "\n" for row in sorted(rows))).encode()


@pytest.fixture
def case(tmp_path, monkeypatch):
    rows = [(guarded.OLD, recipe, "1") for recipe in writer.RECIPES]
    rows += [("CHEBI:34683", "CultureMech:100001", "2"),
             ("kgmicrobe.compound:z", "CultureMech:100002", "3")]
    before = table(rows)
    after = table([(guarded.NEW if identity == guarded.OLD else identity, recipe, count)
                   for identity, recipe, count in rows])
    anchors = {path: (ROOT / path).read_bytes() if path == guarded.OWNER else b"frozen anchor\n"
               for path in writer.ANCHORS}
    monkeypatch.setattr(writer, "ANCHORS", {p: guarded.digest(b) for p, b in anchors.items()})
    monkeypatch.setattr(writer, "BEFORE_SHA", guarded.digest(before))
    monkeypatch.setattr(writer, "AFTER_SHA", guarded.digest(after))
    for path, content in {**anchors, writer.MEMBERSHIP: before}.items():
        target = tmp_path / path
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(content)
    return tmp_path, tmp_path / "evidence/repair.json", before, after, anchors


def native_available():
    return pytest.importorskip("kg_microbe_write")


def test_native_repair_preserves_cohort_header_other_rows_and_inputs(case):
    native_available()
    root, log, before, after, anchors = case
    result = writer.repair(root, log, apply=True)
    assert (root / writer.MEMBERSHIP).read_bytes() == after
    assert {p: (root / p).read_bytes() for p in anchors} == anchors
    assert before.splitlines()[0] == after.splitlines()[0]
    assert log.with_suffix(".before-membership.tsv").read_bytes() == before
    assert result["approval"].startswith("NONE") and result["curator"] == "Codex"
    assert result["llm_assisted"] is True
    assert len(result["memberships"]) == 32
    journal = json.loads(Path(result["transaction"]["journal"]).read_text())
    assert journal["changed"] == [str(root / writer.MEMBERSHIP)]
    assert journal["previous"][str(root / writer.MEMBERSHIP)].encode() == before
    receipt = log.read_bytes()
    assert writer.repair(root, log, apply=True)["changed"] is False
    assert log.read_bytes() == receipt


def test_native_dry_run_has_no_outputs(case):
    native_available()
    root, log, before, _, _ = case
    result = writer.repair(root, log)
    assert result["changed"] and not result["applied"]
    assert (root / writer.MEMBERSHIP).read_bytes() == before
    assert not log.parent.exists()


@pytest.mark.parametrize("path", [guarded.OWNER, guarded.LEDGER, guarded.SSSOM])
def test_identity_anchor_drift_refuses_before_writing(case, path):
    root, log, before, _, _ = case
    (root / path).write_bytes((root / path).read_bytes() + b"\n")
    with pytest.raises(ValueError, match="anchor changed"):
        writer.repair(root, log, apply=True)
    assert (root / writer.MEMBERSHIP).read_bytes() == before
    assert not log.exists()


def test_ignored_destination_owner_collision_refuses(case):
    root, log, before, _, _ = case
    other = root / "data/ingredients/mapped/.ignored-backup/owner.yaml"
    other.parent.mkdir()
    other.write_text(f"identifier: {guarded.NEW}\nmapping_status: MAPPED\n")
    with pytest.raises(ValueError, match="Destination identity already held"):
        writer.repair(root, log, apply=True)
    assert (root / writer.MEMBERSHIP).read_bytes() == before


def test_wrong_membership_preimage_refuses(case):
    root, log, before, _, _ = case
    (root / writer.MEMBERSHIP).write_bytes(before + b"\n")
    with pytest.raises(ValueError, match="frozen preimage"):
        writer.repair(root, log, apply=True)
    assert not log.exists()


@pytest.mark.parametrize("change", ["partial", "destination", "missing", "extra", "count", "duplicate", "unrelated"])
def test_structural_or_scope_drift_refuses_even_if_preimage_is_rehashed(case, monkeypatch, change):
    _, _, before, _, _ = case
    rows = list(csv.DictReader(io.StringIO(before.decode().split("\n", 1)[1]), delimiter="\t"))
    selected = next(r for r in rows if r["mim_identifier"] == guarded.OLD)
    if change == "partial":
        selected["mim_identifier"] = guarded.NEW
    elif change == "destination":
        rows.append(selected | {"mim_identifier": guarded.NEW})
    elif change == "missing":
        rows.remove(selected)
    elif change == "extra":
        rows.append(selected | {"recipe_id": "CultureMech:999999"})
    elif change == "count":
        selected["occurrences"] = "2"
    elif change == "duplicate":
        rows.append(dict(selected))
    else:
        rows[0]["occurrences"] = "99"
    changed = table([tuple(row.values()) for row in rows])
    monkeypatch.setattr(writer, "BEFORE_SHA", guarded.digest(changed))
    with pytest.raises(ValueError):
        writer.repaired_membership(changed)


@pytest.mark.parametrize("suffix", [None, ".before-membership.tsv"])
@pytest.mark.parametrize("symlink", [False, True])
def test_reserved_output_collision_preserves_competitor_and_membership(case, suffix, symlink):
    native_available()
    root, log, before, _, _ = case
    occupied = log if suffix is None else log.with_suffix(suffix)
    occupied.parent.mkdir()
    victim = root / "competitor"
    victim.write_bytes(b"competitor")
    if symlink:
        occupied.symlink_to(victim)
    else:
        occupied.write_bytes(b"competitor")
    with pytest.raises(FileExistsError):
        writer.repair(root, log, apply=True)
    assert occupied.read_bytes() == victim.read_bytes() == b"competitor"
    assert (root / writer.MEMBERSHIP).read_bytes() == before


@pytest.mark.parametrize("suffix", [None, ".before-membership.tsv"])
@pytest.mark.parametrize("symlink", [False, True])
@pytest.mark.parametrize("timing", ["reserved", "prepared", "after_commit", "completion"])
def test_native_reservation_races_preserve_competitors_and_recovery(case, monkeypatch, suffix, symlink, timing):
    native = native_available()
    root, log, before, after, _ = case
    replaced = log if suffix is None else log.with_suffix(suffix)
    victim = root / "competitor"
    victim.write_bytes(b"competitor")

    def replace():
        replaced.unlink()
        if symlink:
            replaced.symlink_to(victim)
        else:
            replaced.write_bytes(b"competitor")

    original = guarded.reserve_receipt_outputs

    class Proxy:
        def __init__(self, handle):
            self.handle = handle

        def __getattr__(self, name):
            return getattr(self.handle, name)

        def write(self, text):
            result = self.handle.write(text)
            state = json.loads(text).get("state")
            if ((timing == "prepared" and state == "prepared")
                    or (timing == "completion" and state == "complete")):
                replace()
            return result

    @contextmanager
    def reserve(*args, **kwargs):
        with original(*args, **kwargs) as handles:
            if timing == "reserved":
                replace()
            yield (Proxy(handles[0]), *handles[1:])

    class Racing(native.ValidatedWriteTransaction):
        def commit(self, *, apply=False):
            result = super().commit(apply=apply)
            if apply and timing == "after_commit":
                replace()
            return result

    monkeypatch.setattr(guarded, "reserve_receipt_outputs", reserve)
    monkeypatch.setattr(guarded, "new_transaction", lambda root, validator, journal: Racing(
        root, validator=validator, journal_dir=journal))
    with pytest.raises(ValueError, match="Reserved evidence output was replaced or removed"):
        writer.repair(root, log, apply=True)
    applied = timing in {"after_commit", "completion"}
    assert (root / writer.MEMBERSHIP).read_bytes() == (after if applied else before)
    assert replaced.is_symlink() is symlink
    assert replaced.read_bytes() == victim.read_bytes() == b"competitor"
    if suffix:
        receipt = json.loads(log.read_text())
        assert receipt["state"] == "failed" and receipt["applied"] is applied
    journals = list((log.parent / f"{log.stem}-journal").glob("write-*.json"))
    assert len(journals) == int(applied)
    if applied:
        assert json.loads(journals[0].read_text())["previous"][str(root / writer.MEMBERSHIP)].encode() == before


def test_input_changes_after_reservation_refuse_native_commit(case, monkeypatch):
    native_available()
    root, log, before, _, _ = case
    original = guarded.reserve_receipt_outputs

    @contextmanager
    def reserve(*args, **kwargs):
        with original(*args, **kwargs) as handles:
            (root / guarded.OWNER).write_bytes(b"concurrent owner change")
            yield handles

    monkeypatch.setattr(guarded, "reserve_receipt_outputs", reserve)
    with pytest.raises(ValueError, match="frozen input changed"):
        writer.repair(root, log, apply=True)
    assert (root / writer.MEMBERSHIP).read_bytes() == before


@pytest.mark.parametrize("label", ["Na2HPO4 x 7 H2O", "Na2HPO4.7H2O", "Na2HPO4•7H2O", "  na2hpo4   x 7 h2o  "])
@pytest.mark.parametrize("old", [guarded.OLD, guarded.PARENT, "", guarded.NEW])
def test_accepted_heptahydrate_labels_route_to_current_identity(label, old):
    assert mim_identifier_for_occurrence({"preferred_term": label, "resolved_identifier": old}) == guarded.NEW


@pytest.mark.parametrize("label", ["Na2HPO4", "Sodium phosphate dibasic", "Na2HPO4 x H2O",
                                    "Na2HPO4 x 2 H2O", "Na2HPO4 x 3 H2O", "Na2HPO4 x 6 H2O",
                                    "Na2HPO4 x 12 H2O", "Na2HPO4-NaH2PO4 buffer", "Unrelated"])
def test_sibling_plain_parent_and_unrelated_labels_keep_their_routing(label):
    assert mim_identifier_for_occurrence({"preferred_term": label, "resolved_identifier": guarded.PARENT}) == guarded.PARENT


def test_native_collector_recovers_exact_archived_32_and_effective_counts(case):
    root, _, before, after, _ = case
    spec = importlib.util.spec_from_file_location("membership_builder_1031", ROOT / "scripts/build_culturemech_membership.py")
    producer = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(producer)
    source = ROOT / "reports/sssom_scientific_curation_20261101/audit875/current-culturemech-occurrences.tsv"
    edges, unknown = producer.collect(source, {guarded.NEW, guarded.PARENT})
    selected = {recipe: count for (identity, recipe), count in edges.items() if identity == guarded.NEW}
    assert selected == dict.fromkeys(writer.RECIPES, 1)
    assert guarded.OLD not in unknown
    owner = yaml.safe_load((root / guarded.OWNER).read_bytes())
    assert effective_occurrence_statistics(owner, membership_counts(root / writer.MEMBERSHIP)) == (26, 26)
    (root / writer.MEMBERSHIP).write_bytes(after)
    assert effective_occurrence_statistics(owner, membership_counts(root / writer.MEMBERSHIP)) == (32, 32)
    assert owner["occurrence_statistics"] == {"total_occurrences": 26, "media_count": 26}
    assert sum(count for (identity, _), count in edges.items() if identity == guarded.PARENT) == 1
    assert before != after


def test_committed_memberships_use_current_owner_and_preserve_exact_cohort():
    """Pending until the root applies the reviewed repair; never rewrite data here."""
    content = (ROOT / writer.MEMBERSHIP).read_bytes()
    rows = list(csv.DictReader((line for line in content.decode().splitlines() if not line.startswith("#")), delimiter="\t"))
    assert not any(row["mim_identifier"] == guarded.OLD for row in rows)
    assert {row["recipe_id"]: row["occurrences"] for row in rows if row["mim_identifier"] == guarded.NEW} == dict.fromkeys(writer.RECIPES, "1")
