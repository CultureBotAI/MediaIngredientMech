"""Lossless native SSSOM partition validation and refusal regressions (#1405)."""

import json

import pytest
import yaml

from mediaingredientmech.export import reviewed_sssom as external
from mediaingredientmech.export import source_bindings as binding
from mediaingredientmech.stable_ids import MIM_PREFIX
from tests.test_source_bindings import Fixture, write_json

PARTITIONS = (
    "source-bindings.sssom.tsv",
    "withheld-source-bindings.sssom.tsv",
    "external-ingredient_mappings.sssom.tsv",
    "external-withheld_mappings.sssom.tsv",
)


def partition_fixture(root, selected, comment):
    """Serialize tiny synthetic partitions through the actual native writer."""
    metadata = {
        "mapping_set_id": "https://example.invalid/source-partition-fixture",
        "predicate_semantics": "skos",
        "license": "https://creativecommons.org/publicdomain/zero/1.0/",
        "curie_map": {
            "SOURCE": "https://example.invalid/source/",
            "MIM": MIM_PREFIX,
            "CHEBI": "http://purl.obolibrary.org/obo/CHEBI_",
            "skos": "http://www.w3.org/2004/02/skos/core#",
            "semapv": "https://w3id.org/semapv/vocab/",
        },
    }
    header = "".join(
        "# " + line + "\n" for line in yaml.safe_dump(metadata, sort_keys=False).splitlines()
    ).encode()
    rows = [
        {
            "subject_id": f"SOURCE:{index}",
            "subject_label": "Synthetic source",
            "predicate_id": "skos:exactMatch",
            "object_id": f"MIM:{index:07d}",
            "object_label": "Synthetic ingredient",
            "mapping_justification": "semapv:ManualMappingCuration",
            "comment": comment if index == 1 else "Second row remains distinct",
        }
        for index in (1, 2)
    ]
    for name in PARTITIONS:
        fields = list(binding.SOURCE_FIELDS)
        selected_rows = [dict(row) for row in rows] if name == selected else []
        if name.startswith("external-"):
            fields.append("other")
            for row in selected_rows:
                row.update(
                    subject_id=row["object_id"],
                    object_id="CHEBI:15382",
                    object_label="(4R)-limonene",
                    other="",
                )
        (root / name).write_bytes(header + external._tsv(fields, selected_rows))
    manifest = {
        "counts": {
            "supported": 2 if selected == PARTITIONS[0] else 0,
            "withheld": 2 if selected == PARTITIONS[1] else 0,
            "withheld_without_owner": 0,
        },
        "external_counts": {
            "supported": 2 if selected == PARTITIONS[2] else 0,
            "withhold": 2 if selected == PARTITIONS[3] else 0,
        },
    }
    return manifest


@pytest.mark.parametrize("partition", PARTITIONS)
@pytest.mark.parametrize("newline", ["\n", "\r\n"])
@pytest.mark.parametrize("ending", ["", "\nlast continuation"])
def test_1405_quoted_hash_lines_preserve_payload_and_validate(tmp_path, partition, newline, ending):
    comment = "First line" + newline + "# retained evidence" + ending
    manifest = partition_fixture(tmp_path, partition, comment)
    before = {name: (tmp_path / name).read_bytes() for name in PARTITIONS}
    rows = binding._sssom_rows(before[partition])
    assert len(rows) == 2
    assert rows[0]["comment"] == comment
    assert rows[1]["comment"] == "Second row remains distinct"
    assert rows[0]["subject_id"] != rows[1]["subject_id"]
    binding.validate_sssom_partitions(tmp_path, manifest)
    assert {name: (tmp_path / name).read_bytes() for name in PARTITIONS} == before


@pytest.mark.parametrize("attack", ["missing-column", "duplicate-column", "extra-cell", "blank-id"])
def test_1405_malformed_partitions_still_fail(tmp_path, attack):
    selected = PARTITIONS[2]
    manifest = partition_fixture(tmp_path, selected, "Ordinary comment")
    path = tmp_path / selected
    raw = path.read_bytes()
    if attack == "missing-column":
        raw = raw.replace(b"object_id\t", b"not_an_identity\t", 1)
    elif attack == "duplicate-column":
        raw = raw.replace(b"object_label\t", b"object_id\t", 1)
    elif attack == "extra-cell":
        raw = raw.replace(b"Ordinary comment\t", b"Ordinary comment\textra\t", 1)
    else:
        raw = raw.replace(b"CHEBI:15382\t", b"\t", 1)
    assert raw != path.read_bytes()
    path.write_bytes(raw)
    with pytest.raises(ValueError):
        binding.validate_sssom_partitions(tmp_path, manifest)


def test_1405_count_mismatch_still_fails(tmp_path):
    manifest = partition_fixture(tmp_path, PARTITIONS[2], "First\n# final evidence")
    manifest["external_counts"]["supported"] = 1
    with pytest.raises(ValueError, match="row count"):
        binding.validate_sssom_partitions(tmp_path, manifest)


@pytest.mark.parametrize("disposition", ["SUPPORTED", "WITHHOLD"])
def test_1405_native_candidate_keeps_reviewed_multiline_comment(tmp_path, disposition):
    fixture = Fixture(tmp_path)
    canonical = tmp_path / binding.EXTERNAL_SOURCE
    metadata, fields, rows = external.read_sssom(canonical)
    rows[0]["comment"] = "Original evidence\r\n# last quoted continuation"
    header = "".join(
        "# " + line + "\n" for line in yaml.safe_dump(metadata, sort_keys=False).splitlines()
    ).encode()
    canonical.write_bytes(header + external._tsv(fields, rows))
    review_path = tmp_path / "external-review.json"
    review = json.loads(review_path.read_bytes())
    evidence_path = tmp_path / "external-evidence.json"
    evidence = json.loads(evidence_path.read_bytes())
    decision = review["decisions"][0]
    decision.update(row_sha256=external.row_sha256(rows[0]), disposition=disposition)
    evidence["entries"]["1"].update(row_sha256=decision["row_sha256"], disposition=disposition)
    write_json(evidence_path, evidence)
    review["inputs"]["external-evidence.json"] = external.digest(evidence_path)
    review["source_sha256"] = external.digest(canonical)
    write_json(review_path, review)
    fixture.review["external_review"]["sha256"] = external.digest(review_path)
    fixture.seal()
    expected, _ = external.expected_products(tmp_path, review_path)
    manifest = binding.export_candidate(tmp_path, fixture.review_path, fixture.output)
    assert binding.validate_candidate(tmp_path, fixture.review_path, fixture.output) == manifest
    for name, content in expected.items():
        assert (fixture.output / ("external-" + name)).read_bytes() == content
    product = (
        "ingredient_mappings.sssom.tsv"
        if disposition == "SUPPORTED"
        else "withheld_mappings.sssom.tsv"
    )
    published = binding._sssom_rows((fixture.output / ("external-" + product)).read_bytes())
    assert published[0] == rows[0]
    assert external.row_sha256(published[0]) == decision["row_sha256"]
    assert manifest["external_counts"] == {
        "source": 4,
        "supported": 4 if disposition == "SUPPORTED" else 3,
        "withhold": 0 if disposition == "SUPPORTED" else 1,
    }
    assert manifest["production_authorized"] is False
