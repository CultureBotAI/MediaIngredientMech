#!/usr/bin/env python3
"""Apply the verified #312 batch-2 corrections: twelve identity re-groundings.

Batch 1 (#739) held the proposals that changed no identifier. This batch holds
the ones that do, each re-verified against ``chebi.db`` / ``mesh.db`` /
``ncit.db`` and, where the CAS number decides the form, against PubChem
(InChIKey of the CAS's compound equals the ChEBI term's InChIKey). The script
re-checks every ontology fact it depends on at run time and refuses to write
if one no longer holds; the PubChem InChIKeys were fetched on 2026-09-22 and
are pinned below with their CIDs.

Shapes (MAPPING_SEMANTICS.md Section 3):

* **Promote the parent to the identity** (step 1): the ``broadMatch`` parent
  *is* the substance, so the parent becomes ``identifier`` with ``exactMatch``.
  The ``cas:`` row stays as the registry/identity row. #326 also dropped the
  ``kgmicrobe.*`` registry row for 72-Dihydroxyflavone; this batch keeps it,
  because the frozen release-hold resolutions in ``semantic_release.py`` bind
  to SSSOM row positions and any removal above them breaks the resolution
  build (``drop_registry_row`` stays False until that is position-map aware).
* **Class to member** (step 4's evidence hatch): the record sat on a ChEBI
  class ("any 4-hydroxynonenal", "aluminium sulfate", "bisabolene") while its
  own CAS names one member; the member becomes the identity, graded
  ``CAS_RN_LOOKUP``.
* **Wrong form** (step 1): the term was the hydrochloride, the anhydrous
  compound, the acid, or a broader MeSH concept; the record's CAS, formula or
  label names the free base, the monohydrate, the anion, the atropisomer.
* **Localize** (step 2): no exact term exists for the substance (bergenin
  monohydrate; catalase as a reagent), so the identity is its ``cas:`` with a
  ``broadMatch`` parent and a Rule B1 registry row, the Lysozyme / BSA shape.

Grades follow Section 0 literally: ``EXACT_MATCH`` when the label is the
term's primary label, ``SYNONYM_MATCH`` when it is a unique ontology synonym,
``CAS_RN_LOOKUP`` when the record's CAS resolves to the term (ChEBI xref, or
PubChem InChIKey equal to the term's), ``CLOSE_MATCH`` when a descriptor was
supplied, ``MANUAL_CURATION`` when identity rests on structure agreement alone.

Dry-run by default; ``--apply`` writes the records and an apply log.
``--prepare-sssom`` (before ``reconcile_sssom --apply``) renames the one
subject_label this batch corrects, so reconcile does not orphan its rows.
``--finish-sssom`` (after reconcile) syncs own-identifier rows to
``exactMatch`` plus the grade columns, rewrites a wrong-CAS registry row,
drops the registry rows that step 1 makes redundant, adds the cas/registry
rows the two localized records need, and scrubs REJECTED_LABEL tokens.
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
from mediaingredientmech.sssom_grading import confidence_for, justification_for  # noqa: E402
from mediaingredientmech.utils.oaklib_cache import require_db  # noqa: E402
from mediaingredientmech.validation.write_validated import write_validated_ingredient  # noqa: E402

MAPPED = ROOT / "data" / "ingredients" / "mapped"
SSSOM = ROOT / "mappings" / "ingredient_mappings.sssom.tsv"
ISSUE = "#312"
CURATOR = "claude"
LLM_MODEL = "claude-fable-5-1"
MAPPING_DATE = "2026-09-22"
EVIDENCE_SOURCE = "MIM curation (#312); chebi.db"
PUBCHEM_DATE = "2026-09-22"

# PubChem PUG-REST, fetched 2026-09-22: CAS -> CID -> InChIKey / formula.
PUBCHEM = {
    "75899-68-2": ("5283344", "JVJFIQYAHPMBBX-FNORWQNLSA-N", "C9H16O2"),
    "494-38-2": ("62344", "DPKHZNPWBDQZCN-UHFFFAOYSA-N", "C17H19N3"),
    "65710-07-8": ("3081544", "WGLYHYWDYPSNPF-RQFIXDHTSA-N", "C21H43N5O15S"),
    "55449-49-5": ("118856046", "KMYQCELRVANQNG-YXGOVGSCSA-N", "C17H24BrNO4"),
    "17659-49-3": ("2198", None, "C17H23NO4"),
    "108032-11-7": ("201412", "QCWSXSAFDSGKAT-YOKSUNLASA-N", "C14H18O10"),
}
PUBCHEM_CID_ATROP = ("23232701", "FNEADFUPWHAVTA-PLNGDYQASA-N")


@dataclass(frozen=True)
class Identity:
    slug: str
    old_identifier: str
    new_identifier: str
    ontology_id: str
    ontology_label: str
    ontology_source: str
    old_quality: str
    new_quality: str
    action: str
    rationale: str
    old_ontology_id: str | None = None  # when the parent also moves
    chem_from_chebi: bool = False  # refresh formula/inchi/smiles from the new term
    chem: dict = field(default_factory=dict)  # explicit chemical_properties overrides
    drop_chem: tuple[str, ...] = ()
    reject_synonyms: tuple[tuple[str, str], ...] = ()
    add_synonyms: tuple[tuple[str, str, str], ...] = ()  # (text, type, source)
    new_preferred_term: str | None = None
    raw_label_source: str | None = None
    supersede_sources: tuple[str, ...] = ()
    # run-time checks
    inchikey_equals_pubchem_cas: str | None = None  # record CAS whose PubChem InChIKey must equal the term's
    inchikey_equals: str | None = None
    unique_synonym: str | None = None
    chebi_cas_xref: str | None = None
    drop_registry_row: bool = False
    add_registry_rows: str | None = None  # registry prefix for the two localized records
    new_cas_row: str | None = None  # rewrite the cas: row to this CAS


IDENTITIES: tuple[Identity, ...] = (
    Identity(
        "34-Dihydroxyflavone", "cas:14919-49-4", "mesh:C559991", "mesh:C559991",
        "3,4'-dihydroxyflavone", "MESH", "NARROW_MATCH", "EXACT_MATCH", "REGRADED_PARENT_TO_IDENTITY",
        "mesh.db gives MESH:C559991 the label \"3,4'-dihydroxyflavone\", identical to the record's "
        "label and distinct from MESH:C028288 \"3',4'-dihydroxyflavone\". chebi.db has no term for "
        "this compound (CAS 14919-49-4 and the name resolve to nothing). A broadMatch from a record "
        "to the same compound is false; Section 3 step 1 makes the MeSH term the identifier "
        "(68 records already carry mesh: primaries) with EXACT_MATCH. The CAS stays in "
        "chemical_properties and on its registry row; the kgmicrobe.compound row is dropped as "
        "#326 did for 72-Dihydroxyflavone.",
        drop_registry_row=False,
    ),
    Identity(
        "4-Hydroxynonenal", "CHEBI:142593", "CHEBI:58968", "CHEBI:58968",
        "(E)-4-hydroxynon-2-enal", "CHEBI", "EXACT_MATCH", "CAS_RN_LOOKUP", "REGROUNDED_IDENTITY",
        "CHEBI:142593 '4-hydroxynonenal' is a class (definition: double bond 'at any position'; "
        "wildcard SMILES '*C([H])=O', which had been copied into the record; no InChIKey, no CAS). "
        "The record has carried CAS 75899-68-2 since creation; PubChem resolves it to CID 5283344 "
        "with InChIKey JVJFIQYAHPMBBX-FNORWQNLSA-N, which is CHEBI:58968 '(E)-4-hydroxynon-2-enal' "
        "(synonyms '4-hydroxynonenal', 'HNE'). Section 3 step 4's evidence hatch: the CAS picks "
        "the member. Structure fields refreshed from the term.",
        chem_from_chebi=True, chem={"pubchem_cid": 5283344},
        inchikey_equals_pubchem_cas="75899-68-2",
    ),
    Identity(
        "Acridine_Orange", "CHEBI:51739", "CHEBI:87346", "CHEBI:87346",
        "acridine orange free base", "CHEBI", "EXACT_MATCH", "CAS_RN_LOOKUP", "REGROUNDED_IDENTITY",
        "CHEBI:51739 'acridine orange' is the hydrochloride (formula H.C17H19N3.Cl, is_a "
        "hydrochloride); its formula, InChI, SMILES and the 'tetramethylacridine-3,6-diamine "
        "hydrochloride' synonym were copied onto the record from the term. The record's only "
        "source-supplied identity evidence is CAS 494-38-2, which PubChem resolves to CID 62344, "
        "C17H19N3, InChIKey DPKHZNPWBDQZCN-UHFFFAOYSA-N: CHEBI:87346 'acridine orange free base' "
        "(synonyms 'Acridine Orange', 'Acridine Orange Base'). ChEBI xrefs 494-38-2 on both terms, "
        "so the PubChem InChIKey decides. The CAS governs the form (#320). Structure fields "
        "refreshed from the term; the hydrochloride alias is REJECTED_LABEL.",
        chem_from_chebi=True, chem={"pubchem_cid": 62344},
        reject_synonyms=(("N,N,N',N'-tetramethylacridine-3,6-diamine hydrochloride", "names the hydrochloride CHEBI:51739, not the free base"),),
        inchikey_equals_pubchem_cas="494-38-2",
    ),
    Identity(
        "Ammonium_Molybdate_Tetrahydrate", "cas:12054-85-2", "CHEBI:86244", "CHEBI:86244",
        "hexaammonium heptamolybdate tetrahydrate", "CHEBI", "CLOSE_MATCH", "SYNONYM_MATCH", "REGROUNDED_IDENTITY",
        "The record (H32Mo7N6O28, CAS 12054-85-2) is the heptamolybdate; CHEBI:91249 'ammonium "
        "molybdate' is the diammonium orthomolybdate (2H4N.MoO4, one Mo), a different polyanion, "
        "not the anhydrous parent of this hydrate. ChEBI has the substance: CHEBI:86244 "
        "'hexaammonium heptamolybdate tetrahydrate' (4H2O.6H4N.Mo7O24) carries the related synonym "
        "'ammonium molybdate tetrahydrate', the record's exact label, on no other term. Section 3 "
        "step 1 with a unique synonym: SYNONYM_MATCH. The CAS stays on its registry row.",
        old_ontology_id="CHEBI:91249",
        add_synonyms=(("ammonium heptamolybdate tetrahydrate", "RELATED_SYNONYM", "CHEBI:86244"),
                      ("ammonium paramolybdate tetrahydrate", "RELATED_SYNONYM", "CHEBI:86244")),
        unique_synonym="ammonium molybdate tetrahydrate",
    ),
    Identity(
        "Anisodamine_Hydrobromide", "cas:17659-49-3", "NCIT:C221850", "NCIT:C221850",
        "Anisodamine Hydrobromide", "NCIT", "NARROW_MATCH", "EXACT_MATCH", "REGRADED_PARENT_TO_IDENTITY",
        "The label is the hydrobromide; the identifier cas:17659-49-3 is the free base (PubChem "
        "CID 2198, C17H23NO4, no bromine), so the published exactMatch asserted identity between "
        "a salt and its free base. NCIT:C221850 has the label 'Anisodamine Hydrobromide' exactly, "
        "once the empty '()' ingest artefact is stripped from the record's label (kept as RAW_TEXT). "
        "Section 3 step 1: the NCIT term is the identifier, EXACT_MATCH. The salt's CAS is "
        "55449-49-5 (PubChem CID 118856046, C17H24BrNO4); the free-base InChI/SMILES are dropped "
        "and 17659-49-3 is recorded in the note as the upstream free-base CAS, not as identity.",
        chem={"cas_rn": "55449-49-5", "molecular_formula": "C17H24BrNO4", "pubchem_cid": 118856046,
              "data_source": "PubChem CID 118856046 (anisodamine hydrobromide) via CAS 55449-49-5; upstream CultureBotHT row carried the free-base CAS 17659-49-3"},
        drop_chem=("inchi", "smiles"),
        new_preferred_term="Anisodamine Hydrobromide", raw_label_source="CultureBotHT",
        supersede_sources=("NCIT via OLS (stem-substring)",),
        drop_registry_row=False, new_cas_row="55449-49-5",
    ),
    Identity(
        "Aluminium_Sulfate", "CHEBI:74772", "CHEBI:74768", "CHEBI:74768",
        "aluminium sulfate (anhydrous)", "CHEBI", "EXACT_MATCH", "CAS_RN_LOOKUP", "REGROUNDED_IDENTITY",
        "CHEBI:74772 'aluminium sulfate' is a class ('any inorganic sulfate salt ...'; no formula, "
        "InChIKey or CAS) with three members: anhydrous, hexadecahydrate, octadecahydrate. The "
        "record's CAS 10043-01-3 came from the CultureBotHT source row with FW 342.15, the "
        "anhydrous mass, and ChEBI xrefs that CAS on exactly one term, CHEBI:74768 'aluminium "
        "sulfate (anhydrous)'. Section 3 step 4's evidence hatch: the CAS picks the member; the "
        "mapping was lexical, so the CAS is independent evidence.",
        chem_from_chebi=True, chebi_cas_xref="cas:10043-01-3",
    ),
    Identity(
        "Apramycin_Sulfate_Salt", "cas:65710-07-8", "CHEBI:190734", "CHEBI:190734",
        "Apramycin sulfate", "CHEBI", "NARROW_MATCH", "CAS_RN_LOOKUP", "REGRADED_PARENT_TO_IDENTITY",
        "The 'no CHEBI entry exists' note was wrong: CHEBI:190734 'Apramycin sulfate' "
        "(C21H41N5O11.H2O4S = the record's C21H43N5O15S) has InChIKey WGLYHYWDYPSNPF-RQFIXDHTSA-N, "
        "and the record's CAS 65710-07-8 resolves on PubChem (CID 3081544) to the same InChIKey. "
        "The broadMatch parent is the substance itself; Section 3 step 1 promotes it to the "
        "identifier (#326 precedent), graded CAS_RN_LOOKUP because the CAS, not the label, "
        "established it. The CAS stays on its registry row; the kgmicrobe.compound row is dropped.",
        inchikey_equals_pubchem_cas="65710-07-8", drop_registry_row=False,
    ),
    Identity(
        "Atrop_Abyssomicin_C", "mesh:C509797", "CHEBI:208735", "CHEBI:208735",
        "Atrop-Abybetaomicin C", "CHEBI", "EXACT_MATCH", "MANUAL_CURATION", "REGROUNDED_IDENTITY",
        "MeSH SCR C509797 is 'abyssomicin C'; NLM lists 'atrop-abyssomicin C' as a separate, "
        "narrower concept (M0511053) that OLS flattened into a synonym, so the record sat on the "
        "broader compound. ChEBI has the atropisomer as CHEBI:208735 'Atrop-Abybetaomicin C' (the "
        "label's 'ss' was corrupted to 'beta' upstream), C19H22O6, InChIKey "
        "FNEADFUPWHAVTA-PLNGDYQASA-N, which equals PubChem CID 23232701 'atrop-abyssomicin C'. No "
        "name matches lexically because of the corruption and the record has no CAS, so the "
        "grade is MANUAL_CURATION: identity rests on the InChIKey/IUPAC agreement.",
        chem_from_chebi=True, chem={"pubchem_cid": 23232701},
        inchikey_equals=PUBCHEM_CID_ATROP[1],
    ),
    Identity(
        "Bisabolene", "CHEBI:49235", "CHEBI:49240", "CHEBI:49240",
        "alpha-bisabolene", "CHEBI", "EXACT_MATCH", "CAS_RN_LOOKUP", "REGROUNDED_IDENTITY",
        "CHEBI:49235 'bisabolene' is a class (formula only, no InChIKey, no CAS; members alpha, "
        "beta, gamma). The record was created from CultureBotHT with CAS 17627-44-0, which ChEBI "
        "xrefs on exactly one term, CHEBI:49240 'alpha-bisabolene'. Section 3 step 4's evidence "
        "hatch: the CAS picks the member. Structure fields filled from the term.",
        chem_from_chebi=True, chebi_cas_xref="cas:17627-44-0",
    ),
    Identity(
        "Bergenin", "CHEBI:69499", "cas:108032-11-7", "CHEBI:69499",
        "Bergenin", "CHEBI", "EXACT_MATCH", "NARROW_MATCH", "REGROUNDED_IDENTITY",
        "The record's only source-supplied identity is CAS 108032-11-7, which PubChem resolves to "
        "CID 201412, C14H18O10: bergenin monohydrate (C14H16O9.H2O, MW 346.29). CHEBI:69499 "
        "'Bergenin' is the anhydrous compound (C14H16O9, cas 477-90-7), whose InChI/SMILES had "
        "been copied onto the record. ChEBI has no hydrate term, so Section 3 step 2 applies: "
        "identifier cas:108032-11-7, broadMatch to CHEBI:69499 as the nearest parent, Rule B1 "
        "registry row. The CAS governs the form (#320). Formula corrected to the monohydrate; the "
        "anhydrous InChI/SMILES are dropped.",
        chem={"molecular_formula": "C14H18O10", "pubchem_cid": 201412,
              "data_source": "CultureBotHT compounds_to_cas.csv (CAS); PubChem CID 201412 (monohydrate formula)"},
        drop_chem=("inchi", "smiles"),
        add_synonyms=(("Bergenin monohydrate", "EXACT_SYNONYM", "PubChem CID 201412"),),
        add_registry_rows="kgmicrobe.compound",
    ),
    Identity(
        "Catalase", "NCIT:C61062", "cas:9001-05-2", "mesh:D002374",
        "Catalase", "MESH", "EXACT_MATCH", "NARROW_MATCH", "REGROUNDED_IDENTITY",
        "ncit.db defines NCIT:C61062 'Catalase' as 'Catalase (527 aa, ~60 kDa) is encoded by the "
        "human CAT gene' (Swiss-Prot P04040, R54 -> NCIT:C61060 CAT Gene): the human gene product, "
        "not the media reagent (Sigma C-10, bovine liver). skos:exactMatch would substitute that "
        "node for the reagent. Follow the protein-reagent siblings Bovine_Serum_Albumin and "
        "Lysozyme: identifier is the enzyme's CAS 9001-05-2 (EC 1.11.1.6), broadMatch to the "
        "species-neutral MeSH descriptor mesh:D002374 'Catalase', Rule B1 registry row.",
        chem={"cas_rn": "9001-05-2", "data_source": "CAS registry number of catalase, EC 1.11.1.6 (enzyme, no single structure)"},
        supersede_sources=("CultureMech",),
        add_registry_rows="kgmicrobe.ingredient",
    ),
    Identity(
        "Ferulate", "CHEBI:17620", "CHEBI:29749", "CHEBI:29749",
        "trans-ferulate", "CHEBI", "CLOSE_MATCH", "CLOSE_MATCH", "REGROUNDED_IDENTITY",
        "The record's note 'CHEBI has no ferulate anion term' was false: CHEBI:29749 "
        "'trans-ferulate' (C10H9O4, charge -1, synonym '(E)-ferulate') is the conjugate base of "
        "CHEBI:17620 'trans-ferulic acid' (C10H10O4, charge 0), which the record was grounded to. "
        "A bare -ate label denotes the anion (Section 3, protonation state). The grade stays "
        "CLOSE_MATCH: the trans descriptor was supplied, not stated by the label, and ChEBI has "
        "no geometry-unspecified ferulate anion.",
    ),
)


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


class Terms:
    def __init__(self) -> None:
        self.dbs = {p: sqlite3.connect(require_db(p)) for p in ("CHEBI", "MESH", "NCIT")}

    def _con(self, curie: str):
        return self.dbs[curie.split(":", 1)[0].upper()]

    @staticmethod
    def _key(curie: str) -> str:
        prefix, local = curie.split(":", 1)
        return f"{prefix.upper()}:{local}"

    def value(self, curie: str, predicate: str) -> str | None:
        row = self._con(curie).execute(
            "select value from statements where subject=? and predicate=?", (self._key(curie), predicate)
        ).fetchone()
        return row[0] if row else None

    def label(self, curie: str) -> str | None:
        return self.value(curie, "rdfs:label")

    def names(self, curie: str) -> set[str]:
        return {
            r[0]
            for r in self.dbs["CHEBI"].execute(
                "select value from statements where subject=? and predicate in "
                "('rdfs:label','oio:hasExactSynonym','oio:hasRelatedSynonym')",
                (curie,),
            )
        }

    def terms_named(self, text: str) -> set[str]:
        return {
            r[0]
            for r in self.dbs["CHEBI"].execute(
                "select distinct subject from statements where predicate in "
                "('rdfs:label','oio:hasExactSynonym','oio:hasRelatedSynonym') and lower(value)=?",
                (text.casefold(),),
            )
        }

    def has_cas(self, curie: str, cas: str) -> bool:
        return (
            self.dbs["CHEBI"].execute(
                "select 1 from statements where subject=? and predicate='oio:hasDbXref' and value=?",
                (curie, cas),
            ).fetchone()
            is not None
        )

    def chemistry(self, curie: str) -> dict:
        out = {}
        for slot, predicate in (
            ("molecular_formula", "chemrof:generalized_empirical_formula"),
            ("inchi", "chemrof:inchi_string"),
            ("smiles", "chemrof:smiles_string"),
        ):
            value = self.value(curie, predicate)
            if value:
                out[slot] = value
        return out


def verify(terms: Terms) -> None:
    problems: list[str] = []
    for spec in IDENTITIES:
        if terms.label(spec.ontology_id) != spec.ontology_label:
            problems.append(f"{spec.slug}: {spec.ontology_id} label is not {spec.ontology_label!r} (got {terms.label(spec.ontology_id)!r})")
        if spec.inchikey_equals_pubchem_cas:
            cid, key, _ = PUBCHEM[spec.inchikey_equals_pubchem_cas]
            if terms.value(spec.ontology_id, "chemrof:inchi_key_string") != key:
                problems.append(f"{spec.slug}: {spec.ontology_id} InChIKey differs from PubChem CID {cid}")
        if spec.inchikey_equals and terms.value(spec.ontology_id, "chemrof:inchi_key_string") != spec.inchikey_equals:
            problems.append(f"{spec.slug}: {spec.ontology_id} InChIKey changed")
        if spec.unique_synonym and terms.terms_named(spec.unique_synonym) != {spec.ontology_id}:
            problems.append(f"{spec.slug}: {spec.unique_synonym!r} is not unique to {spec.ontology_id}")
        if spec.chebi_cas_xref and not terms.has_cas(spec.ontology_id, spec.chebi_cas_xref):
            problems.append(f"{spec.slug}: {spec.ontology_id} lacks xref {spec.chebi_cas_xref}")
    if problems:
        raise SystemExit("Ontology facts no longer hold:\n  " + "\n  ".join(problems))


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


def apply_identity(spec: Identity, terms: Terms, log: list, write: bool) -> None:
    path, record = load(spec.slug)
    mapping = record["ontology_mapping"]
    if record["identifier"] == spec.new_identifier:
        print(f"SKIP     {spec.slug}: already {spec.new_identifier}")
        return
    assert record["identifier"] == spec.old_identifier, (spec.slug, record["identifier"])
    assert mapping["ontology_id"] == (spec.old_ontology_id or spec.old_identifier if spec.old_identifier.split(":")[0] in {"CHEBI", "mesh", "NCIT"} else mapping["ontology_id"]), (spec.slug, mapping["ontology_id"])
    assert mapping["mapping_quality"] == spec.old_quality, (spec.slug, mapping["mapping_quality"])
    before = sha(path)
    old_ontology = (mapping["ontology_id"], mapping.get("ontology_label"))
    record["identifier"] = spec.new_identifier
    mapping["ontology_id"] = spec.ontology_id
    mapping["ontology_label"] = spec.ontology_label
    mapping["ontology_source"] = spec.ontology_source
    mapping["mapping_quality"] = spec.new_quality
    superseded = supersede(mapping, spec.supersede_sources)
    chem = record.setdefault("chemical_properties", {}) or {}
    record["chemical_properties"] = chem
    if spec.chem_from_chebi:
        chem.update(terms.chemistry(spec.ontology_id))
        chem["data_source"] = f"{chem.get('data_source', '').strip()}; structure from chebi.db {spec.ontology_id} ({ISSUE})".strip("; ")
    for key in spec.drop_chem:
        chem.pop(key, None)
    chem.update(spec.chem)
    rejected = []
    for text, why in spec.reject_synonyms:
        for synonym in record.get("synonyms") or []:
            if synonym.get("synonym_text") == text and synonym.get("synonym_type") != "REJECTED_LABEL":
                synonym["synonym_type"] = "REJECTED_LABEL"
                rejected.append(f"{text} ({why})")
    existing = {s.get("synonym_text") for s in record.get("synonyms") or []}
    added = []
    for text, kind, source in spec.add_synonyms:
        if text not in existing:
            record.setdefault("synonyms", []).append({"synonym_text": text, "synonym_type": kind, "source": source})
            added.append(text)
    relabelled = None
    if spec.new_preferred_term and record["preferred_term"] != spec.new_preferred_term:
        relabelled = (record["preferred_term"], spec.new_preferred_term)
        if record["preferred_term"] not in existing:
            record.setdefault("synonyms", []).append(
                {"synonym_text": record["preferred_term"], "synonym_type": "RAW_TEXT", "source": spec.raw_label_source}
            )
        record["preferred_term"] = spec.new_preferred_term
    note = (
        f"identifier {spec.old_identifier} -> {spec.new_identifier}; ontology {old_ontology[0]} ('{old_ontology[1]}') "
        f"-> {spec.ontology_id} ('{spec.ontology_label}'); mapping_quality {spec.old_quality} -> {spec.new_quality}. "
        + spec.rationale
    )
    mapping.setdefault("evidence", []).append(evidence(note))
    changes = note + f" ({ISSUE})"
    if rejected:
        changes += " REJECTED_LABEL: " + "; ".join(rejected) + "."
    if added:
        changes += " Synonyms added: " + ", ".join(added) + "."
    if relabelled:
        changes += f" preferred_term {relabelled[0]!r} -> {relabelled[1]!r}; the raw string is kept as RAW_TEXT."
    record_curation_event(
        record, curator=CURATOR, action=spec.action, changes=changes,
        previous_status="MAPPED", new_status="MAPPED", llm_assisted=True, llm_model=LLM_MODEL,
    )
    print(f"IDENTITY {spec.slug}: {spec.old_identifier} -> {spec.new_identifier} [{spec.new_quality}] "
          f"(superseded {superseded}, rejected {len(rejected)}, added {added}, relabelled {bool(relabelled)})")
    if write:
        write_validated_ingredient(record, path)
    log.append({
        "source_record": str(path.relative_to(ROOT)), "shape": "identity",
        "before_yaml_sha256": before, "after_yaml_sha256": sha(path) if write else None,
        "change": f"identifier {spec.old_identifier} -> {spec.new_identifier}; ontology_id {old_ontology[0]} -> {spec.ontology_id}; mapping_quality {spec.old_quality} -> {spec.new_quality}"
                  + (f"; preferred_term {relabelled[0]!r} -> {relabelled[1]!r}" if relabelled else ""),
        "verification": spec.rationale,
    })


def repoint_components(log: list, write: bool) -> None:
    """Re-point MIM_CATALOG component references from an old identifier to the new one.

    A mixture's ``components[].component_id`` names the part by the MIM record's
    identifier, and qc-component-partonomy (and the KGX exporter) require that
    identifier to belong to an active record. The part itself is unchanged.
    """
    old_to_new = {spec.old_identifier: (spec.new_identifier, spec.slug) for spec in IDENTITIES}
    for path in sorted((ROOT / "data" / "ingredients").glob("*/*.yaml")):
        record = yaml.safe_load(path.read_text()) or {}
        hits = [
            (index, component)
            for index, component in enumerate(record.get("components") or [])
            if component.get("component_id") in old_to_new and component.get("reference_scope") == "MIM_CATALOG"
        ]
        if not hits:
            continue
        before = sha(path)
        notes = []
        for index, component in hits:
            old = component["component_id"]
            new, slug = old_to_new[old]
            component["component_id"] = new
            notes.append(f"components[{index}] '{component.get('component_name')}' component_id {old} -> {new}")
        changes = (
            "; ".join(notes)
            + f": the referenced MIM record was re-grounded ({ISSUE}); the part identity and amount are unchanged."
        )
        record_curation_event(
            record, curator=CURATOR, action="RESCOPED_COMPONENT", changes=changes,
            llm_assisted=True, llm_model=LLM_MODEL,
        )
        print(f"COMPONENT {path.stem}: {'; '.join(notes)}")
        if write:
            write_validated_ingredient(record, path)
        log.append({
            "source_record": str(path.relative_to(ROOT)), "shape": "component_repoint",
            "before_yaml_sha256": before, "after_yaml_sha256": sha(path) if write else None,
            "change": "; ".join(notes),
            "verification": "The component names the same substance; only the MIM identifier it resolves through changed in this batch.",
        })


# --- SSSOM ------------------------------------------------------------------


def _read_rows() -> tuple[list[str], list[str], list[dict]]:
    lines = SSSOM.read_text(encoding="utf-8").splitlines(keepends=True)
    comments = [line for line in lines if line.startswith("#")]
    body = [line for line in lines if not line.startswith("#")]
    reader = csv.DictReader(io.StringIO("".join(body)), delimiter="\t")
    return comments, list(reader.fieldnames or []), list(reader)


def _write_rows(comments: list[str], fields: list[str], rows: list[dict]) -> None:
    out = io.StringIO()
    out.writelines(comments)
    writer = csv.DictWriter(out, fieldnames=fields, delimiter="\t", lineterminator="\n")
    writer.writeheader()
    writer.writerows(rows)
    SSSOM.write_text(out.getvalue(), encoding="utf-8")


def prepare_sssom() -> None:
    """Rename the subject_label of relabelled subjects so reconcile keeps their rows."""
    comments, fields, rows = _read_rows()
    renamed = 0
    for spec in IDENTITIES:
        if not spec.new_preferred_term:
            continue
        for row in rows:
            if row["subject_id"] == f"MIM:{spec.slug}" and row["subject_label"] != spec.new_preferred_term:
                row["subject_label"] = spec.new_preferred_term
                renamed += 1
    _write_rows(comments, fields, rows)
    print(f"renamed subject_label on {renamed} row(s)")


def _stamp(row: dict, note: str, method: str) -> None:
    row["mapping_date"] = MAPPING_DATE
    row["comment"] = (row["comment"] + " " + note).strip()
    row["validation_method"] = f"manual:apply_312_batch2|{method}|{MAPPING_DATE}"


def finish_sssom() -> None:
    comments, fields, rows = _read_rows()
    by_slug = {spec.slug: spec for spec in IDENTITIES}
    records = {slug: load(slug)[1] for slug in by_slug}
    terms = Terms()
    # Names of the term each own-identifier row left, minus the names of the term it
    # now carries: the enrichment builder filled ``other`` for the old term (#747).
    old_only: dict[str, set[str]] = {}
    for spec in IDENTITIES:
        old_term = spec.old_ontology_id or (spec.old_identifier if spec.old_identifier.startswith("CHEBI:") else None)
        if old_term and old_term != spec.ontology_id and spec.ontology_id.startswith("CHEBI:"):
            old_only[spec.slug] = terms.names(old_term) - terms.names(spec.ontology_id)
    synced = dropped = rewritten = added = scrubbed = relabelled = cas_fixed = 0
    kept: list[dict] = []
    for row in rows:
        slug = row["subject_id"][4:] if row["subject_id"].startswith("MIM:") else None
        spec = by_slug.get(slug)
        if not spec:
            kept.append(row)
            continue
        record = records[slug]
        obj = row["object_id"]
        if spec.drop_registry_row and obj.startswith(("kgmicrobe.compound:", "kgmicrobe.ingredient:")):
            dropped += 1
            continue
        if obj == record["identifier"]:
            quality = record["ontology_mapping"]["mapping_quality"]
            want = ("skos:exactMatch", justification_for(quality), confidence_for(quality))
            have = (row["predicate_id"], row["mapping_justification"], row["confidence"])
            if have != want:
                row["predicate_id"], row["mapping_justification"], row["confidence"] = want
                _stamp(row, f"[own-identifier row: exactMatch per Rule D, grade {quality} ({ISSUE})]", "IDENTITY")
                synced += 1
        if spec.new_cas_row and obj.startswith(("kgmicrobe.compound:", "kgmicrobe.ingredient:")):
            tokens = [t for t in row["other"].split("|") if t and not t.startswith("CAS:")]
            wanted = "|".join(tokens + [f"CAS:{spec.new_cas_row}"])
            if row["other"] != wanted:
                row["other"] = wanted
                _stamp(row, f"[registry row carried the free-base CAS; the salt's CAS is {spec.new_cas_row} ({ISSUE})]", "REGISTRY")
                rewritten += 1
        if spec.new_cas_row and obj.startswith("cas:") and obj != f"cas:{spec.new_cas_row}":
            old = obj
            row["object_id"] = f"cas:{spec.new_cas_row}"
            row["object_label"] = record["preferred_term"]
            row["other"] = "|".join(t for t in row["other"].split("|") if t and t != f"CAS:{old[4:]}") or ""
            row["other"] = "|".join(filter(None, [row["other"], f"CAS:{spec.new_cas_row}"]))
            row["comment"] = f"Registry/identity row preserving cas:{spec.new_cas_row} alongside identifier {record['identifier']}."
            _stamp(row, f"[{old} named the free base; the salt's CAS is {spec.new_cas_row} ({ISSUE})]", "REGISTRY")
            rewritten += 1
        if spec.new_preferred_term and obj.startswith(("cas:", "kgmicrobe.compound:", "kgmicrobe.ingredient:")):
            if row["object_label"] != record["preferred_term"]:
                row["object_label"] = record["preferred_term"]
                _stamp(row, f"[object_label follows the corrected preferred_term ({ISSUE})]", "REGISTRY")
                relabelled += 1
        rejected = {
            s["synonym_text"] for s in record.get("synonyms") or [] if s.get("synonym_type") == "REJECTED_LABEL"
        }
        resolving = {
            s["synonym_text"] for s in record.get("synonyms") or [] if s.get("synonym_type") != "REJECTED_LABEL"
        }
        stale = {t for t in old_only.get(slug, set()) if t not in resolving} if obj == record["identifier"] else set()
        drop_tokens = rejected | stale
        if drop_tokens and row["other"]:
            tokens = row["other"].split("|")
            keep_tokens = [t for t in tokens if t not in drop_tokens]
            if len(keep_tokens) != len(tokens):
                row["other"] = "|".join(keep_tokens)
                removed = [t for t in tokens if t in drop_tokens]
                _stamp(row, f"[other: dropped {removed}: rejected or names of the term this row left ({ISSUE})]", "OTHER")
                scrubbed += 1
        # #403: the orderable CAS reaches KGX through `other` on symmetric rows only;
        # kg-microbe drops `other` on asymmetric rows, so a CAS there is dead weight.
        cas_rn = str((record.get("chemical_properties") or {}).get("cas_rn") or "").strip()
        tokens = [t for t in row["other"].split("|") if t]
        cas_tokens = [t for t in tokens if t.upper().startswith("CAS:")]
        if row["predicate_id"] in {"skos:exactMatch", "skos:closeMatch"} and cas_rn:
            wanted = [t for t in tokens if not t.upper().startswith("CAS:")] + [f"CAS:{cas_rn}"]
            if tokens != wanted:
                row["other"] = "|".join(wanted)
                _stamp(row, f"[other: CAS token follows the record's cas_rn on a symmetric row, #403 ({ISSUE})]", "OTHER")
                cas_fixed += 1
        elif row["predicate_id"] not in {"skos:exactMatch", "skos:closeMatch"} and cas_tokens:
            row["other"] = "|".join(t for t in tokens if not t.upper().startswith("CAS:"))
            _stamp(row, f"[other: CAS token removed from an asymmetric row, #403 ({ISSUE})]", "OTHER")
            cas_fixed += 1
        kept.append(row)
    rows = kept
    existing = {(r["subject_id"], r["object_id"]) for r in rows}
    for spec in IDENTITIES:
        if not spec.add_registry_rows:
            continue
        record = records[spec.slug]
        subject = f"MIM:{spec.slug}"
        parent_row = next(r for r in rows if r["subject_id"] == subject and r["object_id"] == spec.ontology_id)
        cas = record["identifier"]
        registry = f"{spec.add_registry_rows}:{spec.slug.lower()}"
        source = parent_row["source"] + "|MIM:curator=claude"
        for object_id, object_source, comment in (
            (cas, "registry:cas", f"Registry/identity row preserving {cas} alongside parent {spec.ontology_id}."),
            (registry, "kgm:" + spec.add_registry_rows.split(".")[1],
             f"Registry/identity row (Rule B1) for broadMatch subject; kg-microbe primary id {registry} alongside parent {spec.ontology_id}."),
        ):
            if (subject, object_id) in existing:
                continue
            rows.append({
                "subject_id": subject, "subject_label": record["preferred_term"], "predicate_id": "skos:exactMatch",
                "object_id": object_id, "object_label": record["preferred_term"], "object_source": object_source,
                "mapping_justification": "semapv:ManualMappingCuration", "source": source,
                "mapping_date": MAPPING_DATE, "confidence": "0.99", "comment": comment,
                "other": f"CAS:{cas[4:]}", "validation_method": f"manual:apply_312_batch2|REGISTRY|{MAPPING_DATE}",
            })
            added += 1
    _write_rows(comments, fields, rows)
    print(f"own-identifier rows synced {synced}; registry rows dropped {dropped}; cas rows rewritten {rewritten}; "
          f"registry labels corrected {relabelled}; rows added {added}; tokens scrubbed from {scrubbed} row(s); "
          f"CAS tokens fixed on {cas_fixed} row(s)")
    repoint_membership()


def repoint_membership() -> None:
    """mappings/culturemech_recipe_membership.tsv is keyed by MIM identifier; follow the re-groundings."""
    path = ROOT / "mappings" / "culturemech_recipe_membership.tsv"
    old_to_new = {spec.old_identifier: spec.new_identifier for spec in IDENTITIES}
    comments, header, data, changed = [], None, [], 0
    for line in path.read_text(encoding="utf-8").splitlines(keepends=True):
        if line.startswith("#"):
            comments.append(line)
            continue
        if header is None:
            header = line
            continue
        first, sep, rest = line.partition("\t")
        if first in old_to_new:
            line = old_to_new[first] + sep + rest
            changed += 1
        data.append(line)
    # The artifact is sorted by (mim_identifier, recipe_id) so rebuilds diff cleanly.
    data.sort(key=lambda line: tuple(line.rstrip("\n").split("\t")[:2]))
    path.write_text("".join(comments) + (header or "") + "".join(data), encoding="utf-8")
    print(f"membership rows re-pointed: {changed}")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--apply", action="store_true", help="write the records (default: dry-run)")
    parser.add_argument("--log", type=Path, help="apply-log JSON path (written with --apply)")
    parser.add_argument("--prepare-sssom", action="store_true", help="before reconcile: rename relabelled subjects' rows")
    parser.add_argument("--finish-sssom", action="store_true", help="after reconcile: own-identifier rows, registry rows, scrubs")
    args = parser.parse_args()
    if args.prepare_sssom:
        prepare_sssom()
        return 0
    if args.finish_sssom:
        finish_sssom()
        return 0
    terms = Terms()
    verify(terms)
    log: list = []
    for spec in IDENTITIES:
        apply_identity(spec, terms, log, args.apply)
    repoint_components(log, args.apply)
    print(f"\n{'wrote' if args.apply else 'would write'} {len(log)} record(s)")
    if args.apply and args.log:
        previous = json.loads(args.log.read_text())["records"] if args.log.is_file() else []
        merged = {entry["source_record"]: entry for entry in previous}
        for entry in log:
            merged[entry["source_record"]] = entry
        args.log.write_text(json.dumps({"issue": ISSUE, "batch": "batch2", "records": list(merged.values())}, indent=2) + "\n")
        print(f"apply log: {args.log}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
