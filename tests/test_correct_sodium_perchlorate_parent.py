"""Sodium-specific writer wiring and exact form/receipt/prefix regressions."""

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
    "sodium_perchlorate_parent", ROOT / "scripts/correct_sodium_perchlorate_parent.py"
)
mod = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(mod)
FROZEN = json.loads((ROOT / "tests/fixtures/issue901-sodium-mapping-before.json").read_bytes())
_SOURCE_ROWS = FROZEN["rows"]
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
    return root, evidence, tmp_path.resolve() / "receipts/source.json", before


@pytest.fixture
def native_runtime():
    pytest.importorskip("kg_microbe_write", reason="Real native publisher required")


def apply(case):
    root, evidence, log, _ = case
    return mod.apply_sources(root, evidence, log, apply=True)


def candidate_bytes(before, current):
    _, fields, pairs = mod.table(before[mod.SSSOM])
    old = {r["object_id"]: r for r, _ in pairs if r["subject_id"] == mod.SUBJECT}
    rows = []
    for obj in (mod.PARENT, mod.IDENTITY, mod.HANDLE):
        row = dict(old[mod.PARENT if obj == mod.PARENT else mod.IDENTITY])
        row.update(
            object_id=obj,
            object_label="sodium perchlorate" if obj == mod.PARENT else mod.NAME,
            predicate_id="skos:broadMatch" if obj == mod.PARENT else "skos:exactMatch",
            other="" if obj == mod.PARENT else "CAS:7791-07-3",
            mapping_date=yaml.safe_load(current)["curation_history"][-1]["timestamp"][:10],
            source=row["source"] + "|MIM:curator=claude",
            validation_method=old[mod.IDENTITY]["validation_method"] if obj == mod.IDENTITY else "",
        )
        rows.append(row)
    return tsv(fields, rows)


def test_correction_preserves_identity_chemistry_roles_and_history(record):
    original = copy.deepcopy(record)
    result = mod.corrected_record(record, timestamp=STAMP)
    assert record == original
    for key in record.keys() - {"ontology_mapping", "curation_history"}:
        assert result[key] == original[key]
    assert result["ontology_mapping"]["mapping_quality"] == "NARROW_MATCH"
    assert result["ontology_mapping"]["evidence"][:-1] == original["ontology_mapping"]["evidence"]
    event = result["curation_history"][-1]
    assert event["curator"] == "claude"
    assert event["llm_model"] == "gpt-6"
    assert event["llm_assisted"] is True
    assert event["previous_status"] == event["new_status"] == "MAPPED"
    assert mod.corrected_record(result) is None


def test_native_schema_gate_rejects_unexpected_field(record):
    record["invented_review_approval"] = True
    with pytest.raises(ValueError, match="closed-schema"):
        mod.corrected_record(record)


def test_full_preimage_exact_preservation_and_timestamp():
    before = mod.frozen_owner()
    old = yaml.safe_load(before)
    after = mod.propose_record(before, timestamp=STAMP)
    new = yaml.safe_load(after)
    for key in set(old) - {"ontology_mapping", "curation_history"}:
        assert new[key] == old[key]
    assert new["ontology_mapping"]["evidence"][:-1] == old["ontology_mapping"]["evidence"]
    assert new["curation_history"][:-1] == old["curation_history"]
    assert new["curation_history"][-1]["curator"] == "claude"
    mod.complete_owner(after)
    for value in ["2025-01-01T00:00:00+00:00", "2026-11-01T00:00:00"]:
        with pytest.raises(ValueError):
            mod.propose_record(before, timestamp=value)


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
            value["cellular_metabolic_roles"][0]["confidence"] = 0.23
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
                value["cellular_metabolic_roles"][0]["confidence"] = 0.23
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
            yaml.safe_load((root / mod.OWNER).read_bytes())["cellular_metabolic_roles"][0][
                "confidence"
            ]
            == 0.23
        )


@pytest.mark.parametrize(
    "field,value",
    [
        ("predicate_id", "skos:exactMatch"),
        ("object_label", "wrong"),
        ("other", "CAS:7791-07-3"),
        ("object_id", "CHEBI:26710"),
        ("mapping_date", "2025-01-01"),
        ("validation_method", "invented"),
        ("source", "invented"),
    ],
)
def test_projection_rejects_wrong_form_or_claim(case, field, value):
    _, _, _, before = case
    current = mod.propose_record(before[mod.OWNER], timestamp=STAMP)
    candidate = candidate_bytes(before, current)
    _, fields, pairs = mod.table(candidate)
    rows = [r for r, _ in pairs]
    rows[0][field] = value
    with pytest.raises(ValueError):
        mod.promoted_sssom(before[mod.SSSOM], tsv(fields, rows), current)


