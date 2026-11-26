"""Synthetic, data-only CM v3 codec regressions for #1431; no native execution."""

from __future__ import annotations

import csv
import io
import json
from copy import deepcopy

import pytest

from mediaingredientmech.export import culturemech_layout as codec
from mediaingredientmech.review_claims import payload_sha256


def canonical(value):
    return json.dumps(
        value, sort_keys=True, separators=(",", ":"), ensure_ascii=False, allow_nan=False
    )


def fixture_case(*, held=False, context_only=False, count=3):
    """Literal producer-shaped data, not an actual packet or scientific report."""
    context = {
        "preferred_term": "synthetic supplied material",
        "resolved_identifier": "",
        "change_action": "REMOVE" if context_only else "",
        "change_stage": "EXPERIMENTAL" if context_only else "",
        "descriptor_role": "ingredient" if context_only else "",
        "variant_name": "",
    }
    if held:
        context.update(descriptor_role="held_mention", held_fields=["OPERATION", "QUANTITY"])
    case_id = payload_sha256(context)
    # Keep source cells and raw header shape independent of the module constants.
    ordinary_fields = (
        "recipe_id recipe_label recipe_category source_path record_class component_field "
        "component_index preferred_term label_source resolved_identifier resolution_source "
        "local_identifier source_compound_id mim_preferred_term mim_matched_label mim_match_type "
        "mim_mapping_status mim_ambiguity mim_ontology_id_diagnostic grounding_reason "
        "concentration_value concentration_unit ingredient_json variant_index variant_name "
        "change_index change_action change_stage descriptor_role descriptor_path "
        "source_modification_index source_text evidence_json change_json"
    ).split()
    held_fields = (
        "recipe_id recipe_label recipe_category source_path variant_index variant_name "
        "mention_index descriptor_path source_label reported_action stage source_modification_index "
        "source_text reason reported_quantity held_fields_json evidence_json mention_json "
        "review_status counts_as_presence"
    ).split()
    product = (
        "variant_ingredient_holds.tsv"
        if held
        else ("variant_ingredient_changes.tsv" if context_only else "ingredient_occurrences.tsv")
    )
    rows, mentions = [], []
    descriptor = {
        "preferred_term": "literal\tlabel\nµ",
        "zero": 0,
        "empty": "",
        "literal": "0",
        "list": ["a", "a", "b"],
        "null": None,
        "flag": False,
    }
    change = {
        "action": "REMOVE",
        "source_text": "retain this exact string",
        "amount": {
            "value": "0",
            "unit": "ML",
            "basis": "PER_BATCH",
            "basis_statement": "literal, no conversion",
        },
    }
    held_payload = {
        "source_label": "synthetic supplied material",
        "reported_action": "UNSPECIFIED",
        "stage": "EXPERIMENTAL",
        "source_text": "synthetic supplied material ?",
        "source_modification_index": 0,
        "reported_quantity": "0",
        "reason": "source operation and quantity not resolved",
        "held_fields": ["OPERATION", "QUANTITY"],
        "evidence": [],
    }
    for index in range(count):
        raw = dict.fromkeys(held_fields if held else ordinary_fields, "")
        raw.update(
            recipe_id="CM:SYNTHETIC",
            source_path="synthetic/recipe.yaml",
            descriptor_path=f"/ingredients/{index}",
            source_text="literal\ttext\nµ",
        )
        if held:
            raw.update(
                mention_json=json.dumps(held_payload, ensure_ascii=False),
                held_fields_json='["OPERATION", "QUANTITY"]',
                review_status="WITHHELD",
                counts_as_presence="false",
                reported_quantity="0",
            )
        else:
            raw.update(
                component_field="ingredients",
                component_index=str(index),
                ingredient_json=json.dumps(descriptor, ensure_ascii=False),
                change_json=json.dumps(change),
                concentration_value="0",
            )
        mention = {
            "product": product,
            "row": index + 7,
            "row_sha256": payload_sha256(raw),
            "recipe_id": raw["recipe_id"],
            "source_path": raw["source_path"],
            "descriptor_path": raw["descriptor_path"],
        }
        if not held:
            mention.update(
                component_field=raw["component_field"], component_index=raw["component_index"]
            )
        mentions.append(mention)
        rows.append(
            {
                **raw,
                "counts_as_presence": "false" if held or context_only else "true",
                "source_product": product,
                "source_row": str(index + 7),
                "case_id": case_id,
            }
        )
    case = {
        "case_id": case_id,
        "context": context,
        "source_mentions": mentions,
        "descriptors": {} if held else {payload_sha256(descriptor): descriptor},
        "change_payloads": {} if held else {payload_sha256(change): change},
        "positive_occurrences": count if not held and not context_only else 0,
        "context_only_mentions": count if context_only and not held else 0,
        "held_source_mentions": count if held else 0,
        "candidate": {
            "owners": ["data/ingredients/unmapped/synthetic.yaml"],
            "rejected_owners": ["data/ingredients/unmapped/retired.yaml"],
            "supported_canonical_rows": [
                {
                    "source_position": 2,
                    "row_sha256": "b" * 64,
                    "subject_id": "MIM:historical",
                    "object_id": "cas:0",
                }
            ],
            "classification": "HISTORICAL_ONLY",
            "owner_record": "synthetic.yaml",
            "owner_record_sha256": "a" * 64,
            "mim_identifier": "kgmicrobe.ingredient:literal",
        },
    }
    if held:
        case["held_payloads"] = {payload_sha256(held_payload): held_payload}
    return case, rows


