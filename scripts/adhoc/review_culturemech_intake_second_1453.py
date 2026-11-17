#!/usr/bin/env python3
"""Display exact source-binding review packets for #1453, 2026-11-16.

Inputs: a pinned owner-partition summary and its pinned owner JSON files.
Output: a lossless view, or serialization of explicitly authored case decisions.
No inferred decisions, identity normalization, source edits or network calls.
The optional claims-only view explicitly omits occurrence-coordinate arrays;
it retains every owner, descriptor, concentration, change, hold and evidence field.
"""

import argparse
import copy
import difflib
import hashlib
import json
import re
from pathlib import Path


def canonical(value):
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False)


def read_pinned(path, expected):
    raw = path.read_bytes()
    if hashlib.sha256(raw).hexdigest() != expected:
        raise ValueError(f"Pinned input changed: {path.name}")
    return json.loads(raw)


def factor_payloads(payloads):
    """Factor exact common fields; reconstruct and compare every complete value."""
    if not payloads:
        return {"common": {}, "items": {}}
    if not all(isinstance(value, dict) for value in payloads.values()):
        raise ValueError("Payload must be a dictionary")
    values = list(payloads.values())
    common = {
        key: copy.deepcopy(value)
        for key, value in values[0].items()
        if all(key in item and canonical(item[key]) == canonical(value) for item in values)
    }
    items = {
        key: {field: value for field, value in payload.items() if field not in common}
        for key, payload in payloads.items()
    }
    reconstructed = {key: {**common, **item} for key, item in items.items()}
    if canonical(reconstructed) != canonical(payloads):
        raise ValueError("Factored view failed exact reconstruction")
    return {"common": common, "items": items}


def field_values(payloads):
    """Lossless transpose: each exact field value plus its descriptor indices."""
    keys = list(payloads)
    fields = {}
    for index, payload in enumerate(payloads.values()):
        for field, value in payload.items():
            encoded = canonical(value)
            group = fields.setdefault(field, {}).setdefault(
                encoded, {"value": value, "indices": []}
            )
            group["indices"].append(index)
    result = {
        "descriptor_keys": keys,
        "fields": {field: list(groups.values()) for field, groups in fields.items()},
    }
    reconstructed = {key: {} for key in keys}
    for field, groups in result["fields"].items():
        for group in groups:
            for index in group["indices"]:
                reconstructed[keys[index]][field] = group["value"]
    if canonical(reconstructed) != canonical(payloads):
        raise ValueError("Field-value view failed exact reconstruction")
    return result


def text_templates(value):
    """Factor repeated long text exactly; show every changed span without inference."""
    table, literals, known = {}, {}, {}

    def encode(item):
        if isinstance(item, dict):
            return {key: encode(child) for key, child in item.items()}
        if isinstance(item, list):
            return [encode(child) for child in item]
        if not isinstance(item, str) or len(item) < 120:
            return item
        if item in known:
            return {"$exact_text": known[item]}
        key = f"T{len(table):04d}"
        known[item] = key
        best = None
        item_tokens = re.findall(r"\w+|\s+|[^\w\s]", item)
        for base_key, base in literals.items():
            base_tokens = re.findall(r"\w+|\s+|[^\w\s]", base)
            matcher = difflib.SequenceMatcher(None, base_tokens, item_tokens, autojunk=False)
            if matcher.quick_ratio() < 0.65:
                continue
            offsets = [0]
            for token in base_tokens:
                offsets.append(offsets[-1] + len(token))
            edits = [
                {
                    "start": offsets[a],
                    "end": offsets[b],
                    "old": "".join(base_tokens[a:b]),
                    "new": "".join(item_tokens[c:d]),
                }
                for tag, a, b, c, d in matcher.get_opcodes()
                if tag != "equal"
            ]
            candidate = {"base": base_key, "edits": edits}
            if best is None or len(canonical(candidate)) < len(canonical(best)):
                best = candidate
        if best is not None and len(canonical(best)) < len(item) * 0.75:
            table[key] = best
        else:
            table[key] = {"literal": item}
            literals[key] = item
        return {"$exact_text": key}

    encoded = encode(value)

    def decode_text(key):
        entry = table[key]
        if "literal" in entry:
            return entry["literal"]
        base = literals[entry["base"]]
        result, cursor = [], 0
        for edit in entry["edits"]:
            if base[edit["start"] : edit["end"]] != edit["old"]:
                raise ValueError("Text edit does not match its literal base")
            result.extend((base[cursor : edit["start"]], edit["new"]))
            cursor = edit["end"]
        result.append(base[cursor:])
        return "".join(result)

    def decode(item):
        if isinstance(item, dict):
            if set(item) == {"$exact_text"}:
                return decode_text(item["$exact_text"])
            return {key: decode(child) for key, child in item.items()}
        if isinstance(item, list):
            return [decode(child) for child in item]
        return item

    if canonical(decode(encoded)) != canonical(value):
        raise ValueError("Text-template display failed exact reconstruction")
    return {
        "contract": "Every edit uses character offsets in its unchanged literal base; all old/new spans are shown. Exact reconstruction was verified. This is a display, not a scientific decision.",
        "text_table": table,
        "payload": encoded,
    }


