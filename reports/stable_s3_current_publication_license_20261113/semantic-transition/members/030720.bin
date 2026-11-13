"""Bounded #1265 administrative-ID projection; never a scientific review.

The fixed historical commit and complete native preimages are independent of the
new manifest. Every biological field, old decision and negative disposition stays
unchanged. No general record-hash equivalence or approval refresh is introduced.
"""

from __future__ import annotations

import argparse
import hashlib
import io
import json
import os
import subprocess
import tempfile
from copy import deepcopy
from dataclasses import dataclass
from datetime import date, datetime, timedelta
from pathlib import Path
from typing import Any

import yaml  # type: ignore[import-untyped]

from mediaingredientmech.curie import mim_curie_for_stem
from mediaingredientmech.stable_ids import MIM_PREFIX, parse_registry

BASE_COMMIT = "0dac278466699129a083343a921c2e0ca18a9ab4"
REPORT_ROOT = "reports/stable_ids_1265_20261108"
MANIFEST = REPORT_ROOT + "/migration.json"
SOURCE = "mappings/ingredient_mappings.sssom.tsv"
REGISTRY = "data/ids/mim_id_registry.tsv"
LIFECYCLE = "data/ids/mim_id_lifecycle.tsv"
OLD_MAPPING_REVIEW = "reports/sssom_completion_20260921/review.json"
MAPPING_REVIEW = REPORT_ROOT + "/mapping-review.json"
MAPPING_EVIDENCE = REPORT_ROOT + "/mapping-evidence.json"
KIND = "mim-stable-id-migration/v1"
PROJECTION_KIND = "mim-inherited-identity-projection/v1"
MAX_BLOB_BYTES = 64 * 1024 * 1024


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError("Identity projection: " + message)


def exact(left: Any, right: Any) -> bool:
    """JSON/YAML scalar types are evidence, so bools never equal integers."""
    if type(left) is not type(right):
        return False
    if isinstance(left, dict):
        return left.keys() == right.keys() and all(exact(left[key], right[key]) for key in left)
    if isinstance(left, list):
        return len(left) == len(right) and all(
            exact(a, b) for a, b in zip(left, right, strict=True)
        )
    return bool(left == right)


def sha(raw: bytes) -> str:
    return hashlib.sha256(raw).hexdigest()


def encode(value: Any) -> bytes:
    return (json.dumps(value, indent=2, ensure_ascii=False, allow_nan=False) + "\n").encode()


def document(raw: bytes) -> dict:
    def unique(pairs):
        result = {}
        for key, value in pairs:
            require(key not in result, "duplicate JSON key")
            result[key] = value
        return result

    result = json.loads(
        raw,
        object_pairs_hook=unique,
        parse_constant=lambda value: (_ for _ in ()).throw(ValueError(value)),
    )
    if not isinstance(result, dict):
        raise ValueError("Identity projection: expected JSON object")
    return result


def safe_path(root: Path, name: str) -> Path:
    path = Path(name)
    require(
        bool(name)
        and not path.is_absolute()
        and path.as_posix() == name
        and ".." not in path.parts
        and "\\" not in name,
        "unsafe input path",
    )
    candidate = root / path
    require(not any(p.is_symlink() for p in (candidate, *candidate.parents)), "aliased input")
    return candidate


def git_files(root: Path, names: list[str]) -> dict[str, bytes]:
    """Read exact regular Git blobs from the fixed scientific baseline."""
    return revision_files(root, BASE_COMMIT, names)


