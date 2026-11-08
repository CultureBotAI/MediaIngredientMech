"""Apply an accepted, hash-bound source-only campaign plan (#1174).

This module proves file transitions, not scientific approval. The three allowed
operations are edit, create and explicit unmapped-to-mapped promotion. A batch
is recoverable, not atomically rolled back. Mapping publication is separate.

Inherited surviving collision pairs can receive same-path edits only with their
identifiers, preferred names and statuses preserved (#1251). Reviewed owners can
leave a family, but no new colliding pair inherits the old family exception.
Existing REJECTED owners can receive substantive same-path, same-key maintenance
while remaining REJECTED (#1252). Neither exception approves identity, a merge,
reactivation or demotion; other status/path and provenance guards still apply.
"""

from __future__ import annotations

import builtins
import ctypes
import hashlib
import json
import os
import re
import stat
import subprocess
import sys
import tempfile
import types
import uuid
from dataclasses import dataclass, field
from itertools import combinations
from pathlib import Path, PurePosixPath
from typing import TYPE_CHECKING, Any


def captured_native_modules(root: Path, sources: dict[str, str]) -> dict[str, types.ModuleType]:
    """Execute the bounded native dependencies from captured bytes (#1195).

    Public cached modules are neither reused nor reloaded. The private receipt
    verifier's deferred SSSOM import resolves to the same private capture.
    Other MIM helpers imported by reviewed_sssom are not called by read_sssom.
    """
    captured = {}
    for name, source in sources.items():
        relative_source = Path(source)
        if (
            relative_source.is_absolute()
            or ".." in relative_source.parts
            or relative_source.as_posix() != source
        ):
            raise ValueError("Noncanonical native dependency source")
        path = root / source
        if any(p.is_symlink() for p in (path, *path.parents)):
            raise ValueError("Aliased native dependency source")
        parents = tuple((p, p.stat().st_dev, p.stat().st_ino) for p in path.parents)
        info = path.lstat()
        if not stat.S_ISREG(info.st_mode) or info.st_nlink != 1:
            raise ValueError("Nonregular native dependency source")
        fd = os.open(path, os.O_RDONLY | os.O_NOFOLLOW)
        with os.fdopen(fd, "rb") as stream:
            opened = os.fstat(stream.fileno())
            if (opened.st_dev, opened.st_ino, opened.st_nlink) != (info.st_dev, info.st_ino, 1):
                raise ValueError("Native dependency changed while opening")
            raw = stream.read()
        if parents != tuple((p, p.stat().st_dev, p.stat().st_ino) for p in path.parents):
            raise ValueError("Native dependency parent changed")
        captured[name] = (path, raw, (info.st_dev, info.st_ino))
    modules: dict[str, types.ModuleType] = {}
    prefix = "_mim_campaign_native_" + uuid.uuid4().hex + "."

    def bound_import(name, globals=None, locals=None, fromlist=(), level=0):
        if level == 0 and fromlist and name in captured:
            return load(name)
        return builtins.__import__(name, globals, locals, fromlist, level)

    def load(name):
        if name in modules:
            return modules[name]
        path, raw, identity = captured[name]
        module = types.ModuleType(prefix + name)
        module.__file__ = str(path)
        module.__package__ = name.rpartition(".")[0]
        module.__dict__["__builtins__"] = {**vars(builtins), "__import__": bound_import}
        modules[name] = module
        # Dataclass metadata needs its private module entry. Never replace a
        # public module or alter a preloaded consumer's functions/globals.
        sys.modules[module.__name__] = module
        exec(compile(raw, str(path), "exec"), module.__dict__)
        return module

    for name in sources:
        load(name)
    guard = modules["mediaingredientmech.curate.publication_guard"]
    for name, (path, raw, identity) in captured.items():
        frozen = guard.FrozenFile.capture(path)
        if frozen.content != raw or frozen.identity != identity:
            raise ValueError("Native dependency changed during captured execution")
        modules[name].__dict__["_campaign_executed_source"] = frozen
    return modules


_NATIVE_NAMES = (
    "mediaingredientmech.curate.publication_guard",
    "mediaingredientmech.curate.apply_receipt",
    "mediaingredientmech.validation.write_validated",
    "mediaingredientmech.validation.mapping_change_receipts",
    "mediaingredientmech.export.reviewed_sssom",
)
_BOUND_NATIVE = captured_native_modules(
    Path(__file__).absolute().parents[3],
    {name: "src/" + name.replace(".", "/") + ".py" for name in _NATIVE_NAMES},
)
if TYPE_CHECKING:
    from mediaingredientmech.curate.apply_receipt import reserve_receipt_outputs
    from mediaingredientmech.curate.publication_guard import (
        FrozenFile,
        check_reserved,
        finish_receipt,
        no_alias,
        publish_validated,
    )
    from mediaingredientmech.export.reviewed_sssom import read_sssom
    from mediaingredientmech.validation.mapping_change_receipts import (
        HISTORICAL_CONTEXT,
        RECEIPTS_DIR,
        receipt_paths,
        verify_mapping_chain,
    )
    from mediaingredientmech.validation.write_validated import (
        validate_ingredient,
        write_validated_ingredient,
        yaml,
    )
else:
    _guard = _BOUND_NATIVE["mediaingredientmech.curate.publication_guard"]
    FrozenFile, check_reserved = _guard.FrozenFile, _guard.check_reserved
    finish_receipt, no_alias, publish_validated = (
        _guard.finish_receipt,
        _guard.no_alias,
        _guard.publish_validated,
    )
    reserve_receipt_outputs = _BOUND_NATIVE[
        "mediaingredientmech.curate.apply_receipt"
    ].reserve_receipt_outputs
    _writer = _BOUND_NATIVE["mediaingredientmech.validation.write_validated"]
    validate_ingredient, write_validated_ingredient, yaml = (
        _writer.validate_ingredient,
        _writer.write_validated_ingredient,
        _writer.yaml,
    )
    _chain = _BOUND_NATIVE["mediaingredientmech.validation.mapping_change_receipts"]
    HISTORICAL_CONTEXT, RECEIPTS_DIR = _chain.HISTORICAL_CONTEXT, _chain.RECEIPTS_DIR
    receipt_paths, verify_mapping_chain = _chain.receipt_paths, _chain.verify_mapping_chain
    read_sssom = _BOUND_NATIVE["mediaingredientmech.export.reviewed_sssom"].read_sssom

