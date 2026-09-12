#!/usr/bin/env python3
"""Keep mappings/ingredient_mappings.sssom.tsv in sync with the curated collection.

The SSSOM file has no full generator: its `validation_method` / per-row `source`
provenance encode historical pipeline-run state that is not present in the curated
YAML, so it cannot be byte-faithfully regenerated. This tool instead reconciles
the *mapping content* against the curated data (the source of truth) — the failure
mode that let it drift silently before. It complements
`validate_sssom_invariants.py` (structural invariants) by checking *currency*.

Drift kinds (curated MAPPED records with an ontology_id are authoritative):
  GAP     — a mapped record has no SSSOM subject row (reported, not auto-added:
            full new-row provenance can't be synthesised)
  ORPHAN  — an SSSOM subject has no mapped record (record removed or now REJECTED)
  STALE   — the subject's ontology row carries an id other than the record's
            current ontology_id (e.g. curated migrated to a generic/parent term)
  PREDICATE — the current non-identity ontology row has a predicate other than
              the one implied by the record's mapping_quality

Modes:
  --check (default)  read-only; print drift; exit 1 if any (use as a CI gate)
  --apply --date D   reconcile STALE rows, sync PREDICATE-only drift, and drop
                     ORPHAN rows; GAPs are reported for manual handling

Usage:
    python scripts/reconcile_sssom.py
    python scripts/reconcile_sssom.py --apply --date 2026-06-05
"""

import argparse
import csv
import io
import sys
from collections import defaultdict
from pathlib import Path

import yaml

# Resolve paths relative to the repo root (this file lives in scripts/), so the
# tool and its tests work regardless of the current working directory.
_REPO = Path(__file__).resolve().parent.parent
SSSOM = _REPO / "mappings" / "ingredient_mappings.sssom.tsv"
CURATED = _REPO / "data" / "curated" / "mapped_ingredients.yaml"

# One table, shared with every other writer (#385). It used to be duplicated
# here and in promote_resolved_unmapped, where three prefixes were missing.
# This script carried no package import before that, so it takes the same
# sys.path bootstrap its sibling writers use rather than starting to require an
# installed package to run (#603).
sys.path.insert(0, str(_REPO / "src"))
from mediaingredientmech.sssom_grading import (  # noqa: E402
    CONFIDENCE,
    PREDICATE,
    justification_for,
)
from mediaingredientmech.utils.object_source import OBJECT_SOURCE  # noqa: E402

# Object-id prefixes that denote an ONTOLOGY mapping row (vs a registry/identity
# row such as cas: / kgmicrobe.*). The stale ontology row must be recognised by
# its object_id PREFIX, not by an `obo:` object_source: MeSH is an ontology
# source here but its object_source is `registry:mesh`, so a MeSH→OBO parent
# remap (e.g. mesh:D013025 → CHEBI:28874) was previously invisible to --apply —
# Pass 1 only captured `obo:`-sourced rows, so the stale mesh row was never
# rewritten (`synced 0`). Matched case-insensitively: data carries lowercase
# `mesh:` while the OBJECT_SOURCE keys (and OBO CURIEs) are uppercase.
ONTOLOGY_PREFIXES = frozenset(
    p.casefold()
    for p in ([k for k, v in OBJECT_SOURCE.items() if v.startswith("obo:")] + ["MESH"])
)


def _is_ontology_row(object_id: str) -> bool:
    """True if ``object_id``'s CURIE prefix is an ontology (not a registry id)."""
    return object_id.split(":", 1)[0].casefold() in ONTOLOGY_PREFIXES


def expected_mappings(curated: dict) -> dict[str, dict]:
    """preferred_term -> ontology_mapping for MAPPED records carrying an ontology_id."""
    out = {}
    for r in curated["ingredients"]:
        if r.get("mapping_status") == "MAPPED":
            om = r.get("ontology_mapping") or {}
            if om.get("ontology_id"):
                out[r["preferred_term"]] = om
    return out


