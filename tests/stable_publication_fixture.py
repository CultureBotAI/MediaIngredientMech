"""Genuine offline adoption → Claw stable-triple fixture for #1335.

These are explicitly synthetic scientific decisions, never campaign approvals.
The native adoption API, review saver, lease, Claw CLI and SSSOM validator all
run unchanged. Only NCIT grounding is used: its native builder path consumes
the fixture's stored label and has no ontology-provider lookup.
"""

from __future__ import annotations

import csv
import gzip
import hashlib
import importlib.metadata
import io
import json
import os
import shutil
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

from tests.test_stable_id_adoption import Fixture, api, commit, initialize

CLAW_REVISION = "c1cbd0f715f2d83d7cb6773797af7651e315454d"
PACKAGED_PRODUCER = Path(__file__).parent / "fixtures/claw_stable_sssom"
PACKAGED_ORIGIN_SHA256 = "69751a98b2b630865a069349779fdd80bf47231dd4cf79f396cfe83e40eaf762"
CANONICAL = "mappings/ingredient_mappings.sssom.tsv"
COLUMNS = (
    "subject_id",
    "subject_label",
    "predicate_id",
    "object_id",
    "object_label",
    "object_source",
    "mapping_justification",
    "source",
    "mapping_date",
    "confidence",
    "comment",
    "other",
    "validation_method",
)


def sha(raw: bytes) -> str:
    return hashlib.sha256(raw).hexdigest()


def now() -> str:
    return datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")


