#!/usr/bin/env python3
"""Read-only dependency-author comparison of completed #1004 products.

Run only after root's complete native chain, selectors, flat exports and unified
publication. Output is JSON on stdout; no repository or report file is written.
This is implementation verification, not an independent adversarial review.
"""

from __future__ import annotations

import argparse
import copy
import csv
import hashlib
import importlib.util
import io
import json
import subprocess
import sys
from collections import Counter
from pathlib import Path

sys.dont_write_bytecode = True
import yaml  # noqa: E402

RUN = Path(__file__).resolve().parent
ROOT = RUN / "step3-mim"
BASE = "99fe4b44d78126d78041a69eeb366c52bedf0caa"
SURVIVOR = "data/ingredients/mapped/Carnitine_Hydrochloride.yaml"
TOMBSTONE = "data/ingredients/mapped/Carnitine_Dl_Hydrochloride.yaml"
NLDM = "data/ingredients/mapped/NLDM_metabolites.yaml"
OWNERS = (SURVIVOR, TOMBSTONE, NLDM)
OLD = "kgmicrobe.compound:carnitine_hydrochloride"
NEW = "NCIT:C216679"
NAME = "Carnitine Hydrochloride"
RAW_NAME = "Carnitine (Dl) Hydrochloride"
LABEL = "DL-Carnitine Hydrochloride"
SUBJECT = "MIM:Carnitine_Hydrochloride"
RETIRED = "MIM:Carnitine_Dl_Hydrochloride"
NLDM_SUBJECT = "MIM:NLDM_metabolites"
SUBJECTS = {SUBJECT, RETIRED, NLDM_SUBJECT}
CANONICAL = "mappings/ingredient_mappings.sssom.tsv"
MEMBERSHIP = "mappings/culturemech_recipe_membership.tsv"
LEDGER = "mappings/unified_mapping_rejections.tsv"
BASELINE = "mappings/other_cross_record_baseline.tsv"
MAPROOT = "reports/sssom_completion_20260921"
SEMROOT = "reports/semantic_review_20260921/resolution"
PRIOR = "reports/ingredient_bundle_20261101_ncit875/review.json"
NEXT = "reports/ingredient_bundle_20261101_carnitine1004"
NCI = "https://api-evsrest.nci.nih.gov/api/v1/concept/ncit/C216679?include=full"
CHEBI = "https://www.ebi.ac.uk/chebi/CHEBI:48601"
RECIPE_IDS = {"CultureMech:" + suffix for suffix in (
    "015654", "015655", "015656", "015665", "015666", "015667", "015668",
    "015669", "015670", "015671", "015740", "015741", "015742", "015749",
)}


def require(condition, message):
    if not condition:
        raise ValueError(message)


def sha(data):
    return hashlib.sha256(data).hexdigest()


def old(path):
    return subprocess.check_output(["git", "show", BASE + ":" + path], cwd=ROOT)


def current(path):
    return (ROOT / path).read_bytes()


def read(path):
    return json.loads(Path(path).read_bytes())


def table(data, *, format):
    """Parse an explicit transport format; a leading # in a data row is data.

    SSSOM and native membership permit a leading comment prelude. Plain TSV
    (including unified mappings and the rejection ledger) has no such prelude.
    Never discard hash-prefixed rows once the table header has been reached.
    """
    require(format in {"plain", "sssom", "commented-membership"}, "Unknown TSV format")
    content = data.decode()
    if format != "plain":
        lines = content.splitlines(keepends=True)
        while lines and lines[0].startswith("#"):
            lines.pop(0)
        content = "".join(lines)
    reader = csv.DictReader(io.StringIO(content), delimiter="\t")
    records = list(reader)
    require(bool(reader.fieldnames) and all(None not in row and None not in row.values() for row in records), "Malformed TSV")
    return reader.fieldnames, records


def load(path, name):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


def outside(data, prefixes):
    prefixes = tuple((prefix + "\t").encode() for prefix in prefixes)
    return b"".join(line for line in data.splitlines(keepends=True) if not line.startswith(prefixes))


def without(record, fields):
    return {key: value for key, value in record.items() if key not in fields}


