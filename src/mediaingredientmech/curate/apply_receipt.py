"""Reserve fresh curation evidence outputs before a mutator writes its owner."""

import os
from contextlib import ExitStack, contextmanager
from pathlib import Path


def _still_reserved(path: Path, identity: tuple[int, int]) -> bool:
    """Check the directory entry itself, without following a replacement symlink."""
    try:
        current = path.lstat()
    except (FileNotFoundError, NotADirectoryError):
        return False
    return (current.st_dev, current.st_ino) == identity


@contextmanager
def reserve_receipt_outputs(log: Path, *, backup_paths: tuple[Path, ...] | None = None):
    """Yield the exclusive receipt handle followed by binary backup handles.

    By default, reserve ``log.with_suffix(".before.yaml")`` and yield the
    existing ``(receipt, backup)`` pair. Explicit ``backup_paths`` are reserved
    in order, and yield ``(receipt, *backups)`` only after every open succeeds.
    An existing receipt or backup, including a symlink, refuses the operation.

    Check reservation identities before yielding. On reservation failure,
    remove only paths still naming this call's open files; a competing
    replacement is not ours to remove. Keep handles open through cleanup so
    an unlinked reserved file's inode cannot be reused during these checks.
    Once the mutator starts, keep its evidence even if a later write fails;
    never erase a source backup after the owner may have changed.
    """
    log.parent.mkdir(parents=True, exist_ok=True)
    paths = backup_paths if backup_paths is not None else (log.with_suffix(".before.yaml"),)
    stack = ExitStack()
    created = []
    try:
        receipt = stack.enter_context(log.open("x", encoding="utf-8"))
        info = os.fstat(receipt.fileno())
        created.append((log, (info.st_dev, info.st_ino)))
        backups = []
        for path in paths:
            backup = stack.enter_context(path.open("xb"))
            info = os.fstat(backup.fileno())
            created.append((path, (info.st_dev, info.st_ino)))
            backups.append(backup)
        for path, identity in created:
            if not _still_reserved(path, identity):
                raise ValueError(f"Reserved evidence output was replaced or removed: {path}")
    except Exception:
        try:
            for path, identity in created:
                if _still_reserved(path, identity):
                    path.unlink(missing_ok=True)
        finally:
            stack.close()
        raise
    try:
        yield (receipt, *backups)
    finally:
        stack.close()
