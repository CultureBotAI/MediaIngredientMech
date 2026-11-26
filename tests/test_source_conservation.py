"""Adversarial pure-data inverse checks for #1431; no native/report operations."""

from __future__ import annotations

import ast
import inspect
import json
from copy import deepcopy

import pytest

from mediaingredientmech.export import source_assembly as assembly
from mediaingredientmech.export import source_conservation as inverse
from tests.test_source_assembly import (
    canonical,
    construct,
    inputs,
    raw_table,
    replace_rows,
    rows,
    sha,
)


@pytest.mark.parametrize(
    "field",
    [
        "source_label",
        "id_origin",
        "projection_contract",
        "source_identity_claimed",
        "original_case_position",
        "projection_declaration_path",
        "projection_declaration_sha256",
    ],
)
def test_all_full_node_metadata_is_checked(field):
    data = inputs()
    candidate = construct(data)
    values = rows(candidate["cm"]["nodes"])
    values[0][field] += "changed"
    candidate["cm"]["nodes"] = replace_rows(candidate["cm"]["nodes"], values)
    with pytest.raises(ValueError, match="full CM node differs"):
        inverse.validate_source_conservation(candidate, **data)


@pytest.mark.parametrize("mutation", ["descriptor", "candidate", "list_order", "empty_presence"])
def test_full_case_payload_not_opaque_hash_only(mutation):
    data = inputs()
    candidate = construct(data)
    nodes = rows(candidate["cm"]["nodes"])
    uses = rows(candidate["cm"]["occurrences"])
    if mutation == "descriptor":
        context = json.loads(uses[0]["context_json"])
        context["descriptors"] = {"f" * 64: {"different": "0"}}
        uses[0]["context_json"] = canonical(context)
    elif mutation == "list_order":
        uses[0]["original_occurrence_position"] = "1"
    else:
        envelope = json.loads(nodes[0]["original_case_without_occurrences_json"])
        if mutation == "candidate":
            envelope["candidate"]["classification"] = "CURRENT_APPROVED"
        else:
            envelope["held_payloads"] = {}
        nodes[0]["original_case_without_occurrences_json"] = canonical(envelope)
    candidate["cm"]["nodes"] = replace_rows(candidate["cm"]["nodes"], nodes)
    candidate["cm"]["occurrences"] = replace_rows(candidate["cm"]["occurrences"], uses)
    with pytest.raises(ValueError):
        inverse.validate_source_conservation(candidate, **data)


def test_changed_ordinary_literal_with_recomputed_candidate_hashes_still_refuses():
    data = inputs()
    changed = deepcopy(data)
    values = rows(changed["cm"]["ordinary"])
    values[0]["counts_as_presence"] = "false"
    changed["cm"]["ordinary"] = replace_rows(changed["cm"]["ordinary"], values)
    changed["cm"]["ordinary_sha256"] = sha(changed["cm"]["ordinary"])
    # No report/native execution: modify a candidate transport cell directly.
    candidate = construct(data)
    uses = rows(candidate["cm"]["occurrences"])
    uses[0]["original_occurrence_json"] = canonical(values[0])
    candidate["cm"]["occurrences"] = replace_rows(candidate["cm"]["occurrences"], uses)
    with pytest.raises(ValueError, match="presence differs"):
        inverse.validate_source_conservation(candidate, **data)


@pytest.mark.parametrize(
    "mutation", ["row_value", "provider", "context", "multiplicity", "order", "padding", "header"]
)
def test_inverse_rejects_kg_loss_and_combination_changes(mutation):
    data = inputs()
    candidate = construct(data)
    values = rows(candidate["occurrences"])
    index = next(
        i
        for i, row in enumerate(values)
        if row[inverse.META[0]] == data["family_paths"]["kg_occurrences"]
    )
    if mutation in {"row_value", "provider", "context"}:
        field = {
            "row_value": "source_record_json",
            "provider": "provider",
            "context": "context_json",
        }[mutation]
        values[index][field] = "changed literal"
    elif mutation == "multiplicity":
        values.append(deepcopy(values[index]))
    elif mutation == "order":
        values[index], values[index + 1] = values[index + 1], values[index]
    elif mutation == "padding":
        values[index]["original_case_id"] = "invented"
    if mutation == "header":
        candidate["occurrences"] = raw_table(list(reversed(list(values[0]))), values)
    else:
        candidate["occurrences"] = replace_rows(candidate["occurrences"], values)
    with pytest.raises(ValueError):
        inverse.validate_source_conservation(candidate, **data)


