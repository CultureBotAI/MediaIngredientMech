"""Verify a content-bound semantic review without treating integrity as approval.

The disposition ledger must account for every finding in its historical baseline.
Unresolved major findings, including components and recipe identity, block release.
This checks the review contract; a curator must still assess the cited science.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
from collections import Counter
from pathlib import Path

import yaml

from mediaingredientmech.sssom_grading import predicate_for
from mediaingredientmech.validation.write_validated import DEFAULT_SCHEMA_PATH


def require(condition: bool, message: str) -> None:
    """Keep validation enabled under Python's optimized mode, too."""
    if not condition:
        raise ValueError(message)


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def local(root: Path, name: str) -> Path:
    path = (root / name).resolve()
    require(path.is_relative_to(root.resolve()), f"Path outside repository: {name}")
    return path


def rows(path: Path, *, kgx: bool = False) -> list[dict[str, str]]:
    with path.open() as stream:
        return list(
            csv.DictReader(
                stream, delimiter="\t", quoting=csv.QUOTE_NONE if kgx else csv.QUOTE_MINIMAL
            )
        )


def evidence_gaps(records: dict[str, dict]) -> dict[str, int]:
    """Recompute the unresolved evidence classes; supplied counts are not trusted."""
    result: Counter[str] = Counter()
    for record in records.values():
        if record.get("mapping_status") == "REJECTED":
            continue
        if record.get("mapping_status") == "AMBIGUOUS":
            result["ambiguous_identities"] += 1
        if (record.get("component_assertion") or {}).get("method") in {
            "ABBREVIATION_EXPANSION",
            "CURATED_INTERPRETATION",
        }:
            result["components_requiring_source_verification"] += len(
                record.get("components") or []
            )
        for facet in (
            "nutritional_roles",
            "physicochemical_roles",
            "cellular_metabolic_roles",
            "community_organism_roles",
        ):
            for role in record.get(facet) or []:
                evidence = role.get("evidence") or []
                if not evidence:
                    result["roles_without_evidence"] += 1
                elif all(e.get("reference_type") == "COMPUTATIONAL_PREDICTION" for e in evidence):
                    result["prediction_only_roles"] += 1
                if facet == "cellular_metabolic_roles" and not role.get("metabolic_context"):
                    result["cellular_roles_without_context"] += 1
    return dict(sorted(result.items()))


def assertion_inventory(records: dict[str, dict], mappings: list[dict[str, str]]) -> Counter:
    """Independently enumerate each assertion payload, including repeated claims."""
    inventory: Counter = Counter()

    def add(source, kind, position, assertion):
        payload = json.dumps(assertion, sort_keys=True, separators=(",", ":"))
        inventory[(source, kind, str(position), payload)] += 1

    for name, record in records.items():
        if record["mapping_status"] == "REJECTED":
            continue
        for facet in (
            "nutritional_roles",
            "physicochemical_roles",
            "cellular_metabolic_roles",
            "community_organism_roles",
            "environmental_context",
        ):
            for position, assertion in enumerate(record.get(facet) or [], 1):
                add(
                    name,
                    "environment" if facet == "environmental_context" else facet,
                    position,
                    assertion,
                )
        for position, part in enumerate(record.get("components") or [], 1):
            add(
                name,
                "component",
                position,
                {"component": part, "component_assertion": record["component_assertion"]},
            )
        if record.get("culturemech_reference"):
            add(name, "recipe_reference", 1, record["culturemech_reference"])
    for position, mapping in enumerate(mappings, 1):
        add("mappings/ingredient_mappings.sssom.tsv", "mapping", position, mapping)
    return inventory


