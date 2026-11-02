"""Bounded CAS correction, native receipt/race and exact candidate projection tests."""

import copy
import csv
import gzip
import importlib.util
import io
import json
import os
import subprocess
import sys
from contextlib import contextmanager
from pathlib import Path

import pytest
import yaml

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "izalpinin_cas", ROOT / "scripts/correct_izalpinin_cas.py"
)
mod = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(mod)
FROZEN = json.loads((ROOT / mod.REPORT / "preimages/mapping-before.json").read_bytes())
_SOURCE_ROWS = [FROZEN["row"]]
STAMP = "2030-01-02T00:00:00+00:00"


@pytest.fixture
def record():
    return yaml.safe_load(mod.frozen_owner())


def tsv(fields, rows, header=b""):
    stream = io.StringIO(newline="")
    writer = csv.DictWriter(stream, fieldnames=fields, delimiter="\t", lineterminator="\n")
    writer.writeheader()
    writer.writerows(rows)
    return header + stream.getvalue().encode()


@pytest.fixture
def case(tmp_path, monkeypatch):
    root = tmp_path.resolve() / "mim"
    root.mkdir()
    target = copy.deepcopy(_SOURCE_ROWS)
    fields = list(target[0])
    other = dict.fromkeys(fields, "")
    other.update(
        subject_id="MIM:untouched",
        subject_label="untouched",
        predicate_id="skos:exactMatch",
        object_id="CHEBI:1",
        object_label="untouched",
        mapping_date="2026-08-01",
    )
    before = {
        mod.OWNER: mod.frozen_owner(),
        mod.SSSOM: tsv(
            fields,
            [*target, other],
            b'# mapping_date: "2026-08-13"\n# mapping_set_version: "2026-08-13"\n',
        ),
        mod.BASELINE: b"subject_id\tother\nMIM:deferred\tunchanged\n",
        mod.SIDECAR: b"subject_id\ttoken\nMIM:held\tunchanged\n",
    }
    manifest = {
        "schema_version": 1,
        "policy_version": "owned-name-policy-v1",
        "artifacts": {str(p): mod.digest(b) for p, b in before.items() if p != mod.OWNER},
        "source_owner_sha256": {mod.RECORD: mod.BEFORE[mod.OWNER]},
        "decisions": [{"historical": "retain exactly"}],
        "generation_manifest_sha256": "original-generation",
        "form_projection_updates": copy.deepcopy(FROZEN["form_projection_updates"]),
    }
    before[mod.MANIFEST] = mod.encoded(manifest)
    for path, data in before.items():
        target_path = root / path
        target_path.parent.mkdir(parents=True, exist_ok=True)
        target_path.write_bytes(data)
        monkeypatch.setitem(mod.BEFORE, path, mod.digest(data))
    evidence = root / mod.EVIDENCE
    evidence.parent.mkdir(parents=True)
    original = ROOT / mod.EVIDENCE
    evidence.write_bytes(original.read_bytes())
    for name in json.loads(original.read_bytes())["files"]:
        dest = root / name
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_bytes((ROOT / name).read_bytes())
    receipt_parent = tmp_path.resolve() / "receipts"
    receipt_parent.mkdir()
    return root, evidence, receipt_parent / "source.json", before


@pytest.fixture
def native_runtime():
    pytest.importorskip("kg_microbe_write", reason="Real native publisher required")


def apply(case):
    root, evidence, log, _ = case
    return mod.apply_sources(root, evidence, log, apply=True)


def candidate_bytes(before, current):
    _, fields, pairs = mod.table(before[mod.SSSOM])
    old = next(row for row, _ in pairs if row["subject_id"] == mod.SUBJECT)
    row = dict(old)
    row.update(
        object_id=mod.IDENTITY,
        other="CAS:480-14-8",
        validation_method="",
        mapping_date=yaml.safe_load(current)["curation_history"][-1]["timestamp"][:10],
        source=row["source"] + "|MIM:curator=claude",
    )
    return tsv(fields, [row])


