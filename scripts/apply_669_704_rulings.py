#!/usr/bin/env python3
"""Apply the contract to the mechanical remainder of #669 and #704.

Three shapes, each decided by MAPPING_SEMANTICS.md rather than by taste:

1. **Wrong-substance synonyms (#669).** Of the 30 ``UNREVIEWED`` Rule K
   baseline entries, 15 are enrichment round-trips that never touch MIM's
   YAML, 7 are ChEBI-backed generic names on a specific record (``mannitol``
   on D-mannitol: ChEBI itself lists them, a policy question left open), and
   10 are names of a *different* substance that has its own record: two other
   peptone products on Bacto peptone, casein hydrolysate on casein peptone,
   the zwitterion on neutral L-cysteine, the free base on putrescine
   dihydrochloride, the member on the vitamin B12 class and the class name on
   the member, the anhydrous salt on its hexahydrate, the anion on citric acid,
   and the monomer on fructooligosaccharides. Those ten are retyped
   ``REJECTED_LABEL`` after checking that ChEBI does not assign the name to the
   record's own identity and that it is the other record's label or a ChEBI
   name of its term.
2. **Tricine (#704.2).** ``CHEBI:46760 tricine`` is a structureless grouping
   class; its neutral child ``CHEBI:39063`` carries the structure and xrefs the
   record's own CAS 5704-04-1. Section 3 asks for the most specific stable
   identifier: the batch-2 class-to-member shape, graded ``CAS_RN_LOOKUP``,
   with the 44 recipe memberships following the identifier.
3. **Na2-citrate (#704.1).** ``Na2-citrate`` names disodium hydrogen citrate
   (PubChem CID 8950, CAS 144-33-2, C6H6Na2O7), a different salt from the
   trisodium record that carried it as an EXACT_SYNONYM since a 2026-04-19
   merge. ChEBI has no disodium term and three CultureMech recipes name it, so
   Section 3 step 2 applies: a new ``cas:144-33-2`` record with ``broadMatch``
   to citric acid (the parent follows the label), a Rule B1 registry row, the
   three memberships moved off the trisodium record, and the name retired
   there.

Dry-run by default; ``--apply`` writes records; ``--finish-sssom`` after
``reconcile_sssom --apply`` adds the new record's rows and scrubs retired
tokens; ``--finish-artifacts --occurrences PATH`` moves the memberships and
refreshes the affected counts.
"""

from __future__ import annotations

import argparse
import csv
import datetime as dt
import hashlib
import io
import json
import sqlite3
import sys
from collections import defaultdict
from dataclasses import dataclass
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "src"))

from mediaingredientmech.curate.curation_event import record_curation_event  # noqa: E402
from mediaingredientmech.utils.culturemech_occurrences import (  # noqa: E402
    SOURCE_LABEL_IDENTIFIER_OVERRIDES,
    _source_label_key,
)
from mediaingredientmech.utils.oaklib_cache import require_db  # noqa: E402
from mediaingredientmech.validation.write_validated import write_validated_ingredient  # noqa: E402

INGREDIENTS = ROOT / "data" / "ingredients"
MAPPED = INGREDIENTS / "mapped"
SSSOM = ROOT / "mappings" / "ingredient_mappings.sssom.tsv"
MEMBERSHIP = ROOT / "mappings" / "culturemech_recipe_membership.tsv"
CURATOR = "claude"
LLM_MODEL = "claude-fable-5-1"
MAPPING_DATE = "2026-09-24"


@dataclass(frozen=True)
class Retire:
    slug: str
    tokens: tuple[str, ...]
    owner_slug: str
    why: str


