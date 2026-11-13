"""Export an evidence-bound, reviewed SSSOM partition without KGX (#729).

Every current source row needs one explicit SUPPORTED or WITHHOLD decision.
Validation regenerates the expected partition from source and reviewed evidence;
updating an output checksum cannot legitimize a changed row or disposition.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import io
import json
import math
import re
import shutil
import stat
import tempfile
from collections import defaultdict
from collections.abc import Mapping
from dataclasses import dataclass
from pathlib import Path, PurePosixPath

import yaml

from mediaingredientmech.curie import mim_curie_for_stem
from mediaingredientmech.review_claims import validate_review_decision
from mediaingredientmech.sssom_metadata import subset_date_metadata
from mediaingredientmech.stable_ids import (
    LIFECYCLE_PATH,
    MIM_PREFIX,
    REGISTRY_PATH,
    parse_registry,
    validate_id,
    validate_records,
)
from mediaingredientmech.synonym_policy import is_resolving_synonym_text

PRODUCTS = (
    "ingredient_mappings.sssom.tsv",
    "withheld_mappings.sssom.tsv",
    "mapping-dispositions.tsv",
)
DISPOSITION_FIELDS = (
    "source_position",
    "row_sha256",
    "subject_id",
    "predicate_id",
    "object_id",
    "owner_record",
    "owner_record_sha256",
    "disposition",
    "review_reason",
    "review_evidence",
    "evidence_key",
)


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def row_sha256(row: dict) -> str:
    return hashlib.sha256(
        json.dumps(row, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    ).hexdigest()


payload_sha = row_sha256


def _unique_object(pairs: list) -> dict:
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError(f"Duplicate JSON key: {key}")
        result[key] = value
    return result


def _json(path: Path) -> dict:
    return _json_bytes(path.read_bytes(), str(path))


def _json_bytes(content: bytes, name: str) -> dict:
    data = json.loads(content, object_pairs_hook=_unique_object)
    if not isinstance(data, dict):
        raise ValueError(f"Expected JSON object: {name}")
    return data


def _relative(root: Path, value: str) -> Path:
    path = root / value
    if (
        Path(value).is_absolute()
        or ".." in Path(value).parts
        or not path.resolve().is_relative_to(root.resolve())
    ):
        raise ValueError(f"Evidence/source path must stay within root: {value}")
    return path


def read_sssom(path: Path, *, content: bytes | None = None) -> tuple[dict, list[str], list[dict]]:
    lines = (path.read_bytes() if content is None else content).decode().splitlines(keepends=True)
    end = 0
    while end < len(lines) and lines[end].startswith("#"):
        end += 1
    metadata = yaml.safe_load("".join(line[1:].removeprefix(" ") for line in lines[:end]))
    if (
        not isinstance(metadata, dict)
        or not metadata.get("mapping_set_id")
        or metadata.get("predicate_semantics") != "skos"
    ):
        raise ValueError("SSSOM needs mapping_set_id and predicate_semantics: skos")
    reader = csv.DictReader(io.StringIO("".join(lines[end:])), delimiter="\t", strict=True)
    fields = list(reader.fieldnames or [])
    required = {"subject_id", "subject_label", "predicate_id", "object_id", "object_label", "other"}
    if len(fields) != len(set(fields)) or not required.issubset(fields):
        raise ValueError("Invalid SSSOM columns")
    rows = list(reader)
    if any(None in row or any(value is None for value in row.values()) for row in rows):
        raise ValueError("Malformed SSSOM row width")
    for row in rows:
        confidence = row.get("confidence", "").strip()
        if confidence:
            try:
                finite = math.isfinite(float(confidence))
            except ValueError as exc:
                raise ValueError("SSSOM confidence must be numeric") from exc
            if not finite:
                raise ValueError("SSSOM confidence must be finite")
    return metadata, fields, rows


def _owners(
    root: Path, rows: list[dict], verified_records: dict | None = None
) -> tuple[list[str], dict]:
    labels, subjects = defaultdict(set), defaultdict(set)
    records = {}
    for path in sorted((root / "data/ingredients").rglob("*.yaml")):
        owner = path.relative_to(root).as_posix()
        content = (verified_records or {}).get(owner)
        record = yaml.safe_load(path.read_bytes() if content is None else content)
        if not isinstance(record, dict) or record.get("mapping_status") != "MAPPED":
            continue
        records[owner] = record
        labels[record["preferred_term"]].add(owner)
        subject = (
            validate_id(record["mim_id"]) if "mim_id" in record else mim_curie_for_stem(path.stem)
        )
        subjects[subject].add(owner)
    owners = []
    for row in rows:
        by_label = labels[row["subject_label"]]
        by_subject = subjects[row["subject_id"]]
        candidates = by_label & by_subject
        if not row["subject_id"].startswith("MIM:") or len(candidates) != 1:
            raise ValueError(f"No unique independent owner for {row['subject_id']}")
        owners.append(next(iter(candidates)))
    return owners, records


def _identity_locations(path: Path, *, regular: bool = True) -> tuple:
    """Bind unaliased identity inputs and their ancestors during byte snapshots."""
    locations = []
    for entry in (path, *path.parents):
        info = entry.lstat()
        if stat.S_ISLNK(info.st_mode):
            raise ValueError(f"Permanent identity symlink refused: {entry}")
        locations.append((info.st_dev, info.st_ino))
    info = path.lstat()
    if regular and (not stat.S_ISREG(info.st_mode) or info.st_nlink != 1):
        raise ValueError(f"Permanent identity nonregular/hardlinked input: {path}")
    return tuple(locations)


def _identity_input(path: Path) -> tuple[Path, bytes, tuple]:
    """Capture exact bytes with stable file/ancestor identities on both sides."""
    before = _identity_locations(path)
    content = path.read_bytes()
    if before != _identity_locations(path):
        raise ValueError(f"Permanent identity input moved during capture: {path}")
    return path, content, before


def permanent_subject(subject: str) -> bool:
    """Reserve numeric MIM spellings, including invalid case/width/Unicode."""
    prefix, separator, local = subject.partition(":")
    return bool(separator and prefix.casefold() == "mim" and local.isdecimal())


class _UniqueLoader(yaml.SafeLoader):
    """Reject duplicate keys in the exact captured owner document."""


def _mapping(loader, node, deep=False):
    result = {}
    for key_node, value_node in node.value:
        key = loader.construct_object(key_node, deep=deep)
        if key in result:
            raise ValueError(f"Duplicate owner YAML key: {key}")
        result[key] = loader.construct_object(value_node, deep=deep)
    return result


_UniqueLoader.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, _mapping)


def _members(root: Path) -> tuple[Path, ...]:
    paths = []
    for kind in ("mapped", "unmapped"):
        directory = root / "data/ingredients" / kind
        _identity_locations(directory, regular=False)
        if not directory.is_dir():
            raise ValueError(f"Missing current owner directory: {kind}")
        paths.extend(sorted(directory.glob("*.yaml")))
    return tuple(paths)


@dataclass(frozen=True)
class PermanentIdentity:
    """Retain the complete current corpus and ledger through publication."""

    root: Path
    members: tuple[Path, ...]
    captures: tuple[tuple[Path, bytes, tuple], ...]
    owners: Mapping[str, tuple[str, dict]]

    def require(self, subject: str, label: str) -> str:
        """Require one active owner and the current label, never an alias join."""
        identifier = validate_id(subject)
        if identifier not in self.owners:
            raise ValueError(f"No active permanent owner: {subject}")
        path, record = self.owners[identifier]
        if record.get("mapping_status") != "MAPPED":
            raise ValueError(f"External row owner is not MAPPED: {subject}")
        if record.get("preferred_term") != label:
            raise ValueError(f"Permanent subject label differs from current owner: {subject}")
        return path

    def verify(self) -> None:
        """Reject content, inode, ancestor, or complete membership drift."""
        if _members(self.root) != self.members:
            raise ValueError("Permanent identity owner inventory changed")
        for path, content, locations in self.captures:
            if _identity_input(path) != (path, content, locations):
                raise ValueError(f"Permanent identity input changed: {path}")

    @property
    def hashes(self) -> dict[Path, str]:
        return {path: hashlib.sha256(content).hexdigest() for path, content, _ in self.captures}


def capture_permanent_identity(
    root: Path,
    metadata: dict,
    *,
    reviewed_inputs: Mapping[str, bytes] | None = None,
) -> PermanentIdentity:
    """Validate native active ownership from captured, optionally reviewed bytes.

    An ordinary mapping review must explicitly pin the entire identity closure,
    including unmapped owners; a mutable ledger or a numeric spelling is not
    sufficient. The standalone invariant validator uses the same native checks.
    """
    root = root.absolute()
    if metadata.get("curie_map", {}).get("MIM") != MIM_PREFIX:
        raise ValueError("Permanent MIM subjects require the permanent MIM URI prefix")
    members = _members(root)
    captures = tuple(
        _identity_input(path) for path in (root / REGISTRY_PATH, root / LIFECYCLE_PATH, *members)
    )
    if reviewed_inputs is not None:
        for path, content, _ in captures:
            name = path.relative_to(root).as_posix()
            if reviewed_inputs.get(name) != content:
                raise ValueError(f"Permanent identity input missing or changed in review: {name}")
    registry = parse_registry(captures[0][1], captures[1][1])
    records = {}
    for path, content, _ in captures[2:]:
        record = yaml.load(content, Loader=_UniqueLoader)
        if not isinstance(record, dict):
            raise ValueError(f"Current owner must be a mapping: {path}")
        records[path.relative_to(root).as_posix()] = record
    validate_records(registry, records)
    result = PermanentIdentity(
        root,
        members,
        captures,
        {record["mim_id"]: (path, record) for path, record in records.items()},
    )
    result.verify()
    return result


def registry_identity_candidates(record: dict, subject: str) -> set[str]:
    """Retain Rule B1's original registry identity, never invent a numeric alias."""
    aliases = record.get("legacy_identifiers", []) if "mim_id" in record else [subject]
    candidates = {
        value
        for value in [record.get("identifier", ""), *aliases]
        if value.startswith(("kgmicrobe.ingredient:", "kgmicrobe.compound:"))
    }
    for alias in aliases:
        if alias.startswith("MIM:"):
            slug = alias.removeprefix("MIM:").lower()
            candidates.update(f"kgmicrobe.{kind}:{slug}" for kind in ("ingredient", "compound"))
    return candidates


