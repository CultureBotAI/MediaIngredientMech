"""Prepare and apply a reviewed campaign's administrative stable-ID adoption (#1303).

No allocation implies scientific support. Apply is a guarded, recoverable sequence,
not a filesystem-atomic batch. The original legacy endpoint is always read-only.
"""

from __future__ import annotations

import argparse
import copy
import hashlib
import io
import json
import os
import re
import subprocess
import sys
import types
import unicodedata
from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path
from typing import Any, cast

from mediaingredientmech.curate.adoption_filesystem import _new_owner, _retire
from mediaingredientmech.curate.apply_receipt import reserve_receipt_outputs
from mediaingredientmech.curate.curation_event import record_curation_event
from mediaingredientmech.curate.publication_guard import (
    FrozenFile,
    check_reserved,
    finish_receipt,
    no_alias,
    publish_validated,
)
from mediaingredientmech.curie import mim_curie_for_stem
from mediaingredientmech.mapping_scope import _load_yaml
from mediaingredientmech.stable_ids import (
    LIFECYCLE_PATH,
    REGISTRY_PATH,
    allocate_ids,
    dump_lifecycle,
    dump_registry,
    parse_registry,
    validate_history,
    validate_records,
)
from mediaingredientmech.validation.write_validated import (
    validate_ingredient,
    write_validated_ingredient,
)

CAPABILITY = "reviewed-campaign-stable-id-adoption-v1"
REPOSITORY = "CultureBotAI/MediaIngredientMech"
SCHEMA = "src/mediaingredientmech/schema/mediaingredientmech.yaml"
AGGREGATES = ("data/curated/mapped_ingredients.yaml", "data/curated/unmapped_ingredients.yaml")
MIGRATION = "reports/stable_ids_1265_20261108/migration.json"
DISPOSITIONS = {"CREATE_DISTINCT_CONCEPT", "BIND_EXISTING_CONCEPT_ONLY", "WITHHOLD_IDENTITY"}
CLAIM_ALGORITHM = "sha256-canonical-json-v1"
CLAIM_DESCRIPTION = (
    "Complete pre-ID adoption decision and current scientific/source context; no mapping approval."
)
_CAPTURE: Any = globals().get("_PRODUCER_CAPTURE")


def require(condition, message):
    if not condition:
        raise ValueError("Stable-ID adoption: " + message)


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def load_yaml(raw: bytes | str) -> Any:
    return _load_yaml(raw.decode("utf-8") if isinstance(raw, bytes) else raw)


def encoded(value):
    return (json.dumps(value, ensure_ascii=False, indent=2, allow_nan=False) + "\n").encode()


def digest(value):
    return sha(
        json.dumps(
            value, sort_keys=True, separators=(",", ":"), ensure_ascii=False, allow_nan=False
        ).encode()
    )


def unique(pairs):
    result = {}
    for key, value in pairs:
        require(key not in result, "duplicate JSON key: " + key)
        result[key] = value
    return result


def document(raw):
    return json.loads(raw, object_pairs_hook=unique)


def keys(value, expected):
    require(isinstance(value, dict) and set(value) == set(expected), "unexpected contract fields")


def relative(name):
    path = Path(name)
    require(
        isinstance(name, str)
        and not path.is_absolute()
        and ".." not in path.parts
        and name == path.as_posix()
        and name not in {"", "."},
        "noncanonical relative path",
    )
    return path


def git(root, *args):
    result = subprocess.run(
        ["git", "--no-optional-locks", *args], cwd=root, capture_output=True, timeout=60
    )
    require(result.returncode == 0, "Git command failed: " + " ".join(args))
    return result.stdout


def root_path(value, role):
    path = Path(value)
    require(".." not in path.parts, role + " root traversal refused (#1315)")
    path = path.absolute()
    no_alias(path)
    return path


def baseline_inventory(root, revision):
    """Hash actual immutable baseline blobs in one Git batch, not a JSON claim."""
    entries = {}
    for raw in git(
        root,
        "ls-tree",
        "-rz",
        "--full-tree",
        revision,
        "--",
        "data/ingredients/mapped",
        "data/ingredients/unmapped",
    ).split(b"\0"):
        if not raw:
            continue
        metadata, name = raw.split(b"\t", 1)
        mode, kind, oid = metadata.decode().split()
        name = name.decode()
        relative(name)
        require(
            mode in {"100644", "100755"}
            and kind == "blob"
            and Path(name).suffix == ".yaml"
            and len(Path(name).parts) == 4,
            "unexpected baseline owner entry",
        )
        entries[name] = oid
    process = subprocess.run(
        ["git", "--no-optional-locks", "cat-file", "--batch"],
        cwd=root,
        input=("\n".join(entries.values()) + "\n").encode(),
        capture_output=True,
        timeout=60,
    )
    require(process.returncode == 0 and entries, "baseline blob capture failed")
    raw, offset, result = process.stdout, 0, {}
    for name, oid in entries.items():
        end = raw.index(b"\n", offset)
        actual_oid, kind, size = raw[offset:end].decode().split()
        require(actual_oid == oid and kind == "blob", "baseline blob response differs")
        start, stop = end + 1, end + 1 + int(size)
        require(raw[stop : stop + 1] == b"\n", "truncated baseline blob")
        result[name] = sha(raw[start:stop])
        offset = stop + 1
    require(offset == len(raw), "extra baseline blob response")
    return result


def inventory(root, during=()):
    result = {}
    for category in ("mapped", "unmapped"):
        directory = root / "data/ingredients" / category
        no_alias(directory)
        require(directory.is_dir(), "missing owner directory")
        transients = []
        for path in sorted(directory.iterdir()):
            if (
                path.is_dir()
                and any((root / name).parent == directory for name in during)
                and path.name.startswith((".campaign-new-", ".kgm-publication-"))
            ):
                no_alias(path)
                transients.append(path)
                require(len(transients) == 1, "unexpected concurrent native staging directories")
                continue
            require(path.suffix == ".yaml" and path.is_file(), "unexpected owner inventory entry")
            result[path.relative_to(root).as_posix()] = FrozenFile.capture(path)
    require(result, "empty complete owner inventory")
    portable = [unicodedata.normalize("NFC", name).casefold() for name in result]
    require(len(set(portable)) == len(portable), "case/Unicode owner aliases")
    return result


def hashes(files):
    return {name: sha(value.content) for name, value in files.items()}


@dataclass
class Inputs:
    root: Path
    files: dict[str, FrozenFile] = field(default_factory=dict)

    def read(self, name, expected=None):
        relative(name)
        if name not in self.files:
            self.files[name] = FrozenFile.capture(self.root / name)
        frozen = self.files[name]
        if expected is not None:
            require(sha(frozen.content) == expected, "input hash differs: " + name)
        return frozen.content

    @property
    def bytes(self):
        return {name: frozen.content for name, frozen in self.files.items()}

    def ref(self, value):
        keys(value, {"path", "sha256"})
        return document(self.read(value["path"], value["sha256"]))

    def verify(self, exclude=()):
        for name, frozen in self.files.items():
            if name not in exclude:
                frozen.verify()


class Claw:
    """Execute only captured native transaction/lease dependencies, without providers."""

    PATHS = {
        "kg_microbe_fleet": "src/kg_microbe_fleet/__init__.py",
        "transaction": "src/kg_microbe_write/transaction.py",
        "locks": "plugins/lock_manager.py",
    }

    def __init__(self, root):
        self.root = root_path(root, "Claw")
        self.head = git(self.root, "rev-parse", "HEAD").decode().strip()
        self.files = {
            path: FrozenFile.capture(self.root / path)
            for path in (*self.PATHS.values(), "uv.lock", "pyproject.toml")
        }
        self.modules = {}
        for name in self.PATHS:
            self.load(name)
        self.verify()

    def load(self, name):
        if name in self.modules:
            return self.modules[name]
        import builtins

        module = types.ModuleType("_adoption_claw_" + str(id(self)) + "_" + name)
        module.__file__ = str(self.root / self.PATHS[name])
        original_import = builtins.__import__

        def imported(name, globals=None, locals=None, fromlist=(), level=0):
            if name == "kg_microbe_fleet" and level == 0:
                return self.load(name)
            require(not name.startswith("kg_microbe"), "uncaptured Claw dependency")
            return original_import(name, globals, locals, fromlist, level)

        module.__dict__["__builtins__"] = {**vars(builtins), "__import__": imported}
        self.modules[name] = module
        sys.modules[module.__name__] = module
        exec(
            compile(self.files[self.PATHS[name]].content, module.__file__, "exec"), module.__dict__
        )
        return module

    def verify(self):
        require(
            git(self.root, "rev-parse", "HEAD").decode().strip() == self.head, "Claw HEAD changed"
        )
        for frozen in self.files.values():
            frozen.verify()

    def receipt(self):
        self.verify()
        return {"root": str(self.root), "head": self.head, "files": hashes(self.files)}


