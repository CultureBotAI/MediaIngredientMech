"""Reviewed source-to-permanent-MIM candidate products, separate from grounding (#1299).

This product grants no production permission. Neither an alias nor an external
mapping can authorize a source identity. Native scientific reports must assess
the entire source row, every occurrence, and the current owning record.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import io
import json
import re
import tempfile
import types
from pathlib import Path

from mediaingredientmech.export import reviewed_sssom as external
from mediaingredientmech.mapping_scope import _load_yaml
from mediaingredientmech.review_claims import payload_sha256
from mediaingredientmech.stable_ids import (
    LIFECYCLE_PATH,
    MIM_PREFIX,
    REGISTRY_PATH,
    parse_registry,
    validate_id,
    validate_records,
)

# The captured execution loader supplies this object before compiling the module.
_PRODUCER_CAPTURE = globals().get("_PRODUCER_CAPTURE")

CAPABILITY = "reviewed-source-bindings-v1"
REPOSITORY = "CultureBotAI/MediaIngredientMech"
HELPER = "scripts/record_review.py"
SCHEMA = "schema/record_review.yaml"
EXTERNAL_SOURCE = "mappings/ingredient_mappings.sssom.tsv"
PRODUCER_PATHS = (
    "src/mediaingredientmech/export/source_bindings.py",
    "src/mediaingredientmech/export/reviewed_sssom.py",
    "src/mediaingredientmech/stable_ids.py",
    "src/mediaingredientmech/review_claims.py",
    "src/mediaingredientmech/mapping_scope.py",
    "src/mediaingredientmech/curie.py",
    "src/mediaingredientmech/synonym_policy.py",
    "src/mediaingredientmech/sssom_metadata.py",
    "src/mediaingredientmech/identity_projection.py",
    "src/mediaingredientmech/export/source_producer.py",
)
PRODUCER_AUXILIARY = ("uv.lock", "pyproject.toml", ".python-version")
ALGORITHM = "mim-source-identity-sha256-v1"
PAYLOAD_DESCRIPTION = (
    "Entire source row, all exact occurrences, proposed owner bytes, mapping status and holds"
)
SOURCE_FIELDS = (
    "subject_id",
    "subject_label",
    "predicate_id",
    "object_id",
    "object_label",
    "mapping_justification",
    "comment",
)


def _require(condition, message):
    if not condition:
        raise ValueError("Source identity candidate: " + message)


def _keys(value, fields):
    _require(isinstance(value, dict) and set(value) == set(fields), "unexpected/missing fields")


def _json(value):
    return (
        json.dumps(value, sort_keys=True, indent=2, ensure_ascii=False, allow_nan=False) + "\n"
    ).encode()


def _sha(raw):
    return hashlib.sha256(raw).hexdigest()


def _text(value):
    return isinstance(value, str) and bool(value.strip())


def _table(raw, required):
    reader = csv.DictReader(io.StringIO(raw.decode("utf-8"), newline=""), delimiter="\t")
    fields = reader.fieldnames
    _require(
        fields and len(set(fields)) == len(fields) and set(required) <= set(fields),
        "invalid TSV columns",
    )
    rows = list(reader)
    _require(all(None not in row and None not in row.values() for row in rows), "malformed TSV row")
    return rows


def source_selector(position, source_id):
    """Exact native snapshot-row selector; display labels are never a key."""
    return json.dumps(
        {"source_position": position, "source_id": source_id}, sort_keys=True, separators=(",", ":")
    )


def graph_id(mim_id):
    """Disambiguate the graph prefix without changing the permanent concept URI."""
    return validate_id(mim_id).replace("MIM:", "MIM.ingredient:", 1)


def expand_mim(value):
    canonical = value.replace("MIM.ingredient:", "MIM:", 1)
    return MIM_PREFIX + validate_id(canonical).split(":", 1)[1]


class _Inputs:
    def __init__(self, root):
        self.root = Path(root).resolve()
        self.hashes = {}
        self.bytes = {}
        self.reports = {}
        self.git_head = _PRODUCER_CAPTURE.start_context(self.root)

    def read(self, name, expected=None):
        if isinstance(name, str) and name in self.hashes:
            _require(
                expected is None or self.hashes[name] == expected, "conflicting input pin: " + name
            )
            return self.bytes[name]
        return self._fresh(name, expected)

    def _fresh(self, name, expected=None):
        _require(
            isinstance(name, str)
            and name
            and not Path(name).is_absolute()
            and ".." not in Path(name).parts,
            "input path must be repository-relative",
        )
        path = self.root / name
        _require(not any(p.is_symlink() for p in (path, *path.parents)), "symlink input refused")
        raw = path.read_bytes()
        digest = _sha(raw)
        _require(expected is None or digest == expected, "stale input: " + name)
        _require(
            name not in self.hashes or self.hashes[name] == digest,
            "input changed during read: " + name,
        )
        self.hashes[name], self.bytes[name] = digest, raw
        return raw

    def recheck(self):
        for name, expected in list(self.hashes.items()):
            self._fresh(name, expected)
        _PRODUCER_CAPTURE.check_context(self.root, self.git_head)


def _inventory(root):
    paths = []
    for category in ("mapped", "unmapped"):
        directory = root / "data/ingredients" / category
        _require(
            directory.is_dir() and not directory.is_symlink(), "missing/aliased record directory"
        )
        paths.extend(p.relative_to(root).as_posix() for p in directory.glob("*.yaml"))
    return sorted(paths)


def _native(inputs):
    raw = inputs.read(HELPER)
    inputs.read(SCHEMA)
    module = types.ModuleType("source_identity_native_review")
    module.__file__ = str(inputs.root / HELPER)
    exec(compile(raw, module.__file__, "exec"), module.__dict__)
    return module


def _assessment(inputs, native, reference, payload, required_inputs):
    _keys(reference, {"path", "target_id", "assessment_id"})
    path = reference["path"]
    markdown = str(Path(path).with_name("review.md"))
    _require(
        path in inputs.hashes and markdown in inputs.hashes, "native report pair must be pinned"
    )
    if path not in inputs.reports:
        report = native.parse_review_bundle(
            path, inputs.bytes[path], inputs.bytes[markdown], inputs.root / SCHEMA
        )
        provenance = native.source_provenance(inputs.root, report)
        _require(
            provenance["status"] not in {"invalid", "unverified"},
            "invalid native report provenance",
        )
        _require(
            report["repository"] == REPOSITORY
            and report["completion"] == "completed"
            and report["scientific_review"] is True,
            "requires completed native scientific review",
        )
        source_inputs = {item["path"]: item["sha256"] for item in report["source"]["inputs"]}
        for name, expected in source_inputs.items():
            inputs.read(name, expected)
        inputs.reports[path] = report, provenance, source_inputs
    report, provenance, source_inputs = inputs.reports[path]
    _require(
        all(source_inputs.get(name) == digest for name, digest in required_inputs.items()),
        "native report omits current source/occurrence/owner/ledger inputs",
    )
    targets = {item["target_id"]: item for item in report["targets"]}
    assessments = {item["assessment_id"]: item for item in report["assessments"]}
    target = targets.get(reference["target_id"], {})
    assessment = assessments.get(reference["assessment_id"], {})
    _require(
        target.get("kind") == "snapshot_row"
        and target.get("path") == payload["source_path"]
        and target.get("selector")
        == source_selector(payload["source_position"], payload["source_id"])
        and target.get("semantic_digest")
        == {
            "algorithm": ALGORITHM,
            "sha256": payload_sha256(payload),
            "description": PAYLOAD_DESCRIPTION,
        },
        "native target does not bind complete identity payload",
    )
    owners = [(item["repository"], item["path"]) for item in target.get("owner_paths", [])]
    _require(
        owners == [(REPOSITORY, payload["owner_record"] or payload["source_path"])],
        "native target owner differs",
    )
    _require(
        assessment.get("target_ids") == [reference["target_id"]]
        and assessment.get("area") == "identity"
        and reference["target_id"] in report["scope"]["reviewed_target_ids"],
        "native identity assessment differs",
    )
    dimensions = {item["name"]: item["value"] for item in assessment.get("dimensions", [])}
    _require(
        dimensions.get("source_identity_scope") == "all_source_occurrences",
        "identity scope must explicitly cover all occurrences",
    )
    conclusion = dimensions.get("source_identity_disposition")
    _require(
        conclusion in {"same_material", "withhold"}, "missing explicit source identity disposition"
    )
    supported = conclusion == "same_material"
    if supported:
        _require(
            assessment["outcome"] == "supported"
            and report["verdict"] in {"pass", "pass_with_limitations", "needs_curation"},
            "unsupported native identity verdict",
        )
        _require(
            not any(
                reference["target_id"] in item["target_ids"]
                and item["status"] in {"open", "deferred"}
                for item in report["findings"]
            ),
            "unresolved native finding",
        )
        evidence = {item["evidence_id"]: item for item in report["evidence"]}
        _require(
            any(
                evidence[key]["kind"] in {"primary_source", "database", "authority"}
                and evidence[key]["support"] == "supports"
                and evidence[key]["reference"] in source_inputs
                and evidence[key].get("snapshot_sha256")
                == source_inputs[evidence[key]["reference"]]
                for key in assessment["evidence_ids"]
            ),
            "source identity requires captured primary evidence",
        )
    return {
        "supported": supported,
        "reviewer": report["reviewer"],
        "reference": reference,
        "assessment": assessment,
        "provenance": provenance,
    }


def _prepare(root, review_path):
    inputs = _Inputs(root)
    review_path = Path(review_path)
    if review_path.is_absolute():
        review_path = review_path.relative_to(inputs.root)
    review = external._json_bytes(inputs.read(review_path.as_posix()), str(review_path))
    _keys(
        review,
        {
            "schema_version",
            "capability",
            "source",
            "record_inputs",
            "ledger_inputs",
            "inputs",
            "external_review",
            "cases",
        },
    )
    _require(
        review["schema_version"] == 1 and review["capability"] == CAPABILITY, "unsupported contract"
    )
    source = review["source"]
    _keys(
        source,
        {
            "nodes",
            "nodes_sha256",
            "occurrences",
            "occurrences_sha256",
            "id_column",
            "label_column",
            "occurrence_id_column",
            "curie_map",
        },
    )
    _require(source["nodes"] != source["occurrences"], "source and occurrence tables must differ")
    rows = _table(
        inputs.read(source["nodes"], source["nodes_sha256"]),
        (source["id_column"], source["label_column"]),
    )
    occurrences = _table(
        inputs.read(source["occurrences"], source["occurrences_sha256"]),
        (source["occurrence_id_column"],),
    )
    identifiers = [row[source["id_column"]] for row in rows]
    _require(
        len(set(identifiers)) == len(identifiers)
        and all(re.fullmatch(r"[^\s:]+:[^\s]+", value) for value in identifiers),
        "source IDs must be unique CURIEs; labels cannot split an ambiguous entity",
    )
    _require(
        isinstance(source["curie_map"], dict)
        and all(
            _text(key) and isinstance(value, str) and re.match(r"https?://|urn:", value)
            for key, value in source["curie_map"].items()
        )
        and {value.split(":", 1)[0] for value in identifiers} <= set(source["curie_map"]),
        "source namespaces must have explicit URI expansions",
    )
    for prefix, iri in {
        "MIM": MIM_PREFIX,
        "MIM.ingredient": MIM_PREFIX,
        "skos": "http://www.w3.org/2004/02/skos/core#",
        "semapv": "https://w3id.org/semapv/vocab/",
    }.items():
        _require(
            prefix not in source["curie_map"] or source["curie_map"][prefix] == iri,
            "conflicting reserved namespace",
        )
    grouped = {value: [] for value in identifiers}
    for position, row in enumerate(occurrences, 1):
        identifier = row[source["occurrence_id_column"]]
        _require(identifier in grouped, "occurrence has no source entity")
        grouped[identifier].append({"position": position, "row": row})
    inventory = _inventory(inputs.root)
    _require(
        isinstance(review["record_inputs"], dict) and sorted(review["record_inputs"]) == inventory,
        "record_inputs must cover complete current corpus",
    )
    _keys(review["ledger_inputs"], {str(REGISTRY_PATH), str(LIFECYCLE_PATH)})
    for group in ("record_inputs", "ledger_inputs", "inputs"):
        _require(isinstance(review[group], dict), "invalid pinned input inventory")
        for name, digest in review[group].items():
            _require(
                isinstance(digest, str) and re.fullmatch(r"[0-9a-f]{64}", digest),
                "invalid input digest",
            )
            inputs.read(name, digest)
    registry = parse_registry(inputs.bytes[str(REGISTRY_PATH)], inputs.bytes[str(LIFECYCLE_PATH)])
    records = {name: _load_yaml(inputs.bytes[name].decode()) for name in inventory}
    validate_records(registry, records)
    cases = review["cases"]
    _require(
        isinstance(cases, list) and len(cases) == len(rows), "cases must cover every source row"
    )
    payloads = []
    for position, (row, case) in enumerate(zip(rows, cases, strict=True), 1):
        _keys(case, {"source_position", "owner_record", "holds", "primary", "skeptic"})
        _require(
            type(case["source_position"]) is int and case["source_position"] == position,
            "cases must retain complete source order",
        )
        owner = case["owner_record"]
        _require(owner is None or owner in records, "unknown proposed owner")
        _require(
            isinstance(case["holds"], list) and all(_text(item) for item in case["holds"]),
            "invalid scientific holds",
        )
        record = records[owner] if owner else {}
        identifier = row[source["id_column"]]
        payload = {
            "source_definition": source,
            "source_path": source["nodes"],
            "source_position": position,
            "source_id": identifier,
            "source_row": row,
            "occurrence_path": source["occurrences"],
            "occurrences": grouped[identifier],
            "owner_record": owner,
            "owner_record_sha256": review["record_inputs"].get(owner),
            "mim_id": record.get("mim_id"),
            "mapping_status": record.get("mapping_status"),
            "holds": case["holds"],
        }
        payloads.append(payload)
    return inputs, review, payloads, records, inventory, len(occurrences)


def inspect_candidates(root, review_path):
    """Prepare exact native review targets and hashes, without an approval verdict."""
    inputs, review, payloads, _, _, _ = _prepare(root, review_path)
    targets = [
        {
            "target_id": "source-" + str(payload["source_position"]),
            "path": payload["source_path"],
            "kind": "snapshot_row",
            "label": payload["source_id"],
            "selector": source_selector(payload["source_position"], payload["source_id"]),
            "semantic_digest": {
                "algorithm": ALGORITHM,
                "sha256": payload_sha256(payload),
                "description": PAYLOAD_DESCRIPTION,
            },
            "owner_paths": [
                {
                    "repository": REPOSITORY,
                    "path": payload["owner_record"] or payload["source_path"],
                    "role": "proposed source identity owner",
                }
            ],
        }
        for payload in payloads
    ]
    inputs.recheck()
    return {
        "status": "inspection_only",
        "targets": targets,
        "payloads": payloads,
        "inputs": {
            name: digest
            for name, digest in inputs.hashes.items()
            if name in review["record_inputs"]
            or name in review["ledger_inputs"]
            or name in {review["source"]["nodes"], review["source"]["occurrences"]}
        },
    }


def _load(root, review_path):
    inputs, review, payloads, records, inventory, occurrence_count = _prepare(root, review_path)
    _PRODUCER_CAPTURE.bind(inputs)
    native = _native(inputs)
    results = []
    source = review["source"]
    for payload, case in zip(payloads, review["cases"], strict=True):
        owner, identifier = payload["owner_record"], payload["source_id"]
        record = records[owner] if owner else {}
        required = {
            source["nodes"]: source["nodes_sha256"],
            source["occurrences"]: source["occurrences_sha256"],
            **review["ledger_inputs"],
        }
        if owner:
            required[owner] = review["record_inputs"][owner]
        primary = _assessment(inputs, native, case["primary"], payload, required)
        skeptic = _assessment(inputs, native, case["skeptic"], payload, required)
        _require(
            primary["reviewer"]["identity"] != skeptic["reviewer"]["identity"]
            and case["primary"]["path"] != case["skeptic"]["path"]
            and skeptic["reviewer"]["independence"] == "independent",
            "requires a distinct independent skeptical reviewer",
        )
        supported = primary["supported"] and skeptic["supported"]
        _require(
            not supported
            or (
                owner
                and not case["holds"]
                and record.get("mapping_status") in {"MAPPED", "UNMAPPED"}
            ),
            "held/ambiguous/rejected/ownerless source identity cannot be supported",
        )
        prefix, local = identifier.split(":", 1)
        _require(
            not supported or expand_mim(record["mim_id"]) != source["curie_map"][prefix] + local,
            "source identity self-loop refused",
        )
        results.append(
            {
                "payload": payload,
                "payload_sha256": payload_sha256(payload),
                "disposition": "SUPPORTED" if supported else "WITHHOLD",
                "primary": primary,
                "skeptic": skeptic,
                "binding": {
                    "subject_id": identifier,
                    "subject_label": payload["source_row"][source["label_column"]],
                    "predicate_id": "skos:exactMatch",
                    "object_id": record.get("mim_id", ""),
                    "object_label": record.get("preferred_term", ""),
                    "mapping_justification": "semapv:ManualMappingCuration",
                    "comment": "Candidate only; payload sha256="
                    + payload_sha256(payload)
                    + "; primary="
                    + case["primary"]["path"]
                    + "; skeptic="
                    + case["skeptic"]["path"],
                },
            }
        )
    _keys(review["external_review"], {"path", "sha256"})
    ref = review["external_review"]
    inputs.read(ref["path"], ref["sha256"])
    loaded = external.load_review(inputs.root, inputs.root / ref["path"])
    _require(
        loaded["review"]["source_sssom"] == EXTERNAL_SOURCE,
        "external review must cover the current root canonical SSSOM",
    )
    for path, digest in loaded["input_snapshot"].items():
        inputs.read(path.relative_to(inputs.root).as_posix(), digest)
    _require(
        all(
            row["subject_id"] in {record["mim_id"] for record in records.values()}
            for row in loaded["rows"]
        ),
        "external mappings must use current permanent subjects",
    )
    _require(
        all(row["subject_id"] != row["object_id"] for row in loaded["rows"]),
        "external self-loop refused",
    )
    products, external_manifest = external._products(loaded)
    _require(inventory == _inventory(inputs.root), "record inventory changed")
    inputs.recheck()
    return inputs, review, results, products, external_manifest, occurrence_count


def expected_products(root, review_path, *, _generation_receipt=None):
    """Reconstruct all candidate bytes from current sources and native reviews."""
    inputs, review, cases, external_products, external_manifest, occurrence_count = _load(
        root, review_path
    )
    products = {"external-" + name: raw for name, raw in external_products.items()}
    for status, name in (
        ("SUPPORTED", "source-bindings.sssom.tsv"),
        ("WITHHOLD", "withheld-source-bindings.sssom.tsv"),
    ):
        metadata = {
            "mapping_set_id": "urn:sha256:" + payload_sha256(review) + ":" + status.lower(),
            "mapping_set_description": "Candidate source identity, "
            + status
            + "; no production permission. Exact native decisions in source-decisions.json.",
            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
            "predicate_semantics": "skos",
            "curie_map": {
                **review["source"]["curie_map"],
                "MIM": MIM_PREFIX,
                "skos": "http://www.w3.org/2004/02/skos/core#",
                "semapv": "https://w3id.org/semapv/vocab/",
            },
        }
        header = "".join(
            "# " + line + "\n"
            for line in external.yaml.safe_dump(metadata, sort_keys=False).splitlines()
        ).encode()
        products[name] = header + external._tsv(
            SOURCE_FIELDS,
            [
                case["binding"]
                for case in cases
                if case["disposition"] == status and case["payload"]["owner_record"] is not None
            ],
        )
    products["source-decisions.json"] = _json(cases)
    producer = (
        _PRODUCER_CAPTURE.receipt(inputs)
        if _generation_receipt is None
        else _PRODUCER_CAPTURE.validate_receipt(_generation_receipt, inputs)
    )
    products["producer.json"] = _json(producer)
    counts = {
        "source_entities": len(cases),
        "source_occurrences": occurrence_count,
        "supported": sum(case["disposition"] == "SUPPORTED" for case in cases),
        "withheld": sum(case["disposition"] == "WITHHOLD" for case in cases),
        "withheld_without_owner": sum(case["payload"]["owner_record"] is None for case in cases),
    }
    manifest = {
        "schema_version": 1,
        "required_capabilities": [CAPABILITY],
        "semantic_status": "REVIEWED_CANDIDATE_ONLY",
        "production_authorized": False,
        "curie_map": {"MIM": MIM_PREFIX, "MIM.ingredient": MIM_PREFIX},
        "counts": counts,
        "external_counts": external_manifest["counts"],
        "producer": {
            "receipt": "producer.json",
            "source_sha256": producer["source_sha256"],
            "selected_context": producer["selected_context"],
        },
        "inputs": inputs.hashes,
        "files": {name: _sha(raw) for name, raw in products.items()},
    }
    products["manifest.json"] = _json(manifest)
    inputs.recheck()
    return products, manifest


def validate_candidate(root, review_path, output):
    output = Path(output)
    _require(
        not output.is_symlink() and not (output / "producer.json").is_symlink(),
        "symlink output refused",
    )
    receipt = external._json_bytes((output / "producer.json").read_bytes(), "producer.json")
    products, manifest = expected_products(root, review_path, _generation_receipt=receipt)
    _require(
        not output.is_symlink() and {path.name for path in output.iterdir()} == set(products),
        "unexpected output inventory",
    )
    for name, raw in products.items():
        path = output / name
        _require(
            not path.is_symlink() and path.is_file() and path.read_bytes() == raw,
            "candidate bytes differ: " + name,
        )
    validate_sssom_partitions(output, manifest)
    return manifest


def validate_sssom_partitions(output, manifest):
    """Use the maintained SSSOM parser/schema and reject silent row loss."""
    from collections import Counter

    from sssom.parsers import parse_sssom_table, to_mapping_set_document
    from sssom.validators import validate_json_schema

    for name, count in (
        ("source-bindings.sssom.tsv", manifest["counts"]["supported"]),
        (
            "withheld-source-bindings.sssom.tsv",
            manifest["counts"]["withheld"] - manifest["counts"]["withheld_without_owner"],
        ),
        ("external-ingredient_mappings.sssom.tsv", manifest["external_counts"]["supported"]),
        ("external-withheld_mappings.sssom.tsv", manifest["external_counts"]["withhold"]),
    ):
        path = Path(output) / name
        rows = _table(
            "".join(
                line
                for line in path.read_text().splitlines(keepends=True)
                if not line.startswith("#")
            ).encode(),
            ("subject_id", "predicate_id", "object_id"),
        )
        native = parse_sssom_table(path, strict=True)
        _require(
            len(rows)
            == len(native.df)
            == len(to_mapping_set_document(native).mapping_set.mappings or [])
            == count,
            "SSSOM parser changed source identity row count",
        )
        keys = ("subject_id", "predicate_id", "object_id")
        _require(
            Counter(tuple(row[key] for key in keys) for row in rows)
            == Counter(tuple(row[key] for key in keys) for row in native.df.to_dict("records")),
            "SSSOM parser changed source identities",
        )
        validate_json_schema(native, fail_on_error=True)


def export_candidate(root, review_path, output):
    """Create one immutable candidate directory; never replace existing output."""
    output = Path(output).absolute()
    _require(
        not any(path.is_symlink() for path in (output, *output.parents)), "symlink output refused"
    )
    _require(not output.exists(), "candidate output already exists")
    products, manifest = expected_products(root, review_path)
    _require(
        not any(
            (Path(root) / name).resolve().is_relative_to(output) for name in manifest["inputs"]
        ),
        "output overlaps an input",
    )
    output.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(prefix=".source-candidate-", dir=output.parent) as temporary:
        stage = Path(temporary) / "candidate"
        stage.mkdir()
        for name, raw in products.items():
            (stage / name).write_bytes(raw)
        validate_candidate(root, review_path, stage)
        # mkdir is the reservation: a competing writer cannot be overwritten.
        # This is a validated immutable candidate, not an atomic live promotion.
        output.mkdir()
        try:
            for name in [name for name in products if name != "manifest.json"] + ["manifest.json"]:
                with (output / name).open("xb") as stream:
                    stream.write((stage / name).read_bytes())
            return validate_candidate(root, review_path, output)
        except BaseException as exc:
            # Keep diagnostic bytes; the additional failure marker makes exact
            # inventory verification fail even if a manifest was already written.
            with (output / "FAILED.json").open("xb") as stream:
                stream.write(
                    _json(
                        {
                            "status": "FAILED_INCOMPLETE_CANDIDATE",
                            "error_type": type(exc).__name__,
                            "message": str(exc),
                        }
                    )
                )
            raise


def consumer_claims(root, review_path, output, *, capabilities):
    """Validated candidate assertions; never infer ontology identity or subclass."""
    _require(CAPABILITY in capabilities, "consumer lacks required capability")
    validate_candidate(root, review_path, output)
    cases = json.loads((Path(output) / "source-decisions.json").read_bytes())
    claims = []
    for case in cases:
        if case["disposition"] == "SUPPORTED":
            row = case["binding"]
            claims.append(
                {
                    **row,
                    "object_id": graph_id(row["object_id"]),
                    "original_subject_id": row["subject_id"],
                    "original_object_id": row["object_id"],
                    "scope": "candidate_source_identity",
                    "payload_sha256": case["payload_sha256"],
                }
            )
    return claims


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path("."))
    parser.add_argument("--review", type=Path, required=True)
    parser.add_argument("--output", type=Path)
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("--validate-only", action="store_true")
    mode.add_argument("--inspect", action="store_true")
    args = parser.parse_args()
    if args.inspect:
        print(json.dumps(inspect_candidates(args.root, args.review), sort_keys=True))
        return
    if args.output is None:
        parser.error("--output is required for export/validation")
    operation = validate_candidate if args.validate_only else export_candidate
    print(json.dumps(operation(args.root, args.review, args.output), sort_keys=True))


if not globals().get("_SOURCE_BINDINGS_CAPTURED", False):
    # Compile an isolated implementation and its complete bounded MIM closure
    # from the bytes we retain. Import-time hashing of cached public modules is
    # not evidence of their executed source (#1195, #1305).
    import sys as _sys
    import uuid as _uuid

    _origin_root = Path(__file__).absolute().parents[3]
    _loader_path = _origin_root / "src/mediaingredientmech/export/source_producer.py"
    if any(path.is_symlink() for path in (_loader_path, *_loader_path.parents)):
        raise ValueError("Aliased producer loader")
    _loader_raw = _loader_path.read_bytes()
    _loader = types.ModuleType("_mim_source_loader_" + _uuid.uuid4().hex)
    _loader.__file__ = str(_loader_path)
    _sys.modules[_loader.__name__] = _loader
    exec(compile(_loader_raw, str(_loader_path), "exec"), _loader.__dict__)
    _capture, _implementation = _loader.captured_native_modules(_origin_root, _loader_raw)
    for _name, _value in _implementation.__dict__.items():
        if not _name.startswith("__"):
            globals()[_name] = _value
    if __name__ == "__main__":
        main()
