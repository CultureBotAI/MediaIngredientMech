#!/usr/bin/env python3
"""Flag chemical labels whose locant list was truncated by a comma-splitting bug.

`data/custom/microbedecoder/*.tsv` contains **zero commas across 6,247 label
rows**, which is impossible for chemical nomenclature — locants like `2,3-` and
`3,4,5-` are everywhere. The mechanism is not comma deletion but *split on comma,
keep the last field*: `3,4,5-trimethoxybenzoate` arrives as `5-trimethoxybenzoate`.

The damage is silent because the truncated string still looks like a chemical
name, and matching happily grounds it — sometimes to the right compound anyway
(`5-trimethoxybenzoate` → `3,4,5-trimethoxybenzoate`, harmless), and sometimes to
a *different real compound* (`5-didehydro-D-gluconic acid` → CHEBI:17426
`5-dehydro-D-gluconic acid`, when the true term is CHEBI:18281
`2,5-didehydro-D-gluconic acid`). The second kind is published as
`skos:exactMatch`, which licenses node substitution downstream.

The detectable signature: a multiplying prefix (di/tri/tetra/…) needs as many
locants as its multiplier. `2,3-dimethyl…` is well formed; `3-dimethyl…` cannot
exist. Only labels carrying an explicit locant group are checked, so unlocanted
names like `dimethyl sulfoxide` are correctly ignored.

    python scripts/check_truncated_locants.py
    python scripts/check_truncated_locants.py --tsv reports/truncated_locants.tsv
"""
from __future__ import annotations

import argparse
import csv
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "src"))
import yaml  # noqa: E402

INGREDIENTS = ROOT / "data" / "ingredients"

MULTIPLIER = {"di": 2, "bis": 2, "tri": 3, "tris": 3, "tetra": 4, "tetrakis": 4,
              "penta": 5, "hexa": 6, "hepta": 7, "octa": 8}

# A locant group (`2`, `2,3`, `4,4'`, `1beta`) immediately followed by `-` and a
# multiplying prefix that starts a substituent word. The prefix must be followed
# by a letter so `tri` in `triticum` or `di` in `dihydrogen`-less words is not
# mistaken for a multiplier on its own.
PATTERN = re.compile(
    r"(?P<locants>\d+[a-z']*(?:\s*,\s*\d+[a-z']*)*)-"
    r"(?P<mult>di|bis|tris|tri|tetrakis|tetra|penta|hexa|hepta|octa)"
    r"(?P<rest>[a-z]{3,})",
    re.I)

# A multiplied *substituent* buried later in the word, after an alkane stem:
# `1,5-Pentanediol` -> the `di` belongs to `diol`, not to `penta`. Written
# separately because the multiplier is not adjacent to the locant group.
SUFFIX_PATTERN = re.compile(
    r"(?P<locants>\d+[a-z']*(?:\s*,\s*\d+[a-z']*)*)-"
    r"(?P<stem>[a-z]*?)"
    r"(?P<mult>di|tri|tetra|penta|hexa)"
    r"(?P<suffix>ol|amine|amide|oic|one|al|thiol|carboxylic)\b",
    re.I)

# Stems where the "multiplier" is really an alkane chain length, not a count of
# substituents: `1-Pentanol`, `3-octanone`, `1-hexanol` are all well formed.
# Every alkane stem continues with `n` (pentan-, hexan-, octan-, heptan-).
ALKANE_STEM = re.compile(r"^n", re.I)


def scan_label(label: str) -> list[tuple[str, int, int]]:
    """Return (matched_text, locant_count, multiplier) for each malformed run."""
    out = []
    for m in PATTERN.finditer(label):
        mult = MULTIPLIER[m.group("mult").lower()]
        if ALKANE_STEM.match(m.group("rest")):
            continue
        n = len([x for x in re.split(r"\s*,\s*", m.group("locants")) if x])
        if n < mult:
            out.append((m.group(0), n, mult))
    for m in SUFFIX_PATTERN.finditer(label):
        mult = MULTIPLIER[m.group("mult").lower()]
        n = len([x for x in re.split(r"\s*,\s*", m.group("locants")) if x])
        if n < mult and not any(m.group(0) == t for t, _, _ in out):
            out.append((m.group(0), n, mult))
    return out


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--tsv", type=Path, help="Also write findings to this TSV.")
    ap.add_argument("--quiet", action="store_true")
    args = ap.parse_args(argv)

    rows = []
    for status in ("mapped", "unmapped"):
        for path in sorted((INGREDIENTS / status).glob("*.yaml")):
            rec = yaml.safe_load(path.read_text(encoding="utf-8", errors="replace")) or {}
            om = rec.get("ontology_mapping") or {}
            label = str(rec.get("preferred_term") or path.stem)
            hits = scan_label(label)
            if not hits:
                continue
            text, n, mult = hits[0]
            rows.append({
                "slug": path.stem, "status_dir": status,
                "identifier": rec.get("identifier") or "",
                "preferred_term": label,
                "malformed": text, "locants_found": n, "locants_needed": mult,
                "ontology_id": om.get("ontology_id") or "",
                "ontology_label": om.get("ontology_label") or "",
                "mapping_quality": om.get("mapping_quality") or "",
                # The ontology label usually still carries the full locant set,
                # so it is the best available guess at the original string.
                "label_has_full_locants": "yes" if not scan_label(
                    str(om.get("ontology_label") or "x")) else "no",
            })

    rows.sort(key=lambda r: (r["mapping_quality"] != "EXACT_MATCH", r["slug"]))
    if not args.quiet:
        print(f"labels with a truncated locant list: {len(rows)}\n")
        for r in rows:
            print(f"  {r['slug'][:44]:<44} {r['identifier'][:16]:<16} "
                  f"{r['malformed'][:26]:<26} needs {r['locants_needed']}, has "
                  f"{r['locants_found']}  -> {r['ontology_label'][:40]}")
    if args.tsv:
        args.tsv.parent.mkdir(parents=True, exist_ok=True)
        with args.tsv.open("w", newline="", encoding="utf-8") as fh:
            w = csv.DictWriter(fh, fieldnames=list(rows[0]) if rows else ["slug"],
                               delimiter="\t", lineterminator="\n")
            w.writeheader()
            w.writerows(rows)
        print(f"\nwrote {len(rows)} rows to {args.tsv}")
    return 1 if rows else 0


if __name__ == "__main__":
    sys.exit(main())