PLAN_KEYS = {
    "schema_version",
    "operation",
    "repository",
    "baseline_commit",
    "intake_heads",
    "before_inventory",
    "after_inventory",
    "protected_inputs",
    "bindings",
    "records",
}
ACCEPTANCE_KEYS = {
    "schema_version",
    "scope",
    "plan_sha256",
    "baseline_commit",
    "intake_heads",
    "binding_sha256",
    "accepted_operations",
    "review_bindings",
}
RECORD_KEYS = {
    "operation_id",
    "kind",
    "before_source_record",
    "source_record",
    "before_yaml_sha256",
    "after_capture",
    "origins",
    "change",
    "verification",
}
BINDING_KEYS = {"binding_id", "role", "path", "sha256", "published_head", "published_path"}
ORIGIN_KEYS = {
    "worker_slot",
    "head_sha",
    "proposal_id",
    "proposal_binding",
    "payload_binding",
    "case_hashes",
}
ROLES = {
    "case_ledger",
    "shard",
    "decision",
    "evidence",
    "proposal",
    "review",
    "reconciliation",
    "producer",
}
PRODUCERS = (
    "src/mediaingredientmech/curate/campaign_owner_apply.py",
    "scripts/apply_unmatched_campaign_owners.py",
    "src/mediaingredientmech/curate/publication_guard.py",
    "src/mediaingredientmech/curate/apply_receipt.py",
    "src/mediaingredientmech/validation/write_validated.py",
    "src/mediaingredientmech/validation/mapping_change_receipts.py",
    "src/mediaingredientmech/export/reviewed_sssom.py",
    "src/mediaingredientmech/schema/mediaingredientmech.yaml",
    "src/mediaingredientmech/schema/mech_shared.yaml",
    "MAPPING_SEMANTICS.md",
    "uv.lock",
)
APPROVAL = "NONE: source application only; no scientific or mapping approval transfers"

# #1195: keep the dependency captures actually compiled above, not a second
# reading of their paths that might already contain a later version.
_PACKAGE_ROOT = Path(__file__).absolute().parents[3]


def _module_path(name: str) -> Path:
    path = sys.modules[name].__file__
    if not isinstance(path, str):
        raise ValueError("Loaded producer lacks a source path")
    return Path(path).absolute()


_LOADED_LOCATIONS = {
    "src/mediaingredientmech/curate/campaign_owner_apply.py": Path(__file__).absolute(),
    "src/mediaingredientmech/curate/publication_guard.py": _module_path(FrozenFile.__module__),
    "src/mediaingredientmech/curate/apply_receipt.py": _module_path(
        reserve_receipt_outputs.__module__
    ),
    "src/mediaingredientmech/validation/write_validated.py": _module_path(
        write_validated_ingredient.__module__
    ),
    "src/mediaingredientmech/validation/mapping_change_receipts.py": _module_path(
        verify_mapping_chain.__module__
    ),
    "src/mediaingredientmech/export/reviewed_sssom.py": _module_path(read_sssom.__module__),
}
_EXECUTED_SOURCES = {
    "src/" + name.replace(".", "/") + ".py": module._campaign_executed_source
    for name, module in _BOUND_NATIVE.items()
}
LOADED_PRODUCERS = {
    name: (
        _EXECUTED_SOURCES[name]
        if name in _EXECUTED_SOURCES
        else FrozenFile.capture(_LOADED_LOCATIONS.get(name, _PACKAGE_ROOT / name))
    )
    for name in PRODUCERS
}


def _check_loaded_producers() -> None:
    for frozen in LOADED_PRODUCERS.values():
        frozen.verify()


def require(condition: Any, message: str) -> None:
    if not condition:
        raise ValueError(message)


def digest(raw: bytes) -> str:
    return hashlib.sha256(raw).hexdigest()


def encoded(value: Any) -> bytes:
    return (json.dumps(value, indent=2, ensure_ascii=False, allow_nan=False) + "\n").encode()


def closed(value: Any, keys: set[str], label: str) -> dict:
    if not isinstance(value, dict) or set(value) != keys:
        raise ValueError(f"Unexpected fields in {label}")
    return value


def text(value: Any, label: str) -> str:
    if not isinstance(value, str) or not value.strip():
        raise ValueError(f"Missing {label}")
    return value


def sha(value: Any) -> str:
    if not isinstance(value, str) or not re.fullmatch(r"[0-9a-f]{64}", value):
        raise ValueError("Invalid SHA256")
    return value


def commit(value: Any) -> str:
    if not isinstance(value, str) or not re.fullmatch(r"[0-9a-f]{40}", value):
        raise ValueError("Invalid Git commit")
    return value


def relative(value: Any) -> str:
    name = text(value, "relative path")
    path = PurePosixPath(name)
    require(
        not path.is_absolute()
        and ".." not in path.parts
        and path.as_posix() == name
        and "\\" not in name,
        "Noncanonical relative path",
    )
    return name


def owner_path(value: Any) -> str:
    name = relative(value)
    parts = PurePosixPath(name).parts
    require(
        len(parts) == 4
        and parts[:2] == ("data", "ingredients")
        and parts[2] in {"mapped", "unmapped"}
        and parts[3].endswith(".yaml"),
        "Owner must be a direct ingredient YAML",
    )
    return name


def unique_json(raw: bytes) -> Any:
    def pairs(items):
        result = {}
        for key, value in items:
            require(key not in result, "Duplicate JSON key")
            result[key] = value
        return result

    return json.loads(raw, object_pairs_hook=pairs)


class UniqueLoader(yaml.SafeLoader):
    pass


def _yaml_mapping(loader, node, deep=False):
    mapping = {}
    for key_node, value_node in node.value:
        key = loader.construct_object(key_node, deep=deep)
        require(key not in mapping, "Duplicate YAML key")
        mapping[key] = loader.construct_object(value_node, deep=deep)
    return mapping


UniqueLoader.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, _yaml_mapping)


def record(raw: bytes) -> dict:
    result = yaml.load(raw, Loader=UniqueLoader)
    if not isinstance(result, dict):
        raise ValueError("Ingredient payload is not a mapping")
    return result


def git(root: Path, *args: str) -> bytes:
    return subprocess.run(["git", "-C", str(root), *args], check=True, capture_output=True).stdout


