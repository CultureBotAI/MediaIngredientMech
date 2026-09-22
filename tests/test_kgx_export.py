"""Standalone MIM exports retain source scope, evidence and distinct identities."""

import csv
import hashlib
import json
import shutil
import tarfile
from pathlib import Path

import pytest
import yaml

from mediaingredientmech.export import kgx

FIXTURES = Path(__file__).parent / "fixtures"


@pytest.fixture
def corpus(tmp_path):
    root = tmp_path / "repo"
    records = yaml.safe_load((FIXTURES / "kgx_records.yaml").read_text())
    for group, entries in records.items():
        directory = root / "data/ingredients" / group
        directory.mkdir(parents=True)
        for name, record in entries.items():
            (directory / f"{name}.yaml").write_text(yaml.safe_dump(record))
        collection = root / "data/curated" / f"{group}_ingredients.yaml"
        collection.parent.mkdir(exist_ok=True)
        collection.write_text(yaml.safe_dump({"ingredients": list(entries.values())}))
    (root / "mappings").mkdir()
    shutil.copyfile(
        FIXTURES / "kgx_mappings.sssom.tsv", root / "mappings/ingredient_mappings.sssom.tsv"
    )
    # Ignored backups are not the live corpus and must never be imported.
    backup = root / "data/ingredients/mapped/backups"
    backup.mkdir()
    (backup / "bad.yaml").write_text("not valid: [")
    return root


def read_rows(path):
    with path.open() as stream:
        return list(csv.DictReader(stream, delimiter="\t", quoting=csv.QUOTE_NONE))


def change_record(root, group, stem, update):
    path = root / "data/ingredients" / group / f"{stem}.yaml"
    record = yaml.safe_load(path.read_text())
    label = record["preferred_term"]
    update(record)
    path.write_text(yaml.safe_dump(record))
    path = root / "data/curated" / f"{group}_ingredients.yaml"
    collection = yaml.safe_load(path.read_text())
    collection["ingredients"] = [
        record if r["preferred_term"] == label else r for r in collection["ingredients"]
    ]
    path.write_text(yaml.safe_dump(collection))


def test_complete_graph_preserves_scope_and_annotations(corpus, tmp_path):
    output = tmp_path / "kgx"
    result = kgx.export_graph(corpus, output)
    nodes = {r["id"]: r for r in read_rows(output / "mim_nodes.tsv")}
    edges = read_rows(output / "mim_edges.tsv")
    assert result["counts"]["active_ingredients"] == 4
    assert result["counts"]["excluded_rejected_records"] == 1
    assert "CHEBI:78018" not in nodes
    assert "MIM.unmapped:UNMAPPED_0001" in nodes
    assert {e["object"] for e in edges if e["subject"] == "MIM:opaque_water_b"} == {"CHEBI:15377"}
    roles = [e for e in edges if e["predicate"] == "biolink:has_chemical_role"]
    assert len(roles) == 2
    assert all(e["subject"] == "MIM:opaque_water_a" for e in roles)
    role = next(e for e in roles if e["metabolic_context"])
    assert role["metabolic_context"] == "fixture organism only"
    assert role["confidence"] == "0.5" and role["publications"] == "doi:10.1234/test"
    assert (
        json.loads(role["assertion_json"])["evidence"][0]["reference_text"]
        == "quoted\nmultiline evidence"
    )
    role = next(e for e in roles if not e["metabolic_context"])
    assert "|" not in role["assertion_json"]
    assert " | " in json.loads(role["assertion_json"])["evidence"][0]["reference_text"]
    parts = [e for e in edges if e["assertion_type"] == "component"]
    quantified = next(e for e in parts if e["concentration_value"])
    assert (
        quantified["object"],
        quantified["concentration_value"],
        quantified["concentration_unit"],
        quantified["completeness"],
    ) == ("CHEBI:15377", "0.1-0.5", "G_PER_L", "PARTIAL")
    unresolved = [e for e in parts if e["reference_scope"] == "UNMAPPED"]
    assert len({e["object"] for e in unresolved}) == 2
    assert all(nodes[e["object"]]["name"] == "unknown fraction" for e in unresolved)
    broad = next(e for e in edges if e["predicate"] == "biolink:subclass_of")
    assert (broad["subject"], broad["object"], broad["relation"]) == (
        "MIM:fixture_mix",
        "FOODON:00000001",
        "skos:broadMatch",
    )
    assert sum(e["predicate"] == "biolink:subclass_of" for e in edges) == 1
    candidate = next(e for e in edges if e["assertion_type"] == "recipe_reference")
    assert candidate["predicate"] == "MIM.vocab:recipe_candidate_unverified"
    assert all(e["subject"] in nodes and e["object"] in nodes for e in edges)
    original = yaml.safe_load((corpus / "data/ingredients/mapped/Water_A.yaml").read_text())
    assert json.loads(nodes["MIM:opaque_water_a"]["record_json"]) == original


