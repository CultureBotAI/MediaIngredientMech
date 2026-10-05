#!/usr/bin/env python3
"""Point four 2026-09-21 merge tombstones at their merge targets (#799).

`docs/LABEL_INDEX_CONTRACT.md`: "For a merged record the `identifier` already
points at the merge target, so the row still resolves correctly and should be
followed." The semantic review of 2026-09-21 merged these four records into
reviewed survivors but left each tombstone on the identity the review had just
rejected, so a consumer that follows REJECTED rows -- as the contract tells it
to -- resolved `NaNO` to NCIT:C54713, the *nano* unit prefix, and `Sodium
phosphate dibasic` to trisodium phosphate. No live record holds any of the four
old identifiers, which is how CultureMech's pin check caught it.

Only `identifier` changes. The merge events promised that the original fields
remain on the tombstone, so `ontology_mapping` (the rejected term) is kept as
provenance, and the old identifier is written into the new curation event.

Writes the collection; follow with `just sync-individual`. Idempotent: a
tombstone already on its target is left alone.

Usage:
    python scripts/fix_799_tombstone_identifiers.py           # preview
    python scripts/fix_799_tombstone_identifiers.py --apply
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from mediaingredientmech.curate.curation_event import record_curation_event  # noqa: E402
from mediaingredientmech.utils.yaml_handler import save_yaml  # noqa: E402

MAPPED = ROOT / "data" / "curated" / "mapped_ingredients.yaml"
CURATOR = "fix_799_tombstone_identifiers"

# preferred_term -> (rejected identity left on the tombstone, merge target)
# Each target is the one the record's own MERGED_INTO event names.
TOMBSTONES = {
    "NaNO": ("NCIT:C54713", "CHEBI:63005"),
    "Atrazin": ("cas:1924-24-9", "CHEBI:15930"),
    "EDTA (chelating agent)": ("NCIT:C360", "CHEBI:4735"),
    "Sodium phosphate dibasic": ("CHEBI:37583", "CHEBI:34683"),
}


def plan(records: list[dict]) -> list[tuple[dict, str, str]]:
    live = {r.get("identifier") for r in records if r.get("mapping_status") == "MAPPED"}
    changes = []
    for term, (old, target) in TOMBSTONES.items():
        hits = [r for r in records if r.get("preferred_term") == term]
        if len(hits) != 1:
            raise SystemExit(f"{term!r} matched {len(hits)} record(s), expected exactly 1")
        record = hits[0]
        if record.get("mapping_status") != "REJECTED":
            raise SystemExit(f"{term!r} is {record.get('mapping_status')}, expected a REJECTED tombstone")
        merged = [e for e in record.get("curation_history") or [] if e.get("action") == "MERGED_INTO"]
        if not merged or not str(merged[-1].get("changes", "")).startswith(f"Merged into {target} "):
            raise SystemExit(f"{term!r}: last MERGED_INTO event does not name {target}")
        if target not in live:
            raise SystemExit(f"{term!r}: merge target {target} is not held by a live MAPPED record")
        if record.get("identifier") == target:
            continue
        if record.get("identifier") != old:
            raise SystemExit(f"{term!r} is on {record.get('identifier')}, expected {old} or {target}")
        changes.append((record, old, target))
    return changes


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args()
    data = yaml.safe_load(MAPPED.read_text(encoding="utf-8"))
    changes = plan(data["ingredients"])
    for record, old, target in changes:
        print(f"{record['preferred_term']}: {old} -> {target}")
    if not changes:
        print("nothing to do: every tombstone already points at its merge target")
        return
    if not args.apply:
        print("preview only; re-run with --apply")
        return
    for record, old, target in changes:
        record["identifier"] = target
        record_curation_event(
            record,
            curator=CURATOR,
            action="CORRECTED",
            changes=(
                f"Tombstone identifier {old} -> {target}, the merge target its MERGED_INTO "
                "event names, so the REJECTED row resolves to the survivor as "
                "docs/LABEL_INDEX_CONTRACT.md requires (#799). The rejected identity stays "
                "in ontology_mapping as provenance; no mapping, synonym or occurrence change."
            ),
            previous_status="REJECTED",
            new_status="REJECTED",
            llm_assisted=False,
        )
    save_yaml(data, MAPPED, backup=False)
    print(f"wrote {len(changes)} record(s); run `just sync-individual`")


if __name__ == "__main__":
    main()
