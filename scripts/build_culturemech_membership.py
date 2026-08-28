#!/usr/bin/env python3
"""Publish which CultureMech recipes use each MIM ingredient (#449).

MIM stores two aggregate counts per record -- `media_count` and
`total_occurrences` -- and nothing else. Those answer "how many", never "which",
so the membership itself has never been reconstructable from this repo. #485
corrected the counts; this publishes the edges they are counted from.

The artifact is an edge list, one row per (MIM ingredient, CultureMech recipe):

    mim_identifier    recipe_id           occurrences
    CHEBI:49976       CultureMech:000473  1

Deliberately NO names on either side. CultureMech recipe names are not unique --
2291 are shared, one names 29 distinct recipes, and 4784 recipes have none -- and
a display string in an edge table invites exactly the name-keyed identity that
#447 removed. Both sides are stable ids; labels are looked up from the records.

`occurrences` is the number of times the ingredient is listed within that one
recipe, so it is >= 1 and usually 1. Summing it over a record's edges reproduces
`total_occurrences`; counting the edges reproduces `media_count`. That is the
documented definition the issue asks for, and the invariant the test asserts.

CAUTION, and it is not a rounding error: several MIM records share one
identifier (#225 / #334). `MgSO4 x 7 H2O` and `MgSO4·H2O` both resolve to
CHEBI:31795, so they share these edges and a monohydrate inherits the
heptahydrate's memberships. Edges are keyed on the identifier because that is
what CultureMech resolved to; they cannot be split until those records are
merged. Do not sum membership across records.

Usage:
    python scripts/build_culturemech_membership.py --occurrences PATH
"""

from __future__ import annotations

import argparse
import csv
import subprocess
import sys
from collections import defaultdict
from pathlib import Path

import yaml

REPO_ROOT = Path(__file__).resolve().parent.parent
CURATED = REPO_ROOT / "data" / "curated" / "mapped_ingredients.yaml"
OUTPUT = REPO_ROOT / "mappings" / "culturemech_recipe_membership.tsv"

# `ingredient_json` carries a whole serialized component.
csv.field_size_limit(1 << 30)


def provenance(occurrences: Path, edges: int, recipes: int, records: int) -> str:
    """Which CultureMech tree these edges came from (#486).

    Recipe ids are stable but the SET of recipes is not, so an edge list read
    later cannot be checked against the tree that produced it without this.
    """
    sha = "unknown"
    try:
        result = subprocess.run(
            ["git", "-C", str(occurrences.resolve().parent), "rev-parse", "--short", "HEAD"],
            capture_output=True, text=True, timeout=30)
        if result.returncode == 0:
            sha = result.stdout.strip() or "unknown"
    except (OSError, subprocess.SubprocessError):
        pass
    return (f"source=ingredient_occurrences.tsv culturemech_rev={sha} "
            f"edges={edges} recipes={recipes} mim_records={records}")


def mim_identifiers() -> set[str]:
    data = yaml.safe_load(CURATED.read_text(encoding="utf-8"))
    return {str(r.get("identifier") or "") for r in data["ingredients"]} - {""}


def collect(occurrences: Path, known: set[str]) -> tuple[dict, list[str]]:
    """(edge -> occurrence count, identifiers seen upstream but absent from MIM)."""
    edges: dict[tuple[str, str], int] = defaultdict(int)
    unknown: set[str] = set()
    with occurrences.open(newline="", encoding="utf-8") as fh:
        reader = csv.DictReader(fh, delimiter="\t")
        for field in ("resolved_identifier", "recipe_id"):
            if field not in (reader.fieldnames or []):
                raise SystemExit(
                    f"error: {occurrences} has no {field!r} column; this needs the "
                    "CultureMech#337 occurrence table."
                )
        for row in reader:
            identifier = (row.get("resolved_identifier") or "").strip()
            recipe_id = (row.get("recipe_id") or "").strip()
            if not identifier or not recipe_id:
                continue
            if identifier not in known:
                # Reported, not dropped silently: an id CultureMech resolved to
                # that MIM does not hold is a gap in one of the two, and which
                # one is a curation question.
                unknown.add(identifier)
                continue
            edges[(identifier, recipe_id)] += 1
    return edges, sorted(unknown)


def write(edges: dict, header: str) -> None:
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    with OUTPUT.open("w", newline="", encoding="utf-8") as fh:
        writer = csv.writer(fh, delimiter="\t", lineterminator="\n")
        writer.writerow([f"# {header}"])
        writer.writerow(["mim_identifier", "recipe_id", "occurrences"])
        # Sorted so re-running is deterministic and the diff is reviewable --
        # dict order would make every rebuild look like a rewrite.
        for (identifier, recipe_id), count in sorted(edges.items()):
            writer.writerow([identifier, recipe_id, count])


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--occurrences", type=Path, required=True,
                        help="CultureMech output/ingredient_occurrences.tsv (#337)")
    args = parser.parse_args(argv)

    known = mim_identifiers()
    edges, unknown = collect(args.occurrences, known)
    recipes = {recipe_id for _, recipe_id in edges}
    records = {identifier for identifier, _ in edges}
    header = provenance(args.occurrences, len(edges), len(recipes), len(records))
    write(edges, header)

    multi = sum(1 for v in edges.values() if v > 1)
    print(header)
    print(f"{len(edges)} membership edge(s) over {len(records)} MIM identifier(s) "
          f"and {len(recipes)} recipe(s)")
    print(f"{multi} edge(s) list the ingredient more than once in one recipe")
    if unknown:
        print(f"{len(unknown)} upstream identifier(s) are not held by MIM and were "
              f"reported rather than published: {', '.join(unknown[:5])}"
              + (" ..." if len(unknown) > 5 else ""))
    print(f"\nwrote {OUTPUT.relative_to(REPO_ROOT)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
