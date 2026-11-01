#!/usr/bin/env python3
"""Apply the bounded #875 exact-form correction; dry-run unless --apply.

The sources phase couples the owner and rejection ledger. The promote phase
accepts a separately generated, hash-bound native SSSOM candidate and changes
only this subject. Neither phase grants scientific approval. Run with the
isolated Claw environment for RepositorySettings, LockManager and transactions.
"""

from __future__ import annotations

import argparse
import copy
import csv
import datetime
import hashlib
import io
import json
import os
import stat
import sys
import tempfile
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
sys.path.insert(0, str(ROOT))

from mediaingredientmech.curate.apply_receipt import reserve_receipt_outputs  # noqa: E402
from mediaingredientmech.curate.curation_event import record_curation_event  # noqa: E402
from mediaingredientmech.validation.write_validated import write_validated_ingredient  # noqa: E402
from scripts.bump_sssom_header import newest_row_date, rewrite  # noqa: E402

OWNER = Path("data/ingredients/mapped/Na2hpo4_X_7_H2o.yaml")
LEDGER = Path("mappings/unified_mapping_rejections.tsv")
SSSOM = Path("mappings/ingredient_mappings.sssom.tsv")
EVIDENCE = Path("reports/ncit_heptahydrate_875_20261101/sources/ncit-C61946.json")
OWNER_BEFORE = "e4f20bded8bb984f76d381636cf79b522983413046bf24bc6168e1065c027636"
LEDGER_BEFORE = "82d7d79172a5efd966f0a6a97ead4faae186128f6d6fdb327366f041ad06aba4"
SSSOM_BEFORE = "a2b83ccdcaad67d89943ccf0f0e30d796cdbc5e418ead247313631b713e89722"
EVIDENCE_SHA = "a112c3e91dd6aa46feb112621ba5d13673df69f1b20665e042e22b8aa05a1d83"
NAME = "Na2HPO4 x 7 H2O"
SUBJECT = "MIM:Na2hpo4_X_7_H2o"
OLD = "kgmicrobe.compound:na2hpo4_x_7_h2o"
NEW = "NCIT:C61946"
LABEL = "Sodium Phosphate, Dibasic, Heptahydrate"
PARENT = "CHEBI:34683"
ACTION = "REGROUNDED_EXACT_HEPTAHYDRATE"
URL = "https://api-evsrest.nci.nih.gov/api/v1/concept/ncit/C61946?include=full"
VERIFICATION = (
    f"NCI EVS NCIt 26.10d {NEW} '{LABEL}' is active and explicitly records CAS "
    f"7782-85-6, formula 2Na.HO4P.7H2O and FDA UNII 70WT22SF4B. Source: {URL}; "
    f"accessed 2026-11-01; archived at {EVIDENCE.as_posix()} (sha256 {EVIDENCE_SHA}). "
    "The approved #875 decision uses MAPPING_SEMANTICS section 3 step 1, which "
    "precedes the CAS fallback. The anhydrous CHEBI:34683 is not this identity."
)
CHANGE = (
    f"Promoted identifier {OLD} to {NEW}; replaced the CHEBI:34683 CLOSE_MATCH "
    "grounding with exact NCIT:C61946 and moved the coupled rejection-ledger "
    "mim_id. Preserved the earlier evidence and history, accepted hydrate aliases, "
    "rejected sibling-form labels, CAS, chemistry, roles and occurrence counts. "
    "The inherited anhydrous structure and provisional BUFFER evidence remain "
    "unresolved. This correction grants no scientific or release approval. " + VERIFICATION
)
MAPPING_EVIDENCE = {"evidence_type": "DATABASE_MATCH", "source": URL, "notes": VERIFICATION}
OLD_MAPPING = {"ontology_id": PARENT, "ontology_label": "disodium hydrogenphosphate",
               "ontology_source": "CHEBI", "mapping_quality": "CLOSE_MATCH"}
NEW_MAPPING = {"ontology_id": NEW, "ontology_label": LABEL,
               "ontology_source": "NCIT", "mapping_quality": "EXACT_MATCH"}
