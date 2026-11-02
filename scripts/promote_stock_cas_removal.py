#!/usr/bin/env python3
"""Capture completed #871/#268 source evidence and promote one native stock CAS delta.

Dry-run by default. CLI owns the native lock; direct callers must hold it.
Historical source verification substitutes exactly two pinned anchors and only
becomes a postpromotion proof after full native replay and journal verification.
"""

from __future__ import annotations

import argparse
import csv
import json
import os
import stat
import subprocess
import sys
from contextlib import contextmanager
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(ROOT / "src"))
from scripts import correct_hydrate_stock_chemistry_871_268 as source  # noqa: E402
from scripts import promote_owned_name_policy as native  # noqa: E402
from scripts.bump_sssom_header import newest_row_date, rewrite  # noqa: E402

policy, guarded, publication = source.shared, source.guarded, source.publication
regular, require, digest, encoded = policy.regular, source.require, guarded.digest, native.encoded
checked_root, ingredient_paths, bound_path = (
    policy.checked_root,
    policy.ingredient_paths,
    source.bound_path,
)
OWNER = Path("data/ingredients/mapped/02_Thiamine_Pyrophosphate.yaml")
RECORD = str(OWNER)
SUBJECT = "MIM:02_Thiamine_Pyrophosphate"
IDENTITY = "kgmicrobe.ingredient:0_2_thiamine_pyrophosphate"
CAS_TOKEN = "CAS:154-87-0"
OLD_STAMP = "OAK+OLS:chebi|SYNONYM_ENRICH|2026-07-07"
STAMP_BASIS = (
    "Explicit canonical reset, not native blank emission: commit "
    "14f7ab71204d1307a0ffaccaf3c614eabfd0d990 (#351) changed CHEBI:9532 "
    "to the stock registry identity while carrying the old ChEBI synonym stamp. "
    "That old-object verdict does not validate this stock. Preserve six "
    "unresolved aliases and WITHHOLD; no scientific approval."
)
SSSOM = Path("mappings/ingredient_mappings.sssom.tsv")
MANIFEST = Path("mappings/ingredient_mappings.sssom.tsv.manifest.json")
BASELINE, SIDECAR = policy.BASELINE, policy.SIDECAR
OUTPUTS = (SSSOM, MANIFEST)
BEFORE = {p: source.META["protected_anchors"][str(p)] for p in source.ANCHORS}
PRODUCER = "33be66ab1b993e2a47792c13daa3e4f39635f2cb"
HISTORICAL_OWNER = "7eece9fb547e213646a2313b9f9bb8f5988f0d13e08d53b2255a33b43f8a659f"
APPROVAL = source.APPROVAL
_CODE = Path(__file__).read_bytes()
# Preserve the donor replay algorithm, but explicitly supply the old root anchor
# after promotion instead of reading the new canonical bytes into that snapshot.
_REPLAY = native._REPLAY.replace(
    "producer,bundle,prior=map(Path,sys.argv[1:])",
    "producer,bundle,prior,root=map(Path,sys.argv[1:])",
).replace(
    "records={Path(p):",
    "snapshot[root/'mappings/ingredient_mappings.sssom.tsv']=prior.read_bytes()\nrecords={Path(p):",
)


def code_inputs():
    require(regular(Path(__file__)) == _CODE, "Loaded promoter changed")
    require(regular(Path(native.__file__)) == native._CODE, "Loaded replay dependency changed")
    result = {Path(__file__): _CODE, Path(native.__file__): native._CODE}
    for p, data in source._LOADED_CODE.items():
        require(regular(p) == data, "Loaded source dependency changed")
        result[p] = data
    return result


def capture_anchors(proof):
    proof = bound_path(proof)
    return {p: proof.with_name(proof.stem + ".before-" + p.name) for p in OUTPUTS}


