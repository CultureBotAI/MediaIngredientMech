"""#1265 exact graph-address projection with inherited positive AND negative review.

The full historical report remains authoritative at its original bytes. This
successor is not a new scientific assessment, and never changes an OPEN decision,
release hold, evidence gap or the full graph's FAIL verdict into approval.
"""

from __future__ import annotations

import csv
import gzip
import io
from copy import deepcopy
from pathlib import Path

from mediaingredientmech.identity_projection import (
    MANIFEST,
    MAPPING_REVIEW,
    REPORT_ROOT,
    Proof,
    document,
    encode,
    exact,
    git_files,
    projection_header,
    prove_identity_migration,
    require,
    safe_path,
    sha,
)
from mediaingredientmech.stable_ids import MIM_PREFIX

OLD_REVIEW = "reports/semantic_review_20260921/resolution/current-review.json"
OLD_REVIEW_SHA = "58bc08f9806cfeaae5760221dbd4d28a7c07b7220ee4ddc9cab85518a5f16434"
REVIEW = REPORT_ROOT + "/semantic-review.json"
DISPOSITIONS = REPORT_ROOT + "/assertion-dispositions.tsv"
ARCHIVE = REPORT_ROOT + "/historical-graph/"
BUNDLE = "output/mim-kgx-710-full"
GRAPH_FILES = ("manifest.json", "mim_nodes.tsv", "mim_edges.tsv", "excluded_records.tsv")
MAX_GRAPH_BYTES = 32 * 1024 * 1024


def read_table(raw: bytes) -> list[dict[str, str]]:
    reader = csv.DictReader(io.StringIO(raw.decode(), newline=""), delimiter="\t")
    require(
        reader.fieldnames is not None and len(reader.fieldnames) == len(set(reader.fieldnames)),
        "invalid graph table columns",
    )
    result = list(reader)
    require(
        all(None not in row and all(value is not None for value in row.values()) for row in result),
        "invalid graph row width",
    )
    return result


def table(rows: list[dict]) -> bytes:
    require(bool(rows), "empty assertion dispositions")
    out = io.StringIO(newline="")
    writer = csv.DictWriter(out, fieldnames=list(rows[0]), delimiter="\t", lineterminator="\n")
    writer.writeheader()
    writer.writerows(rows)
    return out.getvalue().encode()


def packed(value) -> str:
    import json

    return json.dumps(value, ensure_ascii=True, sort_keys=True, separators=(",", ":")).replace(
        "|", "\\u007c"
    )


def edge_identity(row: dict[str, str]) -> str:
    """Independent reconstruction of the native assertion identity's typed fields."""
    fields = (
        "subject",
        "predicate",
        "object",
        "relation",
        "primary_knowledge_source",
        "provided_by",
        "assertion_type",
        "source_record",
        "source_position",
        "confidence",
        "assertion_json",
    )
    projected = {key: row[key] for key in fields}
    kind = row["assertion_type"]
    assertion = document(row["assertion_json"].encode())
    if kind in {
        "nutritional_roles",
        "physicochemical_roles",
        "cellular_metabolic_roles",
        "community_organism_roles",
    }:
        projected.update(
            publications=row["publications"], metabolic_context=row["metabolic_context"]
        )
    elif kind == "component":
        component, description = assertion["component"], assertion["component_assertion"]
        projected.update(
            reference_scope=component["reference_scope"],
            concentration_value=component.get("concentration_value", ""),
            concentration_unit=component.get("concentration_unit", ""),
            completeness=description["completeness"],
            assertion_method=description["method"],
        )
    else:
        require(
            kind in {"mapping", "environment", "recipe_reference"}, "unknown graph assertion type"
        )
    return "MIM.assertion:" + sha(packed(projected).encode())


