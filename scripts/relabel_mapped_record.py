"""Rename a MAPPED record's preferred_term, keeping the old name as a synonym (#228).

Needed when a record's name claims something its identifier and its own chemistry
do not support -- CHEBI:18397 was called "Phenethylamine Hydrochloride" while
carrying the free base's CAS (64-04-0, the same xref ChEBI itself records),
formula (C8H11N) and SMILES. The name, not the mapping, was wrong, and the SSSOM
row published `skos:exactMatch` between the salt's name and the free base.

preferred_term is load-bearing: it is the SSSOM subject_label and the source of
the subject_id slug, and the per-record filename derives from it. So a rename
has to move the SSSOM row too, and keep it in subject_label sort order. Doing
that by hand is how rows go STALE.

The old name is preserved as a RAW_TEXT synonym -- it is a real label some
medium recipe used, and #229 means synonyms are published, so it stays
resolvable.

Dry-run by default; pass --apply.
"""

from __future__ import annotations

import argparse
import datetime as dt
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


def plan_sssom_move(old_term: str, new_term: str) -> tuple[str, str]:
    """Return (new file text, description). Writes nothing — the caller writes it
    only after save_yaml() has validated, so a validation failure cannot leave the
    SSSOM renamed and the YAML untouched."""
    # keepends, like promote_resolved_unmapped.py._sorted_insert: split("\n")
    # leaves a trailing "" that the sort loop never breaks on, so a term sorting
    # last is appended AFTER it — injecting a blank line and dropping the final
    # newline.
    lines = SSSOM.read_text().splitlines(keepends=True)
    header_i = next(i for i, ln in enumerate(lines) if ln.startswith("subject_id"))
    hits = [i for i, ln in enumerate(lines)
            if i > header_i and ln.split("\t")[1:2] == [old_term]]
    if len(hits) != 1:
        raise SystemExit(
            f"expected exactly 1 SSSOM row with subject_label {old_term!r}, found {len(hits)}. "
            "Records with a Rule-B1 registry set (narrowMatch + kgmicrobe.compound: + cas:) "
            "carry 2-3 rows and are not supported here — relabel those by hand.")
    clash = [i for i, ln in enumerate(lines)
             if i > header_i and ln.split("\t")[1:2] == [new_term]]
    if clash:
        raise SystemExit(f"an SSSOM row already has subject_label {new_term!r} "
                         f"(line {clash[0] + 1}); relabelling would duplicate the subject")
    row = lines.pop(hits[0])
    eol = "\n" if row.endswith("\n") else ""
    cols = row.rstrip("\n").split("\t")
    cols[0] = f"MIM:{sanitize_filename(new_term)}"
    cols[1] = new_term
    new_row = "\t".join(cols) + eol
    i = header_i + 1
    while i < len(lines):
        c = lines[i].split("\t")
        if len(c) > 1 and c[1].strip() and c[1] > new_term:
            break
        i += 1
    lines.insert(i, new_row)
    if not lines[-1].endswith("\n"):
        lines[-1] += "\n"
    return "".join(lines), f"{cols[0]}\t{new_term}  (row moved to line {i + 1})"


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--identifier", required=True, help="the record's CURIE")
    ap.add_argument("--to", required=True, help="new preferred_term")
    ap.add_argument("--reason", required=True, help="why the old name was wrong")
    ap.add_argument("--curator", default="relabel_mapped_record")
    ap.add_argument("--apply", action="store_true")
    args = ap.parse_args()

    doc = yaml.safe_load(MAPPED.read_text())
    hits = [r for r in doc["ingredients"] if r["identifier"] == args.identifier]
    if len(hits) != 1:
        raise SystemExit(f"{args.identifier} matches {len(hits)} mapped records, expected 1")
    rec = hits[0]
    old = rec["preferred_term"]
    if old == args.to:
        raise SystemExit(f"{args.identifier} is already named {old!r}")

    stamp = dt.datetime.now(dt.timezone.utc).isoformat()
    rec["preferred_term"] = args.to
    existing = {s.get("synonym_text") for s in rec.setdefault("synonyms", [])}
    if old not in existing:
        rec["synonyms"].append(
            {"synonym_text": old, "synonym_type": "RAW_TEXT", "source": "relabelled"})
    # deliberately no --quality: mapping_quality drives the SSSOM predicate_id
    # and confidence, and rewriting it here without also rewriting those (and any
    # Rule-B1 registry row) would publish e.g. NARROW_MATCH as skos:exactMatch.
    rec.setdefault("curation_history", []).append({
        "timestamp": stamp, "curator": args.curator, "action": "RELABELLED",
        "changes": (f"preferred_term {old!r} -> {args.to!r}; old name kept as a RAW_TEXT "
                    f"synonym. {args.reason}"),
        "llm_assisted": True,
    })
    doc["generation_date"] = stamp

    if any(r is not rec and r.get("preferred_term") == args.to for r in doc["ingredients"]):
        raise SystemExit(f"another mapped record already has preferred_term {args.to!r}; "
                         "renaming would collide in the per-record export index")
    sssom_text, moved = plan_sssom_move(old, args.to)
    print(f"{args.identifier}: {old!r} -> {args.to!r}")
    print(f"  SSSOM: {moved}")
    print(f"  old name kept as RAW_TEXT synonym")

    if not args.apply:
        print("\nDRY RUN -- nothing written. Pass --apply to write.")
        return 0
    # YAML first: it validates, and a failure here must not leave the SSSOM
    # renamed against an unchanged collection (ORPHAN + GAP, manual recovery).
    save_yaml(doc, MAPPED, validate=True, target_class="IngredientCollection")
    SSSOM.write_text(sssom_text)
    print("\nwrote data/curated/mapped_ingredients.yaml + SSSOM")
    print("next: just export-individual && just export-lists && just export-browser && just qc")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
