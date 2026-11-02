"""Reconstruct two immutable source-operation test prestates (#1113).

These tests and their writers are original execution evidence. Their temporary
cases must use the protected anchors from that operation, independently of later
publication changes. This adapter does not change a writer, assertion, or skip.
"""

from __future__ import annotations

import base64
import gzip
import hashlib
import json
import stat
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ARCHIVE = Path(__file__).parent / "fixtures/step7c_source_anchors_1113/anchors.json.gz"
ARCHIVE_SHA256 = "79f7dd8f70964428d593de36102c9339fd0b53718aa5066943b532008372a96b"
BASE = "54eadef802d2ff159bf4ba9bec51492fe3bb99d4"
ANCHORS = {
    "mappings/ingredient_mappings.sssom.tsv": "55823757c6b15f43de69370da7fe6c4468ff21f14e5f4994cf53115e04ae0d74",
    "mappings/ingredient_mappings.sssom.tsv.manifest.json": "1a30715b1e5e5e89bf2063a1e9eecd8c18fea13781ab9dff3214e75a553cca58",
    "mappings/other_cross_record_baseline.tsv": "f52921f8cf4aaf16f070b9b33bb8809e0a7ee809f7a66805bdf7bd01c9610bcb",
    "mappings/suppressed_aliases.tsv": "3d1e6c1f6393aaf05b8f7235c5393372206ea0f73db0699ddbdca14053bf8f84",
    "UNIFIED_INGREDIENT_MAPPING.tsv": "1edaba0f0f2d1afb84129a2ba185963a2cdf3e9b982690fdfd610df1fd78cc88",
    "UNIFIED_INGREDIENT_MAPPING.provenance.json": "172018698861b2161238ca72ad116269e213b72a111a5dbe4a265eb643399bc9",
}
MODULES = {
    "tests/test_curate_step7c_source_labels.py": {
        "sha256": "07dc71958650182138a4847bcad59163f6b426e97e080f2b69c8e47ccefe17e1",
        "anchors": tuple(name for name in ANCHORS if name.startswith("mappings/")),
        "case_length": 4,
    },
    "tests/test_correct_diketo_bacdive_evidence.py": {
        "sha256": "9ca603ae82b0b65d0be6b3afed009eda043f9bf690394973787123356aad12bc",
        "anchors": tuple(ANCHORS),
        "case_length": 2,
    },
}


def require(condition, message):
    if not condition:
        raise ValueError(message)


def digest(data):
    return hashlib.sha256(data).hexdigest()


def frozen_anchors(archive=ARCHIVE):
    raw = archive.read_bytes()
    require(digest(raw) == ARCHIVE_SHA256, "Historical anchor archive hash changed")
    doc = json.loads(gzip.decompress(raw))
    require(
        set(doc) == {"schema_version", "source_revision", "anchors"}
        and doc["schema_version"] == 1
        and doc["source_revision"] == BASE
        and set(doc["anchors"]) == set(ANCHORS),
        "Historical anchor archive contract changed",
    )
    result = {
        name: base64.b64decode(value, validate=True) for name, value in doc["anchors"].items()
    }
    require(
        all(digest(result[name]) == sha for name, sha in ANCHORS.items()),
        "Historical anchor content hash changed",
    )
    return result


def restore_requested_case(request, *, repository_root=ROOT, archive=ARCHIVE):
    """Restore only hash-bound modules' requested cases in their own tmp_path."""
    if "case" not in request.fixturenames:
        return False
    module_path = Path(request.path)
    matching = [
        info for name, info in MODULES.items() if module_path == repository_root / name
    ]
    if not matching:
        return False
    require(module_path == module_path.resolve(), "Historical test module is aliased")
    info = matching[0]
    require(digest(module_path.read_bytes()) == info["sha256"], "Historical test changed")
    frozen = frozen_anchors(archive)
    case = request.getfixturevalue("case")
    require(
        isinstance(case, tuple) and len(case) == info["case_length"],
        "Historical case shape changed",
    )
    root = case[0]
    tmp_path = request.getfixturevalue("tmp_path").resolve()
    require(
        isinstance(root, Path)
        and root == root.resolve() == tmp_path
        and root != repository_root.resolve()
        and root.is_dir(),
        "Historical case must belong to its exact pytest tmp_path",
    )
    before = case[3] if len(case) == 4 else None
    if before is not None:
        require(
            isinstance(before, dict) and all(Path(name) in before for name in info["anchors"]),
            "Historical case before dictionary changed",
        )
    # Validate every target before any replacement; symlinks and hard links could
    # otherwise let a temporary test fixture overwrite a repository or foreign file.
    for name in info["anchors"]:
        target = root / name
        require(target == target.resolve(), "Historical anchor path is aliased")
        metadata = target.lstat()
        require(
            stat.S_ISREG(metadata.st_mode) and metadata.st_nlink == 1,
            "Historical anchor must be an unaliased regular fixture file",
        )
    for name in info["anchors"]:
        (root / name).write_bytes(frozen[name])
        if before is not None:
            before[Path(name)] = frozen[name]
    return True