@contextmanager
def reserve_capture(proof):
    """Reserve all three proof outputs relative to one held, verified parent FD."""
    proof = bound_path(proof)
    parent = proof.parent
    intended = parent.lstat()
    require(stat.S_ISDIR(intended.st_mode), "Proof parent must already exist")
    identity = publication._identity(intended)
    fd = os.open(parent, os.O_RDONLY | os.O_DIRECTORY | os.O_NOFOLLOW)
    files = {}
    handed_over = False

    def check():
        require(
            parent == parent.resolve() and publication._identity(parent.lstat()) == identity,
            "Proof parent changed",
        )
        for path, handle in files.items():
            info = path.lstat()
            require(
                path == path.resolve()
                and stat.S_ISREG(info.st_mode)
                and info.st_nlink == 1
                and publication._identity(info) == publication._identity(os.fstat(handle)),
                "Reserved proof output changed",
            )

    try:
        require(
            publication._identity(os.fstat(fd)) == identity,
            "Proof parent changed during acquisition",
        )
        check()
        for path in (proof, *capture_anchors(proof).values()):
            check()
            files[path] = os.open(
                path.name, os.O_WRONLY | os.O_CREAT | os.O_EXCL | os.O_NOFOLLOW, 0o600, dir_fd=fd
            )
            check()
        handed_over = True
        yield files, check
    finally:
        if not handed_over:
            for path, handle in files.items():
                try:
                    info = os.stat(path.name, dir_fd=fd, follow_symlinks=False)
                    if publication._identity(info) == publication._identity(os.fstat(handle)):
                        os.unlink(path.name, dir_fd=fd)
                except FileNotFoundError:
                    pass
        for handle in files.values():
            os.close(handle)
        os.close(fd)


def write_fd(handle, data):
    view = memoryview(data)
    while view:
        written = os.write(handle, view)
        require(written > 0, "Proof write made no progress")
        view = view[written:]
    os.fsync(handle)


def capture_sources(root, source_log, proof, *, apply=False):
    root, source_log, proof = checked_root(root), bound_path(source_log), bound_path(proof)
    inputs, result = source.source_receipt(root, source_log)
    inputs.update(code_inputs())
    paths = ingredient_paths(root)
    anchors = capture_anchors(proof)
    require(proof.parent.is_dir(), "Proof parent must already exist")
    require(
        not any(os.path.lexists(p) for p in (proof, *anchors.values())),
        "Proof output already exists",
    )
    doc = {
        "schema_version": 1,
        "kind": "stock-cas-completed-source-capture",
        "approval": APPROVAL,
        "root": str(root),
        "source_log": str(source_log),
        "source_result": result,
        "source_receipt_sha256": digest(inputs[source_log]),
        "input_sha256": {str(p): digest(b) for p, b in inputs.items()},
        "anchors": {str(p): {"path": str(anchors[p]), "sha256": BEFORE[p]} for p in OUTPUTS},
        "state": "complete",
    }
    policy.validate_scope(root, inputs, paths)
    if not apply:
        return {"applied": False, "approval": APPROVAL, "capture": doc}
    with reserve_capture(proof) as (handles, check):
        check()
        policy.validate_scope(root, inputs, paths)
        for p, destination in anchors.items():
            write_fd(handles[destination], inputs[root / p])
            check()
        policy.validate_scope(root, inputs, paths)
        write_fd(handles[proof], encoded(doc))
        check()
        policy.validate_scope(root, inputs, paths)
    return {"applied": True, "approval": APPROVAL, "proof_sha256": digest(regular(proof))}


