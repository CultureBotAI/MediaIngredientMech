"""Bind the #710 source adjudications to current records, mappings and full KGX.

This dated builder preserves unresolved historical findings. It carries forward
positive assertion reviews only for identical source records and payloads; the
explicit identity/role/component plans are the only new scientific decisions.
"""

import argparse
import csv
import hashlib
import json
from pathlib import Path

import yaml

from mediaingredientmech.sssom_grading import predicate_for
from mediaingredientmech.validation.semantic_release import (
    adjudicate_assertions,
    adjudicate_findings,
    current_assertions,
    evidence_gaps,
    rows,
    sha,
    validate_release_holds,
)

ROOT = Path(__file__).resolve().parents[3]
HERE = Path(__file__).resolve().parent
BASE = HERE.parent
FROZEN_RELEASE_HOLD_ID = "MIM.hold:724-aromatic-trait-synonym"
FROZEN_RELEASE_HOLD_REASON = (
    "The mapping's other field publishes 'degradation: aromatic compound' as a compound synonym. "
    "This is an organism trait phrase, not a compound name (#703). Withhold the entire mapping "
    "from the supported release and preserve its unchanged row in the separate backlog (#724). "
    "The broader source correction in #703 remains open."
)


def relative(path):
    return str(path.relative_to(ROOT))


def write_rows(path, entries):
    with path.open("w") as stream:
        writer = csv.DictWriter(stream, fieldnames=list(entries[0]), delimiter="\t", lineterminator="\n")
        writer.writeheader()
        writer.writerows(entries)


def apply_release_holds(document, assertions, edges, owners, record_hashes, evidence_path):
    """Apply the frozen negative review after every positive approval path."""
    if document.get("required_hold_ids") != [FROZEN_RELEASE_HOLD_ID]:
        raise ValueError("Missing frozen release hold #724")
    held = validate_release_holds(document, assertions, edges, owners, record_hashes)
    hold = next(iter(held.values()))
    if (hold["owner_record"] != "data/ingredients/mapped/Aromatic_Compound.yaml"
            or hold["review_reason"] != FROZEN_RELEASE_HOLD_REASON
            or hold["issues"] != ["https://github.com/CultureBotAI/MediaIngredientMech/issues/703",
                                  "https://github.com/CultureBotAI/MediaIngredientMech/issues/724"]):
        raise ValueError("Frozen release-hold owner, reason or issue scope changed")
    for decision in assertions:
        if decision["assertion_id"] in held:
            decision.update(resolution_status="OPEN", review_reason=hold["review_reason"], review_evidence=evidence_path)
    validate_release_holds(document, assertions, edges, owners, record_hashes, assertions, evidence_path)


def has_mechanical_evidence_gap(kind, assertion):
    """A historical pass cannot override current explicit evidence limitations."""
    if kind.endswith("_roles"):
        evidence = assertion.get("evidence") or []
        return (not evidence or all(e.get("reference_type") == "COMPUTATIONAL_PREDICTION" for e in evidence)
                or (kind == "cellular_metabolic_roles" and not assertion.get("metabolic_context")))
    if kind == "component":
        return assertion["component_assertion"]["method"] in {"ABBREVIATION_EXPANSION", "CURATED_INTERPRETATION"}
    return kind == "recipe_reference" and assertion.get("relationship") == "CANDIDATE_UNVERIFIED"


