"""#1431 pure native-hook/capture checks; no native operation or real packet.

Only named pure function ASTs are compiled. Importing source_bindings would
start producer capture, so these tests deliberately do not import that module,
create reports, inspect sources, export products or invoke historical replay.
"""

from __future__ import annotations

import ast
import hashlib
import io
import json
import re
from collections import Counter, defaultdict
from copy import deepcopy
from pathlib import Path
from types import SimpleNamespace

import pytest

from mediaingredientmech.export import source_assembly as assembly
from mediaingredientmech.export import source_conservation as conservation
from mediaingredientmech.export import source_input_selection as source_selection
from mediaingredientmech.review_claims import payload_sha256
from tests.test_source_assembly import canonical, raw_table, rows
from tests.test_source_input_writer import fixture, nested_count_fixture, pin, raw, select

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "src/mediaingredientmech/export/source_bindings.py"
TREE = ast.parse(SOURCE.read_text())
PURE_NAMES = {
    "_require",
    "_keys",
    "_json",
    "_sha",
    "_combined_input",
    "_combined_declaration",
    "_combined_source_inputs",
    "_combined_kg_inputs",
    "_combined_kg_accounting",
    "_combined_document",
    "_combined_graph_rows",
    "_source_capabilities",
}
NAMESPACE = {
    "json": json,
    "hashlib": hashlib,
    "Path": Path,
    "io": io,
    "re": re,
    "Counter": Counter,
    "defaultdict": defaultdict,
    "payload_sha256": payload_sha256,
    "conservation": conservation,
    "source_selection": source_selection,
    "CAPABILITY": "reviewed-source-bindings-v1",
    "culturemech_replay": SimpleNamespace(CAPABILITY="culturemech-intake-v3-replay-v1"),
}
exec(
    compile(
        ast.Module(
            body=[n for n in TREE.body if isinstance(n, ast.FunctionDef) and n.name in PURE_NAMES],
            type_ignores=[],
        ),
        str(SOURCE),
        "exec",
    ),
    NAMESPACE,
)


def function(name):
    return NAMESPACE[name]


