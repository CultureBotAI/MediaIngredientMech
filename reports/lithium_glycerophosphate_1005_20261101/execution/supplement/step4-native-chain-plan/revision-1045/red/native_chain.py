#!/usr/bin/env python3
"""Bounded Step 4 chain. Plan/preflight/verify are read-only; mutations need --execute.

Source application, canonical promotion, receipt creation, source pin, selectors,
unified rebuild/stamp, Git and publication remain explicit supervisor operations.
This harness author is not the independent Step 4 reviewer.
"""
from __future__ import annotations

import argparse
import ast
from collections import Counter
import csv
import datetime
from functools import lru_cache
import hashlib
import io
import json
from pathlib import Path
import re
import subprocess
import sys

import yaml

HERE = Path(__file__).resolve().parent
RUN = HERE.parent
ROOT = RUN / "step4-mim"
HELPER = RUN / "run_step4_mim.py"
BASE = "838d0c2627552b0094545ebb580b5bb9b1a84d57"
PLAN_SHA = "6f252116a6ed7cc90d9e7769fdd4311c95a7edfef029486f4077634384b0c774"
OWNER = "data/ingredients/mapped/Sn-Glycerol_3-phosphate_Lithium_Salt.yaml"
SUBJECT = "MIM:Sn-Glycerol_3-phosphate_Lithium_Salt"
IDENTITY = "kgmicrobe.compound:sn-glycerol_3-phosphate_lithium_salt"
CANONICAL = "mappings/ingredient_mappings.sssom.tsv"
BASELINE = "mappings/other_cross_record_baseline.tsv"
MAPPING = "reports/sssom_completion_20260921/review.json"
ASSEMBLER = "reports/sssom_completion_20260921/assemble_review.py"
RECEIPTS = "reports/sssom_completion_20260921/mapping_changes"
SEMANTIC = "reports/semantic_review_20260921/resolution"
SEMANTIC_REVIEW = SEMANTIC + "/current-review.json"
ASSERTIONS = SEMANTIC + "/assertion-dispositions.tsv"
FINDINGS = SEMANTIC + "/finding-dispositions.tsv"
PRIOR = "reports/ingredient_bundle_20261101_carnitine1004/review.json"
NEXT = "reports/ingredient_bundle_20261101_lithium1005"
FULL = "output/mim-kgx-710-full"  # Existing native CI rebuild path.
REVIEWED = "output/mim-reviewed-sssom"
SUPPORTED = "output/step4-supported-kgx"
COMPANION = "output/step4-ingredient-bundle"
TARGET_KEYS = {(SUBJECT, "skos:broadMatch", "CHEBI:15978"), (SUBJECT, "skos:exactMatch", IDENTITY)}


def require(condition, message):
    if not condition:
        raise ValueError(message)


def digest(payload):
    return hashlib.sha256(payload).hexdigest()


def payload(path):
    path = Path(path)
    require(path.is_file() and not path.is_symlink(), "Missing/nonregular input: " + str(path))
    return path.read_bytes()


def sha(path):
    return digest(payload(path))


def read(path):
    return json.loads(payload(path))


def git(*args):
    return subprocess.check_output(["git", *args], cwd=ROOT)


@lru_cache(maxsize=None)
def base(path):
    return git("show", BASE + ":" + path)


def table(content, *, sssom=False):
    """Only an SSSOM metadata prelude is metadata; plain # labels remain data."""
    lines = content.decode().splitlines(keepends=True)
    metadata = []
    if sssom:
        while lines and lines[0].startswith("#"):
            metadata.append(lines.pop(0))
    reader = csv.DictReader(io.StringIO("".join(lines)), delimiter="\t")
    result = list(reader)
    require(reader.fieldnames and all(None not in row for row in result), "Malformed TSV")
    return metadata, reader.fieldnames, result, lines


def rows(content, *, sssom=False):
    return table(content, sssom=sssom)[2]


def key(row):
    return tuple(row[c] for c in ("subject_id", "predicate_id", "object_id"))


