#!/usr/bin/env python3
"""Prepared Step 3 dependency chain. Default: print the plan; never auto-apply.

Root must separately apply/review sources, promote the bounded canonical rows,
publish the three-owner mapping receipt and advance REVIEWED_SOURCE. This driver
does not do those operations, edit selectors, rebuild unified, or mutate Git.
"""

from __future__ import annotations

import argparse
import ast
import csv
import datetime
import hashlib
import io
import json
import re
import subprocess
import sys
from collections import Counter
from pathlib import Path

HERE = Path(__file__).resolve().parent
RUN = HERE.parent
ROOT = RUN / "step3-mim"
HELPER = RUN / "run_step3_mim.py"
BASE = "99fe4b44d78126d78041a69eeb366c52bedf0caa"
CANONICAL = "mappings/ingredient_mappings.sssom.tsv"
MAPPING_REVIEW = "reports/sssom_completion_20260921/review.json"
ASSEMBLER = "reports/sssom_completion_20260921/assemble_review.py"
SEMANTIC = "reports/semantic_review_20260921/resolution"
SEMANTIC_REVIEW = SEMANTIC + "/current-review.json"
FULL = "output/mim-kgx-710-full"  # This exact path is rebuilt by existing CI.
REVIEWED = "output/mim-reviewed-sssom"
SUPPORTED = "output/step3-supported-kgx"
COMPANION = "output/step3-ingredient-bundle"
PRIOR = "reports/ingredient_bundle_20261101_ncit875/review.json"
NEXT = "reports/ingredient_bundle_20261101_carnitine1004"
NLDM = "data/ingredients/mapped/NLDM_metabolites.yaml"
SALT = "data/ingredients/mapped/Carnitine_Hydrochloride.yaml"
TOMBSTONE = "data/ingredients/mapped/Carnitine_Dl_Hydrochloride.yaml"


def require(condition, message):
    if not condition:
        raise ValueError(message)


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def read(path):
    return json.loads(Path(path).read_bytes())


def rows(path, *, sssom=False):
    content = Path(path).read_text()
    if sssom:
        content = "".join(line for line in content.splitlines(keepends=True) if not line.startswith("#"))
    return list(csv.DictReader(io.StringIO(content), delimiter="\t"))


def uv(*args):
    return ["uv", "run", "--frozen", "python", *args]


def build_commands():
    return [
        ("canonical-qc", ["just", "qc-sssom"]),
        ("assemble-review", uv(ASSEMBLER)),
        ("reviewed-export", ["just", "export-reviewed-sssom", MAPPING_REVIEW, REVIEWED]),
        ("reviewed-qc", ["just", "qc-reviewed-sssom", MAPPING_REVIEW, REVIEWED]),
        ("full-kgx", ["just", "export-kgx", FULL]),
        ("semantic-build", uv(SEMANTIC + "/build_review.py", "--bundle", FULL)),
        ("semantic-integrity", uv("-m", "mediaingredientmech.validation.semantic_release", "--root", ".", "--report", SEMANTIC_REVIEW)),
        ("supported-export", ["just", "export-supported-kgx", SEMANTIC_REVIEW, SUPPORTED]),
        ("supported-qc", ["just", "qc-supported-kgx", SEMANTIC_REVIEW, SUPPORTED]),
        ("supported-sssom-schema", uv("-c", "from sssom.parsers import parse_sssom_table; from sssom.validators import SchemaValidationType, validate; validate(parse_sssom_table('" + SUPPORTED + "/ingredient_mappings.sssom.tsv'), validation_types=[SchemaValidationType.JsonSchema, SchemaValidationType.PrefixMapCompleteness, SchemaValidationType.StrictCurieFormat])")),
        ("companion-refresh", uv("scripts/refresh_unchanged_cohort.py", "--baseline", BASE, "--prior-review", PRIOR, "--output", NEXT + "/review.json", "--receipt", NEXT + "/dependency-refresh.json", "--prior-copy", NEXT + "/prior-review.json")),
        ("companion-export", uv("-m", "mediaingredientmech.export.ingredient_bundle", "export", "--review", NEXT + "/review.json", "--output", COMPANION)),
        # The validator command is added only after reading the actual new manifest.
    ]