def encode(case, rows):
    return codec.encode_case(case, rows, expected_case_sha256=payload_sha256(case))


def decode(case, node, carriers):
    return codec.reconstruct_case(node, carriers, expected_case_sha256=payload_sha256(case))


def change_context(carrier, mutate):
    context = json.loads(carrier["context_json"])
    mutate(context)
    carrier["context_json"] = canonical(context)


@pytest.mark.parametrize("options", [{}, {"context_only": True}, {"held": True}])
def test_roundtrip_retains_full_case_rows_and_both_orders(options):
    case, rows = fixture_case(**options)
    rows.reverse()  # Physical source order is independent of source_mentions order.
    before = deepcopy((case, rows))
    node, carriers = encode(case, rows)
    restored, restored_rows = decode(case, node, carriers)
    assert (restored, restored_rows) == before
    assert (case, rows) == before
    assert restored.keys() == case.keys()
    assert [item["original_occurrence_position"] for item in carriers] == ["3", "2", "1"]
    assert restored["candidate"] == case["candidate"]
    assert node["original_case_sha256"] == payload_sha256(case)
    assert payload_sha256(
        json.loads(node["original_case_without_occurrences_json"])
    ) != payload_sha256(case)
    assert len(carriers) == len(rows)
    # Results are independent objects: caller mutation cannot alter the input.
    restored["candidate"]["owners"].append("changed outside codec")
    restored_rows[0]["source_text"] = "changed outside codec"
    assert (case, rows) == before


@pytest.mark.parametrize("held_key", [False, True])
def test_absent_and_empty_dictionary_presence_is_exact(held_key):
    case, rows = fixture_case()
    case["descriptors"] = {}
    case["change_payloads"] = {}
    if held_key:
        case["held_payloads"] = {}
    node, carriers = encode(case, rows)
    restored, _ = decode(case, node, carriers)
    assert ("held_payloads" in restored) is held_key
    assert restored["descriptors"] == restored["change_payloads"] == {}
    assert all(set(json.loads(item["context_json"])) == {"source_mentions"} for item in carriers)


def test_literal_zero_empty_types_lists_and_typed_holds_are_not_normalized():
    case, rows = fixture_case()
    restored, literal = decode(case, *encode(case, rows))
    value = next(iter(restored["descriptors"].values()))
    assert (value["zero"], value["empty"], value["literal"], value["null"], value["flag"]) == (
        0,
        "",
        "0",
        None,
        False,
    )
    assert type(value["zero"]) is int and type(value["flag"]) is bool
    assert value["list"] == ["a", "a", "b"]
    assert literal[0]["concentration_value"] == "0"
    held_case, held_rows = fixture_case(held=True)
    restored, literal = decode(held_case, *encode(held_case, held_rows))
    assert restored["context"]["held_fields"] == ["OPERATION", "QUANTITY"]
    assert next(iter(restored["held_payloads"].values()))["reported_quantity"] == "0"
    assert all(
        row["counts_as_presence"] == "false" and row["review_status"] == "WITHHELD"
        for row in literal
    )


