"""Bounded owned-name source correction and canonical projection regressions."""
import copy
import importlib.util
import json
from pathlib import Path
import shutil
import sys
import os
import subprocess
from contextlib import contextmanager

import pytest
import yaml

ROOT = Path(__file__).resolve().parents[1]
HERE = ROOT / "tests"
spec = importlib.util.spec_from_file_location("owned_name_draft", ROOT / "scripts/apply_owned_name_policy.py")
w = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = w
spec.loader.exec_module(w)
STAMP = "2026-11-01T12:00:00+00:00"


@pytest.fixture(scope="module")
def current():
    return w.propose_sources({p: w.frozen(p) for p in w.OWNERS}, timestamp=STAMP)


def candidate(current):
    """Explicit frozen-input fixture, independently checked by native producer below."""
    fields, old = w.table(w.frozen(w.SSSOM))
    rows = []
    for prior in old:
        path = Path("data/ingredients/mapped/" + prior["subject_id"][4:] + ".yaml")
        if path not in current:
            continue
        row = dict(prior)
        record = yaml.safe_load(current[path])
        row["mapping_date"] = STAMP[:10]
        row["source"] = "|".join(["MIM:" + x["source"] for x in record["ontology_mapping"]["evidence"]] + ["MIM:curator=Codex", "kgm:fixture"])
        if path == w.G:
            row["other"], row["comment"] = "", ""
        elif path == w.BETA:
            row["other"] = "beta-D-galactopyranosyl-(1->4)-beta-D-glucopyranose|CAS:5965-66-2"
            row["comment"] = ""
        elif row["object_id"] == "CHEBI:15978":
            row.update(object_id="CHEBI:17270", object_label="glycerol 2-phosphate", comment="", validation_method="")
            row["other"] = "|".join(prior["other"].split("|")[1:])
        else:
            row["comment"] = prior["comment"].replace("CHEBI:15978", "CHEBI:17270")
        rows.append(row)
    return w.tsv(fields, rows)


def project(current, raw=None):
    return w.promoted_sssom(w.frozen(w.SSSOM), raw or candidate(current), current,
        kg_sources_by_target={key: ["kgm:fixture"] for key in ("CHEBI:15978", "CHEBI:36218", "CHEBI:17270")})


def test_three_exact_source_changes_and_history_prefixes(current):
    assert set(current) == set(w.OWNERS)
    for p, data in current.items():
        old, new = yaml.safe_load(w.frozen(p)), yaml.safe_load(data)
        assert new["curation_history"][:-1] == old["curation_history"]
        event = new["curation_history"][-1]
        assert event["curator"] == "Codex" and event["llm_assisted"] is True
        assert event["timestamp"] == STAMP and "NONE" in event["changes"]
        for key in set(old) - {"synonyms", "ontology_mapping", "curation_history"}:
            assert new[key] == old[key]
        if p != w.NA:
            assert new["ontology_mapping"] == old["ontology_mapping"]
            for i, synonym in enumerate(new["synonyms"]):
                expected = dict(old["synonyms"][i])
                if p == w.G and i in (1, 2, 3):
                    expected["synonym_type"] = "REJECTED_LABEL"
                    assert synonym["source"] == "sssom_other_backfill"
                elif p == w.BETA and i == 0:
                    expected["synonym_type"] = "RELATED_SYNONYM"
                assert synonym == expected
        else:
            assert new["synonyms"] == old["synonyms"]
            assert new["ontology_mapping"]["ontology_id"] == "CHEBI:17270"
            assert new["ontology_mapping"]["mapping_quality"] == "NARROW_MATCH"
            assert old["ontology_mapping"]["evidence"][0]["notes"] in new["ontology_mapping"]["evidence"][0]["notes"]
            assert new["ontology_mapping"]["evidence"][0]["notes"].startswith("Historical evidence superseded by #1020")
            assert [x["source"] for x in new["ontology_mapping"]["evidence"][1:]] == list(w.PARENT_URLS)
    reason = yaml.safe_load(current[w.G])["curation_history"][-1]["changes"]
    assert all(x in reason for x in ("Gro", "glycerolum", "glycyl alcohol", w.GLY_URL, "ef5963dbacd1d57d743637073cc8d2a12b6f8d940447e5c1bfdba519081e0961"))
    assert "Negative alias evidence" in reason
    w.verify_complete_sources(current)


