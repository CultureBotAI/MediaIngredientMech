"""Report records that share one identifier, and gate against new ones (#218).

In MIM the record `identifier` IS the ontology CURIE, so two records with the
same identifier both assert they are that term. 61 such groups exist today.

They are not one problem with one fix. Collapsing them blindly destroys real
distinctions -- CHEBI:34683 is held by Na2HPO4 and five of its hydrates, and a
medium calling for Na2HPO4x7H2O is not calling for the anhydrous salt. Others
conflate materially different substances on one over-generic term
(cas:39280-21-2 covers rhamnogalacturonan from soy bean AND potato), which needs
distinct identifiers, not a merge.

So this does NOT auto-classify. Deciding what a group is, is a curation
judgement; a heuristic that gets it wrong launders a guess into a
machine-readable verdict. It emits the signals a curator needs and carries a
`disposition` column humans own.

`disposition` values come from MAPPING_SEMANTICS.md Section 3, which settles the
whole class in one rule -- one record per distinct substance, and a record's
identifier is the most specific stable id denoting THAT substance:

  MERGE_SAME_SUBSTANCE           the records describe one substance; fold one
                                 into the other. NOTE every baseline row is
                                 collection=mapped, so all 15 need MAPPED-to-
                                 MAPPED merge tooling, which does not exist yet
                                 (#226). merge_unmapped_into_mapped.py does not
                                 apply to any of them.
  NEEDS_OWN_ID                   one record is more specific than the shared
                                 term. It takes its own id -- exact ontology
                                 term if one exists, else cas:, else a minted
                                 kgmicrobe.compound: -- and narrowMatches the
                                 parent. reground_mapped_record.py does the
                                 move, BUT refuses when the destination is
                                 already held, which is true for the headline
                                 cases; those need reground + merge together.
  NEEDS_OWN_ID_MEMBER_UNDECIDED  as above, but which member surrenders the id
                                 has not been decided (e.g. MICRO:0000455
                                 'Algal' vs 'WC' trace elements).
  HYDRATE_FAMILY_UNREVIEWED      an anhydrous/hydrate family. NOT yet decided:
                                 some are merges because the shared term IS the
                                 hydrate (CHEBI:32150 is sodium thiosulfate
                                 pentahydrate), others need their own id. Each
                                 needs reading; do not bulk-convert.
  UNREVIEWED                     not yet decided

What it enforces (`--check`, exit 2):
  * an identifier duplicated that is not in the baseline
  * a baseline group that GREW
  * a baseline group whose MEMBERS CHANGED at constant size -- otherwise
    records can be swapped underneath a curator's verdict, and "these two
    spellings are safe to merge" silently comes to mean two different compounds
  * a baseline group that vanished -- normally good, but deleting the whole
    collection also makes every group vanish, so it must be an explicit
    baseline refresh rather than a silent pass

It also reports the inverse defect it cannot gate: one substance under two
identifiers (`MgSO4x7H2O` is both CHEBI:32599 and CHEBI:31795).
"""

from __future__ import annotations

import argparse
import collections
import csv
import hashlib
import re
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
COLLECTIONS = {
    "mapped": ROOT / "data" / "curated" / "mapped_ingredients.yaml",
    "unmapped": ROOT / "data" / "curated" / "unmapped_ingredients.yaml",
}
BASELINE = ROOT / "mappings" / "duplicate_identifier_baseline.tsv"
REPORT = ROOT / "reports" / "duplicate_identifiers.tsv"

FIELDS = ["identifier", "collection", "record_count", "members_fingerprint",
          "disposition", "same_after_folding", "hydrate_markers", "preferred_terms"]

# A REJECTED record is a tombstone, not a claim to be the term, so it does not
# make a duplicate. PENDING_REVIEW does count: an unreviewed proposal colliding
# with a live mapping is exactly what should be caught before it is promoted.
NOT_A_CLAIM = {"REJECTED"}

