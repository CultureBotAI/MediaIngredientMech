"""Native project-data license regressions (#788; local finding ec79bcb6)."""

import json

import pytest
from sssom.parsers import parse_sssom_table

from mediaingredientmech.export import reviewed_sssom as external
from mediaingredientmech.export import source_bindings as binding
from mediaingredientmech.stable_ids import MIM_PREFIX
from tests.test_source_bindings import Fixture, write_json

DATA_LICENSE = "https://creativecommons.org/licenses/by/4.0/"
HISTORICAL_EXTERNAL_LICENSE = "https://creativecommons.org/publicdomain/zero/1.0/"
SOURCE_PRODUCTS = ("source-bindings.sssom.tsv", "withheld-source-bindings.sssom.tsv")


@pytest.fixture
def licensed_candidate(tmp_path):
    fixture = Fixture(tmp_path)
    fixture.review["cases"][0]["holds"] = ["Original supplied preparation remains unresolved"]
    fixture.seal(withheld=(1,))
    external_products, _ = external.expected_products(tmp_path, tmp_path / "external-review.json")
    canonical = (tmp_path / binding.EXTERNAL_SOURCE).read_bytes()
    manifest = binding.export_candidate(tmp_path, fixture.review_path, fixture.output)
    assert binding.validate_candidate(tmp_path, fixture.review_path, fixture.output) == manifest
    return fixture, manifest, external_products, canonical


def test_source_identity_partitions_use_project_license_preserve_external_bytes(licensed_candidate):
    fixture, manifest, external_products, canonical = licensed_candidate
    assert manifest["counts"] == {
        "source_entities": 4,
        "source_occurrences": 5,
        "supported": 3,
        "withheld": 1,
        "withheld_without_owner": 0,
    }
    assert manifest["production_authorized"] is False
    for name, expected_subjects in zip(
        SOURCE_PRODUCTS, ({"SOURCE:2", "SOURCE:3", "SOURCE:4"}, {"SOURCE:1"}), strict=True
    ):
        path = fixture.output / name
        native = parse_sssom_table(path, strict=True)
        rows = binding._sssom_rows(path.read_bytes())
        assert native.metadata["license"] == DATA_LICENSE
        assert native.prefix_map["MIM"] == MIM_PREFIX
        assert list(rows[0]) == list(binding.SOURCE_FIELDS)
        assert {row["subject_id"] for row in rows} == expected_subjects
        for row in rows:
            assert row["object_id"] == f"MIM:{int(row['subject_id'].split(':')[1]):07d}"
            assert row["predicate_id"] == "skos:exactMatch"
            assert row["mapping_justification"] == "semapv:ManualMappingCuration"
            assert "Candidate only; payload sha256=" in row["comment"]
            assert "; primary=reviews/structured/" in row["comment"]
            assert "; skeptic=reviews/structured/" in row["comment"]

    # Historical/external licenses and complete payloads are not replaced by the
    # project-authored source-identity license, including the empty external hold partition.
    for name, original in external_products.items():
        assert (fixture.output / ("external-" + name)).read_bytes() == original
    for name in ("ingredient_mappings.sssom.tsv", "withheld_mappings.sssom.tsv"):
        metadata, _, _ = external.read_sssom(fixture.output / ("external-" + name))
        assert metadata["license"] == HISTORICAL_EXTERNAL_LICENSE
    assert (fixture.root / binding.EXTERNAL_SOURCE).read_bytes() == canonical
    _, _, external_rows = external.read_sssom(
        fixture.output / "external-ingredient_mappings.sssom.tsv"
    )
    assert {row["predicate_id"] for row in external_rows} == {
        "skos:exactMatch",
        "skos:broadMatch",
        "skos:closeMatch",
    }
    assert all(row["comment"] == "Preserve exact historical commentary" for row in external_rows)

    decisions = json.loads((fixture.output / "source-decisions.json").read_bytes())
    assert [case["disposition"] for case in decisions] == [
        "WITHHOLD",
        "SUPPORTED",
        "SUPPORTED",
        "SUPPORTED",
    ]
    assert decisions[0]["payload"]["holds"] == fixture.review["cases"][0]["holds"]
    assert len(decisions[1]["payload"]["occurrences"]) == 2
    assert decisions[3]["payload"]["mim_id"] == "MIM:0000004"
    assert decisions[3]["payload"]["mapping_status"] == "UNMAPPED"
    assert not any(row["subject_id"] == "MIM:0000004" for row in external_rows)
    claims = binding.consumer_claims(
        fixture.root, fixture.review_path, fixture.output, capabilities={binding.CAPABILITY}
    )
    assert [claim["original_subject_id"] for claim in claims] == [
        "SOURCE:2",
        "SOURCE:3",
        "SOURCE:4",
    ]
    assert [claim["object_id"] for claim in claims] == [
        "MIM.ingredient:0000002",
        "MIM.ingredient:0000003",
        "MIM.ingredient:0000004",
    ]
    assert all(claim["predicate_id"] == "skos:exactMatch" for claim in claims)


@pytest.mark.parametrize("name", SOURCE_PRODUCTS)
def test_reconstruction_rejects_wrong_source_license_even_after_manifest_rehash(
    licensed_candidate, name
):
    fixture, _, _, _ = licensed_candidate
    path = fixture.output / name
    original = path.read_bytes()
    assert original.count(DATA_LICENSE.encode()) == 1
    changed = original.replace(DATA_LICENSE.encode(), HISTORICAL_EXTERNAL_LICENSE.encode(), 1)
    path.write_bytes(changed)
    manifest_path = fixture.output / "manifest.json"
    manifest = json.loads(manifest_path.read_bytes())
    manifest["files"][name] = external.digest(path)
    write_json(manifest_path, manifest)
    assert manifest["files"][name] == external.digest(path)
    assert parse_sssom_table(path, strict=True).metadata["license"] == HISTORICAL_EXTERNAL_LICENSE
    # Hash consistency cannot substitute for native reconstruction of the current
    # producer's licensed bytes. Both nonempty source partitions are exercised.
    with pytest.raises(ValueError, match="candidate bytes differ: " + name):
        binding.validate_candidate(fixture.root, fixture.review_path, fixture.output)
