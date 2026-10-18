"""Apply only the frozen, reviewed #232 parent-name synonym decisions.

Mirrors trait_synonyms/apply.py. The default invocation validates the plan
without writing; --stamp records the derived after-hashes into the plan once;
--apply performs the guarded write; --verify requires the completed state.
Aggregate and generated-product synchronization is deliberately separate.
"""

from __future__ import annotations

import argparse
import copy
import hashlib
import json
from pathlib import Path

import yaml

from mediaingredientmech.curate.curation_event import record_curation_event
from mediaingredientmech.validation.write_validated import (
    ValidationFailedError,
    validate_ingredient,
    write_validated_ingredient,
)

ROOT = Path(__file__).resolve().parents[3]
FOLDER = Path(__file__).resolve().parent
ISSUE = "https://github.com/CultureBotAI/MediaIngredientMech/issues/232"
EXPECTED_RECORDS, EXPECTED_TOKENS = 23, 57


def sha256_bytes(value: bytes) -> str:
    return hashlib.sha256(value).hexdigest()


def json_sha256(value: object) -> str:
    return sha256_bytes(json.dumps(value, sort_keys=True, ensure_ascii=False, separators=(",", ":")).encode())


def yaml_bytes(record: dict) -> bytes:
    return yaml.safe_dump(record, default_flow_style=False, sort_keys=False, allow_unicode=True, width=80).encode()


def reviewed_after(entry: dict, timestamp: str) -> dict:
    """Derive the only allowed change; unrelated claims cannot enter via a plan."""
    before = entry["before_record"]
    if before["identifier"] != entry["identifier"]:
        raise ValueError(f"Owner identity mismatch: {entry['source_record']}")
    if json_sha256(before) != entry["before_record_sha256"]:
        raise ValueError(f"Invalid archived source: {entry['source_record']}")
    after = copy.deepcopy(before)
    positions, tokens = set(), []
    for decision in entry["decisions"]:
        position = decision["synonym_position"]
        if position in positions:
            raise ValueError("Duplicate synonym decision")
        positions.add(position)
        synonym = after["synonyms"][position]
        if synonym != decision["before_synonym"]:
            raise ValueError("Reviewed synonym payload or position changed")
        if decision["disposition"] != "REJECTED_LABEL" or not decision["reason"]:
            raise ValueError("Missing explicit non-name disposition")
        if synonym["synonym_type"] == "REJECTED_LABEL":
            raise ValueError("Plan must not append an event for an unchanged synonym")
        synonym["synonym_type"] = "REJECTED_LABEL"
        tokens.append(synonym["synonym_text"])
    if not tokens:
        raise ValueError("Empty record review")
    record_curation_event(
        after,
        curator="claude",
        action="REJECTED_PARENT_NAME_SYNONYMS",
        changes=(
            "Retyped names of the parent compound or of a different hydrate as "
            "provenance-only REJECTED_LABEL, because this record is a distinct salt, "
            "hydrate or tombstone form and the label index resolved the parent's name "
            "here (#232): "
            + "; ".join(repr(token) for token in tokens)
            + ". Preserved original text and source metadata. No identity, mapping, "
            "role, or remaining-synonym claim was adjudicated."
        ),
        llm_assisted=True,
        timestamp=timestamp,
    )
    return after


def validate_plan(plan: dict, root: Path, stamp: bool = False) -> list[tuple[Path, dict, bool]]:
    if plan["issue"] != ISSUE or plan["schema_version"] != 1:
        raise ValueError("Unexpected review plan")
    entries = plan["records"]
    if len(entries) != EXPECTED_RECORDS or sum(len(e["decisions"]) for e in entries) != EXPECTED_TOKENS:
        raise ValueError(f"The reviewed scope is exactly {EXPECTED_RECORDS} records / {EXPECTED_TOKENS} tokens")
    paths, prepared = set(), []
    for entry in entries:
        relative = Path(entry["source_record"])
        if relative.parent != Path("data/ingredients/mapped") or relative.suffix != ".yaml":
            raise ValueError("Unexpected target path")
        if relative in paths:
            raise ValueError("Duplicate source record")
        paths.add(relative)
        after = reviewed_after(entry, plan["curation_timestamp"])
        if stamp:
            entry["after_record_sha256"] = json_sha256(after)
            entry["after_yaml_sha256"] = sha256_bytes(yaml_bytes(after))
        if json_sha256(after) != entry["after_record_sha256"]:
            raise ValueError("Reviewed final record changed")
        if sha256_bytes(yaml_bytes(after)) != entry["after_yaml_sha256"]:
            raise ValueError("Reviewed final serialization changed")
        for record in (entry["before_record"], after):
            errors = validate_ingredient(record)
            if errors:
                raise ValidationFailedError(root / relative, errors)
        current_bytes = (root / relative).read_bytes()
        current = yaml.safe_load(current_bytes)
        done = current == after and sha256_bytes(current_bytes) == entry["after_yaml_sha256"]
        if not done and (current != entry["before_record"] or sha256_bytes(current_bytes) != entry["before_yaml_sha256"]):
            raise ValueError(f"Source changed since review: {relative}")
        prepared.append((root / relative, after, done))
    return prepared


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    group = parser.add_mutually_exclusive_group()
    group.add_argument("--stamp", action="store_true")
    group.add_argument("--apply", action="store_true")
    group.add_argument("--verify", action="store_true")
    parser.add_argument("--root", type=Path, default=ROOT)
    args = parser.parse_args()
    plan_path = FOLDER / "decisions.json"
    plan = json.loads(plan_path.read_text())
    prepared = validate_plan(plan, args.root, stamp=args.stamp)
    if args.stamp:
        plan_path.write_text(json.dumps(plan, indent=2, ensure_ascii=False) + "\n")
    pending = [(path, after) for path, after, done in prepared if not done]
    if args.verify and pending:
        raise ValueError("Reviewed source changes are not yet fully applied")
    if args.apply and pending:
        baseline = plan["baseline_sssom"]
        if sha256_bytes((args.root / baseline["path"]).read_bytes()) != baseline["sha256"]:
            raise ValueError("Published SSSOM changed since the exact token review")
        for path, after in pending:
            write_validated_ingredient(after, path)
        if not all(done for _, _, done in validate_plan(plan, args.root)):
            raise ValueError("Source write verification failed")
        receipt = {
            "issue": ISSUE, "status": "SOURCE_CORRECTION_APPLIED",
            "decisions_sha256": sha256_bytes(plan_path.read_bytes()),
            "records_changed": len(pending), "parent_name_tokens_retyped": EXPECTED_TOKENS,
            "closed_schema_before_after": "PASS",
            "only_reviewed_synonym_types_and_one_curation_event_changed": "PASS",
            "original_text_and_source_metadata_preserved": "PASS",
            "generated_products": "Synchronization and regeneration owned by parent task",
        }
        (FOLDER / "apply-receipt.json").write_text(json.dumps(receipt, indent=2) + "\n")
    print(json.dumps({"status": "PASS", "records_validated_before_and_after": len(prepared), "parent_name_tokens_reviewed": EXPECTED_TOKENS,
                      "pending_source_writes": 0 if args.apply else len(pending),
                      "mode": "stamp" if args.stamp else "apply" if args.apply else "verify" if args.verify else "check"}, indent=2))


if __name__ == "__main__":
    main()