def expected_identifiers(curated: dict) -> dict[str, str]:
    """preferred_term -> primary identifier for MAPPED ontology-grounded records."""
    out = {}
    for r in curated["ingredients"]:
        if r.get("mapping_status") == "MAPPED":
            om = r.get("ontology_mapping") or {}
            if om.get("ontology_id") and r.get("identifier"):
                out[r["preferred_term"]] = str(r["identifier"])
    return out


def _read_sssom():
    lines = SSSOM.read_text().splitlines(keepends=True)
    header = [ln for ln in lines if ln.startswith("#")]
    body = [ln for ln in lines if not ln.startswith("#")]
    rows = list(csv.DictReader(io.StringIO("".join(body)), delimiter="\t"))
    return header, body[0], body[1:], rows


def find_drift(curated: dict, rows: list[dict]) -> dict[str, list]:
    by_label: dict[str, list[dict]] = defaultdict(list)
    for row in rows:
        by_label[row["subject_label"]].append(row)
    expected = expected_mappings(curated)

    gaps = sorted(t for t in expected if t not in by_label)
    orphans = sorted(t for t in by_label if t not in expected)
    stale = []
    predicate = []
    grade: list = []
    primary_identifiers = expected_identifiers(curated)
    for term, om in sorted(expected.items()):
        if term not in by_label:
            continue
        if om["ontology_id"] not in {r["object_id"] for r in by_label[term]}:
            stale.append((term, om["ontology_id"], sorted(r["object_id"] for r in by_label[term])))
            continue
        quality = str(om.get("mapping_quality") or "")
        if quality not in PREDICATE:
            continue
        want = expected_grade(quality)
        for row in by_label[term]:
            object_id = row["object_id"]
            if not (
                object_id == om["ontology_id"]
                and object_id != primary_identifiers.get(term)
                and _is_ontology_row(object_id)
            ):
                continue
            have = row_grade(row)
            if have[0] != want[0]:
                predicate.append((term, object_id, want[0], have[0]))
            elif have != want:
                # Right predicate, stale grade metadata: invisible before #623,
                # because the detector keyed on the predicate while the writer
                # syncs all three columns together.
                fields = [
                    name
                    for name, got, expect in zip(
                        ("mapping_justification", "confidence"), have[1:], want[1:]
                    )
                    if got != expect
                ]
                grade.append((term, object_id, quality, fields, have, want))
    return {
        "gaps": gaps,
        "orphans": orphans,
        "stale": stale,
        "predicate": predicate,
        "grade": grade,
    }


def _canonical_label_resolver():
    """Return f(ontology_id) -> OBO-canonical label, required so synced rows pass
    Rule B4 (the curated ontology_label is often non-canonical, e.g. casing or a
    trade name). Resolves CHEBI from the local sqlite; other prefixes fall back to
    None (caller keeps the curated label, and validate_sssom_invariants will flag
    it if it violates B4)."""
    from oaklib import get_adapter

    adapters: dict = {}
    chebi_db = f"sqlite:///{Path.home() / '.data' / 'oaklib' / 'chebi.db'}"

    def resolve(oid: str) -> str | None:
        prefix = oid.split(":", 1)[0]
        if prefix != "CHEBI":
            return None
        try:
            if "CHEBI" not in adapters:
                adapters["CHEBI"] = get_adapter(chebi_db)
            return adapters["CHEBI"].label(oid)
        except Exception as e:  # missing sqlite cache, adapter failure, etc.
            print(f"  warning: could not resolve label for {oid} ({e}); "
                  "keeping curated ontology_label", file=sys.stderr)
            return None

    return resolve


def _append_comment(existing: str, note: str) -> str:
    """Append a reconciliation note without dropping any existing curator comment."""
    existing = (existing or "").strip()
    return f"{existing} {note}".strip() if existing else note


def _quality(ontology_mapping: dict) -> str:
    return str(ontology_mapping.get("mapping_quality") or "")


def _sync_quality_columns(fields: list[str], column: dict[str, int], quality: str) -> None:
    fields[column["predicate_id"]] = PREDICATE[quality]
    fields[column["mapping_justification"]] = justification_for(quality)
    fields[column["confidence"]] = CONFIDENCE[quality]