RETIREMENTS: tuple[Retire, ...] = (
    Retire("Bacto_Peptone", ("Fish peptone", "Meat peptone"), "Fish_peptone",
           "names of other peptone products, each with its own record (Fish_peptone, Meat_peptone)"),
    Retire("Casein_Peptone", ("Casein hydrolysate",), "Casein_hydrolysate",
           "the acid hydrolysate product has its own record (Casein_hydrolysate, MICRO:0001366)"),
    Retire("L-cysteine", ("L-cysteine zwitterion",), "L-cysteine_Zwitterion",
           "the zwitterion CHEBI:35235 has its own record; the record is neutral L-cysteine CHEBI:17561"),
    Retire("Putrescine_Dihydrochloride", ("Putrescine",), "Putrescine",
           "the free base's name on the dihydrochloride salt (Section 3: salts are not the parent)"),
    Retire("Vitamin_B12", ("Cyanocobalamin",), "Cyanocobalamin",
           "the member's name on the vitamin B12 class record CHEBI:176843; Cyanocobalamin has its own record"),
    Retire("Cyanocobalamin", ("Vitamin B12",), "Vitamin_B12",
           "ChEBI assigns 'vitamin B12' to CHEBI:176843, the class record, not to cyanocobalamin CHEBI:17439"),
    Retire("Nh42ni_So42_X_6_H2o", ("(NH4)2Ni(SO4)2",), "Nh42ni_So42",
           "the anhydrous salt's label on the hexahydrate record"),
    Retire("Citric_Acid", ("Citrate",), "Citrate",
           "a bare -ate label denotes the anion (Section 3 protonation rule); the Citrate record holds CHEBI:16947"),
    Retire("Fructooligosaccharides_Fos", ("FRUCTOSE",), "Fructose",
           "the monomer's name on the oligosaccharide record"),
)

# --- Tricine ----------------------------------------------------------------
TRICINE = {"slug": "Tricine", "old": "CHEBI:46760", "new": "CHEBI:39063",
           "label": "N-tris(hydroxymethyl)methylglycine", "cas": "cas:5704-04-1"}

# --- Na2-citrate ------------------------------------------------------------
NA2_CITRATE = {
    "slug": "Na2-citrate", "identifier": "cas:144-33-2", "preferred_term": "Na2-citrate",
    "parent": "CHEBI:30769", "parent_label": "citric acid", "registry": "kgmicrobe.compound:na2-citrate",
    "formula": "C6H6Na2O7", "inchikey": "CEYULKASIQJZGP-UHFFFAOYSA-L", "pubchem_cid": 8950,
    "source_slug": "Trisodium_Citrate", "source_identifier": "CHEBI:53258",
}


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def find(slug: str) -> Path:
    hits = list(INGREDIENTS.glob(f"*/{slug}.yaml"))
    if len(hits) != 1:
        raise SystemExit(f"{slug}: expected one record file, found {hits}")
    return hits[0]


class Chebi:
    def __init__(self) -> None:
        self.con = sqlite3.connect(require_db("CHEBI"))

    def names(self, curie: str | None) -> set[str]:
        if not curie or not curie.startswith("CHEBI:"):
            return set()
        return {r[0].casefold() for r in self.con.execute(
            "select value from statements where subject=? and predicate in "
            "('rdfs:label','oio:hasExactSynonym','oio:hasRelatedSynonym')", (curie,))}

    def label(self, curie: str) -> str | None:
        row = self.con.execute("select value from statements where subject=? and predicate='rdfs:label'", (curie,)).fetchone()
        return row[0] if row else None

    def value(self, curie: str, predicate: str) -> str | None:
        row = self.con.execute("select value from statements where subject=? and predicate=?", (curie, predicate)).fetchone()
        return row[0] if row else None

    def cas_terms(self, cas: str) -> set[str]:
        return {r[0] for r in self.con.execute("select subject from statements where predicate='oio:hasDbXref' and value=?", (cas,))}


