"""Closed, approval-free campaign publication (#1174).

Source curation, scientific approval and companion review are separate. This
module reconstructs a reviewed row plan, preserves the old policy history, and
uses native receipt alignment/replay and guarded filesystem publication.
"""

from __future__ import annotations

import csv
import hashlib
import io
import json
import os
import re
import subprocess
import sys
import types
from collections.abc import Callable
from contextlib import ExitStack, contextmanager
from copy import deepcopy
from pathlib import Path, PurePosixPath
from typing import TYPE_CHECKING, Any, cast

import yaml  # type: ignore[import-untyped]

from mediaingredientmech.curate import campaign_owner_apply as _source_owner

_NATIVE_SOURCES = {
    "mediaingredientmech.curate.publication_guard": "src/mediaingredientmech/curate/publication_guard.py",
    "mediaingredientmech.validation.mapping_change_receipts": "src/mediaingredientmech/validation/mapping_change_receipts.py",
    "mediaingredientmech.export.reviewed_sssom": "src/mediaingredientmech/export/reviewed_sssom.py",
    "mediaingredientmech.sssom_metadata": "src/mediaingredientmech/sssom_metadata.py",
    "mediaingredientmech.synonym_policy": "src/mediaingredientmech/synonym_policy.py",
    "campaign_native_sssom_invariants": "scripts/validate_sssom_invariants.py",
}
_BOUND_NATIVE = _source_owner.captured_native_modules(
    Path(__file__).absolute().parents[2], _NATIVE_SOURCES
)
if TYPE_CHECKING:
    from mediaingredientmech.curate.publication_guard import (
        FrozenFile,
        check_reserved,
        finish_receipt,
        no_alias,
        publish_validated,
    )
    from mediaingredientmech.sssom_metadata import subset_date_metadata
    from mediaingredientmech.validation import mapping_change_receipts as native
else:
    _guard = _BOUND_NATIVE["mediaingredientmech.curate.publication_guard"]
    FrozenFile, check_reserved = _guard.FrozenFile, _guard.check_reserved
    finish_receipt, no_alias = _guard.finish_receipt, _guard.no_alias
    publish_validated = _guard.publish_validated
    subset_date_metadata = _BOUND_NATIVE["mediaingredientmech.sssom_metadata"].subset_date_metadata
    native = _BOUND_NATIVE["mediaingredientmech.validation.mapping_change_receipts"]

SOURCE = native.SSSOM_SOURCE
POLICY = SOURCE + ".manifest.json"
SIDECAR = "mappings/suppressed_aliases.tsv"
BASELINE = "mappings/other_cross_record_baseline.tsv"
MAKER = "reports/sssom_completion_20260921/mapping_changes/make_receipt.py"
MAKER_SHA = "2d007139f3cea26df86217807c263fd3580771034719fb1fd79361d884b5a121"
UPDATE = "campaign_publication_updates"
ISSUE = "https://github.com/CultureBotAI/MediaIngredientMech/issues/1174"
PRODUCER_REVISION = "76c1ebeea3fc7f80bf1abe044688f298f390cfac"
PRODUCER_SHA = "38d59f42953305f6fc51e4fc24dfc59ee1919bfb961595b67a8afe9f8a46a1bc"
APPROVAL = "NONE: all touched rows and changed owners require separate scientific review"
HISTORICAL_FIELDS = frozenset({"source", "comment", "confidence", "validation_method"})
POLICY_KEYS = frozenset(
    {
        "schema_version",
        "policy_version",
        "approval",
        "scope",
        "decisions",
        "policy_evidence",
        "producer_revision",
        "generation_manifest_sha256",
        "generation_receipt_sha256",
        "source_receipt_sha256",
        "sssom_before_sha256",
        "baseline_before_sha256",
        "artifacts",
        "source_owner_sha256",
        "form_projection_updates",
        "registry_correction_updates",
        "stock_cas_removal_updates",
        "owned_name_suppression_updates",
        "source_alias_addition_updates",
        UPDATE,
    }
)
POLICY_REQUIRED = POLICY_KEYS - {
    "form_projection_updates",
    "registry_correction_updates",
    "stock_cas_removal_updates",
    "owned_name_suppression_updates",
    "source_alias_addition_updates",
    UPDATE,
}
PLAN_KEYS = frozenset(
    {
        "schema_version",
        "kind",
        "issue",
        "approval",
        "batch",
        "scope",
        "owner_plan",
        "owner_receipt",
        "publication_producers",
        "before",
        "generation",
        "receipt_prefix",
        "native_context",
        "rows",
    }
)
_LOADED = Path(__file__).read_bytes()
LOADED_PRODUCERS = {
    path: _BOUND_NATIVE[name]._campaign_executed_source for name, path in _NATIVE_SOURCES.items()
}
LOADED_PRODUCERS["src/mediaingredientmech/campaign_publication.py"] = FrozenFile.capture(
    Path(__file__).absolute()
)
LOADED_PRODUCERS["src/mediaingredientmech/curate/campaign_owner_apply.py"] = (
    _source_owner.LOADED_PRODUCERS["src/mediaingredientmech/curate/campaign_owner_apply.py"]
)


def require(condition: object, message: str) -> None:
    if not condition:
        raise ValueError("Campaign publication: " + message)


def sha(raw: bytes) -> str:
    return hashlib.sha256(raw).hexdigest()


def read_json(raw: bytes) -> Any:
    def pairs(items):
        result = {}
        for key, value in items:
            require(key not in result, "duplicate JSON field")
            result[key] = value
        return result

    def invalid_number(value):
        raise ValueError("Campaign publication: non-finite JSON value " + value)

    return json.loads(raw, object_pairs_hook=pairs, parse_constant=invalid_number)


