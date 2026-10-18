#!/usr/bin/env python3
"""Apply the verified #312 batch-1 corrections: grade-only regrades and parent
re-anchors, no identifier changes (#312, #245).

The 36 identity proposals on #312 were one reader's verdicts, never refuted.
This batch holds the eleven that change no identifier: five ``mapping_quality``
regrades, five parent re-anchors, and one REJECTED tombstone whose ontology row
still named the anhydrous salt. Each was re-verified against ``chebi.db`` before
being listed here, and the script re-checks the ChEBI facts it depends on at
run time and refuses to write if any of them no longer hold.

What each shape means under MAPPING_SEMANTICS.md:

* **Regrade** (Section 0): the term is right, the grade overstated or
  understated how it was established. The own-identifier SSSOM row keeps
  ``skos:exactMatch`` (Rule D); ``reconcile_sssom.py --apply`` syncs the
  justification/confidence columns from the new grade.
* **Parent re-anchor** (Section 3 step 2, #245): the ``cas:``/registry identity
  stays; only the ``broadMatch`` parent moves to the closest broader term the
  label names. ``reconcile_sssom.py --apply`` rewrites the ontology row and the
  "alongside parent" registry-row comments.

Dry-run by default; ``--apply`` writes the records and an apply log that the
review-lock receipt (``reports/sssom_completion_20260921/mapping_changes/``)
is built from. ``--finish-sssom`` adds any SSSOM row reconcile cannot create,
scrubs the wrong-compound tokens from ``other``, and syncs the grade columns of the
regraded own-identifier rows, which ``reconcile_sssom`` leaves alone by design.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import io
import json
import sqlite3
import sys
from dataclasses import dataclass, field
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "src"))

from mediaingredientmech.curate.curation_event import record_curation_event  # noqa: E402
from mediaingredientmech.utils.oaklib_cache import require_db  # noqa: E402
from mediaingredientmech.validation.write_validated import write_validated_ingredient  # noqa: E402

MAPPED = ROOT / "data" / "ingredients" / "mapped"
SSSOM = ROOT / "mappings" / "ingredient_mappings.sssom.tsv"
ISSUE = "#312"
CURATOR = "claude"
LLM_MODEL = "claude-fable-5-1"
MAPPING_DATE = "2026-09-22"
EVIDENCE_SOURCE = "MIM curation (#312); chebi.db"


@dataclass(frozen=True)
class Regrade:
    slug: str
    old_quality: str
    new_quality: str
    term: str
    term_label: str
    rationale: str
    # (term, synonym text) pairs that must be present in chebi.db for the rationale to hold
    requires_synonym: tuple[tuple[str, str], ...] = ()
    # synonym texts that must NOT be a name of the term (grade capped at CLOSE_MATCH)
    requires_not_name: tuple[str, ...] = ()


@dataclass(frozen=True)
class Reanchor:
    slug: str
    old_parent: str
    new_parent: str
    new_parent_label: str
    rationale: str
    old_source: str = "CHEBI"
    new_source: str = "CHEBI"
    old_quality: str = "NARROW_MATCH"
    new_quality: str = "NARROW_MATCH"
    supersede_sources: tuple[str, ...] = ()
    requires_synonym: tuple[tuple[str, str], ...] = ()
    requires_cas: tuple[tuple[str, str], ...] = ()
    reject_synonyms: tuple[tuple[str, str], ...] = field(default_factory=tuple)


REGRADES: tuple[Regrade, ...] = (
    Regrade(
        "5-Hydroxydodecanoate", "EXACT_MATCH", "SYNONYM_MATCH",
        "CHEBI:195418", "5-hydroxylaurate",
        "The label '5-Hydroxydodecanoate' resolves through the ChEBI related synonym "
        "'5-hydroxydodecanoate'; the primary label is '5-hydroxylaurate'. Section 0: a "
        "resolution through a unique ontology synonym is SYNONYM_MATCH, not EXACT_MATCH. "
        "Identifier and term unchanged; the own-identifier row stays skos:exactMatch (Rule D).",
        requires_synonym=(("CHEBI:195418", "5-hydroxydodecanoate"),),
    ),
    Regrade(
        "Caproic_Acid", "EXACT_MATCH", "SYNONYM_MATCH",
        "CHEBI:30776", "hexanoic acid",
        "The label 'Caproic acid' is a ChEBI related synonym of CHEBI:30776, whose primary "
        "label is 'hexanoic acid'. Section 0: synonym resolution is SYNONYM_MATCH. The CAS "
        "142-62-1 on the record is ChEBI's own xref for the term. Identifier unchanged.",
        requires_synonym=(("CHEBI:30776", "caproic acid"),),
    ),
    Regrade(
        "D-galactonic_Acid_Lactone", "SYNONYM_MATCH", "CLOSE_MATCH",
        "CHEBI:15895", "D-galactono-1,4-lactone",
        "'D-galactonic Acid Lactone' is not a label or synonym of any ChEBI term: every name "
        "on CHEBI:15895 states gamma or 1,4, and the bare 'D-Galactonolactone' is a synonym of "
        "the 1,5-lactone CHEBI:15945. The ring size was supplied from outside ChEBI (the "
        "Biolog substrate is the gamma-lactone), so the grade is CLOSE_MATCH per Section 0. "
        "Identifier unchanged; the own-identifier row stays skos:exactMatch (Rule D).",
        requires_synonym=(("CHEBI:15945", "D-Galactonolactone"),),
        requires_not_name=("D-galactonic Acid Lactone",),
    ),
    Regrade(
        "Hydroxystreptomycin", "CLOSE_MATCH", "SYNONYM_MATCH",
        "CHEBI:24750", "5'-hydroxystreptomycin",
        "'Hydroxystreptomycin' is a verbatim ChEBI related synonym of CHEBI:24750 and of no "
        "other term, and the term carries xref cas:6835-00-3. The earlier CLOSE_MATCH note "
        "('the term names the position and the label does not') understated a unique "
        "synonym resolution, which Section 0 grades SYNONYM_MATCH. Identifier unchanged.",
        requires_synonym=(("CHEBI:24750", "Hydroxystreptomycin"),),
    ),
    Regrade(
        "Glutamyl-glutamic_Acid", "SYNONYM_MATCH", "CLOSE_MATCH",
        "CHEBI:5390", "Glu-Glu",
        "'Glutamyl-glutamic Acid' is not a name on CHEBI:5390 (its names are Glu-Glu and "
        "L-alpha-glutamyl-L-glutamic acid). The term is alpha-linked and L,L-specific; the "
        "label states neither, and the gamma isomer is the separate term CHEBI:73705. The "
        "alpha/L,L reading was supplied by peptide-nomenclature convention, so Section 0 "
        "grades it CLOSE_MATCH. Identifier unchanged; own-identifier row stays exactMatch.",
        requires_not_name=("Glutamyl-glutamic Acid",),
    ),
)

REANCHORS: tuple[Reanchor, ...] = (
    Reanchor(
        "1-ethyl-3-methylimidazolium_Acetate", "CHEBI:61326", "CHEBI:63895", "ionic liquid",
        "The record is the neutral salt (CAS 143314-17-4, two-fragment SMILES). CHEBI:61326 "
        "'1-ethyl-3-methylimidazolium' is the bare cation, C6H11N2 charge +1: a component of "
        "the salt, not a broader term for it (Section 6). ChEBI has no term for the acetate "
        "salt, so the closest broader class is CHEBI:63895 'ionic liquid', the parent the "
        "sibling record 1-ethyl-3-methylimidazolium_Lysine already uses. cas: identity, "
        "NARROW_MATCH grade and both registry rows unchanged (Section 3 step 2).",
        supersede_sources=("CHEBI via OLS (stem-substring)",),
    ),
    Reanchor(
        "2-oxobutyric_Acid_Sodium_Salt", "CHEBI:16763", "CHEBI:30831", "2-oxobutanoic acid",
        "Section 3: for a salt the broadMatch parent follows the label, and '...Acid sodium "
        "salt' names the acid. The #322 note said ChEBI has no '2-oxobutanoic acid' term; it "
        "does: CHEBI:30831, xref cas:600-18-0, synonym '2-Oxobutyric acid'. The anion "
        "CHEBI:16763 was the fallback for a false premise. cas: identity unchanged.",
        supersede_sources=("MIM curation (#322)",),
        requires_synonym=(("CHEBI:30831", "2-Oxobutyric acid"),),
        requires_cas=(("CHEBI:30831", "cas:600-18-0"),),
    ),
    Reanchor(
        "3-sialyllactose_Sodium_Salt", "CHEBI:26714", "CHEBI:151472",
        "N-acetyl-alpha-neuraminyl-(2->3)-beta-D-galactosyl-(1->4)-D-glucose",
        "CHEBI:26714 'sodium salt' is the class of all sodium salts: it keeps the counterion "
        "and discards the compound (#322). The label names 3'-sialyllactose, and ChEBI has "
        "it: CHEBI:151472 carries the related synonym \"3'-sialyllactose\" and xref "
        "cas:35890-38-1 (the free trisaccharide). The reground_compositional_classes NO_PARENT "
        "claim 'no sialyllactose term of any form' was false. cas:128596-80-5 identity, "
        "NARROW_MATCH grade and both registry rows unchanged (Section 3 step 2, #245).",
        supersede_sources=("CHEBI via OLS (stem-substring)",),
        requires_synonym=(("CHEBI:151472", "3'-sialyllactose"),),
        requires_cas=(("CHEBI:151472", "cas:35890-38-1"),),
        reject_synonyms=(("Propionate (sodium salt)", "names a different compound (propionate), not 3'-sialyllactose"),),
    ),
    Reanchor(
        "6-O-sialyllactose_Sodium_Salt", "CHEBI:26714", "CHEBI:153372",
        "5-acetamido-3,5-dideoxy-D-glycero-alpha-D-galacto-non-2-ulopyranonosyl-(2->6)-beta-D-galactopyranosyl-(1->4)-D-glucopyranose",
        "As for the 3'-isomer: CHEBI:26714 is the class of sodium salts. The label names "
        "6'-sialyllactose, and CHEBI:153372 carries the related synonyms \"6'-sialyllactose\" "
        "and \"6'SL\"; it is the anomer-unspecified D-glucopyranose form, so it is the closest "
        "broader term for the salt. cas:157574-76-0 identity, NARROW_MATCH grade and both "
        "registry rows unchanged (Section 3 step 2, #245).",
        supersede_sources=("CHEBI via OLS (stem-substring)",),
        requires_synonym=(("CHEBI:153372", "6'-sialyllactose"),),
        reject_synonyms=(("Propionate (sodium salt)", "names a different compound (propionate), not 6'-sialyllactose"),),
    ),
    Reanchor(
        "Arabinan_From_Sugar_Beet", "FOODON:00003412", "CHEBI:22590", "arabinan",
        "FOODON:00003412 'sugar beet' is the source organ the stem-substring matcher took "
        "from the trailing qualifier; a polysaccharide is not a kind of a root. The head noun "
        "is arabinan, CHEBI:22590, the closest broader term (the botanical source stays in the "
        "preferred_term). cas:11078-27-6 identity, NARROW_MATCH grade and both registry rows "
        "unchanged (Section 3 step 2, #245).",
        old_source="FOODON",
        supersede_sources=("FOODON via OLS (stem-substring)",),
    ),
)

TOMBSTONE = {
    "slug": "Mgcl2x_6_H2o",
    "old_parent": "CHEBI:6636",
    "new_parent": "CHEBI:86345",
    "new_parent_label": "magnesium dichloride hexahydrate",
    "reject_synonym": ("Magnesium chloride anhydrous", "names the anhydrous salt CHEBI:6636, not the hexahydrate"),
    "rationale": (
        "REJECTED tombstone (merged into Mgcl2_X_6_H2o by #414): its identifier was re-pointed "
        "to CHEBI:86345 on 2026-08-20 but ontology_mapping still named CHEBI:6636 'magnesium "
        "dichloride', so the anhydrous label was still claimed by a hexahydrate record (#232). "
        "Point the mapping at the hexahydrate term and retype the anhydrous alias REJECTED_LABEL."
    ),
}

# One SSSOM row reconcile_sssom cannot create: a parent row for a subject that had only a registry row.
# Rows reconcile cannot create (a parent row for a subject that had only a registry
# row). Empty in this batch: Arabinoxylan_Rye_Flour's parent anchor is deferred,
# because reports/semantic_review_20260921/corrections/identity-plan.json pins that
# record's 2026-09-21 state and the resolution review refuses any later edit to it.
NEW_ROWS: tuple[dict, ...] = ()


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


class Chebi:
    def __init__(self) -> None:
        self.con = sqlite3.connect(require_db("CHEBI"))

    def label(self, curie: str) -> str | None:
        row = self.con.execute(
            "select value from statements where subject=? and predicate='rdfs:label'", (curie,)
        ).fetchone()
        return row[0] if row else None

    def names(self, curie: str) -> set[str]:
        return {
            r[0].casefold()
            for r in self.con.execute(
                "select value from statements where subject=? and predicate in "
                "('rdfs:label','oio:hasExactSynonym','oio:hasRelatedSynonym')",
                (curie,),
            )
        }

    def terms_named(self, text: str) -> set[str]:
        return {
            r[0]
            for r in self.con.execute(
                "select distinct subject from statements where predicate in "
                "('rdfs:label','oio:hasExactSynonym','oio:hasRelatedSynonym') and lower(value)=?",
                (text.casefold(),),
            )
        }

    def has_cas(self, curie: str, cas: str) -> bool:
        return (
            self.con.execute(
                "select 1 from statements where subject=? and predicate='oio:hasDbXref' and value=?",
                (curie, cas),
            ).fetchone()
            is not None
        )


def verify(chebi: Chebi) -> None:
    """Refuse to run if any ChEBI fact a rationale depends on no longer holds."""
    problems: list[str] = []
    for spec in REGRADES:
        if chebi.label(spec.term) != spec.term_label:
            problems.append(f"{spec.slug}: {spec.term} label is not {spec.term_label!r}")
        for term, text in spec.requires_synonym:
            if text.casefold() not in chebi.names(term):
                problems.append(f"{spec.slug}: {term} lacks name {text!r}")
            if spec.new_quality == "SYNONYM_MATCH" and chebi.terms_named(text) != {term}:
                problems.append(f"{spec.slug}: {text!r} is not unique to {term}")
        for text in spec.requires_not_name:
            if chebi.terms_named(text):
                problems.append(f"{spec.slug}: {text!r} is a ChEBI name after all")
    for spec in REANCHORS:
        if chebi.label(spec.new_parent) != spec.new_parent_label:
            problems.append(f"{spec.slug}: {spec.new_parent} label is not {spec.new_parent_label!r}")
        for term, text in spec.requires_synonym:
            if text.casefold() not in chebi.names(term):
                problems.append(f"{spec.slug}: {term} lacks name {text!r}")
        for term, cas in spec.requires_cas:
            if not chebi.has_cas(term, cas):
                problems.append(f"{spec.slug}: {term} lacks xref {cas}")
    if chebi.label(TOMBSTONE["new_parent"]) != TOMBSTONE["new_parent_label"]:
        problems.append("tombstone: CHEBI:86345 label changed")
    if problems:
        raise SystemExit("ChEBI facts no longer hold:\n  " + "\n  ".join(problems))


def load(slug: str) -> tuple[Path, dict]:
    path = MAPPED / f"{slug}.yaml"
    return path, yaml.safe_load(path.read_text())


def evidence(notes: str) -> dict:
    return {"evidence_type": "MANUAL_CURATION", "source": EVIDENCE_SOURCE, "notes": notes}


def supersede(mapping: dict, sources: tuple[str, ...]) -> int:
    n = 0
    for entry in mapping.get("evidence") or []:
        if entry.get("source") in sources and not str(entry.get("notes", "")).startswith("SUPERSEDED"):
            entry["notes"] = f"SUPERSEDED ({ISSUE}): " + str(entry.get("notes", ""))
            n += 1
    return n


def reject_synonym(record: dict, text: str, why: str) -> bool:
    for synonym in record.get("synonyms") or []:
        if isinstance(synonym, dict) and synonym.get("synonym_text") == text:
            if synonym.get("synonym_type") == "REJECTED_LABEL":
                return False
            synonym["synonym_type"] = "REJECTED_LABEL"
            return True
    return False


def apply_regrade(spec: Regrade, log: list, write: bool) -> None:
    path, record = load(spec.slug)
    mapping = record["ontology_mapping"]
    assert mapping["ontology_id"] == spec.term, (spec.slug, mapping["ontology_id"])
    if mapping["mapping_quality"] == spec.new_quality:
        print(f"SKIP     {spec.slug}: already {spec.new_quality}")
        return
    assert mapping["mapping_quality"] == spec.old_quality, (spec.slug, mapping["mapping_quality"])
    before = sha(path)
    mapping["mapping_quality"] = spec.new_quality
    mapping.setdefault("evidence", []).append(
        evidence(f"mapping_quality {spec.old_quality} -> {spec.new_quality}. {spec.rationale}")
    )
    record_curation_event(
        record, curator=CURATOR, action="REGRADED_MAPPING_QUALITY",
        changes=f"mapping_quality {spec.old_quality} -> {spec.new_quality} ({ISSUE}). {spec.rationale}",
        previous_status="MAPPED", new_status="MAPPED", llm_assisted=True, llm_model=LLM_MODEL,
    )
    print(f"REGRADE  {spec.slug}: {spec.old_quality} -> {spec.new_quality} on {spec.term}")
    if write:
        write_validated_ingredient(record, path)
    log.append({
        "source_record": str(path.relative_to(ROOT)), "shape": "regrade",
        "before_yaml_sha256": before, "after_yaml_sha256": sha(path) if write else None,
        "change": f"mapping_quality {spec.old_quality} -> {spec.new_quality}; identifier and ontology_id {spec.term} unchanged",
        "verification": spec.rationale,
    })


def apply_reanchor(spec: Reanchor, log: list, write: bool) -> None:
    path, record = load(spec.slug)
    mapping = record["ontology_mapping"]
    if mapping["ontology_id"] == spec.new_parent:
        print(f"SKIP     {spec.slug}: already anchored to {spec.new_parent}")
        return
    assert mapping["ontology_id"] == spec.old_parent, (spec.slug, mapping["ontology_id"])
    assert mapping["mapping_quality"] == spec.old_quality, (spec.slug, mapping["mapping_quality"])
    assert mapping.get("ontology_source") == spec.old_source, (spec.slug, mapping.get("ontology_source"))
    before = sha(path)
    old_label = mapping.get("ontology_label")
    mapping["ontology_id"] = spec.new_parent
    mapping["ontology_label"] = spec.new_parent_label
    mapping["ontology_source"] = spec.new_source
    mapping["mapping_quality"] = spec.new_quality
    superseded = supersede(mapping, spec.supersede_sources)
    rejected = [text for text, why in spec.reject_synonyms if reject_synonym(record, text, why)]
    mapping.setdefault("evidence", []).append(
        evidence(f"parent {spec.old_parent} ('{old_label}') -> {spec.new_parent} ('{spec.new_parent_label}'). {spec.rationale}")
    )
    changes = f"broadMatch parent {spec.old_parent} ('{old_label}') -> {spec.new_parent} ('{spec.new_parent_label}') ({ISSUE}). {spec.rationale}"
    if spec.old_quality != spec.new_quality:
        changes += f" mapping_quality {spec.old_quality} -> {spec.new_quality}."
    if rejected:
        changes += " Retyped REJECTED_LABEL: " + "; ".join(rejected) + "."
    record_curation_event(
        record, curator=CURATOR, action="REGROUNDED_PARENT_TERM", changes=changes,
        previous_status="MAPPED", new_status="MAPPED", llm_assisted=True, llm_model=LLM_MODEL,
    )
    print(f"REANCHOR {spec.slug}: {spec.old_parent} -> {spec.new_parent} '{spec.new_parent_label}'"
          f" (superseded {superseded} note(s), rejected {rejected})")
    if write:
        write_validated_ingredient(record, path)
    log.append({
        "source_record": str(path.relative_to(ROOT)), "shape": "parent_reanchor",
        "before_yaml_sha256": before, "after_yaml_sha256": sha(path) if write else None,
        "change": f"ontology_id {spec.old_parent} -> {spec.new_parent}; identifier {record['identifier']} unchanged"
                  + (f"; mapping_quality {spec.old_quality} -> {spec.new_quality}" if spec.old_quality != spec.new_quality else "")
                  + (f"; REJECTED_LABEL {rejected}" if rejected else ""),
        "verification": spec.rationale,
    })


def apply_tombstone(log: list, write: bool) -> None:
    spec = TOMBSTONE
    path, record = load(spec["slug"])
    assert record.get("mapping_status") == "REJECTED", spec["slug"]
    mapping = record["ontology_mapping"]
    if mapping["ontology_id"] == spec["new_parent"]:
        print(f"SKIP     {spec['slug']}: already {spec['new_parent']}")
        return
    assert mapping["ontology_id"] == spec["old_parent"], mapping["ontology_id"]
    before = sha(path)
    mapping["ontology_id"] = spec["new_parent"]
    mapping["ontology_label"] = spec["new_parent_label"]
    rejected = reject_synonym(record, *spec["reject_synonym"])
    mapping.setdefault("evidence", []).append(evidence(spec["rationale"]))
    record_curation_event(
        record, curator=CURATOR, action="CORRECTED",
        changes=f"ontology_id {spec['old_parent']} -> {spec['new_parent']} ({ISSUE}). {spec['rationale']}",
        previous_status="REJECTED", new_status="REJECTED", llm_assisted=True, llm_model=LLM_MODEL,
    )
    print(f"TOMBSTONE {spec['slug']}: {spec['old_parent']} -> {spec['new_parent']} (rejected alias: {rejected})")
    if write:
        write_validated_ingredient(record, path)
    log.append({
        "source_record": str(path.relative_to(ROOT)), "shape": "tombstone_mapping",
        "before_yaml_sha256": before, "after_yaml_sha256": sha(path) if write else None,
        "change": f"ontology_id {spec['old_parent']} -> {spec['new_parent']} on a REJECTED tombstone; alias retyped REJECTED_LABEL",
        "verification": spec["rationale"],
    })


def finish_sssom() -> None:
    """Add the row reconcile cannot create, scrub this batch's wrong-compound tokens from
    ``other``, and sync the grade columns of the regraded own-identifier rows.

    ``reconcile_sssom`` syncs justification/confidence only on the non-primary ontology
    row; the builder writes them by grade on the own-identifier row too (compare
    MIM:Adipate, CLOSE_MATCH, ManualMappingCuration/0.9), so this batch does the same.
    """
    from mediaingredientmech.sssom_grading import confidence_for, justification_for
    text = SSSOM.read_text(encoding="utf-8")
    lines = text.splitlines(keepends=True)
    comments = [line for line in lines if line.startswith("#")]
    body = [line for line in lines if not line.startswith("#")]
    reader = csv.DictReader(io.StringIO("".join(body)), delimiter="\t")
    rows = list(reader)
    fields = list(reader.fieldnames or [])
    existing = {(r["subject_id"], r["object_id"]) for r in rows}
    added = 0
    for row in NEW_ROWS:
        assert set(row) == set(fields), set(row) ^ set(fields)
        if (row["subject_id"], row["object_id"]) in existing:
            continue
        rows.append(dict(row))
        added += 1
    graded = 0
    regraded = {f"MIM:{spec.slug}": spec for spec in REGRADES}
    for row in rows:
        spec = regraded.get(row["subject_id"])
        if not spec or row["object_id"] != spec.term:
            continue
        want = (justification_for(spec.new_quality), confidence_for(spec.new_quality))
        if (row["mapping_justification"], row["confidence"]) == want:
            continue
        row["mapping_justification"], row["confidence"] = want
        row["mapping_date"] = MAPPING_DATE
        note = f"[grade reconciled to curated mapping {MAPPING_DATE}: {spec.old_quality} -> {spec.new_quality} ({ISSUE})]"
        row["comment"] = (row["comment"] + " " + note).strip()
        row["validation_method"] = f"manual:apply_312_batch1|GRADE|{MAPPING_DATE}"
        graded += 1
    scrubbed = 0
    rejected_by_subject = {
        f"MIM:{spec.slug}": {text for text, _ in spec.reject_synonyms} for spec in REANCHORS if spec.reject_synonyms
    }
    for row in rows:
        drop = rejected_by_subject.get(row["subject_id"])
        if not drop or not row["other"]:
            continue
        kept = [t for t in row["other"].split("|") if t not in drop]
        if len(kept) != len(row["other"].split("|")):
            row["other"] = "|".join(kept)
            scrubbed += 1
    out = io.StringIO()
    out.writelines(comments)
    writer = csv.DictWriter(out, fieldnames=fields, delimiter="\t", lineterminator="\n")
    writer.writeheader()
    writer.writerows(rows)
    SSSOM.write_text(out.getvalue(), encoding="utf-8")
    print(f"appended {added} SSSOM row(s); synced grade columns on {graded} own-identifier row(s); "
          f"scrubbed wrong-compound tokens from {scrubbed} row(s)")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--apply", action="store_true", help="write the records (default: dry-run)")
    parser.add_argument("--log", type=Path, help="apply-log JSON path (written with --apply)")
    parser.add_argument("--finish-sssom", action="store_true",
                        help="after reconcile_sssom --apply: add the parent row reconcile cannot create, "
                             "sync regraded own-identifier grade columns, scrub wrong-compound tokens")
    args = parser.parse_args()
    if args.finish_sssom:
        finish_sssom()
        return 0
    verify(Chebi())
    log: list = []
    for spec in REGRADES:
        apply_regrade(spec, log, args.apply)
    for spec in REANCHORS:
        apply_reanchor(spec, log, args.apply)
    apply_tombstone(log, args.apply)
    print(f"\n{'wrote' if args.apply else 'would write'} {len(log)} record(s)")
    if args.apply and args.log:
        args.log.write_text(json.dumps({"issue": ISSUE, "batch": "batch1", "records": log}, indent=2) + "\n")
        print(f"apply log: {args.log}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
