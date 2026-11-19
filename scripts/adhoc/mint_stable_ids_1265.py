#!/usr/bin/env python3
"""One-time, offline #1265 migration (2026-11-08).

Inputs: exact pre-migration Git tree, record YAMLs and published SSSOM.
Outputs: validated records, immutable registries and hash-bound migration receipt.
Dry run stages under .temp; --apply uses Claw's ValidatedWriteTransaction, which
must be installed or on PYTHONPATH. No science/status/old-history edits are allowed.
Run from the isolated MIM worktree, with no concurrent writers to these paths.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import subprocess
import sys
from copy import deepcopy
from datetime import datetime, timedelta
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "src"))
from mediaingredientmech.curate.curation_event import record_curation_event  # noqa: E402
from mediaingredientmech.curie import mim_curie_for_stem  # noqa: E402
from mediaingredientmech.stable_ids import (  # noqa: E402
    LIFECYCLE_PATH,
    MIM_PREFIX,
    REGISTRY_PATH,
    Registry,
    allocate_ids,
    dump_lifecycle,
    dump_registry,
    validate_records,
)
from mediaingredientmech.validation.write_validated import write_validated_ingredient  # noqa: E402

SOURCE_COMMIT = "0dac278466699129a083343a921c2e0ca18a9ab4"
SSSOM = Path("mappings/ingredient_mappings.sssom.tsv")
RECEIPT = Path("reports/stable_ids_1265_20261108/migration.json")


def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def encode(value: dict) -> bytes:
    return (json.dumps(value, indent=2, ensure_ascii=False) + "\n").encode()


def migrate_record(record: dict, path: str, identifier: str, timestamp: str) -> dict:
    if "mim_id" in record or "legacy_identifiers" in record:
        raise ValueError("Initial mint refuses an already identified record")
    result = deepcopy(record)
    result["mim_id"] = identifier
    result["legacy_identifiers"] = list(dict.fromkeys([
        mim_curie_for_stem(Path(path).stem), record["identifier"],
    ]))
    record_curation_event(
        result, curator="codex", action="ASSIGNED_MIM_ID", llm_assisted=True,
        timestamp=timestamp,
        changes=f"#1265: assigned permanent {identifier}; retained mapping identifier and legacy aliases.",
    )
    # This native per-record-only field is appended by sync-curated's exporter.
    if "discussions" in result:
        result["discussions"] = result.pop("discussions")
    return result


def migrate_sssom(raw: bytes, aliases: dict[str, str]) -> bytes:
    lines = raw.decode().splitlines(keepends=True)
    prefix_count = 0
    columns = None
    result = []
    for line in lines:
        if re.match(r"#\s+MIM:", line):
            result.append(f'#   MIM: "{MIM_PREFIX}"\n')
            prefix_count += 1
        elif line.startswith("#") or not line.strip():
            result.append(line)
        elif columns is None:
            columns = line.rstrip("\r\n").split("\t")
            result.append(line)
        else:
            fields = line.rstrip("\r\n").split("\t")
            if len(fields) != len(columns):
                raise ValueError("Malformed SSSOM row")
            position = columns.index("subject_id")
            fields[position] = aliases[fields[position]]
            result.append("\t".join(fields) + "\n")
    if prefix_count != 1 or columns is None:
        raise ValueError("Expected exactly one MIM prefix and a SSSOM header")
    return "".join(result).encode()


def require_complete_inventory(root: Path) -> None:
    """Require every direct mapped/unmapped owner from the frozen Git tree (#1277)."""
    groups = ("data/ingredients/mapped", "data/ingredients/unmapped")
    raw = subprocess.check_output(
        ["git", "ls-tree", "-rz", "--name-only", SOURCE_COMMIT, "--", *groups],
        cwd=root, timeout=60,
    )
    baseline = {
        name for item in raw.split(b"\0") if item
        for name in (item.decode(),)
        if Path(name).parent.as_posix() in groups and Path(name).suffix == ".yaml"
    }
    current = {
        path.relative_to(root).as_posix()
        for group in groups for path in (root / group).glob("*.yaml")
    }
    if current != baseline:
        raise ValueError(
            "Complete record inventory differs from frozen baseline: "
            f"missing={sorted(baseline - current)}, extra={sorted(current - baseline)}"
        )


def prepare(root: Path, stage: Path, timestamp: str) -> tuple[dict, dict, dict]:
    when = datetime.fromisoformat(timestamp)
    if when.utcoffset() != timedelta(0):
        raise ValueError("An explicit UTC timestamp is required")
    if stage.exists():
        raise ValueError("Stage already exists; retain it and choose a new stage")
    if not stage.resolve().is_relative_to(root.resolve() / ".temp"):
        raise ValueError("Durable staging must be under this worktree's .temp")
    for relative in (REGISTRY_PATH, LIFECYCLE_PATH, RECEIPT):
        if (root / relative).exists():
            raise ValueError("Initial mint refuses existing registry or receipt")
    require_complete_inventory(root)
    inputs = {}
    records = {}
    for group in ("mapped", "unmapped"):
        for path in sorted((root / "data/ingredients" / group).glob("*.yaml")):
            if path.is_symlink():
                raise ValueError("Record symlinks are not allowed")
            name = path.relative_to(root).as_posix()
            inputs[name] = path.read_bytes()
            records[name] = yaml.safe_load(inputs[name])
    if not records:
        raise ValueError("Empty corpus")
    plan = allocate_ids(Registry(), records, minted_on=when.date().isoformat())
    outputs = {}
    entries = []
    transformed = {}
    aliases = {}
    for name in sorted(records):
        record = migrate_record(records[name], name, plan.assignments[name], timestamp)
        transformed[name] = record
        alias = mim_curie_for_stem(Path(name).stem)
        if alias in aliases:
            raise ValueError("Ambiguous historical SSSOM subject")
        aliases[alias] = record["mim_id"]
        target = stage / name
        write_validated_ingredient(record, target)
        outputs[name] = target.read_bytes()
        entries.append({"path": name, "mim_id": record["mim_id"],
                        "legacy_identifiers": record["legacy_identifiers"],
                        "before_sha256": sha(inputs[name]), "after_sha256": sha(outputs[name])})
    validate_records(plan.registry, transformed)
    inputs[str(SSSOM)] = (root / SSSOM).read_bytes()
    outputs[str(SSSOM)] = migrate_sssom(inputs[str(SSSOM)], aliases)
    outputs[str(REGISTRY_PATH)] = dump_registry(plan.registry)
    outputs[str(LIFECYCLE_PATH)] = dump_lifecycle(plan.registry)
    manifest = {
        "schema_version": 1, "kind": "mim-stable-id-migration/v1",
        "source_commit": SOURCE_COMMIT, "minted_on": when.date().isoformat(),
        "timestamp": timestamp, "registry_path": str(REGISTRY_PATH),
        "lifecycle_path": str(LIFECYCLE_PATH),
        "registry_sha256": sha(outputs[str(REGISTRY_PATH)]),
        "lifecycle_sha256": sha(outputs[str(LIFECYCLE_PATH)]),
        "before_sssom_sha256": sha(inputs[str(SSSOM)]),
        "after_sssom_sha256": sha(outputs[str(SSSOM)]),
        "records": entries, "approval": "NONE", "scientific_approval_added": False,
    }
    outputs[str(RECEIPT)] = encode(manifest)
    for name, raw in outputs.items():
        target = stage / name
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(raw)
    return inputs, outputs, manifest


def publish(root: Path, stage: Path, inputs: dict, outputs: dict, *, apply: bool):
    require_complete_inventory(root)
    from kg_microbe_write import ValidatedWriteTransaction

    def validate(path, text):
        if text.encode() != outputs[path.relative_to(root).as_posix()]:
            raise ValueError("Staged bytes differ")

    # A whole-batch recheck before commit; this isolated worktree has one writer.
    for name, raw in inputs.items():
        if (root / name).read_bytes() != raw:
            raise ValueError(f"Source changed during staging: {name}")
    transaction = ValidatedWriteTransaction(
        root, validator=validate, journal_dir=stage / "transaction-journal",
    )
    for name, raw in outputs.items():
        if name not in inputs and (root / name).exists():
            raise ValueError(f"New output already exists: {name}")
        transaction.stage(name, raw.decode())
    return transaction.commit(apply=apply)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=ROOT)
    parser.add_argument("--stage", type=Path, required=True)
    parser.add_argument("--timestamp", required=True)
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args()
    root = args.root.resolve()
    head = subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=root, text=True).strip()
    if head != SOURCE_COMMIT:
        raise ValueError("One-time migration must start at its frozen base commit")
    stage = args.stage if args.stage.is_absolute() else root / args.stage
    inputs, outputs, manifest = prepare(root, stage, args.timestamp)
    # Compare all source files with Git, not only HEAD's name: reject dirty data.
    from mediaingredientmech.identity_projection import git_files

    baseline = git_files(root, list(inputs))
    for name, raw in inputs.items():
        if raw != baseline[name]:
            raise ValueError(f"Input differs from the approved baseline: {name}")
    result = publish(root, stage, inputs, outputs, apply=args.apply)
    print(json.dumps({"records": len(manifest["records"]), "applied": result.applied,
                      "files": result.touched, "receipt": str(RECEIPT),
                      "stage": str(stage.relative_to(root))}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
