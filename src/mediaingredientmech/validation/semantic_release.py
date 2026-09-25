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

# Negative scientific review must survive edits to both a report and its ledger.
# A change to this exact release decision requires a reviewed policy revision,
# not merely fresh hashes on a cleared or retargeted ledger (#724, #725).
FROZEN_RELEASE_HOLDS = {
    "MIM.hold:724-aromatic-trait-synonym": {
        "hold_id": "MIM.hold:724-aromatic-trait-synonym",
        "assertion_id": "MIM.review:0932a61d300f2a4adf3a44e93be1e495b0c310946cda0e85c6d51b907bd0bc90",
        "source_record": "mappings/ingredient_mappings.sssom.tsv",
        "source_record_sha256": "aa328df9bab3d7a5cf555c0200d43c6987820268f2b48757d8d203b281d3f809",
        "assertion_type": "mapping",
        "source_position": "437",
        "assertion_sha256": "54d74839ecc2eadcb8d2f8f787288f509aeeda698867ecbc38d14ead740376b6",
        "edge_id": "MIM.assertion:fb0977bd847b293ab7e79a6968678e52d36c2a11db2f88cd0a01883ab0494594",
        "owner_record": "data/ingredients/mapped/Aromatic_Compound.yaml",
        "owner_record_sha256": "1b934b840f9941aadbc305120f44c072f113ccd89745915ea190ecc588a4d9c9",
        "disposition": "WITHHOLD",
        "review_reason": (
            "The mapping's other field publishes 'degradation: aromatic compound' as a compound synonym. "
            "This is an organism trait phrase, not a compound name (#703). Withhold the entire mapping "
            "from the supported release and preserve its unchanged row in the separate backlog (#724). "
            "The broader source correction in #703 remains open."
        ),
        "issues": [
            "https://github.com/CultureBotAI/MediaIngredientMech/issues/703",
            "https://github.com/CultureBotAI/MediaIngredientMech/issues/724",
        ],
    }
}

# #729 explicitly resolves #724 after the source-level #703 correction. Keep
# the original negative decision above: neither deleting the hold nor merely
# editing its disposition may release the old payload. Only this reviewed
# corrected assertion and owner can use the resolution path.
FROZEN_RELEASE_HOLD_RESOLUTIONS = {
    "MIM.hold:724-aromatic-trait-synonym": {
        "assertion_id": "MIM.review:4174ff835afe982e4c1684fd08fa1b04cf9bc85b517fe65552badb67976df303",
        "assertion_sha256": "48222f60d12c7acb38223d3036eb44e7a7c687fb868e7dbe134a77964edb8491",
        "owner_record": "data/ingredients/mapped/Aromatic_Compound.yaml",
        "owner_record_sha256": "bbbfcafd33a763fc81b1a1bc425a4e270c791aac6e51d668726798ee16ff47b6",
        "edge_id": "MIM.assertion:6c5d59e0f710f8bef03da8bc39aad5a6cad741653eaac9adbb2690ac6db51880",
        "resolution": "SOURCE_CORRECTED",
        "evidence": "reports/sssom_completion_20260921/trait-synonym-refresh.json",
        "evidence_sha256": "00eb08f04e988859ff76605bf4567114f106f73f314fbd36f66261662c45433c",
        "mapping_review": "reports/sssom_completion_20260921/review.json",
    }
}


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
        relation = predicate
        if predicate == "skos:broadMatch":
            projected = "biolink:broad_match"
        elif predicate == "skos:narrowMatch":
            subject, obj = obj, subject
            projected = "biolink:broad_match"
            relation = "skos:broadMatch"
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
            relation,
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