def archive_historical_reviews(root, old_rows, original_records, hashes, archive_path):
    """Preserve exact prior reasoning; a missing or changed receipt grants no approval."""
    existing = json.loads(archive_path.read_text()).get("reports", {}) if archive_path.exists() else {}
    archived, eligible = {}, []
    for old in old_rows:
        name = old["source_record"]
        original = original_records.get(name, {})
        path_name, expected = original.get("review_report"), original.get("report_sha256")
        if (old["verdict"] not in {"pass", "pass_with_minor_issues"}
                or hashes.get(name) != old["record_sha256"]
                or original.get("record_sha256") != old["record_sha256"]
                or not expected or not path_name or old.get("review_report") != path_name):
            continue
        path = (root / path_name).resolve()
        if not path.is_relative_to(root.resolve()):
            continue
        # Existing local evidence must itself match; a changed file cannot be
        # hidden by an older archive. A clean checkout can use the bound archive.
        if path.is_file():
            data = path.read_bytes()
        elif path_name in existing:
            entry = existing[path_name]
            if entry.get("sha256") != expected:
                continue
            data = entry.get("text", "").encode()
        else:
            continue
        if hashlib.sha256(data).hexdigest() != expected:
            continue
        archived[path_name] = {"original_path": path_name, "sha256": expected, "text": data.decode()}
        eligible.append(old)
    archive_path.write_text(json.dumps({"schema_version": 1,
        "scope": "Exact historical review texts for unchanged records eligible for inherited assertion review; not new source research.",
        "reports": dict(sorted(archived.items()))}, ensure_ascii=True, indent=2) + "\n")
    return eligible


def inherited_role_supported(reviews, old, owner, kind, payload_sha, edge, record_hash):
    """Record review does not approve a role's later, narrower biological meaning."""
    return any(review.get("disposition") in {
                   "ELIGIBLE_SAME_ROLE_SOURCE", "ELIGIBLE_RECIPE_SOURCE", "ELIGIBLE_PRIMARY_STUDY"}
               and review.get("source_record") == owner
               and review.get("source_record_sha256") == record_hash
               and review.get("assertion_type") == kind
               and review.get("assertion_sha256") == payload_sha
               and review.get("edge_id") == edge["id"]
               and review.get("source_position") == edge.get("source_position")
               and review.get("historical_review_path") == old.get("review_report")
               and bool(review.get("historical_review_sha256"))
               and review["historical_review_sha256"] == old.get("historical_review_sha256")
               and bool(review.get("review_reason", "").strip())
               for review in reviews)


def inherited_approval(old_rows, hashes, owner, kind, payload_sha, edge, assertion, role_reviews=()):
    """Match original source identity, bytes, claim and (for roles/parts) position."""
    if has_mechanical_evidence_gap(kind, assertion):
        return False
    return any(old["source_record"] == owner and old["assertion_type"] == kind
               and old["assertion_sha256"] == payload_sha
               and old["verdict"] in {"pass", "pass_with_minor_issues"}
               and hashes.get(owner) == old["record_sha256"]
               and (kind == "mapping" or old["edge_id"] == edge["id"])
               and (not kind.endswith("_roles") or inherited_role_supported(
                   role_reviews, old, owner, kind, payload_sha, edge, hashes.get(owner)))
               for old in old_rows)


def identity_mapping_supported(record, assertion):
    """A reviewed identity approves its precise relation/target, not its label's other mappings."""
    ontology = record["ontology_mapping"]
    primary_label = ontology["ontology_label"] if record["identifier"] == ontology["ontology_id"] else record["preferred_term"]
    supported_targets = {(record["identifier"], "skos:exactMatch", primary_label)}
    if record["identifier"] != ontology["ontology_id"]:
        supported_targets.add((ontology["ontology_id"], predicate_for(ontology["mapping_quality"]), ontology["ontology_label"]))
    return (assertion["subject_label"] == record["preferred_term"]
            and (assertion["object_id"], assertion["predicate_id"], assertion["object_label"]) in supported_targets)


def role_supported(item, name, record, record_hash, position, assertion):
    """Chemical identity and source position are part of the reviewed biological claim."""
    return (item.get("source_path") == name and record_hash == item.get("after_sha256")
            and record == item.get("after_record") and str(position) == item.get("source_position")
            and assertion == item.get("after_assertion"))


