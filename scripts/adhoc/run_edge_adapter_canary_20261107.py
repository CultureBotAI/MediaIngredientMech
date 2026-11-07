"""Publish bounded or full pinned MIM assertions for CLAW #767, 2026-11-07.

Inputs: immutable native archive/bundle paths and SHA256 pins, explicit positions.
Outputs: atomic new assertions.jsonl and a manifest with verified persisted counters.
The same launcher publishes the canary and, after its approval, the full export.
"""

from __future__ import annotations

import argparse
from collections import Counter
import hashlib
import json
from pathlib import Path
import tempfile

from kg_microbe_curation.identity import canonical_json
from kg_microbe_curation.native import validate_native_assertion
from mediaingredientmech.export.edge_curation import build_native_assertions
from mediaingredientmech.export import edge_curation
from mediaingredientmech.edge_publication import publish_stage


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--archive", type=Path, required=True)
    parser.add_argument("--bundle", type=Path, required=True)
    parser.add_argument("--source-commit", required=True)
    parser.add_argument("--archive-sha256", required=True)
    parser.add_argument("--manifest-sha256", required=True)
    parser.add_argument("--review-path", default="reports/sssom_completion_20260921/review.json")
    selection = parser.add_mutually_exclusive_group(required=True)
    selection.add_argument("--positions", type=int, nargs="+")
    selection.add_argument("--all", action="store_true")
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    if args.output.exists() or args.output.is_symlink():
        raise ValueError("Refusing to replace an existing export destination")
    assertions = build_native_assertions(
        archive=args.archive,
        bundle=args.bundle,
        source_commit=args.source_commit,
        archive_sha256=args.archive_sha256,
        manifest_sha256=args.manifest_sha256,
        review_path=args.review_path,
        positions=tuple(args.positions) if args.positions else None,
    )
    content = b"".join(canonical_json(assertion) + b"\n" for assertion in assertions)
    counts = dict(Counter(item["native_review"]["status"] for item in assertions))
    manifest = {
        "schema_version": 1,
        "contract": assertions[0]["contract"],
        "source_commit": args.source_commit,
        "source_archive_sha256": args.archive_sha256,
        "native_bundle_manifest_sha256": args.manifest_sha256,
        "adapter_sha256": hashlib.sha256(Path(edge_curation.__file__).read_bytes()).hexdigest(),
        "source_positions": args.positions,
        "rows": len(assertions),
        "native_status_counts": counts,
        "assertions_sha256": hashlib.sha256(content).hexdigest(),
        "assertions_bytes": len(content),
        "independent_scientific_reviews": 0,
        "kg_occurrences_approved": 0,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(
        prefix=".mim-native-stage-", dir=args.output.parent
    ) as temporary:
        stage = Path(temporary) / "export"
        stage.mkdir()
        (stage / "assertions.jsonl").write_bytes(content)
        (stage / "manifest.json").write_text(json.dumps(manifest, indent=2, sort_keys=True) + "\n")
        persisted = [
            json.loads(line) for line in (stage / "assertions.jsonl").read_bytes().splitlines()
        ]
        for assertion in persisted:
            validate_native_assertion(assertion)
        if persisted != assertions or len(persisted) != manifest["rows"] or not content:
            raise ValueError("Persisted native assertion verification failed")
        publish_stage(stage, args.output)
    if (args.output / "assertions.jsonl").read_bytes() != content:
        raise ValueError("Published native assertion verification failed")
    print(json.dumps({"output": str(args.output), **manifest}, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
