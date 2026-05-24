#!/usr/bin/env python3
"""Audit YAML-writing scripts in MediaIngredientMech.

For every Python module under ``scripts/`` and the central
``src/mediaingredientmech/{curation,utils}`` packages that writes a YAML
(looks for ``yaml.dump``, ``yaml.safe_dump``, ``write_validated_ingredient``,
or ``.write_text(`` on a ``.yaml`` path), record:

  - target_kind: ``ingredient`` (writes back to per-ingredient or collection
    YAML in ``data/ingredients/`` or ``data/curated/``), ``report`` (writes
    a manifest / report / log / analysis output), ``mixed`` (does both --
    typically importers that write ingredients plus a sibling index), or
    ``unknown`` (couldn't classify from the script source).
  - appends to ``curation_history``?
  - has a ``--dry-run`` flag?
  - calls ``write_validated_ingredient()`` (or ``linkml-validate`` etc.)
    before writing?
  - is mentioned in ``justfile`` (i.e. wired into a target)?

TSV columns: path, writes_yaml, target_kind, appends_curation_history,
has_dry_run, validates_before_write, wired_into_just.

Use ``target_kind`` to scope follow-up work --
``record_curation_event()`` adoption is meaningful only for ``ingredient``
and ``mixed`` writers; reports / manifests / logs aren't ingredients and
don't have a curation history.

Output: TSV to stdout (and via ``--out`` to a file).

Ported from CultureMech's ``scripts/audit_writers.py``.
"""

from __future__ import annotations

import argparse
import csv
import re
import sys
from pathlib import Path

ROOT = Path(".").resolve()
SEARCH_DIRS = [
    Path("scripts"),
    Path("src/mediaingredientmech/curation"),
    Path("src/mediaingredientmech/utils"),
]

# Patterns
_WRITE_YAML_HINT = re.compile(r"\.ya?ml['\"]|\.yaml\b")
_CURATION_APPEND = re.compile(
    r"curation_history.*?(append|\+=|\.insert)"
    r"|['\"]curator['\"]\s*:"
    r"|append_curation_event"
    r"|record_curation_event"
    r"|_add_event\("
)
_DRY_RUN = re.compile(r"--dry[-_]run|dry_run\s*[:=]")
_VALIDATE_BEFORE_WRITE = re.compile(
    r"linkml[._-]?validate"
    r"|RecipeValidator"
    r"|validate_recipe\("
    r"|validate_ingredient\("
    r"|validator\.validate\("
    r"|write_validated_ingredient\("
    r"|write_validated_recipe\("
    # save_yaml(..., validate=True ...) — the package-level helper's opt-in
    # that routes through write_validated_ingredient.
    r"|save_yaml\([^)]*validate\s*=\s*True"
)
# Heuristic for "writes back to an ingredient YAML under data/ingredients/
# or data/curated/" (i.e. would benefit from a CurationEvent) vs writes a
# report/manifest/index (where curation_history is meaningless).
_INGREDIENT_WRITER = re.compile(
    r"data/ingredients/"
    r"|data/curated/"
    r"|mapped_ingredients\.yaml"
    r"|unmapped_[A-Za-z_]+\.yaml"
    r"|write_validated_ingredient\("
    r"|save_yaml\("
    r"|IngredientCurator"
)
_REPORT_WRITER = re.compile(
    # Narrowly target report/manifest/log sinks. Match argparse-style
    # `args.output`/`args.report` and explicit report/log path names.
    r"args\.output\b"
    r"|args\.report\b"
    r"|out\.write_text\b"
    r"|report_file\b"
    r"|report_path\b"
    r"|log_file\b"
    r"|manifest\b"
    r"|reports/\S+\.(tsv|json|md|yaml)"
    r"|\.tsv['\"]?\)"
    r"|\.json['\"]?\)"
)


def script_paths() -> list[Path]:
    out: list[Path] = []
    for d in SEARCH_DIRS:
        if not d.exists():
            continue
        out.extend(sorted(p for p in d.rglob("*.py") if "__pycache__" not in str(p)))
    return out


