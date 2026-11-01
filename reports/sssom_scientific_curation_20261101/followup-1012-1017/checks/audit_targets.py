"""Read-only exact target audit for the bounded follow-up review."""

import csv
import hashlib
import io
import json
import subprocess
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1] / "mim"
BASE = "4625afd492b6cf43e3b499d1425d2453d490009d"
PRIOR = "612860e467aff74ecc1339df7c3c32b1bf940b95"
NAME = "mappings/ingredient_mappings.sssom.tsv"


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def historical(rev, path):
    return subprocess.check_output(["git", "show", rev + ":" + path], cwd=ROOT)


def table(raw):
    return list(csv.DictReader(io.StringIO("".join(
        line for line in raw.decode().splitlines(keepends=True) if not line.startswith("#")
    )), delimiter="\t"))


def read(path):
    return json.loads((ROOT / path).read_text())


current_bytes = (ROOT / NAME).read_bytes()
baseline_bytes = historical(BASE, NAME)
current, baseline = table(current_bytes), table(baseline_bytes)
assert len(current) == len(baseline) == 2987
assert [tuple(r[k] for k in ("subject_id", "predicate_id", "object_id")) for r in current] == [
    tuple(r[k] for k in ("subject_id", "predicate_id", "object_id")) for r in baseline
]
changes = []
for pos, (before, after) in enumerate(zip(baseline, current, strict=True), 1):
    if before != after:
        changes.append({
            "position": pos,
            "selector": {k: after[k] for k in ("subject_id", "predicate_id", "object_id")},
            "changed_fields": {k: {"before": before[k], "after": after[k]} for k in after if before[k] != after[k]},
        })
expected = {184: {"other"}, 258: {"other"}, 535: {"other"}, 648: {"other", "mapping_date"},
            649: {"mapping_date"}, 901: {"other"}, 1728: {"other"}, 2528: {"other"}, 2588: {"other"}}
assert {c["position"]: set(c["changed_fields"]) for c in changes} == expected
assert "DL-carnitine" in current[647]["other"].split("|")
assert "carnitinamide" not in current[647]["other"].casefold()

review_path = "reports/sssom_completion_20260921/review.json"
review, prior_review = read(review_path), json.loads(historical(PRIOR, review_path))
counts = Counter(d["disposition"] for d in review["decisions"])
assert counts == {"SUPPORTED": 1740, "WITHHOLD": 1247}
assert [(d["source_position"], d["disposition"]) for d in review["decisions"]] == [
    (d["source_position"], d["disposition"]) for d in prior_review["decisions"]
]
assert review["source_sha256"] == sha(current_bytes)
assert all(review["decisions"][pos - 1]["disposition"] == "WITHHOLD" for pos in expected)
identity_holds = [645, 646, 647, 2524, 2525, 2526]
assert all(review["decisions"][pos - 1]["disposition"] == "WITHHOLD" for pos in identity_holds)
receipt14 = read("reports/sssom_completion_20260921/mapping_changes/issue669-1003-scoped-alias-corrections.json")
receipt15 = read("reports/sssom_completion_20260921/mapping_changes/issue1014-provenance-restoration.json")
assert receipt14["before_sha256"] == sha(baseline_bytes)
assert receipt14["after_sha256"] == receipt15["before_sha256"]
assert receipt15["after_sha256"] == sha(current_bytes)
mapping_evidence = read("reports/sssom_completion_20260921/mapping-evidence.json")
coexisting_bases = {str(pos): mapping_evidence["entries"][str(pos)]["basis"] for pos in (184, 901, 2528)}
assert all({"synonym_correction", "mapping_change"} <= set(b) for b in coexisting_bases.values())

companion_path = "reports/ingredient_bundle_20261101_followup/review.json"
companion = read(companion_path)
previous_companion_path = "reports/ingredient_bundle_20261101/review.json"
previous_companion = read(previous_companion_path)
dependency = read("reports/ingredient_bundle_20261101_followup/dependency-refresh.json")
assert companion["decisions"] == previous_companion["decisions"]
assert companion["record_inputs"] == previous_companion["record_inputs"]
assert len(companion["decisions"]) == 51 and len(companion["record_inputs"]) == 20
claims = read(companion["claims_file"])["claims"]
assert len(claims) == 51
assert sha((ROOT / companion["claims_file"]).read_bytes()) == companion["claims_sha256"] == previous_companion["claims_sha256"]
assert companion["base_review_sha256"] == sha((ROOT / review_path).read_bytes())
assert dependency["successor_review_sha256"] == sha((ROOT / companion_path).read_bytes())
assert (ROOT / "reports/ingredient_bundle_20261101_followup/prior-review.json").read_bytes() == (ROOT / previous_companion_path).read_bytes()
for name, digest in (companion["inputs"] | companion["record_inputs"]).items():
    assert sha((ROOT / name).read_bytes()) == digest, name
for entry in dependency["selected_mapping_evidence_unchanged"]:
    row = entry["original_row"]
    assert baseline.count(row) == current.count(row) == 1
assert dependency["scientific_approval_added"] is False
replay = HERE.parents[0] / "final-replay-review.json"
assert replay.read_bytes() == (ROOT / companion_path).read_bytes()

semantic = read("reports/semantic_review_20260921/resolution/current-review.json")
assert semantic["release_verdict"] == "FAIL"
assert len(semantic["blocking_finding_ids"]) == 1733
assert len(semantic["blocking_assertion_ids"]) == 2272
protected = {}
for name in [".github/workflows/qc-evidence.yaml", "workflow/mech-workflow.yaml", "UNIFIED_INGREDIENT_MAPPING.tsv"]:
    raw = (ROOT / name).read_bytes()
    assert historical(PRIOR, name) == raw
    assert historical(BASE, name) == raw
    protected[name] = sha(raw)
result = {
    "status": "PASS", "completed_at": datetime.now(timezone.utc).isoformat(),
    "scope": "Exact mechanical comparison; no scientific approval or hold retirement",
    "baseline_revision": BASE, "previous_pr_head": PRIOR,
    "current_head": subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=ROOT).decode().strip(),
    "canonical": {"sha256": sha(current_bytes), "rows": len(current), "changed_rows": changes,
                  "unchanged_payloads": len(current) - len(changes), "added_rows": 0, "removed_rows": 0,
                  "row_identity_order_unchanged": True, "dispositions": dict(counts),
                  "prior_head_dispositions_unchanged": True, "changed_positions_all_withheld": True,
                  "additional_identity_hold_positions": identity_holds,
                  "receipt_chain": [14, 15], "coexisting_evidence_bases": coexisting_bases},
    "companion": {"sha256": sha((ROOT / companion_path).read_bytes()), "claims": len(claims),
                  "claim_counts": dict(Counter(c["kind"] for c in claims)),
                  "owners": len(companion["record_inputs"]), "claims_and_decisions_unchanged": True,
                  "owner_bytes_unchanged": True, "selected_original_complete_rows_unchanged": True,
                  "current_final_producer_replay_identical": True, "scientific_approval_added": False},
    "semantic_release": {"verdict": semantic["release_verdict"], "blocking_findings": 1733, "blocking_assertions": 2272},
    "protected_files_unchanged": protected,
}
output = HERE / "target-audit.json"
with output.open("x") as handle:
    json.dump(result, handle, indent=2)
    handle.write("\n")
print(json.dumps({"status": result["status"], "canonical_rows": len(current), "changed_rows": len(changes),
                  "companion_claims": len(claims), "companion_owners": len(companion["record_inputs"]),
                  "report": str(output)}, indent=2))