def test_deterministic_archive_and_all_manifest_members(corpus, tmp_path):
    first, second = tmp_path / "first", tmp_path / "second"
    kgx.export_graph(corpus, first)
    kgx.export_graph(corpus, second)
    assert (first / "mim-kgx.tar.gz").read_bytes() == (second / "mim-kgx.tar.gz").read_bytes()
    with tarfile.open(first / "mim-kgx.tar.gz") as archive:
        manifest = json.load(archive.extractfile("manifest.json"))
        assert set(archive.getnames()) == {"manifest.json", *manifest["members"]}
        for name, expected in manifest["members"].items():
            data = archive.extractfile(name).read()
            assert hashlib.sha256(data).hexdigest() == expected["sha256"]
            assert len(data) == expected["bytes"]
            assert data.count(b"\n") - 1 == expected["rows"]


def test_parallel_role_evidence_is_not_collapsed(corpus, tmp_path):
    def add_role(record):
        role = json.loads(json.dumps(record["nutritional_roles"][0]))
        role["confidence"] = 0.2
        role["evidence"][0]["reference_text"] = "independent synthetic evidence"
        record["nutritional_roles"].append(role)

    change_record(corpus, "mapped", "Water_A", add_role)
    output = tmp_path / "release"
    manifest = kgx.export_graph(corpus, output)
    roles = [
        e for e in read_rows(output / "mim_edges.tsv") if e["assertion_type"] == "nutritional_roles"
    ]
    assert len(roles) == 2
    assert len({e["id"] for e in roles}) == 2
    assert len({(e["subject"], e["predicate"], e["object"]) for e in roles}) == 1
    assert {e["confidence"] for e in roles} == {"0.6", "0.2"}
    assert manifest["counts"]["edges"] == manifest["counts"]["unique_triples"] + 1


def test_inverse_mapping_projects_child_to_parent_and_retains_original_row(corpus, tmp_path):
    path = corpus / "mappings/ingredient_mappings.sssom.tsv"
    path.write_text(
        path.read_text()
        + "MIM:opaque_water_a\tWater A\tskos:narrowMatch\tFOODON:00000002\tfixture child\t0.9\n"
    )
    output = tmp_path / "release"
    kgx.export_graph(corpus, output)
    inverse = next(
        e for e in read_rows(output / "mim_edges.tsv") if e["relation"] == "skos:narrowMatch"
    )
    assert (inverse["subject"], inverse["predicate"], inverse["object"]) == (
        "FOODON:00000002",
        "biolink:subclass_of",
        "MIM:opaque_water_a",
    )
    original = json.loads(inverse["assertion_json"])
    assert (original["subject_id"], original["object_id"]) == (
        "MIM:opaque_water_a",
        "FOODON:00000002",
    )


def test_existing_output_is_never_replaced(corpus, tmp_path):
    output = tmp_path / "release"
    output.mkdir()
    (output / "mim-kgx.tar.gz").write_bytes(b"previous accepted archive")
    with pytest.raises(FileExistsError):
        kgx.export_graph(corpus, output)
    assert (output / "mim-kgx.tar.gz").read_bytes() == b"previous accepted archive"


def test_collection_drift_fails_before_publication(corpus, tmp_path):
    path = corpus / "data/ingredients/mapped/Water_A.yaml"
    record = yaml.safe_load(path.read_text())
    record["notes"] = "unreconciled change"
    path.write_text(yaml.safe_dump(record))
    with pytest.raises(ValueError, match="Collection/per-record drift"):
        kgx.export_graph(corpus, tmp_path / "release")
    assert not (tmp_path / "release").exists()


@pytest.mark.parametrize("predicate", ["skos:exactMatch", "skos:narrowMatch"])
def test_stale_parent_direction_is_rejected(corpus, tmp_path, predicate):
    path = corpus / "mappings/ingredient_mappings.sssom.tsv"
    path.write_text(path.read_text().replace("skos:broadMatch", predicate))
    with pytest.raises(ValueError, match="Stale SSSOM grounding or direction"):
        kgx.export_graph(corpus, tmp_path / "release")


def test_component_scope_error_is_rejected(corpus, tmp_path):
    change_record(
        corpus,
        "mapped",
        "Mixture",
        lambda r: r["components"][0].update(reference_scope="EXTERNAL_TERM"),
    )
    with pytest.raises(ValueError, match="Component validation failed"):
        kgx.export_graph(corpus, tmp_path / "release")


def test_known_identifier_duplicates_do_not_hide_component_cycles(corpus, tmp_path):
    def update(record):
        record["ingredient_type"] = "STOCK_SOLUTION"
        record["components"] = [
            {
                "component_name": "Fixture mixture",
                "component_id": "kgmicrobe.ingredient:fixture_mix",
                "reference_scope": "MIM_CATALOG",
            }
        ]
        record["component_assertion"] = {
            "method": "LABEL_ENUMERATION",
            "completeness": "UNKNOWN",
            "evidence": [{"evidence_type": "SOURCE_LABEL", "source": "fixture:label"}],
        }

    change_record(corpus, "mapped", "Water_B", update)
    with pytest.raises(ValueError, match="Cycle in material component assertions"):
        kgx.export_graph(corpus, tmp_path / "release")


