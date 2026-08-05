"""Merge one MAPPED record into another (#226).

The missing third case. `promote_resolved_unmapped.py` does UNMAPPED -> CURIE;
`merge_unmapped_into_mapped.py` folds an UNMAPPED record into a mapped one;
`reground_mapped_record.py` moves a mapped record to a different term. None of
them can merge two records that are both MAPPED — which is every one of the 61
groups in `mappings/duplicate_identifier_baseline.tsv` (all `collection=mapped`),
and the reason `reground_mapped_record.py` has to refuse when the destination
CURIE is already held.

Semantics follow the repo's own, not invented ones. `audit_occurrence_stats.py`
documents `REJECTED_NONZERO` as "a REJECTED (merged) record still reporting
occurrences (counts should have been transferred to its representative)", so a
merge here:

  * transfers occurrence_statistics to the representative (summed -- each
    mention is a real mention, and media_count <= total_occurrences is preserved
    when both inputs satisfy it, which audit_occurrence_stats enforces)
  * carries the source's preferred_term and synonyms over as RAW_TEXT synonyms,
    and unions its role facets
  * tombstones the source as REJECTED with zeroed counts rather than deleting
    it, which is what `.claude/skills/merge-ingredients` step 4 asks for and
    what #220 wants
  * drops the source's SSSOM rows -- reconcile_sssom treats a row pointing at a
    REJECTED record as ORPHAN

The tombstone keeps its identifier. `audit_duplicate_identifiers.py` excludes
REJECTED records from a duplicate claim, so the group closes.

Dry-run by default; pass --apply.
"""

from __future__ import annotations

import argparse
import datetime as dt
import re
import sys
from pathlib import Path

import yaml

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
from mediaingredientmech.utils.yaml_handler import save_yaml  # noqa: E402

ROOT = Path(__file__).resolve().parents[1]
MAPPED = ROOT / "data" / "curated" / "mapped_ingredients.yaml"
SSSOM = ROOT / "mappings" / "ingredient_mappings.sssom.tsv"

ROLE_FIELDS = ("nutritional_roles", "functional_roles", "cellular_metabolic_roles")


def source_id(rec: dict) -> str | None:
    m = re.search(r"source_id=([^\s;)]+)", str(rec.get("notes") or ""))
    return m.group(1) if m else None


def one(recs: list[dict], curie: str, term: str | None, what: str) -> dict:
    hits = [r for r in recs if r["identifier"] == curie]
    if term:
        hits = [r for r in hits if r["preferred_term"] == term]
    if len(hits) != 1:
        raise SystemExit(
            f"{what} {curie}" + (f" (preferred_term={term!r})" if term else "")
            + f" matches {len(hits)} records, expected exactly 1. When a CURIE is held by "
              "several records, pass --from-term / --into-term to disambiguate.")
    return hits[0]