def _safe_synonyms(row: dict, record: dict) -> None:
    rejected = {
        str(synonym.get("synonym_text", "")).strip().casefold()
        for synonym in record.get("synonyms") or []
        if synonym.get("synonym_type") == "REJECTED_LABEL"
    }
    tokens = [token.strip() for token in row.get("other", "").split("|") if token.strip()]
    if any(
        not is_resolving_synonym_text(token) or token.casefold() in rejected for token in tokens
    ):
        raise ValueError(f"Non-resolving/rejected synonym in supported row: {row['subject_id']}")


def _safe_identifiers(row: dict) -> None:
    """Check active CAS identities and annotations without inferring chemical identity."""
    for field in ("subject_id", "object_id", "other", "xref"):
        for value in row.get(field, "").split("|"):
            token = value.strip()
            if token.lower().startswith("cas:"):
                number = token.split(":", 1)[1]
            elif re.fullmatch(r"\d+-\d+-\d+", token):
                number = token
            else:
                continue
            if not re.fullmatch(r"[1-9][0-9]{1,6}-[0-9]{2}-[0-9]", number):
                raise ValueError(f"Invalid CAS identifier in supported {field}: {token}")
            digits = number.replace("-", "")
            check = sum(weight * int(digit) for weight, digit in enumerate(digits[-2::-1], 1)) % 10
            if check != int(digits[-1]):
                raise ValueError(f"Invalid CAS check digit in supported {field}: {token}")


