"""Bind the completed review and its unresolved findings to this exact MIM snapshot.

This consolidates existing adjudications and the explicitly documented new review
decisions. It never treats schema validity or a successful join as semantic approval.
Run from the repository root. The accepted KGX bundle must already exist.
"""

import csv
import hashlib
import io
import json
import subprocess
import unicodedata
from collections import Counter
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[2]
OUT = Path(__file__).resolve().parent
BUNDLE = ROOT / "output/mim-kgx-20260921"
MAPPED_REVIEW_REV = "44093d6e5275b7965e55f8bc01457c3a7a736692"
UNMAPPED_REVIEW_REV = "60c4c8eea4eec613a4b5396dd12ce94d6032455e"
inputs = {}


def packed(value):
    return json.dumps(value, sort_keys=True, ensure_ascii=True, separators=(",", ":"))


def sha(data):
    return hashlib.sha256(data).hexdigest()


def read(path):
    path = ROOT / path
    data = path.read_bytes()
    inputs[str(path.relative_to(ROOT))] = sha(data)
    return data


def tsv(data, kgx=False):
    return list(
        csv.DictReader(
            io.StringIO(data.decode()),
            delimiter="\t",
            quoting=csv.QUOTE_NONE if kgx else csv.QUOTE_MINIMAL,
        )
    )


def git(*args):
    return subprocess.check_output(["git", *args], cwd=ROOT)


def snapshot(revision):
    entries = git("ls-tree", "-rz", revision, "data/ingredients").split(b"\0")
    return {
        unicodedata.normalize("NFC", e.split(b"\t", 1)[1].decode()): e.split(b"\t", 1)[0]
        .split()[2]
        .decode()
        for e in entries
        if e
    }


def write(name, rows):
    assert rows, name
    path = OUT / name
    with path.open("w", newline="") as stream:
        writer = csv.DictWriter(
            stream, fieldnames=list(rows[0]), delimiter="\t", lineterminator="\n"
        )
        writer.writeheader()
        writer.writerows(rows)
    return {"rows": len(rows), "sha256": sha(path.read_bytes())}


read(Path(__file__).relative_to(ROOT))
read(OUT.relative_to(ROOT) / "DECISIONS.md")
read("MAPPING_SEMANTICS.md")
mapped_snapshot = snapshot(MAPPED_REVIEW_REV)
unmapped_snapshot = snapshot(UNMAPPED_REVIEW_REV)
unmapped_report = "mappings/unmapped_ingredient_review_2026-09-01.md"
read(unmapped_report)
ledger_path = "reports/yaml_record_review/manifest.tsv"
ledger = {r["path"]: r for r in tsv(read(ledger_path))}
nodes = tsv(read(BUNDLE.relative_to(ROOT) / "mim_nodes.tsv"), kgx=True)
edges = tsv(read(BUNDLE.relative_to(ROOT) / "mim_edges.tsv"), kgx=True)
manifest = json.loads(read(BUNDLE.relative_to(ROOT) / "manifest.json"))
archive_hash = sha(read(BUNDLE.relative_to(ROOT) / "mim-kgx.tar.gz"))
assert len(nodes) == manifest["counts"]["nodes"]
assert len(edges) == manifest["counts"]["edges"]
node_for_path = {n["source_record"]: n for n in nodes if n["node_kind"] == "ingredient"}
records, findings, candidates = {}, [], []


def finding(path, kind, severity, unit, reason, evidence):
    identifier = "SEM:" + sha(packed([path, kind, unit]).encode())[:20]
    row = dict(
        finding_id=identifier,
        source_record=path,
        record_scope=(
            "excluded_rejected" if records[path]["mapping_status"] == "REJECTED" else "active"
        ),
        kind=kind,
        severity=severity,
        affected_unit=unit,
        disposition="open",
        reason=reason,
        evidence=evidence,
    )
    assert identifier not in {r["finding_id"] for r in findings}
    findings.append(row)
    if records[path]["mapping_status"] != "REJECTED":
        records[path]["finding_ids"].append(identifier)
        if severity in {"major", "blocker"}:
            records[path]["verdict"] = "needs_curation"
    return identifier


