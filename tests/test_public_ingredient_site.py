"""The deployed artifact, rather than a local renderer preview, covers every record."""

import importlib.util
import json
from pathlib import Path

import pytest
import yaml

from mediaingredientmech.stable_ids import (
    LIFECYCLE_PATH, REGISTRY_PATH, Lifecycle, Mint, Registry,
    dump_lifecycle, dump_registry, resolver_url,
)

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
    (docs / "data").mkdir()
    for name in ("ingredient_umap.json", "ingredient_graph.json"):
        (docs / "data" / name).write_text(json.dumps({"points": [{"id": "MIM:0000001"}]}))
    source = repo / "data/ingredients/mapped/Mix + tea.yaml"
    source.parent.mkdir(parents=True)
    source.write_text(
        yaml.safe_dump(
            {
                "mim_id": "MIM:0000001",
                "legacy_identifiers": ["MIM:Mix_tea", "CHEBI:123"],
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
    registry = Registry((Mint("MIM:0000001", "Tea", "2026-11-08"),))
    (repo / REGISTRY_PATH).parent.mkdir(parents=True)
    (repo / REGISTRY_PATH).write_bytes(dump_registry(registry))
    (repo / LIFECYCLE_PATH).write_bytes(dump_lifecycle(registry))
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
    assert "Permanent record ID" in html and "MIM:0000001" in html
    assert "Mapping identifier" in html and "CHEBI:123" in html
    assert "Legacy identifiers" in html and "MIM:Mix_tea" in html
    assert '<main id="main-content">' in html
    assert 'href="../../../browser.html"' in html
    assert 'src="../../../theme-toggle.js"' in html
    assert "<script>alert(1)</script>" not in (output / "records/index.html").read_text()
    assert "&lt;script&gt;" in (output / "records/index.html").read_text()
    assert data["ingredients"][0]["record_id"] == "MIM:0000001"
    assert data["ingredients"][0]["stable_url"] == resolver_url("MIM:0000001")
    resolver = (output / "ingredient/MIM_0000001/index.html").read_text()
    assert 'href="../../records/ingredient/mapped/Mix_tea.html"' in resolver
    assert "&lt;script&gt;" in resolver and "<script>alert(1)</script>" not in resolver


@pytest.mark.parametrize("mutation", ["source", "page", "catalog", "asset", "build-input", "resolver"])
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
    elif mutation == "resolver":
        (output / "ingredient/MIM_0000001/index.html").write_text("stale destination")
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


@pytest.mark.parametrize("name", ["ingredient_umap.json", "ingredient_graph.json"])
def test_visualization_source_identity_changes_invalidate_site(corpus, builder, tmp_path, name):
    repo, _ = corpus
    output = tmp_path / "site"
    builder.build_site(repo, output)
    path = repo / "docs/data" / name
    path.write_text(path.read_text().replace("MIM:0000001", "MIM:9999999"))
    with pytest.raises(ValueError, match="build inputs are stale"):
        builder.check_site(repo, output)


@pytest.mark.parametrize("name", ["ingredient_umap.json", "ingredient_graph.json"])
def test_visualization_output_identity_changes_invalidate_site(corpus, builder, tmp_path, name):
    repo, _ = corpus
    output = tmp_path / "site"
    builder.build_site(repo, output)
    path = output / "data" / name
    path.write_text(path.read_text().replace("MIM:0000001", "MIM:9999999"))
    with pytest.raises(ValueError, match="Changed generated site asset"):
        builder.check_site(repo, output)


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


def test_stable_route_survives_label_filename_and_directory_change(corpus, builder, tmp_path):
    repo, source = corpus
    before = tmp_path / "before"
    builder.build_site(repo, before)
    original = json.loads((before / "data/ingredients.json").read_text())["ingredients"][0]
    assert (before / original["detail_page"]).is_file()
    record = yaml.safe_load(source.read_text())
    record["preferred_term"] = "Corrected name"
    replacement = repo / "data/ingredients/unmapped/Corrected_Name.yaml"
    replacement.parent.mkdir(parents=True)
    replacement.write_text(yaml.safe_dump(record))
    source.unlink()
    after = tmp_path / "after"
    builder.build_site(repo, after)
    current = json.loads((after / "data/ingredients.json").read_text())["ingredients"][0]
    assert current["stable_url"] == original["stable_url"]
    assert current["record_id"] == original["record_id"] == "MIM:0000001"
    assert current["detail_page"] != original["detail_page"]
    assert (after / current["detail_page"]).is_file()
    resolver = (after / "ingredient/MIM_0000001/index.html").read_text()
    assert "../../records/ingredient/unmapped/Corrected_Name.html" in resolver
    assert "mapped/Mix_tea.html" not in resolver


def test_retired_and_merged_ids_keep_tombstones_through_replacement_chain(corpus, builder, tmp_path):
    repo, source = corpus
    registry = Registry(
        tuple(Mint(f"MIM:{n:07d}", f"Mint label {n}", "2026-11-08") for n in (1, 2, 3)),
        (
            Lifecycle("MIM:0000001", "retired", "MIM:0000002", "2026-11-08T01:00:00Z", "Corrected identity"),
            Lifecycle("MIM:0000002", "merged", "MIM:0000003", "2026-11-08T02:00:00Z", "Merged duplicate"),
        ),
    )
    (repo / REGISTRY_PATH).write_bytes(dump_registry(registry))
    (repo / LIFECYCLE_PATH).write_bytes(dump_lifecycle(registry))
    record = yaml.safe_load(source.read_text())
    record["mim_id"] = "MIM:0000003"
    source.write_text(yaml.safe_dump(record))
    output = tmp_path / "site"
    builder.build_site(repo, output)
    first = (output / "ingredient/MIM_0000001/index.html").read_text()
    second = (output / "ingredient/MIM_0000002/index.html").read_text()
    assert "Mint label 1" in first and "identifier is retired" in first
    assert 'href="../MIM_0000002/"' in first
    assert 'href="../MIM_0000003/"' in first
    assert "identifier is merged" in second and 'href="../MIM_0000003/"' in second
    assert "../../records/ingredient/mapped/Mix_tea.html" in first
    assert len(json.loads((output / "records/build.json").read_text())["resolvers"]) == 3


@pytest.mark.parametrize("relative", [REGISTRY_PATH, LIFECYCLE_PATH])
def test_registry_and_lifecycle_are_bound_to_site_freshness(corpus, builder, tmp_path, relative):
    repo, source = corpus
    if relative == LIFECYCLE_PATH:
        registry = Registry(
            (Mint("MIM:0000001", "Old tea", "2026-11-08"), Mint("MIM:0000002", "Tea", "2026-11-08")),
            (Lifecycle("MIM:0000001", "merged", "MIM:0000002", "2026-11-08T01:00:00Z", "Duplicate reviewed"),),
        )
        (repo / REGISTRY_PATH).write_bytes(dump_registry(registry))
        (repo / LIFECYCLE_PATH).write_bytes(dump_lifecycle(registry))
        record = yaml.safe_load(source.read_text())
        record["mim_id"] = "MIM:0000002"
        source.write_text(yaml.safe_dump(record))
    output = tmp_path / "site"
    builder.build_site(repo, output)
    ledger = repo / relative
    # Valid structural changes leave the current page routes unchanged. Only
    # the input digest binding can detect these provenance-only differences.
    old = ledger.read_text()
    new = old.replace("Duplicate reviewed", "Duplicate rechecked") if relative == LIFECYCLE_PATH else old.replace("Tea", "Original tea")
    assert old != new
    ledger.write_text(new)
    with pytest.raises(ValueError, match="build inputs are stale"):
        builder.check_site(repo, output)


def test_site_refuses_duplicate_stable_id_before_promotion(corpus, builder, tmp_path):
    repo, source = corpus
    source.with_name("Distinct.yaml").write_text(source.read_text())
    output = tmp_path / "site"
    with pytest.raises(ValueError, match="Duplicate MIM ID"):
        builder.build_site(repo, output)
    assert not output.exists()


def test_site_refuses_unknown_record_id(corpus, builder, tmp_path):
    repo, source = corpus
    source.write_text(source.read_text().replace("MIM:0000001", "MIM:0000099"))
    with pytest.raises(ValueError, match="unknown or retired"):
        builder.build_site(repo, tmp_path / "site")
