#!/usr/bin/env python3
"""Apply only accepted campaign owner bytes; dry run by default (#1174)."""

import argparse
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from mediaingredientmech.curate.campaign_owner_apply import apply, prepare


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, required=True)
    parser.add_argument("--plan", type=Path, required=True)
    parser.add_argument("--acceptance", type=Path, required=True)
    parser.add_argument("--receipt-dir", type=Path, required=True)
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("--apply", action="store_true")
    mode.add_argument("--dry-run", action="store_true")
    args = parser.parse_args(argv)
    prepared = prepare(args.root, args.plan, args.acceptance)
    result = apply(prepared, args.receipt_dir, enabled=args.apply)
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
