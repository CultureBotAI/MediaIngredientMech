#!/usr/bin/env python3
"""Apply the bounded #901 sodium-perchlorate form correction with exact guarded source/promotion receipts.

Dry-run by default. CLI owns the configured native lock; Python callers must hold
it. Neither source correction nor native generation grants scientific approval.
"""

from __future__ import annotations

import argparse
import copy
import csv
import datetime
import json
import subprocess
import sys
import tempfile
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(ROOT / "src"))
from mediaingredientmech.curate.curation_event import record_curation_event  # noqa: E402
from mediaingredientmech.validation.write_validated import (  # noqa: E402
    validate_ingredient,
    write_validated_ingredient,
)
from scripts import apply_owned_name_policy as policy  # noqa: E402
from scripts import promote_heptahydrate_ncit as guarded  # noqa: E402
from scripts import promote_owned_name_policy as native  # noqa: E402
from scripts.bump_sssom_header import newest_row_date, rewrite  # noqa: E402

RECORD = "data/ingredients/mapped/Sodium_Perchlorate_Monohydrate.yaml"
BEFORE_SHA256 = "1f39286747eb8f3a2ec3da7919f9e6cb197221fcfef46af69a6784afd8f83ccc"
ACTION = "CORRECTED_HYDRATE_PARENT_PREDICATE"
CURATOR = "claude"
EVIDENCE_SOURCE = "MIM curation (#901); PubChem CID 516899; ChEBI:132103"
VERIFICATION = (
    "PubChem CID 516899 records CAS 7791-07-3 and formula ClH2NaO5; its "
    "water-containing InChI agrees with this monohydrate. CHEBI:132103 sodium "
    "perchlorate has the distinct water-free formula ClO4.Na and CAS 7601-89-0. "
    "Current MAPPING_SEMANTICS section 3 and its form-of ruling support the "
    "identity-retaining parent broadMatch and native B1 repair authorized by "
    "#901 comment 6565222455, not subclass projection or exact parent identity. "
    "The bounded searches did not resolve an exact eligible grounding. "
    "SNOMED 765356005 remains an unverified label-only lead: primary concept "
    "access was blocked and the native source enum lacks SNOMED. This does not "
    "establish global absence or disprove an exact term, and grants no registry "
    "workaround. Sigma71852 was not inspected because the request timed out. "
    "No role or release approval is implied. Archived sources: "
    "https://pubchem.ncbi.nlm.nih.gov/compound/516899 ; "
    "https://www.ebi.ac.uk/chebi/CHEBI:132103 ."
)
CHANGE = (
    "Corrected CLOSE_MATCH to NARROW_MATCH for the sodium perchlorate parent "
    "CHEBI:132103 under the current form-of ruling (#901); the SSSOM predicate "
    "is skos:broadMatch with required native B1 handle "
    "kgmicrobe.compound:sodium_perchlorate_monohydrate. Retained primary "
    "cas:7791-07-3, chemistry, synonyms, counts and ELECTRON_ACCEPTOR role "
    "with its existing publication, context and confidence. Historical #342 "
    "reasoning remains provenance. The unresolved SNOMED exact-term lead is "
    "not dismissed; this bounded predicate/handle repair grants no scientific "
    "or role approval, and the changed owner withdraws its old role approval."
)
EVIDENCE_NOT_BEFORE = "2026-11-01T22:11:57.373022+00:00"


OWNER = Path(RECORD)
SSSOM = Path("mappings/ingredient_mappings.sssom.tsv")
BASELINE = Path("mappings/other_cross_record_baseline.tsv")
SIDECAR = Path("mappings/suppressed_aliases.tsv")
MANIFEST = Path("mappings/ingredient_mappings.sssom.tsv.manifest.json")
FIXTURE = ROOT / "tests/fixtures/issue901-sodium-perchlorate-owner-before.yaml"
EVIDENCE = Path("reports/sodium_perchlorate_form_901_20261101/source-evidence.json")
EVIDENCE_SHA = "e4fdd650cd72d9b9c915c461504aa760a564863d245eb7b365e8e50a25499236"
SUBJECT = "MIM:Sodium_Perchlorate_Monohydrate"
IDENTITY = "cas:7791-07-3"
PARENT = "CHEBI:132103"
HANDLE = "kgmicrobe.compound:sodium_perchlorate_monohydrate"
NAME = "Sodium perchlorate monohydrate"
PRODUCER = "9bd09b2ba163212a65289b91313f98cb0937476f"
APPROVAL = (
    "NONE: source/form correction only; every changed claim requires fresh mapping-specific review."
)
BEFORE = {
    OWNER: BEFORE_SHA256,
    SSSOM: "51b268361cd8e5134eb03d22fbf11ab1dd1cdcee0eee58a1cfd1ada02a193f28",
    BASELINE: "f52921f8cf4aaf16f070b9b33bb8809e0a7ee809f7a66805bdf7bd01c9610bcb",
    SIDECAR: "3d1e6c1f6393aaf05b8f7235c5393372206ea0f73db0699ddbdca14053bf8f84",
    MANIFEST: "d12d0ce5a97650d2bc7f224f93e1394949029668546be1178fe1a7e22af4f091",
}
_CODE = Path(__file__).read_bytes()
digest = guarded.digest
require = native.require
regular = policy.regular
checked_root = policy.checked_root
ingredient_paths = policy.ingredient_paths
encoded = native.encoded


