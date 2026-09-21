"""Export the active MIM corpus as a provenance-preserving, standalone KGX graph.

Only assertions present in MIM are projected. Parent mappings become child-to-parent
subclass edges under MIM's declared convention; original SSSOM rows remain intact.
Components are material parts, never identity or recipe-variant relationships.
"""

from __future__ import annotations

import argparse
import csv
import gzip
import hashlib
import io
import json
import math
import os
import tarfile
import tempfile
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any

import yaml

from mediaingredientmech.sssom_grading import predicate_for
from mediaingredientmech.validation.component_partonomy import validate_component_partonomy
from mediaingredientmech.validation.write_validated import DEFAULT_SCHEMA_PATH, validate_ingredient

SOURCE = "MIM:ingredients"
ROLE_ENUMS = {
    "nutritional_roles": "NutritionalRoleEnum",
    "physicochemical_roles": "PhysicochemicalRoleEnum",
    "cellular_metabolic_roles": "CellularMetabolicRoleEnum",
    "community_organism_roles": "CommunityOrganismRoleEnum",
}
MATCHES = {
    f"skos:{name}Match": f"biolink:{name}_match" for name in ("exact", "close", "broad", "narrow")
}
CATEGORIES = {
    "SINGLE_INGREDIENT": "biolink:ChemicalEntity",
    "UNDEFINED_MIXTURE": "biolink:ComplexMolecularMixture",
    "STOCK_SOLUTION": "biolink:ChemicalMixture",
    "NAMED_MEDIUM": "biolink:ChemicalMixture",
}
NODE_COLUMNS = (
    "id",
    "name",
    "category",
    "provided_by",
    "node_kind",
    "source_record",
    "record_identifier",
    "mapping_status",
    "ingredient_type",
    "review_status",
    "record_json",
    "review_json",
    "definition_json",
    "reference_labels_json",
)
EDGE_COLUMNS = (
    "id",
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
    "publications",
    "metabolic_context",
    "reference_scope",
    "concentration_value",
    "concentration_unit",
    "completeness",
    "assertion_method",
    "assertion_json",
)
CURIE_MAP = {
    "MIM": "https://github.com/CultureBotAI/MediaIngredientMech/blob/main/data/ingredients/mapped/",
    "MIM.unmapped": "https://w3id.org/mediaingredientmech/unmapped/",
    "MIM.component": "https://w3id.org/mediaingredientmech/component/",
    "MIM.role": "https://w3id.org/mediaingredientmech/role/",
    "MIM.vocab": "https://w3id.org/mediaingredientmech/vocabulary/",
    "MIM.assertion": "https://w3id.org/mediaingredientmech/assertion/",
    "biolink": "https://w3id.org/biolink/vocab/",
    "skos": "http://www.w3.org/2004/02/skos/core#",
    "BFO": "http://purl.obolibrary.org/obo/BFO_",
    "RO": "http://purl.obolibrary.org/obo/RO_",
    "CultureMech": "https://w3id.org/culturemech/",
    "doi": "https://doi.org/",
    "PMID": "http://www.ncbi.nlm.nih.gov/pubmed/",
}
RETIRED_HIERARCHY = {
    "parent_ingredient",
    "child_ingredients",
    "variant_type",
    "variant_notes",
    "role_inheritance",
}


def packed(value: Any) -> str:
    """Encode complete annotations without literal KGX list or TSV delimiters."""
    return json.dumps(value, ensure_ascii=True, sort_keys=True, separators=(",", ":")).replace(
        "|", "\\u007c"
    )


def digest(path: Path) -> str:
    """Hash the exact input or output bytes."""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def read_yaml(path: Path) -> dict[str, Any]:
    """Read YAML with the safe C loader when available."""
    result = yaml.load(path.read_text(), Loader=getattr(yaml, "CSafeLoader", yaml.SafeLoader))
    if not isinstance(result, dict):
        raise ValueError(f"Expected a YAML mapping: {path}")
    return result


