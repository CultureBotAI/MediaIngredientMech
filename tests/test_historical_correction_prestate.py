"""#1441: exact historical evidence setup must preserve current execution guards."""

from __future__ import annotations

import base64
import gzip
import importlib.util
import json
import os
from pathlib import Path
from types import SimpleNamespace

import pytest

from tests import historical_correction_prestate as context

ROOT = context.ROOT


def original_module():
    spec = importlib.util.spec_from_file_location(
        "test_original_diketo_1441", ROOT / context.MODULE
    )
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def copy_inputs(root):
    names = {context.MODULE, context.WRITER, context.MANIFEST}
    meta = json.loads((ROOT / context.MANIFEST).read_bytes())
    names.update(meta["files"])
    for name in names:
        target = root / name
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes((ROOT / name).read_bytes())
    return root


def test_complete_context_changes_only_evidence_roots_and_restores_them(tmp_path):
    module = original_module()
    writer = module.writer
    code = writer.propose_sources.__code__
    dependencies = dict(writer._LOADED_CODE)
    maintained = (ROOT / context.HISTORICAL_SOURCE).read_bytes()
    destination = tmp_path / "evidence"
    with context.correction_context(module, destination) as bound:
        assert bound is True
        assert module.ROOT == writer.ROOT == destination
        assert writer.propose_sources.__code__ is code
        assert writer._LOADED_CODE == dependencies
        inputs = context.evidence_bytes()
        assert set(inputs) == {
            context.MANIFEST,
            *writer.META["files"],
            *writer.META["protected_anchors"],
        }
        assert all((destination / name).read_bytes() == raw for name, raw in inputs.items())
        assert writer.evidence_inputs(writer.ROOT)
        historical = (destination / context.HISTORICAL_SOURCE).read_bytes()
        assert (
            context.digest(historical) == writer.META["files"][context.HISTORICAL_SOURCE]["sha256"]
        )
        assert historical != maintained
    assert module.ROOT == writer.ROOT == ROOT
    assert (ROOT / context.HISTORICAL_SOURCE).read_bytes() == maintained
    assert writer._LOADED_CODE == dependencies
    assert b'ROOT / "src/mediaingredientmech/additional_mappings.py"' in maintained


@pytest.mark.parametrize("kind", ["other", "same_basename"])
def test_unrelated_modules_never_read_archive_or_create_context(tmp_path, kind):
    name = "tests/other.py" if kind == "other" else "elsewhere/" + Path(context.MODULE).name
    module = SimpleNamespace(__file__=str(ROOT / name))
    destination = tmp_path / "must-not-exist"
    with context.correction_context(module, destination, archive=tmp_path / "missing.gz") as bound:
        assert bound is False
    assert not destination.exists()


@pytest.mark.parametrize("target", ["test", "writer"])
def test_changed_original_module_or_writer_refuses_before_output(tmp_path, target):
    repo = copy_inputs(tmp_path / "repository")
    name = context.MODULE if target == "test" else context.WRITER
    path = repo / name
    path.write_bytes(path.read_bytes() + b"\n# changed\n")
    module = SimpleNamespace(
        __file__=str(repo / context.MODULE),
        writer=SimpleNamespace(__file__=str(repo / context.WRITER)),
    )
    destination = tmp_path / "must-not-exist"
    with pytest.raises(
        ValueError, match="original test changed|original correction writer changed"
    ):
        with context.correction_context(module, destination, repository_root=repo):
            pytest.fail("Changed module entered context")
    assert not destination.exists()


@pytest.mark.parametrize("kind", ["outer", "content", "members", "revision"])
def test_archive_corruption_is_rejected_without_rewriting_manifest(tmp_path, monkeypatch, kind):
    raw = context.ARCHIVE.read_bytes()
    if kind == "outer":
        raw += b"changed"
    else:
        value = json.loads(gzip.decompress(raw))
        if kind == "content":
            value["files"][context.HISTORICAL_SOURCE] = base64.b64encode(b"wrong").decode()
        elif kind == "members":
            value["files"]["../foreign"] = value["files"].pop(context.HISTORICAL_SOURCE)
        else:
            value["source_revision"] = "unreviewed"
        raw = gzip.compress(json.dumps(value).encode(), mtime=0)
        monkeypatch.setattr(context, "ARCHIVE_SHA256", context.digest(raw))
    archive = tmp_path / "bad.gz"
    archive.write_bytes(raw)
    before = (ROOT / context.MANIFEST).read_bytes()
    with pytest.raises(
        ValueError, match="archive hash|archive contract|historical source/evidence"
    ):
        context.evidence_bytes(archive=archive)
    assert (ROOT / context.MANIFEST).read_bytes() == before


