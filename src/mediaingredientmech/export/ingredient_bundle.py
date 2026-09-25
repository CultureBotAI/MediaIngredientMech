"""Publish an immutable ingredient-scope bundle after replaying existing reviews."""

from __future__ import annotations

import argparse
import shutil
import tempfile
from pathlib import Path

from mediaingredientmech.export.reviewed_sssom import load_review
from mediaingredientmech.ingredient_bundle_contract import (
    ARTIFACTS,
    BUNDLE_VERSION,
    PROFILE_NAME,
    REQUIRED_CAPABILITIES,
    SCHEMA_NAME,
    canonical_json,
    content_sha256,
    contract_resource,
    read_json,
    reviewed_products,
    safe_member,
    validate_bundle,
)


def export_bundle(root: Path, review_path: Path, output: Path) -> dict:
    """Validate current owners/reviews and publish a new directory atomically.

    The manifest hash is the release pin. Rebuilding the same reviewed inputs
    yields identical bytes; neither a clock value nor a mutable branch is an ID.
    """
    root = root.resolve()
    if output.exists():
        raise ValueError("Ingredient bundle releases are immutable; choose a new output directory")
    review_path = (
        review_path if review_path.is_absolute() else safe_member(root, review_path.as_posix())
    )
    review_bytes = review_path.read_bytes()
    review = read_json(review_bytes)
    # Reuse the full existing mapping review, not a checksum-only subset approval.
    base = load_review(root, Path(review["base_review"]))
    if base["review_sha256"] != review["base_review_sha256"]:
        raise ValueError("Companion review refers to a stale original mapping review")
    names = {
        review["claims_file"],
        review["base_review"],
        *review["inputs"],
        *review["record_inputs"],
    }
    sources = {name: safe_member(root, name).read_bytes() for name in names}
    artifacts, loaded = reviewed_products(review, sources)
    members = {
        PROFILE_NAME: contract_resource(PROFILE_NAME),
        SCHEMA_NAME: contract_resource(SCHEMA_NAME),
        "review.json": review_bytes,
        **artifacts,
        **{"sources/" + name: value for name, value in sources.items()},
    }
    required = set(REQUIRED_CAPABILITIES)
    if loaded["products"]:
        required.add("catalog-products-v1")
    if loaded["occurrences"]:
        required.add("ingredient-occurrences-v1")
    manifest = {
        "schema_version": BUNDLE_VERSION,
        "cohort": sorted(loaded["owners"]),
        "coverage": "reviewed_scoped_cohort",
        "legacy_compatibility": "separate_explicit_input_only",
        "required_capabilities": sorted(required),
        "review": "review.json",
        "source_root": "sources",
        "artifacts": {key: name if name in artifacts else None for key, name in ARTIFACTS.items()},
        "provenance": {
            "review_sha256": content_sha256(review_bytes),
            "base_review_sha256": review["base_review_sha256"],
            "exporter": "mediaingredientmech.export.ingredient_bundle",
            "exporter_sha256": content_sha256(Path(__file__).read_bytes()),
            "validator_sha256": content_sha256(
                Path(__file__).parents[1].joinpath("ingredient_bundle_contract.py").read_bytes()
            ),
        },
        "members": {
            name: {"sha256": content_sha256(value), "bytes": len(value)}
            for name, value in sorted(members.items())
        },
    }
    output.parent.mkdir(parents=True, exist_ok=True)
    temporary = Path(tempfile.mkdtemp(prefix=".ingredient-bundle-", dir=output.parent))
    try:
        for name, value in members.items():
            path = safe_member(temporary, name)
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_bytes(value)
        (temporary / "manifest.json").write_bytes(canonical_json(manifest) + b"\n")
        result = validate_bundle(temporary)
        snapshots = {
            safe_member(root, name): content_sha256(value) for name, value in sources.items()
        }
        snapshots.update(base["input_snapshot"])
        snapshots[review_path] = content_sha256(review_bytes)
        if any(
            content_sha256(path.read_bytes()) != expected for path, expected in snapshots.items()
        ):
            raise ValueError("Input changed during ingredient bundle export")
        if output.exists():
            raise ValueError("Ingredient bundle output appeared during export")
        temporary.rename(output)
        return {
            "manifest_sha256": result["fingerprint"],
            "mappings": len(loaded["mappings"]),
            "identifiers": len(loaded["identifiers"]),
            "products": len(loaded["products"]),
            "occurrences": len(loaded["occurrences"]),
        }
    finally:
        if temporary.exists():
            shutil.rmtree(temporary)


def main() -> None:
    """Export or independently validate the explicitly selected reviewed cohort."""
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="command", required=True)
    export = commands.add_parser("export")
    export.add_argument("--root", type=Path, default=Path.cwd())
    export.add_argument("--review", type=Path, required=True)
    export.add_argument("--output", type=Path, required=True)
    validate = commands.add_parser("validate")
    validate.add_argument("bundle", type=Path)
    validate.add_argument("--manifest-sha256", required=True)
    args = parser.parse_args()
    if args.command == "export":
        result = export_bundle(args.root, args.review, args.output)
    else:
        loaded = validate_bundle(args.bundle, expected_manifest_sha256=args.manifest_sha256)
        result = {"manifest_sha256": loaded["fingerprint"], "status": "PASS"}
    print(canonical_json(result).decode())


if __name__ == "__main__":
    main()
