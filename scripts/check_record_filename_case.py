#!/usr/bin/env python3
"""Catch per-record filenames that drift in case only (#352).

A record file whose name changes *only in case* is invisible on macOS and breaks
CI on Linux. It has cost three failed CI runs and one apparent lost record.

## Mechanism

`export_individual_records.py` clears `data/ingredients/` and re-writes it, and
filenames are **sticky by what is on disk** (`collect_existing_filenames`), so a
record keeps the name it already has. When a record's `identifier` changes, that
lookup misses, the name is re-derived by `sanitize_filename(preferred_term)`, and
the historical corpus was written by more than one naming rule — so the derived
name can differ from the committed one *in case alone*.

On a case-insensitive filesystem (macOS, the default) that divergence is
undetectable:

* the exporter deletes `Thiamine_Pyrophosphate.yaml` and writes
  `Thiamine_pyrophosphate.yaml`;
* `git status` reports **no change**, because git matches the path
  case-insensitively on such a volume;
* every local gate passes, because the exporter and every checker read the same
  single file.

On Linux CI, git checks out the committed capital-P name and the exporter then
creates the lowercase-p one. Now there are **two** files for one record:
`browser_export.py` reads 2842 records against a `docs/data/` carrying 2841, and
`check_flat_export_coverage` reports `ingredients.json` stale — pointing at the
artifact rather than at the filename that actually moved.

## What is checked

**Drift** — a path git tracks whose on-disk spelling differs only in case. This
is the one that fires on macOS, where it is otherwise undetectable.

**Collision** — two tracked paths that differ only in case. On Linux both exist
and one record silently shadows the other; on macOS only one can be checked out.

Both are computed from `git ls-files -z` (never plain `ls-files`, which
backslash-quotes non-ASCII paths and produces five spurious hits in this corpus)
compared against `os.listdir`, with NFC normalisation so macOS's NFD spelling of
`α`/`ß` is not mistaken for drift.

Deliberately does NOT re-run the exporter into a temp directory to compare
names. Filenames are sticky by existing directory contents, so exporting into an
empty directory re-derives ~1150 of them differently — a comparison that looks
alarming and means nothing.

    python scripts/check_record_filename_case.py            # report
    python scripts/check_record_filename_case.py --fix      # print git mv commands
"""
from __future__ import annotations

import argparse
import os
import subprocess
import sys
import unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
RECORDS = "data/ingredients"
SUBDIRS = ("mapped", "unmapped")


def _nfc(text: str) -> str:
    return unicodedata.normalize("NFC", text)


def tracked_paths(root: Path = ROOT, prefix: str = RECORDS) -> set[str]:
    """Paths git tracks, case-exact. `-z` avoids ls-files' backslash quoting."""
    out = subprocess.run(["git", "ls-files", "-z", prefix],
                         capture_output=True, cwd=root, check=True).stdout
    return {_nfc(p) for p in out.decode("utf-8").split("\0") if p.endswith(".yaml")}


def disk_paths(root: Path = ROOT, prefix: str = RECORDS) -> set[str]:
    """Paths actually on disk — what the exporter reads when deciding names."""
    found: set[str] = set()
    for sub in SUBDIRS:
        d = root / prefix / sub
        if d.is_dir():
            found |= {_nfc(f"{prefix}/{sub}/{name}")
                      for name in os.listdir(d) if name.endswith(".yaml")}
    return found


def find_drift(tracked: set[str], disk: set[str]) -> list[tuple[str, str]]:
    """(tracked, on-disk) pairs that differ only in case."""
    by_lower = {p.lower(): p for p in disk}
    drift = []
    for path in sorted(tracked - disk):
        actual = by_lower.get(path.lower())
        if actual is not None:
            drift.append((path, actual))
    return drift


def find_collisions(tracked: set[str]) -> list[list[str]]:
    """Groups of tracked paths that differ only in case."""
    groups: dict[str, list[str]] = {}
    for path in tracked:
        groups.setdefault(path.lower(), []).append(path)
    return [sorted(g) for g in groups.values() if len(g) > 1]


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--fix", action="store_true",
                    help="print the git mv commands that repair the drift")
    args = ap.parse_args(argv)

    tracked, disk = tracked_paths(), disk_paths()
    drift = find_drift(tracked, disk)
    collisions = find_collisions(tracked)

    missing = sorted(p for p in tracked - disk
                     if p.lower() not in {d.lower() for d in disk})
    untracked = sorted(p for p in disk - tracked
                       if p.lower() not in {t.lower() for t in tracked})

    print(f"tracked: {len(tracked)}   on disk: {len(disk)}")
    print(f"  case drift (tracked vs on-disk spelling): {len(drift)}")
    print(f"  case collisions within the tracked set  : {len(collisions)}")
    print(f"  genuinely absent from disk              : {len(missing)}")
    print(f"  on disk but untracked                   : {len(untracked)}")

    if drift:
        print("\nCASE DRIFT — invisible to `git status` on macOS, two files on Linux:")
        for was, now in drift:
            print(f"  git tracks : {was}")
            print(f"  on disk    : {now}")
    if collisions:
        print("\nCASE COLLISION — one record shadows the other on Linux:")
        for group in collisions:
            for p in group:
                print(f"  {p}")
    for label, items in (("genuinely absent from disk", missing),
                         ("on disk but untracked", untracked)):
        if items:
            print(f"\n{label.upper()}:")
            for p in items[:20]:
                print(f"  {p}")

    if args.fix and drift:
        print("\n# git cannot swap case directly on a case-insensitive volume,\n"
              "# so each rename goes via an intermediate path:")
        for i, (was, now) in enumerate(drift):
            tmp = f"{Path(was).parent}/__case_fix_{i}.yaml"
            print(f"git mv -f {was!r} {tmp!r} && git mv -f {tmp!r} {now!r}")

    if drift or collisions or missing or untracked:
        print("\nFAIL: per-record filenames do not match what git tracks. "
              "Re-run with --fix for the repair commands.")
        return 1
    print("\nOK: every tracked per-record filename matches its on-disk spelling.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
