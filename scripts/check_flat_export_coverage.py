"""docs/data/ must be fresh, and every raw label MIM knows must resolve from it (#229).

MIM's job is turning a raw ingredient string from a medium recipe into an
ontology term. Consumers do that by joining against the published artifacts.

Merging a duplicate deletes its record and keeps the raw label only as a synonym
on the target, and merges add no SSSOM row (SSSOM subjects are preferred_terms
of MAPPED records, never synonyms). `docs/data/ingredients.json` has always
carried a synonyms array, but the CSV/JSON backlog exports here did not -- so
after PR #227 `D-lactate` still resolved from ingredients.json and resolved from
neither `all_ingredients.csv` nor the SSSOM TSV.

Two independent failures, so two checks:

  FRESHNESS  regenerate the exports into a temp dir and require them to match
             what is committed. This is the one that catches a merge applied to
             data/curated/ without re-running the export -- the stale CSV still
             carries the deleted record's own row, so a coverage check alone
             sees the label and passes while it now resolves to a record that no
             longer exists. That is exactly how #214's first pass shipped six
             artifacts naming records it had just deleted.

  COVERAGE   every preferred_term and every published synonym in the curated
             collections must be resolvable from each flat CSV. Freshness alone
             would not catch an export that consistently drops labels.

Exits 2 on either.
"""

from __future__ import annotations

import argparse
import collections
import csv
import filecmp
import json
import subprocess
import sys
import tempfile
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
CURATED = ROOT / "data" / "curated"
DOCS = ROOT / "docs" / "data"
EXPORTER = ROOT / "scripts" / "export_lists.py"
BROWSER = ROOT / "scripts" / "browser_export.py"
SEP = "|"

# (flat artifact, curated collections it must cover)
COVERAGE = {
    "all_ingredients.csv": ("mapped_ingredients.yaml", "unmapped_ingredients.yaml"),
    "mapped_ingredients.csv": ("mapped_ingredients.yaml",),
    "unmapped_ingredients.csv": ("unmapped_ingredients.yaml",),
}
# Regenerated deterministically. The .md exports embed a `Generated:` timestamp,
# so they can never compare equal and are excluded from the freshness check.
DETERMINISTIC = sorted(
    {f"{stem}_ingredients.{ext}"
     for stem in ("all", "mapped", "unmapped") for ext in ("csv", "json")}
    | {"label_index.csv"})   # per-label resolution with precedence (#232)


def fail(msg: str) -> int:
    print(f"\nERROR: {msg}")
    return 2


def _browser_payload(path: Path):
    """ingredients.json minus its `metadata.generated` stamp, which changes every
    run — so compare the payload, not the bytes."""
    doc = json.loads(path.read_text())
    return doc.get("ingredients")


def check_freshness() -> int:
    with tempfile.TemporaryDirectory() as tmp:
        proc = subprocess.run(
            [sys.executable, str(EXPORTER), "--output-dir", tmp, "--format", "all"],
            capture_output=True, text=True, cwd=ROOT)
        if proc.returncode != 0:
            return fail(f"export_lists.py failed:\n{proc.stdout}\n{proc.stderr}")
        stale = [name for name in DETERMINISTIC
                 if not (DOCS / name).exists()
                 or not filecmp.cmp(DOCS / name, Path(tmp) / name, shallow=False)]
        # ingredients.json comes from a different producer and was outside every
        # gate — it was the artifact that DID resolve merged labels correctly and
        # was itself stale by a record. Issue #233.
        proc = subprocess.run(
            [sys.executable, str(BROWSER), "--output", str(Path(tmp) / "ingredients.json")],
            capture_output=True, text=True, cwd=ROOT)
        if proc.returncode != 0:
            return fail(f"browser_export.py failed:\n{proc.stdout}\n{proc.stderr}")
        live = DOCS / "ingredients.json"
        if not live.exists() or _browser_payload(live) != _browser_payload(Path(tmp) / "ingredients.json"):
            stale.append("ingredients.json")
    if stale:
        # the two artifacts come from different producers reading different
        # sources, so name the right remedy for each rather than one blanket
        # "run export-lists" that does nothing for ingredients.json
        remedy = {n: ("`just export-browser`  (browser_export.py, reads data/ingredients/)"
                      if n == "ingredients.json"
                      else "`just export-lists`    (export_lists.py, reads data/curated/)")
                  for n in stale}
        return fail(
            "docs/data/ does not match what its producer generates — it is stale:\n"
            + "".join(f"  {n:26} regenerate with {remedy[n]}\n" for n in stale)
            + "\nCommit the result. A stale export keeps publishing records that "
              "curation has already deleted or merged.")
    print(f"freshness: {len(DETERMINISTIC) + 1} regenerated artifact(s) match their producers")
    return 0


