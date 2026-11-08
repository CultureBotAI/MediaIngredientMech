"""Regression coverage for exclusive, durable manifest-last publication."""

import json
import os
from pathlib import Path
import stat

import pytest

from mediaingredientmech.edge_publication import publish_stage


@pytest.fixture
def stage(tmp_path):
    directory = tmp_path / "stage"
    directory.mkdir()
    (directory / "assertions.jsonl").write_bytes(b'{"assertion":"fixture"}\n')
    (directory / "manifest.json").write_text(json.dumps({"rows": 1}))
    return directory


def test_existing_empty_destination_is_preserved(stage):
    output = stage.parent / "output"
    output.mkdir()
    before = output.stat().st_ino
    with pytest.raises(FileExistsError):
        publish_stage(stage, output)
    assert output.stat().st_ino == before
    assert list(output.iterdir()) == []


def test_concurrent_destination_creation_cannot_be_replaced(stage, monkeypatch):
    output = stage.parent / "output"
    original = os.mkdir

    def competing_mkdir(path, *args, **kwargs):
        if Path(path) == output:
            original(path, *args, **kwargs)
        return original(path, *args, **kwargs)

    monkeypatch.setattr(os, "mkdir", competing_mkdir)
    with pytest.raises(FileExistsError):
        publish_stage(stage, output)
    assert list(output.iterdir()) == []
    assert (stage / "manifest.json").is_file()


def test_manifest_commits_last_and_directories_are_synced(stage, monkeypatch):
    output = stage.parent / "output"
    linked, synced = [], []
    real_link, real_sync = os.link, os.fsync

    def link(source, target, **kwargs):
        if target == "manifest.json":
            assert os.stat("assertions.jsonl", dir_fd=kwargs["dst_dir_fd"]).st_size > 0
        linked.append(target)
        return real_link(source, target, **kwargs)

    def sync(fd):
        synced.append(stat.S_ISDIR(os.fstat(fd).st_mode))
        return real_sync(fd)

    monkeypatch.setattr(os, "link", link)
    monkeypatch.setattr(os, "fsync", sync)
    publish_stage(stage, output)
    assert linked == ["assertions.jsonl", "manifest.json"]
    assert synced.count(True) >= 4
    assert synced.count(False) == 2
    assert (output / "assertions.jsonl").read_bytes() == (stage / "assertions.jsonl").read_bytes()
    assert (output / "manifest.json").read_bytes() == (stage / "manifest.json").read_bytes()


def test_failure_before_manifest_leaves_no_committed_export(stage, monkeypatch):
    output = stage.parent / "output"
    real_link = os.link

    def link(source, target, **kwargs):
        if target == "manifest.json":
            raise OSError("simulated interruption")
        return real_link(source, target, **kwargs)

    monkeypatch.setattr(os, "link", link)
    with pytest.raises(OSError, match="simulated interruption"):
        publish_stage(stage, output)
    assert (output / "assertions.jsonl").is_file()
    assert not (output / "manifest.json").exists()
