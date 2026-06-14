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

Modes:
  --check (default)  read-only; print drift; exit 1 if any (use as a CI gate)
  --apply --date D   reconcile STALE (rewrite the ontology row from curated) and
                     drop ORPHAN rows; GAPs are reported for manual handling

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

OBJECT_SOURCE = {
    "CHEBI": "obo:chebi.owl", "FOODON": "obo:foodon.owl", "ENVO": "obo:envo.owl",
    "UBERON": "obo:uberon.owl", "NCIT": "obo:ncit.owl", "MICRO": "obo:micro.owl",
    "BTO": "obo:bto.owl", "MESH": "registry:mesh", "CAS": "registry:cas",
    "kgmicrobe.compound": "kgm:compound", "kgmicrobe.ingredient": "kgm:ingredient",
}
PREDICATE = {
    "EXACT_MATCH": "skos:exactMatch", "CLOSE_MATCH": "skos:closeMatch",
    "SYNONYM_MATCH": "skos:exactMatch", "NARROW_MATCH": "skos:narrowMatch",
    "BROAD_MATCH": "skos:broadMatch",
}

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
    for term, om in sorted(expected.items()):
        if term in by_label and om["ontology_id"] not in {r["object_id"] for r in by_label[term]}:
            stale.append((term, om["ontology_id"], sorted(r["object_id"] for r in by_label[term])))
    return {"gaps": gaps, "orphans": orphans, "stale": stale}


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


def apply_reconcile(curated: dict, date: str) -> tuple[int, int]:
    header, col_line, data_lines, rows = _read_sssom()
    cols = col_line.rstrip("\n").split("\t")
    idx = {c: i for i, c in enumerate(cols)}
    expected = expected_mappings(curated)
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
                new_pred = PREDICATE.get(
                    expected[term].get("mapping_quality"), r["predicate_id"]
                ).split(":", 1)[-1]
                remap[term] = (r["object_id"], new_id, old_pred, new_pred)

    # Pass 2: rewrite.
    out, n_stale, n_orphan = [], 0, 0
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
                f[idx["predicate_id"]] = PREDICATE.get(om.get("mapping_quality"), f[idx["predicate_id"]])
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
        out.append("\t".join(f) + "\n")

    new_header = []
    for ln in header:
        if ln.startswith("# mapping_set_version:"):
            ln = f'# mapping_set_version: "{date}"\n'
        elif ln.startswith("# mapping_date:"):
            ln = f'# mapping_date: "{date}"\n'
        new_header.append(ln)
    SSSOM.write_text("".join(new_header) + col_line + "".join(out))
    return n_stale, n_orphan


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
    n_stale, n_orphan = apply_reconcile(curated, args.date)
    print(f"\nApplied: synced {n_stale} stale row(s), removed {n_orphan} orphan row(s).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
