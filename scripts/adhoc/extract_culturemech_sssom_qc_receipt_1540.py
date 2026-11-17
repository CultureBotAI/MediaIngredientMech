#!/usr/bin/env python3
"""Preserve raw native QC and extract its strict JSON, #1540, 2026-11-17.

Inputs: exact SHA-pinned native stdout and expected supported/withheld row counts.
Outputs: new raw log, unchanged parsed JSON result, and byte-provenance receipt.
No SSSOM, scientific decision, source recipe or accepted intake is changed.
"""

import argparse
import hashlib
import json
from pathlib import Path

from mediaingredientmech.intake import culturemech as native


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, required=True)
    parser.add_argument("--expected-raw-sha256", required=True)
    parser.add_argument("--supported-rows", type=int, required=True)
    parser.add_argument("--withheld-rows", type=int, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    native.output_preflight(args.output, [args.input])
    raw = args.input.read_bytes()
    digest = hashlib.sha256(raw).hexdigest()
    native.require(digest == args.expected_raw_sha256, "Raw QC bytes differ from reviewed pin")
    lines = raw.decode("utf-8").splitlines(keepends=True)
    start = next(index for index, line in enumerate(lines) if line.strip() == "{")
    result = json.loads("".join(lines[start:]))  # Refuses any trailing non-JSON output.
    native.require(result["status"] == "PASS", "Native QC did not pass")
    counts = {
        "ingredient_mappings.sssom.tsv": args.supported_rows,
        "withheld_mappings.sssom.tsv": args.withheld_rows,
    }
    native.require(set(result["partitions"]) == set(counts), "Unexpected native QC partitions")
    for name, count in counts.items():
        part = result["partitions"][name]
        native.require(count >= 0 and part["status"] == "PASS", "Partition QC did not pass")
        native.require(
            all(part[key] == count for key in ("raw_rows", "native_rows", "linkml_rows")),
            "Native QC row counts differ",
        )
    args.output.parent.mkdir(parents=True, exist_ok=True)
    with native.staging(args.output) as stage:
        (stage / "native-qc.log").write_bytes(raw)
        native.write_json(stage / "native-qc.json", result)
        native.require(
            json.loads((stage / "native-qc.json").read_text()) == result, "Parsed result changed"
        )
        native.require((stage / "native-qc.log").read_bytes() == raw, "Raw stdout changed")
        native.require(args.input.read_bytes() == raw, "Source QC changed during extraction")
        native.write_json(
            stage / "serialization-receipt.json",
            {
                "status": "PRESERVED_RAW_AND_STRICT_NATIVE_QC_RESULT",
                "issue": 1540,
                "raw_stdout": native.fingerprint(stage / "native-qc.log"),
                "strict_json": native.fingerprint(stage / "native-qc.json"),
                "preserved_prefix_lines": start,
                "partition_counts": counts,
                "helper_sha256": native.fingerprint(Path(__file__))["sha256"],
                "scope": "Serialization repair only; exact native result object and all diagnostic stdout bytes preserved.",
            },
        )
    print(json.dumps(native.fingerprint(args.output / "serialization-receipt.json")))


if __name__ == "__main__":
    main()