OLD_REASON = (
    "The stated heptahydrate is distinct from anhydrous disodium hydrogenphosphate; "
    "ChEBI has no term for this hydration state, and the parent survives only as "
    "CLOSE_MATCH (#321/#334, #342). The stale kg_microbe_node_id was withdrawn in "
    "the REMOVED_PARENT_IDENTITY event. Reject the stale recipe term.id in unified "
    "identity columns (#808, culturebotai-claw#571). The record carries its own "
    "heptahydrate CAS 7782-85-6, so promotion to cas:7782-85-6 under "
    "MAPPING_SEMANTICS §3 step 2 is still open (#875); that change must update "
    "this row's mim_id in the same commit. See data/ingredients/mapped/Na2hpo4_X_7_H2o.yaml."
)
NEW_REASON = (
    f"The heptahydrate is exactly {NEW} '{LABEL}' under MAPPING_SEMANTICS section "
    f"3 step 1 (#875), supported by NCI EVS CAS 7782-85-6 and formula "
    f"2Na.HO4P.7H2O: {URL}. This supersedes the earlier CAS-only promotion "
    "rationale. Keep anhydrous CHEBI:34683 rejected in unified identity columns "
    "(#808); the removed parent KG identity is not restored. Source evidence and "
    f"preserved history: {OWNER.as_posix()}. No scientific or release approval is asserted."
)
APPROVAL = "NONE: mapping correction only; fresh mapping-specific review is required."


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def render(record: dict) -> bytes:
    """Use the native validated serializer, without writing a maintained owner."""
    with tempfile.TemporaryDirectory(prefix="mim-875-validate-") as directory:
        path = Path(directory) / OWNER.name
        write_validated_ingredient(record, path)
        return path.read_bytes()


def verify_evidence(data: bytes) -> None:
    if digest(data) != EVIDENCE_SHA:
        raise ValueError("Inspected NCI evidence bytes changed")
    term = json.loads(data)
    properties = {p["type"]: p["value"] for p in term["properties"]}
    if (term.get("code") != "C61946" or term.get("name") != LABEL
            or term.get("active") is not True or term.get("version") != "26.10d"
            or any(properties.get(k) != v for k, v in {
                "CAS_Registry": "7782-85-6", "Chemical_Formula": "2Na.HO4P.7H2O",
                "FDA_UNII_Code": "70WT22SF4B"}.items())):
        raise ValueError("NCI evidence does not verify the reviewed exact form")


def corrected_record(before: bytes, *, timestamp: str | None = None) -> bytes:
    record = yaml.safe_load(before)
    if record.get("identifier") == NEW:
        restored = copy.deepcopy(record)
        history = restored.get("curation_history") or []
        event = history[-1] if history else {}
        expected = {"curator": "Codex", "action": ACTION, "changes": CHANGE,
                    "previous_status": "MAPPED", "new_status": "MAPPED",
                    "llm_assisted": True, "llm_model": "gpt-6"}
        if (any(event.get(k) != v for k, v in expected.items())
                or set(event) != {*expected, "timestamp"}
                or any(restored["ontology_mapping"].get(k) != v for k, v in NEW_MAPPING.items())
                or restored["ontology_mapping"].get("evidence", [])[-1:] != [MAPPING_EVIDENCE]):
            raise ValueError("Partial or changed prior NCIT correction")
        try:
            timestamp = datetime.datetime.fromisoformat(event["timestamp"])
        except (TypeError, ValueError) as error:
            raise ValueError("Invalid correction timestamp") from error
        if timestamp.utcoffset() != datetime.timedelta(0):
            raise ValueError("Correction timestamp must identify UTC")
        history.pop()
        restored["identifier"] = OLD
        restored["ontology_mapping"].update(OLD_MAPPING)
        restored["ontology_mapping"]["evidence"].pop()
        if digest(render(restored)) != OWNER_BEFORE:
            raise ValueError("Prior correction changed unreviewed owner content")
        return before
    if digest(before) != OWNER_BEFORE:
        raise ValueError("Owner bytes changed; fresh review is required")
    if (record.get("identifier") != OLD or record.get("preferred_term") != NAME
            or record.get("mapping_status") != "MAPPED"
            or record.get("chemical_properties", {}).get("cas_rn") != "7782-85-6"
            or any(record.get("ontology_mapping", {}).get(k) != v for k, v in OLD_MAPPING.items())):
        raise ValueError("Unexpected heptahydrate identity or mapping")
    proposal = copy.deepcopy(record)
    proposal["identifier"] = NEW
    proposal["ontology_mapping"].update(NEW_MAPPING)
    proposal["ontology_mapping"].setdefault("evidence", []).append(dict(MAPPING_EVIDENCE))
    record_curation_event(proposal, curator="Codex", action=ACTION, changes=CHANGE,
                          previous_status="MAPPED", new_status="MAPPED", llm_assisted=True,
                          llm_model="gpt-6", timestamp=timestamp)
    return render(proposal)


