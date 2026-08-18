#!/usr/bin/env python3
"""Move `Carboxymethyl cellulose` off the SODIUM SALT term (#322).

The record names plain carboxymethyl cellulose and is grounded to
`CHEBI:234035 "carboxymethylcellulose sodium salt"` — a different substance, and
one MIM already has a separate record for:

    Carboxymethyl cellulose                 CHEBI:234035  carboxymethylcellulose sodium salt
    Carboxymethyl cellulose (sodium salt)   FOODON:03460374

So the generic record holds the salt's term while the salt record holds a FOODON
term. The two are crossed.

`CHEBI:85146 "carboxymethylcellulose"` is the plain form — *"A polysaccharide
derivative that is cellulose in which carboxymethyl groups are bound to some of
the hydroxyl groups of the glucopyranose monomers"* — and it lists **"Carboxymethyl
cellulose"** among its synonyms, which is this record's label exactly. It is held
by no other record.

Under kg-microbe's consumption rules a symmetric row overwrites the ontology
term's canonical name, so the old row also renamed the *sodium salt* term to the
generic name. Regrounding fixes the identity claim and the rename together.

## Why this is the only row fixed here

This is the one genuine defect found in #322's 119-row cohort. The cohort is
`exactMatch` rows whose CHEBI target carries no molecular formula, and that
signal turns out not to identify class-level overstatement:

* 90 of 119 targets have **fewer than 5** direct subclasses — leaves, not classes.
  The absent formula reflects polymers, dyes and salts whose chemistry was never
  backfilled, not a grouping term.
* Where the target IS a class (>=50 subclasses), the MIM record names **that same
  class** in every case: `Amino Acid`->`amino acid`, `Bile Acid`->`bile acid`,
  `Lactone`->`lactone`, `Polysaccharides`->`polysaccharide`. Class-to-class is
  legitimate.
* Of the 16 rows whose labels genuinely differ, all but this one are spelling or
  synonym variants: `Gelatine`->`gelatin`, `MgCO3`->`magnesium carbonate`,
  `HEPES`->its systematic name, `Dihydrocelastrol`->`triptohypol C` (which lists
  `dihydrocelastrol` as a synonym).

Not left alone but noted: `Carboxymethyl cellulose (sodium salt)` sits on
FOODON:03460374 while `CHEBI:753907 "carboxymethylcellulose sodium"` exists.
Moving it is a separate decision about FOODON-vs-CHEBI for salts, and #330
already has that record open on a different question.

    python scripts/reground_carboxymethyl_cellulose.py            # dry-run
    python scripts/reground_carboxymethyl_cellulose.py --apply
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "src"))
import yaml  # noqa: E402

from mediaingredientmech.utils.yaml_handler import save_yaml  # noqa: E402

MAPPED = ROOT / "data" / "curated" / "mapped_ingredients.yaml"
SSSOM = ROOT / "mappings" / "ingredient_mappings.sssom.tsv"
DATE = "2026-08-18"
STAMP = f"{DATE}T00:00:00+00:00"
CURATOR = "reground_carboxymethyl_cellulose"

LABEL = "Carboxymethyl cellulose"
OLD_TERM = "CHEBI:234035"
NEW_TERM = "CHEBI:85146"
NEW_LABEL = "carboxymethylcellulose"


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--apply", action="store_true")
    args = ap.parse_args(argv)

    mapped = yaml.safe_load(MAPPED.read_text(encoding="utf-8")) or {}
    records = mapped.get("ingredients") or []
    rec = next((r for r in records if str(r.get("preferred_term")) == LABEL), None)
    if rec is None:
        print(f"SKIP: no record {LABEL!r}")
        return 0
    if str(rec.get("identifier")) != OLD_TERM:
        print(f"SKIP: {LABEL!r} is on {rec.get('identifier')}, expected {OLD_TERM}")
        return 0
    if any(str(r.get("identifier")) == NEW_TERM for r in records if r is not rec):
        print(f"SKIP: {NEW_TERM} already held")
        return 0

    note = (
        f"Regrounded {OLD_TERM} 'carboxymethylcellulose sodium salt' -> {NEW_TERM} "
        f"{NEW_LABEL!r} (#322). The record names plain carboxymethyl cellulose; the "
        f"old term is the SODIUM SALT, a different substance that MIM already has a "
        f"separate record for ('Carboxymethyl cellulose (sodium salt)', "
        f"FOODON:03460374) — the two were crossed. CHEBI:85146 is the plain form "
        f"and lists 'Carboxymethyl cellulose' among its synonyms, i.e. this "
        f"record's label exactly. It also matters downstream: kg-microbe overwrites "
        f"an ontology term's canonical name from a symmetric row, so the old "
        f"mapping was renaming the sodium-salt term to the generic name as well as "
        f"asserting the wrong identity.")

    om = rec.setdefault("ontology_mapping", {})
    rec["identifier"] = NEW_TERM
    om.update({"ontology_id": NEW_TERM, "ontology_label": NEW_LABEL,
               "ontology_source": "CHEBI", "mapping_quality": "SYNONYM_MATCH"})
    om.setdefault("evidence", []).append({
        "evidence_type": "MANUAL_CURATION",
        "source": "MIM curation (#322)", "notes": note})
    rec.setdefault("curation_history", []).append({
        "timestamp": STAMP, "curator": CURATOR,
        "action": "REGROUNDED_OFF_SALT_TERM",
        "changes": note, "llm_assisted": False})

    lines = SSSOM.read_text(encoding="utf-8").splitlines(keepends=True)
    kept, subject, dropped = [], None, 0
    for line in lines:
        cells = line.rstrip("\n").split("\t")
        if len(cells) >= 4 and cells[1] == LABEL and cells[3] == OLD_TERM:
            subject = subject or cells[0]     # reuse the existing MIM: subject
            dropped += 1
            continue
        kept.append(line)
    hdr = next(i for i, l in enumerate(kept) if l.startswith("subject_id"))
    ncols = len(kept[hdr].rstrip("\n").split("\t"))
    row = [subject or f"MIM:{LABEL.replace(' ', '_')}", LABEL, "skos:exactMatch",
           NEW_TERM, NEW_LABEL, "obo:chebi.owl", "semapv:ManualMappingCuration",
           f"MIM:curation (#322)|MIM:curator={CURATOR}", DATE, "0.95", "", "",
           f"manual:{CURATOR}|{DATE}"]
    kept.insert(hdr + 1, "\t".join((row + [""] * ncols)[:ncols]) + "\n")

    if args.apply:
        save_yaml(mapped, MAPPED)
        SSSOM.write_text("".join(kept), encoding="utf-8")

    print(f"{'APPLIED' if args.apply else 'DRY RUN (re-run with --apply)'}\n")
    print(f"  {LABEL!r}")
    print(f"     {OLD_TERM} 'carboxymethylcellulose sodium salt'")
    print(f"  -> {NEW_TERM} {NEW_LABEL!r}")
    print(f"     {dropped} SSSOM row(s) replaced, subject preserved")
    return 0


if __name__ == "__main__":
    sys.exit(main())