def indexed(items, key_fn):
    result = {key_fn(item): item for item in items}
    require(len(result) == len(items), "Duplicate comparison key")
    return result


def without(item, *fields):
    return {k: v for k, v in item.items() if k not in fields}


def uv(*args):
    return ["uv", "run", "--frozen", "python", *args]


def commands():
    return [
        ("canonical-qc", ["just", "qc-sssom"]),
        ("assemble-review", uv(ASSEMBLER)),
        ("reviewed-export", ["just", "export-reviewed-sssom", MAPPING, REVIEWED]),
        ("reviewed-qc", ["just", "qc-reviewed-sssom", MAPPING, REVIEWED]),
        ("full-kgx", ["just", "export-kgx", FULL]),
        ("semantic-build", uv(SEMANTIC + "/build_review.py", "--bundle", FULL)),
        ("semantic-integrity", uv("-m", "mediaingredientmech.validation.semantic_release", "--root", ".", "--report", SEMANTIC_REVIEW)),
        ("supported-export", ["just", "export-supported-kgx", SEMANTIC_REVIEW, SUPPORTED]),
        ("supported-qc", ["just", "qc-supported-kgx", SEMANTIC_REVIEW, SUPPORTED]),
        ("supported-sssom-schema", uv("-c", "from sssom.parsers import parse_sssom_table; from sssom.validators import SchemaValidationType, validate; validate(parse_sssom_table('" + SUPPORTED + "/ingredient_mappings.sssom.tsv'), validation_types=[SchemaValidationType.JsonSchema, SchemaValidationType.PrefixMapCompleteness, SchemaValidationType.StrictCurieFormat])")),
        ("companion-refresh", uv("scripts/refresh_unchanged_cohort.py", "--baseline", BASE, "--prior-review", PRIOR, "--output", NEXT + "/review.json", "--receipt", NEXT + "/dependency-refresh.json", "--prior-copy", NEXT + "/prior-review.json")),
        ("companion-export", uv("-m", "mediaingredientmech.export.ingredient_bundle", "export", "--review", NEXT + "/review.json", "--output", COMPANION)),
    ]


def gates():
    tests = ["tests/test_curate_lithium_glycerophosphate.py", "tests/test_mapping_change_receipt.py", "tests/test_reviewed_sssom.py", "tests/test_semantic_review_builder.py", "tests/test_semantic_mapping_review.py", "tests/test_ingredient_bundle.py", "tests/test_ingredient_bundle_dependency_refresh.py", "tests/test_unified_rejections.py", "tests/test_unified_source_holds.py"]
    return [
        ("focused-regressions", uv("-m", "pytest", "-q", "-o", "addopts=", "-p", "no:cacheprovider", *tests)),
        ("full-qc", ["just", "qc"]),
        ("curies-and-products", ["just", "curie-validate", "validate-products"]),
        ("unified-gates", ["just", "check-unified-rejections", "check-unified-freshness"]),
        ("writer-audit", ["just", "audit-writers"]),
        ("full-suite", uv("-m", "pytest", "-q", "-o", "addopts=", "-p", "no:cacheprovider")),
    ]


def exports():
    return [
        ("flat-exports", ["just", "export-indexes", "export-lists", "export-browser"]),
        ("visual-metadata", uv("scripts/refresh_visualization_metadata.py")),
        ("visual-currency", ["just", "check-visualizations"]),
    ]


def immutable():
    require(sha(HERE / "prepared-inputs.json") == PLAN_SHA, "Prepared input contract changed")
    plan = read(HERE / "prepared-inputs.json")
    require(sha(HELPER) == plan["helper_sha256"], "Run helper changed")
    require(sha(RUN / "step4-context.json") == plan["source_context_sha256"], "Run context changed")
    require(sha(HERE / "approved-comment.json") == plan["approved_comment_sha256"], "Approved comment capture changed")
    require(sha(RUN / "approved-plan.txt") == plan["approved_plan_sha256"], "Approved plan changed")
    require(git("rev-parse", "HEAD").decode().strip() == BASE, "Execution is restricted to the prepared durable base before feature commit")
    require(git("branch", "--show-current").decode().strip() == plan["branch"], "Unexpected work branch")
    for path, expected in {**plan["protected_inputs"], **plan["old_receipts"]}.items():
        require(sha(ROOT / path) == expected == digest(base(path)), "Protected input changed: " + path)
    return plan