def read_sssom(path: Path) -> tuple[dict[str, Any], list[dict[str, str]]]:
    """Read mappings and their declared prefix map without changing annotations."""
    lines = path.read_text().splitlines(keepends=True)
    metadata = yaml.safe_load("".join(line[1:] for line in lines if line.startswith("#")))
    rows = list(csv.DictReader((s for s in lines if not s.startswith("#")), delimiter="\t"))
    if not isinstance(metadata, dict) or metadata.get("predicate_semantics") != "skos":
        raise ValueError("SSSOM must explicitly declare predicate_semantics: skos")
    if not rows or any(None in row or None in row.values() for row in rows):
        raise ValueError("Empty or malformed SSSOM rows")
    return metadata, rows


def _acyclic(pairs: list[tuple[str, str]], label: str) -> None:
    """Reject directed cycles, including self references, without recursive depth limits."""
    children: dict[str, set[str]] = defaultdict(set)
    indegree: Counter[str] = Counter()
    for subject, obj in pairs:
        if obj not in children[subject]:
            children[subject].add(obj)
            indegree[obj] += 1
            indegree.setdefault(subject, 0)
    queue = [node for node, degree in indegree.items() if degree == 0]
    visited = 0
    while queue:
        node = queue.pop()
        visited += 1
        for child in children[node]:
            indegree[child] -= 1
            if indegree[child] == 0:
                queue.append(child)
    if visited != len(indegree):
        raise ValueError(f"Cycle in {label}")


def _cell(value: Any) -> str:
    """Require TSV-safe scalar cells; never silently truncate literal source text."""
    text = str(value) if value is not None else ""
    if any(c in text for c in ("\t", "\r", "\n", "\x00")):
        raise ValueError("Embedded control character in KGX scalar")
    return text


def _publications(assertion: dict[str, Any]) -> str:
    values = set()
    for item in assertion.get("evidence", []):
        for key, prefix in (("doi", "doi:"), ("pmid", "PMID:"), ("url", "")):
            if item.get(key):
                values.add(prefix + str(item[key]))
    return "|".join(sorted(values))


def _load_inputs(root: Path) -> tuple[list[tuple[str, dict]], dict[str, str]]:
    """Read only the two live record directories and check both curated collections."""
    records = []
    paths = []
    hashes = {}
    for group in ("mapped", "unmapped"):
        folder = root / "data" / "ingredients" / group
        files = sorted(folder.glob("*.yaml"))
        if not files:
            raise ValueError(f"No live records in {folder}")
        paths.extend(files)
        hashes.update({str(p.relative_to(root)): digest(p) for p in files})
        individual = [(str(p.relative_to(root)), read_yaml(p)) for p in files]
        collection = root / "data" / "curated" / f"{group}_ingredients.yaml"
        paths.append(collection)
        hashes[str(collection.relative_to(root))] = digest(collection)
        curated = read_yaml(collection).get("ingredients")
        # Discussions alone are deliberately per-record authored (#148/#236).
        projected = [
            packed({k: v for k, v in r.items() if k != "discussions"}) for _, r in individual
        ]
        if not isinstance(curated, list) or Counter(projected) != Counter(
            packed({k: v for k, v in r.items() if k != "discussions"}) for r in curated
        ):
            raise ValueError(f"Collection/per-record drift in {group}")
        records.extend(individual)
    paths.extend([root / "mappings/ingredient_mappings.sssom.tsv"])
    ledger = root / "reports/yaml_record_review/manifest.tsv"
    if ledger.exists():
        paths.append(ledger)
    for path in paths:
        name = str(path.relative_to(root))
        current = digest(path)
        if name in hashes and hashes[name] != current:
            raise ValueError(f"Input changed while reading: {name}")
        hashes[name] = current
    return records, hashes


