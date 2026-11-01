"""One-time evidence packaging; reads run artifacts, writes only this directory.

Usage: python package_evidence.py RUN
Requires the existing MIM Python environment for PyYAML. This is an archival
helper, not an ingredient writer, generator, review, or publication command.
"""

from pathlib import Path
from datetime import datetime, timezone
import csv
import hashlib
import io
import json
import subprocess
import sys

import yaml


RUN = Path(sys.argv[1]).resolve()
REPO = RUN / "step2-mim"
OUT = Path(__file__).resolve().parent
REPORT = OUT.parent
BASE = "40b787d37d33d544551389ff019f2d64ad63d7cc"
OWNER = "data/ingredients/mapped/Na2hpo4_X_7_H2o.yaml"
SUBJECT = "MIM:Na2hpo4_X_7_H2o"
CANONICAL = "mappings/ingredient_mappings.sssom.tsv"
NATIVE_RECEIPT = "reports/sssom_completion_20260921/mapping_changes/issue875-ncit-exact-heptahydrate.json"
copied = []
references = []


def sha(data):
    return hashlib.sha256(data).hexdigest()


def write(relative, data):
    destination = OUT / relative
    destination.parent.mkdir(parents=True, exist_ok=True)
    with destination.open("xb") as stream:
        stream.write(data)


def document(relative, value):
    write(relative, (json.dumps(value, indent=2, ensure_ascii=False) + "\n").encode())


def copy(source, relative):
    source = RUN / source
    data = source.read_bytes()
    write(relative, data)
    assert source.read_bytes() == data, f"Source changed during copy: {source}"
    copied.append({"source": str(source), "packaged": relative,
                   "sha256": sha(data), "bytes": len(data)})
    return data


def reference(source, reason, **extra):
    source = Path(source)
    data = source.read_bytes()
    references.append({"source": str(source), "sha256": sha(data),
                       "bytes": len(data), "reason": reason, **extra})
    return data


def rows(data):
    return list(csv.DictReader(
        (line for line in data.decode().splitlines() if not line.startswith("#")),
        delimiter="\t"))


def git_bytes(path):
    return subprocess.check_output(["git", "show", f"{BASE}:{path}"], cwd=REPO)


frozen = {
    "README.md": "1e04dc58c21b76fc7d5fb90c49b7f8f4e8141417f868eb69680e897dd6785e7e",
    "sources/ncit-C61946.json": "a112c3e91dd6aa46feb112621ba5d13673df69f1b20665e042e22b8aa05a1d83",
    "sources/ncit-C61946-receipt.json": "9e6c6364182d4450114a8662eecf9a1db38d16a47cdcbbfc3f71cce21bb1bebb",
}
for name, digest in frozen.items():
    assert sha((REPORT / name).read_bytes()) == digest

for name in ["source-apply.json", "mapping-promotion.json", "receipt-publication.json",
             "source-apply.before.yaml", "source-apply.before-ledger.tsv"]:
    copy(f"step2-application/{name}", f"application/{name}")

generation_dir = REPO / "output/step2-native-candidate"
for path in sorted(generation_dir.rglob("*")):
    if path.is_file() and path.name != "candidate.sssom.tsv":
        relative = path.relative_to(generation_dir)
        copy(str(path.relative_to(RUN)), f"generation/{relative}")

logs = [
    "step2-baseline-strict", "step2-baseline-terms", "step2-writer-focused-green",
    "step2-writer-committed-preapply-red", "step2-writer-config-preflight",
    "step2-writer-production-dry-run", "step2-writer-lint-final", "step2-writer-mutations",
    "step2-source-apply", "step2-sync-curated", "step2-native-candidate",
    "step2-candidate-invariants", "step2-candidate-curies", "step2-candidate-labels",
    "step2-promotion-dry-run", "step2-mapping-promotion", "step2-native-mapping-receipt",
]
for name in logs:
    metadata = json.loads((RUN / f"logs/{name}.json").read_text())
    data = (RUN / f"logs/{name}.log").read_bytes()
    assert sha(data) == metadata["log_sha256"]
    assert metadata["exit_code"] == (1 if name == "step2-writer-committed-preapply-red" else 0)
    for suffix in ["json", "log"]:
        copy(f"logs/{name}.{suffix}", f"logs/{name}.{suffix}")

for name in ["generate_candidate.py", "validate_candidate.py", "make_step2_receipt.py", "run.py"]:
    copy(name, f"harnesses/{name}")
