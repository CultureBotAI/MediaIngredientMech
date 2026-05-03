#!/usr/bin/env python3
"""
CI-friendly validator for ``mappings/ingredient_mappings.sssom.tsv``.

Mirrors ``kg-microbe/mappings/validate_isolation_source_mappings.py``:
stdlib only (``csv`` + ``argparse``), per-row stderr report, exit-2 on
violation so CI blocks the merge.

Initial scope = Rule A (auto-classifier token-overlap gate). Rules B1–B4
(structural invariants on ``MIM:<slug>`` rows) land in PR2. See plan
``culturebotai-claw/.claude/plans/now-focus-on-culturemech-piped-shell.md``.

Rule A — for every row whose ``source`` column is "auto-classifier-only"
(every pipe-separated tag is ``MIM:curator=...``), accept iff at least
one of:

  * ``confidence`` >= 0.95
  * ``subject_label`` and ``object_label`` share at least one
    discriminating token (lowercase, length >= 2, stop-words removed —
    pattern reused verbatim from
    ``culturebotai-claw/scripts/foodon_pass.py:64-105``)
  * the subject's MIM YAML at ``data/ingredients/mapped/{slug}.yaml``
    carries an independent CAS-RN or PubChem CID xref (registry
    corroboration). This is read lazily — only when the previous two
    tiers have failed — and uses a minimal regex parser to avoid a
    PyYAML dependency in CI.

Rejected rows are written to ``mappings/needs_curator_review.tsv`` with
the same column shape as the source SSSOM plus a trailing
``reject_reason`` column. Workflow: fix the row in MIM (re-emit via the
claw builder) or leave it in the triage TSV; CI fails as long as a
violating row sits in ``ingredient_mappings.sssom.tsv``.

Exit codes:
  0 — every row passes Rule A.
  2 — at least one row failed Rule A (CI-blocking).
"""
from __future__ import annotations

import argparse
import csv
import re
import sys
from pathlib import Path
from typing import Iterable, Iterator

REPO_ROOT = Path(__file__).resolve().parent.parent
DEFAULT_SSSOM = REPO_ROOT / "mappings" / "ingredient_mappings.sssom.tsv"
DEFAULT_REJECT_TSV = REPO_ROOT / "mappings" / "needs_curator_review.tsv"
INGREDIENTS_DIR = REPO_ROOT / "data" / "ingredients" / "mapped"

AUTO_PIPELINE_TAGS = frozenset({
    "MIM:curator=auto_classify_ingredient_type",
    "MIM:curator=backfill_parent_terms",
})
CURATOR_TAG_PREFIX = "MIM:curator="
CONFIDENCE_TIER = 0.95


# ---------------------------------------------------------------------------
# Token-overlap heuristic — copied verbatim from
# culturebotai-claw/scripts/foodon_pass.py:64-105 to keep this validator
# stdlib-only. Any change there should be mirrored here.
# ---------------------------------------------------------------------------
_STOP_TOKENS = frozenset({
    "the", "a", "an", "of", "and", "or", "in", "on", "with",
    # Domain-stop words that appear in many media names but say nothing
    # specific (a match on these alone is too generic):
    "no", "nr", "type", "grade", "form", "powder", "solution",
    "extract", "broth", "infusion", "agar",
})


def _tokens(s: str) -> set[str]:
    """Lowercase tokens (alpha runs of length >= 2), minus stop words."""
    return {t for t in re.findall(r"[A-Za-z]{2,}", (s or "").lower())
            if t not in _STOP_TOKENS}


# ---------------------------------------------------------------------------
# Lazy MIM YAML chemistry lookup — minimal regex parser, no PyYAML.
# The validator only needs the truthiness of two flat scalar keys nested
# under the ``chemical_properties:`` block: ``cas_rn`` and ``pubchem_cid``
# (the schema name; the spec calls it ``pubchem`` — both spellings are
# accepted to be robust to either source).
# ---------------------------------------------------------------------------
_CHEM_BLOCK_RE = re.compile(
    r"^chemical_properties:\s*$(.*?)(?=^\S|\Z)",
    re.MULTILINE | re.DOTALL,
)
_SCALAR_RE = re.compile(r"^\s+(\w+):\s*(.+?)\s*$", re.MULTILINE)