def inventory(root: Path) -> dict[str, FrozenFile]:
    result = {}
    for category in ("mapped", "unmapped"):
        directory = root / "data/ingredients" / category
        no_alias(directory)
        require(directory.is_dir(), "Missing owner category")
        # Native corpus includes ignored direct children, not nested backups.
        for pattern in ("*.yaml", "*.yml"):
            for path in sorted(directory.glob(pattern)):
                require(path.suffix == ".yaml", "YML owner needs explicit contract review")
                result[str(path.relative_to(root))] = FrozenFile.capture(path)
    return result


def _snapshot_members(directory: Path) -> set[str]:
    no_alias(directory)
    require(directory.is_dir(), "Historical snapshot directory is missing")
    return {
        str(path.relative_to(directory))
        for path in directory.rglob("*")
        if path.is_file() or path.is_symlink()
    }


def hashes(files: dict[str, FrozenFile]) -> dict[str, str]:
    return {path: digest(item.content) for path, item in sorted(files.items())}


@dataclass
class Prepared:
    root: Path
    plan_ref: dict
    acceptance_ref: dict
    plan: dict
    acceptance: dict
    inputs: dict[str, FrozenFile]
    before: dict[str, FrozenFile]
    after_inventory: dict[str, str]
    payloads: dict[str, bytes]
    checkpoint: dict[str, FrozenFile]
    protected: dict[str, FrozenFile]
    operations: list[dict]
    states: dict[str, FrozenFile] = field(default_factory=dict)


def _ref(
    root: Path,
    value: Any,
    inputs: dict[str, FrozenFile],
    historical: dict[str, bytes] | None = None,
) -> bytes:
    ref = closed(value, {"path", "sha256"}, "file reference")
    path, expected = relative(ref["path"]), sha(ref["sha256"])
    if historical is not None and path in historical:
        raw = historical[path]
    else:
        captured = FrozenFile.capture(root / path)
        require(
            path not in inputs or inputs[path].content == captured.content,
            "Conflicting input bindings",
        )
        inputs[path] = captured
        raw = captured.content
    require(digest(raw) == expected, f"Input hash differs: {path}")
    return raw


def _map(root, ref, key, inputs, historical=None):
    data = closed(unique_json(_ref(root, ref, inputs, historical)), {"schema_version", key}, key)
    require(
        type(data["schema_version"]) is int and data["schema_version"] == 1,
        "Unknown inventory version",
    )
    require(isinstance(data[key], dict), "Inventory must be an object")
    for path, value in data[key].items():
        (owner_path if key == "owners" else relative)(path)
        sha(value)
    return data[key]


