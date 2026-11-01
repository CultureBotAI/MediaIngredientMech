"""Actual guarded publication of the bounded #669 canonical projection."""
from contextlib import contextmanager
import gzip
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys

import pytest

from scripts import apply_owned_name_policy as w
from scripts import promote_owned_name_policy as p


def test_prior_only_suppression_keeps_newly_observed_origins():
    current = w.propose_sources({path: w.frozen(path) for path in w.OWNERS}, timestamp="2026-11-01T12:00:00+00:00")
    # Projection fixture is already checked against the actual producer in the
    # source suite. This test isolates the historical + fresh origin union.
    from tests.test_owned_name_policy import project
    diagnostic = [x["precuration_diagnostic_encounter"] for x in w.PLAN if x["yaml_alias_basis"]]
    item = next(x for x in w.PLAN if x["disposition"] == "SUPPRESS" and not x["yaml_alias_basis"])
    observed = {"subject_id": item["subject_id"], "token_key": item["token_key"], "token": item["token"],
        "disposition": "SUPPRESS", "owner_subject_ids": json.dumps(sorted(x["subject_id"] for x in item["credited_owners"])),
        "input_surfaces": '["kgm.synonym"]', "source_refs": '["bound-source#subject_label"]', "evidence_refs": '["new-captured-origin"]'}
    result = w.canonical_sidecar(project(current), candidate_sidecar=w.tsv(w.COLS, diagnostic + [observed]))
    row = next(x for x in w.table(result)[1] if (x["subject_id"], x["token_key"]) == (item["subject_id"], item["token_key"]))
    assert set(json.loads(row["input_surfaces"])) == {"prior_sssom", "kgm.synonym"}
    assert "new-captured-origin" in json.loads(row["evidence_refs"])
    assert any(w.CANON_SHA in x for x in json.loads(row["source_refs"]))


_GEN = r'''
import importlib.util,json,sys,yaml
from pathlib import Path
producer,root,kg,bundle=map(Path,sys.argv[1:])
entry=producer/'scripts/build_mim_ingredient_sssom.py'
spec=importlib.util.spec_from_file_location('native_fixture_generation',entry)
b=importlib.util.module_from_spec(spec);sys.modules[spec.name]=b
exec(compile(entry.read_bytes(),str(entry),'exec'),b.__dict__)
records={path:yaml.safe_load(path.read_bytes()) for path in sorted((root/'data/ingredients/mapped').glob('*.yaml'))}
owners=b.build_owner_index({b._mim_curie(path.name):data for path,data in records.items()})
labels={'CHEBI:15978':'sn-glycerol 3-phosphate','CHEBI:36218':'beta-lactose','CHEBI:17270':'glycerol 2-phosphate'}
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
'''


