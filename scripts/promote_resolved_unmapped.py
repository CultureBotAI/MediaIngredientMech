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
# Ontologies this helper can resolve a target in. NCIT matters because it carries
# drugs and reagents ChEBI's semsql build lags on -- Polymyxin B, Lysostaphin,
# Colistin Sulfate and Carbomycin all have exact NCIT labels while their CHEBI
# accessions are absent locally, so a CHEBI-only helper called them unresolvable.
_OAK = Path.home() / ".data" / "oaklib"
ONTOLOGY_DB = {"CHEBI": CHEBI_DB, "NCIT": _OAK / "ncit.db",
               "FOODON": _OAK / "foodon.db", "ENVO": _OAK / "envo.db",
               # MeSH is written lowercase in MIM records (mesh:C017721) but
               # uppercase inside the build, so lookups upper-case the prefix.
               "MESH": _OAK / "mesh.db"}
OBJECT_SOURCE = {"CHEBI": "obo:chebi.owl", "NCIT": "obo:ncit.owl",
                 "FOODON": "obo:foodon.owl", "ENVO": "obo:envo.owl",
                 "MESH": "registry:mesh"}

PREDICATE = {"EXACT_MATCH": "skos:exactMatch", "SYNONYM_MATCH": "skos:exactMatch",
             "CLOSE_MATCH": "skos:closeMatch", "NARROW_MATCH": "skos:narrowMatch",
             # The record IS its mint; closeMatch is what the 136 existing
             # self-referential registry records use, and it keeps Rule B1 (which
             # fires only on narrowMatch) out of the picture.
             "FALLBACK_REGISTRY": "skos:closeMatch"}
CONFIDENCE = {"EXACT_MATCH": "0.99", "SYNONYM_MATCH": "0.95", "CLOSE_MATCH": "0.9",
              "NARROW_MATCH": "0.9", "FALLBACK_REGISTRY": "0.9"}

# The Section 3 registry namespaces, imported rather than re-declared so the two
# scripts that can perform this move cannot drift apart (#279).
from reground_mapped_record import (  # noqa: E402
    REGISTRY_PREFIXES, REGISTRY_SOURCE, check_registry_mint, is_registry_mint,
)