def combined_fixture(*, nested=False, literal_payload=False, opaque_kg_cell=None):
    """Synthetic complete authority/closure, without native Selection or reports."""
    data = (
        nested_count_fixture(
            {
                "AGREEING_LABEL_AND_IDENTIFIER": 0,
                "AMBIGUOUS_OWNER": 0,
                "KNOWN_UNMAPPED_OWNER": 0,
                "NO_ACTIVE_OWNER": 1,
                "SOURCE_IDENTIFIER_CONFLICT": 0,
                "SOURCE_IDENTIFIER_MISSING": 0,
            }
        )
        if nested
        else fixture(extra_case=True)
    )
    captured, scope = data["captures"], data["scope"]
    refs = scope["authorities"]
    if literal_payload:
        original = json.loads(captured["original/cases.json"])
        original[0]["literal"]["quantities"] = {"amount": 0.125, "zero": -0.0, "unknown": None}
        original[0]["occurrence_declaration"] = {"status": "UNKNOWN", "count": None}
        captured["original/cases.json"] = raw(original)
        accounting = json.loads(captured["original/accounting.json"])
        accounting["case_ledger"]["sha256"] = pin(captured["original/cases.json"])["sha256"]
        captured["original/accounting.json"] = raw(accounting)
        transport = json.loads(captured["kg/manifest.json"])
        for key, path in (
            ("cases", "original/cases.json"),
            ("accounting", "original/accounting.json"),
        ):
            transport["inputs"][key].update(pin(captured[path]))
        captured["kg/manifest.json"] = raw(transport)
        crosswalk_path = data["controls"]["reviewed_crosswalk"]["path"]
        crosswalk = json.loads(captured[crosswalk_path])
        crosswalk["cases"][original[0]["case_id"]]["original_sha256"] = payload_sha256(original[0])
        captured[crosswalk_path] = raw(crosswalk)
        data["controls"]["reviewed_crosswalk"]["sha256"] = pin(captured[crosswalk_path])["sha256"]
        for ref in refs.values():
            ref["sha256"] = pin(captured[ref["path"]])["sha256"]
    original_owner = json.loads(captured[refs["kg_source_selection"]["path"]])
    nodes = rows(captured[refs["kg_nodes"]["path"]])
    if opaque_kg_cell is not None:
        for node in nodes:
            node["projection_declaration_json"] = opaque_kg_cell
    occurrences = rows(captured[refs["kg_occurrences"]["path"]])
    frozen_root, revision = "/synthetic/historical/kg", "a" * 40
    graph_rows, graph_bytes, graph_pins = {}, {}, {}
    for provider in original_owner["provider_counts"]:
        ids = [n["source_id"] for n in nodes if provider in json.loads(n["providers_json"])]
        graph_rows[provider, "nodes"] = [
            {"id": identifier, "name": '"literal quote"'} for identifier in ids
        ]
        graph_rows[provider, "edges"] = [
            {
                "subject": "TAXON:synthetic",
                "predicate": "biolink:has_part",
                "object": row["source_id"],
                "source_assertion_id": row["source_locator"],
                "literal_quantity": "0",
            }
            for row in occurrences
            if row["provider"] == provider
        ]
        for kind in ("nodes", "edges"):
            values = graph_rows[provider, kind]
            fields = list(values[0])
            raw_graph = (
                "\t".join(fields)
                + "\n"
                + "".join("\t".join(row[field] for field in fields) + "\n" for row in values)
            ).encode()
            member = f"data/transformed/{provider}/{kind}.tsv"
            graph_bytes[member] = raw_graph
            graph_pins[member] = {**pin(raw_graph), "columns": fields, "row_count": len(values)}
    for node in nodes:
        current = []
        for provider in json.loads(node["providers_json"]):
            graph = graph_rows[provider, "nodes"]
            position = next(i for i, row in enumerate(graph, 1) if row["id"] == node["source_id"])
            member = f"data/transformed/{provider}/nodes.tsv"
            current.append(
                {
                    "provider": provider,
                    "position": position,
                    "row": graph[position - 1],
                    "input": {"path": frozen_root + "/" + member, **pin(graph_bytes[member])},
                }
            )
        node["current_graph_node_rows_json"] = canonical(current)

    def save_role(role, value, *, binary=False):
        value = value if binary else raw(value)
        name = refs[role]["path"]
        captured[name] = value
        refs[role]["sha256"] = pin(value)["sha256"]

    save_role("kg_nodes", raw_table(list(nodes[0]), nodes), binary=True)
    transport = json.loads(captured[refs["kg_transport_manifest"]["path"]])
    transport["files"]["source-nodes.tsv"] = refs["kg_nodes"]["sha256"]
    save_role("kg_transport_manifest", transport)
    node_ledger = [
        {
            "kg_node_row": i,
            "node": node,
            "combined_global_row": 100 + i,
            "combined_row": {**node, "historical_only": "old CM offset"},
        }
        for i, node in enumerate(nodes, 1)
    ]
    ledger, positions = [], Counter()
    for ordinal, occurrence in enumerate(occurrences, 1):
        provider = occurrence["provider"]
        positions[provider] += 1
        position = positions[provider]
        member = f"data/transformed/{provider}/edges.tsv"
        graph_row = graph_rows[provider, "edges"][position - 1]
        combined = {**occurrence, "historical_only": "old CM offset"}
        ledger.append(
            {
                "provider": provider,
                "source_id": occurrence["source_id"],
                "kg_occurrence_row": ordinal,
                "kg_occurrence_row_sha256": payload_sha256(occurrence),
                "occurrence": occurrence,
                "combined_global_row": 1000 + ordinal,
                "combined_row_sha256": payload_sha256(combined),
                "combined_row": combined,
                "graph_member": member,
                "graph_sha256": pin(graph_bytes[member])["sha256"],
                "graph_row": position,
                "graph_row_sha256": payload_sha256(graph_row),
                "graph_full_row": graph_row,
            }
        )
    tsv_fields = (
        "provider source_id kg_occurrence_row combined_global_row graph_member graph_row "
        "kg_occurrence_row_sha256 combined_row_sha256 graph_row_sha256 full_row_json"
    ).split()
    save_role("kg_full_node_ledger", node_ledger)
    save_role("kg_full_row_ledger_json", ledger)
    save_role(
        "kg_full_row_ledger_tsv",
        raw_table(
            tsv_fields,
            [
                {**{key: str(row[key]) for key in tsv_fields[:-1]}, "full_row_json": canonical(row)}
                for row in ledger
            ],
        ),
        binary=True,
    )
    parent = raw({"historical": "separately selected parent"})
    proof = {
        "schema_version": 1,
        "historical_manifest_sha256": pin(parent)["sha256"],
        "kgm_revision": revision,
        "kg_manifest_sha256": refs["kg_transport_manifest"]["sha256"],
        "graph_members": graph_pins,
        "outputs": {
            filename: {
                **pin(captured[refs[role]["path"]]),
                "row_count": len(nodes) if role == "kg_full_node_ledger" else len(ledger),
            }
            for role, filename in (
                ("kg_full_node_ledger", "full-node-ledger.json"),
                ("kg_full_row_ledger_json", "full-row-ledger.json"),
                ("kg_full_row_ledger_tsv", "full-row-ledger.tsv"),
            )
        },
    }
    save_role("kg_row_reconciliation", proof)
    prior_files = {
        name: raw({"synthetic_partition": name})
        for name in (
            "manifest.json",
            "ingredient_mappings.sssom.tsv",
            "withheld_mappings.sssom.tsv",
            "mapping-dispositions.tsv",
        )
    }
    consumed = {
        "source_commit": "b" * 40,
        "directory": "prior",
        "files": {name: pin(value)["sha256"] for name, value in prior_files.items()},
        "manifest_sha256": pin(prior_files["manifest.json"])["sha256"],
    }
    release_record = raw(
        {
            "source_commit": consumed["source_commit"],
            "manifest_sha256": consumed["manifest_sha256"],
            "files": {k: v for k, v in consumed["files"].items() if k != "manifest.json"},
        }
    )
    member_bytes = {"snapshots/" + name: value for name, value in graph_bytes.items()}
    member_bytes.update({"prior/" + name: value for name, value in prior_files.items()})
    member_bytes.update(
        {
            "evidence/parent.json": parent,
            "snapshots/mappings/mim_reviewed_release.json": release_record,
        }
    )
    closure = {
        "schema_version": 1,
        "upstream_revision": revision,
        "mim_revision": consumed["source_commit"],
        "consumed_reviewed": consumed,
        "parent_manifest": {"path": "evidence/parent.json", "sha256": pin(parent)["sha256"]},
        "files": {name: pin(value) for name, value in member_bytes.items()},
    }
    save_role("kg_source_manifest", closure)
    for member, value in member_bytes.items():
        captured[(Path(refs["kg_source_manifest"]["path"]).parent / member).as_posix()] = value
    owner = original_owner
    owner.update(
        schema_version=1,
        status="REVIEWED_HISTORICAL_SOURCE_CLOSURE",
        production_admission=False,
        selected_kgm={"root": frozen_root, "revision": revision},
        consumed_prior_mim={
            "source_commit": consumed["source_commit"],
            "partition_pins": consumed,
            "committed_pin_record": {"path": "/historical/pin.json", **pin(release_record)},
        },
    )
    owner["kg_transport_manifest_sha256"] = refs["kg_transport_manifest"]["sha256"]
    for key, role in (
        ("source_receipt", "kg_source_manifest"),
        ("row_reconciliation", "kg_row_reconciliation"),
    ):
        owner[key].update(pin(captured[refs[role]["path"]]))
    for role, filename in (
        ("kg_full_node_ledger", "full-node-ledger.json"),
        ("kg_full_row_ledger_json", "full-row-ledger.json"),
        ("kg_full_row_ledger_tsv", "full-row-ledger.tsv"),
    ):
        owner["ledgers"][filename].update(pin(captured[refs[role]["path"]]))
    save_role("kg_source_selection", owner)
    declaration_path = data["controls"]["declaration"]["path"]
    declaration = json.loads(captured[declaration_path])
    declaration["original_source_scope"] = deepcopy(scope)
    captured[declaration_path] = canonical(declaration).encode()
    data["controls"]["declaration"]["sha256"] = pin(captured[declaration_path])["sha256"]
    selected = select(data)
    args = {
        key: selected[key]
        for key in (
            "cm",
            "kg",
            "family_paths",
            "curie_map",
            "historical_obligations",
            "reviewed_crosswalk",
        )
    }
    candidate = assembly.combine_sources(assembly.project_culturemech(args["cm"]), **args)
    artifacts = {
        "cm_nodes": candidate["cm"]["nodes"],
        "cm_occurrences": candidate["cm"]["occurrences"],
        "cm_raw_row_map": raw(candidate["cm"]["raw_row_map"]),
        "cm_case_crosswalk": raw(candidate["cm"]["case_crosswalk"]),
        "combined_nodes": candidate["nodes"],
        "combined_occurrences": candidate["occurrences"],
        "combined_position_map": raw(candidate["position_map"]),
        "cm_reconciliation": candidate["reconciliation"],
        "kg_provider_cases": raw(candidate["kg_provider_cases"]),
        "historical_obligations": raw(candidate["historical_obligations"]),
        "obligation_crosswalk": raw(candidate["obligation_crosswalk"]),
    }
    captured.update({scope["artifacts"][role]: value for role, value in artifacts.items()})
    captured["output/projection-declaration.json"] = captured[declaration_path]
    hashes = {name: pin(value)["sha256"] for name, value in captured.items()}
    cm_selection = SimpleNamespace(
        path=refs["culturemech_package"]["path"],
        required_inputs={name: digest for name, digest in hashes.items() if name.startswith("cm/")},
        proof_paths=selected["selected_metadata_paths"],
        declaration=lambda name: {"path": name, "sha256": hashes[name]},
    )
    inputs = SimpleNamespace(
        bytes=captured,
        hashes=hashes,
        cm_replay=cm_selection,
        cm_required_inputs={},
        combined_conservation=False,
    )
    review = {
        "inputs": dict(hashes),
        "culturemech_intake_replay": refs["culturemech_package"],
        "source": {
            "nodes": scope["artifacts"]["combined_nodes"],
            "nodes_sha256": pin(candidate["nodes"])["sha256"],
            "occurrences": scope["artifacts"]["combined_occurrences"],
            "occurrences_sha256": pin(candidate["occurrences"])["sha256"],
            "id_column": "source_id",
            "label_column": "source_label",
            "occurrence_id_column": "source_id",
            "curie_map": selected["curie_map"],
        },
    }
    return inputs, review, scope, candidate, args