def gate_commands():
    tests = [
        "tests/test_merge_carnitine_hydrochloride.py",
        "tests/test_carnitine_occurrence_routing.py",
        "tests/test_carnitine_merge_dependencies.py",
        "tests/test_mapping_change_receipt.py",
        "tests/test_reviewed_sssom.py",
        "tests/test_semantic_review_builder.py",
        "tests/test_semantic_mapping_review.py",
        "tests/test_ingredient_bundle.py",
        "tests/test_ingredient_bundle_dependency_refresh.py",
        "tests/test_unified_rejections.py",
        "tests/test_unified_source_holds.py",
    ]
    return [
        ("receipt-regression-tests", uv("-m", "pytest", "-q", "-o", "addopts=", "-p", "no:cacheprovider", *tests)),
        ("full-qc", ["just", "qc"]),
        ("curies-and-product-labels", ["just", "curie-validate", "validate-products"]),
        ("unified-gates", ["just", "check-unified-rejections", "check-unified-freshness"]),
        ("full-suite", uv("-m", "pytest", "-q", "-o", "addopts=", "-p", "no:cacheprovider")),
    ]


def protected_inputs():
    plan = read(HERE / "prepared-inputs.json")
    require(sha(HELPER) == plan["orchestration_helper"]["sha256"], "Run environment helper changed; review before proceeding")
    for path, expected in plan["protected_inputs"].items():
        require(sha(ROOT / path) == expected, "Protected source changed: " + path)
    require(sha(HERE / "nldm-before.json") == plan["frozen_baseline_sha256"], "Baseline proof changed")
    return plan


def prerequisite_receipts(args):
    plan = protected_inputs()
    require(args.source_log and args.mapping_receipt, "build requires --source-log and --mapping-receipt from root's completed publication")
    subprocess.run(["git", "merge-base", "--is-ancestor", BASE, "HEAD"], cwd=ROOT, check=True)
    branch = subprocess.check_output(["git", "branch", "--show-current"], cwd=ROOT, text=True).strip()
    require(branch == plan["branch"], "Unexpected work branch")
    source_path = Path(args.source_log).expanduser().resolve()
    receipt_path = (ROOT / args.mapping_receipt).resolve()
    require(receipt_path.is_relative_to(ROOT / "reports/sssom_completion_20260921/mapping_changes"), "Mapping receipt must be a native published chain member")
    source, receipt = read(source_path), read(receipt_path)
    require(source.get("phase") == "sources" and source.get("state") == "complete" and source.get("applied") is True, "Source transaction is incomplete")
    require(str(source.get("approval", "")).startswith("NONE"), "Source transaction cannot grant release approval")
    by_owner = {r["source_record"]: r for r in source["records"]}
    require(len(source["records"]) == 3 and set(by_owner) == {SALT, TOMBSTONE, NLDM}, "Source receipt must bind all three owners exactly")
    for owner, record in by_owner.items():
        require(record["before_yaml_sha256"] == plan["inputs"][owner], "Wrong owner preimage: " + owner)
        require(record["after_yaml_sha256"] == sha(ROOT / owner), "Stale owner afterimage: " + owner)
    for path, expected in source["output_sha256"].items():
        require(sha(ROOT / path) == expected, "Source output changed: " + path)
    require(receipt["records"] == source["records"], "Mapping receipt must preserve the exact three-owner receipt context")
    require(receipt["sequence"] == 17 and receipt["before_sha256"] == plan["inputs"][CANONICAL], "Unexpected mapping chain base; stop for root review")
    require(receipt["after_sha256"] == sha(ROOT / CANONICAL), "Receipt does not bind current canonical bytes")
    require(str(receipt.get("approval", "")).startswith("NONE"), "Mapping receipt cannot grant approval")
    source_tree = ast.parse((ROOT / ASSEMBLER).read_text())
    pin = next(ast.literal_eval(node.value) for node in source_tree.body if isinstance(node, ast.Assign) and any(isinstance(target, ast.Name) and target.id == "REVIEWED_SOURCE" for target in node.targets))
    require(pin == sha(ROOT / CANONICAL), "Root must advance REVIEWED_SOURCE to the verified promoted canonical SHA")
    require(receipt["after_row_count"] == receipt["before_row_count"] - 4, "Expected five reviewed salt rows replaced by one")
    return {"source_log": str(source_path), "source_log_sha256": sha(source_path), "mapping_receipt": str(receipt_path.relative_to(ROOT)), "mapping_receipt_sha256": sha(receipt_path)}