def _json(path: Path, value: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("x", encoding="utf-8") as handle:
        json.dump(value, handle, indent=2, sort_keys=True, ensure_ascii=False)
        handle.write("\n")


def _git(root: Path, *args: str) -> str:
    return (
        subprocess.check_output(
            ["git", *args],
            cwd=root,
            stderr=subprocess.PIPE,
            timeout=30,
            env={**os.environ, "GIT_NO_LAZY_FETCH": "1", "GIT_TERMINAL_PROMPT": "0"},
        )
        .decode()
        .strip()
    )


def materialize_producer(destination: Path, *, source: Path = PACKAGED_PRODUCER) -> Path:
    """Reconstruct exact upstream source under an honestly synthetic Git HEAD.

    The fixture is self-contained and offline. Its source manifest pins actual
    upstream bytes; the generation manifest records the new local commit
    rather than impersonating the upstream c1 revision.
    """
    origin_raw = (source / "ORIGIN.json").read_bytes()
    if sha(origin_raw) != PACKAGED_ORIGIN_SHA256:
        raise ValueError("Packaged producer origin manifest changed")
    origin = json.loads(origin_raw)
    if origin["upstream_revision"] != CLAW_REVISION:
        raise ValueError("Packaged producer upstream revision differs")
    captured = {}
    for name, entry in origin["files"].items():
        path = source / entry["fixture_path"]
        if path.is_symlink():
            raise ValueError("Packaged producer source is aliased")
        raw = path.read_bytes()
        if sha(raw) != entry["sha256"] or len(raw) != entry["size"]:
            raise ValueError("Packaged producer source changed: " + name)
        captured[name] = raw
    expected = {entry["fixture_path"] for entry in origin["files"].values()} | {
        "ORIGIN.json",
        "README.md",
    }
    actual = {path.relative_to(source).as_posix() for path in source.rglob("*") if path.is_file()}
    if actual != expected:
        raise ValueError("Packaged producer file membership differs")
    destination.mkdir(parents=True, exist_ok=False)
    initialize(destination)
    _git(
        destination,
        "remote",
        "set-url",
        "origin",
        "https://github.com/CultureBotAI/culturebotai-claw.git",
    )
    for name, raw in captured.items():
        path = destination / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(raw)
    _json(
        destination / "SYNTHETIC_PRODUCER.json",
        {
            "schema_version": 1,
            "scope": "Test-only reconstruction of exact reviewed upstream source",
            "upstream_revision": CLAW_REVISION,
            "upstream_manifest_sha256": PACKAGED_ORIGIN_SHA256,
            "actual_git_head_is_synthetic": True,
            "source_files": {name: sha(raw) for name, raw in captured.items()},
        },
    )
    synthetic = commit(destination)
    if synthetic == CLAW_REVISION:
        raise ValueError("Synthetic source checkout must not impersonate the upstream revision")
    return destination


class NativeReviewAdoptionFixture(Fixture):
    """Retain the existing complete fixture, using the native immutable saver."""

    def save_report(self, report):
        return self.native.save_review(
            self.root, report, schema_path=self.root / "schema/record_review.yaml"
        )


def completed_adoption(
    tmp: Path, monkeypatch, *, additional_sources=None
) -> NativeReviewAdoptionFixture:
    """Return three current owners and an actually verified adoption receipt.

    Exact has one synthetic external assertion, New is an accepted concept with
    a role hold and no external mapping, Move retains its existing identity,
    and Held is withheld. The raw New alias on Exact produces actual owned-name
    suppression after New is admitted. All owner inputs precede adoption.
    """
    tmp.mkdir(parents=True, exist_ok=True)
    fixture = NativeReviewAdoptionFixture(
        tmp,
        monkeypatch,
        additional_sources=additional_sources,
        original_records=[
            {
                "identifier": "NCIT:C80300",
                "preferred_term": "Exact",
                "mapping_status": "MAPPED",
                "ontology_mapping": {
                    "ontology_id": "NCIT:C80300",
                    "ontology_label": "Maltose Monohydrate",
                    "ontology_source": "NCIT",
                    "mapping_quality": "EXACT_MATCH",
                },
                "synonyms": [{"synonym_text": "New", "synonym_type": "RAW_TEXT"}],
                "curation_history": [],
            },
            {
                "identifier": "UNMAPPED_1",
                "preferred_term": "Move",
                "mapping_status": "UNMAPPED",
                "curation_history": [],
            },
        ],
    )
    # This deliberately historical fixture is an input, not a generated or
    # approved candidate. Its provenance cells give the new publication tests
    # a real beforeimage whose obligations cannot silently disappear.
    canonical = fixture.root / CANONICAL
    canonical.parent.mkdir(parents=True, exist_ok=True)
    content = io.StringIO()
    content.write(
        "# mapping_set_id: https://example.invalid/synthetic-prior-mapping\n"
        "# license: https://creativecommons.org/publicdomain/zero/1.0/\n"
        "# predicate_semantics: skos\n"
        "# curie_map:\n"
        "#   MIM: https://example.invalid/legacy-name/\n"
        "#   NCIT: http://purl.obolibrary.org/obo/NCIT_\n"
        "#   skos: http://www.w3.org/2004/02/skos/core#\n"
        "#   semapv: https://w3id.org/semapv/vocab/\n"
        "#   obo: http://purl.obolibrary.org/obo/\n"
    )
    writer = csv.DictWriter(content, fieldnames=COLUMNS, delimiter="\t", lineterminator="\n")
    writer.writeheader()
    writer.writerow(
        {
            "subject_id": "MIM:Exact",
            "subject_label": "Exact",
            "predicate_id": "skos:exactMatch",
            "object_id": "NCIT:C80300",
            "object_label": "Maltose Monohydrate",
            "object_source": "obo:ncit.owl",
            "mapping_justification": "semapv:ManualMappingCuration",
            "source": "MIM:synthetic-original-source",
            "mapping_date": "2026-01-01",
            "confidence": "0.99",
            "comment": "Synthetic original provenance comment",
            "other": "New",
            "validation_method": "synthetic-prior-stamp",
        }
    )
    canonical.write_text(content.getvalue(), encoding="utf-8")
    fixture.prepare()
    fixture.accept()
    result = api.apply(
        fixture.root,
        fixture.stage,
        fixture.acceptance,
        fixture.receipt,
        enabled=True,
    )
    assert result["state"] == "COMPLETE"
    assert (
        api.verify_completed(
            fixture.root,
            fixture.stage,
            fixture.receipt / "application.json",
        )["status"]
        == "COMPLETE_CURRENT_CANDIDATE"
    )
    assert not (fixture.root / fixture.held).exists()
    return fixture


def generate_diagnostic(
    fixture: NativeReviewAdoptionFixture,
    producer_root: Path,
    *,
    directory: Path | None = None,
) -> dict:
    """Run the actual c1 CLI once, preserving stdout/stderr and runtime evidence.

    The caller selects the read-only producer checkout explicitly. A failing
    child leaves its outputs and evidence in this fixture's durable directory.
    No provider function, lease, validation gate or source loader is replaced.
    """
    if sys.version_info[:2] != (3, 13):
        raise ValueError("The publication fixture requires maintained Python 3.13")
    producer_root = producer_root.absolute()
    if any(path.is_symlink() for path in (producer_root, *producer_root.parents)):
        raise ValueError("The fixture producer must use its original unaliased path")
    if _git(producer_root, "rev-parse", "HEAD") != CLAW_REVISION:
        raise ValueError("Fixture requires the explicitly reviewed c1 Claw producer")
    paths = (
        "scripts/build_mim_ingredient_sssom.py",
        "scripts/kgm_unified_mappings.py",
        "plugins/lock_manager.py",
        "src/kg_microbe_utils",
        "src/kg_microbe_write",
        "src/kg_microbe_fleet",
    )
    if _git(producer_root, "status", "--porcelain", "--", *paths):
        raise ValueError("Fixture Claw producer has changed tracked or untracked source")
    directory = directory or fixture.root / ".temp/stable-diagnostic"
    directory = directory.absolute()
    directory.relative_to(fixture.root)
    directory.mkdir(parents=True, exist_ok=False)
    kgm = directory / "synthetic-kg-microbe"
    initialize(kgm)
    mappings = kgm / "mappings"
    mappings.mkdir()
    # Complete, empty synthetic KG source. NCIT does not call the CHEBI loader.
    (mappings / "kgmicrobe_unified_entity_mappings.sssom.tsv.gz").write_bytes(
        gzip.compress(
            b"subject_id\tsubject_label\tpredicate_id\tobject_id\tobject_label\tsource\n",
            mtime=0,
        )
    )
    commit(kgm)
    output = directory / "candidate.sssom.tsv"
    sidecar = directory / "candidate.suppressed.tsv"
    manifest = directory / "candidate.generation.json"
    contract = fixture.root / "src/mediaingredientmech/stable_ids.py"
    selected_environment = {
        "MEDIAINGREDIENTMECH_ROOT": str(fixture.root),
        "KGMICROBE_ROOT": str(kgm),
        "OPENCLAW_WORKSPACE": os.environ["OPENCLAW_WORKSPACE"],
        "PYTHONPATH": os.pathsep.join((str(fixture.root / "src"), str(producer_root / "src"))),
        "PYTHONDONTWRITEBYTECODE": "1",
        "GIT_NO_LAZY_FETCH": "1",
        "GIT_TERMINAL_PROMPT": "0",
        "PATH": str(Path(sys.executable).parent) + os.pathsep + os.environ.get("PATH", ""),
    }
    validator = shutil.which("sssom", path=selected_environment["PATH"])
    if not validator:
        raise ValueError("Actual sssom CLI is required; the fixture does not skip validation")
    argv = [
        sys.executable,
        "-B",
        str(producer_root / "scripts/build_mim_ingredient_sssom.py"),
        "--identity-mode",
        "stable",
        "--mim-stable-id-contract-sha256",
        sha(contract.read_bytes()),
        "--output",
        str(output),
        "--suppressed-aliases-output",
        str(sidecar),
        "--generation-manifest-output",
        str(manifest),
        "--prior-stamps-from",
        str(fixture.root / CANONICAL),
    ]
    before = (fixture.root / CANONICAL).read_bytes()
    assert (
        api.verify_completed(
            fixture.root,
            fixture.stage,
            fixture.receipt / "application.json",
        )["status"]
        == "COMPLETE_CURRENT_CANDIDATE"
    )
    evidence = {
        "schema_version": 1,
        "purpose": "Synthetic native adoption and stable diagnostic fixture; no scientific campaign approval",
        "started_at": now(),
        "command": argv,
        "cwd": str(fixture.root),
        "selected_environment": selected_environment,
        "python": {
            "executable": sys.executable,
            "resolved_executable": str(Path(sys.executable).resolve()),
            "version": sys.version,
            "executable_sha256": sha(Path(sys.executable).read_bytes()),
        },
        "sssom": {
            "executable": validator,
            "executable_sha256": sha(Path(validator).read_bytes()),
            "version": importlib.metadata.version("sssom"),
        },
        "producer": {"root": str(producer_root), "revision": CLAW_REVISION},
        "mim_revision": _git(fixture.root, "rev-parse", "HEAD"),
        "kg_microbe_revision": _git(kgm, "rev-parse", "HEAD"),
        "adoption_stage": str(fixture.stage),
        "adoption_receipt": str(fixture.receipt / "application.json"),
        "canonical_before_sha256": sha(before),
    }
    failure = None
    try:
        run = subprocess.run(
            argv,
            cwd=fixture.root,
            env={**os.environ, **selected_environment},
            capture_output=True,
            timeout=180,
        )
        stdout, stderr, exit_code = run.stdout, run.stderr, run.returncode
    except subprocess.TimeoutExpired as exc:
        stdout, stderr, exit_code = exc.stdout or b"", exc.stderr or b"", None
        failure = "Native stable diagnostic exceeded 180 seconds"
    for name, content in (("stdout.txt", stdout), ("stderr.txt", stderr)):
        with (directory / name).open("xb") as handle:
            handle.write(content)
    evidence.update(
        finished_at=now(),
        exit_code=exit_code,
        failure=failure,
        stdout_sha256=sha(stdout),
        stderr_sha256=sha(stderr),
        artifacts={
            str(path): sha(path.read_bytes()) if path.exists() else None
            for path in (output, sidecar, manifest)
        },
    )
    runtime = directory / "runtime.json"
    _json(runtime, evidence)
    if failure or exit_code != 0:
        raise AssertionError(
            f"Native stable generation failed; evidence: {runtime}; {failure or exit_code}"
        )
    generated = json.loads(manifest.read_bytes())
    assert generated["schema_version"] == 1
    assert generated["policy_version"] == "owned-name-policy-v1"
    assert generated["identity_mode"] == "stable"
    assert generated["external_sssom_validation"] == "passed"
    assert generated["source_revisions"] == {
        "claw": CLAW_REVISION,
        "mim": evidence["mim_revision"],
        "kg_microbe": evidence["kg_microbe_revision"],
    }
    assert generated["stable_id_contract_sha256"] == sha(contract.read_bytes())
    assert generated["source_binding_candidate"] is None
    assert generated["artifacts"] == [
        {"role": role, "path": str(path), "sha256": sha(path.read_bytes())}
        for role, path in (("sssom", output), ("suppressed_aliases", sidecar))
    ]
    assert len(generated["owner_subjects"]) == 3
    assert generated["emitted_rows"] == 1
    accounting = {row["subject_id"]: row for row in generated["owner_candidate_accounting"]}
    assert accounting["MIM:0000001"]["external_candidate_rows"] == 1
    assert accounting["MIM:0000003"]["external_candidate_rows"] == 0
    assert all(row["scientific_approval_added"] is False for row in accounting.values())
    suppressed = list(csv.DictReader(io.StringIO(sidecar.read_text()), delimiter="\t"))
    assert any(
        row["subject_id"] == "MIM:0000001"
        and row["token_key"] == "new"
        and json.loads(row["owner_subject_ids"]) == ["MIM:0000003"]
        for row in suppressed
    )
    for pin in generated["source_inputs"]:
        path = Path(pin["path"])
        assert (sha(path.read_bytes()) if path.exists() else None) == pin["sha256"]
    for name, digest in generated["producer_import_snapshot"].items():
        assert sha(Path(name).read_bytes()) == digest
    assert (fixture.root / CANONICAL).read_bytes() == before
    assert (
        api.verify_completed(
            fixture.root,
            fixture.stage,
            fixture.receipt / "application.json",
        )["status"]
        == "COMPLETE_CURRENT_CANDIDATE"
    )
    return {
        "sssom": output,
        "suppressed_aliases": sidecar,
        "manifest": manifest,
        "runtime": runtime,
        "generation": generated,
    }