# Water of crystallisation. Covers 'x 7 H2O', 'x n H2O', '·7H2O', '7H2O',
# 'x H2O', and hydrate words with or without a multiplier prefix (hemipenta-,
# sesqui-, dodeca-). Deliberately NOT a bare /hydrate/ substring: that matches
# 'borohydrate' in 'b-Mannan borohydrate reduced carob seed', which is not a
# hydrate. \b anchoring plus an optional prefix group keeps 'carbohydrate',
# 'hydroxide', 'tetrahydrofuran' and 'dihydrogen' out.
HYDRATE = re.compile(
    r"[x·•]\s*(?:\d+|n)?\s*H2\s*O"
    r"|\d\s*H2\s*O"
    r"|(?<![a-z])(?:hemi|sesqui|mono|di|tri|tetra|penta|hexa|hepta|octa|nona|deca|dodeca)*"
    r"hydrate\b",
    re.IGNORECASE,
)


def fold(term: str) -> str:
    """Case/punctuation-insensitive form. Nothing chemical is inferred."""
    return re.sub(r"[^a-z0-9]+", "", str(term).lower())


def fingerprint(terms: list[str]) -> str:
    """Stable id for a group's membership, so a swap at constant size is seen."""
    return hashlib.sha256(chr(31).join(sorted(fold(t) for t in terms)).encode()).hexdigest()[:12]


class DataProblem(Exception):
    """Anything that should exit 2 with a message rather than a traceback."""


def load(path: Path) -> list[dict]:
    if not path.exists():
        raise DataProblem(f"missing collection: {path.relative_to(ROOT)}")
    try:
        doc = yaml.safe_load(path.read_text())
    except yaml.YAMLError as exc:
        raise DataProblem(f"unparseable YAML in {path.relative_to(ROOT)}: {exc}") from exc
    if not isinstance(doc, dict) or not isinstance(doc.get("ingredients"), list):
        raise DataProblem(f"{path.relative_to(ROOT)} has no 'ingredients' list")
    return doc["ingredients"]


def survey() -> tuple[list[dict], list[str]]:
    rows: list[dict] = []
    folded_to_ids: dict[str, set[str]] = collections.defaultdict(set)
    for name, path in COLLECTIONS.items():
        by_id: dict[str, list[dict]] = collections.defaultdict(list)
        for r in load(path):
            if not isinstance(r, dict) or "identifier" not in r:
                raise DataProblem(f"{path.relative_to(ROOT)}: record without an identifier")
            if r.get("mapping_status") in NOT_A_CLAIM:
                continue
            by_id[r["identifier"]].append(r)
            folded_to_ids[fold(r.get("preferred_term", ""))].add(str(r["identifier"]))
        for curie, recs in sorted(by_id.items()):
            if len(recs) < 2:
                continue
            terms = [str(r.get("preferred_term", "")) for r in recs]
            rows.append({
                "identifier": curie,
                "collection": name,
                "record_count": len(recs),
                "members_fingerprint": fingerprint(terms),
                "disposition": "UNREVIEWED",
                "same_after_folding": str(len({fold(t) for t in terms}) == 1).lower(),
                "hydrate_markers": str(sum(bool(HYDRATE.search(t)) for t in terms)),
                "preferred_terms": " | ".join(terms),
            })
    # the inverse defect: one name, several identifiers. Reported, not gated --
    # some are legitimately different terms for similar-looking names.
    collisions = [f"{name} -> {', '.join(sorted(ids))}"
                  for name, ids in sorted(folded_to_ids.items()) if len(ids) > 1 and name]
    return rows, collisions


def load_baseline() -> dict[tuple[str, str], dict]:
    if not BASELINE.exists():
        raise DataProblem(
            f"no baseline at {BASELINE.relative_to(ROOT)}; run --write-baseline once and commit it")
    with BASELINE.open() as fh:
        reader = csv.DictReader(fh, delimiter="\t")
        missing = set(FIELDS) - set(reader.fieldnames or [])
        if missing:
            raise DataProblem(
                f"{BASELINE.relative_to(ROOT)} is missing column(s): {', '.join(sorted(missing))}")
        out = {}
        for r in reader:
            try:
                int(r["record_count"])
            except (TypeError, ValueError):
                raise DataProblem(
                    f"{BASELINE.relative_to(ROOT)}: bad record_count "
                    f"{r['record_count']!r} for {r['identifier']}") from None
            out[(r["identifier"], r["collection"])] = r
    if not out:
        raise DataProblem(f"{BASELINE.relative_to(ROOT)} has no rows")
    return out