def test_exact_correction_preserves_history_scientific_scope_and_known_candidate(record):
    before = copy.deepcopy(record)
    after = mod.corrected_record(record, timestamp=STAMP)
    assert record == before and after is not None
    assert after["identifier"] == after["ontology_mapping"]["ontology_id"] == mod.IDENTITY
    assert after["chemical_properties"]["cas_rn"] == "480-14-8"
    assert after["ontology_mapping"]["mapping_quality"] == "FALLBACK_REGISTRY"
    assert after["ontology_mapping"]["evidence"][:-1] == before["ontology_mapping"]["evidence"]
    assert after["curation_history"][:-1] == before["curation_history"]
    event = after["curation_history"][-1]
    assert event["curator"] == "claude" and event["llm_assisted"] is True
    assert "WITHHOLD" in event["changes"] and "LIPIDMAPS:LMPK12111656" in event["changes"]
    assert "OPEN" in event["changes"] and mod.APPROVAL.startswith("NONE:")
    restored = copy.deepcopy(after)
    for field in ("identifier", "ontology_mapping", "chemical_properties", "curation_history"):
        restored[field] = before[field]
    assert restored == before
    assert not {"molecular_formula", "inchi", "pubchem_cid", "molecular_weight"} & set(
        after["chemical_properties"]
    )
    assert mod.corrected_record(after) is None


@pytest.mark.parametrize(
    "mutation", ["identity", "chemistry", "mapping", "synonym", "unknown", "history"]
)
def test_pure_proposal_refuses_unreviewed_state(record, mutation):
    changed = copy.deepcopy(record)
    if mutation == "identity":
        changed["identifier"] = "cas:480-14-8"
    elif mutation == "chemistry":
        changed["chemical_properties"]["cas_rn"] = "480-14-8"
    elif mutation == "mapping":
        changed["ontology_mapping"]["mapping_quality"] = "EXACT_MATCH"
    elif mutation == "synonym":
        changed["synonyms"] = [{"name": "unreviewed"}]
    elif mutation == "unknown":
        changed["scientific_approval"] = True
    else:
        changed["curation_history"] = []
    with pytest.raises(ValueError):
        mod.corrected_record(changed, timestamp=STAMP)


def test_native_cas_syntax_success_is_separate_from_approval(record):
    from mediaingredientmech.ingredient_bundle_contract import valid_cas

    assert not valid_cas(mod.OLD_IDENTITY) and valid_cas(mod.IDENTITY)
    after = mod.corrected_record(record, timestamp=STAMP)
    assert after["ontology_mapping"]["mapping_quality"] == "FALLBACK_REGISTRY"
    assert mod.APPROVAL.startswith("NONE:") and "WITHHOLD" in mod.APPROVAL
    assert "final primary" in mod.APPROVAL and "OPEN" in mod.APPROVAL


@pytest.mark.parametrize("stamp", ["2026-11-02T01:26:34+00:00", "2030-01-02T01:00:00+01:00"])
def test_evidence_timestamp_boundary(stamp):
    with pytest.raises(ValueError, match="UTC after captured evidence"):
        mod.propose_record(mod.frozen_owner(), timestamp=stamp)


@pytest.mark.parametrize(
    "field,value",
    [
        ("object_id", "cas:480-14-4"),
        ("object_id", "LIPIDMAPS:LMPK12111656"),
        ("predicate_id", "skos:broadMatch"),
        ("object_source", "lipidmaps"),
        ("object_label", "galangin"),
        ("other", "CAS:480-14-4"),
        ("validation_method", "none|UNKNOWN_TERM|2026-07-07"),
        ("validation_method", "manual|APPROVED|2030-01-02"),
        ("mapping_date", "2026-01-01"),
        ("mapping_justification", "semapv:LexicalMatching"),
    ],
)
def test_single_row_projection_rejects_wrong_claim_or_inherited_stamp(case, field, value):
    _, _, _, before = case
    current = mod.propose_record(before[mod.OWNER], timestamp=STAMP)
    raw = candidate_bytes(before, current)
    _, columns, pairs = mod.table(raw)
    row = pairs[0][0]
    row[field] = value
    with pytest.raises(ValueError):
        mod.promoted_sssom(before[mod.SSSOM], tsv(columns, [row]), current)


@pytest.mark.parametrize("kind", ["missing", "duplicate", "extra_handle"])
def test_projection_cannot_add_parent_or_b1(case, kind):
    _, _, _, before = case
    current = mod.propose_record(before[mod.OWNER], timestamp=STAMP)
    _, columns, pairs = mod.table(candidate_bytes(before, current))
    rows = [pairs[0][0]]
    if kind == "missing":
        rows = []
    elif kind == "duplicate":
        rows *= 2
    else:
        rows.append(dict(rows[0], object_id="kgmicrobe.compound:izalpinin"))
    with pytest.raises(ValueError):
        mod.promoted_sssom(before[mod.SSSOM], tsv(columns, rows), current)


