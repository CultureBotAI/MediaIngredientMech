#!/usr/bin/env python3
"""Gate against published MIM: subjects disappearing without an alias (#300).

External consumers (CultureMech, CommunityMech, kg-microbe) persist `MIM:<slug>`
CURIEs from `mappings/ingredient_mappings.sssom.tsv`. When a record is renamed,
merged, or deleted, its `MIM:` subject disappears from the SSSOM. Git rename
history (`scripts/build_curie_alias_map.py`) catches pure file moves (`R`), but
a merge (`scripts/merge_mapped_records.py`) deletes the source file (`D`) and
removes its SSSOM rows, leaving no git rename trail unless an entry is added to
`mappings/mim_curie_alias_seeds.tsv` and `just curie-aliases` is run.

What `--check` enforces (exit 2 on failure):
  * Every `subject_id` in `mappings/published_mim_subjects_baseline.tsv` must
    either still be present in `mappings/ingredient_mappings.sssom.tsv` or
    appear as `old_curie` in `mappings/mim_curie_aliases.tsv` with a
    `current_curie` that is present in `mappings/ingredient_mappings.sssom.tsv`.

What `--write-baseline` does:
  * Refuses (exit 2) if any baseline subject has vanished from the SSSOM without
    a valid alias in `mappings/mim_curie_aliases.tsv` — so `--write-baseline`
    cannot be used to launder a missing alias.
  * Writes the current SSSOM subjects to
    `mappings/published_mim_subjects_baseline.tsv`.
"""

from __future__ import annotations

import argparse
import csv
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SSSOM = ROOT / "mappings" / "ingredient_mappings.sssom.tsv"
ALIASES = ROOT / "mappings" / "mim_curie_aliases.tsv"
BASELINE = ROOT / "mappings" / "published_mim_subjects_baseline.tsv"
FIELDS = ["subject_id", "subject_label"]


def load_sssom_subjects(sssom_path: Path = SSSOM) -> dict[str, str]:
    """Return {subject_id: subject_label} from the published SSSOM."""
    subjects: dict[str, str] = {}
    with sssom_path.open(newline="", encoding="utf-8") as fh:
        data_lines = [line for line in fh if not line.startswith("#")]
    for row in csv.DictReader(data_lines, delimiter="\t"):
        sid = (row.get("subject_id") or "").strip()
        label = (row.get("subject_label") or "").strip()
        if sid and sid not in subjects:
            subjects[sid] = label
    return dict(sorted(subjects.items()))


def load_aliases(aliases_path: Path = ALIASES) -> dict[str, str]:
    """Return {old_curie: current_curie} from mappings/mim_curie_aliases.tsv."""
    if not aliases_path.is_file():
        return {}
    out: dict[str, str] = {}
    with aliases_path.open(newline="", encoding="utf-8") as fh:
        for row in csv.DictReader(fh, delimiter="\t"):
            old = (row.get("old_curie") or "").strip()
            new = (row.get("current_curie") or "").strip()
            if old and new:
                out[old] = new
    return out


def load_baseline(baseline_path: Path = BASELINE) -> dict[str, str]:
    """Return {subject_id: subject_label} from the tracked baseline TSV."""
    if not baseline_path.is_file():
        raise SystemExit(
            f"ERROR: missing baseline {baseline_path.relative_to(ROOT)}; "
            "run --write-baseline once and commit it."
        )
    out: dict[str, str] = {}
    with baseline_path.open(newline="", encoding="utf-8") as fh:
        for row in csv.DictReader(fh, delimiter="\t"):
            sid = (row.get("subject_id") or "").strip()
            label = (row.get("subject_label") or "").strip()
            if sid:
                out[sid] = label
    return out


def resolve_alias(curie: str, aliases: dict[str, str]) -> str | None:
    """Follow alias chain from `curie`, guarding against cycles."""
    if curie not in aliases:
        return None
    seen = {curie}
    cur = aliases[curie]
    while cur in aliases and cur not in seen:
        seen.add(cur)
        cur = aliases[cur]
    return cur