def _cas_relocated_acquisition(root, packet_ref, verified, publication, generation, proof, ref):
    """Bind #1411 relocation to a selected native acquisition, not a new root.

    This checks provenance only. The full current semantic-release verifier must
    still reconstruct the transition; neither a capsule nor its COMPLETE receipt
    grants scientific support or clears the ordinary CAS backlog.
    """
    from mediaingredientmech.native_acquisition import Evidence

    class VerifiedInputs:
        def read(self, name, expected):
            _relative(root, name)
            raw = verified.get(name)
            if raw is None or hashlib.sha256(raw).hexdigest() != expected:
                raise ValueError("CAS relocation evidence must be pinned by the ordinary review")
            return raw

        def document(self, name, expected):
            return _json_bytes(self.read(name, expected), name)

    if not isinstance(packet_ref, dict) or set(packet_ref) != {"path", "sha256"}:
        raise ValueError("CAS relocation requires an explicit pinned native transition")
    evidence = Evidence(
        VerifiedInputs(), packet_ref, lambda raw: _json_bytes(raw, "CAS native acquisition")
    )
    selected = evidence.packet["publication"]
    if not isinstance(selected, dict) or set(selected) != {
        "root",
        "receipt",
        "manifest",
        "request",
    }:
        raise ValueError("CAS relocation publication selection differs")
    original = selected["root"]
    if (
        not isinstance(original, str)
        or not original.startswith("/")
        or str(PurePosixPath(original)) != original
        or ".." in PurePosixPath(original).parts
        or generation.get("root") != original
        or proof.get("relative_path") != ref["path"]
        or proof["path"] != str(PurePosixPath(original) / ref["path"])
    ):
        raise ValueError("CAS relocation original root/request identity differs")
    receipt = evidence.document(original, selected["receipt"])
    manifest = evidence.document(original, selected["manifest"])
    request = evidence.document(original, selected["request"])
    capability = "reviewed-stable-sssom-publication-v1"
    if (
        receipt.get("capability") != capability
        or receipt.get("state") != "COMPLETE"
        or receipt.get("recovery_required") is not False
        or receipt.get("scientific_approval_added") is not False
        or receipt.get("manifest") != selected["manifest"]
        or manifest.get("capability") != capability
        or manifest.get("root") != original
        or manifest.get("head") != generation.get("head")
        or manifest.get("scientific_approval_added") is not False
        or manifest.get("request") != selected["request"]
        or request.get("capability") != capability
        or request.get("head") != manifest.get("head")
        or request.get("generation") != publication["generation"]
        or generation.get("state") != "COMPLETE"
        or generation.get("returncode") != 0
    ):
        raise ValueError("CAS relocation complete native reference chain differs")
    outputs = manifest.get("outputs")
    expected_outputs = {
        "mappings/ingredient_mappings.sssom.tsv",
        "mappings/suppressed_aliases.tsv",
        "mappings/stable_sssom_generation.json",
        "mappings/stable_sssom_publication.json",
    }
    if (
        not isinstance(outputs, dict)
        or set(outputs) != expected_outputs
        or receipt.get("outputs") != outputs
    ):
        raise ValueError("CAS relocation native output inventory differs")
    for name, pin in outputs.items():
        if evidence.read(original, {"path": name, "sha256": pin}) != VerifiedInputs().read(
            name, pin
        ):
            raise ValueError("CAS relocation current native output differs")
    # Require exact acquisition tuples for the entire connecting chain. An equal
    # hash under another source root/path is not a substitute for these members.
    for reference in (
        publication["generation"],
        generation["outputs"]["manifest"],
        ref,
        proof["request"]["claims"],
    ):
        if evidence.read(original, reference) != VerifiedInputs().read(
            reference["path"], reference["sha256"]
        ):
            raise ValueError("CAS relocation captured provenance differs")