def bound_path(path: Path) -> Path:
    """Require a canonical absolute identity before binding a receipt or artifact."""
    absolute = Path(path).absolute()
    require(absolute == absolute.resolve(), "Receipt/input path must be resolved without aliases")
    return absolute


def corrected_record(record: dict, *, timestamp: str | None = None) -> dict | None:
    """Return a validated proposal, refusing related forms and unexpected state."""
    mapping = record.get("ontology_mapping") or {}
    chemistry = record.get("chemical_properties") or {}
    expected = {
        "identifier": "cas:7791-07-3",
        "preferred_term": "Sodium perchlorate monohydrate",
        "mapping_status": "MAPPED",
    }
    if any(record.get(key) != value for key, value in expected.items()):
        raise ValueError("The reviewed monohydrate identity no longer matches")
    if any(
        mapping.get(key) != value
        for key, value in {
            "ontology_id": "CHEBI:132103",
            "ontology_label": "sodium perchlorate",
            "ontology_source": "CHEBI",
        }.items()
    ):
        raise ValueError("The reviewed anhydrous parent no longer matches")
    if any(
        chemistry.get(key) != value
        for key, value in {
            "cas_rn": "7791-07-3",
            "molecular_formula": "ClH2NaO5",
            "pubchem_cid": 516899,
        }.items()
    ):
        raise ValueError("The reviewed monohydrate chemistry no longer matches")
    own_evidence = [e for e in mapping.get("evidence", []) if e.get("source") == EVIDENCE_SOURCE]
    own_history = [
        e
        for e in record.get("curation_history", [])
        if e.get("action") == ACTION and e.get("changes") == CHANGE
    ]
    if mapping.get("mapping_quality") == "NARROW_MATCH":
        if (
            len(own_evidence) == len(own_history) == 1
            and own_evidence[0].get("notes") == VERIFICATION
        ):
            errors = validate_ingredient(record)
            if errors:
                raise ValueError(
                    f"Completed proposal fails native closed-schema validation: {errors}"
                )
            return None
        raise ValueError("An existing NARROW_MATCH is not this reviewed correction")
    if mapping.get("mapping_quality") != "CLOSE_MATCH" or own_evidence or own_history:
        raise ValueError("Unexpected mapping quality or partial prior correction")
    proposal = copy.deepcopy(record)
    proposal["ontology_mapping"]["mapping_quality"] = "NARROW_MATCH"
    proposal["ontology_mapping"].setdefault("evidence", []).append(
        {
            "evidence_type": "DATABASE_MATCH",
            "source": EVIDENCE_SOURCE,
            "notes": VERIFICATION,
        }
    )
    record_curation_event(
        proposal,
        curator=CURATOR,
        action=ACTION,
        changes=CHANGE,
        previous_status="MAPPED",
        new_status="MAPPED",
        llm_assisted=True,
        llm_model="gpt-6",
        timestamp=timestamp,
    )
    errors = validate_ingredient(proposal)
    if errors:
        raise ValueError(f"Proposed record fails native closed-schema validation: {errors}")
    return proposal


def frozen_owner() -> bytes:
    data = regular(FIXTURE)
    require(digest(data) == BEFORE[OWNER], "Immutable owner preimage changed")
    return data


def render(record: dict) -> bytes:
    with tempfile.TemporaryDirectory(prefix="mim-901-render-") as temporary:
        path = Path(temporary) / "record.yaml"
        write_validated_ingredient(record, path)
        return path.read_bytes()


