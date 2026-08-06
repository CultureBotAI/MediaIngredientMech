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

Refuses if the destination is already held (by a non-tombstoned record), if the
record is not MAPPED, or if the destination is absent/obsolete in the local
chebi.db. A held destination usually means the two records are the same
substance — scripts/merge_mapped_records.py handles that case, and the refusal
message says so. Dry-run by default.

REGISTRY MINTS (#273)
---------------------
`--to` also accepts a registry CURIE — `cas:`, `kgmicrobe.compound:`,
`kgmicrobe.ingredient:` — for the MAPPING_SEMANTICS.md Section 3 case: a
substance with no exact ontology term takes its registry identifier AND asserts
a narrowMatch to the nearest ontology parent. 248 records already hold `cas:`
identifiers in that shape; before #273 nothing could move an existing mapped
record INTO it, because the destination was validated by ontology lookup and a
mint resolves in no adapter.

With a mint, `--parent` is required and is what gets validated and recorded in
`ontology_mapping`; quality is forced to NARROW_MATCH (the only honest quality
for a parent). The SSSOM row's predicate becomes `skos:narrowMatch` and a
sibling `skos:exactMatch` row to the mint is emitted — Rule B1 requires that
pairing, and a narrowMatch without it fails validate_sssom_invariants.

    reground_mapped_record.py --identifier CHEBI:15741 \\
        --to cas:150-90-3 --parent CHEBI:15741 --reason '...' --apply
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


# Registry namespaces a record may take as its IDENTIFIER when no ontology term
# denotes the substance (MAPPING_SEMANTICS.md Section 3). These resolve in no
# ontology adapter by design, so they are validated by shape, not by lookup.
REGISTRY_PREFIXES = ("cas:", "kgmicrobe.compound:", "kgmicrobe.ingredient:")
REGISTRY_SOURCE = {"cas": "registry:cas", "kgmicrobe.compound": "kgm:compound",
                   "kgmicrobe.ingredient": "kgm:ingredient"}


def is_registry_mint(curie: str) -> bool:
    return curie.startswith(REGISTRY_PREFIXES)


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


def plan_sssom(subject_label: str, old_curie: str, new_curie: str, new_label: str,
               mint: str | None = None) -> tuple[str, str]:
    """Rewrite the object columns in place. Subject is unchanged, so no re-sort.

    When ``mint`` is given the record is taking a registry identifier: the existing
    row becomes a ``skos:narrowMatch`` to the parent, and a sibling ``skos:exactMatch``
    row to the mint is appended. Rule B1 requires that pairing — a narrowMatch from a
    MIM subject with no registry exactMatch sibling fails validate_sssom_invariants.
    """
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
    note = f"object {old_curie} -> {new_curie} '{new_label}' (line {hits[0] + 1})"
    eol = "\n" if lines[hits[0]].endswith("\n") else ""
    if mint:
        cols[2] = "skos:narrowMatch"
        registry = REGISTRY_SOURCE.get(mint.split(":", 1)[0], "")
        sibling = list(cols)
        sibling[2], sibling[3], sibling[4] = "skos:exactMatch", mint, subject_label
        sibling[5] = registry
        lines[hits[0]] = "\t".join(cols) + eol
        lines.insert(hits[0] + 1, "\t".join(sibling) + (eol or "\n"))
        note += (f"; predicate -> skos:narrowMatch, plus a Rule B1 registry "
                 f"exactMatch row to {mint}")
    else:
        lines[hits[0]] = "\t".join(cols) + eol
    if not lines[-1].endswith("\n"):
        lines[-1] += "\n"
    return "".join(lines), note


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--identifier", required=True, help="the record's current CURIE")
    ap.add_argument("--to", required=True,
                    help=("the CURIE it should hold — an ontology term, or a registry "
                          "mint (cas: / kgmicrobe.compound: / kgmicrobe.ingredient:) "
                          "when no ontology term denotes the substance"))
    ap.add_argument("--parent",
                    help=("REQUIRED when --to is a registry mint: the ontology term to "
                          "narrowMatch. Section 3 says a minted record asserts a parent; "
                          "without one the record claims an identity nothing relates to"))
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
    held = [r for r in doc["ingredients"] if r["identifier"] == args.to
            and r.get("mapping_status") != "REJECTED"]
    if held:
        raise SystemExit(
            f"{args.to} is already held by {', '.join(repr(r['preferred_term']) for r in held)}.\n"
            "If this record and that one are the same substance, merge instead:\n"
            f"  uv run python scripts/merge_mapped_records.py \\\n"
            f"      --from {args.identifier} --into {args.to} --reason '...'\n"
            "If they are different substances, the destination is not free — pick the term "
            "that denotes THIS one (MAPPING_SEMANTICS.md Section 3).")

    minted = is_registry_mint(args.to)
    if minted:
        # A mint denotes the substance; the ontology_mapping still has to point at a
        # real term, so the parent is what gets validated and what the record maps to.
        if not args.parent:
            raise SystemExit(
                f"--to {args.to} is a registry mint, so --parent is required.\n"
                "MAPPING_SEMANTICS.md Section 3: a substance with no exact ontology term "
                "takes its registry CURIE as identifier AND asserts a narrowMatch to the "
                "nearest ontology parent. Without a parent the record would assert an "
                "identity nothing in any ontology relates to.")
        if is_registry_mint(args.parent):
            raise SystemExit(f"--parent {args.parent} must be an ontology term, not a mint")
        args.quality = "NARROW_MATCH"          # the only honest quality for a parent
        term_curie, new_label = args.parent, chebi_label(args.parent)
    else:
        if args.parent:
            raise SystemExit("--parent applies only when --to is a registry mint")
        term_curie, new_label = args.to, chebi_label(args.to)

    stamp = dt.datetime.now(dt.timezone.utc).isoformat()
    old = args.identifier
    om = rec.setdefault("ontology_mapping", {})
    old_label = om.get("ontology_label")
    rec["identifier"] = args.to
    om.update({"ontology_id": term_curie, "ontology_label": new_label,
               "mapping_quality": args.quality})
    rec.setdefault("curation_history", []).append({
        "timestamp": stamp, "curator": args.curator, "action": "CORRECTED",
        "changes": (f"Re-grounded {old} '{old_label}' -> {args.to} '{new_label}' "
                    f"({args.quality}). {args.reason}"),
        "previous_status": "MAPPED", "new_status": "MAPPED", "llm_assisted": True,
    })
    doc["generation_date"] = stamp

    sssom_text, moved = plan_sssom(rec["preferred_term"], old, term_curie, new_label,
                                   mint=args.to if minted else None)
    print(f"{rec['preferred_term']!r}: {old} '{old_label}' -> {args.to} "
          + (f"(narrowMatch {term_curie} '{new_label}')" if minted
             else f"'{new_label}'"))
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
