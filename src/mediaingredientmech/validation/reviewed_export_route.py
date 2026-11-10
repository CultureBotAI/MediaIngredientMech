"""Route current reviews separately from the immutable #1265 proof (#1325).

This read-only gate does not prepare roots, rewrite reviews or grant science.
The original projected route remains the default. Ordinary current reviews
require a separately pinned, genuine historical checkout and native replay.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import stat
import subprocess
import sys
from pathlib import Path
from typing import Any

from mediaingredientmech import identity_projection as projection
from mediaingredientmech.export import reviewed_sssom
from mediaingredientmech.ingredient_bundle_contract import (
    content_sha256,
    read_json,
    reviewed_products,
    safe_member,
)

DEFAULT_REVIEW = Path(projection.MAPPING_REVIEW)
DEFAULT_COMPANION = Path(projection.REPORT_ROOT) / "companion-review.json"


def _require(condition: bool, reason: str) -> None:
    if not condition:
        raise ValueError("Reviewed export route: " + reason)


def _merge_snapshots(snapshots: dict[Path, str], additions: dict[Path, str]) -> None:
    """Keep every validator's original byte binding across shared inputs (#1326)."""
    for path, expected in additions.items():
        _require(
            path not in snapshots or snapshots[path] == expected,
            "conflicting validated input snapshots: " + str(path),
        )
    snapshots.update(additions)


def _root(path: Path) -> Path:
    _require(".." not in path.parts, "root traversal refused")
    path = path.absolute()
    _require(not any(p.is_symlink() for p in (path, *path.parents)), "aliased root")
    _require(path.is_dir(), "missing root")
    return path


def _git(root: Path, *args: str) -> bytes:
    result = subprocess.run(
        ["git", "--no-optional-locks", *args],
        cwd=root,
        env={**os.environ, "GIT_NO_LAZY_FETCH": "1", "GIT_TERMINAL_PROMPT": "0"},
        capture_output=True,
        timeout=120,
        check=False,
    )
    _require(result.returncode == 0, "Git provenance check failed: " + result.stderr.decode())
    return result.stdout


def _historical_checkout(root: Path, revision: str) -> dict[str, Any]:
    """Verify actual committed bytes, not Git's cached stat-based clean signal.

    The caller supplies an independently reviewed full revision. This does not
    create a repository or claim an arbitrary tree is the historical migration;
    the existing native projection checker establishes that separate fact.
    """
    _require(bool(re.fullmatch(r"[0-9a-f]{40}", revision)), "full historical SHA required")
    _require(
        Path(_git(root, "rev-parse", "--show-toplevel").decode().strip()) == root,
        "historical root must be an exact Git worktree",
    )
    _require(
        _git(root, "rev-parse", "HEAD").decode().strip() == revision, "historical HEAD differs"
    )
    _require(
        _git(root, "rev-parse", "--show-object-format").strip() == b"sha1",
        "unsupported Git object format",
    )
    _require(
        not _git(root, "diff", "--cached", "--name-only", "-z", revision),
        "historical index differs",
    )
    tree = _git(root, "ls-tree", "-rz", "--full-tree", revision)
    count = 0
    for entry in tree.split(b"\0"):
        if not entry:
            continue
        header, name = entry.split(b"\t", 1)
        mode, kind, expected = header.split()
        _require(
            kind == b"blob" and mode in {b"100644", b"100755", b"120000"},
            "unsupported historical Git entry",
        )
        relative = Path(os.fsdecode(name))
        _require(
            not relative.is_absolute() and ".." not in relative.parts, "unsafe historical Git path"
        )
        path = root / relative
        _require(
            not any(p.is_symlink() for p in path.parents if p != root.parent),
            "aliased historical ancestor",
        )
        info = path.lstat()
        if mode == b"120000":
            _require(stat.S_ISLNK(info.st_mode), "historical symlink type changed")
            raw = os.fsencode(os.readlink(path))
        else:
            _require(stat.S_ISREG(info.st_mode), "historical input is not regular")
            _require(
                bool(info.st_mode & 0o111) == (mode == b"100755"),
                "historical executable mode changed",
            )
            raw = path.read_bytes()
        actual = hashlib.sha1(
            b"blob " + str(len(raw)).encode() + b"\0" + raw, usedforsecurity=False
        ).hexdigest()
        _require(actual.encode() == expected, "historical committed bytes differ: " + str(relative))
        count += 1
    return {
        "revision": revision,
        "tree": _git(root, "rev-parse", revision + "^{tree}").decode().strip(),
        "tracked_files": count,
    }


def _projection_check(root: Path) -> dict:
    """Invoke the unchanged native checker, including every original assertion."""
    result = subprocess.run(
        [
            sys.executable,
            "-m",
            "mediaingredientmech.identity_projection",
            "--root",
            str(root),
            "--check",
        ],
        capture_output=True,
        text=True,
        timeout=300,
        check=False,
    )
    _require(result.returncode == 0, "native historical projection failed: " + result.stderr)
    answer: object = json.loads(result.stdout)
    if not isinstance(answer, dict):
        raise ValueError("Reviewed export route: invalid native projection response")
    _require(
        answer.get("checked") is True and answer.get("scientific_approval_added") is False,
        "unexpected native projection result",
    )
    return answer


