"""#1005 preserves uncertain supplied chemistry and guarded publication evidence."""

import csv
import importlib.util
import io
import json
import os
import shutil
from contextlib import contextmanager
from pathlib import Path

import pytest
import yaml

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("lithium_writer", ROOT / "scripts/curate_lithium_glycerophosphate.py")
writer = importlib.util.module_from_spec(spec)
spec.loader.exec_module(writer)
STAMP = "2026-11-01T11:00:00+00:00"


def tsv(fields, rows):
    output = io.StringIO(newline="")
    stream = csv.DictWriter(output, fieldnames=fields, delimiter="\t", lineterminator="\n")
    stream.writeheader()
    stream.writerows(rows)
    return output.getvalue().encode()


@pytest.fixture
def native_runtime():
    """Only transaction tests need the separately installed Claw publisher."""
    pytest.importorskip("kg_microbe_write", reason="Native Claw transaction integration is optional")


@pytest.fixture
def case(tmp_path, monkeypatch):
    root = tmp_path.resolve()
    before = {writer.OWNER: writer.frozen_owner(),
              writer.SSSOM: (writer.FIXTURES / "target.sssom.tsv").read_bytes(),
              writer.BASELINE: (writer.FIXTURES / "baseline.tsv").read_bytes()}
    for path, data in before.items():
        target = root / path
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(data)
        monkeypatch.setitem(writer.BEFORE, path, writer.digest(data))
    evidence = root / writer.EVIDENCE
    shutil.copytree(ROOT / writer.EVIDENCE, evidence)
    return root, evidence, root / "receipts/source.json", before


def apply(case):
    root, evidence, log, _ = case
    return writer.apply_sources(root, evidence, log, apply=True)


def candidate(case):
    root, _, _, before = case
    return candidate_bytes(before, (root / writer.OWNER).read_bytes())


def candidate_bytes(before, current):
    record = yaml.safe_load(current)
    fields, old = writer.table(before[writer.SSSOM])
    rows = []
    for obj in ("CHEBI:15978", "kgmicrobe.compound:sn-glycerol_3-phosphate_lithium_salt"):
        row = dict(next(r for r in old if r["object_id"] == obj))
        row.update(source="|".join(["MIM:" + e["source"] for e in record["ontology_mapping"]["evidence"]]
                                   + ["MIM:curator=Codex", "kgm:native_ontology:chebi"]),
                   mapping_date=record["curation_history"][-1]["timestamp"][:10],
                   other="" if obj == "CHEBI:15978" else "CAS:17989-41-2",
                   comment="" if obj == "CHEBI:15978" else "Registry/identity row preserving kgmicrobe.compound:sn-glycerol_3-phosphate_lithium_salt alongside parent CHEBI:15978.")
        rows.append(row)
    return tsv(fields, rows)


def promotion(case):
    root, _, source, _ = case
    apply(case)
    path = root / "candidate.tsv"
    path.write_bytes(candidate(case))
    return {"root": root, "candidate": path, "source_log": source,
            "log": source.with_name("promotion.json"), "candidate_sha256": writer.digest(path.read_bytes())}


def test_proposal_exact_approved_fields_and_all_preserved_science(case):
    _, _, _, before = case
    old = yaml.safe_load(before[writer.OWNER])
    result = writer.propose_record(before[writer.OWNER], timestamp=STAMP)
    new = yaml.safe_load(result)
    assert new["identifier"] == "kgmicrobe.compound:sn-glycerol_3-phosphate_lithium_salt"
    assert new["supplied_form"] == [{"name": "sn-Glycerol 3-phosphate lithium salt", "cas_rn": "17989-41-2",
                                   "form": "lithium salt", "supplier": "Sigma-Aldrich", "catalog_number": "94124",
                                   "notes": "free-acid CAS/FW; Li stoichiometry unstated"}]
    assert "chemical_properties" not in new
    assert new["curation_history"][:-1] == old["curation_history"]
    event = new["curation_history"][-1]
    assert event["timestamp"] == STAMP and event["curator"] == "Codex"
    assert event["llm_assisted"] is True and event["llm_model"] == "gpt-6"
    assert json.dumps(old["chemical_properties"], sort_keys=True) in event["changes"]
    assert "No scientific/release approval" in event["changes"]
    for key in set(old) - {"identifier", "chemical_properties", "ontology_mapping", "curation_history"}:
        assert new[key] == old[key]
    assert new["ontology_mapping"]["evidence"][:-1] == old["ontology_mapping"]["evidence"]
    for key in set(old["ontology_mapping"]) - {"evidence"}:
        assert new["ontology_mapping"][key] == old["ontology_mapping"][key]
    writer.complete_owner(result)