def canonical_label(cid: str) -> str:
    prefix = cid.split(":", 1)[0].upper()
    cid = f"{prefix}:{cid.split(':', 1)[1]}"      # builds store the prefix uppercase
    db = ONTOLOGY_DB.get(prefix)
    if db is None:
        raise SystemExit(f"{cid}: no local build configured for prefix {prefix!r} "
                         f"(have {', '.join(sorted(ONTOLOGY_DB))})")
    if not db.exists():
        raise SystemExit(f"{cid}: {db} is missing — the {prefix} build is not downloaded")
    con = sqlite3.connect(f"file:{db}?mode=ro", uri=True)
    row = con.execute("SELECT value FROM statements WHERE subject=? AND predicate='rdfs:label'", (cid,)).fetchone()
    dep = con.execute("SELECT 1 FROM statements WHERE subject=? AND predicate='owl:deprecated'", (cid,)).fetchone()
    con.close()
    if not row:
        raise SystemExit(f"{cid} has no rdfs:label in {db.name} (absent / wrong id)")
    if dep:
        raise SystemExit(f"{cid} is obsolete in {prefix} — pick a current term")
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
    ap.add_argument("--to", required=True,
                    help=("target CHEBI CURIE, e.g. CHEBI:30915 — or a registry mint "
                          "(cas: / kgmicrobe.compound: / kgmicrobe.ingredient:) when no "
                          "ontology term denotes the substance, which then requires "
                          "--parent"))
    ap.add_argument("--parent",
                    help=("REQUIRED when --to is a registry mint: the ontology term to "
                          "narrowMatch (MAPPING_SEMANTICS.md Section 3)"))
    ap.add_argument("--quality", default="EXACT_MATCH", choices=list(PREDICATE))
    ap.add_argument("--evidence-source", default="promote_resolved_unmapped")
    ap.add_argument("--note", default="")
    ap.add_argument("--date", default="2026-06-16")
    ap.add_argument("--apply", action="store_true")
    a = ap.parse_args()
    minted = is_registry_mint(a.to)
    if minted:
        # Section 3: the mint denotes the substance, the parent is what the record
        # maps to. Validate and record the parent; the mint is validated by shape.
        if a.quality == "FALLBACK_REGISTRY":
            # The second established registry shape: no ontology term denotes this
            # substance at all, so the mint IS the mapping. ontology_id is the mint
            # itself (self-referential), matching the 82 FALLBACK_REGISTRY and 54
            # PLACEHOLDER records already in the corpus. Requiring a parent here
            # would force a narrowMatch to whatever class happens to be nearest --
            # the over-claim #270 tracks.
            if a.parent:
                raise SystemExit("--parent does not apply to FALLBACK_REGISTRY: the "
                                 "point of the shape is that no ontology term denotes it")
            term_curie = None          # resolved to the mint after slug derivation
        elif not a.parent:
            raise SystemExit(
                f"--to {a.to} is a registry mint, so --parent is required (or pass "
                "--quality FALLBACK_REGISTRY if NO ontology term denotes it).\n"
                "MAPPING_SEMANTICS.md Section 3: a substance with no exact ontology "
                "term takes its registry CURIE as identifier AND asserts a narrowMatch "
                "to the nearest parent. Rule B1 then requires both SSSOM rows.")
        elif a.parent.split(":", 1)[0].upper() not in ONTOLOGY_DB:
            raise SystemExit(f"--parent must be one of {', '.join(sorted(ONTOLOGY_DB))}")
        if a.parent:
            a.quality = "NARROW_MATCH"
            term_curie = a.parent
    else:
        if a.parent:
            raise SystemExit("--parent applies only when --to is a registry mint")
        if a.to.split(":", 1)[0].upper() not in ONTOLOGY_DB:
            raise SystemExit(f"this helper promotes to {', '.join(sorted(ONTOLOGY_DB))} ids "
                             "or a registry mint")
        if a.quality == "NARROW_MATCH":
            raise SystemExit(
                "NARROW_MATCH on an ontology destination needs a registry identifier "
                "too (Rule B1). Pass --to <cas:/kgmicrobe.compound: mint> --parent "
                f"{a.to} instead.")
        term_curie = a.to

    label = canonical_label(term_curie) if term_curie else None
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
    if minted:
        # Derived from the subject slug, not trusted from the caller: Rule B1 matches
        # the mint's local part against it exactly, and a mismatch only surfaces after
        # the write, as a CI failure on an already-published row.
        a.to = check_registry_mint(a.to, slug)
        if term_curie is None:
            # FALLBACK_REGISTRY: the mint IS the mapping, and its label is the
            # record's own preferred_term -- there is no ontology label to borrow.
            term_curie, label = a.to, pref
    print(f"Promote {a.identifier} ({pref!r}) -> {a.to}"
          + (f"  [FALLBACK_REGISTRY — no ontology term denotes this]"
             if a.quality == "FALLBACK_REGISTRY"
             else f"  [narrowMatch {term_curie} {label!r}]" if minted
             else f" {label!r}  [{a.quality}]"))
    print(f"  SSSOM: MIM:{slug}  {PREDICATE[a.quality]}  {term_curie}  '{label}'"
          f"  conf={CONFIDENCE[a.quality]}")
    if minted and a.quality == "NARROW_MATCH":
        print(f"  SSSOM: MIM:{slug}  skos:exactMatch  {a.to}  (Rule B1 registry row)")

    # transform the record
    rec["identifier"] = a.to
    rec["ontology_mapping"] = {
        "ontology_id": term_curie, "ontology_label": label,
        "ontology_source": term_curie.split(":", 1)[0].upper(),
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
    review = f"manual:promote_resolved_unmapped|PROMOTED|{a.date}"
    row = "\t".join([f"MIM:{slug}", pref, PREDICATE[a.quality], term_curie, label,
                     (REGISTRY_SOURCE.get(term_curie.split(":", 1)[0], "")
                      if is_registry_mint(term_curie)
                      else OBJECT_SOURCE.get(term_curie.split(":", 1)[0].upper(), "")),
                     "semapv:ManualMappingCuration", src, a.date,
                     CONFIDENCE[a.quality], "", "", review]) + "\n"
    if minted and a.quality == "NARROW_MATCH":
        # Rule B1: a narrowMatch from a MIM subject must carry a sibling registry
        # exactMatch row, or validate_sssom_invariants rejects the file. A
        # FALLBACK_REGISTRY record has no narrowMatch, so its single closeMatch row
        # to the mint IS the registry row -- a second one would just duplicate it.
        registry = REGISTRY_SOURCE.get(a.to.split(":", 1)[0], "")
        row += "\t".join([f"MIM:{slug}", pref, "skos:exactMatch", a.to, pref, registry,
                          "semapv:ManualMappingCuration", src, a.date, "0.99",
                          "", "", review]) + "\n"

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