def corrected_ledger(before: bytes) -> bytes:
    old = f"{NAME}\t{PARENT}\t{OLD}\t{OLD_REASON}\n".encode()
    new = f"{NAME}\t{PARENT}\t{NEW}\t{NEW_REASON}\n".encode()
    if digest(before) == LEDGER_BEFORE and before.splitlines(keepends=True).count(old) == 1:
        return b"".join(new if line == old else line for line in before.splitlines(keepends=True))
    if before.splitlines(keepends=True).count(new) == 1:
        restored = b"".join(old if line == new else line for line in before.splitlines(keepends=True))
        if digest(restored) == LEDGER_BEFORE:
            return before
    raise ValueError("Rejection ledger changed or has a partial NCIT correction")


def unique_destination(root: Path) -> None:
    """Include ignored/nested YAML when checking for another destination owner."""
    for path in (root / "data/ingredients").rglob("*.yaml"):
        if path == root / OWNER:
            continue
        record = yaml.safe_load(path.read_text())
        if isinstance(record, dict) and (
            record.get("identifier") == NEW
            or (record.get("mapping_status") == "MAPPED"
                and (record.get("ontology_mapping") or {}).get("ontology_id") == NEW)
        ):
            raise ValueError(f"Destination identity already held by {path}")


def recheck(inputs: dict[Path, bytes]) -> None:
    if any(path.read_bytes() != expected for path, expected in inputs.items()):
        raise ValueError("A frozen input changed before write")


def new_transaction(root: Path, validator, journal: Path):
    from kg_microbe_write import ValidatedWriteTransaction

    return ValidatedWriteTransaction(root, validator=validator, journal_dir=journal)


def recheck_reserved(reservations: dict[Path, tuple[int, int]]) -> None:
    """Check directory entries against still-open descriptors, never symlinks."""
    for path, identity in reservations.items():
        try:
            current = path.lstat()
        except (FileNotFoundError, NotADirectoryError):
            current = None
        if (current is None or not stat.S_ISREG(current.st_mode)
                or (current.st_dev, current.st_ino) != identity):
            raise ValueError(f"Reserved evidence output was replaced or removed: {path}")


def publish(root: Path, outputs: dict[Path, bytes], inputs: dict[Path, bytes],
            log: Path, backups: dict[Path, bytes], result: dict, *, apply: bool) -> dict:
    """Caller owns the verified repository lock; every output validates first."""
    reservations = {}

    def validate(path, text):
        if text.encode() != outputs[path.relative_to(root)]:
            raise ValueError("Staged output differs from the bounded proposal")
        recheck(inputs)
        recheck_reserved(reservations)

    transaction = new_transaction(root, validate, log.parent / f"{log.stem}-journal")
    for path, data in outputs.items():
        transaction.stage(path, data.decode())
    transaction.commit()
    if apply:
        with reserve_receipt_outputs(log, backup_paths=tuple(backups)) as handles:
            receipt, *backup_handles = handles
            for path, handle in zip((log, *backups), handles, strict=True):
                info = os.fstat(handle.fileno())
                reservations[path] = (info.st_dev, info.st_ino)
            applied = None
            mutation_started = False
            try:
                recheck_reserved(reservations)
                recheck(inputs)
                for handle, data in zip(backup_handles, backups.values(), strict=True):
                    handle.write(data)
                    handle.flush()
                receipt.write(json.dumps({**result, "applied": False, "state": "prepared"}, indent=2) + "\n")
                receipt.flush()
                recheck_reserved(reservations)
                mutation_started = True
                applied = transaction.commit(apply=True)
                result = {**result, "transaction": applied.as_dict()}
                recheck_reserved(reservations)
                if any((root / path).read_bytes() != data for path, data in outputs.items()):
                    raise ValueError("Written outputs differ; retain receipt and recovery journal")
                receipt.seek(0)
                receipt.truncate()
                receipt.write(json.dumps({**result, "applied": True, "state": "complete"}, indent=2) + "\n")
                receipt.flush()
                recheck_reserved(reservations)
            except Exception as error:
                # Use only our held descriptor: never open, unlink, or overwrite
                # a competing pathname. A lost receipt may have no surviving
                # directory entry; the native journal remains recovery evidence.
                failure = {**result, "state": "failed", "error": str(error),
                           "applied": True if applied is not None else (None if mutation_started else False),
                           "recovery_required": mutation_started,
                           "journal_directory": str(log.parent / f"{log.stem}-journal")}
                try:
                    receipt.seek(0)
                    receipt.truncate()
                    receipt.write(json.dumps(failure, indent=2) + "\n")
                    receipt.flush()
                except OSError:
                    pass  # Preserve the original failure and native journal.
                raise
    return {**result, "applied": apply, "changed": True}


