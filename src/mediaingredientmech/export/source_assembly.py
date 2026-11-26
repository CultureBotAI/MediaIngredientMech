"""Pure, source-only CM/KGM table construction (#1431).

No writer, native hook or scientific selection is provided. Callers supply
independently authenticated original bytes, hashes, declaration and historical
relations. Generated CM addresses denote immutable source scopes, not minted
ingredient IDs. Current owner decisions never enter construction.
"""

from __future__ import annotations

import csv
import io
from collections.abc import Sequence
from copy import deepcopy
from typing import Any

from mediaingredientmech.export import culturemech_layout as codec
from mediaingredientmech.export.source_conservation import (
    BRIDGE_FIELDS,
    DOMAIN,
    ID_ORIGIN,
    META,
    NODE_FIELDS,
    OCCURRENCE_FIELDS,
    _cell,
    _declaration,
    _family_paths,
    _historical,
    _keys,
    _namespaces,
    _read_table,
    _require,
    _selected_cm,
    _selected_kg,
    _sha,
    _source_id,
)
from mediaingredientmech.review_claims import payload_sha256


def render_tables(fields: Sequence[str], rows: list[dict[str, str]]) -> bytes:
    """Serialize only complete string rows under the unchanged reader budget."""
    _require(
        bool(fields) and len(set(fields)) == len(fields) and all(fields), "invalid table header"
    )
    for field in fields:
        _cell(field)
    for row in rows:
        _keys(row, set(fields))
        for value in row.values():
            _cell(value)
    stream = io.StringIO(newline="")
    writer = csv.DictWriter(stream, fieldnames=fields, delimiter="\t", lineterminator="\n")
    writer.writeheader()
    writer.writerows(rows)
    raw = stream.getvalue().encode("utf-8")
    header, parsed = _read_table(raw)
    _require(header == tuple(fields) and parsed == rows, "complete table roundtrip differs")
    return raw


def project_culturemech(cm: dict[str, Any]) -> dict[str, Any]:
    """Project all accepted cases without changing their literal source scope.

    The private Python argument keys are checked by ``_selected_cm``. Raw table
    pins, per-case hashes and ``selected_scope`` must come from the independently
    selected accepted package. This function does not acquire that authority.
    """
    cases, originals = _selected_cm(cm)
    declaration, declaration_path = _declaration(cm)
    per_case: dict[str, list[dict[str, str]]] = {case["case_id"]: [] for case in cases}
    for original in originals:
        per_case[original["row"]["case_id"]].append(original["row"])
    nodes, case_map, by_coordinate = [], [], {}
    for position, case in enumerate(cases):
        digest = cm["case_hashes"][case["case_id"]]
        node, uses = codec.encode_case(case, per_case[case["case_id"]], expected_case_sha256=digest)
        identifier = _source_id(case, digest, cm["declaration_sha256"])
        nodes.append(
            {
                "source_id": identifier,
                "source_label": case["context"]["preferred_term"],
                "id_origin": ID_ORIGIN,
                "projection_contract": DOMAIN,
                "original_case_position": str(position),
                "source_identity_claimed": "false",
                **node,
                "projection_declaration_json": declaration,
                "projection_declaration_sha256": cm["declaration_sha256"],
                "projection_declaration_path": declaration_path,
            }
        )
        case_map.append(
            {
                "source_position": position + 1,
                "source_id": identifier,
                "original_case_position": position,
                "original_case_id": case["case_id"],
                "original_case_sha256": digest,
            }
        )
        for original, carrier in zip(per_case[case["case_id"]], uses, strict=True):
            key = (original["source_product"], original["source_row"])
            _require(key not in by_coordinate, "repeated projected coordinate")
            by_coordinate[key] = {"source_id": identifier, **carrier}
    occurrences, raw_map = [], []
    for position, original in enumerate(originals, 1):
        row = original["row"]
        carrier = by_coordinate.pop((row["source_product"], row["source_row"]))
        occurrences.append(carrier)
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
    _require(not by_coordinate, "unemitted original CM coordinates")
    return {
        "nodes": render_tables(NODE_FIELDS, nodes),
        "occurrences": render_tables(OCCURRENCE_FIELDS, occurrences),
        "raw_row_map": raw_map,
        "case_crosswalk": case_map,
    }


