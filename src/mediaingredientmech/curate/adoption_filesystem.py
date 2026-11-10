"""Guarded file primitives for the stable-ID adoption transaction (#1303).

Extracted from campaign_owner_apply at 84241993a278a7a413422ef89a52c0b47dc57831.
Issue #1314 binds recovery directories and closes failed descriptor acquisitions.
These are filesystem operations, not schema validation, admission or a batch
transaction. Callers must validate bytes, hold the repository write lease,
reserve recovery evidence and recheck the complete transaction inputs.
See docs/adoption-filesystem.md for provenance and failure limits.
"""

from __future__ import annotations

import ctypes
import os
import stat
import sys
import tempfile
from pathlib import Path
from typing import Any

from mediaingredientmech.curate.publication_guard import FrozenFile, no_alias


def require(condition: Any, message: str) -> None:
    if not condition:
        raise ValueError(message)


def _new_owner(root: Path, name: str, raw: bytes, recheck):
    path = root / name
    no_alias(path)
    require(not os.path.lexists(path), "New destination exists")
    parent = path.parent
    parent_stat = parent.stat()
    fd = os.open(parent, os.O_RDONLY | os.O_DIRECTORY | os.O_NOFOLLOW)
    try:
        require(
            (os.fstat(fd).st_dev, os.fstat(fd).st_ino) == (parent_stat.st_dev, parent_stat.st_ino),
            "New-owner parent changed",
        )
        with tempfile.TemporaryDirectory(prefix=".campaign-new-", dir=parent) as directory:
            staging = Path(directory) / "owner.yaml"
            # Bytes already rendered and schema-validated in prepare.
            with staging.open("xb") as handle:
                handle.write(raw)
                handle.flush()
                os.fsync(handle.fileno())
            staged = FrozenFile.capture(staging)
            recheck()
            staged.verify()
            # Unlike replace, link refuses a competing final entry atomically.
            os.link(staging, path.name, dst_dir_fd=fd, follow_symlinks=False)
            staging.unlink()
            result = FrozenFile.capture(path)
            require(
                result.identity == staged.identity and result.content == raw,
                "Exclusive owner installation differs",
            )
            require(
                (parent.stat().st_dev, parent.stat().st_ino)
                == (parent_stat.st_dev, parent_stat.st_ino),
                "New-owner parent changed",
            )
            return result
    finally:
        os.close(fd)


def _rename_exclusive(source_fd: int, source: str, target_fd: int, target: str) -> None:
    """Refuse an occupied recovery entry atomically on maintained platforms.

    A portable os.rename overwrites an intervening recovery file. Refuse the
    operation if the platform lacks its no-replace primitive; never fall back.
    """
    libc = ctypes.CDLL(None, use_errno=True)
    if sys.platform == "darwin":
        function, flags = getattr(libc, "renameatx_np", None), 0x00000004
    elif sys.platform.startswith("linux"):
        function, flags = getattr(libc, "renameat2", None), 1
    else:
        function, flags = None, 0
    if function is None:
        raise ValueError("No exclusive owner-retirement primitive")
    function.argtypes = [
        ctypes.c_int,
        ctypes.c_char_p,
        ctypes.c_int,
        ctypes.c_char_p,
        ctypes.c_uint,
    ]
    function.restype = ctypes.c_int
    if function(source_fd, os.fsencode(source), target_fd, os.fsencode(target), flags) != 0:
        code = ctypes.get_errno()
        raise OSError(code, os.strerror(code), target)


def _retire(source: FrozenFile, recovery: Path, recheck):
    recovery = recovery.absolute()
    no_alias(recovery)
    initial = recovery.lstat()
    identity = (initial.st_dev, initial.st_ino)
    require(
        stat.S_ISDIR(initial.st_mode),
        "Relocation recovery path is not a directory",
    )
    parents = []
    for parent in recovery.parents:
        info = parent.stat()
        parents.append((parent, (info.st_dev, info.st_ino)))
    source_fd = recovery_fd = None

    def check_recovery(*, retired=False):
        no_alias(recovery)
        for parent, expected in parents:
            current = parent.stat()
            require(
                (current.st_dev, current.st_ino) == expected,
                "Relocation recovery ancestor changed",
            )
        current = recovery.lstat()
        require(
            stat.S_ISDIR(current.st_mode) and (current.st_dev, current.st_ino) == identity,
            "Relocation recovery directory changed",
        )
        if recovery_fd is not None:
            opened = os.fstat(recovery_fd)
            require(
                stat.S_ISDIR(opened.st_mode) and (opened.st_dev, opened.st_ino) == identity,
                "Relocation recovery descriptor changed",
            )
        require(
            set(os.listdir(recovery_fd if recovery_fd is not None else recovery))
            == ({"retired-owner.yaml"} if retired else set()),
            "Relocation recovery directory is not fresh or has unexpected entries",
        )

    check_recovery()
    source.verify()
    recheck()
    try:
        source_fd = os.open(source.path.parent, os.O_RDONLY | os.O_DIRECTORY | os.O_NOFOLLOW)
        recovery_fd = os.open(recovery, os.O_RDONLY | os.O_DIRECTORY | os.O_NOFOLLOW)
        require(
            (os.fstat(source_fd).st_dev, os.fstat(source_fd).st_ino) == source.parents[0][1],
            "Relocation source parent changed",
        )
        source.verify()
        check_recovery()
        # No bytes are destroyed. A raced entry is retained here and causes a
        # failed receipt; the operator never performs destructive auto-recovery.
        _rename_exclusive(source_fd, source.path.name, recovery_fd, "retired-owner.yaml")
        check_recovery(retired=True)
        retired = FrozenFile.capture(recovery / "retired-owner.yaml")
        require(
            retired.identity == source.identity and retired.content == source.content,
            "Relocation retired a changed entry; retained for recovery",
        )
        require(not os.path.lexists(source.path), "Relocation source reappeared")
        check_recovery(retired=True)
        return retired
    finally:
        try:
            if recovery_fd is not None:
                os.close(recovery_fd)
        finally:
            if source_fd is not None:
                os.close(source_fd)
