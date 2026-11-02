"""WC stock identity scope, occurrence routing and guarded source publication (#751)."""

import importlib.util
import json
import shutil
import subprocess
from contextlib import contextmanager
from pathlib import Path

import pytest
import yaml

from mediaingredientmech.sssom_grading import predicate_for
from mediaingredientmech.utils.culturemech_occurrences import (
    effective_occurrence_statistics,
    mim_identifier_for_occurrence,
)

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("curate_wc_stock", ROOT / "scripts/curate_wc_stock_751.py")
mod = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(mod)
STAMP = "2030-01-02T00:00:00+00:00"


@pytest.fixture
def before():
    return {mod.OWNER: mod.frozen()}


@pytest.fixture(scope="session")
def anchors():
    result = {}
    for path in mod.ANCHORS:
        data = subprocess.check_output(
            ["git", "cat-file", "blob", f"{mod.META['base_revision']}:{path}"], cwd=ROOT,
        )
        assert mod.guarded.digest(data) == mod.META["protected_anchors"][str(path)]
        result[path] = data
    return result


@pytest.fixture
def native_runtime():
    return pytest.importorskip("kg_microbe_write", reason="Real native transaction required")


@pytest.fixture
def case(tmp_path, before, anchors):
    root = tmp_path.resolve() / "mim"
    root.mkdir()
    shutil.copytree(ROOT / mod.REPORT, root / mod.REPORT)
    for path, data in (before | anchors).items():
        (root / path).parent.mkdir(parents=True, exist_ok=True)
        (root / path).write_bytes(data)
    log = tmp_path.resolve() / "receipts/wc-source.json"
    log.parent.mkdir()
    return root, log


def assert_owner_unchanged(root):
    assert (root / mod.OWNER).read_bytes() == mod.frozen()


def test_only_identity_quality_evidence_and_one_event_change(before):
    untouched = dict(before)
    proposed = mod.propose_sources(before, timestamp=STAMP)
    old, new = yaml.safe_load(before[mod.OWNER]), yaml.safe_load(proposed[mod.OWNER])
    assert before == untouched
    assert set(proposed) == {mod.OWNER}
    assert new["curation_history"][:-1] == old["curation_history"]
    assert new["ontology_mapping"]["evidence"][:-1] == old["ontology_mapping"]["evidence"]
    assert new["identifier"] == "kgmicrobe.ingredient:wc_trace_elements_solution"
    assert new["ontology_mapping"]["ontology_id"] == "MICRO:0000455"
    assert new["ontology_mapping"]["mapping_quality"] == "NARROW_MATCH"
    assert predicate_for(new["ontology_mapping"]["mapping_quality"]) == "skos:broadMatch"
    event = new["curation_history"].pop()
    evidence = new["ontology_mapping"]["evidence"].pop()
    new["identifier"] = old["identifier"]
    new["ontology_mapping"]["mapping_quality"] = old["ontology_mapping"]["mapping_quality"]
    assert new == old
    assert event["action"] == "REKEYED_WC_STOCK_IDENTITY"
    assert event["curator"] == "Codex" and event["llm_assisted"] is True
    assert event["previous_status"] == event["new_status"] == "MAPPED"
    assert mod.META["owner_sha256"] in event["changes"]
    assert mod.MANIFEST_SHA in evidence["notes"]
    assert mod.verify_complete(proposed) == STAMP


def test_evidence_distinguishes_specific_recipe_from_generic_class():
    evidence = json.loads((ROOT / mod.META["primary_evidence"]).read_bytes())
    assert evidence["ontology"]["curie"] == "MICRO:0000455"
    assert evidence["ontology"]["label"] == "trace elements solution"
    assert evidence["ontology"]["whole_ontology_search"]["fields_examined"] > 0
    assert evidence["ontology"]["whole_ontology_search"]["wc_hits"] == []
    stock = evidence["utex_tables"]["utex-wc-trace.html"]
    assert len(stock[1:]) == 8
    for name in ("utex-wc.html", "utex-wc-plus.html"):
        assert [row for row in evidence["utex_tables"][name] if row[1] == mod.NAME] == [
            ["8", mod.NAME, "1 mL/L", "", ""]
        ]
    assert mod.META["approval"].startswith("NONE")


