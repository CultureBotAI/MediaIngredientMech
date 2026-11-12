"""Issue #1222: actual opt-in executor closure, cached modules and substitutions."""

from __future__ import annotations

import builtins
import os
import subprocess
from copy import deepcopy
from types import SimpleNamespace

import pytest

from mediaingredientmech import ingredient_bundle_contract as native
from mediaingredientmech import retained_companion
from mediaingredientmech.export.companion_producer import BASE, LOADER, PATHS, load
from mediaingredientmech.validation.current_semantic_release import (
    _retained_companion_implementation,
)
from tests.test_retained_companion import ROOT
from tests.test_retained_companion import current as current
from tests.test_retained_companion import original as original


def test_cached_public_native_modules_and_resources_are_not_used(current, monkeypatch):
    def stale(*args, **kwargs):
        raise AssertionError("cached public implementation must not execute")

    monkeypatch.setattr(retained_companion, "reviewed_products", stale)
    monkeypatch.setattr(native, "contract_resource", stale)
    products, loaded = native.reviewed_products(current[0], current[1])
    assert loaded["retained_obligations"]["claim_count"] == 51
    assert set(loaded["retained_implementation"]["files"]) == set(PATHS)
    assert retained_companion.ARTIFACT in products


@pytest.mark.parametrize(
    "name",
    [
        "src/mediaingredientmech/retained_companion.py",
        "src/mediaingredientmech/export/companion_producer.py",
        "src/mediaingredientmech/profiles/ingredient_scope_v1.yaml",
        "uv.lock",
    ],
)
def test_rehashed_selected_dependency_is_not_executing_dependency(current, name):
    review, sources, _ = deepcopy(current)
    sources[name] += b"\n# test-only different selected bytes\n"
    review["inputs"][name] = native.content_sha256(sources[name])
    with pytest.raises(ValueError, match="executing/selected dependency differs"):
        native.reviewed_products(review, sources)


def fixture_capture(tmp_path):
    for name in PATHS:
        path = tmp_path / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes((ROOT / name).read_bytes())
    for args in [
        ["init", "-q"],
        ["add", "."],
        [
            "-c",
            "user.name=Fixture",
            "-c",
            "user.email=fixture@example.invalid",
            "commit",
            "-qm",
            "TEST ONLY captured executable closure",
        ],
    ]:
        subprocess.run(["git", *args], cwd=tmp_path, check=True, capture_output=True)
    return load(tmp_path, (tmp_path / LOADER).read_bytes())


@pytest.mark.parametrize(
    "name",
    [
        "src/mediaingredientmech/retained_companion.py",
        "src/mediaingredientmech/profiles/ingredient_bundle_v1.schema.json",
    ],
)
def test_changed_executing_dependency_refuses_completion(tmp_path, name):
    capture = fixture_capture(tmp_path)
    original = capture.implementation()
    assert name in original["files"]
    path = tmp_path / name
    path.write_bytes(path.read_bytes() + b"\n")
    with pytest.raises(ValueError, match="executed producer/dependency changed"):
        capture.implementation()


def test_same_byte_symlink_substitution_refused(tmp_path):
    capture = fixture_capture(tmp_path)
    path = tmp_path / "src/mediaingredientmech/retained_companion.py"
    alternate = tmp_path / "same-bytes.py"
    path.rename(alternate)
    path.symlink_to(alternate)
    with pytest.raises(ValueError, match="symlink"):
        capture.verify()


def test_uncaptured_relative_dependency_and_resource_refused(tmp_path):
    capture = fixture_capture(tmp_path)
    with pytest.raises(ValueError, match="uncaptured native dependency"):
        capture.imported(
            "", {"__package__": "mediaingredientmech"}, fromlist=("unlisted",), level=1
        )
    resources = capture.imported("importlib.resources", fromlist=("files",))
    with pytest.raises(ValueError, match="uncaptured companion resource"):
        resources.files("mediaingredientmech").joinpath("unlisted.json").read_bytes()


def test_semantic_membership_hook_is_conditional_and_complete():
    calls = []

    def read(name):
        calls.append(name)
        return (ROOT / name).read_bytes()

    inputs = SimpleNamespace(read=read)
    _retained_companion_implementation(inputs, {})
    assert calls == []
    _retained_companion_implementation(inputs, {"retained_obligations": {}})
    assert set(calls) == set(PATHS)
    changed = SimpleNamespace(
        read=lambda name: read(name) + (b"\n" if name.endswith("retained_companion.py") else b"")
    )
    with pytest.raises(ValueError, match="retained companion implementation differs"):
        _retained_companion_implementation(changed, {"retained_obligations": {}})


def test_direct_uncaptured_retained_entry_refused():
    with pytest.raises(ValueError, match="captured native entry required"):
        retained_companion.reviewed_products({}, {})


@pytest.mark.parametrize("alias", ["symlink", "hardlink", "ancestor"])
def test_initial_bootstrap_alias_refused_before_any_execution(tmp_path, monkeypatch, alias):
    """#1399: eventual rejection cannot undo top-level helper execution."""
    target = tmp_path / BASE
    target.parent.mkdir(parents=True)
    raw = (ROOT / BASE).read_bytes()
    target.write_bytes(raw)
    other = tmp_path / "identical-helper.py"
    if alias == "symlink":
        target.rename(other)
        target.symlink_to(other)
    elif alias == "hardlink":
        os.link(target, other)
    else:
        original_parent = target.parent
        moved = original_parent.with_name("actual-export")
        original_parent.rename(moved)
        original_parent.symlink_to(moved, target_is_directory=True)
    executions = []
    actual_exec = builtins.exec

    def observe(code, *args, **kwargs):
        if getattr(code, "co_filename", None) == str(target):
            executions.append(code.co_filename)
        return actual_exec(code, *args, **kwargs)

    monkeypatch.setattr(builtins, "exec", observe)
    with pytest.raises(ValueError, match="Companion bootstrap:.*alias"):
        load(tmp_path, (ROOT / LOADER).read_bytes())
    assert executions == []
