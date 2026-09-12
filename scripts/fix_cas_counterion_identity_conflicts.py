#!/usr/bin/env python3
"""Reground five CAS-selected records with salt/counterion conflicts (#455).

`audit_cas_chebi_followup` created these records from CultureBotHT
`compounds_to_cas.csv` by resolving the source CAS-RN through ChEBI xrefs. The
source labels name salts or a tellurite; the selected ChEBI terms name the free
acid, the zwitterion, the organic anion, colistin without sulfate, or already
correct potassium tellurite under the misspelled source label.

Each fix is intentionally literal:

* three salts keep a `cas:` primary identity with the old ChEBI term as their
  nearest parent and PubChem-backed chemistry for the exact salt;
* `Colistin sulfate salt` merges into the existing exact `NCIT:C386`
  `Colistin Sulfate` record;
* `potassium tellurate` is relabelled to `potassium tellurite` because its
  CultureBotHT CAS-RN and selected ChEBI term both denote tellurite.

Dry-run by default; pass `--apply` to write the curated collection and SSSOM.
"""

from __future__ import annotations

import argparse
import csv
import io
import sys
from dataclasses import dataclass
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "src"))

from reground_mapped_record import check_registry_mint  # noqa: E402

from mediaingredientmech.sssom_grading import CONFIDENCE, JUSTIFICATION, PREDICATE  # noqa: E402
from mediaingredientmech.synonym_policy import is_resolving_synonym  # noqa: E402
from mediaingredientmech.utils.object_source import object_source_for  # noqa: E402
from mediaingredientmech.utils.yaml_handler import save_yaml  # noqa: E402

MAPPED = ROOT / "data" / "curated" / "mapped_ingredients.yaml"
SSSOM = ROOT / "mappings" / "ingredient_mappings.sssom.tsv"

STAMP = "2026-09-12T00:00:00+00:00"
DATE = STAMP[:10]
CURATOR = "fix_cas_counterion_identity_conflicts"
ISSUE = "#455"


@dataclass(frozen=True)
class PubChemProperties:
    cid: int
    cas_rn: str
    molecular_formula: str
    smiles: str
    inchi: str


@dataclass(frozen=True)
class CasRegrounding:
    subject_id: str
    preferred_term: str
    old_identifier: str
    old_cas_rn: str
    parent_id: str
    parent_label: str
    exact: PubChemProperties
    stale_synonym_sources: frozenset[str]
    rationale: str

    @property
    def new_identifier(self) -> str:
        return f"cas:{self.exact.cas_rn}"


