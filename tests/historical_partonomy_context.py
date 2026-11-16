"""Authenticate the dated partonomy regression context without editing assertions.

#467: the original 2026-09-21 tests describe a finite historical corpus. Current
corpus validation remains separate in test_historical_partonomy_context.py.
This fixture restores data/evidence only; current validators and migration code
execute, and no historical fixture is installed into maintained data.
"""

from __future__ import annotations

import base64
import gzip
import hashlib
import json
import os
from contextlib import contextmanager
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REVISION = "085948099b3b8f37eced6248704a60cee3d9502c"
ARCHIVE = ROOT / "tests/fixtures/historical_partonomy_467/context.json.gz"
ARCHIVE_SHA256 = "eebf3e149c9ebd064e690cc56bd687a7ebebc022aa40df9355472be724b95de7"
INPUTS = {
    "data/curated/mapped_ingredients.yaml": (
        "27cc6d8e68d68c91eb2fc08586138182a5626ebf07f8903b774cdf81ce9b44a8",
        9654910,
    ),
    "data/curated/unmapped_ingredients.yaml": (
        "c5e70ba3192ae0ce71d4175755e51179ac00d83bef8ce3f8d6ec4af8f89ecfdb",
        701940,
    ),
    "mappings/microbedecoder_residual_research_decomposition.tsv": (
        "b6a9d5d729ece6eb038e4f8e0d6d5813b3a117284d45a1fc8918b15f24e4fb86",
        7873,
    ),
    "reports/semantic_review_20260921/resolution/components/before-records.json": (
        "9bf6749fb8fbeeb20ab19150eca3d9604bf4fe3c30ed5c66bca77537cf5cc521",
        119879,
    ),
}
CASES = {
    "tests/test_component_partonomy.py": (
        "199a2abab3835a0608c77901d038f34f61dc37384db544b677e506082b0f8dc6",
        {"test_real_curated_corpus_has_no_partonomy_violations"},
    ),
    "tests/test_component_partonomy_migration.py": (
        "afe419b0b43b6fb69e4253279077dd7dcac538269086377008bba295eebc37ca",
        {
            "test_migration_is_idempotent_on_its_historical_reviewed_inventory",
            "test_historical_migration_refuses_current_reviewed_inventory_without_changes",
        },
    ),
}
WRITER = "scripts/migrate_component_partonomy.py"
WRITER_SHA256 = "8b10d993ccf8c83c00f4694a5d9002c18e3a9b3aa94acd4f6a253d103f712dfc"


def require(condition, message):
    if not condition:
        raise ValueError("Historical partonomy context: " + message)


def digest(raw):
    return hashlib.sha256(raw).hexdigest()


def regular(path):
    path = Path(path).absolute()
    require(path == path.resolve() and path.is_file(), "aliased or missing input")
    require(path.stat().st_nlink == 1, "hardlinked input")
    return path.read_bytes()


def context_bytes(archive=ARCHIVE):
    raw = regular(archive)
    require(digest(raw) == ARCHIVE_SHA256, "archive hash differs")
    return decode_context(raw)


def decode_context(raw):
    """Bind each payload independently, even if container metadata is rewritten."""
    doc = json.loads(gzip.decompress(raw))
    require(
        set(doc) == {"schema_version", "source_revision", "files"}
        and type(doc["schema_version"]) is int
        and doc["schema_version"] == 1
        and doc["source_revision"] == REVISION
        and set(doc["files"]) == set(INPUTS),
        "archive identity or membership differs",
    )
    result = {}
    for name, (expected, size) in INPUTS.items():
        item = doc["files"][name]
        require(set(item) == {"sha256", "bytes", "base64"}, "input metadata differs")
        content = base64.b64decode(item["base64"], validate=True)
        require(
            item["sha256"] == digest(content) == expected
            and type(item["bytes"]) is int
            and item["bytes"] == len(content) == size,
            "input bytes differ: " + name,
        )
        result[name] = content
    return result


def requested_case(module_path, case, repository_root=ROOT):
    path = Path(module_path)
    for name, (_, cases) in CASES.items():
        if path == repository_root / name and case in cases:
            return name
    return None


@contextmanager
def bind_context(module, case, destination, *, repository_root=ROOT, archive=ARCHIVE):
    name = requested_case(module.__file__, case, repository_root)
    if name is None:
        yield False
        return
    require(digest(regular(repository_root / name)) == CASES[name][0], "original test changed")
    require(digest(regular(repository_root / WRITER)) == WRITER_SHA256, "current writer changed")
    require(module.ROOT == repository_root, "test already rebound")
    inputs = context_bytes(archive)
    evidence = "mappings/microbedecoder_residual_research_decomposition.tsv"
    require(regular(repository_root / evidence) == inputs[evidence], "writer evidence changed")
    destination = Path(destination).absolute()
    require(
        destination == destination.resolve()
        and destination.parent.is_dir()
        and not os.path.lexists(destination),
        "new unaliased destination required",
    )
    destination.mkdir()
    for relative, content in inputs.items():
        path = destination / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        with path.open("xb") as stream:
            stream.write(content)
    original = module.ROOT
    module.ROOT = destination
    try:
        yield True
    finally:
        module.ROOT = original
        require(
            {p.relative_to(destination).as_posix() for p in destination.rglob("*") if p.is_file()}
            == set(inputs),
            "fixture membership changed",
        )
        require(
            all(regular(destination / relative) == content for relative, content in inputs.items()),
            "fixture content changed",
        )
