"""Portable #1265 owner-address projection of the fixed historical cohort.

Replays the original decisions against their original bytes first. Only owner
addresses and the hashes that depend on those addresses are projected; scientific
payloads, evidence, negative dispositions and xref eligibility remain unchanged.
"""

from __future__ import annotations

from copy import deepcopy

from mediaingredientmech import identity_projection_inventory as inventory
from mediaingredientmech.identity_projection import (
    BASE_COMMIT,
    LIFECYCLE,
    MANIFEST,
    MAPPING_REVIEW,
    REGISTRY,
    REPORT_ROOT,
    Proof,
    document,
    encode,
    exact,
    git_files,
    projection_header,
    require,
    safe_path,
    sha,
    verify_record_transition,
)
from mediaingredientmech.stable_ids import MIM_PREFIX, parse_registry

OLD_REVIEW = "reports/owned_name_deferred_669_20261103/companion-review.json"
OLD_REVIEW_SHA = "ba15d43306f33972d7abcd67185e5bf571f2224f00e757c2603e017a895ac815"
REVIEW = REPORT_ROOT + "/companion-review.json"
ARCHIVE = REPORT_ROOT + "/historical-companion/"


def declared_sources(review: dict) -> dict[str, str]:
    declared: dict[str, str] = {}
    for group in ("inputs", "record_inputs"):
        for name, digest in review[group].items():
            require(name not in declared or declared[name] == digest, "conflicting companion input")
            declared[name] = digest
    for path, digest in (
        (review["claims_file"], review["claims_sha256"]),
        (review["base_review"], review["base_review_sha256"]),
    ):
        require(
            path not in declared or declared[path] == digest, "conflicting companion control input"
        )
        declared[path] = digest
    return declared


def products(proof: Proof, mapping_outputs: dict[str, bytes]) -> dict[str, bytes]:
    original_raw = git_files(proof.root, [OLD_REVIEW])[OLD_REVIEW]
    require(sha(original_raw) == OLD_REVIEW_SHA, "historical companion authority differs")
    original = document(original_raw)
    historical = git_files(proof.root, list(declared_sources(original)))
    historical[OLD_REVIEW] = original_raw
    outputs = {ARCHIVE + name: raw for name, raw in historical.items()}
    outputs.update(inventory.products(proof))
    for name, raw in historical.items():
        if name.startswith("reports/"):
            require(
                safe_path(proof.root, name).read_bytes() == raw,
                "historical companion report changed",
            )
            proof.snapshots[name] = raw
    inputs = {name: sha(raw) for name, raw in outputs.items()}
    for name in (MANIFEST, REGISTRY, LIFECYCLE):
        inputs[name] = sha(proof.snapshots[name])
    inputs[MAPPING_REVIEW] = sha(mapping_outputs[MAPPING_REVIEW])
    # Keep the public exporter controls explicit. claims_file is the archived,
    # original claim document; no newly stamped scientific claim is invented.
    review = {
        "schema_version": 1,
        "identity_projection": projection_header(proof, OLD_REVIEW, original_raw),
        "historical_review": ARCHIVE + OLD_REVIEW,
        "base_review": MAPPING_REVIEW,
        "base_review_sha256": inputs[MAPPING_REVIEW],
        "claims_file": ARCHIVE + original["claims_file"],
        "claims_sha256": original["claims_sha256"],
        "inputs": dict(sorted(inputs.items())),
        "record_inputs": {name: sha(proof.after[name]) for name in original["record_inputs"]},
    }
    sources = {
        **outputs,
        **{name: proof.snapshots[name] for name in (MANIFEST, REGISTRY, LIFECYCLE)},
        MAPPING_REVIEW: mapping_outputs[MAPPING_REVIEW],
        **{name: proof.after[name] for name in original["record_inputs"]},
    }
    projected_products(review, sources)
    outputs[REVIEW] = encode(review)
    proof.recheck()
    return outputs