def _cas_backlog(root, source, metadata, rows, decisions, verified, transition_ref=None):
    """Retain exact native diagnostic history; this never authorizes a positive claim.

    Native publication separately reconstructs generation and authenticates its
    scientific/source endpoint. This ordinary boundary carries its exact current
    provenance and immutable inputs, and cannot strip or promote a held row.
    The independent supported-CAS validator remains unchanged.
    """
    canonical = "mappings/ingredient_mappings.sssom.tsv"
    manifest_name = "mappings/stable_sssom_generation.json"
    publication_name = "mappings/stable_sssom_publication.json"
    capability = metadata.get("cas_disposition_capability")
    manifest_path = root / manifest_name
    observed = (
        _json_bytes(_identity_input(manifest_path)[1], manifest_name)
        if manifest_path.exists()
        else None
    )
    publication_path = root / publication_name
    observed_publication = (
        _json_bytes(_identity_input(publication_path)[1], publication_name)
        if publication_path.exists()
        else None
    )
    publication_selected = False
    if observed_publication is not None:
        publication_selected = any(
            item.get("cas_disposition") is not None or item.get("mandatory_disposition") is not None
            for item in observed_publication.get("selection", {}).get("rows", [])
        )
        generation_ref = observed_publication.get("generation")
        if isinstance(generation_ref, dict) and isinstance(generation_ref.get("path"), str):
            generation_path = _relative(root, generation_ref["path"])
            if generation_path.exists():
                raw = _identity_input(generation_path)[1]
                observed_generation = _json_bytes(raw, generation_ref["path"])
                if observed_generation.get("cas_dispositions") is not None:
                    if hashlib.sha256(raw).hexdigest() != generation_ref.get("sha256"):
                        raise ValueError("CAS backlog publication generation reference changed")
                    publication_selected = True
    selected = (
        observed is not None and observed.get("cas_dispositions") is not None
    ) or publication_selected
    if capability is None and not selected:
        if "cas_disposition_request" in metadata:
            raise ValueError("CAS disposition request lacks its required capability")
        return None
    if (
        capability != "reviewed-invalid-cas-dispositions-v1"
        or not selected
        or source != root / canonical
        or observed is None
        or observed.get("cas_dispositions") is None
    ):
        raise ValueError("CAS disposition capability/provenance missing or stripped")

    def document(ref):
        if not isinstance(ref, dict) or set(ref) != {"path", "sha256"}:
            raise ValueError("CAS disposition reference differs")
        raw = verified.get(ref["path"])
        if raw is None or hashlib.sha256(raw).hexdigest() != ref["sha256"]:
            raise ValueError("CAS disposition evidence must be pinned by the ordinary review")
        return _json_bytes(raw, ref["path"])

    if manifest_name not in verified or publication_name not in verified:
        raise ValueError("CAS backlog requires current native generation/publication provenance")
    manifest = _json_bytes(verified[manifest_name], manifest_name)
    publication = _json_bytes(verified[publication_name], publication_name)
    if (
        manifest != observed
        or publication != observed_publication
        or publication.get("artifacts", {}).get(canonical) != digest(source)
    ):
        raise ValueError("CAS backlog current native artifacts differ")
    generation = document(publication["generation"])
    generation_manifest = document(generation["outputs"]["manifest"])
    if generation_manifest != manifest:
        raise ValueError("CAS backlog original generation proof differs")
    proof = manifest["cas_dispositions"]
    ref = metadata["cas_disposition_request"]
    if generation.get("cas_dispositions") != ref or proof["sha256"] != ref["sha256"]:
        raise ValueError("CAS backlog request binding differs")
    original_root = generation.get("root")
    if (
        not isinstance(original_root, str)
        or not original_root.startswith("/")
        or str(PurePosixPath(original_root)) != original_root
        or ".." in PurePosixPath(original_root).parts
        or not isinstance(ref.get("path"), str)
        or proof.get("relative_path") != ref["path"]
        or proof.get("path") != str(PurePosixPath(original_root) / ref["path"])
    ):
        raise ValueError("CAS backlog original request/root binding differs")
    _relative(root, ref["path"])
    if original_root != str(root):
        _cas_relocated_acquisition(
            root, transition_ref, verified, publication, generation, proof, ref
        )
    request = document(ref)
    claims = document(request["claims"])
    if request != proof["request"] or claims != proof["content"]:
        raise ValueError("CAS backlog claims or paired review selection changed")
    # The replaced canonical beforeimage remains an exact historical input, not
    # a purported current canonical file. Require its real bytes among the
    # ordinary review's retained evidence; no hash-only history is accepted.
    canonical_sha = claims["canonical"]["sha256"]
    if not any(hashlib.sha256(raw).hexdigest() == canonical_sha for raw in verified.values()):
        raise ValueError("CAS backlog complete historical canonical bytes omitted")
    required = {**claims["evidence_inputs"], **request["review_inputs"]}
    required.update({r["path"]: r["sha256"] for r in request["reviews"]})
    required.update({e["owner"]["path"]: e["owner"]["sha256"] for e in claims["entries"]})
    if claims["source_correction"] is not None:
        correction = claims["source_correction"]
        required[correction["path"]] = correction["sha256"]
    for name, expected in required.items():
        if name == canonical and expected == canonical_sha:
            continue  # Authenticated historical bytes were required immediately above.
        if name not in verified or hashlib.sha256(verified[name]).hexdigest() != expected:
            raise ValueError("CAS backlog immutable evidence changed or omitted: " + name)
    held = {item["candidate_position"]: item for item in proof["held_rows"]}
    selection = publication["selection"]["rows"]
    for position, obligation in held.items():
        candidates = [item for item in selection if item["candidate_position"] == position]
        if len(candidates) != 1:
            raise ValueError("CAS backlog publication row missing")
        item = candidates[0]
        if (
            item.get("mandatory_disposition") != "INSTALL_WITHHOLD"
            or item["disposition"] != "INSTALL_WITHHOLD"
            or item.get("cas_disposition") != obligation
            or item["candidate_row"] != obligation["candidate_row"]
            or not any(old["row"] == obligation["historical_row"] for old in item["before_rows"])
        ):
            raise ValueError("CAS backlog hold/history stripped or promoted")
        matches = [i for i, row in enumerate(rows, 1) if row == item["proposed_row"]]
        if len(matches) != 1 or decisions[matches[0]]["disposition"] != "WITHHOLD":
            raise ValueError("Historical invalid CAS must remain in the ordinary WITHHOLD backlog")
    return proof