@pytest.mark.parametrize("label", ["WC Trace Elements Solution", "  wc  trace elements solution "])
def test_only_normalized_exact_wc_label_routes_to_new_identity(label):
    assert mim_identifier_for_occurrence({
        "preferred_term": label, "resolved_identifier": "MICRO:0000455",
    }) == "kgmicrobe.ingredient:wc_trace_elements_solution"


@pytest.mark.parametrize("label, expected", [
    ("Algal Trace Elements Solution", "kgmicrobe.ingredient:algal_trace_elements_solution"),
    ("trace elements solution", "MICRO:0000455"),
    ("WC Trace Elements Solution 2x", "MICRO:0000455"),
    ("WC", "MICRO:0000455"),
])
def test_algal_generic_and_unreviewed_wc_labels_remain_distinct(label, expected):
    assert mim_identifier_for_occurrence({
        "preferred_term": label, "resolved_identifier": "MICRO:0000455",
    }) == expected


def test_no_membership_is_invented_and_stored_counts_survive(before):
    new = yaml.safe_load(mod.propose_sources(before, timestamp=STAMP)[mod.OWNER])
    assert new["occurrence_statistics"] == {"total_occurrences": 2, "media_count": 2}
    assert effective_occurrence_statistics(new, {}) == (2, 2)
    assert new["nutritional_roles"] == yaml.safe_load(before[mod.OWNER])["nutritional_roles"]
    assert "components" not in new and "chemical_properties" not in new


@pytest.mark.parametrize("field", ["identifier", "synonyms", "curation_history", "nutritional_roles"])
def test_changed_preimage_is_refused(before, field):
    document = yaml.safe_load(before[mod.OWNER])
    document.pop(field)
    before[mod.OWNER] = yaml.safe_dump(document).encode()
    with pytest.raises(ValueError, match="preimage"):
        mod.propose_sources(before, timestamp=STAMP)


@pytest.mark.parametrize("stamp", ["2000-01-01T00:00:00+00:00", "2030-01-02T00:00:00", "2030-01-02T00:00:00+01:00"])
def test_event_requires_utc_after_evidence(before, stamp):
    with pytest.raises(ValueError, match="Timestamp"):
        mod.propose_sources(before, timestamp=stamp)


@pytest.mark.parametrize("field", ["identifier", "occurrence_statistics", "nutritional_roles"])
def test_changed_completed_owner_cannot_claim_idempotence(before, field):
    proposed = mod.propose_sources(before, timestamp=STAMP)
    document = yaml.safe_load(proposed[mod.OWNER])
    document.pop(field)
    proposed[mod.OWNER] = yaml.safe_dump(document).encode()
    with pytest.raises(ValueError, match="Partial or changed"):
        mod.verify_complete(proposed)


def test_native_dry_run_apply_receipt_and_idempotence(native_runtime, case, anchors):
    root, log = case
    dry = mod.apply_sources(root, log)
    assert dry["applied"] is False and not log.exists()
    assert_owner_unchanged(root)
    applied = mod.apply_sources(root, log, apply=True)
    assert applied["transaction"]["changed"] == [str(root / mod.OWNER)]
    assert applied["transaction"]["created"] == []
    assert applied["records"][0]["before_yaml_sha256"] == mod.META["owner_sha256"]
    assert mod.backups(log)[mod.OWNER].read_bytes() == mod.frozen()
    assert all((root / p).read_bytes() == data for p, data in anchors.items())
    _, receipt = mod.source_receipt(root, log)
    assert receipt["approval"].startswith("NONE")
    assert mod.apply_sources(root, log, apply=True)["changed"] is False


