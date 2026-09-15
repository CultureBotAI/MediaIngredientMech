#!/usr/bin/env python3
"""Check both current graph maps before publication, without loading vectors or models."""

from __future__ import annotations

import argparse
import json
import math
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT / "src"))

from mediaingredientmech.graph_embedding_receipts import corpus_receipt, load_receipt  # noqa: E402

MAPS = (("ingredient_umap", {"pacmap", "umap"}), ("ingredient_graph", {"sfdp"}))


def check_graph_receipts(root: Path = REPO_ROOT) -> list[dict]:
    """Bind the intended graph outputs to all current source files and ordered matches."""
    root = root.resolve()
    corpus = root / "data" / "ingredients"
    for directory in (root / "data", corpus, corpus / "mapped", corpus / "unmapped"):
        if directory.is_symlink() or not directory.is_dir():
            raise ValueError(f"missing real graph corpus directory: {directory}")
    # Same flat YAML population as the generator. Path.glob includes ignored files;
    # REJECTED records still belong to the source census, outside the eligible ledger.
    current = corpus_receipt(
        [
            path
            for category in ("mapped", "unmapped")
            for path in (corpus / category).glob("*.yaml")
        ],
        corpus,
    )
    current_paths = {entry["path"] for entry in current["files"]}
    checked = []
    for basename, methods in MAPS:
        metadata = root / "docs" / "data" / (basename + ".metadata.json")
        receipt = load_receipt(metadata)
        if set(receipt["outputs"]) != {basename + ".json"}:
            raise ValueError(f"graph receipt does not bind the intended JSON: {metadata}")
        if receipt["projection"]["method"] not in methods:
            raise ValueError(f"unexpected graph reducer: {metadata}")
        if receipt["corpus"] != current:
            raise ValueError(f"graph corpus changed since generation: {metadata}")

        coverage, ledger = receipt["coverage"], receipt["matching"]["rows"]
        projected = {row["identifier"]: row for row in ledger if row["status"] == "projected"}
        missing = [row["identifier"] for row in ledger if row["status"] == "missing_vector"]
        rejected = coverage.get("rejected_records")
        source_paths = [row.get("source_path") for row in ledger]
        if (
            any(row["status"] not in {"projected", "missing_vector"} for row in ledger)
            or any(row["source_nodes"] for row in ledger if row["status"] == "missing_vector")
            or not isinstance(rejected, list)
            or any(not isinstance(value, str) for value in source_paths + rejected)
            or len(set(source_paths + rejected)) != len(source_paths) + len(rejected)
            or set(source_paths + rejected) != current_paths
            or coverage.get("missing_records") != missing
            or type(coverage.get("omitted")) is not int
            or coverage["omitted"] != len(missing)
            or coverage.get("eligible_records") != len(ledger)
            or coverage.get("embedded_records") != len(projected)
            or type(coverage.get("synthetic_records")) is not int
            or coverage["synthetic_records"] != 0
        ):
            raise ValueError(f"graph coverage does not account for the complete corpus: {metadata}")

        points = json.loads((metadata.parent / (basename + ".json")).read_text())
        if (
            not isinstance(points, list)
            or len(points) != coverage["projected"]
            or any(
                not isinstance(row, dict)
                or not all(
                    type(row.get(axis)) in (int, float) and math.isfinite(row[axis])
                    for axis in ("umap_x", "umap_y")
                )
                for row in points
            )
            or [row.get("id") for row in points] != receipt["matrix"]["row_ids"]
        ):
            raise ValueError(f"graph points differ from the ordered receipt: {metadata}")
        for point in points:
            match = projected[point["id"]]
            if match.get("match_method") != point.get("embedding_method") or match[
                "source_nodes"
            ] != [point.get("embedding_source_node")]:
                raise ValueError(f"graph point differs from its lookup ledger: {metadata}")
        checked.append(
            {
                "receipt": metadata.relative_to(root).as_posix(),
                "points": len(points),
                "corpus_count": current["count"],
                "corpus_sha256": current["sha256"],
                "source_sha256": receipt["source"]["sha256"],
            }
        )
    return checked


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=REPO_ROOT)
    args = parser.parse_args(argv)
    try:
        result = check_graph_receipts(args.root)
    except (OSError, ValueError, TypeError, KeyError) as error:
        print(f"graph publication refused: {error}", file=sys.stderr)
        return 1
    print(json.dumps({"verified_graphs": result}, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
