"""Independent attacks on scientific projection and current review coverage."""

import copy
import csv
import hashlib
from pathlib import Path

import pytest
import yaml

from mediaingredientmech.export import kgx
from mediaingredientmech.validation.semantic_release import (
    adjudicate_assertions,
    current_assertions,
    evidence_gaps,
    verify_projection,
)


@pytest.fixture
def projection(tmp_path):
    fixtures = Path(__file__).parent / "fixtures"
    grouped = yaml.safe_load((fixtures / "kgx_records.yaml").read_text())
    records, hashes = {}, {}
    for group, entries in grouped.items():
        directory = tmp_path / "data/ingredients" / group
        directory.mkdir(parents=True)
        for name, record in entries.items():
            path = directory / f"{name}.yaml"
            path.write_text(yaml.safe_dump(record))
            relative = str(path.relative_to(tmp_path))
            records[relative] = record
            hashes[relative] = hashlib.sha256(path.read_bytes()).hexdigest()
        collection = tmp_path / "data/curated" / f"{group}_ingredients.yaml"
        collection.parent.mkdir(exist_ok=True)
        collection.write_text(yaml.safe_dump({"ingredients": list(entries.values())}))
    mapping_path = tmp_path / "mappings/ingredient_mappings.sssom.tsv"
    mapping_path.parent.mkdir()
    mapping_path.write_bytes((fixtures / "kgx_mappings.sssom.tsv").read_bytes())
    mappings = list(csv.DictReader(
        (line for line in mapping_path.read_text().splitlines() if not line.startswith("#")),
        delimiter="\t",
    ))
    graph, _, _ = kgx.build_graph(tmp_path)
    return {
        "records": records, "mappings": mappings,
        "nodes": list(graph.nodes.values()), "edges": graph.edges,
        "hashes": hashes, "sssom_sha": hashlib.sha256(mapping_path.read_bytes()).hexdigest(),
    }


def check_projection(projection):
    verify_projection(**{key: projection[key] for key in ("records", "mappings", "nodes", "edges")})


def rehash_edge(edge):
    """An attacker can update ordinary integrity digests after changing a triple."""
    payload = {key: value for key, value in edge.items() if key != "id"}
    edge["id"] = "MIM.assertion:" + hashlib.sha256(kgx.packed(payload).encode()).hexdigest()


def test_untampered_projection_is_accepted(projection):
    check_projection(projection)


@pytest.mark.parametrize("kind,field,replacement", [
    ("cellular_metabolic_roles", "subject", "MIM:opaque_water_b"),
    ("cellular_metabolic_roles", "object", "CHEBI:15377"),
    ("cellular_metabolic_roles", "predicate", "biolink:exact_match"),
    ("cellular_metabolic_roles", "metabolic_context", "all organisms, all conditions"),
    ("cellular_metabolic_roles", "publications", "doi:10.9999/uninspected"),
    ("cellular_metabolic_roles", "id", "MIM.assertion:forged"),
    ("component", "reference_scope", "EXTERNAL_TERM"),
    ("component", "concentration_value", "1000"),
    ("component", "completeness", "COMPLETE"),
    ("recipe_reference", "relation", "MIM.vocab:recipe_exact_formulation"),
])
def test_intact_payload_cannot_hide_changed_scientific_edge(projection, kind, field, replacement):
    edge = next(row for row in projection["edges"] if row["assertion_type"] == kind)
    payload = edge["assertion_json"]
    edge[field] = replacement
    if field != "id":
        rehash_edge(edge)
    assert edge["assertion_json"] == payload
    with pytest.raises(ValueError, match="projection differs"):
        check_projection(projection)


def test_broad_mapping_direction_cannot_be_reversed(projection):
    edge = next(row for row in projection["edges"] if row["relation"] == "skos:broadMatch")
    edge["subject"], edge["object"] = edge["object"], edge["subject"]
    rehash_edge(edge)
    with pytest.raises(ValueError, match="projection differs"):
        check_projection(projection)