@dataclass
class Loaded:
    inputs: Inputs
    legacy: Inputs
    claw: Claw
    request: dict
    request_path: str
    owners: dict
    legacy_owners: dict
    existing: dict
    operations: dict
    decisions: dict
    context: dict
    payloads: list
    head: str
    index: bytes
    initial_dirty: set
    historical_after: dict | None = None

    def check(self, states=None, during=()):
        require(_CAPTURE is not None, "captured producer unavailable")
        _CAPTURE.verify()
        self.claw.verify()
        require(
            git(self.inputs.root, "rev-parse", "HEAD").decode().strip() == self.head,
            "accepted HEAD changed",
        )
        require(
            git(self.inputs.root, "ls-files", "--stage", "-z") == self.index, "Git index changed"
        )
        require(
            git(self.legacy.root, "rev-parse", "HEAD").decode().strip()
            == self.request["legacy"]["head"],
            "legacy HEAD changed",
        )
        self.legacy.verify()
        require(
            hashes(inventory(self.legacy.root)) == hashes(self.legacy_owners),
            "legacy owner membership changed",
        )
        mutable = set(self.owners) | set(AGGREGATES) | {str(REGISTRY_PATH), str(LIFECYCLE_PATH)}
        if self.historical_after is not None:
            self.inputs.verify(mutable | set(self.historical_after))
            require(
                hashes(inventory(self.inputs.root)) == self.historical_after,
                "current adopted endpoint differs",
            )
        elif states is None:
            self.inputs.verify()
            require(
                hashes(inventory(self.inputs.root)) == hashes(self.owners),
                "target owner inventory changed",
            )
        else:
            mutable |= set(states)
            self.inputs.verify(mutable)
            for name, frozen in states.items():
                if name not in during:
                    frozen.verify()
            expected = {name for name in states if name.startswith("data/ingredients/")}
            current = set(inventory(self.inputs.root, during=during))
            require(
                current - set(during) == expected - set(during),
                "unexpected intermediate owner membership",
            )
        dirty = set(
            git(self.inputs.root, "diff", "--name-only", "--no-renames", "-z", self.head)
            .decode()
            .split("\0")
        ) - {""}
        require(dirty <= self.initial_dirty | mutable, "unrelated tracked mutation")


