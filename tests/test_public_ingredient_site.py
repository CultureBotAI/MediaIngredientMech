"""The deployed artifact, rather than a local renderer preview, covers every record."""

import importlib.util
import json
from pathlib import Path

import pytest
import yaml

ROOT = Path(__file__).resolve().parents[1]


@pytest.fixture
def builder():
    spec = importlib.util.spec_from_file_location(
        "mim_site_builder", ROOT / "scripts/build_pages_site.py"
    )
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


@pytest.fixture
def corpus(tmp_path, builder, monkeypatch):
    repo = tmp_path / "repo"
    docs = repo / "docs"
    docs.mkdir(parents=True)
    for name in ("index.html", "browser.html", "theme-toggle.js", "map-record-navigation.js", "ingredient_umap.html", "ingredient_graph.html"):
        (docs / name).write_text((ROOT / "docs" / name).read_text())
    source = repo / "data/ingredients/mapped/Mix + tea.yaml"
    source.parent.mkdir(parents=True)
    source.write_text(
        yaml.safe_dump(
            {
                "identifier": "CHEBI:123",
                "preferred_term": "Tea <script>alert(1)</script>",
                "mapping_status": "MAPPED",
                "ingredient_type": "UNDEFINED_MIXTURE",
                "components": [
                    {
                        "component_name": "water",
                        "component_id": "CHEBI:15377",
                        "reference_scope": "EXTERNAL_TERM",
                    }
                ],
                "component_assertion": {"method": "LABEL_ENUMERATION", "completeness": "COMPLETE"},
            }
        )
    )
    monkeypatch.setattr(builder.render, "REPO_ROOT", repo)
    return repo, source


def test_public_catalog_routes_render_typed_components_and_escape_index(corpus, builder, tmp_path):
    repo, _ = corpus
    output = tmp_path / "site"
    assert builder.build_site(repo, output) == 1
    builder.check_site(repo, output)
    data = json.loads((output / "data/ingredients.json").read_text())
    page = output / data["ingredients"][0]["detail_page"]
    assert page.is_file()
    assert page.relative_to(output).as_posix() == "records/ingredient/mapped/Mix_tea.html"
    html = page.read_text()
    assert "Material components" in html and "LABEL_ENUMERATION" in html
    assert "EXTERNAL_TERM" in html and "CHEBI:15377" in html
    assert '<main id="main-content">' in html
    assert 'href="../../../browser.html"' in html
    assert 'src="../../../theme-toggle.js"' in html
    assert "<script>alert(1)</script>" not in (output / "records/index.html").read_text()
    assert "&lt;script&gt;" in (output / "records/index.html").read_text()


@pytest.mark.parametrize("mutation", ["source", "page", "catalog", "asset", "build-input"])
def test_site_checker_rejects_missing_or_stale_generated_content(
    corpus, builder, tmp_path, mutation
):
    repo, source = corpus
    output = tmp_path / "site"
    builder.build_site(repo, output)
    catalog = output / "data/ingredients.json"
    page = output / json.loads(catalog.read_text())["ingredients"][0]["detail_page"]
    if mutation == "source":
        source.write_text(source.read_text().replace("water", "salt"))
    elif mutation == "page":
        page.unlink()
    elif mutation == "catalog":
        data = json.loads(catalog.read_text())
        data["ingredients"] = []
        catalog.write_text(json.dumps(data))
    elif mutation == "asset":
        (output / "records/style.css").write_text("broken")
    else:
        (repo / "docs/browser.html").write_text("changed source")
    with pytest.raises((ValueError, FileNotFoundError)):
        builder.check_site(repo, output)


def test_slug_collision_refuses_build_before_overwriting_record(corpus, builder, tmp_path):
    repo, source = corpus
    source.with_name("Mix   tea.yaml").write_text(source.read_text())
    output = tmp_path / "site"
    with pytest.raises(ValueError, match="collide"):
        builder.build_site(repo, output)
    assert not output.exists()


def test_pages_and_required_check_build_the_same_public_artifact():
    deploy = yaml.safe_load((ROOT / ".github/workflows/generate-pages.yaml").read_text())
    steps = deploy["jobs"]["deploy"]["steps"]
    build = next(s for s in steps if "build_pages_site.py" in s.get("run", ""))
    upload = next(s for s in steps if s.get("uses", "").startswith("actions/upload-pages-artifact"))
    assert "--output site" in build["run"]
    assert upload["with"]["path"] == "site"
    triggers = deploy.get("on", deploy.get(True))
    assert "data/ingredients/**" in triggers["push"]["paths"]
    ci = yaml.safe_load((ROOT / ".github/workflows/qc-flat-coverage.yaml").read_text())
    assert any("build_pages_site.py" in s.get("run", "") for s in ci["jobs"]["qc"]["steps"])


@pytest.mark.parametrize(
    "dependency",
    [
        "micro_source.py",
        "ontology_sources/micro/manifest.json",
        "synonym_policy.py",
        "utils/yaml_handler.py",
    ],
)
def test_checker_rejects_dependency_only_drift(corpus, builder, tmp_path, monkeypatch, dependency):
    import shutil

    repo, _ = corpus
    package = tmp_path / "package"
    shutil.copytree(builder.PACKAGE_ROOT, package, ignore=shutil.ignore_patterns("__pycache__"))
    monkeypatch.setattr(builder, "PACKAGE_ROOT", package)
    output = tmp_path / "site"
    builder.build_site(repo, output)
    changed = package / dependency
    changed.write_text(changed.read_text() + "\n")
    with pytest.raises(ValueError, match="build inputs are stale"):
        builder.check_site(repo, output)