def run_combined(inputs, review):
    return function("_combined_source_inputs")(
        inputs, review, rows(inputs.bytes[review["source"]["nodes"]])
    )


def test_complete_combined_synthetic_hook_preserves_every_input_and_historical_position():
    inputs, review, scope, candidate, args = combined_fixture()
    before = deepcopy((inputs.bytes, inputs.hashes, review))
    required = run_combined(inputs, review)
    assert inputs.combined_conservation is True
    assert (inputs.bytes, inputs.hashes, review) == before
    assert all(required[name] == inputs.hashes[name] for name in scope["artifacts"].values())
    assert all(required[ref["path"]] == ref["sha256"] for ref in scope["authorities"].values())
    closure = json.loads(inputs.bytes[scope["authorities"]["kg_source_manifest"]["path"]])
    assert all(
        required["authority/" + name] == pin["sha256"] for name, pin in closure["files"].items()
    )
    assert (
        required["output/projection-declaration.json"]
        == inputs.hashes["output/projection-declaration.json"]
    )
    assert (
        conservation.validate_source_conservation(candidate, **args)["scientific_approval"] is False
    )
    old_ledger = json.loads(inputs.bytes[scope["authorities"]["kg_full_row_ledger_json"]["path"]])
    assert old_ledger[0]["combined_global_row"] == 1001  # Deliberately not the new position.