CAS_REGROUNDINGS = (
    CasRegrounding(
        subject_id="MIM:Glycyrrhizic_Acid_Ammonium_Salt",
        preferred_term="Glycyrrhizic Acid, Ammonium Salt",
        old_identifier="CHEBI:15939",
        old_cas_rn="1405-86-3",
        parent_id="CHEBI:15939",
        parent_label="glycyrrhizinic acid",
        exact=PubChemProperties(
            cid=62074,
            cas_rn="53956-04-0",
            molecular_formula="C42H65NO16",
            smiles=(
                "C[C@]12CC[C@](C[C@H]1C3=CC(=O)[C@@H]4[C@]5(CC[C@@H](C"
                "([C@@H]5CC[C@]4([C@@]3(CC2)C)C)(C)C)O[C@@H]6[C@@H]([C@H]"
                "([C@@H]([C@H](O6)C(=O)O)O)O)O[C@H]7[C@@H]([C@H]([C@@H]"
                "([C@H](O7)C(=O)O)O)O)O)C)(C)C(=O)O.N"
            ),
            inchi=(
                "InChI=1S/C42H62O16.H3N/c1-37(2)21-8-11-42(7)31(20(43)"
                "16-18-19-17-39(4,36(53)54)13-12-38(19,3)14-15-41(18,42)"
                "6)40(21,5)10-9-22(37)55-35-30(26(47)25(46)29(57-35)"
                "33(51)52)58-34-27(48)23(44)24(45)28(56-34)32(49)50;/"
                "h16,19,21-31,34-35,44-48H,8-15,17H2,1-7H3,(H,49,50)"
                "(H,51,52)(H,53,54);1H3/t19-,21-,22-,23-,24-,25-,26-,"
                "27+,28-,29-,30+,31+,34-,35-,38+,39-,40-,41+,42+;/m0./s1"
            ),
        ),
        stale_synonym_sources=frozenset({"chebi_synonym_review"}),
        rationale=(
            "The CultureBotHT label names an ammonium salt, while the ChEBI xref "
            "selected glycyrrhizinic acid without ammonium. PubChem CID 62074 "
            "verifies CAS 53956-04-0 for ammonium glycyrrhizate, and no exact "
            "local ChEBI term denotes this salt."
        ),
    ),
    CasRegrounding(
        subject_id="MIM:Dimethylsulfoniopropionate_Hydrochloride",
        preferred_term="Dimethylsulfoniopropionate hydrochloride",
        old_identifier="CHEBI:16457",
        old_cas_rn="7314-30-9",
        parent_id="CHEBI:16457",
        parent_label="S,S-dimethyl-beta-propiothetin",
        exact=PubChemProperties(
            cid=5316899,
            cas_rn="4337-33-1",
            molecular_formula="C5H11ClO2S",
            smiles="C[S+](C)CCC(=O)O.[Cl-]",
            inchi="InChI=1S/C5H10O2S.ClH/c1-8(2)4-3-5(6)7;/h3-4H2,1-2H3;1H",
        ),
        stale_synonym_sources=frozenset({"chebi_synonym_review"}),
        rationale=(
            "The CultureBotHT label names the hydrochloride/chloride form, while "
            "CHEBI:16457 denotes zwitterionic DMSP with no chloride. PubChem CID "
            "5316899 verifies CAS 4337-33-1 for the chloride, and no exact local "
            "ChEBI term denotes this salt."
        ),
    ),
    CasRegrounding(
        subject_id="MIM:N-lauroylsarcosine_Sodium_Salt",
        preferred_term="N-lauroylsarcosine sodium salt",
        old_identifier="CHEBI:183704",
        old_cas_rn="137-16-6",
        parent_id="CHEBI:183705",
        parent_label="N-Lauroylsarcosine",
        exact=PubChemProperties(
            cid=23668817,
            cas_rn="137-16-6",
            molecular_formula="C15H28NNaO3",
            smiles="CCCCCCCCCCCC(=O)N(C)CC(=O)[O-].[Na+]",
            inchi=(
                "InChI=1S/C15H29NO3.Na/c1-3-4-5-6-7-8-9-10-11-12-14(17)"
                "16(2)13-15(18)19;/h3-13H2,1-2H3,(H,18,19);/q;+1/p-1"
            ),
        ),
        stale_synonym_sources=frozenset({"chebi_synonym_review"}),
        rationale=(
            "The CultureBotHT label and CAS-RN name sodium lauroylsarcosinate, "
            "while CHEBI:183704 denotes only the organic anion. PubChem CID "
            "23668817 verifies CAS 137-16-6 for the sodium salt; CHEBI:183705 is "
            "the local free-acid parent."
        ),
    ),
)


@dataclass(frozen=True)
class LabelCorrection:
    old_subject_id: str
    new_subject_id: str
    old_preferred_term: str
    new_preferred_term: str
    identifier: str
    cas_rn: str
    ontology_id: str
    ontology_label: str


POTASSIUM_TELLURITE = LabelCorrection(
    old_subject_id="MIM:Potassium_Tellurate",
    new_subject_id="MIM:Potassium_Tellurite",
    old_preferred_term="potassium tellurate",
    new_preferred_term="potassium tellurite",
    identifier="CHEBI:75248",
    cas_rn="7790-58-1",
    ontology_id="CHEBI:75248",
    ontology_label="potassium tellurite",
)


def _append_source(source: str) -> str:
    pieces = [piece for piece in source.split("|") if piece]
    tag = f"MIM:curator={CURATOR}"
    if tag not in pieces:
        pieces.append(tag)
    return "|".join(pieces)


def _find_record(
    records: list[dict],
    *,
    identifier: str,
    preferred_term: str,
    status: str | None = "MAPPED",
) -> dict:
    hits = [
        record
        for record in records
        if record.get("identifier") == identifier
        and record.get("preferred_term") == preferred_term
        and (status is None or record.get("mapping_status") == status)
    ]
    if len(hits) != 1:
        raise SystemExit(
            f"{preferred_term!r} on {identifier} matched {len(hits)} record(s), "
            "expected exactly 1"
        )
    return hits[0]


def _supersede_old_evidence(ontology_mapping: dict, reason: str) -> None:
    for evidence in ontology_mapping.get("evidence") or []:
        note = str(evidence.get("notes") or "")
        if not note.startswith("SUPERSEDED"):
            evidence["notes"] = f"SUPERSEDED ({ISSUE}): {reason} Original note follows. {note}"


