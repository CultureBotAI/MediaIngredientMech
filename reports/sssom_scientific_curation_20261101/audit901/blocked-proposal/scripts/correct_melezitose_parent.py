#!/usr/bin/env python3
"""Apply the evidence-settled melezitose monohydrate parent correction (#901).

Dry-run by default. This owns one record only; synchronization and the native
approval-free mapping-change receipt are separate required publication steps.
"""

from __future__ import annotations

import argparse
import copy
import hashlib
import json
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "src"))

from mediaingredientmech.curate.curation_event import record_curation_event  # noqa: E402
from mediaingredientmech.curate.apply_receipt import reserve_receipt_outputs  # noqa: E402
from mediaingredientmech.validation.write_validated import (  # noqa: E402
    validate_ingredient,
    write_validated_ingredient,
)

RECORD = "data/ingredients/mapped/D-_-melezitose_Monohydrate.yaml"
BEFORE_SHA256 = "e17d80e75cf8794f5f4e2cab65a4cff77c92f921add55e36185549f75aff3222"
ACTION = "CORRECTED_HYDRATE_PARENT_PREDICATE"
CURATOR = "correct_melezitose_parent.py"
EVIDENCE_SOURCE = "MIM curation (#901); PubChem CID 16217716; ChEBI:6731"
VERIFICATION = (
    "PubChem CID 16217716 formula C18H34O17, CAS synonym 10030-67-8 and "
    "stereochemical InChI agree with this monohydrate. PubChem parent CID 92817 "
    "agrees with anhydrous CHEBI:6731 (C18H32O16). Bounded live OLS and pinned "
    "local ChEBI searches found no exact monohydrate term. CHEBI:183824 is "
    "anhydrous with different stereochemistry and is not a substitute. "
    "Current MAPPING_SEMANTICS section 3 and its form-of ruling require "
    "skos:broadMatch plus B1 identity, not subclass projection or exact parent "
    "identity. No role approval is implied. Sources: "
    "https://pubchem.ncbi.nlm.nih.gov/compound/16217716 ; "
    "https://pubchem.ncbi.nlm.nih.gov/compound/92817 ; "
    "https://www.ebi.ac.uk/chebi/CHEBI:6731 ."
)
CHANGE = (
    "Corrected CLOSE_MATCH to NARROW_MATCH for the anhydrous melezitose parent "
    "CHEBI:6731 under the current form-of ruling (#901); the SSSOM predicate is "
    "skos:broadMatch with required B1 local identity "
    "kgmicrobe.compound:d-_-melezitose_monohydrate. Retained distinct primary "
    "cas:10030-67-8, all chemistry, synonyms and provisional carbon role. "
    "Historical #342 reasoning remains provenance; no role or release approval "
    "is carried by this correction."
)


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def corrected_record(record: dict, *, timestamp: str | None = None) -> dict | None:
    """Return a validated proposal, refusing related forms and unexpected state."""
    mapping = record.get("ontology_mapping") or {}
    chemistry = record.get("chemical_properties") or {}
    expected = {
        "identifier": "cas:10030-67-8",
        "preferred_term": "D-(+)-melezitose monohydrate",
        "mapping_status": "MAPPED",
    }
    if any(record.get(key) != value for key, value in expected.items()):
        raise ValueError("The reviewed monohydrate identity no longer matches")
    if any(mapping.get(key) != value for key, value in {
        "ontology_id": "CHEBI:6731", "ontology_label": "melezitose",
        "ontology_source": "CHEBI",
    }.items()):
        raise ValueError("The reviewed anhydrous parent no longer matches")
    if any(chemistry.get(key) != value for key, value in {
        "cas_rn": "10030-67-8", "molecular_formula": "C18H34O17",
        "pubchem_cid": 16217716,
    }.items()):
        raise ValueError("The reviewed monohydrate chemistry no longer matches")
    own_evidence = [e for e in mapping.get("evidence", [])
                    if e.get("source") == EVIDENCE_SOURCE]
    own_history = [e for e in record.get("curation_history", [])
                   if e.get("action") == ACTION and e.get("changes") == CHANGE]
    if mapping.get("mapping_quality") == "NARROW_MATCH":
        if len(own_evidence) == len(own_history) == 1 and own_evidence[0].get("notes") == VERIFICATION:
            return None
        raise ValueError("An existing NARROW_MATCH is not this reviewed correction")
    if mapping.get("mapping_quality") != "CLOSE_MATCH" or own_evidence or own_history:
        raise ValueError("Unexpected mapping quality or partial prior correction")
    proposal = copy.deepcopy(record)
    proposal["ontology_mapping"]["mapping_quality"] = "NARROW_MATCH"
    proposal["ontology_mapping"].setdefault("evidence", []).append({
        "evidence_type": "DATABASE_MATCH", "source": EVIDENCE_SOURCE,
        "notes": VERIFICATION,
    })
    record_curation_event(
        proposal, curator=CURATOR, action=ACTION, changes=CHANGE,
        previous_status="MAPPED", new_status="MAPPED", llm_assisted=True,
        llm_model="gpt-6", timestamp=timestamp,
    )
    errors = validate_ingredient(proposal)
    if errors:
        raise ValueError(f"Proposed record fails native closed-schema validation: {errors}")
    return proposal


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--apply", action="store_true")
    parser.add_argument("--log", type=Path, required=True)
    args = parser.parse_args()
    path = ROOT / RECORD
    before_bytes = path.read_bytes()
    before = yaml.safe_load(before_bytes)
    proposal = corrected_record(before)
    if proposal is None:
        print("No change: the exact reviewed correction is already present")
        return 0
    if digest(before_bytes) != BEFORE_SHA256:
        raise ValueError("Source bytes differ from the reviewed input; re-review before applying")
    entry = {
        "source_record": RECORD, "shape": "hydrate_parent_predicate",
        "before_yaml_sha256": digest(before_bytes), "after_yaml_sha256": None,
        "change": CHANGE, "verification": VERIFICATION,
    }
    if args.apply:
        with reserve_receipt_outputs(args.log) as (receipt, backup):
            backup.write(before_bytes)
            backup.flush()
            write_validated_ingredient(proposal, path)
            entry["after_yaml_sha256"] = digest(path.read_bytes())
            receipt.write(json.dumps({"records": [entry]}, indent=2) + "\n")
    print(json.dumps({"applied": args.apply, "records": [entry]}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
