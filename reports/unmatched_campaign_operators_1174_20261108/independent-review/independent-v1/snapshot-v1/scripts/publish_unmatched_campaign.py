"""Publish a closed #1174 plan; defaults to a guarded dry run."""

import argparse
import json
from pathlib import Path

from mediaingredientmech.campaign_publication import publish


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path.cwd())
    parser.add_argument("--plan", type=Path, required=True)
    parser.add_argument("--receipt-dir", type=Path, required=True)
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args()
    print(json.dumps(publish(args.root, args.plan, args.receipt_dir, apply=args.apply), indent=2))


if __name__ == "__main__":
    main()