def verify(chebi: Chebi) -> None:
    problems = []
    for spec in RETIREMENTS:
        record = yaml.safe_load(find(spec.slug).read_text())
        owner = yaml.safe_load(find(spec.owner_slug).read_text())
        own = chebi.names(record["identifier"])
        other = chebi.names(owner["identifier"]) | {str(owner.get("preferred_term") or "").casefold()}
        if spec.slug == "Bacto_Peptone":
            other |= {"meat peptone"}  # second owner record, Meat_peptone
        for token in spec.tokens:
            key = token.casefold()
            if key in own:
                problems.append(f"{spec.slug}: ChEBI assigns {token!r} to the record's own identity")
            if key not in other:
                problems.append(f"{spec.slug}: {token!r} is not {spec.owner_slug}'s label or a ChEBI name of its term")
    if chebi.label(TRICINE["new"]) != TRICINE["label"]:
        problems.append("Tricine: CHEBI:39063 label changed")
    if chebi.cas_terms(TRICINE["cas"]) != {TRICINE["new"]}:
        problems.append(f"Tricine: {TRICINE['cas']} is not xref'd on exactly CHEBI:39063")
    if chebi.label(NA2_CITRATE["parent"]) != NA2_CITRATE["parent_label"]:
        problems.append("Na2-citrate: CHEBI:30769 label changed")
    if _source_label_key("Na2-citrate") not in SOURCE_LABEL_IDENTIFIER_OVERRIDES:
        problems.append("Na2-citrate: SOURCE_LABEL_IDENTIFIER_OVERRIDES lacks 'Na2-citrate'")
    if problems:
        raise SystemExit("Preconditions fail:\n  " + "\n  ".join(problems))


def apply_retirements(log: list, write: bool) -> None:
    for spec in RETIREMENTS:
        path = find(spec.slug)
        record = yaml.safe_load(path.read_text())
        before = sha(path)
        retired = []
        for synonym in record.get("synonyms") or []:
            if synonym.get("synonym_text") in spec.tokens and synonym.get("synonym_type") != "REJECTED_LABEL":
                retired.append(f"{synonym['synonym_text']!r} ({synonym.get('synonym_type')})")
                synonym["synonym_type"] = "REJECTED_LABEL"
        if not retired:
            print(f"SKIP   {spec.slug}")
            continue
        record_curation_event(
            record, curator=CURATOR, action="REJECTED_WRONG_SUBSTANCE_SYNONYMS",
            changes=(f"Retyped REJECTED_LABEL: {', '.join(retired)}: {spec.why} (#669). Kept as provenance only; "
                     "it must not resolve, be exported, or enter the SSSOM other column."),
            previous_status="MAPPED", new_status="MAPPED", llm_assisted=True, llm_model=LLM_MODEL,
        )
        print(f"RETIRE {spec.slug}: {', '.join(retired)}")
        if write:
            write_validated_ingredient(record, path)
        log.append({"source_record": str(path.relative_to(ROOT)), "shape": "synonym_retirement",
                    "before_yaml_sha256": before, "after_yaml_sha256": sha(path) if write else None,
                    "change": "REJECTED_LABEL: " + ", ".join(retired), "verification": spec.why})


def apply_tricine(chebi: Chebi, log: list, write: bool) -> None:
    path = find(TRICINE["slug"])
    record = yaml.safe_load(path.read_text())
    if record["identifier"] == TRICINE["new"]:
        print("SKIP   Tricine: already re-grounded")
        return
    assert record["identifier"] == TRICINE["old"], record["identifier"]
    before = sha(path)
    mapping = record["ontology_mapping"]
    mapping["ontology_id"] = TRICINE["new"]
    mapping["ontology_label"] = TRICINE["label"]
    mapping["mapping_quality"] = "CAS_RN_LOOKUP"
    record["identifier"] = TRICINE["new"]
    chem = record.setdefault("chemical_properties", {})
    for slot, predicate in (("molecular_formula", "chemrof:generalized_empirical_formula"), ("inchi", "chemrof:inchi_string"), ("smiles", "chemrof:smiles_string")):
        value = chebi.value(TRICINE["new"], predicate)
        if value:
            chem[slot] = value
    chem["data_source"] = f"{chem.get('data_source', '')}; structure from chebi.db CHEBI:39063 (#704)".strip("; ")
    note = ("identifier CHEBI:46760 -> CHEBI:39063; ontology 'tricine' -> 'N-tris(hydroxymethyl)methylglycine'; "
            "mapping_quality EXACT_MATCH -> CAS_RN_LOOKUP. CHEBI:46760 is a grouping class with a label and nothing "
            "else (no formula, InChIKey or definition); its children are the neutral CHEBI:39063, which owns the "
            "structure, the systematic names and the xref cas:5704-04-1 (the record's own CAS, on no other term), "
            "and the zwitterion CHEBI:46759. Section 3: the most specific stable identifier (#704).")
    mapping.setdefault("evidence", []).append({"evidence_type": "MANUAL_CURATION", "source": "MIM curation (#704); chebi.db", "notes": note})
    record_curation_event(record, curator=CURATOR, action="REGROUNDED_IDENTITY", changes=note + " (#704)",
                          previous_status="MAPPED", new_status="MAPPED", llm_assisted=True, llm_model=LLM_MODEL)
    print("IDENTITY Tricine: CHEBI:46760 -> CHEBI:39063 [CAS_RN_LOOKUP]")
    if write:
        write_validated_ingredient(record, path)
    log.append({"source_record": str(path.relative_to(ROOT)), "shape": "identity",
                "before_yaml_sha256": before, "after_yaml_sha256": sha(path) if write else None,
                "change": "identifier CHEBI:46760 -> CHEBI:39063; mapping_quality EXACT_MATCH -> CAS_RN_LOOKUP", "verification": note})


