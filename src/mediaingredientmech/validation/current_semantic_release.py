"""Current graph review after a verified native publication (#1387).

The fixed historical graph remains an independently replayed authority. This
route never extends the identity-only proof or inherits its positive decisions.
Current mappings come only from the explicit ordinary mapping/companion pair;
other graph assertions remain OPEN until a separate assertion-review contract
is selected. A canonical installation is not a release review.
"""

from __future__ import annotations

import argparse
import csv
import io
import json
import os
import subprocess
import sys
import tempfile
from pathlib import Path

import yaml  # type: ignore[import-untyped]

from mediaingredientmech import identity_projection as identity
from mediaingredientmech import identity_projection_graph as historical_graph
from mediaingredientmech.curate import stable_sssom_publication as publication
from mediaingredientmech.export import reviewed_sssom
from mediaingredientmech.ingredient_bundle_contract import canonical_json, read_json, safe_member
from mediaingredientmech.validation import reviewed_export_route, semantic_release

CAPABILITY = "mim-current-semantic-graph/v1"
SOURCE = identity.SOURCE
POLICY = "src/mediaingredientmech/validation/current_semantic_release.py"
REQUEST_KEYS = {
    "schema_version",
    "capability",
    "historical_root",
    "historical_revision",
    "transition",
    "mapping_review",
    "companion_review",
    "bundle",
    "hold_reviews",
    "review_inputs",
    "finding_dispositions",
    "record_lineage",
}


def require(value, message):
    if not value:
        raise ValueError("Current semantic graph: " + message)


def encoded(value):
    return canonical_json(value) + b"\n"


def table(rows, fields):
    out = io.StringIO(newline="")
    writer = csv.DictWriter(out, fields, delimiter="\t", lineterminator="\n")
    writer.writeheader()
    writer.writerows(rows)
    return out.getvalue().encode()


def graph_table(raw):
    """Parse the captured KGX member, never a second mutable filesystem read."""
    reader = csv.DictReader(
        io.StringIO(raw.decode(), newline=""), delimiter="\t", quoting=csv.QUOTE_NONE
    )
    require(
        reader.fieldnames and len(reader.fieldnames) == len(set(reader.fieldnames)),
        "invalid graph member columns",
    )
    rows = list(reader)
    require(
        all(None not in row and None not in row.values() for row in rows), "malformed graph member"
    )
    return rows


def independent_pair(references, reviewers):
    """#1388 identity is the native identity string, not mutable metadata."""
    require(len(references) == len(reviewers) == 2, "two native reviewers required")
    identities = [reviewer.get("identity") for reviewer in reviewers]
    require(
        all(isinstance(value, str) and value.strip() for value in identities)
        and identities[0] != identities[1]
        and references[0]["path"] != references[1]["path"]
        and reviewers[1].get("independence") == "independent"
        and isinstance(reviewers[1].get("independence_basis"), str)
        and reviewers[1]["independence_basis"].strip(),
        "distinct reviewer identities and a separate independent skeptic required",
    )


class Inputs:
    """One byte snapshot; additions cannot replace an earlier observation."""

    def __init__(self, root):
        self.root = reviewed_export_route._root(Path(root))
        self.raw = {}

    def read(self, name, expected=None):
        path = safe_member(self.root, name)
        raw = path.read_bytes()
        require(name not in self.raw or self.raw[name] == raw, "input changed: " + name)
        require(expected is None or identity.sha(raw) == expected, "stale input: " + name)
        self.raw[name] = raw
        return raw

    def document(self, name, expected=None):
        return read_json(self.read(name, expected))

    def recheck(self):
        for name, raw in self.raw.items():
            require(safe_member(self.root, name).read_bytes() == raw, "late input drift: " + name)

    def hashes(self):
        return {name: identity.sha(raw) for name, raw in sorted(self.raw.items())}