def closed(value: Any, keys: set[str] | frozenset[str], label: str) -> dict:
    require(isinstance(value, dict) and set(value) == keys, "unknown/missing " + label + " fields")
    return cast(dict, value)


def digest(value: Any) -> str:
    require(isinstance(value, str) and re.fullmatch(r"[0-9a-f]{64}", value), "invalid digest")
    return cast(str, value)


def relative(value: Any) -> str:
    require(isinstance(value, str) and value, "missing relative path")
    p = PurePosixPath(value)
    require(
        not p.is_absolute() and str(p) == value and not {".", ".."} & set(p.parts),
        "unsafe relative path",
    )
    require("\\" not in value and "\x00" not in value, "nonportable path")
    return cast(str, value)


def member(root: Path, name: str) -> Path:
    p = root / relative(name)
    no_alias(p)
    require(p.absolute().is_relative_to(root), "path outside root")
    return p


def absolute(path: Path) -> Path:
    require(
        path.is_absolute() and str(path) == os.path.normpath(str(path)) and ".." not in path.parts,
        "noncanonical absolute path",
    )
    no_alias(path)
    return path


def encoded(value: Any) -> bytes:
    return (
        json.dumps(value, indent=2, sort_keys=True, ensure_ascii=False, allow_nan=False) + "\n"
    ).encode()


def hash_map(value: Any) -> dict[str, str]:
    require(isinstance(value, dict), "missing hash inventory")
    for name, expected in value.items():
        relative(name)
        digest(expected)
    return cast(dict[str, str], value)


def table(raw: bytes) -> tuple[list[str], list[str], list[dict[str, str]], list[str]]:
    """Keep unrelated physical rows byte-identical; reject multiline ambiguity."""
    lines = raw.decode("utf-8").splitlines(keepends=True)
    require(all(line.endswith("\n") for line in lines), "unterminated SSSOM line")
    i = next((i for i, line in enumerate(lines) if not line.startswith("#")), None)
    require(i is not None, "missing SSSOM header")
    i = cast(int, i)
    header, body = lines[:i], lines[i + 1 :]
    require(
        not any(line.startswith("#") or not line.strip() for line in body),
        "embedded SSSOM metadata",
    )
    fields = next(csv.reader([lines[i]], delimiter="\t"))
    require(len(fields) == len(set(fields)), "duplicate SSSOM column")
    values = [next(csv.reader([line], delimiter="\t")) for line in body]
    require(all(len(row) == len(fields) for row in values), "nonphysical SSSOM row")
    return (
        header + [lines[i]],
        fields,
        [dict(zip(fields, row, strict=True)) for row in values],
        body,
    )


def render_row(fields: list[str], row: dict[str, str]) -> str:
    require(
        set(row) == set(fields) and all(isinstance(v, str) for v in row.values()),
        "row fields differ",
    )
    require(not any("\n" in v or "\r" in v for v in row.values()), "multiline row")
    output = io.StringIO(newline="")
    csv.DictWriter(output, fieldnames=fields, delimiter="\t", lineterminator="\n").writerow(row)
    return output.getvalue()


def subject(path: str) -> str:
    return "MIM:" + re.sub(
        r"[^A-Za-z0-9_\-.]", lambda m: f"~{ord(m.group(0)):02X}", Path(path).stem
    )


def slot(row: dict) -> tuple[str, str]:
    prefix = row["object_id"].split(":", 1)[0]
    return row["subject_id"], (
        prefix if prefix in {"cas", "kgmicrobe.ingredient", "kgmicrobe.compound"} else "ontology"
    )