def test_primary_routes_are_same_payload_with_distinct_receipts():
    evidence = w.evidence_inputs(w.ROOT / w.EVIDENCE)
    assert evidence[w.ROOT / w.EVIDENCE / "pubchem-13408-09-8-properties.json"] == evidence[w.ROOT / w.EVIDENCE / "pubchem-2735049-properties.json"]
    receipts = [json.loads(evidence[w.ROOT / w.EVIDENCE / (name + ".receipt.json")]) for name in ("pubchem-13408-09-8-properties.json", "pubchem-2735049-properties.json")]
    assert receipts[0]["url"] != receipts[1]["url"] and receipts[0]["sha256"] == receipts[1]["sha256"]


def test_scope_exact_bytes_stamps_provenance_and_deferred_rows(current):
    actual = project(current)
    assert b"owned-name-policy-v1; suppression-sidecar-required" in actual
    fields, before = w.table(w.frozen(w.SSSOM))
    _, after = w.table(actual)
    old = {(x["subject_id"], x["object_id"]): x for x in before}
    new = {(x["subject_id"], x["object_id"]): x for x in after}
    assert len(before) == len(after)
    edited = {"MIM:" + p.stem for p in w.OWNERS}
    suppressed = {x["subject_id"] for x in w.PLAN if x["disposition"] == "SUPPRESS"}
    for key, row in old.items():
        if key[0] not in edited:
            assert {k: v for k, v in new[key].items() if k != "other"} == {k: v for k, v in row.items() if k != "other"}
        if key[0] not in edited | suppressed:
            assert new[key] == row
    # L-asparagine's confidence, comment, source vocabulary and stamp stay exact.
    key = ("MIM:L-asparagine", "CHEBI:17196")
    assert new[key]["confidence"] == "0.95"
    assert new[key]["comment"] == old[key]["comment"]
    assert new[key]["source"] == old[key]["source"]
    assert new[key]["validation_method"] == old[key]["validation_method"]
    # New parent has correction-only provenance and retains #390 as history.
    parent = new[("MIM:Na2glycerophosphate5h2o", "CHEBI:17270")]
    assert parent["validation_method"] == ""
    assert old[("MIM:Na2glycerophosphate5h2o", "CHEBI:15978")]["comment"] in parent["comment"]
    assert "Historical" in parent["comment"] and "CHEBI:15978" in parent["comment"]
    assert "Edison" not in parent["source"]
    for obj in ("cas:13408-09-8", "kgmicrobe.compound:na2glycerophosphate5h2o"):
        key = ("MIM:Na2glycerophosphate5h2o", obj)
        for field in ("object_id", "confidence", "other", "validation_method"):
            assert new[key][field] == old[key][field]
        assert "CHEBI:17270" in new[key]["comment"]
    deferred = json.loads((w.REPORT / "decisions/deferred-pairs-to-preserve.json").read_bytes())
    for pair in deferred:
        for item in pair["canonical_rows"]:
            row = item["row"]
            assert new[(row["subject_id"], row["object_id"])] == row
    selected = {"MIM:" + p.stem for p in w.AFFECTED}
    unchanged = lambda data: [line for line in data.splitlines(True) if not line.startswith(b"#") and line.split(b"\t", 1)[0].decode() not in selected]
    assert unchanged(actual) == unchanged(w.frozen(w.SSSOM))


@pytest.mark.parametrize("field,value", [("confidence", "0.8"), ("comment", "invented"), ("validation_method", "new approval"), ("other", "Gro"), ("source", "MIM:invented"), ("object_label", "wrong label"), ("mapping_date", "2025-01-01"), ("predicate_id", "skos:closeMatch")])
def test_candidate_substitution_refused(current, field, value):
    fields, rows = w.table(candidate(current))
    rows[0][field] = value
    with pytest.raises(ValueError, match="bounded native row"):
        project(current, w.tsv(fields, rows))


def test_baseline_exact_twelve_retirements_no_deferred_change():
    old = w.frozen(w.BASELINE)
    new = w.retired_baseline(old)
    assert len(w.table(new)[1]) == 23
    assert set(new.splitlines(True)[1:]) < set(old.splitlines(True)[1:])
    deferred = json.loads((w.REPORT / "decisions/deferred-pairs-to-preserve.json").read_bytes())
    assert w.table(new)[1] == [x["baseline"] for x in deferred]


def test_sidecar_scoped_eleven_and_historical_origins(current):
    sample = [x["precuration_diagnostic_encounter"] for x in w.PLAN if x["yaml_alias_basis"]]
    diagnostic = w.tsv(w.COLS, sample)
    _, rows = w.table(w.canonical_sidecar(project(current), candidate_sidecar=diagnostic))
    assert len(rows) == 11 and len({(r["subject_id"], r["token_key"]) for r in rows}) == 11
    assert sum(json.loads(r["input_surfaces"]) == ["prior_sssom"] for r in rows) == 4
    assert all(r["subject_id"] != "MIM:Na2glycerophosphate5h2o" for r in rows)
    with pytest.raises(ValueError, match="still-published"):
        w.canonical_sidecar(w.frozen(w.SSSOM), candidate_sidecar=diagnostic)


