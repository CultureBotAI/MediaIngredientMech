"""Review, prepare, install and verify a stable SSSOM artifact set (#1335).

Installation preserves the full candidate, including withheld assertions. It is
not a supported export and grants no scientific approval. Source-binding and
ordinary external-row release reviews remain distinct downstream operations.
"""

from __future__ import annotations

import argparse
import base64
import builtins
import csv
import io
import json
import os
import subprocess
import sys
import time
import types
import uuid
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from mediaingredientmech.curate.adoption_filesystem import _new_owner
from mediaingredientmech.curate.apply_receipt import reserve_receipt_outputs
from mediaingredientmech.curate.publication_guard import (
    FrozenFile,
    check_reserved,
    finish_receipt,
    no_alias,
    publish_validated,
)
from mediaingredientmech.export.reviewed_sssom import _tsv, read_sssom
from mediaingredientmech.stable_ids import (
    LIFECYCLE_PATH,
    REGISTRY_PATH,
    build_record_index,
    parse_registry,
    validate_records,
)

CAPABILITY = "reviewed-stable-sssom-publication-v1"
GENERATION = "native-stable-sssom-invocation-v1"
CANONICAL = "mappings/ingredient_mappings.sssom.tsv"
SUPPRESSIONS = "mappings/suppressed_aliases.tsv"
PROVENANCE = "mappings/stable_sssom_publication.json"
DIAGNOSTIC_MANIFEST = "mappings/stable_sssom_generation.json"
OUTPUTS = (CANONICAL, SUPPRESSIONS, DIAGNOSTIC_MANIFEST, PROVENANCE)
CONTRACT = "src/mediaingredientmech/stable_ids.py"
MARKER = "owned-name-policy-v1; suppression-sidecar-required"
SIDECAR_FIELDS = (
    "subject_id",
    "token_key",
    "token",
    "owner_subject_ids",
    "disposition",
    "input_surfaces",
    "source_refs",
    "evidence_refs",
)
_CAPTURE: Any = globals().get("_PRODUCER_CAPTURE")
_ADOPTION: Any = None


def native():
    """Keep the already-reviewed adoption producer's original closure intact."""
    global _ADOPTION
    if _ADOPTION is None:
        path = _CAPTURE.root / "src/mediaingredientmech/curate/adoption_producer.py"
        raw = _CAPTURE.files[str(path.relative_to(_CAPTURE.root))][0]
        loader = types.ModuleType("_publication_adoption_loader")
        loader.__file__ = str(path)
        loader.__dict__["__builtins__"] = vars(builtins)
        exec(compile(raw, str(path), "exec"), loader.__dict__)
        _, _ADOPTION = loader.load(_CAPTURE.root, raw)
    return _ADOPTION


def successor_native():
    """Keep the source successor's own producer, never substitute publication's."""
    name = "src/mediaingredientmech/curate/curation_successor_producer.py"
    raw = _CAPTURE.files[name][0]
    loader = types.ModuleType("_publication_successor_loader")
    loader.__file__ = str(_CAPTURE.root / name)
    loader.__dict__["__builtins__"] = vars(builtins)
    exec(compile(raw, loader.__file__, "exec"), loader.__dict__)
    capture, implementation = loader.load(_CAPTURE.root, raw)
    require(
        all(_CAPTURE.files[n][0] == value[0] for n, value in capture.files.items()),
        "successor capture differs from selected publication producer",
    )
    return implementation


def _successor(root, reference, files, *, before=None, publication_receipt=None):
    endpoint = successor_native().Endpoint(
        root,
        native().document(_read_ref(files, reference)),
        publication=before if publication_receipt is not None else None,
        publication_receipt=publication_receipt,
    )
    return endpoint


def require(value, message):
    if not value:
        raise ValueError("Stable SSSOM publication: " + message)


def _ref(root, path, raw=None):
    path = Path(path).absolute()
    native().relative(str(path.relative_to(root)))
    return {
        "path": str(path.relative_to(root)),
        "sha256": native().sha(FrozenFile.capture(path).content if raw is None else raw),
    }


def _path(root, path):
    path = Path(path)
    if not path.is_absolute():
        path = root / native().relative(str(path))
    require(".." not in path.parts and path.is_relative_to(root), "path escaped selected root")
    no_alias(path)
    return path


def _read_ref(inputs, ref):
    native().keys(ref, {"path", "sha256"})
    return inputs.read(ref["path"], ref["sha256"])


def _producer_paths(claw):
    paths = {
        claw / "scripts/build_mim_ingredient_sssom.py",
        claw / "scripts/kgm_unified_mappings.py",
        claw / "plugins/lock_manager.py",
    }
    for package in ("kg_microbe_utils", "kg_microbe_write", "kg_microbe_fleet"):
        directory = claw / "src" / package
        no_alias(directory)
        paths.update(directory.rglob("*.py"))
    return tuple(sorted(paths))


def _generation_check(root, receipt, files, *, before=None):
    """Bind a real maintained invocation, not a plausible standalone manifest."""
    api = native()
    api.keys(
        receipt,
        {
            "schema_version",
            "capability",
            "state",
            "root",
            "head",
            "adoption",
            "claw",
            "kg_microbe",
            "runtime",
            "argv",
            "environment",
            "started_at",
            "finished_at",
            "returncode",
            "outputs",
            "stdout",
            "stderr",
        }
        | ({"registry_retirement_proposal"} if "registry_retirement_proposal" in receipt else set())
        | ({"cas_dispositions"} if "cas_dispositions" in receipt else set())
        | (
            {"curation_successor", "successor_input_closure"}
            if "curation_successor" in receipt
            else set()
        ),
    )
    if "curation_successor" in receipt:
        require(
            receipt["adoption"] is None and isinstance(receipt["curation_successor"], dict),
            "conflicting or absent source-successor selection",
        )
        _read_ref(files, receipt["curation_successor"])
    proposal_ref = receipt.get("registry_retirement_proposal")
    if proposal_ref is not None:
        _read_ref(files, proposal_ref)
    cas_ref = receipt.get("cas_dispositions")
    if cas_ref is not None:
        _read_ref(files, cas_ref)
    require(
        receipt["schema_version"] == 1
        and receipt["capability"] == GENERATION
        and receipt["state"] == "COMPLETE"
        and receipt["returncode"] == 0,
        "actual completed native generation required",
    )
    require(receipt["root"] == str(root), "generation belongs to another root")
    api.git(root, "merge-base", "--is-ancestor", receipt["head"], "HEAD")
    require(receipt["runtime"] == _CAPTURE.runtime, "generation runtime differs")
    claw = api.root_path(receipt["claw"]["root"], "Claw producer")
    kg = api.root_path(receipt["kg_microbe"]["root"], "KG input")
    require(
        api.git(claw, "rev-parse", "HEAD").decode().strip() == receipt["claw"]["head"],
        "generator revision changed",
    )
    require(
        api.git(kg, "rev-parse", "HEAD").decode().strip() == receipt["kg_microbe"]["head"],
        "KG input revision changed",
    )
    manifest_raw = _read_ref(files, receipt["outputs"]["manifest"])
    manifest = api.document(manifest_raw)
    cas_proof = manifest.get("cas_dispositions")
    require(
        (cas_ref is None and cas_proof is None)
        or (
            cas_ref is not None
            and isinstance(cas_proof, dict)
            and cas_proof.get("path") == str(_path(root, cas_ref["path"]))
            and cas_proof.get("sha256") == cas_ref["sha256"]
        ),
        "CAS disposition selection/proof differs",
    )
    candidate = _read_ref(files, receipt["outputs"]["sssom"])
    sidecar = _read_ref(files, receipt["outputs"]["suppressions"])
    _read_ref(files, receipt["stdout"])
    _read_ref(files, receipt["stderr"])
    expected_command = _command(
        root,
        claw,
        {
            key: root / receipt["outputs"][key]["path"]
            for key in ("sssom", "suppressions", "manifest")
        },
        proposal_ref,
        cas_ref,
    )
    require(receipt["argv"] == expected_command, "unsupported generator command")
    require(receipt["environment"] == _environment(root, claw, kg), "generator roots differ")
    require(
        manifest["schema_version"] == 1
        and manifest["identity_mode"] == "stable"
        and manifest["external_sssom_validation"] == "passed"
        and manifest["stable_id_contract_sha256"] == api.sha(files.read(CONTRACT))
        and manifest["validation_replay"].startswith("disabled:"),
        "stable validated diagnostic contract required",
    )
    require(
        manifest["source_revisions"]
        == {
            "claw": receipt["claw"]["head"],
            "mim": receipt["head"],
            "kg_microbe": receipt["kg_microbe"]["head"],
        },
        "manifest producer revisions differ",
    )
    require(
        manifest["artifacts"]
        == [
            {
                "role": "sssom",
                "path": str(root / receipt["outputs"]["sssom"]["path"]),
                "sha256": api.sha(candidate),
            },
            {
                "role": "suppressed_aliases",
                "path": str(root / receipt["outputs"]["suppressions"]["path"]),
                "sha256": api.sha(sidecar),
            },
        ],
        "diagnostic artifact pair differs",
    )
    captured, absent = {}, []
    for item in manifest["source_inputs"]:
        api.keys(item, {"path", "sha256"})
        path = api.root_path(item["path"], "generation input")
        require(str(path) not in captured and path not in absent, "duplicate generation input")
        if item["sha256"] is None:
            require(not os.path.lexists(path), "formerly absent generation input appeared")
            absent.append(path)
        else:
            relative = str(path.relative_to(root)) if path.is_relative_to(root) else None
            frozen = (
                before.get(relative) if before and relative in before else FrozenFile.capture(path)
            )
            require(
                api.sha(frozen.content) == item["sha256"], "generation source changed: " + str(path)
            )
            captured[str(path)] = frozen
    producers = {
        str(path): api.sha(FrozenFile.capture(path).content) for path in _producer_paths(claw)
    }
    require(
        producers == manifest["producer_import_snapshot"] == receipt["claw"]["files"],
        "complete producer graph differs",
    )
    require(
        all(
            path in captured and api.sha(captured[path].content) == value
            for path, value in producers.items()
        ),
        "manifest omits producer inputs",
    )
    owners = api.inventory(root)
    records = {name: api.load_yaml(frozen.content) for name, frozen in owners.items()}
    registry = parse_registry(files.read(str(REGISTRY_PATH)), files.read(str(LIFECYCLE_PATH)))
    validate_records(registry, records)
    expected_subjects = {str(root / path): record["mim_id"] for path, record in records.items()}
    require(
        manifest["owner_subjects"] == expected_subjects
        and set(manifest["mapped_record_paths"]) == set(expected_subjects),
        "complete stable owner membership differs",
    )
    for name, frozen in owners.items():
        require(
            str(root / name) in captured and captured[str(root / name)].content == frozen.content,
            "manifest omits current owner",
        )
    for name in (str(REGISTRY_PATH), str(LIFECYCLE_PATH), CONTRACT, CANONICAL):
        require(str(root / name) in captured, "manifest omits required current input: " + name)
    _, _, rows = read_sssom(Path("candidate"), content=candidate)
    require(manifest["emitted_rows"] == len(rows), "generation row count differs")
    expected_accounting = [
        {
            "path": path,
            "subject_id": subject,
            "mapping_status": records[str(Path(path).relative_to(root))].get("mapping_status"),
            "external_candidate_rows": sum(row["subject_id"] == subject for row in rows),
            "scientific_approval_added": False,
        }
        for path, subject in expected_subjects.items()
    ]
    require(
        sorted(manifest["owner_candidate_accounting"], key=lambda x: x["path"])
        == sorted(expected_accounting, key=lambda x: x["path"]),
        "owner accounting differs",
    )
    _replay_generation(
        root, claw, kg, receipt, manifest, manifest_raw, candidate, sidecar, captured, absent
    )
    return manifest, candidate, sidecar, captured, absent, owners, records


