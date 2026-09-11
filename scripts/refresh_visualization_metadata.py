#!/usr/bin/env python3
"""Refresh stable metadata in published visualization JSON artifacts.

The UMAP and graph coordinates need the large KG-Microbe embedding TSV, but
their stable node metadata only depends on the file-backed ingredient records.
Use this after targeted curation changes to bring existing published nodes back
in sync without recomputing coordinates.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from check_visualization_currency import ARTIFACTS, ROOT, live_records


def refresh_artifact(path: Path, live: dict[str, dict[str, object]]) -> tuple[int, int]:
    payload = json.loads(path.read_text(encoding="utf-8"))
    if isinstance(payload, dict):
        entries = payload.get("ingredients")
    else:
        entries = payload
    if not isinstance(entries, list):
        raise ValueError(f"{path} does not contain a visualization node list")

    removed = 0
    updated = 0
    refreshed: list[object] = []
    for entry in entries:
        if not isinstance(entry, dict):
            refreshed.append(entry)
            continue

        record_key = str(entry.get("id") or "").strip()
        expected = live.get(record_key)
        if expected is None and record_key:
            removed += 1
            continue

        if expected is not None:
            changed = False
            for field, value in expected.items():
                if entry.get(field) != value:
                    entry[field] = value
                    changed = True
            if changed:
                updated += 1

        refreshed.append(entry)

    if isinstance(payload, dict):
        payload["ingredients"] = refreshed
    else:
        payload = refreshed

    path.write_text(f"{json.dumps(payload, indent=2)}\n", encoding="utf-8")
    return removed, updated


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--docs-data",
        type=Path,
        default=ROOT / "docs" / "data",
        help="Directory containing ingredient_umap.json and ingredient_graph.json",
    )
    args = parser.parse_args()

    live = live_records()
    for artifact in ARTIFACTS:
        path = args.docs_data / artifact
        if not path.exists():
            continue
        removed, updated = refresh_artifact(path, live)
        print(f"{artifact}: removed {removed} stale node(s), updated {updated} node(s)")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
