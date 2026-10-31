"""Missing graph vectors cannot become synthetic biological neighborhoods."""

import sys
import types

import numpy as np
import pytest
import yaml

from scripts.generate_ingredient_umap import IngredientUMAPGenerator, build_visualization_data


def write_record(root, stem, identifier, category="mapped", **extra):
    path = root / category / f"{stem}.yaml"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        yaml.safe_dump(
            {
                "identifier": identifier,
                "preferred_term": stem,
                "mapping_status": category.upper(),
                **extra,
            }
        )
    )


def test_missing_mapped_and_unmapped_are_omitted_with_coverage(tmp_path, monkeypatch):
    captured = []

    class Reducer:
        def __init__(self, **kwargs):
            self.n_neighbors, self.n_MN, self.n_FP = 1, 0, 1

        def fit_transform(self, vectors, **kwargs):
            captured.append(vectors.copy())
            return vectors[:, :2]

    monkeypatch.setitem(sys.modules, "pacmap", types.SimpleNamespace(PaCMAP=Reducer))
    vectors = {"CHEBI:1": np.array([1.0, 2.0, 3.0]), "CHEBI:2": np.array([4.0, 5.0, 6.0])}
    write_record(tmp_path, "direct", "CHEBI:1")
    write_record(tmp_path, "ontology", "OTHER:1", ontology_mapping={"ontology_id": "CHEBI:2"})
    write_record(tmp_path, "missing_mapped", "CHEBI:missing")
    write_record(tmp_path, "missing_unmapped", "UNMAPPED_4", "unmapped")
    generator = IngredientUMAPGenerator(vectors)
    frame = generator.generate_umap(tmp_path)
    second = generator.generate_umap(tmp_path)
    assert len(frame) == len(second) == 2
    assert frame.attrs["coverage"] == {
        "eligible_records": 4,
        "embedded_records": 2,
        "missing_records": ["MIM:missing_mapped", "MIM:missing_unmapped"],
        "synthetic_records": 0,
        "eligible": 4,
        "projected": 2,
        "omitted": 2,
        "rejected_records": [],
    }
    np.testing.assert_array_equal(captured[0], captured[1])
    rows = {row["id"]: row for row in build_visualization_data(frame, tmp_path)}
    assert rows["MIM:direct"]["embedding_method"] == "direct_identifier"
    assert rows["MIM:ontology"]["embedding_method"] == "ontology_mapping"
    assert rows["MIM:ontology"]["embedding_source_node"] == "CHEBI:2"


@pytest.mark.parametrize(
    "record,expected",
    [
        ({"identifier": "CHEBI:1"}, ("CHEBI:1", "direct_identifier")),
        (
            {"identifier": "UNMAPPED_1", "synonyms": [{"synonym_text": "CHEBI:1"}]},
            ("CHEBI:1", "synonym_reference"),
        ),
        (
            {"identifier": "UNMAPPED_1", "notes": "source_id=mediadive.ingredient:2"},
            ("mediadive.ingredient:2", "history_reference"),
        ),
        ({"identifier": "UNMAPPED_1"}, None),
    ],
)
def test_actual_lookup_method_is_retained(record, expected):
    generator = IngredientUMAPGenerator(
        {"CHEBI:1": np.ones(3), "mediadive.ingredient:2": np.ones(3)}
    )
    assert generator.match_embedding(record) == expected


def test_all_missing_does_not_invent_a_projection(tmp_path):
    write_record(tmp_path, "missing", "UNMAPPED_1", "unmapped")
    with pytest.raises(ValueError, match="No ingredient embeddings"):
        IngredientUMAPGenerator({}).generate_umap(tmp_path)