def _has_projection(value: Any) -> bool:
    if isinstance(value, dict):
        return "identity_projection" in value or any(_has_projection(v) for v in value.values())
    if isinstance(value, list):
        return any(_has_projection(v) for v in value)
    return (
        value in {projection.PROJECTION_KIND, "identity-projection-v1"}
        if isinstance(value, str)
        else False
    )


def _ordinary_evidence(review: dict, sources: dict[str, bytes]) -> None:
    """Do not turn a stripped projected wrapper into ordinary science evidence.

    Historical context may remain a declared input. The selected decision proof
    itself must be ordinary; explicit inherited projection always needs replay.
    """
    _require(not _has_projection(review), "projected review cannot use the ordinary route")
    for decision in review.get("decisions", []):
        name = decision["review_evidence"]
        document = read_json(sources[name])
        entry = document.get("entries", {}).get(decision["evidence_key"])
        _require(
            "identity_projection" not in document and not _has_projection(entry),
            "inherited decision proof cannot be stripped into ordinary evidence",
        )


def check_route(
    root: Path,
    review_path: Path = DEFAULT_REVIEW,
    *,
    companion_review: Path | None = None,
    route: str = "projected",
    historical_root: Path | None = None,
    historical_revision: str | None = None,
) -> dict:
    """Check the selected route without emitting or modifying any data product."""
    root = _root(root)
    _require(route in {"projected", "ordinary"}, "unknown route")
    review_path = safe_member(root, review_path.as_posix())
    review_bytes = review_path.read_bytes()
    review = read_json(review_bytes)
    _require(
        review.get("source_sssom") == projection.SOURCE,
        "review must cover the current canonical table",
    )
    snapshots = {review_path: content_sha256(review_bytes)}
    history = None
    if route == "projected":
        _require(
            historical_root is None and historical_revision is None,
            "projected route does not redirect its proof",
        )
        _require("identity_projection" in review, "projected review proof is missing")
        native = _projection_check(root)
    else:
        _require(not _has_projection(review), "projected review cannot use the ordinary route")
        _require(
            historical_root is not None and historical_revision is not None,
            "ordinary route requires pinned historical root/revision",
        )
        _require(
            companion_review is not None, "ordinary route requires its paired companion review"
        )
        assert historical_root is not None and historical_revision is not None
        historical_root = _root(historical_root)
        _require(
            not root.is_relative_to(historical_root) and not historical_root.is_relative_to(root),
            "historical and current roots must be disjoint",
        )
        _require(
            review_path.relative_to(root) != DEFAULT_REVIEW,
            "immutable projected review cannot become ordinary",
        )
        history = _historical_checkout(historical_root, historical_revision)
        native = _projection_check(historical_root)
    loaded = reviewed_sssom.load_review(root, review_path)
    _merge_snapshots(snapshots, loaded["input_snapshot"])
    if route == "ordinary":
        _ordinary_evidence(
            review, {name: safe_member(root, name).read_bytes() for name in review["inputs"]}
        )
    companion_counts = None
    if companion_review is not None:
        companion_path = safe_member(root, companion_review.as_posix())
        raw = companion_path.read_bytes()
        companion = read_json(raw)
        _require(
            ("identity_projection" in companion) == (route == "projected"),
            "companion projection route differs",
        )
        _require(
            companion.get("base_review") == str(review_path.relative_to(root))
            and companion.get("base_review_sha256") == content_sha256(review_bytes),
            "companion does not bind selected current review",
        )
        names = {
            companion["claims_file"],
            companion["base_review"],
            *companion["inputs"],
            *companion["record_inputs"],
        }
        sources = {name: safe_member(root, name).read_bytes() for name in names}
        if route == "ordinary":
            _ordinary_evidence(companion, sources)
        _, claims = reviewed_products(companion, sources)
        _merge_snapshots(snapshots, {companion_path: content_sha256(raw)})
        _merge_snapshots(
            snapshots,
            {safe_member(root, name): content_sha256(value) for name, value in sources.items()},
        )
        companion_counts = {
            kind: len(claims[kind])
            for kind in ("mappings", "identifiers", "products", "occurrences")
        }
    for path, expected in snapshots.items():
        _require(
            content_sha256(path.read_bytes()) == expected,
            "current review input changed during routing: " + str(path),
        )
    if history is not None:
        assert historical_root is not None and historical_revision is not None
        _require(
            _historical_checkout(historical_root, historical_revision) == history,
            "historical checkout changed",
        )
    return {
        "route": route,
        "review_sha256": content_sha256(review_bytes),
        "source_rows": len(loaded["rows"]),
        "companion_counts": companion_counts,
        "historical_checkout": history,
        "native_projection": native,
        "scientific_approval_added": False,
        "production_authorized": False,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path.cwd())
    parser.add_argument("--review", type=Path, default=DEFAULT_REVIEW)
    parser.add_argument("--companion-review", type=Path)
    parser.add_argument("--route", choices=("projected", "ordinary"), default="projected")
    parser.add_argument("--historical-root", type=Path)
    parser.add_argument("--historical-revision")
    args = parser.parse_args()
    print(
        json.dumps(
            check_route(
                args.root,
                args.review,
                companion_review=args.companion_review,
                route=args.route,
                historical_root=args.historical_root,
                historical_revision=args.historical_revision,
            ),
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