def _load(root, request_path, *, before=None, historical_after=None):
    root = root_path(root, "target")
    require(_CAPTURE is not None, "captured producer unavailable")
    target = Inputs(root, dict(before or {}))
    request_path = (
        str(Path(request_path).relative_to(root))
        if Path(request_path).is_absolute()
        else str(request_path)
    )
    request = document(target.read(request_path))
    keys(
        request,
        {
            "schema_version",
            "capability",
            "baseline_commit",
            "history_base",
            "timestamp",
            "claw_root",
            "legacy",
            "target_inventory",
            "target_inputs",
            "existing",
            "decisions",
            "context",
            "payloads",
            "review_inputs",
            "origin_accounting",
            "origin_proof",
            "eligibility_intake",
        },
    )
    require(
        request["schema_version"] == 1 and request["capability"] == CAPABILITY,
        "unsupported contract",
    )
    root_path(request["claw_root"], "Claw")
    stamp = datetime.fromisoformat(request["timestamp"])
    offset = stamp.utcoffset()
    require(offset is not None and offset.total_seconds() == 0, "explicit UTC timestamp required")
    head = git(root, "rev-parse", "HEAD").decode().strip()
    if before is None:
        require(head == request["baseline_commit"], "target HEAD differs")
    else:
        git(root, "merge-base", "--is-ancestor", request["baseline_commit"], "HEAD")
    index = git(root, "ls-files", "--stage", "-z")
    _CAPTURE.bind(target)
    owners = (
        inventory(root)
        if before is None
        else {
            name: frozen for name, frozen in before.items() if name.startswith("data/ingredients/")
        }
    )
    require(hashes(owners) == request["target_inventory"], "complete target inventory differs")
    for name, expected in request["target_inputs"].items():
        target.read(name, expected)
    require(
        {*AGGREGATES, str(REGISTRY_PATH), str(LIFECYCLE_PATH), MIGRATION}
        <= set(request["target_inputs"]),
        "missing aggregate/ledger/migration inputs",
    )
    for name, frozen in owners.items():
        target.read(name, sha(frozen.content))
    registry = parse_registry(target.read(str(REGISTRY_PATH)), target.read(str(LIFECYCLE_PATH)))
    current = {name: load_yaml(frozen.content) for name, frozen in owners.items()}
    validate_records(registry, current)
    validate_history(root, request["history_base"])
    legacy_spec = request["legacy"]
    keys(legacy_spec, {"root", "head", "plan", "application", "cases"})
    legacy = Inputs(root_path(legacy_spec["root"], "legacy"))
    require(
        legacy.root != root
        and not root.is_relative_to(legacy.root)
        and not legacy.root.is_relative_to(root),
        "legacy/target roots overlap",
    )
    require(
        git(legacy.root, "rev-parse", "HEAD").decode().strip() == legacy_spec["head"],
        "legacy HEAD differs",
    )
    plan, receipt, cases = [
        legacy.ref(legacy_spec[key]) for key in ("plan", "application", "cases")
    ]
    require(
        receipt["state"] == "complete"
        and receipt["recovery_required"] is False
        and receipt["plan"] == legacy_spec["plan"],
        "legacy application not complete for this plan",
    )
    git(legacy.root, "merge-base", "--is-ancestor", plan["baseline_commit"], "HEAD")
    require(
        receipt["baseline_commit"] == plan["baseline_commit"]
        and baseline_inventory(legacy.root, plan["baseline_commit"]) == receipt["before_inventory"],
        "legacy before inventory differs from actual Git baseline",
    )
    acceptance = legacy.ref(receipt["acceptance"])
    require(
        acceptance["schema_version"] == 1
        and acceptance["scope"] == "source_application_only"
        and acceptance["plan_sha256"] == legacy_spec["plan"]["sha256"]
        and acceptance["baseline_commit"] == plan["baseline_commit"]
        and acceptance["intake_heads"] == plan["intake_heads"]
        and acceptance["binding_sha256"]
        == {b["binding_id"]: b["sha256"] for b in plan["bindings"]},
        "legacy source-only acceptance differs",
    )
    denominator = [entry for entry in plan["bindings"] if entry["binding_id"] == "full-case-ledger"]
    require(
        len(denominator) == 1
        and denominator[0]["role"] == "case_ledger"
        and {key: denominator[0][key] for key in ("path", "sha256")} == legacy_spec["cases"],
        "full original case ledger binding differs",
    )
    legacy_owners = inventory(legacy.root)
    require(
        hashes(legacy_owners) == receipt["after_inventory"], "legacy application afterimages differ"
    )
    for name, frozen in legacy_owners.items():
        legacy.read(name, sha(frozen.content))
    operations = {row["operation_id"]: row for row in plan["records"]}
    require(
        acceptance["accepted_operations"]
        == {key: row["after_capture"]["sha256"] for key, row in operations.items()},
        "legacy accepted operation coverage differs",
    )
    require(
        len(operations) == len(plan["records"])
        and set(receipt["completed_operations"]) == set(operations),
        "incomplete legacy operation coverage",
    )
    require(
        receipt["before_inventory"] == legacy.ref(plan["before_inventory"])["owners"]
        and receipt["after_inventory"] == legacy.ref(plan["after_inventory"])["owners"],
        "legacy plan inventory differs",
    )
    require(
        len(receipt["records"]) == len(operations)
        and {r["operation_id"] for r in receipt["records"]} == set(operations),
        "incomplete application record coverage",
    )
    for row in receipt["records"]:
        operation = operations[row["operation_id"]]
        require(
            all(row[key] == value for key, value in operation.items()),
            "application operation differs from original plan",
        )
        if row["before_capture"]:
            require(
                row["before_source_record"] in receipt["before_inventory"]
                and row["before_capture"]["sha256"]
                == receipt["before_inventory"][row["before_source_record"]],
                "application beforeimage lineage differs",
            )
            legacy.read(row["before_capture"]["path"], row["before_capture"]["sha256"])
    case_index = {row["case_id"]: row for row in cases}
    require(len(case_index) == len(cases), "duplicate case IDs")
    for operation in operations.values():
        require(operation["source_record"] in legacy_owners, "operation lacks current owner")
        require(
            sha(legacy_owners[operation["source_record"]].content)
            == operation["after_capture"]["sha256"],
            "legacy owner differs from operation",
        )
        for origin in operation["origins"]:
            require(
                all(
                    key in case_index and digest(case_index[key]) == value
                    for key, value in origin["case_hashes"].items()
                ),
                "origin case attribution differs",
            )
    # Preserve the original complete origin universe, including origins that
    # were deferred or retired before source application. These objects retain
    # their original authority; this is not a replay or a new science approval.
    origin_cores, universe = {}, {}
    for binding in plan["bindings"]:
        if re.fullmatch(r"w[0-9]{2}-decisions", binding["binding_id"]):
            origin_cores[binding["binding_id"]] = legacy.ref(
                {key: binding[key] for key in ("path", "sha256")}
            )
        if re.fullmatch(r"w[0-9]{2}(?:-gyps)?-proposals", binding["binding_id"]):
            core = legacy.ref({key: binding[key] for key in ("path", "sha256")})
            origin_cores[binding["binding_id"]] = core
            for proposal in core["proposals"]:
                key = binding["binding_id"][:3] + "::" + proposal["proposal_id"]
                require(key not in universe, "duplicate original origin")
                require(
                    set(proposal["case_ids"]) <= set(case_index),
                    "original proposal case absent from full ledger",
                )
                universe[key] = proposal
    require(universe, "original proposal denominator unavailable")
    require(
        all(
            slot.replace("worker-", "w") + suffix in origin_cores
            for slot in plan["intake_heads"]
            for suffix in ("-proposals", "-decisions")
        ),
        "missing original worker proposal/decision cores",
    )
    origin_accounting = target.ref(request["origin_accounting"])
    origin_proof = target.ref(request["origin_proof"])
    crossed = {row["origin_id"]: row for row in origin_accounting}
    require(
        len(crossed) == len(origin_accounting) and set(crossed) == set(universe),
        "full original origin crosswalk differs",
    )
    applied = {}
    for key, operation in operations.items():
        for origin in operation["origins"]:
            origin_id = origin["worker_slot"].replace("worker-", "w") + "::" + origin["proposal_id"]
            require(origin_id not in applied, "origin applied more than once")
            applied[origin_id] = (key, operation["after_capture"]["sha256"])
    for key, row in crossed.items():
        require(
            row["status"] in {"apply", "deferred", "retired"}, "unknown original origin disposition"
        )
        if key in applied:
            require(
                row["status"] == "apply"
                and (row["operation_id"], row["payload_sha256"]) == applied[key],
                "applied origin lineage differs",
            )
        else:
            require(
                row["status"] in {"deferred", "retired"}, "nonselected origin cannot become applied"
            )
        require(bool(row["evidence_refs"]), "origin disposition lacks original evidence")
        for reference in row["evidence_refs"]:
            legacy.read(reference["path"], reference["sha256"])
    require(set(applied) <= set(crossed), "selected origin absent from original universe")
    proof = origin_proof["native_prepare_proof"]
    require(
        origin_proof["structurally_complete"] is True
        and origin_proof["scientific_approval"] is False
        and origin_proof["application_authorized"] is False
        and origin_proof["origin_count"] == len(universe)
        and origin_proof["applied_origin_count"] == len(applied)
        and origin_proof["native_operation_count"] == len(operations),
        "original crosswalk proof scope differs",
    )
    require(
        proof["plan_sha256"] == legacy_spec["plan"]["sha256"]
        and proof["acceptance_sha256"] == receipt["acceptance"]["sha256"]
        and proof["before_owner_sha256"] == receipt["before_inventory"]
        and proof["after_owner_sha256"] == receipt["after_inventory"],
        "original crosswalk proof endpoint differs",
    )
    for pins in (proof["native_input_sha256"], origin_proof["evidence_sha256"]):
        for name, expected in pins.items():
            legacy.read(name, expected)
    migration = document(target.read(MIGRATION))
    minted = {row["mim_id"]: row for row in migration["records"]}
    existing = {row["mim_id"]: row for row in request["existing"]}
    require(
        len(existing) == len(request["existing"])
        and set(existing) == set(registry.states) == set(minted),
        "complete existing ID lineage required",
    )
    for identifier, row in existing.items():
        keys(row, {"mim_id", "stable_path", "legacy_path"})
        original = minted[identifier]["path"]
        require(
            row["stable_path"] == original
            and current[original]["mim_id"] == identifier
            and sha(owners[original].content) == minted[identifier]["after_sha256"],
            "existing stable scientific baseline requires reconciliation",
        )
        moves = [op for op in operations.values() if op["before_source_record"] == original]
        require(
            len(moves) <= 1
            and row["legacy_path"] == (moves[0]["source_record"] if moves else original),
            "existing owner path lineage differs",
        )
        require(row["legacy_path"] in legacy_owners, "missing retained legacy owner")
    creates = {key for key, row in operations.items() if row["kind"] == "create"}
    intake = target.ref(request["eligibility_intake"])
    prior_context = {row["candidate_key"]: row for row in intake["candidates"]}
    require(
        len(prior_context) == len(intake["candidates"]) and set(prior_context) == creates,
        "complete original eligibility intake required (#1317)",
    )
    for key, candidate in prior_context.items():
        owner = operations[key]["source_record"]
        require(
            candidate["owner_path"] == owner
            and candidate["owner_sha256"] == sha(legacy_owners[owner].content),
            "eligibility intake owner binding differs (#1317)",
        )
        require(
            isinstance(candidate["known_conditions_and_holds"], list),
            "literal original hold evidence required (#1317)",
        )
    decisions = {row["operation_id"]: row for row in request["decisions"]}
    require(
        len(decisions) == len(request["decisions"]) and set(decisions) == creates,
        "every create requires exactly one explicit decision",
    )
    for row in decisions.values():
        keys(
            row,
            {
                "operation_id",
                "disposition",
                "concept_key",
                "owner_operation",
                "existing_mim_id",
                "identity_holds",
                "other_holds",
                "primary",
                "skeptic",
            },
        )
        require(
            row["disposition"] is None or row["disposition"] in DISPOSITIONS,
            "unknown concept disposition",
        )
        require(
            all(
                row[name] is None
                or (
                    isinstance(row[name], list)
                    and all(isinstance(value, str) and value for value in row[name])
                )
                for name in ("identity_holds", "other_holds")
            ),
            "residual hold classification must be null or explicit statements (#1317)",
        )
        if row["disposition"] not in {None, "WITHHOLD_IDENTITY"}:
            require(
                row["identity_holds"] == [],
                "unresolved identity hold or unassessed residual identity (#1317)",
            )
        if row["disposition"] == "CREATE_DISTINCT_CONCEPT" or (
            row["disposition"] is None and row["concept_key"] is not None
        ):
            require(
                isinstance(row["concept_key"], str)
                and row["concept_key"]
                and row["owner_operation"] in creates
                and row["existing_mim_id"] is None,
                "invalid new concept grouping",
            )
        elif row["disposition"] == "BIND_EXISTING_CONCEPT_ONLY":
            require(
                row["existing_mim_id"] in existing
                and row["concept_key"] is None
                and row["owner_operation"] is None,
                "invalid existing-concept reference",
            )
        else:
            require(
                row["concept_key"] is None
                and row["owner_operation"] is None
                and row["existing_mim_id"] is None,
                "withheld proposal cannot select an owner",
            )
    context = {
        "legacy_plan": plan,
        "legacy_application": legacy_spec["application"],
        "legacy_inventory": hashes(legacy_owners),
        "cases": cases,
        "origin_cores": origin_cores,
        "original_origin_accounting": origin_accounting,
        "original_origin_proof": origin_proof,
        "eligibility_intake": request["eligibility_intake"],
        "policy_sha256": sha(target.read("MAPPING_SEMANTICS.md")),
        "target_inventory": hashes(owners),
        "registry_sha256": sha(target.read(str(REGISTRY_PATH))),
        "lifecycle_sha256": sha(target.read(str(LIFECYCLE_PATH))),
        "existing": request["existing"],
    }
    payloads = []
    for key in sorted(decisions):
        row = decisions[key]
        group = [
            name
            for name, item in decisions.items()
            if row["concept_key"] is not None and item["concept_key"] == row["concept_key"]
        ]
        if group:
            require(
                all(
                    decisions[name]["disposition"] in {None, "CREATE_DISTINCT_CONCEPT"}
                    and decisions[name]["owner_operation"] == row["owner_operation"]
                    for name in group
                )
                and row["owner_operation"] in group,
                "inconsistent concept group",
            )
        payloads.append(
            {
                "operation_id": key,
                "context_sha256": digest(context),
                "proposal_scope": {"operation_id": key},
                "original_eligibility_context": prior_context[key],
                "owner": load_yaml(legacy_owners[operations[key]["source_record"]].content),
                "owner_sha256": sha(legacy_owners[operations[key]["source_record"]].content),
                "origins": operations[key]["origins"],
            }
        )
    dirty = set(
        git(root, "diff", "--name-only", "--no-renames", "-z", head).decode().split("\0")
    ) - {""}
    for path in dirty:
        target.read(path)
    loaded = Loaded(
        target,
        legacy,
        Claw(request["claw_root"]),
        request,
        request_path,
        owners,
        legacy_owners,
        existing,
        operations,
        decisions,
        context,
        payloads,
        head,
        index,
        dirty,
        historical_after,
    )
    loaded.check()
    return loaded


