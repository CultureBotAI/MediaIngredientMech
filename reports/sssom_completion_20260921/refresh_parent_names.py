"""Apply only the reviewed #232 parent-name synonym delta, checked by the pinned producer.

Parameterized copy of refresh_trait_synonyms.py: same producer pin, same
veto and loss checks, a different decisions file and receipt.

A full producer rebuild also refreshes unrelated enrichment and confidence
annotations. This bounded refresh preserves those fields and all other rows.
The producer is supplied from the repository's exact shared-tooling pin.
"""

import argparse
import csv
import hashlib
import importlib.util
import io
import json
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent


def digest(data):
    return hashlib.sha256(data).hexdigest()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--claw", type=Path, required=True)
    args = parser.parse_args()
    plan = json.loads((HERE / "parent_names/decisions.json").read_text())
    target = ROOT / plan["baseline_sssom"]["path"]
    original = target.read_bytes()
    if digest(original) != plan["baseline_sssom"]["sha256"]:
        raise ValueError("Source differs from the reviewed #232 baseline")
    producer = args.claw / "scripts/build_mim_ingredient_sssom.py"
    # This digest identifies the actual producer bytes from pin 44db08d5.
    expected = "62fec32826c54257d39daee0ca688f546222a92e730db106cdfd6fbb232cd4d8"
    if digest(producer.read_bytes()) != expected:
        raise ValueError("Not the reviewed pinned producer")
    sys.path.insert(0, str(producer.parent))
    spec = importlib.util.spec_from_file_location("pinned_mim_producer", producer)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    lines = original.decode().splitlines(keepends=True)
    comments = [line for line in lines if line.startswith("#")]
    reader = csv.DictReader((line for line in lines if not line.startswith("#")), delimiter="\t")
    rows = list(reader)
    changes = []
    for entry in plan["records"]:
        path = ROOT / entry["source_record"]
        record = yaml.safe_load(path.read_text())
        rejected = {d["before_synonym"]["synonym_text"] for d in entry["decisions"]}
        for reviewed in entry["sssom_rows"]:
            old = reviewed["row"]
            row = rows[reviewed["data_row_position"] - 1]
            if row != old:
                raise ValueError("Source row differs from reviewed parent-name decision")
            # Feed the previous enrichment surfaces to the pinned producer;
            # its explicit rejection veto must defeat upstream reintroduction.
            regenerated = module._row_from_yaml(
                path,
                {},
                {},
                {row["object_id"]: (row["object_label"], row["other"].split("|"))},
                {row["object_id"]: row["object_label"]},
            )
            rebuilt = next(r for r in regenerated if r["object_id"] == row["object_id"])
            published = set(rebuilt["other"].split("|"))
            if rejected & published:
                raise ValueError("Pinned producer republished a rejected parent name")
            kept = [token for token in row["other"].split("|") if token not in rejected]
            if any(token not in published for token in kept):
                raise ValueError("Producer lost an unrelated existing synonym")
            for token in rejected:
                if not any(
                    s["synonym_text"] == token and s["synonym_type"] == "REJECTED_LABEL"
                    for s in record["synonyms"]
                ):
                    raise ValueError("Reviewed source rejection is missing")
            row["other"] = "|".join(kept)
            changes.append(
                {
                    "source_record": entry["source_record"],
                    "source_record_sha256": digest(path.read_bytes()),
                    "source_position": reviewed["data_row_position"],
                    "before": old,
                    "after": dict(row),
                    "removed_tokens": sorted(rejected),
                }
            )
    out = io.StringIO()
    out.writelines(comments)
    writer = csv.DictWriter(out, fieldnames=reader.fieldnames, delimiter="\t", lineterminator="\n")
    writer.writeheader()
    writer.writerows(rows)
    result = out.getvalue().encode()
    receipt = {
        "schema_version": 1,
        "scope": "Bounded synonym-only refresh; no new identity, predicate, confidence or provenance assertion.",
        "producer_pin": (ROOT / "scripts/.vendored_canon_ref").read_text().strip(),
        "producer_sha256": expected,
        "before_sha256": digest(original),
        "after_sha256": digest(result),
        "row_count": len(rows),
        "changed_rows": len(changes),
        "removed_tokens": sum(len(c["removed_tokens"]) for c in changes),
        "changes": changes,
    }
    target.write_bytes(result)
    (HERE / "parent-name-refresh.json").write_text(json.dumps(receipt, indent=2) + "\n")
    print(json.dumps({k: v for k, v in receipt.items() if k != "changes"}, indent=2))


if __name__ == "__main__":
    main()
