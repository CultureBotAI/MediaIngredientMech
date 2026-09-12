#!/usr/bin/env python3
"""Reground ten CAS-selected records with stereochemical conflicts (#456).

`audit_cas_chebi_followup` created these records from CultureBotHT
`compounds_to_cas.csv` by resolving each source CAS-RN through ChEBI xrefs. The
source labels name racemates, a cis/Z ester, or a fixed optical/alkene isomer,
but the selected ChEBI rows point at a single stereoisomer or at a
stereo-unspecified parent.

Each fix is intentionally literal:

* six DL/racemic forms keep their source `cas:` identity with the
  stereo-unspecified ChEBI term as the nearest parent;
* the alpha-toxicarol racemate uses a local `kgmicrobe.compound:`
  fallback identity because its imported CAS number belongs to a fixed
  stereoisomer and no broader ChEBI parent was verified;
* the cis methyl p-coumarate record uses a local `kgmicrobe.compound:`
  identity with a narrow mapping to its stereo-unspecified ChEBI parent;
* `Perillic Acid (-)` and `Trans,Trans-Farnesol` move to exact stereospecific
  ChEBI terms.

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
sys.path.insert(0, str(ROOT / "scripts"))

from reground_mapped_record import check_registry_mint  # noqa: E402

from mediaingredientmech.sssom_grading import CONFIDENCE, JUSTIFICATION, PREDICATE  # noqa: E402
from mediaingredientmech.synonym_policy import is_resolving_synonym  # noqa: E402
from mediaingredientmech.utils.object_source import object_source_for  # noqa: E402
from mediaingredientmech.utils.yaml_handler import save_yaml  # noqa: E402

MAPPED = ROOT / "data" / "curated" / "mapped_ingredients.yaml"
SSSOM = ROOT / "mappings" / "ingredient_mappings.sssom.tsv"

STAMP = "2026-09-12T00:00:00+00:00"
DATE = STAMP[:10]
CURATOR = "fix_cas_stereochemical_identity_conflicts"
ISSUE = "#456"


@dataclass(frozen=True)
class ChemicalProperties:
    molecular_formula: str
    data_source: str
    smiles: str | None = None
    inchi: str | None = None
    cas_rn: str | None = None
    pubchem_cid: int | None = None

    def to_dict(self) -> dict[str, object]:
        out: dict[str, object] = {
            "data_source": self.data_source,
            "retrieval_date": STAMP,
            "molecular_formula": self.molecular_formula,
        }
        if self.cas_rn is not None:
            out["cas_rn"] = self.cas_rn
        if self.pubchem_cid is not None:
            out["pubchem_cid"] = self.pubchem_cid
        if self.inchi is not None:
            out["inchi"] = self.inchi
        if self.smiles is not None:
            out["smiles"] = self.smiles
        return out


@dataclass(frozen=True)
class RegistryRegrounding:
    subject_id: str
    preferred_term: str
    old_identifier: str
    old_cas_rn: str
    parent_id: str
    parent_label: str
    primary_identifier: str
    exact: ChemicalProperties
    rationale: str
    stale_synonym_sources: frozenset[str] = frozenset({"chebi_synonym_review"})

    @property
    def cas_identifier(self) -> str | None:
        if self.exact.cas_rn is None:
            return None
        return f"cas:{self.exact.cas_rn}"


@dataclass(frozen=True)
class FallbackRegistryRegrounding:
    subject_id: str
    preferred_term: str
    old_identifier: str
    old_cas_rn: str
    primary_identifier: str
    exact: ChemicalProperties
    rationale: str
    stale_synonym_sources: frozenset[str] = frozenset({"chebi_synonym_review"})


CAS_REGROUNDINGS = (
    RegistryRegrounding(
        subject_id="MIM:DL-2-Aminobutyric_Acid",
        preferred_term="DL-2-Aminobutyric acid",
        old_identifier="CHEBI:35621",
        old_cas_rn="2835-81-6",
        parent_id="CHEBI:35621",
        parent_label="alpha-aminobutyric acid",
        primary_identifier="cas:2835-81-6",
        exact=ChemicalProperties(
            cas_rn="2835-81-6",
            data_source="CultureBotHT compounds_to_cas.csv; ChEBI:35621",
            molecular_formula="C4H9NO2",
            inchi="InChI=1S/C4H9NO2/c1-2-3(5)4(6)7/h3H,2,5H2,1H3,(H,6,7)",
            smiles="CCC(N)C(=O)O",
        ),
        rationale=(
            "The CultureBotHT label and CAS-RN name the DL/racemic form, while "
            "CHEBI:35621 is stereo-unspecified and has separate D and L children. "
            "No exact local ChEBI term denotes the racemate."
        ),
    ),
    RegistryRegrounding(
        subject_id="MIM:DL-3-Aminoisobutyric_Acid",
        preferred_term="DL-3-Aminoisobutyric acid",
        old_identifier="CHEBI:27389",
        old_cas_rn="144-90-1",
        parent_id="CHEBI:27389",
        parent_label="3-aminoisobutyric acid",
        primary_identifier="cas:144-90-1",
        exact=ChemicalProperties(
            cas_rn="144-90-1",
            data_source="CultureBotHT compounds_to_cas.csv; PubChem CID 64956",
            pubchem_cid=64956,
            molecular_formula="C4H9NO2",
            inchi="InChI=1S/C4H9NO2/c1-3(2-5)4(6)7/h3H,2,5H2,1H3,(H,6,7)",
            smiles="CC(CN)C(=O)O",
        ),
        rationale=(
            "The CultureBotHT label and CAS-RN name the DL/racemic form, while "
            "CHEBI:27389 is stereo-unspecified and has separate R and S children. "
            "No exact local ChEBI term denotes the racemate."
        ),
    ),
    RegistryRegrounding(
        subject_id="MIM:DL-Glyceraldehyde_3-phosphate",
        preferred_term="DL-Glyceraldehyde 3-phosphate",
        old_identifier="CHEBI:17138",
        old_cas_rn="591-59-3",
        parent_id="CHEBI:17138",
        parent_label="glyceraldehyde 3-phosphate",
        primary_identifier="cas:591-59-3",
        exact=ChemicalProperties(
            cas_rn="591-59-3",
            data_source="CultureBotHT compounds_to_cas.csv; PubChem CID 729",
            pubchem_cid=729,
            molecular_formula="C3H7O6P",
            inchi=("InChI=1S/C3H7O6P/c4-1-3(5)2-9-10(6,7)8/" "h1,3,5H,2H2,(H2,6,7,8)"),
            smiles="[H]C(=O)C(O)COP(=O)(O)O",
        ),
        rationale=(
            "The CultureBotHT label and CAS-RN name the DL/racemic form, while "
            "CHEBI:17138 is stereo-unspecified and has separate D and L children. "
            "No exact local ChEBI term denotes the racemate."
        ),
    ),
    RegistryRegrounding(
        subject_id="MIM:DL-glyceraldehyde",
        preferred_term="DL-glyceraldehyde",
        old_identifier="CHEBI:5445",
        old_cas_rn="56-82-6",
        parent_id="CHEBI:5445",
        parent_label="glyceraldehyde",
        primary_identifier="cas:56-82-6",
        exact=ChemicalProperties(
            cas_rn="56-82-6",
            data_source="CultureBotHT compounds_to_cas.csv; PubChem CID 751",
            pubchem_cid=751,
            molecular_formula="C3H6O3",
            inchi="InChI=1S/C3H6O3/c4-1-3(6)2-5/h1,3,5-6H,2H2",
            smiles="[H]C(=O)C(O)CO",
        ),
        rationale=(
            "The CultureBotHT label and CAS-RN name the DL/racemic form, while "
            "CHEBI:5445 is stereo-unspecified and has separate D and L children. "
            "No exact local ChEBI term denotes the racemate."
        ),
    ),
    RegistryRegrounding(
        subject_id="MIM:N-_3-oxohexanoyl-dl-homoserine_Lactone",
        preferred_term="N-(3-oxohexanoyl)-DL-homoserine lactone",
        old_identifier="CHEBI:29640",
        old_cas_rn="76924-95-3",
        parent_id="CHEBI:29640",
        parent_label="N-(3-oxohexanoyl)homoserine lactone",
        primary_identifier="cas:76924-95-3",
        exact=ChemicalProperties(
            cas_rn="76924-95-3",
            data_source="CultureBotHT compounds_to_cas.csv; PubChem CID 119133",
            pubchem_cid=119133,
            molecular_formula="C10H15NO4",
            inchi=(
                "InChI=1S/C10H15NO4/c1-2-3-7(12)6-9(13)11-8-4-5-"
                "15-10(8)14/h8H,2-6H2,1H3,(H,11,13)"
            ),
            smiles="CCCC(=O)CC(=O)NC1CCOC1=O",
        ),
        rationale=(
            "The CultureBotHT label and CAS-RN name the DL/racemic homoserine "
            "lactone, while CHEBI:29640 is stereo-unspecified and has a separate "
            "L child. No exact local ChEBI term denotes the racemate."
        ),
    ),
    RegistryRegrounding(
        subject_id="MIM:Rac-3-Hydroxypentanoic_Acid",
        preferred_term="rac-3-Hydroxypentanoic Acid",
        old_identifier="CHEBI:139272",
        old_cas_rn="10237-77-1",
        parent_id="CHEBI:139272",
        parent_label="3-hydroxypentanoic acid",
        primary_identifier="cas:10237-77-1",
        exact=ChemicalProperties(
            cas_rn="10237-77-1",
            data_source="CultureBotHT compounds_to_cas.csv; PubChem CID 107802",
            pubchem_cid=107802,
            molecular_formula="C5H10O3",
            inchi="InChI=1S/C5H10O3/c1-2-4(6)3-5(7)8/h4,6H,2-3H2,1H3,(H,7,8)",
            smiles="CCC(O)CC(=O)O",
        ),
        rationale=(
            "The CultureBotHT label and CAS-RN name a racemate, while "
            "CHEBI:139272 is stereo-unspecified and has separate R and S "
            "children. No exact local ChEBI term denotes the racemate."
        ),
    ),
)

KGM_REGROUNDINGS = (
    RegistryRegrounding(
        subject_id="MIM:Methyl-cis-p-coumarate",
        preferred_term="methyl-cis-p-coumarate",
        old_identifier="CHEBI:86904",
        old_cas_rn="3943-97-3",
        parent_id="CHEBI:86904",
        parent_label="4-coumaric acid methyl ester",
        primary_identifier="kgmicrobe.compound:methyl-cis-p-coumarate",
        exact=ChemicalProperties(
            data_source="ChEBI:86904 formula only",
            molecular_formula="C10H10O3",
        ),
        rationale=(
            "The CultureBotHT label names the cis/Z ester, while CHEBI:86904 is "
            "stereo-unspecified and CAS 3943-97-3 denotes the trans/E ester. No "
            "exact local ChEBI term or CAS number was verified for the cis form."
        ),
    ),
)

REGISTRY_REGROUNDINGS = CAS_REGROUNDINGS + KGM_REGROUNDINGS

FALLBACK_REGROUNDINGS = (
    FallbackRegistryRegrounding(
        subject_id="MIM:Alpha-toxicarol_Dl",
        preferred_term="Alpha-Toxicarol (Dl)",
        old_identifier="CHEBI:9643",
        old_cas_rn="82-09-7",
        primary_identifier="kgmicrobe.compound:alpha-toxicarol_dl",
        exact=ChemicalProperties(
            data_source="CHEBI:9643 formula only",
            molecular_formula="C23H22O7",
        ),
        rationale=(
            "The CultureBotHT label names the DL/racemic form, while CHEBI:9643 "
            "and CAS 82-09-7 denote a fixed stereoisomer. No exact local ChEBI "
            "term, CAS number, or broader ontology parent was verified for the "
            "racemate."
        ),
    ),
)


@dataclass(frozen=True)
class ExactChebiRegrounding:
    subject_id: str
    preferred_term: str
    old_identifier: str
    old_cas_rn: str
    new_identifier: str
    new_label: str
    exact: ChemicalProperties
    rationale: str
    stale_synonym_sources: frozenset[str] = frozenset({"chebi_synonym_review"})


EXACT_CHEBI_REGROUNDINGS = (
    ExactChebiRegrounding(
        subject_id="MIM:Perillic_Acid",
        preferred_term="Perillic Acid (-)",
        old_identifier="CHEBI:36999",
        old_cas_rn="7694-45-3",
        new_identifier="CHEBI:109544",
        new_label="(4R)-4-(1-methylethenyl)-1-cyclohexenecarboxylic acid",
        exact=ChemicalProperties(
            data_source="PubChem CID 5702197",
            pubchem_cid=5702197,
            molecular_formula="C10H14O2",
            inchi=(
                "InChI=1S/C10H14O2/c1-7(2)8-3-5-9(6-4-8)10(11)12/"
                "h5,8H,1,3-4,6H2,2H3,(H,11,12)/t8-/m0/s1"
            ),
            smiles="C=C(C)[C@H]1CC=C(C(=O)O)CC1",
        ),
        rationale=(
            "The CultureBotHT label names the (-) enantiomer. PubChem CID "
            "5702197 has the same stereochemical InChIKey as CHEBI:109544, "
            "while the old CHEBI:36999 target is stereo-unspecified."
        ),
    ),
    ExactChebiRegrounding(
        subject_id="MIM:TransTrans-Farnesol",
        preferred_term="Trans,Trans-Farnesol",
        old_identifier="CHEBI:28600",
        old_cas_rn="4602-84-0",
        new_identifier="CHEBI:16619",
        new_label="(2-trans,6-trans)-farnesol",
        exact=ChemicalProperties(
            cas_rn="106-28-5",
            data_source="PubChem CID 445070",
            pubchem_cid=445070,
            molecular_formula="C15H26O",
            inchi=(
                "InChI=1S/C15H26O/c1-13(2)7-5-8-14(3)9-6-10-"
                "15(4)11-12-16/h7,9,11,16H,5-6,8,10,12H2,1-4H3/"
                "b14-9+,15-11+"
            ),
            smiles="CC(C)=CCC/C(C)=C/CC/C(C)=C/CO",
        ),
        rationale=(
            "The CultureBotHT label names the (2E,6E) isomer. CHEBI:16619 and "
            "PubChem CID 445070 denote (2-trans,6-trans)-farnesol, while the old "
            "CHEBI:28600 target and CAS 4602-84-0 are stereo-unspecified."
        ),
    ),
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


def _guard(record: dict, *, preferred_term: str, old_identifier: str, old_cas_rn: str) -> dict:
    mapping = record.setdefault("ontology_mapping", {})
    if mapping.get("ontology_id") != old_identifier or record.get("identifier") != old_identifier:
        raise SystemExit(
            f"{preferred_term!r} moved since #456 review: "
            f"{record.get('identifier')} -> {mapping.get('ontology_id')}"
        )
    old_chem = record.get("chemical_properties") or {}
    if str(old_chem.get("cas_rn") or "").strip() != old_cas_rn:
        raise SystemExit(
            f"{preferred_term!r} CAS is {old_chem.get('cas_rn')!r}, " f"expected {old_cas_rn!r}"
        )
    return mapping


def _kgm_identifier(subject_id: str) -> str:
    return check_registry_mint(
        "kgmicrobe.compound:",
        subject_id.split(":", 1)[1],
    )


def _reground_to_registry(record: dict, spec: RegistryRegrounding) -> str:
    mapping = _guard(
        record,
        preferred_term=spec.preferred_term,
        old_identifier=spec.old_identifier,
        old_cas_rn=spec.old_cas_rn,
    )
    kgm_identifier = _kgm_identifier(spec.subject_id)
    if spec.primary_identifier.startswith("kgmicrobe.") and (
        spec.primary_identifier != kgm_identifier
    ):
        raise SystemExit(
            f"{spec.primary_identifier} will not satisfy Rule B1 for {spec.subject_id}; "
            f"expected {kgm_identifier}"
        )

    _supersede_old_evidence(
        mapping,
        "the CAS-selected ChEBI term denotes a different stereochemical form.",
    )
    rejected = _reject_synonyms(record, spec.stale_synonym_sources)

    record["identifier"] = spec.primary_identifier
    record["chemical_properties"] = spec.exact.to_dict()
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
                f"record now uses {spec.primary_identifier} as the exact registry "
                f"identity plus a narrowMatch to {spec.parent_id}."
            ),
        }
    )
    record.setdefault("curation_history", []).append(
        {
            "timestamp": STAMP,
            "curator": CURATOR,
            "action": "REGROUNDED_STEREOCHEMICAL_FORM",
            "changes": (
                f"identifier {spec.old_identifier} -> {spec.primary_identifier}; "
                f"ontology mapping set to NARROW_MATCH {spec.parent_id} "
                f"({spec.parent_label!r}). Replaced target-derived chemistry "
                f"and marked {rejected} inherited ChEBI synonym(s) as "
                f"REJECTED_LABEL ({ISSUE})."
            ),
            "previous_status": "MAPPED",
            "new_status": "MAPPED",
            "llm_assisted": False,
        }
    )
    return (
        f"REGROUND {spec.preferred_term:<45} " f"{spec.old_identifier} -> {spec.primary_identifier}"
    )


def _reground_to_fallback(record: dict, spec: FallbackRegistryRegrounding) -> str:
    mapping = _guard(
        record,
        preferred_term=spec.preferred_term,
        old_identifier=spec.old_identifier,
        old_cas_rn=spec.old_cas_rn,
    )
    kgm_identifier = _kgm_identifier(spec.subject_id)
    if spec.primary_identifier != kgm_identifier:
        raise SystemExit(
            f"{spec.primary_identifier} does not match the derived local "
            f"compound id for {spec.subject_id}; "
            f"expected {kgm_identifier}"
        )

    _supersede_old_evidence(
        mapping,
        "the CAS-selected ChEBI term denotes a sibling stereochemical form.",
    )
    rejected = _reject_synonyms(record, spec.stale_synonym_sources)

    record["identifier"] = spec.primary_identifier
    record["chemical_properties"] = spec.exact.to_dict()
    mapping.update(
        {
            "ontology_id": spec.primary_identifier,
            "ontology_label": spec.preferred_term,
            "ontology_source": "kgmicrobe.compound",
            "mapping_quality": "FALLBACK_REGISTRY",
        }
    )
    mapping.setdefault("evidence", []).append(
        {
            "evidence_type": "CURATOR_JUDGMENT",
            "source": f"MIM curation ({ISSUE})",
            "notes": (
                f"{spec.rationale} The record now keeps "
                f"{spec.primary_identifier} as a local fallback identity without "
                "an ontology row."
            ),
        }
    )
    record.setdefault("curation_history", []).append(
        {
            "timestamp": STAMP,
            "curator": CURATOR,
            "action": "REGROUNDED_STEREOCHEMICAL_FORM",
            "changes": (
                f"identifier {spec.old_identifier} -> {spec.primary_identifier}; "
                "removed the sibling ChEBI stereoisomer mapping. Replaced "
                f"target-derived chemistry and marked {rejected} inherited ChEBI "
                f"synonym(s) as REJECTED_LABEL ({ISSUE})."
            ),
            "previous_status": "MAPPED",
            "new_status": "MAPPED",
            "llm_assisted": False,
        }
    )
    return (
        f"REGROUND {spec.preferred_term:<45} " f"{spec.old_identifier} -> {spec.primary_identifier}"
    )


def _reground_to_exact_chebi(record: dict, spec: ExactChebiRegrounding) -> str:
    mapping = _guard(
        record,
        preferred_term=spec.preferred_term,
        old_identifier=spec.old_identifier,
        old_cas_rn=spec.old_cas_rn,
    )
    _supersede_old_evidence(
        mapping,
        "the CAS-selected ChEBI term denotes a broader stereochemical parent.",
    )
    rejected = _reject_synonyms(record, spec.stale_synonym_sources)

    record["identifier"] = spec.new_identifier
    record["chemical_properties"] = spec.exact.to_dict()
    mapping.update(
        {
            "ontology_id": spec.new_identifier,
            "ontology_label": spec.new_label,
            "ontology_source": "CHEBI",
            "mapping_quality": "EXACT_MATCH",
        }
    )
    mapping.setdefault("evidence", []).append(
        {
            "evidence_type": "CURATOR_JUDGMENT",
            "source": f"MIM curation ({ISSUE})",
            "notes": (
                f"{spec.rationale} The record now maps exactly to "
                f"{spec.new_identifier} instead of the old "
                f"{spec.old_identifier} stereo-unspecified parent."
            ),
        }
    )
    record.setdefault("curation_history", []).append(
        {
            "timestamp": STAMP,
            "curator": CURATOR,
            "action": "REGROUNDED_STEREOCHEMICAL_FORM",
            "changes": (
                f"identifier {spec.old_identifier} -> {spec.new_identifier}; "
                f"ontology mapping set to EXACT_MATCH {spec.new_identifier} "
                f"({spec.new_label!r}). Replaced target-derived chemistry and "
                f"marked {rejected} inherited ChEBI synonym(s) as REJECTED_LABEL "
                f"({ISSUE})."
            ),
            "previous_status": "MAPPED",
            "new_status": "MAPPED",
            "llm_assisted": False,
        }
    )
    return f"REGROUND {spec.preferred_term:<45} " f"{spec.old_identifier} -> {spec.new_identifier}"


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


def _with_cas_token(other: str, cas_rn: str | None) -> str:
    if cas_rn is None:
        return other
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
    spec: RegistryRegrounding,
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
                f"Local stereochemical identity retained because no exact ontology "
                f"term for {spec.preferred_term} was verified; {spec.parent_id} is "
                f"the nearest ChEBI parent ({ISSUE})."
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
    confidence: str = CONFIDENCE["EXACT_MATCH"],
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
            "confidence": confidence,
            "comment": comment,
            "other": other,
            "validation_method": "",
        }
    )
    return row


def _registry_rows(
    original: dict[str, str],
    fieldnames: list[str],
    spec: RegistryRegrounding,
    other: str,
) -> list[dict[str, str]]:
    kgm_id = _kgm_identifier(spec.subject_id)
    exact_other = _with_cas_token(other, spec.exact.cas_rn)
    rows = [_parent_row(original, fieldnames, spec, other)]

    if spec.cas_identifier is not None:
        rows.append(
            _registry_row(
                original,
                fieldnames,
                subject_id=spec.subject_id,
                subject_label=spec.preferred_term,
                object_id=spec.cas_identifier,
                object_source=object_source_for(spec.cas_identifier),
                comment=(
                    f"CAS identity row preserving {spec.cas_identifier} alongside "
                    f"parent {spec.parent_id}."
                ),
                other=exact_other,
            )
        )

    rows.append(
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
        )
    )
    return rows


def _fallback_row(
    original: dict[str, str],
    fieldnames: list[str],
    spec: FallbackRegistryRegrounding,
    other: str,
) -> dict[str, str]:
    return _registry_row(
        original,
        fieldnames,
        subject_id=spec.subject_id,
        subject_label=spec.preferred_term,
        object_id=spec.primary_identifier,
        object_source=object_source_for(spec.primary_identifier),
        comment=(
            f"Local registry identity retained because no exact ontology term or "
            f"broader ontology parent for {spec.preferred_term} was verified "
            f"({ISSUE})."
        ),
        other=other,
        confidence=CONFIDENCE["FALLBACK_REGISTRY"],
    )


def _exact_chebi_row(
    row: dict[str, str],
    fieldnames: list[str],
    record: dict,
    spec: ExactChebiRegrounding,
) -> dict[str, str]:
    out = _blank_row(fieldnames)
    out.update(row)
    out.update(
        {
            "object_id": spec.new_identifier,
            "object_label": spec.new_label,
            "object_source": object_source_for(spec.new_identifier),
            "predicate_id": PREDICATE["EXACT_MATCH"],
            "mapping_justification": JUSTIFICATION["EXACT_MATCH"],
            "source": _append_source(row.get("source", "")),
            "mapping_date": DATE,
            "confidence": CONFIDENCE["EXACT_MATCH"],
            "other": _with_cas_token(
                _sssom_other(record, object_label=spec.new_label),
                spec.exact.cas_rn,
            ),
            "validation_method": "",
        }
    )
    return out


def rewrite_sssom(records: list[dict]) -> tuple[str, int, int]:
    lines = SSSOM.read_text(encoding="utf-8").splitlines(keepends=True)
    preamble = [line for line in lines if line.startswith("#")]
    body = [line for line in lines if not line.startswith("#")]
    if not body:
        raise SystemExit("SSSOM body is empty")

    header = body[0].rstrip("\n")
    fieldnames = header.split("\t")
    registry_by_subject = {spec.subject_id: spec for spec in REGISTRY_REGROUNDINGS}
    fallback_by_subject = {spec.subject_id: spec for spec in FALLBACK_REGROUNDINGS}
    exact_by_subject = {spec.subject_id: spec for spec in EXACT_CHEBI_REGROUNDINGS}
    record_by_label = {str(record.get("preferred_term") or ""): record for record in records}

    registry_count = 0
    fallback_count = 0
    exact_count = 0
    out = io.StringIO()
    writer = csv.DictWriter(out, fieldnames=fieldnames, delimiter="\t", lineterminator="\n")
    out.write(f"{header}\n")

    for line in body[1:]:
        row = next(csv.DictReader(io.StringIO(f"{header}\n{line}"), delimiter="\t"))
        fallback_spec = fallback_by_subject.get(row.get("subject_id") or "")
        if fallback_spec is not None:
            if row.get("object_id") != fallback_spec.old_identifier:
                raise SystemExit(
                    f"{fallback_spec.subject_id} points at {row.get('object_id')}, "
                    f"expected {fallback_spec.old_identifier}"
                )
            record = record_by_label[fallback_spec.preferred_term]
            other = _sssom_other(record, object_label=fallback_spec.preferred_term)
            writer.writerow(_fallback_row(row, fieldnames, fallback_spec, other))
            fallback_count += 1
            continue

        registry_spec = registry_by_subject.get(row.get("subject_id") or "")
        if registry_spec is not None:
            if row.get("object_id") != registry_spec.old_identifier:
                raise SystemExit(
                    f"{registry_spec.subject_id} points at {row.get('object_id')}, "
                    f"expected {registry_spec.old_identifier}"
                )
            record = record_by_label[registry_spec.preferred_term]
            other = _sssom_other(record, object_label=registry_spec.parent_label)
            writer.writerows(_registry_rows(row, fieldnames, registry_spec, other))
            registry_count += 1
            continue

        exact_spec = exact_by_subject.get(row.get("subject_id") or "")
        if exact_spec is not None:
            if row.get("object_id") != exact_spec.old_identifier:
                raise SystemExit(
                    f"{exact_spec.subject_id} points at {row.get('object_id')}, "
                    f"expected {exact_spec.old_identifier}"
                )
            writer.writerow(
                _exact_chebi_row(
                    row,
                    fieldnames,
                    record_by_label[exact_spec.preferred_term],
                    exact_spec,
                )
            )
            exact_count += 1
            continue

        out.write(line)
        if not line.endswith("\n"):
            out.write("\n")

    if registry_count != len(REGISTRY_REGROUNDINGS):
        raise SystemExit(
            f"rewrote {registry_count} registry rows, " f"expected {len(REGISTRY_REGROUNDINGS)}"
        )
    if fallback_count != len(FALLBACK_REGROUNDINGS):
        raise SystemExit(
            f"rewrote {fallback_count} fallback row(s), " f"expected {len(FALLBACK_REGROUNDINGS)}"
        )
    if exact_count != len(EXACT_CHEBI_REGROUNDINGS):
        raise SystemExit(
            f"rewrote {exact_count} exact ChEBI rows, " f"expected {len(EXACT_CHEBI_REGROUNDINGS)}"
        )

    return "".join(preamble) + out.getvalue(), registry_count, fallback_count, exact_count


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
        _reground_to_registry(
            _find_record(
                records,
                identifier=spec.old_identifier,
                preferred_term=spec.preferred_term,
            ),
            spec,
        )
        for spec in REGISTRY_REGROUNDINGS
    ]
    output.extend(
        _reground_to_fallback(
            _find_record(
                records,
                identifier=spec.old_identifier,
                preferred_term=spec.preferred_term,
            ),
            spec,
        )
        for spec in FALLBACK_REGROUNDINGS
    )
    output.extend(
        _reground_to_exact_chebi(
            _find_record(
                records,
                identifier=spec.old_identifier,
                preferred_term=spec.preferred_term,
            ),
            spec,
        )
        for spec in EXACT_CHEBI_REGROUNDINGS
    )

    sssom_text, registry_count, fallback_count, exact_count = rewrite_sssom(records)

    if args.apply:
        save_yaml(collection, MAPPED, validate=True, target_class="IngredientCollection")
        SSSOM.write_text(sssom_text, encoding="utf-8")

    print(
        f"{'APPLIED' if args.apply else 'DRY RUN (re-run with --apply)'} - "
        f"{registry_count} registry regrounding(s), "
        f"{fallback_count} fallback regrounding(s), "
        f"{exact_count} exact ChEBI regrounding(s)\n"
    )
    for line in output:
        print(f"  {line}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