@pytest.mark.parametrize("nested", [False, True])
def test_full_hook_preserves_literal_quantities_unknowns_and_nested_counts(nested):
    inputs, review, scope, candidate, _ = combined_fixture(nested=nested, literal_payload=True)
    before = deepcopy(inputs.bytes)
    required = run_combined(inputs, review)
    assert inputs.bytes == before
    original = json.loads(inputs.bytes[scope["authorities"]["original_case_ledger"]["path"]])[0]
    actual = candidate["kg_provider_cases"][0]
    assert canonical(actual) == canonical(original)
    assert actual["literal"]["quantities"] == {"amount": 0.125, "zero": -0.0, "unknown": None}
    assert '"zero":-0.0' in canonical(actual)
    assert actual["occurrence_declaration"] == {"status": "UNKNOWN", "count": None}
    assert actual["holds"] == ["IDENTITY_FORM"]
    assert "cm/consumer/prepared/intake.json" in required


@pytest.mark.parametrize("attack", ["no-replay", "package", "metadata", "columns", "source-path"])
def test_combined_requires_exact_native_selection_and_source_contract(attack):
    inputs, review, _, _, _ = combined_fixture()
    if attack == "no-replay":
        inputs.cm_replay = None
    elif attack == "package":
        inputs.cm_replay.path = "cm/consumer/prepared/intake.json"
    elif attack == "metadata":
        inputs.cm_replay.declaration = lambda name: {"path": name, "sha256": "0" * 64}
    elif attack == "columns":
        review["source"]["occurrence_id_column"] = "label"
    else:
        review["source"]["occurrences"] = "unrelated.tsv"
    with pytest.raises(ValueError):
        run_combined(inputs, review)
    assert inputs.combined_conservation is False


@pytest.mark.parametrize("group", ["authorities", "artifacts"])
def test_every_role_must_be_an_explicit_current_input(group):
    inputs, review, scope, _, _ = combined_fixture()
    for ref in scope[group].values():
        name = ref["path"] if isinstance(ref, dict) else ref
        omitted = deepcopy(review)
        omitted["inputs"].pop(name)
        with pytest.raises(ValueError, match="explicitly pinned"):
            run_combined(inputs, omitted)
        assert inputs.combined_conservation is False


@pytest.mark.parametrize(
    "attack", ["missing", "changed", "conflicting-pin", "parent-traversal", "absolute"]
)
def test_combined_input_rejects_unselected_or_changed_capture(attack):
    inputs, review, _, _, _ = combined_fixture()
    name = "output/projection-declaration.json"
    if attack == "missing":
        del inputs.bytes[name]
    elif attack == "changed":
        inputs.bytes[name] += b" "
    elif attack == "conflicting-pin":
        inputs.hashes[name] = "0" * 64
    elif attack == "parent-traversal":
        name = "../outside"
    else:
        name = "/outside"
    with pytest.raises(ValueError):
        function("_combined_input")(inputs, review, name)


@pytest.mark.parametrize(
    "attack", ["missing-declaration", "different-path", "different-hash", "different-inline"]
)
def test_all_cm_rows_must_agree_on_one_declaration(attack):
    inputs, review, _, _, _ = combined_fixture()
    source_rows = rows(inputs.bytes[review["source"]["nodes"]])
    target = source_rows[1]
    if attack == "missing-declaration":
        target["projection_declaration_json"] = ""
    elif attack == "different-path":
        target["projection_declaration_path"] = "other/declaration.json"
    elif attack == "different-hash":
        target["projection_declaration_sha256"] = "0" * 64
    else:
        target["projection_declaration_json"] += " "
    with pytest.raises(ValueError):
        function("_combined_source_inputs")(inputs, review, source_rows)