def test_dictionary_key_order_does_not_change_first_fit_placement():
    case, rows = fixture_case()
    entries = [{"value": "a" * 70000}, {"value": "b" * 70000}, {"value": "c" * 70000}]
    case["descriptors"] = {payload_sha256(item): item for item in entries}
    first = encode(case, rows)
    case["descriptors"] = dict(reversed(list(case["descriptors"].items())))
    second = encode(case, rows)
    assert first == second
    assert decode(case, *second) == (case, rows)
    fragments = [json.loads(item["context_json"]) for item in second[1]]
    keys = [list(item["descriptors"]) for item in fragments]
    assert keys == [[key] for key in sorted(case["descriptors"])]
    # Fixed dictionary order puts the later small change on the first available carrier.
    assert "change_payloads" in fragments[0]


def test_unicode_limit_is_characters_not_utf8_bytes_and_native_reader_agrees():
    case, rows = fixture_case(count=1)
    value = {"text": "µ" * 70000}
    case["descriptors"] = {payload_sha256(value): value}
    node, carriers = encode(case, rows)
    cell = carriers[0]["context_json"]
    assert len(cell) < 131072 < len(cell.encode("utf-8"))
    stream = io.StringIO(newline="")
    writer = csv.writer(stream, delimiter="\t")
    writer.writerow([cell])
    stream.seek(0)
    assert next(csv.reader(stream, delimiter="\t")) == [cell]
    assert decode(case, node, carriers) == (case, rows)
    assert csv.field_size_limit() == 131072


def test_exact_native_character_ceiling_accepts_and_one_more_refuses():
    case, rows = fixture_case(count=1)
    case["change_payloads"] = {}
    value = {"text": ""}
    case["descriptors"] = {payload_sha256(value): value}
    _, carriers = encode(case, rows)
    value["text"] = "x" * (131072 - len(carriers[0]["context_json"]))
    case["descriptors"] = {payload_sha256(value): value}
    node, carriers = encode(case, rows)
    assert len(carriers[0]["context_json"]) == 131072
    assert decode(case, node, carriers) == (case, rows)
    value["text"] += "x"
    case["descriptors"] = {payload_sha256(value): value}
    with pytest.raises(ValueError, match="no carrier fits"):
        encode(case, rows)


@pytest.mark.parametrize("location", ["envelope", "row", "entry", "capacity"])
def test_oversize_cells_and_indivisible_entries_refuse_without_input_change(location):
    case, rows = fixture_case(count=1)
    if location == "envelope":
        case["candidate"]["classification"] = "x" * 131072
    elif location == "row":
        rows[0]["source_text"] = "x" * 131072
        raw = {
            key: value
            for key, value in rows[0].items()
            if key not in {"counts_as_presence", "source_product", "source_row", "case_id"}
        }
        case["source_mentions"][0]["row_sha256"] = payload_sha256(raw)
    elif location == "entry":
        value = {"text": "x" * 131072}
        case["descriptors"] = {payload_sha256(value): value}
    else:
        values = [{"text": char * 70000} for char in "ab"]
        case["descriptors"] = {payload_sha256(value): value for value in values}
    before = deepcopy((case, rows))
    with pytest.raises(ValueError, match="over-budget|no carrier fits"):
        encode(case, rows)
    assert (case, rows) == before
    assert csv.field_size_limit() == 131072


def test_non_native_budget_is_refused_without_calling_a_setter(monkeypatch):
    case, rows = fixture_case()
    calls = []

    def changed_reader(*args):
        calls.append(args)
        return 2**31

    monkeypatch.setattr(codec.csv, "field_size_limit", changed_reader)
    with pytest.raises(ValueError, match="reader character limit changed"):
        encode(case, rows)
    assert calls == [()]


@pytest.mark.parametrize(
    "mutation",
    ["missing", "duplicate", "foreign", "changed_row", "presence", "foreign_case", "row_type"],
)
def test_source_rows_require_bijective_exact_coordinates_and_literal_hashes(mutation):
    case, rows = fixture_case()
    if mutation == "missing":
        rows.pop()
    elif mutation == "duplicate":
        rows[1] = deepcopy(rows[0])
    elif mutation == "foreign":
        rows[0]["source_row"] = "99"
    elif mutation == "changed_row":
        rows[0]["source_text"] += " changed"
    elif mutation == "presence":
        rows[0]["counts_as_presence"] = "false"
    elif mutation == "foreign_case":
        rows[0]["case_id"] = "f" * 64
    else:
        rows[0]["concentration_value"] = 0
    with pytest.raises(ValueError):
        encode(case, rows)


