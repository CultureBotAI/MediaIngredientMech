#!/usr/bin/env python3
"""Correct exactly fifteen reviewed hydrate/stock chemistry records (#871/#268), dry-run by default.

The CLI holds the native repository lock; direct callers must hold that lock.
Native publication validates the complete batch before writing and preserves
failure receipts/journals for recovery. This operation grants no approval.
"""

from __future__ import annotations

import argparse
import copy
import datetime as dt
import importlib
import json
import sys
import tempfile
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(ROOT / "src"))
from mediaingredientmech.curate.curation_event import record_curation_event  # noqa: E402
from mediaingredientmech.validation.write_validated import (  # noqa: E402
    write_validated_ingredient,
)
from scripts import apply_owned_name_policy as shared  # noqa: E402
from scripts import promote_heptahydrate_ncit as guarded  # noqa: E402
from scripts import step7a_guarded_publication as publication  # noqa: E402

REPORT = Path("reports/hydrate_stock_chemistry_871_268_20261102")
MANIFEST = REPORT / "source-evidence.json"
MANIFEST_SHA = "44c88cc3ca03038e5e5c94b35c8d6dfd05412451b8d9c75d402512e526b4ef94"
_MANIFEST = shared.regular(ROOT / MANIFEST)
if guarded.digest(_MANIFEST) != MANIFEST_SHA:
    raise ValueError("Reviewed source manifest changed before import")
META = json.loads(_MANIFEST)
OWNERS = tuple(Path(p) for p in META["owners"])
EXPECTED_NAMES = frozenset(
    {
        "Nicl2_X_2_H2o.yaml",
        "Cu_No32_X_3_H2o.yaml",
        "Cecl3_X_7_H2o.yaml",
        "02_Thiamine_Pyrophosphate.yaml",
        "K2hpo4_X_3_H2o.yaml",
        "Nah2po4_X_2_H2o.yaml",
        "Na2hpo4_X_2_H2o.yaml",
        "Cocl2_X_4_H2o.yaml",
        "Chlorhexidine_Diacetate_Salt_Hydrate.yaml",
        "Disodium_Phosphate_Heptahydrate_002_M_Stock.yaml",
        "DL-Isocitric_Acid_Trisodium_Salt_Hydrate.yaml",
        "Cefsulodin_Sodium_Salt_Hydrate.yaml",
        "Bathophenanthrolinedisulfonic_Acid_Disodium_Salt_Hydrate.yaml",
        "Na2hpo4_X_7_H2o.yaml",
        "Cocl2_X_2_H2o.yaml",
    }
)
if set(OWNERS) != {Path("data/ingredients/mapped") / n for n in EXPECTED_NAMES}:
    raise ValueError("Exactly the reviewed fifteen owners are required")
ANCHORS = tuple(Path(p) for p in META["protected_anchors"])
APPROVAL = META["approval"]
ACTION = META["action"]
CURATOR = META["curator"]
CODE_PATHS = tuple(
    dict.fromkeys(
        (
            Path(__file__),
            Path(shared.__file__),
            Path(publication.__file__),
            *shared.CODE_PATHS,
            ROOT / "MAPPING_SEMANTICS.md",
            ROOT / "src/mediaingredientmech/schema/mech_shared.yaml",
            ROOT / "pyproject.toml",
            ROOT / "uv.lock",
        )
    )
)
_LOADED_CODE = {p: shared.regular(p) for p in CODE_PATHS}


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)


def bound_path(path: Path) -> Path:
    path = Path(path).absolute()
    require(path == path.resolve(), "Receipt path must be resolved without aliases")
    return path


def evidence_inputs(root: Path) -> dict[Path, bytes]:
    raw = shared.regular(root / MANIFEST)
    require(raw == _MANIFEST, "Reviewed source manifest changed")
    result = {root / MANIFEST: raw}
    for name, item in META["files"].items():
        path = Path(name)
        require(
            not path.is_absolute() and ".." not in path.parts and path.as_posix() == name,
            "Unsafe evidence path",
        )
        data = shared.regular(root / path)
        require(
            guarded.digest(data) == item["sha256"] and len(data) == item["bytes"],
            f"Reviewed capture/preimage changed: {name}",
        )
        result[root / path] = data
    return result


