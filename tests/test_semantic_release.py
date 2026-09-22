"""A complete review inventory must not silently lose unresolved science."""

import copy
import csv
import hashlib
import json
import os
import subprocess
import sys
from pathlib import Path

import pytest
import yaml

from mediaingredientmech.validation.semantic_release import (
    adjudicate_findings,
    assertion_inventory,
    current_assertions,
    evidence_gaps,
    validate,
)


@pytest.fixture
def review():
    name = "data/ingredients/mapped/example.yaml"
    finding = {
        "finding_id": "SEM:example",
        "source_record": name,
        "record_scope": "active",
        "kind": "component_source_scope",
        "severity": "major",
        "reason": "The source preparation has not been checked.",
    }
    decision = {
        **finding,
        "current_record": name,
        "current_record_sha256": "source-hash",
        "resolution_status": "OPEN",
        "resolution_reason": "",
        "resolution_evidence": "",
    }
    return {
        "baseline": [finding],
        "dispositions": [decision],
        "records": {name: {"mapping_status": "MAPPED"}},
        "record_hashes": {name: "source-hash"},
        "inputs": {"evidence.json": "evidence-hash"},
    }


@pytest.mark.parametrize(
    "kind", ["component_source_scope", "recipe_identity", "existing_record_review", "role_evidence"]
)
def test_every_major_finding_blocks_even_without_prediction_only_roles(review, kind):
    review["baseline"][0]["kind"] = kind
    review["dispositions"][0]["kind"] = kind
    assert evidence_gaps(review["records"]) == {}
    assert adjudicate_findings(**review) == ["SEM:example"]


@pytest.mark.parametrize(
    "mutation", ["drop", "duplicate", "stale", "weaken", "exclude_active", "unbound_resolution"]
)
def test_adversarial_disposition_mutations_are_rejected(review, mutation):
    decision = review["dispositions"][0]
    if mutation == "drop":
        review["dispositions"] = []
    elif mutation == "duplicate":
        review["dispositions"].append(copy.deepcopy(decision))
    elif mutation == "stale":
        decision["current_record_sha256"] = "old-hash"
    elif mutation == "weaken":
        decision["severity"] = "minor"
    elif mutation == "exclude_active":
        decision["resolution_status"] = "EXCLUDED_REJECTED"
    else:
        decision.update(
            resolution_status="RESOLVED",
            resolution_reason="Reviewed",
            resolution_evidence="missing.json",
        )
    with pytest.raises(ValueError):
        adjudicate_findings(**review)


def test_resolved_finding_requires_reason_and_hashed_support(review):
    review["dispositions"][0].update(
        resolution_status="RESOLVED",
        resolution_reason="Original preparation checked and corrected.",
        resolution_evidence="evidence.json",
    )
    assert adjudicate_findings(**review) == []


def test_retired_record_can_be_excluded_without_certifying_its_old_claims(review):
    name = next(iter(review["records"]))
    review["records"][name]["mapping_status"] = "REJECTED"
    review["dispositions"][0]["resolution_status"] = "EXCLUDED_REJECTED"
    assert adjudicate_findings(**review) == []


def test_role_and_component_gaps_are_computed_from_current_records():
    record = {
        "mapping_status": "AMBIGUOUS",
        "nutritional_roles": [{"role": "CARBON_SOURCE", "evidence": []}],
        "cellular_metabolic_roles": [
            {
                "role": "ELECTRON_DONOR",
                "evidence": [{"reference_type": "COMPUTATIONAL_PREDICTION"}],
            }
        ],
        "components": [{"component_name": "guessed part"}],
        "component_assertion": {"method": "ABBREVIATION_EXPANSION"},
    }
    assert evidence_gaps({"example": record}) == {
        "ambiguous_identities": 1,
        "cellular_roles_without_context": 1,
        "components_requiring_source_verification": 1,
        "prediction_only_roles": 1,
        "roles_without_evidence": 1,
    }
    record["mapping_status"] = "REJECTED"
    assert evidence_gaps({"example": record}) == {}


