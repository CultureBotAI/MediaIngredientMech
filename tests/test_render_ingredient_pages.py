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