def frozen(path: Path) -> bytes:
    data = shared.regular(ROOT / META["owners"][str(path)]["preimage"])
    require(guarded.digest(data) == META["owners"][str(path)]["sha256"], "Preimage changed")
    return data


def change_text(path: Path) -> str:
    return META["owners"][str(path)]["event_changes"]


def changed_fields(before: dict, path: Path) -> dict:
    """Only the independently reviewed field matrix; no chemistry inference."""
    proposal = copy.deepcopy(before)
    item = META["owners"][str(path)]
    for field in item["delete"]:
        parts = field.split(".")
        target = proposal
        for part in parts[:-1]:
            target = target[part]
        require(parts[-1] in target, "Reviewed deleted field is absent")
        del target[parts[-1]]
    for field, value in item["set"].items():
        parts = field.split(".")
        target = proposal
        for part in parts[:-1]:
            target = target[part]
        target[parts[-1]] = copy.deepcopy(value)
    return proposal


def propose_sources(original: dict[Path, bytes], *, timestamp: str) -> dict[Path, bytes]:
    require(set(original) == set(OWNERS), "Exactly fifteen owner preimages required")
    when = dt.datetime.fromisoformat(timestamp)
    require(
        when.utcoffset() == dt.timedelta(0)
        and when >= dt.datetime.fromisoformat(META["evidence_not_before"]),
        "Timestamp must be UTC after the reviewed evidence",
    )
    evidence_inputs(ROOT)
    result = {}
    for path in OWNERS:
        require(original[path] == frozen(path), f"Owner differs from reviewed preimage: {path}")
        before = yaml.safe_load(original[path])
        item = META["owners"][str(path)]
        require(
            before.get("identifier") == item["identifier"]
            and before.get("mapping_status") == item["mapping_status"]
            and len(before.get("curation_history", [])) == item["history_count"],
            "Reviewed owner identity/history differs",
        )
        proposal = changed_fields(before, path)
        require(proposal != before, "No substantive correction; history must not be appended")
        record_curation_event(
            proposal,
            curator=CURATOR,
            action=ACTION,
            changes=change_text(path),
            timestamp=timestamp,
            previous_status=before["mapping_status"],
            new_status=before["mapping_status"],
            llm_assisted=True,
            llm_model=META["llm_model"],
        )
        unchanged = copy.deepcopy(proposal)
        event = unchanged["curation_history"].pop()
        require(
            unchanged == changed_fields(before, path) and event["action"] == ACTION,
            "Unexpected proposal field",
        )
        with tempfile.TemporaryDirectory(prefix="mim-871-268-render-") as directory:
            target = Path(directory) / path.name
            write_validated_ingredient(proposal, target)
            result[path] = target.read_bytes()
    return result


def verify_complete(current: dict[Path, bytes]) -> str:
    require(set(current) == set(OWNERS), "Exactly fifteen completed owners required")
    try:
        stamps = {
            yaml.safe_load(data)["curation_history"][-1]["timestamp"] for data in current.values()
        }
    except (KeyError, TypeError, IndexError) as error:
        raise ValueError("Incomplete source correction") from error
    require(len(stamps) == 1, "Completed owner timestamps differ")
    stamp = stamps.pop()
    require(
        current == propose_sources({p: frozen(p) for p in OWNERS}, timestamp=stamp),
        "Partial or changed source correction",
    )
    return stamp


def backups(log: Path) -> dict[Path, Path]:
    return {p: log.with_name(log.stem + ".before-" + p.name) for p in OWNERS}


def native_code_inputs() -> dict[Path, bytes]:
    """Bind executed native publication modules; optional imports stay off pure paths."""
    modules = [
        importlib.import_module(name)
        for name in (
            "kg_microbe_write",
            "kg_microbe_write.transaction",
        )
    ]
    return {
        Path(module.__file__).resolve(): shared.regular(Path(module.__file__).resolve())
        for module in modules
    }