def _replay_generation(
    root, claw, kg, receipt, manifest, manifest_raw, candidate, sidecar, captured, absent
):
    """#1339: self-consistent hashes are not proof of native generation.

    Replay the captured c1 transformations against all exact input bytes and the
    recorded label resolution. No provider is called; labels still require
    their own current scientific review. Compare every byte of all three native
    artifacts, including owner accounting, provenance and optional input absence.
    """
    name = "src/mediaingredientmech/curate/stable_sssom_replay.py"
    raw = _CAPTURE.files[name][0]
    payload = {
        "root": str(root),
        "claw": str(claw),
        "kg_microbe": str(kg),
        "inputs": {
            **{
                path: base64.b64encode(frozen.content).decode("ascii")
                for path, frozen in captured.items()
            },
            **{str(path): None for path in absent},
        },
        "registry_retirement_proposal": receipt.get("registry_retirement_proposal"),
        "cas_dispositions": receipt.get("cas_dispositions"),
        "canonical_label_resolution": manifest["canonical_label_resolution"],
        "source_revisions": manifest["source_revisions"],
        "outputs": {
            key: str(root / receipt["outputs"][key]["path"]) for key in ("sssom", "suppressions")
        },
    }
    # Compile the actual captured helper, not mutable source or cached bytecode.
    bootstrap = (
        "import sys; exec(compile(sys.argv[1], sys.argv[2], 'exec'), "
        "{'__name__': '__main__', '__file__': sys.argv[2]})"
    )
    process = subprocess.run(
        [sys.executable, "-c", bootstrap, raw.decode("utf-8"), str(_CAPTURE.root / name)],
        input=native().encoded(payload),
        cwd=root,
        env={**os.environ, **_environment(root, claw, kg)},
        capture_output=True,
        timeout=180,
    )
    # #1342: retain native diagnostics on the diagnostic channel, never in
    # the replay/CLI JSON. Genuine generation stdout/stderr are already held.
    if process.stderr:
        sys.stderr.write(process.stderr.decode("utf-8", errors="replace"))
    require(
        process.returncode == 0,
        "native generation replay failed: "
        + process.stderr.decode("utf-8", errors="replace")[-2000:],
    )
    replayed = native().document(process.stdout)
    native().keys(replayed, {"sssom", "suppressions", "manifest"})
    expected = {
        "sssom": candidate,
        "suppressions": sidecar,
        "manifest": manifest_raw,
    }
    for key, actual in expected.items():
        require(
            base64.b64decode(replayed[key], validate=True) == actual,
            "native generation replay differs: " + key,
        )
    _CAPTURE.verify()


def _command(root, claw, outputs, registry_retirement_proposal=None, cas_dispositions=None):
    command = [
        sys.executable,
        str(claw / "scripts/build_mim_ingredient_sssom.py"),
        "--identity-mode",
        "stable",
        "--mim-stable-id-contract-sha256",
        native().sha(FrozenFile.capture(root / CONTRACT).content),
        "--no-preserve-validation",
        "--output",
        str(outputs["sssom"]),
        "--suppressed-aliases-output",
        str(outputs["suppressions"]),
        "--generation-manifest-output",
        str(outputs["manifest"]),
    ]
    if registry_retirement_proposal is not None:
        native().keys(registry_retirement_proposal, {"path", "sha256"})
        command.extend(
            [
                "--registry-retirement-proposal",
                str(_path(root, registry_retirement_proposal["path"])),
                "--registry-retirement-proposal-sha256",
                registry_retirement_proposal["sha256"],
            ]
        )
    if cas_dispositions is not None:
        native().keys(cas_dispositions, {"path", "sha256"})
        command.extend(
            [
                "--cas-dispositions",
                str(_path(root, cas_dispositions["path"])),
                "--cas-dispositions-sha256",
                cas_dispositions["sha256"],
            ]
        )
    return command


def _environment(root, claw, kg):
    return {
        "MEDIAINGREDIENTMECH_ROOT": str(root),
        "KGMICROBE_ROOT": str(kg),
        "PYTHONPATH": str(claw / "src") + os.pathsep + str(root / "src"),
        "PATH": str(Path(sys.executable).parent) + os.pathsep + os.defpath,
    }


def _adoption_capture(root, stage, receipt_path):
    """Retain the verified adoption's native closure for terminal checks."""
    api = native()
    receipt_file = FrozenFile.capture(receipt_path)
    receipt = api.document(receipt_file.content)
    before = {
        name: FrozenFile.capture(root / api.relative(ref["path"]))
        for name, ref in receipt["beforeimages"].items()
    }
    loaded, _, manifest, staged, _ = api._prepared(root, stage, before=before)
    api._acceptance(loaded, manifest, receipt["acceptance"]["path"])
    return loaded, [
        manifest,
        *staged.values(),
        *before.values(),
        receipt_file,
        FrozenFile.capture(root / receipt["operational_fit"]["path"]),
    ]