def apply_na2_citrate(log: list, write: bool) -> None:
    spec = NA2_CITRATE
    # retire on the trisodium record
    path = find(spec["source_slug"])
    record = yaml.safe_load(path.read_text())
    before = sha(path)
    retired = False
    for synonym in record.get("synonyms") or []:
        if synonym.get("synonym_text") == "Na2-citrate" and synonym.get("synonym_type") != "REJECTED_LABEL":
            synonym["synonym_type"] = "REJECTED_LABEL"
            retired = True
    if retired:
        record_curation_event(
            record, curator=CURATOR, action="REJECTED_WRONG_SUBSTANCE_SYNONYMS",
            changes=("Retyped REJECTED_LABEL: 'Na2-citrate' (EXACT_SYNONYM): by nomenclature disodium hydrogen citrate "
                     "(PubChem CID 8950, CAS 144-33-2, C6H6Na2O7), a different salt from trisodium citrate; the "
                     "2026-04-19 merge conflated it. The name now has its own record, Na2-citrate (#704)."),
            previous_status="MAPPED", new_status="MAPPED", llm_assisted=True, llm_model=LLM_MODEL,
        )
        print(f"RETIRE {spec['source_slug']}: 'Na2-citrate'")
        if write:
            write_validated_ingredient(record, path)
        log.append({"source_record": str(path.relative_to(ROOT)), "shape": "synonym_retirement",
                    "before_yaml_sha256": before, "after_yaml_sha256": sha(path) if write else None,
                    "change": "REJECTED_LABEL: 'Na2-citrate'", "verification": "Disodium hydrogen citrate is a different salt; own record minted."})
    # mint the disodium record
    new_path = MAPPED / f"{spec['slug']}.yaml"
    if new_path.exists():
        print("SKIP   Na2-citrate: record exists")
        return
    now = dt.datetime.now(dt.timezone.utc).isoformat()
    rationale = ("Na2-citrate is disodium hydrogen citrate (PubChem CID 8950, CAS 144-33-2, C6H6Na2O7, InChIKey "
                 "CEYULKASIQJZGP-UHFFFAOYSA-L). ChEBI has no disodium citrate term, and three CultureMech recipes "
                 "name it, so MAPPING_SEMANTICS Section 3 step 2 applies: cas: identity, broadMatch to the acid the "
                 "label's salt derives from (CHEBI:30769 citric acid), Rule B1 registry row. Previously an "
                 "EXACT_SYNONYM on Trisodium_Citrate after a 2026-04-19 merge that conflated the two salts (#704).")
    record = {
        "identifier": spec["identifier"],
        "preferred_term": spec["preferred_term"],
        "ontology_mapping": {
            "ontology_id": spec["parent"], "ontology_label": spec["parent_label"], "ontology_source": "CHEBI",
            "mapping_quality": "NARROW_MATCH",
            "evidence": [{"evidence_type": "MANUAL_CURATION", "source": "MIM curation (#704); PubChem CID 8950; chebi.db", "notes": rationale}],
        },
        "synonyms": [
            {"synonym_text": "Na2-citrate", "synonym_type": "RAW_TEXT", "source": "CultureMech"},
            {"synonym_text": "disodium hydrogen citrate", "synonym_type": "EXACT_SYNONYM", "source": "PubChem CID 8950"},
            {"synonym_text": "disodium citrate", "synonym_type": "RELATED_SYNONYM", "source": "PubChem CID 8950"},
        ],
        "mapping_status": "MAPPED",
        "occurrence_statistics": {"total_occurrences": 0, "media_count": 0},
        "curation_history": [],
        "chemical_properties": {"cas_rn": "144-33-2", "molecular_formula": spec["formula"],
                                "data_source": "PubChem CID 8950 (CAS 144-33-2)", "retrieval_date": now},
        "ingredient_type": "SINGLE_INGREDIENT",
    }
    record_curation_event(record, curator=CURATOR, action="CREATED",
                          changes=f"Created from the raw label 'Na2-citrate' split off Trisodium_Citrate. {rationale}",
                          new_status="MAPPED", llm_assisted=True, llm_model=LLM_MODEL)
    print("MINT   Na2-citrate: cas:144-33-2, broadMatch CHEBI:30769")
    if write:
        write_validated_ingredient(record, new_path)
    log.append({"source_record": str(new_path.relative_to(ROOT)), "shape": "new_record",
                "before_yaml_sha256": None, "after_yaml_sha256": sha(new_path) if write else None,
                "change": "new record cas:144-33-2 (disodium hydrogen citrate), broadMatch CHEBI:30769", "verification": rationale})


