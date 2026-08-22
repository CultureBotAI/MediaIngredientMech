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

Git history is not the only way a subject is retired
-----------------------------------------------------
A published ``MIM:`` subject can stop resolving without any file ever being
renamed, so ``git log --diff-filter=R`` cannot see it:

* **Escaping.** ``(R)-lactate.yaml`` has always had that name, but the published
  SSSOM carried ``MIM:(R)-lactate`` while ``mim_curie_for_stem`` produces
  ``MIM:~28R~29-lactate``. The file never moved; the two sides disagree about
  how to spell it, and only the escaped form satisfies ``curie.py``'s
  ``_CURIE_RE``.
* **Case.** ``MIM:EDTA_Stock`` vs ``Edta_Stock.yaml`` — a case-only rename on a
  case-insensitive filesystem, which git may never have recorded.
* **Recomputed subjects.** Several MIM writers derive the SSSOM subject from
  ``preferred_term`` rather than the filename (#293, #307), so the published
  file contains subjects that were never filenames at all.

Those are supplied by ``mappings/mim_curie_alias_seeds.tsv`` and folded into the
same graph as the git renames, so chaining and validation apply identically. The
seeds file is an **input**, hand- or tooling-maintained; this script overwrites
its output wholesale, so anything not derivable from git has to live there or it
is silently dropped on the next run.

Input:  ``mappings/mim_curie_alias_seeds.tsv``
    old_curie  current_curie  retired_at  reason
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
SEEDS_DEFAULT = REPO / "mappings" / "mim_curie_alias_seeds.tsv"

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


def collect_seeds(path: Path) -> list[tuple[str, str, str]]:
    """[(old_curie, current_curie, iso_date)] from the seeds TSV, or [] if absent.

    Seeds are retirements git cannot see (escaping, case-only renames on a
    case-insensitive filesystem, subjects recomputed from `preferred_term`).
    Applied after the git renames so a seed can retarget an alias whose git
    target was itself later re-spelled.
    """
    if not path.exists():
        return []
    seeds: list[tuple[str, str, str]] = []
    with path.open(newline="") as f:
        for row in csv.DictReader(f, delimiter="\t"):
            old = (row.get("old_curie") or "").strip()
            new = (row.get("current_curie") or "").strip()
            if not old or not new:
                continue
            seeds.append((old, new, (row.get("retired_at") or "").strip()))
    return seeds


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--output", type=Path, default=OUT_DEFAULT)
    ap.add_argument("--seeds", type=Path, default=SEEDS_DEFAULT,
                    help="Retirements git cannot derive. Default: %(default)s")
    args = ap.parse_args()

    renames = collect_renames()
    print(f"rename records in history: {len(renames)}")

    seeds = collect_seeds(args.seeds)
    print(f"seeded retirements (not derivable from git): {len(seeds)}")

    # One edge list, folded once: git renames first (historical), then seeds
    # (discovered at publish time), so a seed can retarget an alias whose git
    # target was itself later re-spelled.
    edges = [(mim_curie(old), mim_curie(new), date) for old, new, date in renames]
    edges += seeds

    # Fold the chain: each old stem points at wherever its target ended up.
    current: dict[str, str] = {}
    first_seen: dict[str, str] = {}
    retired_at: dict[str, str] = {}
    for o, n, date in edges:
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