def test_review_findings_remain_visible(corpus, tmp_path):
    path = corpus / "reports/yaml_record_review/manifest.tsv"
    path.parent.mkdir(parents=True)
    path.write_text(
        "path\tverdict\tseverity\n" "data/ingredients/mapped/Water_A.yaml\tneeds_curation\tmajor\n"
    )
    output = tmp_path / "release"
    manifest = kgx.export_graph(corpus, output, path)
    nodes = {r["id"]: r for r in read_rows(output / "mim_nodes.tsv")}
    assert nodes["MIM:opaque_water_a"]["review_status"] == "needs_curation"
    assert manifest["counts"]["ingredient_review_status"] == {
        "needs_curation": 1,
        "not_reviewed": 3,
    }


@pytest.mark.parametrize("binding", ["missing", "stale", "current"])
def test_positive_review_requires_current_record_hash(corpus, tmp_path, binding):
    record = corpus / "data/ingredients/mapped/Water_A.yaml"
    record_hash = hashlib.sha256(record.read_bytes()).hexdigest()
    path = corpus / "reports/yaml_record_review/manifest.tsv"
    path.parent.mkdir(parents=True)
    supplied_hash = {"missing": "", "stale": "0" * 64, "current": record_hash}[binding]
    path.write_text(
        "path\tverdict\trecord_sha256\n"
        f"data/ingredients/mapped/Water_A.yaml\tpass\t{supplied_hash}\n"
    )
    output = tmp_path / "release"
    kgx.export_graph(corpus, output, path)
    nodes = {r["id"]: r for r in read_rows(output / "mim_nodes.tsv")}
    node = nodes["MIM:opaque_water_a"]
    assert node["review_status"] == (
        "pass" if binding == "current" else "historical_review_unverified"
    )
    assert json.loads(node["review_json"])["verdict"] == "pass"


def test_ignored_review_ledger_does_not_silently_change_default_export(corpus, tmp_path):
    first, second = tmp_path / "before", tmp_path / "after"
    kgx.export_graph(corpus, first)
    ledger = corpus / "reports/yaml_record_review/manifest.tsv"
    ledger.parent.mkdir(parents=True)
    ledger.write_text("path\tverdict\ndata/ingredients/mapped/Water_A.yaml\tpass\n")
    kgx.export_graph(corpus, second)
    assert (first / "mim-kgx.tar.gz").read_bytes() == (second / "mim-kgx.tar.gz").read_bytes()


def test_hierarchy_cycles_through_primary_identity_are_rejected(corpus, tmp_path):
    path = corpus / "mappings/ingredient_mappings.sssom.tsv"
    rows = path.read_text()
    header = next(line for line in rows.splitlines() if not line.startswith("#"))
    columns = header.split("\t")
    # These broader links cycle after exact identities are resolved.
    for subject, label, obj in [
        ("MIM:opaque_water_a", "Water A", "kgmicrobe.ingredient:fixture_mix"),
        ("MIM:fixture_mix", "Fixture mixture", "CHEBI:15377"),
    ]:
        row = dict.fromkeys(columns, "")
        row.update(
            subject_id=subject,
            subject_label=label,
            predicate_id="skos:broadMatch",
            object_id=obj,
            object_label=obj,
        )
        rows += "\t".join(row[c] for c in columns) + "\n"
    path.write_text(rows)
    with pytest.raises(ValueError, match="Cycle in broader/narrower mappings"):
        kgx.export_graph(corpus, tmp_path / "release")


def test_mid_export_input_mutation_cannot_publish(corpus, tmp_path, monkeypatch):
    write = kgx._write_tsv

    def changed(*args, **kwargs):
        result = write(*args, **kwargs)
        path = corpus / "data/ingredients/mapped/Water_A.yaml"
        path.write_text(path.read_text() + "\n# concurrent edit\n")
        return result

    monkeypatch.setattr(kgx, "_write_tsv", changed)
    with pytest.raises(ValueError, match="Input changed before publication"):
        kgx.export_graph(corpus, tmp_path / "release")
    assert not (tmp_path / "release").exists()


def test_ambiguous_source_survives_without_identity_mapping(corpus, tmp_path):
    change_record(corpus, "unmapped", "Unknown", lambda r: r.update(mapping_status="AMBIGUOUS"))
    output = tmp_path / "ambiguous"
    kgx.export_graph(corpus, output)
    nodes = {r["id"]: r for r in read_rows(output / "mim_nodes.tsv")}
    source = "MIM.unmapped:UNMAPPED_0001"
    assert nodes[source]["mapping_status"] == "AMBIGUOUS"
    assert json.loads(nodes[source]["record_json"])["mapping_status"] == "AMBIGUOUS"
    assert not any(
        row["subject"] == source
        and row["predicate"]
        in {"biolink:exact_match", "biolink:close_match", "biolink:subclass_of"}
        for row in read_rows(output / "mim_edges.tsv")
    )