def current_assertions(records, mappings, record_hashes, sssom_sha):
    """Return content identities only; this function never grants scientific approval."""
    result = []
    hashes = {**record_hashes, "mappings/ingredient_mappings.sssom.tsv": sssom_sha}
    for (source, kind, position, payload), count in sorted(
        assertion_inventory(records, mappings).items()
    ):
        require(count == 1, "Repeated assertion inventory key")
        payload_sha = hashlib.sha256(payload.encode()).hexdigest()
        identity = json.dumps([source, kind, position, payload_sha], separators=(",", ":"))
        result.append(
            {
                "assertion_id": "MIM.review:" + hashlib.sha256(identity.encode()).hexdigest(),
                "source_record": source,
                "source_record_sha256": hashes[source],
                "assertion_type": kind,
                "source_position": position,
                "assertion_sha256": payload_sha,
            }
        )
    return result


def adjudicate_assertions(expected, dispositions, inputs):
    """Every current assertion needs its own current, explicit review disposition."""
    wanted = {row["assertion_id"]: row for row in expected}
    actual = {row["assertion_id"]: row for row in dispositions}
    require(len(wanted) == len(expected), "Duplicate expected assertion")
    require(len(actual) == len(dispositions), "Duplicate assertion disposition")
    require(wanted.keys() == actual.keys(), "Incomplete current assertion review coverage")
    blocking = []
    for key, identity in wanted.items():
        decision = actual[key]
        require(
            all(decision.get(field) == value for field, value in identity.items()),
            f"Stale current assertion review: {key}",
        )
        status = decision.get("resolution_status")
        require(status in {"APPROVED", "OPEN"}, f"Unknown assertion disposition: {key}")
        if status == "OPEN":
            blocking.append(key)
        else:
            require(
                bool(decision.get("review_reason", "").strip()),
                f"Missing assertion review reason: {key}",
            )
            require(
                bool(decision.get("review_evidence")) and decision["review_evidence"] in inputs,
                f"Assertion approval lacks hashed evidence: {key}",
            )
    return sorted(blocking)


def _packed(value):
    return json.dumps(value, ensure_ascii=True, sort_keys=True, separators=(",", ":")).replace(
        "|", "\\u007c"
    )


