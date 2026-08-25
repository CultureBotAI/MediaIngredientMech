#!/usr/bin/env python3
"""Fail-closed compatibility stub for the retired CultureMech merge utility.

The former implementation defaulted to a live collection overwrite, dropped
records absent from an aggregate, and wrote a report even in dry-run mode. Git
history retains that migration artifact; this module deliberately exposes no
merge, conversion, or file-I/O API. See issue #453.
"""

from __future__ import annotations

import argparse
import sys
from collections.abc import Sequence

RETIREMENT_MESSAGE = (
    "error: the CultureMech merge utility is retired because it can delete or "
    "overwrite MIM-owned curation from lossy aggregate data (#453). No files "
    "were read or written. Use reviewed, scoped curation updates until #447 "
    "and #449 define a safe replacement."
)


def build_parser() -> argparse.ArgumentParser:
    """Retain legacy arguments so old automation receives a clear error."""
    parser = argparse.ArgumentParser(
        description="Retired CultureMech-to-MIM merge utility (see #453)"
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Ignored legacy argument; the command is always fail-closed",
    )
    parser.add_argument(
        "--verbose",
        "-v",
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