def propose_record(before: bytes, *, timestamp: str) -> bytes:
    require(digest(before) == BEFORE[OWNER], "Owner differs from reviewed preimage")
    when = datetime.datetime.fromisoformat(timestamp)
    require(
        when.utcoffset() == datetime.timedelta(0)
        and when >= datetime.datetime.fromisoformat(EVIDENCE_NOT_BEFORE),
        "Correction timestamp must be UTC after captured evidence",
    )
    proposal = corrected_record(yaml.safe_load(before), timestamp=timestamp)
    require(proposal is not None, "Preimage is already corrected")
    return render(proposal)


def complete_owner(current: bytes) -> None:
    try:
        stamp = yaml.safe_load(current)["curation_history"][-1]["timestamp"]
        expected = propose_record(frozen_owner(), timestamp=stamp)
    except (KeyError, TypeError, IndexError) as error:
        raise ValueError("Incomplete source correction") from error
    require(current == expected, "Completed owner differs from exact correction")


def evidence_inputs(root: Path, evidence: Path) -> dict[Path, bytes]:
    evidence = bound_path(evidence)
    raw = regular(evidence)
    require(digest(raw) == EVIDENCE_SHA, "Reviewed source manifest changed")
    doc = json.loads(raw)
    expected = {
        "schema_version": "1.0.0",
        "owner_record": RECORD,
        "owner_before_sha256": BEFORE[OWNER],
        "primary_identifier": IDENTITY,
        "parent_identifier": PARENT,
        "pubchem_cid": 516899,
        "evidence_not_before": EVIDENCE_NOT_BEFORE,
    }
    require(all(doc.get(k) == v for k, v in expected.items()), "Evidence identity contract differs")
    require({d["issue"] for d in doc["decisions"]} == {901}, "Evidence decisions differ")
    result = {evidence: raw}
    require(bool(doc["files"]), "Source evidence has no captures")
    for name, info in doc["files"].items():
        path = Path(name)
        require(not path.is_absolute() and ".." not in path.parts, "Unsafe source evidence path")
        data = regular(root / path)
        require(
            digest(data) == info["sha256"] and len(data) == info["bytes"], "Source capture changed"
        )
        result[root / path] = data
    return result


def code_inputs() -> dict[Path, bytes]:
    require(regular(Path(__file__)) == _CODE, "Loaded writer source changed")
    require(regular(Path(native.__file__)) == native._CODE, "Loaded replay source changed")
    for path, loaded in policy._LOADED_CODE.items():
        require(regular(path) == loaded, "Loaded shared dependency changed")
    paths = [
        Path(__file__),
        Path(guarded.__file__),
        Path(native.__file__),
        Path(policy.__file__),
        FIXTURE,
        ROOT / "scripts/bump_sssom_header.py",
        ROOT / "MAPPING_SEMANTICS.md",
        ROOT / "justfile",
        ROOT / "pyproject.toml",
        ROOT / "uv.lock",
        ROOT / "src/mediaingredientmech/curate/apply_receipt.py",
        ROOT / "src/mediaingredientmech/curate/curation_event.py",
        ROOT / "src/mediaingredientmech/validation/write_validated.py",
        ROOT / "src/mediaingredientmech/schema/mediaingredientmech.yaml",
    ]
    return {path: regular(path) for path in paths}


def validate_scope(root: Path, inputs: dict[Path, bytes], paths: set[Path]) -> None:
    policy.validate_scope(root, inputs, paths)
    for path in paths - {root / OWNER}:
        record = yaml.safe_load(inputs[path])
        if isinstance(record, dict) and record.get("mapping_status") != "REJECTED":
            require(
                record.get("identifier") not in {IDENTITY, HANDLE},
                "Another active owner claims this identity",
            )


def backups(log: Path) -> dict[Path, Path]:
    return {path: log.with_name(log.stem + ".before-" + path.name) for path in BEFORE}


