"""#1387 inventories, #1388 independent identities, and #1389 captured graph bytes."""

from __future__ import annotations

import copy
import csv
import hashlib
import json
from pathlib import Path
from types import SimpleNamespace

import pytest
import yaml

from mediaingredientmech.export.kgx import export_graph
from mediaingredientmech.identity_projection_graph import edge_identity
from mediaingredientmech.validation.current_semantic_release import (
    Inputs,
    current_graph,
    hold_payloads,
    independent_pair,
)
from tests.test_semantic_release import reviewed_bundle as original_bundle

ROOT = Path(__file__).resolve().parents[1]
SOURCE = "mappings/ingredient_mappings.sssom.tsv"
OWNER = "data/ingredients/mapped/Water.yaml"


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def write_json(path, value):
    path.write_text(json.dumps(value, sort_keys=True, indent=2) + "\n")


def graph_rows(path):
    with path.open(newline="") as stream:
        reader = csv.DictReader(stream, delimiter="\t", quoting=csv.QUOTE_NONE)
        return reader.fieldnames, list(reader)


def replace_member(root, bundle, name, fields, entries):
    """Model an attacker updating ordinary member hashes after a payload edit."""
    path = root / bundle / name
    with path.open("w", newline="") as stream:
        writer = csv.DictWriter(
            stream,
            fieldnames=fields,
            delimiter="\t",
            quoting=csv.QUOTE_NONE,
            quotechar=None,
            lineterminator="\n",
        )
        writer.writeheader()
        writer.writerows(entries)
    manifest_path = root / bundle / "manifest.json"
    manifest = json.loads(manifest_path.read_text())
    manifest["members"][name].update(sha256=sha(path), bytes=path.stat().st_size)
    write_json(manifest_path, manifest)


@pytest.fixture
def native_bundle(tmp_path):
    # The existing fixture invokes the real native graph exporter. Current
    # validation additionally binds implementation bytes in its owned root.
    root, _ = original_bundle.__wrapped__(tmp_path)
    manifest = json.loads((root / "bundle/manifest.json").read_text())
    for name, expected in manifest["implementation"].items():
        relative = "src/mediaingredientmech/" + name
        raw = (ROOT / relative).read_bytes()
        assert hashlib.sha256(raw).hexdigest() == expected
        destination = root / relative
        destination.parent.mkdir(parents=True, exist_ok=True)
        destination.write_bytes(raw)
    return root


def test_native_current_graph_preserves_exact_owner_and_mapping_inventory(native_bundle):
    inputs = Inputs(native_bundle)
    records, hashes, mappings, edges = current_graph(inputs, "bundle")
    assert set(records) == {OWNER, "data/ingredients/unmapped/Unknown.yaml"}
    assert {record["mim_id"] for record in records.values()} == {
        "MIM:0000001",
        "MIM:0000002",
    }
    assert hashes == {name: sha(native_bundle / name) for name in records}
    assert len(mappings) == len(edges) == 1
    assert mappings[0]["subject_id"] == edges[0]["subject"] == "MIM:0000001"
    assert mappings[0]["object_id"] == edges[0]["object"] == "CHEBI:15377"
    assert edges[0]["predicate"] == "biolink:exact_match"
    assert edges[0]["relation"] == "skos:exactMatch"
    assert json.loads(edges[0]["assertion_json"]) == mappings[0]
    assert {OWNER, SOURCE, "bundle/manifest.json", "bundle/mim_edges.tsv"} <= inputs.raw.keys()
    inputs.recheck()


@pytest.mark.parametrize("changed", ["owner", "canonical"])
def test_rehashed_current_source_cannot_certify_a_stale_graph(native_bundle, changed):
    root = native_bundle
    relative = OWNER if changed == "owner" else SOURCE
    path = root / relative
    if changed == "owner":
        record = yaml.safe_load(path.read_text())
        record["identifier"] = "CHEBI:999"
        path.write_text(yaml.safe_dump(record))
    else:
        path.write_text(path.read_text().replace("CHEBI:15377", "CHEBI:999"))
    manifest_path = root / "bundle/manifest.json"
    manifest = json.loads(manifest_path.read_text())
    manifest["inputs"][relative] = sha(path)
    write_json(manifest_path, manifest)
    expected = (
        "graph owner payload differs"
        if changed == "owner"
        else "Mapping does not identify the current source record"
    )
    with pytest.raises(ValueError, match=expected):
        current_graph(Inputs(root), "bundle")