def verify_outputs():
    protected_inputs()
    before = read(HERE / "nldm-before.json")
    mapping = read(ROOT / MAPPING_REVIEW)
    counts = Counter(row["disposition"] for row in mapping["decisions"])
    require(counts == {"SUPPORTED": 1739, "WITHHOLD": 1243}, "Unexpected complete mapping partition; no broader approval changes authorized")
    nldm_mapping = [row for row in mapping["decisions"] if row["owner_record"] == NLDM]
    salt_mapping = [row for row in mapping["decisions"] if row["owner_record"] == SALT]
    require(len(nldm_mapping) == 1 and nldm_mapping[0]["disposition"] == "WITHHOLD", "NLDM mapping approval was not withdrawn")
    require(len(salt_mapping) == 1 and salt_mapping[0]["disposition"] == "WITHHOLD", "New NCIT salt row requires fresh mapping-specific approval")
    require(not any(row["owner_record"] == TOMBSTONE for row in mapping["decisions"]), "Rejected duplicate still owns a canonical row")
    canonical = rows(ROOT / CANONICAL, sssom=True)
    corrected = canonical[salt_mapping[0]["source_position"] - 1]
    require((corrected["subject_id"], corrected["object_id"], corrected["predicate_id"]) == ("MIM:Carnitine_Hydrochloride", "NCIT:C216679", "skos:exactMatch"), "Wrong promoted salt identity")
    subject = before["mapping_row"]["subject_id"]
    decisions = rows(ROOT / SEMANTIC / "assertion-dispositions.tsv")
    nldm_after = [row for row in decisions if row["source_record"] == NLDM]
    key = lambda row: (row["assertion_type"], row["source_position"])
    old, new = ({key(row): row for row in group} for group in (before["nonmapping_dispositions"], nldm_after))
    require(set(old) == set(new) and len(new) == 68, "NLDM nonmapping cohort changed")
    require(all(row["resolution_status"] == "OPEN" for row in new.values()), "A stale NLDM nonmapping approval survived")
    require(all(row["source_record_sha256"] == sha(ROOT / NLDM) != before["owner_sha256"] for row in new.values()), "NLDM dispositions are not bound to changed current owner")
    changed = [k for k in old if old[k]["assertion_sha256"] != new[k]["assertion_sha256"]]
    require(changed == [("component", "59")], "NLDM payload scope exceeded component 59")
    mapping_position = str(nldm_mapping[0]["source_position"])
    semantic_mapping = [row for row in decisions if row["assertion_type"] == "mapping" and row["source_position"] == mapping_position]
    require(len(semantic_mapping) == 1 and semantic_mapping[0]["resolution_status"] == "OPEN", "NLDM graph mapping approval survived")
    def is_nldm(edge):
        return edge["source_record"] == NLDM or (edge["assertion_type"] == "mapping" and json.loads(edge["assertion_json"])["subject_id"] == subject)
    supported = rows(ROOT / SUPPORTED / "mim_edges.tsv")
    require(not any(is_nldm(edge) for edge in supported), "Supported graph still publishes a withdrawn NLDM claim")
    backlog = read(ROOT / SUPPORTED / "unsupported-backlog.json")
    require(sum(is_nldm(item["edge"]) for item in backlog["assertions"]) == 69, "Backlog does not preserve all 69 withdrawn NLDM claims")
    semantic = read(ROOT / SEMANTIC_REVIEW)
    require(semantic["release_verdict"] == "FAIL", "Do not claim full scientific release from an integrity pass")
    audit = read(ROOT / NEXT / "dependency-refresh.json")
    require(audit["scientific_approval_added"] is False, "Companion refresh added scientific approval")
    require(audit["claim_counts"] == {"mapping": 20, "identifier": 18, "product": 3, "occurrence": 10}, "Companion claim cohort changed")
    require(len(audit["owner_hashes_unchanged"]) == 20, "Companion owner cohort changed")
    require(not ({SALT, TOMBSTONE, NLDM} & set(audit["owner_hashes_unchanged"])), "Changed owners entered unchanged companion cohort")
    require((ROOT / NEXT / "prior-review.json").read_bytes() == (ROOT / PRIOR).read_bytes(), "Prior companion was not preserved byte-for-byte")
    require(read(ROOT / NEXT / "review.json")["decisions"] == read(ROOT / PRIOR)["decisions"], "Companion approval decisions changed")
    movements = sum(item["base_decision_locations"]["before"] != item["base_decision_locations"]["after"] for item in audit["selected_mapping_evidence_unchanged"])
    return {"mapping_rows": len(canonical), "mapping_counts": dict(counts), "nldm_approvals_withdrawn": 69, "nldm_unchanged_nonmapping_payloads": 67, "nldm_changed_payload": list(changed[0]), "semantic_assertions": len(decisions), "semantic_status_counts": dict(Counter(row["resolution_status"] for row in decisions)), "full_scientific_release": semantic["release_verdict"], "blocking_findings": len(semantic["blocking_finding_ids"]), "blocking_assertions": len(semantic["blocking_assertion_ids"]), "companion_claims": 51, "companion_owners": 20, "companion_relocated_mapping_decisions": movements, "companion_manifest_sha256": sha(ROOT / COMPANION / "manifest.json")}