# --- SSSOM ------------------------------------------------------------------


def _read_rows():
    lines = SSSOM.read_text(encoding="utf-8").splitlines(keepends=True)
    comments = [line for line in lines if line.startswith("#")]
    body = [line for line in lines if not line.startswith("#")]
    reader = csv.DictReader(io.StringIO("".join(body)), delimiter="\t")
    return comments, list(reader.fieldnames or []), list(reader)


def _write_rows(comments, fields, rows) -> None:
    out = io.StringIO()
    out.writelines(comments)
    writer = csv.DictWriter(out, fieldnames=fields, delimiter="\t", lineterminator="\n")
    writer.writeheader()
    writer.writerows(rows)
    SSSOM.write_text(out.getvalue(), encoding="utf-8")


def _stamp(row, note, method) -> None:
    row["mapping_date"] = MAPPING_DATE
    row["comment"] = (row["comment"] + " " + note).strip()
    row["validation_method"] = f"manual:apply_669_704_rulings|{method}|{MAPPING_DATE}"


def finish_sssom() -> None:
    from mediaingredientmech.sssom_grading import confidence_for, justification_for

    comments, fields, rows = _read_rows()
    slugs = [s.slug for s in RETIREMENTS] + [TRICINE["slug"], NA2_CITRATE["source_slug"], NA2_CITRATE["slug"]]
    records = {s: yaml.safe_load(find(s).read_text()) for s in slugs}
    scrubbed = synced = added = 0
    for row in rows:
        slug = row["subject_id"][4:] if row["subject_id"].startswith("MIM:") else None
        record = records.get(slug)
        if not record:
            continue
        rejected = {s["synonym_text"] for s in record.get("synonyms") or [] if s.get("synonym_type") == "REJECTED_LABEL"}
        tokens = [t for t in row["other"].split("|") if t]
        keep = [t for t in tokens if t not in rejected]
        if keep != tokens:
            row["other"] = "|".join(keep)
            _stamp(row, f"[other: dropped {[t for t in tokens if t in rejected]}: REJECTED_LABEL on the record (#669/#704)]", "OTHER")
            scrubbed += 1
        if row["object_id"] == record["identifier"] and row["object_id"].startswith("CHEBI:"):
            quality = record["ontology_mapping"]["mapping_quality"]
            want = ("skos:exactMatch", justification_for(quality), confidence_for(quality))
            have = (row["predicate_id"], row["mapping_justification"], row["confidence"])
            if have != want:
                row["predicate_id"], row["mapping_justification"], row["confidence"] = want
                _stamp(row, f"[own-identifier row: exactMatch per Rule D, grade {quality} (#704)]", "IDENTITY")
                synced += 1
        cas_rn = str((record.get("chemical_properties") or {}).get("cas_rn") or "").strip()
        tokens = [t for t in row["other"].split("|") if t]
        symmetric = row["predicate_id"] in {"skos:exactMatch", "skos:closeMatch"}
        if symmetric and cas_rn:
            wanted = [t for t in tokens if not t.upper().startswith("CAS:")] + [f"CAS:{cas_rn}"]
            if tokens != wanted:
                row["other"] = "|".join(wanted)
                _stamp(row, "[other: CAS token follows the record's cas_rn on a symmetric row, #403]", "OTHER")
        elif not symmetric and any(t.upper().startswith("CAS:") for t in tokens):
            row["other"] = "|".join(t for t in tokens if not t.upper().startswith("CAS:"))
            _stamp(row, "[other: CAS token removed from an asymmetric row, #403]", "OTHER")
    # rows for the minted record
    spec = NA2_CITRATE
    subject = f"MIM:{spec['slug']}"
    existing = {(r["subject_id"], r["object_id"]) for r in rows}
    record = records[spec["slug"]]
    source = "MIM:CultureMech|MIM:curator=claude|MIM:MIM curation (#704)"
    for object_id, object_label, object_source, predicate, confidence, comment, other in (
        (spec["parent"], spec["parent_label"], "obo:chebi.owl", "skos:broadMatch", "0.9",
         "Parent anchor per MAPPING_SEMANTICS Section 3 step 2 (#704): a citrate salt's parent follows the label to the acid; no ChEBI term for disodium hydrogen citrate.",
         "disodium hydrogen citrate|disodium citrate"),
        (spec["identifier"], spec["preferred_term"], "registry:cas", "skos:exactMatch", "0.99",
         f"Registry/identity row preserving {spec['identifier']} alongside parent {spec['parent']}.", "CAS:144-33-2"),
        (spec["registry"], spec["preferred_term"], "kgm:compound", "skos:exactMatch", "0.99",
         f"Registry/identity row (Rule B1) for broadMatch subject; kg-microbe primary id {spec['registry']} alongside parent {spec['parent']}.", "CAS:144-33-2"),
    ):
        if (subject, object_id) in existing:
            continue
        rows.append({"subject_id": subject, "subject_label": record["preferred_term"], "predicate_id": predicate,
                     "object_id": object_id, "object_label": object_label, "object_source": object_source,
                     "mapping_justification": "semapv:ManualMappingCuration", "source": source, "mapping_date": MAPPING_DATE,
                     "confidence": confidence, "comment": comment, "other": other,
                     "validation_method": f"manual:apply_669_704_rulings|REGISTRY|{MAPPING_DATE}"})
        added += 1
    _write_rows(comments, fields, rows)
    print(f"rejected tokens scrubbed from {scrubbed} row(s); own-identifier rows synced {synced}; rows added {added}")