def inspect(root, request_path):
    """Return authentic pre-ID targets for authors; never synthesize review pairs."""
    loaded = _load(root, request_path)
    context_path, payload_path = (
        loaded.request["context"]["path"],
        loaded.request["payloads"]["path"],
    )
    targets = [
        {
            "target_id": p["operation_id"],
            "label": p["owner"]["preferred_term"],
            "kind": "snapshot_row",
            "path": payload_path,
            "selector": p["operation_id"],
            "semantic_digest": {
                "algorithm": CLAIM_ALGORITHM,
                "sha256": digest(p),
                "description": CLAIM_DESCRIPTION,
            },
            "owner_paths": [
                {"repository": REPOSITORY, "path": payload_path, "role": "proposed pre-ID concept"}
            ],
        }
        for p in loaded.payloads
    ]
    return {
        "approval": "NONE",
        "context_path": context_path,
        "context": loaded.context,
        "payloads_path": payload_path,
        "payloads": loaded.payloads,
        "targets": targets,
    }


def _reviews(loaded, references, payload, *, scientific=True):
    inputs = loaded.inputs
    native = _CAPTURE.script("scripts/record_review.py")
    required = {
        loaded.request[key]["path"]: loaded.request[key]["sha256"]
        for key in ("context", "payloads", "eligibility_intake")
    }
    required["MAPPING_SEMANTICS.md"] = sha(inputs.read("MAPPING_SEMANTICS.md"))
    results = []
    for reference in references:
        keys(reference, {"path", "target_id", "assessment_id"})
        path = reference["path"]
        md = str(Path(path).with_name("review.md"))
        require(
            path in loaded.request["review_inputs"] and md in loaded.request["review_inputs"],
            "native review pair must be pinned",
        )
        report = native.parse_review_bundle(
            path, inputs.read(path), inputs.read(md), inputs.root / "schema/record_review.yaml"
        )
        require(
            native.source_provenance(inputs.root, report)["status"]
            not in {"invalid", "unverified"},
            "invalid native provenance",
        )
        require(
            report["repository"] == REPOSITORY
            and report["completion"] == "completed"
            and report["scientific_review"] is scientific,
            "completed native review required",
        )
        source = {x["path"]: x["sha256"] for x in report["source"]["inputs"]}
        for name, expected in source.items():
            inputs.read(name, expected)
        require(
            all(source.get(name) == expected for name, expected in required.items()),
            "review omits exact context/payload inputs",
        )
        target: dict[str, Any] = next(
            (x for x in report["targets"] if x["target_id"] == reference["target_id"]), {}
        )
        assessment: dict[str, Any] = next(
            (x for x in report["assessments"] if x["assessment_id"] == reference["assessment_id"]),
            {},
        )
        require(
            target.get("path") == loaded.request["payloads"]["path"]
            and target.get("kind") == "snapshot_row"
            and target.get("selector") == payload["operation_id"]
            and target.get("semantic_digest")
            == {
                "algorithm": CLAIM_ALGORITHM,
                "sha256": digest(payload),
                "description": CLAIM_DESCRIPTION,
            },
            "review target differs from complete pre-ID payload",
        )
        require(
            target.get("owner_paths")
            == [
                {
                    "repository": REPOSITORY,
                    "path": loaded.request["payloads"]["path"],
                    "role": "proposed pre-ID concept",
                }
            ],
            "review owner target differs",
        )
        require(
            reference["target_id"] in report["scope"]["reviewed_target_ids"],
            "target outside completed native review scope",
        )
        require(
            assessment.get("target_ids") == [reference["target_id"]]
            and assessment.get("area") == "identity",
            "explicit single-target identity assessment required",
        )
        dimensions = {x["name"]: x["value"] for x in assessment.get("dimensions", [])}
        require(
            dimensions.get("concept_disposition")
            == loaded.decisions[payload["operation_id"]]["disposition"]
            and dimensions.get("concept_scope") == "complete_source_and_duplicate_boundary",
            "explicit current concept decision required",
        )
        decision = loaded.decisions[payload["operation_id"]]
        for name in ("identity_holds", "other_holds"):
            require(
                dimensions.get("residual_" + name)
                == json.dumps(decision[name], ensure_ascii=False, separators=(",", ":")),
                "both native reviews must state the explicit residual hold classification (#1317)",
            )
        if decision["disposition"] == "CREATE_DISTINCT_CONCEPT":
            require(
                dimensions.get("concept_key") == decision["concept_key"]
                and dimensions.get("concept_owner_operation") == decision["owner_operation"],
                "native review must explicitly select the exact concept group and owner",
            )
        elif decision["disposition"] == "BIND_EXISTING_CONCEPT_ONLY":
            require(
                dimensions.get("concept_existing_mim_id") == decision["existing_mim_id"],
                "native review must explicitly select the existing concept",
            )
        if decision["disposition"] != "WITHHOLD_IDENTITY":
            require(
                assessment["outcome"] == "supported"
                and report["verdict"] in {"pass", "pass_with_limitations", "needs_curation"},
                "unsupported concept decision",
            )
            require(
                all(
                    x["status"] == "passed"
                    for x in report["checks"]
                    if x["required"] and reference["target_id"] in x["target_ids"]
                ),
                "required native check did not pass",
            )
            require(
                not any(
                    x["status"] in {"open", "deferred"}
                    and reference["target_id"] in x["target_ids"]
                    for x in report["findings"]
                ),
                "unresolved concept finding",
            )
            evidence = {x["evidence_id"]: x for x in report["evidence"]}
            require(
                any(
                    evidence[key]["kind"] in {"primary_source", "database", "authority"}
                    and evidence[key]["support"] == "supports"
                    and evidence[key]["reference"] in source
                    and evidence[key].get("snapshot_sha256") == source[evidence[key]["reference"]]
                    for key in assessment["evidence_ids"]
                ),
                "captured primary concept evidence required",
            )
        results.append(report)
    require(
        len(results) == 2
        and references[0]["path"] != references[1]["path"]
        and results[0]["reviewer"]["identity"] != results[1]["reviewer"]["identity"]
        and results[1]["reviewer"].get("independence") == "independent"
        and results[1]["reviewer"].get("independence_basis"),
        "separate skeptical reviewer required",
    )


def _admitted(loaded):
    require(
        all(row["disposition"] in DISPOSITIONS for row in loaded.decisions.values()),
        "unassessed concept decisions cannot prepare",
    )
    require(
        loaded.inputs.ref(loaded.request["context"]) == loaded.context
        and loaded.inputs.ref(loaded.request["payloads"]) == loaded.payloads,
        "inspection context/payloads are stale",
    )
    for name, expected in loaded.request["review_inputs"].items():
        loaded.inputs.read(name, expected)
    for payload in loaded.payloads:
        row = loaded.decisions[payload["operation_id"]]
        _reviews(loaded, [row["primary"], row["skeptic"]], payload)