def repin_artifact(inputs, review, path, value):
    inputs.bytes[path] = value
    inputs.hashes[path] = review["inputs"][path] = pin(value)["sha256"]
    for kind in ("nodes", "occurrences"):
        if review["source"][kind] == path:
            review["source"][kind + "_sha256"] = pin(value)["sha256"]


@pytest.mark.parametrize(
    "role",
    [
        "cm_raw_row_map",
        "cm_case_crosswalk",
        "combined_position_map",
        "kg_provider_cases",
        "historical_obligations",
        "obligation_crosswalk",
    ],
)
def test_independent_inverse_rejects_rehashed_sidecar_loss(role):
    inputs, review, scope, _, _ = combined_fixture()
    path = scope["artifacts"][role]
    value = json.loads(inputs.bytes[path])
    if isinstance(value, list):
        value.pop()
    else:
        value["cases"].pop(next(iter(value["cases"])))
    repin_artifact(inputs, review, path, raw(value))
    with pytest.raises(ValueError):
        run_combined(inputs, review)
    assert inputs.combined_conservation is False


@pytest.mark.parametrize("role", ["cm_occurrences", "combined_occurrences", "cm_reconciliation"])
def test_independent_inverse_rejects_rehashed_table_loss(role):
    inputs, review, scope, _, _ = combined_fixture()
    path = scope["artifacts"][role]
    values = rows(inputs.bytes[path])
    header = list(values[0])
    values.pop()
    repin_artifact(inputs, review, path, raw_table(header, values))
    with pytest.raises(ValueError):
        run_combined(inputs, review)
    assert inputs.combined_conservation is False


@pytest.mark.parametrize(
    "attack", ["missing-member", "member-size", "member-pin", "parent", "prior", "revision"]
)
def test_closure_members_parent_and_prior_consumption_are_required(attack):
    inputs, review, scope, _, _ = combined_fixture()
    refs = scope["authorities"]
    path = refs["kg_source_manifest"]["path"]
    receipt = json.loads(inputs.bytes[path])
    member = next(iter(receipt["files"]))
    if attack == "missing-member":
        review["inputs"].pop("authority/" + member)
    elif attack == "member-size":
        receipt["files"][member]["bytes"] = True
    elif attack == "member-pin":
        receipt["files"][member]["sha256"] = "0" * 64
    elif attack == "parent":
        receipt["parent_manifest"]["sha256"] = "0" * 64
    elif attack == "prior":
        receipt["consumed_reviewed"]["source_commit"] = "c" * 40
    else:
        receipt["upstream_revision"] = "c" * 40
    inputs.bytes[path] = raw(receipt)
    with pytest.raises(ValueError):
        function("_combined_kg_inputs")(inputs, review, scope)


@pytest.mark.parametrize(
    "attack",
    [
        "node-position",
        "node-payload",
        "provider",
        "occurrence-position",
        "occurrence-payload",
        "graph-row",
        "graph-hash",
        "tsv-full-row",
        "tsv-scalar",
        "duplicate-occurrence",
        "missing-occurrence",
    ],
)
def test_full_ledger_accounting_refuses_literal_and_coordinate_changes(attack):
    inputs, _, scope, candidate, args = combined_fixture()
    result = conservation.validate_source_conservation(candidate, **args)
    refs = scope["authorities"]
    if attack.startswith("node-"):
        path = refs["kg_full_node_ledger"]["path"]
        value = json.loads(inputs.bytes[path])
        if attack == "node-position":
            value[0]["kg_node_row"] = True
        else:
            value[0]["node"]["source_label"] = "changed"
        inputs.bytes[path] = raw(value)
    elif attack.startswith("tsv-"):
        path = refs["kg_full_row_ledger_tsv"]["path"]
        value = rows(inputs.bytes[path])
        value[0]["full_row_json" if attack == "tsv-full-row" else "source_id"] = "{}"
        inputs.bytes[path] = raw_table(list(value[0]), value)
    else:
        path = refs["kg_full_row_ledger_json"]["path"]
        value = json.loads(inputs.bytes[path])
        if attack == "provider":
            value[0]["provider"] = "metatraits"
        elif attack == "occurrence-position":
            value[0]["kg_occurrence_row"] = True
        elif attack == "occurrence-payload":
            value[0]["occurrence"]["context_json"] = "{}"
        elif attack == "graph-row":
            value[0]["graph_row"] = True
        elif attack == "graph-hash":
            value[0]["graph_row_sha256"] = "0" * 64
        elif attack == "duplicate-occurrence":
            value.append(deepcopy(value[0]))
        else:
            value.pop()
        inputs.bytes[path] = raw(value)
    with pytest.raises(ValueError):
        function("_combined_kg_accounting")(inputs, scope, result)