def _load(
    root: Path, plan_path: Path, acceptance_path: Path, historical=None, protected_history=None
):
    _check_loaded_producers()
    relative(str(plan_path.relative_to(root)))
    relative(str(acceptance_path.relative_to(root)))
    inputs: dict[str, FrozenFile] = {}
    plan_file, accepted_file = FrozenFile.capture(plan_path), FrozenFile.capture(acceptance_path)
    plan_ref = {"path": str(plan_path.relative_to(root)), "sha256": digest(plan_file.content)}
    accepted_ref = {
        "path": str(acceptance_path.relative_to(root)),
        "sha256": digest(accepted_file.content),
    }
    require(plan_path != acceptance_path, "Plan and acceptance roles collide")
    inputs[plan_ref["path"]], inputs[accepted_ref["path"]] = plan_file, accepted_file
    plan = closed(unique_json(plan_file.content), PLAN_KEYS, "plan")
    acceptance = closed(unique_json(accepted_file.content), ACCEPTANCE_KEYS, "acceptance")
    require(
        type(plan["schema_version"]) is int
        and plan["schema_version"] == 1
        and type(acceptance["schema_version"]) is int
        and acceptance["schema_version"] == 1,
        "Unknown plan or acceptance version",
    )
    require(
        plan["operation"] == "apply_reviewed_campaign_owners"
        and plan["repository"] == "CultureBotAI/MediaIngredientMech",
        "Wrong operation or repository",
    )
    commit(plan["baseline_commit"])
    require(
        acceptance["plan_sha256"] == plan_ref["sha256"]
        and acceptance["baseline_commit"] == plan["baseline_commit"]
        and acceptance["scope"] == "source_application_only",
        "Acceptance does not bind plan",
    )
    require(
        isinstance(plan["intake_heads"], dict) and bool(plan["intake_heads"]),
        "Missing intake heads",
    )
    for slot, head in plan["intake_heads"].items():
        require(re.fullmatch(r"worker-(?:0[1-9]|10)", slot), "Invalid worker slot")
        commit(head)
    require(acceptance["intake_heads"] == plan["intake_heads"], "Accepted heads differ")
    before = _map(root, plan["before_inventory"], "owners", inputs)
    after = _map(root, plan["after_inventory"], "owners", inputs)
    protected = _map(root, plan["protected_inputs"], "files", inputs)
    require(
        isinstance(plan["bindings"], list) and bool(plan["bindings"]), "Missing artifact bindings"
    )
    bindings, binding_bytes = {}, {}
    for binding in plan["bindings"]:
        closed(binding, BINDING_KEYS, "artifact binding")
        name = text(binding["binding_id"], "binding id")
        require(
            name not in bindings and binding["role"] in ROLES, "Duplicate binding or unknown role"
        )
        # Only actual owner preimages may be historical evidence. A protected
        # checkpoint never excuses drift in code, reviews or intake artifacts.
        raw = _ref(
            root,
            {"path": binding["path"], "sha256": binding["sha256"]},
            inputs,
            historical if binding["role"] == "evidence" else None,
        )
        if binding["published_head"] is None:
            require(binding["published_path"] is None, "Partial published binding")
        else:
            head, path = commit(binding["published_head"]), relative(binding["published_path"])
            require(head in plan["intake_heads"].values(), "Artifact uses an undeclared head")
            require(git(root, "show", f"{head}:{path}") == raw, "Published artifact bytes differ")
        bindings[name], binding_bytes[name] = binding, raw
    require(ROLES <= {b["role"] for b in bindings.values()}, "Missing required evidence role")
    require(
        acceptance["binding_sha256"] == {k: b["sha256"] for k, b in bindings.items()},
        "Acceptance omits or changes artifact bindings",
    )
    require(
        isinstance(acceptance["review_bindings"], list)
        and bool(acceptance["review_bindings"])
        and len(set(acceptance["review_bindings"])) == len(acceptance["review_bindings"])
        and all(
            k in bindings and bindings[k]["role"] == "review" for k in acceptance["review_bindings"]
        ),
        "Missing accepted independent review bindings",
    )
    producer_paths = {b["path"] for b in bindings.values() if b["role"] == "producer"}
    require(set(PRODUCERS) == producer_paths, "Producer input set differs")
    for path in PRODUCERS:
        require(
            LOADED_PRODUCERS[path].content == inputs[path].content,
            f"Loaded producer differs: {path}",
        )
    ledgers = [
        unique_json(binding_bytes[k]) for k, b in bindings.items() if b["role"] == "case_ledger"
    ]
    require(len(ledgers) == 1 and isinstance(ledgers[0], list), "Need one full case ledger")
    cases = {}
    for case in ledgers[0]:
        require(
            isinstance(case, dict)
            and isinstance(case.get("case_id"), str)
            and case["case_id"] not in cases,
            "Duplicate or malformed source case",
        )
        cases[case["case_id"]] = digest(
            json.dumps(
                case, sort_keys=True, separators=(",", ":"), ensure_ascii=False, allow_nan=False
            ).encode()
        )
    require(isinstance(plan["records"], list) and bool(plan["records"]), "Empty owner plan")
    payloads, operations, origins_seen, destinations, sources = {}, [], set(), set(), set()
    expected_after = dict(before)
    for entry in plan["records"]:
        closed(entry, RECORD_KEYS, "owner operation")
        opid, kind = text(entry["operation_id"], "operation id"), entry["kind"]
        require(
            opid not in payloads and kind in {"edit", "create", "promote"},
            "Duplicate/unknown operation",
        )
        destination = owner_path(entry["source_record"])
        require(destination.casefold() not in destinations, "Destination collision")
        destinations.add(destination.casefold())
        source = entry["before_source_record"]
        require(
            not any(p.casefold() == destination.casefold() and p != source for p in before),
            "Destination collides with an existing owner path",
        )
        if kind == "create":
            require(
                source is None and entry["before_yaml_sha256"] is None, "Create has a predecessor"
            )
            require(destination not in before, "New owner already exists")
        else:
            source = owner_path(source)
            require(
                source not in sources and before.get(source) == sha(entry["before_yaml_sha256"]),
                "Missing, reused or stale owner preimage",
            )
            sources.add(source)
            if kind == "edit":
                require(source == destination, "Edit cannot relocate an owner")
            else:
                require(
                    source.startswith("data/ingredients/unmapped/")
                    and destination.startswith("data/ingredients/mapped/")
                    and destination not in before,
                    "Invalid promotion paths",
                )
                del expected_after[source]
        text(entry["change"], "change explanation")
        text(entry["verification"], "verification explanation")
        raw = _ref(root, entry["after_capture"], inputs)
        payloads[opid] = raw
        expected_after[destination] = digest(raw)
        require(
            isinstance(entry["origins"], list) and bool(entry["origins"]), "Missing source origins"
        )
        for origin in entry["origins"]:
            closed(origin, ORIGIN_KEYS, "source origin")
            require(
                plan["intake_heads"].get(origin["worker_slot"]) == origin["head_sha"],
                "Origin head differs",
            )
            key = (origin["worker_slot"], origin["proposal_id"])
            require(key not in origins_seen, "A proposal is applied more than once")
            origins_seen.add(key)
            binding = bindings.get(origin["proposal_binding"], {})
            require(
                binding.get("role") == "proposal"
                and binding.get("published_head") == origin["head_sha"],
                "Origin lacks its published proposal binding",
            )
            proposals = unique_json(binding_bytes[origin["proposal_binding"]])
            require(
                isinstance(proposals, dict) and isinstance(proposals.get("proposals"), list),
                "Malformed proposal ledger",
            )
            matches = [
                p for p in proposals["proposals"] if p.get("proposal_id") == origin["proposal_id"]
            ]
            require(len(matches) == 1, "Origin proposal missing or duplicated")
            original = matches[0]
            if kind == "create":
                require(
                    original.get("kind") == "new_owner" and original.get("before_sha256") is None,
                    "New owner origin has a predecessor",
                )
            else:
                require(
                    original.get("kind") == "edit_existing_owner"
                    and original.get("owner_path") == source
                    and original.get("before_sha256") == entry["before_yaml_sha256"],
                    "Origin owner preimage differs",
                )
            original_payload = closed(
                original.get("after_capture"),
                {"root", "path", "sha256"},
                "worker payload reference",
            )
            require(
                original_payload["root"] == "artifact",
                "Original payload must be an archived worker artifact",
            )
            original_path = relative(original_payload["path"])
            original_sha = sha(original_payload["sha256"])
            payload_binding = bindings.get(origin["payload_binding"], {})
            require(
                payload_binding.get("role") == "evidence"
                and payload_binding.get("sha256") == original_sha
                and payload_binding.get("published_head") == origin["head_sha"]
                and (
                    payload_binding.get("published_path") == original_path
                    or str(payload_binding.get("published_path")).endswith("/" + original_path)
                ),
                "Original proposal payload lacks an exact published binding",
            )
            claim = origin["case_hashes"]
            require(
                isinstance(claim, dict)
                and bool(claim)
                and set(claim) == set(matches[0]["case_ids"]),
                "Proposal source cases differ",
            )
            require(
                all(cases.get(caseid) == sha(value) for caseid, value in claim.items()),
                "Source case hash differs",
            )
        operations.append(dict(entry))
    require(expected_after == after, "After inventory is not the exact declared transition")
    require(
        acceptance["accepted_operations"]
        == {entry["operation_id"]: digest(payloads[entry["operation_id"]]) for entry in operations},
        "Acceptance omits or changes final operation payloads",
    )
    require(
        not (set(protected) & (sources | {e["source_record"] for e in operations})),
        "Protected input is an owner output",
    )
    for path, expected in protected.items():
        _ref(root, {"path": path, "sha256": expected}, inputs, protected_history)
    return (
        plan_ref,
        accepted_ref,
        plan,
        acceptance,
        inputs,
        before,
        after,
        protected,
        payloads,
        operations,
    )