def _records(loaded):
    """Administrative-only transformation; current scientific objects win."""
    records, moves = {}, {}
    original_receipt = document(loaded.inputs.read(MIGRATION))
    original = {row["mim_id"]: row for row in original_receipt["records"]}
    for identifier, row in loaded.existing.items():
        stable_path, legacy_path = row["stable_path"], row["legacy_path"]
        stable = load_yaml(loaded.owners[stable_path].content)
        scientific = load_yaml(loaded.legacy_owners[legacy_path].content)
        baseline = load_yaml(
            git(
                loaded.inputs.root,
                "show",
                original_receipt["source_commit"] + ":" + original[identifier]["path"],
            )
        )
        require(
            sha(
                git(
                    loaded.inputs.root,
                    "show",
                    original_receipt["source_commit"] + ":" + original[identifier]["path"],
                )
            )
            == original[identifier]["before_sha256"],
            "original mint beforeimage differs",
        )
        history = baseline.get("curation_history", [])
        require(
            stable.get("curation_history", [])[: len(history)] == history
            and scientific.get("curation_history", [])[: len(history)] == history,
            "historical scientific events require reconciliation",
        )
        administrative = stable.get("curation_history", [])[len(history) :]
        require(
            all(
                event.get("action") == "ASSIGNED_MIM_ID" and identifier in event.get("changes", "")
                for event in administrative
            ),
            "unexpected stable administrative history",
        )
        result = copy.deepcopy(scientific)
        result["mim_id"] = identifier
        result["legacy_identifiers"] = list(
            dict.fromkeys(
                [
                    *stable.get("legacy_identifiers", []),
                    *scientific.get("legacy_identifiers", []),
                    scientific["identifier"],
                    mim_curie_for_stem(Path(legacy_path).stem),
                ]
            )
        )
        result["curation_history"] = [
            *scientific.get("curation_history", []),
            *copy.deepcopy(administrative),
        ]
        if result != stable or stable_path != legacy_path:
            record_curation_event(
                result,
                curator="stable_id_adoption",
                action="ADOPTED_CAMPAIGN_MIM_ID",
                timestamp=loaded.request["timestamp"],
                llm_assisted=True,
                changes=f"#1303: retained {identifier}; adopted exact current legacy owner and preserved original mint/source history; no scientific approval transferred.",
            )
        records[legacy_path] = result
        if stable_path != legacy_path:
            require(legacy_path not in loaded.owners, "move destination already exists")
            moves[stable_path] = legacy_path
    selected = {
        row["owner_operation"]
        for row in loaded.decisions.values()
        if row["disposition"] == "CREATE_DISTINCT_CONCEPT"
    }
    for operation_id in sorted(selected):
        path = loaded.operations[operation_id]["source_record"]
        require(path not in records and path not in loaded.owners, "new concept path collides")
        value = copy.deepcopy(load_yaml(loaded.legacy_owners[path].content))
        require("mim_id" not in value, "legacy new owner already has an ID")
        records[path] = value
    registry = parse_registry(
        loaded.inputs.read(str(REGISTRY_PATH)), loaded.inputs.read(str(LIFECYCLE_PATH))
    )
    plan = allocate_ids(registry, records, minted_on=loaded.request["timestamp"][:10])
    for path, record in records.items():
        if "mim_id" not in record:
            record["mim_id"] = plan.assignments[path]
            record["legacy_identifiers"] = list(
                dict.fromkeys(
                    [
                        *record.get("legacy_identifiers", []),
                        mim_curie_for_stem(Path(path).stem),
                        record["identifier"],
                    ]
                )
            )
            record_curation_event(
                record,
                curator="stable_id_adoption",
                action="ASSIGNED_MIM_ID",
                timestamp=loaded.request["timestamp"],
                llm_assisted=True,
                changes=f"#1303: assigned {record['mim_id']} to the explicitly reviewed distinct concept; mapping and role holds unchanged.",
            )
    portable = [unicodedata.normalize("NFC", name).casefold() for name in records]
    require(len(set(portable)) == len(portable), "destination case/Unicode aliases")
    validate_records(plan.registry, records)
    return records, moves, plan


def _stage_path(root, path):
    require(".." not in Path(path).parts, "stage/receipt traversal refused (#1315)")
    path = Path(path).absolute()
    no_alias(path)
    require(
        path.is_relative_to(root / ".temp") and path != root / ".temp",
        "stage must be a fresh durable child of this root's .temp",
    )
    require(not os.path.lexists(path), "stage/receipt already exists")
    return path


def serialized(record, schema, target_class=None):
    """Use the unchanged native closed-schema writer with an in-memory target."""
    stream = io.StringIO()

    class MemoryTarget:
        @property
        def parent(self):
            return self

        def mkdir(self, **kwargs):
            pass

        def open(self, mode, encoding):
            require(mode == "w" and encoding == "utf-8", "unexpected native serialization mode")

            class HeldStream:
                def __enter__(self):
                    return stream

                def __exit__(self, *_):
                    return False

            return HeldStream()

    write_validated_ingredient(
        record, cast(Path, MemoryTarget()), schema_path=schema, target_class=target_class
    )
    raw = stream.getvalue().encode()
    require(load_yaml(raw) == record, "native serializer changed record")
    return raw


class PreparationTree:
    """Exclusive private staging; directory creation is descriptor-relative.

    Final file installs use the same native guarded new-file primitive as apply.
    This reserves no managed output and conveys no publication authorization.
    """

    def __init__(self, root, stage):
        self.root, self.stage = root, stage
        self.directories = {p: (p.stat().st_dev, p.stat().st_ino) for p in (root, *root.parents)}
        self.files = {}
        self.ensure(stage, exclusive=True)

    def check(self):
        for path, identity in self.directories.items():
            no_alias(path)
            require(
                (path.stat().st_dev, path.stat().st_ino) == identity,
                "preparation directory changed",
            )
        for frozen in self.files.values():
            frozen.verify()

    def ensure(self, path, exclusive=False):
        path = Path(path)
        require(
            ".." not in path.parts and path.is_relative_to(self.root),
            "preparation directory escaped root",
        )
        if path in self.directories:
            require(not exclusive, "preparation directory already exists")
            self.check()
            return
        self.ensure(path.parent)
        fd = os.open(path.parent, os.O_RDONLY | os.O_DIRECTORY | os.O_NOFOLLOW)
        try:
            require(
                (os.fstat(fd).st_dev, os.fstat(fd).st_ino) == self.directories[path.parent],
                "preparation parent changed while opening",
            )
            try:
                os.mkdir(path.name, mode=0o700, dir_fd=fd)
            except FileExistsError:
                require(
                    not exclusive and path == self.root / ".temp",
                    "unexpected occupied preparation directory",
                )
            child = os.open(path.name, os.O_RDONLY | os.O_DIRECTORY | os.O_NOFOLLOW, dir_fd=fd)
            try:
                self.directories[path] = (os.fstat(child).st_dev, os.fstat(child).st_ino)
            finally:
                os.close(child)
            self.check()
        finally:
            os.close(fd)

    def put(self, name, raw):
        path = self.stage / relative(name)
        self.ensure(path.parent)
        self.check()
        frozen = _new_owner(self.stage, name, raw, self.check)
        self.files[name] = frozen
        self.check()
        return frozen


def _dry_run(loaded, outputs):
    def validator(path, text):
        require(
            text.encode() == outputs[path.relative_to(loaded.inputs.root).as_posix()],
            "staged transaction substitution",
        )

    transaction = loaded.claw.modules["transaction"].ValidatedWriteTransaction(
        loaded.inputs.root, validator=validator
    )
    for name, raw in outputs.items():
        transaction.stage(name, raw.decode())
    result = transaction.commit(apply=False)
    require(result.applied is False, "native dry-run unexpectedly applied")
    return result.as_dict()


