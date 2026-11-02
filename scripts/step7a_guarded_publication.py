"""#1086 journal confinement for the two new Step7a writers only.

Native transaction validation, data replacement and recovery format are retained.
Only journal creation/completion uses directory-relative descriptors; historical
publishers remain unchanged. Each application owns a fresh one-run directory.
The caller must create the canonical receipt parent before invoking this helper.
"""

from __future__ import annotations

import hashlib
import json
import os
import stat
import uuid
from contextlib import contextmanager
from pathlib import Path

from scripts import promote_heptahydrate_ncit as guarded

_CODE = Path(__file__).read_bytes()


def _require(condition, message):
    if not condition:
        raise ValueError(message)


def _canonical(path):
    path = Path(path).absolute()
    _require(path == path.resolve(), "Journal/receipt path is aliased")
    return path


def _identity(info):
    return info.st_dev, info.st_ino


def _journal_path(log):
    log = _canonical(log)
    return log.parent / (log.stem + "-journal")


def _absent(path):
    _require(not os.path.lexists(path), "Journal directory already exists; preserve it")


@contextmanager
def _reserve_directory(log):
    """Keep both descriptors open; never remove a competing path or old journal."""
    directory = _journal_path(log)
    _absent(directory)
    _canonical(directory.parent)
    intended = directory.parent.lstat()
    _require(stat.S_ISDIR(intended.st_mode), "Receipt parent must already be a directory")
    parent_identity = _identity(intended)
    parent_fd = os.open(directory.parent, os.O_RDONLY | os.O_DIRECTORY | os.O_NOFOLLOW)
    journal_fd = None
    try:
        _require(
            _identity(os.fstat(parent_fd)) == parent_identity,
            "Receipt parent changed during acquisition",
        )
        _canonical(directory.parent)
        _require(
            _identity(directory.parent.lstat()) == parent_identity,
            "Receipt parent changed before journal creation",
        )
        os.mkdir(directory.name, mode=0o700, dir_fd=parent_fd)
        journal_fd = os.open(
            directory.name, os.O_RDONLY | os.O_DIRECTORY | os.O_NOFOLLOW, dir_fd=parent_fd
        )
        journal_identity = _identity(os.fstat(journal_fd))

        def check():
            _canonical(directory)
            _require(
                _identity(directory.parent.stat()) == parent_identity,
                "Journal parent directory was replaced",
            )
            info = directory.lstat()
            _require(
                stat.S_ISDIR(info.st_mode) and _identity(info) == journal_identity,
                "Journal directory was replaced",
            )

        check()
        yield directory, journal_fd, check
    finally:
        if journal_fd is not None:
            os.close(journal_fd)
        os.close(parent_fd)


def _write_at(fd, name, payload, *, replacing=False):
    """Atomic native-format bytes through the held directory, never its pathname."""
    data = json.dumps(payload, indent=2, sort_keys=True).encode()
    temporary = ".journal-" + uuid.uuid4().hex + ".tmp"
    output = os.open(
        temporary, os.O_WRONLY | os.O_CREAT | os.O_EXCL | os.O_NOFOLLOW, 0o600, dir_fd=fd
    )
    try:
        with os.fdopen(output, "wb") as stream:
            stream.write(data)
            stream.flush()
            os.fsync(stream.fileno())
        if not replacing:
            # Link exclusively into the same held directory; never overwrite an
            # attacker-created final name. The temporary remains on failure.
            os.link(temporary, name, src_dir_fd=fd, dst_dir_fd=fd, follow_symlinks=False)
            os.unlink(temporary, dir_fd=fd)
        else:
            os.replace(temporary, name, src_dir_fd=fd, dst_dir_fd=fd)
    except Exception:
        # Preserve our staged/recovery bytes; do not unlink a competing entry.
        raise


def _read_at(fd, name):
    handle = os.open(name, os.O_RDONLY | os.O_NOFOLLOW, dir_fd=fd)
    with os.fdopen(handle, "rb") as stream:
        info = os.fstat(stream.fileno())
        _require(
            stat.S_ISREG(info.st_mode) and info.st_nlink == 1,
            "Journal must be a single regular file",
        )
        return stream.read()


def _transaction(root, validator, lease):
    from kg_microbe_write.transaction import JOURNAL_VERSION, ValidatedWriteTransaction

    directory, fd, check = lease

    class ConfinedJournalTransaction(ValidatedWriteTransaction):
        def _write_journal(self, changed, created):
            check()
            self._journal_name = "write-" + uuid.uuid4().hex + ".json"
            self._journal_payload = {
                "version": JOURNAL_VERSION,
                "root": str(self.root),
                "status": "in_progress",
                "changed": [str(p) for p in changed],
                "created": [str(p) for p in created],
                "previous": {
                    str(c.path): c.old_text for c in self.staged if c.changed and c.exists
                },
            }
            _write_at(fd, self._journal_name, self._journal_payload)
            check()  # Before the native owner replacement loop begins.
            return directory / self._journal_name

        def _complete_journal(self, path):
            check()
            _require(path == directory / self._journal_name, "Native journal path changed")
            _require(
                _read_at(fd, self._journal_name)
                == json.dumps(self._journal_payload, indent=2, sort_keys=True).encode(),
                "Native journal beforeimage changed",
            )
            payload = {**self._journal_payload, "status": "complete"}
            _write_at(fd, self._journal_name, payload, replacing=True)
            check()

        def _prune_journals(self, *, keep):
            # Exclusive one-run directory: no historical journals to prune.
            check()

    return ConfinedJournalTransaction(root, validator=validator, journal_dir=directory)


