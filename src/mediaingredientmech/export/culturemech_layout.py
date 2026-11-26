"""Lossless, in-memory layout of supplied CultureMech v3 cases (#1431).

This codec uses existing source-table cell names. It does not load a packet,
mint an identity, authorize a candidate, or perform native source conservation.
The caller must authenticate the complete input packet, its ordered source
tables, and the expected full-case hash separately. Historical ``candidate``
annotations are payload, never current scientific approval.

Dictionary entries are storage fragments, not assertions about their carrier
rows. The entire case and every original literal row remain reconstructible;
physical row order and case mention order are separate and both are retained.
"""

from __future__ import annotations

import csv
import json
import math
import re
from copy import deepcopy
from typing import Any, cast

from mediaingredientmech.review_claims import payload_sha256

# The unchanged native CSV reader default, measured in decoded characters.
# Refuse a process whose global reader budget has been temporarily raised by
# intake; never borrow its larger limit or change that process-wide setting.
NATIVE_CELL_CHARACTER_LIMIT = 131072
_DICTIONARIES = ("descriptors", "change_payloads", "held_payloads")
_COUNTS = ("positive_occurrences", "context_only_mentions", "held_source_mentions")
_CASE = {"case_id", "context", "source_mentions", "candidate", *_COUNTS, *_DICTIONARIES[:2]}
_CONTEXT = {
    "preferred_term",
    "resolved_identifier",
    "change_action",
    "change_stage",
    "descriptor_role",
    "variant_name",
}
_MENTION = {"product", "row", "row_sha256", "recipe_id", "source_path", "descriptor_path"}
_CANDIDATE = {"owners", "rejected_owners", "supported_canonical_rows", "classification"}
_OWNER = {"owner_record", "owner_record_sha256", "mim_identifier"}
_SUPPORTED_ROW = {"source_position", "row_sha256", "subject_id", "object_id"}
_HELD_PAYLOAD = {
    "source_label",
    "reported_action",
    "stage",
    "source_modification_index",
    "source_text",
    "reason",
    "held_fields",
    "reported_quantity",
    "evidence",
}
_HELD_PRODUCT = "variant_ingredient_holds.tsv"
_PRODUCTS = {"ingredient_occurrences.tsv", "variant_ingredient_changes.tsv", _HELD_PRODUCT}
_ADDED = {"source_product", "source_row", "case_id"}
_ORDINARY_FIELDS = set(
    "recipe_id recipe_label recipe_category source_path record_class component_field "
    "component_index preferred_term label_source resolved_identifier resolution_source "
    "local_identifier source_compound_id mim_preferred_term mim_matched_label mim_match_type "
    "mim_mapping_status mim_ambiguity mim_ontology_id_diagnostic grounding_reason "
    "concentration_value concentration_unit ingredient_json variant_index variant_name "
    "change_index change_action change_stage descriptor_role descriptor_path "
    "source_modification_index source_text evidence_json change_json counts_as_presence "
    "source_product source_row case_id".split()
)
_HELD_FIELDS = set(
    "recipe_id recipe_label recipe_category source_path variant_index variant_name "
    "mention_index descriptor_path source_label reported_action stage source_modification_index "
    "source_text reason reported_quantity held_fields_json evidence_json mention_json "
    "review_status counts_as_presence source_product source_row case_id".split()
)
_NODE = {
    "original_case_id",
    "original_case_without_occurrences_json",
    "original_case_sha256",
    "original_occurrence_count",
}
_CARRIER = {
    "original_case_id",
    "original_occurrence_position",
    "original_occurrence_json",
    "context_json",
}


