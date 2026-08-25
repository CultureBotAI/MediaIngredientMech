#!/usr/bin/env python3
"""Fail-closed stub for the retired CultureMech role-enrichment writer.

The former implementation mutated the mapped collection in place from an
incomplete CultureMech aggregate. Git history retains that migration artifact;
this module deliberately exposes no enrichment or file-I/O API. See issue
#453.
"""

from __future__ import annotations

import argparse
import sys
from collections.abc import Sequence

RETIREMENT_MESSAGE = (
    "error: the CultureMech role-enrichment writer is retired because it can "
    "overwrite MIM-owned curation from an incomplete aggregate (#453). No "
    "files were read or written. Apply evidence-backed role changes through "
    "the maintained curation workflow instead."
)


def build_parser() -> argparse.ArgumentParser:
    """Retain the legacy flag so old automation receives a clear error."""
    parser = argparse.ArgumentParser(
        description="Retired CultureMech role-enrichment writer (see #453)"
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Ignored legacy argument; the command is always fail-closed",
    )
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    """Explain the retirement and fail before reading or writing any path."""
    build_parser().parse_args(argv)
    print(RETIREMENT_MESSAGE, file=sys.stderr)
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