def receipt_paths():
    # Include ignored/nested paths and refuse symlinks; nothing is hidden by gitignore.
    return {p.relative_to(ROOT).as_posix() for p in (ROOT / RECEIPTS).rglob("*.json") if p.is_file() or p.is_symlink()}


def chain_tail(plan):
    receipts = [json.loads(base(p)) for p in plan["old_receipts"]]
    receipts.sort(key=lambda x: x["sequence"])
    require([r["sequence"] for r in receipts] == list(range(1, len(receipts) + 1)), "Historical receipt sequence is not contiguous")
    for previous, current in zip(receipts, receipts[1:]):
        require(previous["after_sha256"] == current["before_sha256"], "Historical receipt chain is broken")
    require(len(receipts) == 17 and receipts[-1]["after_sha256"] == digest(base(CANONICAL)), "Expected verified merged Step 3 tail")
    return receipts[-1]


def preflight():
    plan = immutable()
    tail = chain_tail(plan)
    require(receipt_paths() == set(plan["old_receipts"]), "Preflight needs exactly the existing receipt path set")
    for path, expected in plan["baseline_source_sha256"].items():
        require(sha(ROOT / path) == expected, "Preflight source/product already changed: " + path)
    target = [r for r in rows(base(CANONICAL), sssom=True) if r["subject_id"] == SUBJECT]
    decisions = [r for r in json.loads(base(MAPPING))["decisions"] if r["owner_record"] == OWNER]
    role = [r for r in rows(base(ASSERTIONS)) if r["source_record"] == OWNER]
    findings = [r for r in rows(base(FINDINGS)) if r["source_record"] == OWNER]
    require(len(target) == len(decisions) == 3 and all(r["disposition"] == "WITHHOLD" for r in decisions), "Baseline target is not three held rows")
    require(len(role) == 1 and role[0]["resolution_status"] == "OPEN", "Expected one unresolved role")
    require(len(findings) == 2 and all(r["resolution_status"] == "OPEN" for r in findings), "Expected two unresolved findings")
    return {"executed": False, "base": BASE, "owner_sha256": sha(ROOT / OWNER), "target_mapping_rows": target, "held_mapping_count": len(decisions), "open_role": role, "open_findings": findings, "immutable_receipts": len(plan["old_receipts"]), "verified_tail": tail["sequence"], "next_expected_sequence": tail["sequence"] + 1, "no_scientific_approval": True}