# --- membership + counts ------------------------------------------------------


def finish_artifacts(occurrences: Path, log: list, write: bool) -> None:
    # Tricine: identifier remap; Na2-citrate: label-driven moves off the trisodium record.
    moves: dict[tuple[str, str], str] = {}
    with occurrences.open(encoding="utf-8") as handle:
        for row in csv.DictReader(handle, delimiter="\t"):
            if _source_label_key(row.get("preferred_term") or "") == _source_label_key("Na2-citrate") and (row.get("resolved_identifier") or "").strip() == NA2_CITRATE["source_identifier"]:
                moves[(NA2_CITRATE["source_identifier"], row["recipe_id"])] = NA2_CITRATE["identifier"]
    lines = MEMBERSHIP.read_text(encoding="utf-8").splitlines(keepends=True)
    comments, header, data, counts = [], None, [], defaultdict(int)
    for line in lines:
        if line.startswith("#"):
            comments.append(line)
            continue
        cells = line.rstrip("\n").split("\t")
        if header is None:
            header = cells
            continue
        if cells[0] == TRICINE["old"]:
            cells[0] = TRICINE["new"]
            counts[TRICINE["new"]] += 1
        replacement = moves.get((cells[0], cells[1]))
        if replacement:
            cells[0] = replacement
            counts[replacement] += 1
        data.append(cells)
    data.sort(key=lambda cells: tuple(cells[:2]))
    if len({(c[0], c[1]) for c in data}) != len(data):
        raise SystemExit("membership moves would create duplicate edge keys")
    print(f"membership edges moved: {dict(sorted(counts.items()))}")
    if write:
        MEMBERSHIP.write_text("".join(comments) + "\t".join(header) + "\n" + "".join("\t".join(c) + "\n" for c in data), encoding="utf-8")
    affected = {TRICINE["new"]: TRICINE["slug"], NA2_CITRATE["identifier"]: NA2_CITRATE["slug"], NA2_CITRATE["source_identifier"]: NA2_CITRATE["source_slug"]}
    tally: dict[str, list[int]] = defaultdict(lambda: [0, 0])
    for cells in data:
        if cells[0] in affected:
            tally[cells[0]][0] += 1
            tally[cells[0]][1] += int(cells[2])
    for identifier, slug in affected.items():
        if identifier not in tally:
            continue
        path = find(slug)
        record = yaml.safe_load(path.read_text())
        stats = record.get("occurrence_statistics") or {}
        old = (stats.get("media_count") or 0, stats.get("total_occurrences") or 0)
        new = tuple(tally[identifier])
        if old == new:
            continue
        before = sha(path)
        record["occurrence_statistics"] = {**stats, "media_count": new[0], "total_occurrences": new[1]}
        record_curation_event(record, curator=CURATOR, action="REFRESHED_OCCURRENCE_STATISTICS",
                              changes=f"occurrence_statistics {old[0]}/{old[1]} -> {new[0]}/{new[1]} after the #704 identity split/re-grounding moved recipe memberships.",
                              previous_status="MAPPED", new_status="MAPPED", llm_assisted=True, llm_model=LLM_MODEL)
        print(f"OCCURRENCES {slug}: {old[0]}/{old[1]} -> {new[0]}/{new[1]}")
        if write:
            write_validated_ingredient(record, path)
        entry = next((e for e in log if e["source_record"] == str(path.relative_to(ROOT))), None)
        if entry:
            entry["after_yaml_sha256"] = sha(path) if write else None
            entry["change"] += f"; occurrence_statistics {old[0]}/{old[1]} -> {new[0]}/{new[1]}"
        else:
            log.append({"source_record": str(path.relative_to(ROOT)), "shape": "occurrence_refresh", "before_yaml_sha256": before,
                        "after_yaml_sha256": sha(path) if write else None, "change": f"occurrence_statistics {old[0]}/{old[1]} -> {new[0]}/{new[1]}",
                        "verification": "Counts follow the identifier and the source label through SOURCE_LABEL_IDENTIFIER_OVERRIDES."})


