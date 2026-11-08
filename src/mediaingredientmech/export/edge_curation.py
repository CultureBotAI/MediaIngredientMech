"""Export pinned native mapping decisions for EdgeMech without granting new review.

The immutable archive and export manifest are independent caller-supplied pins.
All declared native inputs are verified before any assertion is returned. Rows,
review decisions and evidence remain native payloads; supported mapping scope
does not authorize biological claims or current KG occurrence decisions.
"""

from __future__ import annotations

import csv
import hashlib
import io
import re
import tarfile
import tempfile
from pathlib import Path, PurePosixPath

from mediaingredientmech.export import reviewed_sssom as reviewed

REPOSITORY = "CultureBotAI/MediaIngredientMech"
SEMANTICS = "MAPPING_SEMANTICS.md"
SCHEMA = "src/mediaingredientmech/schema/mediaingredientmech.yaml"
MAX_INPUT_BYTES = 128 * 1024 * 1024


def _sha(content: bytes) -> str:
    return hashlib.sha256(content).hexdigest()


def _relative(value: str) -> str:
    path = PurePosixPath(value)
    if not value or path.is_absolute() or ".." in path.parts or str(path) != value or "\\" in value:
        raise ValueError(f"Unsafe native archive path: {value!r}")
    return value


def _pinned_bytes(path: Path, expected: str) -> bytes:
    if not re.fullmatch(r"[0-9a-f]{64}", expected):
        raise ValueError("An explicit SHA256 pin is required")
    if not path.is_file() or path.is_symlink() or path.stat().st_size > MAX_INPUT_BYTES:
        raise ValueError(f"Input must be a bounded regular file: {path}")
    content = path.read_bytes()
    if _sha(content) != expected:
        raise ValueError(f"Pinned input hash mismatch: {path}")
    return content


def _archive_snapshot(content: bytes, commit: str, review_path: str, root: Path) -> None:
    prefix = f"MediaIngredientMech-{commit}/"
    with tarfile.open(fileobj=io.BytesIO(content), mode="r:gz") as archive:
        members = {}
        for member in archive:
            if not member.name.startswith(prefix):
                if member.name.rstrip("/") == prefix.rstrip("/") and member.isdir():
                    continue
                raise ValueError("Archive member is outside the pinned repository root")
            name = member.name[len(prefix) :].rstrip("/")
            if not name:
                continue
            _relative(name)
            if name in members:
                raise ValueError(f"Duplicate archive member: {name}")
            members[name] = member

        def read(name: str) -> bytes:
            _relative(name)
            member = members.get(name)
            if member is None or not member.isfile() or member.size > MAX_INPUT_BYTES:
                raise ValueError(f"Missing or unsafe archived input: {name}")
            stream = archive.extractfile(member)
            if stream is None:
                raise ValueError(f"Unreadable archived input: {name}")
            return stream.read()

        review_content = read(review_path)
        review = reviewed._json_bytes(review_content, review_path)
        names = {review_path, review["source_sssom"], SEMANTICS, SCHEMA}
        for group in ("inputs", "record_inputs"):
            if not isinstance(review.get(group), dict):
                raise ValueError(f"Missing native {group}")
            names.update(review[group])
        # Native owner resolution must see every ingredient, including records
        # absent from the review inventory, so ambiguous ownership fails closed.
        names.update(
            name
            for name in members
            if name.startswith("data/ingredients/") and name.endswith(".yaml")
        )
        total = 0
        for name in sorted(names):
            data = read(name)
            total += len(data)
            if total > MAX_INPUT_BYTES:
                raise ValueError("Native input closure exceeds the extraction limit")
            destination = root / name
            destination.parent.mkdir(parents=True, exist_ok=True)
            destination.write_bytes(data)