def canonical_scope(old_bytes, new_bytes):
    old_meta, old_fields, old, old_lines = table(old_bytes, sssom=True)
    new_meta, new_fields, new, new_lines = table(new_bytes, sssom=True)
    require(old_fields == new_fields, "Canonical columns changed")
    old_target = indexed([r for r in old if r["subject_id"] == SUBJECT], key)
    new_target = indexed([r for r in new if r["subject_id"] == SUBJECT], key)
    require(set(old_target) == TARGET_KEYS | {(SUBJECT, "skos:exactMatch", "cas:17989-41-2")} and set(new_target) == TARGET_KEYS, "Wrong three-to-two subject boundary")
    require([line for line in old_lines if not line.startswith(SUBJECT + "\t")] == [line for line in new_lines if not line.startswith(SUBJECT + "\t")], "Unrelated canonical row/header bytes changed")
    date_line = lambda line: re.match(r"# (mapping_set_version|mapping_date):", line)
    require([x for x in old_meta if not date_line(x)] == [x for x in new_meta if not date_line(x)], "Unrelated canonical metadata changed")
    newest = max(r["mapping_date"] for r in new)
    for name in ("mapping_set_version", "mapping_date"):
        found = [x for x in new_meta if x.startswith("# " + name + ":")]
        require(len(found) == 1 and found[0].strip() == f'# {name}: "{newest}"', "Header date does not equal newest actual row date")
    for k, row in new_target.items():
        previous = old_target[k]
        mutable = ("source", "mapping_date", "other") if k[1] == "skos:broadMatch" else ("source", "mapping_date", "comment")
        require(without(previous, *mutable) == without(row, *mutable), "Unexpected target row payload change: " + str(k))
        require(set(previous["source"].split("|")) <= set(row["source"].split("|")), "Historical source token lost")
        if k[1] == "skos:broadMatch":
            require(row["other"] == "" and row["comment"] == previous["comment"] and "#390" in row["comment"], "Broad row alias or historical #390 comment changed")
        else:
            require(row["other"] == "CAS:17989-41-2", "CAS procurement display token changed")
            require(row["comment"] == f"Registry/identity row preserving {IDENTITY} alongside parent CHEBI:15978.", "Unexpected local primary identity explanation")
    return old, new


def prerequisites(args):
    plan = immutable()
    tail = chain_tail(plan)
    require(args.source_log and args.mapping_receipt, "Supply completed --source-log and published --mapping-receipt")
    source_path = Path(args.source_log).absolute()
    relative = Path(args.mapping_receipt)
    require(not relative.is_absolute() and relative.parent.as_posix() == RECEIPTS and relative.suffix == ".json", "Expected one direct native mapping receipt path")
    receipt_path = ROOT / relative
    source, receipt = read(source_path), read(receipt_path)
    require(receipt_paths() == set(plan["old_receipts"]) | {relative.as_posix()}, "Receipt path set changed")
    require(source.get("phase") == "sources" and source.get("state") == "complete" and source.get("applied") is True and str(source.get("approval", "")).startswith("NONE"), "Source transaction is incomplete or grants approval")
    require(len(source["records"]) == 1 and source["records"][0]["source_record"] == OWNER, "Source receipt must bind exactly the lithium owner")
    record = source["records"][0]
    require(record["before_yaml_sha256"] == digest(base(OWNER)) and record["after_yaml_sha256"] == sha(ROOT / OWNER), "Source owner hash binding changed")
    require(source["output_sha256"] == {OWNER: sha(ROOT / OWNER)}, "Source transaction output scope changed")
    require(source["sssom_before_sha256"] == digest(base(CANONICAL)) and source["baseline_before_sha256"] == digest(base(BASELINE)), "Source canonical/baseline preimage changed")
    require(receipt["records"] == source["records"] and str(receipt.get("approval", "")).startswith("NONE"), "Mapping receipt owner or approval context differs")
    require(receipt["issue"] == "https://github.com/CultureBotAI/MediaIngredientMech/issues/1005", "Receipt does not cite the approved issue")
    require(receipt["sequence"] == tail["sequence"] + 1 == 18 and receipt["before_sha256"] == tail["after_sha256"] and receipt["after_sha256"] == sha(ROOT / CANONICAL), "Receipt is not the verified next chain link")
    require(receipt["touched_subjects"] == [SUBJECT] and (receipt["changed_rows"], receipt["removed_rows"], receipt["added_rows"]) == (2, 1, 0), "Mapping receipt exceeds approved subject/row scope")
    old, new = canonical_scope(base(CANONICAL), payload(ROOT / CANONICAL))
    require(receipt["before_row_count"] == len(old) and receipt["after_row_count"] == len(new) == len(old) - 1, "Receipt row counts disagree")
    old_positions = [i for i, row in enumerate(old, 1) if row["subject_id"] == SUBJECT]
    new_positions = [i for i, row in enumerate(new, 1) if row["subject_id"] == SUBJECT]
    require([receipt["position_map"][i - 1] for i in old_positions] == [new_positions[0], None, new_positions[1]], "Target native receipt alignment is not [first,null,second]")
    astree = ast.parse(payload(ROOT / ASSEMBLER))
    pins = [ast.literal_eval(n.value) for n in astree.body if isinstance(n, ast.Assign) and any(isinstance(t, ast.Name) and t.id == "REVIEWED_SOURCE" for t in n.targets)]
    require(pins == [sha(ROOT / CANONICAL)], "Root must bind the assembler pin to the promoted bytes")
    old_pin = digest(base(CANONICAL)).encode()
    require(base(ASSEMBLER).count(old_pin) == 1 and payload(ROOT / ASSEMBLER) == base(ASSEMBLER).replace(old_pin, sha(ROOT / CANONICAL).encode()), "Assembler changed beyond the exact reviewed source pin")
    baseline_lines = base(BASELINE).splitlines(keepends=True)
    removed = [line for line in baseline_lines if line.startswith((SUBJECT + "\tGlycerol 3-phosphate\tMIM:Glycerol_3-phosphate\t").encode())]
    require(len(removed) == 1 and payload(ROOT / BASELINE) == b"".join(line for line in baseline_lines if line != removed[0]), "Rule K retirement exceeds the one approved pair")
    old_record, current = yaml.safe_load(base(OWNER)), yaml.safe_load(payload(ROOT / OWNER))
    require(current["identifier"] == IDENTITY and "chemical_properties" not in current, "Lithium identity/active chemistry contract violated")
    require(current["nutritional_roles"] == old_record["nutritional_roles"] and current["synonyms"] == old_record["synonyms"], "Unapproved role or rejected-synonym change")
    require(current["curation_history"][:-1] == old_record["curation_history"], "Old history was changed")
    individual_record_scope()
    return {"source_log": str(source_path), "source_sha256": sha(source_path), "mapping_receipt": relative.as_posix(), "mapping_receipt_sha256": sha(receipt_path), "canonical_rows_before": len(old), "canonical_rows_after": len(new), "old_receipts_preserved": len(plan["old_receipts"])}