def revision_files(
    root: Path, revision: str, names: list[str], *, missing_ok: bool = False
) -> dict[str, bytes]:
    """Read bounded regular blobs at a full commit ID; never checkout files."""
    require(
        len(revision) == 40 and all(char in "0123456789abcdef" for char in revision),
        "full Git revision required",
    )
    require(len(names) == len(set(names)), "duplicate historical path")
    for name in names:
        safe_path(root, name)
        require("\n" not in name and "\r" not in name, "invalid historical path")
    listing = subprocess.check_output(["git", "ls-tree", "-rz", revision], cwd=root, timeout=60)
    objects = {}
    wanted = set(names)
    for row in listing.split(b"\0"):
        if not row:
            continue
        metadata, raw_path = row.split(b"\t", 1)
        mode, kind, oid = metadata.decode().split()
        path = raw_path.decode()
        if path in wanted:
            require(mode in {"100644", "100755"} and kind == "blob", "nonregular historical input")
            objects[path] = oid
    require(missing_ok or set(objects) == set(names), "historical inventory differs")
    names = [name for name in names if name in objects]
    result = subprocess.check_output(
        ["git", "cat-file", "--batch"],
        cwd=root,
        input="".join(objects[name] + "\n" for name in names).encode(),
        timeout=120,
    )
    stream = io.BytesIO(result)
    contents = {}
    for name in names:
        blob_oid, blob_kind, size = stream.readline().split()
        require(
            blob_oid.decode() == objects[name] and blob_kind == b"blob", "historical object differs"
        )
        count = int(size)
        require(0 <= count <= MAX_BLOB_BYTES, "historical blob exceeds bound")
        raw = stream.read(count)
        require(len(raw) == count and stream.read(1) == b"\n", "incomplete historical blob")
        contents[name] = raw
    require(not stream.read(1), "extra historical data")
    return contents


def record_paths(root: Path, *, historical: bool = False) -> list[str]:
    groups = ("data/ingredients/mapped", "data/ingredients/unmapped")
    if historical:
        raw = subprocess.check_output(
            ["git", "ls-tree", "-rz", "--name-only", BASE_COMMIT, "--", *groups],
            cwd=root,
            timeout=60,
        )
        return sorted(path.decode() for path in raw.split(b"\0") if path.endswith(b".yaml"))
    paths = []
    for group in groups:
        folder = safe_path(root, group)
        require(folder.is_dir(), "missing ingredient directory")
        for path in folder.rglob("*.yaml"):
            relative = path.relative_to(root).as_posix()
            require(safe_path(root, relative).is_file(), "nonregular ingredient")
            paths.append(relative)
    return sorted(paths)


try:
    from yaml import CSafeLoader as _YamlBase
except ImportError:
    from yaml import SafeLoader as _YamlBase


class UniqueRecordLoader(_YamlBase):
    """Reject parser-dependent duplicate fields at every record nesting level."""

    def construct_mapping(self, node, deep=False):
        self.flatten_mapping(node)
        result = {}
        for key_node, value_node in node.value:
            key = self.construct_object(key_node, deep=deep)
            require(key not in result, "duplicate YAML record key")
            result[key] = self.construct_object(value_node, deep=deep)
        return result


def verify_record_transition(
    entry: dict, before_raw: bytes, after_raw: bytes, manifest: dict, mint: Any, index: int
) -> tuple[dict, dict]:
    require(
        set(entry) == {"path", "mim_id", "legacy_identifiers", "before_sha256", "after_sha256"},
        "unsupported record transition",
    )
    name, identifier = entry["path"], f"MIM:{index:07d}"
    require(
        sha(before_raw) == entry["before_sha256"] and sha(after_raw) == entry["after_sha256"],
        "record preimage or postimage differs",
    )
    old, new = (yaml.load(raw, Loader=UniqueRecordLoader) for raw in (before_raw, after_raw))
    require(isinstance(old, dict) and isinstance(new, dict), "invalid ingredient record")
    require("mim_id" not in old and "legacy_identifiers" not in old, "record was already minted")
    legacy = list(dict.fromkeys([mim_curie_for_stem(Path(name).stem), old["identifier"]]))
    require(
        entry["mim_id"] == identifier
        and new.get("mim_id") == identifier
        and entry["legacy_identifiers"] == legacy
        and new.get("legacy_identifiers") == legacy,
        "assigned identity or aliases differ",
    )
    require(
        mint.mim_id == identifier
        and mint.label_at_minting == old["preferred_term"]
        and mint.minted_on == manifest["minted_on"]
        and mint.status == "active"
        and not mint.replaced_by,
        "registry binding differs",
    )
    old_history = old.get("curation_history", [])
    history = new.get("curation_history")
    require(
        isinstance(old_history, list)
        and isinstance(history, list)
        and len(history) == len(old_history) + 1
        and exact(history[:-1], old_history),
        "historical curation events changed",
    )
    event = history[-1]
    expected_event = {
        "timestamp": manifest["timestamp"],
        "curator": "codex",
        "action": "ASSIGNED_MIM_ID",
        "llm_assisted": True,
        "changes": f"#1265: assigned permanent {identifier}; retained mapping identifier and legacy aliases.",
    }
    require(exact(event, expected_event), "migration history event differs")
    restored = deepcopy(new)
    del restored["mim_id"], restored["legacy_identifiers"]
    if "curation_history" in old:
        restored["curation_history"] = old_history
    else:
        del restored["curation_history"]
    require(exact(restored, old), "migration changed a biological or other preexisting field")
    return old, new