def write_tsv(path: Path, rows: list[dict]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=FIELDS, delimiter="\t")
        w.writeheader()
        w.writerows(rows)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    mode = ap.add_mutually_exclusive_group()
    mode.add_argument("--check", action="store_true",
                      help="exit 2 unless the duplicate set matches the baseline exactly")
    mode.add_argument("--write-baseline", action="store_true",
                      help="seed/refresh the baseline, keeping dispositions whose members "
                           "are unchanged")
    args = ap.parse_args()

    try:
        rows, collisions = survey()
        total = sum(r["record_count"] for r in rows)
        print(f"{len(rows)} identifier(s) held by more than one record "
              f"({total} records, {total - len(rows)} excess)")
        for name in COLLECTIONS:
            n = [r for r in rows if r["collection"] == name]
            if n:
                print(f"  {name:9} {len(n)} group(s)")
        print(f"  {sum(r['same_after_folding'] == 'true' for r in rows)} differ only "
              "by case/punctuation")
        print(f"  {sum(int(r['hydrate_markers']) > 0 for r in rows)} carry hydrate notation")
        if collisions:
            print(f"  {len(collisions)} name(s) map to MORE THAN ONE identifier "
                  "(inverse defect, reported not gated)")

        if args.write_baseline:
            try:
                prior = load_baseline()
            except DataProblem:
                prior = {}
            kept = reset = 0
            for r in rows:
                was = prior.get((r["identifier"], r["collection"]))
                if not was or was.get("disposition", "UNREVIEWED") == "UNREVIEWED":
                    continue
                if was.get("members_fingerprint") == r["members_fingerprint"]:
                    r["disposition"] = was["disposition"]
                    kept += 1
                else:
                    # the records this verdict was about are not the records here
                    r["disposition"] = "UNREVIEWED"
                    reset += 1
            write_tsv(BASELINE, rows)
            print(f"\nwrote {BASELINE.relative_to(ROOT)} "
                  f"({kept} disposition(s) kept, {reset} reset — membership changed)")
            return 0

        write_tsv(REPORT, rows)
        print(f"\nreport: {REPORT.relative_to(ROOT)}")
        for c in collisions[:10]:
            print(f"    same name, different identifiers: {c}")

        if not args.check:
            return 0

        known = load_baseline()
        now = {(r["identifier"], r["collection"]): r for r in rows}

        new = sorted(k for k in now if k not in known)
        grew = sorted(k for k in now if k in known
                      and now[k]["record_count"] > int(known[k]["record_count"]))
        swapped = sorted(k for k in now if k in known
                         and now[k]["record_count"] == int(known[k]["record_count"])
                         and now[k]["members_fingerprint"] != known[k].get("members_fingerprint"))
        gone = sorted(k for k in known if k not in now)

        if not (new or grew or swapped or gone):
            print("\nOK: duplicate identifiers match the tracked baseline exactly.")
            return 0

        print("\nERROR: the duplicate-identifier set does not match the baseline")
        for k in new:
            print(f"  NEW      {k[0]} ({k[1]}) held by {now[k]['record_count']} records")
        for k in grew:
            print(f"  GREW     {k[0]} ({k[1]}) "
                  f"{known[k]['record_count']} -> {now[k]['record_count']} records")
        for k in swapped:
            print(f"  SWAPPED  {k[0]} ({k[1]}) same count, different records — "
                  f"baseline disposition {known[k]['disposition']!r} no longer applies")
            print(f"           was: {known[k]['preferred_terms']}")
            print(f"           now: {now[k]['preferred_terms']}")
        for k in gone:
            print(f"  GONE     {k[0]} ({k[1]}) no longer duplicated")
        if gone and not (new or grew or swapped):
            print("\nGONE entries are usually progress — but losing records wholesale looks "
                  "identical here, so refresh the baseline deliberately rather than letting "
                  "this pass silently.")
        print("\nTwo records sharing an identifier both claim to BE that term. Merge them, "
              "give one a distinct identifier, or refresh the baseline deliberately:\n"
              "  uv run python scripts/audit_duplicate_identifiers.py --write-baseline")
        return 2

    except DataProblem as exc:
        print(f"\nERROR: {exc}")
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
