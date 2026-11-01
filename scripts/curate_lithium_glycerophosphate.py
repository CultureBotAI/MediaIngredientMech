#!/usr/bin/env python3
"""Bounded #1005 source correction and candidate promotion; dry-run by default.

The CLI holds the repository lock; callers of the Python apply API must hold it.
One-time production preimages are pinned, while tests use small explicit tables.
Neither a successful transaction nor its receipt grants scientific approval.
"""

from __future__ import annotations

import argparse
import copy
import csv
import datetime
import io
import json
import stat
import sys
import tempfile
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(ROOT / "src"))

from mediaingredientmech.curate.curation_event import record_curation_event  # noqa: E402
from mediaingredientmech.validation.write_validated import write_validated_ingredient  # noqa: E402
from scripts import promote_heptahydrate_ncit as guarded  # noqa: E402
from scripts.bump_sssom_header import newest_row_date, rewrite  # noqa: E402

OWNER = Path("data/ingredients/mapped/Sn-Glycerol_3-phosphate_Lithium_Salt.yaml")
SSSOM = Path("mappings/ingredient_mappings.sssom.tsv")
BASELINE = Path("mappings/other_cross_record_baseline.tsv")
FIXTURES = ROOT / "tests/fixtures/issue1005-before"
EVIDENCE = Path("reports/lithium_glycerophosphate_1005_20261101/sources")
MANIFEST_SHA = "ca89868b74535eb7d4296fbb3cb14cc6da8cb599dd78ab27ef95baff61f1eb24"
BEFORE = {
    OWNER: "94fff493bf4b0ddc19144054a44305ea29de113477254be64e1dc86c0f128f51",
    SSSOM: "d5cd812a8c44c85438d73c68c7a8c3067a505765e4cd54e3a64cef029f2d8ed6",
    BASELINE: "c5b74bd950417baf7f96632f03154e26ef29bb909dfd19560f8460ba5378bfd4",
}
SUBJECT = "MIM:Sn-Glycerol_3-phosphate_Lithium_Salt"
OLD = "cas:17989-41-2"
NEW = "kgmicrobe.compound:sn-glycerol_3-phosphate_lithium_salt"
PARENT = "CHEBI:15978"
NAME = "sn-Glycerol 3-phosphate lithium salt"
ACTION = "CORRECTED_LITHIUM_GLYCEROPHOSPHATE_IDENTITY"
APPROVAL = "NONE: source correction; surviving mappings and provisional role require fresh scientific review."
DECISION = "https://github.com/CultureBotAI/MediaIngredientMech/issues/1005#issuecomment-6556888392"
SIGMA = "https://www.sigmaaldrich.com/US/en/product/sigma/94124"
FORM = {"name": NAME, "cas_rn": "17989-41-2", "form": "lithium salt", "supplier": "Sigma-Aldrich",
        "catalog_number": "94124", "notes": "free-acid CAS/FW; Li stoichiometry unstated"}
VERIFICATION = (
    f"Approved distinct local lithium-salt identity and broad CHEBI:15978: {DECISION}. "
    f"Sigma-Aldrich 94124 names the lithium salt with variable Li content and free-acid CAS/FW: {SIGMA}. "
    "ChEBI https://www.ebi.ac.uk/chebi/backend/api/public/compound/15978/ and PubChem "
    "https://pubchem.ncbi.nlm.nih.gov/compound/439162 describe the free acid, not lithium-salt chemistry. "
    f"Primary captures inspected 2026-11-01: {EVIDENCE}/manifest.json (sha256 {MANIFEST_SHA}). "
    "The successful Sigma capture is extracted primary-page text; the separate empty HTTP capture timed out. "
    "CultureBotHT CSV is an ignored local raw snapshot, not a commit-attested blob. No direct CAS Registry "
    "verification, fixed Li stoichiometry or new chemical structure is claimed. Historical CHEBI/KG sources "
    "remain provenance, not salt-identity proof. No scientific/release approval; CARBON_SOURCE stays provisional."
)
digest = guarded.digest


def regular(path: Path) -> bytes:
    if path.resolve() != path.absolute() or not stat.S_ISREG(path.lstat().st_mode):
        raise ValueError(f"Input must be a regular original path, not an alias: {path}")
    return path.read_bytes()