def _validate_bundle(root: Path, loaded: dict, bundle: Path, manifest_bytes: bytes) -> dict:
    manifest = reviewed._json_bytes(manifest_bytes, "manifest.json")
    if (
        manifest.get("schema_version") != 1
        or manifest.get("semantic_status") != "PASS_SUPPORTED_SUBSET"
    ):
        raise ValueError("Unsupported native bundle manifest")
    if set(manifest.get("files", {})) != set(reviewed.PRODUCTS):
        raise ValueError("Native bundle product inventory differs")
    if {path.name for path in bundle.iterdir()} != {*reviewed.PRODUCTS, "manifest.json"}:
        raise ValueError("Native bundle contains unexpected or missing files")
    review = loaded["review"]
    if any(
        manifest.get(key) != expected
        for key, expected in {
            "source_sssom": review["source_sssom"],
            "source_sha256": review["source_sha256"],
            "review_sha256": loaded["review_sha256"],
        }.items()
    ):
        raise ValueError("Bundle is not bound to the archived source and review")
    products = {
        name: _pinned_bytes(bundle / name, manifest["files"][name]) for name in reviewed.PRODUCTS
    }
    counts = {"source": len(loaded["rows"])}
    for disposition, filename in (
        ("SUPPORTED", reviewed.PRODUCTS[0]),
        ("WITHHOLD", reviewed.PRODUCTS[1]),
    ):
        _, fields, actual = reviewed.read_sssom(bundle / filename, content=products[filename])
        expected = [
            row
            for row, decision in zip(loaded["rows"], loaded["decisions"], strict=True)
            if decision["disposition"] == disposition
        ]
        if fields != loaded["fields"] or actual != expected:
            raise ValueError("Bundle partition changed native payloads or membership")
        counts[disposition.lower()] = len(expected)
    if manifest.get("counts") != counts:
        raise ValueError("Bundle counts differ from the complete native partition")
    reader = csv.DictReader(
        io.StringIO(products[reviewed.PRODUCTS[2]].decode()), delimiter="\t", strict=True
    )
    if reader.fieldnames != list(reviewed.DISPOSITION_FIELDS):
        raise ValueError("Native disposition fields differ")
    expected_decisions = []
    for row, decision in zip(loaded["rows"], loaded["decisions"], strict=True):
        item = dict(decision)
        item.update({field: row[field] for field in ("subject_id", "predicate_id", "object_id")})
        item["owner_record_sha256"] = review["record_inputs"][decision["owner_record"]]
        expected_decisions.append(
            {field: str(item[field]) for field in reviewed.DISPOSITION_FIELDS}
        )
    if list(reader) != expected_decisions:
        raise ValueError("Bundle dispositions differ from exact native decisions")
    reviewed._check_snapshot(loaded)
    return manifest