def verify_transition(manifest: dict, before: dict[str, bytes], after: dict[str, bytes]) -> dict:
    """Pure complete transition proof, usable by both native and portable checks."""
    from mediaingredientmech.export.reviewed_sssom import read_sssom

    required = {
        "schema_version",
        "kind",
        "source_commit",
        "minted_on",
        "timestamp",
        "records",
        "before_sssom_sha256",
        "after_sssom_sha256",
        "registry_sha256",
        "lifecycle_sha256",
        "registry_path",
        "lifecycle_path",
        "approval",
        "scientific_approval_added",
    }
    require(set(manifest) == required, "unsupported migration manifest fields")
    require(
        type(manifest["schema_version"]) is int
        and manifest["schema_version"] == 1
        and manifest["kind"] == KIND
        and manifest["source_commit"] == BASE_COMMIT,
        "unsupported migration authority",
    )
    require(
        manifest["approval"] == "NONE" and manifest["scientific_approval_added"] is False,
        "administrative migration cannot grant approval",
    )
    require(
        manifest["registry_path"] == REGISTRY and manifest["lifecycle_path"] == LIFECYCLE,
        "registry paths differ",
    )
    minted = date.fromisoformat(manifest["minted_on"])
    when = datetime.fromisoformat(manifest["timestamp"])
    require(when.utcoffset() == timedelta(0) and when.date() == minted, "invalid migration date")
    entries = manifest["records"]
    require(isinstance(entries, list) and bool(entries), "empty migration inventory")
    names = [entry.get("path") for entry in entries]
    require(
        all(isinstance(name, str) for name in names) and names == sorted(set(names)),
        "migration inventory is not unique lexical path order",
    )
    require(
        set(before) == {*names, SOURCE} and set(after) == {*names, SOURCE, REGISTRY, LIFECYCLE},
        "complete preimage/postimage inventory differs",
    )
    require(
        sha(before[SOURCE]) == manifest["before_sssom_sha256"]
        and sha(after[SOURCE]) == manifest["after_sssom_sha256"]
        and sha(after[REGISTRY]) == manifest["registry_sha256"]
        and sha(after[LIFECYCLE]) == manifest["lifecycle_sha256"],
        "migration artifact hash differs",
    )
    registry = parse_registry(after[REGISTRY], after[LIFECYCLE])
    require(
        len(registry.entries) == len(entries) and not registry.events,
        "first mint must exactly cover records without lifecycle changes",
    )
    aliases, owners, old_records, new_records = {}, {}, {}, {}
    for index, (entry, mint) in enumerate(zip(entries, registry.entries, strict=True), 1):
        name, identifier = entry["path"], f"MIM:{index:07d}"
        old, new = verify_record_transition(entry, before[name], after[name], manifest, mint, index)
        alias = mim_curie_for_stem(Path(name).stem)
        require(alias not in aliases, "ambiguous historical owner identity")
        aliases[alias], owners[identifier] = identifier, name
        old_records[name], new_records[name] = old, new
    old_meta, old_fields, old_rows = read_sssom(Path(SOURCE), content=before[SOURCE])
    new_meta, new_fields, new_rows = read_sssom(Path(SOURCE), content=after[SOURCE])
    require(old_fields == new_fields and len(old_rows) == len(new_rows), "SSSOM shape changed")
    expected_meta = deepcopy(old_meta)
    expected_meta["curie_map"]["MIM"] = MIM_PREFIX
    require(exact(expected_meta, new_meta), "SSSOM metadata changed beyond the MIM resolver")
    for old_row, new_row in zip(old_rows, new_rows, strict=True):
        require(old_row["subject_id"] in aliases, "unowned historical mapping")
        require(
            new_row == dict(old_row, subject_id=aliases[old_row["subject_id"]]),
            "mapping changed beyond its administrative subject ID",
        )
    return {
        "aliases": aliases,
        "owners": owners,
        "old_records": old_records,
        "new_records": new_records,
        "old_rows": old_rows,
        "rows": new_rows,
        "metadata": new_meta,
        "fields": new_fields,
    }