def _validate_records(root, operations, payloads, before_bytes):
    before = {path: record(raw) for path, raw in before_bytes.items()}
    after = dict(before)
    for entry in operations:
        if entry["before_source_record"] is not None:
            del after[entry["before_source_record"]]
        after[entry["source_record"]] = record(payloads[entry["operation_id"]])

    def collision_pairs(records):
        indexes: dict[tuple[str, Any], set[str]] = {}
        for path, data in records.items():
            for key_kind, value in (
                ("identifier", data.get("identifier")),
                ("preferred name", str(data.get("preferred_term", "")).casefold()),
            ):
                indexes.setdefault((key_kind, value), set()).add(path)
        return {
            (*key, left, right)
            for key, paths in indexes.items()
            for left, right in combinations(sorted(paths), 2)
        }

    # #1251: compare the complete catalogue, not selected-owner uniqueness.
    # No new member, replacement, key change or relocation inherits a pair.
    # Owners leaving a family may follow the ordinary reviewed identity route.
    prior_pairs, final_pairs = collision_pairs(before), collision_pairs(after)
    require(
        final_pairs <= prior_pairs,
        "Final proposed owners introduce a new collision pair",
    )
    family_paths = {path for _, _, left, right in final_pairs for path in (left, right)}
    for entry in operations:
        data = record(payloads[entry["operation_id"]])
        source = entry["before_source_record"]
        old = before[source] if source is not None else {}
        retained_keys = data.get("identifier") == old.get("identifier") and data.get(
            "preferred_term"
        ) == old.get("preferred_term")
        if source in family_paths:
            require(
                entry["kind"] == "edit"
                and source == entry["source_record"]
                and retained_keys
                and data.get("mapping_status") == old.get("mapping_status"),
                "Inherited collision family requires unchanged paths, keys and statuses",
            )
        errors = validate_ingredient(
            data,
            target_class="IngredientRecord",
            schema_path=root / "src/mediaingredientmech/schema/mediaingredientmech.yaml",
        )
        require(not errors, "Native IngredientRecord validation failed")
        history = data.get("curation_history")
        if not isinstance(history, list) or not history:
            raise ValueError("Missing curation history")
        # #1252: inherited tombstones may be maintained, never revived or
        # recreated through this exception. Other category rules stay intact.
        if "REJECTED" in (old.get("mapping_status"), data.get("mapping_status")):
            require(
                entry["kind"] == "edit"
                and source == entry["source_record"]
                and old.get("mapping_status") == data.get("mapping_status") == "REJECTED"
                and retained_keys,
                "Rejected owner requires same-path, same-key rejected maintenance",
            )
        else:
            require(
                (data.get("mapping_status") == "MAPPED")
                == entry["source_record"].startswith("data/ingredients/mapped/"),
                "Owner category differs from mapping status",
            )
        if source is not None:
            prior = old.get("curation_history", [])
            require(
                history[: len(prior)] == prior and len(history) > len(prior),
                "History prefix was altered or not extended",
            )
            require(
                {k: v for k, v in old.items() if k != "curation_history"}
                != {k: v for k, v in data.items() if k != "curation_history"},
                "History-only/no-op application refused",
            )
            if entry["kind"] == "promote":
                require(
                    old.get("mapping_status") == "UNMAPPED"
                    and data.get("mapping_status") == "MAPPED",
                    "Wrong promotion lineage",
                )


def prepare(root: Path, plan_path: Path, acceptance_path: Path) -> Prepared:
    root = root.absolute()
    no_alias(root)
    require(".." not in root.parts, "Noncanonical repository root")
    loaded = _load(root, plan_path.absolute(), acceptance_path.absolute())
    (
        plan_ref,
        acceptance_ref,
        plan,
        accepted,
        inputs,
        expected_before,
        after,
        protected_map,
        payloads,
        operations,
    ) = loaded
    require(
        git(root, "rev-parse", "HEAD").decode().strip() == plan["baseline_commit"],
        "Integration HEAD differs",
    )
    require(
        not git(root, "diff", "--name-only", "HEAD", "--").strip(),
        "Tracked checkout has outstanding changes",
    )
    before = inventory(root)
    require(hashes(before) == expected_before, "Complete owner inventory differs")
    _validate_records(root, operations, payloads, {p: f.content for p, f in before.items()})
    proof = verify_mapping_chain(root)
    for entry in operations:
        if entry["kind"] == "promote":
            require(
                not proof["owner_chains"].get(entry["before_source_record"]),
                "Promotion source has prior native owner-chain links",
            )
        if entry["kind"] == "edit":
            chain = proof["owner_chains"].get(entry["before_source_record"], [])
            require(
                not chain or chain[-1]["after_sha256"] == entry["before_yaml_sha256"],
                "Selected owner preimage is disconnected from native history",
            )
        else:
            require(
                not proof["owner_chains"].get(entry["source_record"]),
                "New destination has prior native owner-chain links",
            )
    checkpoint = {p: FrozenFile.capture(root / p) for p in proof["input_hashes"]}
    require(
        all(protected_map.get(path) == value for path, value in proof["input_hashes"].items()),
        "Accepted protected inputs omit native checkpoint pins",
    )
    require(hashes(checkpoint) == proof["input_hashes"], "Native checkpoint changed")
    # Complete rendering happens before receipt reservation or owner mutation.
    scratch = root / ".temp"
    no_alias(scratch)
    scratch.mkdir(exist_ok=True)
    with tempfile.TemporaryDirectory(prefix="mim-owner-render-", dir=scratch) as directory:
        for index, entry in enumerate(operations):
            path = Path(directory) / f"{index}.yaml"
            write_validated_ingredient(
                record(payloads[entry["operation_id"]]),
                path,
                target_class="IngredientRecord",
                schema_path=root / "src/mediaingredientmech/schema/mediaingredientmech.yaml",
            )
            require(
                path.read_bytes() == payloads[entry["operation_id"]],
                "Reviewed payload is not native-rendered bytes",
            )
    result = Prepared(
        root,
        plan_ref,
        acceptance_ref,
        plan,
        accepted,
        inputs,
        before,
        after,
        payloads,
        checkpoint,
        {p: inputs[p] for p in protected_map},
        operations,
        dict(before),
    )
    _recheck(result)
    return result