def frozen_owner() -> bytes:
    data = regular(FIXTURES / OWNER.name)
    if digest(data) != BEFORE[OWNER]:
        raise ValueError("Immutable owner preimage changed")
    return data


def render(record: dict) -> bytes:
    with tempfile.TemporaryDirectory(prefix="mim-1005-validate-") as temporary:
        output = Path(temporary) / "record.yaml"
        write_validated_ingredient(record, output)
        return output.read_bytes()


def propose_record(before: bytes, *, timestamp: str) -> bytes:
    if digest(before) != BEFORE[OWNER]:
        raise ValueError("Owner differs from the reviewed preimage")
    parsed = datetime.datetime.fromisoformat(timestamp)
    if parsed.utcoffset() != datetime.timedelta(0) or parsed.date() < datetime.date(2026, 11, 1):
        raise ValueError("Correction timestamp must be UTC and follow the inspected evidence")
    record = copy.deepcopy(yaml.safe_load(before))
    if record["identifier"] != OLD or record["ontology_mapping"]["ontology_id"] != PARENT:
        raise ValueError("Unexpected reviewed identity")
    chemistry = record.pop("chemical_properties")
    record["identifier"] = NEW
    record["supplied_form"] = [dict(FORM)]
    record["ontology_mapping"]["evidence"].append({
        "evidence_type": "MANUAL_CURATION", "source": SIGMA,
        "notes": "Corrects the prior free-acid CAS identity interpretation while retaining its evidence. " + VERIFICATION,
    })
    changes = (
        f"Replaced {OLD} identity with {NEW}; retained broad CHEBI:15978 and exact local registry identity. "
        "Recorded Sigma 94124 procurement metadata without inventing Li stoichiometry. Removed active free-acid "
        "chemical_properties, preserved exactly here and in the immutable preimage: "
        + json.dumps(chemistry, sort_keys=True) + ". Preserved prior history, rejected parent labels, occurrence "
        "counts and provisional role/evidence unchanged. Retired only the published Glycerol 3-phosphate alias "
        "and its Rule K allowance; removed the false exact CAS mapping. " + VERIFICATION
    )
    record_curation_event(record, curator="Codex", action=ACTION, changes=changes, timestamp=timestamp,
                          previous_status="MAPPED", new_status="MAPPED", llm_assisted=True, llm_model="gpt-6")
    return render(record)


def complete_owner(current: bytes) -> None:
    try:
        timestamp = yaml.safe_load(current)["curation_history"][-1]["timestamp"]
        expected = propose_record(frozen_owner(), timestamp=timestamp)
    except (KeyError, TypeError, IndexError) as error:
        raise ValueError("Incomplete source correction") from error
    if current != expected:
        raise ValueError("Partial or changed source correction")


def evidence_inputs(directory: Path) -> dict[Path, bytes]:
    manifest_path = directory / "manifest.json"
    raw = regular(manifest_path)
    if digest(raw) != MANIFEST_SHA:
        raise ValueError("Reviewed source manifest changed")
    inputs = {manifest_path: raw}
    for name, item in json.loads(raw)["files"].items():
        if Path(name).name != name:
            raise ValueError("Evidence must use direct filenames")
        path = directory / name
        data = regular(path)
        if digest(data) != item["sha256"] or len(data) != item["bytes"]:
            raise ValueError(f"Reviewed evidence changed: {name}")
        inputs[path] = data
    term = json.loads(inputs[directory / "chebi-15978-primary.json"])
    prop = json.loads(inputs[directory / "pubchem-439162-properties.json"])["PropertyTable"]["Properties"]
    supplier = json.loads(inputs[directory / "sigma-94124-web-response.json"])
    failure = json.loads(inputs[directory / "sigma-94124-http.html.receipt.json"])
    if (term["chebi_accession"] != PARENT or term["ascii_name"] != "sn-glycerol 3-phosphate"
            or len(prop) != 1 or prop[0]["CID"] != 439162 or prop[0]["MolecularFormula"] != "C3H9O6P"
            or supplier["url"] != SIGMA or "free acid basis" not in supplier["response"]
            or "xLi" not in supplier["response"] or failure["successful_http"] is not False
            or inputs[directory / "sigma-94124-http.html"] != b""):
        raise ValueError("Evidence does not support the approved procurement/parent distinction")
    return inputs