def test_assertion_coverage_preserves_duplicates_and_source_positions():
    role = {"role": "CARBON_SOURCE", "evidence": []}
    records = {"example": {"mapping_status": "MAPPED", "nutritional_roles": [role, role]}}
    inventory = assertion_inventory(records, [])
    assert sum(inventory.values()) == 2
    assert {key[2] for key in inventory} == {"1", "2"}


def test_validation_remains_enabled_with_python_optimization(review):
    review["dispositions"] = []
    script = (
        "import json; from mediaingredientmech.validation.semantic_release import adjudicate_findings; "
        f"adjudicate_findings(**json.loads({json.dumps(review)!r}))"
    )
    result = subprocess.run(
        [sys.executable, "-O", "-c", script],
        env={**os.environ, "PYTHONPATH": str(Path(__file__).parents[1] / "src")},
        capture_output=True,
        text=True,
    )
    assert result.returncode != 0
    assert "Incomplete finding coverage" in result.stderr


def test_unrelated_rejected_record_cannot_hide_active_finding(review):
    unrelated = "data/ingredients/mapped/unrelated.yaml"
    review["records"][unrelated] = {"mapping_status": "REJECTED"}
    review["record_hashes"][unrelated] = "retired-hash"
    review["dispositions"][0].update(
        current_record=unrelated,
        current_record_sha256="retired-hash",
        resolution_status="EXCLUDED_REJECTED",
    )
    with pytest.raises(ValueError, match="continuity"):
        adjudicate_findings(**review)


def test_renamed_record_requires_current_and_historical_hash_bound_lineage(review):
    old = review["baseline"][0]["source_record"]
    new = "data/ingredients/unmapped/example.yaml"
    review["records"][new] = review["records"].pop(old)
    review["record_hashes"][new] = review["record_hashes"].pop(old)
    review["dispositions"][0]["current_record"] = new
    review["baseline_hashes"] = {old: "historical-hash"}
    review["lineage"] = [
        {
            "source_record": old,
            "source_sha256": "historical-hash",
            "current_record": new,
            "current_sha256": "source-hash",
            "kind": "MOVE",
            "evidence": "evidence.json",
        }
    ]
    assert adjudicate_findings(**review) == ["SEM:example"]
    review["lineage"][0]["source_sha256"] = "different-historical-record"
    with pytest.raises(ValueError, match="historical baseline"):
        adjudicate_findings(**review)


def test_merge_lineage_must_follow_explicit_representative(review):
    old = review["baseline"][0]["source_record"]
    new = "data/ingredients/mapped/representative.yaml"
    review["records"][old].update(mapping_status="REJECTED", representative="CHEBI:15377")
    review["records"][new] = {"mapping_status": "MAPPED", "identifier": "CHEBI:15377"}
    review["record_hashes"][new] = "survivor-hash"
    review["dispositions"][0].update(current_record=new, current_record_sha256="survivor-hash")
    review["baseline_hashes"] = {old: "historical-hash"}
    review["lineage"] = [
        {
            "source_record": old,
            "source_sha256": "historical-hash",
            "current_record": new,
            "current_sha256": "survivor-hash",
            "kind": "MERGE",
            "evidence": "evidence.json",
        }
    ]
    assert adjudicate_findings(**review) == ["SEM:example"]
    review["records"][old]["representative"] = "CHEBI:78018"
    with pytest.raises(ValueError, match="representative"):
        adjudicate_findings(**review)