def row_projection(
    before: bytes, candidate: bytes, records: list[dict], plan: list[dict]
) -> tuple[bytes, list[dict]]:
    header, fields, old, lines = table(before)
    _, candidate_fields, generated, _ = table(candidate)
    require(fields == candidate_fields, "native/canonical columns differ")
    owners = {r["source_record"]: r for r in records}
    subject_owners = {subject(p): p for p in owners}
    require(len(subject_owners) == len(owners), "ambiguous source subject")
    old_slots = {slot(r): i for i, r in enumerate(old, 1)}
    new_slots = {slot(r): i for i, r in enumerate(generated, 1)}
    require(
        len(old_slots) == len(old) and len(new_slots) == len(generated), "ambiguous native row slot"
    )
    expected = {}
    for key in old_slots.keys() | new_slots.keys():
        if key[0] in subject_owners:
            expected[key] = (old_slots.get(key), new_slots.get(key), subject_owners[key[0]])
    require(isinstance(plan, list), "row plan must be a list")
    seen, replacements, appended, trace = set(), {}, [], []
    for operation in plan:
        closed(
            operation,
            {"owner", "before_position", "native_position", "preserve_fields"},
            "row plan",
        )
        owner = relative(operation["owner"])
        require(owner in owners, "row owner not in applied source scope")
        a, b = operation["before_position"], operation["native_position"]
        require(a is not None or b is not None, "empty row operation")
        for pos, rows in ((a, old), (b, generated)):
            require(
                pos is None or (type(pos) is int and 1 <= pos <= len(rows)),
                "row position outside source",
            )
        left, right = old[a - 1] if a else None, generated[b - 1] if b else None
        key = slot(cast(dict, right or left))
        require(
            key not in seen and expected.get(key) == (a, b, owner),
            "missing/extra/misowned row plan",
        )
        seen.add(key)
        preserve = operation["preserve_fields"]
        require(
            isinstance(preserve, list)
            and len(preserve) == len(set(preserve))
            and set(preserve) <= HISTORICAL_FIELDS,
            "invalid preserved provenance fields",
        )
        require(
            not preserve or (left is not None and right is not None),
            "provenance has no historical row",
        )
        result = dict(right) if right is not None else None
        if result is not None:
            for field in preserve:
                require(field in fields, "preserved field not in schema")
                result[field] = cast(dict, left)[field]
        if a:
            replacements[a] = result
        else:
            appended.append((b, result))
        trace.append(
            {
                "owner": owner,
                "before_position": a,
                "native_position": b,
                "preserve_fields": preserve,
                "before": left,
                "after": result,
                "changed_cells": [
                    {
                        "field": field,
                        "before": left.get(field) if left else None,
                        "after": result.get(field) if result else None,
                        "basis": "native_owner_projection" if result else "native_slot_absent",
                    }
                    for field in fields
                    if (left or {}).get(field) != (result or {}).get(field)
                ],
            }
        )
    require(seen == set(expected), "row plan does not cover every selected native/canonical slot")
    out_rows, body = [], []
    for i, row in enumerate(old, 1):
        result = replacements.get(i, row)
        if result is not None:
            out_rows.append(result)
            body.append(lines[i - 1] if result == row else render_row(fields, result))
    for _, added_row in sorted(appended):
        out_rows.append(cast(dict, added_row))
        body.append(render_row(fields, cast(dict, added_row)))
    dates = subset_date_metadata({}, out_rows)
    for date_key in ("mapping_date", "mapping_set_version"):
        indices = [
            i for i, line in enumerate(header[:-1]) if line.startswith("# " + date_key + ":")
        ]
        require(
            len(indices) == 1 and date_key in dates, "missing/duplicate canonical date metadata"
        )
        previous = header[indices[0]]
        header[indices[0]] = f"# {date_key}: {dates[date_key]}\n"
        if previous != header[indices[0]]:
            trace.append(
                {
                    "metadata_field": date_key,
                    "before": previous,
                    "after": header[indices[0]],
                    "basis": "native subset_date_metadata over exact projected rows",
                }
            )
    return ("".join(header + body)).encode(), trace


class Capture:
    """Immutable input roles, membership, and original path identities."""

    def __init__(self, root: Path):
        self.root = absolute(root)
        self.files: dict[Path, FrozenFile] = {}
        self.absent: set[Path] = set()
        self.checks: list[Callable[[], None]] = []

    def read(self, name: str, expected: str | None = None) -> bytes:
        return self.external(member(self.root, name), expected)

    def external(self, path: Path, expected: str | None = None) -> bytes:
        absolute(path)
        item = FrozenFile.capture(path)
        if item.path in self.files:
            require(item == self.files[item.path], "input changed between roles")
        self.files[item.path] = item
        if expected is not None:
            require(sha(item.content) == digest(expected), "input digest differs: " + str(path))
        return cast(bytes, item.content)

    def ref(self, value: dict) -> bytes:
        closed(value, {"path", "sha256"}, "file reference")
        return self.read(relative(value["path"]), digest(value["sha256"]))

    def verify(self, exclude: set[Path] | None = None) -> None:
        for check in self.checks:
            check()
        for path, item in self.files.items():
            if path not in (exclude or set()):
                item.verify()
        for path in self.absent:
            no_alias(path)
            require(not path.exists(), "previously absent input appeared")


def _owner_proof(root: Path, plan: dict) -> dict:
    from mediaingredientmech.curate.campaign_owner_apply import verify_completed

    return cast(
        dict,
        verify_completed(
            root,
            member(root, plan["owner_plan"]["path"]),
            member(root, plan["owner_receipt"]["path"]),
        ),
    )


def _capture_source_completion(capture: Capture, proof: dict) -> None:
    """Hold complete inventories, not just the initially enumerated files (#1194)."""
    from mediaingredientmech.curate.campaign_owner_apply import hashes, inventory

    root = capture.root
    expected = hash_map(proof["after_inventory"])
    require(hashes(inventory(root)) == expected, "source completion inventory differs")
    for path, expected_sha in expected.items():
        capture.read(path, expected_sha)
    for path, expected_sha in hash_map(proof["immutable_input_sha256"]).items():
        capture.read(path, expected_sha)

    def owners_recheck() -> None:
        require(
            hashes(inventory(root)) == expected,
            "source completion owner membership or bytes changed",
        )

    capture.checks.append(owners_recheck)

    def snapshot_members(directory: Path) -> set[str]:
        no_alias(directory)
        require(directory.is_dir(), "source snapshot disappeared")
        members = set()
        for parent, directories, files in os.walk(directory, followlinks=False):
            for name in directories:
                no_alias(Path(parent) / name)
            for name in files:
                path = Path(parent) / name
                no_alias(path)
                members.add(str(path.relative_to(directory)))
        return members

    for role in ("checkpoint", "protected_snapshot"):
        snapshot = closed(proof[role], {"root", "input_sha256"}, "source snapshot")
        directory = member(root, relative(snapshot["root"]))
        members = hash_map(snapshot["input_sha256"])
        require(snapshot_members(directory) == set(members), "source snapshot membership differs")
        for path, expected_sha in members.items():
            capture.external(member(directory, path), expected_sha)

        def snapshot_recheck(directory=directory, members=frozenset(members)) -> None:
            require(
                snapshot_members(directory) == members,
                "source snapshot membership changed",
            )

        capture.checks.append(snapshot_recheck)

    for record in proof["records"]:
        if record["shape"] == "promotion":
            old_path = member(root, relative(record["before_source_record"]))
            require(not os.path.lexists(old_path), "retired source reappeared")
            capture.absent.add(old_path)


