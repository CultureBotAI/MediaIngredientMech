#!/usr/bin/env python3
"""Check SSSOM MIM subjects against registered current record identities (#1265).

Permanent numeric subjects resolve through the append-only ID registry and the
current corpus, independently of filenames. Preserved historical aliases can
resolve only when unambiguous. No records, mappings or aliases are rewritten.
Unknown/ambiguous subjects and invalid registry/corpus state exit nonzero.

    python scripts/check_sssom_subject_files.py
"""

from __future__ import annotations

import argparse
import csv
import sys
from pathlib import Path

from mediaingredientmech.curie import CurieNormalizer

ROOT = Path(__file__).resolve().parent.parent


def check_subjects(root: Path, sssom: Path) -> tuple[dict[str, str], dict[str, str]]:
    """Return unique MIM subject resolutions and unresolved-subject reasons."""
    normalizer = CurieNormalizer(repo_root=root, sssom_path=sssom)
    resolved: dict[str, str] = {}
    unresolved: dict[str, str] = {}
    with sssom.open(newline="", encoding="utf-8") as stream:
        rows = csv.DictReader((line for line in stream if not line.startswith("#")),
                              delimiter="\t")
        if not rows.fieldnames or "subject_id" not in rows.fieldnames:
            raise ValueError("SSSOM requires a subject_id column")
        for row in rows:
            subject = (row.get("subject_id") or "").strip()
            if not subject.casefold().startswith("mim:"):
                continue
            verdict = normalizer.resolve(subject)
            if verdict:
                resolved[subject] = verdict.curie
            else:
                unresolved[subject] = verdict.problem
    return resolved, unresolved


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=ROOT)
    parser.add_argument("--sssom", type=Path)
    args = parser.parse_args(argv)
    sssom = args.sssom or args.root / "mappings/ingredient_mappings.sssom.tsv"
    try:
        resolved, unresolved = check_subjects(args.root, sssom)
    except (OSError, ValueError) as exc:
        print(f"MIM subject check failed: {exc}", file=sys.stderr)
        return 1
    print(f"MIM subjects: {len(resolved) + len(unresolved)}")
    print(f"Resolved through registry and current records: {len(resolved)}")
    for subject, target in sorted(resolved.items()):
        if subject != target:
            print(f"  {subject} -> {target}")
    print(f"Unresolved subjects: {len(unresolved)}")
    for subject, problem in sorted(unresolved.items()):
        print(f"  {subject}: {problem}")
    return 1 if unresolved else 0


if __name__ == "__main__":
    sys.exit(main())
