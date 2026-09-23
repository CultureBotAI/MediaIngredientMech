"""Record a verified mapping-change batch as a link in the reviewed-SSSOM chain.

The trait and parent-name refreshes are synonym-only: they change ``other`` and
nothing else, so the assembler could verify them with the pinned producer. A
mapping change (a re-anchored parent, a regrade, a re-grounded identity, a
merge, a minted registry id) changes the row payload itself and may add or
remove rows. No producer can vouch for that; what the chain can still do is
make the change **explicit and auditable**, and refuse to carry any prior
approval across it.

A receipt therefore records, for one batch:

* the SSSOM digest before and after, so the chain stays link-by-link;
* every owner record the batch touched, with before/after YAML digests and the
  verification the curator wrote for it (from the mutator's apply log);
* every row that changed, was added or was removed, with its full before/after
  payload and both positions; and
* ``position_map``: for each pre-batch row position, the post-batch position
  (or ``null`` when the row was removed), so the assembler can carry the
  baseline's position-keyed cohorts, holds and decisions forward.

Rows are aligned by subject and slot (ontology row, ``cas:`` row, or the
registry prefix), which is stable across every shape above; a row whose slot
gains a new object is a *change*, not a removal plus an addition.

The assembler never turns a receipt into a SUPPORTED disposition. Every row a
receipt touches is WITHHOLD with the receipt as its basis, until a
mapping-specific review approves the corrected mapping.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
HERE = Path(__file__).resolve().parent
SOURCE = ROOT / "mappings/ingredient_mappings.sssom.tsv"


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def rows_of(data: bytes) -> list[dict]:
    lines = data.decode().splitlines(keepends=True)
    return list(csv.DictReader((line for line in lines if not line.startswith("#")), delimiter="\t"))


def slot(row: dict) -> tuple[str, str]:
    """Stable alignment key: the subject plus which of its rows this is."""
    obj = row["object_id"]
    prefix = obj.split(":", 1)[0]
    if prefix in {"cas", "kgmicrobe.ingredient", "kgmicrobe.compound"}:
        return row["subject_id"], prefix
    return row["subject_id"], "ontology"


def align(before: list[dict], after: list[dict]) -> tuple[list[dict], list[int | None]]:
    before_by = {}
    for i, row in enumerate(before, 1):
        key = slot(row)
        if key in before_by:
            raise ValueError(f"Two pre-batch rows share a slot: {key}")
        before_by[key] = (i, row)
    after_by = {}
    for j, row in enumerate(after, 1):
        key = slot(row)
        if key in after_by:
            raise ValueError(f"Two post-batch rows share a slot: {key}")
        after_by[key] = (j, row)
    changes = []
    position_map: list[int | None] = [None] * len(before)
    for key, (i, old) in before_by.items():
        if key in after_by:
            j, new = after_by[key]
            position_map[i - 1] = j
            if old != new:
                changes.append({"kind": "changed", "before_position": i, "after_position": j,
                                "before": old, "after": new})
        else:
            changes.append({"kind": "removed", "before_position": i, "after_position": None,
                            "before": old, "after": None})
    for key, (j, new) in after_by.items():
        if key not in before_by:
            changes.append({"kind": "added", "before_position": None, "after_position": j,
                            "before": None, "after": new})
    changes.sort(key=lambda c: (c["after_position"] or 0, c["before_position"] or 0))
    return changes, position_map


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--batch", required=True, help="receipt name, e.g. issue312-batch1")
    parser.add_argument("--sequence", type=int, required=True, help="1-based link order after the synonym refreshes")
    parser.add_argument("--issue", required=True)
    parser.add_argument("--scope", required=True, help="one sentence: what kind of change this batch makes")
    parser.add_argument("--before-sssom", type=Path, required=True, help="byte copy of the SSSOM taken before the batch")
    parser.add_argument("--apply-log", type=Path, required=True, help="the mutator's apply log (records with before/after hashes)")
    args = parser.parse_args()
    before_bytes = args.before_sssom.read_bytes()
    after_bytes = SOURCE.read_bytes()
    before, after = rows_of(before_bytes), rows_of(after_bytes)
    changes, position_map = align(before, after)
    log = json.loads(args.apply_log.read_text())
    records = []
    for entry in log["records"]:
        path = ROOT / entry["source_record"]
        current = digest(path.read_bytes())
        if entry["after_yaml_sha256"] != current:
            raise ValueError(f"{entry['source_record']} changed after the apply log was written")
        records.append({
            "source_record": entry["source_record"],
            "shape": entry["shape"],
            "before_yaml_sha256": entry["before_yaml_sha256"],
            "after_yaml_sha256": entry["after_yaml_sha256"],
            "change": entry["change"],
            "verification": entry["verification"],
        })
    touched_subjects = {c["after"]["subject_id"] if c["after"] else c["before"]["subject_id"] for c in changes}
    receipt = {
        "schema_version": 1,
        "batch": args.batch,
        "sequence": args.sequence,
        "issue": args.issue,
        "scope": args.scope,
        "approval": "NONE: every touched row is withheld pending mapping-specific review; no prior approval carries across this link.",
        "before_sha256": digest(before_bytes),
        "after_sha256": digest(after_bytes),
        "before_row_count": len(before),
        "after_row_count": len(after),
        "records": records,
        "changed_rows": sum(c["kind"] == "changed" for c in changes),
        "added_rows": sum(c["kind"] == "added" for c in changes),
        "removed_rows": sum(c["kind"] == "removed" for c in changes),
        "touched_subjects": sorted(touched_subjects),
        "changes": changes,
        "position_map": position_map,
    }
    out = HERE / f"{args.batch}.json"
    out.write_text(json.dumps(receipt, indent=2) + "\n")
    print(json.dumps({k: v for k, v in receipt.items() if k not in {"changes", "position_map", "records"}}, indent=2))
    print(f"wrote {out.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
