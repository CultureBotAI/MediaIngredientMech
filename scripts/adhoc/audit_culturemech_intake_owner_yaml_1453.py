#!/usr/bin/env python3
"""Audit pinned MIM owner YAML for duplicate mapping keys, #1453, 2026-11-17.

Inputs: exact prepared intake manifest pin and its named current owner bytes.
Output: new JSON audit; no owner edits, source regeneration or network calls.
Merge-expanded duplicate keys are reported too, with no assumed intent.
"""

import argparse
import hashlib
import json
from pathlib import Path

import yaml

from mediaingredientmech.intake import culturemech as intake

ROOT = Path(__file__).resolve().parents[2]


class UniqueKeyLoader(yaml.CSafeLoader):
    pass


def unique_mapping(loader, node, deep=False):
    loader.flatten_mapping(node)
    result = {}
    for key_node, value_node in node.value:
        key = loader.construct_object(key_node, deep=deep)
        if key in result:
            raise ValueError(f"Repeated mapping key {key!r} at line {key_node.start_mark.line + 1}")
        result[key] = loader.construct_object(value_node, deep=deep)
    return result


UniqueKeyLoader.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, unique_mapping)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--intake", type=Path, required=True)
    parser.add_argument("--expected-intake-sha256", required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    manifest, _ = intake.read_json(args.intake / "intake.json", args.expected_intake_sha256)
    findings = []
    for name, expected in manifest["mim_record_inputs"].items():
        raw = intake.relative(ROOT, name).read_bytes()
        if {"sha256": hashlib.sha256(raw).hexdigest(), "bytes": len(raw)} != expected:
            raise ValueError("Pinned owner changed: " + name)
        try:
            yaml.load(raw, Loader=UniqueKeyLoader)
        except (ValueError, yaml.YAMLError) as exc:
            findings.append({"path": name, "error": str(exc)})
    intake.check_snapshot(ROOT, manifest["mim_record_inputs"])
    intake.read_json(args.intake / "intake.json", args.expected_intake_sha256)
    result = {
        "status": "OWNERS_UNAMBIGUOUS" if not findings else "AMBIGUOUS_OWNER_YAML",
        "intake_sha256": args.expected_intake_sha256,
        "owner_files": len(manifest["mim_record_inputs"]),
        "findings": findings,
        "helper_sha256": intake.fingerprint(Path(__file__))["sha256"],
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    intake.write_json(args.output, result)
    print(json.dumps(result))


if __name__ == "__main__":
    main()
