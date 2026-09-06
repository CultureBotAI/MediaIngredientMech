#!/usr/bin/env python3
"""Restore the CultureMech grounding evidence the residual importer never wrote (#541).

`create_records_from_groundings.py` (#505) created 110 records from CultureMech's
unresolved residual and emitted their SSSOM rows directly, stamping
`MIM:culturemech:output/ingredient_occurrences.tsv` into the published `source`
column. It never wrote the corresponding `ontology_mapping.evidence` onto the
records.

The builder derives `source` only from `ontology_mapping.evidence[].source`
(`build_mim_ingredient_sssom.py::_join_sources`), so the tag existed solely in
the published artifact. The first honest rebuild (#540) dropped it from all 110
rows and no rebuild could ever put it back.

Each record still states its own provenance in `curation_history` -- action
`CREATED_FROM_CULTUREMECH_RESIDUAL`, curator
`claude_culturemech_residual_grounding`, and a `changes` line naming both the
ontology match and the occurrence table. This script promotes that narrative
into the structured field the builder reads. It invents nothing: a record is
touched only when its own history says where it came from.
"""

from __future__ import annotations

import argparse
import re
from datetime import datetime, timezone
from pathlib import Path

import yaml

REPO = Path(__file__).resolve().parent.parent
MAPPED = REPO / "data" / "ingredients" / "mapped"

CREATION_ACTION = "CREATED_FROM_CULTUREMECH_RESIDUAL"
CREATION_CURATOR = "claude_culturemech_residual_grounding"
EVIDENCE_SOURCE = "culturemech:output/ingredient_occurrences.tsv"
EVIDENCE_TYPE = "LEXICAL_MATCH"
CURATOR = "claude_restore_culturemech_evidence"

# The importer wrote one of two sentences. Both name what was matched, which is
# what distinguishes a label hit from a synonym hit in the restored note.
_SYNONYM_MATCH = re.compile(r"exact match of an exact synonym", re.IGNORECASE)


def creation_event(record: dict) -> dict | None:
    """The record's own account of being imported from CultureMech, if any."""
    for event in record.get("curation_history") or []:
        if (event.get("action") or "").strip() != CREATION_ACTION:
            continue
        if (event.get("curator") or "").strip() != CREATION_CURATOR:
            continue
        if EVIDENCE_SOURCE in (event.get("changes") or ""):
            return event
    return None


def build_evidence(record: dict, event: dict) -> dict:
    """One evidence row restating the creation event in structured form."""
    mapping = record.get("ontology_mapping") or {}
    matched = "an exact ontology synonym" if _SYNONYM_MATCH.search(
        event.get("changes") or ""
    ) else "the ontology label"
    return {
        "evidence_type": EVIDENCE_TYPE,
        "source": EVIDENCE_SOURCE,
        "notes": (
            f"Surface form appears in CultureMech's occurrence table and was grounded to "
            f"{mapping.get('ontology_id')} on an exact match against {matched}. "
            f"Restored from the record's own creation history (#541); the residual "
            f"importer wrote this provenance only into the published SSSOM."
        ),
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.strip().splitlines()[0])
    parser.add_argument("--apply", action="store_true", help="write the records")
    args = parser.parse_args()

    stamp = datetime.now(timezone.utc).isoformat()
    touched = skipped_has_evidence = skipped_no_provenance = 0

    for path in sorted(MAPPED.glob("*.yaml")):
        record = yaml.safe_load(path.read_text(encoding="utf-8"))
        if not isinstance(record, dict):
            continue
        mapping = record.get("ontology_mapping") or {}
        if not mapping:
            continue
        if mapping.get("evidence"):
            skipped_has_evidence += 1
            continue
        event = creation_event(record)
        if event is None:
            # No self-attested CultureMech origin: leave it alone rather than
            # assert provenance the record does not claim.
            skipped_no_provenance += 1
            continue

        mapping["evidence"] = [build_evidence(record, event)]
        record.setdefault("curation_history", []).append(
            {
                "timestamp": stamp,
                "curator": CURATOR,
                "action": "CORRECTED",
                "changes": (
                    f"Added ontology_mapping.evidence recording the CultureMech occurrence "
                    f"table as the source of this grounding. The provenance was already in "
                    f"this record's {CREATION_ACTION} history entry but absent from the "
                    f"structured field the SSSOM builder reads, so a rebuild dropped "
                    f"MIM:{EVIDENCE_SOURCE} from the published row (#541)."
                ),
                "llm_assisted": False,
            }
        )
        touched += 1
        if args.apply:
            path.write_text(
                yaml.dump(record, sort_keys=False, allow_unicode=True, default_flow_style=False),
                encoding="utf-8",
            )

    verb = "Updated" if args.apply else "Would update"
    print(f"{verb} {touched} record(s)")
    print(f"  skipped, already had evidence      : {skipped_has_evidence}")
    print(f"  skipped, no self-attested CultureMech origin: {skipped_no_provenance}")
    if not args.apply:
        print("\nPreview only. Pass --apply to write.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