def _maker(capture: Capture):
    raw = capture.read(MAKER)
    require(sha(raw) == MAKER_SHA, "native receipt maker changed")
    module = types.ModuleType("campaign_native_receipt_maker")
    module.__file__ = str(member(capture.root, MAKER))
    exec(compile(raw, module.__file__, "exec"), module.__dict__)
    return module


def _receipt(
    proof: dict, maker: Any, plan: dict, owners: list[dict], before: bytes, after: bytes
) -> dict:
    old, new = maker.rows_of(before), maker.rows_of(after)
    changes, positions = maker.align(old, new)
    records = []
    for owner in owners:
        record = {
            key: owner[key]
            for key in (
                "source_record",
                "shape",
                "before_yaml_sha256",
                "after_yaml_sha256",
                "change",
                "verification",
            )
        }
        if owner["shape"] == "promotion":
            previous = relative(owner["before_source_record"])
            require(
                not proof["owner_chains"].get(previous),
                "promotion old path has native owner-chain history; migration review required",
            )
            require(
                not proof["owner_chains"].get(owner["source_record"]),
                "promotion destination has native owner-chain history; migration review required",
            )
            record["before_source_record"] = previous
        records.append(record)
    result = {
        "schema_version": 1,
        "batch": plan["batch"],
        "sequence": len(proof["receipts"]) + 1,
        "issue": ISSUE,
        "scope": plan["scope"],
        "approval": APPROVAL,
        "before_sha256": sha(before),
        "after_sha256": sha(after),
        "before_row_count": len(old),
        "after_row_count": len(new),
        "records": records,
        "changes": changes,
        "position_map": positions,
        "touched_subjects": sorted({(c["after"] or c["before"])["subject_id"] for c in changes}),
    }
    result.update(
        {
            kind + "_rows": sum(c["kind"] == kind for c in changes)
            for kind in ("changed", "added", "removed")
        }
    )
    native._validate_receipt(result, complete=True)
    # #1197: row replay alone cannot detect a disconnected owner preimage.
    # Validate the complete prospective owner chain before reserving outputs.
    receipt_path = native.RECEIPTS_DIR + "/" + plan["batch"] + ".json"
    native._owner_chains(
        proof["receipts"] + [result],
        proof["receipt_paths"] + [receipt_path],
        {**proof["receipt_inputs"], receipt_path: sha(encoded(result))},
    )
    replay = native.walk_mapping_changes(
        proof["receipts"] + [result],
        start_sha256=proof["start_sha256"],
        reviewed_sha256=sha(after),
        baseline_rows=proof["baseline_rows"],
        refreshed_rows=proof["refreshed_rows"],
    )
    require(replay[2] == new, "native row replay differs from projection")
    return result