def individual_record_scope():
    existing = {path for path in git("ls-tree", "-r", "--name-only", BASE, "data/ingredients").decode().splitlines() if path.endswith(".yaml")}
    actual = {p.relative_to(ROOT).as_posix() for p in (ROOT / "data/ingredients").rglob("*.yaml")}
    require(actual == existing, "Individual record membership changed, including ignored/nested files")
    for path in sorted(existing):
        if path.endswith(".yaml") and path != OWNER:
            require(payload(ROOT / path) == base(path), "Unrelated individual owner changed: " + path)
    return existing


def mapping_by_key(decisions, canonical):
    bound = []
    for decision in decisions:
        position = decision["source_position"]
        require(isinstance(position, int) and 1 <= position <= len(canonical), "Mapping position out of range")
        require(str(position) == str(decision["evidence_key"]), "Mapping evidence key no longer names its row")
        bound.append((key(canonical[position - 1]), decision))
    require(len({k for k, _ in bound}) == len(bound), "Duplicate mapping key")
    return dict(bound)


def compare_mapping_decisions(old_decisions, new_decisions, old_rows, new_rows):
    old = mapping_by_key(old_decisions, old_rows)
    new = mapping_by_key(new_decisions, new_rows)
    unrelated_old = {k: without(v, "source_position", "evidence_key") for k, v in old.items() if k[0] != SUBJECT}
    unrelated_new = {k: without(v, "source_position", "evidence_key") for k, v in new.items() if k[0] != SUBJECT}
    require(unrelated_old == unrelated_new, "Unrelated complete mapping decision changed beyond native location")
    selected = {k: v for k, v in new.items() if k[0] == SUBJECT}
    require(set(selected) == TARGET_KEYS and all(v["owner_record"] == OWNER and v["disposition"] == "WITHHOLD" for v in selected.values()), "Target mappings are not exactly two held rows")
    return len(unrelated_new)