def test_projection_and_manifest_preserve_other_rows_and_historical_owner_map(case):
    _, _, source_log, before = case
    current = mod.propose_record(before[mod.OWNER], timestamp=STAMP)
    canonical = mod.promoted_sssom(before[mod.SSSOM], candidate_bytes(before, current), current)
    _, _, old_rows = mod.table(before[mod.SSSOM])
    _, _, rows = mod.table(canonical)
    assert len(rows) == len(old_rows) and rows[1][1] == old_rows[1][1]
    assert rows[0][0]["object_id"] == mod.IDENTITY and rows[0][0]["validation_method"] == ""
    result = json.loads(
        mod.promotion_manifest(
            before[mod.MANIFEST], canonical, current, source_log, "a" * 64, "b" * 64, "c" * 64
        )
    )
    prior = json.loads(before[mod.MANIFEST])
    assert result["form_projection_updates"] == prior["form_projection_updates"]
    change = result.pop("registry_correction_updates")
    assert (
        len(change) == 1 and change[0]["issue"] == 753 and change[0]["approval"].startswith("NONE:")
    )
    assert change[0]["prior_manifest_sha256"] == mod.digest(before[mod.MANIFEST])
    assert "not an all-current corpus snapshot" in change[0]["scope"]
    result["artifacts"][str(mod.SSSOM)] = prior["artifacts"][str(mod.SSSOM)]
    result["source_owner_sha256"][mod.RECORD] = prior["source_owner_sha256"][mod.RECORD]
    assert result == prior


@pytest.mark.usefixtures("native_runtime")
def test_source_dry_run_complete_receipt_and_exact_noop(case):
    root, evidence, log, before = case
    assert mod.apply_sources(root, evidence, log)["applied"] is False
    assert not log.exists() and all((root / p).read_bytes() == b for p, b in before.items())
    result = apply(case)
    assert result["approval"].startswith("NONE") and len(result["records"]) == 1
    assert json.loads(log.read_bytes())["state"] == "complete"
    for path, backup in mod.backups(log).items():
        assert backup.read_bytes() == before[path]
    assert mod.apply_sources(root, evidence, log, apply=True)["changed"] is False


@pytest.mark.parametrize(
    "kind",
    [
        "missing_receipt",
        "approval",
        "transaction",
        "backup",
        "role",
        "unknown",
        "timestamp",
        "canonical",
        "sidecar",
        "manifest",
        "evidence",
    ],
)
@pytest.mark.usefixtures("native_runtime")
def test_source_completed_noop_rejects_corruption(case, kind):
    root, evidence, log, _ = case
    apply(case)
    if kind == "missing_receipt":
        log.unlink()
    elif kind in {"approval", "transaction"}:
        value = json.loads(log.read_bytes())
        if kind == "approval":
            value["approval"] = "APPROVED"
        else:
            value["transaction"]["changed"] = []
        log.write_bytes(mod.encoded(value))
    elif kind in {"role", "unknown", "timestamp"}:
        value = yaml.safe_load((root / mod.OWNER).read_bytes())
        if kind == "role":
            value["occurrence_statistics"]["total_occurrences"] = 99
        elif kind == "unknown":
            value["invented_review_approval"] = True
        else:
            value["curation_history"][-1]["timestamp"] = "2030-01-03T00:00:00+00:00"
        (root / mod.OWNER).write_text(yaml.safe_dump(value, sort_keys=False))
    else:
        path = {
            "backup": mod.backups(log)[mod.OWNER],
            "canonical": root / mod.SSSOM,
            "sidecar": root / mod.SIDECAR,
            "manifest": root / mod.MANIFEST,
            "evidence": evidence,
        }[kind]
        path.write_bytes(path.read_bytes() + b"\n")
    with pytest.raises((ValueError, FileNotFoundError)):
        mod.apply_sources(root, evidence, log, apply=True)


