#!/usr/bin/env python3
"""Assert every curation-target pathspec still matches at least one tracked file.

The curation-history advisory counts how many curation targets a PR changed. It
**counts**; it never asserts. So a pathspec that matches nothing yields `0`, and
the job reports "No curation records changed" — indistinguishable from a PR that
genuinely changed none. The check reads as healthy precisely when it has stopped
working.

Not hypothetical: `data/custom/*.yaml` matched zero tracked files for its entire
life, because that directory holds a single `.tsv` (fixed in #180). Issue #181.

This is the assertion the counting never made. It reads the same
`conf/curation_targets.txt` the workflow does, so the two cannot drift.

WHAT THIS DOES NOT CATCH, stated plainly rather than implied by a green tick: a
PARTIAL miss. If `data/curated/` ever gains a subdirectory, `data/curated/*.yaml`
still matches the seven flat files, so a >=1 assertion stays green while silently
skipping the nested ones. Catching that needs per-directory reasoning, not a
count. The obvious "make it consistent" fix is also wrong here — switching to the
directory form would pull in 24 generated `.md` summaries and fire the advisory
on every regeneration.

Exit codes: 0 = every pathspec matches, 1 = at least one matches nothing,
2 = usage/configuration error.
"""

from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
DEFAULT_SPECS = REPO_ROOT / "conf" / "curation_targets.txt"


def load_specs(path: Path) -> list[str]:
    """Pathspecs from the shared list, ignoring blank lines and comments."""
    if not path.is_file():
        raise SystemExit(f"Curation-target list not found: {path}")
    specs = [
        line.strip()
        for line in path.read_text(encoding="utf-8").splitlines()
        if line.strip() and not line.lstrip().startswith("#")
    ]
    if not specs:
        raise SystemExit(f"{path} lists no pathspecs.")
    return specs


def match_count(spec: str, root: Path) -> int:
    """How many tracked files a pathspec matches.

    `git ls-files`, not a filesystem glob: the advisory it guards uses git
    pathspec semantics, so anything else would verify a different question than
    the one being asked.
    """
    proc = subprocess.run(
        ["git", "ls-files", "--", spec],
        cwd=root,
        capture_output=True,
        text=True,
        check=False,
    )
    if proc.returncode != 0:
        raise SystemExit(
            f"`git ls-files -- {spec}` failed (exit {proc.returncode}).\n"
            f"{proc.stderr.strip()}"
        )
    return len(proc.stdout.split())


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--specs", type=Path, default=DEFAULT_SPECS)
    parser.add_argument(
        "--print-specs",
        action="store_true",
        help="Print the pathspecs, space-separated and shell-quoted, for the workflow to consume.",
    )
    args = parser.parse_args(argv)

    specs = load_specs(args.specs)

    if args.print_specs:
        print(" ".join(f"'{spec}'" for spec in specs))
        return 0

    empty: list[str] = []
    print(f"Checking {len(specs)} curation-target pathspec(s) from {args.specs.name}:")
    for spec in specs:
        count = match_count(spec, REPO_ROOT)
        marker = "OK " if count else "!! "
        print(f"  {marker}{spec:<32} {count} tracked file(s)")
        if not count:
            empty.append(spec)

    if not empty:
        print("\nEvery pathspec matches at least one tracked file.")
        return 0

    # Display relative to the repo when possible, but never crash on a --specs
    # path outside it: the failure path must not fail.
    try:
        shown = args.specs.resolve().relative_to(REPO_ROOT)
    except ValueError:
        shown = args.specs
    print(
        f"\n{len(empty)} pathspec(s) match NOTHING. The curation-history advisory "
        f"counts matches\nand never asserts, so these silently contribute 0 and the "
        f"job still reports\n'no curation records changed'. Fix the spec in "
        f"{shown}, or remove it if\nthe surface is gone."
    )
    return 1


if __name__ == "__main__":
    sys.exit(main())
