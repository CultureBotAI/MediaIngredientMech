"""Fold an UNMAPPED record into the MAPPED record it duplicates.

`promote_resolved_unmapped.py` cannot do this: promoting would give the record
an identifier another record already holds, creating an unreviewed family and
an ambiguous record address -- the defect `just qc-duplicate-ids` gates (#218).
When research shows that a raw label is the same supplied substance as the
existing mapped record, the answer is a merge, not a second record.

What a merge does:
  * add the raw label to the target as a RAW_TEXT synonym
  * carry the source's upstream source_id (kgmicrobe.trait: or
    kgmicrobe.compound:) into the target's curation_history, since it lives only
    in free-text `notes` and the source record goes away (#220)
  * delete the source record and fix the collection counts
  * add NO SSSOM row -- the target already has one, and SSSOM subjects are
    preferred_terms of mapped records, never synonyms

Generalised from the one-off in #214, which was the first time this was needed.
Merging two MAPPED records is a different and harder problem (occurrence, role
and SSSOM-row reconciliation) -- see #226.

Input is a TSV with columns: source_term, target_curie, target_preferred_term,
rationale. `target_preferred_term` disambiguates a CURIE held by more than one
record; leave it blank when the CURIE is unique. Resolution is strict: an
ambiguous or missing target is an error, never a last-wins guess.

Dry-run by default; pass --apply to write.
"""

from __future__ import annotations

import argparse
import csv
import datetime as dt
import re
import sys
from pathlib import Path

import yaml

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
from mediaingredientmech.utils.yaml_handler import save_yaml  # noqa: E402

ROOT = Path(__file__).resolve().parents[1]
MAPPED = ROOT / "data" / "curated" / "mapped_ingredients.yaml"
UNMAPPED = ROOT / "data" / "curated" / "unmapped_ingredients.yaml"


def source_id(rec: dict) -> str | None:
    m = re.search(r"source_id=([^\s;)]+)", str(rec.get("notes") or ""))
    return m.group(1) if m else None


def resolve_target(mapped: dict, curie: str, term: str) -> dict:
    hits = [r for r in mapped["ingredients"] if r["identifier"] == curie]
    if term:
        hits = [r for r in hits if r["preferred_term"] == term]
    if len(hits) != 1:
        raise LookupError(
            f"{curie}" + (f" (preferred_term={term!r})" if term else "")
            + f" resolves to {len(hits)} mapped records, expected exactly 1")
    return hits[0]


def resolve_source(unmapped: dict, term: str) -> dict:
    """Strict, for the same reason as the target: a `{preferred_term: record}`
    dict keeps the last match, which would attach the synonym and the audit entry
    to the wrong source identifier and orphan the other record."""
    hits = [r for r in unmapped["ingredients"] if r["preferred_term"] == term]
    if len(hits) != 1:
        raise LookupError(
            f"{term!r} matches {len(hits)} records in the unmapped collection, expected exactly 1")
    return hits[0]


# Everything a source record can carry that a synonym on the target cannot
# represent. The merge would silently drop these, so refuse instead: this batch
# happened to have none, but the script is meant to be reused.
UNMERGEABLE = ("chemical_properties", "nutritional_roles", "functional_roles",
               "ontology_mapping", "evidence", "ingredient_type")