def source_check(source_path):
    source = read(source_path)
    require(source.get("phase") == "sources" and source.get("state") == "complete" and source.get("applied") is True, "Incomplete source receipt")
    require(str(source.get("approval", "")).startswith("NONE"), "Source receipt must grant no release approval")
    entries = {entry["source_record"]: entry for entry in source["records"]}
    require(len(source["records"]) == 3 and set(entries) == set(OWNERS), "Source receipt must bind exactly three owners")
    before = {path: yaml.safe_load(old(path)) for path in OWNERS}
    after = {path: yaml.safe_load(current(path)) for path in OWNERS}
    for path in OWNERS:
        entry = entries[path]
        require(entry["before_yaml_sha256"] == sha(old(path)), "Wrong durable owner preimage: " + path)
        require(entry["after_yaml_sha256"] == sha(current(path)), "Wrong current owner afterimage: " + path)
        original, amended = before[path]["curation_history"], after[path]["curation_history"]
        require(len(amended) == len(original) + 1 and amended[:-1] == original, "Historical curation prefix changed: " + path)
        event = amended[-1]
        require(event["timestamp"] == source["timestamp"] and event["changes"] == entry["change"], "Source event differs from receipt")
        require(event["llm_assisted"] is True and event["curator"] == "Codex", "Curation attribution changed")
    allowed = {
        SURVIVOR: {"identifier", "ontology_mapping", "chemical_properties", "synonyms", "curation_history"},
        TOMBSTONE: {"identifier", "ontology_mapping", "mapping_status", "representative", "chemical_properties", "synonyms", "curation_history"},
        NLDM: {"components", "curation_history"},
    }
    for path in OWNERS:
        require(without(before[path], allowed[path]) == without(after[path], allowed[path]), "Unrelated owner field changed: " + path)
    for path in (SURVIVOR, TOMBSTONE):
        require(after[path]["identifier"] == NEW, "Wrong corrected identifier")
        previous, updated = before[path]["ontology_mapping"], after[path]["ontology_mapping"]
        exact = {"ontology_id": NEW, "ontology_label": LABEL, "ontology_source": "NCIT", "mapping_quality": "EXACT_MATCH"}
        require(all(updated[key] == value for key, value in exact.items()), "Wrong exact salt grounding")
        require(without(previous, {*exact, "evidence"}) == without(updated, {*exact, "evidence"}), "Unrelated grounding field changed")
        require(updated["evidence"][:-1] == previous["evidence"] and len(updated["evidence"]) == len(previous["evidence"]) + 1, "Mapping evidence history changed")
        require(updated["evidence"][-1]["source"] == NCI, "New grounding lacks the reviewed primary source")
    survivor, tombstone = after[SURVIVOR], after[TOMBSTONE]
    require(survivor["mapping_status"] == "MAPPED" and tombstone["mapping_status"] == "REJECTED", "Wrong active/rejected states")
    require(tombstone["representative"] == NEW and "chemical_properties" not in tombstone, "Tombstone exposes a stale active identity")
    require(json.dumps(before[TOMBSTONE]["chemical_properties"], sort_keys=True) in tombstone["curation_history"][-1]["changes"], "Prior tombstone chemistry was not preserved in history")
    chemistry = survivor["chemical_properties"]
    for key, value in {"cas_rn": "461-05-2", "pubchem_cid": 5970, "molecular_formula": "C7H16ClNO3", "molecular_weight": 197.66}.items():
        require(chemistry[key] == value, "Wrong chloride chemistry: " + key)
    rejected = copy.deepcopy(before[TOMBSTONE]["synonyms"][0])
    require(rejected["synonym_text"] == "3-hydroxy-4-(trimethylammonio)butanoate", "Unexpected duplicate synonym preimage")
    rejected["synonym_type"] = "REJECTED_LABEL"
    require(tombstone["synonyms"] == [rejected, *before[TOMBSTONE]["synonyms"][1:]], "Tombstone synonym attribution changed")
    require(survivor["synonyms"] == [*before[SURVIVOR]["synonyms"], rejected, {"synonym_text": RAW_NAME, "synonym_type": "RAW_TEXT", "source": "CultureBotHT"}], "Unexpected survivor synonym change")
    expected_parts = copy.deepcopy(before[NLDM]["components"])
    require(expected_parts[58]["component_id"] == OLD, "Wrong NLDM component preimage")
    expected_parts[58]["component_id"] = NEW
    require(after[NLDM]["components"] == expected_parts, "NLDM changed beyond component 59 identity")
    expected_outputs = {*OWNERS, LEDGER, MEMBERSHIP}
    require(set(source["output_sha256"]) == expected_outputs, "Source output scope changed")
    for path, expected in source["output_sha256"].items():
        require(sha(current(path)) == expected, "Source output drift: " + path)
    require(source["sssom_before_sha256"] == sha(old(CANONICAL)) and source["baseline_before_sha256"] == sha(old(BASELINE)), "Source canonical anchors do not match durable base")
    for path in (*OWNERS, LEDGER, MEMBERSHIP, CANONICAL, BASELINE):
        backup = Path(source_path).with_name(Path(source_path).stem + ".before-" + Path(path).name)
        require(backup.read_bytes() == old(path), "Source receipt beforeimage differs from durable base: " + path)
        require(source["input_sha256"][str(ROOT / path)] == sha(old(path)), "Source receipt input hash differs from durable base: " + path)
    evidence_directory = Path(source["evidence_directory"])
    evidence_manifest_path = evidence_directory / "manifest.json"
    evidence_manifest = read(evidence_manifest_path)
    require(source["evidence_manifest_sha256"] == sha(evidence_manifest_path.read_bytes()), "Reviewed primary source manifest changed")
    require(source["input_sha256"][str(evidence_manifest_path)] == source["evidence_manifest_sha256"], "Source receipt lacks its exact evidence manifest")
    for name, evidence in evidence_manifest["files"].items():
        require(Path(name).name == name, "Evidence manifest contains a nonlocal source name")
        path = evidence_directory / name
        raw = path.read_bytes()
        require(sha(raw) == evidence["sha256"] == source["input_sha256"][str(path)] and len(raw) == evidence["bytes"], "Reviewed primary source capture changed: " + name)
    transaction = source.get("transaction", {})
    require(transaction.get("applied") is True and not transaction.get("created") and not transaction.get("unchanged"), "Unexpected source transaction result")
    require(set(transaction["changed"]) == {str(ROOT / path) for path in expected_outputs}, "Unexpected transaction mutation scope")
    # Raw git blob hashes also include ignored/nested current files in the path set.
    object_format = subprocess.check_output(["git", "rev-parse", "--show-object-format"], cwd=ROOT, text=True).strip()
    require(object_format in {"sha1", "sha256"}, "Unsupported Git object format")
    tracked = {}
    for entry in subprocess.check_output(["git", "ls-tree", "-rz", BASE, "--", "data/ingredients"], cwd=ROOT).split(b"\0"):
        if not entry:
            continue
        metadata, path_bytes = entry.split(b"\t", 1)
        path = path_bytes.decode()
        if path.endswith(".yaml"):
            tracked[path] = metadata.split()[2].decode()
    present = {str(path.relative_to(ROOT)) for path in (ROOT / "data/ingredients").rglob("*.yaml")}
    require(set(tracked) == present, "Ingredient file population changed (ignored files included)")
    changed = []
    for path, blob in tracked.items():
        data = current(path)
        if hashlib.new(object_format, b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest() != blob:
            changed.append(path)
    require(set(changed) == set(OWNERS), "Unrelated per-record bytes changed: " + repr(changed))
    return source, before, after, {"source_log_sha256": sha(Path(source_path).read_bytes()), "records_changed": sorted(changed), "unrelated_record_blobs_unchanged": len(tracked) - 3, "history_prefixes_preserved": True, "owner_hashes": {path: sha(current(path)) for path in OWNERS}}


def membership_check():
    original, amended = old(MEMBERSHIP), current(MEMBERSHIP)
    fields, prior = table(original, format="commented-membership")
    new_fields, subsequent = table(amended, format="commented-membership")
    require(fields == new_fields == ["mim_identifier", "recipe_id", "occurrences"], "Membership schema changed")
    cohort = [row for row in prior if row["mim_identifier"] == OLD]
    require(len(cohort) == 14 and {row["recipe_id"] for row in cohort} == RECIPE_IDS and all(row["occurrences"] == "1" for row in cohort), "Historical cohort drift")
    require(not any(row["mim_identifier"] == NEW for row in prior), "Unexpected prior destination cohort")
    lines = original.splitlines(keepends=True)
    header = []
    while lines and lines[0].startswith(b"#"):
        header.append(lines.pop(0))
    header.append(lines.pop(0))
    replaced = [NEW.encode() + b"\t" + line.split(b"\t", 1)[1] if line.startswith((OLD + "\t").encode()) else line for line in lines]
    expected = b"".join(header) + b"".join(sorted(replaced, key=lambda line: tuple(line.split(b"\t")[:2])))
    require(amended == expected, "Membership changed beyond 14 identity cells and native ordering")
    require(len(subsequent) == len(prior), "Membership row count changed")
    return {"identity_cells_migrated": 14, "historical_recipe_ids": sorted(RECIPE_IDS), "occurrences_preserved": True, "header_and_unrelated_row_bytes_preserved": True, "sha256": sha(amended)}


def ledger_check():
    original, amended = old(LEDGER), current(LEDGER)
    fields, prior = table(original, format="plain")
    new_fields, subsequent = table(amended, format="plain")
    require(fields == new_fields, "Ledger schema changed")
    was = [row for row in prior if row["ingredient_name"] == NAME]
    now = [row for row in subsequent if row["ingredient_name"] == NAME]
    require(len(was) == 1 and was[0]["rejected_id"] == "CHEBI:91318" and was[0]["mim_id"] == OLD, "Unexpected ledger preimage")
    require(len(now) == 2 and {row["rejected_id"] for row in now} == {"CHEBI:91318", "CHEBI:48601"}, "Wrong two-row rejection scope")
    require(all(row["mim_id"] == NEW and NCI in row["reason"] and SURVIVOR in row["reason"] for row in now), "Rejections lack corrected owner or evidence")
    require(CHEBI in next(row["reason"] for row in now if row["rejected_id"] == "CHEBI:48601"), "Preventive amide rejection lacks primary citation")
    require(outside(original, {NAME}) == outside(amended, {NAME}), "Unrelated ledger bytes changed")
    require(len(subsequent) == len(prior) + 1, "Unexpected ledger population")
    return {"changed_existing_rejection": "CHEBI:91318", "added_preventive_rejection": "CHEBI:48601", "owner": NEW, "unrelated_bytes_unchanged": True, "sha256": sha(amended)}


def mapping_check(source, after, receipt_path):
    original, amended = old(CANONICAL), current(CANONICAL)
    fields, prior = table(original, format="sssom")
    new_fields, subsequent = table(amended, format="sssom")
    require(fields == new_fields, "Canonical field order changed")
    require(outside(original, SUBJECTS) == outside(amended, SUBJECTS), "Unrelated canonical rows or header bytes changed")
    maker = load(ROOT / MAPROOT / "mapping_changes/make_receipt.py", "step3_final_native_mapping_alignment")
    changes, positions = maker.align(prior, subsequent)
    require(Counter(row["kind"] for row in changes) == {"changed": 2, "removed": 4}, "Canonical change is not exactly 2 changed / 4 removed")
    changed = {row["after"]["subject_id"]: row for row in changes if row["kind"] == "changed"}
    require(set(changed) == {SUBJECT, NLDM_SUBJECT}, "Unexpected changed canonical subjects")
    removed = [row["before"] for row in changes if row["kind"] == "removed"]
    require(Counter(row["subject_id"] for row in removed) == {RETIRED: 3, SUBJECT: 1}, "Wrong removed subject rows")
    require(next(row for row in removed if row["subject_id"] == SUBJECT)["object_id"] == OLD, "Wrong survivor registry row removed")
    survivor = changed[SUBJECT]["after"]
    require((survivor["object_id"], survivor["object_label"], survivor["predicate_id"]) == (NEW, LABEL, "skos:exactMatch"), "Wrong canonical salt identity")
    require(survivor["other"] == RAW_NAME + "|CAS:461-05-2", "Wrong salt alias/CAS scope")
    nldm = changed[NLDM_SUBJECT]
    nldm_fields = {key for key in fields if nldm["before"][key] != nldm["after"][key]}
    require(nldm_fields <= {"source", "mapping_date", "validation_method"}, "NLDM mapping payload changed beyond approved provenance")
    for subject, owner in ((SUBJECT, SURVIVOR), (NLDM_SUBJECT, NLDM)):
        historical = list(dict.fromkeys(token for row in prior if row["subject_id"] == subject for token in row["source"].split("|")))
        current_sources = changed[subject]["after"]["source"].split("|")
        expected = set(historical) | {"MIM:" + item["source"] for item in after[owner]["ontology_mapping"]["evidence"]} | {"MIM:curator=Codex"}
        require(current_sources[:len(historical)] == historical and set(current_sources) == expected and len(current_sources) == len(set(current_sources)), "Historical source lineage changed or acquired an unsupported token")
        require(changed[subject]["after"]["mapping_date"] == max(event["timestamp"][:10] for event in after[owner]["curation_history"]), "Row date does not match current curation history")
    receipt = read(receipt_path)
    require(receipt["sequence"] == 17 and str(receipt["approval"]).startswith("NONE"), "Wrong mapping receipt sequence/approval")
    require(receipt["before_sha256"] == sha(original) and receipt["after_sha256"] == sha(amended), "Mapping receipt digest mismatch")
    require(receipt["records"] == source["records"] and receipt["changes"] == changes and receipt["position_map"] == positions, "Mapping receipt does not replay the actual three-owner batch")
    require((receipt["changed_rows"], receipt["removed_rows"], receipt["added_rows"]) == (2, 4, 0), "Receipt row counts differ")
    baseline_before, baseline_after = old(BASELINE), current(BASELINE)
    retired = {f"{subject}\tDL-carnitine\tMIM:Dl-carnitine\tUNREVIEWED\n".encode() for subject in (SUBJECT, RETIRED)}
    require(all(baseline_before.splitlines(keepends=True).count(line) == 1 for line in retired), "Expected two allowances absent from durable baseline")
    require(baseline_after == b"".join(line for line in baseline_before.splitlines(keepends=True) if line not in retired), "Rule K baseline changed beyond two retirements")
    before_review = json.loads(old(MAPROOT + "/review.json"))
    after_review = read(ROOT / MAPROOT / "review.json")
    new_decisions = {row["source_position"]: row for row in after_review["decisions"]}
    unchanged_decisions = 0
    for decision in before_review["decisions"]:
        if decision["owner_record"] in OWNERS:
            continue
        destination = positions[decision["source_position"] - 1]
        require(destination is not None, "Unrelated mapping approval row removed")
        now = new_decisions[destination]
        require((now["owner_record"], now["disposition"], now["row_sha256"]) == (decision["owner_record"], decision["disposition"], decision["row_sha256"]), "Unrelated mapping identity/payload/decision changed")
        unchanged_decisions += 1
    return {"rows_before": len(prior), "rows_after": len(subsequent), "changed": 2, "removed": 4, "added": 0, "unrelated_row_and_metadata_bytes_unchanged": True, "nldm_changed_columns": sorted(nldm_fields), "historical_source_tokens_preserved": True, "unrelated_mapping_decisions_preserved": unchanged_decisions, "baseline_allowances_retired": 2, "canonical_sha256": sha(amended), "mapping_receipt": str(receipt_path.relative_to(ROOT)), "mapping_receipt_sha256": sha(Path(receipt_path).read_bytes())}


def unified_check(after_records):
    path = "UNIFIED_INGREDIENT_MAPPING.tsv"
    original, amended = old(path), current(path)
    fields, prior = table(original, format="plain")
    new_fields, subsequent = table(amended, format="plain")
    require(fields == new_fields, "Unified schema changed")
    old_rows = {row["ingredient_name"]: row for row in prior}
    new_rows = {row["ingredient_name"]: row for row in subsequent}
    require(len(old_rows) == len(prior) and len(new_rows) == len(subsequent), "Duplicate unified ingredient name")
    require(old_rows.keys() == new_rows.keys(), "Unified ingredient population changed")
    changed = {name: {key: [old_rows[name][key], new_rows[name][key]] for key in fields if old_rows[name][key] != new_rows[name][key]} for name in old_rows if old_rows[name] != new_rows[name]}
    require(set(changed) == {NAME}, "Unified changed more than the one approved name")
    require({"mim_id", "cas_rn"} <= set(changed[NAME]) <= {"mim_id", "cas_rn", "synonyms"}, "Unified changed an unapproved column")
    require(changed[NAME]["mim_id"] == [OLD, NEW] and new_rows[NAME]["cas_rn"] == "461-05-2", "Wrong unified salt identity")
    require(outside(original, {NAME}) == outside(amended, {NAME}), "Unrelated unified row/order/header bytes changed")
    require(all(old_rows[name]["occurrence_count"] == new_rows[name]["occurrence_count"] for name in old_rows), "Unified occurrence counts changed")
    require(new_rows[NAME]["occurrence_count"] == "14", "Frozen source cohort no longer has fourteen occurrences")
    require(all(not new_rows[NAME][key] for key in ("chebi_id", "culturemech_term_id", "kg_microbe_node_id")), "Wrong source ChEBI identity leaked into the salt row")
    record = after_records[SURVIVOR]
    allowed = {record["preferred_term"], record["ontology_mapping"]["ontology_label"]} | {item["synonym_text"] for item in record["synonyms"] if item["synonym_type"] != "REJECTED_LABEL"}
    tokens = set(filter(None, new_rows[NAME]["synonyms"].split("|")))
    require(tokens <= allowed, "Unified published an unsupported salt synonym")
    return {"rows": len(subsequent), "changed_rows": 1, "unchanged_rows": len(subsequent) - 1, "delta": changed, "occurrences_before": sum(int(row["occurrence_count"]) for row in prior), "occurrences_after": sum(int(row["occurrence_count"]) for row in subsequent), "every_occurrence_cell_preserved": True, "unrelated_raw_bytes_preserved": True, "sha256": sha(amended)}


def reviews_check():
    package = RUN / "step3-native-chain-plan"
    index = read(package / "evidence-index.json")
    driver_path = package / "native_chain.py"
    require(sha(driver_path.read_bytes()) == index["files"]["native_chain.py"]["sha256"], "Frozen chain verifier changed")
    driver = load(driver_path, "step3_final_frozen_chain_verifier")
    verification = driver.verify_outputs()
    driver.require_selectors()
    prior = json.loads(old(PRIOR))
    successor = read(ROOT / NEXT / "review.json")
    require(current(PRIOR) == old(PRIOR), "Historical companion review changed")
    require(successor["decisions"] == prior["decisions"] and successor["record_inputs"] == prior["record_inputs"], "Companion approvals or selected owners changed")
    require(successor["claims_file"] == prior["claims_file"] and successor["claims_sha256"] == prior["claims_sha256"], "Companion claim set changed")
    require(current(prior["claims_file"]) == old(prior["claims_file"]) and sha(current(prior["claims_file"])) == prior["claims_sha256"], "Companion claim bytes differ from durable base")
    old_semantic = json.loads(old(SEMROOT + "/current-review.json"))
    new_semantic = read(ROOT / SEMROOT / "current-review.json")
    old_findings = set(old_semantic["blocking_finding_ids"])
    new_findings = set(new_semantic["blocking_finding_ids"])
    verification["actual_findings"] = {"before": len(old_findings), "after": len(new_findings), "added_ids": sorted(new_findings - old_findings), "removed_ids": sorted(old_findings - new_findings), "count_assumption": "none; report the actual content-bound result"}
    verification["evidence_gaps_before"] = old_semantic["evidence_gaps"]
    verification["evidence_gaps_after"] = new_semantic["evidence_gaps"]
    verification["companion_durable_claim_bytes_and_decisions_preserved"] = True
    return verification


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source-log", type=Path, default=RUN / "step3-application/source-apply.json")
    parser.add_argument("--mapping-receipt", type=Path, help="Relative to step3-mim; default discovers the sole native sequence-17 receipt")
    args = parser.parse_args()
    subprocess.run(["git", "merge-base", "--is-ancestor", BASE, "HEAD"], cwd=ROOT, check=True)
    if args.mapping_receipt:
        receipt_path = (ROOT / args.mapping_receipt).resolve()
    else:
        candidates = [path for path in (ROOT / MAPROOT / "mapping_changes").glob("*.json") if read(path).get("sequence") == 17]
        require(len(candidates) == 1, "Final mapping receipt is not ready or ambiguous")
        receipt_path = candidates[0]
    require(receipt_path.is_relative_to(ROOT / MAPROOT / "mapping_changes"), "Receipt must be in the native mapping chain")
    # Catch concurrent product changes during this read-only comparison.
    relevant = [*OWNERS, MEMBERSHIP, LEDGER, CANONICAL, BASELINE, "UNIFIED_INGREDIENT_MAPPING.tsv", MAPROOT + "/review.json", MAPROOT + "/mapping-evidence.json", SEMROOT + "/current-review.json", SEMROOT + "/assertion-dispositions.tsv", NEXT + "/review.json", NEXT + "/dependency-refresh.json", NEXT + "/prior-review.json"]
    snapshot = {path: sha(current(path)) for path in relevant}
    source, before, after, sources = source_check(args.source_log)
    result = {
        "scope": "dependency-author verification; not independent adversarial review",
        "baseline": BASE,
        "execution_head": subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=ROOT, text=True).strip(),
        "sources": sources,
        "membership": membership_check(),
        "ledger": ledger_check(),
        "canonical": mapping_check(source, after, receipt_path),
        "unified": unified_check(after),
        "reviews": reviews_check(),
        "input_sha256": snapshot,
        "writes_performed": False,
    }
    require({path: sha(current(path)) for path in relevant} == snapshot, "A compared product changed during analysis")
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