def compare_assertions(old, new, old_rows, new_rows, owner_sha, canonical_sha):
    nonmap = lambda items: indexed([x for x in items if x["assertion_type"] != "mapping" and x["source_record"] != OWNER], lambda x: (x["source_record"], x["assertion_type"], x["source_position"]))
    require(nonmap(old) == nonmap(new), "Unrelated nonmapping assertion payload/disposition changed")
    before = [x for x in old if x["source_record"] == OWNER]
    after = [x for x in new if x["source_record"] == OWNER]
    require(len(before) == len(after) == 1 and after[0]["assertion_type"] == "nutritional_roles" and after[0]["resolution_status"] == "OPEN", "Target provisional role was removed, expanded or approved")
    require(after[0]["source_record_sha256"] == owner_sha, "Target role owner hash is stale")
    require(without(before[0], "assertion_id", "source_record_sha256") == without(after[0], "assertion_id", "source_record_sha256"), "Target role payload/reason/evidence changed")
    def mappings(items, canonical):
        return indexed([x for x in items if x["assertion_type"] == "mapping"], lambda x: key(canonical[int(x["source_position"]) - 1]))
    om, nm = mappings(old, old_rows), mappings(new, new_rows)
    strip = lambda x: without(x, "assertion_id", "source_record_sha256", "source_position")
    require({k: strip(v) for k, v in om.items() if k[0] != SUBJECT} == {k: strip(v) for k, v in nm.items() if k[0] != SUBJECT}, "Unrelated mapping assertion payload/status/reason/evidence changed")
    require(all(x["source_record"] == CANONICAL and x["source_record_sha256"] == canonical_sha for x in nm.values()), "Mapping assertion source binding is stale")
    selected = {k: v for k, v in nm.items() if k[0] == SUBJECT}
    require(set(selected) == TARGET_KEYS and all(x["resolution_status"] == "OPEN" for x in selected.values()), "A target mapping assertion was approved or lost")


def compare_findings(old, new, owner_sha):
    previous, current = indexed(old, lambda x: x["finding_id"]), indexed(new, lambda x: x["finding_id"])
    require(set(previous) == set(current), "Finding cohort changed; do not blanket retire mixed identity/role findings")
    for finding_id, row in current.items():
        if previous[finding_id]["source_record"] == OWNER:
            require(row["resolution_status"] == "OPEN" and row["current_record_sha256"] == owner_sha, "Target mixed/role finding was resolved or is stale")
            require(without(row, "current_record_sha256") == without(previous[finding_id], "current_record_sha256"), "Target finding payload/evidence changed")
        else:
            require(row == previous[finding_id], "Unrelated finding changed: " + finding_id)


