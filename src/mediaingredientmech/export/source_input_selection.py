"""Authenticate the fixed CM/KGM source-only input profile (#1431).

The caller supplies captured bytes and a separately selected authority map.
This pure adapter preserves whole originals; it neither reads files nor grants
scientific approval. Native admission and the writer share these role joins.
"""

from __future__ import annotations

from collections import Counter
from copy import deepcopy
from pathlib import PurePosixPath
from typing import Any

from mediaingredientmech.export.source_conservation import (
    _canonical,
    _declaration,
    _json,
    _keys,
    _path,
    _pin,
    _read_table,
    _require,
    _sha,
)
from mediaingredientmech.review_claims import payload_sha256

PROFILE = "cm-v3-kgm-source-conservation-v1"
AUTHORITY_ROLES = frozenset(
    {
        "culturemech_package",
        "kg_source_selection",
        "kg_source_manifest",
        "kg_row_reconciliation",
        "kg_full_node_ledger",
        "kg_full_row_ledger_json",
        "kg_full_row_ledger_tsv",
        "kg_transport_manifest",
        "kg_nodes",
        "kg_occurrences",
        "original_case_ledger",
        "original_origin_ledger",
        "original_eligibility_intake",
    }
)
ARTIFACT_NAMES = {
    "cm_nodes": "cm-source-nodes.tsv",
    "cm_occurrences": "cm-source-occurrences.tsv",
    "cm_raw_row_map": "cm-raw-row-map.json",
    "cm_case_crosswalk": "cm-case-crosswalk.json",
    "combined_nodes": "source-nodes.tsv",
    "combined_occurrences": "source-occurrences.tsv",
    "combined_position_map": "combined-position-map.json",
    "cm_reconciliation": "cm-reconciliation.tsv",
    "kg_provider_cases": "kg-provider-cases.json",
    "historical_obligations": "historical-obligations.json",
    "obligation_crosswalk": "obligation-crosswalk.json",
}


def validate_scope(scope: dict[str, Any]) -> None:
    """Validate fixed role names, without treating a profile as authority."""
    _keys(scope, {"profile", "authorities", "artifacts"})
    _require(scope["profile"] == PROFILE, "unknown source-input profile")
    _keys(scope["authorities"], set(AUTHORITY_ROLES))
    _keys(scope["artifacts"], set(ARTIFACT_NAMES))
    paths = []
    for ref in scope["authorities"].values():
        _keys(ref, {"path", "sha256"})
        paths.append(_path(ref["path"]))
        _require(
            type(ref["sha256"]) is str
            and len(ref["sha256"]) == 64
            and all(c in "0123456789abcdef" for c in ref["sha256"]),
            "invalid authority digest",
        )
    paths.extend(_path(value) for value in scope["artifacts"].values())
    _require(len(set(paths)) == len(paths), "source profile paths overlap")


def _indexed(value: Any, key: str) -> dict[str, Any]:
    _require(type(value) is list, "original ledger must be a complete list")
    result = {}
    for item in value:
        _require(type(item) is dict, "original ledger entry is not an object")
        identifier = item.get(key)
        _require(
            type(identifier) is str and bool(identifier) and identifier not in result,
            "missing/duplicate original ledger ID",
        )
        result[identifier] = deepcopy(item)
    return result


def _metadata_counts(value: Any) -> None:
    """Counts are JSON integers, never bool/float equality aliases (#1553)."""
    _require(type(value) is dict, "metadata counts must be an object")
    _require(
        all(type(count) is int and count >= 0 for count in value.values()),
        "metadata counts must be nonnegative integers",
    )