def source_context(root: Path, evidence: Path, current: bytes, original: dict[Path, bytes]):
    complete_owner(current)
    paths = ingredient_paths(root)
    inputs = {path: regular(path) for path in paths}
    inputs.update({root / path: regular(root / path) for path in BEFORE})
    inputs.update(evidence_inputs(root, evidence) | code_inputs())
    for path, content in original.items():
        require(digest(content) == BEFORE[path], "Source anchor preimage changed")
    historical = dict(inputs)
    historical.update({root / path: content for path, content in original.items()})
    record = yaml.safe_load(current)
    result = {
        "phase": "sources",
        "approval": APPROVAL,
        "timestamp": record["curation_history"][-1]["timestamp"],
        "evidence_manifest": str(evidence),
        "evidence_manifest_sha256": EVIDENCE_SHA,
        "input_sha256": {str(path): digest(data) for path, data in historical.items()},
        "output_sha256": {str(OWNER): digest(current)},
        "sssom_before_sha256": BEFORE[SSSOM],
        "baseline_before_sha256": BEFORE[BASELINE],
        "records": [
            {
                "source_record": RECORD,
                "shape": "hydrate_parent_predicate",
                "before_yaml_sha256": BEFORE[OWNER],
                "after_yaml_sha256": digest(current),
                "change": CHANGE,
                "verification": VERIFICATION,
            }
        ],
    }
    validate_scope(root, inputs, paths)
    return inputs, result, paths


def source_receipt(root: Path, log: Path):
    root, log = checked_root(root), bound_path(log)
    current = regular(root / OWNER)
    saved = json.loads(regular(log))
    original = {path: regular(backup) for path, backup in backups(log).items()}
    inputs, expected, paths = source_context(
        root, Path(saved["evidence_manifest"]), current, original
    )
    inputs[log] = policy.completed_receipt(log, expected, root, changed={OWNER})
    inputs.update({backup: original[path] for path, backup in backups(log).items()})
    validate_scope(root, inputs, paths)
    return inputs, saved


def apply_sources(
    root: Path, evidence: Path, log: Path, *, apply: bool = False, promotion_log: Path | None = None
):
    root, evidence, log = checked_root(root), bound_path(evidence), bound_path(log)
    original = {path: regular(root / path) for path in BEFORE}
    if digest(original[OWNER]) != BEFORE[OWNER]:
        source_receipt(root, log)
        if all(digest(original[p]) == BEFORE[p] for p in BEFORE if p != OWNER):
            return {"applied": False, "changed": False, "approval": APPROVAL}
        require(
            promotion_log is not None,
            "Changed canonical anchors require original completed promotion receipt",
        )
        verify_completed(root, promotion_log, source_log=log)
        return {"applied": False, "changed": False, "approval": APPROVAL}
    for path, data in original.items():
        require(digest(data) == BEFORE[path], "Original source/canonical anchor differs")
    current = propose_record(
        original[OWNER], timestamp=datetime.datetime.now(datetime.timezone.utc).isoformat()
    )
    inputs, result, paths = source_context(root, evidence, current, original)
    return guarded.publish(
        root,
        {OWNER: current},
        inputs,
        log,
        {backup: original[path] for path, backup in backups(log).items()},
        result,
        apply=apply,
        validate_scope=lambda: validate_scope(root, inputs, paths),
    )


def table(data: bytes):
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


def promoted_sssom(before: bytes, candidate: bytes, current: bytes) -> bytes:
    complete_owner(current)
    header, fields, prior = table(before)
    _, candidate_fields, generated = table(candidate)
    require(fields == candidate_fields, "Candidate columns differ")
    old = {r["object_id"]: r for r, _ in prior if r["subject_id"] == SUBJECT}
    target = [(r, line) for r, line in generated if r["subject_id"] == SUBJECT]
    require(len(old) == 2 and set(old) == {PARENT, IDENTITY}, "Prior target rows differ")
    require(
        len(target) == 3 and {r["object_id"] for r, _ in target} == {PARENT, IDENTITY, HANDLE},
        "Missing, duplicated or wrong target triplet",
    )
    record = yaml.safe_load(current)
    for row, _ in target:
        obj = row["object_id"]
        require(row["subject_label"] == NAME, "Candidate subject label differs")
        require(
            row["predicate_id"] == ("skos:broadMatch" if obj == PARENT else "skos:exactMatch"),
            "Candidate form predicate differs",
        )
        require(
            row["object_label"] == ("sodium perchlorate" if obj == PARENT else NAME),
            "Candidate target label differs",
        )
        require(
            row["other"] == ("" if obj == PARENT else "CAS:7791-07-3"),
            "Unreviewed candidate token",
        )
        require(
            row["mapping_date"] == record["curation_history"][-1]["timestamp"][:10],
            "Candidate date differs",
        )
        require(
            row["validation_method"]
            == (old[IDENTITY]["validation_method"] if obj == IDENTITY else ""),
            "Native prior validation stamp differs",
        )
        if obj == IDENTITY:
            require(row["comment"] == old[IDENTITY]["comment"], "CAS provenance comment differs")
        require(
            "MIM:curator=claude" in row["source"].split("|"),
            "Candidate lacks actual curator source",
        )
    by_object = {r["object_id"]: line for r, line in target}
    out = [
        (by_object[row["object_id"]] if row["subject_id"] == SUBJECT else line)
        for row, line in prior
    ]
    # Existing positions remain stable; the new handle follows the old rows.
    result = ("".join(header) + "".join(out) + by_object[HANDLE]).encode()
    lines = result.decode().splitlines(keepends=True)
    date = newest_row_date(lines)
    require(date is not None, "Projected mapping date absent")
    updated, _ = rewrite(lines, date)
    return "".join(updated).encode()