def verify_projection(records, mappings, nodes, edges):
    """Check the graph's scientific endpoints and fields against an independent projection.

    Do not import the exporter: a bug in its direction or endpoint logic must not
    become its own expected answer. JSON payload equality alone is insufficient.
    """
    node_by_id = {node["id"]: node for node in nodes}
    require(len(node_by_id) == len(nodes), "Duplicate graph node ID")
    expected_nodes = {}
    references: dict[str, set[str]] = {}
    local_ids = {}
    categories = {
        "SINGLE_INGREDIENT": "biolink:ChemicalEntity",
        "UNDEFINED_MIXTURE": "biolink:ComplexMolecularMixture",
        "STOCK_SOLUTION": "biolink:ChemicalMixture",
        "NAMED_MEDIUM": "biolink:ChemicalMixture",
    }
    for name, record in records.items():
        if record["mapping_status"] == "REJECTED":
            continue
        if record["mapping_status"] == "MAPPED":
            candidates = {
                row["subject_id"]
                for row in mappings
                if row["subject_label"] == record["preferred_term"]
            }
            require(len(candidates) == 1, f"No unique mapping subject for {name}")
            identifier = next(iter(candidates))
            own = [row for row in mappings if row["subject_id"] == identifier]
            require(
                any(
                    row["object_id"] == record["identifier"]
                    and row["predicate_id"] == "skos:exactMatch"
                    for row in own
                ),
                f"Mapping does not identify the current source record: {name}",
            )
            grounding = record.get("ontology_mapping") or {}
            if grounding.get("ontology_id"):
                target = grounding["ontology_id"]
                predicate = (
                    "skos:exactMatch"
                    if target == record["identifier"]
                    else predicate_for(grounding.get("mapping_quality"))
                )
                require(
                    any(
                        row["object_id"] == target and row["predicate_id"] == predicate
                        for row in own
                    ),
                    f"Mapping does not match the current source grounding: {name}",
                )
        else:
            require(
                record["mapping_status"] in {"UNMAPPED", "AMBIGUOUS"}, "Unsupported active status"
            )
            identifier = "MIM.unmapped:" + record["identifier"]
        require(identifier not in expected_nodes, "Ingredient node identity collision")
        local_ids[name] = identifier
        expected_nodes[identifier] = {
            "name": record["preferred_term"],
            "node_kind": "ingredient",
            "category": categories.get(record.get("ingredient_type"), "biolink:NamedThing"),
            "source_record": name,
            "record_identifier": record["identifier"],
            "mapping_status": record["mapping_status"],
            "ingredient_type": record.get("ingredient_type", ""),
        }

    def reference(identifier, label):
        require(
            identifier not in expected_nodes
            or expected_nodes[identifier]["node_kind"] == "external_reference",
            "External reference collides with a local node",
        )
        expected_nodes[identifier] = {
            "node_kind": "external_reference",
            "category": "biolink:NamedThing",
        }
        references.setdefault(identifier, set())
        if label:
            references[identifier].add(label)

    expected_edges = {}

    def edge(source, kind, position, subject, predicate, obj, relation, assertion, **attributes):
        confidence = assertion.get("confidence", "")
        row = {
            "subject": subject,
            "predicate": predicate,
            "object": obj,
            "relation": relation,
            "primary_knowledge_source": "MIM:ingredients",
            "provided_by": "MIM:ingredients",
            "assertion_type": kind,
            "source_record": source,
            "source_position": str(position),
            "confidence": "" if confidence is None else str(confidence),
            "assertion_json": _packed(assertion),
            **attributes,
        }
        row["id"] = "MIM.assertion:" + hashlib.sha256(_packed(row).encode()).hexdigest()
        key = (source, kind, str(position))
        require(key not in expected_edges, "Duplicate expected graph assertion")
        expected_edges[key] = row

    for position, mapping in enumerate(mappings, 1):
        subject, obj, predicate = (
            mapping["subject_id"],
            mapping["object_id"],
            mapping["predicate_id"],
        )
        require(subject in local_ids.values(), "Mapping subject is not an active ingredient")
        reference(obj, mapping["object_label"])
        if predicate == "skos:broadMatch":
            projected = "biolink:subclass_of"
        elif predicate == "skos:narrowMatch":
            subject, obj = obj, subject
            projected = "biolink:subclass_of"
        else:
            require(
                predicate in {"skos:exactMatch", "skos:closeMatch"}, "Unsupported mapping relation"
            )
            projected = (
                "biolink:exact_match" if predicate == "skos:exactMatch" else "biolink:close_match"
            )
        edge(
            "mappings/ingredient_mappings.sssom.tsv",
            "mapping",
            position,
            subject,
            projected,
            obj,
            predicate,
            mapping,
        )
    enums = {
        "nutritional_roles": "NutritionalRoleEnum",
        "physicochemical_roles": "PhysicochemicalRoleEnum",
        "cellular_metabolic_roles": "CellularMetabolicRoleEnum",
        "community_organism_roles": "CommunityOrganismRoleEnum",
    }
    schema = yaml.safe_load(DEFAULT_SCHEMA_PATH.read_text())
    for name, subject in local_ids.items():
        record = records[name]
        for facet, enum in enums.items():
            for position, role in enumerate(record.get(facet) or [], 1):
                obj = f"MIM.role:{enum}.{role['role']}"
                community = facet == "community_organism_roles"
                expected_nodes[obj] = {
                    "name": role["role"],
                    "node_kind": "role",
                    "category": "biolink:Attribute" if community else "biolink:ChemicalRole",
                    "definition_json": _packed(
                        schema["enums"][enum]["permissible_values"][role["role"]]
                    ),
                }
                publications = {
                    prefix + str(item[key])
                    for item in role.get("evidence", [])
                    for key, prefix in (("doi", "doi:"), ("pmid", "PMID:"), ("url", ""))
                    if item.get(key)
                }
                edge(
                    name,
                    facet,
                    position,
                    subject,
                    "biolink:has_attribute" if community else "biolink:has_chemical_role",
                    obj,
                    "MIM.vocab:" + facet,
                    role,
                    publications="|".join(sorted(publications)),
                    metabolic_context=role.get("metabolic_context", ""),
                )
        for position, component in enumerate(record.get("components") or [], 1):
            obj = component.get("component_id")
            if obj:
                reference(obj, component["component_name"])
            else:
                obj = (
                    "MIM.component:"
                    + hashlib.sha256(
                        _packed([subject, component["component_name"]]).encode()
                    ).hexdigest()
                )
                require(obj not in expected_nodes, "Unresolved component identity collision")
                expected_nodes[obj] = {
                    "name": component["component_name"],
                    "category": "biolink:NamedThing",
                    "node_kind": "unresolved_component",
                    "source_record": name,
                }
            assertion = record["component_assertion"]
            edge(
                name,
                "component",
                position,
                subject,
                "biolink:has_part",
                obj,
                "BFO:0000051",
                {"component": component, "component_assertion": assertion},
                reference_scope=component["reference_scope"],
                concentration_value=component.get("concentration_value", ""),
                concentration_unit=component.get("concentration_unit", ""),
                completeness=assertion["completeness"],
                assertion_method=assertion["method"],
            )
        for position, context in enumerate(record.get("environmental_context") or [], 1):
            obj = context["environment_term"]
            reference(obj, context.get("environment_label", ""))
            edge(
                name,
                "environment",
                position,
                subject,
                "MIM.vocab:environmental_context",
                obj,
                "MIM.vocab:environmental_context",
                context,
            )
        if record.get("culturemech_reference"):
            claim = record["culturemech_reference"]
            reference(claim["medium_id"], claim.get("medium_name", ""))
            relation = "MIM.vocab:recipe_" + claim["relationship"].lower()
            edge(
                name, "recipe_reference", 1, subject, relation, claim["medium_id"], relation, claim
            )
    for identifier, labels in references.items():
        expected_nodes[identifier].update(
            name=min(labels) if labels else identifier,
            reference_labels_json=_packed(sorted(labels)),
        )
    require(
        node_by_id.keys() == expected_nodes.keys(),
        "Graph node identity coverage differs from source",
    )
    for identifier, expected in expected_nodes.items():
        node = node_by_id[identifier]
        require(node.get("provided_by") == "MIM:ingredients", "Incorrect graph node provider")
        require(
            all(node.get(key, "") == str(value) for key, value in expected.items()),
            f"Graph node projection differs from source: {identifier}",
        )
    actual_edges = {
        (row["source_record"], row["assertion_type"], row["source_position"]): row for row in edges
    }
    require(len(actual_edges) == len(edges), "Duplicate graph assertion")
    require(actual_edges.keys() == expected_edges.keys(), "Graph edge coverage differs from source")
    optional = {
        "publications",
        "metabolic_context",
        "reference_scope",
        "concentration_value",
        "concentration_unit",
        "completeness",
        "assertion_method",
    }
    for key, expected in expected_edges.items():
        actual = actual_edges[key]
        require(
            actual["subject"] in node_by_id and actual["object"] in node_by_id,
            "Undeclared graph endpoint",
        )
        require(
            all(
                actual.get(field, "") == str(expected.get(field, ""))
                for field in expected.keys() | optional
            ),
            f"Graph edge projection differs from source: {key}",
        )


