#!/usr/bin/env python3
"""Move MAPPED records into mapped_ingredients.yaml and publish them (#370).

`reconcile_sssom.py` reads only `data/curated/mapped_ingredients.yaml`. But most
promotion paths set `mapping_status: MAPPED` **in place**, wherever the record
happens to live, so a fully-curated record can sit in `unmapped_ingredients.yaml`
where the reconciler cannot see it — and its mapping is therefore never published
to `mappings/ingredient_mappings.sssom.tsv`, the artefact kg-microbe re-syncs.

`promote_resolved_unmapped.py` gets this right and always has: its docstring says
"Move + transform the record from unmapped_ingredients.yaml into
mapped_ingredients.yaml", and it pops from one collection and inserts into the
other while fixing both header counts. The records this script moves were
promoted by other paths that skipped that step.

Everything here follows `promote_resolved_unmapped`'s own conventions, imported
rather than restated so the two cannot drift:

* the SSSOM subject is `MIM:<existing per-record filename stem>`, taken from
  `collect_existing_filenames`. Deriving it from the label instead is wrong —
  real subjects preserve hyphens (`MIM:Thiamine-hcl_X_2_H2o`), and a re-derived
  subject silently matches nothing. That mistake has now been made three times in
  this corpus, twice by me.
* `PREDICATE` / `CONFIDENCE` / `OBJECT_SOURCE` / `REGISTRY_SOURCE` decide the row.
  A `FALLBACK_REGISTRY` record maps to `skos:closeMatch` against its own mint,
  and that single self-referential row IS its registry row — Rule B1 fires only
  on narrowMatch, so no second row is needed or wanted.

Records already carrying an SSSOM row are moved but not re-published.

    python scripts/move_mapped_out_of_unmapped_collection.py            # dry-run
    python scripts/move_mapped_out_of_unmapped_collection.py --apply
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "src"))
sys.path.insert(0, str(ROOT / "scripts"))
import yaml  # noqa: E402

from mediaingredientmech.utils.yaml_handler import save_yaml  # noqa: E402
from export_individual_records import (  # noqa: E402
    collect_existing_filenames, sanitize_filename,
)
from promote_resolved_unmapped import (  # noqa: E402
    CONFIDENCE, OBJECT_SOURCE, PREDICATE, REGISTRY_SOURCE, is_registry_mint,
)

MAPPED = ROOT / "data" / "curated" / "mapped_ingredients.yaml"
UNMAPPED = ROOT / "data" / "curated" / "unmapped_ingredients.yaml"
SSSOM = ROOT / "mappings" / "ingredient_mappings.sssom.tsv"
DATE = "2026-08-15"
CURATOR = "move_mapped_out_of_unmapped_collection"
ISSUE = "#370"


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--apply", action="store_true")
    args = ap.parse_args(argv)

    mapped = yaml.safe_load(MAPPED.read_text(encoding="utf-8")) or {}
    unmapped = yaml.safe_load(UNMAPPED.read_text(encoding="utf-8")) or {}
    index = collect_existing_filenames(ROOT / "data" / "ingredients")

    existing_subjects = set()
    lines = SSSOM.read_text(encoding="utf-8").splitlines(keepends=True)
    for line in lines:
        if line.startswith("#"):
            continue
        cells = line.split("\t")
        if len(cells) >= 2:
            existing_subjects.add(cells[1])

    movers = [r for r in unmapped.get("ingredients", []) or []
              if r.get("mapping_status") == "MAPPED"]
    moved, published, already, skipped = [], [], [], []
    rows: list[str] = []

    for rec in movers:
        pref = str(rec.get("preferred_term") or "")
        om = rec.get("ontology_mapping") or {}
        term = str(om.get("ontology_id") or "")
        grade = str(om.get("mapping_quality") or "")
        if not term or grade not in PREDICATE:
            skipped.append(f"{pref}: ontology_id={term!r} quality={grade!r} — not publishable")
            continue

        rec.setdefault("curation_history", []).append({
            "timestamp": f"{DATE}T00:00:00+00:00", "curator": CURATOR,
            "action": "MOVED_TO_MAPPED_COLLECTION",
            "changes": (
                f"Moved from unmapped_ingredients.yaml to mapped_ingredients.yaml "
                f"({ISSUE}). The record was already MAPPED; it had been promoted in "
                f"place by a path that does not move between collections, and "
                f"reconcile_sssom reads only the mapped collection — so its mapping "
                f"was curated but unpublished."),
            "llm_assisted": False})
        moved.append(pref)

        if pref in existing_subjects:
            already.append(pref)
            continue

        slug = index.for_record(rec) or sanitize_filename(pref)
        prefix = term.split(":", 1)[0]
        source = (REGISTRY_SOURCE.get(prefix, "") if is_registry_mint(term)
                  else OBJECT_SOURCE.get(prefix.upper(), ""))
        label = str(om.get("ontology_label") or pref)
        rows.append("\t".join([
            f"MIM:{slug}", pref, PREDICATE[grade], term, label, source,
            "semapv:ManualMappingCuration",
            f"MIM:curation ({ISSUE})|MIM:curator={CURATOR}", DATE,
            CONFIDENCE[grade], "", "",
            f"manual:{CURATOR}|MOVED|{DATE}"]) + "\n")
        published.append(f"{pref[:38]:<40} {PREDICATE[grade]:<18} {term}")

        # Rule B1: a narrowMatch from a MIM subject needs a sibling registry
        # exactMatch row whose object's local part equals the subject slug. A
        # FALLBACK_REGISTRY record needs none — its closeMatch row to its own
        # mint already IS that row, and B1 fires only on narrow/broadMatch.
        ident = str(rec.get("identifier") or "")
        if PREDICATE[grade] == "skos:narrowMatch" and is_registry_mint(ident):
            rows.append("\t".join([
                f"MIM:{slug}", pref, "skos:exactMatch", ident, pref,
                REGISTRY_SOURCE.get(ident.split(":", 1)[0], ""),
                "semapv:ManualMappingCuration",
                f"MIM:curation ({ISSUE})|MIM:curator={CURATOR}", DATE,
                CONFIDENCE[grade], "", "",
                f"manual:{CURATOR}|MOVED|{DATE}"]) + "\n")
            published.append(f"{'':<40} {'skos:exactMatch':<18} {ident}  (Rule B1 registry row)")

    if args.apply and moved:
        keep = [r for r in unmapped["ingredients"] if r not in movers or
                str(r.get("preferred_term")) in {s.split(":")[0] for s in skipped}]
        # rebuild explicitly: anything skipped stays behind
        skipped_labels = {s.split(":")[0] for s in skipped}
        keep = [r for r in unmapped["ingredients"]
                if r.get("mapping_status") != "MAPPED"
                or str(r.get("preferred_term")) in skipped_labels]
        actually_moved = [r for r in unmapped["ingredients"] if r not in keep]
        unmapped["ingredients"] = keep
        unmapped["total_count"] = len(keep)
        unmapped["unmapped_count"] = sum(
            1 for r in keep if r.get("mapping_status") == "UNMAPPED")
        mapped["ingredients"] = actually_moved + mapped["ingredients"]
        mapped["total_count"] = len(mapped["ingredients"])
        mapped["mapped_count"] = sum(
            1 for r in mapped["ingredients"] if r.get("mapping_status") == "MAPPED")
        save_yaml(mapped, MAPPED)
        save_yaml(unmapped, UNMAPPED)

        hdr = next(i for i, l in enumerate(lines) if l.startswith("subject_id"))
        ncols = len(lines[hdr].rstrip("\n").split("\t"))
        lines[hdr + 1:hdr + 1] = [
            "\t".join(r.rstrip("\n").split("\t")[:ncols]
                      + [""] * max(0, ncols - len(r.rstrip("\n").split("\t")))) + "\n"
            for r in rows]
        SSSOM.write_text("".join(lines), encoding="utf-8")

    print(f"{'APPLIED' if args.apply else 'DRY RUN (re-run with --apply)'} — "
          f"{len(moved)} moved, {len(published)} SSSOM row(s) added\n")
    print(f"  published ({len(published)}):")
    for p in published[:25]:
        print(f"     {p}")
    if len(published) > 25:
        print(f"     ... {len(published) - 25} more")
    if already:
        print(f"\n  moved but already had an SSSOM row ({len(already)}): {already}")
    for s in skipped:
        print(f"  SKIPPED {s}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
