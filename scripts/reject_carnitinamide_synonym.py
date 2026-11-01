#!/usr/bin/env python3
"""Retain the superseded carnitinamide alias as rejected provenance (#1003).

Dry-run by default. Owns one synonym and its history only; aggregate, SSSOM,
exports and content-bound review receipts require their native producers.
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

from mediaingredientmech.curate.apply_receipt import reserve_receipt_outputs  # noqa: E402
from mediaingredientmech.curate.curation_event import record_curation_event  # noqa: E402
from mediaingredientmech.validation.write_validated import (  # noqa: E402
    validate_ingredient,
    write_validated_ingredient,
)

RECORD = "data/ingredients/mapped/Carnitine_Hydrochloride.yaml"
BEFORE_SHA256 = "c123a3f76cf2277ca68a08c99e58f96845842fd90c75bdd19b90ab8db7bb6780"
ALIAS = "4-amino-2-hydroxy-N,N,N-trimethyl-4-oxobutan-1-aminium chloride"
ACTION = "REJECTED_WRONG_SUBSTANCE_SYNONYM"
VERIFICATION = (
    "Official ChEBI:48601 assigns this exact IUPAC name to carnitinamide chloride "
    "(C7H17N2O2.Cl), whereas CHEBI:17126 carnitine is C7H15NO3. The amide name "
    "survived this record's 2026-07-05 correction of the erroneous CHEBI:48601 "
    "mapping. Sources inspected 2026-11-01: "
    "https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:48601 ; "
    "https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:17126 ."
)
CHANGE = (
    f"Retyped '{ALIAS}' from EXACT_SYNONYM to REJECTED_LABEL, preserving its "
    "original chebi_synonym_review source (#1003; #669). " + VERIFICATION + " "
    "Preserved the current identifier, parent mapping, status and occurrences; "
    "unresolved salt/CAS/stereochemistry questions are not adjudicated, and "
    "no scientific or release approval is asserted."
)


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def corrected_record(record: dict, *, timestamp: str | None = None) -> dict | None:
    """Return the bounded proposal, refusing changed identity or partial edits."""
    expected = {
        "identifier": "kgmicrobe.compound:carnitine_hydrochloride",
        "preferred_term": "Carnitine Hydrochloride",
        "mapping_status": "MAPPED",
    }
    mapping = record.get("ontology_mapping") or {}
    if any(record.get(key) != value for key, value in expected.items()):
        raise ValueError("The reviewed carnitine hydrochloride identity changed")
    if any(mapping.get(key) != value for key, value in {
        "ontology_id": "CHEBI:17126", "ontology_label": "carnitine",
        "ontology_source": "CHEBI", "mapping_quality": "NARROW_MATCH",
    }.items()):
        raise ValueError("The reviewed carnitine parent mapping changed")
    hits = [s for s in record.get("synonyms", []) if s.get("synonym_text") == ALIAS]
    if len(hits) != 1 or hits[0].get("source") != "chebi_synonym_review":
        raise ValueError("Expected exactly the reviewed sourced amide alias")
    history = [e for e in record.get("curation_history", [])
               if e.get("action") == ACTION and e.get("changes") == CHANGE]
    if hits[0].get("synonym_type") == "REJECTED_LABEL" and len(history) == 1:
        return None
    if hits[0].get("synonym_type") != "EXACT_SYNONYM" or history:
        raise ValueError("Unexpected synonym type or partial prior correction")
    proposal = copy.deepcopy(record)
    next(s for s in proposal["synonyms"] if s["synonym_text"] == ALIAS)["synonym_type"] = "REJECTED_LABEL"
    record_curation_event(
        proposal, curator="reject_carnitinamide_synonym.py", action=ACTION, changes=CHANGE,
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
    proposal = corrected_record(yaml.safe_load(before_bytes))
    if proposal is None:
        print("No change: the exact sourced rejection is already present")
        return 0
    if digest(before_bytes) != BEFORE_SHA256:
        raise ValueError("Source bytes changed; re-review before applying")
    entry = {
        "source_record": RECORD, "shape": "synonym_retirement",
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
