#!/usr/bin/env python3
"""Registry/identity rows assert identity, so they take exactMatch (#409).

#409 asked which artifact is authoritative when the claw builder and the
published SSSOM disagree on 249 predicates. The answer is neither wholesale:

* 227 rows the BUILDER got wrong — it demoted `SYNONYM_MATCH` to `closeMatch`,
  conflating "found via the ontology's synonym list" with "semantically close
  but not exact". Fixed upstream in culturebotai-claw#74.
* **22 rows this file gets wrong**, which is what this script repairs.

## The 22

Each is a registry/identity row of the shape

    MIM:Terpene_hydrate  skos:closeMatch  cas:2451-01-6  "Terpene hydrate"

where the object CURIE **is that record's own `identifier`** and the object
label is byte-identical to the subject label. The row exists to preserve the
registry-form identity alongside a broader ontology parent, so it asserts that
`MIM:X` and the registry CURIE denote the same thing — by construction, not by
judgement. `closeMatch` says "these are similar", which is strictly weaker than
what the record itself already claims by holding that identifier.

Nothing here re-grounds anything: the parent row, the identifier and the label
are all untouched. Only the predicate on the self-identity row changes, and
only where object_id == the record's identifier and the labels agree.

Confidence moves with it, to the 0.99 the corpus uses for exactMatch.

    python scripts/fix_registry_row_predicates.py            # dry-run
    python scripts/fix_registry_row_predicates.py --apply
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "src"))
import yaml  # noqa: E402

SSSOM = REPO_ROOT / "mappings" / "ingredient_mappings.sssom.tsv"
MAPPED = REPO_ROOT / "data" / "curated" / "mapped_ingredients.yaml"
UNMAPPED = REPO_ROOT / "data" / "curated" / "unmapped_ingredients.yaml"


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--apply", action="store_true")
    args = ap.parse_args(argv)

    ident: dict[str, str] = {}
    for path in (MAPPED, UNMAPPED):
        for rec in (yaml.safe_load(path.read_text(encoding="utf-8")) or {}
                    ).get("ingredients", []):
            term = str(rec.get("preferred_term") or "")
            # A tombstone carries the winner's identifier, so it must not be
            # allowed to authorise a predicate change on the winner's row.
            if not term or rec.get("mapping_status") == "REJECTED":
                continue
            identifier = str(rec.get("identifier") or "")
            parent = str((rec.get("ontology_mapping") or {}).get("ontology_id") or "")
            # Only records whose identifier DIFFERS from their ontology parent
            # have a separate identity row at all — that is the claw builder's
            # own dual-emission condition (`primary_id != obj_id`). Without it
            # this also matches every ordinary record's primary mapping row,
            # because there the identifier IS the ontology term: 353 rows
            # instead of 22, and 273 of them are rows the builder agrees are
            # closeMatch because the curator graded the mapping CLOSE_MATCH.
            # Promoting those would overwrite a curation decision.
            if identifier and parent and identifier != parent:
                ident.setdefault(term, identifier)

    lines = SSSOM.read_text(encoding="utf-8").splitlines(keepends=True)
    hdr_i = next(i for i, ln in enumerate(lines) if ln.startswith("subject_id"))
    cols = lines[hdr_i].rstrip("\n").split("\t")
    c_subj, c_pred = cols.index("subject_label"), cols.index("predicate_id")
    c_obj, c_olab = cols.index("object_id"), cols.index("object_label")
    c_conf = cols.index("confidence")

    changed, out = [], []
    for i, line in enumerate(lines):
        if i <= hdr_i or line.startswith("#"):
            out.append(line)
            continue
        cells = line.rstrip("\n").split("\t")
        if len(cells) <= c_conf or cells[c_pred] != "skos:closeMatch":
            out.append(line)
            continue
        subj = cells[c_subj]
        # Identity row: object IS the record's own identifier, and the object
        # label repeats the subject label. Both conditions, deliberately —
        # matching on the identifier alone would also catch a parent row that
        # happens to be the identifier, where the labels legitimately differ.
        if (ident.get(subj) and cells[c_obj] == ident[subj]
                and cells[c_olab].strip().lower() == subj.strip().lower()):
            cells[c_pred] = "skos:exactMatch"
            cells[c_conf] = "0.99"
            changed.append((subj, cells[c_obj]))
            out.append("\t".join(cells) + "\n")
            continue
        out.append(line)

    if args.apply and changed:
        SSSOM.write_text("".join(out), encoding="utf-8")

    print(f"{'APPLIED' if args.apply else 'DRY RUN (re-run with --apply)'}\n")
    print(f"  registry identity rows promoted closeMatch -> exactMatch: {len(changed)}")
    for subj, obj in changed[:8]:
        print(f"    {subj!r} -> {obj}")
    if len(changed) > 8:
        print(f"    ... and {len(changed) - 8} more")
    return 0


if __name__ == "__main__":
    sys.exit(main())