def code_inputs() -> dict[Path, bytes]:
    paths = [Path(__file__), Path(guarded.__file__), ROOT / "scripts/bump_sssom_header.py",
             ROOT / "src/mediaingredientmech/curate/apply_receipt.py",
             ROOT / "src/mediaingredientmech/curate/curation_event.py",
             ROOT / "src/mediaingredientmech/validation/write_validated.py",
             ROOT / "src/mediaingredientmech/schema/mediaingredientmech.yaml"]
    return {p: regular(p) for p in paths}


def validate_scope(root: Path, inputs: dict[Path, bytes]) -> None:
    for path, expected in inputs.items():
        if regular(path) != expected:
            raise ValueError(f"A bound input changed before publication: {path}")
    for path in (root / "data/ingredients").rglob("*.yaml"):
        if path == root / OWNER:
            continue
        record = yaml.safe_load(regular(path))
        if isinstance(record, dict) and (record.get("identifier") == NEW or (
                record.get("mapping_status") == "MAPPED"
                and (record.get("ontology_mapping") or {}).get("ontology_id") == NEW)):
            raise ValueError(f"Destination identity already held: {path}")


def backups(log: Path) -> dict[Path, Path]:
    return {p: log.with_name(log.stem + ".before-" + p.name) for p in BEFORE}


def record_receipt(current: bytes) -> list[dict]:
    return [{"source_record": str(OWNER), "shape": "distinct_lithium_salt_identity",
             "before_yaml_sha256": BEFORE[OWNER], "after_yaml_sha256": digest(current),
             "change": yaml.safe_load(current)["curation_history"][-1]["changes"], "verification": VERIFICATION}]


def source_result(root: Path, evidence: Path, current: bytes) -> dict:
    bound = {str(root / p): h for p, h in BEFORE.items()}
    bound.update({str(p): digest(b) for p, b in (evidence_inputs(evidence) | code_inputs()).items()})
    return {"phase": "sources", "approval": APPROVAL,
            "timestamp": yaml.safe_load(current)["curation_history"][-1]["timestamp"],
            "evidence_directory": str(evidence), "evidence_manifest_sha256": MANIFEST_SHA,
            "input_sha256": bound, "output_sha256": {str(OWNER): digest(current)},
            "sssom_before_sha256": BEFORE[SSSOM], "baseline_before_sha256": BEFORE[BASELINE],
            "records": record_receipt(current)}


def completed_receipt(log: Path, expected: dict, root: Path, changed: set[Path]) -> bytes:
    raw = regular(log)
    value = json.loads(raw)
    transaction = value.get("transaction") or {}
    if (any(value.get(k) != v for k, v in expected.items()) or value.get("state") != "complete"
            or value.get("applied") is not True or transaction.get("applied") is not True
            or set(transaction.get("changed", [])) != {str(root / p) for p in changed}
            or len(transaction.get("changed", [])) != len(changed)
            or transaction.get("created") != [] or transaction.get("unchanged") != []):
        raise ValueError("Completed receipt does not bind this exact execution")
    return raw


def source_receipt(root: Path, log: Path, current: bytes) -> tuple[dict[Path, bytes], dict]:
    complete_owner(current)
    source = json.loads(regular(log))
    evidence = Path(source["evidence_directory"])
    expected = source_result(root, evidence, current)
    inputs = {log: completed_receipt(log, expected, root, {OWNER})}
    inputs.update(evidence_inputs(evidence) | code_inputs())
    for path, backup in backups(log).items():
        data = regular(backup)
        if digest(data) != BEFORE[path]:
            raise ValueError(f"Source preimage changed: {path}")
        inputs[backup] = data
    return inputs, source


def table(data: bytes) -> tuple[list[str], list[dict]]:
    lines = data.decode().splitlines(keepends=True)
    while lines and (lines[0].startswith("#") or not lines[0].strip()):
        lines.pop(0)
    reader = csv.DictReader(io.StringIO("".join(lines)), delimiter="\t")
    rows = list(reader)
    if not reader.fieldnames or any(None in r or None in r.values() for r in rows):
        raise ValueError("Malformed SSSOM table")
    return reader.fieldnames, rows


def retired_baseline(before: bytes) -> bytes:
    line = f"{SUBJECT}\tGlycerol 3-phosphate\tMIM:Glycerol_3-phosphate\tUNREVIEWED\n".encode()
    lines = before.splitlines(keepends=True)
    if digest(before) != BEFORE[BASELINE] or lines.count(line) != 1:
        raise ValueError("Expected exactly the reviewed Rule K allowance")
    return b"".join(x for x in lines if x != line)