def adjudicate_findings(
    baseline: list[dict[str, str]],
    dispositions: list[dict[str, str]],
    records: dict[str, dict],
    record_hashes: dict[str, str],
    inputs: dict[str, str],
    baseline_hashes: dict[str, str] | None = None,
    lineage: list[dict[str, str]] | None = None,
) -> list[str]:
    """Return blocking IDs after checking complete, current review dispositions."""
    original = {row["finding_id"]: row for row in baseline}
    current = {row["finding_id"]: row for row in dispositions}
    require(len(original) == len(baseline), "Duplicate baseline finding")
    require(len(current) == len(dispositions), "Duplicate finding disposition")
    require(set(original) == set(current), "Incomplete finding coverage")
    moves = {}
    for item in lineage or []:
        source, target = item["source_record"], item["current_record"]
        require(source != target, "Lineage must change the record path")
        require(source not in moves, "Duplicate source lineage")
        require(target in records, "Lineage target is not a current record")
        require(
            baseline_hashes is not None and baseline_hashes.get(source) == item["source_sha256"],
            "Lineage source is not bound to the historical baseline",
        )
        require(record_hashes[target] == item["current_sha256"], "Stale lineage target")
        require(
            bool(item.get("evidence")) and item["evidence"] in inputs,
            "Lineage lacks hashed evidence",
        )
        require(item["kind"] in {"MOVE", "MERGE"}, "Unknown lineage kind")
        if item["kind"] == "MOVE":
            require(source not in records, "Moved source is still a current record")
        else:
            require(
                source in records and records[source].get("mapping_status") == "REJECTED",
                "Merge source must remain an explicit rejected tombstone",
            )
            require(
                records[source].get("representative") == records[target]["identifier"],
                "Merge representative differs from lineage target",
            )
        moves[source] = target
    blocking = []
    for finding_id, finding in original.items():
        decision = current[finding_id]
        require(
            all(decision.get(key) == value for key, value in finding.items()),
            f"Historical finding changed: {finding_id}",
        )
        name = decision["current_record"]
        source = finding["source_record"]
        require(
            name == source or moves.get(source) == name,
            f"Finding record continuity is unproven: {finding_id}",
        )
        require(name in records, f"Missing current record: {finding_id}")
        require(
            decision["current_record_sha256"] == record_hashes[name],
            f"Stale finding disposition: {finding_id}",
        )
        status = decision["resolution_status"]
        require(status in {"OPEN", "RESOLVED", "EXCLUDED_REJECTED"}, "Unknown disposition")
        if status == "EXCLUDED_REJECTED":
            require(records[name].get("mapping_status") == "REJECTED", "Active record excluded")
        elif status == "RESOLVED":
            require(
                bool(decision.get("resolution_reason", "").strip()), "Missing resolution reason"
            )
            require(
                bool(decision.get("resolution_evidence"))
                and decision["resolution_evidence"] in inputs,
                f"Resolution lacks hashed evidence: {finding_id}",
            )
        elif records[name].get("mapping_status") != "REJECTED" and finding["severity"] in {
            "major",
            "blocker",
        }:
            blocking.append(finding_id)
    return sorted(blocking)