class Graph:
    """Keep record nodes distinct, and retain one edge for each supplied assertion."""

    def __init__(self) -> None:
        self.nodes: dict[str, dict[str, str]] = {}
        self.edges: list[dict[str, str]] = []
        self.reference_labels: dict[str, set[str]] = defaultdict(set)

    def node(self, identifier: str, name: str, category: str, kind: str, **fields: str) -> None:
        if identifier in self.nodes:
            raise ValueError(f"Duplicate local node: {identifier}")
        self.nodes[identifier] = {
            "id": identifier,
            "name": name,
            "category": category,
            "node_kind": kind,
            "provided_by": SOURCE,
            **fields,
        }

    def reference(self, identifier: str, label: str = "") -> None:
        if label:
            self.reference_labels[identifier].add(label)
        if identifier not in self.nodes:
            self.node(identifier, label or identifier, "biolink:NamedThing", "external_reference")
        elif self.nodes[identifier]["node_kind"] != "external_reference":
            raise ValueError(f"External reference collides with local node: {identifier}")

    def edge(
        self,
        subject: str,
        predicate: str,
        obj: str,
        relation: str,
        kind: str,
        source: str,
        position: int,
        assertion: dict[str, Any],
        **fields: str,
    ) -> None:
        if subject not in self.nodes or obj not in self.nodes:
            raise ValueError(f"Undeclared edge endpoint: {subject} -> {obj}")
        confidence = assertion.get("confidence", "")
        if confidence != "" and confidence is not None:
            if not math.isfinite(float(confidence)) or not 0 <= float(confidence) <= 1:
                raise ValueError(f"Invalid confidence in {source}")
        row = {
            "subject": subject,
            "predicate": predicate,
            "object": obj,
            "relation": relation,
            "primary_knowledge_source": SOURCE,
            "provided_by": SOURCE,
            "assertion_type": kind,
            "source_record": source,
            "source_position": str(position),
            "confidence": str(confidence) if confidence is not None else "",
            "assertion_json": packed(assertion),
            **fields,
        }
        row["id"] = "MIM.assertion:" + hashlib.sha256(packed(row).encode()).hexdigest()
        self.edges.append(row)