def _yaml_path_for_subject(subject_id: str) -> Path:
    """Map ``MIM:<slug>`` -> ``data/ingredients/mapped/<slug>.yaml``."""
    if not subject_id.startswith("MIM:"):
        return INGREDIENTS_DIR / f"{subject_id}.yaml"
    return INGREDIENTS_DIR / f"{subject_id[4:]}.yaml"


def has_registry_chemistry(subject_id: str) -> bool:
    """True iff the subject's YAML carries a non-empty ``cas_rn`` or
    ``pubchem_cid`` (a.k.a. ``pubchem``) under ``chemical_properties:``.

    Intentionally tolerant: returns False on missing-file / parse-error.
    """
    path = _yaml_path_for_subject(subject_id)
    try:
        text = path.read_text(encoding="utf-8")
    except (FileNotFoundError, OSError):
        return False
    block_match = _CHEM_BLOCK_RE.search(text)
    if not block_match:
        return False
    block = block_match.group(1)
    for key, value in _SCALAR_RE.findall(block):
        if key not in ("cas_rn", "pubchem_cid", "pubchem"):
            continue
        v = value.strip().strip('"').strip("'")
        if v and v.lower() not in ("null", "~", "none"):
            return True
    return False


# ---------------------------------------------------------------------------
# SSSOM I/O — handle the YAML-prelude header block by streaming until the
# first non-comment line, which is the column header.
# ---------------------------------------------------------------------------
def _read_sssom(path: Path) -> tuple[list[str], list[str], list[dict[str, str]]]:
    """Return (prelude_lines, fieldnames, rows). Prelude lines start with
    '#' and are preserved verbatim for round-trip writing."""
    prelude: list[str] = []
    with path.open("r", encoding="utf-8", newline="") as f:
        header_line: str | None = None
        for line in f:
            if line.startswith("#"):
                prelude.append(line.rstrip("\n"))
                continue
            header_line = line.rstrip("\n")
            break
        if header_line is None:
            raise ValueError(f"{path}: no column header found")
        fieldnames = header_line.split("\t")
        reader = csv.DictReader(f, fieldnames=fieldnames, delimiter="\t")
        rows = [dict(r) for r in reader]
    return prelude, fieldnames, rows


def _write_reject_tsv(
    path: Path,
    prelude: list[str],
    fieldnames: list[str],
    rejects: list[tuple[dict[str, str], str]],
) -> None:
    """Write the rejects to ``needs_curator_review.tsv`` with the SSSOM
    prelude preserved and an extra trailing ``reject_reason`` column."""
    out_fields = list(fieldnames) + ["reject_reason"]
    with path.open("w", encoding="utf-8", newline="") as f:
        for line in prelude:
            f.write(line + "\n")
        writer = csv.DictWriter(
            f, fieldnames=out_fields, delimiter="\t", extrasaction="ignore",
            lineterminator="\n",
        )
        writer.writeheader()
        for row, reason in rejects:
            out = dict(row)
            out["reject_reason"] = reason
            writer.writerow(out)


# ---------------------------------------------------------------------------
# Rule A
# ---------------------------------------------------------------------------
def _is_auto_classifier_only(source: str) -> bool:
    """True iff every pipe-separated tag in ``source`` is a
    ``MIM:curator=...`` automation stamp AND at least one is one of the
    declared auto-pipeline tags. A non-curator tag (``MIM:CultureBotHT``,
    ``MIM:cbclaw_review_fix``, ``MIM:CultureMech``, ``MIM:manual review …``,
    etc.) means a human touched the row — accept."""
    tags = [t.strip() for t in (source or "").split("|") if t.strip()]
    if not tags:
        return False
    if not all(t.startswith(CURATOR_TAG_PREFIX) for t in tags):
        return False
    # at least one tag is a declared auto-classifier pipeline
    return any(t in AUTO_PIPELINE_TAGS for t in tags)


def _confidence(row: dict[str, str]) -> float:
    raw = (row.get("confidence") or "").strip()
    if not raw:
        return 0.0
    try:
        return float(raw)
    except ValueError:
        return 0.0