def test_projection_triplet_and_policy_successor_preserve_unrelated_bytes(case):
    root, _, source, before = case
    current = mod.propose_record(before[mod.OWNER], timestamp=STAMP)
    canonical = mod.promoted_sssom(before[mod.SSSOM], candidate_bytes(before, current), current)
    _, _, pairs = mod.table(canonical)
    assert len([r for r, _ in pairs if r["subject_id"] == mod.SUBJECT]) == 3
    assert next(
        line for r, line in mod.table(before[mod.SSSOM])[2] if r["subject_id"] == "MIM:untouched"
    ) == next(line for r, line in pairs if r["subject_id"] == "MIM:untouched")
    update = json.loads(
        mod.promotion_manifest(
            before[mod.MANIFEST], canonical, current, source, "a" * 64, "b" * 64, "c" * 64
        )
    )
    original = json.loads(before[mod.MANIFEST])
    for key in set(original) - {"artifacts", "source_owner_sha256", "form_projection_updates"}:
        assert update[key] == original[key]
    assert update["form_projection_updates"][:-1] == original["form_projection_updates"]
    assert update["artifacts"][str(mod.SIDECAR)] == mod.digest(before[mod.SIDECAR])
    assert update["form_projection_updates"][-1]["prior_manifest_sha256"] == mod.digest(
        before[mod.MANIFEST]
    )


