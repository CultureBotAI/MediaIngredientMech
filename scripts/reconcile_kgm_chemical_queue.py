"""Reconcile source-owned KG chemical candidates without approving identities.

The source snapshot, current native MIM review, and consumed reviewed partition
are separate authorities. Exact casefold name hits are lexical observations,
never permission to collapse source IDs or override a downstream material hold.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import io
import json
import os
from collections import Counter, defaultdict
from contextlib import ExitStack, contextmanager
from pathlib import Path

import yaml

from mediaingredientmech import ingredient_bundle_refresh
from mediaingredientmech.curie import mim_curie_for_stem
from mediaingredientmech.export.reviewed_sssom import PRODUCTS, load_review, read_sssom, row_sha256
from mediaingredientmech.synonym_policy import is_resolving_synonym


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def json_bytes(value: object) -> bytes:
    return (json.dumps(value, indent=2, sort_keys=True, ensure_ascii=False) + "\n").encode()


def relative_file(root: Path, name: str) -> Path:
    path = root / name
    if (
        Path(name).is_absolute()
        or ".." in Path(name).parts
        or not path.resolve().is_relative_to(root)
    ):
        raise ValueError(f"Snapshot path escapes root: {name}")
    if not path.is_file():
        raise ValueError(f"Missing snapshot file: {name}")
    return path


def tsv_rows(path: Path) -> list[dict]:
    with path.open(newline="") as stream:
        reader = csv.DictReader(stream, delimiter="\t", strict=True)
        if not reader.fieldnames or len(reader.fieldnames) != len(set(reader.fieldnames)):
            raise ValueError(f"Invalid TSV header: {path}")
        rows = list(reader)
    if any(None in row or any(value is None for value in row.values()) for row in rows):
        raise ValueError(f"Malformed TSV row: {path}")
    return rows


def candidate_id(candidate: dict) -> str:
    payload = [candidate[key] for key in ("source", "source_id", "category")]
    return hashlib.sha256(
        json.dumps(payload, separators=(",", ":"), ensure_ascii=False).encode()
    ).hexdigest()


OBSERVATION_FIELDS = {
    "source_record": "source_record",
    "subject": "subject",
    "source_column": "source_column",
    "source_literal": "value",
    "source_citation": "source_citation",
    "object_curie": "object",
    "predicate": "predicate",
    "relation": "relation",
    "primary_knowledge_source": "primary_knowledge_source",
    "knowledge_level": "knowledge_level",
    "agent_type": "agent_type",
    "value_encoding": "value_encoding",
}


def verify_observation_holds(holds: list[dict], observations: list[dict]) -> None:
    """Bind the entire assertion, including its predicate, not merely its ID."""
    expected = Counter(tuple(row[key] for key in OBSERVATION_FIELDS) for row in holds)
    actual = Counter(tuple(row[key] for key in OBSERVATION_FIELDS.values()) for row in observations)
    if expected != actual:
        raise ValueError("Downstream holds do not exactly match observation witnesses")


def load_snapshot(root: Path) -> tuple[dict, list[dict], dict, dict[Path, str]]:
    root = root.resolve()
    path = root / "source-manifest.json"
    manifest = json.loads(path.read_bytes())
    if manifest.get("schema_version") != 1:
        raise ValueError("Unsupported source manifest")
    hashes = {path: digest(path)}
    for name, expected in manifest["files"].items():
        item = relative_file(root, name)
        if digest(item) != expected["sha256"] or item.stat().st_size != expected["bytes"]:
            raise ValueError(f"Changed source snapshot: {name}")
        hashes[item] = expected["sha256"]

    def bound(name: str) -> Path:
        item = relative_file(root, name)
        if item not in hashes:
            raise ValueError(f"Unbound source snapshot: {name}")
        return item

    spec = manifest["candidates"]
    candidates = json.loads(bound(spec["path"]).read_bytes())
    if digest(bound(spec["path"])) != spec["sha256"] or len(candidates) != spec["rows"]:
        raise ValueError("Candidate inventory differs from source manifest")
    if dict(Counter(item["source"] for item in candidates)) != spec["counts_by_source"]:
        raise ValueError("Candidate source counts differ")
    seen = set()
    for item in candidates:
        if item["candidate_id"] != candidate_id(item) or item["candidate_id"] in seen:
            raise ValueError("Invalid or duplicate source candidate identity")
        seen.add(item["candidate_id"])
        if not item["source_id"] or not item["category"]:
            raise ValueError("Missing source ID or category")
        if any(not isinstance(item[key], str) for key in ("source_label", "raw_source_label")):
            raise ValueError("Source labels must be literal strings, including blank labels")
    holds = defaultdict(list)
    source_ids = {(item["source"], item["source_id"]) for item in candidates}
    for table in manifest["hold_tables"]:
        rows = [
            row
            for row in tsv_rows(bound(table["path"]))
            if (table["source"], row[table["source_id_field"]]) in source_ids
        ]
        if "exact_observation_witness" in table:
            verify_observation_holds(rows, tsv_rows(bound(table["exact_observation_witness"])))
        for row in rows:
            holds[(table["source"], row[table["source_id_field"]])].append(
                {"table": table["path"], "row": row}
            )
    return manifest, candidates, dict(holds), hashes


def load_consumed(root: Path, expected: dict) -> tuple[dict, dict, dict[Path, str]]:
    """Verify the coherent consumed partition; never count WITHHOLD as coverage."""
    hashes = {}
    for name in (*PRODUCTS, "manifest.json"):
        path = root / name
        hashes[path] = digest(path)
        if hashes[path] != expected["files"][name]:
            raise ValueError(f"Consumed export differs from captured source: {name}")
    manifest = json.loads((root / "manifest.json").read_bytes())
    if (
        manifest.get("schema_version") != 1
        or manifest.get("semantic_status") != "PASS_SUPPORTED_SUBSET"
    ):
        raise ValueError("Consumed export is not a reviewed supported subset")
    for name in PRODUCTS:
        if manifest["files"][name] != hashes[root / name]:
            raise ValueError("Consumed manifest product hashes differ")
    dispositions = tsv_rows(root / "mapping-dispositions.tsv")
    positions = [int(row["source_position"]) for row in dispositions]
    if sorted(positions) != list(range(1, len(positions) + 1)):
        raise ValueError("Consumed dispositions do not form a complete source partition")
    if any(row["disposition"] not in {"SUPPORTED", "WITHHOLD"} for row in dispositions):
        raise ValueError("Unknown consumed disposition")
    by_hash = defaultdict(list)
    for row in dispositions:
        by_hash[row["row_sha256"]].append(row)
    indexed = defaultdict(list)
    counts = {"source": len(dispositions)}
    for disposition, product, count_key in (
        ("SUPPORTED", PRODUCTS[0], "supported"),
        ("WITHHOLD", PRODUCTS[1], "withhold"),
    ):
        _, _, rows = read_sssom(root / product)
        expected_rows = Counter(
            row["row_sha256"] for row in dispositions if row["disposition"] == disposition
        )
        if Counter(row_sha256(row) for row in rows) != expected_rows:
            raise ValueError("Consumed partition rows differ from dispositions")
        counts[count_key] = len(rows)
        for row in rows:
            proof = [
                entry for entry in by_hash[row_sha256(row)] if entry["disposition"] == disposition
            ]
            for entry in proof:
                if any(
                    entry[key] != row[key] for key in ("subject_id", "predicate_id", "object_id")
                ):
                    raise ValueError("Consumed disposition row identity differs")
            labels = [("subject_label", row["subject_label"])]
            labels.extend(
                ("other", token.strip()) for token in row["other"].split("|") if token.strip()
            )
            for field, label in labels:
                indexed[label.casefold()].append(
                    {
                        "matched_field": field,
                        "matched_label": label,
                        "disposition": disposition,
                        "row_sha256": row_sha256(row),
                        "row": row,
                        "review_dispositions": proof,
                    }
                )
    if counts != manifest["counts"]:
        raise ValueError("Consumed partition counts differ from manifest")
    return manifest, dict(indexed), hashes


def record_paths(root: Path) -> list[Path]:
    """Native record surfaces exclude nested historical backups (#1152).

    Directory membership, not Git tracking, is authoritative: an ignored direct
    child is still a current record and must participate in reconciliation.
    """
    return sorted(
        path
        for surface in ("mapped", "unmapped")
        for path in (root / "data/ingredients" / surface).glob("*.yaml")
    )


def load_owners(root: Path, loaded: dict) -> tuple[dict, dict, dict[Path, str]]:
    native = defaultdict(list)
    for row, decision in zip(loaded["rows"], loaded["decisions"], strict=True):
        native[decision["owner_record"]].append({"row": row, "decision": decision})
    owners, index, hashes = {}, defaultdict(list), {}
    for path in record_paths(root):
        content = path.read_bytes()
        record = yaml.safe_load(content)
        name = path.relative_to(root).as_posix()
        hashes[path] = hashlib.sha256(content).hexdigest()
        if path in loaded["input_snapshot"] and hashes[path] != loaded["input_snapshot"][path]:
            raise ValueError(f"Owner changed after native review: {name}")
        owners[name] = {
            "path": name,
            "sha256": hashes[path],
            "subject_id": mim_curie_for_stem(path.stem),
            "preferred_term": record.get("preferred_term", ""),
            "identifier": record.get("identifier", ""),
            "mapping_status": record.get("mapping_status", ""),
            "ontology_mapping": record.get("ontology_mapping"),
            "native_review_rows": native[name],
        }
        label = record.get("preferred_term", "")
        if label:
            index[label.casefold()].append(
                {
                    "owner": name,
                    "kind": "preferred_term",
                    "label": label,
                    "resolving": record.get("mapping_status") != "REJECTED",
                }
            )
        for synonym in record.get("synonyms") or []:
            label = synonym.get("synonym_text", "")
            if label:
                index[label.casefold()].append(
                    {
                        "owner": name,
                        "kind": "synonym",
                        "label": label,
                        "synonym_type": synonym.get("synonym_type", ""),
                        "resolving": record.get("mapping_status") != "REJECTED"
                        and is_resolving_synonym(synonym),
                        "synonym": synonym,
                    }
                )
    return owners, dict(index), hashes


def reconcile(
    candidates: list[dict], owners: dict, index: dict, consumed: dict, holds: dict
) -> tuple[list[dict], dict]:
    ledger = []
    groups = defaultdict(list)
    for item in sorted(
        candidates, key=lambda row: (row["source"], row["source_id"], row["category"])
    ):
        hits, coverage = [], []
        for field in ("source_label", "raw_source_label"):
            label = item[field]
            if not label.strip():
                continue
            hits.extend(
                {"candidate_field": field, **hit} for hit in index.get(label.casefold(), [])
            )
            coverage.extend(
                {"candidate_field": field, **hit} for hit in consumed.get(label.casefold(), [])
            )
        matched_owners = sorted({hit["owner"] for hit in hits})
        resolving = sorted({hit["owner"] for hit in hits if hit["resolving"]})
        downstream = holds.get((item["source"], item["source_id"]), [])
        flags = []
        if not item["source_label"].strip() and not item["raw_source_label"].strip():
            flags.append("BLANK_SOURCE_LABEL")
        if downstream:
            flags.append("DOWNSTREAM_MATERIAL_HOLD")
        if len(resolving) > 1:
            flags.append("AMBIGUOUS_MULTIPLE_OWNERS")
        if hits and not resolving:
            flags.append("NON_RESOLVING_OR_REJECTED_LABEL_ONLY")
        if not hits:
            flags.append("NO_EXACT_CASEFOLD_NAME_MATCH")
        if any(owners[name]["mapping_status"] == "UNMAPPED" for name in resolving):
            flags.append("MATCHED_UNMAPPED_OWNER")
        if any(owners[name]["mapping_status"] == "AMBIGUOUS" for name in resolving):
            flags.append("MATCHED_AMBIGUOUS_OWNER")
        if any(
            entry["decision"]["disposition"] == "WITHHOLD"
            for name in resolving
            for entry in owners[name]["native_review_rows"]
        ):
            flags.append("MATCHED_OWNER_HAS_WITHHELD_MAPPINGS")
        supported = [hit for hit in coverage if hit["disposition"] == "SUPPORTED"]
        if supported:
            flags.append("CONSUMED_SUPPORTED_LEXICAL_COVERAGE")
        elif resolving:
            flags.append("MIM_NAME_NOT_IN_CONSUMED_SUPPORTED_EXPORT")
        ledger.append(
            {
                **item,
                "name_hits": hits,
                "owners": [owners[name] for name in matched_owners],
                "resolving_owner_paths": resolving,
                "consumed_name_hits": coverage,
                "downstream_holds": downstream,
                "triage_flags": flags,
                "scientific_identity_approved_by_reconciliation": False,
            }
        )
        groups[item["source_label"].casefold()].append(
            {
                key: item[key]
                for key in ("candidate_id", "source", "source_id", "category", "source_label")
            }
        )
    summary = {
        "candidate_count": len(ledger),
        "counts_by_source": dict(sorted(Counter(row["source"] for row in ledger).items())),
        "flag_counts": dict(
            sorted(Counter(flag for row in ledger for flag in row["triage_flags"]).items())
        ),
        "flag_counts_are_overlapping": True,
        "flag_counts_by_source": {
            source: dict(
                sorted(
                    Counter(
                        flag
                        for row in ledger
                        if row["source"] == source
                        for flag in row["triage_flags"]
                    ).items()
                )
            )
            for source in sorted({row["source"] for row in ledger})
        },
        "exact_casefold_label_groups": [
            {"casefold_label": label, "members": groups[label]} for label in sorted(groups)
        ],
        "grouping_is_not_identity_merging": True,
        "scientific_approval_added": False,
    }
    return ledger, summary


@contextmanager
def reserve_output_directory(output: Path):
    """Reserve an unaliased destination through retained parent handles (#1155).

    Walk from the filesystem root with O_NOFOLLOW instead of reopening an
    absolute path after a check. A replaced ancestor cannot redirect mkdir or
    publication. The caller must recheck these bindings after reserving files.
    """
    output = Path(os.path.abspath(output))
    flags = os.O_RDONLY | os.O_DIRECTORY | os.O_NOFOLLOW
    with ExitStack() as stack:
        parent_fd = os.open(output.anchor, flags)
        stack.callback(os.close, parent_fd)
        bindings = []

        def verify_bindings():
            for directory_fd, component, identity in bindings:
                try:
                    actual = os.stat(component, dir_fd=directory_fd, follow_symlinks=False)
                except OSError as error:
                    raise ValueError("Output directory binding disappeared") from error
                if (actual.st_dev, actual.st_ino) != identity:
                    raise ValueError("Output directory binding changed")

        for position, component in enumerate(output.parts[1:], 1):
            verify_bindings()
            is_output = position == len(output.parts) - 1
            if is_output:
                # The leaf directory is exclusively ours; never adopt a
                # directory created by another publisher between checks.
                os.mkdir(component, dir_fd=parent_fd)
            else:
                try:
                    os.stat(component, dir_fd=parent_fd, follow_symlinks=False)
                except FileNotFoundError:
                    os.mkdir(component, dir_fd=parent_fd)
            intended = os.stat(component, dir_fd=parent_fd, follow_symlinks=False)
            identity = (intended.st_dev, intended.st_ino)
            try:
                child_fd = os.open(component, flags, dir_fd=parent_fd)
            except OSError as error:
                raise ValueError("Output directory component is aliased or unavailable") from error
            stack.callback(os.close, child_fd)
            actual = os.fstat(child_fd)
            if (actual.st_dev, actual.st_ino) != identity:
                raise ValueError("Output directory changed during acquisition")
            bindings.append((parent_fd, component, identity))
            parent_fd = child_fd
        verify_bindings()
        yield verify_bindings
        verify_bindings()


def run(
    snapshot_root: Path, mim_root: Path, review_path: Path, consumed_root: Path, output: Path
) -> dict:
    snapshot_root, mim_root, consumed_root = (
        snapshot_root.resolve(),
        mim_root.resolve(),
        consumed_root.resolve(),
    )
    manifest, candidates, holds, hashes = load_snapshot(snapshot_root)
    if output.resolve().is_relative_to(Path(manifest["upstream_root"]).resolve()):
        raise ValueError("Output must not write to the upstream checkout")
    if any(output.resolve().is_relative_to(mim_root / name) for name in ("data", "mappings")):
        raise ValueError("Output must not write under maintained MIM data surfaces")
    if output.exists() or any(parent.is_symlink() for parent in [output, *output.parents]):
        raise ValueError("Output must be a new directory without symlink parents")
    consumed_manifest, coverage, consumed_hashes = load_consumed(
        consumed_root, manifest["consumed_reviewed"]
    )
    loaded = load_review(mim_root, review_path)
    owners, index, record_hashes = load_owners(mim_root, loaded)
    ledger, summary = reconcile(candidates, owners, index, coverage, holds)
    hashes.update(consumed_hashes)
    hashes.update(loaded["input_snapshot"])
    hashes.update(record_hashes)
    hashes[Path(__file__).resolve()] = digest(Path(__file__).resolve())
    publisher = Path(ingredient_bundle_refresh.__file__).resolve()
    hashes[publisher] = digest(publisher)

    def verify_inputs():
        for path, expected in hashes.items():
            if digest(path) != expected:
                raise ValueError(f"Input changed during reconciliation: {path}")
        if set(record_hashes) != set(record_paths(mim_root)):
            raise ValueError("MIM record membership changed during reconciliation")

    verify_inputs()
    summary["mim_record_count"] = len(owners)
    summary["native_current_dispositions"] = dict(
        Counter(item["disposition"] for item in loaded["decisions"])
    )
    summary["consumed_partition_counts"] = consumed_manifest["counts"]
    summary["current_source_equals_consumed_source"] = (
        loaded["review"]["source_sha256"] == consumed_manifest["source_sha256"]
    )
    receipt = {
        "schema_version": 1,
        "source_manifest_sha256": digest(snapshot_root / "source-manifest.json"),
        "current_review_sha256": loaded["review_sha256"],
        "consumed_manifest_sha256": digest(consumed_root / "manifest.json"),
        "scientific_review": False,
        "input_hashes": {str(path): value for path, value in sorted(hashes.items())},
        "scope": "Lexical reconciliation only; preserves source IDs, predicates, native dispositions and downstream holds",
    }
    products = {"ledger.json": json_bytes(ledger), "summary.json": json_bytes(summary)}
    stream = io.StringIO(newline="")
    fields = [
        "candidate_id",
        "source",
        "source_id",
        "category",
        "source_label",
        "raw_source_label",
        "occurrences",
        "occurrences_definition",
        "triage_flags",
        "resolving_owner_paths",
    ]
    writer = csv.DictWriter(stream, fieldnames=fields, delimiter="\t", lineterminator="\n")
    writer.writeheader()
    for row in ledger:
        writer.writerow(
            {
                key: (
                    json.dumps(row[key], ensure_ascii=False)
                    if isinstance(row[key], list)
                    else row[key]
                )
                for key in fields
            }
        )
    products["ledger.tsv"] = stream.getvalue().encode()
    receipt["outputs"] = {
        name: hashlib.sha256(content).hexdigest() for name, content in products.items()
    }
    products["receipt.json"] = json_bytes(receipt)
    with reserve_output_directory(output) as verify_destination:

        def verify_publication():
            verify_destination()
            verify_inputs()

        ingredient_bundle_refresh.publish_new_files(
            [(output / name, content) for name, content in products.items()], verify_publication
        )
    return summary


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--kgm-source-snapshot-dir", type=Path, required=True)
    parser.add_argument("--mim-root", type=Path, required=True)
    parser.add_argument("--mim-review-report", type=Path, required=True)
    parser.add_argument("--consumed-reviewed-dir", type=Path, required=True)
    parser.add_argument("--output-dir", type=Path, required=True)
    args = parser.parse_args()
    summary = run(
        args.kgm_source_snapshot_dir,
        args.mim_root,
        args.mim_review_report,
        args.consumed_reviewed_dir,
        args.output_dir,
    )
    print(
        json.dumps(
            {key: value for key, value in summary.items() if key != "exact_casefold_label_groups"},
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
