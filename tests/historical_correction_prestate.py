"""Exact test-only evidence context for the historical #1111 writer (#1441).

The archived source-label script is an input named by the original manifest,
not executable replacement code. The current correction writer and its complete
current dependency capture execute unchanged. Only its evidence-root lookup and
the exact original test module's fixture input root are scoped to this prestate.
"""

from __future__ import annotations

import base64
import gzip
import hashlib
import json
import os
import stat
from contextlib import contextmanager
from pathlib import Path

from tests import historical_source_anchors as anchors

ROOT = anchors.ROOT
MODULE = "tests/test_correct_diketo_bacdive_evidence.py"
WRITER = "scripts/correct_diketo_bacdive_evidence.py"
WRITER_SHA256 = "b77c0307979f2b8225053c3f4257c34808981d94b567a13dc3e1adf0f6b173c3"
MANIFEST = "reports/diketo_bacdive_evidence_1111_20261102/source-evidence.json"
MANIFEST_SHA256 = "41defe43ca5fc06502964d155ea58376d5420c0ce2cb8ffe660294c18638d892"
HISTORICAL_SOURCE = "scripts/curate_step7c_source_labels.py"
SOURCE_REVISION = "21e76ee324a8a04bb4e5c1d48363b647020042d8"
ARCHIVE = Path(__file__).parent / "fixtures/historical_correction_prestate_1441/source.json.gz"
ARCHIVE_SHA256 = "8bab165a062573a3af61e88265252bb9a47408b6a496d63a8dd024bdd4be61a6"


def require(condition, message):
    if not condition:
        raise ValueError("Historical correction context: " + message)


def digest(raw):
    return hashlib.sha256(raw).hexdigest()


def file_state(info):
    return (
        info.st_dev,
        info.st_ino,
        info.st_mode,
        info.st_nlink,
        info.st_size,
        info.st_mtime_ns,
        info.st_ctime_ns,
    )


def regular(path):
    """Read exact unaliased evidence bytes, retaining file and parent identities."""
    path = Path(path).absolute()
    require(path == path.resolve(), "aliased input")
    parents = [(p, (p.stat().st_dev, p.stat().st_ino)) for p in path.parents]
    before = path.lstat()
    require(stat.S_ISREG(before.st_mode) and before.st_nlink == 1, "aliased input file")
    with os.fdopen(os.open(path, os.O_RDONLY | os.O_NOFOLLOW), "rb") as stream:
        opened = os.fstat(stream.fileno())
        require((opened.st_dev, opened.st_ino) == (before.st_dev, before.st_ino), "input replaced")
        raw = stream.read()
        require(
            file_state(os.fstat(stream.fileno())) == file_state(opened), "input changed during read"
        )
    after = path.lstat()
    require(file_state(after) == file_state(before) and path == path.resolve(), "input changed")
    require(
        all((p.stat().st_dev, p.stat().st_ino) == identity for p, identity in parents),
        "input parent changed",
    )
    return raw


def evidence_bytes(*, repository_root=ROOT, archive=ARCHIVE):
    """Authenticate every manifest file and protected anchor before any output."""
    manifest = regular(repository_root / MANIFEST)
    require(digest(manifest) == MANIFEST_SHA256, "manifest changed")
    meta = json.loads(manifest)
    compressed = regular(archive)
    require(digest(compressed) == ARCHIVE_SHA256, "archive hash changed")
    doc = json.loads(gzip.decompress(compressed))
    require(
        set(doc) == {"schema_version", "source_revision", "files"}
        and type(doc["schema_version"]) is int
        and doc["schema_version"] == 1
        and doc["source_revision"] == SOURCE_REVISION
        and set(doc["files"]) == {HISTORICAL_SOURCE},
        "archive contract changed",
    )
    historical = base64.b64decode(doc["files"][HISTORICAL_SOURCE], validate=True)
    result = {MANIFEST: manifest}
    for name, item in meta["files"].items():
        path = Path(name)
        require(not path.is_absolute() and ".." not in path.parts, "unsafe manifest path")
        raw = historical if name == HISTORICAL_SOURCE else regular(repository_root / path)
        require(
            digest(raw) == item["sha256"] and len(raw) == item["bytes"],
            "historical source/evidence changed: " + name,
        )
        result[name] = raw
    frozen = anchors.frozen_anchors()
    require(
        meta["protected_anchors"] == anchors.ANCHORS
        and all(
            digest(frozen[name]) == expected for name, expected in meta["protected_anchors"].items()
        ),
        "protected anchor contract changed",
    )
    require(not set(result) & set(frozen), "conflicting historical context members")
    return result | frozen


def verify_context(root, inputs, identities):
    require(root == root.resolve() and root.is_dir(), "aliased context root")
    members = set()
    for path in root.rglob("*"):
        require(not path.is_symlink(), "aliased context member")
        if path.is_file():
            members.add(path.relative_to(root).as_posix())
    require(members == set(inputs), "context membership changed")
    require(
        all(
            (path.stat().st_dev, path.stat().st_ino) == identity
            for path, identity in identities.items()
        ),
        "context identity changed",
    )
    require(
        all(regular(root / name) == raw for name, raw in inputs.items()), "context content changed"
    )


@contextmanager
def correction_context(module, destination, *, repository_root=ROOT, archive=ARCHIVE):
    """Bind only the exact original module/writer; restore both roots on exit."""
    path = Path(module.__file__)
    if path != repository_root / MODULE:
        yield False
        return
    require(digest(regular(path)) == anchors.MODULES[MODULE]["sha256"], "original test changed")
    writer = module.writer
    require(
        Path(writer.__file__) == repository_root / WRITER
        and digest(regular(repository_root / WRITER)) == WRITER_SHA256,
        "original correction writer changed",
    )
    require(module.ROOT == writer.ROOT == repository_root, "unexpected original evidence root")
    inputs = evidence_bytes(repository_root=repository_root, archive=archive)
    require(writer._MANIFEST == inputs[MANIFEST], "loaded manifest changed")
    destination = Path(destination).absolute()
    require(
        destination == destination.resolve()
        and not os.path.lexists(destination)
        and destination.parent.is_dir()
        and destination != repository_root,
        "context destination must be new and unaliased",
    )
    destination.mkdir()
    for name, raw in inputs.items():
        target = destination / name
        target.parent.mkdir(parents=True, exist_ok=True)
        with target.open("xb") as stream:
            stream.write(raw)
    identities = {
        path: (path.stat().st_dev, path.stat().st_ino)
        for path in (destination, *destination.parents, *destination.rglob("*"))
    }
    verify_context(destination, inputs, identities)
    original_test_root, original_writer_root = module.ROOT, writer.ROOT
    module.ROOT = writer.ROOT = destination
    try:
        yield True
    finally:
        module.ROOT, writer.ROOT = original_test_root, original_writer_root
        verify_context(destination, inputs, identities)