@pytest.mark.parametrize(
    "sidecar", ["raw_row_map", "case_crosswalk", "position_map", "reconciliation"]
)
def test_maps_and_bridge_are_verified_against_actual_rows(sidecar):
    data = inputs()
    candidate = construct(data)
    if sidecar in {"raw_row_map", "case_crosswalk"}:
        candidate["cm"][sidecar].pop()
    elif sidecar == "position_map":
        candidate[sidecar][0]["native_position"] += 1
    else:
        bridge = rows(candidate[sidecar])
        bridge[-1]["lane"] = "positive_inventory"
        candidate[sidecar] = replace_rows(candidate[sidecar], bridge)
    with pytest.raises(ValueError):
        inverse.validate_source_conservation(candidate, **data)


@pytest.mark.parametrize(
    "mutation", ["omit_case", "omit_origin", "clear_hold", "invent_relation", "omit_provider"]
)
def test_historical_obligations_cannot_disappear_or_become_approval(mutation):
    data = inputs()
    candidate = construct(data)
    if mutation == "omit_case":
        candidate["historical_obligations"]["cases"].pop("OLD:CM")
    elif mutation == "omit_origin":
        candidate["historical_obligations"]["origins"].clear()
    elif mutation == "clear_hold":
        candidate["historical_obligations"]["cases"]["OLD:CM"]["holds"] = []
    elif mutation == "omit_provider":
        candidate["kg_provider_cases"].pop()
    else:
        candidate["obligation_crosswalk"]["cases"]["OLD:CM"]["targets"] = [
            {"source_id": rows(candidate["nodes"])[0]["source_id"], "source_position": 1}
        ]
    with pytest.raises(ValueError):
        inverse.validate_source_conservation(candidate, **data)


@pytest.mark.parametrize(
    "bad", ["wrong_hash", "missing_key", "no_reason", "foreign_target", "repeated_target"]
)
def test_supplied_crosswalk_has_complete_honest_structure(bad):
    data = inputs()
    entry = data["reviewed_crosswalk"]["cases"]["OLD:CM"]
    if bad == "wrong_hash":
        entry["original_sha256"] = "f" * 64
    elif bad == "missing_key":
        data["reviewed_crosswalk"]["origins"].clear()
    elif bad == "no_reason":
        entry["unresolved_reason"] = ""
    elif bad == "foreign_target":
        entry["targets"] = [{"source_id": "kgmicrobe.compound:absent", "source_position": 100}]
    else:
        target = {"source_id": "mediadive.ingredient:7", "source_position": 4}
        entry["targets"] = [target, deepcopy(target)]
    with pytest.raises(ValueError):
        construct(data)


def test_explicit_reviewed_relation_is_preserved_without_identity_inference():
    data = inputs()
    entry = data["reviewed_crosswalk"]["cases"]["OLD:0"]
    entry["targets"] = [{"source_id": "mediadive.ingredient:7", "source_position": 4}]
    entry["unresolved_reason"] = ""
    entry["evidence"] = ["synthetic:independent-literal-provider-relation"]
    candidate = construct(data)
    result = inverse.validate_source_conservation(candidate, **data)
    assert candidate["obligation_crosswalk"] == data["reviewed_crosswalk"]
    assert result["scientific_approval"] is False
    assert candidate["historical_obligations"]["cases"]["OLD:0"]["holds"] == ["IDENTITY_FORM"]


@pytest.mark.parametrize(
    "mutation",
    ["provider_payload", "case_hash", "missing_link", "foreign_provider", "duplicate_source"],
)
def test_kg_selected_provider_obligations_are_not_just_counts(mutation):
    data = inputs()
    kg = data["kg"]
    if mutation == "provider_payload":
        kg["cases"][0]["holds"] = []
    elif mutation == "case_hash":
        kg["case_hashes"].pop("OLD:0")
    else:
        kind = "occurrences" if mutation == "foreign_provider" else "nodes"
        values = rows(kg[kind])
        if mutation == "missing_link":
            values[1]["original_case_ids_json"] = '["OLD:1"]'
        elif mutation == "foreign_provider":
            values[0]["provider"] = "unselected"
        else:
            values.append(deepcopy(values[0]))
        kg[kind] = replace_rows(kg[kind], values)
        kg[kind + "_sha256"] = sha(kg[kind])
    with pytest.raises(ValueError):
        construct(data)


@pytest.mark.parametrize(
    "prefix", ["MIMCMREFv1", "MIM", "MIM.ingredient", "mediadive.ingredient", "kgmicrobe.compound"]
)
def test_reserved_namespace_meanings_cannot_change(prefix):
    data = inputs()
    data["curie_map"][prefix] = "https://invalid.example/"
    with pytest.raises(ValueError, match="URI meaning"):
        construct(data)