def _generation(
    capture: Capture, plan: dict, before: bytes, inventory: dict
) -> tuple[bytes, bytes, dict]:
    """Replay the captured native producer without network label lookups."""
    config = closed(
        plan["generation"],
        {"candidate", "sidecar", "manifest", "producer_root", "kg_root"},
        "generation",
    )
    candidate, sidecar, raw_manifest = (
        capture.ref(config[key]) for key in ("candidate", "sidecar", "manifest")
    )
    manifest = closed(
        read_json(raw_manifest),
        {
            "schema_version",
            "policy_version",
            "artifacts",
            "scope",
            "external_sssom_validation",
            "prior_stamp_sources",
            "source_inputs",
            "producer_import_snapshot",
            "producer_binding_scope",
            "mapped_record_paths",
            "source_revisions",
            "canonical_label_resolution",
            "policy_evidence",
            "emitted_rows",
        },
        "native generation manifest",
    )
    require(
        type(manifest["schema_version"]) is int
        and manifest["schema_version"] == 1
        and manifest["policy_version"] == "owned-name-policy-v1"
        and manifest["external_sssom_validation"] == "passed",
        "unvalidated native candidate",
    )
    root = capture.root
    producer_root, kg_root = Path(config["producer_root"]), Path(config["kg_root"])
    for path in (producer_root, kg_root):
        absolute(path)
    revisions = closed(
        manifest["source_revisions"], {"claw", "mim", "kg_microbe"}, "source revisions"
    )
    require(
        all(
            isinstance(value, str) and re.fullmatch(r"[0-9a-f]{40}", value)
            for value in revisions.values()
        ),
        "invalid source revision",
    )
    require(
        manifest["source_revisions"]["claw"] == PRODUCER_REVISION, "unreviewed producer revision"
    )
    require(
        subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=producer_root, text=True).strip()
        == PRODUCER_REVISION,
        "producer revision moved",
    )
    require(
        subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=kg_root, text=True).strip()
        == revisions["kg_microbe"],
        "kg-microbe revision moved",
    )
    producer = producer_root / "scripts/build_mim_ingredient_sssom.py"
    source = capture.external(producer, PRODUCER_SHA)
    mapped = {
        str(root / p): h for p, h in inventory.items() if p.startswith("data/ingredients/mapped/")
    }
    require(
        manifest["mapped_record_paths"] == sorted(mapped), "generation mapped membership differs"
    )
    input_names = {}
    for item in manifest["source_inputs"]:
        closed(item, {"path", "sha256"}, "generation source")
        path = Path(item["path"])
        absolute(path)
        require(
            path.is_absolute()
            and path not in input_names
            and any(path.is_relative_to(r) for r in (root, producer_root, kg_root)),
            "unconfined/duplicate native source",
        )
        no_alias(path)
        expected = item["sha256"]
        if path == root / SOURCE:
            require(
                expected == sha(before), "native stamp source differs from canonical beforeimage"
            )
            content = before
        elif expected is None:
            require(not path.exists(), "absent native source appeared")
            capture.absent.add(path)
            content = None
        else:
            content = capture.external(path, expected)
        input_names[path] = content
    require(
        all(
            root / p in input_names
            and isinstance(input_names[root / p], bytes)
            and sha(cast(bytes, input_names[root / p])) == h
            for p, h in inventory.items()
            if p.startswith("data/ingredients/mapped/")
        ),
        "generation omitted current owners",
    )
    artifacts = manifest["artifacts"]
    require(isinstance(artifacts, list) and len(artifacts) == 2, "native artifact count differs")
    for item, role, ref in zip(
        artifacts,
        ("sssom", "suppressed_aliases"),
        (config["candidate"], config["sidecar"]),
        strict=True,
    ):
        require(
            item == {"role": role, "path": str(root / ref["path"]), "sha256": ref["sha256"]},
            "native artifact roles differ",
        )
    old_environment = {
        key: os.environ.get(key) for key in ("MEDIAINGREDIENTMECH_ROOT", "KGMICROBE_ROOT")
    }
    try:
        os.environ.update(MEDIAINGREDIENTMECH_ROOT=str(root), KGMICROBE_ROOT=str(kg_root))
        module = types.ModuleType("campaign_pinned_native_generator")
        module.__file__ = str(producer)
        sys.modules[module.__name__] = module
        exec(compile(source, str(producer), "exec"), module.__dict__)
    finally:
        for key, value in old_environment.items():
            if value is None:
                os.environ.pop(key, None)
            else:
                os.environ[key] = value
    producers = set(module._producer_paths())
    expected_inputs = (
        {Path(p) for p in mapped}
        | producers
        | {module.RESIDUAL_JSON, module.KGM_UNIFIED_TSV, root / SOURCE}
    )
    require(set(input_names) == expected_inputs, "native input coverage differs")
    require(manifest["prior_stamp_sources"] == [str(root / SOURCE)], "unsupported stamp history")
    actual_graph = {str(p): sha(b) for p, b in module._IMPORTED_PRODUCER_BYTES.items()}
    require(manifest["producer_import_snapshot"] == actual_graph, "native producer graph differs")
    for graph_path, expected in actual_graph.items():
        capture.external(Path(graph_path), expected)
    records = {Path(p): yaml.safe_load(input_names[Path(p)]) for p in mapped}
    owned = module.build_owner_index(
        {module._mim_curie(p.name): data for p, data in records.items()}
    )
    residual_raw = input_names[module.RESIDUAL_JSON]
    residual = (
        {d["source_file"]: d for d in json.loads(residual_raw).get("decisions", [])}
        if residual_raw
        else {}
    )
    kg_path = module.KGM_UNIFIED_TSV
    kg_sources = module.load_kgm_source_index(kg_path) if input_names[kg_path] else {}
    kg_labels = module.load_kgm_labels(kg_path) if input_names[kg_path] else {}
    labels = manifest["canonical_label_resolution"]
    require(
        isinstance(labels, dict)
        and all(isinstance(k, str) and isinstance(v, str) for k, v in labels.items()),
        "invalid native label capture",
    )
    generated: list[dict] = []
    suppressions: list[Any] = []
    for path in sorted(records):
        generated.extend(
            module._row_from_yaml(
                path,
                residual,
                kg_sources,
                kg_labels,
                labels,
                record=records[path],
                owners=owned,
                suppressions=suppressions,
            )
        )
    unique = {(r["subject_id"], r["object_id"]): r for r in generated}
    generated = list(unique.values())
    stamps = {
        (r["subject_id"], r["predicate_id"], r["object_id"]): r["validation_method"].strip()
        for r in table(before)[2]
        if r.get("validation_method", "").strip()
    }
    module.apply_replayed_stamps(generated, stamps)
    require(generated == table(candidate)[2], "native row replay differs from diagnostic candidate")
    require(
        module.render_suppressed_aliases(suppressions) == sidecar,
        "native suppression replay differs",
    )
    require(manifest["emitted_rows"] == len(generated), "native row count differs")
    module._check_producer_bindings()

    def producer_recheck():
        require(set(module._producer_paths()) == producers, "producer membership changed")
        require(
            subprocess.check_output(
                ["git", "rev-parse", "HEAD"], cwd=producer_root, text=True
            ).strip()
            == PRODUCER_REVISION,
            "producer revision changed",
        )
        module._check_producer_bindings()
        require(
            subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=kg_root, text=True).strip()
            == revisions["kg_microbe"],
            "kg-microbe revision changed",
        )

    capture.checks.append(producer_recheck)
    return candidate, sidecar, manifest


