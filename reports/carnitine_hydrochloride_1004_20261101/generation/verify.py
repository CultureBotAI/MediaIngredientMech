#!/usr/bin/env python3
"""Read-only verification of the portable #1004 generation captures."""

from __future__ import annotations

import argparse
import csv
import gzip
import hashlib
import io
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent


def require(condition, message):
    if not condition:
        raise ValueError(message)


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def read(path):
    return json.loads(path.read_bytes())


def table(raw, *, metadata):
    content = raw.decode()
    if metadata:
        lines = content.splitlines(keepends=True)
        while lines and lines[0].startswith("#"):
            lines.pop(0)
        content = "".join(lines)
    return list(csv.DictReader(io.StringIO(content), delimiter="\t"))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repository", type=Path, help="Optionally verify referenced maintained evidence against this repository")
    parser.add_argument("--originals", action="store_true", help="Optionally verify all captured original source files still match")
    args = parser.parse_args()
    manifest = read(HERE / "manifest.json")
    files = manifest["files"]
    actual = {str(path.relative_to(HERE)) for path in HERE.rglob("*") if path.is_file()}
    require(actual == set(files) | {"manifest.json"}, "Package file set differs from manifest")
    for relative, entry in files.items():
        path = HERE / relative
        require(not path.is_symlink() and path.resolve().is_relative_to(HERE), "Unsafe archive path")
        raw = path.read_bytes()
        require(len(raw) == entry["bytes"] and sha(raw) == entry["sha256"], "Archive hash differs: " + relative)
    sources = {}
    for entry in manifest["sources"]:
        archived = (HERE / entry["archive_path"]).read_bytes()
        require(sha(archived) == entry["archive_sha256"] and len(archived) == entry["archive_bytes"], "Source archive binding differs")
        require(entry["encoding"] in {"identity", "gzip"}, "Unknown archive encoding")
        raw = gzip.decompress(archived) if entry["encoding"] == "gzip" else archived
        require(sha(raw) == entry["raw_sha256"] and len(raw) == entry["raw_bytes"], "Decoded source hash differs: " + entry["source_path"])
        require(entry["source_path"] not in sources, "Duplicate original source identity")
        sources[entry["source_path"]] = raw
        if args.originals:
            require(Path(entry["source_path"]).read_bytes() == raw, "Original source changed: " + entry["source_path"])

    original_run = manifest["original_roots"]["run"]
    original_mim = manifest["original_roots"]["mim"]

    def source(root, relative):
        key = str(Path(root) / relative)
        require(key in sources, "Missing original source capture: " + key)
        return sources[key]

    def original_json(root, relative):
        return json.loads(source(root, relative))

    frozen = HERE / "analyzer-1039"
    frozen_index = read(frozen / "evidence-index.json")
    require(sha((frozen / "evidence-index.json").read_bytes()) == manifest["frozen_analyzer_index_sha256"], "Frozen #1039 index changed")
    require({str(path.relative_to(frozen)) for path in frozen.rglob("*") if path.is_file()} == set(frozen_index["files"]) | {"evidence-index.json"}, "Frozen #1039 file set changed")
    for relative, entry in frozen_index["files"].items():
        require(sha((frozen / relative).read_bytes()) == entry["sha256"], "Frozen #1039 evidence changed")
    preparation = HERE / "native-chain/plan"
    for relative, entry in read(preparation / "evidence-index.json")["files"].items():
        require(sha((preparation / relative).read_bytes()) == entry["sha256"], "Frozen native-chain preparation changed")

    for command in read(HERE / "command-index.json"):
        receipt = original_json(original_run, "logs/" + command["name"] + ".json")
        require(receipt["exit_code"] == command["exit_code"], "Command exit status changed")
        require(receipt["log"] in sources and sha(sources[receipt["log"]]) == receipt["log_sha256"] == command["original_log_sha256"], "Command log is not receipt-bound")
    build = original_json(original_run, "step3-native-chain-plan/executions/step3-chain-v1-build/complete.json")
    require(build["complete"] is True, "Native build not complete")
    summary = read(HERE / "summary.json")
    candidate = source(original_mim, "output/step3-native-candidate/candidate.sssom.tsv")
    generation = original_json(original_mim, "output/step3-native-candidate/generation-receipt.json")
    require(len(table(candidate, metadata=True)) == summary["native_diagnostic_rows"] == 2975, "Wrong diagnostic population")
    require(sha(candidate) == generation["candidate_sha256"] == summary["native_diagnostic_sha256"], "Candidate provenance hash differs")
    require(generation["producer_revision"] == summary["producer_revision"] == "6a7172585eb68da7f4fe01aee75a82458ddd470c", "Wrong producer identity")
    before_inputs = source(original_mim, "output/step3-native-candidate/inputs-before.json")
    require(before_inputs == source(original_mim, "output/step3-native-candidate/inputs-after.json"), "Candidate input bytes drifted")
    require(sha(before_inputs) == generation["input_manifest_sha256"], "Candidate input manifest changed")
    require(sha(source(original_run, "generate_candidate.py")) == generation["harness_sha256"], "Generation harness does not match receipt")
    require(len(generation["label_maps"]) == 4, "Missing label-map receipts")
    for name, digest in generation["label_maps"].items():
        require(sha(source(original_mim, "output/step3-native-candidate/" + name)) == digest, "Label-map receipt changed")
    require(generation["scientific_approval_added"] is False and generation["supervisor_binding"] is None, "Generation cannot add approval or invent binding")
    for directory, expected_rows in (("output/step3-native-candidate/native-invariants", 2975), ("output/step3-canonical-native-invariants", 2982)):
        receipt = original_json(original_mim, directory + "/receipt.json")
        require(receipt["exit_code"] == 0 and receipt["rows"] == expected_rows, "Invariant execution differs")
        require(table(source(original_mim, directory + "/rejects.tsv"), metadata=True) == [], "Invariant rejects were not empty")

    analysis = original_json(original_run, "logs/step3-final-data-comparison-after-1039.log")
    require(analysis["canonical"] == summary["canonical"] and analysis["unified"] == summary["unified"] and analysis["reviews"] == summary["reviews"], "Summary differs from corrected analysis")
    unified = source(original_run, "step3-unified-evidence-v2/unified-candidate.tsv")
    prior_unified = source(original_run, "step3-unified-evidence-v2/unified-before.tsv")
    publication = original_json(original_run, "step3-unified-evidence-v2/unified-generation-receipt.json")
    require(sha(prior_unified) == publication["before_sha256"] and sha(unified) == publication["after_sha256"] == analysis["unified"]["sha256"], "Unified publication byte chain differs")
    require(publication["applied"] is True and publication["state"] == "complete" and publication["transaction"]["applied"] is True, "Unified publication is not completed")
    require(publication["transaction"]["changed"] == [str(Path(original_mim) / "UNIFIED_INGREDIENT_MAPPING.tsv")], "Unexpected unified transaction mutation scope")
    require(publication["transaction"]["journal"] in sources, "Native publication journal is missing")
    unified_rows = table(unified, metadata=False)
    require(len(unified_rows) == 4170 and sum(int(row["occurrence_count"]) for row in unified_rows) == 209330, "Plain unified TSV population changed")
    require({row["ingredient_name"]: int(row["occurrence_count"]) for row in unified_rows if row["ingredient_name"].startswith("#")} == {"#N2": 3, "#N2O": 2, "#argon": 1, "#Ar": 1}, "Hash-prefixed data rows are missing")
    require(analysis["unified"]["changed_rows"] == 1 and analysis["reviews"]["nldm_approvals_withdrawn"] == 69 and analysis["reviews"]["companion_claims"] == 51, "Bounded analysis changed")

    reviewed = original_json(original_mim, "output/mim-reviewed-sssom/manifest.json")
    full = original_json(original_mim, "output/mim-kgx-710-full/manifest.json")
    supported = original_json(original_mim, "output/step3-supported-kgx/manifest.json")
    companion_bytes = source(original_mim, "output/step3-ingredient-bundle/manifest.json")
    require(reviewed["counts"] == {"source": 2982, "supported": 1739, "withhold": 1243}, "Reviewed partition differs")
    require(reviewed["source_sha256"] == analysis["canonical"]["canonical_sha256"], "Reviewed SSSOM does not bind canonical bytes")
    require(full["counts"]["edges"] == 4487 and full["counts"]["sssom_rows"] == 2982, "Complete graph counts changed")
    require(supported["release_verdict"] == "PASS" and supported["full_release_verdict"] == "FAIL", "Subset/full scientific boundaries changed")
    require(supported["counts"]["edges"] == 2151 and supported["counts"]["backlog_unapproved_edges"] == 2336, "Supported/backlog counts changed")
    require(sha(companion_bytes) == analysis["reviews"]["companion_manifest_sha256"] and len(json.loads(companion_bytes)["cohort"]) == 20, "Companion manifest changed")
    omissions = summary["inherited_aggregate_limitations"]["records"]
    require(len(omissions) == 8 and all(row["fields"] == ["discussions"] and row["individual_and_aggregate_unchanged_from_base"] for row in omissions), "Inherited aggregate scope limitation changed")
    require(summary["scientific_approval_added"] is False and summary["supervisor_binding"] is None, "Package cannot grant approval or invent bindings")
    if args.repository:
        repository = args.repository.resolve()
        for reference in manifest["references"]:
            raw = (repository / reference["repository_path"]).read_bytes()
            require(sha(raw) == reference["sha256"] and len(raw) == reference["bytes"], "Referenced maintained evidence differs")
    print(json.dumps({"archive_integrity": "PASS", "files": len(files), "captured_source_identities": len(sources), "diagnostic_rows": 2975, "canonical_rows": 2982, "unified_rows": 4170, "occurrences": 209330, "nldm_approvals_withdrawn": 69, "companion_claims_unchanged": 51, "full_scientific_release": "FAIL", "inherited_aggregate_discussion_omissions": 8, "writes_performed": False}, indent=2))


if __name__ == "__main__":
    main()
