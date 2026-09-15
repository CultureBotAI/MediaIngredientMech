"""Publication requires an explicit switch and current validated full inputs."""

from __future__ import annotations

import json
from pathlib import Path
from types import SimpleNamespace

import pytest

from mediaingredientmech import text_map_site as site


def configure(root: Path, value="false"):
    config = root / "conf" / "text_map.yaml"
    config.parent.mkdir(parents=True, exist_ok=True)
    config.write_text(f"enabled: {value}\n")


def fake_pipeline():
    calls = []
    profile = {
        "model": "BAAI/bge-large-en-v1.5",
        "revision": "d4aa6901d3a41ba39fb536a557fa166f842b0e09",
        "dimension": 1024,
        "max_seq_length": 512,
    }
    manifest = {"encoder": profile, "projection": {"implementation": "pacmap.PaCMAP"}}

    def validate(bundle, *, input_path):
        assert json.loads(input_path.read_text()) == {"test": "fresh full inputs"}
        calls.append(("validate", bundle, input_path))
        return manifest

    def stage(output, published_dir, *, input_path, expected_bundle):
        assert json.loads(input_path.read_text()) == {"test": "fresh full inputs"}
        calls.append(("stage", output, published_dir, expected_bundle))
        return manifest

    pipeline = SimpleNamespace(
        MODEL=profile["model"],
        MODEL_REVISION=profile["revision"],
        MODEL_DIMENSION=1024,
        MAX_SEQ_LENGTH=512,
        current_bundle=lambda output: output / ("a" * 64),
        validate_bundle=validate,
        stage_map=stage,
    )
    return pipeline, calls, manifest


def enable_fixture(root, monkeypatch):
    configure(root, "true")
    source = root / "data" / "text_map"
    source.mkdir(parents=True)
    (source / "current.json").write_text("{}")
    pipeline, calls, manifest = fake_pipeline()
    monkeypatch.setattr(site, "load_pipeline", lambda _root: pipeline)

    def export(actual_root, output, **kwargs):
        assert actual_root == root
        assert not kwargs, "publication cannot request a canary or limited input set"
        output.write_text(json.dumps({"test": "fresh full inputs"}))
        return {"scope": "full"}

    monkeypatch.setattr(site, "export_inputs", export)
    return pipeline, calls, manifest


def test_disabled_map_requires_no_runtime_or_artifact(tmp_path, monkeypatch):
    configure(tmp_path)
    monkeypatch.setattr(
        site, "load_pipeline", lambda _root: pytest.fail("disabled map loaded runtime")
    )
    with site.prepare_text_map(tmp_path) as ready:
        assert ready is None


def test_enabled_map_missing_bundle_fails(tmp_path):
    configure(tmp_path, "true")
    with pytest.raises(ValueError, match="current.json"), site.prepare_text_map(tmp_path):
        pass


def test_enabled_map_missing_shared_runtime_fails(tmp_path):
    configure(tmp_path, "true")
    source = tmp_path / "data" / "text_map"
    source.mkdir(parents=True)
    (source / "current.json").write_text("{}")
    with pytest.raises(ValueError, match="CLAW-governed"), site.prepare_text_map(tmp_path):
        pass


@pytest.mark.parametrize("value", ["1", "'true'", "null", "[]"])
def test_enablement_requires_an_actual_boolean(tmp_path, value):
    configure(tmp_path, value)
    with pytest.raises(ValueError, match="enabled boolean"), site.prepare_text_map(tmp_path):
        pass


def test_enabled_map_uses_fresh_full_inputs_and_canonical_stage(tmp_path, monkeypatch):
    _, calls, _ = enable_fixture(tmp_path, monkeypatch)
    with site.prepare_text_map(tmp_path) as ready:
        inputs = ready.inputs
        ready.stage(tmp_path / "published")
        assert calls[-1] == (
            "stage",
            tmp_path / "data" / "text_map",
            tmp_path / "published" / "text-map",
            "a" * 64,
        )
    assert not inputs.exists()
    assert calls[0][0] == "validate"


