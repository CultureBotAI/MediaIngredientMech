"""#1265 frozen postimages for a narrow read-only unified freshness exemption.

An unchanged administrative migration may be ignored only when the unified
artifact's complete stamped source digest matches a proven preimage or postimage
snapshot and current source bytes equal the proven migration postimage. Old scientific drift,
subsequent edits, added/deleted records and unknown proofs remain non-exempt.
"""

from __future__ import annotations

import base64
import gzip
import hashlib
import io
from pathlib import Path

from mediaingredientmech.identity_projection import (
    BASE_COMMIT,
    MANIFEST,
    REPORT_ROOT,
    SOURCE,
    Proof,
    document,
    encode,
    git_files,
    record_paths,
    require,
    safe_path,
    sha,
    verify_transition,
)

FROZEN = REPORT_ROOT + "/migration-postimages.json.gz"
MAX_POSTIMAGE_BYTES = 64 * 1024 * 1024


def frozen_products(proof: Proof) -> dict[str, bytes]:
    document = {
        "schema_version": 1,
        "kind": "mim-identity-frozen-postimages/v1",
        "source_commit": BASE_COMMIT,
        "manifest_sha256": sha(proof.snapshots[MANIFEST]),
        "files": {
            name: base64.b64encode(raw).decode("ascii") for name, raw in sorted(proof.after.items())
        },
    }
    content = encode(document)
    require(len(content) <= MAX_POSTIMAGE_BYTES, "frozen postimage document exceeds bound")
    return {FROZEN: gzip.compress(content, mtime=0)}


def decode_frozen(
    manifest_raw: bytes, before: dict[str, bytes], compressed: bytes
) -> tuple[dict[str, bytes], dict]:
    with gzip.GzipFile(fileobj=io.BytesIO(compressed)) as stream:
        raw = stream.read(MAX_POSTIMAGE_BYTES + 1)
    require(len(raw) <= MAX_POSTIMAGE_BYTES, "frozen postimage document exceeds bound")
    archive = document(raw)
    require(
        set(archive) == {"schema_version", "kind", "source_commit", "manifest_sha256", "files"}
        and type(archive["schema_version"]) is int
        and archive["schema_version"] == 1
        and archive["kind"] == "mim-identity-frozen-postimages/v1"
        and archive["source_commit"] == BASE_COMMIT
        and archive["manifest_sha256"] == sha(manifest_raw),
        "frozen postimage authority differs",
    )
    require(isinstance(archive["files"], dict), "invalid frozen postimage inventory")
    after = {
        name: base64.b64decode(value, validate=True) for name, value in archive["files"].items()
    }
    transition = verify_transition(document(manifest_raw), before, after)
    return after, transition


def identity_only_matches(
    before: dict[str, bytes],
    after: dict[str, bytes],
    current: dict[str, bytes],
    stamped: dict[str, bytes],
) -> set[str]:
    """Both sides must match byte-for-byte; a preexisting or later edit counts."""
    return {
        name
        for name in current
        if name.startswith("data/ingredients/")
        and name in before
        and name in after
        and name in stamped
        and stamped[name] in (before[name], after[name])
        and current[name] == after[name]
    }


def input_snapshot_digest(files: dict[str, bytes]) -> tuple[str, int]:
    """Use the native freshness stamper's complete relative-path/byte digest."""
    records = {
        name.removeprefix("data/ingredients/"): raw
        for name, raw in files.items()
        if name.startswith("data/ingredients/") and name.endswith(".yaml")
    }
    accumulator = hashlib.sha256()
    for name, raw in sorted(records.items()):
        accumulator.update(name.encode("utf-8"))
        accumulator.update(b"\0")
        accumulator.update(sha(raw).encode("ascii"))
        accumulator.update(b"\n")
    return accumulator.hexdigest(), len(records)


def stamped_snapshot(
    before: dict[str, bytes], after: dict[str, bytes], digest: str, count: int
) -> dict[str, bytes] | None:
    """A Git merge base is not the stamped working tree (#1270)."""
    if type(count) is not int:
        return None
    for snapshot in (before, after):
        if input_snapshot_digest(snapshot) == (digest, count):
            return snapshot
    return None


def eligible_identity_paths(
    root: Path, candidates: list[str], *, stamped_digest: str, stamped_count: int
) -> set[str]:
    """Return only independently proved administrative-only drift paths.

    Missing projection artifacts mean no applicable exemption, not a new baseline.
    Present malformed/stale evidence raises so callers cannot treat it as healthy.
    This reads current bytes but never touches, rewrites, pushes or deletes them.
    """
    root = root.resolve()
    manifest_path, archive_path = safe_path(root, MANIFEST), safe_path(root, FROZEN)
    if not manifest_path.exists() and not archive_path.exists():
        return set()
    manifest_raw, archive_raw = manifest_path.read_bytes(), archive_path.read_bytes()
    names = record_paths(root, historical=True)
    before = git_files(root, [*names, SOURCE])
    after, transition = decode_frozen(manifest_raw, before, archive_raw)
    require(set(transition["new_records"]) == set(names), "frozen migration corpus differs")
    selected = sorted(set(candidates) & set(names))
    stamped = stamped_snapshot(before, after, stamped_digest, stamped_count)
    if stamped is None:
        return set()
    current = {
        name: safe_path(root, name).read_bytes()
        for name in selected
        if safe_path(root, name).is_file()
    }
    result = identity_only_matches(before, after, current, stamped)
    require(
        manifest_path.read_bytes() == manifest_raw and archive_path.read_bytes() == archive_raw,
        "frozen proof changed during freshness scan",
    )
    require(
        all(safe_path(root, name).read_bytes() == raw for name, raw in current.items()),
        "current record changed during freshness scan",
    )
    return result
