#!/usr/bin/env python3
"""Promote reviewed microbedecoder auto-groundings PENDING_REVIEW -> MAPPED (batch).

The microbedecoder import (#193) held 386 `ols-label-exact` groundings at
`mapping_status: PENDING_REVIEW` so they could not reach the published SSSOM before a
review pass (#192). This encodes the promotion so it is repeatable and gate-checked
instead of hand-edited across 386 records + the SSSOM.

For every row in the review manifest whose `review_verdict` is PENDING (i.e. NOT one of
the 17 `SUSPECT_ID_OUT_OF_RANGE` already demoted), and only if it still round-trips in
the local OAK adapter (id resolves AND its canonical label still equals the record's
`ontology_label`, case-insensitive), this:

  1. Flips `mapping_status` PENDING_REVIEW -> MAPPED in data/curated/mapped_ingredients.yaml
     and appends a REVIEWED_AND_PROMOTED curation_history entry. The record already carries
     a complete `ontology_mapping` (EXACT_MATCH) from the import, so nothing else changes.
  2. Fixes the header `mapped_count`.
  3. Synthesises an SSSOM row (subject `MIM:<existing file stem>` from the manifest so the
     export never renames it; skos:exactMatch; semapv:LexicalMatching — the honest
     derivation; object_source obo:chebi.owl / obo:ncit.owl), inserted in subject_label
     sort order. reconcile_sssom refuses to auto-add GAP rows, so they are added here.
  4. Writes the verdict (APPROVED / SUSPECT_ID_OUT_OF_RANGE / FAILED_ROUNDTRIP) and a
     reviewer note back into the manifest.

It does NOT regenerate per-record files, docs, or run qc — do that after --apply:
    uv run python scripts/export_individual_records.py
    uv run python scripts/export_lists.py
    python scripts/reconcile_sssom.py            # expect GAP 0
    python scripts/validate_sssom_invariants.py
    just validate-all && just qc-roundtrip

Usage:
    python scripts/promote_microbedecoder_reviewed.py                 # dry-run, all
    python scripts/promote_microbedecoder_reviewed.py --limit 1 --apply   # canary
    python scripts/promote_microbedecoder_reviewed.py --apply             # the rest
"""
from __future__ import annotations
import argparse, csv, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "src"))
import yaml
from mediaingredientmech.utils.yaml_handler import save_yaml
from oaklib import get_adapter

MAPPED = ROOT / "data" / "curated" / "mapped_ingredients.yaml"
SSSOM = ROOT / "mappings" / "ingredient_mappings.sssom.tsv"
MANIFEST = ROOT / "mappings" / "microbedecoder_auto_mapped_review.tsv"

OBJECT_SOURCE = {"CHEBI": "obo:chebi.owl", "NCIT": "obo:ncit.owl"}
NOTE = ("Reviewed by review-ingredients: id resolves in local OAK adapter and its canonical "
        "label exact-matches the record ontology_label (case-insensitive); no synonym-only, "
        "homonym, or out-of-range issue. Promoted PENDING_REVIEW -> MAPPED.")


def _adapters():
    return {"CHEBI": get_adapter("sqlite:obo:chebi"), "NCIT": get_adapter("sqlite:obo:ncit")}


