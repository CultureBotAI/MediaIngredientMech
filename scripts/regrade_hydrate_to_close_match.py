#!/usr/bin/env python3
"""Re-grade hydrate -> anhydrous mappings from narrowMatch to closeMatch (#342).

`skos:narrowMatch` asserts the subject is **narrower in meaning** than the object
— a subsumption claim. For a hydrate mapped to its anhydrous form, that claim is
false, and ChEBI says so itself:

    CHEBI:53503 cobalt chloride hexahydrate      subClassOf  CHEBI:35505 hydrate
    CHEBI:53542 nickel chloride hexahydrate      subClassOf  CHEBI:35505 hydrate
    CHEBI:91258 disodium hydrogenphosphate dihydrate  subClassOf  CHEBI:35505 hydrate

In none of these is the anhydrous compound an ancestor, even transitively. ChEBI
files hydrates under `CHEBI:35505 hydrate`, never under the anhydrous form, and
chemically that is right: `CoCl2·2H2O` is a distinct substance that *contains*
`CoCl2` rather than a specialization of it — different formula, mass, crystal
structure and CAS.

`skos:closeMatch` is the honest predicate: "sufficiently similar to be used
interchangeably in some applications", with no subsumption claim.

**Rule B1's reach changes, deliberately.** B1 requires a `kgmicrobe.*` registry
row only for narrow/broadMatch subjects, so these records leave its scope. The
minted identity rows are still correct and are **kept** — a hydrate that ChEBI
cannot name still needs its own identifier, which is what stops it collapsing
onto its anhydrous parent. B1 simply stops being the mechanism that enforces it.

Scope is every record whose label names a hydrate while its mapped term does not,
regardless of which cohort created it. That is **72 records**, not the 50 quoted
when #342 was filed: that figure counted only the `anchor_cas_hydrate_records`
and #341 cohorts, and the class is corpus-wide.

Records whose term is *itself* a hydrate are untouched — there the grade was
never asserting a hydration difference.

    python scripts/regrade_hydrate_to_close_match.py            # dry-run
    python scripts/regrade_hydrate_to_close_match.py --apply
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

COLLECTION = ROOT / "data" / "curated" / "mapped_ingredients.yaml"
SSSOM = ROOT / "mappings" / "ingredient_mappings.sssom.tsv"
STAMP = "2026-08-13T00:00:00+00:00"
CURATOR = "regrade_hydrate_to_close_match"
ISSUE = "#342"

# NOTE the absence of a leading \b before `hydrate`. `\bhydrate\b` requires a word
# boundary, which "monohydrate" / "tetrahydrate" / "hexahydrate" do not have — the
# preceding character is a letter. An earlier version of this pattern silently
# skipped 24 records spelled that way, matching only ` x N H2O`, `·NH2O` and the
# free-standing word "hydrate".
HYDRATE = re.compile(r"(\bx\s*\d*\s*h2o\b|·\s*\d*\s*h2o|hydrate\b)", re.IGNORECASE)


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )
    ap.add_argument("--apply", action="store_true")
    args = ap.parse_args(argv)

    coll = yaml.safe_load(COLLECTION.read_text(encoding="utf-8", errors="replace")) or {}
    changed: list[str] = []
    labels: set[str] = set()

    for rec in coll.get("ingredients", []):
        if rec.get("mapping_status") == "REJECTED":
            continue
        label = str(rec.get("preferred_term") or "")
        om = rec.get("ontology_mapping") or {}
        onto_label = str(om.get("ontology_label") or "")
        onto_id = str(om.get("ontology_id") or "")
        if om.get("mapping_quality") != "NARROW_MATCH":
            continue
        if not onto_id.startswith("CHEBI:"):
            continue
        # The record names a hydrate and the term does not: the grade is
        # asserting exactly the hydration difference ChEBI refuses to subsume.
        if not HYDRATE.search(label) or HYDRATE.search(onto_label):
            continue

        om["mapping_quality"] = "CLOSE_MATCH"
        om.setdefault("evidence", []).append({
            "evidence_type": "DATABASE_MATCH", "source": f"MIM curation ({ISSUE})",
            "notes": (
                f"mapping_quality NARROW_MATCH -> CLOSE_MATCH, predicate skos:narrowMatch "
                f"-> skos:closeMatch. narrowMatch asserts this record is *narrower in "
                f"meaning* than {onto_id} ({onto_label!r}) — a subsumption ChEBI itself "
                f"denies: it files hydrates under CHEBI:35505 'hydrate', never under the "
                f"anhydrous compound, which is not an ancestor even transitively. A hydrate "
                f"is a distinct substance containing the anhydrous form, not a "
                f"specialization of it. closeMatch claims similarity without subsumption. "
                f"The ontology_id and the record's own identifier are unchanged."),
        })
        rec.setdefault("curation_history", []).append({
            "timestamp": STAMP, "curator": CURATOR, "action": "REGRADED_HYDRATE_TO_CLOSE_MATCH",
            "changes": (f"mapping_quality NARROW_MATCH -> CLOSE_MATCH ({ISSUE}); a hydrate is "
                        f"not subsumed by its anhydrous form, and ChEBI does not model it as "
                        f"such."),
            "llm_assisted": False,
        })
        labels.add(label)
        changed.append(f"{label[:40]:<41} -> {onto_id} {onto_label[:30]}")

    lines = SSSOM.read_text(encoding="utf-8").splitlines(keepends=True)
    rows = 0
    for i, line in enumerate(lines):
        cells = line.rstrip("\n").split("\t")
        if len(cells) < 5 or cells[1] not in labels:
            continue
        if cells[2] != "skos:narrowMatch" or not cells[3].startswith("CHEBI:"):
            continue
        cells[2] = "skos:closeMatch"
        lines[i] = "\t".join(cells) + "\n"
        rows += 1

    if args.apply and changed:
        save_yaml(coll, COLLECTION)
        SSSOM.write_text("".join(lines), encoding="utf-8")

    print(f"{'APPLIED' if args.apply else 'DRY RUN (re-run with --apply)'} — "
          f"{len(changed)} record(s), {rows} SSSOM row(s)\n")
    for c in changed[:20]:
        print(f"  {c}")
    if len(changed) > 20:
        print(f"  ... {len(changed) - 20} more")
    return 0


if __name__ == "__main__":
    sys.exit(main())