def build_graph(root: Path) -> tuple[Graph, dict[str, Any], list[dict[str, str]]]:
    """Validate source structure and construct the complete explicit MIM projection."""
    package = Path(__file__).parents[1]
    implementation_paths = [
        Path(__file__),
        DEFAULT_SCHEMA_PATH,
        DEFAULT_SCHEMA_PATH.with_name("mech_shared.yaml"),
        package / "sssom_grading.py",
        package / "validation/component_partonomy.py",
        package / "validation/write_validated.py",
    ]
    implementation = {str(p.relative_to(package)): digest(p) for p in implementation_paths}
    records, hashes = _load_inputs(root)
    metadata, mappings = read_sssom(root / "mappings/ingredient_mappings.sssom.tsv")
    schema = read_yaml(DEFAULT_SCHEMA_PATH)
    errors = validate_ingredient(
        {"ingredients": [r for _, r in records]}, target_class="IngredientCollection"
    )
    if errors:
        raise ValueError(f"Source schema validation failed: {[e.message for e in errors[:5]]}")
    violations = validate_component_partonomy(r for _, r in records)
    if violations:
        raise ValueError(f"Component validation failed: {violations[:5]}")
    by_label: dict[str, set[str]] = defaultdict(set)
    for row in mappings:
        if row["predicate_id"] not in MATCHES or not row["subject_id"].startswith("MIM:"):
            raise ValueError("Unsupported SSSOM predicate or subject")
        by_label[row["subject_label"]].add(row["subject_id"])
    if any(len(subjects) != 1 for subjects in by_label.values()):
        raise ValueError("Ambiguous SSSOM subject label")
    ledger_path = root / "reports/yaml_record_review/manifest.tsv"
    reviews = {}
    if ledger_path.exists():
        with ledger_path.open() as stream:
            for row in csv.DictReader(stream, delimiter="\t"):
                if row["path"] in reviews:
                    raise ValueError("Duplicate review ledger entry")
                reviews[row["path"]] = row
    graph = Graph()
    active = []
    excluded = []
    for path, record in records:
        if RETIRED_HIERARCHY.intersection(record):
            raise ValueError(f"Retired hierarchy field in {path}")
        status = record["mapping_status"]
        if status == "REJECTED":
            excluded.append({"source_record": path, "record_json": packed(record)})
            continue
        if status == "MAPPED":
            subjects = by_label.get(record["preferred_term"], set())
            if len(subjects) != 1:
                raise ValueError(f"No unique SSSOM subject for {path}")
            identifier = next(iter(subjects))
            own_rows = [r for r in mappings if r["subject_id"] == identifier]
            if not any(
                r["object_id"] == record["identifier"] and r["predicate_id"] == "skos:exactMatch"
                for r in own_rows
            ):
                raise ValueError(f"Missing exact primary identity mapping for {path}")
            grounding = record.get("ontology_mapping") or {}
            if grounding.get("ontology_id"):
                target = grounding["ontology_id"]
                predicate = (
                    "skos:exactMatch"
                    if target == record["identifier"]
                    else predicate_for(grounding.get("mapping_quality"))
                )
                if not any(
                    r["object_id"] == target and r["predicate_id"] == predicate for r in own_rows
                ):
                    raise ValueError(f"Stale SSSOM grounding or direction for {path}")
        elif status in {"UNMAPPED", "AMBIGUOUS"}:
            identifier = "MIM.unmapped:" + record["identifier"]
        else:
            raise ValueError(f"Unsupported active mapping status: {status}")
        review = reviews.get(path, {})
        graph.node(
            identifier,
            record["preferred_term"],
            CATEGORIES.get(record.get("ingredient_type", ""), "biolink:NamedThing"),
            "ingredient",
            source_record=path,
            record_identifier=record["identifier"],
            mapping_status=status,
            ingredient_type=record.get("ingredient_type", ""),
            review_status=review.get("verdict", "not_reviewed"),
            review_json=packed(review),
            record_json=packed(record),
        )
        active.append((identifier, path, record))
    if set().union(*by_label.values()) - graph.nodes.keys():
        raise ValueError("SSSOM references absent or rejected ingredient records")
    hierarchy = []
    primary_ids = {identifier: record["identifier"] for identifier, _, record in active}
    seen_pairs = set()
    for position, row in enumerate(mappings, 1):
        subject, obj, pred = row["subject_id"], row["object_id"], row["predicate_id"]
        if (subject, obj) in seen_pairs:
            raise ValueError("Duplicate SSSOM subject/object pair")
        seen_pairs.add((subject, obj))
        graph.reference(obj, row["object_label"])
        edge_subject, edge_object, predicate = subject, obj, MATCHES[pred]
        # MAPPING_SEMANTICS.md Section 1 explicitly requires subclass projection
        # for MIM's curated kind-of mappings. This is a dataset-specific contract,
        # not a general assertion that arbitrary SKOS mappings imply OWL classes.
        if pred == "skos:broadMatch":
            predicate = "biolink:subclass_of"
            hierarchy.append((primary_ids[subject], obj))
        elif MATCHES[pred] == "biolink:narrow_match":
            edge_subject, edge_object, predicate = obj, subject, "biolink:subclass_of"
            hierarchy.append((obj, primary_ids[subject]))
        graph.edge(
            edge_subject,
            predicate,
            edge_object,
            pred,
            "mapping",
            "mappings/ingredient_mappings.sssom.tsv",
            position,
            row,
        )
    component_pairs = []
    for subject, path, record in active:
        for facet, enum in ROLE_ENUMS.items():
            for position, role in enumerate(record.get(facet, []), 1):
                value = role["role"]
                definition = schema["enums"][enum]["permissible_values"][value]
                obj = f"MIM.role:{enum}.{value}"
                community = facet == "community_organism_roles"
                if obj not in graph.nodes:
                    graph.node(
                        obj,
                        value,
                        "biolink:Attribute" if community else "biolink:ChemicalRole",
                        "role",
                        definition_json=packed(definition),
                    )
                graph.edge(
                    subject,
                    "biolink:has_attribute" if community else "biolink:has_chemical_role",
                    obj,
                    f"MIM.vocab:{facet}",
                    facet,
                    path,
                    position,
                    role,
                    publications=_publications(role),
                    metabolic_context=role.get("metabolic_context", ""),
                )
        for position, component in enumerate(record.get("components", []), 1):
            obj = component.get("component_id")
            if obj:
                graph.reference(obj, component["component_name"])
                component_pairs.append((record["identifier"], obj))
            else:
                obj = (
                    "MIM.component:"
                    + hashlib.sha256(
                        packed([subject, component["component_name"]]).encode()
                    ).hexdigest()
                )
                graph.node(
                    obj,
                    component["component_name"],
                    "biolink:NamedThing",
                    "unresolved_component",
                    source_record=path,
                )
            assertion = record["component_assertion"]
            graph.edge(
                subject,
                "biolink:has_part",
                obj,
                "BFO:0000051",
                "component",
                path,
                position,
                {"component": component, "component_assertion": assertion},
                reference_scope=component["reference_scope"],
                concentration_value=component.get("concentration_value", ""),
                concentration_unit=component.get("concentration_unit", ""),
                completeness=assertion["completeness"],
                assertion_method=assertion["method"],
            )
        for position, context in enumerate(record.get("environmental_context", []), 1):
            obj = context["environment_term"]
            graph.reference(obj, context.get("environment_label", ""))
            relation = "MIM.vocab:environmental_context"
            graph.edge(subject, relation, obj, relation, "environment", path, position, context)
        if record.get("culturemech_reference"):
            reference = record["culturemech_reference"]
            obj = reference["medium_id"]
            graph.reference(obj, reference.get("medium_name", ""))
            relation = "MIM.vocab:recipe_" + reference["relationship"].lower()
            graph.edge(subject, relation, obj, relation, "recipe_reference", path, 1, reference)
    _acyclic(component_pairs, "material component assertions")
    _acyclic(hierarchy, "broader/narrower mappings")
    for identifier, labels in graph.reference_labels.items():
        node = graph.nodes[identifier]
        node["reference_labels_json"] = packed(sorted(labels))
        node["name"] = min(labels) if labels else identifier
    if len({r["id"] for r in graph.edges}) != len(graph.edges):
        raise ValueError("Duplicate assertion IDs")
    prefixes = {**metadata["curie_map"], **CURIE_MAP}
    for identifier in [
        *graph.nodes,
        *(r["predicate"] for r in graph.edges),
        *(r["relation"] for r in graph.edges),
    ]:
        prefix, sep, local = identifier.partition(":")
        if (
            not sep
            or not local
            or prefix not in prefixes
            or any(c.isspace() for c in identifier)
            or "|" in identifier
        ):
            raise ValueError(f"Invalid or undeclared CURIE: {identifier}")
    for name, before in hashes.items():
        if digest(root / name) != before:
            raise ValueError(f"Input changed during export: {name}")
    manifest = {
        "format_version": 1,
        "source": SOURCE,
        "curie_map": prefixes,
        "inputs": hashes,
        "implementation": implementation,
        "counts": {
            "nodes": len(graph.nodes),
            "edges": len(graph.edges),
            "unique_triples": len(
                {(e["subject"], e["predicate"], e["object"]) for e in graph.edges}
            ),
            "active_ingredients": len(active),
            "excluded_rejected_records": len(excluded),
            "sssom_rows": len(mappings),
            "nodes_by_kind": dict(
                sorted(Counter(n["node_kind"] for n in graph.nodes.values()).items())
            ),
            "edges_by_assertion_type": dict(
                sorted(Counter(e["assertion_type"] for e in graph.edges).items())
            ),
            "edges_by_predicate": dict(
                sorted(Counter(e["predicate"] for e in graph.edges).items())
            ),
            "ingredient_review_status": dict(
                sorted(
                    Counter(
                        n["review_status"]
                        for n in graph.nodes.values()
                        if n["node_kind"] == "ingredient"
                    ).items()
                )
            ),
        },
        "validation": {
            "source_schema": "passed",
            "collection_roundtrip": "passed",
            "component_partonomy": "passed",
            "endpoint_closure": "passed",
            "component_cycles": 0,
            "mapping_hierarchy_cycles": 0,
        },
        "limitations": [
            "Structural and faithful-projection validation is not semantic approval of every curated assertion.",
            "Review dispositions are copied from the ledger; not re-adjudicated or content-bound approvals.",
            "No local ingredient variant hierarchy is encoded by MIM; only published broad/narrow mappings are exported.",
            "External-reference labels are source labels, not a fresh ontology-authority claim; categories remain NamedThing.",
            "Native environmental and recipe predicates are MIM extensions; strict Biolink conformance is not claimed.",
            "Roles retain conditional context, evidence, and confidence; no organism utilization is inferred.",
        ],
    }
    return graph, manifest, excluded


