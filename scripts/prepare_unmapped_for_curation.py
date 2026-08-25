#!/usr/bin/env python3
"""Fail-closed stub for the retired CultureMech unmapped-record writer.

The former implementation rebuilt ``unmapped_ingredients.yaml`` from an
incomplete CultureMech aggregate and discarded MIM-owned curation that was not
present in that snapshot. Git history retains the migration artifact; this
module deliberately exposes no conversion or file-I/O API. See issue #453.
"""

from __future__ import annotations

import argparse
import sys
from collections.abc import Sequence

RETIREMENT_MESSAGE = (
    "error: the CultureMech unmapped-record writer is retired because it can "
    "replace MIM-owned curation from an incomplete aggregate (#453). No files "
    "were read or written. Review source differences and apply scoped curation "
    "updates until #447 and #449 define a safe replacement."
)


def build_parser() -> argparse.ArgumentParser:
    """Build the compatibility parser for a command that had no options."""
    return argparse.ArgumentParser(
        description="Retired CultureMech unmapped-record writer (see #453)"
    )


def main(argv: Sequence[str] | None = None) -> int:
    """Explain the retirement and fail before reading or writing any path."""
    build_parser().parse_args(argv)
    print(RETIREMENT_MESSAGE, file=sys.stderr)
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