for group, baseline in [("mapped", mapped_snapshot), ("unmapped", unmapped_snapshot)]:
    for file in sorted((ROOT / "data/ingredients" / group).glob("*.yaml")):
        path = str(file.relative_to(ROOT))
        data = read(path)
        record = yaml.load(data, Loader=yaml.CSafeLoader)
        blob = hashlib.sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest()
        # A changed record requires a new decision; this dated audit cannot approve it.
        assert baseline.get(unicodedata.normalize("NFC", path)) == blob, path
        previous = ledger.get(path)
        status = record["mapping_status"]
        report = previous["report"] if previous else unmapped_report
        report_bytes = read(report)
        verdict = previous["verdict"] if previous else "reviewed_unmapped"
        if status == "REJECTED":
            verdict = "excluded_rejected"
        records[path] = dict(
            source_record=path,
            record_sha256=sha(data),
            identifier=record["identifier"],
            preferred_term=record["preferred_term"],
            mapping_status=status,
            prior_verdict=previous["verdict"] if previous else "reviewed_unmapped",
            verdict=verdict,
            basis="unchanged_source_with_existing_semantic_review",
            baseline_commit=MAPPED_REVIEW_REV if previous else UNMAPPED_REVIEW_REV,
            baseline_git_blob=blob,
            review_report=report,
            report_sha256=sha(report_bytes),
            finding_ids=[],
            record=record,
        )
        if status != "REJECTED":
            assert json.loads(node_for_path[path]["record_json"]) == record
        if previous and previous["verdict"] != "pass":
            finding(
                path,
                "existing_record_review",
                previous["severity"],
                path,
                previous["notes"],
                report,
            )
        if status == "UNMAPPED" and record.get("ontology_mapping"):
            om = record["ontology_mapping"]
            bad = file.stem in {
                "Inorganic_Salts-starch_Agar",
                "Iron_As_Fecl3_In_Edta",
                "Khayasin_C",
                "Xyloglucan_Heptaoctanona_Saccharides",
            }
            verdict = (
                "unsupported_parent_proposal" if bad else "retain_as_nonidentity_parent_proposal"
            )
            candidates.append(
                dict(
                    source_record=path,
                    record_sha256=sha(data),
                    target=om["ontology_id"],
                    verdict=verdict,
                    published_as_edge="false",
                    evidence="DECISIONS.md#unmapped-candidates",
                )
            )
            if bad:
                finding(
                    path,
                    "unmapped_parent_scope",
                    "major",
                    "ontology_mapping",
                    "A component, related compound, or polymer source does not establish a kind-of relationship for the whole ingredient.",
                    "DECISIONS.md#unmapped-candidates",
                )

assert len(node_for_path) == sum(r["mapping_status"] != "REJECTED" for r in records.values())
node_paths = {n["id"]: n["source_record"] for n in nodes if n["node_kind"] == "ingredient"}
edge_decisions = {}
for edge in edges:
    path = node_paths[edge["subject"]]
    assertion = json.loads(edge["assertion_json"])
    kind = edge["assertion_type"]
    decision = "inherit_record_review"
    rationale = "Source assertion unchanged; existing record review applies."
    if kind.endswith("_roles"):
        evidence = assertion.get("evidence", [])
        if not evidence or all(
            e.get("reference_type") == "COMPUTATIONAL_PREDICTION" for e in evidence
        ):
            decision = "insufficient_evidence"
            rationale = (
                "No evidence is supplied."
                if not evidence
                else "Only explicitly provisional computational evidence is supplied; not an independently supported role claim."
            )
            if kind == "cellular_metabolic_roles" and not assertion.get("metabolic_context"):
                rationale += " Organism-conditional role also lacks metabolic context."
            finding(
                path,
                "role_evidence",
                "major",
                edge["id"],
                rationale,
                records[path]["review_report"] + " | DECISIONS.md#roles",
            )
    if kind == "component" and edge["assertion_method"] in {
        "ABBREVIATION_EXPANSION",
        "CURATED_INTERPRETATION",
    }:
        decision = "requires_source_verification"
        rationale = "Expansion/interpretation is retained as an assertion, but the exact source preparation must be verified before semantic approval. UNKNOWN/PARTIAL completeness is not proof of membership."
        finding(
            path,
            "component_source_scope",
            "major",
            edge["id"],
            rationale,
            "DECISIONS.md#components",
        )
    if kind == "recipe_reference" and assertion["relationship"] == "EXACT_FORMULATION":
        decision = "insufficient_evidence"
        rationale = "Stored evidence lists common constituent names but does not identify and compare the original BHI formulation and amounts; exact formulation identity is not demonstrated."
        finding(
            path,
            "recipe_identity",
            "major",
            edge["id"],
            rationale,
            "DECISIONS.md#recipe-references",
        )
    edge_decisions[edge["id"]] = (decision, rationale)