def test_evidence_is_primary_bytes_with_failed_supplier_capture_classified(case):
    _, evidence, _, _ = case
    inputs = writer.evidence_inputs(evidence)
    failed = json.loads(inputs[evidence / "sigma-94124-http.html.receipt.json"])
    assert failed["successful_http"] is False and inputs[evidence / "sigma-94124-http.html"] == b""
    supplier = json.loads(inputs[evidence / "sigma-94124-web-response.json"])
    assert "not raw HTTP HTML" in supplier["capture_kind"]
    assert "free acid basis" in supplier["response"]
    assert b"sn-Glycerol 3-phosphate lithium salt,17989-41-2,Sigma,94124,172.07" in inputs[evidence / "compounds_to_cas.csv"]


def test_pure_promotion_preserves_comment_stamps_and_exact_row_scope(case):
    _, _, _, before = case
    current = writer.propose_record(before[writer.OWNER], timestamp=STAMP)
    actual = writer.promoted_sssom(before[writer.SSSOM], candidate_bytes(before, current), current)
    _, prior = writer.table(before[writer.SSSOM])
    _, rows = writer.table(actual)
    target = {r["object_id"]: r for r in rows if r["subject_id"] == writer.SUBJECT}
    assert set(target) == {writer.PARENT, writer.NEW}
    assert len(rows) == len(prior) - 1
    for obj, row in target.items():
        old = next(r for r in prior if r["subject_id"] == writer.SUBJECT and r["object_id"] == obj)
        assert row["validation_method"] == old["validation_method"]
        assert set(old["source"].split("|")) <= set(row["source"].split("|"))
        assert row["mapping_date"] == STAMP[:10]
    assert target[writer.PARENT]["comment"] == next(
        r["comment"] for r in prior if r["subject_id"] == writer.SUBJECT and r["object_id"] == writer.PARENT)
    assert target[writer.PARENT]["comment"].startswith("[#390")
    assert (target[writer.PARENT]["predicate_id"], target[writer.PARENT]["other"]) == ("skos:broadMatch", "")
    assert (target[writer.NEW]["predicate_id"], target[writer.NEW]["other"]) == ("skos:exactMatch", "CAS:17989-41-2")
    unchanged = [line for line in before[writer.SSSOM].splitlines(keepends=True)
                 if not line.startswith((b"#", (writer.SUBJECT + "\t").encode()))]
    assert unchanged == [line for line in actual.splitlines(keepends=True)
                         if not line.startswith((b"#", (writer.SUBJECT + "\t").encode()))]
    removed = f"{writer.SUBJECT}\tGlycerol 3-phosphate\tMIM:Glycerol_3-phosphate\tUNREVIEWED\n".encode()
    baseline = writer.retired_baseline(before[writer.BASELINE])
    assert baseline == before[writer.BASELINE].replace(removed, b"")
    writer.completed_anchors(before[writer.SSSOM], before[writer.BASELINE], actual, baseline, current)


@pytest.mark.parametrize("field,value", [("source", "MIM:invented"), ("validation_method", ""),
                                        ("other", "Glycerol 3-phosphate"), ("predicate_id", "skos:exactMatch"),
                                        ("object_id", "cas:17989-41-2"), ("mapping_date", "2025-01-01"),
                                        ("comment", "unreviewed replacement"), ("object_label", "lithium salt")])
def test_pure_candidate_claim_substitution_refused(case, field, value):
    _, _, _, before = case
    current = writer.propose_record(before[writer.OWNER], timestamp=STAMP)
    fields, rows = writer.table(candidate_bytes(before, current))
    rows[0][field] = value
    with pytest.raises(ValueError, match="candidate rows|bounded native row"):
        writer.promoted_sssom(before[writer.SSSOM], tsv(fields, rows), current)


