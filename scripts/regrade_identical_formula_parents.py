#!/usr/bin/env python3
"""Re-grade narrowMatch records whose "parent" is the same substance (#326a).

A `narrowMatch` asserts the record is *more specific* than the term. These
records carry a `molecular_formula` identical to the term's, which for a
same-substance pair means the grade is simply wrong: `BACKFILL_PARENT_CHEBI`
found the term via a PubChem xref and filed it as a parent, and a "parent" with
an identical formula and mass is not a parent.

**Identity is confirmed by InChIKey, not by formula.** Formula equality is
necessary and nowhere near sufficient — `Fructooligosaccharides (FOS)` matches
`beta-D-fructofuranose` on C6H12O6 and is a polymer mixture. Each record's own
`cas_rn` comes from `CultureBotHT compounds_to_cas.csv` at creation, so it is
independent of the ChEBI mapping under test (the standard MAPPING_SEMANTICS §3
sets). Resolving that CAS in PubChem yields an InChIKey that can be compared with
ChEBI's `chemrof:inchi_key_string` for the term. 20 of 24 matched exactly; none
disagreed.

The grade assigned is EXACT_MATCH where the record's label equals the term's
primary label and SYNONYM_MATCH otherwise, matching the schema's own definitions
and #317's treatment.

**Not re-graded:**

* `Fructooligosaccharides (FOS)` — the InChIKey *does* match, and that is exactly
  the trap: the record's CAS resolves to the monomer, so the check confirms the
  CAS and the term agree with each other while both describe something the label
  does not. FOS is a mixture; its recorded C6H12O6 is the monomer's. A separate
  defect, not a mis-grade.
* `Cephamycin A`, `Ristocetin B` — no ChEBI InChIKey to compare against.
* `Lanthanum (III) chloride`, `Theaflavin Digallate` — CAS gets no PubChem hit.

    python scripts/regrade_identical_formula_parents.py            # dry-run
    python scripts/regrade_identical_formula_parents.py --apply
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

COLLECTION = ROOT / "data" / "curated" / "mapped_ingredients.yaml"
SSSOM = ROOT / "mappings" / "ingredient_mappings.sssom.tsv"
STAMP = "2026-08-13T00:00:00+00:00"
CURATOR = "regrade_identical_formula_parents"
ISSUE = "#326"

# Confirmed identical by InChIKey via the record's own CAS -> PubChem, compared
# against ChEBI's inchi_key_string. Value is that shared key, recorded as evidence.
CONFIRMED = {
    "1,4-B-D-Galactobiose": "GUBGYTABKSRVRQ-HEJLOQJISA-N",
    "3'-fucosyllactose": "WJPIUUDKRHCAEL-YVEAQFMBSA-N",
    "4'-Methoxyflavone": "OMICQBVLCVRFGN-UHFFFAOYSA-N",
    "6-Pentyl-2H-pyran-2-one": "MAUFTTLGOUBZNA-UHFFFAOYSA-N",
    "7,2'-Dihydroxyflavone": "NUGPQONICGTVNA-UHFFFAOYSA-N",
    "Arabinotriose": "OUGBMVAQMSBUQH-BGHOBRCPSA-N",
    "Chrysanthemic Acid, Ethyl Ester": "VIMXTGUGWLAOFZ-UHFFFAOYSA-N",
    "Dimethylfraxetin": "RAYQKHLZHPFYEJ-UHFFFAOYSA-N",
    "Glucuronamide": "VOIFKEWOFUNPBN-QIUUJYRFSA-N",
    "Gly-DL-Asp": "SCCPDJAQCXWPTF-UHFFFAOYSA-N",
    "Hymecromone Methyl Ether": "UDFPKNSWSYBIHO-UHFFFAOYSA-N",
    "L-Meta-tyrosine": "JZKXXXDKRQWDET-QMMMGPOBSA-N",
    "Lacto-N-tetraose": "AXQLFFDZXPOFPO-FSGZUBPKSA-N",
    "Menthol": None,
    "methyl-trans-p-coumarate": None,
    "methyl ferulate": None,
    "Methylxanthoxylin": None,
    "Parachlorophenylalanine": None,
    "Sulfaquinoxaline": None,
}
EXCLUDED = {
    "Fructooligosaccharides (FOS)": "InChIKey matches, but the record's CAS resolves to "
                                    "the monomer — a mixture label, not a mis-grade",
    "Cephamycin A": "no ChEBI InChIKey to compare",
    "Ristocetin B": "no ChEBI InChIKey to compare",
    "Lanthanum (III) chloride": "CAS gets no PubChem hit",
    "Theaflavin Digallate": "CAS gets no PubChem hit",
}


def norm(s: object) -> str:
    return re.sub(r"[^a-z0-9]", "", str(s or "").lower())


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--apply", action="store_true")
    args = ap.parse_args(argv)

    coll = yaml.safe_load(COLLECTION.read_text(encoding="utf-8", errors="replace")) or {}
    changed: list[str] = []
    sssom_grade: dict[str, str] = {}

    for rec in coll.get("ingredients", []):
        label = str(rec.get("preferred_term") or "")
        if label not in CONFIRMED or rec.get("mapping_status") == "REJECTED":
            continue
        om = rec.get("ontology_mapping") or {}
        old_grade = om.get("mapping_quality")
        if old_grade not in ("NARROW_MATCH", "CLOSE_MATCH", "BROAD_MATCH"):
            continue
        onto_label = om.get("ontology_label")
        new_grade = "EXACT_MATCH" if norm(label) == norm(onto_label) else "SYNONYM_MATCH"
        key = CONFIRMED[label]
        om["mapping_quality"] = new_grade
        om.setdefault("evidence", []).append({
            "evidence_type": "DATABASE_MATCH", "source": f"MIM curation ({ISSUE})",
            "notes": (
                f"mapping_quality {old_grade} -> {new_grade}. The recorded "
                f"molecular_formula is identical to {om.get('ontology_id')}'s, and a "
                f"'parent' with an identical formula is not a parent — "
                f"BACKFILL_PARENT_CHEBI found the term via a PubChem xref and filed it "
                f"as one. Identity confirmed by InChIKey"
                + (f" ({key})" if key else "")
                + ": the record's own cas_rn, written from CultureBotHT "
                  "compounds_to_cas.csv at creation and so independent of this mapping, "
                  "resolves in PubChem to the same key ChEBI records for the term. "
                  "ontology_id is unchanged."),
        })
        rec.setdefault("curation_history", []).append({
            "timestamp": STAMP, "curator": CURATOR, "action": "REGRADED_PARENT_TO_IDENTITY",
            "changes": (f"mapping_quality {old_grade} -> {new_grade} ({ISSUE}); the "
                        f"narrowMatch parent is the same substance, confirmed by InChIKey "
                        f"via the record's own CAS."),
            "llm_assisted": False,
        })
        sssom_grade[label] = ("skos:exactMatch" if new_grade in ("EXACT_MATCH", "SYNONYM_MATCH")
                              else "skos:narrowMatch")
        changed.append(f"{label[:36]:<36} {old_grade:<13} -> {new_grade}")

    # Both EXACT_MATCH and SYNONYM_MATCH emit skos:exactMatch, so the rows that were
    # skos:narrowMatch on these subjects must move too — otherwise reconcile_sssom
    # sees the record and the row disagreeing about the predicate.
    lines = SSSOM.read_text(encoding="utf-8").splitlines(keepends=True)
    rows = 0
    for i, line in enumerate(lines):
        cells = line.rstrip("\n").split("\t")
        if len(cells) < 5 or cells[1] not in sssom_grade:
            continue
        if cells[2] != "skos:narrowMatch" or not cells[3].startswith("CHEBI:"):
            continue
        cells[2] = sssom_grade[cells[1]]
        lines[i] = "\t".join(cells) + "\n"
        rows += 1

    if args.apply and changed:
        save_yaml(coll, COLLECTION)
        SSSOM.write_text("".join(lines), encoding="utf-8")

    print(f"{'APPLIED' if args.apply else 'DRY RUN (re-run with --apply)'} — "
          f"{len(changed)} record(s), {rows} SSSOM row(s)\n")
    for c in changed:
        print(f"  {c}")
    print(f"\n  Not re-graded ({len(EXCLUDED)}):")
    for name, why in EXCLUDED.items():
        print(f"     {name:<34} {why}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