def validate(root: Path, report_path: Path) -> dict:
    root = root.resolve()
    report = json.loads(report_path.read_text())
    require(report["schema_version"] == 1, "Unsupported review schema")
    inputs = report["inputs"]
    required_inputs = {
        report["baseline_findings"],
        report["baseline_manifest"],
        report["finding_dispositions"],
        report["assertion_dispositions"],
        "mappings/ingredient_mappings.sssom.tsv",
        report["bundle"] + "/manifest.json",
    }
    if report.get("record_lineage"):
        required_inputs.add(report["record_lineage"])
    require(required_inputs <= inputs.keys(), "Missing required review input")
    for name, expected in inputs.items():
        require(sha(local(root, name)) == expected, f"Stale review input: {name}")
    baseline_manifest = json.loads(local(root, report["baseline_manifest"]).read_text())
    baseline_name = Path(report["baseline_findings"]).name
    require(
        baseline_manifest["members"].get(baseline_name, {}).get("sha256")
        == inputs[report["baseline_findings"]],
        "Historical baseline findings do not match the baseline manifest",
    )
    paths = {
        str(path.relative_to(root)): path
        for group in ("mapped", "unmapped")
        for path in (root / "data/ingredients" / group).glob("*.yaml")
    }
    require(bool(paths), "Empty ingredient corpus")
    require(paths.keys() == report["record_inputs"].keys(), "Incomplete record coverage")
    record_hashes = {name: sha(path) for name, path in paths.items()}
    require(record_hashes == report["record_inputs"], "Stale record review")
    records = {
        name: yaml.load(path.read_text(), Loader=getattr(yaml, "CSafeLoader", yaml.SafeLoader))
        for name, path in paths.items()
    }
    bundle = local(root, report["bundle"])
    manifest = json.loads((bundle / "manifest.json").read_text())
    require(
        {"mim_nodes.tsv", "mim_edges.tsv"} <= manifest["members"].keys(),
        "Missing required graph member",
    )
    require(set(record_hashes) <= manifest["inputs"].keys(), "Graph omits source-record provenance")
    for name, expected in manifest["inputs"].items():
        require(sha(local(root, name)) == expected, f"Stale graph source: {name}")
    for name, details in manifest["members"].items():
        require(sha(local(bundle, name)) == details["sha256"], f"Stale graph member: {name}")
    nodes = rows(bundle / "mim_nodes.tsv", kgx=True)
    ingredients = [n for n in nodes if n["node_kind"] == "ingredient"]
    active = {name for name, record in records.items() if record["mapping_status"] != "REJECTED"}
    require(
        len(ingredients) == len(active) and {n["source_record"] for n in ingredients} == active,
        "Incomplete graph ingredient coverage",
    )
    for node in ingredients:
        require(
            json.loads(node["record_json"]) == records[node["source_record"]],
            "Graph ingredient payload differs from reviewed source",
        )
    with (root / "mappings/ingredient_mappings.sssom.tsv").open() as stream:
        mappings = list(
            csv.DictReader((line for line in stream if not line.startswith("#")), delimiter="\t")
        )
    edges = rows(bundle / "mim_edges.tsv", kgx=True)
    actual = Counter(
        (
            edge["source_record"],
            edge["assertion_type"],
            edge["source_position"],
            json.dumps(json.loads(edge["assertion_json"]), sort_keys=True, separators=(",", ":")),
        )
        for edge in edges
    )
    require(actual == assertion_inventory(records, mappings), "Incomplete graph assertion coverage")
    verify_projection(records, mappings, nodes, edges)
    lineage = (
        json.loads(local(root, report["record_lineage"]).read_text())["moves"]
        if report.get("record_lineage")
        else []
    )
    blocking = adjudicate_findings(
        rows(local(root, report["baseline_findings"])),
        rows(local(root, report["finding_dispositions"])),
        records,
        record_hashes,
        inputs,
        baseline_manifest["inputs"],
        lineage,
    )
    blocking_assertions = adjudicate_assertions(
        current_assertions(
            records, mappings, record_hashes, inputs["mappings/ingredient_mappings.sssom.tsv"]
        ),
        rows(local(root, report["assertion_dispositions"])),
        inputs,
    )
    gaps = evidence_gaps(records)
    verdict = "FAIL" if blocking or gaps or blocking_assertions else "PASS"
    require(report["blocking_finding_ids"] == blocking, "Incorrect blocking finding inventory")
    require(
        report["blocking_assertion_ids"] == blocking_assertions,
        "Incorrect blocking assertion inventory",
    )
    require(report["evidence_gaps"] == gaps, "Incorrect evidence-gap counts")
    require(report["release_verdict"] == verdict, "False semantic release verdict")
    return {
        "integrity": "PASS",
        "semantic_release": verdict,
        "blocking_findings": len(blocking),
        "blocking_assertions": len(blocking_assertions),
        "evidence_gaps": gaps,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path.cwd())
    parser.add_argument("--report", type=Path, required=True)
    parser.add_argument("--require-pass", action="store_true")
    args = parser.parse_args()
    result = validate(args.root, args.report)
    print(json.dumps(result, indent=2))
    if args.require_pass and result["semantic_release"] != "PASS":
        raise SystemExit(1)


if __name__ == "__main__":
    main()