def _captured_sources(root, source_log, proof):
    """Internal historical reconstruction; NOT a completed canonical transition proof."""
    root, source_log, proof = checked_root(root), bound_path(source_log), bound_path(proof)
    proof_raw = regular(proof)
    doc = json.loads(proof_raw)
    require(
        proof_raw == encoded(doc)
        and set(doc)
        == {
            "schema_version",
            "kind",
            "approval",
            "root",
            "source_log",
            "source_result",
            "source_receipt_sha256",
            "input_sha256",
            "anchors",
            "state",
        },
        "Completed source capture bytes/fields differ",
    )
    require(
        doc.get("schema_version") == 1
        and doc.get("kind") == "stock-cas-completed-source-capture"
        and doc.get("state") == "complete"
        and doc.get("root") == str(root)
        and doc.get("source_log") == str(source_log)
        and doc.get("approval") == APPROVAL,
        "Completed source capture contract differs",
    )
    anchors = capture_anchors(proof)
    require(
        doc["anchors"] == {str(p): {"path": str(anchors[p]), "sha256": BEFORE[p]} for p in OUTPUTS},
        "Historical anchor substitutions differ",
    )
    old = {p: regular(path) for p, path in anchors.items()}
    require(
        all(digest(b) == BEFORE[p] for p, b in old.items()), "Captured historical anchor differs"
    )
    current = {p: regular(root / p) for p in source.OWNERS}
    timestamp = source.verify_complete(current)
    paths = ingredient_paths(root)
    require({root / p for p in source.OWNERS} <= paths, "Missing corrected owner")
    inputs = {p: regular(p) for p in paths}
    inputs.update(source.evidence_inputs(root))
    inputs.update(source.native_code_inputs())
    for p, expected in source._LOADED_CODE.items():
        require(regular(p) == expected, "Loaded source dependency changed")
        inputs[p] = expected
    for p in source.ANCHORS:
        data = old[p] if p in OUTPUTS else regular(root / p)
        require(digest(data) == BEFORE[p], "Protected historical source anchor changed")
        inputs[root / p] = data
    historical = inputs | {root / p: source.frozen(p) for p in source.OWNERS}
    result = {
        "phase": "sources",
        "approval": APPROVAL,
        "timestamp": timestamp,
        "evidence_manifest": str(root / source.MANIFEST),
        "evidence_manifest_sha256": source.MANIFEST_SHA,
        "input_sha256": {str(p): digest(b) for p, b in historical.items()},
        "output_sha256": {str(p): digest(b) for p, b in current.items()},
        "records": [
            {
                "source_record": str(p),
                "shape": source.META["owners"][str(p)]["shape"],
                "before_yaml_sha256": source.META["owners"][str(p)]["sha256"],
                "after_yaml_sha256": digest(current[p]),
                "change": source.change_text(p),
                "verification": (
                    "Exact reviewed owner preimage and primary chemistry evidence bound by "
                    f"{source.MANIFEST}@sha256={source.MANIFEST_SHA}; only the explicit delete/set matrix "
                    "and one history event are applied. " + APPROVAL
                ),
            }
            for p in source.OWNERS
        ],
    }
    require(
        doc["source_result"] == result,
        "Captured source result differs from exact frozen writer contract",
    )
    inputs[source_log] = policy.completed_receipt(
        source_log, result, root, changed=set(source.OWNERS)
    )
    require(
        digest(inputs[source_log]) == doc["source_receipt_sha256"],
        "Captured source receipt changed",
    )
    for p, backup in source.backups(source_log).items():
        inputs[backup] = regular(backup)
        require(inputs[backup] == source.frozen(p), "Source backup changed")
    inputs.update(
        publication.completed_journal(
            root,
            source_log,
            json.loads(inputs[source_log]),
            previous={p: source.frozen(p) for p in source.OWNERS},
        )
    )
    inputs.update(code_inputs())
    require(
        doc["input_sha256"] == {str(p): digest(b) for p, b in inputs.items()},
        "Completed source capture input inventory differs",
    )
    # Historical identities are retained in the proof above. Current-scope checks
    # use actual current bytes; promote must prove BOTH exact output transitions.
    inputs.update({root / p: regular(root / p) for p in OUTPUTS})
    inputs.update({anchors[p]: b for p, b in old.items()})
    inputs[proof] = proof_raw
    policy.validate_scope(root, inputs, paths)
    return inputs, result, old


def table(data):
    lines = data.decode().splitlines(keepends=True)
    start = next(i for i, line in enumerate(lines) if not line.startswith("#"))
    fields = next(csv.reader([lines[start]], delimiter="\t"))
    rows = list(csv.DictReader(lines[start:], delimiter="\t"))
    require(
        len(rows) == len(lines[start + 1 :])
        and all(None not in r and None not in r.values() for r in rows),
        "Malformed SSSOM rows",
    )
    return lines[: start + 1], fields, list(zip(rows, lines[start + 1 :], strict=True))