def _policy(
    before: bytes,
    plan: dict,
    plan_sha: str,
    owner_proof: dict,
    receipt_name: str,
    receipt_raw: bytes,
    canonical: bytes,
    trace: list[dict],
) -> bytes:
    old = read_json(before)
    require(
        set(old) <= POLICY_KEYS and POLICY_REQUIRED <= set(old), "unknown/missing old policy fields"
    )
    require(
        type(old["schema_version"]) is int
        and old["schema_version"] == 1
        and old["policy_version"] == "owned-name-policy-v1",
        "unknown policy version",
    )
    hash_map(old["source_owner_sha256"])
    require(
        set(old["artifacts"]) == {SOURCE, SIDECAR, BASELINE}, "policy artifact membership differs"
    )
    history = old.get(UPDATE, [])
    require(isinstance(history, list), "invalid campaign history")
    result = deepcopy(old)
    result["artifacts"][SOURCE] = sha(canonical)
    result[UPDATE] = history + [
        {
            "schema_version": 1,
            "issue": ISSUE,
            "approval": APPROVAL,
            "plan_sha256": plan_sha,
            "owner_plan": plan["owner_plan"],
            "owner_receipt": plan["owner_receipt"],
            "prior_manifest_sha256": sha(before),
            "mapping_receipt": {"path": receipt_name, "sha256": sha(receipt_raw)},
            "generation": plan["generation"],
            "before_inventory": owner_proof["before_inventory"],
            "after_inventory": owner_proof["after_inventory"],
            "records": owner_proof["records"],
            "sssom_before_sha256": plan["before"]["canonical"]["sha256"],
            "sssom_after_sha256": sha(canonical),
            "trace_sha256": sha(encoded(trace)),
            "suppression_policy": "unchanged historical sidecar and baseline",
        }
    ]
    # Deliberately leave every historical owner attribution and old history untouched.
    return encoded(result)


def _verify_projected_rule_k(capture: Capture, canonical: bytes) -> None:
    """#1200: unchanged native ownership rule over all final rows, no exemptions added."""
    names = {
        name: path
        for name, path in _NATIVE_SOURCES.items()
        if name
        in {
            "mediaingredientmech.curate.publication_guard",
            "mediaingredientmech.synonym_policy",
            "campaign_native_sssom_invariants",
        }
    }
    original_path = list(sys.path)
    try:
        modules = _source_owner.captured_native_modules(capture.root, names)
    finally:
        sys.path[:] = original_path
    for name, module in modules.items():
        executed = module._campaign_executed_source
        require(
            executed.content == capture.files[capture.root / names[name]].content,
            "native Rule K producer changed before execution",
        )
        executed.verify()
    failures = list(
        modules["campaign_native_sssom_invariants"].evaluate_rule_k(table(canonical)[2])
    )
    require(
        not failures,
        "global projected Rule K impact requires reviewed scope: "
        + json.dumps(
            [
                {"source_position": position, "subject_id": row["subject_id"], "reason": reason}
                for position, row, reason in failures
            ],
            sort_keys=True,
        ),
    )


