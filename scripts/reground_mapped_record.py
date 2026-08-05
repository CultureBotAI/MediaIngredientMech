"""Move a MAPPED record to a different ontology term (#228).

`promote_resolved_unmapped.py` takes UNMAPPED -> CURIE. This is the other case:
a record that is already mapped, to the wrong term. It comes up whenever a
hydrate or salt was grounded to its anhydrous / free parent because nobody found
the specific term -- `Sodium glutamate monohydrate` sat on CHEBI:64243
(monosodium L-glutamate, anhydrous) while CHEBI:232425
(monosodium L-glutamate hydrate) existed all along.

That matters for recipes: the monohydrate is 187.13 g/mol against the
anhydrous 169.11, a 10.6% weigh-out difference.

In MIM the record `identifier` IS the CURIE, so a re-ground rewrites the
identifier, the ontology_mapping, and the SSSOM row's object columns. The
subject (preferred_term) does NOT change, so the row keeps its position.

The freed CURIE becomes available, which is usually the point: another record
that is genuinely that term can then be promoted onto it.

Refuses if the destination is already held, if the record is not MAPPED, or if
the destination is absent/obsolete in the local chebi.db. Dry-run by default.
"""

from __future__ import annotations

import argparse
import datetime as dt
import os
import sqlite3
import sys
from pathlib import Path

import yaml

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
from mediaingredientmech.utils.yaml_handler import save_yaml  # noqa: E402

ROOT = Path(__file__).resolve().parents[1]
MAPPED = ROOT / "data" / "curated" / "mapped_ingredients.yaml"
SSSOM = ROOT / "mappings" / "ingredient_mappings.sssom.tsv"
CHEBI_DB = Path(os.path.expanduser("~/.data/oaklib/chebi.db"))


def chebi_label(curie: str) -> str:
    con = sqlite3.connect(CHEBI_DB)
    row = con.execute(
        "select value from statements where subject=? and predicate='rdfs:label'",
        (curie,)).fetchone()
    if not row:
        raise SystemExit(f"{curie} has no rdfs:label in {CHEBI_DB} — absent or wrong id")
    dep = con.execute(
        "select value from statements where subject=? and predicate='owl:deprecated'",
        (curie,)).fetchone()
    if dep:
        raise SystemExit(f"{curie} is obsolete in ChEBI — pick a current term")
    return row[0]


def plan_sssom(subject_label: str, old_curie: str, new_curie: str, new_label: str) -> tuple[str, str]:
    """Rewrite the object columns in place. Subject is unchanged, so no re-sort."""
    lines = SSSOM.read_text().splitlines(keepends=True)
    header = next(i for i, ln in enumerate(lines) if ln.startswith("subject_id"))
    hits = [i for i, ln in enumerate(lines)
            if i > header and ln.split("\t")[1:2] == [subject_label]]
    if len(hits) != 1:
        raise SystemExit(
            f"expected exactly 1 SSSOM row with subject_label {subject_label!r}, "
            f"found {len(hits)}. Records carrying a Rule-B1 registry set (narrowMatch + "
            "kgmicrobe.compound: + cas:) have several rows — re-ground those by hand.")
    cols = lines[hits[0]].rstrip("\n").split("\t")
    if cols[3] != old_curie:
        raise SystemExit(f"SSSOM row object_id is {cols[3]}, expected {old_curie}")
    cols[3], cols[4] = new_curie, new_label
    eol = "\n" if lines[hits[0]].endswith("\n") else ""
    lines[hits[0]] = "\t".join(cols) + eol
    if not lines[-1].endswith("\n"):
        lines[-1] += "\n"
    return "".join(lines), f"object {old_curie} -> {new_curie} '{new_label}' (line {hits[0] + 1})"


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--identifier", required=True, help="the record's current CURIE")
    ap.add_argument("--to", required=True, help="the CURIE it should hold")
    ap.add_argument("--quality", default="EXACT_MATCH")
    ap.add_argument("--reason", required=True)
    ap.add_argument("--curator", default="reground_mapped_record")
    ap.add_argument("--apply", action="store_true")
    args = ap.parse_args()

    doc = yaml.safe_load(MAPPED.read_text())
    hits = [r for r in doc["ingredients"] if r["identifier"] == args.identifier]
    if len(hits) != 1:
        raise SystemExit(f"{args.identifier} matches {len(hits)} mapped records, expected 1")
    rec = hits[0]
    if rec.get("mapping_status") != "MAPPED":
        raise SystemExit(f"{args.identifier} is {rec.get('mapping_status')}, not MAPPED")
    if any(r["identifier"] == args.to for r in doc["ingredients"]):
        raise SystemExit(f"{args.to} is already held by another record — merge instead")

    new_label = chebi_label(args.to)
    stamp = dt.datetime.now(dt.timezone.utc).isoformat()
    old = args.identifier
    om = rec.setdefault("ontology_mapping", {})
    old_label = om.get("ontology_label")
    rec["identifier"] = args.to
    om.update({"ontology_id": args.to, "ontology_label": new_label,
               "mapping_quality": args.quality})
    rec.setdefault("curation_history", []).append({
        "timestamp": stamp, "curator": args.curator, "action": "CORRECTED",
        "changes": (f"Re-grounded {old} '{old_label}' -> {args.to} '{new_label}' "
                    f"({args.quality}). {args.reason}"),
        "previous_status": "MAPPED", "new_status": "MAPPED", "llm_assisted": True,
    })
    doc["generation_date"] = stamp

    sssom_text, moved = plan_sssom(rec["preferred_term"], old, args.to, new_label)
    print(f"{rec['preferred_term']!r}: {old} '{old_label}' -> {args.to} '{new_label}'")
    print(f"  SSSOM: {moved}")
    print(f"  {old} is now free")

    if not args.apply:
        print("\nDRY RUN -- nothing written. Pass --apply to write.")
        return 0
    save_yaml(doc, MAPPED, validate=True, target_class="IngredientCollection")
    SSSOM.write_text(sssom_text)
    print("\nwrote data/curated/mapped_ingredients.yaml + SSSOM")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