def build_native_assertions(
    *,
    archive: Path,
    bundle: Path,
    source_commit: str,
    archive_sha256: str,
    manifest_sha256: str,
    review_path: str = "reports/sssom_completion_20260921/review.json",
    positions: tuple[int, ...] | None = None,
) -> list[dict]:
    """Adapt verified immutable MIM decisions, with one-based source positions.

    ``positions=None`` selects the entire verified source partition. Callers
    must first exercise a bounded selection through their actual publisher.
    The shared CLAW native-assertion contract must be installed by the caller.
    No files are published by this function and no current KG edge is approved.
    """
    from kg_microbe_curation.identity import sha256_json
    from kg_microbe_curation.native import (
        NATIVE_CONTRACT,
        native_assertion_id,
        validate_native_assertion,
    )

    if not re.fullmatch(r"[0-9a-f]{40}", source_commit):
        raise ValueError("An exact native Git commit is required")
    _relative(review_path)
    archive_content = _pinned_bytes(archive, archive_sha256)
    manifest_bytes = _pinned_bytes(bundle / "manifest.json", manifest_sha256)
    with tempfile.TemporaryDirectory(prefix="mim-native-assertions-") as temporary:
        root = Path(temporary)
        _archive_snapshot(archive_content, source_commit, review_path, root)
        loaded = reviewed.load_review(root, root / review_path)
        manifest = _validate_bundle(root, loaded, bundle, manifest_bytes)
        selected = tuple(range(1, len(loaded["rows"]) + 1)) if positions is None else positions
        if (
            not selected
            or len(set(selected)) != len(selected)
            or any(type(i) is not int or not 1 <= i <= len(loaded["rows"]) for i in selected)
        ):
            raise ValueError(
                "Source positions must be unique, nonempty and within the native partition"
            )
        review = loaded["review"]

        def locator(path: str, selector: dict | None = None) -> dict:
            return {
                "repository": REPOSITORY,
                "commit": source_commit,
                "path": path,
                "selector": selector or {},
            }

        results = []
        for position in selected:
            row, decision = loaded["rows"][position - 1], loaded["decisions"][position - 1]
            evidence_path, owner = decision["review_evidence"], decision["owner_record"]
            proof = reviewed._json(root / evidence_path)["entries"][decision["evidence_key"]]
            paths = sorted(
                {review["source_sssom"], review_path, evidence_path, owner, SEMANTICS, SCHEMA}
            )
            evidence = []
            for path in paths:
                item = {
                    "evidence_id": "native-file:" + path,
                    "locator": locator(path),
                    "sha256": reviewed.digest(root / path),
                    "ancestry": [],
                }
                if path == evidence_path:
                    item["locator"]["selector"] = {"entries_key": decision["evidence_key"]}
                    item["payload"] = proof
                    item["ancestry"] = ["native-file:" + review_path, "native-file:" + owner]
                evidence.append(item)
            supported = decision["disposition"] == "SUPPORTED"
            assertion = {
                "contract": NATIVE_CONTRACT,
                "native_locator": {
                    **locator(review["source_sssom"], {"source_position": position}),
                    "source_sha256": review["source_sha256"],
                    "payload_sha256": sha256_json(row),
                },
                "payload": {
                    "subject": row["subject_id"],
                    "predicate": row["predicate_id"],
                    "object": row["object_id"] or None,
                    "native_payload": row,
                    "context": {
                        "scope": "native_mapping_payload_only",
                        "owner_record": owner,
                        "source_archive_sha256": archive_sha256,
                        "export_manifest_sha256": manifest_sha256,
                        "native_partition_counts": manifest["counts"],
                        "withheld_is_global_ban": False,
                        "matching_policy": "exact_native_payload_and_dependency_bindings",
                        "match_selector": {
                            "subject": row["subject_id"],
                            "predicate": row["predicate_id"],
                            "object": row["object_id"] or None,
                            "native_payload_sha256": sha256_json(row),
                            "source_sha256": review["source_sha256"],
                            "review_sha256": loaded["review_sha256"],
                            "owner_record_sha256": review["record_inputs"][owner],
                            "evidence_sha256": review["inputs"][evidence_path],
                        },
                    },
                    "interpretation": {
                        "normalization_contract": "mim-native-sssom-exact-lexical/v1",
                        "normalizer_contract_sha256": reviewed.digest(root / SEMANTICS),
                        "schema_sha256": reviewed.digest(root / SCHEMA),
                        "prefix_map_sha256": sha256_json(loaded["metadata"].get("curie_map", {})),
                    },
                },
                "evidence": evidence,
                "native_review": {
                    "status": "supported" if supported else "withheld",
                    "locator": locator(review_path, {"source_position": position}),
                    "sha256": loaded["review_sha256"],
                    "payload": decision,
                    "payload_sha256": sha256_json(decision),
                    "rationale": decision["review_reason"],
                },
                "assurance": "inherited_native_review" if supported else "native_withheld_decision",
                "limitations": [
                    "Inherited native mapping review only; no independent scientific review was performed.",
                    "Exact mapping payload and dependency scope only; no organism-growth, medium preference or other biological claim is inferred.",
                    "Withheld mappings remain scoped native backlog entries, not global negative assertions.",
                    "All native review input and record hashes were verified; the review file binds their complete inventory.",
                ],
                "independent_scientific_review": False,
            }
            assertion["assertion_id"] = native_assertion_id(assertion)
            validate_native_assertion(assertion)
            results.append(assertion)
        reviewed._check_snapshot(loaded)
    # Detect concurrent replacement, including input changes after extraction.
    _pinned_bytes(archive, archive_sha256)
    _pinned_bytes(bundle / "manifest.json", manifest_sha256)
    for name, digest in manifest["files"].items():
        _pinned_bytes(bundle / name, digest)
    return results