def generate(
    root,
    claw_root,
    kg_root,
    adoption_stage,
    adoption_receipt,
    directory,
    registry_retirement_proposal=None,
    registry_retirement_proposal_sha256=None,
    curation_successor=None,
    curation_successor_sha256=None,
    cas_dispositions=None,
    cas_dispositions_sha256=None,
):
    """Run the actual native Claw CLI, retain failures and all three artifacts.

    No provider or network policy is changed. Callers must supply already-reviewed
    inputs and arrange allowed ontology resources. This command makes no release.
    """
    api = native()
    root, claw, kg = (
        api.root_path(value, role)
        for value, role in ((root, "target"), (claw_root, "Claw"), (kg_root, "KG input"))
    )
    _CAPTURE.bind(api.Inputs(root))
    require(
        bool(registry_retirement_proposal) == bool(registry_retirement_proposal_sha256),
        "registry retirement proposal and explicit digest are required together",
    )
    proposal_file, proposal_ref = None, None
    if registry_retirement_proposal is not None:
        proposal_file = FrozenFile.capture(_path(root, registry_retirement_proposal))
        require(
            api.sha(proposal_file.content) == registry_retirement_proposal_sha256,
            "registry retirement proposal digest differs",
        )
        proposal_ref = _ref(root, proposal_file.path, proposal_file.content)
    require(
        bool(cas_dispositions) == bool(cas_dispositions_sha256),
        "CAS dispositions and explicit digest are required together",
    )
    cas_file, cas_ref = None, None
    if cas_dispositions is not None:
        cas_file = FrozenFile.capture(_path(root, cas_dispositions))
        require(
            api.sha(cas_file.content) == cas_dispositions_sha256, "CAS disposition digest differs"
        )
        cas_ref = _ref(root, cas_file.path, cas_file.content)
    require(
        bool(curation_successor) == bool(curation_successor_sha256),
        "successor endpoint and digest are required together",
    )
    endpoint, endpoint_ref = None, None
    if curation_successor is not None:
        require(
            adoption_stage is None and adoption_receipt is None,
            "successor and legacy adoption arguments conflict",
        )
        endpoint_inputs = api.Inputs(root)
        endpoint_ref = {
            "path": str(_path(root, curation_successor).relative_to(root)),
            "sha256": curation_successor_sha256,
        }
        endpoint = _successor(root, endpoint_ref, endpoint_inputs)
        adopted, adoption_files = endpoint, list(endpoint_inputs.files.values())
        adoption = None
    else:
        require(
            not os.path.lexists(root / "data/curation_successor.json"),
            "explicit successor endpoint required",
        )
        adoption_stage, adoption_receipt = _path(root, adoption_stage), _path(
            root, adoption_receipt
        )
        api.verify_completed(root, adoption_stage, adoption_receipt)
        adopted, adoption_files = _adoption_capture(root, adoption_stage, adoption_receipt)
        adoption = {
            "stage": str(adoption_stage.relative_to(root)),
            "receipt": _ref(root, adoption_receipt),
        }
    tree = api.PreparationTree(root, api._stage_path(root, _path(root, directory)))
    outputs = {
        "sssom": tree.stage / "candidate.sssom.tsv",
        "suppressions": tree.stage / "suppressed_aliases.tsv",
        "manifest": tree.stage / "generation.json",
    }
    producer_files = {str(p): FrozenFile.capture(p) for p in _producer_paths(claw)}
    receipt = {
        "schema_version": 1,
        "capability": GENERATION,
        "state": "RUNNING",
        "root": str(root),
        "head": api.git(root, "rev-parse", "HEAD").decode().strip(),
        "adoption": adoption,
        "claw": {
            "root": str(claw),
            "head": api.git(claw, "rev-parse", "HEAD").decode().strip(),
            "files": api.hashes(producer_files),
        },
        "kg_microbe": {"root": str(kg), "head": api.git(kg, "rev-parse", "HEAD").decode().strip()},
        "runtime": _CAPTURE.runtime,
        "registry_retirement_proposal": proposal_ref,
        "cas_dispositions": cas_ref,
        "argv": _command(root, claw, outputs, proposal_ref, cas_ref),
        "environment": _environment(root, claw, kg),
        "started_at": datetime.now(timezone.utc).isoformat(),
    }
    if endpoint is not None:
        receipt.update(curation_successor=endpoint_ref, successor_input_closure=endpoint.closure())
    tree.put("invocation.json", api.encoded(receipt))
    try:
        if proposal_file is not None:
            proposal_file.verify()
        if cas_file is not None:
            cas_file.verify()
        process = subprocess.run(
            receipt["argv"],
            cwd=root,
            env={**os.environ, **receipt["environment"]},
            capture_output=True,
            timeout=1800,
        )
        tree.put("stdout.txt", process.stdout)
        tree.put("stderr.txt", process.stderr)
        require(
            process.returncode == 0, "native generator failed with exit " + str(process.returncode)
        )
        for frozen in producer_files.values():
            frozen.verify()
        receipt.update(
            state="COMPLETE",
            finished_at=datetime.now(timezone.utc).isoformat(),
            returncode=process.returncode,
            outputs={k: _ref(root, p) for k, p in outputs.items()},
            stdout=_ref(root, tree.stage / "stdout.txt"),
            stderr=_ref(root, tree.stage / "stderr.txt"),
        )
        generation_inputs = api.Inputs(root)
        checked = _generation_check(root, receipt, generation_inputs)
        _cas_source_correction(checked[0], endpoint, endpoint_ref)
        _, _, _, sources, absent, owners, _ = checked

        def terminal_check():
            # #1336: hold the actual CLI artifacts across the last expensive
            # adoption replay and both sides of success receipt publication.
            tree.check()
            _CAPTURE.verify()
            adopted.check()
            for frozen in (*adoption_files, *producer_files.values(), *sources.values()):
                frozen.verify()
            if proposal_file is not None:
                proposal_file.verify()
            if cas_file is not None:
                cas_file.verify()
            require(
                api.hashes(api.inventory(root)) == api.hashes(owners),
                "generation owner membership changed",
            )
            require(
                set(map(str, _producer_paths(claw))) == set(producer_files),
                "generation producer membership changed",
            )
            for path in absent:
                require(not os.path.lexists(path), "absent generation source appeared")
            require(
                api.git(root, "rev-parse", "HEAD").decode().strip() == receipt["head"]
                and api.git(claw, "rev-parse", "HEAD").decode().strip() == receipt["claw"]["head"]
                and api.git(kg, "rev-parse", "HEAD").decode().strip()
                == receipt["kg_microbe"]["head"],
                "generation Git context changed",
            )
            # Read the retained triple last, after the potentially long scans.
            generation_inputs.verify()

        log = tree.stage / "receipt.json"
        with reserve_receipt_outputs(log, backup_paths=()) as (handle,):
            try:
                if endpoint is None:
                    api.verify_completed(root, adoption_stage, adoption_receipt)
                else:
                    endpoint.verify_native()
                finish_receipt(handle, log, receipt, terminal_check)
            except BaseException as error:
                # finish_receipt removes any success-shaped bytes on drift.
                # Keep a truthful failure in our still-reserved diagnostic log.
                check_reserved(handle, log)
                handle.seek(0)
                handle.truncate()
                handle.write(
                    api.encoded(
                        {
                            "state": "FAILED_GENERATION",
                            "error": str(error),
                            "canonical_writes": False,
                        }
                    ).decode()
                )
                handle.flush()
                check_reserved(handle, log)
                raise
        return receipt
    except BaseException as error:
        tree.put(
            "FAILED.json",
            api.encoded(
                {
                    "state": "FAILED_GENERATION",
                    "error": str(error),
                    "canonical_writes": False,
                    "outputs_may_exist": True,
                }
            ),
        )
        raise


def _sidecar(raw):
    reader = csv.DictReader(io.StringIO(raw.decode()), delimiter="\t", strict=True)
    require(reader.fieldnames == list(SIDECAR_FIELDS), "unexpected suppression columns")
    result = list(reader)
    require(
        all(None not in row and None not in row.values() for row in result), "malformed suppression"
    )
    return result


def _render_candidate(raw, fields, rows):
    text = raw.decode()
    prelude = "".join(line for line in text.splitlines(keepends=True) if line.startswith("#"))
    return prelude.encode() + _tsv(fields, rows)


def _cas_source_correction(manifest, endpoint, endpoint_ref):
    """Require real reviewed source withdrawal, never a diagnostic success flag (#1383)."""
    proof = manifest.get("cas_dispositions")
    if proof is None:
        return
    claims = proof["content"]
    correction = claims["source_correction"]
    retired = [entry for entry in claims["entries"] if entry["action"] == "RETIRE_INVALID_CAS"]
    require(
        not retired or (endpoint is not None and correction == endpoint_ref),
        "CAS retirement requires the genuinely selected source-correction endpoint",
    )
    if correction is not None:
        require(
            endpoint is not None and correction == endpoint_ref,
            "CAS source-correction proof differs",
        )
    if endpoint is None:
        return
    operations = {
        operation["mim_id"]: operation for operation in endpoint.loaded.request["operations"]
    }
    for entry in claims["entries"]:
        owner = entry["owner"]
        if entry["action"] == "RETIRE_INVALID_CAS":
            operation = operations.get(owner["mim_id"])
            require(
                operation is not None
                and operation["after_path"] == owner["path"]
                and operation["proposal"]["sha256"] == owner["sha256"]
                and entry["row"]["object_id"] in operation["rejected_identifiers"],
                "CAS retirement lacks actual reviewed corrective owner/rejection",
            )
        else:
            require(
                owner["mim_id"] not in operations, "held owner was changed by source correction"
            )
            original = endpoint.loaded.predecessor.owners.get(owner["path"])
            require(
                original is not None and native().sha(original.content) == owner["sha256"],
                "held owner differs from preserved adoption predecessor",
            )