def validate_release_holds(
    document, assertions, edges, owners, record_hashes, dispositions=None, evidence_path=None
):
    """Bind negative review to the exact current claim and prevent approval overrides."""
    require(document.get("schema_version") == 1, "Unsupported release-hold schema")
    required = document.get("required_hold_ids")
    holds = document.get("holds")
    require(
        isinstance(required, list) and all(isinstance(key, str) and key for key in required),
        "Missing required release-hold inventory",
    )
    require(len(required) == len(set(required)), "Duplicate required release hold")
    require(isinstance(holds, list), "Missing release holds")
    resolutions = document.get("resolutions", [])
    require(isinstance(resolutions, list), "Invalid release-hold resolutions")
    resolved_ids = [item.get("hold_id") for item in resolutions]
    require(len(resolved_ids) == len(set(resolved_ids)), "Duplicate release-hold resolution")
    hold_ids = [hold.get("hold_id") for hold in holds]
    require(len(hold_ids) == len(set(hold_ids)), "Duplicate release hold")
    require(not set(hold_ids) & set(resolved_ids), "Release hold both active and resolved")
    require(set(hold_ids + resolved_ids) == set(required), "Missing or unexpected release hold")
    by_hold_id = {hold["hold_id"]: hold for hold in holds}
    by_resolution = {item["hold_id"]: item for item in resolutions}
    for policy_id, policy in FROZEN_RELEASE_HOLDS.items():
        if policy_id in by_resolution:
            resolution = by_resolution[policy_id]
            expected = FROZEN_RELEASE_HOLD_RESOLUTIONS.get(policy_id)
            if expected is None:
                raise ValueError("Unreviewed release-hold resolution")
            require(
                all(resolution.get(k) == v for k, v in expected.items()),
                "Maintained release-hold resolution was altered or retargeted",
            )
            historical = [
                h for h in document.get("historical_holds", []) if h.get("hold_id") == policy_id
            ]
            require(
                len(historical) == 1 and all(historical[0].get(k) == v for k, v in policy.items()),
                "Original negative release review was not preserved",
            )
            original_payload = json.dumps(
                historical[0].get("assertion"), sort_keys=True, separators=(",", ":")
            )
            require(
                hashlib.sha256(original_payload.encode()).hexdigest() == policy["assertion_sha256"],
                "Original negative release payload was altered",
            )
            continue
        if policy["owner_record"] in record_hashes or policy_id in by_hold_id:
            require(policy_id in by_hold_id, "Maintained release-hold policy was removed")
            require(
                all(by_hold_id[policy_id].get(field) == value for field, value in policy.items()),
                "Maintained release-hold policy was altered or retargeted",
            )
    identities = {row["assertion_id"]: row for row in assertions}
    require(len(identities) == len(assertions), "Duplicate current assertion for release holds")
    edge_index = {
        (edge["source_record"], edge["assertion_type"], edge["source_position"]): edge
        for edge in edges
    }
    require(len(edge_index) == len(edges), "Duplicate graph assertion for release holds")
    for key, resolution in by_resolution.items():
        require(key in FROZEN_RELEASE_HOLD_RESOLUTIONS, "Unknown release-hold resolution")
        identity = identities.get(resolution.get("assertion_id"), {})
        require(
            identity.get("assertion_sha256") == resolution["assertion_sha256"],
            "Resolved release hold has no matching current assertion",
        )
        edge = edge_index.get(
            (
                identity.get("source_record"),
                identity.get("assertion_type"),
                identity.get("source_position"),
            ),
            {},
        )
        require(edge.get("id") == resolution["edge_id"], "Resolved release-hold edge changed")
        claim = json.loads(edge.get("assertion_json", "{}"))
        require(
            owners.get(claim.get("subject_id")) == resolution["owner_record"],
            "Resolved release-hold owner changed",
        )
        require(
            record_hashes.get(resolution["owner_record"]) == resolution["owner_record_sha256"],
            "Resolved release-hold source changed",
        )
    held = {}
    for hold in holds:
        key = hold.get("assertion_id")
        require(key in identities, "Missing current assertion for release hold")
        require(key not in held, "Multiple release holds for one assertion")
        identity = identities[key]
        identity_fields = (
            "assertion_id",
            "source_record",
            "source_record_sha256",
            "assertion_type",
            "source_position",
            "assertion_sha256",
        )
        require(
            all(hold.get(field) == identity.get(field) for field in identity_fields),
            f"Stale release-hold assertion: {key}",
        )
        edge = edge_index.get(
            (identity["source_record"], identity["assertion_type"], identity["source_position"])
        )
        if edge is None:
            raise ValueError("Missing release-hold graph edge")
        require(hold.get("edge_id") == edge["id"], "Stale release-hold graph edge")
        claim = json.loads(edge["assertion_json"])
        require(hold.get("assertion") == claim, "Stale release-hold payload")
        owner = (
            owners.get(claim.get("subject_id"))
            if identity["assertion_type"] == "mapping"
            else identity["source_record"]
        )
        require(owner is not None and hold.get("owner_record") == owner, "Wrong release-hold owner")
        require(
            owner in record_hashes and hold.get("owner_record_sha256") == record_hashes[owner],
            "Stale release-hold owner record",
        )
        require(hold.get("disposition") == "WITHHOLD", "Unknown release-hold disposition")
        require(bool(hold.get("review_reason", "").strip()), "Missing release-hold reason")
        issues = hold.get("issues")
        require(
            isinstance(issues, list)
            and bool(issues)
            and len(issues) == len(set(issues))
            and all(
                isinstance(issue, str) and issue.startswith("https://github.com/")
                for issue in issues
            ),
            "Missing release-hold issue provenance",
        )
        held[key] = hold
    if dispositions is not None:
        decisions = {row["assertion_id"]: row for row in dispositions}
        require(len(decisions) == len(dispositions), "Duplicate release-hold disposition")
        for key, hold in held.items():
            decision = decisions.get(key, {})
            require(decision.get("resolution_status") == "OPEN", "Active release hold was approved")
            require(
                decision.get("review_reason") == hold["review_reason"],
                "Release-hold reason was replaced",
            )
            require(
                evidence_path is not None and decision.get("review_evidence") == evidence_path,
                "Release-hold disposition lacks its bound evidence",
            )
    return held


