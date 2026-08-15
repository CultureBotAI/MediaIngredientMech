#!/usr/bin/env python3
"""Apply the curated microbedecoder decompositions to the records (#213/#308).

`mappings/microbedecoder_residual_research_decomposition.tsv` holds 42 curated
decompositions — `source_label`, `strategy`, and a `component_curies` column of
`CURIE:label` pairs — produced by the microbedecoder research pass. **Nothing
ever wrote them into the records.** The file sat as a mapping artefact while the
records it describes stayed at `NEEDS_EXPERT`.

This applies it, and it supersedes the label-splitting in
`decompose_substrate_combinations.py`, which was derived independently before
this file was found. The curated column is strictly better on two counts:

*It resolves constituents a label split cannot.* `CMC + PY + Horse Serum` splits
into a literal `PY`, which resolves to nothing; the curated row expands it to
peptone + yeast extract. Likewise `Corn Steep Liquor` -> `cas:66071-94-1` and
`3-methyl mercaptopropionate` -> `CHEBI:1438`, both of which the split left
without an id.

*It covers labels that state no composition at all.* `PYG`, `PYGS`, `GYPS`,
`PYEG`, `BHI` are abbreviations — there is nothing to split on. The curated file
carries their expansions, which is the only way these become blends-of-ingredients
rather than opaque names.

Matching is on the normalised `source_label`, because the file's spelling and the
record's differ (`H2 + methanol` vs `H2+methanol`, `cyclopentanol+CO2` vs
`Cyclopentanol+CO2`).

Three strategies, all treated the same way structurally — the distinction is
recorded in the evidence rather than in the shape:

    split              the label names its constituents; components are those
    map_to_medium      a named medium; components are what the recipe contains
    map_to_ingredient  resolves to a single ingredient, so one component

Records still at NEEDS_EXPERT are promoted and minted under the #288
STOCK_SOLUTION convention. Records already minted keep their identifier and only
their `components` are replaced.

    python scripts/apply_curated_decompositions.py            # dry-run
    python scripts/apply_curated_decompositions.py --apply
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
CURATED = ROOT / "mappings" / "microbedecoder_residual_research_decomposition.tsv"
STAMP = "2026-08-14T00:00:00+00:00"
CURATOR = "apply_curated_decompositions"
ISSUE = "#213/#308"

UNDEFINED_PREFIXES = ("MICRO:", "FOODON:", "UBERON:", "ENVO:", "UNMAPPED", "cas:")

# CultureMech media these blends resolve to, VERIFIED BY COMPOSITION rather than
# by name — fuzzy name matching is what put `KF` on Lys-Phe. Recorded in
# `culturemech_medium_name`, the slot whose stated purpose is to "link complex
# media entries to their full recipe formulations".
#
# Only two of the twelve survive that check. `Modified Cooked Meat Medium` matches
# `cooked_meat_medium`, which is the UNmodified one; `Fastidious Anaerobe Broth
# With Meat Granules` matches a broth carrying no meat granules; `PYG` is
# ambiguous across six CultureMech variants (`pyg_medium`, `pyg_medium_i`,
# `pyg_medium_b`, `pyg_medium_c`, `pyg_medium_modified`, `pyg_agar_h`) and
# picking one would be a guess. The rest have no CultureMech medium at all.
CULTUREMECH_MEDIUM = {
    "BHI": ("CultureMech:015492", "BHI",
            "composition Beef heart + Calf brains + Proteose Peptone + Disodium "
            "phosphate + Sodium Chloride is brain heart infusion"),
    "GYPS": ("CultureMech:002799", "gyps_medium",
             "name matches exactly and 3 of 4 curated constituents agree (glucose, "
             "peptone, yeast extract); CultureMech additionally lists MES and Sea "
             "Salt and no starch, so the recipes are close but not identical"),
}
STRATEGY_WHY = {
    "split": "the label names its constituents",
    "map_to_medium": "it is a named medium and these are what the recipe contains",
    "map_to_ingredient": "it resolves to a single named ingredient",
}


def norm(text: object) -> str:
    return re.sub(r"[^a-z0-9]", "", str(text or "").lower())


def slug(text: object) -> str:
    return re.sub(r"[^a-z0-9]+", "_", str(text).lower()).strip("_")


def parse_components(cell: str) -> list[dict]:
    """`CHEBI:17234:glucose|MICRO:0000178:peptone` -> component dicts.

    The CURIE itself contains a colon, so split from the right on the FIRST two
    fields only: prefix:accession:label.
    """
    out = []
    for chunk in str(cell or "").split("|"):
        chunk = chunk.strip()
        if not chunk:
            continue
        parts = chunk.split(":")
        if len(parts) >= 3:
            curie = ":".join(parts[:2])
            label = ":".join(parts[2:]).strip()
        elif len(parts) == 2:
            # A pseudo-prefix marking a constituent with no CURIE, e.g.
            # `VFA_mix:volatile fatty acid mixture (undefined)`. Keep the human
            # name and drop the marker — carrying `VFA_mix:` into component_name
            # would publish a prefix that resolves to nothing.
            curie, label = "", parts[1].strip()
        else:
            curie, label = "", chunk
        comp = {"component_name": label or curie}
        if curie:
            comp["component_id"] = curie
        comp["source"] = f"microbedecoder research decomposition ({ISSUE})"
        out.append(comp)
    return out


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--apply", action="store_true")
    args = ap.parse_args(argv)

    curated = {}
    with CURATED.open(encoding="utf-8") as fh:
        for row in csv.DictReader(fh, delimiter="\t"):
            curated.setdefault(norm(row["source_label"]), row)

    colls = {p: (yaml.safe_load(p.read_text(encoding="utf-8", errors="replace")) or {})
             for p in (MAPPED, UNMAPPED)}
    promoted, refreshed, skipped = [], [], []
    seen = set()

    for path, coll in colls.items():
        for rec in coll.get("ingredients", []) or []:
            label = str(rec.get("preferred_term") or "")
            row = curated.get(norm(label))
            if row is None:
                continue
            seen.add(norm(label))
            comps = parse_components(row["component_curies"])
            if not comps:
                skipped.append(f"{label}: curated row has no component_curies")
                continue

            ids = [c.get("component_id", "") for c in comps]
            undefined = any(str(i).startswith(UNDEFINED_PREFIXES) for i in ids) or \
                any(not i for i in ids)
            itype = "UNDEFINED_MIXTURE" if undefined else "DEFINED_MEDIUM"
            was_expert = rec.get("mapping_status") in ("NEEDS_EXPERT", "PENDING_REVIEW")

            rec["components"] = comps
            rec["ingredient_type"] = itype
            cm = CULTUREMECH_MEDIUM.get(label)
            if cm:
                rec["culturemech_medium_name"] = cm[1]

            why = (
                f"Components taken from the curated microbedecoder research "
                f"decomposition (mappings/microbedecoder_residual_research_"
                f"decomposition.tsv, strategy={row['strategy']}): "
                f"{STRATEGY_WHY.get(row['strategy'], row['strategy'])}. "
                f"{len(comps)} constituent(s), "
                f"{sum(1 for i in ids if i)} carrying an identifier. "
                f"That file was produced by the research pass and never written into "
                f"the records; this applies it. It resolves constituents a label split "
                f"cannot — abbreviations such as PY, and named media such as BHI, state "
                f"no composition to split on. ingredient_type={itype}. No concentrations "
                f"are recorded: the curated row states none."
                + (f" Cross-referenced to CultureMech medium {cm[0]} ({cm[1]!r}) via "
                   f"culturemech_medium_name, verified by COMPOSITION not by name: "
                   f"{cm[2]}." if cm else ""))

            if was_expert:
                old_id = rec.get("identifier")
                new_id = f"kgmicrobe.ingredient:{slug(label)}"
                rec["identifier"] = new_id
                rec["mapping_status"] = "MAPPED"
                om = rec.setdefault("ontology_mapping", {})
                om.update({"ontology_id": new_id, "ontology_label": label,
                           "ontology_source": "kgmicrobe.ingredient",
                           "mapping_quality": "FALLBACK_REGISTRY"})
                om.setdefault("evidence", []).append({
                    "evidence_type": "MANUAL_CURATION",
                    "source": f"MIM curation ({ISSUE})", "notes": why})
                rec.setdefault("curation_history", []).append({
                    "timestamp": STAMP, "curator": CURATOR,
                    "action": "DECOMPOSED_FROM_CURATED_RESEARCH",
                    "previous_status": "NEEDS_EXPERT", "new_status": "MAPPED",
                    "changes": f"{old_id} -> {new_id} (FALLBACK_REGISTRY). {why}",
                    "llm_assisted": False})
                promoted.append(f"{label[:42]:<44} {itype:<18} {len(comps)} components")
            else:
                rec.setdefault("curation_history", []).append({
                    "timestamp": STAMP, "curator": CURATOR,
                    "action": "REPLACED_COMPONENTS_WITH_CURATED",
                    "changes": (f"components replaced with the curated research "
                                f"decomposition, superseding the label split. {why}"),
                    "llm_assisted": False})
                refreshed.append(f"{label[:42]:<44} {itype:<18} {len(comps)} components")

    unseen = [r["source_label"] for k, r in curated.items() if k not in seen]

    if args.apply and (promoted or refreshed):
        for path, coll in colls.items():
            save_yaml(coll, path)

    print(f"{'APPLIED' if args.apply else 'DRY RUN (re-run with --apply)'} — "
          f"{len(promoted)} promoted, {len(refreshed)} refreshed\n")
    print(f"  promoted from NEEDS_EXPERT and minted ({len(promoted)}):")
    for p in sorted(promoted):
        print(f"     {p}")
    print(f"\n  components replaced with the curated set ({len(refreshed)}):")
    for r in sorted(refreshed):
        print(f"     {r}")
    if unseen:
        print(f"\n  curated rows with no matching record ({len(unseen)}):")
        for u in sorted(unseen):
            print(f"     {u}")
    for s in skipped:
        print(f"  SKIPPED {s}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