def _require(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError("CultureMech v3 layout: " + message)


def _keys(value: Any, required: set[str], optional: set[str] | None = None) -> None:
    _require(type(value) is dict, "expected object")
    _require(required <= value.keys() <= required | (optional or set()), "unknown/missing fields")


def _json_value(value: Any) -> None:
    """Refuse Python-only values that JSON would silently coerce or discard."""
    if type(value) is dict:
        _require(all(type(key) is str for key in value), "non-string JSON key")
        for item in value.values():
            _json_value(item)
    elif type(value) is list:
        for item in value:
            _json_value(item)
    else:
        _require(type(value) in (str, int, float, bool, type(None)), "non-JSON value")
        _require(type(value) is not float or math.isfinite(value), "non-finite JSON number")


def _json(value: Any) -> str:
    try:
        _json_value(value)
        return json.dumps(
            value, sort_keys=True, separators=(",", ":"), ensure_ascii=False, allow_nan=False
        )
    except (RecursionError, UnicodeError) as exc:
        raise ValueError("CultureMech v3 layout: invalid JSON value") from exc


def _digest(value: Any) -> str:
    _require(
        type(value) is str and re.fullmatch(r"[0-9a-f]{64}", value) is not None, "invalid SHA256"
    )
    return cast(str, value)


def _reader_limit() -> int:
    _require(
        csv.field_size_limit() == NATIVE_CELL_CHARACTER_LIMIT,
        "native CSV reader character limit changed",
    )
    return NATIVE_CELL_CHARACTER_LIMIT


def _cell(value: str, label: str, limit: int) -> str:
    _require(type(value) is str, f"non-string cell: {label}")
    try:
        value.encode("utf-8")
    except UnicodeError as exc:
        raise ValueError(f"CultureMech v3 layout: invalid Unicode in {label}") from exc
    _require(len(value) <= limit, f"over-budget cell {label}: {len(value)} characters > {limit}")
    return value


def _unique(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    result = {}
    for key, value in pairs:
        _require(key not in result, f"duplicate JSON key: {key}")
        result[key] = value
    return result


def _parse(value: str, label: str, limit: int) -> dict[str, Any]:
    _cell(value, label, limit)
    try:
        result = json.loads(value, object_pairs_hook=_unique)
    except (json.JSONDecodeError, RecursionError) as exc:
        raise ValueError(f"CultureMech v3 layout: invalid JSON in {label}") from exc
    _require(type(result) is dict and _json(result) == value, f"noncanonical JSON in {label}")
    return cast(dict[str, Any], result)


def _positive_integer(value: Any) -> int:
    _require(type(value) is int and value > 0, "invalid positive integer")
    return cast(int, value)


def _position(value: Any) -> int:
    _require(
        type(value) is str and re.fullmatch(r"[1-9][0-9]*", value) is not None,
        "invalid position cell",
    )
    return int(value)


def _mention(value: Any) -> tuple[str, int]:
    _require(
        type(value) is dict and type(value.get("product")) is str and value["product"] in _PRODUCTS,
        "unknown mention product",
    )
    fields = (
        _MENTION
        if value["product"] == _HELD_PRODUCT
        else _MENTION
        | {
            "component_field",
            "component_index",
        }
    )
    _keys(value, fields)
    _require(all(type(value[key]) is str for key in fields - {"row"}), "mention string required")
    _digest(value["row_sha256"])
    return value["product"], _positive_integer(value["row"])


def _case(value: Any, *, envelope: bool = False) -> None:
    _keys(value, _CASE, {"held_payloads"})
    _json(value)  # Validate the complete tree, including opaque historical payloads.
    context = value["context"]
    _keys(context, _CONTEXT, {"held_fields"})
    _require(all(type(context[key]) is str for key in _CONTEXT), "context string required")
    if "held_fields" in context:
        _require(
            type(context["held_fields"]) is list
            and all(type(item) is str for item in context["held_fields"]),
            "held fields list required",
        )
    _require(_digest(value["case_id"]) == payload_sha256(context), "case/context hash differs")
    _require(type(value["source_mentions"]) is list, "source mentions list required")
    coordinates = [_mention(item) for item in value["source_mentions"]]
    _require(len(set(coordinates)) == len(coordinates), "repeated mention coordinate")
    for name in _COUNTS:
        _require(type(value[name]) is int and value[name] >= 0, "invalid literal count")
    if envelope:
        _require(not coordinates, "envelope has nonempty source mentions")
    else:
        _require(bool(coordinates), "case has no original occurrence carriers")
        _require(sum(value[name] for name in _COUNTS) == len(coordinates), "case count differs")
    for field in _DICTIONARIES:
        if field not in value:
            continue
        _require(type(value[field]) is dict, f"dictionary required: {field}")
        _require(not envelope or not value[field], f"envelope has nonempty dictionary: {field}")
        for key, item in value[field].items():
            _require(type(item) is dict, f"dictionary entry is not an object: {field}/{key}")
            _require(
                _digest(key) == payload_sha256(item),
                f"dictionary entry hash differs: {field}/{key}",
            )
            if field == "held_payloads":
                _require(item.keys() <= _HELD_PAYLOAD, "unknown held payload fields")
    candidate = value["candidate"]
    _keys(candidate, _CANDIDATE, _OWNER)
    _require(
        not (candidate.keys() & _OWNER) or _OWNER <= candidate.keys(), "partial owner annotation"
    )
    for field in ("owners", "rejected_owners"):
        _require(
            type(candidate[field]) is list and all(type(item) is str for item in candidate[field]),
            "candidate owners list required",
        )
    _require(type(candidate["classification"]) is str, "candidate classification string required")
    if "owner_record" in candidate:
        _require(
            all(type(candidate[key]) is str for key in _OWNER), "owner annotation string required"
        )
        _digest(candidate["owner_record_sha256"])
    _require(type(candidate["supported_canonical_rows"]) is list, "historical rows list required")
    for row in candidate["supported_canonical_rows"]:
        _keys(row, _SUPPORTED_ROW)
        _positive_integer(row["source_position"])
        _digest(row["row_sha256"])
        _require(
            type(row["subject_id"]) is str and type(row["object_id"]) is str,
            "historical row string required",
        )


def _row(row: Any, mention: dict[str, Any], case_id: str) -> None:
    held = mention["product"] == _HELD_PRODUCT
    _keys(row, _HELD_FIELDS if held else _ORDINARY_FIELDS)
    _require(
        all(type(value) is str for value in row.values()), "literal source cells must be strings"
    )
    _require(
        row["case_id"] == case_id
        and row["source_product"] == mention["product"]
        and _position(row["source_row"]) == mention["row"],
        "source row coordinate differs",
    )
    for key in ("recipe_id", "source_path", "descriptor_path") + (
        () if held else ("component_field", "component_index")
    ):
        _require(row[key] == mention[key], f"source row mention field differs: {key}")
    removed = _ADDED if held else _ADDED | {"counts_as_presence"}
    raw = {key: value for key, value in row.items() if key not in removed}
    _require(payload_sha256(raw) == mention["row_sha256"], "original source row hash differs")
    # Ordinary presence is an added cell, not part of the producer's row hash.
    # Bind it to the exact original product, without inferring identity approval.
    expected = "true" if mention["product"] == "ingredient_occurrences.tsv" else "false"
    _require(row["counts_as_presence"] == expected, "literal source presence differs")


def encode_case(
    case: dict[str, Any], source_rows: list[dict[str, str]], *, expected_case_sha256: str
) -> tuple[dict[str, str], list[dict[str, str]]]:
    """Return existing node cells and one carrier per exact supplied source row.

    ``source_rows`` must be the complete case subset in original physical table
    order. No case sorting or source ID/owner selection takes place here. The
    required external hash binds the complete case, not just its envelope.
    """
    limit = _reader_limit()
    _case(case)
    _require(
        payload_sha256(case) == _digest(expected_case_sha256), "expected full-case hash differs"
    )
    _require(type(source_rows) is list, "source rows list required")
    mentions = case["source_mentions"]
    positions = {_mention(item): index for index, item in enumerate(mentions)}
    contexts: list[dict[str, Any]] = [{"source_mentions": [deepcopy(item)]} for item in mentions]
    ordered: list[tuple[dict[str, str], int]] = []
    seen = set()
    for row in source_rows:
        _require(
            type(row) is dict and type(row.get("source_product")) is str, "source row required"
        )
        coordinate = (row["source_product"], _position(row.get("source_row")))
        _require(
            coordinate in positions and coordinate not in seen, "foreign/repeated source coordinate"
        )
        seen.add(coordinate)
        position = positions[coordinate]
        _row(row, mentions[position], case["case_id"])
        ordered.append((row, position))
    _require(len(seen) == len(positions), "missing source coordinates")
    envelope = deepcopy(case)
    envelope["source_mentions"] = []
    for field in _DICTIONARIES:
        if field in envelope:
            envelope[field] = {}
    node = {
        "original_case_id": case["case_id"],
        "original_case_without_occurrences_json": _json(envelope),
        "original_case_sha256": expected_case_sha256,
        "original_occurrence_count": str(len(mentions)),
    }
    for name, value in node.items():
        _cell(value, f"{case['case_id']}/{name}", limit)
    for context in contexts:
        _cell(_json(context), f"{case['case_id']}/source_mentions", limit)
    for field in _DICTIONARIES:
        for key, value in sorted(case.get(field, {}).items()):
            for context in contexts:
                attempt = deepcopy(context)
                attempt.setdefault(field, {})[key] = deepcopy(value)
                if len(_json(attempt)) <= limit:
                    context.clear()
                    context.update(attempt)
                    break
            else:
                size = len(_json({field: {key: value}}))
                raise ValueError(
                    f"CultureMech v3 layout: no carrier fits {case['case_id']}/{field}/{key} "
                    f"({size} fragment characters, limit {limit})"
                )
    carriers = []
    for row, position in ordered:
        carrier = {
            "original_case_id": case["case_id"],
            "original_occurrence_position": str(position + 1),
            "original_occurrence_json": _json(row),
            "context_json": _json(contexts[position]),
        }
        for name, value in carrier.items():
            _cell(value, f"{case['case_id']}/{position + 1}/{name}", limit)
        carriers.append(carrier)
    return node, carriers


def reconstruct_case(
    node: dict[str, str], carriers: list[dict[str, str]], *, expected_case_sha256: str
) -> tuple[dict[str, Any], list[dict[str, str]]]:
    """Invert only this layout; refuse loss, duplication, foreign rows and tampering.

    Returns the full case and complete literal source rows in carrier physical
    order. Matching the authenticated expected hash is data integrity only;
    native conservation and scientific reviews remain separate requirements.
    """
    limit = _reader_limit()
    _keys(node, _NODE)
    for name, value in node.items():
        _cell(value, name, limit)
    _require(
        _digest(node["original_case_sha256"]) == _digest(expected_case_sha256),
        "expected full-case hash differs",
    )
    case = _parse(node["original_case_without_occurrences_json"], "case envelope", limit)
    _case(case, envelope=True)
    _require(case["case_id"] == node["original_case_id"], "node case differs")
    count = _position(node["original_occurrence_count"])
    _require(type(carriers) is list and len(carriers) == count, "carrier count differs")
    mentions: dict[int, dict[str, Any]] = {}
    rows = []
    for carrier in carriers:
        _keys(carrier, _CARRIER)
        for name, value in carrier.items():
            _cell(value, name, limit)
        _require(carrier["original_case_id"] == case["case_id"], "foreign case carrier")
        position = _position(carrier["original_occurrence_position"])
        _require(position <= count and position not in mentions, "foreign/repeated list position")
        context = _parse(carrier["context_json"], "context", limit)
        _keys(context, {"source_mentions"}, set(_DICTIONARIES) & case.keys())
        _require(
            type(context["source_mentions"]) is list and len(context["source_mentions"]) == 1,
            "singleton source mention required",
        )
        mention = context["source_mentions"][0]
        _mention(mention)
        mentions[position] = mention
        for field in _DICTIONARIES:
            if field not in context:
                continue
            _require(
                type(context[field]) is dict and bool(context[field]), "empty/invalid fragment"
            )
            for key, value in context[field].items():
                _require(key not in case[field], f"repeated dictionary entry: {field}/{key}")
                case[field][key] = value
        row = _parse(carrier["original_occurrence_json"], "original row", limit)
        _row(row, mention, case["case_id"])
        rows.append(row)
    _require(set(mentions) == set(range(1, count + 1)), "missing list positions")
    case["source_mentions"] = [mentions[index] for index in range(1, count + 1)]
    _case(case)
    _require(payload_sha256(case) == expected_case_sha256, "reconstructed full-case hash differs")
    # Authenticate deterministic placement, not just the union of fragments.
    _require(
        encode_case(case, rows, expected_case_sha256=expected_case_sha256) == (node, carriers),
        "noncanonical fragment placement",
    )
    return case, rows