def _reject_synonyms(record: dict, sources: frozenset[str]) -> int:
    rejected = 0
    for synonym in record.get("synonyms") or []:
        if str(synonym.get("source") or "") not in sources:
            continue
        if synonym.get("synonym_type") != "REJECTED_LABEL":
            synonym["synonym_type"] = "REJECTED_LABEL"
            rejected += 1
    return rejected


def _exact_properties(spec: PubChemProperties) -> dict:
    return {
        "cas_rn": spec.cas_rn,
        "data_source": f"PubChem CID {spec.cid}",
        "retrieval_date": STAMP,
        "pubchem_cid": spec.cid,
        "molecular_formula": spec.molecular_formula,
        "inchi": spec.inchi,
        "smiles": spec.smiles,
    }


def _reground_to_cas(record: dict, spec: CasRegrounding) -> str:
    mapping = record.setdefault("ontology_mapping", {})
    if (
        mapping.get("ontology_id") != spec.old_identifier
        or record.get("identifier") != spec.old_identifier
    ):
        raise SystemExit(
            f"{spec.preferred_term!r} moved since #455 review: "
            f"{record.get('identifier')} -> {mapping.get('ontology_id')}"
        )
    old_chem = record.get("chemical_properties") or {}
    if str(old_chem.get("cas_rn") or "").strip() != spec.old_cas_rn:
        raise SystemExit(
            f"{spec.preferred_term!r} CAS is {old_chem.get('cas_rn')!r}, "
            f"expected {spec.old_cas_rn!r}"
        )

    _supersede_old_evidence(
        mapping,
        "the CAS-selected ChEBI term denotes a different salt/counterion form.",
    )
    rejected = _reject_synonyms(record, spec.stale_synonym_sources)

    record["identifier"] = spec.new_identifier
    record["chemical_properties"] = _exact_properties(spec.exact)
    mapping.update(
        {
            "ontology_id": spec.parent_id,
            "ontology_label": spec.parent_label,
            "ontology_source": "CHEBI",
            "mapping_quality": "NARROW_MATCH",
        }
    )
    mapping.setdefault("evidence", []).append(
        {
            "evidence_type": "CURATOR_JUDGMENT",
            "source": f"MIM curation ({ISSUE})",
            "notes": (
                f"{spec.rationale} Per MAPPING_SEMANTICS.md Section 3, the "
                f"record now uses {spec.new_identifier} as the exact registry "
                f"identity plus a narrowMatch to {spec.parent_id}."
            ),
        }
    )
    record.setdefault("curation_history", []).append(
        {
            "timestamp": STAMP,
            "curator": CURATOR,
            "action": "REGROUNDED_COUNTERION_FORM",
            "changes": (
                f"identifier {spec.old_identifier} -> {spec.new_identifier}; "
                f"CAS-RN {spec.old_cas_rn} -> {spec.exact.cas_rn}; ontology "
                f"mapping set to NARROW_MATCH {spec.parent_id} "
                f"({spec.parent_label!r}). Replaced target-derived chemistry with "
                f"PubChem CID {spec.exact.cid} and marked {rejected} inherited "
                f"ChEBI synonym(s) as REJECTED_LABEL ({ISSUE})."
            ),
            "previous_status": "MAPPED",
            "new_status": "MAPPED",
            "llm_assisted": False,
        }
    )
    return f"REGROUND {spec.preferred_term:<42} {spec.old_identifier} -> {spec.new_identifier}"


def _sssom_other(record: dict, *, object_label: str) -> str:
    drop = {
        str(record.get("preferred_term") or "").strip().casefold(),
        object_label.strip().casefold(),
        "",
    }
    out: list[str] = []
    seen: set[str] = set()
    for synonym in record.get("synonyms") or []:
        if not isinstance(synonym, dict) or not is_resolving_synonym(synonym):
            continue
        token = str(synonym.get("synonym_text") or "").strip()
        key = token.casefold()
        if key in drop or key in seen:
            continue
        out.append(token)
        seen.add(key)
    return "|".join(out)


def _with_cas_token(other: str, cas_rn: str) -> str:
    token = f"CAS:{cas_rn}"
    parts = [part.strip() for part in other.split("|") if part.strip()]
    if not any(part.casefold() == token.casefold() for part in parts):
        parts.append(token)
    return "|".join(parts)


def _blank_row(fieldnames: list[str]) -> dict[str, str]:
    return dict.fromkeys(fieldnames, "")