# These source-specific judgments were read and adjudicated in this review.
for stem, reason in {
    "GYPS": "The cited decomposition explicitly says Salts (or Starch), while the active component list asserts starch. The source-specific expansion remains unresolved.",
    "PYGS": "The cited expansion acknowledges that S can mean salts or soluble starch; a definite component choice requires the original recipe context.",
}.items():
    path = f"data/ingredients/mapped/{stem}.yaml"
    finding(
        path, "ambiguous_abbreviation", "major", "components", reason, "DECISIONS.md#components"
    )

sssom_path = "mappings/ingredient_mappings.sssom.tsv"
data = read(sssom_path)
current_rows = tsv(
    b"".join(line for line in data.splitlines(keepends=True) if not line.startswith(b"#"))
)
old_data = git("show", MAPPED_REVIEW_REV + ":" + sssom_path)
old_rows = tsv(
    b"".join(line for line in old_data.splitlines(keepends=True) if not line.startswith(b"#"))
)
old = {(r["subject_id"], r["object_id"]): r for r in old_rows}
assert len(old) == len(current_rows)
sssom_reviews = []
for row in current_rows:
    key = row["subject_id"], row["object_id"]
    previous = old[key]
    changes = [k for k in row if row[k] != previous[k]]
    assert set(changes) <= {"comment", "predicate_id", "mapping_date", "validation_method"}, key
    direction = "unchanged"
    if "predicate_id" in changes:
        assert (previous["predicate_id"], row["predicate_id"]) == (
            "skos:narrowMatch",
            "skos:broadMatch",
        )
        direction = "reviewed_skos_child_to_broader_parent_correction"
    path = node_paths[row["subject_id"]]
    record = records[path]
    verdict = (
        "blocked_by_record_findings" if record["verdict"] == "needs_curation" else record["verdict"]
    )
    sssom_reviews.append(
        dict(
            subject_id=row["subject_id"],
            predicate_id=row["predicate_id"],
            object_id=row["object_id"],
            row_sha256=sha(packed(row).encode()),
            source_record=path,
            record_sha256=record["record_sha256"],
            verdict=verdict,
            direction_review=direction,
            review_report=record["review_report"],
            changed_fields=packed(changes),
            rationale="Whole-record findings block certification; this status does not assert that every blocked mapping triple is false.",
        )
    )

assertion_reviews = []
for edge in edges:
    path = node_paths[edge["subject"]]
    record = records[path]
    verdict, reason = edge_decisions[edge["id"]]
    if verdict == "inherit_record_review":
        verdict = (
            "blocked_by_record_findings"
            if record["verdict"] == "needs_curation"
            else record["verdict"]
        )
    assertion_reviews.append(
        dict(
            edge_id=edge["id"],
            subject=edge["subject"],
            predicate=edge["predicate"],
            object=edge["object"],
            assertion_type=edge["assertion_type"],
            assertion_sha256=sha(edge["assertion_json"].encode()),
            source_record=path,
            record_sha256=record["record_sha256"],
            verdict=verdict,
            rationale=reason,
            review_report=record["review_report"],
        )
    )

