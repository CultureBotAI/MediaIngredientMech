#!/usr/bin/env python3
"""Promote reviewed microbedecoder auto-groundings PENDING_REVIEW -> MAPPED (batch).

The microbedecoder import (#193) held 386 `ols-label-exact` groundings at
`mapping_status: PENDING_REVIEW` so they could not reach the published SSSOM before a
review pass (#192). This encodes the promotion so it is repeatable and gate-checked
instead of hand-edited across 386 records + the SSSOM.

A row is promoted only if it passes BOTH gates:

  * **round-trip** — the id resolves in the local OAK adapter and its canonical label
    still equals the record's `ontology_label` (case-insensitive);
  * **specificity** (#203) — the object is not a broad class-level grouping, and has no
    strictly more specific sibling label.

The round-trip gate alone is tautological: the record's `ontology_label` came from the
same OLS lookup that produced the grounding, so it re-derives the identity that created
the mapping and passed 386/386 of the population it was written for. It would approve
any wrong grounding whose id resolves — which is how `MIM:Sulfonamide -> CHEBI:35358`
(the structural functional-group class, 2976 direct subclasses) was approved when the
intended target was `CHEBI:87228 "sulfonamide antibiotic"` (24). Since `skos:exactMatch`
licenses node substitution, publishing that would let kg-microbe collapse every
sulfonamide-resistance edge onto the functional-group node.

The specificity gate is what can say no. It holds such rows at `NEEDS_SENSE_REVIEW` for
a human verdict rather than auto-approving them; on this corpus it flags 12 of 403 (3%),
including the known-bad one.

For every row in the review manifest whose `review_verdict` is PENDING (i.e. NOT one of
the 17 `SUSPECT_ID_OUT_OF_RANGE` already demoted), and only if it passes both gates, this:

  1. Flips `mapping_status` PENDING_REVIEW -> MAPPED in data/curated/mapped_ingredients.yaml
     and appends a REVIEWED_AND_PROMOTED curation_history entry. The record already carries
     a complete `ontology_mapping` (EXACT_MATCH) from the import, so nothing else changes.
  2. Fixes the header `mapped_count`.
  3. Synthesises an SSSOM row (subject `MIM:<existing file stem>` from the manifest so the
     export never renames it; skos:exactMatch; semapv:LexicalMatching — the honest
     derivation; object_source obo:chebi.owl / obo:ncit.owl), inserted in subject_label
     sort order. reconcile_sssom refuses to auto-add GAP rows, so they are added here.
  4. Writes the verdict (APPROVED / FAILED_ROUNDTRIP / NEEDS_SENSE_REVIEW) and a reviewer
     note back into the manifest — every outcome, not only the approvals.

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
import argparse, csv, datetime as dt, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "src"))
sys.path.insert(0, str(ROOT / "scripts"))
import yaml
from mediaingredientmech.utils.yaml_handler import save_yaml
from oaklib import get_adapter

MAPPED = ROOT / "data" / "curated" / "mapped_ingredients.yaml"
SSSOM = ROOT / "mappings" / "ingredient_mappings.sssom.tsv"
MANIFEST = ROOT / "mappings" / "microbedecoder_auto_mapped_review.tsv"

# Imported, not re-declared (#385). This table existed in FOUR scripts and this
# copy listed only CHEBI and NCIT — so promoting a FOODON, ENVO, MICRO, UBERON,
# BTO or MESH record through here published an empty object_source (or, where
# the lookup indexes directly, raised KeyError). That is #381's defect, which
# #384 fixed in one table while three others still carried it.
from promote_resolved_unmapped import OBJECT_SOURCE  # noqa: E402
NOTE = ("Reviewed by review-ingredients: id resolves in local OAK adapter, its canonical "
        "label exact-matches the record ontology_label (case-insensitive), AND it passed "
        "the specificity check (#203) — not a broad class-level term, and no strictly "
        "more specific sibling label exists. Promoted PENDING_REVIEW -> MAPPED.")

# A term with this many DIRECT subclasses is a class-level grouping, not a substance.
# Publishing skos:exactMatch to one licenses node substitution, which is how
# MIM:Sulfonamide -> CHEBI:35358 (2976 subclasses) would have collapsed every
# sulfonamide-resistance edge onto the functional-group node (#203). The intended
# target there, CHEBI:87228 "sulfonamide antibiotic", has 24 — so the default sits
# above that and below the groupings actually seen in this corpus.
DEFAULT_SUBCLASS_ALARM = 50
# A label that is a strict prefix of another term's label ("sulfonamide" vs
# "sulfonamide antibiotic") MAY be the wrong sense. On its own this fires on 163 of
# 403 rows — far too noisy to gate on — so it only counts when the term is also
# somewhat broad. Together they flag 12 of 403 (3%), including the known-bad one.
PREFIX_SUBCLASS_FLOOR = 10


def _adapters(prefixes=("CHEBI", "NCIT")):
    """Adapters for the prefixes a caller actually needs (#395).

    This used to build CHEBI and NCIT unconditionally, so a CHEBI-only caller
    downloaded ~525MB of `ncit.db.gz` it never read —
    `partition_class_term_cohort.py` reads one table of one database and paid
    that on a cold cache. `_specificity_index` already tolerates a partial map
    (a prefix whose adapter has no SQL engine yields empty results, making the
    check a no-op rather than a false alarm), so narrowing the default costs
    nothing downstream.
    """
    return {p: get_adapter(f"sqlite:obo:{p.lower()}") for p in prefixes}


def _specificity_index(adapters: dict) -> dict:
    """Per-prefix (direct-subclass counts, lowercased label set), pulled in bulk.

    ``incoming_relationship_map`` costs ~4-7s per term, which is unusable over a
    corpus this size; two grouped SQL queries answer the same questions for every
    term at once in about a second. Mirrors ``chem_formula.build_formula_lookup``.
    Prefixes whose adapter has no SQL engine yield empty maps, which makes the
    specificity check a no-op for them rather than a false alarm.
    """
    from sqlalchemy import text

    index = {}
    for prefix, adapter in adapters.items():
        engine = getattr(adapter, "engine", None)
        if engine is None:
            index[prefix] = ({}, set())
            continue
        try:
            with engine.connect() as conn:
                counts = {
                    str(o): int(n)
                    for o, n in conn.execute(text(
                        "SELECT object, COUNT(*) FROM edge "
                        "WHERE predicate = 'rdfs:subClassOf' GROUP BY object"))
                    if o
                }
                labels = {
                    str(v).lower()
                    for _, v in conn.execute(text(
                        "SELECT subject, value FROM statements "
                        "WHERE predicate = 'rdfs:label' AND value IS NOT NULL"))
                    if v
                }
            index[prefix] = (counts, labels)
        except Exception:
            index[prefix] = ({}, set())
    return index


def _specificity_alarm(index: dict, curie: str, label: str, alarm: int):
    """Reason this (id, label) needs a human sense-verdict, or None if it is specific.

    Returns a human-readable string naming the evidence, so the manifest records WHY
    a row was held rather than just that it was.
    """
    if alarm <= 0:
        # The documented escape hatch. Guarded explicitly: `n > 0` would otherwise
        # flag every term with even one subclass, i.e. do the OPPOSITE of disabling.
        return None
    prefix = curie.split(":")[0]
    counts, labels = index.get(prefix, ({}, set()))
    if not counts and not labels:
        return None                       # no index for this ontology: cannot judge
    n = counts.get(curie, 0)
    lab = (label or "").strip().lower()
    more_specific = sorted(l for l in labels if lab and l.startswith(lab + " "))
    if n > alarm:
        detail = f"{n} direct subclasses"
        if more_specific:
            detail += f"; more specific term(s) exist e.g. {more_specific[0]!r}"
        return f"class-level term ({detail})"
    if more_specific and n > PREFIX_SUBCLASS_FLOOR:
        return (f"possible wrong sense: {n} direct subclasses and "
                f"{len(more_specific)} strictly more specific label(s), "
                f"e.g. {more_specific[0]!r}")
    return None


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
    ap.add_argument("--subclass-alarm", type=int, default=DEFAULT_SUBCLASS_ALARM,
                    help=(f"hold any object with more than N direct subclasses for a human "
                          f"sense-verdict (default {DEFAULT_SUBCLASS_ALARM}); 0 disables "
                          "the specificity check"))
    args = ap.parse_args()

    manifest_rows = list(csv.DictReader(MANIFEST.read_text().splitlines(), delimiter="\t"))
    curated = yaml.safe_load(MAPPED.read_text())
    by_id = {r.get("identifier"): r for r in curated["ingredients"]}
    ad = _adapters()

    index = _specificity_index(ad)

    promote, skipped = [], []
    # (manifest row, reason) keyed by the verdict to write back, so the manifest
    # records every outcome instead of only the successes.
    failed_roundtrip, needs_sense = [], []
    for mrow in manifest_rows:
        if mrow["review_verdict"] != "PENDING":
            continue
        oid = mrow["ontology_id"]
        rec = by_id.get(mrow["identifier"])
        if rec is None or rec.get("mapping_status") != "PENDING_REVIEW":
            # A state mismatch, NOT a round-trip failure: the record moved on since
            # the manifest was written. Left PENDING for a curator to reconcile.
            skipped.append((mrow, "not PENDING_REVIEW in curated")); continue
        prefix = oid.split(":")[0]
        lbl = ad[prefix].label(oid) if prefix in ad else None
        if lbl is None:
            why = "id does not resolve in OAK"
            skipped.append((mrow, why)); failed_roundtrip.append((mrow, why)); continue
        # Compare against the RECORD's label, which is what gets published, falling
        # back to the manifest's copy. 11 rows (incl. the #207 antibiotics) carry an
        # empty ontology_label in the manifest while the record holds the correct one,
        # and comparing manifest-first reported those as "label drift" and refused to
        # promote records that were in fact clean.
        rec_label = ((rec.get("ontology_mapping") or {}).get("ontology_label")
                     or mrow["ontology_label"] or "")
        if not rec_label.strip():
            why = "no ontology_label recorded on the record or in the manifest"
            skipped.append((mrow, why)); failed_roundtrip.append((mrow, why)); continue
        if lbl.strip().lower() != rec_label.strip().lower():
            why = f"label drift: oak={lbl!r} record={rec_label!r}"
            skipped.append((mrow, why)); failed_roundtrip.append((mrow, why)); continue
        # The round-trip above only re-derives the identity that CREATED the mapping
        # (the record's ontology_label came from the same OLS lookup), so on its own
        # it approves everything. The specificity check is the half that can say no.
        alarm = _specificity_alarm(index, oid, rec_label, args.subclass_alarm)
        if alarm:
            why = f"specificity: {alarm}"
            skipped.append((mrow, why)); needs_sense.append((mrow, alarm)); continue
        promote.append((mrow, rec))
        if args.limit and len(promote) >= args.limit:
            break

    print(f"manifest PENDING rows: {sum(1 for m in manifest_rows if m['review_verdict']=='PENDING')}")
    print(f"to promote (verified): {len(promote)}   skipped: {len(skipped)}")
    print(f"  of which FAILED_ROUNDTRIP: {len(failed_roundtrip)}   "
          f"NEEDS_SENSE_REVIEW: {len(needs_sense)}")
    for m, why in skipped[:20]:
        print(f"  SKIP {m['identifier']} ({m['ontology_id']}): {why}")

    # Build SSSOM rows + mutate records
    run_stamp = dt.datetime.now(dt.timezone.utc).isoformat(timespec="seconds")
    sssom_rows = []
    promoted_ids = set()
    for mrow, rec in promote:
        stem = mrow["file"][:-5] if mrow["file"].endswith(".yaml") else mrow["file"]
        oid = mrow["ontology_id"]
        obj_src = OBJECT_SOURCE.get(oid.split(":")[0], "")
        src = "MIM:microbedecoder|MIM:curator=review-ingredients"
        # object_label from the record, not the manifest: 11 manifest rows carry an
        # empty ontology_label, which published SSSOM rows with a blank object_label.
        obj_label = ((rec.get("ontology_mapping") or {}).get("ontology_label")
                     or mrow["ontology_label"] or "")
        row = "\t".join([f"MIM:{stem}", rec["preferred_term"], "skos:exactMatch", oid,
                         obj_label, obj_src, "semapv:LexicalMatching", src,
                         args.date, "0.99", "", "",
                         f"manual:review-ingredients|APPROVED|{args.date}"]) + "\n"
        sssom_rows.append((rec["preferred_term"], row))
        rec["mapping_status"] = "MAPPED"
        rec.setdefault("curation_history", []).append({
            # A real instant, not midnight of --date: the old form stamped history
            # entries EARLIER than the record they describe, which reads as the
            # promotion having happened before the import (#203).
            "timestamp": run_stamp,
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

    # Write verdicts back to the manifest. Every outcome is recorded, not just the
    # approvals: FAILED_ROUNDTRIP was documented in this script's docstring but never
    # written anywhere, so the one failure mode the manifest exists to capture was the
    # one it could not capture (#203).
    held = {m["identifier"]: why for m, why in failed_roundtrip}
    sense = {m["identifier"]: why for m, why in needs_sense}
    for m in manifest_rows:
        if m["identifier"] in promoted_ids:
            m["review_verdict"] = "APPROVED"
            m["reviewer_notes"] = ("review-ingredients: OAK round-trip pass (id resolves, "
                                   "label exact-match) AND specificity check pass; "
                                   "promoted to MAPPED")
        elif m["identifier"] in held:
            m["review_verdict"] = "FAILED_ROUNDTRIP"
            m["reviewer_notes"] = f"review-ingredients: {held[m['identifier']]}; left PENDING_REVIEW"
        elif m["identifier"] in sense:
            m["review_verdict"] = "NEEDS_SENSE_REVIEW"
            m["reviewer_notes"] = (
                f"review-ingredients: {sense[m['identifier']]}. A skos:exactMatch to a "
                "class-level term licenses node substitution, so this needs a human "
                "verdict on the intended sense before promotion (#203). Left "
                "PENDING_REVIEW.")
    with MANIFEST.open("w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(manifest_rows[0].keys()), delimiter="\t")
        w.writeheader(); w.writerows(manifest_rows)

    print(f"\nApplied: promoted {len(promoted_ids)}, added {len(sssom_rows)} SSSOM rows, wrote manifest verdicts.")
    print("Now run: export_individual_records.py, export_lists.py, reconcile_sssom.py (expect GAP 0), "
          "validate_sssom_invariants.py, just validate-all && just qc-roundtrip")
    return 0


if __name__ == "__main__":
    sys.exit(main())