@pytest.mark.parametrize("kind", ["bytes", "symlink", "hardlink", "parent_alias"])
def test_all_other_manifest_inputs_remain_authenticated(tmp_path, kind):
    repo = copy_inputs(tmp_path / "repository")
    name = "reports/step7c_source_labels_313_235_20261102/sources/bacdive-34.html"
    path = repo / name
    if kind == "bytes":
        path.write_bytes(path.read_bytes() + b"changed")
    elif kind == "parent_alias":
        parent = path.parent
        foreign = tmp_path / "foreign-parent"
        parent.rename(foreign)
        parent.symlink_to(foreign, target_is_directory=True)
    else:
        foreign = tmp_path / "foreign"
        path.rename(foreign)
        if kind == "symlink":
            path.symlink_to(foreign)
        else:
            os.link(foreign, path)
    with pytest.raises(ValueError, match="historical source/evidence|aliased"):
        context.evidence_bytes(repository_root=repo)


@pytest.mark.parametrize("kind", ["symlink", "hardlink"])
def test_archive_aliases_are_refused_even_with_identical_bytes(tmp_path, kind):
    real = tmp_path / "real.gz"
    real.write_bytes(context.ARCHIVE.read_bytes())
    alias = tmp_path / "alias.gz"
    if kind == "symlink":
        alias.symlink_to(real)
    else:
        os.link(real, alias)
    with pytest.raises(ValueError, match="aliased"):
        context.evidence_bytes(archive=alias)


@pytest.mark.parametrize("kind", ["occupied", "aliased_parent"])
def test_destination_is_new_and_unaliased_before_any_write(tmp_path, kind):
    module = original_module()
    destination = tmp_path / "evidence"
    if kind == "occupied":
        destination.mkdir()
        (destination / "sentinel").write_bytes(b"keep")
    else:
        real = tmp_path / "real"
        real.mkdir()
        alias = tmp_path / "alias"
        alias.symlink_to(real, target_is_directory=True)
        destination = alias / "evidence"
    with pytest.raises(ValueError, match="destination must be new and unaliased"):
        with context.correction_context(module, destination):
            pytest.fail("Invalid output entered context")
    if kind == "occupied":
        assert (destination / "sentinel").read_bytes() == b"keep"
    else:
        assert list(real.iterdir()) == []
    assert module.ROOT == module.writer.ROOT == ROOT


@pytest.mark.parametrize("kind", ["content", "extra", "symlink", "same_bytes_replacement"])
def test_late_evidence_change_refuses_and_always_restores_module_roots(tmp_path, kind):
    module = original_module()
    destination = tmp_path / "evidence"
    with pytest.raises(
        ValueError, match="context content|context membership|aliased|context identity"
    ):
        with context.correction_context(module, destination):
            path = destination / context.HISTORICAL_SOURCE
            if kind == "content":
                path.write_bytes(path.read_bytes() + b"changed")
            elif kind == "extra":
                (destination / "extra").write_bytes(b"extra")
            else:
                foreign = tmp_path / "foreign"
                path.rename(foreign)
                if kind == "symlink":
                    path.symlink_to(foreign)
                else:
                    path.write_bytes(foreign.read_bytes())
    assert module.ROOT == module.writer.ROOT == ROOT


def test_wrong_loaded_evidence_root_refuses_before_output(tmp_path):
    module = original_module()
    module.writer.ROOT = tmp_path
    destination = tmp_path / "evidence"
    with pytest.raises(ValueError, match="unexpected original evidence root"):
        with context.correction_context(module, destination):
            pytest.fail("Wrong-root module entered context")
    assert not destination.exists()