@pytest.mark.parametrize("kind", ["primary", "manifest", "canonical", "unified", "evidence-symlink"])
def test_changed_input_prevents_any_owner_write(case, kind):
    root, log = case
    path = root / {
        "primary": mod.META["primary_evidence"], "manifest": mod.MANIFEST,
        "canonical": "mappings/ingredient_mappings.sssom.tsv",
        "unified": "UNIFIED_INGREDIENT_MAPPING.tsv",
        "evidence-symlink": mod.META["primary_evidence"],
    }[kind]
    if kind == "evidence-symlink":
        original = path.with_suffix(".original")
        path.rename(original)
        path.symlink_to(original)
    else:
        path.write_bytes(path.read_bytes() + b"\n")
    with pytest.raises(ValueError):
        mod.apply_sources(root, log, apply=True)
    assert not log.exists()
    assert_owner_unchanged(root)


@pytest.mark.parametrize("kind", ["identifier", "casefold-identifier", "ontology"])
def test_nested_ignored_destination_collision_is_refused(case, kind):
    root, log = case
    (root / ".gitignore").write_text("data/ingredients/mapped/ignored/\n")
    hidden = root / "data/ingredients/mapped/ignored/nested/other.yaml"
    hidden.parent.mkdir(parents=True)
    document = {"identifier": mod.NEW, "mapping_status": "REJECTED"}
    if kind == "casefold-identifier":
        document["identifier"] = mod.NEW.upper()
    elif kind == "ontology":
        document = {"identifier": "UNMAPPED_9999", "mapping_status": "MAPPED",
                    "ontology_mapping": {"ontology_id": mod.NEW}}
    hidden.write_text(yaml.safe_dump(document))
    with pytest.raises(ValueError, match="identity already held"):
        mod.apply_sources(root, log, apply=True)
    assert not log.exists()
    assert_owner_unchanged(root)


def test_missing_exact_source_override_is_refused(case, monkeypatch):
    root, log = case
    monkeypatch.delitem(mod.SOURCE_LABEL_IDENTIFIER_OVERRIDES, mod._source_label_key(mod.NAME))
    with pytest.raises(ValueError, match="override"):
        mod.apply_sources(root, log, apply=True)
    assert_owner_unchanged(root)


@pytest.mark.parametrize("kind", ["receipt", "backup", "receipt-symlink"])
def test_receipt_outputs_reserved_before_owner_write(native_runtime, case, kind):
    root, log = case
    path = mod.backups(log)[mod.OWNER] if kind == "backup" else log
    if kind == "receipt-symlink":
        original = log.parent / "foreign.json"
        original.write_bytes(b"preserve")
        path.symlink_to(original)
    else:
        path.write_bytes(b"preserve")
    with pytest.raises((ValueError, FileExistsError)):
        mod.apply_sources(root, log, apply=True)
    assert path.read_bytes() == b"preserve"
    assert_owner_unchanged(root)


def test_destination_added_during_reservation_is_refused(native_runtime, case, monkeypatch):
    root, log = case
    reserve = mod.guarded.reserve_receipt_outputs

    @contextmanager
    def race(*args, **kwargs):
        with reserve(*args, **kwargs) as handles:
            path = root / "data/ingredients/mapped/late.yaml"
            path.write_text(yaml.safe_dump({"identifier": mod.NEW}))
            yield handles

    monkeypatch.setattr(mod.guarded, "reserve_receipt_outputs", race)
    with pytest.raises(native_runtime.ValidationFailed, match="path set"):
        mod.apply_sources(root, log, apply=True)
    assert_owner_unchanged(root)
    assert json.loads(log.read_text())["state"] == "failed"


def test_completed_receipt_cannot_claim_approval(native_runtime, case):
    root, log = case
    mod.apply_sources(root, log, apply=True)
    receipt = json.loads(log.read_text())
    receipt["approval"] = "APPROVED"
    log.write_text(json.dumps(receipt))
    with pytest.raises(ValueError, match="exact execution"):
        mod.source_receipt(root, log)