def promoted_sssom(before, candidate, current):
    source.verify_complete(current)
    header, fields, prior = table(before)
    _, candidate_fields, generated = table(candidate)
    require(fields == candidate_fields, "Candidate columns differ")
    old = [r for r, _ in prior if r["subject_id"] == SUBJECT]
    target = [(r, line) for r, line in generated if r["subject_id"] == SUBJECT]
    require(len(old) == len(target) == 1, "Exactly one old and candidate stock row required")
    row, line = target[0]
    old = old[0]
    tokens = old["other"].split("|")
    require(len(tokens) == 7 and tokens.count(CAS_TOKEN) == 1, "Prior stock aliases differ")
    record = yaml.safe_load(current[OWNER])
    history = record["curation_history"][-1]
    expected_source = "|".join(
        ["MIM:" + e["source"] for e in record["ontology_mapping"]["evidence"] if e.get("source")]
        + ["MIM:curator=" + history["curator"]]
    )
    expected = dict(
        old,
        other="|".join(t for t in tokens if t != CAS_TOKEN),
        source=expected_source,
        mapping_date=history["timestamp"][:10],
        validation_method=OLD_STAMP,
    )
    require(
        old["validation_method"] == OLD_STAMP
        and old["object_id"] == IDENTITY
        and old["predicate_id"] == "skos:exactMatch"
        and row == expected,
        "Candidate stock row exceeds exact CAS/provenance scope",
    )
    projected = dict(row, validation_method="")
    line = "\t".join(projected[k] for k in fields) + "\n"
    output = "".join(header) + "".join(
        line if r["subject_id"] == SUBJECT else raw for r, raw in prior
    )
    lines = output.splitlines(keepends=True)
    date = newest_row_date(lines)
    require(date is not None, "Projected mapping date absent")
    return "".join(rewrite(lines, date)[0]).encode()