def _selection(loaded):
    """Derive every changed/retained/removed payload; decisions remain unassessed."""
    api = native()
    _, old_fields, old = read_sssom(Path(CANONICAL), content=loaded.before[CANONICAL].content)
    _, fields, candidate = read_sssom(Path("candidate"), content=loaded.candidate)
    require(old_fields == fields, "column migration requires a separate reviewed implementation")
    index = build_record_index(loaded.records)
    old_by_key: dict[tuple[str, str, str], list[dict]] = {}
    for position, row in enumerate(old, 1):
        owner = index.lookup(row["subject_id"])
        subject = loaded.records[owner]["mim_id"]
        key = (subject, row["predicate_id"], row["object_id"])
        old_by_key.setdefault(key, []).append({"position": position, "row": row})
    items, seen = [], set()
    cas_proof = loaded.manifest.get("cas_dispositions")
    cas_held = (
        {}
        if cas_proof is None
        else {item["candidate_position"]: item for item in cas_proof["held_rows"]}
    )
    for position, row in enumerate(candidate, 1):
        key = (row["subject_id"], row["predicate_id"], row["object_id"])
        require(key not in seen, "duplicate candidate triple")
        seen.add(key)
        owner = index.lookup(row["subject_id"])
        require(
            loaded.records[owner]["mim_id"] == row["subject_id"], "nonpermanent candidate identity"
        )
        require(
            row["predicate_id"]
            in {"skos:exactMatch", "skos:closeMatch", "skos:narrowMatch", "skos:broadMatch"},
            "unsupported candidate predicate",
        )
        before_rows = old_by_key.pop(key, [])
        proposed = dict(row)
        # Keep original source vocabulary and comments byte-for-byte as tokens /
        # substrings. Old validation stamps remain in history, not new approval.
        for field, separator in (("source", "|"), ("comment", " ")):
            values = []
            for value in [
                *(entry["row"].get(field, "") for entry in before_rows),
                row.get(field, ""),
            ]:
                for token in (value.split("|") if field == "source" else [value]):
                    if token and token not in values:
                        values.append(token)
            proposed[field] = separator.join(values)
        items.append(
            {
                "entry_id": f"row-{position:06d}",
                "candidate_position": position,
                "owner": owner,
                "owner_sha256": api.sha(loaded.owners[owner].content),
                "before_rows": before_rows,
                "candidate_row": row,
                "proposed_row": proposed,
                "disposition": None,
                "reason": None,
            }
        )
        if position in cas_held:
            obligation = cas_held[position]
            require(
                obligation["candidate_row"] == row
                and obligation["mandatory_disposition"] == "WITHHOLD"
                and any(old["row"] == obligation["historical_row"] for old in before_rows),
                "forced-held candidate/history differs",
            )
            items[-1].update(
                mandatory_disposition="INSTALL_WITHHOLD",
                cas_disposition=obligation,
            )
    for _, before_rows in sorted(old_by_key.items()):
        first = before_rows[0]
        owner = index.lookup(first["row"]["subject_id"])
        items.append(
            {
                "entry_id": f"removed-{first['position']:06d}",
                "candidate_position": None,
                "owner": owner,
                "owner_sha256": api.sha(loaded.owners[owner].content),
                "before_rows": before_rows,
                "candidate_row": None,
                "proposed_row": None,
                "disposition": None,
                "reason": None,
            }
        )
    rows = [entry["proposed_row"] for entry in items if entry["proposed_row"] is not None]
    # Preserve the complete previous suppression payload, including its exact
    # vocabulary, while resolving endpoint aliases through the native registry.
    old_sidecar = _sidecar(loaded.before[SUPPRESSIONS].content)
    new_sidecar = _sidecar(loaded.sidecar)
    active_subjects = {row["subject_id"] for row in rows}
    suppression: dict[tuple[str, str], dict] = {}
    retired = []
    for origin, entries in (("prior", old_sidecar), ("generated", new_sidecar)):
        for raw in entries:
            row = dict(raw)
            row["subject_id"] = loaded.records[index.lookup(row["subject_id"])]["mim_id"]
            row["owner_subject_ids"] = json.dumps(
                sorted(
                    {
                        loaded.records[index.lookup(value)]["mim_id"]
                        for value in api.document(row["owner_subject_ids"])
                    }
                ),
                ensure_ascii=False,
            )
            if row["subject_id"] not in active_subjects:
                require(origin == "prior", "generated suppression has no candidate subject")
                retired.append(raw)
                continue
            pair = (row["subject_id"], row["token_key"])
            require(
                row["token"].strip().casefold() == row["token_key"]
                and row["disposition"] == "SUPPRESS",
                "invalid suppression token/disposition",
            )
            require(
                not any(
                    token.strip().casefold() == row["token_key"]
                    for r in rows
                    if r["subject_id"] == row["subject_id"]
                    for token in r.get("other", "").split("|")
                ),
                "historically suppressed token reappeared",
            )
            if pair in suppression:
                for field in SIDECAR_FIELDS[3:]:
                    if field != "disposition":
                        row[field] = json.dumps(
                            sorted(
                                set(api.document(row[field]))
                                | set(api.document(suppression[pair][field]))
                            ),
                            ensure_ascii=False,
                        )
            suppression[pair] = row
    for row in suppression.values():
        require(
            row["subject_id"] not in api.document(row["owner_subject_ids"]),
            "self-owned suppression",
        )
        for field in ("owner_subject_ids", "input_surfaces", "source_refs", "evidence_refs"):
            values = api.document(row[field])
            require(
                values
                and values == sorted(set(values))
                and all(isinstance(v, str) and v for v in values),
                "incomplete suppression provenance",
            )
    suppression_rows = [suppression[key] for key in sorted(suppression)]
    context = {
        "adoption": loaded.generation["adoption"],
        "generation": loaded.request["generation"],
        "owners": api.hashes(loaded.owners),
        "registry": api.sha(loaded.inputs.read(str(REGISTRY_PATH))),
        "lifecycle": api.sha(loaded.inputs.read(str(LIFECYCLE_PATH))),
        "contract": api.sha(loaded.inputs.read(CONTRACT)),
        "before": {name: api.sha(f.content) if f else None for name, f in loaded.before.items()},
        "historical_reviews": loaded.request["historical_reviews"],
    }
    if loaded.successor is not None:
        context.update(
            curation_successor=loaded.generation["curation_successor"],
            successor_input_closure=loaded.successor.closure(),
        )
    return {
        "schema_version": 1,
        "capability": CAPABILITY,
        "context": context,
        "rows": items,
        "history": loaded.history,
        "suppression": {
            "prior": old_sidecar,
            "generated": new_sidecar,
            "proposed": suppression_rows,
            "retired": retired,
        },
    }


def _historical_reviews(loaded):
    """Read original native obligations in their genuine frozen Git context.

    These are historical acquisitions, not current stable-row approvals. Keep
    their full assessments and holds; current reviewers assess preservation of
    that content independently. No report is restamped or re-saved here.
    """
    api = native()
    specifications = loaded.request["historical_reviews"]
    require(
        isinstance(specifications, list) and specifications,
        "historical native review evidence required",
    )
    script = _CAPTURE.script("scripts/record_review.py")
    history, files, roots, seen = [], [], {}, set()
    for number, specification in enumerate(specifications, 1):
        api.keys(specification, {"root", "head", "review", "markdown_sha256"})
        root = api.root_path(specification["root"], "historical review")
        require(
            root != loaded.root and not root.samefile(loaded.root),
            "historical review root must remain physically independent and frozen (#1337)",
        )
        head = api.git(root, "rev-parse", "HEAD").decode().strip()
        require(head == specification["head"], "historical review HEAD differs")
        roots[str(root)] = head
        source = api.Inputs(root)
        raw = _read_ref(source, specification["review"])
        name = specification["review"]["path"]
        require((str(root), name) not in seen, "duplicate historical review")
        seen.add((str(root), name))
        md = str(Path(name).with_name("review.md"))
        markdown = source.read(md, specification["markdown_sha256"])
        report = script.parse_review_bundle(
            name, raw, markdown, loaded.root / "schema/record_review.yaml"
        )
        provenance = script.source_provenance(root, report)
        require(
            provenance["status"] not in {"invalid", "unverified"}
            and report["repository"] == api.REPOSITORY
            and report["completion"] == "completed",
            "invalid original historical review provenance/completion",
        )
        for item in report["source"]["inputs"]:
            source.read(item["path"], item["sha256"])
        source.verify()
        files.extend(source.files.values())
        history.append(
            {
                "entry_id": f"history-{number:03d}",
                "binding": specification,
                "role": "historical acquisition; not current stable-row approval",
                "original_report": report,
                "original_source_inputs": api.hashes(source.files),
            }
        )
    return history, files, roots


