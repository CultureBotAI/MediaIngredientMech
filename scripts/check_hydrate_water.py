#!/usr/bin/env python3
"""Report hydrate records whose formula omits the water, by element totals (#321).

Supersedes the ad-hoc string matching used to triage #321, which got the count
wrong in three separate ways:

1. **`\\bhydrate\\b` never matched "monohydrate".** There is no word boundary
   before "hydrate" when the preceding character is a letter, so every record
   spelled with a multiplier prefix — monohydrate, tetrahydrate, hexahydrate —
   was invisible. 24 records were silently skipped.
2. **"borohydrate" is not a hydrate.** It ends in `-hydrate` by spelling alone.
3. **A combined formula masks the water.** Asking whether a formula *contains
   the string* `H2O` calls `Gly-Gln monohydrate` (`C7H15N3O5`) defective, when
   that value is the monohydrate — `C7H13N3O4` plus one water, written combined
   rather than as `.H2O`. Ten records are wrong for this reason alone.

So this compares **element totals**: parse the record's formula and its mapped
term's, and ask whether the record equals the term plus *n* waters, where *n* is
the stoichiometry the label states. That is immune to notation.

Three outcomes per record:

* ``ok``       — totals equal the term's plus n·H2O, however the formula is written
* ``missing``  — totals equal the term's exactly, and the term is not itself a
                 hydrate, so the record inherited the anhydrous value
* ``unknown``  — no stated *n*, no term formula, or the totals match neither

`unknown` is reported, never guessed. A record whose label says "hydrate" with no
number cannot be checked this way, and inventing a coefficient would put a
fabricated mass into a published field.

    python scripts/check_hydrate_water.py             # summary
    python scripts/check_hydrate_water.py --list      # every record
    python scripts/check_hydrate_water.py --check     # exit 1 if any are missing
"""
from __future__ import annotations

import argparse
import collections
import re
import sqlite3
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "src"))
import yaml  # noqa: E402

COLLECTION = ROOT / "data" / "curated" / "mapped_ingredients.yaml"
CHEBI_DB = Path.home() / ".data" / "oaklib" / "chebi.db"
FORMULA_PRED = "chemrof:generalized_empirical_formula"

MULTIPLIER = {"mono": 1, "di": 2, "tri": 3, "tetra": 4, "penta": 5, "hexa": 6,
              "hepta": 7, "octa": 8, "nona": 9, "deca": 10, "dodeca": 12}
# No leading \b: "monohydrate" has no word boundary before "hydrate".
HYDRATE_LABEL = re.compile(r"(\bx\s*\d*\s*h2o\b|·\s*\d*\s*h2o|hydrate\b)", re.IGNORECASE)
HYDRATION_WORD = re.compile(
    r"\b(mono|di|tri|tetra|penta|hexa|hepta|octa|nona|deca|dodeca)hydrate\b", re.IGNORECASE)
HYDRATION_N = re.compile(r"(?:x|·)\s*(\d*)\s*H2O", re.IGNORECASE)
NOT_A_HYDRATE = re.compile(r"borohydrate", re.IGNORECASE)
ELEMENT = re.compile(r"([A-Z][a-z]?)(\d*)")


def parse_formula(formula: object) -> collections.Counter | None:
    """ChEBI dot-notation -> element counts. ``2Cl.Co.2H2O`` -> Cl2 Co1 H4 O2.

    Returns None for anything that is not a plain formula (SMILES, free text),
    so callers can treat it as unknown rather than mis-parsing it.
    """
    if not formula:
        return None
    text = str(formula).strip().replace("·", ".")
    if not re.fullmatch(r"[A-Za-z0-9.\s]+", text):
        return None
    total: collections.Counter = collections.Counter()
    for part in text.split("."):
        part = part.strip()
        if not part:
            continue
        lead = re.match(r"^(\d+)(.*)$", part)
        mult = int(lead.group(1)) if lead else 1
        body = lead.group(2) if lead else part
        counts: collections.Counter = collections.Counter()
        for element, digits in ELEMENT.findall(body):
            if element:
                counts[element] += int(digits or 1)
        for element in counts:
            total[element] += counts[element] * mult
    return total or None


