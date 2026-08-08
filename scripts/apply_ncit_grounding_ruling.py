#!/usr/bin/env python3
"""Record the curator ruling that settles the five build-displaced antibiotics.

## What was undecided

During the microbedecoder residual work, five records whose exact ChEBI term
sits above the local semsql build's range (#197/#207/#249) were grounded to a
term this repo *can* validate instead:

    Carbomycin        CHEBI:756054 -> NCIT:C166659
    Colistin_Sulfate  CHEBI:759883 -> NCIT:C386
    Lysostaphin       CHEBI:753395 -> NCIT:C166895
    Polymyxin_B       CHEBI:759086 -> NCIT:C61894
    Gentamicin        CHEBI:759884 -> CHEBI:17833  (gentamycin, SYNONYM_MATCH)

Those groundings were correct but their STATUS was ambiguous: two records said
in as many words that the displaced ChEBI id was "the exact term" and that the
record "should move back to it once the build carries it". Read that way, all
five were stopgaps waiting on an upstream event — and all five accessions do
exist in kg-microbe's own ChEBI 253, so a future curator syncing against the
consumer's ontology had a standing invitation to "restore" them.

## The ruling (curator, 2026-08-07)

**NCIT is correct.** These are final groundings, not placeholders. A term the
repo can resolve and label-check is a better published mapping than one it can
only take on trust from OLS4, and that judgement does not expire when the build
catches up.

Gentamicin stays on CHEBI:17833 for the same reason and one more: it resolves,
so MIM's own source preference (CHEBI ranks above NCIT — see
`curie.py::PREFIX_RANK`) already selects it. The four NCIT groundings are that
same preference order working, not an exception to it: CHEBI simply had nothing
validatable to offer.

What this script does is make the ruling *legible on the records themselves*, so
the next curator reads a decision rather than an unfinished task.

Idempotent: re-running adds nothing. Writes the collection
(`data/curated/mapped_ingredients.yaml`), which is the source of truth —
`just export-individual` then projects it onto `data/ingredients/`. Editing the
per-record files directly is the #148 trap: the next export silently reverts it.

Usage:
    python scripts/apply_ncit_grounding_ruling.py --dry-run
    python scripts/apply_ncit_grounding_ruling.py --only Lysostaphin   # canary
    python scripts/apply_ncit_grounding_ruling.py --apply
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "src"))

from mediaingredientmech.utils.yaml_handler import load_yaml, save_yaml  # noqa: E402

COLLECTION = REPO_ROOT / "data" / "curated" / "mapped_ingredients.yaml"

CURATOR = "curator_ruling_2026_08_07"
ACTION = "CURATOR_RULING"
# Fixed, not `now()`: the ruling has a date, and a re-run must not mint a new
# event that differs only by timestamp (which would defeat the idempotence check).
TIMESTAMP = "2026-08-07T00:00:00+00:00"

_SHARED = (
    "Curator ruling (#207): this grounding is FINAL, not a stopgap. "
    "{displaced} is a valid live ChEBI accession that is absent from the local "
    "semsql build (252 vs ChEBI 253), and it does exist in kg-microbe's own "
    "ChEBI — so a future sync against the consumer's ontology may look like an "
    "invitation to restore it. It is not. A term this repo can resolve and "
    "label-check is the better published mapping, and that judgement does not "
    "expire when the build catches up. Do not re-ground to {displaced} without "
    "a new curator decision."
)

# preferred_term -> (current id, displaced ChEBI id, per-record rationale)
RULINGS = {
    "Carbomycin": (
        "NCIT:C166659", "CHEBI:756054",
        "NCIT:C166659 'Carbomycin' is an exact label match and resolves locally.",
    ),
    "Colistin Sulfate": (
        "NCIT:C386", "CHEBI:759883",
        "NCIT:C386 'Colistin Sulfate' is an exact label match and resolves locally.",
    ),
    "Lysostaphin": (
        "NCIT:C166895", "CHEBI:753395",
        "NCIT:C166895 'Lysostaphin' is an exact label match and resolves locally.",
    ),
    "Polymyxin B": (
        "NCIT:C61894", "CHEBI:759086",
        "NCIT:C61894 'Polymyxin B' is an exact label match and resolves locally.",
    ),
    "Gentamicin": (
        "CHEBI:17833", "CHEBI:759884",
        "Supersedes the deferred intent recorded by `issue_213_premise_correction`, "
        "which said this record 'should move back to [CHEBI:759884] once the build "
        "carries it'. It should not. CHEBI:17833 'gentamycin' resolves, is the same "
        "aminoglycoside (an orthographic variant, hence SYNONYM_MATCH), and CHEBI "
        "already outranks NCIT in this repo's source preference "
        "(curie.py::PREFIX_RANK), so the ordinary rule selects it.",
    ),
}


def already_ruled(record: dict) -> bool:
    return any(
        (e or {}).get("curator") == CURATOR
        for e in (record.get("curation_history") or [])
    )


def build_event(displaced: str, rationale: str) -> dict:
    return {
        "timestamp": TIMESTAMP,
        "curator": CURATOR,
        "action": ACTION,
        "changes": (
            "Ruling recorded; no mapping changed. " + rationale
        ),
        "new_status": "MAPPED",
        "llm_assisted": False,
        "notes": _SHARED.format(displaced=displaced),
    }


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    mode = ap.add_mutually_exclusive_group(required=True)
    mode.add_argument("--dry-run", action="store_true",
                      help="Report what would change; touch nothing.")
    mode.add_argument("--apply", action="store_true")
    ap.add_argument("--only", metavar="PREFERRED_TERM", default=None,
                    help="Act on a single record — run one as a canary first.")
    args = ap.parse_args(argv)

    data = load_yaml(COLLECTION)
    records = data["ingredients"]

    targets = dict(RULINGS)
    if args.only:
        if args.only not in targets:
            ap.error(f"--only {args.only!r} is not one of: {', '.join(sorted(RULINGS))}")
        targets = {args.only: RULINGS[args.only]}

    changed = skipped = 0
    seen: set[str] = set()
    for rec in records:
        term = rec.get("preferred_term")
        if term not in targets:
            continue
        seen.add(term)
        current, displaced, rationale = targets[term]
        actual = (rec.get("ontology_mapping") or {}).get("ontology_id")
        if actual != current:
            # The ruling names the grounding it is ruling ON. If the record has
            # moved since, the ruling may no longer apply — refuse rather than
            # staple a decision onto a mapping nobody ruled on.
            print(f"REFUSED {term}: expected {current}, record holds {actual}")
            return 2
        if already_ruled(rec):
            print(f"  skip  {term:18} ruling already recorded")
            skipped += 1
            continue
        print(f"  {'would add' if args.dry_run else 'add'}   {term:18} "
              f"{current:14} (displaced {displaced})")
        if args.apply:
            rec.setdefault("curation_history", []).append(
                build_event(displaced, rationale))
        changed += 1

    missing = set(targets) - seen
    if missing:
        print(f"REFUSED: not found in the collection: {', '.join(sorted(missing))}")
        return 2

    print(f"\n{changed} record(s) to update, {skipped} already ruled.")
    if args.apply and changed:
        save_yaml(data, COLLECTION, backup=True, validate=True,
                  target_class="IngredientCollection")
        print(f"Wrote {COLLECTION.relative_to(REPO_ROOT)} (schema-validated).")
        print("Next: `just export-individual` to project onto data/ingredients/.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
