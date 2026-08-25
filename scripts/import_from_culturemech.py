#!/usr/bin/env python3
"""Fail-closed compatibility stub for the retired CultureMech bulk importer.

The former implementation replaced both curated collections with lossy,
schema-invalid projections of CultureMech aggregate files. Git history retains
that migration artifact; this module deliberately exposes no conversion or
write API. See issue #453.
"""

from __future__ import annotations

import argparse
import sys
from collections.abc import Sequence
from pathlib import Path

RETIREMENT_MESSAGE = (
    "error: the CultureMech bulk importer is retired because it can overwrite "
    "MIM-owned curation with a lossy, schema-invalid projection (#453). No files "
    "were read or written. Review CultureMech changes and apply a scoped curated "
    "update until the replacement contracts in #447 and #449 are implemented."
)


def build_parser() -> argparse.ArgumentParser:
    """Retain legacy arguments so old automation receives a clear error."""
    parser = argparse.ArgumentParser(
        description="Retired CultureMech-to-MIM bulk importer (see #453)"
    )
    parser.add_argument(
        "--source-dir",
        type=Path,
        help="Ignored legacy argument; retained so old automation fails clearly",
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        help="Ignored legacy argument; retained so old automation fails clearly",
    )
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    """Explain the retirement and fail before reading or writing any path."""
    build_parser().parse_args(argv)
    print(RETIREMENT_MESSAGE, file=sys.stderr)
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