def historical_proof(root, revision, scratch):
    """Replay the actual old semantic graph/chain, then native address projection.

    Archived graph members and Git blobs are materialized only in a disposable
    private readback tree. No historical checkout or report is rewritten. The
    old ordinary validator still sees its exact original canonical endpoint.
    """
    root = reviewed_export_route._root(Path(root))
    checkout = reviewed_export_route._historical_checkout(root, revision)
    reviewed_export_route._projection_check(root)
    proof = identity.prove_identity_migration(root)
    original_raw = identity.git_files(root, [historical_graph.OLD_REVIEW])[
        historical_graph.OLD_REVIEW
    ]
    require(
        identity.sha(original_raw) == historical_graph.OLD_REVIEW_SHA,
        "historical semantic authority differs",
    )
    original = read_json(original_raw)
    graph, _ = historical_graph.old_graph(proof)
    manifest = read_json(graph["manifest.json"])
    require(
        identity.sha(graph["manifest.json"])
        == original["inputs"][historical_graph.BUNDLE + "/manifest.json"],
        "historical graph manifest differs",
    )
    names = set(original["inputs"]) | set(original["record_inputs"]) | set(manifest["inputs"])
    names.discard(historical_graph.BUNDLE + "/manifest.json")
    before = identity.git_files(root, sorted(names))
    for name, expected in {**original["inputs"], **original["record_inputs"]}.items():
        if name != historical_graph.BUNDLE + "/manifest.json":
            require(
                identity.sha(before[name]) == expected, "historical graph input differs: " + name
            )
    before[historical_graph.OLD_REVIEW] = original_raw
    before.update({historical_graph.BUNDLE + "/" + name: raw for name, raw in graph.items()})
    # Today's graph validator requires permanent IDs. Execute the exact trusted
    # pre-ID native implementation, whose semantic entry point is already bound
    # by the historical review, against its original data and receipt endpoint.
    # The remaining package closure comes from the same fixed Git authority;
    # never import today's implementation while claiming historical execution.
    package_names = (
        reviewed_export_route._git(
            root,
            "ls-tree",
            "-rz",
            "--name-only",
            identity.BASE_COMMIT,
            "--",
            "src/mediaingredientmech",
        )
        .decode()
        .split("\0")
    )
    package = identity.git_files(root, [name for name in package_names if name])
    for name, raw in package.items():
        require(name not in before or before[name] == raw, "historical module closure conflicts")
    before.update(package)
    with tempfile.TemporaryDirectory(prefix="legacy-semantic-", dir=scratch) as directory:
        legacy = Path(directory)
        for name, raw in before.items():
            target = safe_member(legacy, name)
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(raw)
        process = subprocess.run(
            [
                sys.executable,
                "-B",
                "-m",
                "mediaingredientmech.validation.semantic_release",
                "--root",
                str(legacy),
                "--report",
                str(legacy / historical_graph.OLD_REVIEW),
            ],
            cwd=legacy,
            env={**os.environ, "PYTHONPATH": str(legacy / "src"), "PYTHONDONTWRITEBYTECODE": "1"},
            capture_output=True,
            timeout=300,
            check=False,
        )
        require(
            process.returncode == 0,
            "native historical graph replay failed: "
            + process.stderr.decode(errors="replace")[-2000:],
        )
        result = read_json(process.stdout)
        require(result.get("integrity") == "PASS", "native historical graph integrity failed")
        require(
            all(safe_member(legacy, name).read_bytes() == raw for name, raw in before.items()),
            "historical replay inputs changed",
        )
    old_nodes, old_edges, old_excluded = [
        historical_graph.read_table(graph[name]) for name in historical_graph.GRAPH_FILES[1:]
    ]
    projected = historical_graph.project_graph(proof, old_nodes, old_edges, old_excluded)
    old_dispositions = historical_graph.read_table(before[original["assertion_dispositions"]])
    old_assertions = semantic_release.current_assertions(
        proof.transition["old_records"],
        proof.transition["old_rows"],
        {name: identity.sha(raw) for name, raw in proof.before.items()},
        identity.sha(proof.before[SOURCE]),
    )
    new_assertions = semantic_release.current_assertions(
        proof.transition["new_records"],
        proof.transition["rows"],
        {name: identity.sha(raw) for name, raw in proof.after.items()},
        identity.sha(proof.after[SOURCE]),
    )
    expected = historical_graph.project_decisions(old_assertions, new_assertions, old_dispositions)
    require(
        expected
        == historical_graph.read_table((root / historical_graph.DISPOSITIONS).read_bytes()),
        "historical projected decisions differ",
    )
    proof.recheck()
    require(
        reviewed_export_route._historical_checkout(root, revision) == checkout,
        "historical checkout drifted",
    )
    return {
        "root": root,
        "revision": revision,
        "checkout": checkout,
        "proof": proof,
        "original": original,
        "original_raw": original_raw,
        "before": before,
        "projected": projected,
        "result": result,
    }