class Loaded:
    def __init__(
        self, root, request_path, *, before=None, historical=False, publication_receipt=None
    ):
        api = native()
        self.inputs = api.Inputs(
            api.root_path(root, "target"),
            {name: frozen for name, frozen in (before or {}).items() if frozen is not None},
        )
        self.root = self.inputs.root
        self.path = str(_path(self.root, request_path).relative_to(self.root))
        self.request = api.document(self.inputs.read(self.path))
        api.keys(
            self.request,
            {
                "schema_version",
                "capability",
                "head",
                "generation",
                "selection",
                "reviews",
                "review_inputs",
                "operational_policy",
                "historical_reviews",
            },
        )
        require(
            self.request["schema_version"] == 1 and self.request["capability"] == CAPABILITY,
            "unsupported publication contract",
        )
        self.head = api.git(self.root, "rev-parse", "HEAD").decode().strip()
        if historical:
            api.git(self.root, "merge-base", "--is-ancestor", self.request["head"], "HEAD")
        else:
            require(self.head == self.request["head"], "selected HEAD changed")
        self.index = api.git(self.root, "ls-files", "--stage", "-z")
        _CAPTURE.bind(self.inputs)
        self.generation = api.document(_read_ref(self.inputs, self.request["generation"]))
        self.before = dict(before or {})
        if before is None:
            for name in OUTPUTS:
                path = self.root / name
                self.before[name] = FrozenFile.capture(path) if os.path.lexists(path) else None
        require(
            set(self.before) == set(OUTPUTS)
            and self.before[CANONICAL] is not None
            and self.before[SUPPRESSIONS] is not None,
            "exact maintained beforeimages required",
        )
        # Reports may explicitly cite the original canonical bytes. Hold those
        # as beforeimages throughout apply/verification, never mislabel the
        # installed endpoint as the report's acquisition input.
        self.inputs.files.update(
            {name: frozen for name, frozen in self.before.items() if frozen is not None}
        )
        generation = _generation_check(self.root, self.generation, self.inputs, before=self.before)
        (
            self.manifest,
            self.candidate,
            self.sidecar,
            self.sources,
            self.absent,
            self.owners,
            self.records,
        ) = generation
        adoption = self.generation["adoption"]
        self.successor = None
        if "curation_successor" in self.generation:
            require(
                not historical or publication_receipt is not None,
                "historical successor requires actual native publication receipt",
            )
            self.successor = _successor(
                self.root,
                self.generation["curation_successor"],
                self.inputs,
                before=self.before,
                publication_receipt=publication_receipt,
            )
            require(
                self.generation["successor_input_closure"] == self.successor.closure(),
                "generation source-successor closure changed",
            )
            self.successor.publication_guard()
            self.adopted, self.adoption_files = self.successor, []
        else:
            require(
                not os.path.lexists(self.root / "data/curation_successor.json"),
                "successor cannot use legacy adoption route",
            )
            api.keys(adoption, {"stage", "receipt"})
            _read_ref(self.inputs, adoption["receipt"])
            self.adoption_stage = _path(self.root, adoption["stage"])
            self.adoption_receipt = _path(self.root, adoption["receipt"]["path"])
            api.verify_completed(self.root, self.adoption_stage, self.adoption_receipt)
            self.adopted, self.adoption_files = _adoption_capture(
                self.root, self.adoption_stage, self.adoption_receipt
            )
        self.claw = api.Claw(self.generation["claw"]["root"])
        _cas_source_correction(
            self.manifest, self.successor, self.generation.get("curation_successor")
        )
        self.policy = api._policy(
            api.document(_read_ref(self.inputs, self.request["operational_policy"]))
        )
        self.history, self.history_files, self.history_roots = _historical_reviews(self)
        if self.successor is not None:
            originals = self.successor.loaded.request["predecessor"]["historical_reviews"]
            require(
                all(
                    {
                        "root": s["identity"]["root"],
                        "head": s["identity"]["head"],
                        "review": s["review"],
                        "markdown_sha256": s["markdown_sha256"],
                    }
                    in self.request["historical_reviews"]
                    for s in originals
                ),
                "source successor historical obligations omitted",
            )
        self.parent = self.root / "mappings"
        no_alias(self.parent)
        self.parent_identity = (self.parent.stat().st_dev, self.parent.stat().st_ino)
        self.endpoint_states = (
            {name: FrozenFile.capture(self.root / name) for name in OUTPUTS}
            if historical
            else self.before
        )
        self.selection = None
        self.reviewer_ids = set()
        self.check()

    def check(self, states=None, during=()):
        api = native()
        _CAPTURE.verify()
        self.inputs.verify(exclude=OUTPUTS)
        self.claw.verify()
        require(
            api.git(self.root, "rev-parse", "HEAD").decode().strip() == self.head
            and api.git(self.root, "ls-files", "--stage", "-z") == self.index,
            "selected Git context changed",
        )
        require(
            api.hashes(api.inventory(self.root)) == api.hashes(self.owners),
            "owner inventory changed",
        )
        require(
            set(map(str, _producer_paths(self.claw.root))) == set(self.generation["claw"]["files"]),
            "producer membership changed",
        )
        for path, frozen in self.sources.items():
            name = (
                str(Path(path).relative_to(self.root))
                if Path(path).is_relative_to(self.root)
                else None
            )
            if name not in OUTPUTS:
                frozen.verify()
        for path in self.absent:
            require(not os.path.lexists(path), "absent source appeared")
        self.adopted.check()
        for frozen in self.adoption_files:
            frozen.verify()
        for root, expected in self.history_roots.items():
            require(
                api.git(Path(root), "rev-parse", "HEAD").decode().strip() == expected,
                "historical review HEAD changed",
            )
        for frozen in self.history_files:
            frozen.verify()
        no_alias(self.parent)
        require(
            (self.parent.stat().st_dev, self.parent.stat().st_ino) == self.parent_identity,
            "canonical parent changed",
        )
        for name, frozen in (self.endpoint_states if states is None else states).items():
            if name in during:
                continue
            if frozen is None:
                require(not os.path.lexists(self.root / name), "absent output appeared: " + name)
            else:
                frozen.verify()
        # #1338: currentness must survive the long scans and every native
        # write boundary, not only initial generation-manifest loading.
        kg_root = api.root_path(self.generation["kg_microbe"]["root"], "KG input")
        require(
            api.git(kg_root, "rev-parse", "HEAD").decode().strip()
            == self.generation["kg_microbe"]["head"],
            "KG input revision changed",
        )


def inspect(root, request_path):
    loaded = Loaded(root, request_path)
    result = _selection(loaded)
    loaded.check()
    return result


def _bundle(loaded, ref):
    api = native()
    api.keys(ref, {"path", "sha256"})
    raw = _read_ref(loaded.inputs, ref)
    md = str(Path(ref["path"]).with_name("review.md"))
    require(md in loaded.request["review_inputs"], "native review Markdown must be pinned")
    markdown = loaded.inputs.read(md, loaded.request["review_inputs"][md])
    script = _CAPTURE.script("scripts/record_review.py")
    report = script.parse_review_bundle(
        ref["path"], raw, markdown, loaded.root / "schema/record_review.yaml"
    )
    require(
        script.source_provenance(loaded.root, report)["status"] not in {"invalid", "unverified"},
        "invalid current native review provenance",
    )
    require(
        report["repository"] == api.REPOSITORY and report["completion"] == "completed",
        "completed native review required",
    )
    source = {entry["path"]: entry["sha256"] for entry in report["source"]["inputs"]}
    for name, expected in source.items():
        loaded.inputs.read(name, expected)
    return report, source


def _assessment(report, tid):
    require(tid in report["scope"]["reviewed_target_ids"], "target outside completed scope")
    checks = [x for x in report["checks"] if x["required"] and tid in x["target_ids"]]
    require(
        checks and all(x["status"] == "passed" for x in checks),
        "required publication checks incomplete",
    )
    require(
        not any(
            tid in x["target_ids"] and x["status"] in {"open", "deferred"}
            for x in report["findings"]
        ),
        "unresolved publication finding",
    )
    selected = [
        x for x in report["assessments"] if x["target_ids"] == [tid] and x["outcome"] == "supported"
    ]
    require(len(selected) == 1, "one explicit installation assessment per target required")
    return selected[0]


def _reviews(loaded, selection):
    api = native()
    require(len(loaded.request["reviews"]) == 2, "primary and separate skeptical review required")
    for name, expected in loaded.request["review_inputs"].items():
        loaded.inputs.read(name, expected)
    selected_path = loaded.request["selection"]["path"]
    claims = {entry["entry_id"]: entry for entry in selection["rows"]}
    claims.update({entry["entry_id"]: entry for entry in selection["history"]})
    claims["suppressions"] = selection["suppression"]
    reports = []
    required_inputs = {
        selected_path: loaded.request["selection"]["sha256"],
        "MAPPING_SEMANTICS.md": api.sha(loaded.inputs.read("MAPPING_SEMANTICS.md")),
        **api.hashes(loaded.owners),
        **{name: api.sha(f.content) for name, f in loaded.before.items() if f is not None},
        **{
            name: api.sha(loaded.inputs.read(name))
            for name in (str(REGISTRY_PATH), str(LIFECYCLE_PATH), CONTRACT)
        },
        loaded.request["generation"]["path"]: loaded.request["generation"]["sha256"],
    }
    if loaded.successor is None:
        ref = loaded.generation["adoption"]["receipt"]
        required_inputs[ref["path"]] = ref["sha256"]
    else:
        ref = loaded.generation["curation_successor"]
        required_inputs.update({ref["path"]: ref["sha256"], **loaded.successor.local_inputs()})
    for ref in loaded.request["reviews"]:
        report, source = _bundle(loaded, ref)
        require(
            report["scientific_review"] is True, "current scientific publication review required"
        )
        require(
            all(source.get(name) == value for name, value in required_inputs.items()),
            "review omits complete current owner/generation/selection inputs",
        )
        targets = {
            entry.get("selector"): entry
            for entry in report["targets"]
            if entry.get("path") == selected_path
        }
        require(set(targets) == set(claims), "review must cover every row and suppression change")
        for key, claim in claims.items():
            target = targets[key]
            require(
                target["kind"] == "snapshot_row"
                and target.get("semantic_digest")
                == {
                    "algorithm": "sha256-canonical-json-v1",
                    "sha256": api.digest(claim),
                    "description": "Complete stable publication selection",
                },
                "reviewed payload differs",
            )
            assessment = _assessment(report, target["target_id"])
            dimensions = {d["name"]: d["value"] for d in assessment.get("dimensions", [])}
            action = (
                "PRESERVE_SUPPRESSION_HISTORY"
                if key == "suppressions"
                else (
                    "PRESERVE_HISTORICAL_OBLIGATIONS"
                    if key.startswith("history-")
                    else claim["disposition"]
                )
            )
            require(
                dimensions.get("publication_action") == action
                and dimensions.get("publication_scope")
                == "canonical_installation_not_release_approval",
                "explicit non-release publication decision required",
            )
            evidence = {item["evidence_id"]: item for item in report["evidence"]}
            require(
                any(
                    evidence[eid]["reference"] in source
                    and evidence[eid].get("snapshot_sha256") == source[evidence[eid]["reference"]]
                    for eid in assessment["evidence_ids"]
                ),
                "captured evidence basis required",
            )
            if action == "INSTALL_SUPPORTED":
                require(
                    any(
                        evidence[eid]["kind"] in {"primary_source", "database", "authority"}
                        and evidence[eid]["support"] == "supports"
                        and evidence[eid]["reference"] in source
                        and evidence[eid].get("snapshot_sha256")
                        == source[evidence[eid]["reference"]]
                        for eid in assessment["evidence_ids"]
                    ),
                    "supported installation needs captured primary scientific evidence",
                )
        reports.append(report)
    identities = [report["reviewer"]["identity"] for report in reports]
    require(
        len(set(identities)) == 2
        and loaded.request["reviews"][0]["path"] != loaded.request["reviews"][1]["path"]
        and reports[1]["reviewer"].get("independence") == "independent"
        and reports[1]["reviewer"].get("independence_basis"),
        "separate skeptical review required",
    )
    loaded.reviewer_ids = set(identities)