@pytest.mark.parametrize(
    "mutation",
    [
        "missing",
        "duplicate",
        "foreign",
        "bool",
        "unicode",
        "padded",
        "foreign_case",
        "reordered_mentions",
    ],
)
def test_carrier_positions_are_complete_unique_exact_and_preserve_list_order(mutation):
    case, rows = fixture_case()
    node, carriers = encode(case, rows)
    if mutation == "missing":
        carriers.pop()
    elif mutation == "duplicate":
        carriers[1]["original_occurrence_position"] = "1"
    elif mutation == "foreign":
        carriers[0]["original_occurrence_position"] = "4"
    elif mutation == "bool":
        carriers[0]["original_occurrence_position"] = True
    elif mutation == "unicode":
        carriers[0]["original_occurrence_position"] = "１"
    elif mutation == "padded":
        carriers[0]["original_occurrence_position"] = "01"
    elif mutation == "foreign_case":
        carriers[0]["original_case_id"] = "f" * 64
    else:
        carriers[0]["original_occurrence_position"], carriers[1]["original_occurrence_position"] = (
            "2",
            "1",
        )
    with pytest.raises(ValueError):
        decode(case, node, carriers)


@pytest.mark.parametrize(
    "mutation", ["omit", "duplicate", "change", "foreign", "absent_map", "move"]
)
def test_dictionary_loss_addition_duplication_mutation_and_noncanonical_placement_refuse(mutation):
    case, rows = fixture_case()
    node, carriers = encode(case, rows)
    source = json.loads(carriers[0]["context_json"])["descriptors"]
    if mutation == "omit":
        change_context(carriers[0], lambda context: context.pop("descriptors"))
    elif mutation == "duplicate":
        change_context(carriers[1], lambda context: context.update(descriptors=source))
    elif mutation == "change":
        change_context(
            carriers[0],
            lambda context: next(iter(context["descriptors"].values())).update(zero="0"),
        )
    elif mutation == "foreign":
        value = {"extra": "foreign case entry"}
        change_context(
            carriers[0],
            lambda context: context["descriptors"].update({payload_sha256(value): value}),
        )
    elif mutation == "absent_map":
        change_context(carriers[0], lambda context: context.update(held_payloads=source))
    else:
        change_context(carriers[0], lambda context: context.pop("descriptors"))
        change_context(carriers[1], lambda context: context.update(descriptors=source))
    with pytest.raises(ValueError):
        decode(case, node, carriers)


@pytest.mark.parametrize(
    "text",
    [
        "{",
        '{"source_mentions":[],"source_mentions":[]}',
        '{"source_mentions": NaN}',
        '{ "source_mentions":[] }',
        "[]",
        '{"source_mentions":[],"extra":0}',
    ],
)
def test_invalid_duplicate_noncanonical_and_unknown_json_refuses(text):
    case, rows = fixture_case()
    node, carriers = encode(case, rows)
    carriers[0]["context_json"] = text
    with pytest.raises(ValueError):
        decode(case, node, carriers)


@pytest.mark.parametrize(
    "mutation",
    [
        "unknown",
        "missing_candidate",
        "partial_owner",
        "bad_count",
        "bool_row",
        "repeat_mention",
        "nonjson",
        "nonstring_key",
        "nan",
        "no_carriers",
        "bad_dictionary",
    ],
)
def test_unknown_shapes_types_and_ambiguous_cases_fail_closed(mutation):
    case, rows = fixture_case()
    if mutation == "unknown":
        case["new_field"] = "cannot discard"
    elif mutation == "missing_candidate":
        case.pop("candidate")
    elif mutation == "partial_owner":
        case["candidate"].pop("owner_record_sha256")
    elif mutation == "bad_count":
        case["positive_occurrences"] = True
    elif mutation == "bool_row":
        case["source_mentions"][0]["row"] = True
    elif mutation == "repeat_mention":
        case["source_mentions"][1] = deepcopy(case["source_mentions"][0])
    elif mutation == "nonjson":
        case["candidate"]["owners"] = ("tuple",)
    elif mutation == "nonstring_key":
        case["descriptors"] = {1: {"key": "not string"}}
    elif mutation == "nan":
        case["candidate"]["classification"] = float("nan")
    elif mutation == "no_carriers":
        case["source_mentions"] = []
        case["positive_occurrences"] = 0
        rows = []
    else:
        case["descriptors"] = {"a" * 64: {"wrong": "key hash"}}
    # Use a separate syntactically valid pin so invalid Python data reaches codec validation.
    with pytest.raises(ValueError):
        codec.encode_case(case, rows, expected_case_sha256="a" * 64)