def require_selectors():
    plans = read(HERE / "planned-repository-paths.json")["root_only_selector_updates"]
    for path in (".github/workflows/qc-reviewed-sssom.yaml", "tests/test_ingredient_bundle.py"):
        old = subprocess.check_output(["git", "show", BASE + ":" + path], cwd=ROOT)
        require(hashlib.sha256(old).hexdigest() == plans[path]["before_sha256"], "Selector baseline changed")
        require(old.count(PRIOR.encode()) == 1, "Unexpected selector occurrence count")
        require((ROOT / path).read_bytes() == old.replace(PRIOR.encode(), (NEXT + "/review.json").encode()), "Root must apply only the exact companion selector advance: " + path)
    docs = (ROOT / "docs/INGREDIENT_BUNDLE.md").read_text()
    require(NEXT + "/review.json" in docs and NEXT + "/README.md" in docs, "Public companion documentation still selects the old cohort")
    require((ROOT / NEXT / "README.md").is_file(), "Root must document the unchanged cohort and measured locator shifts")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("stage", nargs="?", choices=("plan", "build", "verify", "gates"), default="plan")
    parser.add_argument("--execute", action="store_true", help="Root-reviewed execution only; omitted means print commands without any write")
    parser.add_argument("--tag", help="Unique log suffix, e.g. step3-chain-v1")
    parser.add_argument("--source-log")
    parser.add_argument("--mapping-receipt", help="Published native receipt path relative to step3-mim")
    args = parser.parse_args()
    if not args.execute or args.stage == "plan":
        print(json.dumps({"executed": False, "build": build_commands(), "after_companion_export": "native validate with SHA256 of the actual new manifest.json", "root_between_stages": "Review receipts/counts; advance exact test/CI/docs selectors; refresh flat exports and visualization metadata; rebuild/stamp/verify unified using merged Claw; update release counts from actual results.", "gates": gate_commands(), "scope": read(HERE / "planned-repository-paths.json")}, indent=2))
        return
    require(args.tag and re.fullmatch(r"[a-zA-Z0-9][a-zA-Z0-9._-]*", args.tag), "Execution requires a unique safe --tag")
    protected_inputs()
    context = prerequisite_receipts(args) if args.stage == "build" else {}
    if args.stage == "build":
        for path in (REVIEWED, FULL, SUPPORTED, COMPANION, NEXT):
            require(not (ROOT / path).exists() and not (ROOT / path).is_symlink(), "Output already exists; preserve and review rather than overwrite: " + path)
    if args.stage == "gates":
        require_selectors()
        context["verified_outputs"] = verify_outputs()
    execution = HERE / "executions" / (args.tag + "-" + args.stage)
    execution.mkdir(parents=True, exist_ok=False)
    def save(name, value):
        with (execution / name).open("x") as stream:
            json.dump(value, stream, indent=2); stream.write("\n")
    save("start.json", {"started_at": datetime.datetime.now(datetime.timezone.utc).isoformat(), "stage": args.stage, "context": context})
    def run(name, command):
        log_name = args.tag + "-" + name
        for suffix in (".log", ".json"):
            require(not (RUN / "logs" / (log_name + suffix)).exists(), "Log already exists: " + log_name)
        with (execution / "commands.jsonl").open("a") as stream:
            stream.write(json.dumps({"name": log_name, "argv": command}) + "\n")
        subprocess.run([sys.executable, str(HELPER), "step3-mim", log_name, "--", *command], check=True)
    if args.stage == "build":
        backups = execution / "before"; backups.mkdir()
        for relative in read(HERE / "planned-repository-paths.json")["chain_rewrites"]:
            destination = backups / relative; destination.parent.mkdir(parents=True, exist_ok=True)
            with destination.open("xb") as stream:
                stream.write((ROOT / relative).read_bytes())
        for name, command in build_commands():
            if name == "companion-refresh":
                (ROOT / NEXT).mkdir(exist_ok=False)
            run(name, command)
        actual = sha(ROOT / COMPANION / "manifest.json")
        run("companion-validate", uv("-m", "mediaingredientmech.export.ingredient_bundle", "validate", COMPANION, "--manifest-sha256", actual))
        save("verified-output.json", verify_outputs())
    elif args.stage == "verify":
        save("verified-output.json", verify_outputs())
    elif args.stage == "gates":
        for name, command in gate_commands():
            run(name, command)
        save("verified-output.json", verify_outputs())
    protected_inputs()
    save("complete.json", {"complete": True, "stage": args.stage, "finished_at": datetime.datetime.now(datetime.timezone.utc).isoformat(), "canonical_sha256": sha(ROOT / CANONICAL)})


if __name__ == "__main__":
    main()