def _outputs(loaded):
    api = native()
    draft = _selection(loaded)
    selection = api.document(_read_ref(loaded.inputs, loaded.request["selection"]))
    expected = api.document(api.encoded(selection))
    require(isinstance(expected.get("rows"), list), "selection rows required")
    for row in expected["rows"]:
        require(
            isinstance(row.get("reason"), str) and row["reason"].strip(),
            "explicit selection rationale required",
        )
        allowed = (
            {"INSTALL_SUPPORTED", "INSTALL_WITHHOLD"}
            if row["candidate_position"]
            else {"REMOVE_WITH_HISTORY"}
        )
        require(row["disposition"] in allowed, "unassessed publication selection")
        require(
            row.get("mandatory_disposition") is None
            or row["disposition"] == row["mandatory_disposition"],
            "historical invalid CAS requires INSTALL_WITHHOLD regardless of review votes",
        )
        row["disposition"], row["reason"] = None, None
    require(expected == draft, "complete derived selection differs; no arbitrary candidate edits")
    _reviews(loaded, selection)
    loaded.selection = selection
    _, fields, _ = read_sssom(Path("candidate"), content=loaded.candidate)
    rows = [
        entry["proposed_row"] for entry in selection["rows"] if entry["proposed_row"] is not None
    ]
    tsv = _render_candidate(loaded.candidate, fields, rows)
    require(MARKER in tsv.decode().split("\nsubject_id", 1)[0], "missing sidecar policy marker")
    previous = loaded.before[PROVENANCE]
    history = api.document(previous.content) if previous is not None else None
    provenance = {
        "schema_version": 1,
        "capability": CAPABILITY,
        "scientific_approval_added": False,
        "ordinary_release_review_required": True,
        "generation": loaded.request["generation"],
        "selection": selection,
        "reviews": loaded.request["reviews"],
        "review_inputs": loaded.request["review_inputs"],
        "historical_publication": history,
        "retention_policy": "Matched rows retain prior source tokens and comments; all prior rows/stamps/suppressions remain in selection history. No validation stamp is inherited.",
        "artifacts": {
            CANONICAL: api.sha(tsv),
            SUPPRESSIONS: api.sha(_tsv(SIDECAR_FIELDS, selection["suppression"]["proposed"])),
        },
    }
    return {
        CANONICAL: tsv,
        SUPPRESSIONS: _tsv(SIDECAR_FIELDS, selection["suppression"]["proposed"]),
        DIAGNOSTIC_MANIFEST: _read_ref(loaded.inputs, loaded.generation["outputs"]["manifest"]),
        PROVENANCE: api.encoded(provenance),
    }


def _validate(loaded, tree, outputs):
    """Run the actual maintained invariant gate, against selected root owners."""
    path = tree.stage / "candidate" / CANONICAL
    command = [
        sys.executable,
        str(loaded.root / "scripts/validate_sssom_invariants.py"),
        str(path),
        "--reject-tsv",
        str(tree.stage / "rejected.tsv"),
    ]
    loaded.check()
    process = subprocess.run(command, cwd=loaded.root, capture_output=True, timeout=180)
    tree.put("validation.stdout.txt", process.stdout)
    tree.put("validation.stderr.txt", process.stderr)
    require(process.returncode == 0, "native qc-sssom failed: " + process.stderr.decode()[-2000:])
    for name, raw in outputs.items():
        require(
            FrozenFile.capture(tree.stage / "candidate" / name).content == raw,
            "validator changed candidate",
        )
    loaded.check()
    return {
        "argv": command,
        "exit_code": process.returncode,
        "stdout_sha256": native().sha(process.stdout),
        "stderr_sha256": native().sha(process.stderr),
    }


def _profile(loaded, staged, context, directory):
    """Use actual complete guards/backups and the native conservative fit model."""
    api = native()
    storage = api.PreparationTree(loaded.root, directory)
    before = {name: f for name, f in loaded.before.items() if f is not None}
    log = directory / "fit.json"
    paths = tuple(directory / f"before-{i:03d}.bin" for i in range(len(before)))
    with reserve_receipt_outputs(log, backup_paths=paths) as handles:
        receipt, *backups = handles
        started = time.perf_counter()
        for handle, frozen in zip(backups, before.values(), strict=True):
            handle.write(frozen.content)
            handle.flush()
            os.fsync(handle.fileno())
        archived = [FrozenFile.capture(path) for path in paths]
        require(
            all(
                f.content == previous.content
                for f, previous in zip(archived, before.values(), strict=True)
            ),
            "operational beforeimages differ",
        )
        backup_seconds = time.perf_counter() - started

        def scan():
            storage.check()
            for handle, path in zip(handles, (log, *paths), strict=True):
                check_reserved(handle, path)
            for frozen in (*archived, *staged.values(), context):
                frozen.verify()
            loaded.check()

        measured = datetime.now(timezone.utc).isoformat()
        samples = []
        for _ in range(2):
            started = time.perf_counter()
            scan()
            samples.append(time.perf_counter() - started)
        result = {
            "model": api.FIT_MODEL,
            "measured_at": measured,
            "context": _ref(loaded.root, context.path, context.content),
            "sample_seconds": samples,
            "backup_seconds": backup_seconds,
            "measured_current_owner_count": len(loaded.owners),
            "lease_namespace": api._lease_namespace(loaded),
            "input_closure": {
                "target": api.hashes(loaded.inputs.files),
                "source": api.hashes(loaded.sources),
                "before": {
                    name: api.sha(f.content) if f else None for name, f in loaded.before.items()
                },
                "staged": {
                    str(f.path.relative_to(loaded.root)): api.sha(f.content)
                    for f in staged.values()
                },
            },
            "maintained_writes": False,
            "lease_acquired": False,
        }
        if loaded.successor is not None:
            result["input_closure"]["curation_successor"] = loaded.successor.closure()
        finish_receipt(receipt, log, result, scan)
    return result, FrozenFile.capture(log)


def _counts(loaded, outputs):
    input_bytes = sum(len(f.content) for f in loaded.inputs.files.values())
    before_bytes = input_bytes + sum(len(f.content) for f in loaded.before.values() if f)
    after_bytes = input_bytes + sum(map(len, outputs.values()))
    return {
        "rechecks": 12 + 5 * len(outputs),
        "peak_growth_factor": max(1, after_bytes / max(1, before_bytes)),
    }


def prepare(root, request_path, stage):
    api = native()
    started = time.perf_counter()
    loaded = Loaded(root, request_path)
    outputs = _outputs(loaded)
    tree = api.PreparationTree(loaded.root, api._stage_path(loaded.root, _path(loaded.root, stage)))
    try:
        staged = {name: tree.put("candidate/" + name, raw) for name, raw in outputs.items()}
        validation = _validate(loaded, tree, outputs)
        manifest = {
            "schema_version": 1,
            "capability": CAPABILITY,
            "state": "PREPARED_CANDIDATE_ONLY",
            "scientific_approval_added": False,
            "root": str(loaded.root),
            "head": loaded.head,
            "request": _ref(loaded.root, loaded.root / loaded.path),
            "before": {
                name: api.sha(f.content) if f else None for name, f in loaded.before.items()
            },
            "outputs": {name: api.sha(raw) for name, raw in outputs.items()},
            "inputs": api.hashes(loaded.inputs.files),
            "owners": api.hashes(loaded.owners),
            "producer": _CAPTURE.receipt(loaded.inputs),
            "native_validation": validation,
        }
        if loaded.successor is not None:
            manifest["curation_successor"] = loaded.successor.closure()
        context = tree.put("fit-context.json", api.encoded(manifest))
        startup = time.perf_counter() - started
        measurement, frozen = _profile(
            loaded,
            staged,
            context,
            loaded.root / ".temp" / ("stable-publication-fit-" + uuid.uuid4().hex),
        )
        # At most five full boundaries per artifact plus setup/final receipt;
        # no owners grow. Byte growth covers larger TSV/history verification.
        counts = _counts(loaded, outputs)
        manifest["operational_budget"] = {
            "policy": loaded.request["operational_policy"],
            "policy_value": loaded.policy,
            "lease_namespace": api._lease_namespace(loaded),
            "counts": counts,
            "startup_seconds": startup,
            "measurement": _ref(loaded.root, frozen.path, frozen.content),
            "forecast_seconds": api._forecast(loaded.policy, counts, measurement, startup),
            "limitations": list(api.FIT_LIMITATIONS),
        }
        tree.put("manifest.json", api.encoded(manifest))
        tree.check()
        loaded.check()
        return manifest
    except BaseException as error:
        try:
            tree.put(
                "FAILED.json",
                api.encoded(
                    {"state": "FAILED_PREPARATION", "error": str(error), "canonical_writes": False}
                ),
            )
        except (OSError, ValueError):
            pass
        raise


