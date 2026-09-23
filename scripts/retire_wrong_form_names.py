#!/usr/bin/env python3
"""Retire the residual #232 label conflicts: names of a different form or a non-name.

After #732 (parent names off salts and hydrates) and the #312 batches, the label
index still reported 29 rows under ``conflict:different_substances``. Every one
is a synonym that names a different chemical form than the record it sits on,
or is not a name at all:

* an anhydrous term's ChEBI names on a hydrate record (``cobalt(2+) chloride``
  on CoCl2 x 2/x 4/x 6 H2O; ``sodium phosphate monobasic anhydrous`` on
  NaH2PO4 x 2 H2O; ``sodium dioxido(dioxo)molybdenum`` on Na2MoO4·2H2O;
  ``trisodium 2-hydroxypropane-1,2,3-tricarboxylate`` on two sodium citrate
  dihydrate tombstones);
* a hydrate label on the anhydrous tombstone (``CaCl2 × 2 H2O`` on Calcium
  Chloride, CHEBI:3312);
* the parent acid's name on its disodium-salt hydrate (``a-Ketoglutaric
  acid``) and the anion's name on a sodium-salt tombstone (``L-glutamate``);
* ``Optional ingredient``, a CultureMech recipe annotation carried as a
  RAW_TEXT synonym on four unrelated compounds.

MAPPING_SEMANTICS.md Section 3: hydrates, anhydrous forms and salts are not
interchangeable, and a synonym must name the record's own substance. Each
retirement is checked at run time against ``chebi.db``: the token must not be
a name of the record's own term, and (unless it is the annotation) must be a
name of the other form's term or another record's label. The token stays on
the record as ``REJECTED_LABEL`` provenance (it must not resolve, be exported,
or enter the SSSOM ``other`` column). Citrate identity questions themselves
(#704) are untouched: only names that ChEBI assigns to a different form move.

Dry-run by default; ``--apply`` writes; ``--finish-sssom`` scrubs the retired
tokens from ``other`` after ``reconcile_sssom``.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import io
import json
import sqlite3
import sys
from dataclasses import dataclass
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "src"))

from mediaingredientmech.curate.curation_event import record_curation_event  # noqa: E402
from mediaingredientmech.utils.oaklib_cache import require_db  # noqa: E402
from mediaingredientmech.validation.write_validated import write_validated_ingredient  # noqa: E402

INGREDIENTS = ROOT / "data" / "ingredients"
SSSOM = ROOT / "mappings" / "ingredient_mappings.sssom.tsv"
ISSUE = "#232"
CURATOR = "claude"
LLM_MODEL = "claude-fable-5-1"
MAPPING_DATE = "2026-09-23"
ANNOTATION = "Optional ingredient"


@dataclass(frozen=True)
class Retire:
    slug: str
    tokens: tuple[str, ...]
    other_term: str | None  # the ChEBI term the token actually names (None for the annotation)
    why: str


TARGETS: tuple[Retire, ...] = (
    Retire("A-Ketoglutaric_Acid_Disodium_Salt_Hydrate", ("a-Ketoglutaric acid",), "CHEBI:30915",
           "names the free acid (Alpha-ketoglutaric_Acid holds it), not the disodium salt hydrate"),
    Retire("Calcium_Chloride", ("CaCl2 × 2 H2O", "CaCl2*2H2O"), "CHEBI:86158",
           "dihydrate labels on the anhydrous CHEBI:3312 tombstone; the dihydrate is Cacl2_X_2_H2o"),
    Retire("Cocl2_X_2_H2o", ("cobalt(2+) chloride", "cobalt(II) chloride"), "CHEBI:35696",
           "ChEBI names of the anhydrous parent CHEBI:35696, enriched onto the hydrate when it still shared that term"),
    Retire("Cocl2_X_4_H2o", ("cobalt(2+) chloride", "cobalt(II) chloride"), "CHEBI:35696",
           "ChEBI names of the anhydrous parent CHEBI:35696, enriched onto the hydrate when it still shared that term"),
    Retire("Cocl2_X_6_H2o", ("cobalt(2+) chloride", "cobalt(II) chloride"), "CHEBI:35696",
           "ChEBI names of the anhydrous CHEBI:35696 on the hexahydrate CHEBI:53503 tombstone"),
    Retire("Na-glutamate", ("L-glutamate",), "CHEBI:29985",
           "the anion's name on the monosodium L-glutamate CHEBI:64243 tombstone"),
    Retire("D-fructose", (ANNOTATION,), None, "a CultureMech recipe annotation, not a name of D-fructose"),
    Retire("Cellulose", (ANNOTATION,), None, "a CultureMech recipe annotation, not a name of cellulose"),
    Retire("Na-acetate", (ANNOTATION,), None, "a CultureMech recipe annotation, not a name of sodium acetate"),
    Retire("Caco3", (ANNOTATION,), None, "a CultureMech recipe annotation, not a name of calcium carbonate"),
    Retire("Na2moo42h2o", ("sodium dioxido(dioxo)molybdenum",), "CHEBI:75215",
           "the anhydrous CHEBI:75215 name on the dihydrate CHEBI:75213 tombstone"),
    Retire("Nah2po4_X_2_H2o", ("sodium phosphate monobasic anhydrous",), "CHEBI:37585",
           "the anhydrous CHEBI:37585 name on a dihydrate label's local identity"),
    Retire("Sodium_Citrate", ("trisodium 2-hydroxypropane-1,2,3-tricarboxylate",), "CHEBI:53258",
           "the anhydrous trisodium citrate CHEBI:53258 name on the sodium citrate dihydrate CHEBI:32142 tombstone"),
    Retire("Trisodium_Citrate_X_2_H2o", ("trisodium 2-hydroxypropane-1,2,3-tricarboxylate",), "CHEBI:53258",
           "the anhydrous trisodium citrate CHEBI:53258 name on the sodium citrate dihydrate CHEBI:32142 tombstone"),
)


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def find(slug: str) -> Path:
    hits = list(INGREDIENTS.glob(f"*/{slug}.yaml"))
    if len(hits) != 1:
        raise SystemExit(f"{slug}: expected one record file, found {hits}")
    return hits[0]


def names(con: sqlite3.Connection, curie: str | None) -> set[str]:
    if not curie or not curie.startswith("CHEBI:"):
        return set()
    return {
        r[0].casefold()
        for r in con.execute(
            "select value from statements where subject=? and predicate in "
            "('rdfs:label','oio:hasExactSynonym','oio:hasRelatedSynonym')",
            (curie,),
        )
    }


def verify(con: sqlite3.Connection) -> None:
    """A token may leave a record only if it is not a name of the record's own identity
    and it is a name of the other form: a ChEBI name of that term, or a resolving label
    or synonym on a live record whose identifier is that term."""
    held: dict[str, set[str]] = {}
    for path in INGREDIENTS.glob("*/*.yaml"):
        record = yaml.safe_load(path.read_text()) or {}
        if record.get("mapping_status") == "REJECTED":
            continue
        tokens = {str(record.get("preferred_term") or "").casefold()}
        tokens |= {
            str(s.get("synonym_text") or "").casefold()
            for s in record.get("synonyms") or []
            if s.get("synonym_type") != "REJECTED_LABEL"
        }
        held.setdefault(str(record.get("identifier") or ""), set()).update(tokens)
    problems = []
    for spec in TARGETS:
        record = yaml.safe_load(find(spec.slug).read_text())
        # A cas:/registry identity has no ChEBI names of its own; its ontology_id is a
        # parent, whose names are exactly what must not sit on the record.
        own = names(con, record["identifier"])
        other = names(con, spec.other_term) | held.get(spec.other_term or "", set())
        for token in spec.tokens:
            key = token.casefold()
            if key in own:
                problems.append(f"{spec.slug}: ChEBI assigns {token!r} to the record's own identity")
            if spec.other_term and key not in other:
                problems.append(f"{spec.slug}: {token!r} is neither a ChEBI name of {spec.other_term} nor held by a record with that identifier")
    if problems:
        raise SystemExit("Retirement criteria fail:\n  " + "\n  ".join(problems))


def apply(log: list, write: bool) -> None:
    for spec in TARGETS:
        path = find(spec.slug)
        record = yaml.safe_load(path.read_text())
        before = sha(path)
        retired = []
        for synonym in record.get("synonyms") or []:
            if synonym.get("synonym_text") in spec.tokens and synonym.get("synonym_type") != "REJECTED_LABEL":
                retired.append(f"{synonym['synonym_text']!r} ({synonym.get('synonym_type')})")
                synonym["synonym_type"] = "REJECTED_LABEL"
        if not retired:
            print(f"SKIP   {spec.slug}: already retired")
            continue
        status = record.get("mapping_status")
        record_curation_event(
            record, curator=CURATOR, action="REJECTED_WRONG_FORM_SYNONYMS",
            changes=(f"Retyped REJECTED_LABEL: {', '.join(retired)}: {spec.why} ({ISSUE}). The token is kept as "
                     "provenance only; it must not resolve, be exported, or enter the SSSOM other column."),
            previous_status=status, new_status=status, llm_assisted=True, llm_model=LLM_MODEL,
        )
        print(f"RETIRE {spec.slug} [{status}]: {', '.join(retired)}")
        if write:
            write_validated_ingredient(record, path)
        log.append({
            "source_record": str(path.relative_to(ROOT)), "shape": "synonym_retirement",
            "before_yaml_sha256": before, "after_yaml_sha256": sha(path) if write else None,
            "change": "REJECTED_LABEL: " + ", ".join(retired),
            "verification": spec.why,
        })


def finish_sssom() -> None:
    lines = SSSOM.read_text(encoding="utf-8").splitlines(keepends=True)
    comments = [line for line in lines if line.startswith("#")]
    body = [line for line in lines if not line.startswith("#")]
    reader = csv.DictReader(io.StringIO("".join(body)), delimiter="\t")
    rows, fields = list(reader), list(reader.fieldnames or [])
    by_subject = {f"MIM:{spec.slug}": set(spec.tokens) for spec in TARGETS}
    scrubbed = 0
    for row in rows:
        drop = by_subject.get(row["subject_id"])
        if not drop or not row["other"]:
            continue
        tokens = [t for t in row["other"].split("|") if t]
        keep = [t for t in tokens if t not in drop]
        if keep != tokens:
            row["other"] = "|".join(keep)
            row["mapping_date"] = MAPPING_DATE
            row["comment"] = (row["comment"] + f" [other: dropped {[t for t in tokens if t in drop]}: REJECTED_LABEL, a different form's name ({ISSUE})]").strip()
            row["validation_method"] = f"manual:retire_wrong_form_names|OTHER|{MAPPING_DATE}"
            scrubbed += 1
    out = io.StringIO()
    out.writelines(comments)
    writer = csv.DictWriter(out, fieldnames=fields, delimiter="\t", lineterminator="\n")
    writer.writeheader()
    writer.writerows(rows)
    SSSOM.write_text(out.getvalue(), encoding="utf-8")
    print(f"retired tokens scrubbed from {scrubbed} row(s)")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--apply", action="store_true")
    parser.add_argument("--log", type=Path)
    parser.add_argument("--finish-sssom", action="store_true")
    args = parser.parse_args()
    if args.finish_sssom:
        finish_sssom()
        return 0
    verify(sqlite3.connect(require_db("CHEBI")))
    log: list = []
    apply(log, args.apply)
    print(f"\n{'wrote' if args.apply else 'would write'} {len(log)} record(s)")
    if args.apply and args.log:
        args.log.write_text(json.dumps({"issue": ISSUE, "batch": "wrong-form-names", "records": log}, indent=2) + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
