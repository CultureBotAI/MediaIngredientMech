#!/usr/bin/env python3
"""Partition #322's cohort by whether the CHEBI target is really a class.

#322 reads "145 records map to structureless CHEBI class terms; 117 graded
EXACT_MATCH". Measured, that does not hold, and this script is how the numbers
were produced so they can be re-derived rather than taken on trust. The
conclusion was posted to the issue as prose; prose is not reproducible, which is
the failure mode `check_cited_artifacts` exists to catch in the sibling repo.

## What it measures

The cohort is `skos:exactMatch` rows whose CHEBI object has no
`molecular_formula` on the MIM record. **That signal does not identify
class-level overstatement**, which is what the issue assumes:

* Most targets are LEAVES. An absent formula usually means a polymer, dye or
  salt whose chemistry was never backfilled — not a grouping term.
* Where the target IS a class, the MIM record generally names that same class
  (`Amino Acid` -> `amino acid`). Class-to-class is legitimate; the defect the
  issue describes is a SPECIFIC SUBSTANCE equated with a class.

So it reports two axes, and the interesting cell is the intersection:
class-shaped target AND labels that disagree.

## Class-ness comes from the repo's own threshold

`DEFAULT_SUBCLASS_ALARM = 50` direct subclasses, set in #203 with its reasoning
recorded: `CHEBI:35358 sulfonamide` has 2976 and would have collapsed every
sulfonamide-resistance edge onto a functional-group node, while the intended
`CHEBI:87228 sulfonamide antibiotic` has 24. Reusing it rather than inventing a
second threshold that could drift from it.

**Absence is not zero.** `counts.get(id, 0)` returns 0 both for a real leaf and
for a term the local ChEBI build has never heard of, so "44 leaves" could
silently mean "44 terms I cannot see". The script checks membership separately
and refuses to report if any target is missing.

    python scripts/partition_class_term_cohort.py
    python scripts/partition_class_term_cohort.py --show-disagreements
"""
from __future__ import annotations

import argparse
import csv
import re
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "src"))
sys.path.insert(0, str(ROOT / "scripts"))
import yaml  # noqa: E402

MAPPED = ROOT / "data" / "curated" / "mapped_ingredients.yaml"
SSSOM = ROOT / "mappings" / "ingredient_mappings.sssom.tsv"


def _norm(s: str) -> str:
    """Compare labels ignoring case, punctuation and a trailing plural.

    Without the plural strip, `Polysaccharides` -> `polysaccharide` reads as a
    disagreement and lands in the defect bucket, which is how a one-row false
    positive got into the first pass of this analysis.
    """
    return re.sub(r"[^a-z0-9]", "", (s or "").lower()).rstrip("s")


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--alarm", type=int, default=None,
                    help="direct-subclass count above which a term is a class "
                         "(default: DEFAULT_SUBCLASS_ALARM from #203)")
    ap.add_argument("--show-disagreements", action="store_true",
                    help="list every row whose subject and object labels differ")
    args = ap.parse_args(argv)

    from promote_microbedecoder_reviewed import (  # noqa: E402
        DEFAULT_SUBCLASS_ALARM, _adapters, _specificity_index,
    )
    alarm = args.alarm or DEFAULT_SUBCLASS_ALARM

    recs = {str(r.get("preferred_term")): r
            for r in (yaml.safe_load(MAPPED.read_text(encoding="utf-8")) or {}
                      ).get("ingredients", [])}
    with SSSOM.open(encoding="utf-8") as fh:
        rows = list(csv.DictReader((l for l in fh if not l.startswith("#")),
                                   delimiter="\t"))

    cohort = [r for r in rows
              if r["predicate_id"] == "skos:exactMatch"
              and r["object_id"].startswith("CHEBI:")
              and not ((recs.get(r["subject_label"]) or {}).get(
                  "chemical_properties") or {}).get("molecular_formula")]

    counts, _ = _specificity_index(_adapters(("CHEBI",))).get("CHEBI", ({}, set()))
    if not counts:
        print("CANNOT MEASURE: no local ChEBI adapter, so every term would read "
              "as a leaf. Build the sqlite ChEBI cache first.")
        return 2

    # A term absent from the build is indistinguishable from a leaf by count
    # alone, and reporting it as a leaf would overstate the benign share.
    known = set(counts) | {r["object_id"] for r in rows
                           if counts.get(r["object_id"], 0) > 0}
    from sqlalchemy import text  # noqa: E402
    engine = getattr(_adapters(("CHEBI",))["CHEBI"], "engine", None)
    if engine is not None:
        with engine.connect() as conn:
            known |= {str(s) for (s,) in conn.execute(text(
                "SELECT DISTINCT subject FROM statements "
                "WHERE predicate='rdfs:label'"))}
    missing = [r["object_id"] for r in cohort if r["object_id"] not in known]
    if missing:
        print(f"CANNOT MEASURE: {len(missing)} target(s) absent from the local "
              f"ChEBI build, e.g. {missing[:3]}. They would read as leaves and "
              f"overstate how benign this cohort is.")
        return 2

    buckets, disagree = Counter(), []
    for r in cohort:
        n = counts.get(r["object_id"], 0)
        is_class = n >= alarm
        same = _norm(r["subject_label"]) == _norm(r["object_label"])
        buckets[(is_class, same)] += 1
        if not same:
            disagree.append((r["subject_label"], r["object_id"],
                             r["object_label"], n))

    print(f"cohort: {len(cohort)} exactMatch rows whose CHEBI target has no "
          f"molecular_formula\nclass threshold: >={alarm} direct subclasses "
          f"(#203)\n")
    shape = Counter()
    for r in cohort:
        n = counts.get(r["object_id"], 0)
        shape["leaf (0)" if n == 0 else "near-leaf (1-4)" if n < 5
              else f"grouping (5-{alarm - 1})" if n < alarm
              else f"CLASS (>={alarm})"] += 1
    for k in ("leaf (0)", "near-leaf (1-4)", f"grouping (5-{alarm - 1})",
              f"CLASS (>={alarm})"):
        print(f"  {shape.get(k, 0):>4}  {k}")

    print("\n  target is a class  x  labels agree")
    for (is_class, same), n in sorted(buckets.items(), key=lambda kv: -kv[1]):
        print(f"    {n:>4}  class={is_class!s:<5} labels_agree={same}")
    defect = buckets[(True, False)]
    print(f"\n  DEFECT SHAPE (class target AND labels disagree): {defect}")
    print("  Everything else is either a leaf, or a record naming the same "
          "class it maps to.")

    if args.show_disagreements:
        print(f"\n  all {len(disagree)} label disagreements — most are spelling "
              f"or synonym variants:")
        for s, o, ol, n in sorted(disagree, key=lambda t: -t[3]):
            print(f"    {s[:32]:<34}{o:<14}{ol[:26]:<28}subclasses={n}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
