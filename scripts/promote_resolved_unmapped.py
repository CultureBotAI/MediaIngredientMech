#!/usr/bin/env python3
"""Promote a resolved UNMAPPED ingredient to a MAPPED CHEBI record — end to end.

Encodes the multi-surface migration recipe (NEXT_TASKS #3) so it is repeatable and
safe instead of hand-edited:

  1. Move + transform the record from data/curated/unmapped_ingredients.yaml into
     data/curated/mapped_ingredients.yaml: set identifier + ontology_mapping (with
     the CANONICAL CHEBI label from the local OAK chebi.db), mapping_status=MAPPED,
     add a PROMOTED_TO_MAPPED curation_history entry; fix both header counts.
  2. Regenerate per-record files (export_individual_records.py) — the file moves
     unmapped/ -> mapped/.
  3. Add the SSSOM row (skos:<predicate> to the CHEBI id, obo:chebi.owl, canonical
     object_label), inserted in subject-label sort order. exact/close need no Rule
     B1 registry sibling; narrow/broad are refused here (they require registry rows
     this helper does not synthesise — hand-curate those).
  4. Regenerate docs (export_lists.py).
  5. Verify: reconcile_sssom (GAP 0) + validate_sssom_invariants.

Usage:
    python scripts/promote_resolved_unmapped.py --identifier UNMAPPED_0323 \\
        --to CHEBI:30915 --quality CLOSE_MATCH \\
        --evidence-source "Edison deep research + local CHEBI verification" \\
        --note "alpha-ketoglutamate = alpha-ketoglutarate / 2-oxoglutarate; acid form." \\
        [--date 2026-06-16] [--apply]

Default is a dry-run (prints the plan); pass --apply to write + regenerate.
"""
from __future__ import annotations
import argparse, subprocess, sqlite3, sys
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
CHEBI_DB = Path.home() / ".data" / "oaklib" / "chebi.db"

PREDICATE = {"EXACT_MATCH": "skos:exactMatch", "SYNONYM_MATCH": "skos:exactMatch",
             "CLOSE_MATCH": "skos:closeMatch"}
CONFIDENCE = {"EXACT_MATCH": "0.99", "SYNONYM_MATCH": "0.95", "CLOSE_MATCH": "0.9"}


def canonical_label(cid: str) -> str:
    con = sqlite3.connect(f"file:{CHEBI_DB}?mode=ro", uri=True)
    row = con.execute("SELECT value FROM statements WHERE subject=? AND predicate='rdfs:label'", (cid,)).fetchone()
    dep = con.execute("SELECT 1 FROM statements WHERE subject=? AND predicate='owl:deprecated'", (cid,)).fetchone()
    con.close()
    if not row:
        raise SystemExit(f"{cid} has no rdfs:label in chebi.db (absent / wrong id)")
    if dep:
        raise SystemExit(f"{cid} is obsolete in CHEBI — pick a current term")
    return row[0]