def generation_inputs(
    root: Path, bundle: Path, producer: Path, source_log: Path, proof: Path, manifest_sha256: str
):
    """Bind merged producer bytes and exact offline replay, with no ontology calls."""
    bound, saved, old = _captured_sources(root, source_log, proof)
    bundle, producer = checked_root(bundle), checked_root(producer)
    names = (
        "candidate.sssom.tsv",
        "suppressed_aliases.tsv",
        "candidate.sssom.tsv.manifest.json",
        "generation-receipt.json",
        "inputs-before.json",
        "inputs-after.json",
        "repository-context.json",
    )
    for name in names:
        bound[bundle / name] = regular(bundle / name)
    manifest = json.loads(bound[bundle / names[2]])
    receipt = json.loads(bound[bundle / "generation-receipt.json"])
    before, after = (
        json.loads(bound[bundle / n]) for n in ("inputs-before.json", "inputs-after.json")
    )
    context = json.loads(bound[bundle / "repository-context.json"])
    require(digest(bound[bundle / names[2]]) == manifest_sha256, "Candidate manifest hash differs")
    require(
        bound[bundle / "inputs-before.json"] == bound[bundle / "inputs-after.json"]
        and before == after
        and receipt["input_bytes_unchanged"] is True,
        "Generation input inventories differ",
    )
    require(
        receipt.get("scientific_approval_added") is False
        and receipt.get("supervisor_binding") is None,
        "Generation cannot confer approval",
    )
    require(
        manifest.get("schema_version") == 1
        and manifest.get("policy_version") == "owned-name-policy-v1"
        and manifest.get("external_sssom_validation") == "passed",
        "Native generation contract differs",
    )
    require(
        manifest["source_revisions"]["claw"] == PRODUCER == receipt["producer_revision"],
        "Wrong producer revision",
    )
    require(
        native.git(producer, "rev-parse", "HEAD").decode().strip() == PRODUCER
        and not native.git(producer, "status", "--porcelain", "--untracked-files=all"),
        "Producer is not clean and pinned",
    )
    for key, path in (("mim", root), ("claw", producer)):
        require(
            context[key]["path"] == str(path)
            and not context[key]["status"]
            and context[key]["revision"] == manifest["source_revisions"][key],
            "Generation checkpoint differs",
        )
    for name, field in (
        (names[0], "candidate_sha256"),
        (names[1], "sidecar_sha256"),
        (names[2], "native_generation_manifest_sha256"),
    ):
        require(
            digest(bound[bundle / name]) == receipt[field], "Generation artifact receipt differs"
        )
    require(
        receipt["input_manifest_sha256"] == digest(bound[bundle / "inputs-before.json"]),
        "Generation input receipt differs",
    )
    require(
        manifest["artifacts"]
        == [
            {
                "path": str(bundle / names[0]),
                "role": "sssom",
                "sha256": receipt["candidate_sha256"],
            },
            {
                "path": str(bundle / names[1]),
                "role": "suppressed_aliases",
                "sha256": receipt["sidecar_sha256"],
            },
        ],
        "Candidate pair differs",
    )
    producers = native.producer_paths(producer)
    code = {Path(p): value for p, value in manifest["producer_import_snapshot"].items()}
    require(set(code) == producers, "Producer dependency membership changed")
    blobs = {}
    for prefix in ("src", "scripts", "plugins"):
        blobs.update(native.git_blobs(producer, PRODUCER, prefix))
    for path in producers:
        data = regular(path)
        require(
            path in blobs and native.matches_blob(data, blobs[path]) and digest(data) == code[path],
            "Producer source changed",
        )
        bound[path] = data
    entry = producer / "scripts/build_mim_ingredient_sssom.py"
    require(
        receipt["executed_entry_source_sha256"] == receipt["producer_sha256"] == code[entry],
        "Executed entrypoint changed",
    )
    label_paths = {bundle / name for name in receipt["label_maps"]}
    require(
        label_paths == set(bundle.glob("label-input-*.json")), "Label receipt membership changed"
    )
    labels = {}
    for path in sorted(label_paths):
        require(path.parent == bundle, "Unsafe label receipt")
        bound[path] = regular(path)
        require(digest(bound[path]) == receipt["label_maps"][path.name], "Label capture changed")
        labels.update(json.loads(bound[path])["labels"])
    require(
        labels == manifest["canonical_label_resolution"],
        "Resolved labels differ from captured maps",
    )
    mapped = {
        path for path in ingredient_paths(root) if path.parent == root / "data/ingredients/mapped"
    }
    require(
        list(map(str, sorted(mapped))) == manifest["mapped_record_paths"],
        "Mapped input membership changed",
    )
    checkpoint = native.git_blobs(
        root, manifest["source_revisions"]["mim"], "data/ingredients/mapped"
    )
    require(set(checkpoint) == mapped, "Generation checkpoint owner membership differs")
    for path in mapped:
        require(
            native.matches_blob(bound[path], checkpoint[path]),
            "Generation owner differs from checkpoint",
        )
    declared = {Path(item["path"]): item["sha256"] for item in manifest["source_inputs"]}
    require(len(declared) == len(manifest["source_inputs"]), "Duplicate declared generation input")
    kgroot = checked_root(Path(context["kg_microbe"]["path"]))
    kg = kgroot / "mappings/kgmicrobe_unified_entity_mappings.sssom.tsv.gz"
    residual = producer / "workspace/reports/kg_microbe_residual_p25_categorized.json"
    prior = capture_anchors(proof)[SSSOM]
    require(
        manifest["prior_stamp_sources"] == [receipt["prior_stamps"]]
        and Path(receipt["prior_stamps"]) in {root / SSSOM, prior}
        and receipt["prior_sha256"] == BEFORE[SSSOM],
        "Prior-stamp source differs",
    )
    require(
        set(declared)
        == mapped | producers | {kg, residual, root / SSSOM, Path(receipt["prior_stamps"])},
        "Native input inventory differs",
    )
    absent = set()
    for path, expected in declared.items():
        if path == root / SSSOM:
            content = bound[prior]
        elif expected is None:
            require(not path.exists() and not path.is_symlink(), "Declared absent input appeared")
            absent.add(path)
            continue
        else:
            content = regular(path)
            bound[path] = content
        require(digest(content) == expected, "Native input bytes changed")
        if path not in producers:
            require(
                before[str(path)] == {"sha256": expected, "bytes": len(content)},
                "Harness input binding differs",
            )
    require(
        manifest["source_revisions"]["kg_microbe"] == context["kg_microbe"]["revision"],
        "KG revision receipt differs",
    )
    replay = subprocess.run(
        [sys.executable, "-I", "-c", _REPLAY, str(producer), str(bundle), str(prior), str(root)],
        capture_output=True,
        text=True,
        check=False,
    )
    require(replay.returncode == 0, "Exact native replay failed: " + replay.stderr[-4000:])
    result = json.loads(replay.stdout)
    require(result["rows"] == manifest["emitted_rows"], "Native replay row count differs")
    return bound, saved, old, result, producers, label_paths, absent