@pytest.fixture
def native_case(tmp_path):
    pytest.importorskip("kg_microbe_write")
    producer_env = os.environ.get("MIM_OWNED_NAME_PRODUCER_ROOT")
    if not producer_env:
        pytest.skip("Explicit merged producer path required for native publication integration")
    root = tmp_path.resolve() / "mim"
    root.mkdir()
    producer = Path(producer_env).resolve()
    for path in (*map(Path, w.OWNER_META), w.SSSOM, w.BASELINE):
        target = root / path
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(w.frozen(path))
    evidence = root / "evidence"
    shutil.copytree(w.ROOT / w.EVIDENCE, evidence)
    source_log = tmp_path.resolve() / "receipts/source.json"
    w.apply_sources(root, evidence, source_log, apply=True)
    for args in (("init", "-q"), ("add", "data", "mappings"),
                 ("-c", "user.name=Fixture", "-c", "user.email=fixture@example.invalid", "commit", "-qm", "immutable source checkpoint")):
        p.git(root, *args)
    revision = p.git(root, "rev-parse", "HEAD").decode().strip()
    bundle = tmp_path.resolve() / "candidate"
    bundle.mkdir()
    kgroot = tmp_path.resolve() / "kg"
    kg = kgroot / "mappings/kgmicrobe_unified_entity_mappings.sssom.tsv.gz"
    kg.parent.mkdir(parents=True)
    # Deliberately include rejected aliases: real producer must drop these only
    # for the phosphate source owner; the legitimate glycerol record is intact.
    fields = ["subject_id", "subject_label", "predicate_id", "object_id", "object_label", "source"]
    rows = []
    for oid, label, aliases in (("CHEBI:15978", "sn-glycerol 3-phosphate", ["Gro", "glycerolum", "glycyl alcohol"]),
                               ("CHEBI:36218", "beta-lactose", []), ("CHEBI:17270", "glycerol 2-phosphate", [])):
        for alias in [label, *aliases]:
            rows.append(dict(zip(fields, ["test:" + str(len(rows)), alias, "skos:exactMatch", oid, label, "fixture"])))
    kg.write_bytes(gzip.compress(w.tsv(fields, rows), mtime=0))
    result = subprocess.run([sys.executable, "-I", "-c", _GEN, str(producer), str(root), str(kg), str(bundle)],
                            capture_output=True, text=True)
    assert result.returncode == 0, result.stderr
    produced = json.loads(result.stdout)
    producers = p.producer_paths(producer)
    mapped = set((root / "data/ingredients/mapped").glob("*.yaml"))
    residual = producer / "workspace/reports/kg_microbe_residual_p25_categorized.json"
    assert not residual.exists(), "Fixture requires the current absent optional residual"
    declared = {path: w.digest(path.read_bytes()) for path in mapped | producers | {kg, root / w.SSSOM}}
    declared[residual] = None
    inventory = {str(path): {"sha256": sha, "bytes": path.stat().st_size} for path, sha in declared.items() if sha is not None}
    for name in ("inputs-before.json", "inputs-after.json"):
        (bundle / name).write_bytes(p.encoded(inventory))
    manifest = {"schema_version": 1, "policy_version": "owned-name-policy-v1", "external_sssom_validation": "passed",
        "source_revisions": {"claw": p.PRODUCER_REVISION, "mim": revision, "kg_microbe": "fixture-ignored-input"},
        "artifacts": [{"path": str(bundle / name), "role": role, "sha256": w.digest((bundle / name).read_bytes())}
                      for name, role in (("candidate.sssom.tsv", "sssom"), ("suppressed_aliases.tsv", "suppressed_aliases"))],
        "producer_import_snapshot": {str(path): declared[path] for path in producers},
        "mapped_record_paths": list(map(str, sorted(mapped))), "source_inputs": [{"path": str(path), "sha256": sha} for path, sha in sorted(declared.items())],
        "canonical_label_resolution": produced["labels"], "prior_stamp_sources": [str(root / w.SSSOM)], "emitted_rows": produced["rows"]}
    manifest_path = bundle / "candidate.sssom.tsv.manifest.json"
    manifest_path.write_bytes(p.encoded(manifest))
    entry_sha = declared[producer / "scripts/build_mim_ingredient_sssom.py"]
    generation = {"input_bytes_unchanged": True, "scientific_approval_added": False, "supervisor_binding": None,
        "producer_revision": p.PRODUCER_REVISION, "candidate_sha256": manifest["artifacts"][0]["sha256"],
        "sidecar_sha256": manifest["artifacts"][1]["sha256"], "native_generation_manifest_sha256": w.digest(manifest_path.read_bytes()),
        "input_manifest_sha256": w.digest((bundle / "inputs-before.json").read_bytes()),
        "executed_entry_source_sha256": entry_sha, "producer_sha256": entry_sha,
        "label_maps": {"label-input-01.json": w.digest((bundle / "label-input-01.json").read_bytes())},
        "prior_stamps": str(root / w.SSSOM), "prior_sha256": w.CANON_SHA}
    (bundle / "generation-receipt.json").write_bytes(p.encoded(generation))
    context = {key: {"path": str(path), "revision": rev, "status": ""} for key, path, rev in
               (("mim", root, revision), ("claw", producer, p.PRODUCER_REVISION), ("kg_microbe", kgroot, "fixture-ignored-input"))}
    (bundle / "repository-context.json").write_bytes(p.encoded(context))
    log = tmp_path.resolve() / "receipts/promotion.json"
    return root, bundle, producer, source_log, log, w.digest(manifest_path.read_bytes())


def run(case, apply=False):
    root, bundle, producer, source_log, log, sha = case
    return p.promote(root, bundle, producer, source_log, log, generation_manifest_sha256=sha, apply=apply)


def test_native_four_artifact_publication_and_complete_noop(native_case):
    root, _, _, source_log, log, _ = native_case
    before = {path: (root / path).read_bytes() for path in (w.SSSOM, w.BASELINE)}
    assert run(native_case)["applied"] is False and not log.exists()
    assert all((root / path).read_bytes() == raw for path, raw in before.items())
    result = run(native_case, True)
    assert result["applied"] is True
    assert len(w.table((root / w.SIDECAR).read_bytes())[1]) == 11
    assert len(w.table((root / w.BASELINE).read_bytes())[1]) == 23
    assert run(native_case, True)["changed"] is False
    assert p.verify_completed(root, log, source_log=source_log)["changed"] is False
    assert w.apply_sources(root, root / "evidence", source_log, promotion_log=log, apply=True)["changed"] is False


