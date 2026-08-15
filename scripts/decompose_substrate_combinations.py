#!/usr/bin/env python3
"""Decompose the `A + B` microbedecoder labels into their components (#213/#308).

37 microbedecoder labels state a composition in the label itself — `Formate+methanol`,
`Glucose + Yeast Extract`, `Peptone + Beef Extract + Yeast Extract`. All 37 sit at
`NEEDS_EXPERT` with **zero occurrences**, which implies a curator will one day find
an ontology term for them. None exists and none could: a combination is not a
substance, and no ontology has a term for "formate plus methanol".

So these are not a mapping problem, they are a *decomposition* problem. Each is
minted as a blend under the `#288` STOCK_SOLUTION convention and its constituents
are recorded in `components`, resolved against MIM's own label index.

**The label is the recipe source.** `IngredientRecord.components` requires that
composition be populated "only from a verifiable recipe source"; here the label
literally enumerates the constituents, so splitting on `+` transcribes rather than
infers. Nothing is added that the label does not say — no concentrations are
invented, and `concentration_value` is left unset because no label states one.

**Unresolved constituents keep their name and lose only their id.**
`component_id` is optional in the schema. `Yeast + Meat Extract + H2` records all
three parts; `Yeast` simply carries no id because MIM has no record for it
(`Yeast Extract` is a different thing). That is more useful than dropping the
record, and it makes the gap visible to anyone querying components for a null id.

**`ingredient_type` follows the constituents, not the label** — and *unresolved
is not the same as undefined*. A blend is `UNDEFINED_MIXTURE` only when one of
its constituents is itself an undefined preparation (an extract, peptone, digest
or body fluid). `1-butanol+CO2` stays `DEFINED_MEDIUM` even though MIM has no
`1-butanol` record: the substance is perfectly well defined, MIM simply lacks the
record. `Glucose + Acetate` is defined; `Glucose + Yeast Extract` is not.

    python scripts/decompose_substrate_combinations.py            # dry-run
    python scripts/decompose_substrate_combinations.py --apply
"""
from __future__ import annotations

import argparse
import csv
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "src"))
import yaml  # noqa: E402

from mediaingredientmech.utils.yaml_handler import save_yaml  # noqa: E402

MAPPED = ROOT / "data" / "curated" / "mapped_ingredients.yaml"
UNMAPPED = ROOT / "data" / "curated" / "unmapped_ingredients.yaml"
LABEL_INDEX = ROOT / "docs" / "data" / "label_index.csv"
STAMP = "2026-08-14T00:00:00+00:00"
CURATOR = "decompose_substrate_combinations"
ISSUE = "#213/#308"

SPLIT = re.compile(r"\s*\+\s*")
# Prefixes whose referent is itself an undefined preparation, so any blend
# containing one cannot be a DEFINED_MEDIUM however well the rest resolves.
UNDEFINED_PREFIXES = ("MICRO:", "FOODON:", "UBERON:", "ENVO:", "UNMAPPED")
# Unresolved is NOT the same as undefined. `1-butanol` is a perfectly defined
# chemical that MIM simply has no record for, so `1-butanol+CO2` is a
# DEFINED_MEDIUM with one component_id missing. Only names that denote a
# preparation or an abbreviation for one make the blend undefined.
UNDEFINED_UNRESOLVED = re.compile(
    r"extract|liquor|serum|fluid|digest|infusion|peptone|broth|yeast"
    r"|^PY$|^TYGVS$|^PYG|^BHI$|^GYPS$", re.IGNORECASE)


def norm(text: object) -> str:
    return re.sub(r"[^a-z0-9]", "", str(text or "").lower())


def slug(text: object) -> str:
    return re.sub(r"[^a-z0-9]+", "_", str(text).lower()).strip("_")


def load_index() -> dict[str, dict]:
    idx: dict[str, dict] = {}
    with LABEL_INDEX.open(encoding="utf-8") as fh:
        for row in csv.DictReader(fh):
            idx.setdefault(norm(row["label"]), row)
    return idx