def prepare(root, request_path, stage):
    loaded = _load(root, request_path)
    _admitted(loaded)
    records, moves, plan = _records(loaded)
    stage = _stage_path(loaded.inputs.root, stage)
    storage = PreparationTree(loaded.inputs.root, stage)
    try:
        tree = stage / "candidate"
        for category in ("mapped", "unmapped"):
            storage.ensure(tree / "data/ingredients" / category)
        for name, record in records.items():
            raw = serialized(record, loaded.inputs.root / SCHEMA)
            if name in loaded.owners and load_yaml(loaded.owners[name].content) == record:
                raw = loaded.owners[name].content
            storage.put("candidate/" + name, raw)
            require(
                load_yaml((tree / name).read_bytes()) == record,
                "serializer changed scientific payload",
            )
        aggregate = _CAPTURE.script("scripts/aggregate_records.py")
        for category, name in zip(("mapped", "unmapped"), AGGREGATES, strict=True):
            storage.check()
            collection, errors = aggregate.aggregate_individual_files(
                tree / "data/ingredients",
                category,
                validate=True,
                order_reference=loaded.inputs.root / name,
            )
            storage.check()
            require(not errors, "native aggregation incomplete")
            if collection is None:
                require(
                    not any(p.split("/")[2] == category for p in records),
                    "native aggregation lost nonempty category",
                )
                collection = {
                    "generation_date": loaded.request["timestamp"],
                    "total_count": 0,
                    "mapped_count": 0,
                    "unmapped_count": 0,
                    "ingredients": [],
                }
            storage.put(
                "candidate/" + name,
                serialized(collection, loaded.inputs.root / SCHEMA, "IngredientCollection"),
            )
        # Exercise the real native exporter in a second private tree, preserving
        # per-record-only fields and filenames from the actual staged corpus.
        exporter = _CAPTURE.script("scripts/export_individual_records.py")
        preserved = exporter.collect_preserved_fields(tree / "data/ingredients")
        names = exporter.collect_existing_filenames(tree / "data/ingredients")
        roundtrip = stage / "roundtrip"

        def record_sink(path, record):
            require(path.is_relative_to(roundtrip), "native exporter destination escaped roundtrip")
            storage.put(
                str(path.relative_to(stage)), serialized(record, loaded.inputs.root / SCHEMA)
            )

        for category, name in zip(("mapped", "unmapped"), AGGREGATES, strict=True):
            storage.ensure(roundtrip / "data/ingredients" / category)
            storage.check()
            stats = exporter.export_collection_to_individual_files(
                tree / name,
                roundtrip / "data/ingredients" / category,
                preserved=preserved,
                existing_names=names,
                record_sink=record_sink,
            )
            storage.check()
            require(
                stats["total"] == len([p for p in records if p.split("/")[2] == category]),
                "native exporter lost owners",
            )
        reexported = inventory(roundtrip)
        require(
            set(reexported) == set(records)
            and all(load_yaml(f.content) == records[p] for p, f in reexported.items()),
            "native roundtrip changed full records or filenames",
        )
        outputs = {name: (tree / name).read_bytes() for name in (*records, *AGGREGATES)}
        outputs[str(REGISTRY_PATH)], outputs[str(LIFECYCLE_PATH)] = dump_registry(
            plan.registry
        ), dump_lifecycle(plan.registry)
        require(
            outputs[str(REGISTRY_PATH)].startswith(loaded.inputs.read(str(REGISTRY_PATH)))
            and outputs[str(LIFECYCLE_PATH)] == loaded.inputs.read(str(LIFECYCLE_PATH)),
            "ledger prefix/lifecycle changed",
        )
        for name in (str(REGISTRY_PATH), str(LIFECYCLE_PATH)):
            storage.put("candidate/" + name, outputs[name])
        dry_run = _dry_run(loaded, outputs)
        loaded.check()
        manifest = {
            "schema_version": 1,
            "capability": CAPABILITY,
            "status": "PREPARED_CANDIDATE_ONLY",
            "scientific_approval_added": False,
            "root": str(loaded.inputs.root),
            "request": {
                "path": loaded.request_path,
                "sha256": sha(loaded.inputs.read(loaded.request_path)),
            },
            "head": loaded.head,
            "index_sha256": sha(loaded.index),
            "history_base": loaded.request["history_base"],
            "inputs": hashes(loaded.inputs.files),
            "legacy_inputs": hashes(loaded.legacy.files),
            "producer": _CAPTURE.receipt(loaded.inputs),
            "claw": loaded.claw.receipt(),
            "before_inventory": hashes(loaded.owners),
            "after_inventory": {p: sha(outputs[p]) for p in records},
            "outputs": {p: sha(raw) for p, raw in outputs.items()},
            "moves": moves,
            "assignments": plan.assignments,
            "decisions": loaded.request["decisions"],
            "source_cases": [case["case_id"] for case in loaded.context["cases"]],
            "native_write_dry_run": dry_run,
        }
        storage.put("manifest.json", encoded(manifest))
        loaded.check()
        return manifest
    except BaseException as error:
        try:
            storage.put(
                "FAILED.json",
                encoded(
                    {
                        "status": "FAILED_PREPARATION",
                        "error": f"{type(error).__name__}: {error}",
                        "live_writes": False,
                    }
                ),
            )
        except (OSError, ValueError):
            # A substituted staging tree must not redirect even the failure log.
            pass
        raise


def _prepared(root, stage, *, before=None):
    root = root_path(root, "target")
    stage = Path(stage).absolute()
    no_alias(stage)
    require(not (stage / "FAILED.json").exists(), "failed preparation cannot apply")
    manifest_file = FrozenFile.capture(stage / "manifest.json")
    manifest = document(manifest_file.content)
    keys(
        manifest,
        {
            "schema_version",
            "capability",
            "status",
            "scientific_approval_added",
            "root",
            "request",
            "head",
            "index_sha256",
            "history_base",
            "inputs",
            "legacy_inputs",
            "producer",
            "claw",
            "before_inventory",
            "after_inventory",
            "outputs",
            "moves",
            "assignments",
            "decisions",
            "source_cases",
            "native_write_dry_run",
        },
    )
    require(
        manifest["schema_version"] == 1
        and manifest["capability"] == CAPABILITY
        and manifest["status"] == "PREPARED_CANDIDATE_ONLY"
        and manifest["scientific_approval_added"] is False
        and manifest["root"] == str(Path(root).absolute()),
        "invalid prepared manifest",
    )
    loaded = _load(
        root,
        manifest["request"]["path"],
        before=before,
        historical_after=manifest["after_inventory"] if before is not None else None,
    )
    require(
        sha(loaded.inputs.read(loaded.request_path)) == manifest["request"]["sha256"],
        "request changed",
    )
    _admitted(loaded)
    records, moves, plan = _records(loaded)
    require(
        manifest["head"] == loaded.request["baseline_commit"]
        and manifest["history_base"] == loaded.request["history_base"],
        "prepared Git provenance differs",
    )
    if before is None:
        require(manifest["index_sha256"] == sha(loaded.index), "prepared Git index differs")
    require(
        all(
            manifest["inputs"].get(name) == pin for name, pin in hashes(loaded.inputs.files).items()
        )
        and all(
            manifest["legacy_inputs"].get(name) == pin
            for name, pin in hashes(loaded.legacy.files).items()
        ),
        "prepared input closure is incomplete",
    )
    require(
        manifest["moves"] == moves
        and manifest["assignments"] == plan.assignments
        and manifest["before_inventory"] == hashes(loaded.owners),
        "prepared administrative plan differs",
    )
    for name, expected in manifest["inputs"].items():
        loaded.inputs.read(name, expected)
    for name, expected in manifest["legacy_inputs"].items():
        loaded.legacy.read(name, expected)
    if before is None:
        require(
            manifest["producer"] == _CAPTURE.receipt(loaded.inputs), "producer provenance changed"
        )
    else:
        current_producer = _CAPTURE.receipt(loaded.inputs)
        require(
            all(
                manifest["producer"][key] == current_producer[key]
                for key in ("source_sha256", "files", "runtime")
            ),
            "executing producer no longer matches original adoption",
        )
        require(
            manifest["producer"]["selected_context"]["git_revision"]
            == loaded.request["baseline_commit"],
            "original adoption Git context differs",
        )
    require(manifest["claw"] == loaded.claw.receipt(), "Claw producer provenance changed")
    require(
        set(manifest["outputs"])
        == {*records, *AGGREGATES, str(REGISTRY_PATH), str(LIFECYCLE_PATH)},
        "prepared output membership differs",
    )
    outputs, staged = {}, {}
    actual_files = set()
    for path in (stage / "candidate").rglob("*"):
        no_alias(path)
        if path.is_file():
            actual_files.add(str(path.relative_to(stage / "candidate")))
    require(actual_files == set(manifest["outputs"]), "extra or missing prepared files")
    for name, expected in manifest["outputs"].items():
        relative(name)
        frozen = FrozenFile.capture(stage / "candidate" / name)
        require(sha(frozen.content) == expected, "prepared output changed")
        outputs[name], staged[name] = frozen.content, frozen
    for name, record in records.items():
        require(
            load_yaml(outputs[name]) == record
            and not validate_ingredient(record, schema_path=loaded.inputs.root / SCHEMA),
            "prepared record or schema differs",
        )
    for category, name in zip(("mapped", "unmapped"), AGGREGATES, strict=True):
        collection = load_yaml(outputs[name])
        expected = [record for path, record in records.items() if path.split("/")[2] == category]
        actual = collection["ingredients"]
        stripped = [{k: v for k, v in record.items() if k != "discussions"} for record in expected]
        require(
            sorted(actual, key=lambda x: x["mim_id"])
            == sorted(stripped, key=lambda x: x["mim_id"]),
            "prepared aggregate lost or changed records",
        )
        require(
            collection["mapped_count"] == sum(r["mapping_status"] == "MAPPED" for r in expected)
            and collection["unmapped_count"]
            == sum(r["mapping_status"] == "UNMAPPED" for r in expected),
            "prepared aggregate status counts differ",
        )
        require(
            collection["total_count"] == len(expected)
            and not validate_ingredient(
                collection,
                target_class="IngredientCollection",
                schema_path=loaded.inputs.root / SCHEMA,
            ),
            "prepared aggregate invalid",
        )
    require(
        outputs[str(REGISTRY_PATH)] == dump_registry(plan.registry)
        and outputs[str(LIFECYCLE_PATH)] == dump_lifecycle(plan.registry),
        "prepared ledgers differ",
    )
    require(
        manifest["after_inventory"] == {p: sha(outputs[p]) for p in records}
        and manifest["decisions"] == loaded.request["decisions"]
        and manifest["source_cases"] == [case["case_id"] for case in loaded.context["cases"]],
        "prepared accounting differs",
    )
    expected_dry_run: dict[str, Any] = {
        "applied": False,
        "changed": [],
        "created": [],
        "unchanged": [],
        "journal": None,
    }
    for name in sorted(outputs):
        previous = loaded.inputs.files.get(name)
        status = (
            "created"
            if previous is None
            else "unchanged" if previous.content == outputs[name] else "changed"
        )
        expected_dry_run[status].append(str(loaded.inputs.root / name))
    require(
        manifest["native_write_dry_run"] == expected_dry_run, "native dry-run accounting differs"
    )
    loaded.check()
    return loaded, manifest, manifest_file, staged, outputs