def verify_outputs(args):
    prerequisite = prerequisites(args)
    old_rows, current_rows = canonical_scope(base(CANONICAL), payload(ROOT / CANONICAL))
    mapping = read(ROOT / MAPPING)
    require(mapping["source_sha256"] == sha(ROOT / CANONICAL), "Mapping review source pin is stale")
    unchanged = compare_mapping_decisions(json.loads(base(MAPPING))["decisions"], mapping["decisions"], old_rows, current_rows)
    assertions = rows(payload(ROOT / ASSERTIONS))
    compare_assertions(rows(base(ASSERTIONS)), assertions, old_rows, current_rows, sha(ROOT / OWNER), sha(ROOT / CANONICAL))
    compare_findings(rows(base(FINDINGS)), rows(payload(ROOT / FINDINGS)), sha(ROOT / OWNER))
    semantic = read(ROOT / SEMANTIC_REVIEW)
    require(semantic["release_verdict"] == "FAIL", "Full scientific release must not be promoted")
    require(semantic["blocking_finding_ids"] == json.loads(base(SEMANTIC_REVIEW))["blocking_finding_ids"], "Historical unresolved finding hold changed")
    def target(edge):
        return edge["source_record"] == OWNER or (edge["assertion_type"] == "mapping" and json.loads(edge["assertion_json"])["subject_id"] == SUBJECT)
    require(not any(target(edge) for edge in rows(payload(ROOT / SUPPORTED / "mim_edges.tsv"))), "Supported graph publishes a target held claim")
    backlog = read(ROOT / SUPPORTED / "unsupported-backlog.json")
    require(sum(target(item["edge"]) for item in backlog["assertions"]) == 3, "Backlog must retain two held target mappings plus the provisional role")
    audit, prior, successor = read(ROOT / NEXT / "dependency-refresh.json"), read(ROOT / PRIOR), read(ROOT / NEXT / "review.json")
    require(audit["scientific_approval_added"] is False and audit["requested_baseline"] == BASE, "Wrong companion dependency refresh or approval")
    require(successor["decisions"] == prior["decisions"] and len(successor["decisions"]) == 51, "Companion claim/decision cohort changed")
    require(successor["record_inputs"] == prior["record_inputs"] and len(successor["record_inputs"]) == 20, "Companion owner hashes changed")
    require(OWNER not in successor["record_inputs"], "Target owner entered unchanged companion")
    require(payload(ROOT / NEXT / "prior-review.json") == payload(ROOT / PRIOR), "Prior companion copy differs")
    require(audit["claim_counts"] == {"mapping": 20, "identifier": 18, "product": 3, "occurrence": 10}, "Companion claim types changed")
    moves = sum(x["base_decision_locations"]["before"] != x["base_decision_locations"]["after"] for x in audit["selected_mapping_evidence_unchanged"])
    return {**prerequisite, "mapping_counts": dict(Counter(x["disposition"] for x in mapping["decisions"])), "unrelated_mapping_decisions_preserved": unchanged, "target_mapping_holds": 2, "target_role_status": "OPEN", "target_role_payload_unchanged": True, "target_findings_open": 2, "all_other_assertion_decisions_preserved": True, "full_scientific_release": semantic["release_verdict"], "blocking_findings": len(semantic["blocking_finding_ids"]), "blocking_assertions": len(semantic["blocking_assertion_ids"]), "semantic_status_counts": dict(Counter(x["resolution_status"] for x in assertions)), "companion_owners": 20, "companion_claims": 51, "companion_mapping_relocations": moves, "scientific_approval_added": False}


def selectors_and_unified():
    for path in read(HERE / "prepared-inputs.json")["selector_paths"]:
        old = base(path)
        require(old.count(PRIOR.encode()) == 1 and payload(ROOT / path) == old.replace(PRIOR.encode(), (NEXT + "/review.json").encode()), "Expected exact owned companion selector advance: " + path)
    docs = payload(ROOT / "docs/INGREDIENT_BUNDLE.md").decode()
    require(NEXT + "/review.json" in docs and NEXT + "/README.md" in docs and (ROOT / NEXT / "README.md").is_file(), "Root must document the actual companion refresh")
    require(payload(ROOT / "UNIFIED_INGREDIENT_MAPPING.tsv") == base("UNIFIED_INGREDIENT_MAPPING.tsv"), "Step 4 requires zero unified row/byte changes")


