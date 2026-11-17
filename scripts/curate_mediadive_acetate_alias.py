#!/usr/bin/env python3
"""Add the source-confirmed trihydrate spelling, without changing identity (#1149).

Dry run by default. The evidence directory contains the archived primary responses
and their retrieval manifest. A native mapping-change receipt and fresh mapping
review are still required: this writer grants no scientific export approval.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from copy import deepcopy
from pathlib import Path

import yaml

from mediaingredientmech.curate.apply_receipt import reserve_receipt_outputs
from mediaingredientmech.curate.curation_event import record_curation_event
from mediaingredientmech.curate.publication_guard import (
    FrozenFile,
    check_reserved,
    finish_receipt,
    no_alias,
    publish_validated,
)
from mediaingredientmech.validation.write_validated import write_validated_ingredient

OWNER = "data/ingredients/mapped/Sodium_Acetate_Trihydrate.yaml"
BEFORE = "f5ffd70ecf632a6dd5d777f37411b47ba2bdb0f6f6b8fcc77b378da52d214e96"
ALIAS = "Na acetate x 3 H2O"
SOURCE = "https://mediadive.dsmz.de/download/ingredient/1315/json"
EVIDENCE = {
    "mediadive-1315.json": "93d213c95d4619c2135836a993d13ed54229f3920a241147d5f4e0eb69bf5d72",
    "chebi-32138.json": "360383e4c9a6f04c00a315b76ca0a0bbf59e93638368db930e67acec7e1dd388",
    "pubchem-cas6131-synonyms.json": "5035690cedd4523533fd1023e1bfd9d92f4a90841101d551fb96f6371d4b0072",
}
VERIFICATION = (
    "MediaDive ingredient 1315 explicitly pairs Na acetate x 3 H2O with CAS 6131-90-4; "
    "ChEBI:32138 and PubChem CID23665404 corroborate sodium acetate trihydrate. "
    "Retain MediaDive's discrepant hydrogen count in archived source evidence; do not "
    "copy it into chemistry. Add only the exact source spelling, with no change to "
    "identity, role, occurrence count, supplied form or prior history. #1149."
)


def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def prepare(data: bytes, evidence: dict[str, bytes], timestamp: str | None = None) -> dict:
    if sha(data) != BEFORE:
        raise ValueError("Owner differs from the scientifically reviewed source")
    if set(evidence) != set(EVIDENCE) or any(sha(evidence[k]) != v for k, v in EVIDENCE.items()):
        raise ValueError("Primary evidence differs from the reviewed captures")
    record = yaml.safe_load(data)
    if (
        record["identifier"],
        record["ontology_mapping"]["ontology_id"],
        record["chemical_properties"]["cas_rn"],
        record["mapping_status"],
    ) != ("CHEBI:32138", "CHEBI:32138", "6131-90-4", "MAPPED"):
        raise ValueError("Wrong substance or status")
    result = deepcopy(record)
    if any(s["synonym_text"].casefold() == ALIAS.casefold() for s in result["synonyms"]):
        raise ValueError("Alias already present; no duplicate/no-op history")
    result["synonyms"].append(
        {
            "synonym_text": ALIAS,
            "synonym_type": "HYDRATE_FORM",
            "source": SOURCE,
        }
    )
    record_curation_event(
        result,
        curator="claude",
        action="ADDED_SOURCE_ALIAS",
        changes=VERIFICATION,
        previous_status="MAPPED",
        new_status="MAPPED",
        llm_assisted=True,
        timestamp=timestamp,
    )
    return result


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path.cwd())
    parser.add_argument("--evidence", type=Path, required=True)
    parser.add_argument("--receipt-dir", type=Path, required=True)
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args()
    no_alias(args.root)
    root = args.root.absolute()
    path = root / OWNER
    no_alias(args.receipt_dir)
    owner = FrozenFile.capture(path)
    captured = {name: FrozenFile.capture(args.evidence / name) for name in EVIDENCE}
    before = owner.content
    evidence = {name: item.content for name, item in captured.items()}
    record = prepare(before, evidence)
    print(json.dumps({"owner": OWNER, "new_alias": ALIAS, "approval": "NONE", "apply": args.apply}))
    if not args.apply:
        return
    # Reserve every output before a guarded writer can alter the record.
    outputs = [args.receipt_dir / "owner-before.yaml", args.receipt_dir / "apply-log.json"]
    if any(p.resolve() == path for p in outputs):
        raise ValueError("Receipt/source collision")
    with reserve_receipt_outputs(outputs[1], backup_paths=(outputs[0],)) as (receipt, backup):

        def recheck():
            for item in captured.values():
                item.verify()
            check_reserved(receipt, outputs[1])
            check_reserved(backup, outputs[0])

        owner.verify()
        recheck()
        backup.write(before)
        backup.flush()
        after = publish_validated(
            owner, lambda staged: write_validated_ingredient(record, staged), recheck
        )
        if yaml.safe_load(after.content) != record:
            raise ValueError("Published owner differs from the validated record")
        entry = {
            "source_record": OWNER,
            "shape": "source_alias_addition",
            "before_yaml_sha256": sha(before),
            "after_yaml_sha256": sha(after.content),
            "change": f"Add HYDRATE_FORM alias {ALIAS!r}; append one history event.",
            "verification": VERIFICATION,
        }

        def final_check():
            after.verify()
            recheck()

        finish_receipt(receipt, outputs[1], {"records": [entry]}, final_check)


if __name__ == "__main__":
    main()
