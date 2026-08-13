#!/usr/bin/env python3
"""Repoint salt records off the bare compositional class terms (#322).

Ten records carry a `narrowMatch` to `CHEBI:26714 sodium salt` or
`CHEBI:26218 potassium salt` — the *class of all sodium salts*. The mapping
keeps the counterion and discards the compound, so eight unrelated ingredients
(`D-Glucose-6-Phosphate sodium salt`, `TAPS sodium salt`, `Sulfamethazine sodium
salt`, …) all resolve to one node downstream.

The `identifier` is not the problem: every one is `cas:`-primary with its own
CAS, which is exactly MAPPING_SEMANTICS §3 step 2. What is wrong is the parent
that step 2 also requires — "the nearest ontology parent" is the compound the
label names, not a compositional category.

**Choosing the parent by the label sidesteps the open acid-vs-anion question**
(#319): where the label says "…Acid sodium salt" the parent is that acid, and
where it names a neutral compound the parent is that compound. No case here
needed the anion, except `2-oxobutyric acid sodium salt`, where ChEBI has the
anion and no acid term — the nearest available parent, noted on the record.

Three of the ten are NOT fixed here because **ChEBI has no term for the parent
at all**: `3'-sialyllactose sodium salt`, `6'-O-sialyllactose sodium salt` (no
`sialyllactose` term of any form) and `Sulfaquinoxaline sodium salt` (no
`sulfaquinoxaline` term). Leaving `sodium salt` on them would be no better, but
removing a required §3 row is a separate decision — tracked rather than guessed.

    python scripts/reground_compositional_classes.py            # dry-run
    python scripts/reground_compositional_classes.py --apply
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "src"))
import yaml  # noqa: E402

from mediaingredientmech.utils.yaml_handler import save_yaml  # noqa: E402

COLLECTION = ROOT / "data" / "curated" / "mapped_ingredients.yaml"
SSSOM = ROOT / "mappings" / "ingredient_mappings.sssom.tsv"
STAMP = "2026-08-13T00:00:00+00:00"
CURATOR = "reground_compositional_classes"
ISSUE = "#322"

GENERIC = {"CHEBI:26714": "sodium salt", "CHEBI:26218": "potassium salt"}

# identifier -> (new parent CURIE, its verbatim ChEBI label, why this parent)
REGROUND = {
    "cas:2013-26-5": ("CHEBI:16763", "2-oxobutanoate",
                      "ChEBI has no '2-oxobutanoic acid' term, so the anion is the "
                      "nearest available parent for the sodium salt"),
    "cas:91446-96-7": ("CHEBI:17426", "5-dehydro-D-gluconic acid",
                       "the acid the label names"),
    "cas:54010-71-8": ("CHEBI:14314", "D-glucose 6-phosphate",
                       "the compound the label names"),
    "cas:576-42-1": ("CHEBI:16002", "D-glucaric acid",
                     "saccharic acid is glucaric acid; the label specifies the D- form"),
    "cas:1219589-99-7": ("CHEBI:18064", "3-hydroxyisobutyric acid",
                         "the acid the label names; the term is stereo-unspecified, "
                         "which matches the label's DL-"),
    "cas:1981-58-4": ("CHEBI:102265", "sulfamethazine",
                      "the compound the label names"),
    "cas:91000-53-2": ("CHEBI:191055",
                       "N-[tris(hydroxymethyl)methyl]-3-aminopropanesulfonic acid",
                       "the systematic name of TAPS"),
}
# Left alone: no ChEBI term exists for the parent.
NO_PARENT = {
    "cas:128596-80-5": "3'-sialyllactose sodium salt",
    "cas:157574-76-0": "6'-O-sialyllactose sodium salt",
    "cas:967-80-6": "Sulfaquinoxaline sodium salt",
}


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--apply", action="store_true")
    args = ap.parse_args(argv)

    coll = yaml.safe_load(COLLECTION.read_text(encoding="utf-8", errors="replace")) or {}
    changed, skipped = [], []
    sssom_edits: dict[str, tuple[str, str]] = {}

    for rec in coll.get("ingredients", []):
        ident = str(rec.get("identifier") or "")
        spec = REGROUND.get(ident)
        if spec is None or rec.get("mapping_status") == "REJECTED":
            continue
        om = rec.get("ontology_mapping") or {}
        old = str(om.get("ontology_id") or "")
        if old not in GENERIC:
            skipped.append(f"{rec.get('preferred_term')}: parent is {old}, expected a "
                           f"compositional class — already fixed?")
            continue
        new_id, new_label, why = spec
        om["ontology_id"] = new_id
        om["ontology_label"] = new_label
        om["ontology_source"] = "CHEBI"
        om.setdefault("evidence", []).append({
            "evidence_type": "DATABASE_MATCH",
            "source": f"MIM curation ({ISSUE})",
            "notes": (f"narrowMatch parent {old} ({GENERIC[old]!r}) -> {new_id} "
                      f"({new_label!r}). The previous parent was the class of all "
                      f"{GENERIC[old]}s: it retained the counterion and discarded the "
                      f"compound, collapsing unrelated ingredients onto one node. "
                      f"Chosen because it is {why}. The record stays cas-primary per "
                      f"MAPPING_SEMANTICS §3 step 2; only the parent moves."),
        })
        rec.setdefault("curation_history", []).append({
            "timestamp": STAMP, "curator": CURATOR, "action": "REGROUNDED_PARENT_TERM",
            "changes": (f"ontology_mapping {old} {GENERIC[old]!r} -> {new_id} "
                        f"{new_label!r} ({ISSUE}); {why}."),
            "llm_assisted": False,
        })
        # Key on subject_label, not a derived subject_id. The MIM: subject is the
        # *sanitised filename* (`MIM:2-oxobutyric_Acid_Sodium_Salt`), which no
        # simple transform of preferred_term reproduces — deriving it matched 0
        # rows. subject_label is the preferred_term verbatim.
        sssom_edits[str(rec.get("preferred_term") or "")] = (new_id, new_label)
        changed.append(f"{str(rec.get('preferred_term'))[:40]:<40} {old} {GENERIC[old]:<15} "
                       f"-> {new_id} {new_label[:34]}")

    # Repoint the matching narrowMatch rows; subject_id and subject_label are unchanged.
    lines = SSSOM.read_text(encoding="utf-8").splitlines(keepends=True)
    rows = 0
    for i, line in enumerate(lines):
        cells = line.rstrip("\n").split("\t")
        if len(cells) < 5 or cells[1] not in sssom_edits:
            continue
        if cells[3] not in GENERIC:
            continue
        cells[3], cells[4] = sssom_edits[cells[1]]
        lines[i] = "\t".join(cells) + "\n"
        rows += 1

    if args.apply and changed:
        save_yaml(coll, COLLECTION)
        SSSOM.write_text("".join(lines), encoding="utf-8")

    print(f"{'APPLIED' if args.apply else 'DRY RUN (re-run with --apply)'} — "
          f"{len(changed)} record(s), {rows} SSSOM row(s)\n")
    for c in changed:
        print(f"  {c}")
    for s in skipped:
        print(f"  SKIPPED {s}")
    print(f"\n  Not fixed — ChEBI has no term for the parent ({len(NO_PARENT)}):")
    for ident, name in NO_PARENT.items():
        print(f"     {name:<40} ({ident})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