@pytest.mark.parametrize("kind", ["owner", "evidence", "new_owner", "alias_directory"])
@pytest.mark.usefixtures("native_runtime")
def test_source_precommit_byte_and_membership_guards(case, monkeypatch, kind):
    root, evidence, log, before = case
    reserve = mod.guarded.reserve_receipt_outputs

    @contextmanager
    def altered(*args, **kwargs):
        with reserve(*args, **kwargs) as handles:
            if kind == "owner":
                value = yaml.safe_load(before[mod.OWNER])
                value["occurrence_statistics"]["total_occurrences"] = 99
                (root / mod.OWNER).write_text(yaml.safe_dump(value, sort_keys=False))
            elif kind == "evidence":
                evidence.write_bytes(evidence.read_bytes() + b"\n")
            elif kind == "new_owner":
                path = root / "data/ingredients/mapped/.ignored/competing.yaml"
                path.parent.mkdir()
                path.write_bytes(before[mod.OWNER])
            else:
                (root / "data/ingredients/mapped/alias").symlink_to(
                    evidence.parent, target_is_directory=True
                )
            yield handles

    monkeypatch.setattr(mod.guarded, "reserve_receipt_outputs", altered)
    from kg_microbe_write.transaction import ValidationFailed

    with pytest.raises((ValueError, ValidationFailed)):
        apply(case)
    assert (root / mod.SSSOM).read_bytes() == before[mod.SSSOM]
    assert json.loads(log.read_bytes())["state"] == "failed"
    if kind != "owner":
        assert (root / mod.OWNER).read_bytes() == before[mod.OWNER]
    else:
        assert (
            yaml.safe_load((root / mod.OWNER).read_bytes())["occurrence_statistics"][
                "total_occurrences"
            ]
            == 99
        )


_GEN = r"""
import importlib.util,json,sys,yaml
from pathlib import Path
producer,root,kg,bundle=map(Path,sys.argv[1:])
entry=producer/'scripts/build_mim_ingredient_sssom.py'
spec=importlib.util.spec_from_file_location('izalpinin_native_fixture_generation',entry)
b=importlib.util.module_from_spec(spec);sys.modules[spec.name]=b
exec(compile(entry.read_bytes(),str(entry),'exec'),b.__dict__)
records={path:yaml.safe_load(path.read_bytes()) for path in sorted((root/'data/ingredients/mapped').glob('*.yaml'))}
owners=b.build_owner_index({b._mim_curie(path.name):data for path,data in records.items()})
labels={}
sources=b.load_kgm_source_index(kg);klabels=b.load_kgm_labels(kg)
rows=[];events=[]
for path,record in records.items():rows.extend(b._row_from_yaml(path,{},sources,klabels,labels,record=record,owners=owners,suppressions=events))
rows=list({(r['subject_id'],r['object_id']):r for r in rows}.values())
b.apply_replayed_stamps(rows,b._load_existing_validation_method(root/'mappings/ingredient_mappings.sssom.tsv'))
b._write_sssom(rows,bundle/'candidate.sssom.tsv')
errors=b._sssom_validate(bundle/'candidate.sssom.tsv')
if errors:raise ValueError(errors)
(bundle/'suppressed_aliases.tsv').write_bytes(b.render_suppressed_aliases(events))
(bundle/'label-input-01.json').write_text(json.dumps({'loader':'immutable-test-labels','labels':labels}))
print(json.dumps({'rows':len(rows),'labels':labels}))
"""