def test_narrow_mapping_requires_the_opposite_orientation(projection, tmp_path):
    path = tmp_path / "mappings/ingredient_mappings.sssom.tsv"
    path.write_text(
        path.read_text()
        + "MIM:opaque_water_a\tWater A\tskos:narrowMatch\tFOODON:00000002\tfixture child\t0.9\n"
    )
    projection["mappings"] = list(csv.DictReader(
        (line for line in path.read_text().splitlines() if not line.startswith("#")),
        delimiter="\t",
    ))
    graph, _, _ = kgx.build_graph(tmp_path)
    projection.update(nodes=list(graph.nodes.values()), edges=graph.edges)
    edge = next(row for row in projection["edges"] if row["relation"] == "skos:narrowMatch")
    assert (edge["subject"], edge["predicate"], edge["object"]) == (
        "FOODON:00000002", "biolink:subclass_of", "MIM:opaque_water_a"
    )
    check_projection(projection)
    edge["subject"], edge["object"] = edge["object"], edge["subject"]
    rehash_edge(edge)
    with pytest.raises(ValueError, match="projection differs"):
        check_projection(projection)


def test_external_reference_label_cannot_imply_another_identity(projection):
    node = next(row for row in projection["nodes"] if row["id"] == "CHEBI:15377")
    node["name"] = "tetrachloroethene"
    with pytest.raises(ValueError, match="node projection differs"):
        check_projection(projection)


def review_rows(projection):
    expected = current_assertions(
        projection["records"], projection["mappings"], projection["hashes"], projection["sssom_sha"]
    )
    decisions = [{**row, "resolution_status": "APPROVED", "review_reason": "Synthetic review fixture only",
                  "review_evidence": "review.txt"} for row in expected]
    return expected, decisions


def test_citation_type_does_not_approve_a_new_role(projection):
    _, old_decisions = review_rows(projection)
    name = "data/ingredients/mapped/Water_B.yaml"
    record = projection["records"][name]
    record["nutritional_roles"] = [{
        "role": "CARBON_SOURCE",
        "evidence": [{"reference_type": "PEER_REVIEWED_PUBLICATION"}],
    }]
    # The old heuristic sees a citation-like object and no evidence gap. A new
    # biological assertion still needs its own explicit reviewed disposition.
    assert evidence_gaps({name: record}) == {}
    expected, _ = review_rows(projection)
    with pytest.raises(ValueError, match="Incomplete current assertion review coverage"):
        adjudicate_assertions(expected, old_decisions, {"review.txt": "hash"})


@pytest.mark.parametrize("mutation", ["record_hash", "assertion_hash", "remove_mapping", "evidence_path", "reason"])
def test_approval_must_bind_the_exact_current_assertion(projection, mutation):
    expected, decisions = review_rows(projection)
    if mutation == "record_hash":
        decisions[0]["source_record_sha256"] = "old-record"
    elif mutation == "assertion_hash":
        decisions[0]["assertion_sha256"] = "different-claim"
    elif mutation == "remove_mapping":
        decisions = [row for row in decisions if row["assertion_type"] != "mapping"]
    elif mutation == "evidence_path":
        decisions[0]["review_evidence"] = "unhashed.txt"
    else:
        decisions[0]["review_reason"] = " "
    with pytest.raises(ValueError):
        adjudicate_assertions(expected, decisions, {"review.txt": "hash"})


def test_open_assertion_cannot_be_masked_by_other_approvals(projection):
    expected, decisions = review_rows(projection)
    open_row = copy.deepcopy(decisions[0])
    open_row.update(resolution_status="OPEN", review_reason="", review_evidence="")
    decisions[0] = open_row
    assert adjudicate_assertions(expected, decisions, {"review.txt": "hash"}) == [open_row["assertion_id"]]
