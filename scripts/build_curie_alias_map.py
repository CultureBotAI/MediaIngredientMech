#!/usr/bin/env python3
"""Generate the MIM CURIE alias map from git rename history.

MIM's published SSSOM subject, ``MIM:<stem>``, is derived from the ingredient
YAML's filename. Filenames are not immutable — ``git log --diff-filter=R`` over
``data/ingredients/`` shows 205 renames, including case-only changes
(``1-Naphtylacetic_Acid`` → ``1-naphtylacetic_Acid``) and every unmapped→mapped
promotion (``unmapped/NH42CO3`` → ``mapped/Nh42co3``). Each one silently retires
a CURIE that external repos may already have persisted.

This walks the rename history and emits, for every historical CURIE, the CURIE it
resolves to today. Renames are chained transitively (A→B→C yields A→C and B→C)
and validated against the working tree, so a stale alias whose target no longer
exists is reported rather than published.

Output: ``mappings/mim_curie_aliases.tsv``
    old_curie  current_curie  first_seen  retired_at  chain_length
"""

from __future__ import annotations

import argparse
import csv
import re
import subprocess
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
OUT_DEFAULT = REPO / "mappings" / "mim_curie_aliases.tsv"

# Mirrors build_mim_ingredient_sssom._mim_curie: the stem, with characters that
# are not URL-safe percent-style escaped as ~HEX so the CURIE round-trips.
def mim_curie(path: str) -> str:
    stem = Path(path).stem
    safe = re.sub(r"[^A-Za-z0-9_\-.]", lambda m: f"~{ord(m.group(0)):02X}", stem)
    return f"MIM:{safe}"


def git(*args: str) -> str:
    return subprocess.run(["git", "-C", str(REPO), *args],
                          capture_output=True, text=True, check=True).stdout


def collect_renames() -> list[tuple[str, str, str]]:
    """[(old_path, new_path, iso_date)] oldest-first."""
    out = git("log", "--diff-filter=R", "--name-status", "--format=%x01%aI",
              "--", "data/ingredients/")
    renames: list[tuple[str, str, str]] = []
    date = ""
    for line in out.splitlines():
        if line.startswith("\x01"):
            date = line[1:].strip()
            continue
        if line.startswith("R"):
            parts = line.split("\t")
            if len(parts) >= 3:
                renames.append((parts[1], parts[2], date))
    renames.reverse()  # oldest first, so later renames win
    return renames


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--output", type=Path, default=OUT_DEFAULT)
    args = ap.parse_args()

    renames = collect_renames()
    print(f"rename records in history: {len(renames)}")

    # Fold the chain: each old stem points at wherever its target ended up.
    current: dict[str, str] = {}
    first_seen: dict[str, str] = {}
    retired_at: dict[str, str] = {}
    for old, new, date in renames:
        o, n = mim_curie(old), mim_curie(new)
        if o == n:
            continue  # directory move only; CURIE unchanged
        # Anything that previously resolved to `o` now resolves to `n`.
        for k, v in list(current.items()):
            if v == o:
                current[k] = n
        current[o] = n
        first_seen.setdefault(o, date)
        retired_at[o] = date

    # Validate targets exist in the working tree.
    live = {mim_curie(str(p)) for d in ("mapped", "unmapped")
            for p in (REPO / "data" / "ingredients" / d).glob("*.yaml")}
    rows, dangling = [], []
    for old, new in sorted(current.items()):
        if old in live:
            # The old name is in use again (a rename was reverted, or another
            # record took the name). Publishing an alias would misdirect.
            dangling.append((old, new, "old CURIE is live again"))
            continue
        if new not in live:
            dangling.append((old, new, "target no longer exists"))
            continue
        chain = 1
        seen, cur = {old}, old
        while cur in current and current[cur] not in seen:
            cur = current[cur]; seen.add(cur); chain += 1
        rows.append({
            "old_curie": old, "current_curie": new,
            "first_seen": first_seen.get(old, ""),
            "retired_at": retired_at.get(old, ""),
            "chain_length": chain,
        })

    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open("w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=["old_curie", "current_curie", "first_seen",
                                          "retired_at", "chain_length"], delimiter="\t")
        w.writeheader()
        w.writerows(rows)

    print(f"live records: {len(live)}")
    print(f"published aliases: {len(rows)}  -> {args.output.relative_to(REPO)}")
    if dangling:
        print(f"\nWITHHELD ({len(dangling)}) — not published:", file=sys.stderr)
        for old, new, why in dangling[:10]:
            print(f"  {old} -> {new}: {why}", file=sys.stderr)
        if len(dangling) > 10:
            print(f"  ... {len(dangling)-10} more", file=sys.stderr)


if __name__ == "__main__":
    main()