def current_graph(inputs, bundle):
    """The ordinary graph's complete inventory and exact native typed projection."""
    root = inputs.root
    names = identity.record_paths(root)
    records = {name: yaml.safe_load(inputs.read(name)) for name in names}
    hashes = {name: identity.sha(inputs.raw[name]) for name in names}
    raw = inputs.read(SOURCE)
    _, _, mappings = reviewed_sssom.read_sssom(root / SOURCE, content=raw)
    manifest = inputs.document(bundle + "/manifest.json")
    require(
        {"mim_nodes.tsv", "mim_edges.tsv"} <= set(manifest["members"]),
        "graph manifest omits required node/edge members",
    )
    require(set(hashes) <= set(manifest["inputs"]), "graph omits owner inputs")
    for name, expected in manifest["inputs"].items():
        inputs.read(name, expected)
    for name, expected in manifest["implementation"].items():
        inputs.read("src/mediaingredientmech/" + name, expected)
    for name, details in manifest["members"].items():
        inputs.read(bundle + "/" + name, details["sha256"])
    nodes = graph_table(inputs.raw[bundle + "/mim_nodes.tsv"])
    edges = graph_table(inputs.raw[bundle + "/mim_edges.tsv"])
    active = {name for name, record in records.items() if record["mapping_status"] != "REJECTED"}
    ingredients = [node for node in nodes if node["node_kind"] == "ingredient"]
    require(
        len(ingredients) == len(active) and {n["source_record"] for n in ingredients} == active,
        "incomplete current graph owner inventory",
    )
    for node in ingredients:
        require(
            read_json(node["record_json"].encode()) == records[node["source_record"]],
            "graph owner payload differs",
        )
    semantic_release.verify_projection(records, mappings, nodes, edges)
    expected = semantic_release.assertion_inventory(records, mappings)
    from collections import Counter

    actual = Counter(
        (
            edge["source_record"],
            edge["assertion_type"],
            edge["source_position"],
            json.dumps(json.loads(edge["assertion_json"]), sort_keys=True, separators=(",", ":")),
        )
        for edge in edges
    )
    require(actual == expected, "incomplete current graph assertion inventory")
    return records, hashes, mappings, edges