def prepare(root: Path, plan_path: Path, *, completed: bool = False) -> dict:
    capture = Capture(root)
    root = capture.root
    require(
        capture.read("src/mediaingredientmech/campaign_publication.py") == _LOADED,
        "loaded publication code differs",
    )
    require(
        plan_path.is_absolute() and plan_path.is_relative_to(root), "plan must be inside repository"
    )
    plan_raw = capture.external(plan_path)
    plan = closed(read_json(plan_raw), PLAN_KEYS, "publication plan")
    producers = hash_map(plan["publication_producers"])
    require(set(producers) == set(LOADED_PRODUCERS), "publication producer set differs")
    for path, loaded in LOADED_PRODUCERS.items():
        loaded.verify()
        require(sha(loaded.content) == producers[path], "loaded publication producer differs")
        capture.read(path, producers[path])

    def loaded_recheck() -> None:
        for loaded in LOADED_PRODUCERS.values():
            loaded.verify()

    capture.checks.append(loaded_recheck)
    require(
        type(plan["schema_version"]) is int
        and plan["schema_version"] == 1
        and plan["kind"] == "unmatched_campaign_publication_v1"
        and plan["issue"] == ISSUE
        and plan["approval"] == "NONE",
        "unsupported plan contract/approval",
    )
    require(
        isinstance(plan["batch"], str) and re.fullmatch(r"issue1174-[a-z0-9-]+", plan["batch"]),
        "invalid batch name",
    )
    require(isinstance(plan["scope"], str) and plan["scope"].strip(), "missing scope")
    for key in ("owner_plan", "owner_receipt"):
        capture.ref(plan[key])
    owner_proof = _owner_proof(root, plan)
    require(
        owner_proof["plan_sha256"] == plan["owner_plan"]["sha256"]
        and owner_proof["receipt_sha256"] == plan["owner_receipt"]["sha256"],
        "source application binding differs",
    )
    _capture_source_completion(capture, owner_proof)
    before_config = closed(
        plan["before"], {"canonical", "policy", "sidecar", "baseline"}, "beforeimages"
    )
    before = {key: capture.ref(ref) for key, ref in before_config.items()}
    actual = {
        key: capture.read(path)
        for key, path in (
            ("canonical", SOURCE),
            ("policy", POLICY),
            ("sidecar", SIDECAR),
            ("baseline", BASELINE),
        )
    }
    require(
        actual["sidecar"] == before["sidecar"] and actual["baseline"] == before["baseline"],
        "historical suppression sidecar/baseline changed",
    )
    if not completed:
        require(actual == before, "canonical/policy baseline differs")
    proof = native.verify_mapping_chain(root)
    prefix = hash_map(plan["receipt_prefix"])
    contexts = hash_map(plan["native_context"])
    require(set(contexts) == set(native.HISTORICAL_CONTEXT), "incomplete native historical context")
    require(
        owner_proof["checkpoint"]["input_sha256"]
        == {**prefix, **contexts, SOURCE: sha(before["canonical"])},
        "publication checkpoint differs from verified source application",
    )
    protected = owner_proof["protected_snapshot"]["input_sha256"]
    require(
        all(
            protected.get(path) == sha(before[key])
            for key, path in (("policy", POLICY), ("sidecar", SIDECAR), ("baseline", BASELINE))
        ),
        "policy beforeimages lack source-application protection",
    )
    for path, expected in {**prefix, **contexts}.items():
        capture.read(path, expected)
    receipt_name = native.RECEIPTS_DIR + "/" + plan["batch"] + ".json"
    require(receipt_name not in prefix, "receipt would overwrite prior history")
    if completed:
        require(
            set(proof["receipt_inputs"]) == set(prefix) | {receipt_name},
            "receipt inventory differs after publication",
        )
        previous = dict(proof)
        require(proof["receipt_paths"][-1] == receipt_name, "publication is not latest receipt")
        previous["receipts"] = proof["receipts"][:-1]
        previous["receipt_paths"] = proof["receipt_paths"][:-1]
        previous["receipt_inputs"] = prefix
        previous["owner_chains"] = native._owner_chains(
            previous["receipts"], proof["receipt_paths"][:-1], prefix
        )
    else:
        require(proof["receipt_inputs"] == prefix, "native receipt prefix differs")
        previous = proof
    require(
        all(proof["input_hashes"].get(p) == h for p, h in contexts.items())
        and all(proof["receipt_inputs"].get(p) == h for p, h in prefix.items()),
        "native history rewritten",
    )
    require(
        not previous["receipts"]
        or previous["receipts"][-1]["after_sha256"] == sha(before["canonical"]),
        "receipt checkpoint differs",
    )
    records = owner_proof["records"]
    require(
        records and len({r["source_record"] for r in records}) == len(records),
        "duplicate/empty applied source scope",
    )
    old_policy = read_json(before["policy"])
    require(
        old_policy["artifacts"]
        == {
            SOURCE: sha(before["canonical"]),
            SIDECAR: sha(before["sidecar"]),
            BASELINE: sha(before["baseline"]),
        },
        "old policy artifact bindings differ",
    )
    for record in records:
        old_path = record.get("before_source_record") or record["source_record"]
        old_hash = record["before_yaml_sha256"]
        historical = old_policy["source_owner_sha256"].get(old_path)
        if record["shape"] == "promotion":
            require(
                not any(
                    row["subject_id"] == subject(old_path) for row in table(before["canonical"])[2]
                ),
                "promotion old unmapped path already has canonical rows; explicit migration required",
            )
        if historical is not None and historical != old_hash:
            require(
                native.record_supersession(
                    previous, owner=old_path, reviewed_sha256=historical, current_sha256=old_hash
                ),
                "selected historical owner pin lacks native bridge",
            )
    candidate, diagnostic_sidecar, manifest = _generation(
        capture, plan, before["canonical"], owner_proof["after_inventory"]
    )
    require(
        manifest["source_revisions"]["mim"] == owner_proof["baseline_commit"],
        "generation revision differs from accepted source baseline",
    )
    selected = {subject(r["source_record"]) for r in records}

    def suppressions(raw):
        return list(csv.DictReader(io.StringIO(raw.decode()), delimiter="\t"))

    old_suppressed = {(r["subject_id"], r["token_key"]): r for r in suppressions(before["sidecar"])}
    needs = [
        r
        for r in suppressions(diagnostic_sidecar)
        if r["subject_id"] in selected
        and (
            (r["subject_id"], r["token_key"]) not in old_suppressed
            or r["owner_subject_ids"]
            != old_suppressed[(r["subject_id"], r["token_key"])]["owner_subject_ids"]
        )
    ]
    require(not needs, "new suppression review required: " + json.dumps(needs, sort_keys=True))
    canonical, trace = row_projection(before["canonical"], candidate, records, plan["rows"])
    _verify_projected_rule_k(capture, canonical)
    receipt = _receipt(previous, _maker(capture), plan, records, before["canonical"], canonical)
    receipt_raw = encoded(receipt)
    policy = _policy(
        before["policy"],
        plan,
        sha(plan_raw),
        owner_proof,
        receipt_name,
        receipt_raw,
        canonical,
        trace,
    )
    if completed:
        require(
            actual["canonical"] == canonical and actual["policy"] == policy,
            "published projection/policy differs",
        )
        require(capture.read(receipt_name) == receipt_raw, "published native receipt differs")
        require(proof["state"] == table(canonical)[2], "native completed replay differs")
    # Distinct file roles, no overlap between input snapshots and publication targets.
    immutable_refs = [plan_path] + [
        root / ref["path"]
        for ref in [
            *before_config.values(),
            plan["owner_plan"],
            plan["owner_receipt"],
            *[plan["generation"][k] for k in ("candidate", "sidecar", "manifest")],
        ]
    ]
    require(len(immutable_refs) == len(set(immutable_refs)), "input roles alias")
    require(
        not set(immutable_refs)
        & {root / SOURCE, root / POLICY, root / SIDECAR, root / BASELINE, root / receipt_name},
        "evidence aliases publication surface",
    )
    capture.verify()
    require(
        set(native._names(root)) == set(prefix) | ({receipt_name} if completed else set()),
        "native receipt membership changed during verification",
    )
    return {
        "capture": capture,
        "plan": plan,
        "plan_path": plan_path,
        "plan_sha256": sha(plan_raw),
        "owner_proof": owner_proof,
        "before": before,
        "canonical": canonical,
        "policy": policy,
        "receipt": receipt_raw,
        "receipt_name": receipt_name,
        "trace": trace,
        "generation_sha256": sha(
            capture.files[root / plan["generation"]["manifest"]["path"]].content
        ),
    }


def validate(root: Path, plan_path: Path) -> dict:
    prepared = prepare(root, plan_path, completed=True)
    return summary(prepared, "verified")


