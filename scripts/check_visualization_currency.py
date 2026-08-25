#!/usr/bin/env python3
"""Fail when a published visualization references records that no longer exist (#401).

`docs/data/ingredient_umap.json` and `ingredient_graph.json` are outward-facing —
the docs site renders them — and they had not been regenerated since #98. By the
time this was written, **114 of their 382 `UNMAPPED_*` ids named records that had
been merged, promoted or retired**, so roughly one node in three was wrong. They
still showed `X` mapped to NCIT "the 24th letter of the English alphabet" (#356),
`Aromatic hydrocarbon` on a retired mint (#392), and both labels corrected in
#397.

Nothing caught it because nothing regenerates them: `generate_ingredient_umap.py`
is reachable only from `just generate-umap`. The same shape as #217 and #380, for
a third artifact.

## Why this gate is membership-based rather than a no-op diff

#380's gate asserts that regenerating produces no diff. That works there because
`generate_index_files.py` is deterministic. **These are not.** Two consecutive
runs with `random_state=42` give:

    umap_x   max Δ 11.46   median Δ 0.5286
    umap_y   max Δ 12.29   median Δ 0.5550
    id set                 IDENTICAL
    total_occurrences / media_count / num_synonyms   IDENTICAL

PaCMAP's layout jitters (BLAS/thread nondeterminism the seed does not reach), so
a byte-diff gate would be permanently red — and a permanently red gate gets
deleted rather than obeyed, which is the failure #380's docstring warns about.

Everything that is *derived from the corpus* is stable, so this asserts that
instead: **every published node must name one live file-backed record, and must
carry that record's semantic identifier separately.** Visualization `id` values
are filename-derived `MIM:` record CURIEs; the non-unique ingredient
`identifier` cannot address sibling records. The check tolerates layout jitter
and needs no regeneration to compare coordinates.

It deliberately does NOT require every live record to appear. The generator drops
ingredients with no embedding, so absence is a coverage question rather than
staleness, and conflating them would make the gate fire on something it cannot
fix.

    python scripts/check_visualization_currency.py            # report
    python scripts/check_visualization_currency.py --strict   # exit 1 on key/identity defects
"""

from __future__ import annotations

import argparse
import json
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "src"))
from mediaingredientmech.curie import mim_curie_for_stem  # noqa: E402
from mediaingredientmech.utils.yaml_handler import load_yaml  # noqa: E402

INGREDIENTS = ROOT / "data" / "ingredients"
ARTIFACTS = ("ingredient_umap.json", "ingredient_graph.json")


def live_records(ingredients_root: Path = INGREDIENTS) -> dict[str, str]:
    """Return file-backed record CURIE -> semantic identifier for live records."""
    records: dict[str, str] = {}
    for category in ("mapped", "unmapped"):
        for path in (ingredients_root / category).glob("*.yaml"):
            try:
                record = load_yaml(path)
            except Exception:
                continue
            if not isinstance(record, dict) or record.get("mapping_status") == "REJECTED":
                continue
            record_key = mim_curie_for_stem(path.stem)
            if record_key in records:
                raise ValueError(f"Duplicate visualization record key: {record_key}")
            records[record_key] = str(record.get("identifier") or "").strip()
    return records


def audit_entries(entries: object, live: dict[str, str]) -> dict[str, list]:
    """Return stable identity defects for one published artifact payload."""
    if not isinstance(entries, list):
        return {
            "invalid_entries": ["payload is not a list"],
            "blank_ids": [],
            "duplicate_ids": [],
            "stale": [],
            "identity_mismatches": [],
        }

    invalid_entries = [index for index, entry in enumerate(entries) if not isinstance(entry, dict)]
    nodes = [entry for entry in entries if isinstance(entry, dict)]
    node_ids = [str(entry.get("id") or "").strip() for entry in nodes]
    blank_ids = [index for index, node_id in enumerate(node_ids) if not node_id]
    ids = {node_id for node_id in node_ids if node_id}
    duplicate_ids = sorted(
        node_id for node_id, count in Counter(node_ids).items() if node_id and count > 1
    )
    stale = sorted(ids - live.keys())
    identity_mismatches = []
    for entry in nodes:
        record_key = str(entry.get("id") or "").strip()
        if record_key not in live:
            continue
        semantic_id = str(entry.get("identifier") or "").strip()
        if semantic_id != live[record_key]:
            identity_mismatches.append(
                (record_key, semantic_id or "<missing>", live[record_key])
            )
    return {
        "invalid_entries": invalid_entries,
        "blank_ids": blank_ids,
        "duplicate_ids": duplicate_ids,
        "stale": stale,
        "identity_mismatches": identity_mismatches,
    }


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )
    ap.add_argument(
        "--strict",
        action="store_true",
        help="exit 1 on missing, duplicate, or semantically mismatched record keys",
    )
    args = ap.parse_args(argv)

    live = live_records()
    if not live:
        print("CANNOT CHECK: no live per-record ingredients loaded.")
        return 2

    worst = 0
    for name in ARTIFACTS:
        path = ROOT / "docs" / "data" / name
        if not path.exists():
            print(f"  {name}: absent — skipped")
            continue
        entries = json.loads(path.read_text(encoding="utf-8"))
        if isinstance(entries, dict):
            entries = entries.get("ingredients", [])
        audit = audit_entries(entries, live)
        invalid_entries = audit["invalid_entries"]
        blank_ids = audit["blank_ids"]
        duplicate_ids = audit["duplicate_ids"]
        stale = audit["stale"]
        identity_mismatches = audit["identity_mismatches"]
        node_count = len(entries) if isinstance(entries, list) else 0
        nonblank_count = max(node_count - len(blank_ids) - len(invalid_entries), 0)
        pct = (100 * len(stale) // nonblank_count) if nonblank_count else 0
        defects = sum(len(values) for values in audit.values())
        flag = "STALE" if defects else "ok"
        print(
            f"  {flag:<6} {name:<24} nodes {node_count:>5}  naming missing "
            f"records {len(stale):>4} ({pct}%)  duplicate keys "
            f"{len(duplicate_ids):>3}  blank keys {len(blank_ids):>3}  "
            f"invalid entries {len(invalid_entries):>3}  "
            f"wrong identities {len(identity_mismatches):>3}"
        )
        for s in stale[:8]:
            print(f"            {s}")
        if len(stale) > 8:
            print(f"            ... {len(stale) - 8} more")
        for record_key in duplicate_ids[:8]:
            print(f"            duplicate record key: {record_key}")
        for index in blank_ids[:8]:
            print(f"            blank record key at node index {index}")
        for index in invalid_entries[:8]:
            print(f"            invalid node entry at index {index}")
        for record_key, observed, expected in identity_mismatches[:8]:
            print(f"            {record_key}: identifier {observed}, expected {expected}")
        worst = max(worst, defects)

    if worst:
        print(
            "\nVisualization nodes have stale, duplicate, or semantically mismatched "
            "record identities. Regenerate:\n"
            "    just generate-umap        # writes docs/data/ingredient_umap.json\n"
            "    just generate-graph       # writes docs/data/ingredient_graph.json\n"
            "Layout coordinates will differ between runs (PaCMAP is not fully "
            "deterministic); only the membership above is asserted."
        )
        if args.strict:
            return 1
    else:
        print("\nOK: every published node names one live record and carries its semantic identity.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