def validate(root: Path, report_path: Path) -> dict:
    root = root.resolve()
    report = json.loads(report_path.read_text())
    require(report["schema_version"] == 1, "Unsupported review schema")
    require(bool(report.get("release_holds")), "Missing release-hold proof")
    inputs = report["inputs"]
    required_inputs = {
        report["baseline_findings"],
        report["baseline_manifest"],
        report["finding_dispositions"],
        report["assertion_dispositions"],
        report["release_holds"],
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
    current = current_assertions(
        records, mappings, record_hashes, inputs["mappings/ingredient_mappings.sssom.tsv"]
    )
    assertion_decisions = rows(local(root, report["assertion_dispositions"]))
    blocking_assertions = adjudicate_assertions(current, assertion_decisions, inputs)
    validate_release_holds(
        json.loads(local(root, report["release_holds"]).read_text()),
        current,
        edges,
        {node["id"]: node["source_record"] for node in ingredients},
        record_hashes,
        assertion_decisions,
        report["release_holds"],
    )
    hold_document = json.loads(local(root, report["release_holds"]).read_text())
    for resolution in hold_document.get("resolutions", []):
        require(
            inputs.get(resolution["evidence"]) == resolution["evidence_sha256"],
            "Release-hold resolution lacks bound correction evidence",
        )
        if resolution.get("mapping_review"):
            require(
                report.get("mapping_review") == resolution["mapping_review"],
                "Corrected release hold requires its mapping-specific review",
            )
    if report.get("mapping_review"):
        from mediaingredientmech.export.reviewed_sssom import load_review

        mapping_review_path = report["mapping_review"]
        require(mapping_review_path in inputs, "Missing bound mapping-specific review")
        reviewed = load_review(root, local(root, mapping_review_path))
        require(
            reviewed["review"]["source_sssom"] == "mappings/ingredient_mappings.sssom.tsv"
            and reviewed["review"]["source_sha256"]
            == inputs["mappings/ingredient_mappings.sssom.tsv"]
            and reviewed["rows"] == mappings,
            "Mapping-specific review describes a different source or payload",
        )
        mapping_decisions = {
            int(d["source_position"]): d
            for d in assertion_decisions
            if d["assertion_type"] == "mapping"
        }
        require(
            len(mapping_decisions) == len(reviewed["decisions"]),
            "Graph mapping review coverage differs from SSSOM",
        )
        for decision in reviewed["decisions"]:
            actual_mapping = mapping_decisions[decision["source_position"]]
            expected_status = "APPROVED" if decision["disposition"] == "SUPPORTED" else "OPEN"
            require(
                actual_mapping["resolution_status"] == expected_status
                and actual_mapping["review_reason"] == decision["review_reason"]
                and actual_mapping["review_evidence"] == mapping_review_path,
                "Graph mapping disposition overrides the mapping-specific review",
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