def summary(prepared: dict, status: str) -> dict:
    return {
        "schema_version": 1,
        "status": status,
        "approval": APPROVAL,
        "plan_sha256": prepared["plan_sha256"],
        "canonical_sha256": sha(prepared["canonical"]),
        "policy_sha256": sha(prepared["policy"]),
        "receipt_path": prepared["receipt_name"],
        "receipt_sha256": sha(prepared["receipt"]),
        "trace_sha256": sha(encoded(prepared["trace"])),
        "owner_count": len(prepared["owner_proof"]["records"]),
    }


@contextmanager
def _reserve(paths: tuple[Path, ...]):
    """Exclusively reserve via held parent descriptors, preserving native semantics.

    Every parent must already exist. A late path swap cannot redirect a new
    evidence file through a substituted directory. Cleanup removes only the
    entries created by this reservation, through their original descriptors.
    """
    parents = {p: (p.stat().st_dev, p.stat().st_ino) for path in paths for p in path.parents}
    created = []
    with ExitStack() as stack:
        descriptors = {}
        handles = []
        try:
            for path in paths:
                no_alias(path)
                parent = path.parent
                if parent not in descriptors:
                    fd = os.open(parent, os.O_RDONLY | os.O_DIRECTORY | os.O_NOFOLLOW)
                    stack.callback(os.close, fd)
                    require(
                        (os.fstat(fd).st_dev, os.fstat(fd).st_ino) == parents[parent],
                        "reservation parent changed",
                    )
                    descriptors[parent] = fd
                fd = os.open(
                    path.name,
                    os.O_CREAT | os.O_EXCL | os.O_RDWR | os.O_NOFOLLOW,
                    0o600,
                    dir_fd=descriptors[parent],
                )
                binary = path != paths[0]
                handle = stack.enter_context(os.fdopen(fd, "w+b" if binary else "w+"))
                info = os.fstat(handle.fileno())
                created.append((path, descriptors[parent], (info.st_dev, info.st_ino)))
                handles.append(handle)
                check_reserved(handle, path)
                for ancestor, identity in parents.items():
                    no_alias(ancestor)
                    require(
                        (ancestor.stat().st_dev, ancestor.stat().st_ino) == identity,
                        "reservation ancestor changed",
                    )
        except Exception:
            for path, fd, identity in created:
                try:
                    info = os.stat(path.name, dir_fd=fd, follow_symlinks=False)
                    if (info.st_dev, info.st_ino) == identity:
                        os.unlink(path.name, dir_fd=fd)
                except FileNotFoundError:
                    pass
            raise
        yield handles, parents


def publish(root: Path, plan_path: Path, receipt_dir: Path, *, apply: bool = False) -> dict:
    prepared = prepare(root, plan_path)
    capture: Capture = prepared["capture"]
    root = capture.root
    no_alias(receipt_dir)
    require(
        receipt_dir.is_absolute()
        and receipt_dir.is_relative_to(root / "reports")
        and receipt_dir.is_dir(),
        "receipt directory must be an existing unaliased report directory",
    )
    log = receipt_dir / "publication.json"
    backups = (receipt_dir / "canonical-before.tsv", receipt_dir / "policy-before.json")
    native_path = member(root, prepared["receipt_name"])
    outputs = (log, *backups, native_path)
    require(
        len(set(outputs)) == len(outputs) and not set(outputs) & set(capture.files),
        "output aliases input",
    )
    for path in outputs:
        no_alias(path)
        require(
            path.parent.is_dir() and not path.exists(), "output already exists or parent absent"
        )
    if not apply:
        return summary(prepared, "dry_run")
    destinations = {root / SOURCE: prepared["canonical"], root / POLICY: prepared["policy"]}
    current = {p: capture.files[p] for p in destinations}
    original_inventory = set(prepared["plan"]["receipt_prefix"])
    with _reserve(outputs) as (handles, parents):
        receipt_handle, canonical_backup, policy_backup, native_handle = handles
        all_handles = list(zip(outputs, handles, strict=True))
        native_written = False

        def recheck(skip: Path | None = None) -> None:
            capture.verify(set(destinations))
            require(
                _owner_proof(root, prepared["plan"]) == prepared["owner_proof"],
                "source application changed during publication",
            )
            require(
                set(native._names(root)) == original_inventory | {prepared["receipt_name"]},
                "receipt membership changed during publication",
            )
            for path, identity in parents.items():
                no_alias(path)
                require(
                    (path.stat().st_dev, path.stat().st_ino) == identity, "output parent changed"
                )
            for path, handle in all_handles:
                check_reserved(handle, path)
            for path, item in current.items():
                if path != skip:
                    item.verify()
            expected_native = prepared["receipt"] if native_written else b""
            require(native_path.read_bytes() == expected_native, "reserved native receipt changed")

        try:
            recheck()
            for handle, content in (
                (canonical_backup, prepared["before"]["canonical"]),
                (policy_backup, prepared["before"]["policy"]),
            ):
                handle.write(content)
                handle.flush()
            for target, content in destinations.items():
                current[target] = publish_validated(
                    current[target],
                    lambda staged, value=content: staged.write_bytes(value),
                    lambda p=target: recheck(p),
                )
                recheck()
            native_handle.write(prepared["receipt"])
            native_handle.flush()
            native_written = True
            recheck()
            result = validate(root, plan_path)
            require(
                result == summary(prepared, "verified"),
                "completed independent verification differs",
            )
            finish_receipt(receipt_handle, log, summary(prepared, "complete"), recheck)
            return summary(prepared, "complete")
        except Exception:
            # A partial attempt is evidence, never a success-shaped mapping link.
            for handle in (receipt_handle, native_handle):
                handle.seek(0)
                handle.truncate()
                handle.flush()
            raise