schema = yaml.load(
    read("src/mediaingredientmech/schema/mediaingredientmech.yaml"), Loader=yaml.CSafeLoader
)
node_reviews = []
for node in nodes:
    kind = node["node_kind"]
    if kind == "ingredient":
        verdict = records[node["source_record"]]["verdict"]
        rationale = "See content-bound ingredient review and its unresolved findings."
    elif kind == "role":
        enum, value = node["id"].split(":", 1)[1].split(".", 1)
        assert (
            json.loads(node["definition_json"])
            == schema["enums"][enum]["permissible_values"][value]
        )
        verdict = "vocabulary_projection_checked"
        rationale = "Facet-specific local role concept; definition retained, no equivalence to the enum's external mappings is asserted. This does not approve any role-assignment edge."
    elif kind == "external_reference":
        assert node["category"] == "biolink:NamedThing"
        verdict = "reference_only"
        rationale = "MIM-supplied reference and labels, without a fresh authority identity/category claim; associated assertions have separate review dispositions."
    else:
        assert kind == "unresolved_component"
        verdict = "reviewed_unresolved"
        rationale = "Parent-scoped named component without an ontology identity; no cross-record identity inferred."
    node_reviews.append(
        dict(
            node_id=node["id"],
            node_kind=kind,
            node_sha256=sha(packed(node).encode()),
            verdict=verdict,
            source_record=node["source_record"],
            rationale=rationale,
        )
    )

members = {}
record_rows = [
    {k: packed(v) if k == "finding_ids" else v for k, v in r.items() if k != "record"}
    for r in records.values()
]
members["records.tsv"] = write("records.tsv", record_rows)
members["kgx_nodes.tsv"] = write("kgx_nodes.tsv", node_reviews)
members["sssom.tsv"] = write("sssom.tsv", sssom_reviews)
members["kgx_assertions.tsv"] = write("kgx_assertions.tsv", assertion_reviews)
members["findings.tsv"] = write("findings.tsv", findings)
members["unpublished_candidates.tsv"] = write("unpublished_candidates.tsv", candidates)
members["resolved_findings.tsv"] = write(
    "resolved_findings.tsv",
    [
        dict(
            finding_id="SEM:kgx-hierarchy-projection",
            severity="major",
            disposition="resolved",
            affected_units=166,
            source="src/mediaingredientmech/export/kgx.py",
            reason="Applied MIM's required child-to-parent subclass projection while preserving original SSSOM evidence; inverse direction covered by regression test.",
            evidence="MAPPING_SEMANTICS.md#1-predicate-semantics | tests/test_kgx_export.py",
        )
    ],
)
for name, before in inputs.items():
    assert sha((ROOT / name).read_bytes()) == before, name
summary = dict(
    review_date="2026-09-21",
    review_coverage="complete",
    semantic_release_verdict="FAIL",
    review_method="Content-bound reuse of unchanged record adjudications, explicit review of all changed SSSOM fields, and additional evidence/scope adjudications documented in DECISIONS.md. No blanket semantic approval.",
    mapped_baseline_commit=MAPPED_REVIEW_REV,
    unmapped_baseline_commit=UNMAPPED_REVIEW_REV,
    kgx_archive_sha256=archive_hash,
    sssom_sha256=sha(data),
    counts=dict(
        records=len(records),
        active_records=len(node_for_path),
        sssom_rows=len(sssom_reviews),
        kgx_nodes=len(node_reviews),
        kgx_assertions=len(assertion_reviews),
        unpublished_candidates=len(candidates),
        active_record_verdicts=dict(
            Counter(r["verdict"] for r in records.values() if r["mapping_status"] != "REJECTED")
        ),
        sssom_verdicts=dict(Counter(r["verdict"] for r in sssom_reviews)),
        kgx_verdicts=dict(Counter(r["verdict"] for r in assertion_reviews)),
        finding_types=dict(Counter(r["kind"] for r in findings)),
    ),
    inputs=inputs,
    members=members,
    limits=[
        "A complete review can fail; unresolved findings are not approvals.",
        "Unmapped records are reviewed for retention without identity claims, not declared chemically resolved.",
        "Historical scientific judgments were reused only for byte-identical source records; every external source was not independently re-queried.",
        "New component and role dispositions indicate insufficient evidence for certification, not proof that the assertions are biologically false.",
        "No curation backlog item was silently repaired or closed by this report.",
    ],
)
(OUT / "manifest.json").write_text(json.dumps(summary, sort_keys=True, indent=2) + "\n")
print(json.dumps({k: v for k, v in summary.items() if k not in {"inputs", "members"}}, indent=2))