def _parent_row(
    original: dict[str, str],
    fieldnames: list[str],
    spec: CasRegrounding,
    other: str,
) -> dict[str, str]:
    row = _blank_row(fieldnames)
    row.update(original)
    row.update(
        {
            "predicate_id": PREDICATE["NARROW_MATCH"],
            "object_id": spec.parent_id,
            "object_label": spec.parent_label,
            "object_source": object_source_for(spec.parent_id),
            "mapping_justification": JUSTIFICATION["NARROW_MATCH"],
            "source": _append_source(original.get("source", "")),
            "mapping_date": DATE,
            "confidence": CONFIDENCE["NARROW_MATCH"],
            "comment": (
                f"Local CAS identity retained because no exact ontology term for "
                f"{spec.preferred_term} was verified; {spec.parent_id} is the "
                f"nearest ChEBI parent ({ISSUE})."
            ),
            "other": other,
            "validation_method": "",
        }
    )
    return row


def _registry_row(
    original: dict[str, str],
    fieldnames: list[str],
    *,
    subject_id: str,
    subject_label: str,
    object_id: str,
    object_source: str,
    comment: str,
    other: str,
) -> dict[str, str]:
    row = _blank_row(fieldnames)
    row.update(original)
    row.update(
        {
            "subject_id": subject_id,
            "subject_label": subject_label,
            "predicate_id": PREDICATE["EXACT_MATCH"],
            "object_id": object_id,
            "object_label": subject_label,
            "object_source": object_source,
            "mapping_justification": JUSTIFICATION["NARROW_MATCH"],
            "source": _append_source(original.get("source", "")),
            "mapping_date": DATE,
            "confidence": CONFIDENCE["EXACT_MATCH"],
            "comment": comment,
            "other": other,
            "validation_method": "",
        }
    )
    return row


def _cas_registry_rows(
    original: dict[str, str],
    fieldnames: list[str],
    spec: CasRegrounding,
    other: str,
) -> list[dict[str, str]]:
    kgm_id = check_registry_mint(
        "kgmicrobe.compound:",
        spec.subject_id.split(":", 1)[1],
    )
    exact_other = _with_cas_token(other, spec.exact.cas_rn)
    return [
        _parent_row(original, fieldnames, spec, other),
        _registry_row(
            original,
            fieldnames,
            subject_id=spec.subject_id,
            subject_label=spec.preferred_term,
            object_id=spec.new_identifier,
            object_source=object_source_for(spec.new_identifier),
            comment=(
                f"Registry/identity row preserving {spec.new_identifier} alongside "
                f"parent {spec.parent_id}."
            ),
            other=exact_other,
        ),
        _registry_row(
            original,
            fieldnames,
            subject_id=spec.subject_id,
            subject_label=spec.preferred_term,
            object_id=kgm_id,
            object_source=object_source_for(kgm_id),
            comment=(
                f"Registry/identity row (Rule B1) for narrowMatch subject; "
                f"kg-microbe primary id {kgm_id} alongside parent {spec.parent_id}."
            ),
            other=exact_other,
        ),
    ]


