#!/usr/bin/env python3
"""Batch-promote microbedecoder UNMAPPED residual records that exact-match an ontology term.

STATUS: COMPLETED PASS — kept for provenance, not for scheduling.
    All 20 rows in the vetted manifest are already MAPPED in the corpus, so a run today
    SKIPs every one on the PK-collision guard and promotes nothing (verified 2026-08-07:
    `python scripts/promote_microbedecoder_residual.py` -> 0 promotions). It is preserved
    because the manifest it consumed (mappings/microbedecoder_residual_grounded.tsv) is
    tracked while the tool that consumed it was not: this script was written on the branch
    behind PR #201, which was CLOSED rather than merged, so the results reached `main`
    through the follow-on PRs while the script did not. The repo keeps its sibling one-shot
    (scripts/apply_microbedecoder_residual_merges.py) for the same reason — a manifest whose
    producer is missing cannot be audited or re-derived.
    DO NOT re-point it at a new manifest with --vetted without fixing two known defects
    first — they are harmless while every row is a no-op and become live on reuse:
      #307  it recomputes the SSSOM subject as MIM:sanitize_filename(preferred_term)
            instead of using the existing per-record file stem, so a promotion whose
            stem predates the current naming rule publishes a subject no file backs
            (CurieNormalizer -> UNKNOWN_SUBJECT). Same defect as #293, second copy.
      #306  it hardcodes ~/.data/oaklib/*.db instead of resolving the cache through
            pystow, so with PYSTOW_HOME set it reports "CHEBI:NNNNN has no rdfs:label
            (absent / wrong id)" — blaming the identifier for a path problem.
    It also does not run the post-conditions listed below; they are manual steps, and
    skipping the browser export leaves docs/data/ingredients.json stale (#276).

The #193 import matched labels EXACTLY only (ols-label-exact) and never tried normalized or
fuzzy matching, so it left groundable chemicals in the UNMAPPED residual. This promotes the
records that a normalize + exact-CI pass recovered (CHEBI and NCIT), reading the vetted list
from mappings/microbedecoder_residual_grounded.tsv.

Same multi-surface move as scripts/promote_resolved_unmapped.py, but batched (regen once, not
per record) and CHEBI **or** NCIT. Per row it:
  1. PK-collision guard: if target id is already a MAPPED primary, SKIP (that is a merge, not a
     promote — handled separately).
  2. Transforms the record in data/curated/unmapped_ingredients.yaml: identifier -> target,
     ontology_mapping (canonical label from the local OAK db), mapping_status MAPPED, appends a
     PROMOTED_TO_MAPPED curation_history entry. Moves it into mapped_ingredients.yaml; fixes both
     header counts.
  3. Synthesises the SSSOM row (subject MIM:sanitize_filename(preferred_term), skos:exactMatch,
     semapv:LexicalMatching, object_source obo:chebi.owl / obo:ncit.owl), inserted in
     subject_label sort order.

Does NOT regenerate per-record files / docs / SSSOM reconcile — run after --apply:
    uv run python scripts/export_individual_records.py
    uv run python scripts/export_lists.py
    python scripts/reconcile_sssom.py            # expect GAP 0
    python scripts/validate_sssom_invariants.py
    just validate-all && just qc-roundtrip

Usage:
    python scripts/promote_microbedecoder_residual.py                 # dry-run, all
    python scripts/promote_microbedecoder_residual.py --limit 1 --apply   # canary
    python scripts/promote_microbedecoder_residual.py --apply             # the rest
"""
from __future__ import annotations
import argparse, csv, sqlite3, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "src"))
sys.path.insert(0, str(ROOT / "scripts"))
import yaml
from mediaingredientmech.utils.yaml_handler import save_yaml
from export_individual_records import sanitize_filename

MAPPED = ROOT / "data" / "curated" / "mapped_ingredients.yaml"
UNMAPPED = ROOT / "data" / "curated" / "unmapped_ingredients.yaml"
SSSOM = ROOT / "mappings" / "ingredient_mappings.sssom.tsv"
VETTED = ROOT / "mappings" / "microbedecoder_residual_grounded.tsv"
DB = {"CHEBI": Path.home() / ".data/oaklib/chebi.db", "NCIT": Path.home() / ".data/oaklib/ncit.db"}
OBJECT_SOURCE = {"CHEBI": "obo:chebi.owl", "NCIT": "obo:ncit.owl"}
CONFIDENCE = {"EXACT_MATCH": "0.99", "SYNONYM_MATCH": "0.95", "CLOSE_MATCH": "0.9"}


def canonical_label(cid: str) -> str:
    pfx = cid.split(":")[0]
    con = sqlite3.connect(f"file:{DB[pfx]}?mode=ro", uri=True)
    row = con.execute("SELECT value FROM statements WHERE subject=? AND predicate='rdfs:label'", (cid,)).fetchone()
    dep = con.execute("SELECT 1 FROM statements WHERE subject=? AND predicate='owl:deprecated'", (cid,)).fetchone()
    con.close()
    if not row:
        raise SystemExit(f"{cid} has no rdfs:label (absent / wrong id)")
    if dep:
        raise SystemExit(f"{cid} is obsolete — pick a current term")
    return row[0]