def _recheck(prepared: Prepared, transition=None):
    _check_loaded_producers()
    native_members = set(receipt_paths(prepared.root))
    expected_members = {p for p in prepared.checkpoint if p.startswith(RECEIPTS_DIR + "/")}
    require(native_members == expected_members, "Native receipt membership changed")
    require(
        {p for p in HISTORICAL_CONTEXT if os.path.lexists(prepared.root / p)}
        == set(HISTORICAL_CONTEXT) & set(prepared.checkpoint),
        "Native historical context changed",
    )
    current = inventory(prepared.root)
    expected = hashes(prepared.states)
    transition_paths = set()
    if transition is not None:
        transition_paths = {transition["source_record"]}
        if transition["before_source_record"]:
            transition_paths.add(transition["before_source_record"])
    require(
        set(current) - transition_paths == set(expected) - transition_paths,
        "Owner membership changed",
    )
    for path, frozen in prepared.states.items():
        if path not in transition_paths:
            frozen.verify()
    for path, frozen in prepared.inputs.items():
        if path in prepared.before:
            if path not in transition_paths and path in prepared.states:
                prepared.states[path].verify()
        else:
            frozen.verify()
    for frozen in prepared.checkpoint.values():
        frozen.verify()
    for frozen in prepared.protected.values():
        frozen.verify()


def _new_owner(root: Path, name: str, raw: bytes, recheck):
    path = root / name
    no_alias(path)
    require(not os.path.lexists(path), "New destination exists")
    parent = path.parent
    parent_stat = parent.stat()
    fd = os.open(parent, os.O_RDONLY | os.O_DIRECTORY | os.O_NOFOLLOW)
    try:
        require(
            (os.fstat(fd).st_dev, os.fstat(fd).st_ino) == (parent_stat.st_dev, parent_stat.st_ino),
            "New-owner parent changed",
        )
        with tempfile.TemporaryDirectory(prefix=".campaign-new-", dir=parent) as directory:
            staging = Path(directory) / "owner.yaml"
            # Bytes already rendered and schema-validated in prepare.
            with staging.open("xb") as handle:
                handle.write(raw)
                handle.flush()
                os.fsync(handle.fileno())
            staged = FrozenFile.capture(staging)
            recheck()
            staged.verify()
            # Unlike replace, link refuses a competing final entry atomically.
            os.link(staging, path.name, dst_dir_fd=fd, follow_symlinks=False)
            staging.unlink()
            result = FrozenFile.capture(path)
            require(
                result.identity == staged.identity and result.content == raw,
                "Exclusive owner installation differs",
            )
            require(
                (parent.stat().st_dev, parent.stat().st_ino)
                == (parent_stat.st_dev, parent_stat.st_ino),
                "New-owner parent changed",
            )
            return result
    finally:
        os.close(fd)


def _rename_exclusive(source_fd: int, source: str, target_fd: int, target: str) -> None:
    """Refuse an occupied recovery entry atomically on maintained platforms.

    A portable os.rename overwrites an intervening recovery file. Refuse the
    operation if the platform lacks its no-replace primitive; never fall back.
    """
    libc = ctypes.CDLL(None, use_errno=True)
    if sys.platform == "darwin":
        function, flags = getattr(libc, "renameatx_np", None), 0x00000004
    elif sys.platform.startswith("linux"):
        function, flags = getattr(libc, "renameat2", None), 1
    else:
        function, flags = None, 0
    if function is None:
        raise ValueError("No exclusive promotion-retirement primitive")
    function.argtypes = [
        ctypes.c_int,
        ctypes.c_char_p,
        ctypes.c_int,
        ctypes.c_char_p,
        ctypes.c_uint,
    ]
    function.restype = ctypes.c_int
    if function(source_fd, os.fsencode(source), target_fd, os.fsencode(target), flags) != 0:
        code = ctypes.get_errno()
        raise OSError(code, os.strerror(code), target)


def _retire(source: FrozenFile, recovery: Path, recheck):
    no_alias(recovery)
    require(
        recovery.is_dir() and not list(recovery.iterdir()),
        "Promotion recovery directory is not fresh",
    )
    source.verify()
    recheck()
    source_fd = os.open(source.path.parent, os.O_RDONLY | os.O_DIRECTORY | os.O_NOFOLLOW)
    recovery_fd = os.open(recovery, os.O_RDONLY | os.O_DIRECTORY | os.O_NOFOLLOW)
    try:
        require(
            (os.fstat(source_fd).st_dev, os.fstat(source_fd).st_ino) == source.parents[0][1],
            "Promotion source parent changed",
        )
        source.verify()
        # No bytes are destroyed. A raced entry is retained here and causes a
        # failed receipt; the operator never performs destructive auto-recovery.
        _rename_exclusive(source_fd, source.path.name, recovery_fd, "retired-owner.yaml")
        retired = FrozenFile.capture(recovery / "retired-owner.yaml")
        require(
            retired.identity == source.identity and retired.content == source.content,
            "Promotion retired a changed entry; retained for recovery",
        )
        require(not os.path.lexists(source.path), "Promotion source reappeared")
        return retired
    finally:
        os.close(source_fd)
        os.close(recovery_fd)