@pytest.mark.parametrize("attack", ["missing", "duplicate"])
def test_rehashed_graph_cannot_omit_or_duplicate_a_current_assertion(native_bundle, attack):
    fields, edges = graph_rows(native_bundle / "bundle/mim_edges.tsv")
    assert len(edges) == 1
    changed = [] if attack == "missing" else [edges[0], copy.deepcopy(edges[0])]
    replace_member(native_bundle, "bundle", "mim_edges.tsv", fields, changed)
    with pytest.raises(ValueError, match="coverage differs|Duplicate graph assertion"):
        current_graph(Inputs(native_bundle), "bundle")


def test_rehashed_graph_cannot_drop_an_unmapped_owner(native_bundle):
    fields, nodes = graph_rows(native_bundle / "bundle/mim_nodes.tsv")
    retained = [node for node in nodes if node["id"] != "MIM:0000002"]
    assert len(retained) == len(nodes) - 1
    replace_member(native_bundle, "bundle", "mim_nodes.tsv", fields, retained)
    with pytest.raises(ValueError, match="incomplete current graph owner inventory"):
        current_graph(Inputs(native_bundle), "bundle")


@pytest.mark.parametrize("member", ["mim_nodes.tsv", "mim_edges.tsv"])
def test_1389_present_graph_files_cannot_replace_required_manifest_members(native_bundle, member):
    path = native_bundle / "bundle/manifest.json"
    manifest = json.loads(path.read_text())
    assert (native_bundle / "bundle" / member).is_file()
    del manifest["members"][member]
    write_json(path, manifest)
    with pytest.raises(ValueError, match="graph manifest omits required node/edge members"):
        current_graph(Inputs(native_bundle), "bundle")


@pytest.mark.parametrize("member", ["mim_nodes.tsv", "mim_edges.tsv"])
def test_1389_late_graph_path_change_cannot_replace_captured_semantics(
    native_bundle, monkeypatch, member
):
    inputs = Inputs(native_bundle)
    relative = "bundle/" + member
    path = native_bundle / relative
    original = path.read_bytes()
    native_read = inputs.read
    mutations = []

    def capture_then_change_path(name, expected=None):
        raw = native_read(name, expected)
        if name == relative:
            # Inject actual late filesystem drift after the genuine hash-bound
            # capture; neither projection nor the input reader is stubbed.
            changed = raw.replace(b"MIM:0000001", b"MIM:9999999")
            assert changed != raw
            path.write_bytes(changed)
            mutations.append(name)
        return raw

    monkeypatch.setattr(inputs, "read", capture_then_change_path)
    records, _, mappings, edges = current_graph(inputs, "bundle")
    assert mutations == [relative]
    assert inputs.raw[relative] == original != path.read_bytes()
    assert records[OWNER]["mim_id"] == "MIM:0000001"
    assert mappings[0]["subject_id"] == edges[0]["subject"] == "MIM:0000001"
    assert edges[0]["object"] == "CHEBI:15377"
    with pytest.raises(ValueError, match="late input drift: " + relative):
        inputs.recheck()


def test_native_broad_mapping_cannot_be_rehashed_into_a_subclass(native_bundle):
    path = native_bundle / SOURCE
    original = path.read_text()
    reader = csv.DictReader(
        (line for line in original.splitlines() if not line.startswith("#")), delimiter="\t"
    )
    parent = next(reader)
    parent.update(
        predicate_id="skos:broadMatch", object_id="CHEBI:24431", object_label="chemical entity"
    )
    # Preserve the exact primary identity sibling while introducing a separate,
    # explicitly synthetic broader mapping for the typed-edge regression.
    path.write_text(original + "\t".join(parent[field] for field in reader.fieldnames) + "\n")
    export_graph(native_bundle, native_bundle / "broad")
    _, _, mappings, native_edges = current_graph(Inputs(native_bundle), "broad")
    assert {mapping["predicate_id"] for mapping in mappings} == {
        "skos:exactMatch",
        "skos:broadMatch",
    }
    assert any(edge["predicate"] == "biolink:broad_match" for edge in native_edges)
    fields, edges = graph_rows(native_bundle / "broad/mim_edges.tsv")
    broader = next(edge for edge in edges if edge["relation"] == "skos:broadMatch")
    broader["predicate"] = "biolink:subclass_of"
    # Rebuild the typed assertion ID as well: neither the manifest nor a fresh
    # assertion ID can authorize a different scientific relation.
    broader["id"] = edge_identity(broader)
    replace_member(native_bundle, "broad", "mim_edges.tsv", fields, edges)
    with pytest.raises(ValueError, match="Graph edge projection differs"):
        current_graph(Inputs(native_bundle), "broad")