@dataclass
class Proof:
    root: Path
    manifest: dict
    before: dict[str, bytes]
    after: dict[str, bytes]
    transition: dict
    snapshots: dict[str, bytes]

    def recheck(self) -> None:
        require(
            record_paths(self.root) == sorted(self.transition["new_records"]),
            "record inventory changed during projection",
        )
        for name, raw in self.snapshots.items():
            require(
                safe_path(self.root, name).read_bytes() == raw, "input changed during projection"
            )


def prove_identity_migration(root: Path) -> Proof:
    root = root.resolve()
    manifest_raw = safe_path(root, MANIFEST).read_bytes()
    manifest = document(manifest_raw)
    names = record_paths(root, historical=True)
    require(record_paths(root) == names, "current ingredient inventory differs from baseline")
    before = git_files(root, [*names, SOURCE])
    after = {
        name: safe_path(root, name).read_bytes() for name in [*names, SOURCE, REGISTRY, LIFECYCLE]
    }
    transition = verify_transition(manifest, before, after)
    proof = Proof(root, manifest, before, after, transition, {MANIFEST: manifest_raw, **after})
    proof.recheck()
    return proof


def _original_mapping(proof: Proof) -> tuple[dict, dict[str, bytes]]:
    """Revalidate exact historical mapping decisions; never infer their status."""
    from mediaingredientmech.export.reviewed_sssom import _safe_identifiers, _safe_synonyms
    from mediaingredientmech.review_claims import validate_review_decision

    raw = git_files(proof.root, [OLD_MAPPING_REVIEW])[OLD_MAPPING_REVIEW]
    review = document(raw)
    require(
        review.get("schema_version") == 1
        and review["source_sssom"] == SOURCE
        and review["source_sha256"] == sha(proof.before[SOURCE]),
        "historical review/source differs",
    )
    declared = dict(review["inputs"])
    for name, digest in review["record_inputs"].items():
        require(name not in declared or declared[name] == digest, "conflicting historical input")
        declared[name] = digest
    historical = git_files(proof.root, list(declared))
    require(
        all(sha(historical[name]) == digest for name, digest in declared.items()),
        "historical review input differs from immutable baseline",
    )
    historical[OLD_MAPPING_REVIEW] = raw
    # Historical review/report evidence is immutable. Changed implementation and
    # source data are separate, explicit current inputs, never restamped evidence.
    for name, content in historical.items():
        if name.startswith("reports/"):
            current = safe_path(proof.root, name).read_bytes()
            require(current == content, "historical scientific report was changed")
            proof.snapshots[name] = current
    old_owners = {
        mim_curie_for_stem(Path(name).stem): name for name in proof.transition["old_records"]
    }
    rows = proof.transition["old_rows"]
    require(
        set(review["record_inputs"]) == {old_owners[row["subject_id"]] for row in rows},
        "historical review owner coverage differs",
    )
    decisions = review["decisions"]
    require(
        len(decisions) == len(rows)
        and [d["source_position"] for d in decisions] == list(range(1, len(rows) + 1)),
        "historical decision inventory differs",
    )
    proofs: dict = {}
    evidence = {name: historical[name] for name in review["inputs"]}
    for row, decision in zip(rows, decisions, strict=True):
        owner = old_owners[row["subject_id"]]
        require(
            review["record_inputs"][owner] == sha(proof.before[owner]),
            "historical owner hash differs",
        )
        validate_review_decision(decision, row, owner, sha(proof.before[owner]), evidence, proofs)
        if decision["disposition"] == "SUPPORTED":
            _safe_synonyms(row, proof.transition["old_records"][owner])
            _safe_identifiers(row)
    identities = {
        (row["subject_id"], row["object_id"])
        for row, decision in zip(rows, decisions, strict=True)
        if decision["disposition"] == "SUPPORTED" and row["predicate_id"] == "skos:exactMatch"
    }
    for row, decision in zip(rows, decisions, strict=True):
        if decision["disposition"] == "SUPPORTED" and row["predicate_id"] in {
            "skos:narrowMatch",
            "skos:broadMatch",
        }:
            slug = row["subject_id"].removeprefix("MIM:").lower()
            require(
                any(
                    (row["subject_id"], f"kgmicrobe.{kind}:{slug}") in identities
                    for kind in ("ingredient", "compound")
                ),
                "historical Rule B1 evidence missing",
            )
    return review, historical


