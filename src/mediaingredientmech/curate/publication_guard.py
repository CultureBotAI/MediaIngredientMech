"""Bind bounded publications to unaliased reviewed inputs (#1153, #1154).

This guards filesystem scope, not scientific approval. Native validators still
produce the candidate. Atomic replacement never overwrites a linked old inode.
"""

from __future__ import annotations

import json
import os
import stat
from collections.abc import Callable
from dataclasses import dataclass
from pathlib import Path
from tempfile import TemporaryDirectory
from typing import BinaryIO, TextIO


def no_alias(path: Path) -> None:
    """Check the original spelling before resolving any symlink away."""
    if any(p.is_symlink() for p in (path, *path.parents)):
        raise ValueError(f"Filesystem alias refused: {path}")


def _identity(info: os.stat_result) -> tuple[int, int]:
    return info.st_dev, info.st_ino


def _regular(info: os.stat_result, path: Path) -> None:
    if not stat.S_ISREG(info.st_mode) or info.st_nlink != 1:
        raise ValueError(f"Nonregular file or hardlink alias refused: {path}")


@dataclass(frozen=True)
class FrozenFile:
    path: Path
    content: bytes
    identity: tuple[int, int]
    parents: tuple[tuple[Path, tuple[int, int]], ...]

    @classmethod
    def capture(cls, path: Path) -> FrozenFile:
        path = path.absolute()
        no_alias(path)
        parents = tuple((p, _identity(p.stat())) for p in path.parents)
        info = path.lstat()
        _regular(info, path)
        # O_NOFOLLOW also refuses a leaf replacement between lstat and open.
        descriptor = os.open(path, os.O_RDONLY | os.O_NOFOLLOW)
        with os.fdopen(descriptor, "rb") as source:
            opened = os.fstat(source.fileno())
            _regular(opened, path)
            if _identity(opened) != _identity(info):
                raise ValueError(f"File identity changed while opening: {path}")
            content = source.read()
            _regular(os.fstat(source.fileno()), path)
        result = cls(path, content, _identity(info), parents)
        result.check_location()
        return result

    def check_location(self) -> None:
        no_alias(self.path)
        for parent, identity in self.parents:
            if _identity(parent.stat()) != identity:
                raise ValueError(f"Input parent changed: {parent}")
        info = self.path.lstat()
        _regular(info, self.path)
        if _identity(info) != self.identity:
            raise ValueError(f"File identity changed: {self.path}")

    def verify(self) -> None:
        self.check_location()
        current = FrozenFile.capture(self.path)
        if current.identity != self.identity or current.content != self.content:
            raise ValueError(f"Captured input changed: {self.path}")


def check_reserved(handle: TextIO | BinaryIO, path: Path) -> None:
    """Retain the native reservation and reject late receipt/backup aliases."""
    no_alias(path)
    current, opened = path.lstat(), os.fstat(handle.fileno())
    _regular(current, path)
    _regular(opened, path)
    if _identity(current) != _identity(opened):
        raise ValueError(f"Reserved output changed: {path}")


def publish_validated(
    target: FrozenFile,
    render: Callable[[Path], None],
    recheck: Callable[[], None],
) -> FrozenFile:
    """Render through the caller's native gate, then replace one held entry.

    A link created even after the final check cannot make replacement mutate
    its old inode. Parent replacement is detected and never reports success.
    """
    target.verify()
    recheck()
    with TemporaryDirectory(prefix=".kgm-publication-", dir=target.path.parent) as directory:
        staged_path = Path(directory) / "validated-output"
        render(staged_path)
        staged = FrozenFile.capture(staged_path)
        parent_fd = os.open(target.path.parent, os.O_RDONLY | os.O_DIRECTORY | os.O_NOFOLLOW)
        target_fd = None
        try:
            if _identity(os.fstat(parent_fd)) != target.parents[0][1]:
                raise ValueError("Publication parent changed")
            target_fd = os.open(target.path.name, os.O_RDONLY | os.O_NOFOLLOW, dir_fd=parent_fd)
            opened = os.fstat(target_fd)
            _regular(opened, target.path)
            if _identity(opened) != target.identity:
                raise ValueError("Publication target changed")
            target.verify()
            recheck()
            staged.verify()
            os.replace(staged_path, target.path.name, dst_dir_fd=parent_fd)
            if os.fstat(target_fd).st_nlink != 0:
                raise ValueError("Target hardlink appeared during publication")
        finally:
            if target_fd is not None:
                os.close(target_fd)
            os.close(parent_fd)
        result = FrozenFile.capture(target.path)
        if result.content != staged.content or result.parents != target.parents:
            raise ValueError("Published output or parent differs")
        recheck()
        result.verify()
        return result


def finish_receipt(receipt: TextIO, path: Path, payload: dict, recheck: Callable[[], None]) -> None:
    """Never leave a success-shaped receipt after detected post-write drift."""
    try:
        check_reserved(receipt, path)
        recheck()
        receipt.write(json.dumps(payload, indent=2, ensure_ascii=False) + "\n")
        receipt.flush()
        check_reserved(receipt, path)
        recheck()
    except Exception:
        # Keep the reserved diagnostic file and source backup, but invalidate
        # a success payload if evidence drifted during receipt publication.
        receipt.seek(0)
        receipt.truncate()
        receipt.flush()
        raise
