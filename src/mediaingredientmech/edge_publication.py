"""Exclusive manifest-last native publication (CLAW #767; MIM #1145/#1146)."""

from __future__ import annotations

import os
from pathlib import Path


def _directory(path: Path) -> int:
    return os.open(path, os.O_RDONLY | os.O_DIRECTORY | os.O_NOFOLLOW)


def publish_stage(stage: Path, output: Path) -> None:
    """Publish immutable files, making manifest.json the atomic commit marker.

    Existing destinations are never replaced. An interrupted publication may
    leave a directory without a manifest; readers must ignore that incomplete
    directory and a retry must choose a new destination.
    """
    names = ("assertions.jsonl", "manifest.json")
    if {path.name for path in stage.iterdir()} != set(names):
        raise ValueError("Native stage must contain exactly payload and manifest")
    for name in names:
        path = stage / name
        if path.is_symlink() or not path.is_file():
            raise ValueError("Native staged outputs must be regular files")
        with path.open("rb") as stream:
            os.fsync(stream.fileno())
    stage_fd = _directory(stage)
    try:
        os.fsync(stage_fd)
    finally:
        os.close(stage_fd)

    # mkdir is the exclusive reservation; unlike rename it cannot replace an
    # empty directory that another publisher created after a prior check.
    output.mkdir()
    output_fd = _directory(output)
    try:
        for name in names:
            os.link(stage / name, name, dst_dir_fd=output_fd, follow_symlinks=False)
            # The payload entry is durable before the complete manifest appears.
            os.fsync(output_fd)
        actual, opened = output.lstat(), os.fstat(output_fd)
        if (actual.st_dev, actual.st_ino) != (opened.st_dev, opened.st_ino):
            raise ValueError("Native destination directory changed during publication")
    finally:
        os.close(output_fd)
    parent_fd = _directory(output.parent)
    try:
        os.fsync(parent_fd)
    finally:
        os.close(parent_fd)