def expected_grade(quality: str) -> tuple[str, str, str]:
    """
    Return the (predicate, justification, confidence) a quality implies.

    `_sync_quality_columns` writes all three together, so all three are what
    "in sync" has to mean. Keying drift on the predicate alone let a row keep
    the right predicate with stale justification or confidence and still be
    reported as clean (#623).

    :param quality: The record's `ontology_mapping.mapping_quality`.
    :return: The grade triple the published row should carry.
    """
    return PREDICATE[quality], justification_for(quality), str(CONFIDENCE[quality])


def row_grade(row: dict) -> tuple[str, str, str]:
    """
    Return the (predicate, justification, confidence) a published row carries.

    :param row: One parsed SSSOM row.
    :return: The grade triple as published.
    """
    return (
        row.get("predicate_id") or "",
        row.get("mapping_justification") or "",
        row.get("confidence") or "",
    )


def apply_reconcile(curated: dict, date: str) -> tuple[int, int, int, int]:
    header, col_line, data_lines, rows = _read_sssom()
    cols = col_line.rstrip("\n").split("\t")
    idx = {c: i for i, c in enumerate(cols)}
    expected = expected_mappings(curated)
    primary_identifiers = expected_identifiers(curated)
    canonical_label = _canonical_label_resolver()

    # Pass 1: per stale subject, record (old id, new id, old predicate-local,
    # new predicate-local) so we can also fix registry/identity rows whose
    # comments embed the old parent id and/or its old predicate word (e.g.
    # "...for narrowMatch subject ... parent mesh:Dxxx").
    remap: dict[str, tuple[str, str, str, str]] = {}
    for r in rows:
        term = r["subject_label"]
        if term in expected and _is_ontology_row(r["object_id"]):
            new_id = expected[term]["ontology_id"]
            if r["object_id"] != new_id:
                old_pred = r["predicate_id"].split(":", 1)[-1]
                new_pred = PREDICATE[_quality(expected[term])].split(":", 1)[-1]
                remap[term] = (r["object_id"], new_id, old_pred, new_pred)

    # Pass 2: rewrite.
    out, n_stale, n_orphan, n_predicate, n_grade = [], 0, 0, 0, 0
    for ln in data_lines:
        if not ln.strip():
            out.append(ln)
            continue
        f = ln.rstrip("\n").split("\t")
        term = f[idx["subject_label"]]
        if term not in expected:
            n_orphan += 1  # orphan subject: drop all of its rows
            continue
        if term in remap:
            old_id, new_id, old_pred, new_pred = remap[term]
            if _is_ontology_row(f[idx["object_id"]]) and f[idx["object_id"]] == old_id:
                # The stale ontology row: sync to the current curated mapping.
                om = expected[term]
                f[idx["object_id"]] = new_id
                # Use the OBO-canonical label (Rule B4), not the curated ontology_label.
                f[idx["object_label"]] = canonical_label(new_id) or om.get("ontology_label") or ""
                f[idx["object_source"]] = OBJECT_SOURCE.get(om.get("ontology_source"), f[idx["object_source"]])
                _sync_quality_columns(f, idx, _quality(om))
                f[idx["mapping_date"]] = date
                if "comment" in idx:
                    f[idx["comment"]] = _append_comment(f[idx["comment"]], f"[reconciled to curated mapping {date}]")
                if "validation_method" in idx:
                    f[idx["validation_method"]] = f"manual:reconcile_sssom|REMAPPED|{date}"
                n_stale += 1
            elif "comment" in idx and (
                old_id in f[idx["comment"]]
                or (old_pred != new_pred and old_pred in f[idx["comment"]])
            ):
                # A registry/identity row whose comment still names the old parent
                # id and/or its old predicate word: update both so the file stays
                # internally consistent (predicate names like narrowMatch/broadMatch
                # are distinctive enough that a plain replace is safe).
                c = f[idx["comment"]].replace(old_id, new_id)
                if old_pred != new_pred:
                    c = c.replace(old_pred, new_pred)
                f[idx["comment"]] = c
        elif (
            _is_ontology_row(f[idx["object_id"]])
            and f[idx["object_id"]] == expected[term].get("ontology_id")
            and f[idx["object_id"]] != primary_identifiers.get(term)
        ):
            quality = _quality(expected[term])
            if quality in PREDICATE:
                want = expected_grade(quality)
                have = (
                    f[idx["predicate_id"]],
                    f[idx["mapping_justification"]] if "mapping_justification" in idx else want[1],
                    f[idx["confidence"]] if "confidence" in idx else want[2],
                )
                if have != want:
                    # Sync on any grade difference, not only a wrong predicate:
                    # the writer has always set all three, so a predicate-only
                    # trigger left justification and confidence stale (#623).
                    kind = "predicate" if have[0] != want[0] else "grade"
                    _sync_quality_columns(f, idx, quality)
                    f[idx["mapping_date"]] = date
                    if "comment" in idx:
                        f[idx["comment"]] = _append_comment(
                            f[idx["comment"]],
                            f"[{kind} reconciled to curated mapping {date}]",
                        )
                    if "validation_method" in idx:
                        f[idx["validation_method"]] = (
                            f"manual:reconcile_sssom|{kind.upper()}|{date}"
                        )
                    if kind == "predicate":
                        n_predicate += 1
                    else:
                        n_grade += 1
        out.append("\t".join(f) + "\n")

    new_header = []
    for ln in header:
        if ln.startswith("# mapping_set_version:"):
            ln = f'# mapping_set_version: "{date}"\n'
        elif ln.startswith("# mapping_date:"):
            ln = f'# mapping_date: "{date}"\n'
        new_header.append(ln)
    SSSOM.write_text("".join(new_header) + col_line + "".join(out))
    return n_stale, n_orphan, n_predicate, n_grade


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--apply", action="store_true", help="Reconcile (default: read-only check)")
    parser.add_argument("--date", help="Run date for --apply, e.g. 2026-06-05")
    args = parser.parse_args()

    curated = yaml.safe_load(CURATED.read_text())
    _, _, _, rows = _read_sssom()
    drift = find_drift(curated, rows)
    total = sum(len(v) for v in drift.values())

    print("SSSOM currency vs curated mapped records:")
    print(f"  GAP    (mapped record, no SSSOM row):   {len(drift['gaps'])}")
    for t in drift["gaps"][:50]:
        print(f"     - {t}")
    print(f"  ORPHAN (SSSOM row, no/REJECTED record): {len(drift['orphans'])}")
    for t in drift["orphans"][:50]:
        print(f"     - {t}")
    print(f"  STALE  (row lacks current ontology_id): {len(drift['stale'])}")
    for term, oid, present in drift["stale"][:50]:
        print(f"     - {term}: expected {oid}, present {present}")
    print(f"  PREDICATE (current ontology row, wrong predicate): {len(drift['predicate'])}")
    for term, oid, expected_predicate, present_predicate in drift["predicate"][:50]:
        print(
            f"     - {term}: {oid} expected {expected_predicate}, "
            f"present {present_predicate}"
        )
    print(f"  GRADE (right predicate, stale grade metadata):     {len(drift['grade'])}")
    for term, oid, quality, fields, have, want in drift["grade"][:50]:
        print(f"     - {term}: {oid} [{quality}] {', '.join(fields)}")
        for name, got, expect in zip(
            ("mapping_justification", "confidence"), have[1:], want[1:]
        ):
            if got != expect:
                print(f"         {name}: present {got!r}, expected {expect!r}")

    if not args.apply:
        if total == 0:
            print("\nOK: SSSOM is in sync with the curated data.")
            return 0
        print(f"\nDRIFT: {total} issue(s). Reconcile: python scripts/reconcile_sssom.py --apply --date <YYYY-MM-DD>")
        return 1

    if not args.date:
        print("\n--apply requires --date YYYY-MM-DD", file=sys.stderr)
        return 2
    if drift["gaps"]:
        print(f"\nNOTE: {len(drift['gaps'])} GAP(s) need new rows with full provenance — "
              "not auto-added; handle manually.")
    n_stale, n_orphan, n_predicate, n_grade = apply_reconcile(curated, args.date)
    print(
        f"\nApplied: synced {n_stale} stale row(s), removed {n_orphan} "
        f"orphan row(s), fixed {n_predicate} predicate row(s) and "
        f"{n_grade} grade row(s)."
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