def promotion_manifest(
    before,
    canonical,
    current,
    source_log,
    *,
    generation_manifest_sha256,
    generation_receipt_sha256,
    source_receipt_sha256,
):
    source_log = bound_path(source_log)
    require(digest(before) == BEFORE[MANIFEST], "Prior policy manifest preimage differs")
    source.verify_complete(current)
    doc = json.loads(before)
    require(
        doc.get("schema_version") == 1 and doc.get("policy_version") == "owned-name-policy-v1",
        "Prior policy manifest contract differs",
    )
    require(
        doc["artifacts"] == {str(p): BEFORE[p] for p in (SSSOM, SIDECAR, BASELINE)}
        and doc["source_owner_sha256"][RECORD] == HISTORICAL_OWNER,
        "Prior policy artifact/historical owner binding differs",
    )
    require("stock_cas_removal_updates" not in doc, "Unexpected prior stock CAS update")
    doc["artifacts"][str(SSSOM)] = digest(canonical)
    doc["source_owner_sha256"][RECORD] = digest(current[OWNER])
    doc["stock_cas_removal_updates"] = [
        {
            "issue": 268,
            "scope": "Only the stock's mis-scoped CAS display assertion and explicitly reviewed provenance; fourteen chemistry-only historical owner pins, all other rows, policy decisions, form updates and registry history remain exact. No alias, mapping or role approval. "
            + STAMP_BASIS,
            "approval": APPROVAL,
            "prior_manifest_sha256": digest(before),
            "source_record": RECORD,
            "historical_owner_sha256": HISTORICAL_OWNER,
            "owner_before_sha256": source.META["owners"][RECORD]["sha256"],
            "owner_after_sha256": digest(current[OWNER]),
            "source_receipt": str(source_log),
            "source_receipt_sha256": source_receipt_sha256,
            "generation_manifest_sha256": generation_manifest_sha256,
            "generation_receipt_sha256": generation_receipt_sha256,
            "sssom_before_sha256": BEFORE[SSSOM],
            "sssom_after_sha256": digest(canonical),
            "sidecar_sha256": BEFORE[SIDECAR],
            "baseline_sha256": BEFORE[BASELINE],
        }
    ]
    return encoded(doc)


def promotion_backups(log):
    return {p: log.with_name(log.stem + ".before-" + p.name) for p in OUTPUTS}


def promote(
    root,
    bundle,
    producer,
    source_log,
    proof,
    log,
    *,
    generation_manifest_sha256,
    apply=False,
    _completed_inputs=False,
):
    root, bundle, producer = checked_root(root), checked_root(bundle), checked_root(producer)
    source_log, proof, log = bound_path(source_log), bound_path(proof), bound_path(log)
    inputs, saved, old, replay, producers, labels, absent = generation_inputs(
        root, bundle, producer, source_log, proof, generation_manifest_sha256
    )
    current = {p: inputs[root / p] for p in source.OWNERS}
    canonical = promoted_sssom(old[SSSOM], inputs[bundle / "candidate.sssom.tsv"], current)
    projection = promotion_manifest(
        old[MANIFEST],
        canonical,
        current,
        source_log,
        generation_manifest_sha256=generation_manifest_sha256,
        generation_receipt_sha256=digest(inputs[bundle / "generation-receipt.json"]),
        source_receipt_sha256=digest(inputs[source_log]),
    )
    outputs = {SSSOM: canonical, MANIFEST: projection}
    actual = {p: regular(root / p) for p in OUTPUTS}
    inputs.update({root / p: b for p, b in actual.items()})
    paths = ingredient_paths(root)
    result = {
        "phase": "promote-stock-cas",
        "approval": APPROVAL,
        "records": saved["records"],
        "source_log": str(source_log),
        "source_proof": str(proof),
        "bundle": str(bundle),
        "producer": str(producer),
        "generation_manifest_sha256": generation_manifest_sha256,
        "source_receipt_sha256": digest(inputs[source_log]),
        "source_proof_sha256": digest(inputs[proof]),
        "input_sha256": {
            str(p): digest(b) for p, b in inputs.items() if p not in {root / p for p in OUTPUTS}
        },
        "output_sha256": {str(p): digest(b) for p, b in outputs.items()},
        "sssom_before_sha256": BEFORE[SSSOM],
        "sssom_after_sha256": digest(canonical),
        "validation_stamp_override": {
            "native_candidate": OLD_STAMP,
            "canonical": "",
            "basis": STAMP_BASIS,
        },
        "native_replay": replay,
        "changed_subjects": [SUBJECT],
        "added_rows": 0,
        "removed_rows": 0,
    }

    def check():
        policy.validate_scope(root, inputs, paths)
        require(
            native.producer_paths(producer) == producers, "Producer dependency membership changed"
        )
        require(
            set(bundle.glob("label-input-*.json")) == labels, "Label receipt membership changed"
        )
        require(
            all(not p.exists() and not p.is_symlink() for p in absent),
            "Absent generation input appeared",
        )

    check()
    backups = promotion_backups(log)
    if actual == outputs:
        inputs[log] = policy.completed_receipt(log, result, root, changed=set(OUTPUTS))
        inputs.update(
            publication.completed_journal(root, log, json.loads(inputs[log]), previous=old)
        )
        for p, backup in backups.items():
            inputs[backup] = regular(backup)
            require(inputs[backup] == old[p], "Promotion beforeimage changed")
        check()
        return (
            (inputs, result)
            if _completed_inputs
            else {"applied": False, "changed": False, "approval": APPROVAL}
        )
    require(not _completed_inputs, "Completed promotion required")
    require(actual == old, "Partial or changed canonical promotion")
    return publication.publish(
        root,
        outputs,
        inputs,
        log,
        {backups[p]: old[p] for p in OUTPUTS},
        result,
        apply=apply,
        validate_scope=check,
    )