def test_expanded_uri_alias_collision_refuses_even_different_curies():
    data = inputs()
    projection = assembly.project_culturemech(data["cm"])
    cm_id = rows(projection["nodes"])[0]["source_id"]
    data["curie_map"]["kgmicrobe.compound"] = inverse.CM_URI
    # A differently spelled alias would collide; even the known KG meaning
    # alteration is refused before it can create that identity collapse.
    with pytest.raises(ValueError, match="URI meaning"):
        assembly.combine_sources(projection, **data)
    inverse._namespaces(
        [{"source_id": cm_id}],
        data["curie_map"] | {"kgmicrobe.compound": "https://w3id.org/kg-microbe/compound/"},
    )
    with pytest.raises(ValueError, match="expanded URI"):
        inverse._namespaces(
            [{"source_id": "MIM:0000001"}, {"source_id": "MIM.ingredient:0000001"}],
            {
                "MIMCMREFv1": inverse.CM_URI,
                "MIM": "https://culturebotai.github.io/MediaIngredientMech/ingredient/MIM_",
                "MIM.ingredient": "https://culturebotai.github.io/MediaIngredientMech/ingredient/MIM_",
            },
        )


def test_inverse_has_no_assembler_native_or_filesystem_import():
    tree = ast.parse(inspect.getsource(inverse))
    imports = [node.module or "" for node in ast.walk(tree) if isinstance(node, ast.ImportFrom)]
    imports += [
        item.name for node in ast.walk(tree) if isinstance(node, ast.Import) for item in node.names
    ]
    assert not any(
        any(
            word in name
            for word in (
                "source_assembly",
                "source_bindings",
                "source_producer",
                "culturemech_replay",
                "subprocess",
            )
        )
        for name in imports
    )
    calls = [node.func for node in ast.walk(tree) if isinstance(node, ast.Call)]
    assert not any(
        isinstance(func, ast.Name) and func.id in {"open", "exec", "eval", "compile"}
        for func in calls
    )


@pytest.mark.parametrize("sidecar", ["raw_row_map", "case_crosswalk", "position_map"])
def test_position_proofs_do_not_coerce_boolean_to_integer(sidecar):
    data = inputs()
    candidate = construct(data)
    if sidecar == "raw_row_map":
        candidate["cm"][sidecar][0]["original_position"] = True
    elif sidecar == "case_crosswalk":
        candidate["cm"][sidecar][0]["original_case_position"] = False
    else:
        candidate[sidecar][0]["native_position"] = True
    with pytest.raises(ValueError, match="map differs"):
        inverse.validate_source_conservation(candidate, **data)


def test_inverse_does_not_use_producer_as_its_oracle(monkeypatch):
    data = inputs()
    candidate = construct(data)

    def forbidden(*args, **kwargs):
        pytest.fail("inverse called producer")

    for name in ("project_culturemech", "combine_sources", "render_tables"):
        monkeypatch.setattr(assembly, name, forbidden)
    assert inverse.validate_source_conservation(candidate, **data)["source_only"] is True


def test_actual_combination_refuses_expanded_mim_alias_collision():
    data = inputs()
    kg = data["kg"]
    replacements = {
        "mediadive.ingredient:7": "MIM:0000001",
        "kgmicrobe.compound:shared": "MIM.ingredient:0000001",
    }
    for kind in ("nodes", "occurrences"):
        values = rows(kg[kind])
        for value in values:
            value["source_id"] = replacements.get(value["source_id"], value["source_id"])
        kg[kind] = replace_rows(kg[kind], values)
        kg[kind + "_sha256"] = sha(kg[kind])
    for case in kg["cases"]:
        case["source_case_id"] = replacements.get(case["source_case_id"], case["source_case_id"])
        kg["case_hashes"][case["case_id"]] = inverse.payload_sha256(case)
    for prefix in ("MIM", "MIM.ingredient"):
        data["curie_map"][
            prefix
        ] = "https://culturebotai.github.io/MediaIngredientMech/ingredient/MIM_"
    with pytest.raises(ValueError, match="expanded URI"):
        construct(data)


def test_unknown_cm_transport_column_refused_before_combination():
    data = inputs()
    projection = assembly.project_culturemech(data["cm"])
    values = rows(projection["nodes"])
    for row in values:
        row["invented_wire_field"] = "unapproved"
    projection["nodes"] = raw_table(list(values[0]), values)
    with pytest.raises(ValueError, match="CM projection headers"):
        assembly.combine_sources(projection, **data)