def generation_inputs(
    root: Path, bundle: Path, producer: Path, source_log: Path, manifest_sha256: str
):
    """Bind merged producer bytes and exact offline replay, with no ontology calls."""
    bound, saved = source_receipt(root, source_log)
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
        before == after and receipt["input_bytes_unchanged"] is True,
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
    prior = backups(source_log)[SSSOM]
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
        [sys.executable, "-I", "-c", native._REPLAY, str(producer), str(bundle), str(prior)],
        capture_output=True,
        text=True,
        check=False,
    )
    require(replay.returncode == 0, "Exact native replay failed: " + replay.stderr[-4000:])
    result = json.loads(replay.stdout)
    require(result["rows"] == manifest["emitted_rows"], "Native replay row count differs")
    return bound, saved, result, producers, label_paths, absent


def promotion_manifest(
    before: bytes,
    canonical: bytes,
    current: bytes,
    source_log: Path,
    generation_manifest_sha256: str,
    generation_receipt_sha256: str,
    source_sha256: str,
) -> bytes:
    source_log = bound_path(source_log)
    doc = json.loads(before)
    require(
        doc.get("schema_version") == 1 and doc.get("policy_version") == "owned-name-policy-v1",
        "Prior policy manifest contract differs",
    )
    require(
        doc["artifacts"] == {str(path): BEFORE[path] for path in (SSSOM, SIDECAR, BASELINE)}
        and doc["source_owner_sha256"][RECORD] == BEFORE[OWNER],
        "Prior policy artifact binding differs",
    )
    prefix = copy.deepcopy(doc.get("form_projection_updates"))
    require(
        isinstance(prefix, list)
        and len(prefix) == 1
        and prefix[0].get("source_record")
        == "data/ingredients/mapped/D-_-melezitose_Monohydrate.yaml",
        "Expected the preserved melezitose form-projection prefix",
    )
    doc["artifacts"][str(SSSOM)] = digest(canonical)
    doc["source_owner_sha256"][RECORD] = digest(current)
    doc["form_projection_updates"] = [
        *prefix,
        {
            "issue": 901,
            "scope": "Sodium perchlorate monohydrate parent/CAS/B1 triplet; original policy decisions, melezitose prefix and generation attribution retained",
            "approval": APPROVAL,
            "prior_manifest_sha256": digest(before),
            "source_record": RECORD,
            "owner_before_sha256": BEFORE[OWNER],
            "owner_after_sha256": digest(current),
            "source_receipt": str(source_log),
            "source_receipt_sha256": source_sha256,
            "generation_manifest_sha256": generation_manifest_sha256,
            "generation_receipt_sha256": generation_receipt_sha256,
            "sssom_before_sha256": BEFORE[SSSOM],
            "sssom_after_sha256": digest(canonical),
            "sidecar_sha256": BEFORE[SIDECAR],
            "baseline_sha256": BEFORE[BASELINE],
        },
    ]
    return encoded(doc)


