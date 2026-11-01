"""Mapping-change receipts are chain links, never approvals (#742, #743).

A receipt records a verified batch of mapping corrections (re-anchored parents,
regrades, re-groundings, merges, mints) as an explicit, auditable link after
the synonym-only refreshes. Two things must hold for the reviewed release to
stay honest: ``make_receipt.align`` must describe exactly what moved, and the
assembler's ``walk_mapping_changes`` must refuse any receipt that does not
chain -- by digest, by sequence, by approval, or by the row it claims to
change -- including a row corrected twice, whose second ``before`` is the
first ``after`` and not the baseline.
"""

from __future__ import annotations

import csv
import hashlib
import importlib.util
import io
import json
import sys
from pathlib import Path

import pytest

_REPO = Path(__file__).parent.parent
sys.path.insert(0, str(_REPO / "src"))


def _load(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


receipt_mod = _load(
    "make_receipt", _REPO / "reports/sssom_completion_20260921/mapping_changes/make_receipt.py"
)
assemble = _load("assemble_review", _REPO / "reports/sssom_completion_20260921/assemble_review.py")


def _row(subject, obj, predicate="skos:exactMatch", **extra):
    row = {"subject_id": subject, "predicate_id": predicate, "object_id": obj, "other": ""}
    row.update(extra)
    return row


BASE = [
    _row("MIM:A", "CHEBI:1"),
    _row("MIM:B", "CHEBI:2", "skos:broadMatch"),
    _row("MIM:B", "cas:1-1-1"),
    _row("MIM:C", "CHEBI:3"),
]


# --- make_receipt.align -----------------------------------------------------


def test_align_reports_changed_added_removed_and_position_map():
    after = [
        _row("MIM:A", "CHEBI:1"),
        _row("MIM:B", "CHEBI:20", "skos:broadMatch"),  # parent re-anchored in place
        _row("MIM:B", "cas:1-1-1"),
        # MIM:C removed (merged away)
        _row("MIM:D", "kgmicrobe.compound:d"),  # minted
    ]
    changes, position_map = receipt_mod.align(BASE, after)
    kinds = {(c["kind"], c["before_position"], c["after_position"]) for c in changes}
    assert kinds == {("changed", 2, 2), ("removed", 4, None), ("added", None, 4)}
    assert position_map == [1, 2, 3, None]
    changed = next(c for c in changes if c["kind"] == "changed")
    assert changed["before"]["object_id"] == "CHEBI:2" and changed["after"]["object_id"] == "CHEBI:20"


def test_align_refuses_two_rows_in_one_slot():
    doubled = BASE + [_row("MIM:A", "CHEBI:99", "skos:closeMatch")]
    with pytest.raises(ValueError, match="share a slot"):
        receipt_mod.align(doubled, doubled)


def test_slot_distinguishes_registry_rows_from_the_ontology_row():
    assert receipt_mod.slot(_row("MIM:X", "cas:1-1-1")) == ("MIM:X", "cas")
    assert receipt_mod.slot(_row("MIM:X", "kgmicrobe.ingredient:x")) == ("MIM:X", "kgmicrobe.ingredient")
    assert receipt_mod.slot(_row("MIM:X", "CHEBI:1")) == ("MIM:X", "ontology")
    assert receipt_mod.slot(_row("MIM:X", "mesh:D1")) == ("MIM:X", "ontology")


# --- assemble_review.walk_mapping_changes -----------------------------------


def _receipt(batch, sequence, before, after, changes, position_map, before_rows, after_rows, **overrides):
    receipt = {
        "schema_version": 1,
        "batch": batch,
        "sequence": sequence,
        "approval": "NONE: withheld pending mapping-specific review",
        "before_sha256": before if len(before) == 64 else hashlib.sha256(before.encode()).hexdigest(),
        "after_sha256": after if len(after) == 64 else hashlib.sha256(after.encode()).hexdigest(),
        "before_row_count": before_rows,
        "after_row_count": after_rows,
        "records": [],
        "changes": changes,
        "position_map": position_map,
    }
    receipt.update(overrides)
    return receipt


def _first_batch():
    """Re-anchor MIM:B's parent in place."""
    return _receipt(
        "b1", 1, "s0", "s1",
        [{"kind": "changed", "before_position": 2, "after_position": 2,
          "before": BASE[1], "after": _row("MIM:B", "CHEBI:20", "skos:broadMatch")}],
        [1, 2, 3, 4], 4, 4,
    )


def _second_batch():
    """Re-anchor MIM:B again, merge MIM:C away, mint MIM:D at the end."""
    return _receipt(
        "b2", 2, "s1", "s2",
        [{"kind": "changed", "before_position": 2, "after_position": 2,
          "before": _row("MIM:B", "CHEBI:20", "skos:broadMatch"),
          "after": _row("MIM:B", "CHEBI:200", "skos:broadMatch")},
         {"kind": "removed", "before_position": 4, "after_position": None, "before": BASE[3], "after": None},
         {"kind": "added", "before_position": None, "after_position": 4, "before": None,
          "after": _row("MIM:D", "kgmicrobe.compound:d")}],
        [1, 2, 3, None], 4, 4,
    )


def _walk(receipts, reviewed="s2", refreshed=None):
    return assemble.walk_mapping_changes(
        receipts, start_sha256=hashlib.sha256(b"s0").hexdigest(),
        reviewed_sha256=hashlib.sha256(reviewed.encode()).hexdigest(), baseline_rows=BASE,
        refreshed_rows=refreshed or {},
    )


def test_two_receipts_chain_through_the_first_correction():
    forward, last, state = _walk([_second_batch(), _first_batch()])  # any order in
    assert forward == [1, 2, 3, None]
    assert set(last) == {2, 4}
    assert last[2]["receipt"] == "b2" and last[2]["after"]["object_id"] == "CHEBI:200"
    assert last[4]["kind"] == "added" and last[4]["receipt"] == "b2"
    assert [r["subject_id"] for r in state] == ["MIM:A", "MIM:B", "MIM:B", "MIM:D"]
    assert state[1]["object_id"] == "CHEBI:200"


def test_second_receipt_must_chain_from_the_first_after_not_the_baseline():
    second = _second_batch()
    second["changes"][0]["before"] = BASE[1]  # claims the baseline row as its "before"
    with pytest.raises(ValueError, match="does not chain from the reviewed row"):
        _walk([_first_batch(), second])


def test_receipt_before_must_match_the_synonym_refreshed_row():
    refreshed = {2: dict(BASE[1], other="alias")}
    first = _first_batch()  # its "before" is the baseline row, not the refreshed one
    with pytest.raises(ValueError, match="does not chain from the reviewed row"):
        _walk([first], reviewed="s1", refreshed=refreshed)
    first["changes"][0]["before"] = refreshed[2]
    forward, last, state = _walk([first], reviewed="s1", refreshed=refreshed)
    assert last[2]["after"]["object_id"] == "CHEBI:20"


@pytest.mark.parametrize(
    "mutate, message",
    [
        (lambda r: r.update(sequence=2), "numbered 1..n"),
        (lambda r: r.update(approval="SUPPORTED: verified"), "approval-free"),
        (lambda r: r.update(before_sha256=hashlib.sha256(b"stale").hexdigest()), "does not chain from the previous link"),
        (lambda r: r.update(after_sha256=hashlib.sha256(b"other").hexdigest()), "does not produce the reviewed source"),
        (lambda r: r.update(position_map=[1, 2, 3]), "position map is incomplete"),
        (lambda r: r.update(position_map=[1, 2, 2, 4]), "not injective"),
        (lambda r: r["changes"].append({"kind": "added", "before_position": None, "after_position": 1,
                                        "before": None, "after": _row("MIM:Z", "CHEBI:9")}),
         "occupied position"),
        (lambda r: r["changes"].__setitem__(0, dict(r["changes"][0], kind="renamed")), "unknown change kind"),
    ],
)
def test_broken_single_receipt_is_refused(mutate, message):
    receipt = _first_batch()
    mutate(receipt)
    with pytest.raises(ValueError, match=message):
        _walk([receipt], reviewed="s1")


def test_removed_row_must_leave_the_position_map():
    second = _second_batch()
    second["position_map"] = [1, 2, 3, 4]  # keeps the row it claims to remove
    second["after_row_count"] = 5
    second["changes"][2]["after_position"] = 5
    with pytest.raises(ValueError, match="removes a row its position map keeps"):
        _walk([_first_batch(), second])


def test_no_receipts_is_the_identity_walk():
    forward, last, state = _walk([], reviewed="s0")
    assert forward == [1, 2, 3, 4] and last == {} and state == BASE


@pytest.mark.parametrize("synonym_corrected,mapping_changed", [(True, True), (True, False), (False, True), (False, False)])
@pytest.mark.parametrize("cohort", [None, "nonmapping_cohorts", "changed-owner-review"])
def test_assembled_evidence_preserves_every_applicable_correction_basis(
    tmp_path, monkeypatch, synonym_corrected, mapping_changed, cohort, prepare=None,
):
    """A later mapping receipt must not hide an earlier synonym correction (#1017).

    Exercise the complete assembler on an isolated one-row source, including its
    native receipt replay and owner hashes. Prior approval must not carry onto a
    changed row, and a correction that never happened must not be invented.
    """
    here = tmp_path / "reports/sssom_completion_20260921"
    owner = "data/ingredients/mapped/A.yaml"

    def write(path, text):
        target = tmp_path / path
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(text)

    def document(name, value):
        write(str((here / name).relative_to(tmp_path)), json.dumps(value) + "\n")

    def sssom(row):
        output = io.StringIO()
        output.write("# mapping_set_id: https://example.org/test\n# predicate_semantics: skos\n")
        writer = csv.DictWriter(output, fieldnames=list(row), delimiter="\t", lineterminator="\n")
        writer.writeheader()
        writer.writerow(row)
        return output.getvalue()

    write(owner, "identifier: CHEBI:1\npreferred_term: A\nmapping_status: MAPPED\n")
    owner_sha = assemble.digest(tmp_path / owner)
    baseline = _row("MIM:A", "CHEBI:1", subject_label="A", object_label="A", other="alias|rejected", comment="")
    corrected = dict(baseline, other="alias") if synonym_corrected else dict(baseline)
    current = dict(corrected, comment="Restored source explanation") if mapping_changed else dict(corrected)
    write(assemble.SOURCE, sssom(current))
    current_sha = assemble.digest(tmp_path / assemble.SOURCE)
    parent_sha = receipt_mod.digest(sssom(corrected).encode())
    baseline_sha = receipt_mod.digest(sssom(baseline).encode())
    document("baseline-mapping-review.json", {
        "schema_version": 1, "source_sha256": baseline_sha,
        "rows": [baseline], "record_inputs": {owner: owner_sha},
        "decisions": [{"source_position": 1, "resolution_status": "APPROVED",
                       "review_reason": "Prior exact-payload review", "review_evidence": "prior-review.md"}],
    })
    document("trait_synonyms/decisions.json", {"records": []})
    document("parent_names/decisions.json", {"records": []})
    document("trait-synonym-refresh.json", {"schema_version": 1, "before_sha256": baseline_sha, "after_sha256": baseline_sha,
                                            "row_count": 1, "changed_rows": 0, "changes": [], "records": []})
    document("parent-name-refresh.json", {
        "schema_version": 1, "before_sha256": baseline_sha, "after_sha256": parent_sha,
        "row_count": 1, "changed_rows": int(synonym_corrected), "records": [],
        "changes": [{"source_position": 1, "before": baseline, "after": corrected,
                     "removed_tokens": ["rejected"]}] if synonym_corrected else [],
    })
    if mapping_changed:
        document("mapping_changes/provenance-repair.json", _receipt(
            "provenance-repair", 1, parent_sha, current_sha,
            [{"kind": "changed", "before_position": 1, "after_position": 1,
              "before": corrected, "after": current}], [1], 1, 1,
            changed_rows=1, added_rows=0, removed_rows=0,
        ))
    for name in ("concern_cohorts", "nonmapping_cohorts", "changed-owner-review"):
        document(f"mapping_review/{name}.json", {"rows": []})
    if cohort:
        entry = {"disposition": "SUPPORTED", "reason": "Exact historical mapping review",
                 "owner_record_sha256": owner_sha, "mapping": baseline}
        if cohort == "nonmapping_cohorts":
            entry.update(owner_record=owner, source_position=1, source_sssom_sha256=baseline_sha)
        else:
            entry.update(owner=owner, decision={"source_position": "1", "source_record_sha256": baseline_sha})
        document(f"mapping_review/{cohort}.json", {"rows": [entry]})
    document("mapping_review/issue-intersections.json", {
        "issue_669_all_baseline_intersections": [],
        "issue_232_conflicting_label_intersections": [], "findings": [],
    })
    for name in ("adversarial-findings", "synonym-adversarial-findings"):
        document(f"mapping_review/{name}.json", {"findings": []})
    document("mapping_review/kgmicrobe-followup.json", {"decisions": []})
    write("reports/semantic_review_20260921/records.tsv", f"source_record\treview_report\n{owner}\tprior-review.md\n")
    for path in (
        "prior-review.md", "MAPPING_SEMANTICS.md",
        "src/mediaingredientmech/export/reviewed_sssom.py",
        "src/mediaingredientmech/review_claims.py", "src/mediaingredientmech/synonym_policy.py",
        "src/mediaingredientmech/record_refresh.py", "scripts/validate_reviewed_sssom_schema.py",
        "src/mediaingredientmech/validation/mapping_change_receipts.py",
        "reports/semantic_review_20260921/resolution/historical-review-evidence.json",
    ):
        write(path, "fixture context\n")
    monkeypatch.setattr(assemble, "ROOT", tmp_path)
    monkeypatch.setattr(assemble, "HERE", here)
    monkeypatch.setattr(assemble, "REVIEWED_SOURCE", current_sha)

    if prepare is not None:
        prepare(here)
    products = assemble.assemble()
    entry = json.loads(products["mapping-evidence.json"])["entries"]["1"]
    basis = entry["basis"]
    assert basis.get("synonym_correction") == ("parent-name-refresh.json" if synonym_corrected else None)
    assert basis.get("mapping_change") == ("provenance-repair" if mapping_changed else None)
    assert entry["disposition"] == ("WITHHOLD" if synonym_corrected or mapping_changed else "SUPPORTED")
    assert entry["row_sha256"] == assemble.row_sha256(current)
    assert entry["owner_record_sha256"] == owner_sha
    if mapping_changed and not cohort:
        assert entry["review_reason"].startswith("Mapping corrected by receipt provenance-repair:")
    if cohort and (mapping_changed or synonym_corrected):
        assert basis["superseded_scoped_review"]["reviewed_sha256"] == owner_sha
        assert basis["superseded_scoped_review"]["current_sha256"] == owner_sha
        assert "superseded" in entry["review_reason"]


@pytest.mark.parametrize("tamper", ["owner", "row", "source", "hash", "position"])
def test_scoped_withdrawal_refuses_unbound_archived_claim(tamper):
    owner = "data/ingredients/mapped/A.yaml"
    old, current = _row("MIM:A", "CHEBI:1"), _row("MIM:A", "CHEBI:2")
    digest = hashlib.sha256(b"owner").hexdigest()
    source = hashlib.sha256(b"baseline").hexdigest()
    entry = {"owner_record": owner, "owner_record_sha256": digest, "mapping": old,
             "source_position": 1, "source_sssom_sha256": source}
    proof = {"baseline_rows": [old], "state": [current], "forward": [1],
             "owner_chains": {}, "receipt_inputs": {"receipt.json": hashlib.sha256(b"receipt").hexdigest()}}
    if tamper == "owner":
        entry["owner_record"] = "data/ingredients/mapped/Other.yaml"
    elif tamper == "row":
        entry["mapping"] = dict(old, other="unreviewed")
    elif tamper == "source":
        entry["source_sssom_sha256"] = hashlib.sha256(b"other source").hexdigest()
    elif tamper == "hash":
        entry["owner_record_sha256"] = hashlib.sha256(b"different owner").hexdigest()
    else:
        proof["forward"] = [None]
    with pytest.raises(ValueError, match="archived row and owner|byte-chain"):
        assemble.withdraw_stale_cohort(entry, current, owner, digest, proof,
                                      {"source_sha256": source}, current_position=1)


@pytest.mark.parametrize("cohort", ["nonmapping_cohorts", "changed-owner-review"])
@pytest.mark.parametrize("reverse", [False, True])
@pytest.mark.parametrize("conflicting", [False, True])
def test_assembler_rejects_duplicate_cohort_positions_before_projection(tmp_path, monkeypatch, cohort, reverse, conflicting):
    def duplicate(here):
        path = here / f"mapping_review/{cohort}.json"
        document = json.loads(path.read_text())
        original = document["rows"][0]
        repeated = json.loads(json.dumps(original))
        if conflicting:
            repeated.update(disposition="WITHHOLD", reason="Conflicting prior scientific decision")
            repeated["mapping"]["other"] = "Unbound competing mapping payload"
        document["rows"] = [repeated, original] if not reverse else [original, repeated]
        path.write_text(json.dumps(document))

    with pytest.raises(ValueError, match=f"Duplicate source position in {cohort}.json"):
        test_assembled_evidence_preserves_every_applicable_correction_basis(
            tmp_path, monkeypatch, False, False, cohort, prepare=duplicate,
        )