def audit(
    baseline: dict[str, str],
    current_subjects: dict[str, str],
    aliases: dict[str, str],
) -> tuple[list[tuple[str, str]], list[tuple[str, str, str]], list[tuple[str, str, str]]]:
    """Compare baseline subjects against current SSSOM and alias map.

    Returns:
      - unaliased_vanished: [(subject_id, subject_label)] missing from SSSOM and aliases
      - dangling_alias: [(subject_id, subject_label, alias_target)] aliased to a target
        not in current SSSOM
      - aliased_retired: [(subject_id, subject_label, alias_target)] cleanly retired via alias
    """
    unaliased_vanished: list[tuple[str, str]] = []
    dangling_alias: list[tuple[str, str, str]] = []
    aliased_retired: list[tuple[str, str, str]] = []

    for sid, label in sorted(baseline.items()):
        if sid in current_subjects:
            continue
        target = resolve_alias(sid, aliases)
        if target is None:
            unaliased_vanished.append((sid, label))
        elif target not in current_subjects:
            dangling_alias.append((sid, label, target))
        else:
            aliased_retired.append((sid, label, target))

    return unaliased_vanished, dangling_alias, aliased_retired


def write_baseline(baseline_path: Path, subjects: dict[str, str]) -> None:
    baseline_path.parent.mkdir(parents=True, exist_ok=True)
    with baseline_path.open("w", newline="", encoding="utf-8") as fh:
        writer = csv.DictWriter(fh, fieldnames=FIELDS, delimiter="\t", lineterminator="\n")
        writer.writeheader()
        for sid, label in sorted(subjects.items()):
            writer.writerow({"subject_id": sid, "subject_label": label})


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument(
        "--check",
        action="store_true",
        help="Exit 2 if any baseline MIM: subject vanished without a live SSSOM alias",
    )
    mode.add_argument(
        "--write-baseline",
        action="store_true",
        help="Refresh mappings/published_mim_subjects_baseline.tsv (refuses if unaliased retirements exist)",
    )
    args = parser.parse_args(argv)

    current_subjects = load_sssom_subjects(SSSOM)
    aliases = load_aliases(ALIASES)

    if args.write_baseline:
        if BASELINE.is_file():
            prior = load_baseline(BASELINE)
            unaliased, dangling, _ = audit(prior, current_subjects, aliases)
            if unaliased or dangling:
                print(
                    "ERROR: refusing to overwrite baseline while published MIM: subjects "
                    "have vanished without a live alias in mappings/mim_curie_aliases.tsv:",
                    file=sys.stderr,
                )
                for sid, label in unaliased:
                    print(f"  VANISHED  {sid} ({label!r}) — no row in mim_curie_aliases.tsv", file=sys.stderr)
                for sid, label, target in dangling:
                    print(
                        f"  DANGLING  {sid} ({label!r}) -> {target} (target not in SSSOM)",
                        file=sys.stderr,
                    )
                print(
                    "\nAdd an alias row to mappings/mim_curie_alias_seeds.tsv and run "
                    "`just curie-aliases` before refreshing the baseline.",
                    file=sys.stderr,
                )
                return 2
        write_baseline(BASELINE, current_subjects)
        rel = BASELINE.relative_to(ROOT) if BASELINE.is_relative_to(ROOT) else BASELINE
        print(f"wrote {len(current_subjects)} subject(s) to {rel}")
        return 0

    baseline = load_baseline(BASELINE)
    unaliased, dangling, retired = audit(baseline, current_subjects, aliases)
    added = sorted(set(current_subjects) - set(baseline))

    print(
        f"published SSSOM subjects: {len(current_subjects)} "
        f"(baseline: {len(baseline)}, new: {len(added)}, aliased retirements: {len(retired)})"
    )
    if not (unaliased or dangling):
        print("OK: every baseline MIM: subject resolves in the SSSOM or via mim_curie_aliases.tsv.")
        return 0

    print(
        "\nERROR: published MIM: subject(s) vanished without a live alias in "
        "mappings/mim_curie_aliases.tsv:",
        file=sys.stderr,
    )
    for sid, label in unaliased:
        print(f"  VANISHED  {sid} ({label!r}) — no row in mim_curie_aliases.tsv", file=sys.stderr)
    for sid, label, target in dangling:
        print(
            f"  DANGLING  {sid} ({label!r}) -> {target} (target not in SSSOM)",
            file=sys.stderr,
        )
    print(
        "\nRecord retired subjects in mappings/mim_curie_alias_seeds.tsv, run "
        "`just curie-aliases`, and then refresh the baseline with:\n"
        "  uv run python scripts/audit_published_subjects.py --write-baseline",
        file=sys.stderr,
    )
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
