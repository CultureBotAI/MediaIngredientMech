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

WHAT THIS DOES NOT CATCH, stated plainly rather than implied by a green tick:
this is a LIVENESS check, not a coverage one. A spec that matches some files but
not the ones intended still passes — `mappings/**` matching 20 files says nothing
about whether those are the 20 that matter. Only "matches literally nothing" is
detectable this way, because that is the failure mode with no other symptom.

(An earlier draft of this warned instead about a "partial miss" if
`data/curated/` gained a subdirectory. That was wrong, and is corrected here
rather than quietly dropped: git pathspecs without `:(glob)` magic use wildmatch
WITHOUT WM_PATHNAME, so a plain `*` DOES cross `/`. `data/ingredients/*.yaml`
and `data/ingredients/**/*.yaml` both match all 2,257 records. It is `**/` that
silently matches nothing against a flat tree, not `*` against a nested one.)

Exit codes: 0 = every pathspec matches, 1 = at least one matches nothing,
2 = usage/configuration error (missing or empty list).
"""

from __future__ import annotations

import argparse
import shlex
import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
DEFAULT_SPECS = REPO_ROOT / "conf" / "curation_targets.txt"


def _config_error(message: str) -> None:
    """Exit 2, so a broken config is distinguishable from a real finding."""
    print(message, file=sys.stderr)
    raise SystemExit(2)


def load_specs(path: Path, role: str | None = None) -> list[str]:
    """Pathspecs from the shared list, optionally filtered to one role.

    Lines are `<role>: <pathspec>`; blank lines and `#` comments are ignored.
    """
    if not path.is_file():
        _config_error(f"Curation-target list not found: {path}")
    specs: list[str] = []
    for lineno, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        stripped = line.strip()
        if not stripped or stripped.startswith("#"):
            continue
        if ":" not in stripped:
            _config_error(f"{path}:{lineno}: expected `<role>: <pathspec>`, got {stripped!r}")
        line_role, _, spec = stripped.partition(":")
        line_role, spec = line_role.strip(), spec.strip()
        if not spec:
            _config_error(f"{path}:{lineno}: no pathspec after the role")
        if role is None or line_role == role:
            specs.append(spec)
    if not specs:
        _config_error(f"{path} lists no pathspecs" + (f" for role {role!r}." if role else "."))
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
    # splitlines, not split: a tracked path containing a space would otherwise
    # count as two files.
    return len(proc.stdout.splitlines())


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--specs", type=Path, default=DEFAULT_SPECS)
    parser.add_argument(
        "--role",
        default=None,
        help="Only pathspecs with this role (`targets` or `history`). Default: all.",
    )
    parser.add_argument(
        "--print-specs",
        action="store_true",
        help="Print the pathspecs, shell-quoted, for the workflow to consume.",
    )
    args = parser.parse_args(argv)

    if args.print_specs:
        # shlex.quote, not a bare f"'{spec}'": a spec containing a single quote
        # would otherwise produce a string the consuming shell cannot parse.
        print(" ".join(shlex.quote(spec) for spec in load_specs(args.specs, args.role)))
        return 0

    # The assertion covers EVERY role — a `history` spec that stops matching is
    # just as dead as a `targets` one.
    specs = load_specs(args.specs)

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
