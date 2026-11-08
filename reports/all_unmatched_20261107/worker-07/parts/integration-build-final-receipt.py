"""Independent final receipt compiler; reads frozen artifacts, writes review only."""
import argparse
import collections
import hashlib
import json
import subprocess
from datetime import datetime, timezone
from pathlib import Path

import yaml

R = Path("reports/all_unmatched_20261107/worker-07")
BASE = "e000d66dd26ab053e9b17ce7bf8d3c873c3dde99"


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def digest(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()).hexdigest()


def read(path):
    return json.loads(path.read_text())


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--native-directory", required=True)
    parser.add_argument("--audit", required=True)
    parser.add_argument("--integrity", required=True)
    args = parser.parse_args()
    output = R / "captures/integration-review-final.json"
    assert not output.exists(), "Preserve earlier review receipts"
    native_dir = Path(args.native_directory)
    native = yaml.safe_load((native_dir / "review.yaml").read_text())
    decisions = read(R / "decisions.json")["decisions"]
    proposals = read(R / "proposals.json")["proposals"]
    evidence = read(R / "evidence.json")["evidence"]
    integrity = read(R / args.integrity)
    assert integrity["status"] == "PASS" and not integrity["errors"]
    for path, expected in integrity["input_hashes"].items():
        assert sha(R / path) == expected, path
    audit = read(R / args.audit)
    assert audit["structural_accounting"] == "PASS"
    validator = read(R / "logs/final-proposal-validation.json")
    assert validator["status"] == "PASS"
    assert validator["proposals_sha256"] == sha(R / "proposals.json")
    assert len(validator["results"]) == len(proposals) == 100
    for proposal, checked in zip(proposals, validator["results"]):
        assert proposal["proposal_id"] == checked["proposal_id"]
        assert proposal["after_capture"]["sha256"] == checked["after_sha256"]
        assert sha(R / proposal["after_capture"]["path"]) == checked["after_sha256"]
        assert not checked["schema_errors"] and not checked["introduced_identifier_collision"]
    baseline = read(R / "captures/root-maintained-baseline-hashes.json")
    assert len(baseline["files"]) == validator["baseline_file_count"]
    assert all(sha(Path(path)) == expected for path, expected in baseline["files"].items())

    primary_receipts = [
        ("A", "captures/c-review-a-final.json", "case_reviews", 0, 70),
        ("B", "parts/a-review-b-final.json", "cases", 70, 140),
        ("C", "parts/b-independent-c-review-final.json", "cases", 140, 188),
    ]
    coverage = []
    for part, path, key, start, stop in primary_receipts:
        reviewed = read(R / path)
        expected_cases = {d["case_id"] for d in decisions[start:stop]}
        assert {c["case_id"] for c in reviewed[key]} == expected_cases
        for relative, expected in reviewed["input_hashes"].items():
            actual = R / relative if "/" in relative else R / "parts" / relative
            assert sha(actual) == expected, relative
        coverage.append({"part": part, "review_path": path, "sha256": sha(R / path), "case_count": stop - start, "case_indices_half_open": [start, stop], "input_hashes_match": True})

    root_science = read(R / "captures/integration-stock-deltas-final.json")
    for reviewed in root_science["cases"]:
        actual = decisions[reviewed["case_index"]]
        scientific = {k: v for k, v in actual.items() if k not in reviewed["scientific_field_hash_exclusions"]}
        assert digest(scientific) == reviewed["reviewed_scientific_fields_sha256"]
    for checked in root_science["proposals_checked"]:
        assert sha(R / checked["capture"]["path"]) == checked["capture"]["sha256"]

    owner_paths = {o["path"] for d in decisions for o in d["owner_records"]}
    assert owner_paths == {target["path"] for target in native["targets"]}
    assert len(owner_paths) == len(native["assessments"]) == 77
    assert native["reviewer"]["independence"] == "self_review"
    assert len(native["findings"]) == 5
    malate = next(a for a in native["assessments"] if "data/ingredients/mapped/Sodium_Malate.yaml" in a["target_ids"])
    assert malate["outcome"] == "concern"
    assert any("data/ingredients/mapped/Sodium_Malate.yaml" in f["target_ids"] for f in native["findings"])
    native_hashes = {}
    for directory in sorted(Path("reviews/structured").glob("*worker07-source-owner-comparison*")):
        review = yaml.safe_load((directory / "review.yaml").read_text())
        for item in review["source"]["inputs"]:
            assert sha(Path(item["path"])) == item["sha256"], item["path"]
        for name in ["review.yaml", "review.md"]:
            native_hashes[str(directory / name)] = sha(directory / name)

    combined = []
    for proposal in proposals:
        if not proposal["proposal_id"].startswith("W07-COMBINED-") or proposal["kind"] != "edit_existing_owner":
            continue
        before = yaml.safe_load(Path(proposal["owner_path"]).read_text())
        after = yaml.safe_load((R / proposal["after_capture"]["path"]).read_text())
        changed = sorted(k for k in before.keys() | after.keys() if before.get(k) != after.get(k))
        assert set(changed) <= {"synonyms", "curation_history", "ontology_mapping"}
        assert before["identifier"] == after["identifier"]
        assert all(v == after["ontology_mapping"].get(k) for k, v in before["ontology_mapping"].items() if k != "evidence")
        old_history = before.get("curation_history", [])
        assert after["curation_history"][:len(old_history)] == old_history
        old = {x["synonym_text"]: x for x in before.get("synonyms", [])}
        new = {x["synonym_text"]: x for x in after.get("synonyms", [])}
        combined.append({"proposal_id": proposal["proposal_id"], "before_sha256": proposal["before_sha256"], "after_capture": proposal["after_capture"], "original_author_payloads": proposal["original_author_payloads"], "changed_fields": changed, "synonym_deltas": [{"text": text, "before": old.get(text), "after": new.get(text)} for text in sorted(old.keys() | new.keys()) if old.get(text) != new.get(text)], "assessment": "Accepted compatible baseline-relative author deltas; source qualifiers, rejected labels, unrelated claims and inherited history retained. No full-owner approval."})
    assert len(combined) == 4

    previous_leads = read(R / "captures/integration-nominal-stock-overlap-leads.json")
    by_proposal = {p["proposal_id"]: p for p in proposals}
    groups = {name: [{"proposal_id": item["proposal_id"], "after_capture": by_proposal[item["proposal_id"]]["after_capture"]} for item in members] for name, members in previous_leads["groups"].items()}
    staged = subprocess.check_output(["git", "diff", "--cached", "--name-status", BASE]).decode().splitlines()
    staged_payloads = []
    for row in staged:
        status, path = row.split("\t", 1)
        assert status == "A" and (path.startswith(str(R) + "/") or path in native_hashes), row
        data = subprocess.check_output(["git", "show", ":" + path])
        staged_payloads.append({"path": path, "index_sha256": hashlib.sha256(data).hexdigest()})
    staged_modes = subprocess.check_output(["git", "diff", "--cached", "--raw", BASE]).decode().splitlines()
    assert all(row.split()[1] == "100644" for row in staged_modes)
    outside_changes = [path for path in subprocess.check_output(["git", "diff", "--name-only"]).decode().splitlines() if not (path.startswith(str(R) + "/") or path in native_hashes)]
    assert not outside_changes

    pinned = ["decisions.json", "evidence.json", "proposals.json", "parts/root-assemble.py", "parts/root-attach-reviews.py", "parts/root-validate-proposals.py", "parts/root-cross-shard-dependencies.py", "parts/root-decision-deltas.json", "parts/root-nominal-stock-proposals.json", "cross-shard-dependencies.json", "logs/final-proposal-validation.json", "logs/final-owner-schema.log", "captures/root-maintained-baseline-hashes.json", "captures/integration-review-initial.json", "captures/integration-review-followup-01.json", "captures/integration-stock-primary-locators.json", "captures/integration-stock-deltas-final.json", "captures/integration-native-wrapper-finding.json", "captures/integration-nominal-stock-overlap-leads.json", args.audit, args.integrity]
    pinned.extend(path for _, path, _, _, _ in primary_receipts)
    result = {
        "reviewer": "/root/integration_reviewer", "reviewed_at": datetime.now(timezone.utc).isoformat(),
        "status": "complete_for_declared_integration_scope", "independence": "No A/B/C primary proposal, root nominal-stock delta, combined owner payload or native review was authored by this reviewer. Reviewer authored only integration findings, checks and receipts.",
        "scope": ["All 188 frozen-case membership, occurrence/source/owner preservation and author-to-final transforms", "100 final proposal payload hashes, native validation linkage, composition/identity boundaries and nominal-stock overlap scan", "Manual baseline-relative review of four existing-owner combined synonym/history/evidence payloads", "Independent primary-capture science review of four root nominal-stock decisions/payloads and one consolidated JCM900/JCM979 Hutner preparation", "Actual 70/70/48 skeptical receipts, shared-payload independence boundaries, 77-owner native-wrapper scope and initial staged artifact boundaries"],
        "base_revision": BASE, "input_hashes": {p: sha(R / p) for p in pinned}, "native_review_hashes": native_hashes,
        "authoritative_native_review": str(native_dir / "review.yaml"),
        "counts": {"cases": len(decisions), "evidence_entries": len(evidence), "proposal_payloads": len(proposals), "independently_checked_evidence_captures": integrity["unique_checked_evidence_capture_count"], "current_maintained_owner_targets": len(owner_paths), "owner_referencing_source_cases": sum(bool(d["owner_records"]) for d in decisions), "baseline_files_unchanged": len(baseline["files"]), "existing_catalogue_record_count": validator["existing_catalogue_record_count"], "existing_catalogue_unique_identifier_count": validator["existing_catalogue_unique_identifier_count"]},
        "primary_independent_review_coverage": coverage,
        "author_to_final_changed_field_groups": [{"changed_fields": list(fields), "case_count": count} for fields, count in collections.Counter(tuple(c["changed_fields"]) for c in integrity["cases"]).items()],
        "shared_source_and_payload_review": {"A8": "C reviews source applicability; B reviews C-P10 payload; unresolved other occurrences remain", "A55": "C reviews source applicability; B reviews C-P01 payload", "C156": "B reviews source applicability; A reviews B122 payload", "A35_A38_A47_B110": "Original source-case reviewers plus this independent review of final combined Hutner payload"},
        "combined_existing_owner_reviews": combined,
        "root_scientific_delta_receipt": {"path": "captures/integration-stock-deltas-final.json", "sha256": sha(R / "captures/integration-stock-deltas-final.json"), "all_four_final_scientific_field_hashes_match": True, "all_five_final_payload_hashes_match": True},
        "final_payloads": [{"proposal_id": p["proposal_id"], "kind": p["kind"], "owner_path": p["owner_path"], "before_sha256": p["before_sha256"], "after_capture": p["after_capture"], "case_ids": p["case_ids"]} for p in proposals],
        "native_scope_assessment": "Successor accurately identifies five confirmed resolving-synonym defects while retaining unresolved source identities. Both saved versions retain all hash-bound inputs. Native wrapper identifies itself as root self-review of bounded source-to-owner comparisons; it is not independent full-owner or export approval. Source-only cases have no invented native owner.",
        "resolved_findings": [
            {"id": "INTEGRATION-01", "resolution": "Verified same nine-input JCM900/JCM979 stock consolidated once, retaining both primary provenance sets, malformed molybdate string and approximate KOH quantity."},
            {"id": "INTEGRATION-02", "resolution": "Validation receipt separately labels 2956 catalogue records and 2862 unique identifiers; prior mislabeled preliminary receipt retained."},
            {"id": "INTEGRATION-03", "resolution": "Four concrete source-qualified nominal stocks and explicitly guarded decision deltas independently reviewed; missing form/solvent/percent details remain UNKNOWN."},
            {"id": "INTEGRATION-04", "resolution": "Successor native wrapper records fifth confirmed Sodium_Malate DL-alias conflict while retaining source salt-stoichiometry uncertainty; initial review/finding preserved."},
        ],
        "nominal_stock_reconciliation_candidates": groups,
        "coordinator_requirements": ["100 proposal payloads are not 100 established chemically distinct substances. Reconcile nominal 0.1 M HCl, 0.1 M Tris pH 7.5, 1 N NaOH and 5% cysteine-HCl-monohydrate contexts before minting/applying every owner. Unknown complete preparation supports neither automatic identity nor distinctness.", "Reconcile all cross-shard owner proposals against frozen original before hashes; the dependency scan is only direct-owner/exact-label scope and cannot establish chemical dependency absence.", "Retain every source-specific missing requirement, original units/occurrences, malformed formula, supplied-form distinction, native WITHHOLD/REJECTED gate and original capture time.", "Any future guarded integration must withdraw changed-owner support, synchronize native surfaces and revalidate/review complete published payloads; this worker performs no maintained edit, merge, downstream rebuild or export."],
        "staged_review": {"scope": "Initial staged snapshot before final handoff/scopes/manifest accounting metadata; all additions regular 100644 files under worker artifact root or the exact two native review pairs.", "file_count": len(staged), "index_files": staged_payloads, "maintained_or_external_path_changes": []},
        "limitations": ["This is independent integration review, not a third fresh primary-source research pass for all 188 cases. Actual separate per-case scientific reviews are the pinned A/B/C receipts.", "Successful structural/schema/capture checks do not establish scientific identity, complete owner support or release approval.", "Final handoff/scopes/progress/manifest and final index metadata are verified separately after this receipt; no future unknown file mutation is approved."],
    }
    output.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps({"path": str(output), "sha256": sha(output), "status": result["status"], "counts": result["counts"]}))


if __name__ == "__main__":
    main()
