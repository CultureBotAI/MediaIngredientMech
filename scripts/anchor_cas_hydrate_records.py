"""Give a `cas:`-identified record its Section 3 anchor rows (#239).

MAPPING_SEMANTICS.md Section 3 step 2: a substance with no exact ontology term
takes `cas:<its own CAS>` as its identifier, a `skos:narrowMatch` to the nearest
ontology parent, AND the Rule B1 registry row. 34 hydrate records satisfy all
three. 22 have only the `cas:` id — they assert no parent at all, so Rule B1
never fires on them (it only requires a registry row for a subject that already
asserts a narrowMatch) and they are invisible to the rule rather than violating
it. That is the "healthiest when it has stopped working" shape.

This adds the two missing rows and points the record's ontology_mapping at the
parent with NARROW_MATCH, leaving the identifier alone.

Input TSV columns: preferred_term, parent_curie, rationale.
Dry-run by default; pass --apply.
"""

from __future__ import annotations

import argparse
import csv
import datetime as dt
import io
import os
import sqlite3
import sys
from pathlib import Path

import yaml

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
sys.path.insert(0, str(Path(__file__).resolve().parent))
from export_individual_records import sanitize_filename  # noqa: E402
from mediaingredientmech.utils.yaml_handler import save_yaml  # noqa: E402

ROOT = Path(__file__).resolve().parents[1]
MAPPED = ROOT / "data" / "curated" / "mapped_ingredients.yaml"
SSSOM = ROOT / "mappings" / "ingredient_mappings.sssom.tsv"
CHEBI_DB = Path(os.path.expanduser("~/.data/oaklib/chebi.db"))


def chebi_label(curie: str) -> str:
    con = sqlite3.connect(CHEBI_DB)
    row = con.execute("select value from statements where subject=? and predicate='rdfs:label'",
                      (curie,)).fetchone()
    if not row:
        raise SystemExit(f"{curie} has no rdfs:label in chebi.db")
    if con.execute("select 1 from statements where subject=? and predicate='owl:deprecated'",
                   (curie,)).fetchone():
        raise SystemExit(f"{curie} is obsolete in ChEBI")
    return row[0]


def sssom_parts() -> tuple[list[str], int, list[dict], list[str]]:
    lines = SSSOM.read_text().splitlines(keepends=True)
    start = next(i for i, ln in enumerate(lines) if ln.startswith("subject_id"))
    fields = lines[start].rstrip("\n").split("\t")
    rows = list(csv.DictReader(io.StringIO("".join(lines[start:])), delimiter="\t"))
    return lines, start, rows, fields


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--plan", required=True, type=Path)
    ap.add_argument("--curator", default="anchor_cas_hydrate_records")
    ap.add_argument("--date", default="2026-08-05")
    ap.add_argument("--apply", action="store_true")
    args = ap.parse_args()

    doc = yaml.safe_load(MAPPED.read_text())
    by_term: dict[str, list[dict]] = {}
    for r in doc["ingredients"]:
        by_term.setdefault(r["preferred_term"], []).append(r)

    lines, start, rows, fields = sssom_parts()
    have_parent = {r["subject_label"] for r in rows
                   if r["predicate_id"] in ("skos:narrowMatch", "skos:broadMatch")}
    have_registry = {r["subject_label"] for r in rows
                     if r["predicate_id"] == "skos:exactMatch"
                     and r["object_id"].startswith("kgmicrobe.")}

    with args.plan.open() as fh:
        plan = list(csv.DictReader(fh, delimiter="\t"))

    stamp = dt.datetime.now(dt.timezone.utc).isoformat()
    new_rows: list[str] = []
    done, problems = [], []

    for p in plan:
        term, parent = p["preferred_term"].strip(), p["parent_curie"].strip()
        recs = by_term.get(term, [])
        recs = [r for r in recs if str(r["identifier"]).startswith("cas:")]
        if len(recs) != 1:
            problems.append(f"{term!r}: {len(recs)} cas:-identified records, expected 1")
            continue
        rec = recs[0]
        if rec.get("mapping_status") != "MAPPED":
            problems.append(f"{term!r}: status {rec.get('mapping_status')}, not MAPPED")
            continue
        label = chebi_label(parent)
        slug = sanitize_filename(term)
        registry = f"kgmicrobe.compound:{slug.lower()}"

        om = rec.setdefault("ontology_mapping", {})
        om.update({"ontology_id": parent, "ontology_label": label,
                   "ontology_source": "CHEBI", "mapping_quality": "NARROW_MATCH"})
        om.setdefault("evidence", []).append({
            "evidence_type": "DATABASE_MATCH", "source": args.curator,
            "notes": (f"{term} is a hydrate/salt with its own CAS and no exact ChEBI term; "
                      f"anchored to the parent {parent} '{label}' by narrowMatch per "
                      f"MAPPING_SEMANTICS.md Section 3 step 2. {p['rationale']}")})
        rec.setdefault("curation_history", []).append({
            "timestamp": stamp, "curator": args.curator, "action": "CORRECTED",
            "changes": (f"Added Section 3 anchor rows: narrowMatch {parent} '{label}' and "
                        f"registry {registry}. identifier {rec['identifier']} unchanged; "
                        f"mapping_quality FALLBACK_REGISTRY -> NARROW_MATCH. {p['rationale']}"),
            "llm_assisted": True})

        base = {f: "" for f in fields}
        base.update({"subject_id": f"MIM:{slug}", "subject_label": term,
                     "mapping_justification": "semapv:ManualMappingCuration",
                     "source": f"MIM:{args.curator}|MIM:curator={args.curator}",
                     "mapping_date": args.date})
        if term not in have_parent:
            r = dict(base, predicate_id="skos:narrowMatch", object_id=parent,
                     object_label=label, object_source="obo:chebi.owl", confidence="0.9")
            new_rows.append("\t".join(r[f] for f in fields) + "\n")
        if term not in have_registry:
            r = dict(base, predicate_id="skos:exactMatch", object_id=registry,
                     object_label=term, object_source="kgm:compound", confidence="0.99",
                     comment=f"Registry/identity row preserving {registry} alongside parent {parent}.")
            new_rows.append("\t".join(r[f] for f in fields) + "\n")
        done.append((rec["identifier"], term, parent, label))

    print(f"anchored {len(done)}/{len(plan)}; {len(new_rows)} SSSOM row(s) to add\n")
    for ident, term, parent, label in done:
        print(f"  {ident:20} {term[:38]:38} --narrowMatch--> {parent} '{label}'")
    if problems:
        print(f"\n{len(problems)} problem(s):")
        for x in problems:
            print(f"   {x}")
        print("\nRefusing to write a partial batch.")
        return 1

    doc["generation_date"] = stamp
    if not args.apply:
        print("\nDRY RUN -- nothing written. Pass --apply to write.")
        return 0

    save_yaml(doc, MAPPED, validate=True, target_class="IngredientCollection")
    # insert each row at its sorted position rather than re-sorting the file: the
    # SSSOM is only *de facto* sorted (it has ~113 case-insensitive ordering
    # resets), so a global sort would reorder ~2600 unrelated rows.
    out = list(lines)
    for row in new_rows:
        label = row.split("\t")[1]
        i = start + 1
        while i < len(out):
            cols = out[i].split("\t")
            if len(cols) > 1 and cols[1].strip() and cols[1] > label:
                break
            i += 1
        out.insert(i, row)
    if not out[-1].endswith("\n"):
        out[-1] += "\n"
    SSSOM.write_text("".join(out))
    print("\nwrote data/curated/mapped_ingredients.yaml + SSSOM")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
