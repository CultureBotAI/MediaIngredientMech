#!/usr/bin/env python3
"""Apply only the reviewed WC stock identity correction (#751), dry-run by default.

The CLI holds the native repository lock; direct callers must hold that lock.
The owner is published through the native validated transaction with reserved
receipt/preimage outputs. SSSOM and generated products are separate phases.
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
from mediaingredientmech.utils.culturemech_occurrences import (  # noqa: E402
    SOURCE_LABEL_IDENTIFIER_OVERRIDES,
    _source_label_key,
)
from mediaingredientmech.validation.write_validated import (  # noqa: E402
    write_validated_ingredient,
)
from scripts import apply_owned_name_policy as shared  # noqa: E402
from scripts import promote_heptahydrate_ncit as guarded  # noqa: E402
from scripts import step7a_guarded_publication as publication  # noqa: E402

REPORT = Path("reports/step7c_wc_stock_751_20261102")
MANIFEST = REPORT / "source-evidence.json"
MANIFEST_SHA = "1076868a28ad39636742ad314a7a7782e981151aa98e85bc95bcf91b6a3e9b5a"
_MANIFEST = shared.regular(ROOT / MANIFEST)
if guarded.digest(_MANIFEST) != MANIFEST_SHA:
    raise ValueError("Reviewed WC manifest changed before import")
META = json.loads(_MANIFEST)
OWNER = Path("data/ingredients/mapped/Wc_Trace_Elements_Solution.yaml")
OWNERS = (OWNER,)
OLD = "MICRO:0000455"
NEW = "kgmicrobe.ingredient:wc_trace_elements_solution"
NAME = "WC Trace Elements Solution"
ACTION = "REKEYED_WC_STOCK_IDENTITY"
APPROVAL = META["approval"]
ANCHORS = tuple(Path(p) for p in META["protected_anchors"])
UTEX_URL = "https://utex.org/products/wc-trace-elements-solution"
MICRO_URL = (
    "https://raw.githubusercontent.com/carrineblank/MicrO/"
    "73963269d9a681157d710f272f8e65e4f7e8897e/MicrOandImportModules/MicrO.owl"
)
VERIFICATION = (
    f"UTEX {UTEX_URL} defines an eight-component WC stock used by WC and WC+; "
    f"MicrO {MICRO_URL} defines MICRO:0000455 as the generic trace elements solution "
    "class. A complete label/synonym scan of that immutable ontology found no "
    "WC-specific class. Primary capture hashes, exact class/table extracts and "
    f"the reviewed owner preimage are bound by {MANIFEST} sha256={MANIFEST_SHA}. "
    "Under MAPPING_SEMANTICS section 3 step 3 this specific mixture has a local "
    "ingredient identity and NARROW_MATCH grounding, exported as skos:broadMatch "
    "to the generic class. The earlier stem-match evidence is retained as history; "
    "it does not establish the generic class as this stock's identity."
)
EVIDENCE = {"evidence_type": "MANUAL_CURATION", "source": UTEX_URL, "notes": VERIFICATION}
CHANGE = (
    f"#751: identifier {OLD} -> {NEW}; mapping_quality LEXICAL_MATCH -> NARROW_MATCH "
    "to the unchanged MICRO:0000455 parent. Preserve the source label, prior "
    "mapping evidence and history, stored occurrences, stock type and provisional "
    "nutritional role. No component, chemistry, membership or role enrichment. "
    f"Reviewed owner sha256={META['owner_sha256']}. {VERIFICATION} {APPROVAL}"
)
CODE_PATHS = tuple(dict.fromkeys((
    Path(__file__), Path(shared.__file__), Path(publication.__file__), *shared.CODE_PATHS,
    ROOT / "src/mediaingredientmech/utils/culturemech_occurrences.py",
    ROOT / "MAPPING_SEMANTICS.md", ROOT / "src/mediaingredientmech/schema/mech_shared.yaml",
    ROOT / "pyproject.toml", ROOT / "uv.lock",
)))
_LOADED_CODE = {p: shared.regular(p) for p in CODE_PATHS}


def require(condition, message):
    if not condition:
        raise ValueError(message)


def bound_path(path):
    path = Path(path).absolute()
    require(path == path.resolve(), "Receipt path must be resolved without aliases")
    return path


def evidence_inputs(root):
    raw = shared.regular(root / MANIFEST)
    require(raw == _MANIFEST, "Reviewed WC source manifest changed")
    result = {root / MANIFEST: raw}
    for name, item in META["files"].items():
        path = Path(name)
        require(not path.is_absolute() and ".." not in path.parts
                and path.as_posix() == name, "Unsafe evidence path")
        data = shared.regular(root / path)
        require(guarded.digest(data) == item["sha256"] and len(data) == item["bytes"],
                f"Reviewed WC capture/preimage changed: {name}")
        result[root / path] = data
    return result


def frozen():
    data = shared.regular(ROOT / META["preimage"])
    require(guarded.digest(data) == META["owner_sha256"], "Reviewed WC preimage changed")
    return data


def propose_sources(original, *, timestamp):
    require(set(original) == set(OWNERS), "Exactly the WC owner preimage is required")
    when = dt.datetime.fromisoformat(timestamp)
    require(when.utcoffset() == dt.timedelta(0)
            and when >= dt.datetime.fromisoformat(META["evidence_not_before"]),
            "Timestamp must be UTC after the reviewed evidence")
    evidence_inputs(ROOT)
    require(original[OWNER] == frozen(), "WC owner differs from reviewed preimage")
    before = yaml.safe_load(original[OWNER])
    require(before.get("identifier") == OLD and before.get("preferred_term") == NAME
            and before.get("mapping_status") == "MAPPED"
            and before.get("ingredient_type") == "STOCK_SOLUTION"
            and before["ontology_mapping"]["ontology_id"] == OLD
            and before["ontology_mapping"]["mapping_quality"] == "LEXICAL_MATCH",
            "Unexpected WC identity or mapping")
    proposal = copy.deepcopy(before)
    proposal["identifier"] = NEW
    proposal["ontology_mapping"]["mapping_quality"] = "NARROW_MATCH"
    proposal["ontology_mapping"]["evidence"].append(dict(EVIDENCE))
    record_curation_event(
        proposal, curator="Codex", action=ACTION, changes=CHANGE, timestamp=timestamp,
        previous_status="MAPPED", new_status="MAPPED", llm_assisted=True, llm_model="gpt-6",
    )
    with tempfile.TemporaryDirectory(prefix="mim-wc-751-render-") as directory:
        target = Path(directory) / OWNER.name
        write_validated_ingredient(proposal, target)
        return {OWNER: target.read_bytes()}


def verify_complete(current):
    require(set(current) == set(OWNERS), "Exactly the completed WC owner is required")
    try:
        stamp = yaml.safe_load(current[OWNER])["curation_history"][-1]["timestamp"]
    except (KeyError, TypeError, IndexError) as error:
        raise ValueError("Incomplete WC source correction") from error
    require(current == propose_sources({OWNER: frozen()}, timestamp=stamp),
            "Partial or changed WC source correction")
    return stamp


def unique_destination(root, paths):
    """Include ignored/nested owners; a parent or tombstone cannot own the mint."""
    for path in paths:
        if path == root / OWNER:
            continue
        record = yaml.safe_load(shared.regular(path))
        if not isinstance(record, dict):
            continue
        identities = [record.get("identifier", "")]
        if record.get("mapping_status") == "MAPPED":
            identities.append((record.get("ontology_mapping") or {}).get("ontology_id", ""))
        require(not any(str(value).strip().casefold() == NEW.casefold() for value in identities),
                f"WC destination identity already held by {path}")


def backups(log):
    return {OWNER: log.with_name(log.stem + ".before-" + OWNER.name)}


def native_code_inputs():
    modules = [importlib.import_module(name)
               for name in ("kg_microbe_write", "kg_microbe_write.transaction")]
    return {Path(m.__file__).resolve(): shared.regular(Path(m.__file__).resolve()) for m in modules}


def source_context(root, current):
    timestamp = verify_complete(current)
    paths = shared.ingredient_paths(root)
    require(root / OWNER in paths, "Reviewed WC owner is absent")
    unique_destination(root, paths)
    require(SOURCE_LABEL_IDENTIFIER_OVERRIDES.get(_source_label_key(NAME)) == NEW,
            "Exact WC source-label override is absent")
    inputs = {p: shared.regular(p) for p in paths} | evidence_inputs(root)
    for path, expected in _LOADED_CODE.items():
        data = shared.regular(path)
        require(data == expected, "Loaded WC writer dependency changed")
        inputs[path] = data
    for path in ANCHORS:
        data = shared.regular(root / path)
        require(guarded.digest(data) == META["protected_anchors"][str(path)],
                "Protected publication anchor changed")
        inputs[root / path] = data
    inputs.update(native_code_inputs())
    historical = inputs | {root / OWNER: frozen()}
    result = {
        "phase": "sources", "approval": APPROVAL, "timestamp": timestamp,
        "evidence_manifest": str(root / MANIFEST), "evidence_manifest_sha256": MANIFEST_SHA,
        "input_sha256": {str(p): guarded.digest(b) for p, b in historical.items()},
        "output_sha256": {str(p): guarded.digest(b) for p, b in current.items()},
        "records": [{"source_record": str(OWNER), "shape": "local_stock_identity",
                     "before_yaml_sha256": META["owner_sha256"],
                     "after_yaml_sha256": guarded.digest(current[OWNER]),
                     "change": CHANGE, "verification": VERIFICATION + " " + APPROVAL}],
    }
    shared.validate_scope(root, inputs, paths)
    return inputs, result, paths


def source_receipt(root, log):
    root, log = shared.checked_root(root), bound_path(log)
    current = {OWNER: shared.regular(root / OWNER)}
    inputs, result, paths = source_context(root, current)
    inputs[log] = shared.completed_receipt(log, result, root, changed=set(OWNERS))
    backup = backups(log)[OWNER]
    data = shared.regular(backup)
    require(data == frozen(), "Completed WC receipt preimage changed")
    inputs[backup] = data
    inputs.update(publication.completed_journal(
        root, log, json.loads(inputs[log]), previous={OWNER: frozen()},
    ))
    shared.validate_scope(root, inputs, paths)
    return inputs, result


def apply_sources(root, log, *, apply=False):
    root, log = shared.checked_root(root), bound_path(log)
    original = {OWNER: shared.regular(root / OWNER)}
    if original != {OWNER: frozen()}:
        source_receipt(root, log)
        return {"applied": False, "changed": False, "approval": APPROVAL}
    current = propose_sources(original, timestamp=dt.datetime.now(dt.timezone.utc).isoformat())
    inputs, result, paths = source_context(root, current)
    return publication.publish(
        root, current, inputs, log, {backups(log)[OWNER]: original[OWNER]}, result, apply=apply,
        validate_scope=lambda: shared.validate_scope(root, inputs, paths),
    )


def main(argv=None):
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
    with LockManager().lock("mediaingredientmech", "#751 bounded WC stock identity"):
        result = apply_sources(root, args.log, apply=args.apply)
    print(json.dumps(result, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