def _sorted_insert(lines, header_i, subject_label, row):
    i = header_i + 1
    while i < len(lines):
        cols = lines[i].split("\t")
        if len(cols) > 1 and cols[1] > subject_label:
            break
        i += 1
    lines.insert(i, row)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--apply", action="store_true")
    ap.add_argument("--limit", type=int, default=0, help="promote at most N (0 = all) — for a canary")
    ap.add_argument("--vetted", default=str(VETTED), help="path to the vetted grounding TSV")
    ap.add_argument("--date", default="2026-08-04")
    args = ap.parse_args()

    rows = list(csv.DictReader(Path(args.vetted).read_text().splitlines(), delimiter="\t"))
    mapped = yaml.safe_load(MAPPED.read_text())
    unmapped = yaml.safe_load(UNMAPPED.read_text())
    mapped_pks = {r["identifier"] for r in mapped["ingredients"]}
    unmapped_idx = {r["identifier"]: i for i, r in enumerate(unmapped["ingredients"])}

    plan, skipped, sssom_rows, to_pop = [], [], [], []
    for row in rows:
        ident, tid = row["identifier"], row["target_id"]
        if tid in mapped_pks:
            skipped.append((ident, tid, "PK collision (already MAPPED) — merge, not promote")); continue
        if ident not in unmapped_idx:
            skipped.append((ident, tid, "not found in unmapped_ingredients.yaml")); continue
        label = canonical_label(tid)
        quality = row["quality"]
        rec = unmapped["ingredients"][unmapped_idx[ident]]
        pref = rec.get("preferred_term", ident)
        slug = sanitize_filename(pref)
        plan.append((ident, pref, tid, label, quality))
        rec["identifier"] = tid
        rec["ontology_mapping"] = {
            "ontology_id": tid, "ontology_label": label, "ontology_source": tid.split(":")[0],
            "mapping_quality": quality,
            "evidence": [{"evidence_type": "LEXICAL_MATCH", "source": "microbedecoder-residual-grounding",
                          "notes": row["note"]}],
        }
        rec["mapping_status"] = "MAPPED"
        rec.setdefault("curation_history", []).append({
            "timestamp": f"{args.date}T00:00:00+00:00", "curator": "microbedecoder-residual-grounding",
            "action": "PROMOTED_TO_MAPPED", "previous_status": "UNMAPPED", "new_status": "MAPPED",
            "llm_assisted": True,
            "changes": f"Promoted {ident} -> {tid} \"{label}\" ({quality}) via normalize+exact-CI "
                       f"(matched {row['matched_via']!r}); the exact-only import missed it. SSSOM row added.",
        })
        src = "MIM:microbedecoder|MIM:curator=microbedecoder-residual-grounding"
        sssom_rows.append((pref, "\t".join([
            f"MIM:{slug}", pref, "skos:exactMatch", tid, label, OBJECT_SOURCE[tid.split(":")[0]],
            "semapv:LexicalMatching", src, args.date, CONFIDENCE[quality], "", "",
            f"manual:microbedecoder-residual-grounding|PROMOTED|{args.date}"]) + "\n"))
        to_pop.append(ident)
        if args.limit and len(plan) >= args.limit:
            break

    print(f"vetted rows: {len(rows)}   to promote: {len(plan)}   skipped: {len(skipped)}")
    for ident, tid, why in skipped:
        print(f"  SKIP {ident} -> {tid}: {why}")
    print("\n=== promotions ===")
    for ident, pref, tid, label, quality in plan:
        print(f"  {ident}\t{pref!r} -> {tid} {label!r} [{quality}]")

    if not args.apply:
        print("\n(dry-run — pass --apply to write collections + SSSOM)")
        return 0

    # apply: pop from unmapped, insert into mapped, fix counts
    pop_set = set(to_pop)
    promoted_recs = [r for r in unmapped["ingredients"] if r["identifier"] in {tid for _, _, tid, _, _ in plan}]
    # move by identifier (records were mutated in-place; identifier is now the target id)
    keep, moved = [], []
    target_ids = {tid for _, _, tid, _, _ in plan}
    for r in unmapped["ingredients"]:
        (moved if r["identifier"] in target_ids else keep).append(r)
    unmapped["ingredients"] = keep
    for r in moved:
        mapped["ingredients"].insert(0, r)
    unmapped["total_count"] = len(unmapped["ingredients"])
    unmapped["unmapped_count"] = sum(1 for r in unmapped["ingredients"] if r.get("mapping_status") == "UNMAPPED")
    mapped["total_count"] = len(mapped["ingredients"])
    mapped["mapped_count"] = sum(1 for r in mapped["ingredients"] if r.get("mapping_status") == "MAPPED")
    save_yaml(mapped, MAPPED, validate=True, target_class="IngredientCollection")
    save_yaml(unmapped, UNMAPPED, validate=True, target_class="IngredientCollection")

    lines = SSSOM.read_text().splitlines(keepends=True)
    header_i = next(i for i, l in enumerate(lines) if not l.startswith("#"))
    for subject_label, row in sssom_rows:
        _sorted_insert(lines, header_i, subject_label, row)
    SSSOM.write_text("".join(lines))

    print(f"\nApplied: promoted {len(moved)}, added {len(sssom_rows)} SSSOM rows.")
    print(f"mapped_count -> {mapped['mapped_count']}, unmapped_count -> {unmapped['unmapped_count']}")
    print("Now regenerate + qc (see module docstring).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