def _acceptance(loaded, manifest_file, acceptance_path):
    path = (
        str(Path(acceptance_path).relative_to(loaded.inputs.root))
        if Path(acceptance_path).is_absolute()
        else str(acceptance_path)
    )
    acceptance = document(loaded.inputs.read(path))
    keys(acceptance, {"manifest_sha256", "review", "markdown_sha256"})
    require(
        acceptance["manifest_sha256"] == sha(manifest_file.content),
        "acceptance names another prepared set",
    )
    report_path = acceptance["review"]["path"]
    report_raw = loaded.inputs.read(report_path, acceptance["review"]["sha256"])
    markdown = loaded.inputs.read(
        str(Path(report_path).with_name("review.md")), acceptance["markdown_sha256"]
    )
    native = _CAPTURE.script("scripts/record_review.py")
    report = native.parse_review_bundle(
        report_path, report_raw, markdown, loaded.inputs.root / "schema/record_review.yaml"
    )
    require(
        native.source_provenance(loaded.inputs.root, report)["status"]
        not in {"invalid", "unverified"},
        "invalid acceptance provenance",
    )
    require(
        report["repository"] == REPOSITORY
        and report["completion"] == "completed"
        and report["scientific_review"] is False
        and report["verdict"] in {"pass", "pass_with_limitations"}
        and report["reviewer"]["independence"] == "independent"
        and report["reviewer"].get("independence_basis"),
        "independent completed technical acceptance required",
    )
    relative_manifest = str(manifest_file.path.relative_to(loaded.inputs.root))
    source = {x["path"]: x["sha256"] for x in report["source"]["inputs"]}
    require(
        source.get(relative_manifest) == sha(manifest_file.content),
        "acceptance omits manifest input",
    )
    for name, expected in source.items():
        loaded.inputs.read(name, expected)
    targets = [
        x
        for x in report["targets"]
        if x.get("path") == relative_manifest
        and x.get("semantic_digest", {}).get("sha256") == sha(manifest_file.content)
    ]
    require(len(targets) == 1, "acceptance target must bind exact manifest bytes")
    target = targets[0]
    require(
        target.get("kind") == "snapshot_row"
        and target.get("selector") == "prepared"
        and target.get("semantic_digest")
        == {
            "algorithm": "sha256",
            "sha256": sha(manifest_file.content),
            "description": "Exact prepared manifest bytes",
        }
        and target.get("owner_paths")
        == [{"repository": REPOSITORY, "path": relative_manifest, "role": "prepared candidate"}],
        "acceptance target contract differs",
    )
    tid = target["target_id"]
    require(tid in report["scope"]["reviewed_target_ids"], "prepared target outside review scope")
    require(
        all(
            x["status"] == "passed"
            for x in report["checks"]
            if x["required"] and tid in x["target_ids"]
        )
        and not any(
            tid in x["target_ids"] and x["status"] in {"open", "deferred"}
            for x in report["findings"]
        ),
        "acceptance has unresolved checks/findings",
    )
    require(
        any(
            x["target_ids"] == [tid]
            and x["outcome"] == "supported"
            and {y["name"]: y["value"] for y in x.get("dimensions", [])}.get("adoption_action")
            == "apply_exact_prepared_set"
            for x in report["assessments"]
        ),
        "explicit prepared-set acceptance required",
    )
    return {"path": path, "sha256": sha(loaded.inputs.read(path))}