def hydration_number(label: str) -> int | None:
    """Waters the label states, by either notation, or None if it states none."""
    m = HYDRATION_N.search(label)
    if m:
        return int(m.group(1) or 1)
    m = HYDRATION_WORD.search(label)
    return MULTIPLIER[m.group(1).lower()] if m else None


def classify(label: str, formula: object, term_formula: object,
             term_label: str) -> tuple[str, str]:
    """-> (ok|missing|unknown, reason)."""
    n = hydration_number(label)
    rec, term = parse_formula(formula), parse_formula(term_formula)
    if n is None:
        return "unknown", "label states no hydration number"
    if rec is None or term is None:
        return "unknown", "record or term formula is not parseable"
    expected = collections.Counter(term)
    expected.update({"H": 2 * n, "O": n})
    if rec == expected:
        return "ok", f"totals equal the term's plus {n} H2O"
    if rec == term:
        if HYDRATE_LABEL.search(term_label):
            return "ok", "term is itself the hydrate and the record matches it"
        return "missing", f"totals equal the anhydrous term's; {n} H2O unaccounted for"
    return "unknown", "totals match neither the term nor the term plus water"


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--list", action="store_true", help="print every record")
    ap.add_argument("--check", action="store_true", help="exit 1 if any are missing")
    ap.add_argument("--chebi-db", type=Path, default=CHEBI_DB)
    args = ap.parse_args(argv)

    if not args.chebi_db.exists():
        print(f"ERROR: ChEBI SQLite not found at {args.chebi_db}", file=sys.stderr)
        return 2
    conn = sqlite3.connect(f"file:{args.chebi_db}?mode=ro", uri=True)

    def term_formula(curie: str) -> str | None:
        row = conn.execute("SELECT value FROM statements WHERE subject=? AND predicate=?",
                           (curie, FORMULA_PRED)).fetchone()
        return row[0] if row else None

    coll = yaml.safe_load(COLLECTION.read_text(encoding="utf-8", errors="replace")) or {}
    buckets: dict[str, list[tuple[str, str]]] = {"ok": [], "missing": [], "unknown": []}

    for rec in coll.get("ingredients", []):
        if rec.get("mapping_status") == "REJECTED":
            continue
        label = str(rec.get("preferred_term") or "")
        if not HYDRATE_LABEL.search(label) or NOT_A_HYDRATE.search(label):
            continue
        cp = rec.get("chemical_properties") or {}
        if not cp.get("molecular_formula"):
            continue
        om = rec.get("ontology_mapping") or {}
        curie = str(om.get("ontology_id") or "")
        verdict, reason = classify(
            label, cp.get("molecular_formula"),
            term_formula(curie) if curie.startswith("CHEBI:") else None,
            str(om.get("ontology_label") or ""))
        buckets[verdict].append((label, reason))

    total = sum(len(v) for v in buckets.values())
    print(f"Hydrate-labelled records with a molecular_formula: {total}\n")
    print(f"  ok      {len(buckets['ok']):>4}  water accounted for, whatever the notation")
    print(f"  missing {len(buckets['missing']):>4}  formula is the anhydrous term's")
    print(f"  unknown {len(buckets['unknown']):>4}  not checkable — reported, never guessed")

    if args.list or args.check:
        for verdict in ("missing", "unknown") if args.check else ("missing", "unknown", "ok"):
            if not buckets[verdict]:
                continue
            print(f"\n  --- {verdict} ({len(buckets[verdict])}) ---")
            for label, reason in sorted(buckets[verdict]):
                print(f"     {label[:46]:<48} {reason}")

    if args.check and buckets["missing"]:
        print(f"\nFAIL: {len(buckets['missing'])} hydrate record(s) carry the anhydrous formula.")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
