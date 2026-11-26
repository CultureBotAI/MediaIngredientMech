"""Small synthetic source-only assembly tests for #1431; no native fixtures."""

from __future__ import annotations

import csv
import hashlib
import io
import json
from copy import deepcopy

import pytest

from mediaingredientmech.export import source_assembly as assembly
from mediaingredientmech.export import source_conservation as inverse
from mediaingredientmech.review_claims import payload_sha256


def canonical(value):
    return json.dumps(
        value, sort_keys=True, separators=(",", ":"), ensure_ascii=False, allow_nan=False
    )


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def raw_table(fields, rows):
    """Independent fixture serialization, including noncanonical JSON literals."""
    text = io.StringIO(newline="")
    writer = csv.DictWriter(text, fieldnames=fields, delimiter="\t", lineterminator="\n")
    writer.writeheader()
    writer.writerows(rows)
    return text.getvalue().encode()


def rows(raw):
    return list(csv.DictReader(io.StringIO(raw.decode(), newline=""), delimiter="\t"))


def replace_rows(raw, replacement):
    fields = next(csv.reader(io.StringIO(raw.decode(), newline=""), delimiter="\t"))
    return raw_table(fields, replacement)


ORDINARY = (
    "recipe_id recipe_label recipe_category source_path record_class component_field "
    "component_index preferred_term label_source resolved_identifier resolution_source "
    "local_identifier source_compound_id mim_preferred_term mim_matched_label mim_match_type "
    "mim_mapping_status mim_ambiguity mim_ontology_id_diagnostic grounding_reason "
    "concentration_value concentration_unit ingredient_json variant_index variant_name "
    "change_index change_action change_stage descriptor_role descriptor_path "
    "source_modification_index source_text evidence_json change_json"
).split()
HELD = (
    "recipe_id recipe_label recipe_category source_path variant_index variant_name "
    "mention_index descriptor_path source_label reported_action stage source_modification_index "
    "source_text reason reported_quantity held_fields_json evidence_json mention_json "
    "review_status counts_as_presence"
).split()