def apply(root, stage, acceptance_path, receipt_dir, *, enabled=False):
    root = root_path(root, "target")
    receipt_dir = Path(receipt_dir).absolute()
    if enabled and os.path.lexists(receipt_dir):
        require(".." not in receipt_dir.parts, "stage/receipt traversal refused (#1315)")
        verified = verify_completed(root, stage, receipt_dir / "application.json")
        previous = document(FrozenFile.capture(receipt_dir / "application.json").content)
        acceptance_file = FrozenFile.capture(Path(acceptance_path).absolute())
        require(
            previous["acceptance"]
            == {
                "path": str(acceptance_file.path.relative_to(Path(root).absolute())),
                "sha256": sha(acceptance_file.content),
            },
            "completed rerun names another acceptance",
        )
        return {"applied": False, "unchanged": True, "verification": verified}
    loaded, manifest, manifest_file, staged, outputs = _prepared(root, stage)
    acceptance = _acceptance(loaded, manifest_file, acceptance_path)
    receipt_dir = _stage_path(loaded.inputs.root, receipt_dir)
    if not enabled:
        loaded.check()
        return {
            "applied": False,
            "approval": "NONE",
            "native_write_dry_run": _dry_run(loaded, outputs),
        }
    locks = loaded.claw.modules["locks"].LockManager()
    with locks.lock("mediaingredientmech", "reviewed campaign stable-ID adoption"):
        lease = locks.check_lock("mediaingredientmech")
        require(lease and lease.get("lease_token"), "native write lease unavailable")
        lease_token = lease["lease_token"]
        loaded.check()
        # This is the native pure planner recheck, not a second allocator.
        _, moves, check_plan = _records(loaded)
        require(
            check_plan.assignments == manifest["assignments"], "registry changed after preparation"
        )
        for frozen in staged.values():
            frozen.verify()
        manifest_file.verify()
        _dry_run(loaded, outputs)
        receipt_storage = PreparationTree(loaded.inputs.root, receipt_dir)
        directory_identity = (receipt_dir.stat().st_dev, receipt_dir.stat().st_ino)
        log = receipt_dir / "application.json"
        states = dict(loaded.owners)
        for name in (*AGGREGATES, str(REGISTRY_PATH), str(LIFECYCLE_PATH)):
            states[name] = loaded.inputs.files[name]
        archives = {
            receipt_dir / f"before-{index:05d}.bin": frozen.content
            for index, frozen in enumerate(states.values())
        }
        before_refs = {
            name: {
                "path": str(path.relative_to(loaded.inputs.root)),
                "sha256": sha(states[name].content),
            }
            for name, path in zip(states, archives, strict=True)
        }
        for index, _name in enumerate(moves):
            receipt_storage.ensure(receipt_dir / f"relocation-{index:05d}")
        result = {
            "schema_version": 1,
            "capability": CAPABILITY,
            "state": "PREPARED",
            "scientific_approval_added": False,
            "manifest": {
                "path": str(manifest_file.path.relative_to(loaded.inputs.root)),
                "sha256": sha(manifest_file.content),
            },
            "acceptance": acceptance,
            "beforeimages": before_refs,
            "expected_outputs": manifest["outputs"],
            "completed_operations": [],
            "retired_sources": {},
            "recovery_required": False,
        }
        with reserve_receipt_outputs(log, backup_paths=tuple(archives)) as handles:
            receipt, *backups = handles
            archived: list[FrozenFile] = []

            def recheck(during=()):
                current_lease = locks.check_lock("mediaingredientmech")
                require(
                    current_lease and current_lease.get("lease_token") == lease_token,
                    "native write lease lost",
                )
                receipt_storage.check()
                no_alias(receipt_dir)
                require(
                    (receipt_dir.stat().st_dev, receipt_dir.stat().st_ino) == directory_identity,
                    "receipt directory changed",
                )
                for path, handle in zip((log, *archives), handles, strict=True):
                    check_reserved(handle, path)
                for frozen in (*archived, *staged.values(), manifest_file):
                    frozen.verify()
                loaded.check(states, during)

            def progress():
                check_reserved(receipt, log)
                receipt.seek(0)
                receipt.truncate()
                receipt.write(encoded(result).decode())
                receipt.flush()
                os.fsync(receipt.fileno())
                check_reserved(receipt, log)

            try:
                for handle, raw in zip(backups, archives.values(), strict=True):
                    handle.write(raw)
                    handle.flush()
                    os.fsync(handle.fileno())
                archived.extend(FrozenFile.capture(path) for path in archives)
                recheck()
                progress()
                result["state"] = "APPLYING"
                # Owners first, then explicit retirements, both aggregates, and
                # append-only ledger last. No intermediate phase is a release.
                owner_outputs = [p for p in outputs if p.startswith("data/ingredients/")]
                phases = [
                    *owner_outputs,
                    "__RELOCATIONS__",
                    *AGGREGATES,
                    str(LIFECYCLE_PATH),
                    str(REGISTRY_PATH),
                ]
                for name in phases:
                    recheck()
                    if name == "__RELOCATIONS__":
                        for index, source in enumerate(moves):
                            retired = _retire(
                                states[source], receipt_dir / f"relocation-{index:05d}", recheck
                            )
                            result["retired_sources"][source] = {
                                "path": str(retired.path.relative_to(loaded.inputs.root)),
                                "sha256": sha(retired.content),
                            }
                            del states[source]
                            archived.append(retired)
                            result["completed_operations"].append(
                                {"kind": "relocate", "source": source, "destination": moves[source]}
                            )
                            recheck()
                            progress()
                        continue
                    raw = outputs[name]
                    if name in states and states[name].content == raw:
                        continue
                    if name in states:

                        def render(p: Path, raw: bytes = raw) -> None:
                            p.write_bytes(raw)

                        def boundary(name: str = name) -> None:
                            recheck((name,))

                        published = publish_validated(states[name], render, boundary)
                    else:
                        published = _new_owner(
                            loaded.inputs.root, name, raw, lambda name=name: recheck((name,))
                        )
                    states[name] = published
                    require(published.content == raw, "unexpected postimage")
                    result["completed_operations"].append(
                        {"kind": "write", "path": name, "sha256": sha(raw)}
                    )
                    recheck()
                    progress()
                require(
                    hashes(inventory(loaded.inputs.root)) == manifest["after_inventory"],
                    "final owner inventory differs",
                )
                validate_records(
                    parse_registry(outputs[str(REGISTRY_PATH)], outputs[str(LIFECYCLE_PATH)]),
                    {name: load_yaml(outputs[name]) for name in manifest["after_inventory"]},
                )
                validate_history(loaded.inputs.root, loaded.request["history_base"])
                result["state"] = "COMPLETE"
                receipt.seek(0)
                receipt.truncate()
                finish_receipt(receipt, log, result, recheck)
                return result
            except BaseException as error:
                result.update(
                    state="FAILED", recovery_required=True, error=f"{type(error).__name__}: {error}"
                )
                result["observed_outputs"] = {}
                for name in set(manifest["outputs"]) | set(manifest["moves"]):
                    try:
                        result["observed_outputs"][name] = {
                            "sha256": sha(FrozenFile.capture(loaded.inputs.root / name).content)
                        }
                    except (OSError, ValueError) as observed:
                        result["observed_outputs"][name] = {
                            "error": f"{type(observed).__name__}: {observed}"
                        }
                try:
                    progress()
                except (OSError, ValueError):
                    pass
                raise


def verify_completed(root, stage, receipt_path):
    """Verify the actual current endpoint using explicitly archived beforeimages.

    Archived inputs are original receipt targets, never mislabeled current files.
    This proves the administrative transition; it grants no new science approval.
    """
    root, stage = root_path(root, "target"), Path(stage).absolute()
    manifest_file = FrozenFile.capture(stage / "manifest.json")
    manifest = document(manifest_file.content)
    receipt_file = FrozenFile.capture(Path(receipt_path).absolute())
    receipt = document(receipt_file.content)
    require(
        receipt["state"] == "COMPLETE"
        and receipt["recovery_required"] is False
        and receipt["scientific_approval_added"] is False
        and receipt["manifest"]
        == {
            "path": str(manifest_file.path.relative_to(root)),
            "sha256": sha(manifest_file.content),
        },
        "no completed adoption receipt",
    )
    required_before = (
        set(manifest["before_inventory"])
        | set(AGGREGATES)
        | {str(REGISTRY_PATH), str(LIFECYCLE_PATH)}
    )
    require(set(receipt["beforeimages"]) == required_before, "incomplete adoption beforeimages")
    before = {}
    for name, reference in receipt["beforeimages"].items():
        frozen = FrozenFile.capture(root / relative(reference["path"]))
        require(
            sha(frozen.content) == reference["sha256"] == manifest["inputs"][name],
            "recovery beforeimage differs",
        )
        before[name] = frozen
    loaded, checked_manifest, checked_file, staged, outputs = _prepared(root, stage, before=before)
    require(
        checked_manifest == manifest and checked_file.content == manifest_file.content,
        "manifest changed during verification",
    )
    acceptance = _acceptance(loaded, manifest_file, receipt["acceptance"]["path"])
    require(acceptance == receipt["acceptance"], "acceptance reference differs")
    require(
        receipt["expected_outputs"] == manifest["outputs"]
        and set(receipt["retired_sources"]) == set(manifest["moves"]),
        "completion scope differs",
    )
    for source, reference in receipt["retired_sources"].items():
        require(not os.path.lexists(root / source), "retired source reappeared")
        require(
            sha(FrozenFile.capture(root / relative(reference["path"])).content)
            == reference["sha256"]
            == manifest["before_inventory"][source],
            "retired source bytes differ",
        )
    for name, expected in manifest["outputs"].items():
        require(
            sha(FrozenFile.capture(root / relative(name)).content) == expected,
            "current maintained output differs",
        )
    expected_events = []
    for name in [p for p in outputs if p.startswith("data/ingredients/")]:
        if name not in before or before[name].content != outputs[name]:
            expected_events.append({"kind": "write", "path": name, "sha256": sha(outputs[name])})
    expected_events.extend(
        {"kind": "relocate", "source": source, "destination": dest}
        for source, dest in manifest["moves"].items()
    )
    for name in (*AGGREGATES, str(LIFECYCLE_PATH), str(REGISTRY_PATH)):
        if before[name].content != outputs[name]:
            expected_events.append({"kind": "write", "path": name, "sha256": sha(outputs[name])})
    require(receipt["completed_operations"] == expected_events, "completed phase log differs")
    loaded.check()
    receipt_file.verify()
    return {
        "status": "COMPLETE_CURRENT_CANDIDATE",
        "scientific_approval_added": False,
        "manifest_sha256": sha(manifest_file.content),
        "original_head": manifest["head"],
        "current_head": loaded.head,
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("operation", choices=["inspect", "prepare", "apply", "verify"])
    parser.add_argument("--root", type=Path, default=Path.cwd())
    parser.add_argument("--request", type=Path)
    parser.add_argument("--stage", type=Path)
    parser.add_argument("--acceptance", type=Path)
    parser.add_argument("--receipt", type=Path)
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args()
    if args.operation == "inspect":
        result = inspect(args.root, args.request)
    elif args.operation == "prepare":
        result = prepare(args.root, args.request, args.stage)
    elif args.operation == "apply":
        result = apply(args.root, args.stage, args.acceptance, args.receipt, enabled=args.apply)
    else:
        result = verify_completed(args.root, args.stage, args.receipt)
    print(encoded(result).decode())


if _CAPTURE is None:
    _root = Path(__file__).absolute().parents[3]
    _path = _root / "src/mediaingredientmech/curate/adoption_producer.py"
    _raw = _path.read_bytes()
    _loader = types.ModuleType("_adoption_loader")
    _loader.__file__ = str(_path)
    exec(compile(_raw, str(_path), "exec"), _loader.__dict__)
    _capture, _implementation = _loader.load(_root, _raw)
    for _name, _value in vars(_implementation).items():
        if not _name.startswith("__"):
            globals()[_name] = _value

if __name__ == "__main__":
    main()