def load_review(root: Path, review_path: Path) -> dict:
    root = root.resolve()
    review_path = review_path if review_path.is_absolute() else root / review_path
    review_bytes = review_path.read_bytes()
    review_sha = hashlib.sha256(review_bytes).hexdigest()
    snapshots = {review_path: review_sha}
    review = _json_bytes(review_bytes, str(review_path))
    if "identity_projection" in review:
        from mediaingredientmech.identity_projection import load_projected_mapping_review

        return load_projected_mapping_review(root, review_path)
    if review.get("schema_version") != 1:
        raise ValueError("Unsupported review schema")
    source = _relative(root, review["source_sssom"])
    source_bytes = source.read_bytes()
    if hashlib.sha256(source_bytes).hexdigest() != review["source_sha256"]:
        raise ValueError("Stale source SSSOM hash")
    snapshots[source] = review["source_sha256"]
    verified = {}
    for group in ("inputs", "record_inputs"):
        if not isinstance(review.get(group), dict):
            raise ValueError(f"Missing {group}")
        for name, expected in review[group].items():
            path = _relative(root, name)
            content = path.read_bytes()
            if hashlib.sha256(content).hexdigest() != expected:
                raise ValueError(f"Stale {group} hash: {name}")
            if path in snapshots and snapshots[path] != expected:
                raise ValueError(f"Conflicting input hashes: {name}")
            verified[name] = content
            snapshots[path] = expected
    metadata, fields, rows = read_sssom(source, content=source_bytes)
    owners, records = _owners(root, rows, verified)
    if set(review["record_inputs"]) != set(owners):
        raise ValueError("record_inputs must exactly cover independently resolved owners")
    decisions = review.get("decisions")
    if not isinstance(decisions, list) or len(decisions) != len(rows):
        raise ValueError("Review decisions must completely cover source rows")
    indexed: dict = {}
    proofs: dict = {}
    evidence_inputs = {name: verified[name] for name in review["inputs"]}
    for decision in decisions:
        position = decision.get("source_position")
        if type(position) is not int or not 1 <= position <= len(rows) or position in indexed:
            raise ValueError("Invalid/duplicate review source position")
        row, owner = rows[position - 1], owners[position - 1]
        validate_review_decision(
            decision,
            row,
            owner,
            review["record_inputs"][owner],
            evidence_inputs,
            proofs,
        )
        if decision["disposition"] == "SUPPORTED":
            _safe_synonyms(row, records[owner])
            _safe_identifiers(row)
        indexed[position] = decision
    cas_proof = _cas_backlog(
        root, source, metadata, rows, indexed, verified, review.get("cas_disposition_transition")
    )
    selected = [
        rows[i - 1] for i, decision in indexed.items() if decision["disposition"] == "SUPPORTED"
    ]
    identities = {
        (row["subject_id"], row["object_id"])
        for row in selected
        if row["predicate_id"] == "skos:exactMatch"
    }
    owner_by_subject = {
        row["subject_id"]: records[owner] for row, owner in zip(rows, owners, strict=True)
    }
    permanent_rows = [
        row
        for row in selected
        if row["predicate_id"] in {"skos:narrowMatch", "skos:broadMatch"}
        and permanent_subject(row["subject_id"])
    ]
    identity = (
        capture_permanent_identity(root, metadata, reviewed_inputs=verified)
        if permanent_rows
        else None
    )
    if identity is not None:
        snapshots.update(identity.hashes)
    for row in selected:
        if row["predicate_id"] in {"skos:narrowMatch", "skos:broadMatch"}:
            if permanent_subject(row["subject_id"]):
                assert identity is not None
                identity.require(row["subject_id"], row["subject_label"])
                continue
            if not any(
                (row["subject_id"], candidate) in identities
                for candidate in registry_identity_candidates(
                    owner_by_subject[row["subject_id"]], row["subject_id"]
                )
            ):
                raise ValueError(
                    f"Supported asymmetric mapping lacks registry identity sibling (Rule B1): {row['subject_id']}"
                )
    loaded = {
        "review": review,
        "review_path": review_path,
        "metadata": metadata,
        "fields": fields,
        "rows": rows,
        "decisions": [indexed[i] for i in range(1, len(rows) + 1)],
        "review_sha256": review_sha,
        "input_snapshot": snapshots,
        "permanent_identity": identity,
        "cas_dispositions": cas_proof,
    }
    _check_snapshot(loaded)
    return loaded