def _merge_colistin(records: list[dict]) -> str:
    loser = _find_record(
        records,
        identifier="CHEBI:37943",
        preferred_term="Colistin sulfate salt",
    )
    winner = _find_record(
        records,
        identifier="NCIT:C386",
        preferred_term="Colistin Sulfate",
    )

    roles = winner.setdefault("physicochemical_roles", [])
    held_roles = {str(role.get("role") or "") for role in roles if isinstance(role, dict)}
    for role in loser.get("physicochemical_roles") or []:
        if str(role.get("role") or "") not in held_roles:
            roles.append(role)

    synonyms = winner.setdefault("synonyms", [])
    if "colistin sulfate salt" not in {
        str(synonym.get("synonym_text") or "").casefold()
        for synonym in synonyms
        if isinstance(synonym, dict)
    }:
        synonyms.append(
            {
                "synonym_text": "Colistin sulfate salt",
                "synonym_type": "RAW_TEXT",
                "source": "MERGED_FROM_CHEBI:37943",
            }
        )

    winner.setdefault("chemical_properties", {})["cas_rn"] = "1264-72-8"
    winner["chemical_properties"]["data_source"] = "CultureBotHT compounds_to_cas.csv"
    winner["chemical_properties"]["retrieval_date"] = STAMP
    winner.setdefault("curation_history", []).append(
        {
            "timestamp": STAMP,
            "curator": CURATOR,
            "action": "MERGED_FROM",
            "changes": (
                "Absorbed 'Colistin sulfate salt' from the CultureBotHT "
                "CAS-selected CHEBI:37943 duplicate. The losing ChEBI target "
                "denoted colistin without sulfate; existing NCIT:C386 denotes "
                f"Colistin Sulfate exactly. Raw label and CAS 1264-72-8 kept ({ISSUE})."
            ),
            "llm_assisted": False,
        }
    )

    loser["identifier"] = "NCIT:C386"
    loser["mapping_status"] = "REJECTED"
    loser["chemical_properties"] = {}
    loser["ontology_mapping"] = {
        "ontology_id": "NCIT:C386",
        "ontology_label": "Colistin Sulfate",
        "ontology_source": "NCIT",
        "mapping_quality": "EXACT_MATCH",
        "evidence": [
            {
                "evidence_type": "CURATOR_JUDGMENT",
                "source": f"MIM curation ({ISSUE})",
                "notes": (
                    "Duplicate of the existing NCIT:C386 'Colistin Sulfate' record; "
                    "the old CHEBI:37943 xref denoted colistin without sulfate."
                ),
            }
        ],
    }
    loser["occurrence_statistics"] = {"total_occurrences": 0, "media_count": 0}
    loser.setdefault("curation_history", []).append(
        {
            "timestamp": STAMP,
            "curator": CURATOR,
            "action": "MERGED_INTO",
            "changes": (
                "Merged into NCIT:C386 'Colistin Sulfate'; this zero-occurrence "
                "CAS-selected duplicate was grounded to CHEBI:37943 colistin "
                f"without sulfate. Tombstoned REJECTED and SSSOM row dropped ({ISSUE})."
            ),
            "llm_assisted": False,
        }
    )
    return "MERGE    Colistin sulfate salt                    CHEBI:37943 -> NCIT:C386"


def _correct_potassium_tellurite(records: list[dict]) -> str:
    spec = POTASSIUM_TELLURITE
    record = _find_record(
        records,
        identifier=spec.identifier,
        preferred_term=spec.old_preferred_term,
    )
    mapping = record.get("ontology_mapping") or {}
    chem = record.get("chemical_properties") or {}
    if mapping.get("ontology_id") != spec.ontology_id:
        raise SystemExit(
            f"{spec.old_preferred_term!r} points at {mapping.get('ontology_id')}, "
            f"expected {spec.ontology_id}"
        )
    if str(chem.get("cas_rn") or "").strip() != spec.cas_rn:
        raise SystemExit(
            f"{spec.old_preferred_term!r} CAS is {chem.get('cas_rn')!r}, "
            f"expected {spec.cas_rn!r}"
        )

    record["preferred_term"] = spec.new_preferred_term
    mapping["ontology_label"] = spec.ontology_label
    mapping["mapping_quality"] = "EXACT_MATCH"
    mapping.setdefault("evidence", []).append(
        {
            "evidence_type": "CURATOR_JUDGMENT",
            "source": f"MIM curation ({ISSUE})",
            "notes": (
                "CultureBotHT imported the label as 'potassium tellurate', but "
                "CAS 7790-58-1 and CHEBI:75248 both denote potassium tellurite. "
                "The record label was corrected to match the exact substance; "
                "the identifier and ontology_id were already correct."
            ),
        }
    )
    record.setdefault("curation_history", []).append(
        {
            "timestamp": STAMP,
            "curator": CURATOR,
            "action": "CORRECTED_SOURCE_LABEL",
            "changes": (
                "preferred_term 'potassium tellurate' -> 'potassium tellurite'. "
                "CAS 7790-58-1 and CHEBI:75248 both denote potassium tellurite, "
                f"so the previous CultureBotHT label was a typo ({ISSUE})."
            ),
            "previous_status": "MAPPED",
            "new_status": "MAPPED",
            "llm_assisted": False,
        }
    )
    return "RELABEL  potassium tellurate                    -> potassium tellurite"


