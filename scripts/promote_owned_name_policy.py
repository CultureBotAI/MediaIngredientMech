"""Promote only the reviewed #669 row fields and paired provenance artifacts.

Dry-run by default. The CLI holds the native repository lock. Candidate replay
uses the merged producer in a fresh interpreter, with captured labels and no
network/provider calls; it does not replace MIM's pinned validation runtime.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from scripts import apply_owned_name_policy as source

PRODUCER_REVISION = "9bd09b2ba163212a65289b91313f98cb0937476f"
OUTPUTS = (source.SSSOM, source.BASELINE, source.SIDECAR, source.PROMOTION_MANIFEST)
_CODE = Path(__file__).read_bytes()

# A private, fresh process avoids loading the newer producer into MIM's pinned
# public kg_microbe_write module namespace. Execute recorded source, not pyc.
_REPLAY = r'''
import importlib.util,json,sys
from pathlib import Path
import yaml
producer,bundle,prior=map(Path,sys.argv[1:])
manifest=json.loads((bundle/'candidate.sssom.tsv.manifest.json').read_bytes())
entry=producer/'scripts/build_mim_ingredient_sssom.py'
spec=importlib.util.spec_from_file_location('owned_name_native_replay',entry)
b=importlib.util.module_from_spec(spec);sys.modules[spec.name]=b
exec(compile(entry.read_bytes(),str(entry),'exec'),b.__dict__)
snapshot={Path(x['path']):(None if x['sha256'] is None else Path(x['path']).read_bytes()) for x in manifest['source_inputs']}
records={Path(p):yaml.safe_load(snapshot[Path(p)]) for p in manifest['mapped_record_paths']}
owners=b.build_owner_index({b._mim_curie(p.name):r for p,r in records.items()})
kg=next(p for p in snapshot if p.name=='kgmicrobe_unified_entity_mappings.sssom.tsv.gz')
kg_sources=b.load_kgm_source_index(kg);kg_labels=b.load_kgm_labels(kg)
residual_path=producer/'workspace/reports/kg_microbe_residual_p25_categorized.json'
residual={x['source_file']:x for x in json.loads(snapshot[residual_path]).get('decisions',[])} if snapshot[residual_path] else {}
rows=[];events=[]
for path,record in records.items():
 rows.extend(b._row_from_yaml(path,residual,kg_sources,kg_labels,manifest['canonical_label_resolution'],record=record,owners=owners,suppressions=events))
final=list({(r['subject_id'],r['object_id']):r for r in rows}.values())
b.apply_replayed_stamps(final,b._load_existing_validation_method(prior))
expected=(b.HEADER_YAML.format(version=b._mapping_set_version(final))+'\t'.join(b.COLUMNS)+'\n'+''.join('\t'.join(str(r.get(c,'')) for c in b.COLUMNS)+'\n' for r in final)).encode()
if expected!=(bundle/'candidate.sssom.tsv').read_bytes(): raise ValueError('Exact native candidate replay differs')
if b.render_suppressed_aliases(events)!=(bundle/'suppressed_aliases.tsv').read_bytes(): raise ValueError('Exact native sidecar replay differs')
b._check_producer_bindings()
print(json.dumps({'kg_sources_by_target':{key:kg_sources.get(key,'') for key in ('CHEBI:15978','CHEBI:36218','CHEBI:17270')},'rows':len(final),'events':len(events)}))
'''


def git(root, *args):
    return subprocess.check_output(["git", "-C", str(root), *args])


def require(condition, message):
    if not condition:
        raise ValueError(message)


def encoded(value):
    return (json.dumps(value, indent=2, sort_keys=True, ensure_ascii=False) + "\n").encode()


def producer_paths(producer):
    paths = {producer / p for p in ("scripts/build_mim_ingredient_sssom.py",
                                    "scripts/kgm_unified_mappings.py", "plugins/lock_manager.py")}
    for package in ("kg_microbe_utils", "kg_microbe_write", "kg_microbe_fleet"):
        directory = producer / "src" / package
        for path in directory.rglob("*"):
            require(not path.is_symlink(), f"Producer directory alias: {path}")
            if path.suffix == ".py":
                paths.add(path)
    return paths


def git_blobs(root, revision, prefix):
    raw = git(root, "ls-tree", "-r", "-z", revision, "--", prefix)
    result = {}
    for entry in raw.split(b"\0"):
        if entry:
            meta, path = entry.split(b"\t", 1)
            mode, kind, blob = meta.split()
            require(mode in (b"100644", b"100755") and kind == b"blob", "Unexpected source git object type")
            result[root / path.decode()] = blob.decode()
    return result


def matches_blob(content, blob):
    return hashlib.sha1(b"blob " + str(len(content)).encode() + b"\0" + content).hexdigest() == blob


def generation_inputs(root, bundle, producer, source_log, manifest_sha256):
    """Validate exact native inputs and replay the merged source graph offline."""
    bound, source_receipt = source.source_receipt(root, source_log)
    require(source.regular(Path(__file__)) == _CODE, "Loaded promoter source changed")
    bound[Path(__file__)] = _CODE
    bundle, producer = source.checked_root(bundle), source.checked_root(producer)
    names = ("candidate.sssom.tsv", "suppressed_aliases.tsv", "candidate.sssom.tsv.manifest.json",
             "generation-receipt.json", "inputs-before.json", "inputs-after.json", "repository-context.json")
    for name in names:
        bound[bundle / name] = source.regular(bundle / name)
    manifest_path = bundle / names[2]
    require(source.digest(bound[manifest_path]) == manifest_sha256, "Native generation manifest hash changed")
    manifest = json.loads(bound[manifest_path])
    receipt = json.loads(bound[bundle / "generation-receipt.json"])
    before, after = (json.loads(bound[bundle / n]) for n in ("inputs-before.json", "inputs-after.json"))
    context = json.loads(bound[bundle / "repository-context.json"])
    require(before == after and receipt["input_bytes_unchanged"] is True,
            "Generation input inventories changed")
    require(receipt.get("scientific_approval_added") is False and receipt.get("supervisor_binding") is None,
            "Generation cannot confer scientific approval or supervisor binding")
    require(manifest.get("schema_version") == 1 and manifest.get("policy_version") == "owned-name-policy-v1"
            and manifest.get("external_sssom_validation") == "passed", "Native generation contract changed")
    require(manifest["source_revisions"]["claw"] == PRODUCER_REVISION == receipt["producer_revision"],
            "Candidate was not built by the reviewed merged producer")
    require(git(producer, "rev-parse", "HEAD").decode().strip() == PRODUCER_REVISION,
            "Producer checkout revision changed")
    require(not git(producer, "status", "--porcelain", "--untracked-files=all"), "Producer checkout is not clean")
    for key, path in (("mim", root), ("claw", producer)):
        require(context[key]["path"] == str(path) and not context[key]["status"]
                and context[key]["revision"] == manifest["source_revisions"][key],
                f"Generation did not capture a clean, bound {key} checkpoint")
    for name, field in ((names[0], "candidate_sha256"), (names[1], "sidecar_sha256"),
                        (names[2], "native_generation_manifest_sha256")):
        require(source.digest(bound[bundle / name]) == receipt[field], f"Generation receipt changed: {name}")
    require(receipt["input_manifest_sha256"] == source.digest(bound[bundle / "inputs-before.json"]),
            "Generation before-inventory receipt changed")
    expected_artifacts = [{"path": str(bundle / names[0]), "role": "sssom", "sha256": receipt["candidate_sha256"]},
                          {"path": str(bundle / names[1]), "role": "suppressed_aliases", "sha256": receipt["sidecar_sha256"]}]
    require(manifest["artifacts"] == expected_artifacts, "Native paired artifacts changed")
    producers = producer_paths(producer)
    declared_code = {Path(p): h for p, h in manifest["producer_import_snapshot"].items()}
    require(set(declared_code) == producers, "Native producer dependency path set changed")
    blobs = git_blobs(producer, PRODUCER_REVISION, "src") | git_blobs(producer, PRODUCER_REVISION, "scripts") | git_blobs(producer, PRODUCER_REVISION, "plugins")
    for path in producers:
        content = source.regular(path)
        require(path in blobs and matches_blob(content, blobs[path]) and source.digest(content) == declared_code[path],
                f"Producer bytes differ from merged commit: {path}")
        bound[path] = content
    entry = producer / "scripts/build_mim_ingredient_sssom.py"
    require(receipt["executed_entry_source_sha256"] == receipt["producer_sha256"] == declared_code[entry],
            "Executed source entrypoint binding changed")
    labels = {}
    label_paths = {bundle / name for name in receipt["label_maps"]}
    require(label_paths == set(bundle.glob("label-input-*.json")), "Label receipt path set changed")
    for path in sorted(label_paths):
        require(path.parent == bundle, "Label receipt escaped generation directory")
        bound[path] = source.regular(path)
        require(source.digest(bound[path]) == receipt["label_maps"][path.name], "Captured label map changed")
        labels.update(json.loads(bound[path])["labels"])
    require(labels == manifest["canonical_label_resolution"], "Native resolved labels differ from captured responses")
    mapped = {p for p in source.ingredient_paths(root) if p.parent == root / "data/ingredients/mapped"}
    require(list(map(str, sorted(mapped))) == manifest["mapped_record_paths"], "Mapped generation path set changed")
    checkpoint = git_blobs(root, manifest["source_revisions"]["mim"], "data/ingredients/mapped")
    require(set(checkpoint) == mapped, "Generation checkpoint owner membership differs")
    for path in mapped:
        require(matches_blob(bound[path], checkpoint[path]), f"Generation owner differs from clean checkpoint: {path}")
    declared = {Path(x["path"]): x["sha256"] for x in manifest["source_inputs"]}
    require(len(declared) == len(manifest["source_inputs"]), "Duplicate generation source input")
    kgroot = source.checked_root(Path(context["kg_microbe"]["path"]))
    kg = kgroot / "mappings/kgmicrobe_unified_entity_mappings.sssom.tsv.gz"
    residual = producer / "workspace/reports/kg_microbe_residual_p25_categorized.json"
    prior = source.backups(source_log)[source.SSSOM]
    require(manifest["prior_stamp_sources"] == [receipt["prior_stamps"]]
            and Path(receipt["prior_stamps"]) in (root / source.SSSOM, prior)
            and receipt["prior_sha256"] == source.CANON_SHA, "Prior-stamp input changed")
    expected_paths = mapped | producers | {kg, residual, root / source.SSSOM, Path(receipt["prior_stamps"])}
    require(set(declared) == expected_paths, "Native input inventory path set changed")
    absent = set()
    for path, expected in declared.items():
        if path == root / source.SSSOM:
            content = source.frozen(source.SSSOM)  # completed promotion retains this exact backup
        elif expected is None:
            require(not path.exists() and not path.is_symlink(), f"Absent native input appeared: {path}")
            absent.add(path)
            continue
        else:
            content = source.regular(path)
            bound[path] = content
        require(source.digest(content) == expected, f"Native input changed: {path}")
        if path not in producers:  # harness binds all data inputs; its code list is smaller
            require(str(path) in before and before[str(path)] == {"sha256": expected, "bytes": len(content)},
                    f"Harness input receipt differs: {path}")
    require(manifest["source_revisions"]["kg_microbe"] == context["kg_microbe"]["revision"],
            "KG revision receipt changed")
    replay = subprocess.run([sys.executable, "-I", "-c", _REPLAY, str(producer), str(bundle), str(prior)],
                            capture_output=True, text=True, check=False)
    require(replay.returncode == 0, "Native offline replay failed: " + replay.stderr[-4000:])
    result = json.loads(replay.stdout)
    require(result["rows"] == manifest["emitted_rows"], "Native replay row count differs")
    return bound, source_receipt, result, producers, label_paths, absent


def promotion_backups(log):
    return {p: log.with_name(log.stem + ".before-" + p.name) for p in (source.SSSOM, source.BASELINE)}


def promote(root, bundle, producer, source_log, log, *, generation_manifest_sha256, apply=False):
    root = source.checked_root(root)
    bundle, producer = Path(bundle).absolute(), Path(producer).absolute()
    source_log, log = Path(source_log).absolute(), Path(log).absolute()
    inputs, receipt, replay, producers, labels, absent = generation_inputs(
        root, bundle, producer, source_log, generation_manifest_sha256)
    current = {p: inputs[root / p] for p in source.OWNERS}
    kg_sources = {k: ["kgm:" + token for token in v.split("|") if token]
                  for k, v in replay["kg_sources_by_target"].items()}
    canonical = source.promoted_sssom(source.frozen(source.SSSOM), inputs[bundle / "candidate.sssom.tsv"],
                                      current, kg_sources_by_target=kg_sources)
    sidecar = source.canonical_sidecar(canonical, candidate_sidecar=inputs[bundle / "suppressed_aliases.tsv"])
    baseline = source.retired_baseline(source.frozen(source.BASELINE))
    ingredient_paths = source.ingredient_paths(root)
    scope_manifest = {"schema_version": 1, "policy_version": "owned-name-policy-v1",
        "scope": "bounded canonical migration; deferred baseline obligations remain unresolved",
        "approval": source.APPROVAL, "producer_revision": PRODUCER_REVISION,
        "generation_manifest_sha256": generation_manifest_sha256,
        "generation_receipt_sha256": source.digest(inputs[bundle / "generation-receipt.json"]),
        "source_receipt_sha256": source.digest(inputs[source_log]),
        "source_owner_sha256": {str(p.relative_to(root)): source.digest(inputs[p])
                                 for p in sorted(inputs) if p in ingredient_paths},
        "artifacts": {str(p): source.digest(b) for p, b in
                      ((source.SSSOM, canonical), (source.SIDECAR, sidecar), (source.BASELINE, baseline))},
        "decisions": source.PLAN, "policy_evidence": source.POLICY,
        "sssom_before_sha256": source.CANON_SHA, "baseline_before_sha256": source.BASELINE_SHA}
    outputs = {source.SSSOM: canonical, source.BASELINE: baseline,
               source.SIDECAR: sidecar, source.PROMOTION_MANIFEST: encoded(scope_manifest)}
    result = {"phase": "promote", "approval": source.APPROVAL, "records": receipt["records"],
        "bundle": str(bundle), "producer": str(producer), "source_log": str(source_log),
        "generation_manifest_sha256": generation_manifest_sha256,
        "source_receipt_sha256": source.digest(inputs[source_log]),
        "input_sha256": {str(p): source.digest(b) for p, b in inputs.items()
                         if p not in {root / source.SSSOM, root / source.BASELINE}},
        "output_sha256": {str(p): source.digest(b) for p, b in outputs.items()},
        "sssom_before_sha256": source.CANON_SHA, "baseline_before_sha256": source.BASELINE_SHA,
        "sssom_after_sha256": source.digest(canonical), "baseline_after_sha256": source.digest(baseline),
        "native_replay": replay}
    actual = {p: source.regular(root / p) if (root / p).exists() else None for p in OUTPUTS}
    paths = source.ingredient_paths(root)

    def check():
        source.validate_scope(root, inputs, paths)
        require(producer_paths(producer) == producers, "Producer dependency path set changed")
        require(set(bundle.glob("label-input-*.json")) == labels, "Label receipt path set changed")
        for path in absent:
            require(not path.exists() and not path.is_symlink(), "Absent native input appeared")
        for path, old in actual.items():
            target = root / path
            if old is None:
                require(not target.exists() and not target.is_symlink(), "Promotion output appeared")
            else:
                require(source.regular(target) == old, "Promotion output changed")

    check()
    if actual == outputs:
        source.completed_receipt(log, result, root, changed={source.SSSOM, source.BASELINE},
                                 created={source.SIDECAR, source.PROMOTION_MANIFEST})
        for path, backup in promotion_backups(log).items():
            require(source.regular(backup) == source.frozen(path), "Promotion beforeimage changed")
        return {"applied": False, "changed": False, "approval": source.APPROVAL}
    require(actual == {source.SSSOM: source.frozen(source.SSSOM), source.BASELINE: source.frozen(source.BASELINE),
                       source.SIDECAR: None, source.PROMOTION_MANIFEST: None},
            "Canonical promotion is partial or changed")
    return source.guarded.publish(root, outputs, inputs, log,
        {p: source.frozen(path) for path, p in promotion_backups(log).items()}, result,
        apply=apply, validate_scope=check)


def verify_completed(root, promotion_log, *, source_log):
    receipt = json.loads(source.regular(promotion_log))
    require(receipt.get("phase") == "promote" and receipt.get("state") == "complete"
            and receipt.get("applied") is True and receipt.get("source_log") == str(Path(source_log).absolute()),
            "A completed, bound promotion receipt is required")
    result = promote(root, Path(receipt["bundle"]), Path(receipt["producer"]), source_log, promotion_log,
                     generation_manifest_sha256=receipt["generation_manifest_sha256"])
    require(result.get("changed") is False, "Promotion receipt does not bind completed outputs")
    return result


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=ROOT)
    for name in ("bundle", "producer", "source-log", "log"):
        parser.add_argument("--" + name, type=Path, required=True)
    parser.add_argument("--generation-manifest-sha256", required=True)
    modes = parser.add_mutually_exclusive_group()
    modes.add_argument("--apply", action="store_true")
    modes.add_argument("--dry-run", action="store_true")
    args = parser.parse_args(argv)
    from plugins.lock_manager import LockManager
    from plugins.repository_settings import RepositorySettings
    root = source.checked_root(args.root)
    target = RepositorySettings.from_environment().get_target("mediaingredientmech")
    require(target.path.resolve() == root, "Configured MIM root differs from requested worktree")
    target.open()
    with LockManager().lock("mediaingredientmech", "#669 bounded canonical promotion"):
        result = promote(root, args.bundle, args.producer, args.source_log, args.log,
                         generation_manifest_sha256=args.generation_manifest_sha256, apply=args.apply)
    print(json.dumps(result, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