def display_packet(packet, *, claims_only=False):
    result = copy.deepcopy(packet)
    for case in result["cases"]:
        for field in ("descriptors", "change_payloads", "held_payloads"):
            if field in case:
                case[field] = {"exact_factored_values": factor_payloads(case[field])}
        if claims_only:
            mentions = case.pop("source_mentions", [])
            case["occurrence_coordinate_display"] = {
                "status": "OMITTED_FROM_THIS_VIEW_ONLY",
                "count": len(mentions),
                "sha256_of_canonical_json": hashlib.sha256(
                    canonical(mentions).encode()
                ).hexdigest(),
                "note": "Complete coordinates remain in the pinned original owner packet.",
                "source_scope_signatures": factor_payloads(
                    {
                        hashlib.sha256(canonical(signature).encode()).hexdigest(): signature
                        for signature in (
                            {
                                key: value
                                for key, value in mention.items()
                                if key not in {"row", "row_sha256"}
                            }
                            for mention in mentions
                        )
                    }
                ),
            }
    result["display_contract"] = (
        "Every factored payload reconstructs exactly as common | items[original_sha256]. "
        "No source label, form, note, concentration, evidence, change or held field is removed. "
        + (
            "Occurrence coordinates are omitted from this claims-only view."
            if claims_only
            else "All occurrence coordinates are retained."
        )
    )
    return result


def serialize_annotations(partitions, summary_pin, annotations_path, output):
    """Bind explicit reviewer annotations; never choose a scientific disposition."""
    summary = read_pinned(partitions / "summary.json", summary_pin)
    raw = annotations_path.read_bytes()
    annotations = json.loads(raw)
    if annotations["intake_sha256"] != summary["intake_sha256"]:
        raise ValueError("Annotations belong to another intake")
    decisions, seen = [], set()
    for entry in annotations["entries"]:
        name = f"owner-{entry['owner_index']:04d}.json"
        packet = read_pinned(partitions / name, summary["files"][name]["sha256"])
        matches = [
            case for case in packet["cases"] if case["case_id"].startswith(entry["case_prefix"])
        ]
        if len(matches) != 1:
            raise ValueError("Authored case prefix is not unique")
        case = matches[0]
        if case["case_id"] in seen:
            raise ValueError("Repeated authored case")
        seen.add(case["case_id"])
        disposition = entry["disposition"]
        if disposition not in {"SUPPORTED", "WITHHOLD"} or not entry["review_reason"].strip():
            raise ValueError("Explicit scientific decision and reason required")
        all_read = entry.get("complete_scientific_payload_review") is True
        if disposition == "SUPPORTED" and not all_read:
            raise ValueError("Support requires explicit complete-payload review declaration")
        decision = {
            "case_id": case["case_id"],
            "row_sha256": packet["case_payload_sha256"][case["case_id"]],
            "disposition": disposition,
            "review_reason": entry["review_reason"],
            "evidence_locators": entry["evidence_locators"],
        }
        for kind, field in (
            ("descriptor", "descriptors"),
            ("change", "change_payloads"),
            ("held", "held_payloads"),
        ):
            members = case.get(field, {})
            inspected = list(members) if all_read else entry.get(f"inspected_{kind}_sha256", [])
            if not set(inspected) <= set(members):
                raise ValueError("Inspected hash is not a case member")
            decision[f"inspected_{kind}_sha256"] = inspected
        if disposition == "SUPPORTED":
            rows = case["candidate"]["supported_canonical_rows"]
            if len(rows) != 1:
                raise ValueError("Explicit row selection required for nonunique canonical rows")
            decision["canonical_row_sha256"] = rows[0]["row_sha256"]
        else:
            decision["blocking_witnesses"] = entry["blocking_witnesses"]
        decisions.append(decision)
    read_pinned(partitions / "summary.json", summary_pin)
    if annotations_path.read_bytes() != raw:
        raise ValueError("Authored annotations changed")
    result = {
        "intake_sha256": summary["intake_sha256"],
        "partition": annotations["partition"],
        "annotation_sha256": hashlib.sha256(raw).hexdigest(),
        "partition_summary_sha256": summary_pin,
        "decisions": decisions,
    }
    with output.open("x") as stream:
        stream.write(json.dumps(result, indent=2, sort_keys=True) + "\n")
    return result


