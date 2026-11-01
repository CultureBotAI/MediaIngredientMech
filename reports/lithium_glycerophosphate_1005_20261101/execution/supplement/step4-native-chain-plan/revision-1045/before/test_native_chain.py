"""Small offline refusal controls; no production chain execution or copied corpus."""
import copy
import csv
import importlib.util
import io
from pathlib import Path

import pytest

spec = importlib.util.spec_from_file_location("step4_chain", Path(__file__).with_name("native_chain.py"))
c = importlib.util.module_from_spec(spec)
spec.loader.exec_module(c)


def render(rows):
    out = io.StringIO(newline="")
    date = max(row["mapping_date"] for row in rows)
    out.write(f'# mapping_set_version: "{date}"\n# mapping_date: "{date}"\n# predicate_semantics: "skos"\n')
    writer = csv.DictWriter(out, fieldnames=list(rows[0]), delimiter="\t", lineterminator="\n")
    writer.writeheader()
    writer.writerows(rows)
    return out.getvalue().encode()


@pytest.fixture
def canonical():
    rows = c.rows(c.base(c.CANONICAL), sssom=True)
    target = [row for row in rows if row["subject_id"] == c.SUBJECT]
    control = copy.deepcopy(next(row for row in rows if row["subject_id"] != c.SUBJECT))
    before = target + [control]
    after = copy.deepcopy([target[0], target[2], control])
    for row in after[:2]:
        row["source"] += "|MIM:explicit-offline-contract-fixture"
        row["mapping_date"] = "2026-11-02"
    after[0]["other"] = ""
    after[1]["comment"] = f"Registry/identity row preserving {c.IDENTITY} alongside parent CHEBI:15978."
    return before, after


def test_bounded_three_to_two_change_and_header_date(canonical):
    old, new = canonical
    assert tuple(map(len, c.canonical_scope(render(old), render(new)))) == (4, 3)


@pytest.mark.parametrize("fault", ["unrelated", "wrong_parent", "restore_cas", "alias", "lost_stamp", "lost_390", "lost_source", "wrong_comment", "cas_display"])
def test_canonical_refuses_out_of_scope_or_provenance_loss(canonical, fault):
    old, new = canonical
    if fault == "unrelated": new[-1]["confidence"] = "0.01"
    if fault == "wrong_parent": new[0]["object_id"] = "CHEBI:1"
    if fault == "restore_cas": new.insert(1, copy.deepcopy(old[1]))
    if fault == "alias": new[0]["other"] = "Glycerol 3-phosphate"
    if fault == "lost_stamp": new[0]["validation_method"] = ""
    if fault == "lost_390": new[0]["comment"] = ""
    if fault == "lost_source": new[0]["source"] = "MIM:fixture-only"
    if fault == "wrong_comment": new[1]["comment"] = "exact free acid"
    if fault == "cas_display": new[1]["other"] = ""
    with pytest.raises(ValueError): c.canonical_scope(render(old), render(new))


def test_plain_hash_names_survive_and_sssom_only_skips_prelude():
    raw = b'ingredient_name\toccurrence_count\n#N2\t3\n#Ar\t1\n'
    assert [r["ingredient_name"] for r in c.rows(raw)] == ["#N2", "#Ar"]
    assert c.rows(b'# metadata\n' + raw, sssom=True) == c.rows(raw)


def mapping_decisions(rows):
    return [{"source_position": i, "evidence_key": str(i), "row_sha256": "payload-" + row["object_id"], "owner_record": c.OWNER if row["subject_id"] == c.SUBJECT else "data/ingredients/mapped/control.yaml", "disposition": "WITHHOLD" if row["subject_id"] == c.SUBJECT else "SUPPORTED", "review_reason": "bounded fixture", "review_evidence": "frozen evidence"} for i, row in enumerate(rows, 1)]


def test_unchanged_mapping_relocation_is_allowed(canonical):
    old, new = canonical
    assert c.compare_mapping_decisions(mapping_decisions(old), mapping_decisions(new), old, new) == 1


@pytest.mark.parametrize("field", ["row_sha256", "owner_record", "disposition", "review_reason", "review_evidence"])
def test_mapping_semantics_are_not_location_equivalence(canonical, field):
    old, new = canonical
    decisions = mapping_decisions(new)
    decisions[-1][field] = "unexpected"
    with pytest.raises(ValueError): c.compare_mapping_decisions(mapping_decisions(old), decisions, old, new)