def apply_sources(root: Path, log: Path, *, apply: bool = False) -> dict:
    inputs = {root / p: (root / p).read_bytes() for p in (OWNER, LEDGER, SSSOM, EVIDENCE)}
    verify_evidence(inputs[root / EVIDENCE])
    owner = corrected_record(inputs[root / OWNER])
    ledger = corrected_ledger(inputs[root / LEDGER])
    owner_changed = owner != inputs[root / OWNER]
    if owner_changed != (ledger != inputs[root / LEDGER]):
        raise ValueError("Owner and ledger must migrate together; partial state refused")
    unique_destination(root)
    if not owner_changed:
        return {"applied": False, "changed": False, "approval": APPROVAL}
    if digest(inputs[root / SSSOM]) != SSSOM_BEFORE:
        raise ValueError("Canonical SSSOM differs from the receipt-chain preimage")
    result = {"phase": "sources", "approval": APPROVAL, "evidence_sha256": EVIDENCE_SHA,
              "ledger_before_sha256": digest(inputs[root / LEDGER]),
              "ledger_after_sha256": digest(ledger), "sssom_before_sha256": SSSOM_BEFORE,
              "records": [{"source_record": OWNER.as_posix(), "shape": "exact_heptahydrate_identity",
                           "before_yaml_sha256": digest(inputs[root / OWNER]),
                           "after_yaml_sha256": digest(owner), "change": CHANGE,
                           "verification": VERIFICATION}]}
    backups = {log.with_suffix(".before.yaml"): inputs[root / OWNER],
               log.with_suffix(".before-ledger.tsv"): inputs[root / LEDGER],
               log.with_suffix(".before.sssom.tsv"): inputs[root / SSSOM]}
    return publish(root, {OWNER: owner, LEDGER: ledger}, inputs, log, backups, result, apply=apply)


def table(data: bytes) -> tuple[list[str], list[dict]]:
    reader = csv.DictReader((line for line in data.decode().splitlines() if not line.startswith("#")), delimiter="\t")
    fields = reader.fieldnames or []
    rows = list(reader)
    if not fields or len(set(fields)) != len(fields) or any(None in r or None in r.values() for r in rows):
        raise ValueError("Malformed SSSOM table")
    return fields, rows


def promoted_sssom(before: bytes, candidate: bytes, owner: bytes) -> bytes:
    if digest(before) != SSSOM_BEFORE:
        raise ValueError("SSSOM before-image changed")
    fields, rows = table(before)
    candidate_fields, candidate_rows = table(candidate)
    old = [r for r in rows if r["subject_id"] == SUBJECT]
    selected = [r for r in candidate_rows if r["subject_id"] == SUBJECT]
    if (candidate_fields != fields or len(old) != 2 or len(selected) != 1
            or {(r["object_id"], r["predicate_id"]) for r in old}
            != {(PARENT, "skos:closeMatch"), (OLD, "skos:exactMatch")}):
        raise ValueError("Expected the reviewed two-row preimage and one native candidate row")
    row = dict(selected[0])
    record = yaml.safe_load(owner)
    if corrected_record(owner) != owner or record["identifier"] != NEW:
        raise ValueError("Owner has not completed the NCIT source correction")
    date = max(event["timestamp"][:10] for event in record["curation_history"])
    expected = {"subject_label": NAME, "object_id": NEW, "object_label": LABEL,
                "predicate_id": "skos:exactMatch", "object_source": "obo:ncit.owl",
                "mapping_justification": "semapv:LexicalMatching", "confidence": "0.99",
                "mapping_date": date, "validation_method": "", "comment": "",
                "other": "Na2HPO4.7H2O|Na2HPO4•7H2O|CAS:7782-85-6"}
    if any(row.get(k) != v for k, v in expected.items()):
        raise ValueError("Candidate differs from the bounded native NCIT mapping")
    required_sources = {f"MIM:{e['source']}" for e in record["ontology_mapping"]["evidence"]}
    required_sources.add("MIM:curator=Codex")
    if set(row["source"].split("|")) != required_sources:
        raise ValueError("Candidate lacks exact owner evidence/curator provenance")
    parent = next(r for r in old if r["object_id"] == PARENT)
    row["source"] = "|".join(dict.fromkeys(parent["source"].split("|") + row["source"].split("|")))
    output = io.StringIO(newline="")
    csv.DictWriter(output, fieldnames=fields, delimiter="\t", lineterminator="\n").writerow(row)
    replaced = False
    lines = []
    for line in before.decode().splitlines(keepends=True):
        if line.startswith(SUBJECT + "\t"):
            if not replaced:
                lines.append(output.getvalue())
                replaced = True
        else:
            lines.append(line)
    newest = newest_row_date(lines)
    if not newest:
        raise ValueError("Cannot derive native SSSOM header date")
    return "".join(rewrite(lines, newest)[0]).encode()