def _prepared(root, stage, *, before=None, historical=False, publication_receipt=None):
    api = native()
    root = api.root_path(root, "target")
    stage = _path(root, stage)
    manifest_file = FrozenFile.capture(stage / "manifest.json")
    manifest = api.document(manifest_file.content)
    require(
        manifest["capability"] == CAPABILITY
        and manifest["schema_version"] == 1
        and manifest["state"] == "PREPARED_CANDIDATE_ONLY"
        and manifest["scientific_approval_added"] is False,
        "no prepared native publication",
    )
    loaded = Loaded(
        root,
        manifest["request"]["path"],
        before=before,
        historical=historical,
        publication_receipt=publication_receipt,
    )
    if loaded.successor is not None:
        require(
            manifest.get("curation_successor") == loaded.successor.closure(),
            "prepared successor closure changed",
        )
    else:
        require("curation_successor" not in manifest, "unexpected source successor proof")
    require(_ref(root, root / loaded.path) == manifest["request"], "prepared request changed")
    outputs = _outputs(loaded)
    require(
        manifest["root"] == str(root)
        and manifest["before"]
        == {name: api.sha(f.content) if f else None for name, f in loaded.before.items()},
        "prepared beforeimages differ",
    )
    require(
        manifest["outputs"] == {name: api.sha(raw) for name, raw in outputs.items()}
        and manifest["owners"] == api.hashes(loaded.owners),
        "prepared selection changed",
    )
    require(
        manifest["inputs"] == api.hashes(loaded.inputs.files), "prepared evidence closure changed"
    )
    current_producer = _CAPTURE.receipt(loaded.inputs)
    old_producer = manifest["producer"]
    # Ordinary commits after installation may advance HEAD; source/runtime
    # bytes must still match exactly. No old producer is executed from JSON.
    for key in ("schema_version", "status", "source_sha256", "files", "runtime"):
        require(old_producer[key] == current_producer[key], "publication producer/runtime changed")
    if not historical:
        require(old_producer == current_producer, "prepared producer context changed")
    else:
        api.git(root, "merge-base", "--is-ancestor", manifest["head"], "HEAD")
    staged = {name: FrozenFile.capture(stage / "candidate" / name) for name in outputs}
    require(
        all(staged[name].content == raw for name, raw in outputs.items()), "prepared output changed"
    )
    budget = manifest["operational_budget"]
    require(
        budget["policy"] == loaded.request["operational_policy"]
        and budget["policy_value"] == loaded.policy
        and budget["lease_namespace"] == api._lease_namespace(loaded),
        "reviewed budget/namespace changed",
    )
    require(budget["counts"] == _counts(loaded, outputs), "operational work estimate changed")
    measurement = api.document(_read_ref(loaded.inputs, budget["measurement"]))
    if loaded.successor is not None:
        require(
            measurement["input_closure"].get("curation_successor") == loaded.successor.closure(),
            "operational fit omits successor proof",
        )
    context_file = FrozenFile.capture(stage / "fit-context.json")
    require(
        measurement["context"] == _ref(root, context_file.path, context_file.content),
        "operational context changed",
    )
    expected_context = dict(manifest)
    expected_context.pop("operational_budget")
    require(
        context_file.content == api.encoded(expected_context), "operational fit context differs"
    )
    require(
        budget["forecast_seconds"]
        == api._forecast(loaded.policy, budget["counts"], measurement, budget["startup_seconds"]),
        "operational forecast changed",
    )
    loaded.check(
        states=(
            None if before is None else {name: FrozenFile.capture(root / name) for name in OUTPUTS}
        )
    )
    return loaded, manifest, manifest_file, staged, outputs


def _acceptance(loaded, manifest_file, acceptance_path):
    api = native()
    path = _path(loaded.root, acceptance_path)
    raw = loaded.inputs.read(str(path.relative_to(loaded.root)))
    acceptance = api.document(raw)
    api.keys(acceptance, {"manifest_sha256", "review", "markdown_sha256"})
    require(
        acceptance["manifest_sha256"] == api.sha(manifest_file.content),
        "acceptance names another prepared set",
    )
    report_ref = acceptance["review"]
    report_raw = _read_ref(loaded.inputs, report_ref)
    md = str(Path(report_ref["path"]).with_name("review.md"))
    markdown = loaded.inputs.read(md, acceptance["markdown_sha256"])
    script = _CAPTURE.script("scripts/record_review.py")
    report = script.parse_review_bundle(
        report_ref["path"], report_raw, markdown, loaded.root / "schema/record_review.yaml"
    )
    require(
        script.source_provenance(loaded.root, report)["status"] not in {"invalid", "unverified"},
        "invalid exact-set acceptance provenance",
    )
    require(
        report["repository"] == api.REPOSITORY
        and report["completion"] == "completed"
        and report["scientific_review"] is False
        and report["verdict"] in {"pass", "pass_with_limitations"}
        and report["reviewer"].get("independence") == "independent"
        and report["reviewer"].get("independence_basis")
        and report["reviewer"]["identity"] not in loaded.reviewer_ids,
        "separate independent exact-set acceptance required",
    )
    source = {entry["path"]: entry["sha256"] for entry in report["source"]["inputs"]}
    name = str(manifest_file.path.relative_to(loaded.root))
    require(source.get(name) == api.sha(manifest_file.content), "acceptance omits manifest")
    for source_path, expected in source.items():
        loaded.inputs.read(source_path, expected)
    targets = [
        target
        for target in report["targets"]
        if target.get("path") == name and target.get("selector") == "prepared"
    ]
    require(len(targets) == 1, "one exact prepared target required")
    target = targets[0]
    require(
        target["kind"] == "snapshot_row"
        and target.get("semantic_digest")
        == {
            "algorithm": "sha256",
            "sha256": api.sha(manifest_file.content),
            "description": "Exact prepared manifest bytes",
        },
        "acceptance target differs",
    )
    assessment = _assessment(report, target["target_id"])
    dimensions = {d["name"]: d["value"] for d in assessment.get("dimensions", [])}
    budget = api.document(manifest_file.content)["operational_budget"]
    require(
        all(
            dimensions.get(key) == value
            for key, value in {
                "publication_action": "apply_exact_prepared_set",
                "operational_budget_sha256": api.digest(budget),
                "lease_seconds": str(budget["policy_value"]["lease_seconds"]),
                "lease_namespace_sha256": api.digest(budget["lease_namespace"]),
                "lease_scheduling": "mediaingredientmech_and_global_conflict_reviewed",
            }.items()
        ),
        "exact set and operational lease acceptance required",
    )
    return _ref(loaded.root, path, raw)