def _rewrite_potassium_row(
    row: dict[str, str],
    fieldnames: list[str],
    record: dict,
) -> dict[str, str]:
    spec = POTASSIUM_TELLURITE
    out = _blank_row(fieldnames)
    out.update(row)
    out.update(
        {
            "subject_id": spec.new_subject_id,
            "subject_label": spec.new_preferred_term,
            "object_id": spec.ontology_id,
            "object_label": spec.ontology_label,
            "object_source": object_source_for(spec.ontology_id),
            "predicate_id": PREDICATE["EXACT_MATCH"],
            "mapping_justification": JUSTIFICATION["EXACT_MATCH"],
            "source": _append_source(row.get("source", "")),
            "mapping_date": DATE,
            "confidence": CONFIDENCE["EXACT_MATCH"],
            "other": _with_cas_token(
                _sssom_other(record, object_label=spec.ontology_label),
                spec.cas_rn,
            ),
            "validation_method": "",
        }
    )
    return out


def _add_cas_to_colistin_winner_row(row: dict[str, str], fieldnames: list[str]) -> dict[str, str]:
    out = _blank_row(fieldnames)
    out.update(row)
    out["other"] = _with_cas_token(out.get("other", ""), "1264-72-8")
    return out


def rewrite_sssom(records: list[dict]) -> tuple[str, int, int, int]:
    lines = SSSOM.read_text(encoding="utf-8").splitlines(keepends=True)
    preamble = [line for line in lines if line.startswith("#")]
    body = [line for line in lines if not line.startswith("#")]
    if not body:
        raise SystemExit("SSSOM body is empty")

    header = body[0].rstrip("\n")
    fieldnames = header.split("\t")
    by_subject = {spec.subject_id: spec for spec in CAS_REGROUNDINGS}
    record_by_label = {str(record.get("preferred_term") or ""): record for record in records}

    regrounded = 0
    merged = 0
    relabelled = 0
    out = io.StringIO()
    writer = csv.DictWriter(out, fieldnames=fieldnames, delimiter="\t", lineterminator="\n")
    out.write(f"{header}\n")

    for line in body[1:]:
        row = next(csv.DictReader(io.StringIO(f"{header}\n{line}"), delimiter="\t"))
        spec = by_subject.get(row.get("subject_id") or "")
        if spec is not None:
            if row.get("object_id") != spec.old_identifier:
                raise SystemExit(
                    f"{spec.subject_id} points at {row.get('object_id')}, "
                    f"expected {spec.old_identifier}"
                )
            record = record_by_label[spec.preferred_term]
            other = _sssom_other(record, object_label=spec.parent_label)
            writer.writerows(_cas_registry_rows(row, fieldnames, spec, other))
            regrounded += 1
            continue

        if row.get("subject_id") == "MIM:Colistin_Sulfate_Salt":
            merged += 1
            continue

        if row.get("subject_id") == POTASSIUM_TELLURITE.old_subject_id:
            writer.writerow(
                _rewrite_potassium_row(
                    row,
                    fieldnames,
                    record_by_label[POTASSIUM_TELLURITE.new_preferred_term],
                )
            )
            relabelled += 1
            continue

        if row.get("subject_id") == "MIM:Colistin_Sulfate":
            writer.writerow(_add_cas_to_colistin_winner_row(row, fieldnames))
            continue

        out.write(line)
        if not line.endswith("\n"):
            out.write("\n")

    if regrounded != len(CAS_REGROUNDINGS):
        raise SystemExit(f"rewrote {regrounded} CAS rows, expected {len(CAS_REGROUNDINGS)}")
    if merged != 1:
        raise SystemExit(f"dropped {merged} colistin row(s), expected 1")
    if relabelled != 1:
        raise SystemExit(f"rewrote {relabelled} potassium row(s), expected 1")

    return "".join(preamble) + out.getvalue(), regrounded, merged, relabelled


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args(argv)

    collection = yaml.safe_load(MAPPED.read_text(encoding="utf-8")) or {}
    records = collection.get("ingredients") or []
    output = [
        _reground_to_cas(
            _find_record(
                records,
                identifier=spec.old_identifier,
                preferred_term=spec.preferred_term,
            ),
            spec,
        )
        for spec in CAS_REGROUNDINGS
    ]
    output.append(_merge_colistin(records))
    output.append(_correct_potassium_tellurite(records))

    sssom_text, regrounded, merged, relabelled = rewrite_sssom(records)

    if args.apply:
        save_yaml(collection, MAPPED, validate=True, target_class="IngredientCollection")
        SSSOM.write_text(sssom_text, encoding="utf-8")

    print(
        f"{'APPLIED' if args.apply else 'DRY RUN (re-run with --apply)'} - "
        f"{regrounded} CAS regrounding(s), {merged} merge(s), "
        f"{relabelled} label correction(s)\n"
    )
    for line in output:
        print(f"  {line}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