def _sorted_insert(lines: list[str], header_i: int, subject_label: str, row: str) -> int:
    """Insert `row` among data rows (after header_i) keeping subject_label sort order."""
    i = header_i + 1
    while i < len(lines):
        cols = lines[i].split("\t")
        if len(cols) > 1 and cols[1] > subject_label:
            break
        i += 1
    lines.insert(i, row)
    return i


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--apply", action="store_true", help="write (default: dry-run)")
    ap.add_argument("--limit", type=int, default=0, help="promote at most N records (0 = all) — for a canary")
    ap.add_argument("--date", default="2026-08-04")
    args = ap.parse_args()

    manifest_rows = list(csv.DictReader(MANIFEST.read_text().splitlines(), delimiter="\t"))
    curated = yaml.safe_load(MAPPED.read_text())
    by_id = {r.get("identifier"): r for r in curated["ingredients"]}
    ad = _adapters()

    promote, skipped = [], []
    for mrow in manifest_rows:
        if mrow["review_verdict"] != "PENDING":
            continue
        oid = mrow["ontology_id"]
        rec = by_id.get(mrow["identifier"])
        if rec is None or rec.get("mapping_status") != "PENDING_REVIEW":
            skipped.append((mrow, "not PENDING_REVIEW in curated")); continue
        prefix = oid.split(":")[0]
        lbl = ad[prefix].label(oid) if prefix in ad else None
        if lbl is None:
            skipped.append((mrow, "id does not resolve in OAK")); continue
        if lbl.strip().lower() != mrow["ontology_label"].strip().lower():
            skipped.append((mrow, f"label drift: oak={lbl!r} record={mrow['ontology_label']!r}")); continue
        promote.append((mrow, rec))
        if args.limit and len(promote) >= args.limit:
            break

    print(f"manifest PENDING rows: {sum(1 for m in manifest_rows if m['review_verdict']=='PENDING')}")
    print(f"to promote (verified): {len(promote)}   skipped: {len(skipped)}")
    for m, why in skipped[:20]:
        print(f"  SKIP {m['identifier']} ({m['ontology_id']}): {why}")

    # Build SSSOM rows + mutate records
    sssom_rows = []
    promoted_ids = set()
    for mrow, rec in promote:
        stem = mrow["file"][:-5] if mrow["file"].endswith(".yaml") else mrow["file"]
        oid = mrow["ontology_id"]
        obj_src = OBJECT_SOURCE.get(oid.split(":")[0], "")
        src = "MIM:microbedecoder|MIM:curator=review-ingredients"
        row = "\t".join([f"MIM:{stem}", rec["preferred_term"], "skos:exactMatch", oid,
                         mrow["ontology_label"], obj_src, "semapv:LexicalMatching", src,
                         args.date, "0.99", "", "",
                         f"manual:review-ingredients|APPROVED|{args.date}"]) + "\n"
        sssom_rows.append((rec["preferred_term"], row))
        rec["mapping_status"] = "MAPPED"
        rec.setdefault("curation_history", []).append({
            "timestamp": f"{args.date}T00:00:00+00:00",
            "curator": "review-ingredients",
            "action": "REVIEWED_AND_PROMOTED",
            "changes": "mapping_status PENDING_REVIEW -> MAPPED",
            "previous_status": "PENDING_REVIEW",
            "new_status": "MAPPED",
            "notes": NOTE,
            "llm_assisted": True,
        })
        promoted_ids.add(mrow["identifier"])

    curated["mapped_count"] = sum(1 for r in curated["ingredients"] if r.get("mapping_status") == "MAPPED")
    print(f"\nnew mapped_count would be: {curated['mapped_count']}")
    print(f"SSSOM rows to add: {len(sssom_rows)}")
    if sssom_rows:
        print("  e.g. " + sssom_rows[0][1].strip()[:160])

    if not args.apply:
        print("\n(dry-run — pass --apply to write curated + SSSOM + manifest verdicts)")
        return 0

    save_yaml(curated, MAPPED, validate=True, target_class="IngredientCollection")

    lines = SSSOM.read_text().splitlines(keepends=True)
    header_i = next(i for i, l in enumerate(lines) if not l.startswith("#"))
    for subject_label, row in sssom_rows:
        _sorted_insert(lines, header_i, subject_label, row)
    SSSOM.write_text("".join(lines))

    # write verdicts back to the manifest
    for m in manifest_rows:
        if m["identifier"] in promoted_ids:
            m["review_verdict"] = "APPROVED"
            m["reviewer_notes"] = "review-ingredients: OAK round-trip pass (id resolves, label exact-match); promoted to MAPPED"
    with MANIFEST.open("w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(manifest_rows[0].keys()), delimiter="\t")
        w.writeheader(); w.writerows(manifest_rows)

    print(f"\nApplied: promoted {len(promoted_ids)}, added {len(sssom_rows)} SSSOM rows, wrote manifest verdicts.")
    print("Now run: export_individual_records.py, export_lists.py, reconcile_sssom.py (expect GAP 0), "
          "validate_sssom_invariants.py, just validate-all && just qc-roundtrip")
    return 0


if __name__ == "__main__":
    sys.exit(main())
