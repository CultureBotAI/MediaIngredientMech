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
import shutil
import tempfile
from collections import defaultdict
from pathlib import Path

import yaml

from mediaingredientmech.curie import mim_curie_for_stem
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
        subjects[mim_curie_for_stem(path.stem)].add(owner)
    owners = []
    for row in rows:
        by_label = labels[row["subject_label"]]
        by_subject = subjects[row["subject_id"]]
        candidates = by_label & by_subject
        if not row["subject_id"].startswith("MIM:") or len(candidates) != 1:
            raise ValueError(f"No unique independent owner for {row['subject_id']}")
        owners.append(next(iter(candidates)))
    return owners, records


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


def load_review(root: Path, review_path: Path) -> dict:
    root = root.resolve()
    review_path = review_path if review_path.is_absolute() else root / review_path
    review_bytes = review_path.read_bytes()
    review_sha = hashlib.sha256(review_bytes).hexdigest()
    snapshots = {review_path: review_sha}
    review = _json_bytes(review_bytes, str(review_path))
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
    indexed, proofs = {}, {}
    for decision in decisions:
        position = decision.get("source_position")
        if type(position) is not int or not 1 <= position <= len(rows) or position in indexed:
            raise ValueError("Invalid/duplicate review source position")
        row, owner = rows[position - 1], owners[position - 1]
        if decision.get("row_sha256") != row_sha256(row) or decision.get("owner_record") != owner:
            raise ValueError("Review row payload or owner does not match source")
        if decision.get("disposition") not in {"SUPPORTED", "WITHHOLD"}:
            raise ValueError("Invalid scientific disposition")
        if (
            not isinstance(decision.get("review_reason"), str)
            or not decision["review_reason"].strip()
        ):
            raise ValueError("Missing scientific review reason")
        evidence, key = decision.get("review_evidence"), decision.get("evidence_key")
        if evidence not in review["inputs"] or not isinstance(key, str) or not key.strip():
            raise ValueError("Missing hash-bound evidence reference")
        if evidence not in proofs:
            proofs[evidence] = _json_bytes(verified[evidence], evidence)
        entry = proofs[evidence].get("entries", {}).get(key)
        expected = {
            field: decision[field] for field in ("row_sha256", "disposition", "review_reason")
        }
        expected["owner_record_sha256"] = review["record_inputs"][owner]
        if not isinstance(entry, dict) or any(
            entry.get(field) != value for field, value in expected.items()
        ):
            raise ValueError("Scientific decision disagrees with exact evidence entry")
        if decision["disposition"] == "SUPPORTED":
            _safe_synonyms(row, records[owner])
        indexed[position] = decision
    selected = [
        rows[i - 1] for i, decision in indexed.items() if decision["disposition"] == "SUPPORTED"
    ]
    identities = {
        (row["subject_id"], row["object_id"])
        for row in selected
        if row["predicate_id"] == "skos:exactMatch"
    }
    for row in selected:
        if row["predicate_id"] in {"skos:broadMatch", "skos:narrowMatch"}:
            slug = row["subject_id"].removeprefix("MIM:").lower()
            if not any(
                (row["subject_id"], f"kgmicrobe.{kind}:{slug}") in identities
                for kind in ("ingredient", "compound")
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
    }
    _check_snapshot(loaded)
    return loaded


def _check_snapshot(loaded: dict) -> None:
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
        metadata = dict(loaded["metadata"])
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