def is_microbedecoder(rec: dict) -> bool:
    blob = yaml.safe_dump(
        {"h": rec.get("curation_history"),
         "e": (rec.get("ontology_mapping") or {}).get("evidence"),
         "s": rec.get("synonyms")}, default_flow_style=False)
    return "microbedecoder" in blob.lower()


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--apply", action="store_true")
    args = ap.parse_args(argv)

    idx = load_index()
    colls = {p: (yaml.safe_load(p.read_text(encoding="utf-8", errors="replace")) or {})
             for p in (MAPPED, UNMAPPED)}

    done: list[str] = []
    partial: list[str] = []
    for path, coll in colls.items():
        for rec in coll.get("ingredients", []) or []:
            if rec.get("mapping_status") not in ("NEEDS_EXPERT", "PENDING_REVIEW"):
                continue
            if not is_microbedecoder(rec):
                continue
            label = str(rec.get("preferred_term") or "")
            if "+" not in label:
                continue
            parts = [p.strip() for p in SPLIT.split(label) if p.strip()]
            if len(parts) < 2:
                continue

            components = []
            unresolved = []
            for part in parts:
                hit = idx.get(norm(part))
                comp = {"component_name": part,
                        "source": f"MIM label decomposition ({ISSUE})"}
                if hit:
                    comp["component_id"] = hit["identifier"]
                else:
                    unresolved.append(part)
                components.append(comp)

            ids = [c.get("component_id", "") for c in components]
            undefined = (any(str(i).startswith(UNDEFINED_PREFIXES) for i in ids)
                         or any(UNDEFINED_UNRESOLVED.search(u) for u in unresolved))
            itype = "UNDEFINED_MIXTURE" if undefined else "DEFINED_MEDIUM"

            old_id = rec.get("identifier")
            new_id = f"kgmicrobe.ingredient:{slug(label)}"
            rec["identifier"] = new_id
            rec["mapping_status"] = "MAPPED"
            rec["ingredient_type"] = itype
            rec["components"] = components

            why = (
                f"The label enumerates its own constituents, so this is a decomposition "
                f"rather than a mapping: no ontology has a term for {label!r}, and none "
                f"could — a combination is not a substance. Minted under the #288 "
                f"STOCK_SOLUTION convention and split on '+', which transcribes the label "
                f"rather than inferring anything. {len(components) - len(unresolved)} of "
                f"{len(components)} constituents resolve to existing MIM records via "
                f"docs/data/label_index.csv"
                + (f"; {', '.join(unresolved)} carr{'ies' if len(unresolved) == 1 else 'y'} "
                   f"no component_id because MIM has no record for "
                   f"{'it' if len(unresolved) == 1 else 'them'}." if unresolved else ".")
                + f" ingredient_type={itype} because "
                + ("at least one constituent is itself an undefined preparation."
                   if undefined else
                   "every constituent is a defined chemical (an unresolved name here "
                   "means MIM lacks the record, not that the substance is undefined).")
                + " No concentrations are recorded: the label states none.")

            om = rec.setdefault("ontology_mapping", {})
            om.update({"ontology_id": new_id, "ontology_label": label,
                       "ontology_source": "kgmicrobe.ingredient",
                       "mapping_quality": "FALLBACK_REGISTRY"})
            om.setdefault("evidence", []).append({
                "evidence_type": "MANUAL_CURATION",
                "source": f"MIM curation ({ISSUE})", "notes": why})
            rec.setdefault("curation_history", []).append({
                "timestamp": STAMP, "curator": CURATOR, "action": "DECOMPOSED_TO_COMPONENTS",
                "previous_status": "NEEDS_EXPERT", "new_status": "MAPPED",
                "changes": f"{old_id} -> {new_id} (FALLBACK_REGISTRY). {why}",
                "llm_assisted": False})

            line = (f"{label[:44]:<46} {itype:<18} "
                    f"{len(components) - len(unresolved)}/{len(components)} resolved")
            (partial if unresolved else done).append(line)

    if args.apply and (done or partial):
        for path, coll in colls.items():
            save_yaml(coll, path)

    print(f"{'APPLIED' if args.apply else 'DRY RUN (re-run with --apply)'} — "
          f"{len(done) + len(partial)} decomposed\n")
    print(f"  every constituent resolved ({len(done)}):")
    for d in sorted(done):
        print(f"     {d}")
    print(f"\n  some constituent unresolved — name kept, id omitted ({len(partial)}):")
    for p in sorted(partial):
        print(f"     {p}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
