"""Prepare and explicitly review a lossless CultureMech source intake (#1453).

Source inventory membership, source-to-record identity approval, and the native
reviewed SSSOM release are separate claims. This module never edits MIM records,
canonical mappings, or an active campaign. Unknown source contracts fail closed.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import os
import shutil
import subprocess
import sys
import tarfile
import tempfile
from collections import Counter, defaultdict
from contextlib import contextmanager
from pathlib import Path
from typing import Any, TypedDict

import yaml  # type: ignore[import-untyped]  # Locked PyYAML has no stubs; validate parsed values below.

from mediaingredientmech.export import reviewed_sssom
from mediaingredientmech.review_claims import payload_sha256, validate_review_decision
from mediaingredientmech.synonym_policy import is_resolving_synonym

ROOT = Path(__file__).resolve().parents[3]
REVIEW = "reports/sssom_completion_20260921/review.json"


class UniqueOwnerLoader(yaml.CSafeLoader):
    """Reject duplicate keys, including merge-expanded overrides (#1467)."""

    def construct_mapping(self, node, deep=False):
        # Disjoint merges retain native safe-loader semantics. Overrides create
        # repeated keys and must not silently choose an owner identity/status.
        self.flatten_mapping(node)
        seen = set()
        for key_node, _value_node in node.value:
            key = self.construct_object(key_node, deep=deep)
            if key in seen:
                raise ValueError(
                    f"Duplicate YAML mapping key {key!r} at line {key_node.start_mark.line + 1}"
                )
            seen.add(key)
        return super().construct_mapping(node, deep=deep)


class SourceContract(TypedDict):
    positive_actions: set[str]
    actions: set[str]
    held_product: str | None


CONTRACTS: dict[str, SourceContract] = {
    "culturemech-direct-ingredients-v2": {
        "positive_actions": {"ADD", "REPLACE", "SET_CONCENTRATION"},
        "actions": {"ADD", "REMOVE", "REPLACE", "SET_CONCENTRATION"},
        "held_product": None,
    },
    "culturemech-direct-ingredients-v3": {
        "positive_actions": {"ADD", "REPLACE", "SET_CONCENTRATION", "SET_AMOUNT"},
        "actions": {"ADD", "REMOVE", "REPLACE", "SET_CONCENTRATION", "SET_AMOUNT"},
        "held_product": "variant_ingredient_holds.tsv",
    },
}
PRODUCTS = {
    "ingredient_occurrences.tsv",
    "ingredients_list.tsv",
    "mapped_ingredients.yaml",
    "unmapped_ingredients.yaml",
    "ingredient_aggregation_errors.tsv",
    "variant_ingredient_changes.tsv",
}
HELD_PRODUCT = "variant_ingredient_holds.tsv"
HELD_FIELDS = (
    "recipe_id",
    "recipe_label",
    "recipe_category",
    "source_path",
    "variant_index",
    "variant_name",
    "mention_index",
    "descriptor_path",
    "source_label",
    "reported_action",
    "stage",
    "source_modification_index",
    "source_text",
    "reason",
    "reported_quantity",
    "held_fields_json",
    "evidence_json",
    "mention_json",
    "review_status",
    "counts_as_presence",
)
HELD_DIMENSIONS = {"SOURCE_CLAIM", "IDENTITY_FORM", "QUANTITY", "OPERATION", "STAGE"}
VARIANT_FIELDS = (
    "variant_index",
    "variant_name",
    "change_index",
    "change_action",
    "change_stage",
    "descriptor_role",
    "descriptor_path",
    "source_modification_index",
    "source_text",
    "evidence_json",
    "change_json",
)
CASE_FIELDS = (
    "preferred_term",
    "resolved_identifier",
    "change_action",
    "change_stage",
    "descriptor_role",
    "variant_name",
)


def require(condition, message):
    if not condition:
        raise ValueError(message)


def fingerprint(path):
    require(path.is_file() and not path.is_symlink(), f"Nonregular input: {path}")
    digest, size = hashlib.sha256(), 0
    with path.open("rb") as stream:
        while chunk := stream.read(1024 * 1024):
            digest.update(chunk)
            size += len(chunk)
    return {"sha256": digest.hexdigest(), "bytes": size}


def relative(root, value):
    path = Path(value)
    require(
        not path.is_absolute() and ".." not in path.parts and path.as_posix() == value,
        "Unsafe relative input path",
    )
    result = root / path
    require(result.resolve().is_relative_to(root.resolve()), "Input escapes root")
    return result


def read_json(path, expected=None):
    actual = fingerprint(path)
    require(expected is None or actual["sha256"] == expected, "Input hash differs from pin")
    content = path.read_bytes()
    require(hashlib.sha256(content).hexdigest() == actual["sha256"], "Input changed while reading")
    return reviewed_sssom._json_bytes(content, str(path)), actual


@contextmanager
def csv_reader(path):
    previous = csv.field_size_limit()
    try:
        csv.field_size_limit(sys.maxsize)
        with path.open(encoding="utf-8", newline="") as stream:
            reader = csv.DictReader(stream, delimiter="\t", strict=True)
            fields = reader.fieldnames or []
            require(fields and len(fields) == len(set(fields)), "Missing/duplicate TSV header")
            yield reader
    finally:
        csv.field_size_limit(previous)


def checked_row(row):
    require(
        None not in row and all(value is not None for value in row.values()),
        "Malformed TSV row width",
    )
    return row


def write_json(path, value):
    with path.open("x", encoding="utf-8") as stream:
        json.dump(value, stream, ensure_ascii=False, sort_keys=True, indent=2, allow_nan=False)
        stream.write("\n")
        stream.flush()
        os.fsync(stream.fileno())


def write_tsv(path, fields, records):
    with path.open("x", encoding="utf-8", newline="") as stream:
        writer = csv.DictWriter(stream, fields, delimiter="\t", lineterminator="\n")
        writer.writeheader()
        writer.writerows(records)


def output_preflight(output, protected):
    require(not output.exists() and not output.is_symlink(), "Output must be a new directory")
    destination = output.resolve()
    for source in protected:
        source = source.resolve()
        require(
            not destination.is_relative_to(source) and not source.is_relative_to(destination),
            "Output overlaps a source or authoritative directory",
        )


@contextmanager
def staging(output):
    """Publish last, with no fallible cleanup after acceptance."""
    directory = Path(tempfile.mkdtemp(prefix="." + output.name + "-", dir=output.parent))
    try:
        yield directory
        require(not output.exists() and not output.is_symlink(), "Output appeared during staging")
        directory.rename(output)
    except BaseException:
        if directory.exists():
            shutil.rmtree(directory)
        raise


def verify_handoff(handoff, pin):
    receipt, receipt_hash = read_json(handoff / "handoff.json", pin)
    require(
        receipt["status"] == "VERIFIED_SOURCE_CANDIDATE_PENDING_ADOPTION",
        "Expected a verified pending-adoption source handoff",
    )
    manifest, manifest_hash = read_json(
        handoff / "bundle/manifest.json", receipt["manifest_sha256"]
    )
    require(manifest["contract"] in CONTRACTS, "Unsupported CultureMech source contract")
    require(receipt["contract"] == manifest["contract"], "Contract mismatch")
    require(
        not manifest["git"]["dirty"] and manifest["git"]["commit"] == receipt["producer_commit"],
        "Expected pinned clean producer",
    )
    require(manifest["scope"] == "full_catalog_direct_ingredients", "Full-catalog source required")
    held_product = CONTRACTS[manifest["contract"]]["held_product"]
    expected_products = PRODUCTS | ({held_product} if held_product else set())
    require(set(manifest["products"]) == expected_products, "Unexpected source product membership")
    snapshots = {"handoff.json": receipt_hash, "bundle/manifest.json": manifest_hash}
    for name, expected in manifest["products"].items():
        actual = fingerprint(relative(handoff, "bundle/" + name))
        require(
            actual == {key: expected[key] for key in ("sha256", "bytes")},
            "Source product differs from manifest: " + name,
        )
        snapshots["bundle/" + name] = actual
    for name, key in (
        ("producer-source.tar.gz", "source_archive_sha256"),
        ("coverage/summary.json", "coverage_summary_sha256"),
        ("original-review-queue.tsv", "queue_sha256"),
    ):
        actual = fingerprint(handoff / name)
        require(actual["sha256"] == receipt[key], "Source handoff pin mismatch: " + name)
        snapshots[name] = actual
    coverage, _ = read_json(handoff / "coverage/summary.json")
    require(
        coverage["result"] == "PASS" and coverage["mode"] == "postapply",
        "Coverage not postapply PASS",
    )
    require(
        coverage["applied_assertions"] == manifest["counts"]["variant_change_events"],
        "Source event/coverage count mismatch",
    )
    if held_product:
        require(
            type(coverage.get("held_mentions")) is int
            and coverage["held_mentions"] == manifest["counts"]["variant_held_mentions"],
            "Source held-mention/coverage count mismatch",
        )
    actual = fingerprint(handoff / "coverage/coverage.tsv")
    require(actual["sha256"] == coverage["coverage_sha256"], "Coverage ledger hash mismatch")
    snapshots["coverage/coverage.tsv"] = actual
    require(coverage["queue_sha256"] == receipt["queue_sha256"], "Coverage queue pin mismatch")
    queued: dict[str, str] = {}
    with csv_reader(handoff / "original-review-queue.tsv") as reader:
        queue_rows = list(reader)
    for row in queue_rows:
        row = checked_row(row)
        key = "data/normalized_yaml/" + row["source_path"]
        relative(handoff, key)
        require(
            key not in queued or queued[key] == row["source_sha256"], "Inconsistent queue preimage"
        )
        queued[key] = row["source_sha256"]
    seen = set()
    for item in coverage["record_snapshots"]:
        path = item["path"]
        require(path not in seen and path in queued, "Duplicate/unexpected coverage record")
        seen.add(path)
        require(item["base_sha256"] == queued[path], "Queue/coverage preimage mismatch")
        key = path.removeprefix("data/normalized_yaml/")
        require(
            item["current_sha256"] == manifest["inputs"][key]["sha256"],
            "Coverage belongs to different recipe bytes",
        )
    require(seen == set(queued), "Incomplete coverage membership")
    require(
        coverage["queue_rows"] == len(queue_rows) and coverage["queue_recipes"] == len(queued),
        "Queue coverage accounting mismatch",
    )
    require(
        all(type(n) is int and n >= 0 for n in coverage["dispositions"].values())
        and sum(coverage["dispositions"].values()) == len(queue_rows),
        "Disposition accounting mismatch",
    )
    return receipt, manifest, coverage, snapshots


def verify_producer(source, manifest, python, producer_root=None):
    """Execute only the hash-pinned archived producer, never a moving checkout."""
    temporary = None
    if producer_root is None:
        temporary = tempfile.TemporaryDirectory(prefix=".producer-verify-", dir=source.parent)
        extraction = Path(temporary.name)
        with tarfile.open(source / "producer-source.tar.gz", "r:gz") as archive:
            names = set()
            for member in archive.getmembers():
                path = Path(member.name)
                require(
                    not path.is_absolute()
                    and ".." not in path.parts
                    and path.parts
                    and path.parts[0] == "producer",
                    "Unsafe producer archive path",
                )
                require(member.name not in names, "Duplicate producer archive member")
                names.add(member.name)
            archive.extractall(extraction, filter="data")
        producer_root = extraction / "producer"
    try:
        expected = dict(manifest["dependencies"])
        expected.update(
            {"data/normalized_yaml/" + name: value for name, value in manifest["inputs"].items()}
        )
        for name, digest in expected.items():
            require(
                fingerprint(relative(producer_root, name)) == digest,
                "Producer bytes differ from candidate: " + name,
            )
        command = [
            str(python),
            "scripts/ingredient_release_bundle.py",
            "verify",
            "--bundle-dir",
            str((source / "bundle").resolve()),
            "--expected-manifest-sha256",
            fingerprint(source / "bundle/manifest.json")["sha256"],
        ]
        result = subprocess.run(
            command, cwd=producer_root, text=True, capture_output=True, check=True
        )
        verification = json.loads(result.stdout)
        require(
            verification["status"] == "VERIFIED_CANDIDATE"
            and verification["assurance"] == "externally_pinned_manifest"
            and verification["counts"] == manifest["counts"],
            "Producer verification did not match source",
        )
        return verification
    finally:
        if temporary is not None:
            temporary.cleanup()


def mim_snapshot(root):
    """Exact label candidates, retaining rejected owners rather than resolving them."""
    index, records, hashes = defaultdict(set), {}, {}
    for path in sorted((root / "data/ingredients").rglob("*.yaml")):
        name = path.relative_to(root).as_posix()
        require(path.is_file() and not path.is_symlink(), f"Nonregular input: {path}")
        data = path.read_bytes()
        hashes[name] = {"sha256": hashlib.sha256(data).hexdigest(), "bytes": len(data)}
        try:
            record = yaml.load(data, Loader=UniqueOwnerLoader)
        except (ValueError, yaml.YAMLError) as exc:
            raise ValueError(f"Invalid MIM owner YAML {name}: {exc}") from exc
        require(isinstance(record, dict), "Invalid MIM record")
        records[name] = record
        labels = {str(record.get("preferred_term") or "")}
        labels.update(
            str(item["synonym_text"])
            for item in record.get("synonyms") or []
            if isinstance(item, dict) and is_resolving_synonym(item)
        )
        for label in labels - {""}:
            index[label.casefold()].add(name)
    return index, records, hashes


def candidate(case, index, records, hashes, native):
    context = case["context"]
    matches = sorted(index.get(context["preferred_term"].casefold(), ()))
    owners = [name for name in matches if records[name].get("mapping_status") != "REJECTED"]
    result: dict[str, Any] = {
        "owners": owners,
        "rejected_owners": sorted(set(matches) - set(owners)),
        "supported_canonical_rows": [],
    }
    if not owners:
        result["classification"] = "NO_ACTIVE_OWNER"
    elif len(owners) != 1:
        result["classification"] = "AMBIGUOUS_OWNER"
    else:
        owner = owners[0]
        record = records[owner]
        result.update(
            owner_record=owner,
            owner_record_sha256=hashes[owner]["sha256"],
            mim_identifier=str(record.get("identifier") or ""),
        )
        if record.get("mapping_status") != "MAPPED":
            result["classification"] = "KNOWN_UNMAPPED_OWNER"
        elif not context["resolved_identifier"]:
            result["classification"] = "SOURCE_IDENTIFIER_MISSING"
        elif context["resolved_identifier"] != result["mim_identifier"]:
            result["classification"] = "SOURCE_IDENTIFIER_CONFLICT"
        else:
            result["classification"] = "AGREEING_LABEL_AND_IDENTIFIER"
        result["supported_canonical_rows"] = [
            {
                "source_position": decision["source_position"],
                "row_sha256": reviewed_sssom.row_sha256(row),
                "subject_id": row["subject_id"],
                "object_id": row["object_id"],
            }
            for row, decision in zip(native["rows"], native["decisions"], strict=True)
            if decision["owner_record"] == owner
            and decision["disposition"] == "SUPPORTED"
            and row["predicate_id"] == "skos:exactMatch"
            and row["object_id"] == result["mim_identifier"]
        ]
    return result


def collect_cases(bundle, destination, manifest):
    policy = CONTRACTS[manifest["contract"]]
    cases: dict[str, dict[str, Any]] = {}
    positive: dict[tuple[str, str], dict[str, str]] = {}
    events: dict[tuple[str, str, str], str] = {}
    ledger_coordinates = set()
    base_count = context_count = 0
    fields = None
    rows_path = destination / "source-mentions.tsv"
    with rows_path.open("x", encoding="utf-8", newline="") as stream:
        writer = None
        for product in ("ingredient_occurrences.tsv", "variant_ingredient_changes.tsv"):
            with csv_reader(bundle / product) as reader:
                if fields is None:
                    fields = list(reader.fieldnames)
                    require(set(VARIANT_FIELDS) <= set(fields), "Missing v2 occurrence context")
                    writer = csv.DictWriter(
                        stream,
                        fields + ["counts_as_presence", "source_product", "source_row", "case_id"],
                        delimiter="\t",
                        lineterminator="\n",
                    )
                    writer.writeheader()
                else:
                    require(
                        reader.fieldnames == fields + ["counts_as_presence"],
                        "Ledger columns differ",
                    )
                assert writer is not None  # Both product paths initialize or reuse the writer.
                for position, raw in enumerate(reader, 1):
                    row = checked_row(raw)
                    action, role = row["change_action"], row["descriptor_role"]
                    scoped = bool(action)
                    expected_presence = True
                    if scoped:
                        require(
                            action in policy["actions"]
                            and role in {"ingredient", "replaced_ingredient"},
                            "Unknown action or descriptor role",
                        )
                        require(
                            role != "replaced_ingredient" or action == "REPLACE",
                            "Old target outside REPLACE",
                        )
                        expected_presence = (
                            action in policy["positive_actions"] and role == "ingredient"
                        )
                        require(
                            all(row[key] for key in VARIANT_FIELDS), "Incomplete variant context"
                        )
                        require(
                            row["descriptor_path"]
                            == f"/variants/{row['variant_index']}/ingredient_changes/{row['change_index']}/{role}",
                            "Descriptor coordinate mismatch",
                        )
                        event = (row["recipe_id"], row["variant_index"], row["change_index"])
                        require(
                            event not in events or events[event] == action, "Event action conflict"
                        )
                        events[event] = action
                    else:
                        require(
                            not any(row[key] for key in VARIANT_FIELDS),
                            "Unscoped row contains variant context",
                        )
                    coordinate = (row["recipe_id"], row["descriptor_path"])
                    if product == "ingredient_occurrences.tsv":
                        require(expected_presence, "Context-only descriptor in positive inventory")
                        if scoped:
                            require(coordinate not in positive, "Duplicate variant occurrence")
                            positive[coordinate] = dict(row)
                        else:
                            base_count += 1
                    else:
                        require(coordinate not in ledger_coordinates, "Duplicate ledger descriptor")
                        ledger_coordinates.add(coordinate)
                        require(
                            scoped and row["counts_as_presence"] == str(expected_presence).lower(),
                            "Incorrect ledger inventory-membership flag",
                        )
                        comparable = {key: row[key] for key in fields}
                        if expected_presence:
                            require(
                                positive.pop(coordinate, None) == comparable,
                                "Ledger/positive occurrence mismatch",
                            )
                            continue
                        context_count += 1
                    context = {key: row[key] for key in CASE_FIELDS}
                    case_id = payload_sha256(context)
                    case = cases.setdefault(
                        case_id,
                        {
                            "case_id": case_id,
                            "context": context,
                            "source_mentions": [],
                            "descriptors": {},
                            "change_payloads": {},
                            "positive_occurrences": 0,
                            "context_only_mentions": 0,
                            "held_source_mentions": 0,
                        },
                    )
                    payload = {key: row[key] for key in fields}
                    descriptor = json.loads(row["ingredient_json"])
                    require(isinstance(descriptor, dict), "Descriptor payload is not an object")
                    case["descriptors"][payload_sha256(descriptor)] = descriptor
                    if scoped:
                        change = json.loads(row["change_json"])
                        require(isinstance(change, dict), "Change payload is not an object")
                        amount = change.get("amount")
                        if action == "SET_AMOUNT":
                            require(isinstance(amount, dict), "SET_AMOUNT lacks literal amount")
                        if amount is not None:
                            require(
                                manifest["contract"] == "culturemech-direct-ingredients-v3"
                                and action in {"ADD", "REPLACE", "SET_AMOUNT"},
                                "Literal amount outside v3 amount contract",
                            )
                            require(
                                isinstance(amount, dict)
                                and amount.get("unit")
                                in {"G", "MG", "MICROG", "ML", "L", "PERCENT"},
                                "Unknown literal amount unit",
                            )
                            expected_basis = (
                                "UNSPECIFIED_PERCENT"
                                if amount["unit"] == "PERCENT"
                                else "PER_BATCH"
                            )
                            require(
                                amount.get("basis") == expected_basis
                                and str(amount.get("value", "")).strip()
                                and str(amount.get("basis_statement", "")).strip(),
                                "Missing/inconsistent literal amount basis",
                            )
                            if role == "ingredient":
                                require(
                                    "concentration" not in descriptor
                                    and not row["concentration_value"]
                                    and not row["concentration_unit"],
                                    "Literal amount was converted to a concentration",
                                )
                        case["change_payloads"][payload_sha256(change)] = change
                    case["source_mentions"].append(
                        {
                            "product": product,
                            "row": position,
                            "row_sha256": payload_sha256(payload),
                            "recipe_id": row["recipe_id"],
                            "source_path": row["source_path"],
                            "component_field": row["component_field"],
                            "component_index": row["component_index"],
                            "descriptor_path": row["descriptor_path"],
                        }
                    )
                    case[
                        "positive_occurrences" if expected_presence else "context_only_mentions"
                    ] += 1
                    writer.writerow(
                        {
                            **payload,
                            "counts_as_presence": str(expected_presence).lower(),
                            "source_product": product,
                            "source_row": position,
                            "case_id": case_id,
                        }
                    )
    require(not positive, "Positive variants missing from change ledger")
    counts = manifest["counts"]
    require(
        base_count == counts["base_direct_occurrences"]
        and context_count == counts["variant_context_only_mentions"]
        and len(events) == counts["variant_change_events"],
        "Source accounting mismatch",
    )
    require(
        dict(Counter(events.values())) == counts["variant_changes_by_action"],
        "Action accounting mismatch",
    )
    require(
        sum(item["positive_occurrences"] for item in cases.values()) == counts["occurrences"],
        "Positive intake membership changed",
    )
    return [cases[key] for key in sorted(cases)]


def collect_held_cases(bundle, destination, manifest):
    """Keep source holds separate; resolve identities without asserting presence."""
    if not CONTRACTS[manifest["contract"]]["held_product"]:
        return []
    cases: dict[str, dict[str, Any]] = {}
    coordinates, labels = set(), set()
    with (
        csv_reader(bundle / HELD_PRODUCT) as reader,
        (destination / "source-held-mentions.tsv").open(
            "x", encoding="utf-8", newline=""
        ) as stream,
    ):
        require(reader.fieldnames == list(HELD_FIELDS), "Unknown held mention columns")
        writer = csv.DictWriter(
            stream,
            [*HELD_FIELDS, "source_product", "source_row", "case_id"],
            delimiter="\t",
            lineterminator="\n",
        )
        writer.writeheader()
        for position, row in enumerate(reader, 1):
            checked_row(row)
            require(
                row["review_status"] == "WITHHELD" and row["counts_as_presence"] == "false",
                "Held source mention asserted approval/presence",
            )
            mention = json.loads(row["mention_json"])
            allowed = {
                "source_label",
                "reported_action",
                "stage",
                "source_modification_index",
                "source_text",
                "reason",
                "held_fields",
                "reported_quantity",
                "evidence",
            }
            require(
                isinstance(mention, dict) and not set(mention) - allowed,
                "Held mention has grounding or unknown assertions",
            )
            held = json.loads(row["held_fields_json"])
            require(
                isinstance(held, list)
                and held
                and all(isinstance(field, str) for field in held)
                and len(set(held)) == len(held)
                and set(held) <= HELD_DIMENSIONS,
                "Invalid held assertion dimensions",
            )
            require(
                mention.get("held_fields") == held
                and mention.get("evidence", []) == json.loads(row["evidence_json"]),
                "Held JSON projection differs",
            )
            for field in allowed - {"held_fields", "evidence"}:
                require(
                    str(mention.get(field, "")) == row[field],
                    "Held column differs from source payload",
                )
            require(
                all(
                    row[field].strip()
                    for field in ("source_label", "source_text", "stage", "reason")
                )
                and row["source_label"] in row["source_text"],
                "Held label lacks exact source binding",
            )
            require(
                row["reported_action"]
                in CONTRACTS[manifest["contract"]]["actions"] | {"UNSPECIFIED"},
                "Unknown held reported action",
            )
            for field in ("variant_index", "mention_index", "source_modification_index"):
                require(
                    row[field].isdigit() and str(int(row[field])) == row[field],
                    "Invalid held coordinate",
                )
            require(
                row["descriptor_path"]
                == f"/variants/{row['variant_index']}/ingredient_mentions/{row['mention_index']}",
                "Held descriptor coordinate mismatch",
            )
            coordinate = (row["recipe_id"], row["descriptor_path"])
            require(coordinate not in coordinates, "Duplicate held mention coordinate")
            coordinates.add(coordinate)
            labels.add(row["source_label"])
            context = {
                "preferred_term": row["source_label"],
                "resolved_identifier": "",
                "change_action": row["reported_action"],
                "change_stage": row["stage"],
                "descriptor_role": "held_mention",
                "variant_name": row["variant_name"],
                "held_fields": sorted(held),
            }
            key = payload_sha256(context)
            case = cases.setdefault(
                key,
                {
                    "case_id": key,
                    "context": context,
                    "source_mentions": [],
                    "descriptors": {},
                    "change_payloads": {},
                    "held_payloads": {},
                    "positive_occurrences": 0,
                    "context_only_mentions": 0,
                    "held_source_mentions": 0,
                },
            )
            case["held_payloads"][payload_sha256(mention)] = mention
            case["held_source_mentions"] += 1
            case["source_mentions"].append(
                {
                    "product": HELD_PRODUCT,
                    "row": position,
                    "row_sha256": payload_sha256(row),
                    "recipe_id": row["recipe_id"],
                    "source_path": row["source_path"],
                    "descriptor_path": row["descriptor_path"],
                }
            )
            writer.writerow(
                {**row, "source_product": HELD_PRODUCT, "source_row": position, "case_id": key}
            )
    require(
        len(coordinates) == manifest["counts"]["variant_held_mentions"]
        and len(labels) == manifest["counts"]["variant_held_labels"],
        "Held mention accounting mismatch",
    )
    return [cases[key] for key in sorted(cases)]


def check_snapshot(root, snapshots):
    for name, expected in snapshots.items():
        require(fingerprint(relative(root, name)) == expected, "Input changed: " + name)


def prepare(handoff, handoff_pin, output, python, *, root=ROOT, producer_root=None, review=REVIEW):
    output_preflight(output, [handoff, root / "data", root / "mappings", root / "reports"])
    receipt, manifest, coverage, inputs = verify_handoff(handoff, handoff_pin)
    source_verification = verify_producer(handoff, manifest, python, producer_root)
    native = reviewed_sssom.load_review(root, Path(review))
    index, records, record_hashes = mim_snapshot(root)
    output.parent.mkdir(parents=True, exist_ok=True)
    with staging(output) as stage:
        for name, expected in inputs.items():
            target = stage / "source" / name
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(relative(handoff, name), target)
            require(fingerprint(target) == expected, "Copied source differs: " + name)
        canonical = reviewed_sssom.export_reviewed(
            root, Path(review), stage / "canonical-reviewed-sssom"
        )
        cases = collect_cases(stage / "source/bundle", stage, manifest)
        cases.extend(collect_held_cases(stage / "source/bundle", stage, manifest))
        cases.sort(key=lambda item: item["case_id"])
        for case in cases:
            case["candidate"] = candidate(case, index, records, record_hashes, native)
        packet = {
            "schema_version": 1,
            "source_manifest_sha256": receipt["manifest_sha256"],
            "canonical_review_sha256": native["review_sha256"],
            "cases": cases,
        }
        write_json(stage / "review-packet.json", packet)
        fields = (
            "case_id",
            "source_label",
            "upstream_identifier",
            "action",
            "stage",
            "role",
            "positive_occurrences",
            "context_only_mentions",
            "held_source_mentions",
            "held_fields_json",
            "classification",
            "candidate_owners_json",
            "supported_canonical_rows_json",
        )
        write_tsv(
            stage / "review-cases.tsv",
            fields,
            [
                {
                    "case_id": case["case_id"],
                    "source_label": case["context"]["preferred_term"],
                    "upstream_identifier": case["context"]["resolved_identifier"],
                    "action": case["context"]["change_action"],
                    "stage": case["context"]["change_stage"],
                    "role": case["context"]["descriptor_role"],
                    "positive_occurrences": case["positive_occurrences"],
                    "context_only_mentions": case["context_only_mentions"],
                    "held_source_mentions": case["held_source_mentions"],
                    "held_fields_json": json.dumps(case["context"].get("held_fields", [])),
                    "classification": case["candidate"]["classification"],
                    "candidate_owners_json": json.dumps(case["candidate"]["owners"]),
                    "supported_canonical_rows_json": json.dumps(
                        case["candidate"]["supported_canonical_rows"]
                    ),
                }
                for case in cases
            ],
        )
        check_snapshot(handoff, inputs)
        require(
            mim_snapshot(root)[2] == record_hashes,
            "MIM owner membership/bytes changed during preparation",
        )
        reviewed_sssom._check_snapshot(native)
        products = {
            path.relative_to(stage).as_posix(): fingerprint(path)
            for path in sorted(stage.rglob("*"))
            if path.is_file()
        }
        value = {
            "schema_version": 1,
            "status": "PREPARED_PENDING_SOURCE_BINDING_REVIEW",
            "source_contract": manifest["contract"],
            "source_producer_commit": receipt["producer_commit"],
            "source_manifest_sha256": receipt["manifest_sha256"],
            "handoff_sha256": handoff_pin,
            "source_verification": source_verification,
            "canonical_sssom": canonical,
            "canonical_review_path": review,
            "canonical_review_sha256": native["review_sha256"],
            "consumer_implementation": fingerprint(Path(__file__)),
            "mim_record_inputs": record_hashes,
            "files": products,
            "counts": {
                "cases": len(cases),
                "source_occurrences": manifest["counts"]["occurrences"],
                "context_only_mentions": manifest["counts"]["variant_context_only_mentions"],
                "held_source_mentions": manifest["counts"].get("variant_held_mentions", 0),
                "classifications": dict(
                    Counter(case["candidate"]["classification"] for case in cases)
                ),
            },
            "coverage_dispositions": coverage["dispositions"],
            "limitations": "Candidate matches are not approved source bindings. Original holds and native publication gates remain. No active campaign or canonical MIM data were changed.",
        }
        write_json(stage / "intake.json", value)
    return value


def verify_intake(intake, pin, root):
    manifest, _ = read_json(intake / "intake.json", pin)
    require(
        manifest["schema_version"] == 1
        and manifest["status"] == "PREPARED_PENDING_SOURCE_BINDING_REVIEW",
        "Not a prepared source intake",
    )
    actual = {path.relative_to(intake).as_posix() for path in intake.rglob("*") if path.is_file()}
    require(
        actual == set(manifest["files"]) | {"intake.json"}, "Unexpected/missing intake artifacts"
    )
    check_snapshot(intake, manifest["files"])
    _index, _records, current = mim_snapshot(root)
    require(
        current == manifest["mim_record_inputs"], "MIM record membership/bytes changed since intake"
    )
    native = reviewed_sssom.load_review(root, Path(manifest["canonical_review_path"]))
    require(
        native["review_sha256"] == manifest["canonical_review_sha256"], "Canonical review changed"
    )
    require(
        reviewed_sssom.validate_reviewed(
            root, Path(manifest["canonical_review_path"]), intake / "canonical-reviewed-sssom"
        )
        == manifest["canonical_sssom"],
        "Canonical reviewed partition changed",
    )
    packet, _ = read_json(intake / "review-packet.json")
    require(
        packet["source_manifest_sha256"] == manifest["source_manifest_sha256"]
        and packet["canonical_review_sha256"] == native["review_sha256"],
        "Review packet provenance mismatch",
    )
    cases = {item["case_id"]: item for item in packet["cases"]}
    require(
        len(cases) == len(packet["cases"]) == manifest["counts"]["cases"],
        "Case membership mismatch",
    )
    for key, case in cases.items():
        require(key == payload_sha256(case["context"]), "Case identifier differs from context")
    return manifest, cases, native


def finalize(intake, pin, review_path, output, *, root=ROOT):
    """Require explicit complete native review; no lexical match grants approval."""
    review_path = relative(root, review_path)
    output_preflight(
        output, [intake, root / "data", root / "mappings", root / "reports", review_path]
    )
    manifest, cases, native = verify_intake(intake, pin, root)
    review, review_hash = read_json(review_path)
    require(
        review["schema_version"] == 1 and review["intake_sha256"] == pin,
        "Review is not bound to this exact intake",
    )
    evidence, evidence_hashes = {}, {}
    for name, expected in review["inputs"].items():
        path = relative(root, name)
        value = fingerprint(path)
        require(value["sha256"] == expected, "Stale source-binding review evidence")
        evidence[name] = path.read_bytes()
        require(
            hashlib.sha256(evidence[name]).hexdigest() == expected, "Evidence changed while reading"
        )
        evidence_hashes[name] = value
    decisions = {}
    for decision in review["decisions"]:
        key = decision["case_id"]
        require(key in cases and key not in decisions, "Unexpected/duplicate review case")
        decisions[key] = decision
    require(set(decisions) == set(cases), "Review must explicitly dispose every intake case")
    rows = []
    proofs: dict[str, Any] = {}
    for key, case in cases.items():
        decision = decisions[key]
        candidate = case["candidate"]
        owner = candidate.get("owner_record", "source/bundle/manifest.json")
        owner_sha = candidate.get("owner_record_sha256", manifest["source_manifest_sha256"])
        validate_review_decision(
            decision, case, owner, owner_sha, evidence, proofs, require_owner_path=True
        )
        canonical = decision.get("canonical_row_sha256", "")
        if decision["disposition"] == "SUPPORTED":
            require(
                not set(case["context"].get("held_fields", [])) & {"SOURCE_CLAIM", "IDENTITY_FORM"},
                "Source identity uncertainty cannot be approved by mapping review",
            )
            require(
                len(candidate["owners"]) == 1, "Supported binding needs a unique current MIM owner"
            )
            require(
                canonical
                and canonical
                in {item["row_sha256"] for item in candidate["supported_canonical_rows"]},
                "Supported source binding lacks a supported native exact-identity row",
            )
        else:
            require(not canonical, "Withheld binding must not assert a supported mapping")
        rows.append(
            {
                "case_id": key,
                "payload_sha256": payload_sha256(case),
                "source_label": case["context"]["preferred_term"],
                "change_action": case["context"]["change_action"],
                "change_stage": case["context"]["change_stage"],
                "descriptor_role": case["context"]["descriptor_role"],
                "positive_occurrences": case["positive_occurrences"],
                "context_only_mentions": case["context_only_mentions"],
                "held_source_mentions": case.get("held_source_mentions", 0),
                "held_fields_json": json.dumps(case["context"].get("held_fields", [])),
                "owner_record": owner,
                "owner_record_sha256": owner_sha,
                "mim_identifier": candidate.get("mim_identifier", "") if canonical else "",
                "canonical_row_sha256": canonical,
                "disposition": decision["disposition"],
                "review_reason": decision["review_reason"],
                "review_evidence": decision["review_evidence"],
                "evidence_key": decision["evidence_key"],
            }
        )
    output.parent.mkdir(parents=True, exist_ok=True)
    with staging(output) as stage:
        for name, selected in (
            ("binding-dispositions.tsv", rows),
            ("supported-bindings.tsv", [r for r in rows if r["disposition"] == "SUPPORTED"]),
            ("withheld-bindings.tsv", [r for r in rows if r["disposition"] == "WITHHOLD"]),
        ):
            write_tsv(stage / name, list(rows[0]), selected)
        for name, expected in {
            **evidence_hashes,
            review_path.relative_to(root).as_posix(): review_hash,
        }.items():
            destination = stage / "review-inputs" / name
            destination.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(relative(root, name), destination)
            require(fingerprint(destination) == expected, "Copied review differs")
        shutil.copytree(intake / "canonical-reviewed-sssom", stage / "canonical-reviewed-sssom")
        verified = reviewed_sssom.validate_reviewed(
            root, Path(manifest["canonical_review_path"]), stage / "canonical-reviewed-sssom"
        )
        verify_intake(intake, pin, root)
        check_snapshot(root, evidence_hashes)
        require(
            fingerprint(review_path) == review_hash,
            "Source-binding review changed during finalization",
        )
        reviewed_sssom._check_snapshot(native)
        value = {
            "schema_version": 1,
            "status": "REVIEWED_SOURCE_INTAKE",
            "intake_sha256": pin,
            "source_manifest_sha256": manifest["source_manifest_sha256"],
            "source_contract": manifest["source_contract"],
            "review_sha256": review_hash["sha256"],
            "canonical_sssom": verified,
            "counts": dict(Counter(row["disposition"] for row in rows)),
            "coverage_dispositions": manifest["coverage_dispositions"],
            "files": {
                path.relative_to(stage).as_posix(): fingerprint(path)
                for path in sorted(stage.rglob("*"))
                if path.is_file()
            },
            "limitations": "Reviewed source bindings and an unchanged native supported/withheld SSSOM snapshot. Context-only mentions remain excluded from inventory membership. No active campaign adoption, new chemical identity curation, canonical publication or KGM installation was performed.",
        }
        write_json(stage / "reviewed-intake.json", value)
    return value


def verify_reviewed(intake, pin, review, output, output_pin, *, root=ROOT):
    """Replay exact native source review and compare every final product byte."""
    observed, _ = read_json(output / "reviewed-intake.json", output_pin)
    with tempfile.TemporaryDirectory(prefix=".source-intake-qc-", dir=output.parent) as temporary:
        rebuilt = Path(temporary) / "reviewed"
        expected = finalize(intake, pin, review, rebuilt, root=root)
        require(observed == expected, "Reviewed receipt differs from native replay")
        names = {
            path.relative_to(output).as_posix() for path in output.rglob("*") if path.is_file()
        }
        require(
            names == set(expected["files"]) | {"reviewed-intake.json"},
            "Reviewed product membership changed",
        )
        check_snapshot(output, expected["files"])
    require(
        fingerprint(output / "reviewed-intake.json")["sha256"] == output_pin,
        "Reviewed receipt changed during verification",
    )
    return {
        "status": "VERIFIED_REVIEWED_SOURCE_INTAKE",
        "intake_sha256": pin,
        "reviewed_intake_sha256": output_pin,
        "counts": expected["counts"],
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)
    prep = sub.add_parser("prepare")
    prep.add_argument("--handoff", type=Path, required=True)
    prep.add_argument("--expected-handoff-sha256", required=True)
    prep.add_argument("--producer-root", type=Path)
    prep.add_argument("--producer-python", type=Path, default=Path(sys.executable))
    prep.add_argument("--output", type=Path, required=True)
    prep.add_argument("--review", default=REVIEW)
    final = sub.add_parser("finalize")
    final.add_argument("--intake", type=Path, required=True)
    final.add_argument("--expected-intake-sha256", required=True)
    final.add_argument("--review", required=True)
    final.add_argument("--output", type=Path, required=True)
    verify = sub.add_parser("verify")
    verify.add_argument("--intake", type=Path, required=True)
    verify.add_argument("--expected-intake-sha256", required=True)
    verify.add_argument("--review", required=True)
    verify.add_argument("--output", type=Path, required=True)
    verify.add_argument("--expected-reviewed-sha256", required=True)
    args = parser.parse_args()
    if args.command == "prepare":
        result = prepare(
            args.handoff,
            args.expected_handoff_sha256,
            args.output,
            args.producer_python,
            producer_root=args.producer_root,
            review=args.review,
        )
        receipt = "intake.json"
    elif args.command == "finalize":
        result = finalize(args.intake, args.expected_intake_sha256, args.review, args.output)
        receipt = "reviewed-intake.json"
    else:
        result = verify_reviewed(
            args.intake,
            args.expected_intake_sha256,
            args.review,
            args.output,
            args.expected_reviewed_sha256,
        )
        print(json.dumps(result, indent=2))
        return
    print(
        json.dumps(
            {
                "status": result["status"],
                "counts": result["counts"],
                "receipt_sha256": fingerprint(args.output / receipt)["sha256"],
            },
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
