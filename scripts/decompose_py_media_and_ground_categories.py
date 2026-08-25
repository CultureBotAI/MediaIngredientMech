#!/usr/bin/env python3
"""RETIRED one-time resolution of PY media and category rows (#213).

The component-bearing results were migrated to the typed partonomy contract in
#369. This historical script exits before reading or writing data because it would
recreate the old untyped shape and the non-partonomic Mono-/Disaccharides list.

Two treatments for the microbedecoder residual, both extending work already in
the corpus rather than inventing an approach.

## Decomposition (8)

`PY-` is peptone-yeast, the standard anaerobe base. The curated research file
already decomposed `PY-glucose-rumen Fluid` as peptone + yeast extract + glucose
+ rumen fluid, so the remaining `PY-` media follow that precedent exactly and the
expansion is not a guess. `Tryptone/yeast/beef (tyb)` is the same shape with
slashes, and its own parenthesised `(tyb)` confirms the reading.

The historical pass also decomposed `Mono- And Disaccharides`; #369 removed that
list because coordinated category members are not material parts. `Esculin Ferric
Citrate` remains a two-substance label enumeration.

## Category grounding (2)

A label that genuinely names a *category* should map to a ChEBI class — that is
what classes are for. This is the mirror image of #322, which found 145 records
mapping to structureless class terms: there the records named specific substances
and the class was wrong. Here the label names the category, so the class is right.

    Sugars                     -> CHEBI:16646 carbohydrate       NARROW_MATCH
    Poly-beta-hydroxyalkanoate -> CHEBI:78037 polyhydroxyalkanoate SYNONYM_MATCH

`Sugars` is a NARROW_MATCH because sugars are a proper subset of carbohydrates —
ChEBI carries no "sugar" synonym on CHEBI:16646, so this is a real subclass
relation rather than a naming variant. Rule B1 then requires a registry row, so
the record also takes a `kgmicrobe.compound:` mint.

`Poly-beta-hydroxyalkanoate` needs no mint: poly-β-hydroxyalkanoate and
polyhydroxyalkanoate are the same polymer class under two spellings, so the grade
is SYNONYM_MATCH and the predicate stays skos:exactMatch.

**Neither gets an SSSOM row.** Both records live in `unmapped_ingredients.yaml`,
and `reconcile_sssom.py` reads only `mapped_ingredients.yaml` (line 41), so a row
for a record in the other collection is an ORPHAN by construction. That matches
the corpus: 60 of the 62 MAPPED records currently sitting in the unmapped
collection have no SSSOM row either. The collection, not the status, decides
whether a mapping gets published — which is itself a defect, tracked separately.

**`Tetrazolium` is deliberately left alone.** ChEBI has no generic tetrazolium
class — only specific salts (`tetrazolium blue`, `tetrazolium violet`,
`2,3,5-triphenyltetrazolium chloride`). In media it is usually TTC as a redox
indicator, but "usually" is an inference, and matching the bare class name to one
of its members is the error #368 records for sulfur.

There is no supported invocation; both dry-run and ``--apply`` fail closed.
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "src"))
import yaml  # noqa: E402

from mediaingredientmech.utils.yaml_handler import save_yaml  # noqa: E402

MAPPED = ROOT / "data" / "curated" / "mapped_ingredients.yaml"
UNMAPPED = ROOT / "data" / "curated" / "unmapped_ingredients.yaml"
SSSOM = ROOT / "mappings" / "ingredient_mappings.sssom.tsv"
STAMP = "2026-08-15T00:00:00+00:00"
CURATOR = "decompose_py_media_and_ground_categories"
ISSUE = "#213/#308"

PY = [("peptone", "MICRO:0000178"), ("yeast extract", "FOODON:03315426")]
DECOMPOSE = {
    "PY-cellobiose": (PY + [("cellobiose", "CHEBI:17057")], "UNDEFINED_MIXTURE"),
    "PY-fructose": (PY + [("fructose", "CHEBI:28757")], "UNDEFINED_MIXTURE"),
    "PY-maltose": (PY + [("maltose", "CHEBI:17306")], "UNDEFINED_MIXTURE"),
    "PY-pectin": (PY + [("pectin", "CHEBI:17309")], "UNDEFINED_MIXTURE"),
    "PYG-0.02% Tween 80": (
        PY + [("glucose", "CHEBI:17234"), ("polysorbate 80", "CHEBI:53426")],
        "UNDEFINED_MIXTURE"),
    "Tryptone/yeast/beef (tyb)": (
        [("tryptone", "MICRO:0000182"), ("yeast extract", "FOODON:03315426"),
         ("beef extract", "FOODON:03302088")], "UNDEFINED_MIXTURE"),
    "Mono- And Disaccharides": (
        [("monosaccharide", "CHEBI:35381"), ("disaccharide", "CHEBI:36233")],
        "DEFINED_MEDIUM"),
    "Esculin Ferric Citrate": (
        [("esculin", "CHEBI:4853"), ("iron(III) citrate", "CHEBI:144421")],
        "DEFINED_MEDIUM"),
}
WHY_DECOMPOSE = {
    "Mono- And Disaccharides":
        "the label names two ChEBI classes, so it decomposes into them rather than "
        "grounding to either",
    "Esculin Ferric Citrate":
        "the label names two substances — esculin and ferric citrate, the latter an "
        "exact synonym of CHEBI:144421 iron(III) citrate",
    "Tryptone/yeast/beef (tyb)":
        "slash-separated constituents, with the parenthesised `(tyb)` confirming the "
        "reading",
}
DEFAULT_WHY = ("`PY-` is peptone-yeast, the standard anaerobe base. The curated research "
               "file already decomposes `PY-glucose-rumen Fluid` as peptone + yeast "
               "extract + glucose + rumen fluid, so this expansion follows an existing "
               "precedent in the corpus rather than a guess")

# label -> (identifier, ontology_id, ontology_label, grade, why)
GROUND = {
    "Sugars": (
        "kgmicrobe.compound:sugars", "CHEBI:16646", "carbohydrate", "NARROW_MATCH",
        "the label names a CATEGORY, and a ChEBI class is what a category should map "
        "to — the mirror image of #322, where records naming specific substances were "
        "wrongly on class terms. NARROW_MATCH because sugars are a proper subset of "
        "carbohydrates: ChEBI carries no `sugar` synonym on CHEBI:16646, so this is a "
        "real subclass relation and not a naming variant. Rule B1 then requires a "
        "sibling registry row, so the record takes a kgmicrobe.compound mint"),
    "Poly-beta-hydroxyalkanoate": (
        "CHEBI:78037", "CHEBI:78037", "polyhydroxyalkanoate", "SYNONYM_MATCH",
        "poly-beta-hydroxyalkanoate and polyhydroxyalkanoate are the same polymer "
        "class under two spellings — the beta- records the 3-hydroxy position that "
        "PHA implies — so this is a naming variant, not a subclass relation, and "
        "needs no registry mint"),
}


def slug(text: object) -> str:
    return re.sub(r"[^a-z0-9]+", "_", str(text).lower()).strip("_")


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--apply", action="store_true")
    args = ap.parse_args(argv)
    print(
        "error: this one-time decomposition writer is retired after the typed "
        "component-partonomy migration (#369); no files were read or written",
        file=sys.stderr,
    )
    return 2

    colls = {p: (yaml.safe_load(p.read_text(encoding="utf-8", errors="replace")) or {})
             for p in (MAPPED, UNMAPPED)}
    index: dict[str, dict] = {}
    for coll in colls.values():
        for rec in coll.get("ingredients", []) or []:
            index.setdefault(str(rec.get("preferred_term") or ""), rec)

    dec_out, gnd_out, skipped = [], [], []
    sssom_rows: list[tuple[str, str, str, str, str]] = []

    for label, (comps, itype) in DECOMPOSE.items():
        rec = index.get(label)
        if rec is None or rec.get("mapping_status") not in ("NEEDS_EXPERT", "PENDING_REVIEW"):
            skipped.append(f"{label}: absent or already resolved")
            continue
        old_id = rec.get("identifier")
        new_id = f"kgmicrobe.ingredient:{slug(label)}"
        why = WHY_DECOMPOSE.get(label, DEFAULT_WHY)
        rec["components"] = [
            {"component_name": n, "component_id": i,
             "source": f"MIM curation ({ISSUE})"} for n, i in comps]
        rec["ingredient_type"] = itype
        rec["identifier"] = new_id
        rec["mapping_status"] = "MAPPED"
        note = (f"Decomposed into {len(comps)} constituents: {why}. Minted under the "
                f"#288 STOCK_SOLUTION convention because no ontology term denotes the "
                f"blend itself. ingredient_type={itype}. No concentrations recorded — "
                f"the label states none"
                + (" beyond the 0.02% on the Tween, which is a working concentration "
                   "for the finished medium rather than a component amount"
                   if "0.02%" in label else "") + ".")
        om = rec.setdefault("ontology_mapping", {})
        om.update({"ontology_id": new_id, "ontology_label": label,
                   "ontology_source": "kgmicrobe.ingredient",
                   "mapping_quality": "FALLBACK_REGISTRY"})
        om.setdefault("evidence", []).append({
            "evidence_type": "MANUAL_CURATION",
            "source": f"MIM curation ({ISSUE})", "notes": note})
        rec.setdefault("curation_history", []).append({
            "timestamp": STAMP, "curator": CURATOR, "action": "DECOMPOSED_TO_COMPONENTS",
            "previous_status": "NEEDS_EXPERT", "new_status": "MAPPED",
            "changes": f"{old_id} -> {new_id} (FALLBACK_REGISTRY). {note}",
            "llm_assisted": False})
        dec_out.append(f"{label[:34]:<36} {itype:<18} {len(comps)} components")

    for label, (ident, onto_id, onto_label, grade, why) in GROUND.items():
        rec = index.get(label)
        if rec is None or rec.get("mapping_status") not in ("NEEDS_EXPERT", "PENDING_REVIEW"):
            skipped.append(f"{label}: absent or already resolved")
            continue
        old_id = rec.get("identifier")
        rec["identifier"] = ident
        rec["mapping_status"] = "MAPPED"
        note = f"Grounded to the ChEBI class {onto_id} ({onto_label!r}): {why}."
        om = rec.setdefault("ontology_mapping", {})
        om.update({"ontology_id": onto_id, "ontology_label": onto_label,
                   "ontology_source": "CHEBI", "mapping_quality": grade})
        om.setdefault("evidence", []).append({
            "evidence_type": "MANUAL_CURATION",
            "source": f"MIM curation ({ISSUE})", "notes": note})
        rec.setdefault("curation_history", []).append({
            "timestamp": STAMP, "curator": CURATOR, "action": "GROUNDED_TO_CHEBI_CLASS",
            "previous_status": "NEEDS_EXPERT", "new_status": "MAPPED",
            "changes": f"{old_id} -> {ident}; ontology_id {onto_id} ({grade}). {note}",
            "llm_assisted": False})
        pred = "skos:narrowMatch" if grade == "NARROW_MATCH" else "skos:exactMatch"
        sssom_rows.append((label, pred, onto_id, onto_label, ident))
        gnd_out.append(f"{label[:34]:<36} {onto_id} {onto_label[:24]:<26} {grade}")

    if args.apply and (dec_out or gnd_out):
        for path, coll in colls.items():
            save_yaml(coll, path)
        # No SSSOM rows: every record touched here lives in
        # unmapped_ingredients.yaml, which reconcile_sssom does not read, so any
        # row would be an immediate ORPHAN. See the module docstring.
        sssom_rows = []
        lines = SSSOM.read_text(encoding="utf-8").splitlines(keepends=True)
        hdr = next(i for i, l in enumerate(lines) if l.startswith("subject_id"))
        ncols = len(lines[hdr].rstrip("\n").split("\t"))
        new = []
        for label, pred, oid, olabel, ident in sssom_rows:
            subj = f"MIM:{re.sub(r'[^A-Za-z0-9]+', '_', label).strip('_')}"
            row = [subj, label, pred, oid, olabel, "obo:chebi.owl",
                   "semapv:ManualMappingCuration", f"MIM:curation ({ISSUE})", "2026-08-15"]
            new.append("\t".join(row + [""] * (ncols - len(row))) + "\n")
            if pred == "skos:narrowMatch":     # Rule B1 registry row
                reg = [subj, label, "skos:exactMatch", ident, label, "kgm:compound",
                       "semapv:ManualMappingCuration", f"MIM:curation ({ISSUE})",
                       "2026-08-15"]
                new.append("\t".join(reg + [""] * (ncols - len(reg))) + "\n")
        lines[hdr + 1:hdr + 1] = new
        SSSOM.write_text("".join(lines), encoding="utf-8")

    print(f"{'APPLIED' if args.apply else 'DRY RUN (re-run with --apply)'} — "
          f"{len(dec_out)} decomposed, {len(gnd_out)} grounded to a ChEBI class\n")
    print(f"  decomposed ({len(dec_out)}):")
    for d in dec_out:
        print(f"     {d}")
    print(f"\n  grounded to a ChEBI class ({len(gnd_out)}):")
    for g in gnd_out:
        print(f"     {g}")
    for s in skipped:
        print(f"  SKIPPED {s}")
    print("\n  Tetrazolium left alone: ChEBI has no generic tetrazolium class, only "
          "specific\n  salts. Matching a bare class name to one of its members is the "
          "error #368 records for sulfur.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