def source_context(root: Path, current: dict[Path, bytes]):
    timestamp = verify_complete(current)
    paths = shared.ingredient_paths(root)
    require({root / p for p in OWNERS} <= paths, "Missing reviewed owner")
    inputs = {p: shared.regular(p) for p in paths}
    inputs.update(evidence_inputs(root))
    for path, expected in _LOADED_CODE.items():
        data = shared.regular(path)
        require(data == expected, "Loaded writer dependency changed")
        inputs[path] = data
    for path in ANCHORS:
        data = shared.regular(root / path)
        require(
            guarded.digest(data) == META["protected_anchors"][str(path)], "Protected anchor changed"
        )
        inputs[root / path] = data
    inputs.update(native_code_inputs())
    historical = inputs | {root / p: frozen(p) for p in OWNERS}
    result = {
        "phase": "sources",
        "approval": APPROVAL,
        "timestamp": timestamp,
        "evidence_manifest": str(root / MANIFEST),
        "evidence_manifest_sha256": MANIFEST_SHA,
        "input_sha256": {str(p): guarded.digest(b) for p, b in historical.items()},
        "output_sha256": {str(p): guarded.digest(b) for p, b in current.items()},
        "records": [
            {
                "source_record": str(p),
                "shape": META["owners"][str(p)]["shape"],
                "before_yaml_sha256": META["owners"][str(p)]["sha256"],
                "after_yaml_sha256": guarded.digest(current[p]),
                "change": change_text(p),
                "verification": (
                    "Exact reviewed owner preimage and primary chemistry evidence bound by "
                    f"{MANIFEST}@sha256={MANIFEST_SHA}; only the explicit delete/set matrix "
                    "and one history event are applied. " + APPROVAL
                ),
            }
            for p in OWNERS
        ],
    }
    shared.validate_scope(root, inputs, paths)
    return inputs, result, paths


def source_receipt(root: Path, log: Path):
    root, log = shared.checked_root(root), bound_path(log)
    current = {p: shared.regular(root / p) for p in OWNERS}
    inputs, result, paths = source_context(root, current)
    inputs[log] = shared.completed_receipt(log, result, root, changed=set(OWNERS))
    for path, backup in backups(log).items():
        data = shared.regular(backup)
        require(data == frozen(path), "Completed receipt preimage changed")
        inputs[backup] = data
    inputs.update(
        publication.completed_journal(
            root, log, json.loads(inputs[log]), previous={p: frozen(p) for p in OWNERS}
        )
    )
    shared.validate_scope(root, inputs, paths)
    return inputs, result


def apply_sources(root: Path, log: Path, *, apply: bool = False):
    root, log = shared.checked_root(root), bound_path(log)
    original = {p: shared.regular(root / p) for p in OWNERS}
    if original != {p: frozen(p) for p in OWNERS}:
        source_receipt(root, log)
        return {"applied": False, "changed": False, "approval": APPROVAL}
    current = propose_sources(original, timestamp=dt.datetime.now(dt.timezone.utc).isoformat())
    inputs, result, paths = source_context(root, current)
    return publication.publish(
        root,
        current,
        inputs,
        log,
        {backup: original[p] for p, backup in backups(log).items()},
        result,
        apply=apply,
        validate_scope=lambda: shared.validate_scope(root, inputs, paths),
    )


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=ROOT)
    parser.add_argument("--log", type=Path, required=True)
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("--apply", action="store_true")
    mode.add_argument("--dry-run", action="store_true")
    args = parser.parse_args(argv)
    from plugins.lock_manager import LockManager
    from plugins.repository_settings import RepositorySettings

    root = shared.checked_root(args.root)
    target = RepositorySettings.from_environment().get_target("mediaingredientmech")
    require(target.path.resolve() == root, "Configured MIM root differs")
    target.open()
    with LockManager().lock(
        "mediaingredientmech", "#871/#268 fifteen bounded chemistry corrections"
    ):
        result = apply_sources(root, args.log, apply=args.apply)
    print(json.dumps(result, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