def combine_sources(
    projection: dict[str, Any],
    *,
    cm: dict[str, Any],
    kg: dict[str, Any],
    family_paths: dict[str, str],
    curie_map: dict[str, str],
    historical_obligations: dict[str, Any],
    reviewed_crosswalk: dict[str, Any],
) -> dict[str, Any]:
    """Combine CM then selected KG without offsets, scientific joins or writes.

    The independent inverse must subsequently validate the complete returned
    candidate against the same independent originals. A construction result is
    neither a native conservation receipt nor permission to publish.
    """
    _keys(projection, {"nodes", "occurrences", "raw_row_map", "case_crosswalk"})
    _family_paths(family_paths)
    _, originals = _selected_cm(cm)
    kg_tables = _selected_kg(kg)
    result: dict[str, Any] = {
        "cm": deepcopy(projection),
        "position_map": [],
        "kg_provider_cases": deepcopy(kg["cases"]),
        "historical_obligations": deepcopy(historical_obligations),
        "obligation_crosswalk": deepcopy(reviewed_crosswalk),
    }
    tables: dict[str, list[dict[str, str]]] = {}
    for kind in ("nodes", "occurrences"):
        families = [
            ("cm", projection[kind], _read_table(projection[kind])),
            ("kg", kg[kind], kg_tables[kind]),
        ]
        fields: list[str] = []
        for family_name, _, (header, _) in families:
            if family_name == "cm":
                _require(
                    header == (NODE_FIELDS if kind == "nodes" else OCCURRENCE_FIELDS),
                    "CM projection headers differ",
                )
            _require(not set(META) & set(header), "family header occupies provenance columns")
            fields.extend(field for field in header if field not in fields)
        fields.extend(META)
        rows = []
        for name, raw, (_, original_rows) in families:
            path = family_paths[name + "_" + kind]
            for position, original in enumerate(original_rows, 1):
                rows.append(
                    {
                        **{key: original.get(key, "") for key in fields},
                        META[0]: path,
                        META[1]: str(position),
                        META[2]: _sha(raw),
                    }
                )
                result["position_map"].append(
                    {
                        "kind": kind,
                        "original_table": path,
                        "original_sha256": _sha(raw),
                        "original_position": position,
                        "native_position": len(rows),
                    }
                )
        result[kind] = render_tables(fields, rows)
        tables[kind] = rows
    _namespaces(tables["nodes"], curie_map)
    ids = {row["source_id"] for row in tables["nodes"]}
    _require(
        all(row["source_id"] in ids for row in tables["occurrences"]), "orphan source occurrence"
    )
    cm_occurrences = [
        (position, row)
        for position, row in enumerate(tables["occurrences"], 1)
        if row[META[0]] == family_paths["cm_occurrences"]
    ]
    _require(len(originals) == len(cm_occurrences), "CM bridge coverage differs")
    bridge = []
    for source_item, (position, carrier) in zip(originals, cm_occurrences, strict=True):
        row = source_item["row"]
        bridge.append(
            {
                "lane": source_item["lane"],
                "source_product": row["source_product"],
                "source_row": row["source_row"],
                "row_sha256": payload_sha256(row),
                "case_id": row["case_id"],
                "native_source_id": carrier["source_id"],
                "native_occurrence_position": str(position),
            }
        )
    result["reconciliation"] = render_tables(BRIDGE_FIELDS, bridge)
    _historical(historical_obligations, reviewed_crosswalk, tables["nodes"])
    return result
