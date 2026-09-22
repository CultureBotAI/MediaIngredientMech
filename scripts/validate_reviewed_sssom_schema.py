"""Native SSSOM schema gate with loss detection for both reviewed partitions (#730).

The native parser can drop malformed rows while returning an empty, schema-valid
mapping set. Row counts and ordered mapping identities must survive parsing.
Extension-column normalization is permitted here: the independent reviewed
exporter checks every output byte against its evidence-derived expectation.
"""

from __future__ import annotations

import argparse
import csv
import io
import json
from decimal import Decimal, InvalidOperation
from pathlib import Path

from sssom.parsers import parse_sssom_table, to_mapping_set_document
from sssom.validators import validate_json_schema

IDENTITY_FIELDS = ("subject_id", "predicate_id", "object_id", "subject_label", "object_label")
PARTITIONS = (
    ("ingredient_mappings.sssom.tsv", "supported"),
    ("withheld_mappings.sssom.tsv", "withhold"),
)


def _confidence(value) -> Decimal | None:
    if value is None or str(value).strip() == "":
        return None
    try:
        result = Decimal(str(value))
    except InvalidOperation as exc:
        raise ValueError(f"Nonnumeric confidence: {value!r}") from exc
    if not result.is_finite():
        raise ValueError(f"Nonfinite confidence: {value!r}")
    return result


def validate_native(output: Path) -> dict:
    manifest = json.loads((output / "manifest.json").read_text())
    results = {}
    for filename, key in PARTITIONS:
        path = output / filename
        text = "".join(
            line for line in path.read_text().splitlines(keepends=True) if not line.startswith("#")
        )
        raw = list(csv.DictReader(io.StringIO(text), delimiter="\t", strict=True))
        if any(None in row or any(value is None for value in row.values()) for row in raw):
            raise ValueError(f"Malformed raw TSV row: {filename}")
        if manifest["counts"][key] != len(raw):
            raise ValueError(f"Raw TSV/manifest row count differs: {filename}")
        native = parse_sssom_table(path, strict=True)
        if len(native.df) != len(raw):
            raise ValueError(
                f"Native parser dropped or added rows: {filename}: raw={len(raw)} native={len(native.df)}"
            )
        for position, (original, parsed) in enumerate(
            zip(raw, native.df.to_dict("records"), strict=True), 1
        ):
            if any(
                str(parsed.get(field, "")) != original.get(field, "") for field in IDENTITY_FIELDS
            ):
                raise ValueError(
                    f"Native parser changed ordered mapping identity: {filename}:{position}"
                )
            raw_confidence = original.get("confidence", "")
            parsed_confidence = parsed.get("confidence", "")
            # An absent optional value may become pandas NaN. It is not a numeric assertion.
            if not str(raw_confidence).strip() and str(parsed_confidence).lower() in {
                "nan",
                "none",
                "",
            }:
                parsed_confidence = ""
            if _confidence(raw_confidence) != _confidence(parsed_confidence):
                raise ValueError(f"Native parser changed confidence: {filename}:{position}")
        document = to_mapping_set_document(native)
        if len(document.mapping_set.mappings or []) != len(raw):
            raise ValueError(f"Native LinkML conversion dropped rows: {filename}")
        validate_json_schema(native, fail_on_error=True)
        results[filename] = {
            "raw_rows": len(raw),
            "native_rows": len(native.df),
            "linkml_rows": len(document.mapping_set.mappings or []),
            "status": "PASS",
        }
    if sum(result["raw_rows"] for result in results.values()) != manifest["counts"]["source"]:
        raise ValueError("Partition counts do not reconcile to the source count")
    return {
        "status": "PASS",
        "scope": "Native SSSOM parsing and LinkML schema; exact row count, ordered identifiers/labels, and numeric confidence preserved. Other extension-field normalization is permitted; reviewed exporter independently verifies complete output bytes.",
        "partitions": results,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("output", type=Path)
    args = parser.parse_args()
    print(json.dumps(validate_native(args.output), sort_keys=True, indent=2))


if __name__ == "__main__":
    main()
