"""Ingredient detail pages expose typed component partonomy (#369)."""

import yaml

from mediaingredientmech import render_ingredient_pages as render


def test_component_partonomy_is_rendered_with_micro_link(tmp_path, monkeypatch):
    monkeypatch.setattr(render, "REPO_ROOT", tmp_path)
    source = tmp_path / "data" / "ingredients" / "mapped" / "Test_Mix.yaml"
    source.parent.mkdir(parents=True)
    source.write_text(
        yaml.safe_dump(
            {
                "identifier": "kgmicrobe.ingredient:test_mix",
                "preferred_term": "Test mix",
                "mapping_status": "MAPPED",
                "ingredient_type": "UNDEFINED_MIXTURE",
                "components": [
                    {
                        "component_name": "clarified rumen fluid",
                        "component_id": "MICRO:0000520",
                        "reference_scope": "EXTERNAL_TERM",
                    }
                ],
                "component_assertion": {
                    "method": "LABEL_ENUMERATION",
                    "completeness": "COMPLETE",
                    "evidence": [
                        {
                            "evidence_type": "SOURCE_LABEL",
                            "source": "microbedecoder",
                            "source_record": "Test mix",
                        }
                    ],
                },
            },
            sort_keys=False,
        ),
        encoding="utf-8",
    )
    output_dir = tmp_path / "pages" / "ingredient"
    status, _, slug = render.render_one(render.make_env(), source, output_dir, force=True)
    assert status == "rendered"
    html = (output_dir / f"{slug}.html").read_text(encoding="utf-8")
    assert "Material components" in html
    assert "LABEL_ENUMERATION" in html
    assert "clarified rumen fluid" in html
    assert "MICRO_0000520" in html


def test_micro_curie_has_an_ols_resolver():
    assert "MICRO_0000520" in render.curie_to_url("MICRO:0000520")


def test_rejected_labels_are_not_rendered_as_synonyms(tmp_path, monkeypatch):
    monkeypatch.setattr(render, "REPO_ROOT", tmp_path)
    source = tmp_path / "data" / "ingredients" / "mapped" / "Reviewed.yaml"
    source.parent.mkdir(parents=True)
    source.write_text(
        yaml.safe_dump(
            {
                "identifier": "CHEBI:1",
                "preferred_term": "Reviewed material",
                "synonyms": [
                    {
                        "synonym_text": "Accepted alias",
                        "synonym_type": "EXACT_SYNONYM",
                        "source": "curator",
                    },
                    {
                        "synonym_text": "Wrong upstream candidate",
                        "synonym_type": "REJECTED_LABEL",
                        "source": "upstream enrichment",
                    },
                ],
            },
            sort_keys=False,
        ),
        encoding="utf-8",
    )
    output_dir = tmp_path / "pages" / "ingredient"

    status, _, slug = render.render_one(render.make_env(), source, output_dir, force=True)

    assert status == "rendered"
    html = (output_dir / f"{slug}.html").read_text(encoding="utf-8")
    synonym_section, rejected_section = html.split(
        '<section id="rejected-labels">', maxsplit=1
    )
    assert "Accepted alias" in synonym_section
    assert "Wrong upstream candidate" not in synonym_section
    assert "Rejected enrichment labels" in rejected_section
    assert "Wrong upstream candidate" in rejected_section
    assert "not synonyms and do not resolve" in rejected_section