def evaluate_rule_a(rows: Iterable[dict[str, str]]) -> Iterator[tuple[int, dict[str, str], str]]:
    """Yield ``(row_number, row, reason)`` for every Rule A reject.
    Row numbers are 1-based, counting from the data row (header is row 0)."""
    for idx, row in enumerate(rows, start=1):
        source = row.get("source", "") or ""
        if not _is_auto_classifier_only(source):
            continue  # human-touched — accept

        # tier 1: high confidence
        if _confidence(row) >= CONFIDENCE_TIER:
            continue

        # tier 2: token-overlap on labels
        sl = _tokens(row.get("subject_label", ""))
        ol = _tokens(row.get("object_label", ""))
        if sl & ol:
            continue

        # tier 3: registry corroboration via subject YAML
        subject_id = (row.get("subject_id") or "").strip()
        if subject_id and has_registry_chemistry(subject_id):
            continue

        reason = (
            "auto-classifier row with confidence<0.95, zero token overlap "
            "between subject_label and object_label, and no CAS/PubChem "
            "corroboration in subject YAML"
        )
        yield idx, row, reason


# TODO PR2: extend with Rules B1-B4 (registry/identity row mandate,
# at-most-one row per (subject_id, object_id), narrowMatch-vs-exactMatch
# disjointness, canonical object_label drift). See plan section "PR2 —
# Group B".


def main(argv: list[str]) -> int:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument(
        "sssom_path",
        nargs="?",
        type=Path,
        default=DEFAULT_SSSOM,
        help=f"path to SSSOM TSV (default: {DEFAULT_SSSOM.relative_to(REPO_ROOT)})",
    )
    p.add_argument(
        "--reject-tsv",
        type=Path,
        default=DEFAULT_REJECT_TSV,
        help=(
            "where to write rejected rows "
            f"(default: {DEFAULT_REJECT_TSV.relative_to(REPO_ROOT)})"
        ),
    )
    args = p.parse_args(argv[1:])

    if not args.sssom_path.is_file():
        print(f"ERROR: SSSOM file not found at {args.sssom_path}", file=sys.stderr)
        return 1

    prelude, fieldnames, rows = _read_sssom(args.sssom_path)
    rejects = list(evaluate_rule_a(rows))

    args.reject_tsv.parent.mkdir(parents=True, exist_ok=True)
    _write_reject_tsv(
        args.reject_tsv,
        prelude,
        fieldnames,
        [(row, reason) for _, row, reason in rejects],
    )

    try:
        reject_display = args.reject_tsv.resolve().relative_to(REPO_ROOT)
    except ValueError:
        reject_display = args.reject_tsv

    if not rejects:
        print(f"OK: {args.sssom_path.name} passed Rule A (auto-classifier "
              f"token-overlap gate). {reject_display} "
              f"written with header only.")
        return 0

    print(
        f"FAIL: {len(rejects)} row(s) in {args.sssom_path.name} fail Rule A "
        f"(auto-classifier token-overlap gate).",
        file=sys.stderr,
    )
    print(
        "Each row below is stamped only with MIM:curator=... automation "
        "tags, has confidence < 0.95, has zero discriminating-token overlap "
        "between subject_label and object_label, and lacks an independent "
        "CAS-RN / PubChem corroboration in its MIM YAML.",
        file=sys.stderr,
    )
    for row_num, row, reason in rejects:
        subject = row.get("subject_label", "?")
        subject_id = row.get("subject_id", "?")
        object_id = row.get("object_id", "?")
        object_label = row.get("object_label", "?")
        print(
            f"  row {row_num}: {subject_id} '{subject}' "
            f"-> {object_id} '{object_label}' — {reason}",
            file=sys.stderr,
        )
    print(
        f"\nRejects written to {reject_display}. "
        "Fix the offending row in MIM (re-emit via the claw builder, or "
        "add a non-curator tag to the source column once a human has "
        "vetted it), or remove the row from the SSSOM. CI fails while a "
        "violating row remains in ingredient_mappings.sssom.tsv.",
        file=sys.stderr,
    )
    return 2


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