def test_converse_incidence_refuses_an_extra_graph_edge_with_coherent_metadata():
    inputs, _, scope, candidate, args = combined_fixture()
    refs = scope["authorities"]
    proof_path, closure_path = (
        refs["kg_row_reconciliation"]["path"],
        refs["kg_source_manifest"]["path"],
    )
    proof, closure = json.loads(inputs.bytes[proof_path]), json.loads(inputs.bytes[closure_path])
    member = "data/transformed/metatraits/edges.tsv"
    frozen = "snapshots/" + member
    path = "authority/" + frozen
    graph = inputs.bytes[path]
    inputs.bytes[path] += graph.splitlines(keepends=True)[1]
    new_pin = pin(inputs.bytes[path])
    proof["graph_members"][member].update(new_pin)
    proof["graph_members"][member]["row_count"] += 1
    closure["files"][frozen] = new_pin
    ledger_path = refs["kg_full_row_ledger_json"]["path"]
    ledger = json.loads(inputs.bytes[ledger_path])
    for entry in ledger:
        if entry["graph_member"] == member:
            entry["graph_sha256"] = new_pin["sha256"]
    tsv_path = refs["kg_full_row_ledger_tsv"]["path"]
    tsv = rows(inputs.bytes[tsv_path])
    for row, entry in zip(tsv, ledger, strict=True):
        row["full_row_json"] = canonical(entry)
    inputs.bytes[ledger_path] = raw(ledger)
    inputs.bytes[tsv_path] = raw_table(list(tsv[0]), tsv)
    inputs.bytes[proof_path], inputs.bytes[closure_path] = raw(proof), raw(closure)
    with pytest.raises(ValueError, match="converse incidence"):
        function("_combined_kg_accounting")(
            inputs, scope, conservation.validate_source_conservation(candidate, **args)
        )


@pytest.mark.parametrize("replacement", [1, True, 1.0])
def test_graph_ordinal_types_and_duplicate_incidence_survive_coherent_tsv_rewrite(replacement):
    inputs, _, scope, candidate, args = combined_fixture()
    refs = scope["authorities"]
    json_path, tsv_path = (
        refs["kg_full_row_ledger_json"]["path"],
        refs["kg_full_row_ledger_tsv"]["path"],
    )
    ledger, tsv = json.loads(inputs.bytes[json_path]), rows(inputs.bytes[tsv_path])
    # The last literal MediaDive occurrence equals the first, but belongs to a
    # second real graph incidence. Reusing its first ordinal must not collapse it.
    assert ledger[-1]["occurrence"] == ledger[0]["occurrence"]
    assert ledger[-1]["graph_row"] == 2
    ledger[-1]["graph_row"] = replacement
    tsv[-1]["graph_row"] = str(replacement)
    tsv[-1]["full_row_json"] = canonical(ledger[-1])
    inputs.bytes[json_path] = raw(ledger)
    inputs.bytes[tsv_path] = raw_table(list(tsv[0]), tsv)
    with pytest.raises(
        ValueError, match="converse incidence" if type(replacement) is int else "edge provenance"
    ):
        function("_combined_kg_accounting")(
            inputs, scope, conservation.validate_source_conservation(candidate, **args)
        )


def test_unquoted_graph_parser_preserves_quotes_and_unchanged_character_limit():
    import csv

    before = csv.field_size_limit()
    assert list(function("_combined_graph_rows")(b'id\tvalue\nx\t"quoted"\n')) == [
        ["id", "value"],
        {"id": "x", "value": '"quoted"'},
    ]
    value = "é" * before
    assert list(function("_combined_graph_rows")(("id\n" + value + "\n").encode()))[1] == {
        "id": value
    }
    with pytest.raises(ValueError):
        list(function("_combined_graph_rows")(("id\n" + value + "é\n").encode()))
    assert csv.field_size_limit() == before


@pytest.mark.parametrize("value", [True, 1.0, "1", None, 0, -1])
@pytest.mark.parametrize("field", ["kg_node_row", "combined_global_row"])
def test_physical_node_ordinals_are_positive_json_integers(field, value):
    inputs, _, scope, candidate, args = combined_fixture()
    path = scope["authorities"]["kg_full_node_ledger"]["path"]
    ledger = json.loads(inputs.bytes[path])
    ledger[0][field] = value
    inputs.bytes[path] = raw(ledger)
    with pytest.raises(ValueError):
        function("_combined_kg_accounting")(
            inputs, scope, conservation.validate_source_conservation(candidate, **args)
        )