@pytest.fixture
def native_case(case, native_runtime, tmp_path):
    producer_env = os.environ.get("MIM_OWNED_NAME_PRODUCER_ROOT")
    if not producer_env:
        pytest.skip("Explicit merged producer path required for native integration")
    root, _, source_log, before = case
    apply(case)
    producer = Path(producer_env).resolve()
    for args in [
        ("init", "-q"),
        ("add", "."),
        (
            "-c",
            "user.name=Fixture",
            "-c",
            "user.email=fixture@example.invalid",
            "commit",
            "-qm",
            "immutable source checkpoint",
        ),
    ]:
        mod.native.git(root, *args)
    revision = mod.native.git(root, "rev-parse", "HEAD").decode().strip()
    bundle = tmp_path.resolve() / "candidate"
    bundle.mkdir()
    kgroot = tmp_path.resolve() / "kg"
    kg = kgroot / "mappings/kgmicrobe_unified_entity_mappings.sssom.tsv.gz"
    kg.parent.mkdir(parents=True)
    fields = ["subject_id", "subject_label", "predicate_id", "object_id", "object_label", "source"]
    kg.write_bytes(
        gzip.compress(
            tsv(
                fields,
                [
                    dict(
                        zip(
                            fields,
                            [
                                "test:izalpinin",
                                "Izalpinin",
                                "skos:exactMatch",
                                "cas:480-14-8",
                                "Izalpinin",
                                "fixture",
                            ],
                            strict=True,
                        )
                    )
                ],
            ),
            mtime=0,
        )
    )
    result = subprocess.run(
        [sys.executable, "-I", "-c", _GEN, str(producer), str(root), str(kg), str(bundle)],
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0, result.stderr
    produced = json.loads(result.stdout)
    producers = mod.native.producer_paths(producer)
    mapped = set((root / "data/ingredients/mapped").glob("*.yaml"))
    residual = producer / "workspace/reports/kg_microbe_residual_p25_categorized.json"
    assert not residual.exists(), "Native fixture requires currently absent optional residual"
    declared = {
        path: mod.digest(path.read_bytes()) for path in mapped | producers | {kg, root / mod.SSSOM}
    }
    declared[residual] = None
    inventory = {
        str(path): {"sha256": sha, "bytes": path.stat().st_size}
        for path, sha in declared.items()
        if sha is not None
    }
    for name in ("inputs-before.json", "inputs-after.json"):
        (bundle / name).write_bytes(mod.encoded(inventory))
    manifest = {
        "schema_version": 1,
        "policy_version": "owned-name-policy-v1",
        "external_sssom_validation": "passed",
        "source_revisions": {
            "claw": mod.PRODUCER,
            "mim": revision,
            "kg_microbe": "fixture-ignored-input",
        },
        "artifacts": [
            {
                "path": str(bundle / name),
                "role": role,
                "sha256": mod.digest((bundle / name).read_bytes()),
            }
            for name, role in [
                ("candidate.sssom.tsv", "sssom"),
                ("suppressed_aliases.tsv", "suppressed_aliases"),
            ]
        ],
        "producer_import_snapshot": {str(path): declared[path] for path in producers},
        "mapped_record_paths": list(map(str, sorted(mapped))),
        "source_inputs": [
            {"path": str(path), "sha256": sha} for path, sha in sorted(declared.items())
        ],
        "canonical_label_resolution": produced["labels"],
        "prior_stamp_sources": [str(root / mod.SSSOM)],
        "emitted_rows": produced["rows"],
    }
    mpath = bundle / "candidate.sssom.tsv.manifest.json"
    mpath.write_bytes(mod.encoded(manifest))
    entry = declared[producer / "scripts/build_mim_ingredient_sssom.py"]
    receipt = {
        "input_bytes_unchanged": True,
        "scientific_approval_added": False,
        "supervisor_binding": None,
        "producer_revision": mod.PRODUCER,
        "candidate_sha256": manifest["artifacts"][0]["sha256"],
        "sidecar_sha256": manifest["artifacts"][1]["sha256"],
        "native_generation_manifest_sha256": mod.digest(mpath.read_bytes()),
        "input_manifest_sha256": mod.digest((bundle / "inputs-before.json").read_bytes()),
        "executed_entry_source_sha256": entry,
        "producer_sha256": entry,
        "label_maps": {
            "label-input-01.json": mod.digest((bundle / "label-input-01.json").read_bytes())
        },
        "prior_stamps": str(root / mod.SSSOM),
        "prior_sha256": mod.BEFORE[mod.SSSOM],
    }
    (bundle / "generation-receipt.json").write_bytes(mod.encoded(receipt))
    context = {
        key: {"path": str(path), "revision": rev, "status": ""}
        for key, path, rev in [
            ("mim", root, revision),
            ("claw", producer, mod.PRODUCER),
            ("kg_microbe", kgroot, "fixture-ignored-input"),
        ]
    }
    (bundle / "repository-context.json").write_bytes(mod.encoded(context))
    return (
        root,
        bundle,
        producer,
        source_log,
        tmp_path.resolve() / "receipts/promotion.json",
        mod.digest(mpath.read_bytes()),
        before,
    )


def promote(case, apply=False):
    root, bundle, producer, source, log, sha, _ = case
    return mod.promote(
        root, bundle, producer, source, log, generation_manifest_sha256=sha, apply=apply
    )


def test_native_generation_promotion_and_completed_source_noop(native_case):
    root, _, _, source, log, _, before = native_case
    assert promote(native_case)["applied"] is False and not log.exists()
    assert (root / mod.SSSOM).read_bytes() == before[mod.SSSOM]
    result = promote(native_case, True)
    assert result["applied"] is True and result["added_rows"] == 0
    assert set(result["transaction"]["changed"]) == {
        str(root / mod.SSSOM),
        str(root / mod.MANIFEST),
    }
    for path in (mod.BASELINE, mod.SIDECAR):
        assert (root / path).read_bytes() == before[path]
    assert promote(native_case, True)["changed"] is False
    assert mod.verify_completed(root, log, source_log=source)["changed"] is False
    assert (
        mod.apply_sources(root, root / mod.EVIDENCE, source, promotion_log=log, apply=True)[
            "changed"
        ]
        is False
    )


@pytest.mark.parametrize(
    "kind", ["candidate", "sidecar", "labels", "manifest", "owner", "source_receipt"]
)
def test_native_generation_substitution_refuses_before_write(native_case, kind):
    root, bundle, _, source, log, _, before = native_case
    path = {
        "candidate": bundle / "candidate.sssom.tsv",
        "sidecar": bundle / "suppressed_aliases.tsv",
        "labels": bundle / "label-input-01.json",
        "manifest": bundle / "candidate.sssom.tsv.manifest.json",
        "owner": root / mod.OWNER,
        "source_receipt": source,
    }[kind]
    if kind == "source_receipt":
        value = json.loads(path.read_bytes())
        value["approval"] = "APPROVED"
        path.write_bytes(mod.encoded(value))
    else:
        path.write_bytes(path.read_bytes() + b"\n")
    with pytest.raises(ValueError):
        promote(native_case, True)
    assert not log.exists() and (root / mod.SSSOM).read_bytes() == before[mod.SSSOM]


def test_consistently_rehashed_wrong_candidate_fails_native_replay(native_case):
    root, bundle, producer, source, log, _, before = native_case
    path = bundle / "candidate.sssom.tsv"
    header, fields, pairs = mod.table(path.read_bytes())
    rows = [row for row, _ in pairs]
    rows[0]["object_label"] = "invented label"
    path.write_bytes(tsv(fields, rows, "".join(header[:-1]).encode()))
    mpath = bundle / "candidate.sssom.tsv.manifest.json"
    value = json.loads(mpath.read_bytes())
    value["artifacts"][0]["sha256"] = mod.digest(path.read_bytes())
    mpath.write_bytes(mod.encoded(value))
    rpath = bundle / "generation-receipt.json"
    value = json.loads(rpath.read_bytes())
    value["candidate_sha256"] = mod.digest(path.read_bytes())
    value["native_generation_manifest_sha256"] = mod.digest(mpath.read_bytes())
    rpath.write_bytes(mod.encoded(value))
    with pytest.raises(ValueError, match="native replay"):
        mod.promote(
            root,
            bundle,
            producer,
            source,
            log,
            generation_manifest_sha256=mod.digest(mpath.read_bytes()),
            apply=True,
        )
    assert not log.exists() and (root / mod.SSSOM).read_bytes() == before[mod.SSSOM]


@pytest.mark.parametrize(
    "kind",
    [
        "candidate",
        "sidecar",
        "manifest",
        "labels",
        "new_label",
        "new_owner",
        "owner_alias",
        "baseline",
    ],
)
def test_promotion_precommit_input_and_membership_changes_refuse(native_case, monkeypatch, kind):
    root, bundle, _, _, log, _, before = native_case
    reserve = mod.guarded.reserve_receipt_outputs

    @contextmanager
    def altered(*args, **kwargs):
        with reserve(*args, **kwargs) as handles:
            if kind == "new_owner":
                path = root / "data/ingredients/mapped/.ignored/competing.yaml"
                path.parent.mkdir()
                path.write_bytes(before[mod.OWNER])
            elif kind == "owner_alias":
                (root / "data/ingredients/mapped/alias").symlink_to(
                    bundle, target_is_directory=True
                )
            elif kind == "new_label":
                (bundle / "label-input-02.json").write_text("{}")
            else:
                path = {
                    "candidate": bundle / "candidate.sssom.tsv",
                    "sidecar": root / mod.SIDECAR,
                    "manifest": root / mod.MANIFEST,
                    "labels": bundle / "label-input-01.json",
                    "baseline": root / mod.BASELINE,
                }[kind]
                path.write_bytes(path.read_bytes() + b"\n")
            yield handles

    monkeypatch.setattr(mod.guarded, "reserve_receipt_outputs", altered)
    from kg_microbe_write.transaction import ValidationFailed

    with pytest.raises((ValueError, ValidationFailed)):
        promote(native_case, True)
    assert (root / mod.SSSOM).read_bytes() == before[mod.SSSOM]
    assert json.loads(log.read_bytes())["state"] == "failed"


@pytest.mark.parametrize("phase", ["source", "promotion"])
def test_completed_noop_still_rejects_ignored_competing_owner(native_case, phase):
    root, _, _, source, log, _, before = native_case
    if phase == "promotion":
        promote(native_case, True)
    path = root / "data/ingredients/mapped/.ignored/competitor.yaml"
    path.parent.mkdir()
    path.write_bytes(before[mod.OWNER])
    with pytest.raises(ValueError):
        if phase == "source":
            mod.apply_sources(root, root / mod.EVIDENCE, source, apply=True)
        else:
            mod.verify_completed(root, log, source_log=source)


def test_loaded_shared_dependency_binding_refuses_mismatch(monkeypatch):
    path = ROOT / "src/mediaingredientmech/schema/mediaingredientmech.yaml"
    monkeypatch.setitem(mod.policy._LOADED_CODE, path, b"different loaded schema")
    with pytest.raises(ValueError, match="Loaded shared dependency"):
        mod.code_inputs()


def test_loaded_replay_binding_refuses_mismatch(monkeypatch):
    monkeypatch.setattr(mod.native, "_CODE", b"different loaded replay")
    with pytest.raises(ValueError, match="Loaded replay source"):
        mod.code_inputs()


@pytest.mark.parametrize("phase", ["source", "manifest"])
def test_literal_parent_path_is_rejected_before_receipt_binding(case, phase):
    root, evidence, log, before = case
    unsafe = log.parent / "alias" / ".." / log.name
    with pytest.raises(ValueError, match="resolved without aliases"):
        if phase == "source":
            mod.apply_sources(root, evidence, unsafe, apply=True)
        else:
            mod.promotion_manifest(
                before[mod.MANIFEST], b"unused", b"unused", unsafe, "a" * 64, "b" * 64, "c" * 64
            )
    assert not log.exists()
    assert all((root / p).read_bytes() == data for p, data in before.items())


@pytest.mark.usefixtures("native_runtime")
@pytest.mark.parametrize("kind", ["symlink", "file", "empty_directory", "old_journal"])
@pytest.mark.parametrize("apply_mode", [False, True])
def test_journal_preexisting_destinations_refused(case, kind, apply_mode):
    root, evidence, log, before = case
    log.parent.mkdir(exist_ok=True)
    journal = log.parent / (log.stem + "-journal")
    outside = log.parent / "unrelated"
    outside.mkdir()
    if kind == "symlink":
        journal.symlink_to(outside, target_is_directory=True)
    elif kind == "file":
        journal.write_bytes(b"unrelated")
    else:
        journal.mkdir()
        if kind == "old_journal":
            (journal / "write-old.json").write_bytes(b"unrelated")
    with pytest.raises(ValueError, match="Journal"):
        mod.apply_sources(root, evidence, log, apply=apply_mode)
    assert not log.exists() and list(outside.iterdir()) == []
    assert all((root / p).read_bytes() == b for p, b in before.items())


@pytest.mark.usefixtures("native_runtime")
@pytest.mark.parametrize(
    "where", ["reservation_leaf", "reservation_parent", "inside_write", "inside_complete"]
)
def test_journal_late_namespace_swaps_cannot_write_foreign_directory(case, monkeypatch, where):
    root, evidence, log, before = case
    log.parent.mkdir(exist_ok=True)
    journal = log.parent / (log.stem + "-journal")
    outside = log.parent.parent / "foreign"
    outside.mkdir()
    retained = log.parent.parent / "retained"
    fired = False

    def swap():
        nonlocal fired
        assert not fired
        fired = True
        path = log.parent if where == "reservation_parent" else journal
        path.rename(retained)
        path.symlink_to(outside, target_is_directory=True)

    if where.startswith("reservation"):
        reserve = mod.guarded.reserve_receipt_outputs

        @contextmanager
        def race(*args, **kwargs):
            with reserve(*args, **kwargs) as handles:
                swap()
                yield handles

        monkeypatch.setattr(mod.guarded, "reserve_receipt_outputs", race)
    else:
        write = mod.publication._write_at

        def race(fd, name, payload, *, replacing=False):
            if replacing == (where == "inside_complete"):
                swap()
            return write(fd, name, payload, replacing=replacing)

        monkeypatch.setattr(mod.publication, "_write_at", race)
    with pytest.raises(Exception, match="[Jj]ournal"):
        mod.apply_sources(root, evidence, log, apply=True)
    assert fired and list(outside.iterdir()) == []
    receipt = retained / log.name if where == "reservation_parent" else log
    saved = json.loads(receipt.read_bytes())
    assert saved["state"] == "failed" and saved["journal_directory"] == str(journal)
    if where == "inside_complete":
        assert (root / mod.OWNER).read_bytes() != before[mod.OWNER]
        assert saved["recovery_required"] is True
    else:
        assert (root / mod.OWNER).read_bytes() == before[mod.OWNER]
    if where.startswith("inside"):
        from kg_microbe_write.transaction import recover

        journals = list(retained.glob("write-*.json"))
        assert len(journals) == 1
        assert recover(journals[0]) == {str(root / mod.OWNER): before[mod.OWNER].decode()}


@pytest.mark.usefixtures("native_runtime")
@pytest.mark.parametrize("kind", ["directory_alias", "wrong_path", "payload", "extra_file"])
def test_completed_journal_is_required_and_bound(case, kind):
    root, evidence, log, _ = case
    apply(case)
    saved = json.loads(log.read_bytes())
    path = Path(saved["transaction"]["journal"])
    if kind == "directory_alias":
        moved = path.parent.with_name("retained")
        path.parent.rename(moved)
        path.parent.symlink_to(moved, target_is_directory=True)
    elif kind == "wrong_path":
        saved["transaction"]["journal"] = str(path.parent.parent / path.name)
        log.write_bytes(mod.encoded(saved))
    elif kind == "payload":
        value = json.loads(path.read_bytes())
        value["previous"] = {}
        path.write_bytes(mod.encoded(value))
        saved["journal_sha256"] = mod.digest(path.read_bytes())
        log.write_bytes(mod.encoded(saved))
    else:
        (path.parent / "unrelated.json").write_bytes(b"{}")
    with pytest.raises(ValueError, match="[Jj]ournal"):
        mod.apply_sources(root, evidence, log, apply=True)


def test_native_partial_promotion_retains_recoverable_journal(native_case, monkeypatch):
    from kg_microbe_write import transaction

    root, _, _, _, log, _, before = native_case
    replace = transaction._atomic_replace

    def fail_second(path, text):
        if path == root / mod.MANIFEST:
            raise OSError("injected second-output failure")
        return replace(path, text)

    monkeypatch.setattr(transaction, "_atomic_replace", fail_second)
    with pytest.raises(Exception, match="write failed after 1"):
        promote(native_case, True)
    saved = json.loads(log.read_bytes())
    assert saved["state"] == "failed" and saved["recovery_required"] is True
    journals = list(Path(saved["journal_directory"]).glob("write-*.json"))
    assert len(journals) == 1
    assert json.loads(journals[0].read_bytes())["status"] == "in_progress"
    assert transaction.recover(journals[0]) == {
        str(root / path): before[path].decode() for path in (mod.SSSOM, mod.MANIFEST)
    }
    assert (root / mod.SSSOM).read_bytes() != before[mod.SSSOM]
    assert (root / mod.MANIFEST).read_bytes() == before[mod.MANIFEST]


@pytest.mark.usefixtures("native_runtime")
def test_parent_acquisition_rejects_nonleaf_alias_before_directory_mutation(case, monkeypatch):
    root, evidence, old_log, before = case
    anchor = old_log.parent / "anchor"
    parent = anchor / "nested"
    parent.mkdir(parents=True)
    foreign = old_log.parent / "foreign"
    (foreign / "nested").mkdir(parents=True)
    log = parent / "source.json"
    retained = old_log.parent / "retained"
    opened = os.open
    fired = False

    def race(path, flags, *args, **kwargs):
        nonlocal fired
        if Path(path) == parent and kwargs.get("dir_fd") is None:
            assert not fired
            fired = True
            anchor.rename(retained)
            anchor.symlink_to(foreign, target_is_directory=True)
        return opened(path, flags, *args, **kwargs)

    monkeypatch.setattr(os, "open", race)
    with pytest.raises(ValueError):
        mod.apply_sources(root, evidence, log, apply=True)
    assert fired and list((foreign / "nested").iterdir()) == []
    assert list((retained / "nested").iterdir()) == []
    assert all((root / p).read_bytes() == data for p, data in before.items())


@pytest.mark.usefixtures("native_runtime")
@pytest.mark.parametrize("apply_mode", [False, True])
def test_missing_receipt_parent_never_uses_racy_pathname_mkdir(case, monkeypatch, apply_mode):
    root, evidence, old_log, before = case
    anchor = old_log.parent / "anchor"
    anchor.mkdir()
    parent = anchor / "nested"
    foreign = old_log.parent / "foreign"
    foreign.mkdir()
    retained = old_log.parent / "retained"
    mkdir = Path.mkdir
    fired = False

    def race(path, *args, **kwargs):
        nonlocal fired
        if path == parent:
            fired = True
            anchor.rename(retained)
            anchor.symlink_to(foreign, target_is_directory=True)
        return mkdir(path, *args, **kwargs)

    monkeypatch.setattr(Path, "mkdir", race)
    with pytest.raises(ValueError, match="Receipt parent must already exist"):
        mod.apply_sources(root, evidence, parent / "source.json", apply=apply_mode)
    assert not fired and list(foreign.iterdir()) == [] and not parent.exists()
    assert all((root / p).read_bytes() == data for p, data in before.items())