def fixture_case(label, specification):
    context = {
        "preferred_term": label,
        "resolved_identifier": "",
        "change_action": "",
        "change_stage": "",
        "descriptor_role": "",
        "variant_name": "",
    }
    case_id = payload_sha256(context)
    descriptor = {"amount": "0", "zero": 0, "empty": "", "null": None, "list": ["x", "x", "µ"]}
    held_payload = {
        "source_label": label,
        "reason": "operation and quantity unresolved",
        "held_fields": ["OPERATION", "QUANTITY"],
        "reported_quantity": "0",
        "evidence": [],
    }
    mentions, source_rows = [], []
    counts = {"positive_occurrences": 0, "context_only_mentions": 0, "held_source_mentions": 0}
    for product, position in specification:
        held = product == "variant_ingredient_holds.tsv"
        raw = dict.fromkeys(HELD if held else ORDINARY, "")
        raw.update(
            recipe_id="CM:synthetic",
            source_path="synthetic/recipe.yaml",
            descriptor_path=f"/ingredients/{position}",
            source_text="literal\tline\nµ",
        )
        if held:
            raw.update(
                review_status="WITHHELD",
                counts_as_presence="false",
                reported_quantity="0",
                held_fields_json='["OPERATION", "QUANTITY"]',
                mention_json=json.dumps(held_payload),
            )
            counts["held_source_mentions"] += 1
        else:
            raw.update(
                component_field="ingredients",
                component_index=str(position),
                concentration_value="0",
                ingredient_json=json.dumps(descriptor, ensure_ascii=False),
            )
            counts[
                (
                    "positive_occurrences"
                    if product == "ingredient_occurrences.tsv"
                    else "context_only_mentions"
                )
            ] += 1
            if product == "variant_ingredient_changes.tsv":
                raw.update(change_action="REMOVE", descriptor_role="replaced_ingredient")
        mention = {
            "product": product,
            "row": position,
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
        source_rows.append(
            {
                **raw,
                "counts_as_presence": (
                    "true" if product == "ingredient_occurrences.tsv" else "false"
                ),
                "source_product": product,
                "source_row": str(position),
                "case_id": case_id,
            }
        )
    case = {
        "case_id": case_id,
        "context": context,
        "source_mentions": mentions,
        "descriptors": {payload_sha256(descriptor): descriptor},
        "change_payloads": {},
        **counts,
        "candidate": {
            "owners": ["historical/owner.yaml"],
            "rejected_owners": ["historical/rejected.yaml"],
            "supported_canonical_rows": [],
            "classification": "HISTORICAL_SUPPORTED",
            "owner_record": "historical/owner.yaml",
            "owner_record_sha256": "a" * 64,
            "mim_identifier": "kgmicrobe.ingredient:historical",
        },
    }
    if counts["held_source_mentions"]:
        case["held_payloads"] = {payload_sha256(held_payload): held_payload}
    return case, source_rows


def inputs(*, extra_case=False):
    a, ar = fixture_case(
        "same label, first scope",
        [
            ("ingredient_occurrences.tsv", 3),
            ("ingredient_occurrences.tsv", 1),
            ("variant_ingredient_holds.tsv", 1),
        ],
    )
    b, br = fixture_case("same label, second scope", [("ingredient_occurrences.tsv", 2)])
    c, cr = fixture_case("context material", [("variant_ingredient_changes.tsv", 1)])
    cases = [c, a, b]
    ordinary = [ar[1], br[0], ar[0], cr[0]]
    if extra_case:
        d, dr = fixture_case("extra lexical scope", [("ingredient_occurrences.tsv", 4)])
        cases.insert(1, d)
        ordinary.insert(1, dr[0])
    source = raw_table(
        [*ORDINARY, "counts_as_presence", "source_product", "source_row", "case_id"], ordinary
    )
    held = raw_table([*HELD, "source_product", "source_row", "case_id"], [ar[2]])
    selected_scope = {
        "accepted_packet_sha256": "b" * 64,
        "selected_kg_owner_receipt_sha256": "c" * 64,
        "source_tables": {"originals/mentions.tsv": sha(source), "originals/held.tsv": sha(held)},
    }
    declaration = canonical(
        {
            "proposed_curie_prefix": "MIMCMREFv1",
            "proposed_contract_version": "mim-culturemech-material-reference-v1",
            "proposed_uri_base": "https://culturebotai.github.io/MediaIngredientMech/source-material-reference/v1/culturemech/",
            "original_case_transport": "synthetic selected v3 envelope/fragments",
            "original_source_scope": selected_scope,
        }
    ).encode()
    cm = {
        "cases": cases,
        "case_hashes": {case["case_id"]: payload_sha256(case) for case in cases},
        "ordinary": source,
        "ordinary_sha256": sha(source),
        "ordinary_path": "originals/mentions.tsv",
        "held": held,
        "held_sha256": sha(held),
        "held_path": "originals/held.tsv",
        "declaration": declaration,
        "declaration_sha256": sha(declaration),
        "declaration_path": "inputs/DECLARATION.json",
        "selected_scope": selected_scope,
    }
    kg_cases = [
        {
            "case_id": f"OLD:{index}",
            "source": provider,
            "source_case_id": identifier,
            "holds": ["IDENTITY_FORM"],
            "prior_status": "UNRESOLVED",
            "literal": {"amount": "0", "evidence": []},
        }
        for index, (provider, identifier) in enumerate(
            [
                ("mediadive", "mediadive.ingredient:7"),
                ("metatraits", "kgmicrobe.compound:shared"),
                ("metatraits_gtdb", "kgmicrobe.compound:shared"),
                ("microbedecoder", "kgmicrobe.compound:decoder"),
            ]
        )
    ]
    nodes = []
    for identifier in (
        "mediadive.ingredient:7",
        "kgmicrobe.compound:shared",
        "kgmicrobe.compound:decoder",
    ):
        linked = [case for case in kg_cases if case["source_case_id"] == identifier]
        nodes.append(
            {
                "source_id": identifier,
                "source_label": "a shared literal label",
                "label_selection": "preserved",
                "label_variants_json": '["x", "x"]',
                "providers_json": json.dumps([case["source"] for case in linked]),
                "original_case_ids_json": json.dumps([case["case_id"] for case in linked]),
                "original_node_rows_json": '[{"literal": "0"}]',
                "current_graph_node_rows_json": "[]",
                "assembly_warnings_json": '["scientific hold retained"]',
            }
        )
    occurrences = [
        {
            "source_id": case["source_case_id"],
            "provider": case["source"],
            "kind": "observation",
            "original_input": "frozen/input.tsv",
            "original_input_sha256": "d" * 64,
            "physical_position": str(index + 1),
            "source_locator": f"row/{index + 1}",
            "source_record_json": '{"amount": "0", "empty": ""}',
            "context_json": '{"holds": ["SOURCE_CLAIM"], "counts_as_presence": false}',
        }
        for index, case in enumerate(kg_cases)
    ]
    occurrences.append(deepcopy(occurrences[0]))  # Literal repeated observation must not collapse.
    node_bytes, occurrence_bytes = raw_table(list(nodes[0]), nodes), raw_table(
        list(occurrences[0]), occurrences
    )
    kg = {
        "nodes": node_bytes,
        "nodes_sha256": sha(node_bytes),
        "occurrences": occurrence_bytes,
        "occurrences_sha256": sha(occurrence_bytes),
        "cases": kg_cases,
        "case_hashes": {case["case_id"]: payload_sha256(case) for case in kg_cases},
    }
    original = {
        "cases": {case["case_id"]: deepcopy(case) for case in kg_cases},
        "origins": {
            "origin:1": {"origin_id": "origin:1", "status": "HELD", "holds": ["SOURCE_CLAIM"]}
        },
    }
    original["cases"]["OLD:CM"] = {
        "case_id": "OLD:CM",
        "holds": ["OPERATION"],
        "old_occurrences": [{"literal": "0"}],
    }
    crosswalk = {
        group: {
            key: {
                "original_sha256": payload_sha256(payload),
                "targets": [],
                "evidence": ["synthetic:retained-history"],
                "unresolved_reason": "no reviewed current relation",
            }
            for key, payload in values.items()
        }
        for group, values in original.items()
    }
    family_paths = {
        family + "_" + kind: "originals/" + family + "-" + kind + ".tsv"
        for family in ("cm", "kg")
        for kind in ("nodes", "occurrences")
    }
    prefixes = {
        "MIMCMREFv1": "https://culturebotai.github.io/MediaIngredientMech/source-material-reference/v1/culturemech/",
        "mediadive.ingredient": "https://mediadive.dsmz.de/ingredient/",
        "kgmicrobe.compound": "https://w3id.org/kg-microbe/compound/",
    }
    return {
        "cm": cm,
        "kg": kg,
        "family_paths": family_paths,
        "curie_map": prefixes,
        "historical_obligations": original,
        "reviewed_crosswalk": crosswalk,
    }


def construct(data):
    return assembly.combine_sources(assembly.project_culturemech(data["cm"]), **data)


def test_complete_projection_and_independent_inverse():
    data = inputs()
    before = deepcopy(data)
    candidate = construct(data)
    result = inverse.validate_source_conservation(candidate, **data)
    assert result == {
        "source_only": True,
        "scientific_approval": False,
        "native_conservation": False,
        "cm_cases": 3,
        "cm_lanes": {"positive_inventory": 3, "context_only": 1, "held": 1},
        "kg_nodes": 3,
        "kg_provider_cases": 4,
        "kg_occurrences": 5,
        "kg_provider_occurrences": {
            "mediadive": 2,
            "metatraits": 1,
            "metatraits_gtdb": 1,
            "microbedecoder": 1,
        },
        "nodes": 6,
        "occurrences": 10,
        "historical_cases": 5,
        "historical_origins": 1,
    }
    assert data == before
    assert list(rows(candidate["cm"]["nodes"])[0]) == list(inverse.NODE_FIELDS)
    originals = rows(data["cm"]["ordinary"]) + rows(data["cm"]["held"])
    assert [
        json.loads(row["original_occurrence_json"]) for row in rows(candidate["cm"]["occurrences"])
    ] == originals
    assert [
        row["original_occurrence_position"] for row in rows(candidate["cm"]["occurrences"])
    ] == ["2", "1", "1", "1", "3"]
    assert [row["native_occurrence_position"] for row in rows(candidate["reconciliation"])] == [
        "1",
        "2",
        "3",
        "4",
        "5",
    ]
    candidate["historical_obligations"]["cases"]["OLD:CM"]["holds"].clear()
    assert data == before  # Returned nested history never aliases caller data.


def test_changed_cm_population_preserves_exact_kg_without_offsets():
    offsets = []
    for extra in (False, True):
        data = inputs(extra_case=extra)
        candidate = construct(data)
        inverse.validate_source_conservation(candidate, **data)
        combined = rows(candidate["occurrences"])
        kg_rows = [
            row
            for row in combined
            if row[inverse.META[0]] == data["family_paths"]["kg_occurrences"]
        ]
        original = rows(data["kg"]["occurrences"])
        assert [{key: row[key] for key in original[0]} for row in kg_rows] == original
        first = next(
            item
            for item in candidate["position_map"]
            if item["kind"] == "occurrences"
            and item["original_table"] == data["family_paths"]["kg_occurrences"]
        )
        offsets.append(first["native_position"])
    assert offsets == [6, 7]


def test_address_exact_formula_and_declaration_versioning():
    data = inputs()
    projection = assembly.project_culturemech(data["cm"])
    case = data["cm"]["cases"][0]
    basis = {
        "domain": "mim-culturemech-material-reference-v1",
        "declaration_sha256": data["cm"]["declaration_sha256"],
        "original_case_id": case["case_id"],
        "original_case_sha256": payload_sha256(case),
    }
    old = rows(projection["nodes"])[0]["source_id"]
    assert old == "MIMCMREFv1:" + sha(canonical(basis).encode())
    declaration = json.loads(data["cm"]["declaration"])
    declaration["original_case_transport"] += "; reviewed successor"
    data["cm"]["declaration"] = canonical(declaration).encode()
    data["cm"]["declaration_sha256"] = sha(data["cm"]["declaration"])
    assert rows(assembly.project_culturemech(data["cm"])["nodes"])[0]["source_id"] != old
    assert data["cm"]["cases"][0] == case


@pytest.mark.parametrize("field", ["ordinary", "held", "declaration"])
def test_independent_input_hash_required(field):
    data = inputs()
    data["cm"][field] += b"\n"
    with pytest.raises(ValueError, match="selected original bytes"):
        assembly.project_culturemech(data["cm"])


@pytest.mark.parametrize("bad", [b'{"x":1,"x":2}', b"{}\n", b"NaN"])
def test_declaration_invalid_or_noncanonical(bad):
    data = inputs()
    data["cm"].update(declaration=bad, declaration_sha256=sha(bad))
    with pytest.raises(ValueError):
        assembly.project_culturemech(data["cm"])


def test_declaration_cannot_select_its_own_authority():
    data = inputs()
    declaration = json.loads(data["cm"]["declaration"])
    declaration["original_source_scope"]["accepted_packet_sha256"] = "e" * 64
    raw = canonical(declaration).encode()
    data["cm"].update(declaration=raw, declaration_sha256=sha(raw))
    with pytest.raises(ValueError, match="independent selected source authority"):
        assembly.project_culturemech(data["cm"])


@pytest.mark.parametrize("target", ["declaration", "declaration_path"])
def test_full_node_added_cells_cannot_exceed_budget(target):
    data = inputs()
    if target == "declaration":
        declaration = json.loads(data["cm"][target])
        declaration["original_case_transport"] = "x" * 131072
        data["cm"].update(declaration=canonical(declaration).encode())
        data["cm"]["declaration_sha256"] = sha(data["cm"]["declaration"])
    else:
        data["cm"][target] = "x" * 131073
    with pytest.raises(ValueError, match="over-budget"):
        assembly.project_culturemech(data["cm"])


def test_character_boundary_is_not_utf8_byte_budget():
    value = "µ" * 131072
    raw = assembly.render_tables(("literal",), [{"literal": value}])
    assert rows(raw) == [{"literal": value}]
    assert len(value.encode()) == 262144
    with pytest.raises(ValueError, match="over-budget"):
        assembly.render_tables(("literal",), [{"literal": value + "µ"}])


@pytest.mark.parametrize(
    "fields,values",
    [
        (("a", "a"), [{"a": "x"}]),
        (("a",), [{"b": "x"}]),
        (("a",), [{"a": 0}]),
        (("a",), [{"a": "\ud800"}]),
    ],
)
def test_render_rejects_lossy_or_invalid_cells(fields, values):
    with pytest.raises(ValueError):
        assembly.render_tables(fields, values)


def test_output_is_deterministic():
    data = inputs()
    assert construct(data) == construct(deepcopy(data))


def test_full_inline_declaration_at_exact_character_limit():
    data = inputs()
    declaration = json.loads(data["cm"]["declaration"])
    declaration["padding"] = ""
    declaration["padding"] = "µ" * (131072 - len(canonical(declaration)))
    raw = canonical(declaration).encode()
    assert len(raw.decode()) == 131072 and len(raw) > 131072
    data["cm"].update(declaration=raw, declaration_sha256=sha(raw))
    candidate = construct(data)
    inverse.validate_source_conservation(candidate, **data)
    assert rows(candidate["nodes"])[0]["projection_declaration_json"] == raw.decode()


@pytest.mark.parametrize("cell", ["family_path", "header", "kg_payload"])
def test_added_and_combined_cells_keep_original_limit(cell):
    data = inputs()
    if cell == "family_path":
        data["family_paths"]["kg_occurrences"] = "x" * 131073
    elif cell == "header":
        with pytest.raises(ValueError, match="over-budget"):
            assembly.render_tables(("x" * 131073,), [])
        return
    else:
        values = rows(data["kg"]["occurrences"])
        values[0]["context_json"] = "µ" * 131073
        data["kg"]["occurrences"] = replace_rows(data["kg"]["occurrences"], values)
        data["kg"]["occurrences_sha256"] = sha(data["kg"]["occurrences"])
    with pytest.raises((ValueError, csv.Error), match="over-budget|field larger"):
        construct(data)


def test_refuses_changed_reader_budget_without_changing_it(monkeypatch):
    original = csv.field_size_limit()
    monkeypatch.setattr(csv, "field_size_limit", lambda: original + 1)
    with pytest.raises(ValueError, match="reader character limit changed"):
        assembly.render_tables(("literal",), [{"literal": "small"}])


@pytest.mark.parametrize("held_presence", ["absent", "empty"])
def test_dictionary_key_presence_retained(held_presence):
    data = inputs()
    case = data["cm"]["cases"][0]
    assert "held_payloads" not in case
    if held_presence == "empty":
        case["held_payloads"] = {}
    data["cm"]["case_hashes"][case["case_id"]] = payload_sha256(case)
    candidate = construct(data)
    inverse.validate_source_conservation(candidate, **data)
    envelope = json.loads(
        rows(candidate["cm"]["nodes"])[0]["original_case_without_occurrences_json"]
    )
    assert ("held_payloads" in envelope) == (held_presence == "empty")


def test_current_owner_selector_is_not_an_assembly_input():
    data = inputs()
    data["cm"]["owner_record"] = "invented/current-owner.yaml"
    with pytest.raises(ValueError, match="unexpected/missing"):
        assembly.project_culturemech(data["cm"])


@pytest.mark.parametrize(
    "change",
    ["case_hash", "duplicate_coordinate", "missing_coordinate", "held_promotion", "wrong_count"],
)
def test_selected_cm_refusals(change):
    data = inputs()
    cm = data["cm"]
    if change == "case_hash":
        cm["case_hashes"][cm["cases"][0]["case_id"]] = "f" * 64
    elif change == "wrong_count":
        cm["cases"][0]["context_only_mentions"] += 1
        cm["case_hashes"][cm["cases"][0]["case_id"]] = payload_sha256(cm["cases"][0])
    else:
        kind = "held" if change == "held_promotion" else "ordinary"
        source = rows(cm[kind])
        if change == "duplicate_coordinate":
            source.append(deepcopy(source[0]))
        elif change == "missing_coordinate":
            source.pop()
        else:
            source[0]["review_status"] = "SUPPORTED"
        cm[kind] = replace_rows(cm[kind], source)
        cm[kind + "_sha256"] = sha(cm[kind])
    with pytest.raises(ValueError):
        assembly.project_culturemech(cm)