def completed_journal(root, log, saved, *, previous):
    """Verify the exact native recovery payload; inode values are not portable pins."""
    from kg_microbe_write.transaction import JOURNAL_VERSION

    directory = _journal_path(log)
    _require(directory.is_dir(), "Completed journal directory is absent")
    path = Path((saved.get("transaction") or {}).get("journal", ""))
    _require(
        path.is_absolute()
        and path.parent == directory
        and path.name.startswith("write-")
        and path.suffix == ".json",
        "Completed journal path differs",
    )
    _canonical(path)
    fd = os.open(directory, os.O_RDONLY | os.O_DIRECTORY | os.O_NOFOLLOW)
    try:
        identity = _identity(os.fstat(fd))
        _require(os.listdir(fd) == [path.name], "Completed journal membership changed")
        raw = _read_at(fd, path.name)
        _require(
            _identity(directory.stat()) == identity and directory == directory.resolve(),
            "Completed journal directory changed",
        )
    finally:
        os.close(fd)
    expected = {
        "version": JOURNAL_VERSION,
        "root": str(root),
        "status": "complete",
        "changed": sorted(str(root / p) for p in previous),
        "created": [],
        "previous": {str(root / p): b.decode() for p, b in previous.items()},
    }
    _require(
        raw == json.dumps(expected, indent=2, sort_keys=True).encode(),
        "Completed native journal payload differs",
    )
    _require(
        saved.get("journal_sha256") == hashlib.sha256(raw).hexdigest(),
        "Completed journal bytes differ",
    )
    return {path: raw}


def publish(root, outputs, inputs, log, backups, result, *, apply, validate_scope=None):
    """Same bounded receipt/publication interface, with a confined native journal."""
    _require(Path(__file__).read_bytes() == _CODE, "Loaded journal adapter changed")
    log = _canonical(log)
    _require(log.parent.is_dir(), "Receipt parent must already exist")
    _absent(_journal_path(log))
    reservations = {}

    def check_directory():
        _absent(_journal_path(log))

    def validate(path, text):
        _require(text.encode() == outputs[path.relative_to(root)], "Staged output differs")
        guarded.recheck(inputs)
        guarded.recheck_reserved(reservations)
        check_directory()
        if validate_scope is not None:
            validate_scope()

    if not apply:
        transaction = guarded.new_transaction(root, validate, None)
        for path, data in outputs.items():
            transaction.stage(path, data.decode())
        transaction.commit()
        return {**result, "applied": False, "changed": True}

    with _reserve_directory(log) as lease:
        directory, fd, check_directory = lease
        transaction = _transaction(root, validate, lease)
        for path, data in outputs.items():
            transaction.stage(path, data.decode())
        transaction.commit()
        with guarded.reserve_receipt_outputs(log, backup_paths=tuple(backups)) as handles:
            receipt, *backup_handles = handles
            for path, handle in zip((log, *backups), handles, strict=True):
                reservations[path] = _identity(os.fstat(handle.fileno()))
            applied = None
            mutation_started = False
            try:
                check_directory()
                guarded.recheck_reserved(reservations)
                guarded.recheck(inputs)
                for handle, data in zip(backup_handles, backups.values(), strict=True):
                    handle.write(data)
                    handle.flush()
                receipt.write(
                    json.dumps({**result, "applied": False, "state": "prepared"}, indent=2) + "\n"
                )
                receipt.flush()
                guarded.recheck_reserved(reservations)
                mutation_started = True
                applied = transaction.commit(apply=True)
                check_directory()
                journal = _read_at(fd, applied.journal_path.name)
                result = {
                    **result,
                    "transaction": applied.as_dict(),
                    "journal_sha256": hashlib.sha256(journal).hexdigest(),
                }
                guarded.recheck_reserved(reservations)
                _require(
                    all((root / p).read_bytes() == b for p, b in outputs.items()),
                    "Written outputs differ; retain recovery evidence",
                )
                receipt.seek(0)
                receipt.truncate()
                receipt.write(
                    json.dumps({**result, "applied": True, "state": "complete"}, indent=2) + "\n"
                )
                receipt.flush()
                guarded.recheck_reserved(reservations)
                check_directory()
            except Exception as error:
                failure = {
                    **result,
                    "state": "failed",
                    "error": str(error),
                    "applied": (
                        True if applied is not None else (None if mutation_started else False)
                    ),
                    "recovery_required": mutation_started,
                    "journal_directory": str(directory),
                }
                try:
                    receipt.seek(0)
                    receipt.truncate()
                    receipt.write(json.dumps(failure, indent=2) + "\n")
                    receipt.flush()
                except OSError:
                    pass
                raise
    return {**result, "applied": True, "changed": True}
