#!/usr/bin/env python3
"""Freshness gate for UNIFIED_INGREDIENT_MAPPING.tsv (#359).

The unified snapshot is built by claw's `build_unified_ingredient_mapping.py`
from MIM's `data/ingredients/` tree plus CultureMech's normalized recipes, and
is committed here as a tracked cross-repo artifact. Nothing recorded what it was
built from, so it went three weeks and forty PRs stale without a single check
going red (#359), and by the time anyone looked the snapshot and the SSSOM
disagreed about what records *are* (#624).

The gate is deliberately MIM-only. A rebuild needs three checkouts and claw's
virtualenv, which CI does not have; but staleness is observable from here alone,
because a snapshot is stale exactly when MIM's own inputs have moved since it
was built. So `--stamp` records a digest of those inputs beside the artifact and
`--check` recomputes it.

    just stamp-unified-freshness    # after a rebuild
    just check-unified-freshness    # CI, and before publishing

The check is a drift *budget*, not absolute freshness. #359's complaint is that
the snapshot went three weeks and forty PRs stale -- unbounded drift, not any
drift. A snapshot one curation batch behind is normal; failing on that would
red-light every curation PR while the only remedy, a rebuild, needs three
checkouts and cannot run in CI (#654). So drift is counted in changed record
files since the stamped rev and compared against a threshold.

A hand-edited artifact is different and always fails: this file is generated,
and editing it in place is the thing to refuse outright.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

_REPO = Path(__file__).resolve().parent.parent
ARTIFACT = _REPO / "UNIFIED_INGREDIENT_MAPPING.tsv"
PROVENANCE = _REPO / "UNIFIED_INGREDIENT_MAPPING.provenance.json"
INPUTS = _REPO / "data" / "ingredients"


def _sha256(path: Path) -> str:
    """Return the hex sha256 of one file, read in chunks."""
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(65536), b""):
            digest.update(chunk)
    return digest.hexdigest()


def inputs_digest(inputs: Path = INPUTS) -> tuple[str, int]:
    """
    Return a digest over every record the builder reads, and the record count.

    Keyed on (relative path, file sha256) pairs sorted by path, so the digest
    moves when a record's content changes, when one is added or removed, and
    when one is renamed -- a rename is exactly how #236's stranded SSSOM
    subjects arise, so it must not be invisible here.

    :param inputs: The `data/ingredients` tree.
    :return: (digest, number of record files).
    """
    records = sorted(p for p in inputs.rglob("*.yaml") if p.is_file())
    accumulator = hashlib.sha256()
    for path in records:
        accumulator.update(str(path.relative_to(inputs)).encode("utf-8"))
        accumulator.update(b"\0")
        accumulator.update(_sha256(path).encode("ascii"))
        accumulator.update(b"\n")
    return accumulator.hexdigest(), len(records)


def _git_rev(root: Path) -> str:
    """
    Return a rev to stamp: the merge-base with origin/main, else HEAD.

    Stamping bare HEAD records a branch commit, and the rebuild-then-squash-merge
    workflow discards exactly that commit -- after which drift is unmeasurable and
    the gate goes quietly advisory, which is the silent-no-op class it exists to
    catch (#658). The merge-base is on the default branch and survives.

    :param root: The checkout to ask.
    :return: A short rev, or the empty string when git cannot answer.
    """
    def _rev(*args: str) -> str:
        try:
            result = subprocess.run(
                ["git", "-C", str(root), *args],
                capture_output=True, text=True, check=True, timeout=30,
            )
            return result.stdout.strip()
        except (subprocess.SubprocessError, OSError):
            return ""

    base = _rev("merge-base", "origin/main", "HEAD")
    if base:
        return _rev("rev-parse", "--short", base) or base[:8]
    return _rev("rev-parse", "--short", "HEAD")


def stamp(artifact: Path, provenance: Path, inputs: Path) -> dict:
    """
    Write the provenance sidecar describing the artifact as it stands now.

    :param artifact: The built TSV.
    :param provenance: Where to write the sidecar.
    :param inputs: The `data/ingredients` tree the builder read.
    :return: The recorded provenance.
    """
    digest, count = inputs_digest(inputs)
    rows = sum(1 for _ in artifact.open(encoding="utf-8")) - 1
    record = {
        "artifact": artifact.name,
        "artifact_sha256": _sha256(artifact),
        "artifact_rows": rows,
        "mim_inputs_digest": digest,
        "mim_record_count": count,
        "mim_rev": _git_rev(_REPO),
        "stamped_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
    }
    provenance.write_text(json.dumps(record, indent=2) + "\n", encoding="utf-8")
    return record


def drift_since(rev: str, inputs: Path, repo: Path = _REPO) -> int | None:
    """
    Return how many record files changed since `rev`, or None if unmeasurable.

    Compares the stamped revision against the working tree, so uncommitted
    curation counts too. None means the question could not be asked -- no git,
    a shallow clone, or a rev this checkout does not have -- which is reported
    as advisory rather than failed: a gate must not fail on a condition it
    cannot measure (#654).

    :param rev: The revision recorded when the snapshot was stamped.
    :param inputs: The `data/ingredients` tree.
    :param repo: The checkout to ask.
    :return: Number of changed record files, or None.
    """
    if not rev:
        return None
    try:
        relative = inputs.resolve().relative_to(repo.resolve())
    except ValueError:
        return None
    def _git(*args: str) -> list[str] | None:
        try:
            result = subprocess.run(
                ["git", "-C", str(repo), *args],
                capture_output=True, text=True, check=True, timeout=60,
            )
        except (subprocess.SubprocessError, OSError):
            return None
        return [line for line in result.stdout.splitlines() if line.strip()]

    changed = _git("diff", "--name-only", rev, "--", str(relative))
    if changed is None:
        return None
    # `git diff` cannot see a file git does not know about, and adding a record
    # is the commonest curation action -- thirty new records read as zero drift
    # without this (#657).
    untracked = _git("ls-files", "--others", "--exclude-standard", "--", str(relative))
    return len(set(changed) | set(untracked or []))


def check(
    artifact: Path,
    provenance: Path,
    inputs: Path,
    max_drift: int = 25,
    repo: Path = _REPO,
) -> list[str]:
    """
    Return one line per reason the artifact must be rebuilt; empty when within budget.

    :param artifact: The built TSV.
    :param provenance: The sidecar written at build time.
    :param inputs: The `data/ingredients` tree.
    :param max_drift: Changed record files tolerated before this fails.
    :param repo: The checkout used to measure drift.
    :return: Human-readable failure reasons.
    """
    if not artifact.exists():
        return [f"{artifact.name} is missing"]
    if not provenance.exists():
        return [
            f"{provenance.name} is missing — the snapshot has no record of what it "
            f"was built from, which is the state #359 describes. Rebuild, then run "
            f"`just stamp-unified-freshness`."
        ]
    recorded = json.loads(provenance.read_text(encoding="utf-8"))
    problems: list[str] = []

    actual_sha = _sha256(artifact)
    if actual_sha != recorded.get("artifact_sha256"):
        problems.append(
            f"{artifact.name} has changed since it was stamped "
            f"({recorded.get('artifact_sha256', '')[:12]} -> {actual_sha[:12]}). "
            f"This file is generated; edit the records and rebuild instead."
        )

    digest, count = inputs_digest(inputs)
    if digest == recorded.get("mim_inputs_digest"):
        return problems

    drift = drift_since(str(recorded.get("mim_rev") or ""), inputs, repo)
    if drift is None:
        print(
            f"NOTE: data/ingredients has moved since the snapshot was stamped, and "
            f"drift could not be measured from git (stamped rev "
            f"{recorded.get('mim_rev') or '?'}). Reporting, not failing (#654)."
        )
        return problems
    if drift > max_drift:
        problems.append(
            f"{drift} record files have changed since the snapshot was built "
            f"(budget {max_drift}; stamped at {recorded.get('mim_rev')}). This is the "
            f"unbounded drift #359 describes, not one curation batch."
        )
    else:
        print(
            f"NOTE: {drift} record file(s) changed since the snapshot was stamped "
            f"(budget {max_drift}). Within budget; rebuild when convenient."
        )
    return problems


def main(argv: list[str]) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("--stamp", action="store_true", help="Record current provenance")
    mode.add_argument("--check", action="store_true", help="Verify freshness (default)")
    parser.add_argument("--artifact", type=Path, default=ARTIFACT)
    parser.add_argument("--provenance", type=Path, default=PROVENANCE)
    parser.add_argument("--inputs", type=Path, default=INPUTS)
    parser.add_argument(
        "--max-drift", type=int, default=25,
        help="Changed record files tolerated before this fails (default: 25)",
    )
    args = parser.parse_args(argv)

    if args.stamp:
        record = stamp(args.artifact, args.provenance, args.inputs)
        print(f"Stamped {args.provenance.name}:")
        for key in ("artifact_rows", "mim_record_count", "mim_rev"):
            print(f"  {key}: {record[key]}")
        print(f"  artifact_sha256: {record['artifact_sha256'][:12]}")
        print(f"  mim_inputs_digest: {record['mim_inputs_digest'][:12]}")
        return 0

    problems = check(args.artifact, args.provenance, args.inputs, args.max_drift)
    if problems:
        print(f"STALE: {args.artifact.name} must be rebuilt.")
        for line in problems:
            print(f"  - {line}")
        print(
            "\nRebuild (needs CultureMech, MIM and claw checked out, and claw's venv):\n"
            "  just rebuild-unified\n"
            "then `just stamp-unified-freshness` and commit both files."
        )
        return 1
    print(f"OK: {args.artifact.name} is within its drift budget.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
