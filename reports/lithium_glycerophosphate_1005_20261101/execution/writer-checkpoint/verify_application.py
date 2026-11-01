"""Read-only post-application verification; no apply/publish or maintained writes.

The native complete_owner check renders a validated proposal in a temporary
directory, then deletes it. All repository data and supplied receipts are read.
Run only after source, canonical promotion and sync-curated have completed.
"""
from pathlib import Path
from datetime import datetime, timezone
import argparse
import hashlib
import importlib.util
import io
import json
import subprocess
import sys
import tarfile

import yaml

RUN = Path(__file__).resolve().parents[1]
BASE = "838d0c2627552b0094545ebb580b5bb9b1a84d57"


def require(value, message):
    if not value:
        raise ValueError(message)


def digest(data):
    return hashlib.sha256(data).hexdigest()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=RUN / "step4-mim")
    parser.add_argument("--baseline-inputs", type=Path, default=RUN / "step4-baseline-inputs-v2.json")
    parser.add_argument("--source-log", type=Path, required=True)
    parser.add_argument("--promotion-log", type=Path, required=True)
    parser.add_argument("--candidate", type=Path, required=True)
    args = parser.parse_args()
    root = args.root.resolve()
    sys.path[:0] = [str(root), str(root / "src")]
    path = root / "scripts/curate_lithium_glycerophosphate.py"
    spec = importlib.util.spec_from_file_location("verified_lithium_writer", path)
    writer = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(writer)
    baseline = json.loads(args.baseline_inputs.read_bytes())
    require(baseline["head"] == BASE, "Wrong approved baseline")
    archive = subprocess.check_output(["git", "archive", BASE, "data/ingredients"], cwd=root)
    with tarfile.open(fileobj=io.BytesIO(archive)) as bundle:
        before_records = {m.name: bundle.extractfile(m).read() for m in bundle.getmembers()
                          if m.isfile() and m.name.endswith(".yaml")}
    frozen_hashes = {name: digest(data) for name, data in before_records.items()}
    require(frozen_hashes == {p: h for p, h in baseline["input_sha256"].items() if p.startswith("data/ingredients/")},
            "Saved baseline record inventory differs from immutable Git content")
    current_paths = {str(p.relative_to(root)): p for p in (root / "data/ingredients").rglob("*.yaml")}
    require(set(current_paths) == set(before_records), "Source record path set changed")
    current_hashes = {name: digest(writer.regular(p)) for name, p in current_paths.items()}
    changed = [name for name in sorted(current_hashes) if current_hashes[name] != frozen_hashes[name]]
    owner = str(writer.OWNER)
    require(changed == [owner], "Expected exactly one changed source record")
    before_bytes = before_records[owner]
    current = writer.regular(root / writer.OWNER)
    old, record = (yaml.safe_load(b) for b in (before_bytes, current))
    require(len(old["curation_history"]) == 8 and record["curation_history"][:-1] == old["curation_history"],
            "Original eight-event history prefix changed")
    unchanged_fields = set(old) - {"identifier", "chemical_properties", "ontology_mapping", "curation_history"}
    require(all(record[k] == old[k] for k in unchanged_fields), "Unreviewed source field changed")
    require(record["ontology_mapping"]["evidence"][:-1] == old["ontology_mapping"]["evidence"], "Prior mapping evidence changed")
    require("chemical_properties" not in record, "Free-acid chemistry remains active")
    require(json.dumps(old["chemical_properties"], sort_keys=True) in record["curation_history"][-1]["changes"],
            "Exact retired chemistry missing from history")
    writer.complete_owner(current)
    source_log = args.source_log.absolute()
    source_inputs, source = writer.source_receipt(root, source_log, current)
    aggregate_path = root / "data/curated/mapped_ingredients.yaml"
    collection = yaml.load(aggregate_path.read_text(), Loader=yaml.CSafeLoader)
    entries = [r for r in collection["ingredients"] if r.get("identifier") == writer.NEW or r.get("preferred_term") == writer.NAME]
    require(entries == [record], "Aggregate target is missing, duplicated or not semantically synchronized")

    def git_bytes(relative):
        return subprocess.check_output(["git", "show", f"{BASE}:{relative}"], cwd=root)

    before = git_bytes(writer.SSSOM)
    baseline_before = git_bytes(writer.BASELINE)
    require(source_inputs[writer.backups(source_log)[writer.SSSOM]] == before, "Canonical source backup differs from baseline")
    require(source_inputs[writer.backups(source_log)[writer.BASELINE]] == baseline_before, "Rule K source backup differs from baseline")
    candidate = writer.regular(args.candidate.absolute())
    canonical = writer.regular(root / writer.SSSOM)
    baseline_after = writer.regular(root / writer.BASELINE)
    require(canonical == writer.promoted_sssom(before, candidate, current), "Canonical differs from bounded native promotion")
    require(baseline_after == writer.retired_baseline(baseline_before), "Rule K delta exceeds the approved one pair")
    expected = {"phase": "promote", "approval": writer.APPROVAL, "records": source["records"],
                "source_receipt_sha256": digest(source_inputs[source_log]), "candidate_sha256": digest(candidate),
                "sssom_before_sha256": digest(before), "sssom_after_sha256": digest(canonical),
                "baseline_before_sha256": digest(baseline_before), "baseline_after_sha256": digest(baseline_after),
                "changed_rows": 2, "removed_rows": 1, "removed_baseline_rows": 1,
                "preserved_historical_source_tokens": True, "preserved_original_validation_stamps": True}
    promotion_log = args.promotion_log.absolute()
    writer.completed_receipt(promotion_log, expected, root, {writer.SSSOM, writer.BASELINE})
    for relative, data in ((writer.SSSOM, before), (writer.BASELINE, baseline_before)):
        require(writer.regular(writer.backups(promotion_log)[relative]) == data, "Promotion backup changed")
    _, prior = writer.table(before)
    _, after = writer.table(canonical)
    old_rows = {r["object_id"]: r for r in prior if r["subject_id"] == writer.SUBJECT}
    selected = [r for r in after if r["subject_id"] == writer.SUBJECT]
    require(len(selected) == 2 and {r["object_id"] for r in selected} == {writer.PARENT, writer.NEW}, "Wrong published row identities")
    allowed = {"source", "mapping_date", "other", "comment"}
    changed_columns = {}
    for row in selected:
        obj = row["object_id"]
        differences = {k for k, value in row.items() if old_rows[obj][k] != value}
        require(differences <= allowed, "Unexpected published column change")
        require(row["validation_method"] == old_rows[obj]["validation_method"], "Historical stamp changed")
        require(set(old_rows[obj]["source"].split("|")) <= set(row["source"].split("|")), "Historical sources lost")
        if obj == writer.PARENT:
            require(row["predicate_id"] == "skos:broadMatch" and not row["other"], "Parent acquired identity aliases/CAS")
            require(row["comment"] == old_rows[obj]["comment"] and row["comment"].startswith("[#390"), "Historical #390 lost")
        else:
            require(row["predicate_id"] == "skos:exactMatch" and row["other"] == "CAS:17989-41-2", "Local registry CAS display scope changed")
        changed_columns[obj] = sorted(differences)

    def unrelated(data):
        return [line for line in data.splitlines(keepends=True)
                if not line.startswith((writer.SUBJECT + "\t").encode())
                and not line.startswith((b"# mapping_date:", b"# mapping_set_version:"))]

    require(unrelated(before) == unrelated(canonical), "Unrelated canonical bytes changed")
    require(len(after) == len(prior) - 1, "Canonical row count delta differs")
    preserved = {}
    for name in ("mappings/culturemech_recipe_membership.tsv", "mappings/unified_mapping_rejections.tsv",
                 "UNIFIED_INGREDIENT_MAPPING.tsv", ".github/workflows/qc-evidence.yaml", "scripts/.vendored_canon_ref"):
        value = digest(writer.regular(root / name))
        require(value == baseline["input_sha256"][name], f"Out-of-scope protected input changed: {name}")
        preserved[name] = value
    require(current_hashes == {n: digest(writer.regular(p)) for n, p in current_paths.items()}, "Records changed during verification")
    print(json.dumps({"verified_at": datetime.now(timezone.utc).isoformat(), "baseline": BASE,
                      "scope": "Authored read-only post-application comparison; not independent scientific approval",
                      "source_records": len(current_hashes), "changed_owners": changed,
                      "unchanged_owners": len(current_hashes) - 1, "history_prefix_events": 8,
                      "role_payloads_unchanged": True, "rejected_labels_unchanged": True,
                      "aggregate_target_equals_individual": True, "complete_source_receipt": True,
                      "complete_promotion_receipt": True, "canonical_before_rows": len(prior),
                      "canonical_after_rows": len(after), "changed_rows": 2, "removed_rows": 1,
                      "changed_columns": changed_columns, "unrelated_canonical_bytes_identical": True,
                      "retired_rule_k_pairs": 1, "canonical_sha256": digest(canonical),
                      "candidate_sha256": digest(candidate), "owner_sha256": digest(current),
                      "source_receipt_sha256": digest(source_inputs[source_log]),
                      "promotion_receipt_sha256": digest(promotion_log.read_bytes()),
                      "preserved_inputs": preserved, "approval": "NONE"}, indent=2))


if __name__ == "__main__":
    main()