for name in ["stable-inputs.json", "mutation-results.json", "run_mutations.py"]:
    copy(f"step2-writer-evidence/{name}", f"writer/{name}")
mutations = json.loads((OUT / "writer/mutation-results.json").read_text())
for result in mutations["results"]:
    case = result["case"]
    data = copy(f"step2-writer-evidence/mutations/{case}/pytest.log", f"writer/mutations/{case}.log")
    assert sha(data) == result["log_sha256"]
    assert result["exit_code"] == (0 if case == "positive" else 1)

for name in ["baseline-and-probes.json", "producer-compatibility-probes.json"]:
    copy(f"step2-preflight/{name}", f"preflight/{name}")
copy("step2-preflight/workflow-20261101T041857Z/ncit-C61946-local-readonly.json",
     "preflight/ncit-C61946-local-readonly.json")
copy("step2-context.json", "context.json")

source = json.loads((OUT / "application/source-apply.json").read_text())
promotion = json.loads((OUT / "application/mapping-promotion.json").read_text())
publication = json.loads((OUT / "application/receipt-publication.json").read_text())
generation = json.loads((OUT / "generation/generation-receipt.json").read_text())
assert sha((OUT / "harnesses/generate_candidate.py").read_bytes()) == generation["harness_sha256"]
assert (OUT / "generation/inputs-before.json").read_bytes() == (OUT / "generation/inputs-after.json").read_bytes()
assert sha((OUT / "generation/inputs-before.json").read_bytes()) == generation["input_manifest_sha256"]
for name, digest in generation["label_maps"].items():
    assert sha((OUT / "generation" / name).read_bytes()) == digest

baseline_data = reference(RUN / "step2-application/source-apply.before.sssom.tsv",
    "Large table recoverable from the durable baseline commit; bounded excerpts packaged.",
    git_revision=BASE, git_path=CANONICAL)
assert baseline_data == git_bytes(CANONICAL)
assert baseline_data == (RUN / "step2-application/mapping-promotion.before.tsv").read_bytes()
canonical_data = reference(REPO / CANONICAL, "Maintained canonical table in this repository.",
    repository_path=CANONICAL)
candidate_data = reference(generation_dir / "candidate.sssom.tsv",
    "Diagnostic full native candidate; never promoted wholesale. Target excerpt packaged.")
native_data = reference(REPO / NATIVE_RECEIPT, "Maintained native sequence-16 receipt in this repository.",
    repository_path=NATIVE_RECEIPT)
assert sha(native_data) == publication["receipt_sha256"]
native = json.loads(native_data)
assert native["sequence"] == 16 and native["changed_rows"] == 1 and native["removed_rows"] == 1
assert native["added_rows"] == 0
for path, digest in publication["previous_receipts_unchanged"].items():
    assert sha(Path(path).read_bytes()) == digest

assert sha(baseline_data) == promotion["sssom_before_sha256"] == native["before_sha256"]
assert sha(canonical_data) == promotion["sssom_after_sha256"] == native["after_sha256"]
assert sha(candidate_data) == promotion["candidate_sha256"] == generation["candidate_sha256"]
tables = {"before": rows(baseline_data), "candidate": rows(candidate_data), "canonical": rows(canonical_data)}
assert {key: len(value) for key, value in tables.items()} == {"before": 2987, "candidate": 2979, "canonical": 2986}
target = {key: [row for row in value if row["subject_id"] == SUBJECT] for key, value in tables.items()}
assert {key: len(value) for key, value in target.items()} == {"before": 2, "candidate": 1, "canonical": 1}
for key, values in target.items():
    stream = io.StringIO(newline="")
    writer = csv.DictWriter(stream, fieldnames=list(values[0]), delimiter="\t", lineterminator="\n")
    writer.writeheader()
    writer.writerows(values)
    write(f"excerpts/{key}-target.tsv", stream.getvalue().encode())

# Compare untouched data lines, not normalized row dictionaries.
def unrelated_lines(data):
    return [line for line in data.splitlines(keepends=True)
            if not line.startswith(b"#") and not line.startswith((SUBJECT + "\t").encode())]

assert unrelated_lines(baseline_data) == unrelated_lines(canonical_data)
old_tokens = set().union(*(set(row["source"].split("|")) for row in target["before"]))
new_tokens = set(target["canonical"][0]["source"].split("|"))
assert old_tokens <= new_tokens
assert target["canonical"][0]["object_id"] == "NCIT:C61946"
assert target["canonical"][0]["predicate_id"] == "skos:exactMatch"
assert not target["canonical"][0]["validation_method"]
assert target["canonical"][0]["comment"] == target["candidate"][0]["comment"]

