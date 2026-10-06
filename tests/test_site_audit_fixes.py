"""Scientific record fields, identities and catalog statistics survive publication."""

import importlib.util
import json
from pathlib import Path

import yaml

from mediaingredientmech import render_ingredient_pages as render
from mediaingredientmech.schema_site import write_schema_site

ROOT = Path(__file__).resolve().parents[1]


def exporter():
    spec = importlib.util.spec_from_file_location(
        "audit_browser_export", ROOT / "scripts/browser_export.py"
    )
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_catalog_counts_actual_status_across_storage_directories(tmp_path):
    sources = tmp_path / "ingredients"
    rows = [
        ("mapped", "a", "REJECTED"),
        ("mapped", "b", "MAPPED"),
        ("unmapped", "c", "AMBIGUOUS"),
        ("unmapped", "d", "UNMAPPED"),
    ]
    for directory, name, status in rows:
        path = sources / directory / (name + ".yaml")
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(
            yaml.safe_dump(
                {
                    "identifier": "cas:" + name,
                    "preferred_term": name,
                    "mapping_status": status,
                    "ontology_mapping": {"ontology_id": "CHEBI:63895"},
                }
            )
        )
    output = tmp_path / "catalog.json"
    exporter().export_ingredients_to_json(sources, output)
    data = json.loads(output.read_text())
    assert data["metadata"]["mapped_count"] == data["metadata"]["unmapped_count"] == 1
    assert data["metadata"]["status_counts"] == {
        "AMBIGUOUS": 1,
        "MAPPED": 1,
        "REJECTED": 1,
        "UNMAPPED": 1,
    }
    assert all("chebi:63895" in row["searchable"] for row in data["ingredients"])
    assert {row["record_id"] for row in data["ingredients"]} == {"MIM:a", "MIM:b", "MIM:c", "MIM:d"}


def test_curated_fields_preserve_roles_context_reference_scope_and_escaping(tmp_path, monkeypatch):
    monkeypatch.setattr(render, "REPO_ROOT", tmp_path)
    source = tmp_path / "mapped" / "Fixture.yaml"
    source.parent.mkdir()
    source.write_text(
        yaml.safe_dump(
            {
                "identifier": "UNMAPPED_123",
                "preferred_term": "Fixture",
                "nutritional_roles": [
                    {
                        "role": "MINERAL_SOURCE",
                        "evidence": [
                            {
                                "reference_text": "doi:10.1000/example",
                                "curator_note": "<script>bad</script>",
                            }
                        ],
                    }
                ],
                "physicochemical_roles": [{"role": "BUFFER"}],
                "cellular_metabolic_roles": [{"role": "COFACTOR"}],
                "environmental_context": [
                    {"environment_term": "ENVO:00002007", "environment_label": "sediment"}
                ],
                "culturemech_reference": {
                    "medium_id": "CultureMech:002799",
                    "relationship": "SIMILAR_COMPOSITION",
                    "evidence": "Does not establish identity.",
                },
                "occurrence_statistics": {
                    "total_occurrences": 2,
                    "media_count": 1,
                    "source_occurrences": [{"source": "source-A", "count": 2}],
                },
            }
        )
    )
    status, _, slug = render.render_one(render.make_env(), source, tmp_path / "out", True)
    html = (tmp_path / "out" / (slug + ".html")).read_text()
    assert status == "rendered"
    for value in [
        "MINERAL_SOURCE",
        "BUFFER",
        "COFACTOR",
        "sediment",
        "SIMILAR_COMPOSITION",
        "Does not establish identity.",
        "source-A",
    ]:
        assert value in html
    assert 'href="#"' not in html and 'href=""' not in html
    assert 'href="https://doi.org/10.1000/example"' in html
    assert "https://culturebotai.github.io/CultureMech/pages/normalized/002799.html" in html
    assert "&lt;script&gt;bad&lt;/script&gt;" in html
    assert "{'source':" not in html


def test_resolvers_are_safe_and_leave_unsupported_primary_ids_unlinked():
    assert "meshb.nlm.nih.gov" in render.curie_to_url("mesh:C028805")
    assert not render.curie_to_url("UNMAPPED_0196")
    assert not render.curie_to_url("kgmicrobe.compound:gyps")
    text = str(render.linked_text("<img src=x> doi:10.1000/test. javascript:alert(1)"))
    assert "<img" not in text and 'href="javascript:' not in text
    assert "https://doi.org/10.1000/test" in text


def test_schema_site_includes_imported_enums_types_and_targets(tmp_path):
    files = write_schema_site(
        ROOT / "src/mediaingredientmech/schema/mediaingredientmech.yaml", tmp_path / "schema"
    )
    index = (tmp_path / "schema/index.html").read_text()
    for name in ["MappingStatusEnum", "DiscussionKindEnum", "string", "IngredientRecord"]:
        assert name in index
    assert all((tmp_path / p).is_file() for p in files)
    assert "REJECTED" in (tmp_path / "schema/enumerations-MappingStatusEnum.html").read_text()


def test_index_has_unique_group_anchors(tmp_path):
    render.write_index(
        tmp_path,
        [
            {
                "ingredient": {"identifier": "mesh:C1", "preferred_term": "<salt>"},
                "slug": "mapped/Salt",
            },
            {
                "ingredient": {"identifier": "CHEBI:2", "preferred_term": "Salt"},
                "slug": "mapped/Salt2",
            },
        ],
    )
    html = (tmp_path / "index.html").read_text()
    assert 'href="#prefix-mesh"' in html and 'id="prefix-mesh"' in html
    assert 'href="#prefix-CHEBI"' in html and 'id="prefix-CHEBI"' in html
    assert "&lt;salt&gt;" in html


def test_maintained_markdown_schema_index_lists_enums_and_types():
    index = (ROOT / "docs/index.md").read_text()
    assert (
        "[MappingStatusEnum](MappingStatusEnum.md)"
        in index.split("## Enumerations")[1].split("## Types")[0]
    )
    assert "[String](String.md)" in index.split("## Types")[1]
    for target in ["MappingStatusEnum.md", "String.md"]:
        assert (ROOT / "docs" / target).is_file()


def test_absent_recipe_reference_does_not_create_a_recipe_link(tmp_path, monkeypatch):
    monkeypatch.setattr(render, "REPO_ROOT", tmp_path)
    source = tmp_path / "mapped/Absent.yaml"
    source.parent.mkdir()
    source.write_text(yaml.safe_dump({"identifier": "CHEBI:15377", "preferred_term": "Water"}))
    env = render.make_env()
    output = tmp_path / "records"
    output.mkdir()
    render.render_one(env, source, output)
    text = (output / "mapped/Absent.html").read_text()
    assert "culturemech-reference" not in text
    assert "/CultureMech/pages/normalized/" not in text