def unmergeable_fields(rec: dict) -> list[str]:
    lost = [f for f in UNMERGEABLE if rec.get(f)]
    occ = rec.get("occurrence_statistics") or {}
    if occ.get("total_occurrences") or occ.get("media_count"):
        lost.append(f"occurrence_statistics({occ.get('total_occurrences')}/{occ.get('media_count')})")
    extra = [s.get("synonym_text") for s in (rec.get("synonyms") or [])
             if s.get("synonym_text") != rec.get("preferred_term")]
    if extra:
        lost.append(f"synonyms({len(extra)} beyond the self-reference)")
    return lost


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--merges", required=True, type=Path, help="TSV of merge decisions")
    ap.add_argument("--curator", default="merge_unmapped_into_mapped")
    ap.add_argument("--apply", action="store_true", help="write; default is dry-run")
    args = ap.parse_args()

    stamp = dt.datetime.now(dt.timezone.utc).isoformat()
    mapped = yaml.safe_load(MAPPED.read_text())
    unmapped = yaml.safe_load(UNMAPPED.read_text())

    REQUIRED = ("source_term", "target_curie", "rationale")
    with args.merges.open() as fh:
        reader = csv.DictReader(fh, delimiter="\t")
        missing = [c for c in REQUIRED if c not in (reader.fieldnames or [])]
        if missing:
            print(f"ERROR: {args.merges} is missing column(s): {', '.join(missing)}")
            return 1
        decisions = list(reader)

    merged, problems = [], []
    for i, d in enumerate(decisions, start=2):  # 2 = first data row, for error messages
        # csv.DictReader pads a short row with None, which would otherwise be
        # interpolated into the audit trail as the literal string "None".
        blank = [c for c in REQUIRED if not (d.get(c) or "").strip()]
        if blank:
            problems.append(f"row {i}: empty or missing {', '.join(blank)}")
            continue
        term, curie = d["source_term"].strip(), d["target_curie"].strip()
        try:
            src = resolve_source(unmapped, term)
        except LookupError as exc:
            problems.append(f"row {i}: {exc}")
            continue
        if src.get("mapping_status") != "UNMAPPED":
            problems.append(f"{term!r}: status is {src.get('mapping_status')}, not UNMAPPED")
            continue
        lost = unmergeable_fields(src)
        if lost:
            problems.append(
                f"{term!r}: source carries data a synonym cannot represent "
                f"({', '.join(lost)}); merge it by hand or extend this script")
            continue
        try:
            tgt = resolve_target(mapped, curie, (d.get("target_preferred_term") or "").strip())
        except LookupError as exc:
            problems.append(f"row {i}: {exc}")
            continue

        existing = {s.get("synonym_text") for s in tgt.setdefault("synonyms", [])}
        if term not in existing:
            tgt["synonyms"].append(
                {"synonym_text": term, "synonym_type": "RAW_TEXT", "source": "microbedecoder"})
        sid = source_id(src)
        tgt.setdefault("curation_history", []).append({
            "timestamp": stamp,
            "curator": args.curator,
            "action": "MERGED_FROM_UNMAPPED_DUPLICATE",
            "changes": (f"Absorbed {src['identifier']} {term!r} as a RAW_TEXT synonym -- "
                        f"{d['rationale']}. No new SSSOM row; {curie} is already mapped."
                        + (f" Source: {sid}." if sid else "")),
            "llm_assisted": True,
        })
        unmapped["ingredients"].remove(src)
        merged.append((src["identifier"], term, curie, tgt["preferred_term"]))

    unmapped["total_count"] = len(unmapped["ingredients"])
    unmapped["unmapped_count"] = sum(
        1 for r in unmapped["ingredients"] if r.get("mapping_status") == "UNMAPPED")
    mapped["total_count"] = len(mapped["ingredients"])
    mapped["mapped_count"] = sum(
        1 for r in mapped["ingredients"] if r.get("mapping_status") == "MAPPED")
    unmapped["generation_date"] = stamp
    mapped["generation_date"] = stamp

    print(f"merged {len(merged)}/{len(decisions)}:")
    for ident, term, curie, tgt in merged:
        print(f"   {ident:15} {term!r} -> {curie} ({tgt})")
    if problems:
        print(f"\n{len(problems)} problem(s):")
        for p in problems:
            print(f"   {p}")
        print("\nRefusing to write a partial batch.")
        return 1
    print(f"\nunmapped collection: total={unmapped['total_count']} "
          f"unmapped={unmapped['unmapped_count']}")

    if not args.apply:
        print("\nDRY RUN -- nothing written. Pass --apply to write.")
        return 0

    save_yaml(mapped, MAPPED, validate=True, target_class="IngredientCollection")
    save_yaml(unmapped, UNMAPPED, validate=True, target_class="IngredientCollection")
    print("\nwrote data/curated/{mapped,unmapped}_ingredients.yaml")
    print("next: just export-individual && just export-lists && just export-browser && just qc")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