def test_legacy_encoder_cannot_be_published_as_the_common_space(tmp_path, monkeypatch):
    _, _, manifest = enable_fixture(tmp_path, monkeypatch)
    manifest["encoder"] = {"model": "MiniLM", "revision": "0" * 40, "dimension": 384}
    with pytest.raises(ValueError, match="pinned fleet BGE"), site.prepare_text_map(tmp_path):
        pass


def test_injected_projector_cannot_reach_the_site_build(tmp_path, monkeypatch):
    _, _, manifest = enable_fixture(tmp_path, monkeypatch)
    manifest["projection"]["implementation"] = "injected-projector"
    with pytest.raises(ValueError, match="actual PaCMAP"), site.prepare_text_map(tmp_path):
        pass


def test_subset_receipt_cannot_reach_publication(tmp_path, monkeypatch):
    enable_fixture(tmp_path, monkeypatch)
    monkeypatch.setattr(site, "export_inputs", lambda _root, _output: {"scope": "subset"})
    with pytest.raises(ValueError, match="full-corpus"), site.prepare_text_map(tmp_path):
        pass


def test_pointer_change_does_not_replace_the_preflight_generation(tmp_path, monkeypatch):
    pipeline, _, _ = enable_fixture(tmp_path, monkeypatch)
    published = tmp_path / "published" / "text-map"
    published.mkdir(parents=True)
    old = published / "index.html"
    old.write_text("previously published map")
    seen = []

    def checked_stage(output, published_dir, *, input_path, expected_bundle):
        seen.append(expected_bundle)
        if pipeline.current_bundle(output).name != expected_bundle:
            raise ValueError("current map differs from preflight generation")
        (published_dir / "index.html").write_text("replacement map")

    monkeypatch.setattr(pipeline, "stage_map", checked_stage)
    with site.prepare_text_map(tmp_path) as ready:
        monkeypatch.setattr(pipeline, "current_bundle", lambda output: output / ("b" * 64))
        with pytest.raises(ValueError, match="preflight generation"):
            ready.stage(tmp_path / "published")
    assert seen == ["a" * 64]
    assert old.read_text() == "previously published map"


def test_alternate_window_cannot_be_published_as_the_common_space(tmp_path, monkeypatch):
    _, _, manifest = enable_fixture(tmp_path, monkeypatch)
    manifest["encoder"]["max_seq_length"] = 256
    with pytest.raises(ValueError, match="pinned fleet BGE"), site.prepare_text_map(tmp_path):
        pass


def test_pages_upload_is_preceded_by_the_actual_staging_command():
    import yaml

    root = Path(__file__).resolve().parents[1]
    workflow = yaml.safe_load((root / ".github/workflows/generate-pages.yaml").read_text())
    steps = workflow["jobs"]["deploy"]["steps"]
    stage = next(
        index
        for index, step in enumerate(steps)
        if "python scripts/stage_text_map.py" in step.get("run", "")
    )
    upload = next(
        index
        for index, step in enumerate(steps)
        if step.get("uses", "").startswith("actions/upload-pages-artifact@")
    )
    assert stage < upload
    assert "|| true" not in steps[stage]["run"]
    trigger = workflow["on"] if "on" in workflow else workflow[True]
    paths = trigger["push"]["paths"]
    assert "data/text_map/**" in paths
    assert "conf/text_map.yaml" in paths


def test_common_and_graph_maps_remain_distinct():
    root = Path(__file__).resolve().parents[1]
    index = (root / "docs/index.html").read_text()
    assert index.index('href="text-map/"') < index.index('href="ingredient_umap.html"')
    assert "Ingredient graph maps" in index
    assert 'href="ingredient_graph.html"' in index


def test_build_docs_preflights_before_other_generators():
    import shutil
    import subprocess

    if shutil.which("just") is None:
        pytest.skip("actual recipe ordering requires just")
    root = Path(__file__).resolve().parents[1]
    result = subprocess.run(
        ["just", "--dry-run", "build-docs"], cwd=root, text=True, capture_output=True, check=True
    )
    commands = result.stdout + result.stderr
    assert commands.index("scripts/stage_text_map.py") < commands.index("gen-doc")
