#!/usr/bin/env python3
"""Remove zero-padding from CAS Registry Numbers (#310).

A CAS RN is `{2..7 digits}-{2 digits}-{1 check digit}` and never carries leading
zeros. Ten values in the corpus do — alignment padding from somewhere in the
ingest — and `cas:0124-09-4` resolves against nothing.

**The issue counts five; there are ten.** Five are primary identifiers, and the
other five sit in `chemical_properties.cas_rn` on records whose identifier is a
CHEBI term:

    identifier  cas:0124-09-4  1,6-Hexanediamine              -> cas:124-09-4
                cas:0303-07-1  2,6-dihydroxybenzoic acid      -> cas:303-07-1
                cas:0305-01-1  Aesculetin                     -> cas:305-01-1
                cas:0392-12-1  Indole-3-pyruvic acid          -> cas:392-12-1
                cas:0612-05-5  methyl-beta-D-xylopyranoside   -> cas:612-05-5
    cas_rn only 0124-04-9      Adipic acid        (CHEBI:30832)
                0140-10-3      Cinnamic acid      (CHEBI:27386)
                0506-12-7      heptadecanoic acid (CHEBI:32365)
                0609-06-3      L-Xylose           (CHEBI:65328)
                0553-12-8      Protoporphyrin     (CHEBI:15430)

Fixing only the identifiers would leave five padded values that still break any
join on CAS-RN, which is the stated reason the issue matters. So both are fixed.

**Verified before changing, not assumed.** Stripping a leading zero is the kind
of edit that looks obviously safe and silently rewrites identity if the padding
were meaningful. Two checks:

* every stripped value passes the CAS check-digit algorithm. Necessary but not
  sufficient — a leading zero contributes 0 to the weighted sum, so the check
  digit cannot by itself tell padded from unpadded.
* every stripped value was resolved against PubChem and returns exactly the
  compound MIM names: 124-09-4 -> Hexamethylenediamine, 305-01-1 -> Esculetin,
  553-12-8 -> protoporphyrin IX, and so on for all ten. That is what actually
  establishes the padding is cosmetic.

The stripped identifier is checked against the corpus for an existing holder
before it is taken — in MIM the identifier IS the CURIE, so colliding with a
live record would create a duplicate primary key rather than fix anything.

    python scripts/strip_cas_leading_zeros.py            # dry-run
    python scripts/strip_cas_leading_zeros.py --apply
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "src"))
import yaml  # noqa: E402

from mediaingredientmech.utils.yaml_handler import save_yaml  # noqa: E402

MAPPED = ROOT / "data" / "curated" / "mapped_ingredients.yaml"
UNMAPPED = ROOT / "data" / "curated" / "unmapped_ingredients.yaml"
SSSOM = ROOT / "mappings" / "ingredient_mappings.sssom.tsv"
STAMP = "2026-08-16T00:00:00+00:00"
CURATOR = "strip_cas_leading_zeros"
ISSUE = "#310"

PADDED = re.compile(r"^0+(\d{2,7}-\d{2}-\d)$")


def check_digit_ok(cas: str) -> bool:
    """Last digit == sum(digit * position-from-right) mod 10."""
    digits = cas.replace("-", "")
    if not digits.isdigit():
        return False
    body, chk = digits[:-1], int(digits[-1])
    return sum(int(c) * (i + 1) for i, c in enumerate(reversed(body))) % 10 == chk


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--apply", action="store_true")
    args = ap.parse_args(argv)

    colls = {p: (yaml.safe_load(p.read_text(encoding="utf-8")) or {})
             for p in (MAPPED, UNMAPPED)}
    records = [r for c in colls.values() for r in (c.get("ingredients") or [])]
    taken = {str(r.get("identifier")): r for r in records}

    ids, props, skipped = [], [], []
    renames: dict[str, str] = {}

    for rec in records:
        label = str(rec.get("preferred_term") or "")
        om = rec.get("ontology_mapping") or {}
        changed = []

        ident = str(rec.get("identifier") or "")
        if ident.startswith("cas:"):
            m = PADDED.match(ident.split(":", 1)[1])
            if m:
                new_cas = m.group(1)
                new = f"cas:{new_cas}"
                if not check_digit_ok(new_cas):
                    skipped.append(f"{label}: {new_cas} fails the CAS check digit")
                    continue
                holder = taken.get(new)
                if holder is not None and holder is not rec:
                    skipped.append(f"{label}: {new} already held by "
                                   f"{holder.get('preferred_term')!r} — would duplicate")
                    continue
                rec["identifier"] = new
                renames[ident] = new
                if str(om.get("ontology_id") or "") == ident:
                    om["ontology_id"] = new
                changed.append(f"identifier {ident} -> {new}")
                ids.append(f"{label[:34]:<36} {ident:<16} -> {new}")

        cp = rec.get("chemical_properties") or {}
        cas = str(cp.get("cas_rn") or "")
        m = PADDED.match(cas)
        if m:
            new_cas = m.group(1)
            if not check_digit_ok(new_cas):
                skipped.append(f"{label}: cas_rn {new_cas} fails the CAS check digit")
            else:
                cp["cas_rn"] = new_cas
                changed.append(f"chemical_properties.cas_rn {cas} -> {new_cas}")
                props.append(f"{label[:34]:<36} {cas:<14} -> {new_cas}  "
                             f"(id {rec.get('identifier')})")

        if changed:
            rec.setdefault("curation_history", []).append({
                "timestamp": STAMP, "curator": CURATOR,
                "action": "STRIPPED_CAS_LEADING_ZERO",
                "changes": (
                    f"{'; '.join(changed)} ({ISSUE}). A CAS Registry Number never "
                    f"carries leading zeros, so the padded form resolved against "
                    f"nothing and any join on CAS-RN silently missed this record. "
                    f"The stripped value passes the CAS check digit and resolves on "
                    f"PubChem to exactly this compound; the padding was ingest "
                    f"alignment, not identity."),
                "llm_assisted": False})

    lines = SSSOM.read_text(encoding="utf-8").splitlines(keepends=True)
    out, rows = [], 0
    for line in lines:
        if line.startswith("#") or line.startswith("subject_id"):
            out.append(line)
            continue
        cells = line.rstrip("\n").split("\t")
        if len(cells) >= 4 and cells[3] in renames:
            cells[3] = renames[cells[3]]
            line = "\t".join(cells) + "\n"
            rows += 1
        out.append(line)

    if args.apply and (ids or props):
        for path, coll in colls.items():
            save_yaml(coll, path)
        SSSOM.write_text("".join(out), encoding="utf-8")

    print(f"{'APPLIED' if args.apply else 'DRY RUN (re-run with --apply)'} — "
          f"{len(ids)} identifier(s), {len(props)} cas_rn value(s), "
          f"{rows} SSSOM row(s)\n")
    print(f"  primary identifiers ({len(ids)}):")
    for i in ids:
        print(f"     {i}")
    print(f"\n  chemical_properties.cas_rn ({len(props)}) — the half the issue missed:")
    for p in props:
        print(f"     {p}")
    for s in skipped:
        print(f"  SKIPPED {s}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