def curated_labels(collections_: tuple[str, ...]) -> dict[str, list[str]]:
    """label -> identifier(s) answering to it, using the exporter's own rule for
    which synonyms are publishable so the two cannot drift apart."""
    sys.path.insert(0, str(ROOT / "scripts"))
    import importlib.util
    spec = importlib.util.spec_from_file_location("export_lists", EXPORTER)
    mod = importlib.util.module_from_spec(spec)
    try:
        spec.loader.exec_module(mod)
    except ImportError as exc:
        # the exporter needs click/rich; a caller without them should get the
        # documented exit 2 and the remedy, not a traceback
        raise SystemExit(fail(
            f"cannot import {EXPORTER.name} ({exc}). Install its dependencies: "
            "pip install pyyaml click rich")) from exc

    out: dict[str, list[str]] = {}
    for name in collections_:
        doc = yaml.safe_load((CURATED / name).read_text()) or {}
        for rec in doc.get("ingredients") or []:
            ident = str(rec.get("identifier", "?"))
            for lab in [rec.get("preferred_term"), *mod._synonyms(rec)]:
                if lab:
                    out.setdefault(lab, []).append(ident)
    return out


def published_labels(path: Path) -> tuple[set[str], dict[str, set[str]]]:
    with path.open(newline="") as fh:
        reader = csv.DictReader(fh)
        if "synonyms" not in (reader.fieldnames or []):
            print(f"\nERROR: {path.relative_to(ROOT)} has no `synonyms` column, so every "
                  "merged raw label is unpublished. Run `just export-lists`.")
            raise SystemExit(2)
        labels: set[str] = set()
        by_label: dict[str, set[str]] = collections.defaultdict(set)
        for row in reader:
            ident = row.get("identifier", "")
            for lab in [row.get("preferred_term"), *(row.get("synonyms") or "").split(SEP)]:
                if lab:
                    labels.add(lab)
                    by_label[lab].add(ident)
    return labels, by_label


def check_coverage(limit: int) -> int:
    rc = 0
    for name, sources in COVERAGE.items():
        path = DOCS / name
        if not path.exists():
            rc = fail(f"{path.relative_to(ROOT)} does not exist — run `just export-lists`.")
            continue
        curated = curated_labels(sources)
        published, by_label = published_labels(path)
        missing = sorted(lab for lab in curated if lab not in published)
        resolved = len(curated) - len(missing)
        print(f"coverage: {name:26} {resolved}/{len(curated)} curated label(s) resolvable")
        if missing:
            rc = fail(f"{len(missing)} label(s) known to MIM resolve to nothing in {name}")
            for lab in missing[:limit]:
                print(f"  {lab!r}  (record {', '.join(curated[lab])})")
            if len(missing) > limit:
                print(f"  ... and {len(missing) - limit} more")
        if name == "all_ingredients.csv":
            ambiguous = {k: v for k, v in by_label.items() if len(v) > 1}
            if ambiguous:
                # Not a failure: a synonym legitimately can be shared. But a
                # consumer's {label: identifier} join is order-dependent for
                # these, and preferred_terms alone used to be unique.
                print(f"  note: {len(ambiguous)} published label(s) map to more than one "
                      "identifier — see #232 for the triage")
    return rc


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--limit", type=int, default=20, help="how many gaps to print")
    ap.add_argument("--skip-freshness", action="store_true",
                    help="coverage only; for callers that just regenerated")
    args = ap.parse_args()

    rc = 0 if args.skip_freshness else check_freshness()
    rc = check_coverage(args.limit) or rc
    if rc == 0:
        print("\nOK: docs/data/ is fresh and every curated label is published.")
    return rc


if __name__ == "__main__":
    sys.exit(main())
