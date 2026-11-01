"""Reserve fresh curation evidence outputs before a mutator writes its owner."""

from contextlib import ExitStack, contextmanager
from pathlib import Path


@contextmanager
def reserve_receipt_outputs(log: Path):
    """Yield exclusive receipt/backup handles; refuse either existing artifact.

    Reservation failures remove only files created by this call. Once the
    mutator starts, keep its evidence even if a later write fails; never erase
    a source backup after the owner may have changed.
    """
    log.parent.mkdir(parents=True, exist_ok=True)
    backup_path = log.with_suffix(".before.yaml")
    stack = ExitStack()
    created = []
    try:
        receipt = stack.enter_context(log.open("x", encoding="utf-8"))
        created.append(log)
        backup = stack.enter_context(backup_path.open("xb"))
        created.append(backup_path)
    except Exception:
        stack.close()
        for path in created:
            path.unlink()
        raise
    try:
        yield receipt, backup
    finally:
        stack.close()