def apply(prepared: Prepared, receipt_dir: Path, *, enabled=False) -> dict:
    if not enabled:
        _recheck(prepared)
        return {
            "applied": False,
            "approval": APPROVAL,
            "plan_sha256": prepared.plan_ref["sha256"],
            "operations": len(prepared.operations),
            "before_inventory": hashes(prepared.before),
            "after_inventory": prepared.after_inventory,
        }
    root = prepared.root
    receipt_dir = receipt_dir.absolute()
    relative(str(receipt_dir.relative_to(root)))
    no_alias(receipt_dir)
    require(not os.path.lexists(receipt_dir), "Receipt directory already exists")
    require(
        not str(receipt_dir.relative_to(root)).startswith("data/"),
        "Receipt directory overlaps data",
    )
    _recheck(prepared)
    receipt_dir.mkdir(mode=0o700)
    directory_stat = receipt_dir.stat()
    log = receipt_dir / "application.json"
    archives: dict[Path, bytes] = {}
    rows = []
    for index, entry in enumerate(prepared.operations):
        before_path = entry["before_source_record"]
        backup = receipt_dir / f"owner-before-{index:04}.yaml" if before_path else None
        if backup:
            archives[backup] = prepared.before[before_path].content
        row = {
            **entry,
            "shape": {
                "edit": "campaign_owner_edit",
                "create": "new_record",
                "promote": "promotion",
            }[entry["kind"]],
            "destination_path": entry["source_record"],
            "source_path": before_path,
            "before_capture": (
                {"path": str(backup.relative_to(root)), "sha256": digest(archives[backup])}
                if backup
                else None
            ),
            "after_yaml_sha256": digest(prepared.payloads[entry["operation_id"]]),
        }
        rows.append(row)
        if entry["kind"] == "promote":
            (receipt_dir / f"promotion-{index:04}").mkdir(mode=0o700)
    for category, files in (("checkpoint", prepared.checkpoint), ("protected", prepared.protected)):
        (receipt_dir / category).mkdir()
        for name, frozen in files.items():
            path = receipt_dir / category / name
            path.parent.mkdir(parents=True, exist_ok=True)
            archives[path] = frozen.content
    require(
        not ({log, *archives} & {f.path for f in prepared.inputs.values()}),
        "Receipt/proof roles collide",
    )
    result = {
        "schema_version": 1,
        "operation": "apply_reviewed_campaign_owners",
        "state": "prepared",
        "approval": APPROVAL,
        "plan": prepared.plan_ref,
        "acceptance": prepared.acceptance_ref,
        "baseline_commit": prepared.plan["baseline_commit"],
        "before_inventory": hashes(prepared.before),
        "after_inventory": prepared.after_inventory,
        "records": rows,
        "checkpoint": {
            "root": str((receipt_dir / "checkpoint").relative_to(root)),
            "input_sha256": hashes(prepared.checkpoint),
        },
        "protected_snapshot": {
            "root": str((receipt_dir / "protected").relative_to(root)),
            "input_sha256": hashes(prepared.protected),
        },
        "completed_operations": [],
        "retired_sources": {},
        "recovery_required": False,
    }
    with reserve_receipt_outputs(log, backup_paths=tuple(archives)) as handles:
        receipt, *backups = handles
        completed_archives: dict[Path, FrozenFile] = {}

        def reserved():
            no_alias(receipt_dir)
            require(
                (receipt_dir.stat().st_dev, receipt_dir.stat().st_ino)
                == (directory_stat.st_dev, directory_stat.st_ino),
                "Receipt directory changed",
            )
            for path, handle in zip((log, *archives), handles, strict=True):
                check_reserved(handle, path)
            for frozen in completed_archives.values():
                frozen.verify()

        def recheck(transition=None):
            reserved()
            _recheck(prepared, transition)

        def progress():
            reserved()
            receipt.seek(0)
            receipt.truncate()
            receipt.write(encoded(result).decode())
            receipt.flush()
            reserved()

        try:
            recheck()
            for handle, raw in zip(backups, archives.values(), strict=True):
                handle.write(raw)
                handle.flush()
                os.fsync(handle.fileno())
            for path, raw in archives.items():
                frozen = FrozenFile.capture(path)
                require(frozen.content == raw, "Reserved archive bytes differ")
                completed_archives[path] = frozen
            progress()
            result["state"] = "applying"
            for index, entry in enumerate(prepared.operations):
                progress()
                recheck()
                source, destination = entry["before_source_record"], entry["source_record"]
                raw = prepared.payloads[entry["operation_id"]]
                if entry["kind"] == "edit":

                    def render(path: Path, raw: bytes = raw) -> None:
                        write_validated_ingredient(
                            record(raw),
                            path,
                            target_class="IngredientRecord",
                            schema_path=root
                            / "src/mediaingredientmech/schema/mediaingredientmech.yaml",
                        )

                    def during_edit(entry: dict = entry) -> None:
                        recheck(entry)

                    published = publish_validated(prepared.states[source], render, during_edit)
                else:
                    published = _new_owner(root, destination, raw, lambda: recheck())
                prepared.states[destination] = published
                if entry["kind"] == "promote":
                    retired = _retire(
                        prepared.states[source],
                        receipt_dir / f"promotion-{index:04}",
                        lambda: recheck(),
                    )
                    result["retired_sources"][source] = {
                        "path": str(retired.path.relative_to(root)),
                        "sha256": digest(retired.content),
                    }
                    completed_archives[retired.path] = retired
                    del prepared.states[source]
                result["completed_operations"].append(entry["operation_id"])
                recheck()
                progress()
            require(
                hashes(inventory(root)) == prepared.after_inventory,
                "Final complete inventory differs",
            )
            allowed = {e["source_record"] for e in prepared.operations} | {
                e["before_source_record"] for e in prepared.operations if e["before_source_record"]
            }
            require(
                set(git(root, "diff", "--name-only", "HEAD", "--").decode().splitlines())
                <= allowed,
                "Unrelated tracked file changed",
            )
            result["state"] = "complete"
            reserved()
            receipt.seek(0)
            receipt.truncate()
            finish_receipt(receipt, log, result, recheck)
            return result
        except BaseException as error:
            result.update(
                state="failed", recovery_required=True, error=f"{type(error).__name__}: {error}"
            )
            # Write only our held descriptor; never reopen or clean a competitor.
            try:
                receipt.seek(0)
                receipt.truncate()
                receipt.write(encoded(result).decode())
                receipt.flush()
            except OSError:
                pass
            raise