@pytest.mark.parametrize("shape", ["missing_parent", "duplicate_identity", "retained_false_cas"])
def test_pure_candidate_target_shape_is_exact(case, shape):
    _, _, _, before = case
    current = writer.propose_record(before[writer.OWNER], timestamp=STAMP)
    fields, rows = writer.table(candidate_bytes(before, current))
    if shape == "missing_parent":
        rows.pop(0)
    elif shape == "duplicate_identity":
        rows.append(dict(rows[1]))
    else:
        _, prior = writer.table(before[writer.SSSOM])
        rows.append(next(r for r in prior if r["object_id"] == writer.OLD))
    with pytest.raises(ValueError, match="exactly two native candidate rows"):
        writer.promoted_sssom(before[writer.SSSOM], tsv(fields, rows), current)


@pytest.mark.parametrize("field,value", [("comment", ""), ("validation_method", "")])
def test_pure_completed_promotion_refuses_lost_comment_or_stamp(case, field, value):
    _, _, _, before = case
    current = writer.propose_record(before[writer.OWNER], timestamp=STAMP)
    promoted = writer.promoted_sssom(before[writer.SSSOM], candidate_bytes(before, current), current)
    fields, rows = writer.table(promoted)
    parent = next(r for r in rows if r["subject_id"] == writer.SUBJECT and r["object_id"] == writer.PARENT)
    parent[field] = value
    header = promoted[:promoted.index(b"subject_id\t")]
    with pytest.raises(ValueError, match="canonical anchors|bounded native row"):
        writer.completed_anchors(before[writer.SSSOM], before[writer.BASELINE], header + tsv(fields, rows),
                                 writer.retired_baseline(before[writer.BASELINE]), current)


@pytest.mark.usefixtures("native_runtime")
def test_dry_run_and_complete_source_receipt_noop(case):
    root, evidence, log, before = case
    result = writer.apply_sources(root, evidence, log)
    assert result["applied"] is False and not log.exists()
    assert all((root / p).read_bytes() == b for p, b in before.items())
    apply(case)
    after = (root / writer.OWNER).read_bytes()
    assert writer.apply_sources(root, evidence, log, apply=True)["changed"] is False
    assert (root / writer.OWNER).read_bytes() == after
    assert len(json.loads(log.read_bytes())["records"]) == 1


@pytest.mark.parametrize("corrupt", ["receipt_missing", "receipt_approval", "receipt_transaction", "backup", "owner", "canonical", "baseline"])
@pytest.mark.usefixtures("native_runtime")
def test_completed_source_requires_original_receipt_and_all_exact_anchors(case, corrupt):
    root, evidence, log, _ = case
    apply(case)
    if corrupt == "receipt_missing":
        log.unlink()
    elif corrupt.startswith("receipt_"):
        value = json.loads(log.read_bytes())
        if corrupt == "receipt_approval":
            value["approval"] = "APPROVED"
        else:
            value["transaction"]["changed"] = []
        log.write_text(json.dumps(value))
    else:
        path = {"backup": writer.backups(log)[writer.OWNER], "owner": root / writer.OWNER,
                "canonical": root / writer.SSSOM, "baseline": root / writer.BASELINE}[corrupt]
        path.write_bytes(path.read_bytes() + b"\n")
    snapshot = {p: p.read_bytes() for p in (root / writer.OWNER, root / writer.SSSOM, root / writer.BASELINE)}
    with pytest.raises((ValueError, FileNotFoundError)):
        writer.apply_sources(root, evidence, log, apply=True)
    assert snapshot == {p: p.read_bytes() for p in snapshot}


