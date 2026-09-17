#!/usr/bin/env python3
"""Every SSSOM ``MIM:`` subject must be a per-record file stem (#236).

**Decided (#236):** a ``MIM:`` subject is ``mim_curie_for_stem(<file stem>)`` —
the record's per-record filename stem with non-URL-safe characters ``~HEX``
escaped. It is fixed for the life of the record and is never re-derived from
``preferred_term``.

#236 posed this as a trade-off between stable per-record paths and slug/path
agreement, with three options: rename files on relabel, declare the slug opaque,
or require every subject to resolve. The trade-off only exists if the slug is
computed from the label. ``export_individual_records.FilenameIndex`` never
renames a file, so deriving the subject from the *stem* gives both properties at
once — the subject never changes, and it always names a file.

The pipeline already worked this way before the decision was written down:

  * claw's publisher emits ``subject_id  MIM:<safe_stem>  -- stable per-YAML CURIE``;
  * ``CurieNormalizer`` builds its known-record set from file stems and returns
    ``UNKNOWN_SUBJECT`` for anything else, so a subject that names no file is not
    harmless — ``equivalent_term`` refuses to cite the mapping;
  * #293 and #307 made promotions publish the existing stem.

**This is a gate.** Before #236 was decided it only reported, and it compared
subjects against *raw* stems without escaping. Every subject whose stem holds a
``(``, ``)`` or ``α`` therefore looked unresolved — 18 false alarms, and zero
genuine ones, measured with the escaping ``CurieNormalizer`` itself uses. The
tool announcing that the question was open was itself producing the evidence
that it was.

    python scripts/check_sssom_subject_files.py
"""
from __future__ import annotations

import csv
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "src"))

from mediaingredientmech.curie import mim_curie_for_stem  # noqa: E402

SSSOM = ROOT / "mappings" / "ingredient_mappings.sssom.tsv"
RECORD_DIRS = (ROOT / "data" / "ingredients" / "mapped",
               ROOT / "data" / "ingredients" / "unmapped")


def known_subjects(record_dirs: tuple[Path, ...] = RECORD_DIRS) -> set[str]:
    """
    Return the ``MIM:`` CURIE every per-record file addresses.

    Uses ``mim_curie_for_stem`` — the same escaping ``CurieNormalizer`` applies —
    rather than the raw stem, which is what made the old report cry wolf.

    :param record_dirs: The per-record directories to scan.
    :return: One escaped ``MIM:`` CURIE per record file.
    """
    return {
        mim_curie_for_stem(path.stem)
        for directory in record_dirs
        if directory.is_dir()
        for path in directory.glob("*.yaml")
    }


def unresolved_subjects(sssom: Path = SSSOM, record_dirs: tuple[Path, ...] = RECORD_DIRS) -> dict[str, str]:
    """
    Return ``{subject_id: subject_label}`` for subjects that name no record file.

    :param sssom: The published mapping set.
    :param record_dirs: The per-record directories to scan.
    :return: The subjects a consumer would resolve as ``UNKNOWN_SUBJECT``.
    """
    known = known_subjects(record_dirs)
    subjects: dict[str, str] = {}
    with sssom.open(newline="", encoding="utf-8") as handle:
        for row in csv.reader(handle, delimiter="\t"):
            if row and row[0].startswith("MIM:"):
                subjects.setdefault(row[0], row[1] if len(row) > 1 else "")
    return {subject: label for subject, label in subjects.items() if subject not in known}


def main() -> int:
    unresolved = unresolved_subjects()
    print(f"MIM: subjects that name no per-record file: {len(unresolved)}")
    for subject, label in sorted(unresolved.items()):
        print(f"  {subject}")
        print(f"      subject_label: {label!r}")
    if not unresolved:
        print("OK: every MIM: subject is an escaped per-record file stem (#236).")
        return 0
    print(
        "\nA subject must be mim_curie_for_stem(<the record's file stem>) and must "
        "never be re-derived from preferred_term (#236). CurieNormalizer resolves "
        "these as UNKNOWN_SUBJECT, so the mapping publishes but cannot be cited."
    )
    return 1


if __name__ == "__main__":
    sys.exit(main())