def execution_inputs(args):
    paths = {OWNER, CANONICAL, BASELINE, "mappings/culturemech_recipe_membership.tsv", "mappings/unified_mapping_rejections.tsv", "UNIFIED_INGREDIENT_MAPPING.tsv", ASSEMBLER, SEMANTIC + "/build_review.py"}
    paths |= receipt_paths()
    for directory in (ROOT / "scripts", ROOT / "src"):
        paths |= {p.relative_to(ROOT).as_posix() for p in directory.rglob("*") if p.suffix in {".py", ".yaml", ".yml", ".json"} and (p.is_file() or p.is_symlink())}
    result = {p: sha(ROOT / p) for p in sorted(paths)}
    result.update({str(HERE / "native_chain.py"): sha(HERE / "native_chain.py"), str(HELPER): sha(HELPER), str(Path(args.source_log).absolute()): sha(Path(args.source_log).absolute())})
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("stage", nargs="?", default="plan", choices=("plan", "preflight", "build", "verify", "exports", "gates"))
    parser.add_argument("--execute", action="store_true")
    parser.add_argument("--tag")
    parser.add_argument("--source-log")
    parser.add_argument("--mapping-receipt")
    args = parser.parse_args()
    if args.stage == "preflight":
        print(json.dumps(preflight(), indent=2)); return
    if args.stage == "verify":
        print(json.dumps(verify_outputs(args), indent=2)); return
    if args.stage == "plan" or not args.execute:
        print(json.dumps({"executed": False, "base": BASE, "profile": "step4-mim", "prerequisites": "Reviewed one-owner source/promotion receipts; verified existing17receipt tail and exclusively published next receipt18; root-updated assembler pin. No driver application/receipt/unified/selector/Git mutations.", "build": commands(), "after_companion_export": "validate actual new manifest SHA256", "exports": exports(), "root_before_gates": "Verify unchanged companion proof, advance exact owned selectors/docs, execute native unified replay with zero-row contract and stamp actual inputs; no new approval.", "gates": gates()}, indent=2)); return
    require(args.tag and re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9._-]*", args.tag), "Explicit execution requires unique safe --tag")
    context = prerequisites(args)
    plan = immutable()
    if args.stage == "build":
        for path in plan["output_directories"]:
            require(not (ROOT / path).exists() and not (ROOT / path).is_symlink(), "Preserve existing output and use reviewed recovery, not overwrite: " + path)
        for path in plan["chain_rewrites"]:
            require(payload(ROOT / path) == base(path), "Dependency output already changed before build: " + path)
    else:
        context["verified_outputs"] = verify_outputs(args)
    if args.stage == "gates":
        selectors_and_unified()
    frozen = execution_inputs(args)
    execution = HERE / "executions" / (args.tag + "-" + args.stage)
    execution.mkdir(parents=True, exist_ok=False)
    def save(name, data):
        with (execution / name).open("x") as stream:
            json.dump(data, stream, indent=2); stream.write("\n")
    save("start.json", {"started_at": datetime.datetime.now(datetime.timezone.utc).isoformat(), "stage": args.stage, "context": context, "input_sha256": frozen, "before_dependency_hashes": {p: sha(ROOT / p) for p in plan["chain_rewrites"]}})
    def run(name, command):
        immutable()
        require(execution_inputs(args) == frozen, "Source/code/receipt input membership or bytes changed")
        log = args.tag + "-" + name
        require(all(not (RUN / "logs" / (log + suffix)).exists() for suffix in (".log", ".json")), "Log tag already used")
        with (execution / "commands.jsonl").open("a") as stream:
            stream.write(json.dumps({"name": log, "argv": command}) + "\n")
        subprocess.run([sys.executable, str(HELPER), "step4-mim", log, "--", *command], check=True)
        require(execution_inputs(args) == frozen, "Native command changed a protected source/code/receipt input")
    if args.stage == "build":
        for name, command in commands():
            if name == "companion-refresh":
                (ROOT / NEXT).mkdir(exist_ok=False)
            run(name, command)
        manifest = sha(ROOT / COMPANION / "manifest.json")
        run("companion-validate", uv("-m", "mediaingredientmech.export.ingredient_bundle", "validate", COMPANION, "--manifest-sha256", manifest))
    elif args.stage == "exports":
        for name, command in exports():
            run(name, command)
    elif args.stage == "gates":
        for name, command in gates():
            run(name, command)
        selectors_and_unified()
    save("verified-output.json", verify_outputs(args))
    immutable()
    save("complete.json", {"complete": True, "stage": args.stage, "finished_at": datetime.datetime.now(datetime.timezone.utc).isoformat(), "scientific_approval_added": False, "canonical_sha256": sha(ROOT / CANONICAL)})


if __name__ == "__main__":
    main()