def promoted_sssom(before: bytes, candidate: bytes, current: bytes) -> bytes:
    if digest(before) != BEFORE[SSSOM]:
        raise ValueError("Canonical preimage changed")
    complete_owner(current)
    record = yaml.safe_load(current)
    fields, prior = table(before)
    candidate_fields, rows = table(candidate)
    old = {r["object_id"]: r for r in prior if r["subject_id"] == SUBJECT}
    selected = [r for r in rows if r["subject_id"] == SUBJECT]
    if (fields != candidate_fields or len(old) != 3 or set(old) != {PARENT, OLD, NEW}
            or len(selected) != 2 or {r["object_id"] for r in selected} != {PARENT, NEW}):
        raise ValueError("Expected three reviewed rows and exactly two native candidate rows")
    source = "|".join(["MIM:" + e["source"] for e in record["ontology_mapping"]["evidence"]]
                      + ["MIM:curator=Codex", "kgm:native_ontology:chebi"])
    corrected = {}
    for row in selected:
        obj = row["object_id"]
        expected = dict(old[obj], source=source, mapping_date=record["curation_history"][-1]["timestamp"][:10])
        expected.update(comment="" if obj == PARENT else f"Registry/identity row preserving {NEW} alongside parent {PARENT}.",
                        other="" if obj == PARENT else "CAS:17989-41-2")
        if row != expected:
            raise ValueError(f"Candidate differs from the bounded native row: {obj}")
        row = dict(row)
        row["source"] = "|".join(dict.fromkeys(old[obj]["source"].split("|") + row["source"].split("|")))
        if obj == PARENT:
            row["comment"] = old[obj]["comment"]
        corrected[obj] = row
    output = []
    seen = []
    for line in before.decode().splitlines(keepends=True):
        if line.startswith(SUBJECT + "\t"):
            row = next(csv.DictReader(io.StringIO("\t".join(fields) + "\n" + line), delimiter="\t"))
            obj = row["object_id"]
            seen.append(obj)
            if obj not in corrected:
                continue
            buffer = io.StringIO(newline="")
            csv.DictWriter(buffer, fieldnames=fields, delimiter="\t", lineterminator="\n").writerow(corrected[obj])
            line = buffer.getvalue()
        output.append(line)
    if len(seen) != 3 or set(seen) != {PARENT, OLD, NEW}:
        raise ValueError("Duplicate or missing canonical target row")
    newest = newest_row_date(output)
    if not newest:
        raise ValueError("Cannot derive canonical header date")
    return "".join(rewrite(output, newest)[0]).encode()


def completed_anchors(before: bytes, baseline: bytes, actual: bytes, current_baseline: bytes,
                      current: bytes) -> None:
    if actual == before and current_baseline == baseline:
        return
    if current_baseline != retired_baseline(baseline):
        raise ValueError("Completed source has changed/partial canonical anchors")
    fields, rows = table(actual)
    record = yaml.safe_load(current)
    for row in rows:
        if row["subject_id"] == SUBJECT:
            row["source"] = "|".join(["MIM:" + e["source"] for e in record["ontology_mapping"]["evidence"]]
                                     + ["MIM:curator=Codex", "kgm:native_ontology:chebi"])
            if row["object_id"] == PARENT:
                row["comment"] = ""
    buffer = io.StringIO(newline="")
    stream = csv.DictWriter(buffer, fieldnames=fields, delimiter="\t", lineterminator="\n")
    stream.writeheader()
    stream.writerows(rows)
    if actual != promoted_sssom(before, buffer.getvalue().encode(), current):
        raise ValueError("Completed source has changed/partial canonical anchors")