@pytest.mark.parametrize("value", [True, 1.0, "1", None, -1])
@pytest.mark.parametrize("kind", ["ledger", "graph"])
def test_physical_counts_reject_coercible_types(kind, value):
    inputs, review, scope, candidate, args = combined_fixture()
    path = scope["authorities"]["kg_row_reconciliation"]["path"]
    proof = json.loads(inputs.bytes[path])
    if kind == "ledger":
        proof["outputs"]["full-node-ledger.json"]["row_count"] = value
    else:
        proof["graph_members"]["data/transformed/mediadive/nodes.tsv"]["row_count"] = value
    inputs.bytes[path] = raw(proof)
    with pytest.raises(ValueError):
        if kind == "ledger":
            function("_combined_kg_inputs")(inputs, review, scope)
        else:
            function("_combined_kg_accounting")(
                inputs, scope, conservation.validate_source_conservation(candidate, **args)
            )


def test_pure_extraction_has_no_native_operation_or_file_io():
    assert {
        n.name for n in TREE.body if isinstance(n, ast.FunctionDef) and n.name in PURE_NAMES
    } == PURE_NAMES
    forbidden = {
        "open",
        "read_bytes",
        "write_bytes",
        "read_text",
        "write_text",
        "_load",
        "_prepare",
        "_native",
        "Selection",
        "replay",
        "inspect_candidates",
        "export_candidate",
        "validate_candidate",
        "project_culturemech",
        "combine_sources",
    }
    for node in TREE.body:
        if isinstance(node, ast.FunctionDef) and node.name in PURE_NAMES:
            names = {
                n.func.id if isinstance(n.func, ast.Name) else n.func.attr
                for n in ast.walk(node)
                if isinstance(n, ast.Call) and isinstance(n.func, (ast.Name, ast.Attribute))
            }
            assert not names & forbidden


@pytest.mark.parametrize("replay", [False, True])
def test_existing_routes_never_claim_combined_conservation(replay):
    inputs = SimpleNamespace(combined_conservation=False)
    assert function("_source_capabilities")(inputs, {} if replay else None) == (
        ["reviewed-source-bindings-v1", "culturemech-intake-v3-replay-v1"]
        if replay
        else ["reviewed-source-bindings-v1"]
    )
    assert function("_combined_declaration")([{"source_id": "SOURCE:ordinary"}]) is None


def test_combined_capability_requires_completed_replay():
    inputs = SimpleNamespace(combined_conservation=True)
    with pytest.raises(ValueError, match="completed CM replay"):
        function("_source_capabilities")(inputs, None)
    assert function("_source_capabilities")(inputs, {"synthetic": "call-return only"}) == [
        "reviewed-source-bindings-v1",
        "culturemech-intake-v3-replay-v1",
        "cm-v3-kgm-source-conservation-v1",
    ]


def test_historical_declaration_retains_limited_route():
    row = {
        "source_id": "MIMCMREFv1:historical",
        "projection_declaration_json": canonical(
            {
                "original_source_scope": {"complete_CM_cases": 1, "status": "historical"},
            }
        ),
    }
    assert function("_combined_declaration")([row]) is None


@pytest.mark.parametrize(
    "scope",
    [
        None,
        [],
        "profile",
        {"profile": "unknown"},
        {"artifacts": {}},
        {"profile": source_selection.PROFILE},
    ],
)
def test_malformed_or_unknown_advertised_profiles_refuse(scope):
    # #1555: malformed scope is a CM declaration only with a real CM marker;
    # unrelated providers may retain an opaque null/list/scalar extra cell.
    row = {
        "source_id": conservation.CM_PREFIX + ":synthetic",
        "projection_contract": conservation.DOMAIN,
        "projection_declaration_json": canonical({"original_source_scope": scope}),
    }
    with pytest.raises(ValueError):
        function("_combined_declaration")([row])


@pytest.mark.parametrize(
    "opaque",
    [
        "",
        '{"another_provider_schema":1}',
        "null",
        "[]",
        '"profile"',
        "not JSON",
        '{"original_source_scope":null}',
        '{"original_source_scope":[]}',
        '{"original_source_scope":{"another_provider_schema":1}}',
    ],
)
def test_1555_ordinary_extra_cells_remain_literal_and_do_not_activate(opaque):
    inputs = SimpleNamespace(cm_replay=None, combined_conservation=False)
    values = [{"source_id": "SOURCE:ordinary", "projection_declaration_json": opaque}]
    before = deepcopy(values)
    assert function("_combined_source_inputs")(inputs, {}, values) == {}
    assert values == before
    assert inputs.combined_conservation is False


@pytest.mark.parametrize(
    "opaque",
    [
        '{"another_provider_schema":1}',
        "null",
        "not JSON",
        '{"original_source_scope":{"another_provider_schema":1}}',
    ],
)
def test_1555_combined_inverse_preserves_original_opaque_kg_cells(opaque):
    inputs, review, scope, _, _ = combined_fixture(opaque_kg_cell=opaque)
    before = deepcopy((inputs.bytes, inputs.hashes, review))
    selected = rows(inputs.bytes[scope["authorities"]["kg_nodes"]["path"]])
    combined = rows(inputs.bytes[review["source"]["nodes"]])
    kg = [r for r in combined if not r["source_id"].startswith(conservation.CM_PREFIX + ":")]
    assert len(kg) == len(selected) > 0
    assert [r["projection_declaration_json"] for r in kg] == [opaque] * len(selected)
    assert function("_combined_declaration")(combined) is not None
    required = run_combined(inputs, review)
    assert scope["authorities"]["kg_nodes"]["path"] in required
    assert inputs.combined_conservation is True
    assert (inputs.bytes, inputs.hashes, review) == before