def test_full_case_hash_is_externally_bound_not_replaceable_with_envelope_hash():
    case, rows = fixture_case()
    node, carriers = encode(case, rows)
    with pytest.raises(ValueError, match="full-case hash"):
        codec.encode_case(case, rows, expected_case_sha256="a" * 64)
    node["original_case_sha256"] = payload_sha256(
        json.loads(node["original_case_without_occurrences_json"])
    )
    with pytest.raises(ValueError, match="full-case hash"):
        decode(case, node, carriers)


def test_historical_candidate_tampering_is_not_invisible():
    case, rows = fixture_case()
    node, carriers = encode(case, rows)
    envelope = json.loads(node["original_case_without_occurrences_json"])
    envelope["candidate"]["classification"] = "CURRENT_APPROVAL_IS_NOT_AUTHORIZED"
    node["original_case_without_occurrences_json"] = canonical(envelope)
    with pytest.raises(ValueError, match="full-case hash"):
        decode(case, node, carriers)


@pytest.mark.parametrize("field", ["descriptors", "change_payloads", "held_payloads"])
def test_omitting_each_dictionary_collection_loses_authenticated_data(field):
    case, rows = fixture_case(held=field == "held_payloads")
    node, carriers = encode(case, rows)
    change_context(carriers[0], lambda context: context.pop(field))
    with pytest.raises(ValueError, match="full-case hash"):
        decode(case, node, carriers)


def test_candidate_without_owner_annotation_and_empty_historical_lists_roundtrips():
    case, rows = fixture_case()
    case["candidate"] = {
        "owners": [],
        "rejected_owners": [],
        "supported_canonical_rows": [],
        "classification": "NO_ACTIVE_OWNER",
    }
    assert decode(case, *encode(case, rows)) == (case, rows)


@pytest.mark.parametrize(
    "field", ["original_case_without_occurrences_json", "original_occurrence_json", "context_json"]
)
def test_every_json_cell_refuses_duplicate_keys_and_noncanonical_encoding(field):
    case, rows = fixture_case()
    for duplicated in (False, True):
        node, carriers = encode(case, rows)
        target = node if field in node else carriers[0]
        if duplicated:
            original = json.loads(target[field])
            first_key = next(iter(original))
            target[field] = (
                target[field][:-1]
                + ","
                + canonical(first_key)
                + ":"
                + canonical(original[first_key])
                + "}"
            )
        else:
            target[field] += " "
        with pytest.raises(ValueError, match="duplicate JSON key|noncanonical JSON"):
            decode(case, node, carriers)


def test_encode_preserves_input_dictionary_objects_and_does_not_alias_outputs():
    case, rows = fixture_case()
    dictionaries = [
        (field, case[field], list(case[field].values()))
        for field in ("descriptors", "change_payloads")
    ]
    node, carriers = encode(case, rows)
    for field, original, values in dictionaries:
        assert case[field] is original
        assert all(
            current is previous
            for current, previous in zip(case[field].values(), values, strict=True)
        )
    node["original_case_id"] = "changed returned node"
    carriers[0]["context_json"] = "changed returned carrier"
    assert case["case_id"] == rows[0]["case_id"]


def test_source_row_mutation_after_layout_still_fails_and_does_not_mutate_inputs():
    case, rows = fixture_case(held=True)
    node, carriers = encode(case, rows)
    row = json.loads(carriers[0]["original_occurrence_json"])
    row["review_status"] = "SUPPORTED"
    carriers[0]["original_occurrence_json"] = canonical(row)
    before = deepcopy((node, carriers))
    with pytest.raises(ValueError, match="source row hash"):
        decode(case, node, carriers)
    assert (node, carriers) == before