def apply_sources(root: Path, evidence: Path, log: Path, *, apply: bool = False) -> dict:
    root, evidence, log = root.resolve(), evidence.absolute(), log.absolute()
    inputs = {root / p: regular(root / p) for p in BEFORE}
    inputs.update(evidence_inputs(evidence) | code_inputs())
    validate_scope(root, inputs)
    current = inputs[root / OWNER]
    if digest(current) != BEFORE[OWNER]:
        bound, _ = source_receipt(root, log, current)
        before = bound[backups(log)[SSSOM]]
        baseline = bound[backups(log)[BASELINE]]
        completed_anchors(before, baseline, inputs[root / SSSOM], inputs[root / BASELINE], current)
        return {"applied": False, "changed": False, "approval": APPROVAL}
    if any(digest(inputs[root / p]) != BEFORE[p] for p in BEFORE):
        raise ValueError("Reviewed canonical/baseline anchor changed")
    current = propose_record(current, timestamp=datetime.datetime.now(datetime.timezone.utc).isoformat())
    result = source_result(root, evidence, current)
    return guarded.publish(root, {OWNER: current}, inputs, log,
                           {backup: inputs[root / p] for p, backup in backups(log).items()}, result, apply=apply,
                           validate_scope=lambda: validate_scope(root, inputs))


def promote(root: Path, candidate: Path, source_log: Path, log: Path, *, apply: bool = False,
            candidate_sha256: str) -> dict:
    root, candidate, source_log, log = root.resolve(), candidate.absolute(), source_log.absolute(), log.absolute()
    current = regular(root / OWNER)
    inputs, source = source_receipt(root, source_log, current)
    inputs[root / OWNER] = current
    proposed = regular(candidate)
    if digest(proposed) != candidate_sha256:
        raise ValueError("Candidate hash changed")
    inputs[candidate] = proposed
    before = inputs[backups(source_log)[SSSOM]]
    baseline = inputs[backups(source_log)[BASELINE]]
    outputs = {SSSOM: promoted_sssom(before, proposed, current), BASELINE: retired_baseline(baseline)}
    actual = {p: regular(root / p) for p in outputs}
    inputs.update({root / p: b for p, b in actual.items()})
    validate_scope(root, inputs)
    result = {"phase": "promote", "approval": APPROVAL, "records": source["records"],
              "source_receipt_sha256": digest(inputs[source_log]), "candidate_sha256": digest(proposed),
              "sssom_before_sha256": digest(before), "sssom_after_sha256": digest(outputs[SSSOM]),
              "baseline_before_sha256": digest(baseline), "baseline_after_sha256": digest(outputs[BASELINE]),
              "changed_rows": 2, "removed_rows": 1, "removed_baseline_rows": 1,
              "preserved_historical_source_tokens": True, "preserved_original_validation_stamps": True}
    if actual == outputs:
        completed_receipt(log, result, root, set(outputs))
        for p in outputs:
            if regular(backups(log)[p]) != {SSSOM: before, BASELINE: baseline}[p]:
                raise ValueError("Promotion beforeimage changed")
        return {"applied": False, "changed": False, "approval": APPROVAL}
    if actual != {SSSOM: before, BASELINE: baseline}:
        raise ValueError("Canonical/baseline changed or promotion is partial")
    return guarded.publish(root, outputs, inputs, log,
                           {backups(log)[p]: b for p, b in actual.items()}, result, apply=apply,
                           validate_scope=lambda: validate_scope(root, inputs))


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("phase", choices=("sources", "promote"))
    parser.add_argument("--root", type=Path, default=ROOT)
    parser.add_argument("--log", type=Path, required=True)
    parser.add_argument("--evidence", type=Path)
    parser.add_argument("--source-log", type=Path)
    parser.add_argument("--candidate", type=Path)
    parser.add_argument("--candidate-sha256")
    modes = parser.add_mutually_exclusive_group()
    modes.add_argument("--apply", action="store_true")
    modes.add_argument("--dry-run", action="store_true")
    args = parser.parse_args(argv)
    if args.phase == "promote" and not all((args.source_log, args.candidate, args.candidate_sha256)):
        parser.error("promote requires --source-log, --candidate and --candidate-sha256")
    from plugins.lock_manager import LockManager
    from plugins.repository_settings import RepositorySettings

    target = RepositorySettings.from_environment().get_target("mediaingredientmech")
    if target.path.resolve() != args.root.resolve():
        raise ValueError("Configured MIM root differs from requested worktree")
    target.open()
    with LockManager().lock("mediaingredientmech", f"#1005 {args.phase}"):
        if args.phase == "sources":
            result = apply_sources(target.path, args.evidence or target.path / EVIDENCE, args.log, apply=args.apply)
        else:
            result = promote(target.path, args.candidate, args.source_log, args.log, apply=args.apply,
                             candidate_sha256=args.candidate_sha256)
    print(json.dumps(result, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
