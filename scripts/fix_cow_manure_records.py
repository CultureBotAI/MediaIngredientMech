#!/usr/bin/env python3
"""Resolve the two cow-manure records and the identity they contradict (#391).

    [mapped  ] Dry cow-manure  ENVO:00003031   MAPPED     BROAD_MATCH
    [unmapped] Cow manure      UNMAPPED_0367   UNMAPPED   NARROW_MATCH

Three problems in four lines.

**`Dry cow-manure` claims to BE animal manure while grading that it is not.**
Here the primary `identifier` is itself `ENVO:00003031`, so the record asserts
identity with *animal manure* — and it
simultaneously grades the mapping BROAD_MATCH, i.e. "the term is broader than
this record". Both cannot hold. §3 is explicit about the remedy: a record
narrower than every available term takes a registry mint and anchors to the
parent asymmetrically.

**The grades are inverses of each other** for the same relationship. Cow manure
cannot be both broader and narrower than animal manure. It is narrower.

**`Cow manure` is UNMAPPED yet carries a populated `ontology_mapping`.** An
unmapped record advertising a grounding is the shape that lets a consumer read a
mapping off a record which, by its own status, has none.

## No more specific ontology term exists

Checked before minting, because §3 step 1 outranks step 3. `cow manure` returns
nothing in ENVO, AGRO or FOODON. The nearest, `ENVO:01001116 "bovine dairy
liquid manure"`, is **liquid** — the opposite of this record — so it is not a
regrounding target.

## What this does

Merges the two into one record on a mint, anchored to ENVO:00003031:

* the surviving record keeps `Dry cow-manure`, the more informative label, and
  gains `Cow manure` as a RAW_TEXT synonym so the generic string still resolves;
* identifier becomes `kgmicrobe.ingredient:dry_cow-manure` (§3 step 3) — the
  local part matches the SSSOM subject slug, which is what Rule B1 checks;
* the ENVO row becomes `skos:narrowMatch`, matching the corpus convention for
  "MIM:X is a kind-of Y" that all 141 other asymmetric rows use — **not** the
  SKOS-literal direction, which is #390 and cannot be changed here without
  inverting those 141 downstream;
* a registry `skos:exactMatch` row is added, which Rule B1 requires of every
  narrowMatch subject.

Both records have **0 occurrences**, so nothing downstream depends on either
shape and the merge cannot lose usage data.

    python scripts/fix_cow_manure_records.py            # dry-run
    python scripts/fix_cow_manure_records.py --apply
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
UNMAPPED = ROOT / "data" / "curated" / "unmapped_ingredients.yaml"
SSSOM = ROOT / "mappings" / "ingredient_mappings.sssom.tsv"
DATE = "2026-08-18"
STAMP = f"{DATE}T00:00:00+00:00"
CURATOR = "fix_cow_manure_records"

KEEP = "Dry cow-manure"
FOLD = "Cow manure"
# Local part MUST equal the SSSOM subject slug lowercased -- Rule B1 checks
# `kgmicrobe.(ingredient|compound):<subject_id[4:].lower()>`. The subject is
# `MIM:Dry_Cow-manure`, so the slug keeps the HYPHEN: `dry_cow-manure`. A
# tidier `dry_cow_manure` fails B1 with "subject has no exactMatch row at
# all", because the registry row is matched on that local part, not by
# predicate alone.
MINT = "kgmicrobe.ingredient:dry_cow-manure"
PARENT = "ENVO:00003031"
PARENT_LABEL = "animal manure"


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--apply", action="store_true")
    args = ap.parse_args(argv)

    mapped = yaml.safe_load(MAPPED.read_text(encoding="utf-8")) or {}
    unmapped = yaml.safe_load(UNMAPPED.read_text(encoding="utf-8")) or {}
    keep = next((r for r in mapped.get("ingredients", [])
                 if str(r.get("preferred_term")) == KEEP), None)
    fold = next((r for r in unmapped.get("ingredients", [])
                 if str(r.get("preferred_term")) == FOLD), None)
    if keep is None:
        print(f"SKIP: {KEEP!r} not found in the mapped collection")
        return 0
    if str(keep.get("identifier")) != PARENT:
        print(f"SKIP: {KEEP!r} is on {keep.get('identifier')}, expected {PARENT} "
              f"— already changed")
        return 0

    occ_keep = (keep.get("occurrence_statistics") or {}).get("total_occurrences", 0)
    occ_fold = ((fold or {}).get("occurrence_statistics") or {}).get(
        "total_occurrences", 0)

    note = (
        f"Minted {MINT} and anchored to {PARENT} {PARENT_LABEL!r} as a "
        f"narrowMatch (#391). The record previously HELD {PARENT} as its "
        f"identifier while grading the mapping BROAD_MATCH — because its "
        f"identifier was the ontology term itself, it asserted identity with animal "
        f"manure and simultaneously graded that it was not that. §3 step 3 gives "
        f"a record narrower than every available term its own identity and "
        f"anchors it to the parent asymmetrically, which is what this does. Step "
        f"1 was checked first: 'cow manure' returns no term in ENVO, AGRO or "
        f"FOODON, and ENVO:01001116 'bovine dairy liquid manure' is LIQUID, the "
        f"opposite of this record. The predicate follows the corpus convention "
        f"used by all 141 other asymmetric rows rather than the SKOS-literal "
        f"direction; that discrepancy is #390 and cannot be changed here without "
        f"inverting those rows downstream.")

    keep["identifier"] = MINT
    keep["mapping_status"] = "MAPPED"
    om = keep.setdefault("ontology_mapping", {})
    om.update({"ontology_id": PARENT, "ontology_label": PARENT_LABEL,
               "ontology_source": "ENVO", "mapping_quality": "NARROW_MATCH"})
    om.setdefault("evidence", []).append({
        "evidence_type": "MANUAL_CURATION",
        "source": "MIM curation (#391)", "notes": note})
    keep.setdefault("curation_history", []).append({
        "timestamp": STAMP, "curator": CURATOR,
        "action": "MINTED_REGISTRY_IDENTIFIER", "changes": note,
        "llm_assisted": False})

    merged = False
    if fold is not None:
        syns = keep.setdefault("synonyms", [])
        if FOLD.lower() not in {str(s.get("synonym_text", "")).lower() for s in syns}:
            syns.append({"synonym_text": FOLD, "synonym_type": "RAW_TEXT",
                         "source": f"MERGED_FROM (#391)"})
        why = (
            f"Absorbed {FOLD!r} (#391). Both records name cow manure and both had "
            f"0 occurrences, so nothing downstream distinguished them and the "
            f"merge cannot lose usage data. They also disagreed with each other: "
            f"{KEEP!r} graded BROAD_MATCH against {PARENT} and {FOLD!r} graded "
            f"NARROW_MATCH against the same term, which are inverses — cow manure "
            f"cannot be both broader and narrower than animal manure. {FOLD!r} was "
            f"additionally UNMAPPED while carrying a populated ontology_mapping, so "
            f"it advertised a grounding its own status denied. The generic string "
            f"still resolves: it is kept as a RAW_TEXT synonym.")
        keep["curation_history"].append({
            "timestamp": STAMP, "curator": CURATOR, "action": "MERGED_FROM",
            "changes": f"{why} Occurrences {occ_keep} + {occ_fold} -> "
                       f"{occ_keep + occ_fold}.",
            "llm_assisted": False})
        occ = keep.setdefault("occurrence_statistics", {})
        occ["total_occurrences"] = occ_keep + occ_fold
        occ["media_count"] = ((keep.get("occurrence_statistics") or {}).get(
            "media_count", 0) or 0) + (((fold.get("occurrence_statistics") or {}).get(
                "media_count", 0)) or 0)
        unmapped["ingredients"] = [r for r in unmapped["ingredients"] if r is not fold]
        merged = True

    for coll, path in ((mapped, MAPPED), (unmapped, UNMAPPED)):
        recs = coll.get("ingredients") or []
        coll["total_count"] = len(recs)
        coll["mapped_count"] = sum(1 for r in recs if r.get("mapping_status") == "MAPPED")
        coll["unmapped_count"] = sum(1 for r in recs
                                     if r.get("mapping_status") == "UNMAPPED")

    lines = SSSOM.read_text(encoding="utf-8").splitlines(keepends=True)
    kept_lines, subject, dropped = [], None, 0
    for line in lines:
        cells = line.rstrip("\n").split("\t")
        if len(cells) >= 4 and cells[1] in (KEEP, FOLD):
            subject = subject or cells[0]
            dropped += 1
            continue
        kept_lines.append(line)
    subject = subject or "MIM:Dry_Cow-manure"
    hdr = next(i for i, l in enumerate(kept_lines) if l.startswith("subject_id"))
    ncols = len(kept_lines[hdr].rstrip("\n").split("\t"))
    prov = f"MIM:curation (#391)|MIM:curator={CURATOR}"
    rows = [
        # Rule B1: a narrowMatch subject must carry a registry exactMatch row
        # whose object local-part equals the subject slug, lowercased.
        [subject, KEEP, "skos:exactMatch", MINT, KEEP,
         "kgm:ingredient", "semapv:ManualMappingCuration", prov, DATE, "0.9",
         "", "", f"manual:{CURATOR}|{DATE}"],
        [subject, KEEP, "skos:narrowMatch", PARENT, PARENT_LABEL,
         "obo:envo.owl", "semapv:ManualMappingCuration", prov, DATE, "0.9",
         "", "", f"manual:{CURATOR}|{DATE}"],
    ]
    for row in reversed(rows):
        kept_lines.insert(hdr + 1, "\t".join((row + [""] * ncols)[:ncols]) + "\n")

    if args.apply:
        save_yaml(mapped, MAPPED)
        save_yaml(unmapped, UNMAPPED)
        SSSOM.write_text("".join(kept_lines), encoding="utf-8")

    print(f"{'APPLIED' if args.apply else 'DRY RUN (re-run with --apply)'}\n")
    print(f"  {KEEP!r}: {PARENT} -> {MINT}, narrowMatch to {PARENT}")
    print(f"  {FOLD!r}: {'merged in as a RAW_TEXT synonym' if merged else 'not found'}")
    print(f"  SSSOM: {dropped} row(s) replaced by 2 (registry exactMatch + narrowMatch)")
    print(f"  subject preserved: {subject}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