def looks_like_yaml_writer(text: str) -> bool:
    if "yaml.safe_dump(" in text or "yaml.dump(" in text:
        return True
    # write_validated_ingredient is the helper that wraps yaml.safe_dump.
    if "write_validated_ingredient(" in text:
        return True
    # save_yaml(...) from mediaingredientmech.utils.yaml_handler — the
    # package-level helper that all converted writer scripts route through.
    if "save_yaml(" in text:
        return True
    # `.write_text(` only counts if combined with a yaml hint nearby.
    if ".write_text(" in text and _WRITE_YAML_HINT.search(text):
        return True
    return False


def audit(path: Path, justfile_text: str) -> dict | None:
    try:
        text = path.read_text()
    except (UnicodeDecodeError, OSError):
        return None
    if not looks_like_yaml_writer(text):
        return None
    # Categorize: a writer that *only* writes reports/manifests does not
    # benefit from CurationEvent — flag separately so follow-ups stay
    # focused on actual ingredient modifiers.
    ingredient = bool(_INGREDIENT_WRITER.search(text))
    report = bool(_REPORT_WRITER.search(text))
    if ingredient and not report:
        target = "ingredient"
    elif report and not ingredient:
        target = "report"
    elif ingredient and report:
        target = "mixed"
    else:
        target = "unknown"
    return {
        "path": str(path),
        "writes_yaml": "yes",
        "target_kind": target,
        "appends_curation_history": "yes" if _CURATION_APPEND.search(text) else "no",
        "has_dry_run": "yes" if _DRY_RUN.search(text) else "no",
        "validates_before_write": "yes" if _VALIDATE_BEFORE_WRITE.search(text) else "no",
        "wired_into_just": "yes" if path.stem in justfile_text or path.name in justfile_text else "no",
    }


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--out", type=Path, default=None, help="TSV output path (default stdout)")
    args = ap.parse_args()

    justfile_path = Path("justfile")
    justfile_text = justfile_path.read_text() if justfile_path.exists() else ""

    rows: list[dict] = []
    for p in script_paths():
        row = audit(p, justfile_text)
        if row is not None:
            rows.append(row)

    fields = [
        "path",
        "writes_yaml",
        "target_kind",
        "appends_curation_history",
        "has_dry_run",
        "validates_before_write",
        "wired_into_just",
    ]

    if args.out:
        args.out.parent.mkdir(parents=True, exist_ok=True)
        with args.out.open("w", newline="") as fh:
            w = csv.DictWriter(fh, fieldnames=fields, delimiter="\t", lineterminator="\n")
            w.writeheader()
            for row in rows:
                w.writerow(row)
        print(f"Wrote {len(rows)} rows to {args.out}", file=sys.stderr)
    else:
        w = csv.DictWriter(sys.stdout, fieldnames=fields, delimiter="\t")
        w.writeheader()
        for row in rows:
            w.writerow(row)

    # Print summary
    def count(field: str, val: str) -> int:
        return sum(1 for r in rows if r[field] == val)

    ingredient_writers = [r for r in rows if r["target_kind"] in ("ingredient", "mixed")]

    print("", file=sys.stderr)
    print(f"=== writers audit summary ({len(rows)} writers) ===", file=sys.stderr)
    print(
        f"  target kind:                ingredient={count('target_kind', 'ingredient')} "
        f"mixed={count('target_kind', 'mixed')} report={count('target_kind', 'report')} "
        f"unknown={count('target_kind', 'unknown')}",
        file=sys.stderr,
    )
    print(
        f"  appends curation_history:   {count('appends_curation_history', 'yes')} / {len(rows)}",
        file=sys.stderr,
    )
    print(
        f"  (ingredient writers only) appends curation_history: "
        f"{sum(1 for r in ingredient_writers if r['appends_curation_history']=='yes')} / "
        f"{len(ingredient_writers)}",
        file=sys.stderr,
    )
    print(
        f"  has --dry-run:              {count('has_dry_run', 'yes')} / {len(rows)}",
        file=sys.stderr,
    )
    print(
        f"  validates before write:     {count('validates_before_write', 'yes')} / {len(rows)}",
        file=sys.stderr,
    )
    print(
        f"  wired into justfile:        {count('wired_into_just', 'yes')} / {len(rows)}",
        file=sys.stderr,
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