def project_graph(
    proof: Proof, old_nodes: list[dict], old_edges: list[dict], old_excluded: list[dict]
) -> tuple[list[dict], list[dict], list[dict]]:
    """Only typed source-address fields change; all biological payloads stay exact."""
    aliases = {}
    for node in old_nodes:
        if node["node_kind"] == "ingredient":
            owner = node["source_record"]
            require(
                exact(
                    document(node["record_json"].encode()), proof.transition["old_records"][owner]
                ),
                "historical graph source record differs",
            )
            aliases[node["id"]] = proof.transition["new_records"][owner]["mim_id"]
    owner_ids = {
        node["source_record"]: aliases[node["id"]]
        for node in old_nodes
        if node["node_kind"] == "ingredient"
    }
    for node in old_nodes:
        if node["node_kind"] == "unresolved_component":
            aliases[node["id"]] = "MIM.component:" + sha(
                packed([owner_ids[node["source_record"]], node["name"]]).encode()
            )
    nodes = deepcopy(old_nodes)
    for node in nodes:
        node["id"] = aliases.get(node["id"], node["id"])
        if node["node_kind"] == "ingredient":
            node["record_json"] = packed(proof.transition["new_records"][node["source_record"]])
    edges = deepcopy(old_edges)
    for edge in edges:
        require(edge["id"] == edge_identity(edge), "historical graph assertion identity differs")
        edge["subject"] = aliases.get(edge["subject"], edge["subject"])
        edge["object"] = aliases.get(edge["object"], edge["object"])
        if edge["assertion_type"] == "mapping":
            position = int(edge["source_position"]) - 1
            require(
                exact(
                    document(edge["assertion_json"].encode()),
                    proof.transition["old_rows"][position],
                ),
                "historical graph mapping differs",
            )
            edge["assertion_json"] = packed(proof.transition["rows"][position])
        edge["id"] = edge_identity(edge)
    excluded = deepcopy(old_excluded)
    for row in excluded:
        require(
            exact(
                document(row["record_json"].encode()),
                proof.transition["old_records"][row["source_record"]],
            ),
            "historical rejected record differs",
        )
        row["record_json"] = packed(proof.transition["new_records"][row["source_record"]])
    return (
        sorted(nodes, key=lambda row: row["id"]),
        sorted(edges, key=lambda row: row["id"]),
        excluded,
    )


def old_graph(
    proof: Proof, *, seed: Path | None = None
) -> tuple[dict[str, bytes], dict[str, bytes]]:
    raw, archives = {}, {}
    for name in GRAPH_FILES:
        archive_name = ARCHIVE + name + ".gz"
        if seed is not None:
            content = safe_path(seed, name).read_bytes()
            archives[archive_name] = gzip.compress(content, mtime=0)
        else:
            archives[archive_name] = safe_path(proof.root, archive_name).read_bytes()
            with gzip.GzipFile(fileobj=io.BytesIO(archives[archive_name])) as stream:
                content = stream.read(MAX_GRAPH_BYTES + 1)
        require(len(content) <= MAX_GRAPH_BYTES, "historical graph member exceeds bound")
        raw[name] = content
    return raw, archives