def drop_sssom_rows(subject_label: str, apply: bool) -> tuple[str, int]:
    lines = SSSOM.read_text().splitlines(keepends=True)
    header = next(i for i, ln in enumerate(lines) if ln.startswith("subject_id"))
    keep, dropped = [], 0
    for i, ln in enumerate(lines):
        if i > header and ln.split("\t")[1:2] == [subject_label]:
            dropped += 1
            continue
        keep.append(ln)
    if keep and not keep[-1].endswith("\n"):
        keep[-1] += "\n"
    return "".join(keep), dropped


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--from", dest="src_curie", required=True, help="record to absorb")
    ap.add_argument("--into", dest="dst_curie", required=True, help="surviving record")
    ap.add_argument("--from-term", help="disambiguate when the CURIE is held by several")
    ap.add_argument("--into-term")
    ap.add_argument("--reason", required=True)
    ap.add_argument("--curator", default="merge_mapped_records")
    ap.add_argument("--apply", action="store_true")
    args = ap.parse_args()

    doc = yaml.safe_load(MAPPED.read_text())
    recs = doc["ingredients"]
    src = one(recs, args.src_curie, args.from_term, "--from")
    dst = one(recs, args.dst_curie, args.into_term, "--into")
    if src is dst:
        raise SystemExit("--from and --into resolve to the same record")
    for label, r in (("--from", src), ("--into", dst)):
        if r.get("mapping_status") != "MAPPED":
            raise SystemExit(f"{label} is {r.get('mapping_status')}, not MAPPED")

    stamp = dt.datetime.now(dt.timezone.utc).isoformat()
    src_term = src["preferred_term"]

    # synonyms: the source's own name plus everything it answered to
    existing = {s.get("synonym_text") for s in dst.setdefault("synonyms", [])}
    carried = []
    for text in [src_term] + [s.get("synonym_text") for s in (src.get("synonyms") or [])]:
        if text and text not in existing and text != dst["preferred_term"]:
            existing.add(text)
            dst["synonyms"].append(
                {"synonym_text": text, "synonym_type": "RAW_TEXT", "source": "merged_record"})
            carried.append(text)

    # occurrence statistics transfer to the representative
    so = src.get("occurrence_statistics") or {}
    do = dst.setdefault("occurrence_statistics", {})
    moved = (so.get("total_occurrences") or 0, so.get("media_count") or 0)
    do["total_occurrences"] = (do.get("total_occurrences") or 0) + moved[0]
    do["media_count"] = (do.get("media_count") or 0) + moved[1]

    # role facets union
    roles_added = []
    for field in ROLE_FIELDS:
        extra = src.get(field) or []
        if not extra:
            continue
        have = dst.setdefault(field, [])
        for item in extra:
            if item not in have:
                have.append(item)
                roles_added.append(field)

    sid = source_id(src)
    dst.setdefault("curation_history", []).append({
        "timestamp": stamp, "curator": args.curator,
        "action": "MERGED_FROM_MAPPED_RECORD",
        "changes": (f"Absorbed {args.src_curie} {src_term!r}: {len(carried)} synonym(s), "
                    f"occurrences +{moved[0]}/{moved[1]}"
                    + (f", role facets from {', '.join(sorted(set(roles_added)))}"
                       if roles_added else "")
                    + f". {args.reason}" + (f" Source: {sid}." if sid else "")),
        "llm_assisted": True,
    })

    # tombstone rather than delete, and zero the counts now they have moved
    src["mapping_status"] = "REJECTED"
    src["occurrence_statistics"] = {"total_occurrences": 0, "media_count": 0}
    src.setdefault("curation_history", []).append({
        "timestamp": stamp, "curator": args.curator, "action": "MERGED_INTO",
        "changes": (f"Merged into {args.dst_curie} {dst['preferred_term']!r}; occurrences "
                    f"transferred. Tombstoned REJECTED, SSSOM rows dropped. {args.reason}"),
        "previous_status": "MAPPED", "new_status": "REJECTED", "llm_assisted": True,
    })

    doc["mapped_count"] = sum(1 for r in recs if r.get("mapping_status") == "MAPPED")
    doc["total_count"] = len(recs)
    doc["generation_date"] = stamp

    sssom_text, dropped = drop_sssom_rows(src_term, args.apply)

    print(f"{args.src_curie} {src_term!r}  ->  {args.dst_curie} {dst['preferred_term']!r}")
    print(f"  synonyms carried:   {len(carried)}")
    print(f"  occurrences moved:  {moved[0]} total / {moved[1]} media")
    print(f"  role facets:        {', '.join(sorted(set(roles_added))) or 'none'}")
    print(f"  SSSOM rows dropped: {dropped}")
    print(f"  source tombstoned REJECTED (identifier kept; excluded from duplicate claims)")
    print(f"  mapped_count -> {doc['mapped_count']}")

    if not args.apply:
        print("\nDRY RUN -- nothing written. Pass --apply to write.")
        return 0
    save_yaml(doc, MAPPED, validate=True, target_class="IngredientCollection")
    SSSOM.write_text(sssom_text)
    print("\nwrote data/curated/mapped_ingredients.yaml + SSSOM")
    print("next: just export-individual && just export-lists && just export-browser && just qc")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