def hold_payloads(history, records, hashes, mappings, provenance):
    """Retain every frozen hold/resolution and every cell in its actual lineage."""
    old = history["original"]
    holds = read_json(history["before"][old["release_holds"]])
    proof = history["proof"]
    owners = {}
    for name, record in records.items():
        mim_id = record.get("mim_id")
        require(mim_id and mim_id not in owners, "missing/duplicate permanent owner")
        owners[mim_id] = name
    result = []
    obligations = [*holds.get("holds", []), *holds.get("resolutions", [])]
    require(
        len(obligations) == len(holds["required_hold_ids"]), "historical hold inventory incomplete"
    )
    for obligation in obligations:
        owner = obligation["owner_record"]
        stable_owner = proof.transition["new_records"][owner]
        current_owner = owners.get(stable_owner["mim_id"])
        require(current_owner is not None, "historical held owner disappeared")
        # A stable ID alone never establishes scientific byte continuity.
        require(
            hashes[current_owner] == identity.sha(proof.after[owner]),
            "held owner changed; explicit owner correction review is required",
        )
        lineage = old.get("release_hold_lineage", {}).get(obligation["assertion_id"], {})
        assertion_id = lineage.get("assertion_id", obligation["assertion_id"])
        decisions = historical_graph.read_table(history["before"][old["assertion_dispositions"]])
        matches = [d for d in decisions if d["assertion_id"] == assertion_id]
        require(
            len(matches) == 1 and matches[0]["assertion_type"] == "mapping",
            "historical held assertion lineage differs",
        )
        position = int(matches[0]["source_position"])
        legacy_row = proof.transition["old_rows"][position - 1]
        stable_row = proof.transition["rows"][position - 1]
        require(
            stable_row == dict(legacy_row, subject_id=stable_owner["mim_id"]),
            "hold projection changed more than the typed subject address",
        )
        entries = [
            entry
            for entry in provenance["selection"]["rows"]
            if any(
                before["position"] == position and before["row"] == stable_row
                for before in entry["before_rows"]
            )
        ]
        require(
            len(entries) == 1 and entries[0]["proposed_row"] is not None,
            "held row removed or publication lineage is incomplete",
        )
        entry = entries[0]
        current = entry["proposed_row"]
        require(
            entry["owner"] == current_owner
            and entry["owner_sha256"] == hashes[current_owner]
            and current in mappings,
            "held row owner/current payload differs",
        )
        negative = next(
            (h for h in holds.get("historical_holds", []) if h["hold_id"] == obligation["hold_id"]),
            obligation,
        )
        result.append(
            {
                "hold_id": obligation["hold_id"],
                "original_negative": negative,
                "historical_obligation": obligation,
                "legacy_row": legacy_row,
                "projected_row": stable_row,
                "current_row": current,
                "owner": current_owner,
                "owner_sha256": hashes[current_owner],
                "changed_cells": {
                    key: {"before": stable_row.get(key), "after": current.get(key)}
                    for key in sorted(set(stable_row) | set(current))
                    if stable_row.get(key) != current.get(key)
                },
            }
        )
    return result