@pytest.mark.parametrize("kind", ["candidate", "diagnostic_sidecar", "generation_manifest", "label", "owner", "source_receipt"])
def test_native_generation_substitution_refused(native_case, kind):
    root, bundle, _, source_log, log, _ = native_case
    path = {"candidate": bundle / "candidate.sssom.tsv", "diagnostic_sidecar": bundle / "suppressed_aliases.tsv",
            "generation_manifest": bundle / "candidate.sssom.tsv.manifest.json", "label": bundle / "label-input-01.json",
            "owner": root / w.G, "source_receipt": source_log}[kind]
    path.write_bytes(path.read_bytes() + b"\n")
    if kind == "source_receipt":
        value = json.loads(path.read_bytes()); value["approval"] = "APPROVED"; path.write_bytes(p.encoded(value))
    with pytest.raises(ValueError):
        run(native_case, True)
    assert (root / w.SSSOM).read_bytes() == w.frozen(w.SSSOM) and not log.exists()


def test_rebound_candidate_requires_actual_native_replay(native_case):
    """Consistent receipt hashes cannot turn an invented row into native output."""
    root, bundle, producer, source_log, log, _ = native_case
    candidate = bundle / "candidate.sssom.tsv"
    raw = candidate.read_bytes()
    lines = raw.splitlines(keepends=True)
    for index, line in enumerate(lines):
        if line.startswith(b"MIM:L-asparagine\t"):
            columns = line.decode().rstrip("\n").split("\t")
            columns[-2] += "|invented alias"
            lines[index] = ("\t".join(columns) + "\n").encode()
            break
    else:
        raise AssertionError("Required unchanged-source fixture row absent")
    candidate.write_bytes(b"".join(lines))
    manifest_path = bundle / "candidate.sssom.tsv.manifest.json"
    manifest = json.loads(manifest_path.read_bytes())
    manifest["artifacts"][0]["sha256"] = w.digest(candidate.read_bytes())
    manifest_path.write_bytes(p.encoded(manifest))
    receipt_path = bundle / "generation-receipt.json"
    receipt = json.loads(receipt_path.read_bytes())
    receipt["candidate_sha256"] = manifest["artifacts"][0]["sha256"]
    receipt["native_generation_manifest_sha256"] = w.digest(manifest_path.read_bytes())
    receipt_path.write_bytes(p.encoded(receipt))
    with pytest.raises(ValueError, match="Exact native candidate replay differs"):
        p.promote(root, bundle, producer, source_log, log,
                  generation_manifest_sha256=w.digest(manifest_path.read_bytes()), apply=True)
    assert (root / w.SSSOM).read_bytes() == w.frozen(w.SSSOM) and not log.exists()


@pytest.mark.parametrize("kind", ["canonical", "sidecar", "manifest", "baseline", "promotion_receipt", "promotion_backup"])
def test_native_completed_promotion_refuses_substitution(native_case, kind):
    root, _, _, _, log, _ = native_case
    run(native_case, True)
    path = {"canonical": root / w.SSSOM, "sidecar": root / w.SIDECAR, "manifest": root / w.PROMOTION_MANIFEST,
            "baseline": root / w.BASELINE, "promotion_receipt": log,
            "promotion_backup": p.promotion_backups(log)[w.SSSOM]}[kind]
    path.write_bytes(path.read_bytes() + b"\n")
    if kind == "promotion_receipt":
        value = json.loads(path.read_bytes()); value["approval"] = "APPROVED"; path.write_bytes(p.encoded(value))
    with pytest.raises(ValueError):
        run(native_case, True)


@pytest.mark.parametrize("kind", ["candidate", "new_sidecar", "new_owner", "owner_alias", "receipt"])
def test_native_promotion_reserved_boundary_refuses_drift(native_case, monkeypatch, kind):
    root, bundle, _, _, log, _ = native_case
    reserve = w.guarded.reserve_receipt_outputs
    @contextmanager
    def altered(*args, **kwargs):
        with reserve(*args, **kwargs) as handles:
            if kind == "candidate":
                path = bundle / "candidate.sssom.tsv"; path.write_bytes(path.read_bytes() + b"\n")
            elif kind == "new_sidecar":
                (root / w.SIDECAR).write_text("competitor")
            elif kind == "new_owner":
                path = root / "data/ingredients/mapped/nested/new.yaml"; path.parent.mkdir(); path.write_bytes(w.frozen(w.G))
            elif kind == "owner_alias":
                (root / "data/ingredients/mapped/alias").symlink_to(root / "evidence", target_is_directory=True)
            else:
                log.unlink(); log.write_text("competing receipt")
            yield handles
    monkeypatch.setattr(w.guarded, "reserve_receipt_outputs", altered)
    with pytest.raises(Exception):
        run(native_case, True)
    assert (root / w.SSSOM).read_bytes() == w.frozen(w.SSSOM)
    assert (root / w.BASELINE).read_bytes() == w.frozen(w.BASELINE)