before_owner = yaml.safe_load((OUT / "application/source-apply.before.yaml").read_bytes())
owner_data = reference(REPO / OWNER, "Maintained corrected record in this repository.", repository_path=OWNER)
after_owner = yaml.safe_load(owner_data)
assert sha(owner_data) == source["records"][0]["after_yaml_sha256"]
assert after_owner["curation_history"][:-1] == before_owner["curation_history"]
changed_owner_fields = sorted(k for k in set(before_owner) | set(after_owner) if before_owner.get(k) != after_owner.get(k))
ledger_before = (OUT / "application/source-apply.before-ledger.tsv").read_bytes()
ledger_after = reference(REPO / "mappings/unified_mapping_rejections.tsv", "Maintained paired ledger.",
    repository_path="mappings/unified_mapping_rejections.tsv")
assert sha(ledger_before) == source["ledger_before_sha256"]
assert sha(ledger_after) == source["ledger_after_sha256"]
before_lines, after_lines = ledger_before.splitlines(keepends=True), ledger_after.splitlines(keepends=True)
assert len(before_lines) == len(after_lines)
ledger_changes = [{"line": i + 1, "before": old.decode().rstrip("\r\n"), "after": new.decode().rstrip("\r\n")}
                  for i, (old, new) in enumerate(zip(before_lines, after_lines)) if old != new]
assert len(ledger_changes) == 1

review_path = "reports/sssom_completion_20260921/review.json"
review_data = reference(REPO / review_path, "Current mapping-review snapshot; only this owner's decision excerpted.",
    repository_path=review_path)
review = json.loads(review_data)
assert review["source_sha256"] == sha(canonical_data)
decisions = [d for d in review["decisions"] if d.get("owner_record") == OWNER]
assert len(decisions) == 1 and decisions[0]["disposition"] == "WITHHOLD"
document("excerpts/mapping-review-target.json", {"source_path": review_path,
    "review_sha256": sha(review_data), "source_sha256": review["source_sha256"],
    "decisions": decisions,
    "note": "Historical review wording is preserved verbatim; its old CAS-promotion wording is superseded by the approved exact-NCIT decision. No approval is inferred."})

for path in sorted((RUN / "step2-application").rglob("write-*.json")):
    reference(path, "Native recovery journal retained in run evidence; large embedded pre-images not duplicated.")
for name in ["scripts/promote_heptahydrate_ncit.py", "tests/test_promote_heptahydrate_ncit.py",
             "tests/fixtures/issue875-owner-before.yaml"]:
    reference(REPO / name, "Authored source/test fixture maintained in this repository.", repository_path=name)

document("snapshot-checks.json", {
    "captured_at": datetime.now(timezone.utc).isoformat(),
    "method": "Read-only hash and payload checks during evidence packaging, not independent scientific review.",
    "author": "Codex", "llm_assisted": True,
    "tables": {key: {"rows": len(value), "target_rows": len(target[key])} for key, value in tables.items()},
    "unrelated_sssom_data_lines_identical": True,
    "baseline_table_matches_git_revision": BASE,
    "source_history_prefix_identical": True,
    "owner_changed_fields": changed_owner_fields,
    "ledger_changes": ledger_changes,
    "all_historical_source_tokens_preserved": True,
    "historical_source_tokens_are_independent_support_for_ncit": False,
    "new_comment_equals_native_candidate": True,
    "inherited_validation_stamp_present": False,
    "candidate_input_manifests_byte_identical": True,
    "candidate_label_capture_hashes_verified": True,
    "native_receipt_sequence": native["sequence"],
    "prior_native_receipts_hashes_verified": len(publication["previous_receipts_unchanged"]),
    "mapping_disposition": decisions[0]["disposition"],
    "scientific_approval_added": False,
    "chemistry_and_buffer_resolved": False,
    "final_qc_or_independent_review_claimed": False,
})
document("artifact-locations.json", {"copied_byte_for_byte": copied,
    "indexed_not_duplicated": references,
    "portability_note": "Absolute paths in raw receipts are historical literals. Copied artifacts resolve via packaged paths above; indexed repository files resolve via repository_path or git_revision/git_path. Run-only large tables and recovery journals remain external and are not claimed to be bundled."})
for name, digest in frozen.items():
    assert sha((REPORT / name).read_bytes()) == digest
print(json.dumps({"copied_files": len(copied), "indexed_files": len(references),
                  "report": str(OUT), "frozen_files_preserved": True}))