def _hold_reviews(inputs, request, payloads, source_path):
    """Positive hold treatment requires separate, exact native release assessments."""
    reviews = request["hold_reviews"]
    require(
        isinstance(reviews, dict) and set(reviews) <= {p["hold_id"] for p in payloads},
        "unexpected hold review",
    )
    for name, expected in request["review_inputs"].items():
        inputs.read(name, expected)
    script = publication._CAPTURE.script("scripts/record_review.py")
    conclusions = {}
    for payload in payloads:
        key = payload["hold_id"]
        pair = reviews.get(key, [])
        if not pair:
            conclusions[key] = "WITHHOLD"
            continue
        require(
            isinstance(pair, list) and len(pair) == 2,
            "primary and independent hold review required",
        )
        authors = []
        decisions = []
        for ref in pair:
            require(
                set(ref) == {"path", "sha256", "markdown_sha256", "target_id", "assessment_id"},
                "invalid native hold review reference",
            )
            raw = inputs.read(ref["path"], ref["sha256"])
            markdown = str(Path(ref["path"]).with_name("review.md"))
            md = inputs.read(markdown, ref["markdown_sha256"])
            report = script.parse_review_bundle(
                ref["path"], raw, md, inputs.root / "schema/record_review.yaml"
            )
            require(
                script.source_provenance(inputs.root, report)["status"]
                not in {"invalid", "unverified"},
                "unverified native hold review",
            )
            require(
                report["repository"] == "CultureBotAI/MediaIngredientMech"
                and report["completion"] == "completed"
                and report["scientific_review"] is True,
                "completed scientific hold review required",
            )
            source = {x["path"]: x["sha256"] for x in report["source"]["inputs"]}
            for name, expected in source.items():
                inputs.read(name, expected)
            for name in (source_path, SOURCE, payload["owner"], "MAPPING_SEMANTICS.md", POLICY):
                require(
                    source.get(name) == identity.sha(inputs.read(name)),
                    "hold review omits current input: " + name,
                )
            targets = [x for x in report["targets"] if x["target_id"] == ref["target_id"]]
            require(
                len(targets) == 1
                and targets[0]["kind"] == "snapshot_row"
                and targets[0]["path"] == source_path
                and targets[0]["selector"] == key
                and targets[0].get("semantic_digest", {}).get("algorithm")
                == "sha256-canonical-json-v1"
                and targets[0]["semantic_digest"]["sha256"]
                == identity.sha(canonical_json(payload)),
                "hold review does not bind complete lineage and current row",
            )
            assessment = publication._assessment(report, ref["target_id"])
            require(assessment["assessment_id"] == ref["assessment_id"], "wrong hold assessment")
            dims = {d["name"]: d["value"] for d in assessment.get("dimensions", [])}
            require(
                dims.get("semantic_scope") == "current_mapping_release_and_historical_hold"
                and dims.get("disposition") in {"SUPPORTED", "WITHHOLD"},
                "installation review is not hold release approval",
            )
            # #1394: native report shape and an identity pair alone cannot bind
            # the actual evidence cited for a present release decision.
            evidence = {item["evidence_id"]: item for item in report["evidence"]}
            captured = [
                evidence[eid]
                for eid in assessment["evidence_ids"]
                if evidence[eid]["reference"] in source
                and evidence[eid].get("snapshot_sha256") == source[evidence[eid]["reference"]]
            ]
            require(captured, "hold review lacks captured evidence")
            if dims["disposition"] == "SUPPORTED":
                require(
                    any(
                        item["kind"] in {"primary_source", "database", "authority"}
                        and item["support"] == "supports"
                        for item in captured
                    ),
                    "supported hold review lacks captured primary evidence",
                )
            authors.append(report["reviewer"])
            decisions.append(dims["disposition"])
        independent_pair(pair, authors)
        conclusions[key] = "SUPPORTED" if decisions == ["SUPPORTED", "SUPPORTED"] else "WITHHOLD"
    return conclusions


def current_findings(inputs, history, records, hashes, request):
    """#1390 apply the original complete finding gate to actual current bytes."""
    original = history["original"]
    baseline_name = original["baseline_findings"]
    baseline_raw = history["before"][baseline_name]
    manifest = read_json(history["before"][original["baseline_manifest"]])
    require(
        manifest["members"].get(Path(baseline_name).name, {}).get("sha256")
        == identity.sha(baseline_raw),
        "historical baseline finding manifest differs",
    )
    require(request["finding_dispositions"], "explicit current finding dispositions required")
    dispositions = historical_graph.read_table(inputs.read(request["finding_dispositions"]))
    lineage = (
        inputs.document(request["record_lineage"])["moves"] if request["record_lineage"] else []
    )
    # Evidence is separately declared and byte-pinned. Copying a historical
    # RESOLVED flag or retaining a permanent ID does not refresh its authority.
    for name, expected in request["review_inputs"].items():
        inputs.read(name, expected)
    blocking = semantic_release.adjudicate_findings(
        historical_graph.read_table(baseline_raw),
        dispositions,
        records,
        hashes,
        inputs.hashes(),
        manifest["inputs"],
        lineage,
    )
    return dispositions, blocking


def _retained_companion_implementation(inputs, companion):
    """Bind the optional complete companion executor without changing old routes."""
    if "retained_obligations" not in companion:
        return
    from mediaingredientmech.ingredient_bundle_contract import retained_implementation

    for name, expected in retained_implementation()["files"].items():
        require(
            identity.sha(inputs.read(name)) == expected,
            "retained companion implementation differs: " + name,
        )