def verify_completed(root: Path, plan_path: Path, receipt_path: Path) -> dict:
    """Recompute exact source completion; historical checkpoint is approval-free.

    The live canonical may advance in a separate publisher. Its earlier native
    checkpoint is replayed from reserved immutable copies; the current owner
    inventory, intake artifacts, accepted payloads and proof paths stay exact.
    """
    root = root.absolute()
    no_alias(root)
    require(".." not in root.parts, "Noncanonical repository root")
    receipt_path = receipt_path.absolute()
    relative(str(receipt_path.relative_to(root)))
    relative(str(plan_path.absolute().relative_to(root)))
    log = FrozenFile.capture(receipt_path)
    saved = unique_json(log.content)
    keys = {
        "schema_version",
        "operation",
        "state",
        "approval",
        "plan",
        "acceptance",
        "baseline_commit",
        "before_inventory",
        "after_inventory",
        "records",
        "checkpoint",
        "protected_snapshot",
        "completed_operations",
        "retired_sources",
        "recovery_required",
    }
    closed(saved, keys, "completed source receipt")
    require(
        saved["schema_version"] == 1
        and saved["operation"] == "apply_reviewed_campaign_owners"
        and saved["state"] == "complete"
        and saved["approval"] == APPROVAL
        and saved["recovery_required"] is False,
        "Not a complete approval-free source receipt",
    )
    historical: dict[str, bytes] = {}
    captures: dict[str, FrozenFile] = {}
    protected_history: dict[str, bytes] = {}
    snapshot_memberships: dict[Path, set[str]] = {}
    row_keys = RECORD_KEYS | {
        "shape",
        "destination_path",
        "source_path",
        "before_capture",
        "after_yaml_sha256",
    }
    require(
        isinstance(saved["records"], list) and bool(saved["records"]),
        "Missing completed owner records",
    )
    for row in saved["records"]:
        closed(row, row_keys, "completed owner record")
        if row["before_source_record"] is not None:
            raw = _ref(root, row["before_capture"], captures)
            require(digest(raw) == row["before_yaml_sha256"], "False source backup")
            historical[row["before_source_record"]] = raw
    for category in ("checkpoint", "protected_snapshot"):
        snapshot = closed(saved[category], {"root", "input_sha256"}, category)
        directory = root / relative(snapshot["root"])
        expected_directory = receipt_path.absolute().parent / (
            "checkpoint" if category == "checkpoint" else "protected"
        )
        require(directory == expected_directory, "Snapshot uses a different proof role")
        no_alias(directory)
        expected = snapshot["input_sha256"]
        require(isinstance(expected, dict), "Invalid checkpoint inputs")
        actual = _snapshot_members(directory)
        require(actual == set(expected), "Historical snapshot membership changed")
        snapshot_memberships[directory] = set(expected)
        for path, expected_sha in expected.items():
            captured = FrozenFile.capture(directory / relative(path))
            require(digest(captured.content) == sha(expected_sha), "Historical snapshot changed")
            captures[str(captured.path.relative_to(root))] = captured
            if category == "protected_snapshot":
                protected_history[path] = captured.content
    loaded = _load(
        root,
        plan_path.absolute(),
        root / relative(saved["acceptance"]["path"]),
        historical,
        protected_history,
    )
    (
        plan_ref,
        acceptance_ref,
        plan,
        accepted,
        inputs,
        before,
        after,
        protected,
        payloads,
        operations,
    ) = loaded
    require(
        saved["plan"] == plan_ref
        and saved["acceptance"] == acceptance_ref
        and saved["baseline_commit"] == plan["baseline_commit"],
        "Receipt plan binding differs",
    )
    require(
        saved["before_inventory"] == before and saved["after_inventory"] == after,
        "Receipt inventories differ",
    )
    require(
        saved["completed_operations"] == [e["operation_id"] for e in operations],
        "Incomplete operation accounting",
    )
    current = inventory(root)
    require(hashes(current) == after, "Current after-owner inventory differs")
    before_bytes = {
        p: (historical[p] if p in historical else f.content)
        for p, f in current.items()
        if p in before
    }
    before_bytes.update({p: historical[p] for p in before if p not in current})
    require(
        {p: digest(b) for p, b in before_bytes.items()} == before,
        "Cannot reconstruct exact before inventory",
    )
    _validate_records(root, operations, payloads, before_bytes)
    proof = verify_mapping_chain(root / saved["checkpoint"]["root"])
    require(
        proof["input_hashes"] == saved["checkpoint"]["input_sha256"], "Native checkpoint differs"
    )
    require(
        all(protected.get(path) == value for path, value in proof["input_hashes"].items()),
        "Accepted protected inputs omit native checkpoint pins",
    )
    expected_retired = {}
    for index, (entry, row) in enumerate(zip(operations, saved["records"], strict=True)):
        expected = {
            **entry,
            "shape": {
                "edit": "campaign_owner_edit",
                "create": "new_record",
                "promote": "promotion",
            }[entry["kind"]],
            "destination_path": entry["source_record"],
            "source_path": entry["before_source_record"],
            "before_capture": (
                {
                    "path": str(
                        (receipt_path.parent / f"owner-before-{index:04}.yaml").relative_to(root)
                    ),
                    "sha256": entry["before_yaml_sha256"],
                }
                if entry["before_source_record"]
                else None
            ),
            "after_yaml_sha256": digest(payloads[entry["operation_id"]]),
        }
        require(row == expected, "Completed owner link differs")
        if entry["kind"] == "edit":
            chain = proof["owner_chains"].get(entry["before_source_record"], [])
            require(
                not chain or chain[-1]["after_sha256"] == entry["before_yaml_sha256"],
                "Selected owner preimage is disconnected from native history",
            )
        else:
            require(
                not proof["owner_chains"].get(entry["source_record"]),
                "New destination has prior native owner-chain links",
            )
        if entry["kind"] == "promote":
            source = entry["before_source_record"]
            require(
                not proof["owner_chains"].get(source),
                "Promotion source has prior native owner-chain links",
            )
            retired = receipt_path.parent / f"promotion-{index:04}/retired-owner.yaml"
            frozen = FrozenFile.capture(retired)
            require(
                frozen.content == historical[source] and not os.path.lexists(root / source),
                "Promotion relocation proof differs",
            )
            captures[str(retired.relative_to(root))] = frozen
            expected_retired[source] = {
                "path": str(retired.relative_to(root)),
                "sha256": digest(frozen.content),
            }
    require(saved["retired_sources"] == expected_retired, "Retired-source evidence differs")
    require(
        saved["protected_snapshot"]["input_sha256"] == protected, "Protected checkpoint differs"
    )
    for frozen in (*captures.values(), *inputs.values(), *current.values(), log):
        frozen.verify()
    # #1194: captured files alone cannot prove the continued absence of another
    # direct owner or archive input after the intervening native replay.
    for directory, expected_members in snapshot_memberships.items():
        require(
            _snapshot_members(directory) == expected_members,
            "Historical snapshot membership changed at completion",
        )
    require(hashes(inventory(root)) == after, "Owner membership or bytes changed at completion")
    _check_loaded_producers()
    return {
        **saved,
        "plan_sha256": plan_ref["sha256"],
        "receipt_sha256": digest(log.content),
        "immutable_input_sha256": {
            str(f.path.relative_to(root)): digest(f.content)
            for f in (*captures.values(), *inputs.values(), log)
        },
    }
