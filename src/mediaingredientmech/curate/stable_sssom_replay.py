"""Deterministic c1 native generation replay, without provider calls (#1339).

A fresh child compiles the captured native entrypoint and its own private local
producer graph. The recorded label resolution is an explicit replay input, not
new ontology verification. This adapter neither edits the producer nor invokes
its provider loaders, publication writer, lock manager or source-binding path.
"""

from __future__ import annotations

import base64
import hashlib
import json
import sys
import tempfile
import types
from contextlib import redirect_stdout
from pathlib import Path
from typing import Any


def digest(raw):
    return None if raw is None else hashlib.sha256(raw).hexdigest()


def encoded(value):
    return (json.dumps(value, indent=2, sort_keys=True, ensure_ascii=False) + "\n").encode()


def replay(request):
    root, claw = Path(request["root"]), Path(request["claw"])
    snapshot = {
        Path(path): None if raw is None else base64.b64decode(raw, validate=True)
        for path, raw in request["inputs"].items()
    }
    entry = claw / "scripts/build_mim_ingredient_sssom.py"
    native: Any = types.ModuleType("_stable_sssom_native_replay")
    native.__file__ = str(entry)
    sys.modules[native.__name__] = native
    entry_bytes = snapshot[entry]
    if entry_bytes is None:
        raise ValueError("native generation replay lacks its captured entrypoint")
    exec(compile(entry_bytes, str(entry), "exec", dont_inherit=True), native.__dict__)
    native._check_producer_bindings()
    if native.MIM_ROOT != root or native.KGM_ROOT != Path(request["kg_microbe"]):
        raise ValueError("native generation replay roots differ")
    if any(snapshot.get(path) != raw for path, raw in native._IMPORTED_PRODUCER_BYTES.items()):
        raise ValueError("native generation replay captured producer bytes differ")
    directories = (root / "data/ingredients/mapped", root / "data/ingredients/unmapped")
    registry = root / "data/ids/mim_id_registry.tsv"
    lifecycle = root / "data/ids/mim_id_lifecycle.tsv"
    contract = root / "src/mediaingredientmech/stable_ids.py"
    expected = {
        *(p for directory in directories for p in directory.glob("*.yaml")),
        *native._producer_paths(),
        registry,
        lifecycle,
        contract,
        native.RESIDUAL_JSON,
        native.KGM_UNIFIED_TSV,
        native.MIM_PUBLISHED_SSSOM,
    }
    if set(snapshot) != expected:
        raise ValueError("complete native generation input membership differs")
    records = {
        path: record
        for directory in directories
        for path, record in native._read_mapped_records(
            directory, snapshot, strict_identity=True
        ).items()
    }
    subjects, index, prefix = native._STABLE_PRODUCER.identity_snapshot(
        root,
        records,
        snapshot[registry],
        snapshot[lifecycle],
        snapshot[contract],
        contract,
        digest(snapshot[contract]),
    )
    compatibility = native._STABLE_PRODUCER.compatibility_registry_objects(
        records, subjects, index, snapshot[native.MIM_PUBLISHED_SSSOM] or b""
    )
    owners = native.build_owner_index({subjects[p]: record for p, record in records.items()})
    residual_raw = snapshot[native.RESIDUAL_JSON]
    residual = (
        {
            decision["source_file"]: decision
            for decision in json.loads(residual_raw).get("decisions", [])
        }
        if residual_raw is not None
        else {}
    )
    labels = request["canonical_label_resolution"]
    if not isinstance(labels, dict) or not all(
        isinstance(key, str) and isinstance(value, str) for key, value in labels.items()
    ):
        raise ValueError("native generation replay requires recorded label-resolution inputs")
    with tempfile.TemporaryDirectory(prefix="mim-stable-native-replay-") as temporary:
        stage = Path(temporary)
        kg_raw = snapshot[native.KGM_UNIFIED_TSV]
        if kg_raw is None:
            kg_sources, kg_labels = {}, {}
        else:
            kg_file = stage / "kg-input.tsv.gz"
            kg_file.write_bytes(kg_raw)
            kg_sources = native.load_kgm_source_index(kg_file)
            kg_labels = native.load_kgm_labels(kg_file)
        rows: list[dict] = []
        suppressions: list[Any] = []
        for path, record in records.items():
            rows.extend(
                native._row_from_yaml(
                    path,
                    residual,
                    kg_sources,
                    kg_labels,
                    labels,
                    record=record,
                    owners=owners,
                    suppressions=suppressions,
                    stable_subject=subjects[path],
                    registry_objects=compatibility.get(subjects[path], ()),
                )
            )
        # Same native ordering and subject/object dedup as _build_candidate.
        unique = {(row["subject_id"], row["object_id"]): row for row in rows}
        final = list(unique.values())
        if not final:
            raise ValueError(
                "native generation replay requires the separate source-binding empty path"
            )
        tsv = stage / "candidate.sssom.tsv"
        native._write_sssom(final, tsv, mim_prefix=prefix)
        candidate = tsv.read_bytes()
    sidecar = native.render_suppressed_aliases(suppressions)
    manifest = {
        "scope": "diagnostic candidate; not canonical promotion or scientific approval",
        "identity_mode": "stable",
        "stable_id_contract_sha256": digest(snapshot[contract]),
        "source_binding_candidate": None,
        "source_binding_native_producers": [],
        "owner_subjects": {str(path): subject for path, subject in subjects.items()},
        "owner_candidate_accounting": [
            {
                "path": str(path),
                "subject_id": subject,
                "mapping_status": records[path].get("mapping_status"),
                "external_candidate_rows": sum(row["subject_id"] == subject for row in final),
                "scientific_approval_added": False,
            }
            for path, subject in subjects.items()
        ],
        "registry_compatibility_objects": compatibility,
        "validation_replay": "disabled: fresh science requires fresh review; prior artifacts remain inputs",
        "external_sssom_validation": "passed",
        "prior_stamp_sources": [],
        "source_inputs": [
            {"path": str(path), "sha256": digest(raw)} for path, raw in sorted(snapshot.items())
        ],
        "producer_import_snapshot": {
            str(path): digest(raw) for path, raw in native._IMPORTED_PRODUCER_BYTES.items()
        },
        "producer_binding_scope": "source entrypoint plus captured local dependency graph; "
        "trusted caller/interpreter, not cryptographic runtime attestation",
        "mapped_record_paths": [str(path) for path in records],
        "source_revisions": request["source_revisions"],
        "canonical_label_resolution": dict(sorted(labels.items())),
        "policy_evidence": list(native.OWNED_NAME_EVIDENCE),
        "emitted_rows": len(final),
        "schema_version": 1,
        "policy_version": native._ARTIFACT_PRODUCER.POLICY_VERSION,
        "artifacts": [
            {"role": role, "path": request["outputs"][name], "sha256": digest(raw)}
            for role, name, raw in (
                ("sssom", "sssom", candidate),
                ("suppressed_aliases", "suppressions", sidecar),
            )
        ],
    }
    native._check_producer_bindings()
    return {
        name: base64.b64encode(raw).decode("ascii")
        for name, raw in (
            ("sssom", candidate),
            ("suppressions", sidecar),
            ("manifest", encoded(manifest)),
        )
    }


if __name__ == "__main__":
    # #1342: c1 deliberately prints Rule F and other native diagnostics on
    # stdout. Preserve them on stderr; reserve stdout for the JSON transport.
    # The original native invocation logs remain immutable generation inputs.
    with redirect_stdout(sys.stderr):
        result = replay(json.load(sys.stdin))
    sys.stdout.write(json.dumps(result, sort_keys=True))