def test_l_asparagine_approval_exact_owner_payload_position(current):
    proof = json.loads((w.REPORT / "decisions/l-asparagine-approval-to-preserve.json").read_bytes())
    role = proof["current_assertion"]
    assert role["resolution_status"] == "APPROVED" and role["source_position"] == "1"
    path = Path(role["source_record"])
    assert path not in current and w.digest(w.frozen(path)) == role["source_record_sha256"]
    entry = proof["inherited_review_entry"]
    assert all(entry[k] == role[k] for k in ("source_record", "source_record_sha256", "source_position", "assertion_sha256"))
    receipts = w.source_records(current)
    assert len(receipts) == 13
    unchanged = [r for r in receipts if r["before_yaml_sha256"] == r["after_yaml_sha256"]]
    assert len(unchanged) == 10 and any(r["source_record"] == str(path) for r in unchanged)


@pytest.fixture
def native_case(tmp_path):
    pytest.importorskip("kg_microbe_write")
    root = tmp_path.resolve()
    for p in (*map(Path, w.OWNER_META), w.SSSOM, w.BASELINE):
        dest = root / p
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_bytes(w.frozen(p))
    evidence = root / "sources"
    shutil.copytree(w.ROOT / w.EVIDENCE, evidence)
    yield root, evidence, root / "receipts/source.json"
    shutil.rmtree(root)


def test_real_native_source_dryrun_apply_and_complete_receipt(native_case):
    root, evidence, log = native_case
    assert w.apply_sources(root, evidence, log)["applied"] is False
    assert not log.exists()
    result = w.apply_sources(root, evidence, log, apply=True)
    assert json.loads(log.read_bytes())["state"] == "complete" and result["applied"] is True
    assert len(result["records"]) == 13
    assert w.apply_sources(root, evidence, log, apply=True)["changed"] is False
    assert (root / "data/ingredients/mapped/L-asparagine.yaml").read_bytes() == w.frozen(Path("data/ingredients/mapped/L-asparagine.yaml"))


@pytest.mark.parametrize("change", ["receipt", "backup", "source", "canonical", "baseline"])
def test_native_complete_binding_refuses_substitution(native_case, change):
    root, evidence, log = native_case
    w.apply_sources(root, evidence, log, apply=True)
    path = {"receipt": log, "backup": log.with_name("source.before-Beta-lactose.yaml"), "source": root / w.BETA, "canonical": root / w.SSSOM, "baseline": root / w.BASELINE}[change]
    path.write_bytes(path.read_bytes() + b"\n")
    if change == "receipt":
        value = json.loads(path.read_bytes());value["approval"] = "APPROVED";path.write_text(json.dumps(value))
    with pytest.raises(ValueError):
        w.apply_sources(root, evidence, log, apply=True)


@pytest.mark.parametrize("kind", ["new_nested_owner", "changed_alias_owner", "reserved_receipt_replaced",
                                  "new_promotion_artifact", "new_symlink_directory"])
def test_native_reserved_boundary_refuses_scope_change(native_case, monkeypatch, kind):
    root, evidence, log = native_case
    reserve = w.guarded.reserve_receipt_outputs
    @contextmanager
    def altered(*args, **kwargs):
        with reserve(*args, **kwargs) as handles:
            if kind == "new_nested_owner":
                path = root / "data/ingredients/mapped/nested/extra.yaml"
                path.parent.mkdir(parents=True)
                path.write_bytes(w.frozen(w.G))
            elif kind == "changed_alias_owner":
                path = root / "data/ingredients/mapped/Lactose.yaml"
                path.write_bytes(path.read_bytes() + b"\n")
            elif kind == "reserved_receipt_replaced":
                log.unlink()
                log.write_text("competing receipt")
            elif kind == "new_promotion_artifact":
                (root / w.PROMOTION_MANIFEST).write_text("{}")
            else:
                target = root / "outside-alias"
                target.mkdir()
                (target / "ignored.yaml").write_bytes(w.frozen(w.G))
                (root / "data/ingredients/mapped/alias").symlink_to(target, target_is_directory=True)
            yield handles
    monkeypatch.setattr(w.guarded, "reserve_receipt_outputs", altered)
    with pytest.raises(Exception, match="path set|changed|replaced|artifact|alias"):
        w.apply_sources(root, evidence, log, apply=True)
    assert all((root / p).read_bytes() == w.frozen(p) for p in w.OWNERS)


