#!/usr/bin/env python3
"""Apply the bounded #753 Izalpinin existing-CAS correction with exact guarded source/promotion receipts.

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
from scripts import step7a_guarded_publication as publication  # noqa: E402
from scripts.bump_sssom_header import newest_row_date, rewrite  # noqa: E402

RECORD = "data/ingredients/mapped/Izalpinin.yaml"
BEFORE_SHA256 = "279a4bc187f755b580b834a85b7d6641b1b9836b08c8f007af405218acad1f7b"
ACTION = "CORRECTED_EXISTING_CAS_VALUE"
CURATOR = "claude"
EVIDENCE_SOURCE = "PubChem CID 5318691; MedChemExpress Izalpinin; MIM correction #753"
VERIFICATION = (
    "PubChem CID 5318691 names Izalpinin and lists CAS 480-14-8; the inspected "
    "MedChemExpress identity entry corroborates that name/CAS pair. This corrects "
    "the existing invalid 480-14-4 assertion, not merely its computed check digit. "
    "The primary LIPID MAPS record LMPK12111656 and nonobsolete OLS class agree "
    "with PubChem on CID, formula, InChI and InChIKey. That exact candidate is "
    "known, but current native source/prefix contracts do not support it. "
    "Final primary identity and source eligibility remain OPEN; retain WITHHOLD. "
    "This note supersedes the historical global-absence wording without deleting "
    "it. The failed authenticated CAS lookup is retained; this is not CAS Registry "
    "certification. The manufacturer is not inferred to have supplied the original "
    "CultureBotHT material, and its marketing chemical-class wording is not adopted. "
    "Sources: https://pubchem.ncbi.nlm.nih.gov/compound/5318691 ; "
    "https://www.medchemexpress.com/us/en/izalpinin.html ; "
    "https://www.lipidmaps.org/databases/lmsd/LMPK12111656 ."
)
CHANGE = (
    "Corrected existing invalid CAS 480-14-4 to source-backed 480-14-8 in identifier, "
    "CAS mapping target and chemical CAS property; updated only its active CAS "
    "provenance/retrieval timestamp and appended claim-specific evidence. "
    "Preserved all prior evidence/history, synonyms, counts, roles and other chemistry. "
    "Verified exact LIPIDMAPS:LMPK12111656 is a known candidate with native source "
    "eligibility and final primary-identity policy OPEN. Retain WITHHOLD: this partial "
    "registry-value repair grants no final CAS fallback or scientific approval."
)
EVIDENCE_NOT_BEFORE = "2026-11-02T01:26:34.872740+00:00"
OWNER = Path(RECORD)
SSSOM = Path("mappings/ingredient_mappings.sssom.tsv")
BASELINE = Path("mappings/other_cross_record_baseline.tsv")
SIDECAR = Path("mappings/suppressed_aliases.tsv")
MANIFEST = Path("mappings/ingredient_mappings.sssom.tsv.manifest.json")
REPORT = Path("reports/izalpinin_registry_753_20261101")
FIXTURE = ROOT / REPORT / "preimages/Izalpinin.yaml"
EVIDENCE = REPORT / "source-evidence.json"
EVIDENCE_SHA = "407a0dba0d455af7f01c98b9151c5f8f13527c494f160157c15eb3af032ea758"
SUBJECT = "MIM:Izalpinin"
OLD_IDENTITY = "cas:480-14-4"
IDENTITY = "cas:480-14-8"
NAME = "Izalpinin"
PRODUCER = "9bd09b2ba163212a65289b91313f98cb0937476f"
APPROVAL = "NONE: existing CAS-value correction only; retain WITHHOLD; final primary identity/source policy OPEN."
BEFORE = {
    OWNER: BEFORE_SHA256,
    SSSOM: "9a7a5cecf28c8b498116a42ce00869e915e7b564793f0fb6c1885a252721c16c",
    BASELINE: "f52921f8cf4aaf16f070b9b33bb8809e0a7ee809f7a66805bdf7bd01c9610bcb",
    SIDECAR: "3d1e6c1f6393aaf05b8f7235c5393372206ea0f73db0699ddbdca14053bf8f84",
    MANIFEST: "eee74e0281279a2e56fa595dce2fa0eb1ccca8728e4801241fc33d2c06dc53db",
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
    """Only the exact reviewed CAS-value correction; syntax grants no approval."""
    original = yaml.safe_load(frozen_owner())
    completed = record.get("identifier") == IDENTITY
    if completed:
        history = record.get("curation_history") or []
        require(bool(history), "Completed correction has no history")
        timestamp = history[-1].get("timestamp")
    else:
        require(record == original, "Unexpected owner identity, field or partial correction")
    proposal = copy.deepcopy(original)
    proposal["identifier"] = IDENTITY
    proposal["ontology_mapping"]["ontology_id"] = IDENTITY
    proposal["ontology_mapping"]["evidence"].append(
        {"evidence_type": "DATABASE_MATCH", "source": EVIDENCE_SOURCE, "notes": VERIFICATION}
    )
    proposal["chemical_properties"]["cas_rn"] = "480-14-8"
    proposal["chemical_properties"]["data_source"] = EVIDENCE_SOURCE
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
    proposal["chemical_properties"]["retrieval_date"] = proposal["curation_history"][-1][
        "timestamp"
    ]
    errors = validate_ingredient(proposal)
    require(not errors, f"Proposed record fails native closed-schema validation: {errors}")
    if completed:
        require(record == proposal, "Completed owner differs from exact correction")
        return None
    return proposal


def frozen_owner() -> bytes:
    data = regular(FIXTURE)
    require(digest(data) == BEFORE[OWNER], "Immutable owner preimage changed")
    return data


def render(record: dict) -> bytes:
    with tempfile.TemporaryDirectory(prefix="mim-753-render-") as temporary:
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
        "incorrect_identifier": OLD_IDENTITY,
        "corrected_identifier": IDENTITY,
        "pubchem_cid": 5318691,
        "known_exact_candidate": "LIPIDMAPS:LMPK12111656",
        "candidate_native_eligibility": "OPEN",
        "final_primary_identity": "OPEN",
        "mapping_disposition": "WITHHOLD",
        "scientific_approval_added": False,
        "evidence_not_before": EVIDENCE_NOT_BEFORE,
    }
    require(all(doc.get(k) == v for k, v in expected.items()), "Evidence identity contract differs")
    require({d["issue"] for d in doc["decisions"]} == {753}, "Evidence decisions differ")
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
    require(
        regular(Path(publication.__file__)) == publication._CODE, "Loaded journal adapter changed"
    )
    for path, loaded in policy._LOADED_CODE.items():
        require(regular(path) == loaded, "Loaded shared dependency changed")
    paths = [
        Path(__file__),
        Path(guarded.__file__),
        Path(native.__file__),
        Path(policy.__file__),
        Path(publication.__file__),
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
                record.get("identifier") not in {OLD_IDENTITY, IDENTITY},
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
                "shape": "registry_value_correction",
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
    inputs.update(
        publication.completed_journal(root, log, saved, previous={OWNER: original[OWNER]})
    )
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
    return publication.publish(
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
    old = [row for row, _ in prior if row["subject_id"] == SUBJECT]
    target = [(row, line) for row, line in generated if row["subject_id"] == SUBJECT]
    require(len(old) == 1 and old[0]["object_id"] == OLD_IDENTITY, "Prior CAS row differs")
    require(len(target) == 1, "Candidate must contain exactly one Izalpinin row")
    row, line = target[0]
    record = yaml.safe_load(current)
    expected = {
        "subject_label": NAME,
        "object_id": IDENTITY,
        "object_label": NAME,
        "predicate_id": "skos:exactMatch",
        "object_source": "registry:cas",
        "other": "CAS:480-14-8",
        "validation_method": "",
        "mapping_date": record["curation_history"][-1]["timestamp"][:10],
    }
    require(all(row.get(k) == v for k, v in expected.items()), "Candidate CAS claim differs")
    for field in ("mapping_justification", "confidence", "comment"):
        require(row[field] == old[0][field], "Unreviewed candidate field: " + field)
    require("MIM:curator=claude" in row["source"].split("|"), "Candidate lacks actual curator")
    require("480-14-4" not in line and "LIPIDMAPS" not in line, "Unapproved identity token")
    output = [line if prior_row["subject_id"] == SUBJECT else raw for prior_row, raw in prior]
    result = ("".join(header) + "".join(output)).splitlines(keepends=True)
    date = newest_row_date(result)
    require(date is not None, "Projected mapping date absent")
    updated, _ = rewrite(result, date)
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
    require(digest(before) == BEFORE[MANIFEST], "Prior policy manifest preimage differs")
    doc = json.loads(before)
    require(
        doc.get("schema_version") == 1 and doc.get("policy_version") == "owned-name-policy-v1",
        "Prior policy manifest contract differs",
    )
    require(
        doc["artifacts"] == {str(p): BEFORE[p] for p in (SSSOM, SIDECAR, BASELINE)}
        and doc["source_owner_sha256"][RECORD] == BEFORE[OWNER],
        "Prior policy artifact binding differs",
    )
    require("registry_correction_updates" not in doc, "Unexpected earlier registry correction")
    doc["artifacts"][str(SSSOM)] = digest(canonical)
    doc["source_owner_sha256"][RECORD] = digest(current)
    doc["registry_correction_updates"] = [
        {
            "issue": 753,
            "scope": "Existing Izalpinin CAS-value correction only; retain WITHHOLD and OPEN final primary/source policy. Other canonical rows, historical owner lineage, policy decisions and two form updates are retained exactly. Source-only node changes are separately tracked by the combined native receipt; this owner map is not an all-current corpus snapshot.",
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
        }
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
        "added_rows": 0,
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
        publication.completed_journal(
            root, log, json.loads(regular(log)), previous={path: original[path] for path in outputs}
        )
        for path, backup in promotion_backups.items():
            require(regular(backup) == original[path], "Promotion beforeimage changed")
        return {"applied": False, "changed": False, "approval": APPROVAL}
    require(
        actual == {path: original[path] for path in outputs},
        "Partial or changed canonical promotion",
    )
    return publication.publish(
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
    with LockManager().lock("mediaingredientmech", "#753 Izalpinin CAS correction " + args.phase):
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