def _hash(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def _table(path, entries, columns):
    with path.open("w") as stream:
        writer = csv.DictWriter(
            stream,
            fieldnames=columns,
            delimiter="\t",
            quotechar=None,
            quoting=csv.QUOTE_NONE,
            lineterminator="\n",
        )
        writer.writeheader()
        writer.writerows(entries)


@pytest.fixture
def reviewed_bundle(tmp_path):
    """A complete synthetic release permits testing the full publication contract."""
    from mediaingredientmech.export.kgx import export_graph

    root = tmp_path
    record = {"identifier": "CHEBI:15377", "preferred_term": "Water", "mapping_status": "MAPPED"}
    unknown = {
        "identifier": "UNMAPPED_0001",
        "preferred_term": "Unknown",
        "mapping_status": "UNMAPPED",
    }
    records = {
        "data/ingredients/mapped/Water.yaml": record,
        "data/ingredients/unmapped/Unknown.yaml": unknown,
    }
    for name, value in records.items():
        path = root / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(yaml.safe_dump(value))
    (root / "data/curated").mkdir()
    for group, value in (("mapped", record), ("unmapped", unknown)):
        (root / f"data/curated/{group}_ingredients.yaml").write_text(
            yaml.safe_dump({"ingredients": [value]})
        )
    mapping = {
        "subject_id": "MIM:water",
        "subject_label": "Water",
        "predicate_id": "skos:exactMatch",
        "object_id": "CHEBI:15377",
        "object_label": "water",
    }
    (root / "mappings").mkdir()
    sssom = root / "mappings/ingredient_mappings.sssom.tsv"
    _table(sssom, [mapping], list(mapping))
    sssom.write_text(
        "# predicate_semantics: skos\n# curie_map:\n#   MIM: https://example.test/mim/\n#   CHEBI: http://purl.obolibrary.org/obo/CHEBI_\n"
        + sssom.read_text()
    )
    export_graph(root, root / "bundle")
    (root / "findings.tsv").write_text("finding_id\n")
    (root / "dispositions.tsv").write_text("finding_id\n")
    (root / "evidence.md").write_text("Synthetic review evidence, for tests only.\n")
    record_hashes = {name: _hash(root / name) for name in records}
    (root / "baseline.json").write_text(
        json.dumps(
            {
                "members": {"findings.tsv": {"sha256": _hash(root / "findings.tsv")}},
                "inputs": record_hashes,
            }
        )
    )
    decisions = [
        {
            **identity,
            "resolution_status": "APPROVED",
            "review_reason": "Reviewed synthetic fixture",
            "review_evidence": "evidence.md",
        }
        for identity in current_assertions(records, [mapping], record_hashes, _hash(sssom))
    ]
    _table(root / "assertions.tsv", decisions, list(decisions[0]))
    inputs = [
        "findings.tsv",
        "dispositions.tsv",
        "baseline.json",
        "assertions.tsv",
        "evidence.md",
        "mappings/ingredient_mappings.sssom.tsv",
        "bundle/manifest.json",
    ]
    report = {
        "schema_version": 1,
        "baseline_findings": "findings.tsv",
        "baseline_manifest": "baseline.json",
        "finding_dispositions": "dispositions.tsv",
        "assertion_dispositions": "assertions.tsv",
        "inputs": {name: _hash(root / name) for name in inputs},
        "record_inputs": record_hashes,
        "bundle": "bundle",
        "blocking_finding_ids": [],
        "blocking_assertion_ids": [],
        "evidence_gaps": {},
        "release_verdict": "PASS",
    }
    path = root / "review.json"
    path.write_text(json.dumps(report))
    return root, path


def test_full_review_accepts_supported_fixture(reviewed_bundle):
    root, path = reviewed_bundle
    assert validate(root, path)["semantic_release"] == "PASS"


def test_full_review_rejects_wrong_triple_even_after_freshness_hashes_updated(reviewed_bundle):
    root, path = reviewed_bundle
    edge_file = root / "bundle/mim_edges.tsv"
    with edge_file.open() as stream:
        reader = csv.DictReader(stream, delimiter="\t", quoting=csv.QUOTE_NONE)
        columns, edges = reader.fieldnames, list(reader)
    edges[0]["predicate"] = "biolink:subclass_of"
    _table(edge_file, edges, columns)
    manifest_path = root / "bundle/manifest.json"
    manifest = json.loads(manifest_path.read_text())
    manifest["members"]["mim_edges.tsv"].update(
        sha256=_hash(edge_file), bytes=edge_file.stat().st_size
    )
    manifest_path.write_text(json.dumps(manifest))
    report = json.loads(path.read_text())
    report["inputs"]["bundle/manifest.json"] = _hash(manifest_path)
    path.write_text(json.dumps(report))
    with pytest.raises(ValueError, match="edge projection"):
        validate(root, path)


def test_review_evidence_changes_invalidate_current_approvals(reviewed_bundle):
    root, path = reviewed_bundle
    (root / "evidence.md").write_text("Changed evidence\n")
    with pytest.raises(ValueError, match="Stale review input: evidence.md"):
        validate(root, path)