def apply(root, stage, acceptance_path, receipt_dir, *, enabled=False):
    api = native()
    root = api.root_path(root, "target")
    receipt_dir = _path(root, receipt_dir)
    if enabled and os.path.lexists(receipt_dir):
        result = verify_completed(root, stage, receipt_dir / "application.json")
        previous = api.document(FrozenFile.capture(receipt_dir / "application.json").content)
        require(
            previous["acceptance"] == _ref(root, _path(root, acceptance_path)),
            "completed rerun acceptance differs",
        )
        return {"applied": False, "unchanged": True, "verification": result}
    started = time.perf_counter()
    loaded, manifest, manifest_file, staged, outputs = _prepared(root, stage)
    acceptance = _acceptance(loaded, manifest_file, acceptance_path)
    budget = manifest["operational_budget"]
    measurement = api.document(_read_ref(loaded.inputs, budget["measurement"]))
    api._fit_age(loaded.policy, measurement)
    if not enabled:
        loaded.check()
        return {
            "applied": False,
            "scientific_approval_added": False,
            "outputs": manifest["outputs"],
        }
    startup = max(budget["startup_seconds"], time.perf_counter() - started)
    measurement, fit_file = _profile(
        loaded,
        staged,
        manifest_file,
        root / ".temp" / ("stable-publication-fit-" + uuid.uuid4().hex),
    )
    forecast = api._forecast(loaded.policy, budget["counts"], measurement, startup)
    api._fit_age(loaded.policy, measurement)
    locks = loaded.claw.modules["locks"].LockManager()
    lease_started = time.monotonic()
    with locks.lock(
        "mediaingredientmech",
        "reviewed stable SSSOM publication",
        timeout=loaded.policy["lease_seconds"],
    ):
        with locks._leases_guard:
            token = locks._leases.get("mediaingredientmech")
        lease = locks.check_lock("mediaingredientmech")
        require(
            token and lease and lease.get("lease_token") == token, "acquired lease ownership lost"
        )
        expires = lease["expires_at"]
        deadline = datetime.fromisoformat(expires)
        require(
            deadline.utcoffset() is not None and locks._utc_now() < deadline,
            "lease already expired",
        )
        tree = api.PreparationTree(root, api._stage_path(root, receipt_dir))
        log = receipt_dir / "application.json"
        paths = {
            name: receipt_dir / f"before-{index:03d}.bin"
            for index, (name, frozen) in enumerate(loaded.before.items())
            if frozen is not None
        }
        result = {
            "schema_version": 1,
            "capability": CAPABILITY,
            "state": "PREPARED",
            "scientific_approval_added": False,
            "manifest": _ref(root, manifest_file.path, manifest_file.content),
            "acceptance": acceptance,
            "beforeimages": {
                name: _ref(root, paths[name], frozen.content) if frozen else None
                for name, frozen in loaded.before.items()
            },
            "outputs": manifest["outputs"],
            "completed_operations": [],
            "recovery_required": False,
            "operational_fit": {
                "receipt": _ref(root, fit_file.path, fit_file.content),
                "startup_seconds": startup,
                "forecast_seconds": forecast,
                "budget_sha256": api.digest(budget),
            },
        }
        states = dict(loaded.before)
        archives: list[FrozenFile] = []
        with reserve_receipt_outputs(log, backup_paths=tuple(paths.values())) as handles:
            receipt, *backups = handles

            def lease_current():
                with locks._leases_guard:
                    require(
                        locks._leases.get("mediaingredientmech") == token,
                        "acquired lease ownership lost",
                    )
                current = locks.check_lock("mediaingredientmech")
                require(
                    current
                    and current.get("lease_token") == token
                    and current.get("expires_at") == expires
                    and locks._utc_now() < deadline
                    and time.monotonic() - lease_started < loaded.policy["lease_seconds"]
                    and api._lease_namespace(loaded) == budget["lease_namespace"],
                    "write lease lost or deadline changed",
                )

            def recheck(during=()):
                lease_current()
                tree.check()
                for handle, path in zip(handles, (log, *paths.values()), strict=True):
                    check_reserved(handle, path)
                for frozen in (*archives, *staged.values(), manifest_file, fit_file):
                    frozen.verify()
                loaded.check(states, during)
                lease_current()

            def progress():
                check_reserved(receipt, log)
                receipt.seek(0)
                receipt.truncate()
                receipt.write(api.encoded(result).decode())
                receipt.flush()
                os.fsync(receipt.fileno())
                check_reserved(receipt, log)

            try:
                for name, handle in zip(paths, backups, strict=True):
                    handle.write(loaded.before[name].content)
                    handle.flush()
                    os.fsync(handle.fileno())
                archives.extend(FrozenFile.capture(path) for path in paths.values())
                recheck()
                progress()
                result["state"] = "APPLYING"
                for name, raw in outputs.items():
                    recheck()
                    if states[name] is not None and states[name].content == raw:
                        continue

                    def boundary(name=name):
                        recheck((name,))

                    if states[name] is None:
                        installed = _new_owner(root, name, raw, boundary)
                    else:

                        def render(path: Path, raw: bytes = raw) -> None:
                            path.write_bytes(raw)

                        installed = publish_validated(states[name], render, boundary)
                    states[name] = installed
                    result["completed_operations"].append({"path": name, "sha256": api.sha(raw)})
                    recheck()
                    progress()
                require(
                    api.hashes(states) == manifest["outputs"],
                    "final installed artifact set differs",
                )
                result["state"] = "COMPLETE"
                receipt.seek(0)
                receipt.truncate()
                finish_receipt(receipt, log, result, recheck)
                return result
            except BaseException as error:
                result.update(
                    state="FAILED", recovery_required=True, error=f"{type(error).__name__}: {error}"
                )
                result["observed_outputs"] = {}
                for name in outputs:
                    try:
                        result["observed_outputs"][name] = _ref(root, root / name)
                    except (OSError, ValueError) as observed:
                        result["observed_outputs"][name] = {"error": str(observed)}
                try:
                    progress()
                except (OSError, ValueError):
                    pass
                raise


def verify_completed(root, stage, receipt_path):
    api = native()
    root = api.root_path(root, "target")
    receipt_file = FrozenFile.capture(_path(root, receipt_path))
    receipt = api.document(receipt_file.content)
    require(
        receipt["capability"] == CAPABILITY
        and receipt["state"] == "COMPLETE"
        and receipt["recovery_required"] is False
        and receipt["scientific_approval_added"] is False,
        "no completed publication",
    )
    require(set(receipt["beforeimages"]) == set(OUTPUTS), "incomplete publication beforeimages")
    before = {}
    for name, ref in receipt["beforeimages"].items():
        frozen = FrozenFile.capture(root / native().relative(ref["path"])) if ref else None
        before[name] = frozen
        if ref:
            assert frozen is not None
            require(api.sha(frozen.content) == ref["sha256"], "archived beforeimage changed")
    loaded, manifest, manifest_file, staged, outputs = _prepared(
        root, stage, before=before, historical=True, publication_receipt=receipt_file
    )
    require(
        receipt["manifest"] == _ref(root, manifest_file.path, manifest_file.content)
        and receipt["outputs"] == manifest["outputs"],
        "completion scope differs",
    )
    require(
        _acceptance(loaded, manifest_file, receipt["acceptance"]["path"]) == receipt["acceptance"],
        "completed acceptance differs",
    )
    expected = [
        {"path": name, "sha256": api.sha(raw)}
        for name, raw in outputs.items()
        if (previous := before[name]) is None or previous.content != raw
    ]
    require(receipt["completed_operations"] == expected, "completed phase log differs")
    fit = receipt["operational_fit"]
    measurement = api.document(_read_ref(loaded.inputs, fit["receipt"]))
    if loaded.successor is not None:
        require(
            measurement["input_closure"].get("curation_successor") == loaded.successor.closure(),
            "completed fit omits successor proof",
        )
    budget = manifest["operational_budget"]
    require(
        fit["budget_sha256"] == api.digest(budget)
        and measurement["context"] == _ref(root, manifest_file.path, manifest_file.content)
        and measurement["lease_namespace"] == budget["lease_namespace"]
        and fit["forecast_seconds"]
        == api._forecast(loaded.policy, budget["counts"], measurement, fit["startup_seconds"]),
        "completed operational fit differs",
    )
    states = {name: FrozenFile.capture(root / name) for name in outputs}
    require(api.hashes(states) == manifest["outputs"], "current canonical artifact set differs")
    loaded.check(states)
    receipt_file.verify()
    return {
        "status": "COMPLETE_CURRENT_CANONICAL_CANDIDATE",
        "scientific_approval_added": False,
        "ordinary_release_review_required": True,
        "outputs": manifest["outputs"],
        "original_head": manifest["head"],
        "current_head": loaded.head,
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("operation", choices=["generate", "inspect", "prepare", "apply", "verify"])
    parser.add_argument("--root", type=Path, default=Path.cwd())
    for name in (
        "request",
        "stage",
        "acceptance",
        "receipt",
        "claw-root",
        "kg-root",
        "adoption-stage",
        "adoption-receipt",
        "registry-retirement-proposal",
        "curation-successor",
        "cas-dispositions",
    ):
        parser.add_argument("--" + name, type=Path)
    parser.add_argument("--registry-retirement-proposal-sha256")
    parser.add_argument("--curation-successor-sha256")
    parser.add_argument("--cas-dispositions-sha256")
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args()
    if args.operation == "generate":
        result = generate(
            args.root,
            args.claw_root,
            args.kg_root,
            args.adoption_stage,
            args.adoption_receipt,
            args.stage,
            args.registry_retirement_proposal,
            args.registry_retirement_proposal_sha256,
            args.curation_successor,
            args.curation_successor_sha256,
            args.cas_dispositions,
            args.cas_dispositions_sha256,
        )
    elif args.operation == "inspect":
        result = inspect(args.root, args.request)
    elif args.operation == "prepare":
        result = prepare(args.root, args.request, args.stage)
    elif args.operation == "apply":
        result = apply(args.root, args.stage, args.acceptance, args.receipt, enabled=args.apply)
    else:
        result = verify_completed(args.root, args.stage, args.receipt)
    print(native().encoded(result).decode())


if _CAPTURE is None:
    _root = Path(__file__).absolute().parents[3]
    _path_loader = _root / "src/mediaingredientmech/curate/stable_publication_producer.py"
    _raw = _path_loader.read_bytes()
    _loader = types.ModuleType("_stable_publication_loader")
    _loader.__file__ = str(_path_loader)
    exec(compile(_raw, str(_path_loader), "exec"), _loader.__dict__)
    _capture, _implementation = _loader.load(_root, _raw)
    for _name, _value in vars(_implementation).items():
        if not _name.startswith("__"):
            globals()[_name] = _value

if __name__ == "__main__":
    main()