def projection_header(proof: Proof, original_path: str, original_bytes: bytes) -> dict:
    return {
        "kind": PROJECTION_KIND,
        "manifest": MANIFEST,
        "manifest_sha256": sha(proof.snapshots[MANIFEST]),
        "source_commit": BASE_COMMIT,
        "original_report": original_path,
        "original_report_sha256": sha(original_bytes),
        "scientific_approval_added": False,
    }


def mapping_products(proof: Proof) -> dict[str, bytes]:
    """Deterministically transport existing decisions without changing any verdict."""
    from mediaingredientmech.export.reviewed_sssom import row_sha256

    original, historical = _original_mapping(proof)
    header = projection_header(proof, OLD_MAPPING_REVIEW, historical[OLD_MAPPING_REVIEW])
    decisions, entries = [], {}
    for row, old in zip(proof.transition["rows"], original["decisions"], strict=True):
        key = str(old["source_position"])
        owner = old["owner_record"]
        decision = dict(
            old, row_sha256=row_sha256(row), review_evidence=MAPPING_EVIDENCE, evidence_key=key
        )
        entries[key] = {
            "row_sha256": decision["row_sha256"],
            "owner_record": owner,
            "owner_record_sha256": sha(proof.after[owner]),
            "disposition": old["disposition"],
            "review_reason": old["review_reason"],
            "identity_projection": {
                **header,
                "original_decision": old,
                "original_owner_sha256": sha(proof.before[owner]),
            },
        }
        decisions.append(decision)
    evidence_bytes = encode(
        {
            "schema_version": 1,
            "scope": "Inherited identity-address projection only; no scientific review added",
            "identity_projection": header,
            "entries": entries,
        }
    )
    inputs = {}
    for name in {
        *original["inputs"],
        OLD_MAPPING_REVIEW,
        MANIFEST,
        REGISTRY,
        LIFECYCLE,
        "src/mediaingredientmech/identity_projection.py",
    }:
        content = safe_path(proof.root, name).read_bytes()
        proof.snapshots[name] = content
        inputs[name] = sha(content)
    inputs[MAPPING_EVIDENCE] = sha(evidence_bytes)
    review = {
        "schema_version": 1,
        "scope": "Inherited MIM mapping decisions at permanent record addresses; no scientific approval added",
        "source_sssom": SOURCE,
        "source_sha256": sha(proof.after[SOURCE]),
        "inputs": dict(sorted(inputs.items())),
        "record_inputs": {
            name: sha(proof.after[name]) for name in sorted(original["record_inputs"])
        },
        "decisions": decisions,
        "identity_projection": header,
    }
    proof.recheck()
    return {MAPPING_EVIDENCE: evidence_bytes, MAPPING_REVIEW: encode(review)}


def load_projected_mapping_review(root: Path, review_path: Path) -> dict:
    """Require exact independently regenerated projection bytes before publication."""
    proof = prove_identity_migration(root)
    require(
        review_path.resolve() == safe_path(proof.root, MAPPING_REVIEW),
        "unexpected projected review path",
    )
    outputs = mapping_products(proof)
    for name, raw in outputs.items():
        require(
            safe_path(proof.root, name).read_bytes() == raw, "identity mapping projection drift"
        )
        proof.snapshots[name] = raw
    review = document(outputs[MAPPING_REVIEW])
    proof.recheck()
    return {
        "review": review,
        "review_path": review_path,
        "metadata": proof.transition["metadata"],
        "fields": proof.transition["fields"],
        "rows": proof.transition["rows"],
        "decisions": review["decisions"],
        "review_sha256": sha(outputs[MAPPING_REVIEW]),
        "input_snapshot": {
            safe_path(proof.root, name): sha(raw) for name, raw in proof.snapshots.items()
        },
    }