def _check_snapshot(loaded: dict) -> None:
    if loaded.get("permanent_identity") is not None:
        loaded["permanent_identity"].verify()
    for path, expected in loaded["input_snapshot"].items():
        if digest(path) != expected:
            raise ValueError(f"Input changed during review/export: {path}")


def _tsv(fields, rows) -> bytes:
    stream = io.StringIO(newline="")
    writer = csv.DictWriter(stream, fieldnames=fields, delimiter="\t", lineterminator="\n")
    writer.writeheader()
    writer.writerows(rows)
    return stream.getvalue().encode()


def expected_products(root: Path, review_path: Path) -> tuple[dict[str, bytes], dict]:
    return _products(load_review(root, review_path))


def _products(loaded: dict) -> tuple[dict[str, bytes], dict]:
    review, rows, decisions = loaded["review"], loaded["rows"], loaded["decisions"]
    products, counts, identifiers = {}, {}, {}
    for disposition, filename, suffix in (
        ("SUPPORTED", PRODUCTS[0], "reviewed-supported"),
        ("WITHHOLD", PRODUCTS[1], "withheld-backlog"),
    ):
        selected = [
            row
            for row, decision in zip(rows, decisions, strict=True)
            if decision["disposition"] == disposition
        ]
        metadata = subset_date_metadata(loaded["metadata"], selected)
        metadata["mapping_set_id"] = str(metadata["mapping_set_id"]).rstrip("/") + "/" + suffix
        metadata["mapping_set_description"] = (
            "Evidence-reviewed supported subset of MediaIngredientMech mappings."
            if disposition == "SUPPORTED"
            else "Withheld MediaIngredientMech mapping backlog. These rows are preserved for review and are not approved for use as supported mappings."
        )
        header = "".join(
            "# " + line + "\n"
            for line in yaml.safe_dump(
                metadata, sort_keys=False, allow_unicode=True, width=100000
            ).splitlines()
        )
        products[filename] = header.encode() + _tsv(loaded["fields"], selected)
        counts[disposition.lower()] = len(selected)
        identifiers[disposition.lower()] = metadata["mapping_set_id"]
    disposition_rows = []
    for row, decision in zip(rows, decisions, strict=True):
        item = dict(decision)
        item.update({field: row[field] for field in ("subject_id", "predicate_id", "object_id")})
        item["owner_record_sha256"] = review["record_inputs"][decision["owner_record"]]
        disposition_rows.append({field: item[field] for field in DISPOSITION_FIELDS})
    products[PRODUCTS[2]] = _tsv(DISPOSITION_FIELDS, disposition_rows)
    manifest = {
        "schema_version": 1,
        "scope": "MIM-only reviewed SSSOM; no KGX dependency",
        "semantic_status": "PASS_SUPPORTED_SUBSET",
        "source_sssom": review["source_sssom"],
        "source_sha256": review["source_sha256"],
        "review_sha256": loaded["review_sha256"],
        "counts": {"source": len(rows), **counts},
        "mapping_set_ids": identifiers,
        "files": {name: hashlib.sha256(content).hexdigest() for name, content in products.items()},
    }
    products["manifest.json"] = (json.dumps(manifest, sort_keys=True, indent=2) + "\n").encode()
    return products, manifest