def show(
    partitions,
    summary_pin,
    indices,
    *,
    claims_only=False,
    section="all",
    case_prefix="",
    start=0,
    limit=None,
):
    summary_path = partitions / "summary.json"
    summary = read_pinned(summary_path, summary_pin)
    for index in indices:
        name = f"owner-{index:04d}.json"
        if name not in summary["files"]:
            raise ValueError("Owner index is not present in the pinned partition")
        packet = read_pinned(partitions / name, summary["files"][name]["sha256"])
        if (
            packet["intake_sha256"] != summary["intake_sha256"]
            or packet["review_packet_sha256"] != summary["review_packet_sha256"]
        ):
            raise ValueError("Owner belongs to another intake")
        if case_prefix:
            packet["cases"] = [
                case for case in packet["cases"] if case["case_id"].startswith(case_prefix)
            ]
            if len(packet["cases"]) != 1:
                raise ValueError("Case prefix must select exactly one case")
        if section == "owner":
            rendered = {
                key: value
                for key, value in packet.items()
                if key not in {"cases", "case_payload_sha256"}
            }
        elif section == "scopes":
            rendered = {"owner_record": packet["owner_record"], "cases": []}
            for case in packet["cases"]:
                contexts = {}
                mentions = case["source_mentions"][start : None if limit is None else start + limit]
                for mention in mentions:
                    signature = {
                        key: value
                        for key, value in mention.items()
                        if key
                        not in {"row", "row_sha256", "recipe_id", "component_index", "source_path"}
                    }
                    contexts.setdefault(
                        canonical(signature), {"route": signature, "source_paths": set()}
                    )["source_paths"].add(mention["source_path"])
                rendered["cases"].append(
                    {
                        "case_id": case["case_id"],
                        "context": case["context"],
                        "total_mentions": len(case["source_mentions"]),
                        "display_start": start,
                        "display_count": len(mentions),
                        "source_scope_projection": [
                            {"route": value["route"], "source_paths": sorted(value["source_paths"])}
                            for value in contexts.values()
                        ],
                        "omitted": "Only repetitive row/hash/recipe-id/component-index coordinates; full originals remain pinned.",
                    }
                )
        elif section == "index":
            rendered = {
                "owner_record": packet["owner_record"],
                "owner_label": packet["owner_payload"].get("preferred_term"),
                "cases": [
                    {
                        "case_id": case["case_id"],
                        "context": case["context"],
                        "payload_sha256": packet["case_payload_sha256"][case["case_id"]],
                        "counts": {
                            field: len(case.get(field, {}))
                            for field in (
                                "descriptors",
                                "change_payloads",
                                "held_payloads",
                                "source_mentions",
                            )
                        },
                        "payload_bytes": {
                            field: len(canonical(case.get(field, {})).encode())
                            for field in ("descriptors", "change_payloads", "held_payloads")
                        },
                    }
                    for case in packet["cases"]
                ],
            }
        elif section in {
            "descriptors",
            "descriptor_values",
            "descriptor_templates",
            "change_payloads",
            "held_payloads",
        }:
            rendered = {"owner_record": packet["owner_record"], "cases": []}
            for case in packet["cases"]:
                source_field = (
                    "descriptors"
                    if section in {"descriptor_values", "descriptor_templates"}
                    else section
                )
                values = list(case.get(source_field, {}).items())
                selected = dict(values[start : None if limit is None else start + limit])
                rendered["cases"].append(
                    {
                        "case_id": case["case_id"],
                        "context": case["context"],
                        "total_payloads": len(values),
                        "display_start": start,
                        "display_count": len(selected),
                        section: text_templates(field_values(selected))
                        if section == "descriptor_templates"
                        else field_values(selected)
                        if section == "descriptor_values"
                        else factor_payloads(selected),
                    }
                )
        else:
            rendered = display_packet(packet, claims_only=claims_only)
        print(
            json.dumps(
                {"owner_index": index, **rendered},
                ensure_ascii=False,
                sort_keys=True,
                indent=2,
            )
        )
    read_pinned(summary_path, summary_pin)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--partitions", required=True, type=Path)
    parser.add_argument("--summary-sha256", required=True)
    parser.add_argument("--owner-index", type=int, action="append")
    parser.add_argument("--annotations", type=Path)
    parser.add_argument("--output", type=Path)
    parser.add_argument("--claims-only", action="store_true")
    parser.add_argument(
        "--section",
        choices=[
            "all",
            "owner",
            "index",
            "scopes",
            "descriptors",
            "descriptor_values",
            "descriptor_templates",
            "change_payloads",
            "held_payloads",
        ],
        default="all",
    )
    parser.add_argument("--case-prefix", default="")
    parser.add_argument("--start", type=int, default=0)
    parser.add_argument("--limit", type=int)
    args = parser.parse_args()
    if args.annotations:
        if not args.output:
            parser.error("--annotations requires --output")
        result = serialize_annotations(
            args.partitions, args.summary_sha256, args.annotations, args.output
        )
        print(json.dumps({"serialized_explicit_decisions": len(result["decisions"])}))
        return
    if not args.owner_index:
        parser.error("Display requires --owner-index")
    show(
        args.partitions,
        args.summary_sha256,
        args.owner_index,
        claims_only=args.claims_only,
        section=args.section,
        case_prefix=args.case_prefix,
        start=args.start,
        limit=args.limit,
    )


if __name__ == "__main__":
    main()