def evaluate(root, request_path, *, hold_payload_path=None, assessed=True):
    inputs = Inputs(root)
    head = reviewed_export_route._git(inputs.root, "rev-parse", "HEAD")
    request_name = (
        str(Path(request_path).relative_to(inputs.root))
        if Path(request_path).is_absolute()
        else str(request_path)
    )
    request = inputs.document(request_name)
    require(
        set(request) == REQUEST_KEYS
        and type(request["schema_version"]) is int
        and request["schema_version"] == 1
        and request["capability"] == CAPABILITY,
        "invalid current semantic request",
    )
    inputs.read(POLICY)
    # Preserve the old gate's implementation closure and the additional native
    # verifiers used by this route, including the exact review parser/schema.
    implementation = {
        "src/mediaingredientmech/validation/semantic_release.py",
        "src/mediaingredientmech/validation/mapping_change_receipts.py",
        "src/mediaingredientmech/validation/reviewed_export_route.py",
        "src/mediaingredientmech/identity_projection.py",
        "src/mediaingredientmech/identity_projection_graph.py",
        "src/mediaingredientmech/identity_projection_bundle.py",
        "src/mediaingredientmech/identity_projection_frozen.py",
        "src/mediaingredientmech/ingredient_bundle_contract.py",
        "src/mediaingredientmech/validation/semantic_transition.py",
        "src/mediaingredientmech/native_acquisition.py",
        "src/mediaingredientmech/validation/semantic_owner_transition.py",
        "scripts/record_review.py",
        "schema/record_review.yaml",
        "uv.lock",
        "pyproject.toml",
        ".python-version",
    }
    for name in implementation:
        inputs.read(name)
    for name, (raw, _) in publication._CAPTURE.files.items():
        require(inputs.read(name) == raw, "native publication implementation differs: " + name)
    historical_root = reviewed_export_route._root(Path(request["historical_root"]))
    require(
        not historical_root.is_relative_to(inputs.root)
        and not inputs.root.is_relative_to(historical_root),
        "historical/current roots must be disjoint",
    )
    scratch = inputs.root / ".temp"
    scratch.mkdir(exist_ok=True)
    history = historical_proof(historical_root, request["historical_revision"], scratch)
    provenance = inputs.document(publication.PROVENANCE)
    for name in publication.OUTPUTS:
        inputs.read(name)
    reviewed_export_route.check_route(
        inputs.root,
        Path(request["mapping_review"]),
        route="ordinary",
        companion_review=Path(request["companion_review"]),
        historical_root=historical_root,
        historical_revision=request["historical_revision"],
    )
    mapping = reviewed_sssom.load_review(
        inputs.root, safe_member(inputs.root, request["mapping_review"])
    )
    for path, expected in mapping["input_snapshot"].items():
        inputs.read(str(path.relative_to(inputs.root)), expected)
    companion = inputs.document(request["companion_review"])
    _retained_companion_implementation(inputs, companion)
    for group in ("inputs", "record_inputs"):
        for name, expected in companion[group].items():
            inputs.read(name, expected)
    inputs.read(companion["claims_file"], companion["claims_sha256"])
    records, hashes, mappings, edges = current_graph(inputs, request["bundle"])
    from mediaingredientmech.validation.semantic_transition import verify as verify_transition

    transition = verify_transition(
        inputs,
        request["transition"],
        history,
        {name: inputs.raw[name] for name in records},
        {
            name: inputs.read(name)
            for name in ("data/ids/mim_id_registry.tsv", "data/ids/mim_id_lifecycle.tsv")
        },
    )
    require(transition["provenance"] == provenance, "semantic transition provenance differs")
    payloads = hold_payloads(history, records, hashes, mappings, provenance)
    if not assessed:
        hold_conclusions = {p["hold_id"]: "WITHHOLD" for p in payloads}
    elif hold_payload_path is None:
        require(not request["hold_reviews"], "hold review needs its frozen payload file")
        hold_conclusions = {p["hold_id"]: "WITHHOLD" for p in payloads}
    else:
        require(
            inputs.document(hold_payload_path) == {"schema_version": 1, "holds": payloads},
            "hold review payload file differs",
        )
        hold_conclusions = _hold_reviews(inputs, request, payloads, hold_payload_path)
    by_position = {x["source_position"]: x for x in mapping["decisions"]}
    for payload in payloads if assessed else []:
        position = mappings.index(payload["current_row"]) + 1
        require(
            by_position[position]["disposition"] == hold_conclusions[payload["hold_id"]],
            "current mapping review overrides an unreviewed historical hold",
        )
    decisions = []
    for item in semantic_release.current_assertions(
        records, mappings, hashes, identity.sha(inputs.raw[SOURCE])
    ):
        decision = dict(
            item,
            resolution_status="OPEN",
            review_reason="No current assertion-level release approval; historical evidence remains preserved.",
            review_evidence="",
        )
        if item["assertion_type"] == "mapping":
            current = by_position[int(item["source_position"])]
            decision.update(
                resolution_status="APPROVED" if current["disposition"] == "SUPPORTED" else "OPEN",
                review_reason=current["review_reason"],
                review_evidence=request["mapping_review"],
            )
        decisions.append(decision)
    # Historical scientific findings remain explicit. The route cannot close
    # one merely because a new source record or current mapping was reviewed.
    old = history["original"]
    historical_findings = historical_graph.read_table(
        history["before"][old["finding_dispositions"]]
    )
    if assessed:
        finding_dispositions, blocking_findings = current_findings(
            inputs, history, records, hashes, request
        )
    else:
        # Inspection is not current finding adjudication or release approval.
        finding_dispositions = []
        blocking_findings = sorted(item["finding_id"] for item in historical_findings)
    blocking = sorted(x["assertion_id"] for x in decisions if x["resolution_status"] == "OPEN")
    gaps = semantic_release.evidence_gaps(records)
    require(
        identity.record_paths(inputs.root) == sorted(records), "current owner inventory drifted"
    )
    inputs.recheck()
    history["proof"].recheck()
    require(
        reviewed_export_route._historical_checkout(historical_root, request["historical_revision"])
        == history["checkout"],
        "historical checkout changed during current review",
    )
    # The portable consumer reconstructs semantic evidence. Original-root
    # transaction verification remains separate; no saved PASS replaces this
    # reconstruction or the exact captured-input terminal checks.
    inputs.recheck()
    require(identity.record_paths(inputs.root) == sorted(records), "late owner inventory drift")
    require(
        reviewed_export_route._git(inputs.root, "rev-parse", "HEAD") == head,
        "HEAD changed during review",
    )
    history["proof"].recheck()
    require(
        reviewed_export_route._historical_checkout(historical_root, request["historical_revision"])
        == history["checkout"],
        "late historical checkout drift",
    )
    return {
        "request": request,
        "request_path": request_name,
        "inputs": inputs.hashes(),
        "record_inputs": hashes,
        "decisions": decisions,
        "holds": payloads,
        "hold_conclusions": hold_conclusions,
        "historical_findings": historical_findings,
        "finding_dispositions": finding_dispositions,
        "historical_release_holds": read_json(history["before"][old["release_holds"]]),
        "historical_review_sha256": identity.sha(history["original_raw"]),
        "historical_result": history["result"],
        "blocking_finding_ids": blocking_findings,
        "blocking_assertion_ids": blocking,
        "evidence_gaps": gaps,
        "release_verdict": "FAIL" if blocking_findings or blocking or gaps else "PASS",
    }


