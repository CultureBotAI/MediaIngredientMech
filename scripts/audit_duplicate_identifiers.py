"""Report mapped records that share one identifier, and stop new ones (#218).

In MIM the record `identifier` IS the ontology CURIE, so two mapped records with
the same identifier are two records asserting they are the same term. 61 such
groups exist today, covering 147 records.

They are not one problem with one fix. Collapsing them blindly destroys real
distinctions -- CHEBI:34683 is held by Na2HPO4 and five of its hydrates, and a
medium calling for Na2HPO4x7H2O is not calling for the anhydrous salt; the
formula weight differs. Others conflate materially different substances on one
over-generic term (cas:39280-21-2 covers rhamnogalacturonan from *soy bean* and
from *potato*; cas:84082-64-4 covers mucin Type II and Type III), which is a
data-integrity bug in the opposite direction: those need distinct identifiers,
not a merge.

So this deliberately does NOT auto-classify. Deciding whether a group is a name
variant, a hydrate family, or two different products is a curation judgement,
and a heuristic that gets it wrong is worse than none -- it launders a guess
into a machine-readable verdict. Instead it emits the signals a curator needs
and carries a `disposition` column in the baseline for humans to fill in.

The one thing it does enforce: `--check` exits 2 when a duplicate identifier
appears that is not already in the tracked baseline. The existing 61 are a
backlog to triage; nothing should silently add a 62nd.
"""

from __future__ import annotations

import argparse
import collections
import csv
import re
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
MAPPED = ROOT / "data" / "curated" / "mapped_ingredients.yaml"
BASELINE = ROOT / "mappings" / "duplicate_identifier_baseline.tsv"
REPORT = ROOT / "reports" / "duplicate_identifiers.tsv"

FIELDS = ["identifier", "record_count", "disposition", "same_after_folding",
          "hydrate_markers", "preferred_terms"]

# Explicit water-of-crystallisation notations only: 'x 7 H2O', '·7H2O', '7H2O',
# 'x H2O', and hydrate words carrying a Greek multiplier. NOT a bare /hydrate/ --
# that matches 'borohydrate' in 'b-Mannan borohydrate reduced carob seed', which
# is not a hydrate at all.
HYDRATE = re.compile(
    r"[x·•]\s*\d*\s*H2\s*O"
    r"|\d\s*H2\s*O"
    r"|\b(?:mono|di|tri|tetra|penta|hexa|hepta|octa|deca|anhydro)hydrate\b",
    re.IGNORECASE,
)


def fold(term: str) -> str:
    """Case/punctuation-insensitive form. Nothing chemical is inferred here."""
    return re.sub(r"[^a-z0-9]+", "", term.lower())


def groups() -> list[tuple[str, list[dict]]]:
    recs = yaml.safe_load(MAPPED.read_text())["ingredients"]
    by_id: dict[str, list[dict]] = collections.defaultdict(list)
    for r in recs:
        by_id[r["identifier"]].append(r)
    return sorted(((k, v) for k, v in by_id.items() if len(v) > 1))


def survey() -> list[dict]:
    rows = []
    for curie, recs in groups():
        terms = [r["preferred_term"] for r in recs]
        rows.append({
            "identifier": curie,
            "record_count": len(recs),
            "disposition": "UNREVIEWED",
            "same_after_folding": str(len({fold(t) for t in terms}) == 1).lower(),
            "hydrate_markers": str(sum(bool(HYDRATE.search(t)) for t in terms)),
            "preferred_terms": " | ".join(terms),
        })
    return rows


def load_baseline() -> dict[str, dict]:
    if not BASELINE.exists():
        return {}
    with BASELINE.open() as fh:
        return {r["identifier"]: r for r in csv.DictReader(fh, delimiter="\t")}


def write_tsv(path: Path, rows: list[dict]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=FIELDS, delimiter="\t")
        w.writeheader()
        w.writerows(rows)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--check", action="store_true",
                    help="exit 2 if a duplicate identifier is not in the baseline")
    ap.add_argument("--write-baseline", action="store_true",
                    help="seed/refresh the baseline, preserving curator dispositions")
    args = ap.parse_args()

    rows = survey()
    total = sum(r["record_count"] for r in rows)
    print(f"{len(rows)} identifier(s) held by more than one mapped record "
          f"({total} records, {total - len(rows)} excess)")
    folded = sum(r["same_after_folding"] == "true" for r in rows)
    hydr = sum(int(r["hydrate_markers"]) > 0 for r in rows)
    print(f"  {folded} differ only by case/punctuation")
    print(f"  {hydr} contain an explicit hydrate notation in at least one term")

    if args.write_baseline:
        prior = load_baseline()
        for r in rows:  # never clobber a curator's decision
            was = prior.get(r["identifier"], {}).get("disposition")
            if was and was != "UNREVIEWED":
                r["disposition"] = was
        write_tsv(BASELINE, rows)
        print(f"\nwrote {BASELINE.relative_to(ROOT)}")
        return 0

    write_tsv(REPORT, rows)
    print(f"\nreport: {REPORT.relative_to(ROOT)}")
    if not args.check:
        return 0

    known = load_baseline()
    if not known:
        print(f"\nERROR: no baseline at {BASELINE.relative_to(ROOT)}; "
              "run --write-baseline once and commit it.")
        return 2

    now = {r["identifier"]: r["record_count"] for r in rows}
    new = sorted(k for k in now if k not in known)
    grew = sorted((k, int(known[k]["record_count"]), v)
                  for k, v in now.items()
                  if k in known and v > int(known[k]["record_count"]))
    gone = sorted(k for k in known if k not in now)

    if gone:
        print(f"\n{len(gone)} baseline entry/entries are no longer duplicated — "
              f"refresh the baseline: {', '.join(gone[:6])}")
    if new or grew:
        print("\nERROR: duplicate mapped identifiers not covered by the baseline")
        for k in new:
            print(f"  NEW   {k} held by {now[k]} records")
        for k, was, is_ in grew:
            print(f"  GREW  {k} {was} -> {is_} records")
        print("\nTwo mapped records sharing an identifier both claim to BE that term. "
              "Merge them, give one a distinct identifier, or — if this is knowingly "
              "added to the backlog — refresh the baseline deliberately.")
        return 2

    print("\nOK: no duplicate identifiers beyond the tracked baseline.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
