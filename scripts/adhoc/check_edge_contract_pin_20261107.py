"""Verify the optional EdgeMech shared source pin for CLAW #767, 2026-11-07.

Inputs: native pyproject metadata and an explicit CLAW source checkout path.
Output: verified commit, contract, and import origin; no repository mutation.
"""

import argparse
from pathlib import Path
import subprocess
import tomllib

from kg_microbe_curation import native


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--claw-root", type=Path, required=True)
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[2]
    pin = tomllib.loads((root / "pyproject.toml").read_text())["tool"]["mediaingredientmech"][
        "edge-curation"
    ]
    checkout = args.claw_root.resolve()
    expected_source = checkout / "src/kg_microbe_curation"
    if Path(native.__file__).resolve().parent != expected_source:
        raise ValueError("Shared native contract imported from an unexpected source checkout")
    head = subprocess.check_output(
        ["git", "-C", str(checkout), "rev-parse", "HEAD"], text=True
    ).strip()
    if head != pin["commit"] or native.NATIVE_CONTRACT != pin["contract"]:
        raise ValueError("Shared contract commit/version differs from the native pin")
    url = subprocess.check_output(
        ["git", "-C", str(checkout), "remote", "get-url", "origin"], text=True
    ).strip()
    if url not in {
        f"https://github.com/{pin['repository']}.git",
        f"https://github.com/{pin['repository']}",
        f"git@github.com:{pin['repository']}.git",
    }:
        raise ValueError("Shared source checkout has an unexpected Git origin")
    dirty = subprocess.check_output(
        ["git", "-C", str(checkout), "status", "--porcelain", "--", "src/kg_microbe_curation"],
        text=True,
    )
    if dirty:
        raise ValueError("Shared contract source differs from the pinned commit")
    print(f"Verified {pin['repository']} at {head}; {native.NATIVE_CONTRACT}")


if __name__ == "__main__":
    main()
