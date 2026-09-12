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

`--check` also verifies the artifact's own sha256, so a hand-edit of the TSV is
caught as well: the whole point is that this file is generated, not curated.
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
    """Return a short git rev for a checkout, or the empty string."""
    try:
        result = subprocess.run(
            ["git", "-C", str(root), "rev-parse", "--short", "HEAD"],
            capture_output=True, text=True, check=True, timeout=30,
        )
        return result.stdout.strip()
    except (subprocess.SubprocessError, OSError):
        return ""


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


def check(artifact: Path, provenance: Path, inputs: Path) -> list[str]:
    """
    Return one line per reason the artifact is not current; empty when fresh.

    :param artifact: The built TSV.
    :param provenance: The sidecar written at build time.
    :param inputs: The `data/ingredients` tree.
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
    if digest != recorded.get("mim_inputs_digest"):
        problems.append(
            f"data/ingredients has changed since the snapshot was built "
            f"({recorded.get('mim_record_count', '?')} records stamped, {count} now; "
            f"digest {recorded.get('mim_inputs_digest', '')[:12]} -> {digest[:12]}). "
            f"The snapshot no longer reflects MIM's records."
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
    args = parser.parse_args(argv)

    if args.stamp:
        record = stamp(args.artifact, args.provenance, args.inputs)
        print(f"Stamped {args.provenance.name}:")
        for key in ("artifact_rows", "mim_record_count", "mim_rev"):
            print(f"  {key}: {record[key]}")
        print(f"  artifact_sha256: {record['artifact_sha256'][:12]}")
        print(f"  mim_inputs_digest: {record['mim_inputs_digest'][:12]}")
        return 0

    problems = check(args.artifact, args.provenance, args.inputs)
    if problems:
        print(f"STALE: {args.artifact.name} is not current with MIM's records.")
        for line in problems:
            print(f"  - {line}")
        print(
            "\nRebuild (needs CultureMech, MIM and claw checked out, and claw's venv):\n"
            "  just rebuild-unified\n"
            "then `just stamp-unified-freshness` and commit both files."
        )
        return 1
    print(f"OK: {args.artifact.name} is current with data/ingredients.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