@pytest.mark.usefixtures("native_runtime")
def test_native_promotion_preserves_unrelated_bytes_comment_stamps_and_noops(case):
    root, evidence, source, before = case
    args = promotion(case)
    result = writer.promote(**args, apply=True)
    assert (result["changed_rows"], result["removed_rows"], result["removed_baseline_rows"]) == (2, 1, 1)
    _, rows = writer.table((root / writer.SSSOM).read_bytes())
    _, prior = writer.table(before[writer.SSSOM])
    target = [r for r in rows if r["subject_id"] == writer.SUBJECT]
    assert len(target) == 2 and {r["object_id"] for r in target} == {writer.PARENT, writer.NEW}
    for row in target:
        old = next(r for r in prior if r["subject_id"] == writer.SUBJECT and r["object_id"] == row["object_id"])
        assert row["validation_method"] == old["validation_method"]
        assert set(old["source"].split("|")) <= set(row["source"].split("|"))
        if row["object_id"] == writer.PARENT:
            assert row["comment"] == old["comment"] and row["comment"].startswith("[#390")
            assert row["other"] == ""
        else:
            assert row["other"] == "CAS:17989-41-2"
    def other(data):
        return [line for line in data.splitlines(keepends=True) if not line.startswith((writer.SUBJECT + "\t").encode())
                and not line.startswith((b"# mapping_date:", b"# mapping_set_version:"))]
    assert other(before[writer.SSSOM]) == other((root / writer.SSSOM).read_bytes())
    removed = f"{writer.SUBJECT}\tGlycerol 3-phosphate\tMIM:Glycerol_3-phosphate\tUNREVIEWED\n".encode()
    assert (root / writer.BASELINE).read_bytes() == before[writer.BASELINE].replace(removed, b"")
    assert writer.promote(**args, apply=True)["changed"] is False
    assert writer.apply_sources(root, evidence, source, apply=True)["changed"] is False


@pytest.mark.parametrize("field,value", [("source", "MIM:invented"), ("validation_method", ""),
                                        ("other", "Glycerol 3-phosphate"), ("predicate_id", "skos:exactMatch"),
                                        ("object_id", "cas:17989-41-2"), ("mapping_date", "2025-01-01")])
@pytest.mark.usefixtures("native_runtime")
def test_candidate_claim_substitution_refused_before_publication(case, field, value):
    args = promotion(case)
    fields, rows = writer.table(args["candidate"].read_bytes())
    rows[0][field] = value
    args["candidate"].write_bytes(tsv(fields, rows))
    args["candidate_sha256"] = writer.digest(args["candidate"].read_bytes())
    with pytest.raises(ValueError):
        writer.promote(**args, apply=True)
    assert not args["log"].exists()
    assert (case[0] / writer.SSSOM).read_bytes() == case[3][writer.SSSOM]


@pytest.mark.parametrize("phase", ["sources", "promote"])
@pytest.mark.parametrize("target", ["log", "backup", "owner_alias"])
@pytest.mark.usefixtures("native_runtime")
def test_native_existing_receipt_backup_or_source_alias_is_refused(case, phase, target):
    root, evidence, source, before = case
    args = promotion(case) if phase == "promote" else None
    log = args["log"] if args else source
    target_path = log if target == "log" else writer.backups(log)[writer.SSSOM]
    if target == "owner_alias":
        target_path = root / writer.OWNER
        actual = root / "original-owner.yaml"
        actual.write_bytes(target_path.read_bytes())
        target_path.unlink()
    else:
        target_path.parent.mkdir(parents=True, exist_ok=True)
        actual = root / "competing-receipt"
        actual.write_bytes(b"competing bytes")
    target_path.symlink_to(actual)
    with pytest.raises((ValueError, FileExistsError)):
        if args:
            writer.promote(**args, apply=True)
        else:
            writer.apply_sources(root, evidence, source, apply=True)
    assert target_path.is_symlink()
    assert (root / writer.SSSOM).read_bytes() == before[writer.SSSOM]