def validate_explicit_plans(records, hashes, roles, identity_support, component_plans, component_dispositions):
    """Fail stale evidence before it can close either findings or current assertions."""
    for item in roles:
        name = item["source_path"]
        if records.get(name) != item["after_record"] or hashes.get(name) != item["after_sha256"]:
            raise ValueError(f"Role plan no longer describes current record: {name}")
        position = int(item["source_position"]) - 1
        if records[name]["cellular_metabolic_roles"][position] != item["after_assertion"]:
            raise ValueError(f"Role plan position changed: {name}")
    for name, record in identity_support.items():
        if records.get(name) != record:
            raise ValueError(f"Identity plan no longer describes current record: {name}")
    for item in component_plans:
        name = item.get("after_path", item["source_record"])
        if records.get(name) != item["after"] or hashes.get(name) != item["after_sha256"]:
            raise ValueError(f"Component plan no longer describes current record: {name}")
    for item in component_dispositions:
        if hashes.get(item["current_record"]) != item["current_record_sha256"]:
            raise ValueError(f"Stale component disposition: {item['finding_id']}")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--bundle", type=Path, required=True)
    args = parser.parse_args()
    bundle = args.bundle.resolve()
    records = {}
    hashes = {}
    for group in ("mapped", "unmapped"):
        for path in sorted((ROOT / "data/ingredients" / group).glob("*.yaml")):
            records[relative(path)] = yaml.load(path.read_text(), Loader=yaml.CSafeLoader)
            hashes[relative(path)] = sha(path)
    historical = json.loads((BASE / "manifest.json").read_text())
    original_records = {r["source_record"]: r for r in rows(BASE / "records.tsv")}
    initial_plan = json.loads((BASE / "corrections/identity-plan.json").read_text())["records"]
    recovered = json.loads((HERE / "identities/identity-plan.json").read_text())["records"]
    roles = json.loads((HERE / "roles/cellular-role-plan.json").read_text())["records"]
    components = rows(HERE / "components/dispositions.tsv")
    current_components = json.loads((HERE / "components/applied-changes.json").read_text())
    identity_support = {item["destination_path"]: item["after_record"] for item in initial_plan + recovered if item["after_record"]["mapping_status"] == "MAPPED"}
    validate_explicit_plans(records, hashes, roles, identity_support, current_components, components)
    component_index = {r["finding_id"]: r for r in components}
    role_index = {r["before_edge_id"]: r for r in rows(HERE / "roles/role-dispositions.tsv")}
    move_map = {item["source_path"]: item["destination_path"] for item in initial_plan + recovered}
    move_map["data/ingredients/mapped/CMC_PY_Horse_Serum.yaml"] = "data/ingredients/unmapped/CMC_PY_Horse_Serum.yaml"
    lineage = []
    for name in original_records:
        if name in records:
            continue
        current = name
        visited = set()
        while current not in records:
            if current in visited or current not in move_map:
                raise ValueError(f"Unreviewed record removal: {name}")
            visited.add(current)
            current = move_map[current]
        proof = HERE / "components/applied-changes.json" if "CMC_PY" in name else HERE / "identities/identity-plan.json"
        lineage.append(dict(source_record=name, source_sha256=historical["inputs"][name], current_record=current,
                            current_sha256=hashes[current], kind="MOVE", evidence=relative(proof)))
    (HERE / "record-lineage.json").write_text(json.dumps({"moves": lineage}, indent=2) + "\n")
    relocated = {item["source_record"]: item["current_record"] for item in lineage}
    recovered_names = {item["destination_path"] for item in recovered}
    initial_decisions = {r["finding_id"]: r for r in rows(BASE / "corrections/blocker_dispositions.tsv")}
    decisions = []
    for finding in rows(BASE / "findings.tsv"):
        name = relocated.get(finding["source_record"], finding["source_record"])
        decision = dict(finding, current_record=name, current_record_sha256=hashes[name],
                        resolution_status="OPEN", resolution_reason="Historical finding remains unresolved; no blanket approval.", resolution_evidence="")
        proof = None
        reason = ""
        if records[name]["mapping_status"] == "REJECTED":
            decision["resolution_status"] = "EXCLUDED_REJECTED"
            decision["resolution_reason"] = "Source record is explicitly rejected and absent from active graph."
        elif finding["finding_id"] in initial_decisions:
            prior = initial_decisions[finding["finding_id"]]
            if prior["disposition"] == "IDENTITY_CORRECTED":
                proof = BASE / "corrections/identity-plan.json"
                reason = prior["reason"]
            elif name in recovered_names:
                proof = HERE / "identities/identity-plan.json"
                reason = "Original source identity recovered and independently matched to the published target; see identity evidence."
        elif finding["finding_id"] in component_index:
            item = component_index[finding["finding_id"]]
            if item["disposition"] != "OPEN_SOURCE_VERIFICATION":
                proof = HERE / "components/dispositions.tsv"
                reason = item["reason"]
        elif finding["kind"] == "role_evidence":
            item = role_index.get(finding["affected_unit"], {})
            if item.get("disposition") == "SUPPORTED_IN_STATED_CONTEXT":
                proof = HERE / "roles/cellular-role-plan.json"
                reason = item["reason"]
        if proof:
            decision.update(resolution_status="RESOLVED", resolution_reason=reason, resolution_evidence=relative(proof))
        decisions.append(decision)
    write_rows(HERE / "finding-dispositions.tsv", decisions)
    sssom_path = ROOT / "mappings/ingredient_mappings.sssom.tsv"
    with sssom_path.open() as stream:
        mappings = list(csv.DictReader((line for line in stream if not line.startswith("#")), delimiter="\t"))
    assertion_rows = current_assertions(records, mappings, hashes, sha(sssom_path))
    # Historical approvals require both the original source bytes and original assertion payload.
    historical_evidence = HERE / "historical-review-evidence.json"
    inherited = archive_historical_reviews(ROOT, rows(BASE / "kgx_assertions.tsv"), original_records, hashes, historical_evidence)
    archived_reports = json.loads(historical_evidence.read_text())["reports"]
    for old in inherited:
        old["historical_review_sha256"] = archived_reports[old["review_report"]]["sha256"]
    role_review_path = HERE / "roles/inherited-role-review.json"
    role_reviews = json.loads(role_review_path.read_text())["entries"]
    graph_owners = {node["id"]: node["source_record"] for node in rows(bundle / "mim_nodes.tsv", kgx=True) if node["node_kind"] == "ingredient"}
    payloads = {}
    graph_edges = rows(bundle / "mim_edges.tsv", kgx=True)
    for edge in graph_edges:
        normal = json.dumps(json.loads(edge["assertion_json"]), sort_keys=True, separators=(",", ":"))
        payloads[(edge["source_record"], edge["assertion_type"], edge["source_position"])] = (normal, edge)
    role_support = {item["source_path"]: item for item in roles}
    gyps = next(item for item in current_components if item["source_record"].endswith("/GYPS.yaml"))
    for decision in assertion_rows:
        name, kind = decision["source_record"], decision["assertion_type"]
        payload, edge = payloads[(name, kind, decision["source_position"])]
        assertion = json.loads(payload)
        packed_sha = hashlib.sha256(payload.replace("|", "\\u007c").encode()).hexdigest()
        decision.update(resolution_status="OPEN", review_reason="No current positive scientific disposition; unresolved evidence or record findings remain.", review_evidence="")
        proof = None
        reason = ""
        owner = graph_owners[assertion["subject_id"]] if kind == "mapping" else name
        if inherited_approval(inherited, hashes, owner, kind, packed_sha, edge, assertion, role_reviews):
            proof = role_review_path if kind.endswith("_roles") else historical_evidence
            reason = ("Explicit role-level source-scope review and archived reasoning apply to the exact unchanged record, assertion and position; not a fresh growth experiment."
                      if kind.endswith("_roles") else "Existing positive review applies to byte-identical source record and assertion payload; not a fresh literature review.")
        if kind == "cellular_metabolic_roles" and role_supported(role_support.get(name, {}), name, records[name], hashes[name], decision["source_position"], assertion):
            proof = HERE / "roles/cellular-role-plan.json"
            reason = "Primary evidence inspected for the explicit organism and conditions; supplied-hydrate extensions are documented inferences."
        elif kind == "mapping" and owner in identity_support:
            source_name = owner
            if records[source_name] != identity_support[source_name]:
                raise ValueError(f"Identity plan no longer describes current record: {source_name}")
            record = identity_support[source_name]
            if identity_mapping_supported(record, assertion):
                proof = HERE / "identities/identity-plan.json" if source_name in recovered_names else BASE / "corrections/identity-plan.json"
                reason = "This exact target, predicate and label are supported by the explicit chemical identity correction plan; this does not approve separate roles or other targets."
        elif kind == "component" and name.endswith("/GYPS.yaml"):
            if records[name] != gyps["after"]:
                raise ValueError("GYPS differs from reviewed recipe correction")
            proof = HERE / "components/applied-changes.json"
            reason = "Original source preparation explicitly supports the partial glucose/yeast/peptone/sulfur membership."
        if proof:
            decision.update(resolution_status="APPROVED", review_reason=reason, review_evidence=relative(proof))
    release_holds_path = HERE / "release-holds.json"
    apply_release_holds(json.loads(release_holds_path.read_text()), assertion_rows, graph_edges,
                        graph_owners, hashes, relative(release_holds_path))
    write_rows(HERE / "assertion-dispositions.tsv", assertion_rows)
    proof_files = [BASE / "manifest.json", BASE / "findings.tsv", BASE / "kgx_assertions.tsv", BASE / "records.tsv",
                   BASE / "corrections/identity-plan.json", HERE / "finding-dispositions.tsv", HERE / "assertion-dispositions.tsv",
                   HERE / "record-lineage.json", sssom_path, bundle / "manifest.json", Path(__file__),
                   historical_evidence,
                   release_holds_path,
                   ROOT / "src/mediaingredientmech/validation/semantic_release.py"]
    for folder in ("identities", "roles", "components"):
        proof_files.extend(path for path in (HERE / folder).iterdir() if path.is_file())
    inputs = {relative(path): sha(path) for path in sorted(set(proof_files))}
    blocking = adjudicate_findings(rows(BASE / "findings.tsv"), decisions, records, hashes, inputs,
                                   baseline_hashes=historical["inputs"], lineage=lineage)
    blocking_assertions = adjudicate_assertions(current_assertions(records, mappings, hashes, sha(sssom_path)), assertion_rows, inputs)
    gaps = evidence_gaps(records)
    report = dict(schema_version=1, release_verdict="FAIL" if blocking or blocking_assertions or gaps else "PASS",
                  baseline_manifest=relative(BASE / "manifest.json"), baseline_findings=relative(BASE / "findings.tsv"),
                  finding_dispositions=relative(HERE / "finding-dispositions.tsv"), assertion_dispositions=relative(HERE / "assertion-dispositions.tsv"),
                  release_holds=relative(release_holds_path),
                  record_lineage=relative(HERE / "record-lineage.json"), bundle=relative(bundle), inputs=inputs, record_inputs=hashes,
                  blocking_finding_ids=blocking, blocking_assertion_ids=blocking_assertions, evidence_gaps=gaps)
    (HERE / "current-review.json").write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps({"verdict": report["release_verdict"], "blocking_findings": len(blocking), "blocking_assertions": len(blocking_assertions), "evidence_gaps": gaps}, indent=2))


if __name__ == "__main__":
    main()