def _sorted_insert(lines: list[str], header_i: int, new_subject_label: str, new_row: str) -> int:
    """Insert new_row among data rows in subject_label (col 2) ascending order."""
    i = header_i + 1
    while i < len(lines):
        cols = lines[i].split("\t")
        if len(cols) > 1 and cols[1] > new_subject_label:
            break
        i += 1
    lines.insert(i, new_row)
    return i


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--identifier", required=True, help="UNMAPPED_* identifier to promote")
    ap.add_argument("--to", required=True, help="target CHEBI CURIE, e.g. CHEBI:30915")
    ap.add_argument("--quality", default="EXACT_MATCH", choices=list(PREDICATE))
    ap.add_argument("--evidence-source", default="promote_resolved_unmapped")
    ap.add_argument("--note", default="")
    ap.add_argument("--date", default="2026-06-16")
    ap.add_argument("--apply", action="store_true")
    a = ap.parse_args()
    if not a.to.startswith("CHEBI:"):
        raise SystemExit("this helper only promotes to CHEBI ids")

    label = canonical_label(a.to)
    mapped = yaml.safe_load(MAPPED.read_text())
    unmapped = yaml.safe_load(UNMAPPED.read_text())
    idx = next((i for i, r in enumerate(unmapped["ingredients"]) if r["identifier"] == a.identifier), None)
    if idx is None:
        raise SystemExit(f"{a.identifier} not found in {UNMAPPED.name}")
    if any(r["identifier"] == a.to for r in mapped["ingredients"]):
        raise SystemExit(f"{a.to} is already a primary key in {MAPPED.name} (PK collision)")

    rec = unmapped["ingredients"][idx]
    pref = rec.get("preferred_term", a.identifier)
    slug = sanitize_filename(pref)
    print(f"Promote {a.identifier} ({pref!r}) -> {a.to} {label!r}  [{a.quality}]")
    print(f"  SSSOM: MIM:{slug}  {PREDICATE[a.quality]}  {a.to}  '{label}'  conf={CONFIDENCE[a.quality]}")

    # transform the record
    rec["identifier"] = a.to
    rec["ontology_mapping"] = {
        "ontology_id": a.to, "ontology_label": label, "ontology_source": "CHEBI",
        "mapping_quality": a.quality,
        "evidence": [{"evidence_type": "DATABASE_MATCH", "source": a.evidence_source,
                      "notes": a.note or f"Resolved to {a.to} ({label})."}],
    }
    rec["mapping_status"] = "MAPPED"
    rec.setdefault("curation_history", []).append({
        "timestamp": f"{a.date}T00:00:00+00:00", "curator": "promote_resolved_unmapped",
        "action": "PROMOTED_TO_MAPPED", "previous_status": "UNMAPPED", "new_status": "MAPPED",
        "llm_assisted": False,
        "changes": f"Promoted {a.identifier} -> {a.to} \"{label}\" ({a.quality}); "
                   f"mapping_status UNMAPPED -> MAPPED, SSSOM row added.",
    })

    # move between collections + fix header counts
    unmapped["ingredients"].pop(idx)
    unmapped["total_count"] = unmapped.get("total_count", len(unmapped["ingredients"]) + 1) - 1
    unmapped["unmapped_count"] = unmapped.get("unmapped_count", 0) - 1
    mapped["ingredients"].insert(0, rec)
    mapped["total_count"] = mapped.get("total_count", len(mapped["ingredients"]) - 1) + 1
    mapped["mapped_count"] = mapped.get("mapped_count", 0) + 1

    # build SSSOM row (13 cols)
    src = f"MIM:{a.evidence_source}|MIM:curator=promote_resolved_unmapped"
    row = "\t".join([f"MIM:{slug}", pref, PREDICATE[a.quality], a.to, label, "obo:chebi.owl",
                     "semapv:ManualMappingCuration", src, a.date, CONFIDENCE[a.quality],
                     "", "", f"manual:promote_resolved_unmapped|PROMOTED|{a.date}"]) + "\n"

    if not a.apply:
        print("\n(dry-run — pass --apply to write collections + SSSOM and regenerate)")
        return

    save_yaml(mapped, MAPPED, validate=True, target_class="IngredientCollection")
    save_yaml(unmapped, UNMAPPED, validate=True, target_class="IngredientCollection")
    lines = SSSOM.read_text().splitlines(keepends=True)
    header_i = next(i for i, l in enumerate(lines) if not l.startswith("#"))
    at = _sorted_insert(lines, header_i, pref, row)
    SSSOM.write_text("".join(lines))
    print(f"  wrote collections + SSSOM row at line {at + 1}")

    print("\nRegenerating per-record files + docs ...")
    subprocess.run([sys.executable, str(ROOT / "scripts" / "export_individual_records.py")], check=True, cwd=ROOT)
    subprocess.run([sys.executable, str(ROOT / "scripts" / "export_lists.py")], check=True, cwd=ROOT)
    print("\nVerifying ...")
    subprocess.run([sys.executable, str(ROOT / "scripts" / "reconcile_sssom.py")], cwd=ROOT)
    subprocess.run([sys.executable, str(ROOT / "scripts" / "validate_sssom_invariants.py")], cwd=ROOT)
    print(f"\nDone. {a.identifier} -> {a.to}. Run `just validate-products` + `just validate-strict` to confirm gates.")


if __name__ == "__main__":
    main()
