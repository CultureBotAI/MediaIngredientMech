"""Pure inverse conservation for supplied CM/KGM source tables (#1431).

The caller independently authenticates the selected authority, original bytes,
case hashes and reviewed historical crosswalk. These in-memory arguments are
not a native request schema, a scientific review, or a substitute for capture.
No filesystem, native loader, owner selection or scientific approval occurs.
The inverse never calls the source assembler or trusts its accounting.
"""

from __future__ import annotations

import csv
import hashlib
import io
import json
import re
from collections import Counter
from pathlib import PurePosixPath
from typing import Any, cast

from mediaingredientmech.export import culturemech_layout as codec
from mediaingredientmech.review_claims import payload_sha256

DOMAIN = "mim-culturemech-material-reference-v1"
CM_PREFIX = "MIMCMREFv1"
CM_URI = (
    "https://culturebotai.github.io/MediaIngredientMech/source-material-reference/v1/culturemech/"
)
ID_ORIGIN = (
    "MIM-generated versioned complete-case material reference; "
    "not an upstream ID or permanent MIM allocation"
)
NODE_FIELDS = (
    "source_id",
    "source_label",
    "id_origin",
    "projection_contract",
    "original_case_position",
    "source_identity_claimed",
    "original_case_id",
    "original_case_without_occurrences_json",
    "original_case_sha256",
    "original_occurrence_count",
    "projection_declaration_json",
    "projection_declaration_sha256",
    "projection_declaration_path",
)
OCCURRENCE_FIELDS = (
    "source_id",
    "original_case_id",
    "original_occurrence_position",
    "original_occurrence_json",
    "context_json",
)
META = ("assembly_original_table", "assembly_original_position", "assembly_original_sha256")
BRIDGE_FIELDS = (
    "lane",
    "source_product",
    "source_row",
    "row_sha256",
    "case_id",
    "native_source_id",
    "native_occurrence_position",
)
_NODE_CODEC = (
    "original_case_id",
    "original_case_without_occurrences_json",
    "original_case_sha256",
    "original_occurrence_count",
)
_CARRIER_CODEC = OCCURRENCE_FIELDS[1:]
_CM_KEYS = {
    "cases",
    "case_hashes",
    "ordinary",
    "ordinary_sha256",
    "ordinary_path",
    "held",
    "held_sha256",
    "held_path",
    "declaration",
    "declaration_sha256",
    "declaration_path",
    "selected_scope",
}
_KG_KEYS = {"nodes", "nodes_sha256", "occurrences", "occurrences_sha256", "cases", "case_hashes"}


