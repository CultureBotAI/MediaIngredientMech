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
instead: **no published node may name a record that does not exist.** That is the
defect, it tolerates layout jitter, and it needs no regeneration to check.

It deliberately does NOT require every live record to appear. The generator drops
ingredients with no embedding, so absence is a coverage question rather than
staleness, and conflating them would make the gate fire on something it cannot
fix.

    python scripts/check_visualization_currency.py            # report
    python scripts/check_visualization_currency.py --strict   # exit 1 on stale ids
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "src"))
import yaml  # noqa: E402

CURATED = ROOT / "data" / "curated"
ARTIFACTS = ("ingredient_umap.json", "ingredient_graph.json")


def live_identifiers() -> set[str]:
    ids: set[str] = set()
    for name in ("mapped_ingredients.yaml", "unmapped_ingredients.yaml"):
        path = CURATED / name
        if not path.exists():
            continue
        for rec in (yaml.safe_load(path.read_text(encoding="utf-8")) or {}
                    ).get("ingredients", []) or []:
            ident = str(rec.get("identifier") or "").strip()
            if ident:
                ids.add(ident)
    return ids


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--strict", action="store_true",
                    help="exit 1 when a visualization names a missing record")
    args = ap.parse_args(argv)

    live = live_identifiers()
    if not live:
        print("CANNOT CHECK: no curated records loaded.")
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
        ids = {str(e.get("id") or e.get("identifier") or "").strip()
               for e in entries if isinstance(e, dict)}
        ids.discard("")
        stale = sorted(ids - live)
        pct = (100 * len(stale) // len(ids)) if ids else 0
        flag = "STALE" if stale else "ok"
        print(f"  {flag:<6} {name:<24} nodes {len(ids):>5}  naming missing "
              f"records {len(stale):>4} ({pct}%)")
        for s in stale[:8]:
            print(f"            {s}")
        if len(stale) > 8:
            print(f"            ... {len(stale) - 8} more")
        worst = max(worst, len(stale))

    if worst:
        print("\nThese nodes name records that no longer exist — merged, promoted or "
              "retired since the visualization was last built. Regenerate:\n"
              "    just generate-umap        # writes docs/data/ingredient_umap.json\n"
              "    just generate-graph       # writes docs/data/ingredient_graph.json\n"
              "Layout coordinates will differ between runs (PaCMAP is not fully "
              "deterministic); only the membership above is asserted.")
        if args.strict:
            return 1
    else:
        print("\nOK: every published node names a record that exists.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