def _write_tsv(path: Path, columns: tuple[str, ...], rows: list[dict[str, str]]) -> dict[str, Any]:
    with path.open("w", encoding="utf-8", newline="") as stream:
        writer = csv.writer(
            stream, delimiter="\t", lineterminator="\n", quoting=csv.QUOTE_NONE, quotechar=None
        )
        writer.writerow(columns)
        for row in rows:
            writer.writerow([_cell(row.get(column, "")) for column in columns])
    return {"rows": len(rows), "bytes": path.stat().st_size, "sha256": digest(path)}


def export_graph(root: Path, output: Path) -> dict[str, Any]:
    """Publish a validated, deterministic bundle into a new directory atomically."""
    root, output = root.resolve(), output.resolve()
    if output.exists():
        raise FileExistsError(f"Use a new output directory; refusing to replace {output}")
    graph, manifest, excluded = build_graph(root)
    output.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(prefix=".mim-kgx-", dir=output.parent) as temporary:
        staging = Path(temporary) / "bundle"
        staging.mkdir()
        manifest["members"] = {
            "mim_nodes.tsv": _write_tsv(
                staging / "mim_nodes.tsv",
                NODE_COLUMNS,
                [graph.nodes[k] for k in sorted(graph.nodes)],
            ),
            "mim_edges.tsv": _write_tsv(
                staging / "mim_edges.tsv", EDGE_COLUMNS, sorted(graph.edges, key=lambda r: r["id"])
            ),
            "excluded_records.tsv": _write_tsv(
                staging / "excluded_records.tsv", ("source_record", "record_json"), excluded
            ),
        }
        (staging / "manifest.json").write_text(
            json.dumps(manifest, sort_keys=True, indent=2) + "\n"
        )
        # Canonical timestamps/modes make the archive reproducible from identical inputs.
        with (staging / "mim-kgx.tar.gz").open("wb") as raw:
            with gzip.GzipFile(filename="", fileobj=raw, mode="wb", mtime=0) as compressed:
                with tarfile.open(fileobj=compressed, mode="w") as archive:
                    for name in [
                        "mim_nodes.tsv",
                        "mim_edges.tsv",
                        "excluded_records.tsv",
                        "manifest.json",
                    ]:
                        content = (staging / name).read_bytes()
                        member = tarfile.TarInfo(name)
                        member.size, member.mode, member.mtime = len(content), 0o644, 0
                        archive.addfile(member, io.BytesIO(content))
        # Input contents and the live-file set are checked again immediately before publication.
        for name, before in manifest["inputs"].items():
            if digest(root / name) != before:
                raise ValueError(f"Input changed before publication: {name}")
        live = {
            str(p.relative_to(root))
            for group in ("mapped", "unmapped")
            for p in (root / "data/ingredients" / group).glob("*.yaml")
        }
        expected = {p for p in manifest["inputs"] if p.startswith("data/ingredients/")}
        if live != expected:
            raise ValueError("Live ingredient files changed during export")
        ledger = "reports/yaml_record_review/manifest.tsv"
        if (root / ledger).exists() != (ledger in manifest["inputs"]):
            raise ValueError("Review ledger presence changed during export")
        for name, before in manifest["implementation"].items():
            if digest(Path(__file__).parents[1] / name) != before:
                raise ValueError(f"Exporter implementation changed during export: {name}")
        os.rename(staging, output)
    return manifest


def main() -> None:
    """Expose the standalone exporter without network or sibling-repository dependencies."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo-root", type=Path, default=Path(__file__).resolve().parents[3])
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    manifest = export_graph(args.repo_root, args.output)
    print(json.dumps(manifest["counts"], indent=2))


if __name__ == "__main__":
    main()
