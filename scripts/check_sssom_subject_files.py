#!/usr/bin/env python3
"""Report SSSOM `MIM:` subjects that do not resolve to a per-record file (#236).

The SSSOM ``curie_map`` expands ``MIM:`` to ``data/ingredients/mapped/``, so a
``MIM:<slug>`` subject reads as an address for the per-record file. But
``export_individual_records.FilenameIndex`` deliberately never renames an existing
file — per-record paths stay stable across relabels — while the SSSOM subject is
recomputed from ``preferred_term`` via ``sanitize_filename`` every time. The two
therefore drift apart whenever a record is relabelled, or whenever a stem predates
a change in the sanitiser.

Nothing else detects this. ``reconcile_sssom`` checks GAP / ORPHAN / STALE against
``ontology_id`` and never looks at the subject slug, which is why a clean reconcile
does not imply the subjects resolve.

**This is a report, not a gate.** #236 has not decided between:

  1. rename per-record files when ``preferred_term`` changes (slug/path agree,
     paths stop being stable);
  2. declare ``MIM:`` slugs opaque identifiers rather than paths and document that
     in the curie_map (the mismatch stops being a defect);
  3. require every subject to resolve, and fix the existing cases.

Under (2) a non-zero count here is expected and harmless. The point of the script
is that whichever option is chosen, the number stops being invisible — and a
relabel's effect on it becomes measurable before the relabel lands, which is what
#209 needs.

    python scripts/check_sssom_subject_files.py
"""
from __future__ import annotations

import csv
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SSSOM = ROOT / "mappings" / "ingredient_mappings.sssom.tsv"
RECORD_DIRS = (ROOT / "data" / "ingredients" / "mapped",
               ROOT / "data" / "ingredients" / "unmapped")


def main() -> int:
    stems = {p.stem for d in RECORD_DIRS if d.is_dir() for p in d.glob("*.yaml")}
    subjects: dict[str, str] = {}
    with SSSOM.open(newline="", encoding="utf-8") as fh:
        for row in csv.reader(fh, delimiter="\t"):
            if row and row[0].startswith("MIM:"):
                subjects.setdefault(row[0][4:], row[1] if len(row) > 1 else "")

    unresolved = {s: lbl for s, lbl in subjects.items() if s not in stems}
    print(f"MIM: subjects: {len(subjects)}   per-record files: {len(stems)}")
    print(f"subjects with NO matching file stem: {len(unresolved)}")
    for slug, label in sorted(unresolved.items()):
        print(f"  MIM:{slug}")
        print(f"      subject_label: {label!r}")
    if unresolved:
        print("\nThis is expected under #236 option 2 (MIM: slugs are opaque ids, not "
              "paths).\nIt is a defect only under option 1 or 3, which are undecided. "
              "Reported, not gated.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