def projected_products(review: dict, sources: dict[str, bytes]) -> tuple[dict[str, bytes], dict]:
    """Portable replay; accepts only the pinned original #1265 cohort authority."""
    from mediaingredientmech.ingredient_bundle_contract import (
        ARTIFACTS,
        annotation_id,
        annotation_table,
        canonical_json,
        reviewed_products,
    )
    from mediaingredientmech.mapping_scope import read_profile_table, write_profile_table

    require(
        set(review)
        == {
            "schema_version",
            "identity_projection",
            "historical_review",
            "base_review",
            "base_review_sha256",
            "claims_file",
            "claims_sha256",
            "inputs",
            "record_inputs",
        },
        "unexpected projected companion fields",
    )
    require(
        type(review["schema_version"]) is int and review["schema_version"] == 1,
        "unsupported projected companion version",
    )
    declared = declared_sources(review)
    require(set(sources) == set(declared), "projected companion source inventory differs")
    require(
        all(sha(sources[name]) == digest for name, digest in declared.items()),
        "projected companion source hash differs",
    )
    require(
        review["historical_review"] == ARCHIVE + OLD_REVIEW
        and sha(sources[ARCHIVE + OLD_REVIEW]) == OLD_REVIEW_SHA,
        "companion authority is not the fixed historical review",
    )
    original_raw = sources[ARCHIVE + OLD_REVIEW]
    original = document(original_raw)
    original_declared = declared_sources(original)
    historical = {name: sources[ARCHIVE + name] for name in original_declared}
    archived = {name for name in sources if name.startswith(ARCHIVE)}
    require(
        archived == {ARCHIVE + name for name in {*original_declared, OLD_REVIEW}},
        "historical companion archive differs",
    )
    old_artifacts, loaded = reviewed_products(original, historical)
    require(
        set(sources)
        == archived
        | {MANIFEST, REGISTRY, LIFECYCLE, MAPPING_REVIEW, inventory.INVENTORY}
        | set(original["record_inputs"]),
        "unexpected projected companion source",
    )
    manifest = document(sources[MANIFEST])
    header = review["identity_projection"]
    require(
        exact(
            header,
            {
                "kind": "mim-inherited-identity-projection/v1",
                "manifest": MANIFEST,
                "manifest_sha256": sha(sources[MANIFEST]),
                "source_commit": BASE_COMMIT,
                "original_report": OLD_REVIEW,
                "original_report_sha256": OLD_REVIEW_SHA,
                "scientific_approval_added": False,
            },
        ),
        "companion projection authority differs",
    )
    require(
        manifest["source_commit"] == BASE_COMMIT
        and manifest["approval"] == "NONE"
        and manifest["scientific_approval_added"] is False
        and manifest["registry_path"] == REGISTRY
        and manifest["lifecycle_path"] == LIFECYCLE
        and sha(sources[REGISTRY]) == manifest["registry_sha256"]
        and sha(sources[LIFECYCLE]) == manifest["lifecycle_sha256"],
        "companion migration differs",
    )
    registry = parse_registry(sources[REGISTRY], sources[LIFECYCLE])
    inventory.validate(sources[inventory.INVENTORY], manifest, registry)
    entries = manifest["records"]
    require(
        len(entries) == len(registry.entries)
        and not registry.events
        and [entry["path"] for entry in entries] == sorted({entry["path"] for entry in entries}),
        "companion mint inventory differs",
    )
    indexed = {
        entry["path"]: (entry, mint, index)
        for index, (entry, mint) in enumerate(zip(entries, registry.entries, strict=True), 1)
    }
    require(
        set(review["record_inputs"]) == set(original["record_inputs"]),
        "companion owner scope changed",
    )
    aliases = {}
    for old_id, owner in loaded["owners"].items():
        entry, mint, index = indexed[owner]
        require(
            sha(historical[owner]) == original["record_inputs"][owner],
            "companion prior owner differs",
        )
        _, new = verify_record_transition(
            entry, historical[owner], sources[owner], manifest, mint, index
        )
        aliases[old_id] = new["mim_id"]
    require(
        review["base_review"] == MAPPING_REVIEW
        and review["claims_file"] == ARCHIVE + original["claims_file"]
        and review["claims_sha256"] == original["claims_sha256"],
        "companion control path differs",
    )
    # The native exporter independently validates the complete projected mapping
    # review. Portable scientific authority remains the exact original cohort.
    base = document(sources[MAPPING_REVIEW])
    require(
        base.get("identity_projection", {}).get("manifest_sha256") == sha(sources[MANIFEST])
        and base["identity_projection"].get("scientific_approval_added") is False,
        "companion base projection differs",
    )
    projected = deepcopy(loaded)
    projected["metadata"]["curie_map"]["MIM"] = MIM_PREFIX
    projected["owners"] = {aliases[key]: value for key, value in loaded["owners"].items()}
    projected["identities"] = {aliases[key]: value for key, value in loaded["identities"].items()}
    for row in projected["mappings"]:
        row["subject_id"] = aliases[row["subject_id"]]
    for row in projected["identifiers"]:
        if row["owner_id"] in aliases:
            row["owner_id"] = aliases[row["owner_id"]]
            row["annotation_id"] = annotation_id(row)
    for group in ("products", "occurrences"):
        for row in projected[group]:
            row["ingredient_id"] = aliases[row["ingredient_id"]]
    projected["mappings"].sort(
        key=lambda row: (row["subject_id"], row["predicate_id"], row["object_id"])
    )
    _, fields, _ = read_profile_table(old_artifacts[ARTIFACTS["mappings"]])
    artifacts = {
        ARTIFACTS["mappings"]: write_profile_table(
            projected["metadata"], fields, projected["mappings"]
        ),
        ARTIFACTS["identifiers"]: annotation_table(projected["identifiers"]),
    }
    for group in ("products", "occurrences"):
        if projected[group]:
            artifacts[ARTIFACTS[group]] = canonical_json(projected[group]) + b"\n"
    return artifacts, projected
