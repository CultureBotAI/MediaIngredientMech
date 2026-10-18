#!/usr/bin/env python3
"""Validate CAS Registry Number check digits across SSSOM releases and YAML records (#753).

CAS Registry Numbers have the format `digits-two_digits-check_digit` where:
  check_digit == sum(int(d) * (i + 1) for i, d in enumerate(reversed(digits_before_last))) % 10

By default, validates:
1. Published SSSOM release (`output/mim-reviewed-sssom/ingredient_mappings.supported.sssom.tsv`):
   any invalid CAS check digit in `object_id` (`cas:...`) or `other` (`CAS:...`) is a
   hard error (`--check` exits 2).
2. Source YAML records (`data/ingredients/mapped/*.yaml`, `data/ingredients/unmapped/*.yaml`):
   reports any invalid CAS check digits in `identifier` (`cas:...`) or
   `chemical_properties.cas_rn`, noting whether the record is already withheld from the
   supported release by `mappings/reviews/kgmicrobe-followup.json`.
"""

from __future__ import annotations

import argparse
import csv
import json
import re
import sys
from pathlib import Path

import yaml

REPO = Path(__file__).resolve().parents[1]
SUPPORTED_SSSOM = REPO / "output" / "mim-reviewed-sssom" / "ingredient_mappings.supported.sssom.tsv"
SOURCE_SSSOM = REPO / "mappings" / "ingredient_mappings.sssom.tsv"
FOLLOWUP_JSON = REPO / "reports" / "sssom_completion_20260921" / "mapping_review" / "kgmicrobe-followup.json"
REVIEW_JSON = REPO / "reports" / "sssom_completion_20260921" / "review.json"
INGREDIENTS_DIR = REPO / "data" / "ingredients"

CAS_RE = re.compile(r"^(?:cas:|CAS:)?(\d{2,7})-(\d{2})-(\d)$")


def is_valid_cas_rn(value: str) -> tuple[bool, int | None, int | None]:
    """Return `(is_valid, actual_check_digit, expected_check_digit)`.

    If `value` does not match the CAS-RN pattern at all, returns `(False, None, None)`.
    """
    m = CAS_RE.match(value.strip())
    if not m:
        return False, None, None
    part1, part2, check_str = m.groups()
    body = part1 + part2
    actual = int(check_str)
    expected = sum(int(d) * (i + 1) for i, d in enumerate(reversed(body))) % 10
    return actual == expected, actual, expected


def load_withheld_slugs(review_path: Path = REVIEW_JSON) -> set[str]:
    if not review_path.exists():
        return set()
    data = json.loads(review_path.read_text(encoding="utf-8"))
    withheld: set[str] = set()
    for entry in data.get("decisions", []):
        if entry.get("disposition") == "WITHHOLD":
            owner = str(entry.get("owner_record") or "")
            if owner:
                withheld.add(Path(owner).stem)
    return withheld


def scan_sssom_file(sssom_path: Path) -> list[dict[str, str]]:
    """Return invalid CAS occurrences in a SSSOM TSV (`object_id` or `other` token)."""
    findings: list[dict[str, str]] = []
    if not sssom_path.exists():
        return findings
    data_lines = [
        line
        for line in sssom_path.read_text(encoding="utf-8").splitlines()
        if line and not line.startswith("#")
    ]
    for row in csv.DictReader(data_lines, delimiter="\t"):
        subj = row.get("subject_id", "")
        obj = row.get("object_id", "")
        if obj.lower().startswith("cas:"):
            ok, actual, expected = is_valid_cas_rn(obj)
            if not ok:
                findings.append(
                    {
                        "source": sssom_path.name,
                        "subject_id": subj,
                        "field": "object_id",
                        "value": obj,
                        "expected_check": str(expected) if expected is not None else "malformed",
                    }
                )
        other = row.get("other", "") or ""
        for token in other.split("|"):
            tok = token.strip()
            if tok.upper().startswith("CAS:"):
                ok, actual, expected = is_valid_cas_rn(tok)
                if not ok:
                    findings.append(
                        {
                            "source": sssom_path.name,
                            "subject_id": subj,
                            "field": "other",
                            "value": tok,
                            "expected_check": str(expected) if expected is not None else "malformed",
                        }
                    )
    return findings


def scan_yaml_records(
    ingredients_dir: Path = INGREDIENTS_DIR,
    withheld_slugs: set[str] | None = None,
) -> list[dict[str, str]]:
    """Return invalid CAS occurrences in per-record YAML files."""
    if withheld_slugs is None:
        withheld_slugs = load_withheld_slugs()
    findings: list[dict[str, str]] = []
    for status in ("mapped", "unmapped"):
        folder = ingredients_dir / status
        if not folder.exists():
            continue
        for path in sorted(folder.glob("*.yaml")):
            rec = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
            if rec.get("mapping_status") == "REJECTED":
                continue
            slug = path.stem
            release_state = "WITHHELD" if slug in withheld_slugs else "PUBLISHED"
            ident = str(rec.get("identifier") or "").strip()
            if ident.lower().startswith("cas:"):
                ok, _actual, expected = is_valid_cas_rn(ident)
                if not ok:
                    findings.append(
                        {
                            "slug": slug,
                            "field": "identifier",
                            "value": ident,
                            "expected_check": str(expected) if expected is not None else "malformed",
                            "release_state": release_state,
                        }
                    )
            cp = rec.get("chemical_properties") or {}
            cas_rn = str(cp.get("cas_rn") or "").strip()
            if cas_rn:
                ok, _actual, expected = is_valid_cas_rn(cas_rn)
                if not ok:
                    findings.append(
                        {
                            "slug": slug,
                            "field": "chemical_properties.cas_rn",
                            "value": cas_rn,
                            "expected_check": str(expected) if expected is not None else "malformed",
                            "release_state": release_state,
                        }
                    )
    return findings


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument(
        "--check",
        action="store_true",
        help="Exit 2 if any published SSSOM row or non-withheld YAML record has an invalid CAS check digit.",
    )
    args = ap.parse_args(argv)

    supported_findings = scan_sssom_file(SUPPORTED_SSSOM)
    yaml_findings = scan_yaml_records()
    published_yaml_findings = [f for f in yaml_findings if f["release_state"] == "PUBLISHED"]
    withheld_yaml_findings = [f for f in yaml_findings if f["release_state"] == "WITHHELD"]

    print(f"Supported SSSOM invalid CAS check digits: {len(supported_findings)}")
    for f in supported_findings:
        print(
            f"  [SUPPORTED_SSSOM] {f['subject_id']} {f['field']}={f['value']} "
            f"(expected check digit: {f['expected_check']})"
        )

    print(f"Published YAML invalid CAS check digits: {len(published_yaml_findings)}")
    for f in published_yaml_findings:
        print(
            f"  [PUBLISHED_YAML] {f['slug']} {f['field']}={f['value']} "
            f"(expected check digit: {f['expected_check']})"
        )

    print(f"Withheld YAML invalid CAS check digits (Upstream CHEBI/CAS typos): {len(withheld_yaml_findings)}")
    for f in withheld_yaml_findings:
        print(
            f"  [WITHHELD_YAML] {f['slug']} {f['field']}={f['value']} "
            f"(expected check digit: {f['expected_check']})"
        )

    if args.check and (supported_findings or published_yaml_findings):
        print(
            f"ERROR: {len(supported_findings)} supported SSSOM and "
            f"{len(published_yaml_findings)} published YAML invalid CAS check digit(s)",
            file=sys.stderr,
        )
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