def promote(
    root: Path,
    bundle: Path,
    producer: Path,
    source_log: Path,
    log: Path,
    *,
    generation_manifest_sha256: str,
    apply: bool = False,
):
    root, bundle, producer = checked_root(root), checked_root(bundle), checked_root(producer)
    source_log, log = bound_path(source_log), bound_path(log)
    inputs, saved, replay, producers, labels, absent = generation_inputs(
        root, bundle, producer, source_log, generation_manifest_sha256
    )
    current = inputs[root / OWNER]
    original = {path: inputs[backup] for path, backup in backups(source_log).items()}
    canonical = promoted_sssom(original[SSSOM], inputs[bundle / "candidate.sssom.tsv"], current)
    projection = promotion_manifest(
        original[MANIFEST],
        canonical,
        current,
        source_log,
        generation_manifest_sha256,
        digest(inputs[bundle / "generation-receipt.json"]),
        digest(inputs[source_log]),
    )
    outputs = {SSSOM: canonical, MANIFEST: projection}
    for path in (BASELINE, SIDECAR):
        require(regular(root / path) == original[path], "Deferred policy/sidecar bytes changed")
    actual = {path: regular(root / path) for path in outputs}
    inputs.update({root / path: data for path, data in actual.items()})
    paths = ingredient_paths(root)
    result = {
        "phase": "promote",
        "approval": APPROVAL,
        "records": saved["records"],
        "source_log": str(source_log),
        "bundle": str(bundle),
        "producer": str(producer),
        "generation_manifest_sha256": generation_manifest_sha256,
        "source_receipt_sha256": digest(inputs[source_log]),
        "input_sha256": {
            str(p): digest(b) for p, b in inputs.items() if p not in {root / p for p in outputs}
        },
        "output_sha256": {str(p): digest(b) for p, b in outputs.items()},
        "sssom_before_sha256": BEFORE[SSSOM],
        "sssom_after_sha256": digest(canonical),
        "native_replay": replay,
        "changed_subjects": [SUBJECT],
        "added_rows": 1,
        "removed_rows": 0,
    }

    def check():
        validate_scope(root, inputs, paths)
        require(
            native.producer_paths(producer) == producers, "Producer dependency membership changed"
        )
        require(
            set(bundle.glob("label-input-*.json")) == labels, "Label receipt membership changed"
        )
        for path in absent:
            require(not path.exists() and not path.is_symlink(), "Absent generation input appeared")

    check()
    promotion_backups = {path: log.with_name(log.stem + ".before-" + path.name) for path in outputs}
    if actual == outputs:
        policy.completed_receipt(log, result, root, changed=set(outputs))
        for path, backup in promotion_backups.items():
            require(regular(backup) == original[path], "Promotion beforeimage changed")
        return {"applied": False, "changed": False, "approval": APPROVAL}
    require(
        actual == {path: original[path] for path in outputs},
        "Partial or changed canonical promotion",
    )
    return guarded.publish(
        root,
        outputs,
        inputs,
        log,
        {backup: original[path] for path, backup in promotion_backups.items()},
        result,
        apply=apply,
        validate_scope=check,
    )


def verify_completed(root: Path, promotion_log: Path, *, source_log: Path):
    saved = json.loads(regular(promotion_log))
    require(
        saved.get("phase") == "promote"
        and saved.get("state") == "complete"
        and saved.get("source_log") == str(bound_path(source_log)),
        "Completed promotion receipt required",
    )
    result = promote(
        root,
        Path(saved["bundle"]),
        Path(saved["producer"]),
        source_log,
        promotion_log,
        generation_manifest_sha256=saved["generation_manifest_sha256"],
    )
    require(result.get("changed") is False, "Promotion is not complete")
    return result


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("phase", choices=("sources", "promote"))
    parser.add_argument("--root", type=Path, default=ROOT)
    parser.add_argument("--log", type=Path, required=True)
    parser.add_argument("--evidence", type=Path)
    parser.add_argument("--source-log", type=Path)
    parser.add_argument("--promotion-log", type=Path)
    parser.add_argument("--bundle", type=Path)
    parser.add_argument("--producer", type=Path)
    parser.add_argument("--generation-manifest-sha256")
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("--apply", action="store_true")
    mode.add_argument("--dry-run", action="store_true")
    args = parser.parse_args(argv)
    if args.phase == "promote" and not all(
        (args.source_log, args.bundle, args.producer, args.generation_manifest_sha256)
    ):
        parser.error("promote requires source-log, bundle, producer and generation-manifest-sha256")
    from plugins.lock_manager import LockManager
    from plugins.repository_settings import RepositorySettings

    root = checked_root(args.root)
    target = RepositorySettings.from_environment().get_target("mediaingredientmech")
    require(target.path.resolve() == root, "Configured MIM root differs")
    target.open()
    with LockManager().lock("mediaingredientmech", "#901 sodium perchlorate " + args.phase):
        if args.phase == "sources":
            result = apply_sources(
                root,
                args.evidence or root / EVIDENCE,
                args.log,
                apply=args.apply,
                promotion_log=args.promotion_log,
            )
        else:
            result = promote(
                root,
                args.bundle,
                args.producer,
                args.source_log,
                args.log,
                generation_manifest_sha256=args.generation_manifest_sha256,
                apply=args.apply,
            )
    print(json.dumps(result, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