def validate_reviewed(root: Path, review_path: Path, output: Path) -> dict:
    loaded = load_review(root, review_path)
    products, manifest = _products(loaded)
    if {path.name for path in output.iterdir()} != set(products):
        raise ValueError("Unexpected or missing output artifact")
    for name, content in products.items():
        if not (output / name).is_file() or (output / name).read_bytes() != content:
            raise ValueError(f"Output differs from source/evidence-derived expectation: {name}")
    _check_snapshot(loaded)
    return manifest


def export_reviewed(root: Path, review_path: Path, output: Path) -> dict:
    loaded = load_review(root, review_path)
    products, _ = _products(loaded)
    protected = {
        loaded["review_path"].resolve(),
        (root / loaded["review"]["source_sssom"]).resolve(),
    }
    protected.update(
        (root / path).resolve()
        for group in ("inputs", "record_inputs")
        for path in loaded["review"][group]
    )
    if any((output / name).resolve() in protected for name in products):
        raise ValueError("Output must not overwrite source or evidence")
    if output.is_symlink():
        raise ValueError("Output directory must not be a symlink")
    if output.exists() and any(path.name not in products for path in output.iterdir()):
        raise ValueError("Output directory contains unrelated files")
    output.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(prefix=f".{output.name}-", dir=output.parent) as temporary:
        stage, backup = Path(temporary) / "new", Path(temporary) / "previous"
        stage.mkdir()
        for name, content in products.items():
            (stage / name).write_bytes(content)
        manifest = validate_reviewed(root, review_path, stage)
        _check_snapshot(loaded)
        if output.exists():
            output.rename(backup)
        try:
            stage.rename(output)
            _check_snapshot(loaded)
        except BaseException:
            if output.exists():
                shutil.rmtree(output)
            if backup.exists():
                backup.rename(output)
            raise
    return manifest


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path.cwd())
    parser.add_argument("--review", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--validate-only", action="store_true")
    args = parser.parse_args()
    action = validate_reviewed if args.validate_only else export_reviewed
    print(json.dumps(action(args.root, args.review, args.output), sort_keys=True, indent=2))


if __name__ == "__main__":
    main()