def select_source_inputs(
    captured: dict[str, bytes],
    *,
    selected_scope: dict[str, Any],
    declaration: bytes,
    declaration_path: str,
    reviewed_crosswalk: bytes,
    curie_map: bytes,
) -> dict[str, Any]:
    """Bind complete originals to independently selected fixed-role authority.

    ``selected_scope`` must come from the separately reviewed execution/native
    selection, never by copying the candidate declaration. CM expected hashes
    come from accepted binding dispositions. KG hashes cover complete original
    cases whose raw ledger is pinned by the owner-selected transport manifest.
    Extra captured inputs may belong to native reports; ``consumed_inputs``
    lets the narrow writer require its own exact inventory without hiding them.
    """
    validate_scope(selected_scope)
    scope = deepcopy(selected_scope)
    consumed: dict[str, str] = {}
    refs = scope["authorities"]

    def read(path: str, digest: str, size: int | None = None) -> bytes:
        path = _path(path)
        _require(path in captured, "selected input missing: " + path)
        raw = _pin(captured[path], digest)
        _require(
            size is None or (type(size) is int and size >= 0 and len(raw) == size),
            "input size differs",
        )
        _require(path not in consumed or consumed[path] == digest, "conflicting input pins")
        consumed[path] = digest
        return raw

    def role(name: str) -> bytes:
        ref = refs[name]
        return read(ref["path"], ref["sha256"])

    def document(raw: bytes) -> Any:
        value = _json(raw.decode("utf-8"))
        _canonical(value)  # Validate JSON values without requiring original formatting.
        return value

    def linked(name: str, pin: dict[str, Any]) -> None:
        _require(type(pin) is dict, "missing authority link")
        raw = role(name)
        _require(pin.get("sha256") == refs[name]["sha256"], "independent authority differs")
        _require(
            type(pin.get("bytes")) is int and pin["bytes"] >= 0 and len(raw) == pin["bytes"],
            "authority size differs",
        )

    for name in AUTHORITY_ROLES:
        role(name)
    owner = document(role("kg_source_selection"))
    _require(type(owner) is dict, "owner selection is not an object")
    _metadata_counts(owner["row_counts"])
    _require(type(owner["provider_counts"]) is dict, "provider counts must be an object")
    for counts in owner["provider_counts"].values():
        _metadata_counts(counts)
    linked("kg_source_manifest", owner["source_receipt"])
    linked("kg_row_reconciliation", owner["row_reconciliation"])
    for name, filename in (
        ("kg_full_node_ledger", "full-node-ledger.json"),
        ("kg_full_row_ledger_json", "full-row-ledger.json"),
        ("kg_full_row_ledger_tsv", "full-row-ledger.tsv"),
    ):
        linked(name, owner["ledgers"][filename])
    intended = owner["intended_accepted_cm_v3"]
    _metadata_counts(intended["expected_counts"])
    linked("culturemech_package", intended["transport_package"])
    _require(
        refs["kg_transport_manifest"]["sha256"] == owner["kg_transport_manifest_sha256"],
        "owner-selected transport differs",
    )
    transport = document(role("kg_transport_manifest"))
    _metadata_counts(transport["counts"])
    for name, original in (
        ("original_case_ledger", "cases"),
        ("original_origin_ledger", "origins"),
        ("original_eligibility_intake", "accounting"),
    ):
        linked(name, transport["inputs"][original])
    for name, filename in (
        ("kg_nodes", "source-nodes.tsv"),
        ("kg_occurrences", "source-occurrences.tsv"),
    ):
        _require(refs[name]["sha256"] == transport["files"][filename], "KG family pin differs")

    package = document(role("culturemech_package"))
    _keys(
        package,
        {
            "schema_version",
            "status",
            "consumer_commit",
            "files",
            "intake_path",
            "intake_sha256",
            "review_path",
            "reviewed_path",
            "reviewed_sha256",
            "limitations",
        },
    )
    _require(
        type(package["schema_version"]) is int
        and package["schema_version"] == 1
        and package["status"] == "ISOLATED_REVIEWED_INTAKE_VERIFICATION_PACKAGE",
        "unsupported CM package",
    )
    package_root = PurePosixPath(refs["culturemech_package"]["path"]).parent

    def member(name: str, expected: str | None = None) -> tuple[str, bytes]:
        name = _path(name)
        pin = package["files"][name]
        _keys(pin, {"sha256", "bytes"})
        _require(expected is None or pin["sha256"] == expected, "CM package pin differs")
        path = (package_root / name).as_posix()
        return path, read(path, pin["sha256"], pin["bytes"])

    def cm_file(name: str, expected: str | None = None) -> tuple[str, bytes]:
        return member("consumer/" + _path(name), expected)

    prepared = _path(package["intake_path"])
    reviewed = _path(package["reviewed_path"])
    intake_path, intake_raw = cm_file(prepared + "/intake.json", package["intake_sha256"])
    final_path, final_raw = cm_file(reviewed + "/reviewed-intake.json", package["reviewed_sha256"])
    review_path, review_raw = cm_file(package["review_path"])
    intake, final = document(intake_raw), document(final_raw)
    _metadata_counts(intake["counts"])
    _metadata_counts(final["counts"])
    _require(
        intake["status"] == "PREPARED_PENDING_SOURCE_BINDING_REVIEW"
        and final["status"] == "REVIEWED_SOURCE_INTAKE"
        and intake["source_contract"]
        == final["source_contract"]
        == "culturemech-direct-ingredients-v3"
        and final["intake_sha256"] == _sha(intake_raw)
        and intake["source_manifest_sha256"] == final["source_manifest_sha256"],
        "CM prepared/reviewed binding differs",
    )
    source_path, source_raw = cm_file(
        prepared + "/source/bundle/manifest.json", intake["source_manifest_sha256"]
    )
    for name, raw in (
        ("source_manifest", source_raw),
        ("prepared_intake", intake_raw),
        ("reviewed_intake", final_raw),
        ("binding_review", review_raw),
    ):
        pin = intended["selected"][name]
        _require(
            pin["sha256"] == _sha(raw)
            and type(pin["bytes"]) is int
            and pin["bytes"] >= 0
            and pin["bytes"] == len(raw),
            "owner-selected CM metadata differs",
        )

    def artifact(prefix: str, manifest: dict[str, Any], name: str) -> tuple[str, bytes]:
        pin = manifest["files"][name]
        path, raw = cm_file(prefix + "/" + name, pin["sha256"])
        _require(
            type(pin["bytes"]) is int and pin["bytes"] >= 0 and len(raw) == pin["bytes"],
            "CM artifact size differs",
        )
        return path, raw

    _, packet_raw = artifact(prepared, intake, "review-packet.json")
    ordinary_path, ordinary = artifact(prepared, intake, "source-mentions.tsv")
    held_path, held = artifact(prepared, intake, "source-held-mentions.tsv")
    _, bindings = artifact(reviewed, final, "binding-dispositions.tsv")
    packet = document(packet_raw)
    _keys(packet, {"schema_version", "source_manifest_sha256", "canonical_review_sha256", "cases"})
    _require(
        type(packet["schema_version"]) is int
        and packet["schema_version"] == 1
        and packet["source_manifest_sha256"] == intake["source_manifest_sha256"]
        and packet["canonical_review_sha256"] == intake["canonical_review_sha256"],
        "CM packet provenance differs",
    )
    case_index = _indexed(packet["cases"], "case_id")
    _, rows = _read_table(bindings)
    hashes: dict[str, str] = {}
    dispositions: Counter[str] = Counter()
    for row in rows:
        identifier = row["case_id"]
        _require(
            identifier in case_index and identifier not in hashes,
            "binding case missing/foreign/repeated",
        )
        hashes[identifier] = row["payload_sha256"]
        _require(
            payload_sha256(case_index[identifier]) == hashes[identifier],
            "accepted case payload differs",
        )
        dispositions[row["disposition"]] += 1
    _require(
        set(hashes) == set(case_index) and len(hashes) == intake["counts"]["cases"],
        "CM full case membership differs",
    )
    _require(dict(dispositions) == final["counts"], "historical binding accounting differs")

    cases_raw, origins_raw = role("original_case_ledger"), role("original_origin_ledger")
    original_cases = document(cases_raw)
    historical = {
        "cases": _indexed(original_cases, "case_id"),
        "origins": _indexed(document(origins_raw), "origin_id"),
    }
    accounting = document(role("original_eligibility_intake"))
    _require(
        accounting["case_ledger"]["sha256"] == _sha(cases_raw)
        and set(_indexed(accounting["cases"], "case_id")) == set(historical["cases"])
        and set(_indexed(accounting["origins"], "origin_id")) == set(historical["origins"]),
        "original obligation accounting differs",
    )
    _require(
        len(historical["cases"]) == transport["counts"]["original_cases"]
        and len(historical["origins"]) == transport["counts"]["original_origins"],
        "original obligation denominator differs",
    )
    kg_cases = [deepcopy(case) for case in original_cases if case["source"] != "culturemech"]
    _require(
        all(case["source"] in owner["provider_counts"] for case in kg_cases),
        "unselected KG provider",
    )
    _require(
        len(kg_cases) == owner["row_counts"]["provider_cases"] == transport["counts"]["kg_cases"],
        "KG provider case denominator differs",
    )
    kg = {
        "cases": kg_cases,
        "case_hashes": {case["case_id"]: payload_sha256(case) for case in kg_cases},
    }
    for name in ("nodes", "occurrences"):
        kg[name] = role("kg_" + name)
        kg[name + "_sha256"] = refs["kg_" + name]["sha256"]
    cm = {
        "cases": deepcopy(packet["cases"]),
        "case_hashes": hashes,
        "ordinary": ordinary,
        "ordinary_sha256": _sha(ordinary),
        "ordinary_path": ordinary_path,
        "held": held,
        "held_sha256": _sha(held),
        "held_path": held_path,
        "declaration": declaration,
        "declaration_sha256": _sha(declaration),
        "declaration_path": _path(declaration_path),
        "selected_scope": scope,
    }
    _declaration(cm)
    artifacts = scope["artifacts"]
    return {
        "cm": cm,
        "kg": kg,
        "family_paths": {
            "cm_nodes": artifacts["cm_nodes"],
            "cm_occurrences": artifacts["cm_occurrences"],
            "kg_nodes": refs["kg_nodes"]["path"],
            "kg_occurrences": refs["kg_occurrences"]["path"],
        },
        "curie_map": document(curie_map),
        "historical_obligations": historical,
        "reviewed_crosswalk": document(reviewed_crosswalk),
        "consumed_inputs": consumed,
        "historical_dispositions_not_current_approval": dict(dispositions),
        "selected_metadata_paths": {
            "prepared_intake": intake_path,
            "reviewed_intake": final_path,
            "binding_review": review_path,
            "source_manifest": source_path,
        },
    }