@pytest.mark.parametrize("marker", ["prefix", "contract"])
@pytest.mark.parametrize(
    "malformed",
    [
        "not JSON",
        "null",
        "[]",
        "{}",
        '{"original_source_scope":null}',
        '{"original_source_scope":[]}',
        '{"original_source_scope":{"profile":"unknown"}}',
        '{"original_source_scope":{"artifacts":{}}}',
    ],
)
def test_1555_either_actual_cm_marker_refuses_malformed_declarations(marker, malformed):
    row = {"source_id": "SOURCE:ordinary", "projection_declaration_json": malformed}
    if marker == "prefix":
        row["source_id"] = conservation.CM_PREFIX + ":synthetic"
    else:
        row["projection_contract"] = conservation.DOMAIN
    with pytest.raises(ValueError):
        function("_combined_declaration")([row])


@pytest.mark.parametrize(
    "scope",
    [
        {"profile": "unknown"},
        {"authorities": {}},
        {"artifacts": {}},
        {"profile": source_selection.PROFILE},
    ],
)
def test_1555_unmarked_explicit_profile_cannot_fall_back_to_ordinary(scope):
    row = {
        "source_id": "SOURCE:ordinary",
        "projection_declaration_json": canonical({"original_source_scope": scope}),
    }
    with pytest.raises(ValueError):
        function("_combined_declaration")([row])


def test_capture_inventories_include_inverse_selector_codec_but_not_writer():
    producer = ast.parse((ROOT / "src/mediaingredientmech/export/source_producer.py").read_text())
    modules = ast.literal_eval(
        next(
            n.value
            for n in producer.body
            if isinstance(n, ast.Assign)
            and any(isinstance(t, ast.Name) and t.id == "MODULES" for t in n.targets)
        )
    )
    paths_node = next(
        n.value
        for n in TREE.body
        if isinstance(n, ast.Assign)
        and any(isinstance(t, ast.Name) and t.id == "PRODUCER_PATHS" for t in n.targets)
    )
    paths = {n.value for n in paths_node.elts if isinstance(n, ast.Constant)}
    for name in ("source_input_selection", "source_conservation", "culturemech_layout"):
        assert "mediaingredientmech.export." + name in modules
        assert "src/mediaingredientmech/export/" + name + ".py" in paths
    assert not any(
        "source_assembly" in name or "assemble_source_inputs" in name for name in (*modules, *paths)
    )
    imports = {
        alias.name
        for n in TREE.body
        if isinstance(n, ast.ImportFrom) and n.module == "mediaingredientmech.export"
        for alias in n.names
    }
    assert {"source_conservation", "source_input_selection"} <= imports
    assert "source_assembly" not in imports


def test_hook_precedes_targets_and_both_consumers_share_prepare():
    prepare = next(n for n in TREE.body if isinstance(n, ast.FunctionDef) and n.name == "_prepare")
    hook = next(
        n
        for n in ast.walk(prepare)
        if isinstance(n, ast.Call)
        and isinstance(n.func, ast.Name)
        and n.func.id == "_combined_source_inputs"
    )
    selection = next(
        n
        for n in ast.walk(prepare)
        if isinstance(n, ast.Call)
        and isinstance(n.func, ast.Attribute)
        and n.func.attr == "Selection"
    )
    payloads = next(
        n
        for n in ast.walk(prepare)
        if isinstance(n, ast.Assign)
        and any(isinstance(t, ast.Name) and t.id == "payloads" for t in n.targets)
    )
    assert selection.lineno < hook.lineno < payloads.lineno
    for name in ("inspect_candidates", "_load"):
        node = next(n for n in TREE.body if isinstance(n, ast.FunctionDef) and n.name == name)
        assert any(
            isinstance(n, ast.Call) and isinstance(n.func, ast.Name) and n.func.id == "_prepare"
            for n in ast.walk(node)
        )
    expected = next(
        n for n in TREE.body if isinstance(n, ast.FunctionDef) and n.name == "expected_products"
    )
    replay = next(
        n
        for n in ast.walk(expected)
        if isinstance(n, ast.Call) and isinstance(n.func, ast.Attribute) and n.func.attr == "replay"
    )
    membership = next(
        n
        for n in ast.walk(expected)
        if isinstance(n, ast.Call)
        and isinstance(n.func, ast.Name)
        and n.func.id == "_source_capabilities"
    )
    assert replay.lineno < membership.lineno