def publish_outputs(
    root: Path, outputs: dict[str, bytes], *, check: bool, replace_derived: bool = False
) -> None:
    """Publish deterministic successors; old scientific authorities are never writable.

    Explicit replacement is limited to these generated successors, after complete
    proof replay. It is useful when implementation provenance changes before a
    reviewed release. Historical scientific reports and migration data are never
    accepted as output paths. A failed per-file publication can be replayed safely.
    """
    from mediaingredientmech.identity_projection_bundle import ARCHIVE as companion_archive
    from mediaingredientmech.identity_projection_bundle import REVIEW as companion_review
    from mediaingredientmech.identity_projection_frozen import FROZEN
    from mediaingredientmech.identity_projection_graph import ARCHIVE as graph_archive
    from mediaingredientmech.identity_projection_graph import DISPOSITIONS
    from mediaingredientmech.identity_projection_graph import REVIEW as semantic_review
    from mediaingredientmech.identity_projection_inventory import INVENTORY

    require(not (check and replace_derived), "check cannot replace generated artifacts")
    for name, content in outputs.items():
        require(
            name
            in {
                MAPPING_EVIDENCE,
                MAPPING_REVIEW,
                companion_review,
                semantic_review,
                DISPOSITIONS,
                FROZEN,
                INVENTORY,
            }
            or name.startswith(companion_archive)
            or name.startswith(graph_archive),
            "not a generated successor path",
        )
        path = safe_path(root, name)
        if path.exists():
            require(
                path.read_bytes() == content or replace_derived,
                "existing successor differs; use explicit --replace-derived",
            )
        else:
            require(not check, "missing projected artifact: " + name)
    if check:
        return
    for name, content in outputs.items():
        path = safe_path(root, name)
        if path.exists() and path.read_bytes() == content:
            continue
        path.parent.mkdir(parents=True, exist_ok=True)
        descriptor, staged = tempfile.mkstemp(prefix=".identity-projection-", dir=path.parent)
        staged_path = Path(staged)
        try:
            with os.fdopen(descriptor, "wb") as handle:
                handle.write(content)
                handle.flush()
                os.fsync(handle.fileno())
            if replace_derived:
                os.replace(staged_path, path)
            else:
                os.link(staged_path, path)
        finally:
            staged_path.unlink(missing_ok=True)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path.cwd())
    parser.add_argument("--check", action="store_true")
    parser.add_argument(
        "--replace-derived",
        action="store_true",
        help="Explicitly refresh only proven generated successors",
    )
    parser.add_argument(
        "--graph", action="store_true", help="Also prove the complete generated graph"
    )
    parser.add_argument(
        "--seed-historical-graph", type=Path, help="One-time baseline artifact directory"
    )
    args = parser.parse_args()
    proof = prove_identity_migration(args.root)
    outputs = mapping_products(proof)
    from mediaingredientmech.identity_projection_bundle import products as companion_products

    outputs.update(companion_products(proof, outputs))
    from mediaingredientmech.identity_projection_frozen import frozen_products

    outputs.update(frozen_products(proof))
    if args.graph:
        from mediaingredientmech.identity_projection_graph import products as graph_products

        outputs.update(graph_products(proof, seed=args.seed_historical_graph))
    publish_outputs(proof.root, outputs, check=args.check, replace_derived=args.replace_derived)
    proof.recheck()
    print(
        json.dumps(
            {
                "kind": PROJECTION_KIND,
                "records": len(proof.transition["new_records"]),
                "rows": len(proof.transition["rows"]),
                "scientific_approval_added": False,
                "checked": args.check,
            }
        )
    )


if __name__ == "__main__":
    main()