@pytest.mark.parametrize("phase", ["sources", "promote"])
@pytest.mark.parametrize("race", ["destination_owner", "source", "candidate_or_evidence"])
@pytest.mark.usefixtures("native_runtime")
def test_native_commit_boundary_rechecks_scope_and_bound_bytes(case, monkeypatch, phase, race):
    root, evidence, source, before = case
    args = promotion(case) if phase == "promote" else None
    original = writer.guarded.reserve_receipt_outputs

    @contextmanager
    def changed(*a, **kw):
        with original(*a, **kw) as handles:
            if race == "destination_owner":
                record = yaml.safe_load(writer.frozen_owner())
                record["identifier"] = writer.NEW
                path = root / "data/ingredients/mapped/.ignored/nested/Competing.yaml"
                path.parent.mkdir(parents=True)
                path.write_bytes(writer.render(record))
            else:
                path = root / writer.OWNER if race == "source" else (
                    args["candidate"] if args else evidence / "chebi-15978-primary.json")
                path.write_bytes(path.read_bytes() + b"\n")
            yield handles

    monkeypatch.setattr(writer.guarded, "reserve_receipt_outputs", changed)
    with pytest.raises((ValueError, RuntimeError)):
        if args:
            writer.promote(**args, apply=True)
        else:
            writer.apply_sources(root, evidence, source, apply=True)
    assert (root / writer.SSSOM).read_bytes() == before[writer.SSSOM]
    assert (root / writer.BASELINE).read_bytes() == before[writer.BASELINE]


@pytest.mark.usefixtures("native_runtime")
def test_shared_parent_owner_is_allowed_and_exact_local_owner_is_not(case):
    root, evidence, log, _ = case
    record = yaml.safe_load(writer.frozen_owner())
    record["identifier"] = "CHEBI:15978"
    other = root / "data/ingredients/mapped/Parent.yaml"
    other.write_bytes(writer.render(record))
    writer.apply_sources(root, evidence, log)
    record["identifier"] = writer.NEW
    other.write_bytes(writer.render(record))
    with pytest.raises(ValueError, match="Destination identity"):
        writer.apply_sources(root, evidence, log)


@pytest.mark.parametrize("corrupt", ["missing", "approval", "backup", "candidate_hash"])
@pytest.mark.usefixtures("native_runtime")
def test_completed_promotion_requires_its_own_execution_receipt(case, corrupt):
    args = promotion(case)
    writer.promote(**args, apply=True)
    if corrupt == "missing":
        args["log"].unlink()
    elif corrupt == "backup":
        p = writer.backups(args["log"])[writer.SSSOM]
        p.write_bytes(p.read_bytes() + b"\n")
    elif corrupt == "candidate_hash":
        args["candidate_sha256"] = "0" * 64
    else:
        value = json.loads(args["log"].read_bytes())
        value["approval"] = "APPROVED"
        args["log"].write_text(json.dumps(value))
    with pytest.raises((ValueError, FileNotFoundError)):
        writer.promote(**args, apply=True)


@pytest.mark.usefixtures("native_runtime")
def test_actual_native_generator_two_rows_and_replayed_stamps(case, monkeypatch):
    path = Path(os.environ.get("MIM_SSSOM_PRODUCER", ROOT.parent / "claw-cas-guard")) / "scripts/build_mim_ingredient_sssom.py"
    if not path.is_file():
        pytest.skip("Native merged producer is an optional explicit integration dependency")
    monkeypatch.syspath_prepend(str(path.parent))
    spec = importlib.util.spec_from_file_location("lithium_native_builder", path)
    builder = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(builder)
    apply(case)
    root, _, _, before = case
    aliases = {"CHEBI:15978": ("Glycerol 3-phosphate", ["sn-glycerol 3-(dihydrogen phosphate)"])}
    rows = builder._row_from_yaml(root / writer.OWNER, {}, {"CHEBI:15978": "native_ontology:chebi"}, aliases,
                                  {"CHEBI:15978": "sn-glycerol 3-phosphate"})
    builder.apply_replayed_stamps(rows, builder._load_existing_validation_method(root / writer.SSSOM))
    fields, _ = writer.table(before[writer.SSSOM])
    assert len(rows) == 2 and [r["other"] for r in rows] == ["", "CAS:17989-41-2"]
    actual = tsv(fields, rows)
    assert actual == candidate(case)
    promoted = writer.promoted_sssom(before[writer.SSSOM], actual, (root / writer.OWNER).read_bytes())
    assert len(writer.table(promoted)[1]) == len(writer.table(before[writer.SSSOM])[1]) - 1