def products(state, output, hold_payload_path):
    prefix = output.as_posix()
    dispositions = table(state["decisions"], list(state["decisions"][0]))
    history = encoded(
        {
            "findings": state["historical_findings"],
            "release_holds": state["historical_release_holds"],
            "review_sha256": state["historical_review_sha256"],
        }
    )
    outputs = {
        prefix + "/assertion-dispositions.tsv": dispositions,
        prefix + "/historical-obligations.json": history,
        prefix
        + "/finding-dispositions.tsv": table(
            state["finding_dispositions"], list(state["finding_dispositions"][0])
        ),
    }
    report = {
        key: state[key]
        for key in (
            "record_inputs",
            "blocking_finding_ids",
            "blocking_assertion_ids",
            "evidence_gaps",
            "release_verdict",
        )
    }
    report.update(
        schema_version=1,
        current_semantic_graph={
            "capability": CAPABILITY,
            "request": state["request_path"],
            "hold_payloads": hold_payload_path,
        },
        bundle=state["request"]["bundle"],
        mapping_review=state["request"]["mapping_review"],
        assertion_dispositions=prefix + "/assertion-dispositions.tsv",
        finding_dispositions=prefix + "/finding-dispositions.tsv",
        historical_obligations=prefix + "/historical-obligations.json",
        inputs={**state["inputs"], **{name: identity.sha(raw) for name, raw in outputs.items()}},
        scientific_approval_added=False,
    )
    outputs[prefix + "/review.json"] = encoded(report)
    return outputs