def _save_log(path: Path, log: list) -> None:
    previous = json.loads(path.read_text())["records"] if path.is_file() else []
    merged = {e["source_record"]: e for e in previous}
    for entry in log:
        if entry["source_record"] in merged:
            merged[entry["source_record"]]["after_yaml_sha256"] = entry["after_yaml_sha256"]
            merged[entry["source_record"]]["change"] += "; " + entry["change"]
        else:
            merged[entry["source_record"]] = entry
    path.write_text(json.dumps({"issue": "#669/#704", "batch": "rulings", "records": list(merged.values())}, indent=2) + "\n")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--apply", action="store_true")
    parser.add_argument("--log", type=Path)
    parser.add_argument("--finish-sssom", action="store_true")
    parser.add_argument("--finish-artifacts", action="store_true")
    parser.add_argument("--occurrences", type=Path)
    args = parser.parse_args()
    if args.finish_sssom:
        finish_sssom()
        return 0
    log: list = []
    if args.finish_artifacts:
        if not args.occurrences:
            raise SystemExit("--finish-artifacts needs --occurrences")
        finish_artifacts(args.occurrences, log, args.apply)
        if args.apply and args.log:
            _save_log(args.log, log)
        return 0
    chebi = Chebi()
    verify(chebi)
    apply_retirements(log, args.apply)
    apply_tricine(chebi, log, args.apply)
    apply_na2_citrate(log, args.apply)
    print(f"\n{'wrote' if args.apply else 'would write'} {len(log)} record(s)")
    if args.apply and args.log:
        _save_log(args.log, log)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
