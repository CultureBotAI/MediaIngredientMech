#!/usr/bin/env python3
"""Unmap the record `X`, which is grounded to a letter of the alphabet (#356).

`X` (101 occurrences) sits on `NCIT:C189218`, whose OLS definition reads, in
full:

    The 24th letter of the English alphabet.

It is graded `EXACT_MATCH`, and in the narrow sense that is true — the label and
the term label are both `X`. That is exactly how it got there: an `UNMAPPED_0256`
placeholder was resolved by normalising the label and finding an ontology term
with a matching string, with nothing checking that the result was a substance.

**What `X` actually is remains unknown, and this script does not guess.** The
plausible readings — a marker column read as an ingredient, a placeholder whose
referent was lost, or a genuine abbreviation from one source — are settled by
source archaeology in the CultureBot media, not by chemistry. That work is still
#356's.

**But the mapping should not stand while that happens.** Publishing a
growth-medium ingredient as a letter of the alphabet asserts something false, at
`EXACT_MATCH` confidence, on a record with 101 occurrences. Returning it to
UNMAPPED says "we do not know", which is both true and strictly better than what
is published today.

So: identifier -> a fresh `UNMAPPED_NNNN`, status -> UNMAPPED, the ontology
mapping removed, the SSSOM row dropped, and the record moved into
`unmapped_ingredients.yaml` (#370 — a status change that skips the move leaves
the record where the reconciler cannot see it). The former mapping is preserved
in `curation_history`, so nothing about how it got there is lost.

## The same-shaped records nearby, and why they are left alone

#356 suggests a guard: flag any `EXACT_MATCH` whose `preferred_term` is <= 3
characters and whose target carries no formula, SMILES, InChI or CAS. Run over
the corpus it returns four records:

    X     NCIT:C189218   occ 101   'X'      <- the 24th letter. Wrong.
    Pea   NCIT:C72056    occ   2   'Pea'    <- plausible; NCIT has no definition
    Rna   mesh:D012313   occ   0   'RNA'    <- correct; RNA is a polymer, so the
                                               absent formula is expected
    Fig   NCIT:C71971    occ   0   'Fig'    <- plausible; likewise undefined

One true positive in four. The rule is a good way to *find* this class of defect
once and a poor gate to run forever, so it is recorded here rather than wired
into CI: the absent-chemistry signal fires on every legitimate polymer and food
term, and a check that cries wolf three times out of four gets switched off.

    python scripts/demote_alphabet_letter_mapping.py            # dry-run
    python scripts/demote_alphabet_letter_mapping.py --apply
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
STAMP = "2026-08-17T00:00:00+00:00"
CURATOR = "demote_alphabet_letter_mapping"
ISSUE = "#356"

LABEL = "X"
EXPECT_TERM = "NCIT:C189218"


def next_unmapped_id(records: list[dict]) -> str:
    used = {int(m.group(1)) for r in records
            if (m := re.fullmatch(r"UNMAPPED_(\d+)", str(r.get("identifier") or "")))}
    return f"UNMAPPED_{max(used, default=0) + 1:04d}"


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--apply", action="store_true")
    args = ap.parse_args(argv)

    mapped = yaml.safe_load(MAPPED.read_text(encoding="utf-8")) or {}
    unmapped = yaml.safe_load(UNMAPPED.read_text(encoding="utf-8")) or {}
    everything = (mapped.get("ingredients") or []) + (unmapped.get("ingredients") or [])

    rec = next((r for r in (mapped.get("ingredients") or [])
                if str(r.get("preferred_term")) == LABEL), None)
    if rec is None:
        print(f"SKIP: no MAPPED record with preferred_term {LABEL!r}")
        return 0
    om = rec.get("ontology_mapping") or {}
    if str(om.get("ontology_id")) != EXPECT_TERM:
        print(f"SKIP: {LABEL!r} is on {om.get('ontology_id')}, expected "
              f"{EXPECT_TERM} — already changed, not re-applying")
        return 0

    new_id = next_unmapped_id(everything)
    old_id = str(rec.get("identifier"))
    occ = (rec.get("occurrence_statistics") or {}).get("total_occurrences", 0)

    note = (
        f"Unmapped from {EXPECT_TERM} ({ISSUE}). The term's definition is 'The "
        f"24th letter of the English alphabet' — it is not a substance, so this "
        f"record published a meaningless node at EXACT_MATCH confidence across "
        f"{occ} occurrences. The grade was not wrong about the STRING: the "
        f"record label and the term label are both 'X', which is how a "
        f"name-normalisation pass produced it from UNMAPPED_0256. Nothing in "
        f"that path checked the result was a chemical. What 'X' denotes is "
        f"still unknown and is deliberately not guessed here — it needs source "
        f"archaeology in the CultureBot media that use it. UNMAPPED states that "
        f"honestly; the previous mapping is retained in this history.")

    rec["identifier"] = new_id
    rec["mapping_status"] = "UNMAPPED"
    rec.pop("ontology_mapping", None)
    rec.setdefault("curation_history", []).append({
        "timestamp": STAMP, "curator": CURATOR,
        "action": "DEMOTED_NON_SUBSTANCE_MAPPING",
        "previous_status": "MAPPED", "new_status": "UNMAPPED",
        "changes": f"identifier {old_id} -> {new_id}; ontology_mapping removed. {note}",
        "llm_assisted": False})
    rec["notes"] = ((str(rec.get("notes") or "") + " ").strip() + " " + note).strip()

    # A status change that does not MOVE the record leaves it where
    # reconcile_sssom cannot see it (#370).
    mapped["ingredients"] = [r for r in mapped["ingredients"] if r is not rec]
    unmapped.setdefault("ingredients", []).insert(0, rec)
    for coll in (mapped, unmapped):
        recs = coll.get("ingredients") or []
        coll["total_count"] = len(recs)
        coll["mapped_count"] = sum(1 for r in recs if r.get("mapping_status") == "MAPPED")
        coll["unmapped_count"] = sum(1 for r in recs if r.get("mapping_status") == "UNMAPPED")

    lines = SSSOM.read_text(encoding="utf-8").splitlines(keepends=True)
    kept, dropped = [], 0
    for line in lines:
        cells = line.rstrip("\n").split("\t")
        if len(cells) >= 4 and cells[1] == LABEL and cells[3] == EXPECT_TERM:
            dropped += 1
            continue
        kept.append(line)

    if args.apply:
        save_yaml(mapped, MAPPED)
        save_yaml(unmapped, UNMAPPED)
        SSSOM.write_text("".join(kept), encoding="utf-8")

    print(f"{'APPLIED' if args.apply else 'DRY RUN (re-run with --apply)'}\n")
    print(f"  {LABEL!r}  {old_id} -> {new_id}   MAPPED -> UNMAPPED   "
          f"({occ} occurrences)")
    print(f"  ontology_mapping removed; {dropped} SSSOM row(s) dropped")
    print(f"  moved into unmapped_ingredients.yaml (#370)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