def products(proof: Proof, *, seed: Path | None = None) -> dict[str, bytes]:
    from mediaingredientmech.validation.semantic_release import current_assertions, evidence_gaps

    original_raw = git_files(proof.root, [OLD_REVIEW])[OLD_REVIEW]
    require(sha(original_raw) == OLD_REVIEW_SHA, "historical semantic authority differs")
    original = document(original_raw)
    require(
        safe_path(proof.root, OLD_REVIEW).read_bytes() == original_raw,
        "historical semantic review changed",
    )
    baseline, archives = old_graph(proof, seed=seed)
    old_manifest = document(baseline["manifest.json"])
    require(
        sha(baseline["manifest.json"]) == original["inputs"][BUNDLE + "/manifest.json"],
        "historical graph is not bound by the scientific review",
    )
    for name in GRAPH_FILES[1:]:
        require(
            sha(baseline[name]) == old_manifest["members"][name]["sha256"],
            "historical graph member differs",
        )
    declared = {**original["inputs"], **original["record_inputs"]}
    declared.pop(BUNDLE + "/manifest.json")
    historical = git_files(proof.root, list(declared))
    require(
        all(sha(historical[name]) == digest for name, digest in declared.items()),
        "historical semantic input differs from fixed baseline",
    )
    for name, raw in historical.items():
        if name.startswith("reports/"):
            require(
                safe_path(proof.root, name).read_bytes() == raw,
                "historical semantic report changed",
            )
            proof.snapshots[name] = raw
    proof.snapshots[OLD_REVIEW] = original_raw
    old_nodes, old_edges, old_excluded = [read_table(baseline[name]) for name in GRAPH_FILES[1:]]
    expected_nodes, expected_edges, expected_excluded = project_graph(
        proof, old_nodes, old_edges, old_excluded
    )
    current_raw = {
        name: safe_path(proof.root, BUNDLE + "/" + name).read_bytes() for name in GRAPH_FILES
    }
    current = document(current_raw["manifest.json"])
    for name in GRAPH_FILES[1:]:
        require(
            sha(current_raw[name]) == current["members"][name]["sha256"],
            "current graph member differs",
        )
    for name, expected in zip(
        GRAPH_FILES[1:], (expected_nodes, expected_edges, expected_excluded), strict=True
    ):
        require(
            exact(read_table(current_raw[name]), expected),
            "graph changes beyond administrative identity: " + name,
        )
    expected_prefix = dict(old_manifest["curie_map"], MIM=MIM_PREFIX)
    require(
        exact(current["counts"], old_manifest["counts"])
        and exact(current["curie_map"], expected_prefix)
        and exact(current["limitations"], old_manifest["limitations"]),
        "graph scientific metadata changed",
    )
    for name, digest in current["inputs"].items():
        raw = safe_path(proof.root, name).read_bytes()
        require(sha(raw) == digest, "stale current graph input")
        proof.snapshots[name] = raw
    for name, digest in current["implementation"].items():
        raw = safe_path(proof.root, "src/mediaingredientmech/" + name).read_bytes()
        require(sha(raw) == digest, "stale graph implementation")
        proof.snapshots["src/mediaingredientmech/" + name] = raw
    old_dispositions = read_table(historical[original["assertion_dispositions"]])
    old_assertions = current_assertions(
        proof.transition["old_records"],
        proof.transition["old_rows"],
        {name: sha(raw) for name, raw in proof.before.items()},
        sha(proof.before["mappings/ingredient_mappings.sssom.tsv"]),
    )
    new_assertions = current_assertions(
        proof.transition["new_records"],
        proof.transition["rows"],
        {name: sha(raw) for name, raw in proof.after.items()},
        sha(proof.after["mappings/ingredient_mappings.sssom.tsv"]),
    )
    decisions = project_decisions(old_assertions, new_assertions, old_dispositions)
    gaps = evidence_gaps(proof.transition["new_records"])
    require(exact(gaps, original["evidence_gaps"]), "evidence gaps changed")
    negatives = sorted(
        row["assertion_id"] for row in decisions if row["resolution_status"] == "OPEN"
    )
    require(
        len(negatives) == len(original["blocking_assertion_ids"]),
        "negative assertion holds changed",
    )
    disposition_raw = table(decisions)
    inputs = {name: sha(raw) for name, raw in archives.items()}
    inputs.update({BUNDLE + "/" + name: sha(raw) for name, raw in current_raw.items()})
    inputs.update(
        {
            MANIFEST: sha(proof.snapshots[MANIFEST]),
            OLD_REVIEW: sha(original_raw),
            DISPOSITIONS: sha(disposition_raw),
        }
    )
    report = {
        "schema_version": 1,
        "identity_projection": projection_header(proof, OLD_REVIEW, original_raw),
        "bundle": BUNDLE,
        "assertion_dispositions": DISPOSITIONS,
        "mapping_review": MAPPING_REVIEW,
        "release_verdict": original["release_verdict"],
        "inherited_release_holds": original["release_holds"],
        "inherited_finding_dispositions": original["finding_dispositions"],
        "blocking_finding_ids": original["blocking_finding_ids"],
        "blocking_assertion_ids": negatives,
        "evidence_gaps": gaps,
        "inputs": dict(sorted(inputs.items())),
        "record_inputs": {
            name: sha(proof.after[name]) for name in sorted(proof.transition["new_records"])
        },
    }
    proof.snapshots.update({BUNDLE + "/" + name: raw for name, raw in current_raw.items()})
    proof.recheck()
    return {**archives, DISPOSITIONS: disposition_raw, REVIEW: encode(report)}


def project_decisions(
    old_assertions: list[dict], new_assertions: list[dict], old_decisions: list[dict]
) -> list[dict]:
    def key(row):
        return row["source_record"], row["assertion_type"], str(row["source_position"])

    old, new, decisions = (
        {key(row): row for row in group}
        for group in (old_assertions, new_assertions, old_decisions)
    )
    require(
        len(old) == len(old_assertions)
        and len(new) == len(new_assertions)
        and len(decisions) == len(old_decisions)
        and old.keys() == new.keys() == decisions.keys(),
        "assertion identity scope changed",
    )
    projected = []
    for decision in old_decisions:
        identity = key(decision)
        require(
            all(str(decision[field]) == str(value) for field, value in old[identity].items()),
            "historical assertion identity differs",
        )
        require(
            decision["resolution_status"] in {"OPEN", "APPROVED"},
            "unsupported historical assertion verdict",
        )
        projected.append(
            dict(decision, **{name: str(value) for name, value in new[identity].items()})
        )
    return projected


def validate(root: Path, report_path: Path) -> dict:
    proof = prove_identity_migration(root)
    require(
        report_path.resolve() == safe_path(proof.root, REVIEW),
        "unexpected projected semantic review path",
    )
    outputs = products(proof)
    for name, raw in outputs.items():
        require(
            safe_path(proof.root, name).read_bytes() == raw, "semantic identity projection drift"
        )
    report = document(outputs[REVIEW])
    proof.recheck()
    return {
        "integrity": "PASS",
        "semantic_release": report["release_verdict"],
        "blocking_findings": len(report["blocking_finding_ids"]),
        "blocking_assertions": len(report["blocking_assertion_ids"]),
        "evidence_gaps": report["evidence_gaps"],
    }