def test_input_snapshot_rejects_replacement_even_with_the_new_expected_hash(tmp_path):
    path = tmp_path / "evidence.txt"
    path.write_bytes(b"original scientific evidence\n")
    inputs = Inputs(tmp_path)
    assert inputs.read(path.name, sha(path)) == path.read_bytes()
    path.write_bytes(b"different scientific evidence\n")
    with pytest.raises(ValueError, match="input changed: evidence.txt"):
        inputs.read(path.name, sha(path))


def test_input_snapshot_rejects_late_byte_drift(tmp_path):
    path = tmp_path / "evidence.txt"
    path.write_bytes(b"original evidence\n")
    inputs = Inputs(tmp_path)
    inputs.read(path.name)
    path.write_bytes(b"changed after graph validation\n")
    with pytest.raises(ValueError, match="late input drift: evidence.txt"):
        inputs.recheck()


@pytest.mark.parametrize("attack", ["missing", "duplicate"])
def test_hold_inventory_refuses_missing_or_duplicate_permanent_owners(native_bundle, attack):
    records, hashes, mappings, _ = current_graph(Inputs(native_bundle), "bundle")
    records = copy.deepcopy(records)
    unknown = records["data/ingredients/unmapped/Unknown.yaml"]
    if attack == "missing":
        unknown.pop("mim_id")
    else:
        unknown["mim_id"] = records[OWNER]["mim_id"]
    # This is an explicitly synthetic empty historical hold inventory, not a
    # substitute for the separately tested native historical/publication proof.
    history = {
        "original": {"release_holds": "holds.json"},
        "before": {"holds.json": b'{"holds":[],"resolutions":[],"required_hold_ids":[]}'},
        "proof": SimpleNamespace(),
    }
    with pytest.raises(ValueError, match="missing/duplicate permanent owner"):
        hold_payloads(history, records, hashes, mappings, {"selection": {"rows": []}})


def distinct_reviewers():
    """Synthetic metadata for the identity check, not saved scientific reviews."""
    return (
        [
            {"path": "reviews/structured/synthetic-primary/review.yaml"},
            {"path": "reviews/structured/synthetic-skeptic/review.yaml"},
        ],
        [
            {"identity": "synthetic-primary", "tool": "primary-process"},
            {
                "identity": "synthetic-skeptic",
                "tool": "skeptic-process",
                "independence": "independent",
                "independence_basis": "Separate reviewer of the exact synthetic target.",
            },
        ],
    )


def test_1388_distinct_native_identities_and_independent_skeptic_are_accepted():
    references, reviewers = distinct_reviewers()
    assert independent_pair(references, reviewers) is None


@pytest.mark.parametrize(
    "attack",
    [
        "same_identity_different_metadata",
        "same_report_path",
        "missing_independence",
        "not_independent",
        "missing_basis",
        "empty_basis",
    ],
)
def test_1388_mutable_metadata_cannot_supply_a_separate_independent_reviewer(attack):
    references, reviewers = distinct_reviewers()
    if attack == "same_identity_different_metadata":
        reviewers[1]["identity"] = reviewers[0]["identity"]
        assert reviewers[0] != reviewers[1]
    elif attack == "same_report_path":
        references[1]["path"] = references[0]["path"]
    elif attack == "missing_independence":
        reviewers[1].pop("independence")
    elif attack == "not_independent":
        reviewers[1]["independence"] = "self_review"
    elif attack == "missing_basis":
        reviewers[1].pop("independence_basis")
    else:
        reviewers[1]["independence_basis"] = " \t "
    with pytest.raises(
        ValueError, match="distinct reviewer identities and a separate independent skeptic required"
    ):
        independent_pair(references, reviewers)