_GEN = r"""
import importlib.util,json,sys,yaml
from pathlib import Path
producer,root,kg,bundle=map(Path,sys.argv[1:])
entry=producer/'scripts/build_mim_ingredient_sssom.py'
spec=importlib.util.spec_from_file_location('sodium_native_fixture_generation',entry)
b=importlib.util.module_from_spec(spec);sys.modules[spec.name]=b
exec(compile(entry.read_bytes(),str(entry),'exec'),b.__dict__)
records={path:yaml.safe_load(path.read_bytes()) for path in sorted((root/'data/ingredients/mapped').glob('*.yaml'))}
owners=b.build_owner_index({b._mim_curie(path.name):data for path,data in records.items()})
labels={'CHEBI:132103':'sodium perchlorate'}
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
                                "test:sodium_perchlorate",
                                "sodium perchlorate",
                                "skos:exactMatch",
                                "CHEBI:132103",
                                "sodium perchlorate",
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
    assert result["applied"] is True and result["added_rows"] == 1
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


def test_native_parent_stamp_reset_is_required(case):
    _, _, _, before = case
    current = mod.propose_record(before[mod.OWNER], timestamp=STAMP)
    candidate = candidate_bytes(before, current)
    _, fields, pairs = mod.table(candidate)
    prior = next(
        row["validation_method"]
        for row, _ in mod.table(before[mod.SSSOM])[2]
        if row["object_id"] == mod.PARENT
    )
    assert prior
    rows = [row for row, _ in pairs]
    rows[0]["validation_method"] = prior
    with pytest.raises(ValueError, match="stamp"):
        mod.promoted_sssom(before[mod.SSSOM], tsv(fields, rows), current)


def test_loaded_shared_dependency_binding_refuses_mismatch(monkeypatch):
    path = ROOT / "src/mediaingredientmech/schema/mediaingredientmech.yaml"
    monkeypatch.setitem(mod.policy._LOADED_CODE, path, b"different loaded schema")
    with pytest.raises(ValueError, match="Loaded shared dependency"):
        mod.code_inputs()


def test_loaded_replay_binding_refuses_mismatch(monkeypatch):
    monkeypatch.setattr(mod.native, "_CODE", b"different loaded replay")
    with pytest.raises(ValueError, match="Loaded replay source"):
        mod.code_inputs()


@pytest.mark.parametrize(
    "section,key,value",
    [
        (None, "identifier", "cas:7601-89-0"),
        (None, "preferred_term", "Sodium perchlorate"),
        ("ontology_mapping", "ontology_id", "SNOMED:765356005"),
        ("chemical_properties", "molecular_formula", "ClNaO4"),
        ("chemical_properties", "pubchem_cid", 522606),
        ("ontology_mapping", "mapping_quality", "EXACT_MATCH"),
        ("ontology_mapping", "mapping_quality", "NARROW_MATCH"),
    ],
)
def test_rejects_wrong_substance_or_partial_correction(record, section, key, value):
    (record if section is None else record[section])[key] = value
    with pytest.raises(ValueError):
        mod.corrected_record(record, timestamp=STAMP)


def test_preserves_real_electron_acceptor_and_ten_history_events(record):
    assert len(record["curation_history"]) == 10  # Frozen preimage, not live corpus.
    role = record["cellular_metabolic_roles"][0]
    assert role["role"] == "ELECTRON_ACCEPTOR" and role["confidence"] == 0.6
    after = yaml.safe_load(mod.propose_record(mod.frozen_owner(), timestamp=STAMP))
    assert after["cellular_metabolic_roles"] == record["cellular_metabolic_roles"]
    assert after["chemical_properties"] == record["chemical_properties"]
    assert after["curation_history"][:-1] == record["curation_history"]
    assert after["synonyms"] == []
    assert "SNOMED 765356005" in mod.VERIFICATION
    assert "does not establish global absence" in mod.VERIFICATION


@pytest.mark.parametrize("stamp", ["2030-01-02T00:00:00+00:00", "2030-01-03T00:00:00+00:00"])
def test_header_tracks_actual_history_date_and_preserves_melezitose_rows(case, stamp):
    _, _, _, before = case
    current = mod.propose_record(before[mod.OWNER], timestamp=stamp)
    after = mod.promoted_sssom(before[mod.SSSOM], candidate_bytes(before, current), current)
    assert f'# mapping_date: "{stamp[:10]}"' in after.decode()
    before_lines = {
        r["object_id"]: line
        for r, line in mod.table(before[mod.SSSOM])[2]
        if r["subject_id"] == "MIM:D-_-melezitose_Monohydrate"
    }
    after_lines = {
        r["object_id"]: line
        for r, line in mod.table(after)[2]
        if r["subject_id"] == "MIM:D-_-melezitose_Monohydrate"
    }
    assert len(before_lines) == 3 and after_lines == before_lines


def test_parent_cas_alias_and_old_stamp_clear_but_cas_comment_and_stamp_survive(native_case):
    root, bundle, _, _, _, _, before = native_case
    old = {
        r["object_id"]: r
        for r, _ in mod.table(before[mod.SSSOM])[2]
        if r["subject_id"] == mod.SUBJECT
    }
    assert old[mod.PARENT]["other"] == old[mod.IDENTITY]["other"] == "CAS:7791-07-3"
    assert old[mod.PARENT]["validation_method"]
    promoted = mod.promoted_sssom(
        before[mod.SSSOM],
        (bundle / "candidate.sssom.tsv").read_bytes(),
        (root / mod.OWNER).read_bytes(),
    )
    new = {r["object_id"]: r for r, _ in mod.table(promoted)[2] if r["subject_id"] == mod.SUBJECT}
    assert new[mod.PARENT]["other"] == new[mod.PARENT]["validation_method"] == ""
    assert new[mod.IDENTITY]["other"] == new[mod.HANDLE]["other"] == "CAS:7791-07-3"
    for key in ("comment", "validation_method"):
        assert new[mod.IDENTITY][key] == old[mod.IDENTITY][key]


@pytest.mark.parametrize("kind", ["absent", "wrong-owner", "duplicate"])
def test_policy_successor_requires_exact_prior_form_prefix(case, kind):
    _, _, source, before = case
    prior = json.loads(before[mod.MANIFEST])
    if kind == "absent":
        prior.pop("form_projection_updates")
    elif kind == "wrong-owner":
        prior["form_projection_updates"][0]["source_record"] = mod.RECORD
    else:
        prior["form_projection_updates"] *= 2
    with pytest.raises(ValueError, match="prefix"):
        mod.promotion_manifest(
            mod.encoded(prior), b"unused", b"unused", source, "a" * 64, "b" * 64, "c" * 64
        )


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


def test_future_dated_evidence_precondition_is_exact():
    with pytest.raises(ValueError, match="after captured evidence"):
        mod.propose_record(mod.frozen_owner(), timestamp="2026-11-01T22:11:57+00:00")
    mod.propose_record(mod.frozen_owner(), timestamp=STAMP)


def test_appended_evidence_attributes_the_actual_sodium_sources(record):
    proposal = mod.corrected_record(record, timestamp=STAMP)
    assert proposal["ontology_mapping"]["evidence"][-1]["source"] == (
        "MIM curation (#901); PubChem CID 516899; ChEBI:132103"
    )
