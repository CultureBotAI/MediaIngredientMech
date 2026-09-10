"""Gate stale same-prefix kg_microbe_node_id values (#554).

`identifier` is the record's semantic identity. `kg_microbe_node_id` is a
compatibility copy consumed by downstream graph exports. When a same-prefix
identifier is corrected but the node id is left behind, published derivative
files keep pointing at the old term even though the curated record has moved.

Cross-prefix differences are possible and need human review: those values may be
intentional local anchors for an external ontology identity. This checker writes
every mismatch to reports/kg_microbe_node_id_mismatches.tsv, but `--check` only
fails on same-prefix mismatches that are always stale drift.
"""

from __future__ import annotations

import argparse
import csv
import re
import sys
from collections.abc import Iterator
from pathlib import Path
from typing import Any

import yaml

ROOT = Path(__file__).resolve().parents[1]
COLLECTIONS = {
    "mapped": ROOT / "data" / "curated" / "mapped_ingredients.yaml",
    "unmapped": ROOT / "data" / "curated" / "unmapped_ingredients.yaml",
}
REPORT = ROOT / "reports" / "kg_microbe_node_id_mismatches.tsv"

FIELDS = [
    "collection",
    "preferred_term",
    "identifier",
    "kg_microbe_node_id",
    "identifier_prefix",
    "kg_microbe_prefix",
    "mismatch_type",
]

PREFIX_RE = re.compile(r"^([A-Za-z][A-Za-z0-9.]*):")


class DataProblem(Exception):
    """Anything that should exit 2 with a message rather than a traceback."""


def curie_prefix(curie: Any) -> str:
    match = PREFIX_RE.match(str(curie))
    return match.group(1) if match else ""


def mismatch_type(identifier: Any, kg_microbe_node_id: Any) -> str:
    identifier_prefix = curie_prefix(identifier)
    kg_microbe_prefix = curie_prefix(kg_microbe_node_id)
    if (
        identifier_prefix
        and kg_microbe_prefix
        and identifier_prefix.casefold() == kg_microbe_prefix.casefold()
    ):
        return "same_prefix"
    return "cross_prefix"


def load_collection(path: Path) -> dict:
    if not path.exists():
        raise DataProblem(f"missing collection: {path.relative_to(ROOT)}")
    try:
        doc = yaml.safe_load(path.read_text())
    except yaml.YAMLError as exc:
        raise DataProblem(f"unparseable YAML in {path.relative_to(ROOT)}: {exc}") from exc
    if not isinstance(doc, dict) or not isinstance(doc.get("ingredients"), list):
        raise DataProblem(f"{path.relative_to(ROOT)} has no 'ingredients' list")
    return doc


def iter_records() -> Iterator[tuple[str, dict]]:
    for collection, path in COLLECTIONS.items():
        for index, record in enumerate(load_collection(path)["ingredients"]):
            if not isinstance(record, dict):
                rel = path.relative_to(ROOT)
                raise DataProblem(f"{rel}: ingredients[{index}] is not a mapping")
            if "identifier" not in record:
                rel = path.relative_to(ROOT)
                raise DataProblem(f"{rel}: ingredients[{index}] has no identifier")
            yield collection, record


def row_for(collection: str, record: dict) -> dict[str, str] | None:
    kg_microbe_node_id = record.get("kg_microbe_node_id")
    if kg_microbe_node_id is None:
        return None

    identifier = record["identifier"]
    if str(identifier) == str(kg_microbe_node_id):
        return None

    identifier_prefix = curie_prefix(identifier)
    kg_microbe_prefix = curie_prefix(kg_microbe_node_id)
    return {
        "collection": collection,
        "preferred_term": str(record.get("preferred_term") or ""),
        "identifier": str(identifier),
        "kg_microbe_node_id": str(kg_microbe_node_id),
        "identifier_prefix": identifier_prefix,
        "kg_microbe_prefix": kg_microbe_prefix,
        "mismatch_type": mismatch_type(identifier, kg_microbe_node_id),
    }


def survey() -> list[dict[str, str]]:
    rows = [
        row
        for collection, record in iter_records()
        if (row := row_for(collection, record)) is not None
    ]
    return sorted(
        rows,
        key=lambda row: (
            row["mismatch_type"],
            row["collection"],
            row["preferred_term"].casefold(),
            row["identifier"],
            row["kg_microbe_node_id"],
        ),
    )


def write_report(rows: list[dict[str, str]]) -> None:
    REPORT.parent.mkdir(parents=True, exist_ok=True)
    with REPORT.open("w", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=FIELDS, delimiter="\t", lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument(
        "--check",
        action="store_true",
        help="exit 2 when a same-prefix kg_microbe_node_id disagrees with identifier",
    )
    args = ap.parse_args()

    try:
        rows = survey()
    except DataProblem as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2

    write_report(rows)

    same_prefix = [row for row in rows if row["mismatch_type"] == "same_prefix"]
    cross_prefix = [row for row in rows if row["mismatch_type"] == "cross_prefix"]
    print(f"{len(rows)} kg_microbe_node_id mismatch(es)")
    print(f"  {len(same_prefix)} same-prefix mismatch(es)")
    print(f"  {len(cross_prefix)} cross-prefix mismatch(es)")
    for row in same_prefix:
        print(
            "  "
            f"{row['collection']}\t{row['preferred_term']}\t"
            f"{row['kg_microbe_node_id']} -> {row['identifier']}"
        )

    if args.check and same_prefix:
        print(f"ERROR: {len(same_prefix)} same-prefix kg_microbe_node_id mismatch(es)")
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