def verify_completed(root, promotion_log, *, source_log, source_proof):
    """Return fully verified current inputs and fifteen source records for native receipt23."""
    promotion_log = bound_path(promotion_log)
    saved = json.loads(regular(promotion_log))
    require(
        saved.get("phase") == "promote-stock-cas"
        and saved.get("state") == "complete"
        and saved.get("source_log") == str(bound_path(source_log))
        and saved.get("source_proof") == str(bound_path(source_proof)),
        "Completed promotion receipt required",
    )
    return promote(
        root,
        Path(saved["bundle"]),
        Path(saved["producer"]),
        source_log,
        source_proof,
        promotion_log,
        generation_manifest_sha256=saved["generation_manifest_sha256"],
        _completed_inputs=True,
    )


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("phase", choices=("capture-sources", "promote", "verify-completed"))
    parser.add_argument("--root", type=Path, default=ROOT)
    parser.add_argument("--source-log", type=Path, required=True)
    parser.add_argument("--source-proof", type=Path, required=True)
    parser.add_argument("--log", type=Path)
    parser.add_argument("--bundle", type=Path)
    parser.add_argument("--producer", type=Path)
    parser.add_argument("--generation-manifest-sha256")
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("--apply", action="store_true")
    mode.add_argument("--dry-run", action="store_true")
    args = parser.parse_args(argv)
    if args.phase == "promote" and not all(
        (args.log, args.bundle, args.producer, args.generation_manifest_sha256)
    ):
        parser.error("promote requires log, bundle, producer and generation-manifest-sha256")
    if args.phase == "verify-completed" and (not args.log or args.apply):
        parser.error("verify-completed requires log and does not accept apply")
    from plugins.lock_manager import LockManager
    from plugins.repository_settings import RepositorySettings

    root = checked_root(args.root)
    target = RepositorySettings.from_environment().get_target("mediaingredientmech")
    require(target.path.resolve() == root, "Configured MIM root differs")
    target.open()
    with LockManager().lock("mediaingredientmech", "#871/#268 bounded stock CAS " + args.phase):
        if args.phase == "capture-sources":
            result = capture_sources(root, args.source_log, args.source_proof, apply=args.apply)
        elif args.phase == "promote":
            result = promote(
                root,
                args.bundle,
                args.producer,
                args.source_log,
                args.source_proof,
                args.log,
                generation_manifest_sha256=args.generation_manifest_sha256,
                apply=args.apply,
            )
        else:
            inputs, result = verify_completed(
                root, args.log, source_log=args.source_log, source_proof=args.source_proof
            )
            result = {
                **result,
                "verified_input_sha256": {str(p): digest(b) for p, b in inputs.items()},
            }
    print(json.dumps(result, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