def _require(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError("Source conservation: " + message)


def _keys(value: Any, keys: set[str]) -> None:
    _require(type(value) is dict and set(value) == keys, "unexpected/missing object fields")


def _canonical(value: Any) -> str:
    # The reviewed codec refuses Python-only JSON coercions, nonfinite values
    # and surrogate strings; reuse its complete value check, not a second codec.
    return codec._json(value)


def _sha(raw: bytes) -> str:
    return hashlib.sha256(raw).hexdigest()


def _pin(raw: Any, digest: Any) -> bytes:
    _require(type(raw) is bytes, "original bytes required")
    _require(
        type(digest) is str and re.fullmatch(r"[0-9a-f]{64}", digest) is not None,
        "invalid independent SHA256",
    )
    _require(_sha(raw) == digest, "selected original bytes differ")
    return cast(bytes, raw)


def _path(value: Any) -> str:
    _require(
        type(value) is str and bool(value) and "\\" not in value and "\x00" not in value,
        "invalid root-relative path",
    )
    p = PurePosixPath(value)
    _require(
        not p.is_absolute() and ".." not in p.parts and p.as_posix() == value and value != ".",
        "invalid root-relative path",
    )
    return cast(str, value)


def _cell(value: Any) -> str:
    return codec._cell(value, "complete source table", codec._reader_limit())


def _read_table(raw: bytes) -> tuple[tuple[str, ...], list[dict[str, str]]]:
    _require(type(raw) is bytes, "TSV bytes required")
    codec._reader_limit()
    reader = csv.DictReader(io.StringIO(raw.decode("utf-8"), newline=""), delimiter="\t")
    fields = reader.fieldnames
    _require(
        bool(fields) and all(fields or []) and len(set(fields or [])) == len(fields or []),
        "invalid TSV header",
    )
    assert fields is not None
    for field in fields:
        _cell(field)
    rows = list(reader)
    for row in rows:
        _require(
            None not in row and all(value is not None for value in row.values()),
            "malformed TSV row",
        )
        for value in row.values():
            _cell(value)
    return tuple(fields), rows


def _json(raw: str) -> Any:
    return json.loads(raw, object_pairs_hook=codec._unique)


def _declaration(cm: dict[str, Any]) -> tuple[str, str]:
    raw = _pin(cm["declaration"], cm["declaration_sha256"])
    text = _cell(raw.decode("utf-8"))
    declaration = _json(text)
    _require(
        type(declaration) is dict and _canonical(declaration) == text,
        "declaration must be exact canonical JSON without newline",
    )
    _require(
        declaration.get("proposed_contract_version") == DOMAIN
        and declaration.get("proposed_curie_prefix") == CM_PREFIX
        and declaration.get("proposed_uri_base") == CM_URI,
        "declaration namespace differs",
    )
    _require(
        type(cm["selected_scope"]) is dict
        and _canonical(declaration.get("original_source_scope"))
        == _canonical(cm["selected_scope"]),
        "declaration differs from independent selected source authority",
    )
    return text, _path(cm["declaration_path"])


def _source_id(case: dict[str, Any], digest: str, declaration_sha: str) -> str:
    basis = {
        "domain": DOMAIN,
        "declaration_sha256": declaration_sha,
        "original_case_id": case["case_id"],
        "original_case_sha256": digest,
    }
    return CM_PREFIX + ":" + _sha(_canonical(basis).encode("utf-8"))


def _lane(row: dict[str, str], held: bool) -> str:
    _require(row.get("counts_as_presence") in {"true", "false"}, "invalid literal presence flag")
    if held:
        _require(
            row.get("review_status") == "WITHHELD" and row["counts_as_presence"] == "false",
            "held occurrence promoted",
        )
        return "held"
    lane = "positive_inventory" if row["counts_as_presence"] == "true" else "context_only"
    if row.get("change_action") == "REMOVE" or row.get("descriptor_role") == "replaced_ingredient":
        _require(lane == "context_only", "removed/displaced context promoted")
    return lane


def _selected_cm(cm: dict[str, Any]) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    _keys(cm, _CM_KEYS)
    _declaration(cm)
    cases, hashes = cm["cases"], cm["case_hashes"]
    _require(
        type(cases) is list and bool(cases) and type(hashes) is dict, "complete cases required"
    )
    ids = [case.get("case_id") for case in cases if type(case) is dict]
    _require(
        len(ids) == len(cases)
        and all(type(value) is str for value in ids)
        and len(set(ids)) == len(ids)
        and set(ids) == set(hashes),
        "case membership/hash inventory differs",
    )
    for case in cases:
        _require(payload_sha256(case) == hashes[case["case_id"]], "accepted full-case hash differs")
    originals, seen = [], set()
    paths = [_path(cm[name + "_path"]) for name in ("ordinary", "held")]
    _require(len(set(paths + [cm["declaration_path"]])) == 3, "selected CM paths overlap")
    for kind, path in zip(("ordinary", "held"), paths, strict=True):
        _, rows = _read_table(_pin(cm[kind], cm[kind + "_sha256"]))
        for position, row in enumerate(rows, 1):
            _require(
                {"source_product", "source_row", "case_id"} <= row.keys(), "CM coordinate missing"
            )
            coord = (row["source_product"], row["source_row"])
            _require(
                coord not in seen and row["case_id"] in hashes, "foreign/repeated CM coordinate"
            )
            seen.add(coord)
            originals.append(
                {
                    "path": path,
                    "sha256": cm[kind + "_sha256"],
                    "position": position,
                    "lane": _lane(row, kind == "held"),
                    "row": row,
                }
            )
    per_case = Counter((item["row"]["case_id"], item["lane"]) for item in originals)
    for case in cases:
        for lane, field in (
            ("positive_inventory", "positive_occurrences"),
            ("context_only", "context_only_mentions"),
            ("held", "held_source_mentions"),
        ):
            _require(
                type(case.get(field)) is int and case[field] == per_case[case["case_id"], lane],
                "accepted per-case lane count differs",
            )
    return cases, originals


def _selected_kg(kg: dict[str, Any]) -> dict[str, tuple[tuple[str, ...], list[dict[str, str]]]]:
    _keys(kg, _KG_KEYS)
    tables = {
        kind: _read_table(_pin(kg[kind], kg[kind + "_sha256"])) for kind in ("nodes", "occurrences")
    }
    nodes, occurrences = tables["nodes"][1], tables["occurrences"][1]
    _require(
        {"source_id", "source_label", "original_case_ids_json"} <= set(tables["nodes"][0])
        and {"source_id", "provider"} <= set(tables["occurrences"][0]),
        "KG columns incomplete",
    )
    ids = [row["source_id"] for row in nodes]
    _require(
        len(set(ids)) == len(ids) and all(not value.startswith(CM_PREFIX + ":") for value in ids),
        "KG source IDs duplicate or occupy CM namespace",
    )
    cases, hashes = kg["cases"], kg["case_hashes"]
    _require(type(cases) is list and type(hashes) is dict, "KG provider cases required")
    case_ids = [case.get("case_id") for case in cases if type(case) is dict]
    _require(
        len(case_ids) == len(cases)
        and all(type(value) is str for value in case_ids)
        and len(set(case_ids)) == len(case_ids)
        and set(case_ids) == set(hashes),
        "KG case membership differs",
    )
    by_id = {case["case_id"]: case for case in cases}
    covered, providers = set(), set()
    for case in cases:
        _require(
            payload_sha256(case) == hashes[case["case_id"]], "KG original provider payload differs"
        )
        _require(
            type(case.get("source")) is str
            and bool(case["source"])
            and case.get("source_case_id") in ids,
            "KG provider/source obligation differs",
        )
        providers.add((case["source_case_id"], case["source"]))
    for node in nodes:
        links = _json(node["original_case_ids_json"])
        _require(
            type(links) is list
            and all(type(key) is str for key in links)
            and len(set(links)) == len(links),
            "invalid original KG case links",
        )
        for key in links:
            _require(
                key in by_id
                and key not in covered
                and by_id[key]["source_case_id"] == node["source_id"],
                "KG original provider case lost/reused/misassigned",
            )
            covered.add(key)
    _require(covered == set(case_ids), "KG provider case omitted")
    _require(
        all((row["source_id"], row["provider"]) in providers for row in occurrences),
        "KG occurrence has no original provider obligation",
    )
    return tables


def _namespaces(nodes: list[dict[str, str]], prefixes: dict[str, str]) -> None:
    _require(type(prefixes) is dict and prefixes.get(CM_PREFIX) == CM_URI, "CM URI meaning differs")
    reserved = {
        "MIM": "https://culturebotai.github.io/MediaIngredientMech/ingredient/MIM_",
        "MIM.ingredient": "https://culturebotai.github.io/MediaIngredientMech/ingredient/MIM_",
        "skos": "http://www.w3.org/2004/02/skos/core#",
        "semapv": "https://w3id.org/semapv/vocab/",
        "mediadive.ingredient": "https://mediadive.dsmz.de/ingredient/",
        "kgmicrobe.compound": "https://w3id.org/kg-microbe/compound/",
    }
    for prefix, iri in prefixes.items():
        _require(
            type(prefix) is str
            and re.fullmatch(r"[^\s:]+", prefix) is not None
            and type(iri) is str
            and re.match(r"https?://|urn:", iri) is not None
            and not any(char.isspace() for char in iri),
            "invalid explicit namespace",
        )
        _require(prefix not in reserved or iri == reserved[prefix], "reserved URI meaning differs")
    seen, uris = set(), set()
    for node in nodes:
        value = node["source_id"]
        _require(re.fullmatch(r"[^\s:]+:[^\s]+", value) is not None, "invalid source CURIE")
        prefix, local = value.split(":", 1)
        _require(prefix in prefixes, "undeclared source prefix")
        uri = prefixes[prefix] + local
        _require(value not in seen and uri not in uris, "duplicate source CURIE/expanded URI")
        seen.add(value)
        uris.add(uri)


def _family_paths(paths: dict[str, str]) -> None:
    _keys(
        paths, {family + "_" + kind for family in ("cm", "kg") for kind in ("nodes", "occurrences")}
    )
    _require(len({_path(value) for value in paths.values()}) == 4, "family paths overlap")


def _historical(
    originals: dict[str, Any], crosswalk: dict[str, Any], nodes: list[dict[str, str]]
) -> None:
    _keys(originals, {"cases", "origins"})
    _keys(crosswalk, {"cases", "origins"})
    targets = {(row["source_id"], index) for index, row in enumerate(nodes, 1)}
    for group in ("cases", "origins"):
        _require(
            type(originals[group]) is dict
            and type(crosswalk[group]) is dict
            and set(originals[group]) == set(crosswalk[group]),
            "historical obligation key loss",
        )
        for key, payload in originals[group].items():
            _require(
                type(key) is str and bool(key) and type(payload) is dict,
                "invalid historical obligation",
            )
            entry = crosswalk[group][key]
            _keys(entry, {"original_sha256", "targets", "evidence", "unresolved_reason"})
            _require(
                entry["original_sha256"] == payload_sha256(payload), "historical payload differs"
            )
            _require(
                type(entry["targets"]) is list
                and type(entry["evidence"]) is list
                and all(type(item) is str and bool(item.strip()) for item in entry["evidence"])
                and type(entry["unresolved_reason"]) is str,
                "invalid supplied obligation relation",
            )
            _require(
                bool(entry["evidence"])
                and (entry["targets"] or entry["unresolved_reason"].strip()),
                "unexplained historical obligation",
            )
            seen = set()
            for target in entry["targets"]:
                _keys(target, {"source_id", "source_position"})
                _require(
                    type(target["source_id"]) is str and type(target["source_position"]) is int,
                    "invalid obligation target",
                )
                pair = (target["source_id"], target["source_position"])
                _require(pair in targets and pair not in seen, "foreign/repeated obligation target")
                seen.add(pair)


def validate_source_conservation(
    candidate: dict[str, Any],
    *,
    cm: dict[str, Any],
    kg: dict[str, Any],
    family_paths: dict[str, str],
    curie_map: dict[str, str],
    historical_obligations: dict[str, Any],
    reviewed_crosswalk: dict[str, Any],
) -> dict[str, Any]:
    """Invert actual candidate rows against independently authenticated originals.

    ``cm`` and ``kg`` hold selected raw bytes and independent expected hashes;
    their parsed cases retain complete historical payloads. ``selected_scope``
    is supplied by the authority selector, never copied out of the candidate.
    ``reviewed_crosswalk`` is external exact evidence, not selected by this code.
    The return value is data accounting only, with no native/scientific verdict.
    """
    _keys(
        candidate,
        {
            "cm",
            "nodes",
            "occurrences",
            "position_map",
            "reconciliation",
            "kg_provider_cases",
            "historical_obligations",
            "obligation_crosswalk",
        },
    )
    projection = candidate["cm"]
    _keys(projection, {"nodes", "occurrences", "raw_row_map", "case_crosswalk"})
    _family_paths(family_paths)
    cases, originals = _selected_cm(cm)
    kg_tables = _selected_kg(kg)
    cm_nodes_header, cm_nodes = _read_table(projection["nodes"])
    cm_occ_header, cm_occurrences = _read_table(projection["occurrences"])
    _require(
        cm_nodes_header == NODE_FIELDS and cm_occ_header == OCCURRENCE_FIELDS,
        "CM projection headers differ",
    )
    _require(
        len(cm_nodes) == len(cases) and len(cm_occurrences) == len(originals), "CM coverage differs"
    )
    declaration, path = _declaration(cm)
    grouped: dict[str, list[dict[str, str]]] = {}
    for row in cm_occurrences:
        grouped.setdefault(row["source_id"], []).append(
            {name: row[name] for name in _CARRIER_CODEC}
        )
    case_crosswalk, restored_rows = [], {}
    for index, (case, node) in enumerate(zip(cases, cm_nodes, strict=True)):
        digest = cm["case_hashes"][case["case_id"]]
        identifier = _source_id(case, digest, cm["declaration_sha256"])
        expected = {
            "source_id": identifier,
            "source_label": case["context"]["preferred_term"],
            "id_origin": ID_ORIGIN,
            "projection_contract": DOMAIN,
            "original_case_position": str(index),
            "source_identity_claimed": "false",
            "projection_declaration_json": declaration,
            "projection_declaration_sha256": cm["declaration_sha256"],
            "projection_declaration_path": path,
        }
        _require(all(node[key] == value for key, value in expected.items()), "full CM node differs")
        decoded, rows = codec.reconstruct_case(
            {key: node[key] for key in _NODE_CODEC},
            grouped.pop(identifier, []),
            expected_case_sha256=digest,
        )
        _require(_canonical(decoded) == _canonical(case), "complete accepted case differs")
        for row in rows:
            coordinate = (row["source_product"], row["source_row"])
            _require(coordinate not in restored_rows, "reused reconstructed coordinate")
            restored_rows[coordinate] = row
        case_crosswalk.append(
            {
                "source_position": index + 1,
                "source_id": identifier,
                "original_case_position": index,
                "original_case_id": case["case_id"],
                "original_case_sha256": digest,
            }
        )
    _require(not grouped and len(restored_rows) == len(originals), "foreign/missing CM carriers")
    raw_map = []
    for position, (original, carrier) in enumerate(zip(originals, cm_occurrences, strict=True), 1):
        row = original["row"]
        _require(
            _json(carrier["original_occurrence_json"]) == row
            and restored_rows.get((row["source_product"], row["source_row"])) == row,
            "CM literal rows or physical order differ",
        )
        raw_map.append(
            {
                "original_table": original["path"],
                "original_sha256": original["sha256"],
                "original_position": original["position"],
                "source_product": row["source_product"],
                "source_row": row["source_row"],
                "case_id": row["case_id"],
                "source_id": carrier["source_id"],
                "cm_occurrence_position": position,
            }
        )
    _require(
        _canonical(projection["raw_row_map"]) == _canonical(raw_map)
        and _canonical(projection["case_crosswalk"]) == _canonical(case_crosswalk),
        "CM raw/case position map differs",
    )
    position_map, actual = [], {}
    for kind in ("nodes", "occurrences"):
        family = [
            ("cm", projection[kind], _read_table(projection[kind])),
            ("kg", kg[kind], kg_tables[kind]),
        ]
        fields: list[str] = []
        for _, _, (header, _) in family:
            _require(not set(META) & set(header), "family header occupies provenance columns")
            fields.extend(field for field in header if field not in fields)
        fields.extend(META)
        header, rows = _read_table(candidate[kind])
        _require(tuple(fields) == header, "ordered-union header differs")
        expected_length = sum(len(table[1]) for _, _, table in family)
        _require(len(rows) == expected_length, "combined row coverage differs")
        cursor = 0
        for name, raw, (original_header, original_rows) in family:
            table_path = family_paths[name + "_" + kind]
            for position, original in enumerate(original_rows, 1):
                row = rows[cursor]
                cursor += 1
                _require(
                    row[META[0]] == table_path
                    and row[META[1]] == str(position)
                    and row[META[2]] == _sha(raw),
                    "family provenance/order differs",
                )
                _require(
                    {key: row[key] for key in original_header} == original
                    and all(
                        row[key] == ""
                        for key in fields
                        if key not in original_header and key not in META
                    ),
                    "inverse original cell/padding differs",
                )
                position_map.append(
                    {
                        "kind": kind,
                        "original_table": table_path,
                        "original_sha256": _sha(raw),
                        "original_position": position,
                        "native_position": cursor,
                    }
                )
        actual[kind] = rows
    _require(
        _canonical(candidate["position_map"]) == _canonical(position_map),
        "actual emitted position map differs",
    )
    _namespaces(actual["nodes"], curie_map)
    ids = {row["source_id"] for row in actual["nodes"]}
    _require(
        all(row["source_id"] in ids for row in actual["occurrences"]), "orphan source occurrence"
    )
    bridge = []
    native_cm = [
        (position, row)
        for position, row in enumerate(actual["occurrences"], 1)
        if row[META[0]] == family_paths["cm_occurrences"]
    ]
    for original, (position, row) in zip(originals, native_cm, strict=True):
        value = original["row"]
        bridge.append(
            {
                "lane": original["lane"],
                "source_product": value["source_product"],
                "source_row": value["source_row"],
                "row_sha256": payload_sha256(value),
                "case_id": value["case_id"],
                "native_source_id": row["source_id"],
                "native_occurrence_position": str(position),
            }
        )
    header, rows = _read_table(candidate["reconciliation"])
    _require(header == BRIDGE_FIELDS and rows == bridge, "literal CM reconciliation bridge differs")
    _require(
        _canonical(candidate["kg_provider_cases"]) == _canonical(kg["cases"]),
        "KG provider payload lost",
    )
    _require(
        _canonical(candidate["historical_obligations"]) == _canonical(historical_obligations)
        and _canonical(candidate["obligation_crosswalk"]) == _canonical(reviewed_crosswalk),
        "independent historical obligation/crosswalk differs",
    )
    _historical(historical_obligations, reviewed_crosswalk, actual["nodes"])
    return {
        "source_only": True,
        "scientific_approval": False,
        "native_conservation": False,
        "cm_cases": len(cases),
        "cm_lanes": dict(Counter(item["lane"] for item in originals)),
        "kg_nodes": len(kg_tables["nodes"][1]),
        "kg_provider_cases": len(kg["cases"]),
        "kg_occurrences": len(kg_tables["occurrences"][1]),
        "kg_provider_occurrences": dict(
            Counter(row["provider"] for row in kg_tables["occurrences"][1])
        ),
        "nodes": len(actual["nodes"]),
        "occurrences": len(actual["occurrences"]),
        "historical_cases": len(historical_obligations["cases"]),
        "historical_origins": len(historical_obligations["origins"]),
    }