def promote(root: Path, log: Path, source_log: Path, candidate: Path,
            candidate_sha256: str, *, apply: bool = False) -> dict:
    source_bytes = source_log.read_bytes()
    source = json.loads(source_bytes)
    owner, ledger, evidence = ((root / p).read_bytes() for p in (OWNER, LEDGER, EVIDENCE))
    verify_evidence(evidence)
    if (source.get("phase") != "sources" or source.get("state") != "complete"
            or source.get("applied") is not True or source.get("approval") != APPROVAL
            or len(source.get("records", [])) != 1
            or source["records"][0]["source_record"] != OWNER.as_posix()
            or source["records"][0]["after_yaml_sha256"] != digest(owner)
            or source.get("ledger_after_sha256") != digest(ledger)
            or corrected_ledger(ledger) != ledger):
        raise ValueError("Completed source receipt does not bind the current owner and ledger")
    before_path = source_log.with_suffix(".before.sssom.tsv")
    before, canonical, proposed = before_path.read_bytes(), (root / SSSOM).read_bytes(), candidate.read_bytes()
    if digest(proposed) != candidate_sha256:
        raise ValueError("Supplied candidate hash changed")
    after = promoted_sssom(before, proposed, owner)
    if canonical == after:
        return {"applied": False, "changed": False, "approval": APPROVAL}
    if canonical != before:
        raise ValueError("Canonical SSSOM changed after the source receipt")
    inputs = {root / OWNER: owner, root / LEDGER: ledger, root / EVIDENCE: evidence,
              root / SSSOM: canonical, source_log: source_bytes, before_path: before,
              candidate: proposed}
    result = {"phase": "promote", "approval": APPROVAL, "records": source["records"],
              "source_receipt_sha256": digest(source_bytes), "candidate_sha256": candidate_sha256,
              "sssom_before_sha256": digest(before), "sssom_after_sha256": digest(after),
              "changed_rows": 1, "removed_rows": 1, "preserved_historical_source_tokens": True}
    return publish(root, {SSSOM: after}, inputs, log,
                   {log.with_suffix(".before.tsv"): before}, result, apply=apply)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("phase", choices=("sources", "promote"))
    parser.add_argument("--root", type=Path, default=ROOT)
    parser.add_argument("--log", type=Path, required=True)
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("--apply", action="store_true")
    mode.add_argument("--dry-run", action="store_true")
    parser.add_argument("--source-log", type=Path)
    parser.add_argument("--candidate", type=Path)
    parser.add_argument("--candidate-sha256")
    args = parser.parse_args(argv)
    if args.phase == "promote" and not all((args.source_log, args.candidate, args.candidate_sha256)):
        parser.error("promote requires --source-log, --candidate and --candidate-sha256")
    from plugins.lock_manager import LockManager
    from plugins.repository_settings import RepositorySettings

    target = RepositorySettings.from_environment().get_target("mediaingredientmech")
    if target.path.resolve() != args.root.resolve():
        raise ValueError("Configured MIM root differs from the requested worktree")
    target.open()
    with LockManager().lock("mediaingredientmech", f"#875 {args.phase}"):
        if args.phase == "sources":
            result = apply_sources(target.path.resolve(), args.log, apply=args.apply)
        else:
            result = promote(target.path.resolve(), args.log, args.source_log,
                             args.candidate, args.candidate_sha256, apply=args.apply)
    print(json.dumps(result, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