def test_actual_native_producer_rows_and_rejected_kg_alias_boundary(current):
    pytest.importorskip("kg_microbe_write")
    if "MIM_OWNED_NAME_PRODUCER_ROOT" not in os.environ:
        pytest.skip("Separate merged Claw producer source profile is not configured")
    path = Path(os.environ["MIM_OWNED_NAME_PRODUCER_ROOT"]) / "scripts/build_mim_ingredient_sssom.py"
    spec = importlib.util.spec_from_file_location("owned_name_draft_native_builder", path)
    builder = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = builder
    exec(compile(path.read_bytes(), str(path), "exec"), builder.__dict__)
    records = {p: yaml.safe_load(current.get(Path(p), w.frozen(Path(p)))) for p in w.OWNER_META}
    owners = builder.build_owner_index({"MIM:" + Path(p).stem: d for p, d in records.items()})
    labels = {"CHEBI:15978": "sn-glycerol 3-phosphate", "CHEBI:36218": "beta-lactose", "CHEBI:17270": "glycerol 2-phosphate"}
    kg_sources = {k: "fixture" for k in labels}
    rows, events = [], []
    for p in w.OWNERS:
        rows.extend(builder._row_from_yaml(w.NATIVE / p, {}, kg_sources,
            {"CHEBI:15978": ("sn-glycerol 3-phosphate", ["Gro", "glycerolum", "glycyl alcohol"])}, labels,
            record=records[str(p)], owners=owners, suppressions=events))
    _, prior = w.table(w.frozen(w.SSSOM))
    stamps = {(r["subject_id"], r["predicate_id"], r["object_id"]): r["validation_method"] for r in prior if r["validation_method"]}
    builder.apply_replayed_stamps(rows, stamps)
    assert rows == w.table(candidate(current))[1]
    assert project(current, w.tsv(w.table(candidate(current))[0], rows)) == project(current)
    glycerol = {"identifier": "CHEBI:17754", "preferred_term": "glycerol", "mapping_status": "MAPPED",
                "ontology_mapping": {"ontology_id": "CHEBI:17754", "ontology_label": "glycerol", "mapping_quality": "EXACT_MATCH"},
                "curation_history": [{"timestamp": STAMP}], "synonyms": []}
    legitimate = builder._row_from_yaml(Path("Glycerol.yaml"), {}, {},
        {"CHEBI:17754": ("glycerol", ["Gro", "glycerolum", "glycyl alcohol"])}, {"CHEBI:17754": "glycerol"},
        record=glycerol, owners={"glycerol": frozenset({"MIM:Glycerol"})})
    assert {"gro", "glycerolum", "glycyl alcohol"} <= {t.casefold() for t in legitimate[0]["other"].split("|")}


@pytest.mark.parametrize("field", ["source_yaml_changes_authorized", "affected_receipt_owner"])
def test_import_rejects_altered_owner_manifest_even_when_restored(tmp_path, field):
    """Real #1052 import/restore, without patching executable globals or code."""
    checkout = tmp_path.resolve() / "checkout"
    for path in w.CODE_PATHS:
        target = checkout / path.relative_to(w.ROOT)
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(path.read_bytes())
    for relative in ("tests/fixtures/issue669-owned-name-before", "reports/owned_name_policy_669_20261101"):
        shutil.copytree(w.ROOT / relative, checkout / relative)
    script = r'''
import importlib.util,json,sys
from pathlib import Path
root,field=Path(sys.argv[1]),sys.argv[2]
manifest=root/'tests/fixtures/issue669-owned-name-before/owner-manifest.json'
before=manifest.read_bytes();data=json.loads(before)
data['data/ingredients/mapped/Na2glycerophosphate5h2o.yaml'][field]=False
manifest.write_text(json.dumps(data))
failure=None
try:
 path=root/'scripts/apply_owned_name_policy.py'
 spec=importlib.util.spec_from_file_location('manifest_restore_probe',path)
 module=importlib.util.module_from_spec(spec);sys.modules[spec.name]=module
 spec.loader.exec_module(module)
except ValueError as error:failure=str(error)
finally:manifest.write_bytes(before)
print(json.dumps({'refused':failure,'original_restored':manifest.read_bytes()==before}))
'''
    result = subprocess.run([sys.executable, "-c", script, str(checkout), field], capture_output=True, text=True)
    assert result.returncode == 0, result.stderr
    proof = json.loads(result.stdout)
    assert proof == {"refused": "Reviewed owner manifest changed before import", "original_restored": True}
