"""Independently reconstruct and replay an applied #1174 publication plan."""

import argparse
import json
from pathlib import Path

from mediaingredientmech.campaign_publication import validate


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path.cwd())
    parser.add_argument("--plan", type=Path, required=True)
    args = parser.parse_args()
    print(json.dumps(validate(args.root, args.plan), indent=2))


if __name__ == "__main__":
    main()