def validate(root: Path | str, report_path: Path | str) -> dict:
    root = reviewed_export_route._root(Path(root))
    report_path = Path(report_path)
    if not report_path.is_absolute():
        report_path = safe_member(root, report_path.as_posix())
    raw = report_path.read_bytes()
    report = read_json(raw)
    context = report["current_semantic_graph"]
    require(
        set(context) == {"capability", "request", "hold_payloads"}
        and context["capability"] == CAPABILITY,
        "invalid current semantic route",
    )
    state = evaluate(root, context["request"], hold_payload_path=context["hold_payloads"])
    expected = products(state, report_path.parent.relative_to(root), context["hold_payloads"])
    for name, content in expected.items():
        require(
            safe_member(root, name).read_bytes() == content,
            "current semantic report/product drift: " + name,
        )
    require(report_path.read_bytes() == raw, "report changed during validation")
    return {
        "integrity": "PASS",
        "semantic_release": state["release_verdict"],
        "blocking_findings": len(state["blocking_finding_ids"]),
        "blocking_assertions": len(state["blocking_assertion_ids"]),
        "evidence_gaps": state["evidence_gaps"],
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("command", choices=("capture-transition", "inspect", "build", "validate"))
    parser.add_argument("--root", type=Path, default=Path.cwd())
    parser.add_argument("--request", type=Path)
    parser.add_argument("--hold-payloads")
    parser.add_argument("--output", type=Path)
    parser.add_argument("--report", type=Path)
    parser.add_argument("--publication-stage", type=Path)
    parser.add_argument("--publication-receipt", type=Path)
    args = parser.parse_args()
    if args.command == "capture-transition":
        from mediaingredientmech.validation.semantic_transition import capture

        require(
            args.publication_stage is not None
            and args.publication_receipt is not None
            and args.output is not None,
            "publication stage/receipt and fresh output required",
        )
        print(
            json.dumps(
                capture(args.root, args.publication_stage, args.publication_receipt, args.output),
                indent=2,
            )
        )
        return
    if args.command == "validate":
        require(args.report is not None, "report required")
        print(json.dumps(validate(args.root, args.report), indent=2))
        return
    require(args.request is not None and args.output is not None, "request/output required")
    state = evaluate(
        args.root,
        args.request,
        hold_payload_path=args.hold_payloads,
        assessed=args.command != "inspect",
    )
    output = safe_member(args.root, args.output.as_posix())
    output.mkdir(parents=False, exist_ok=False)
    if args.command == "inspect":
        artifacts = {
            args.output.as_posix()
            + "/hold-payloads.json": encoded({"schema_version": 1, "holds": state["holds"]})
        }
    else:
        artifacts = products(state, args.output, args.hold_payloads)
    for name, content in artifacts.items():
        with safe_member(args.root, name).open("xb") as stream:
            stream.write(content)
    print(
        json.dumps(
            {
                "outputs": {name: identity.sha(raw) for name, raw in artifacts.items()},
                "scientific_approval_added": False,
            },
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