def test_target_mapping_cannot_be_approved(canonical):
    old, new = canonical
    decisions = mapping_decisions(new)
    decisions[0]["disposition"] = "SUPPORTED"
    with pytest.raises(ValueError): c.compare_mapping_decisions(mapping_decisions(old), decisions, old, new)


def assertions(rows, *, current):
    owner_hash, canonical_hash = ("new-owner", "new-canonical") if current else ("old-owner", "old-canonical")
    result = [{"assertion_id": owner_hash + "-role", "source_record": c.OWNER, "source_record_sha256": owner_hash, "assertion_type": "nutritional_roles", "source_position": "1", "assertion_sha256": "unchanged-role", "resolution_status": "OPEN", "review_reason": "provisional", "review_evidence": ""}, {"assertion_id": "control-role", "source_record": "control.yaml", "source_record_sha256": "control-owner", "assertion_type": "nutritional_roles", "source_position": "1", "assertion_sha256": "control-payload", "resolution_status": "APPROVED", "review_reason": "existing", "review_evidence": "original"}]
    for i, row in enumerate(rows, 1):
        result.append({"assertion_id": canonical_hash + str(i), "source_record": c.CANONICAL, "source_record_sha256": canonical_hash, "assertion_type": "mapping", "source_position": str(i), "assertion_sha256": "payload-" + row["object_id"], "resolution_status": "OPEN" if row["subject_id"] == c.SUBJECT else "APPROVED", "review_reason": "existing", "review_evidence": "original"})
    return result


def test_semantic_location_changes_preserve_full_payload_and_holds(canonical):
    old, new = canonical
    c.compare_assertions(assertions(old, current=False), assertions(new, current=True), old, new, "new-owner", "new-canonical")


@pytest.mark.parametrize("fault", ["role_payload", "role_approve", "role_missing", "unrelated_role", "unrelated_mapping_payload", "unrelated_mapping_reason", "unrelated_mapping_approval", "target_mapping_approve", "stale_canonical"])
def test_semantic_changes_are_not_silently_carried(canonical, fault):
    old, new = canonical
    before, after = assertions(old, current=False), assertions(new, current=True)
    if fault == "role_payload": after[0]["assertion_sha256"] = "changed"
    if fault == "role_approve": after[0]["resolution_status"] = "APPROVED"
    if fault == "role_missing": after.pop(0)
    if fault == "unrelated_role": after[1]["review_reason"] = "changed"
    if fault == "unrelated_mapping_payload": after[-1]["assertion_sha256"] = "changed"
    if fault == "unrelated_mapping_reason": after[-1]["review_reason"] = "changed"
    if fault == "unrelated_mapping_approval": after[-1]["resolution_status"] = "OPEN"
    if fault == "target_mapping_approve": after[2]["resolution_status"] = "APPROVED"
    if fault == "stale_canonical": after[-1]["source_record_sha256"] = "stale"
    with pytest.raises(ValueError): c.compare_assertions(before, after, old, new, "new-owner", "new-canonical")


def findings():
    return [{"finding_id": k, "source_record": c.OWNER, "current_record_sha256": "old-owner", "resolution_status": "OPEN", "reason": "mixed identity and provisional role", "resolution_reason": "unresolved", "evidence": "original"} for k in ["mixed", "role"]] + [{"finding_id": "control", "source_record": "control.yaml", "current_record_sha256": "control-owner", "resolution_status": "OPEN", "reason": "unrelated", "resolution_reason": "unresolved", "evidence": "original"}]


def test_mixed_and_role_findings_remain_open_under_new_owner_hash():
    before, after = findings(), findings()
    for row in after[:2]: row["current_record_sha256"] = "new-owner"
    c.compare_findings(before, after, "new-owner")


@pytest.mark.parametrize("fault", ["retire", "resolve", "reason", "unrelated", "stale_owner"])
def test_findings_cannot_be_blanket_retired_or_rewritten(fault):
    before, after = findings(), findings()
    for row in after[:2]: row["current_record_sha256"] = "new-owner"
    if fault == "retire": after.pop(0)
    if fault == "resolve": after[0]["resolution_status"] = "RESOLVED"
    if fault == "reason": after[0]["reason"] = "all science approved"
    if fault == "unrelated": after[-1]["resolution_reason"] = "changed"
    if fault == "stale_owner": after[1]["current_record_sha256"] = "old-owner"
    with pytest.raises(ValueError): c.compare_findings(before, after, "new-owner")
