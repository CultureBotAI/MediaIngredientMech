"""The published SSSOM must still carry each record's CAS in `other` (#403).

`CAS:<rn>` in the `other` column is how the orderable number reaches KGX as a
synonym: kg-microbe's consolidator splits `other` on `|` and extends the
ontology entity's synonym list, but **only for symmetric rows**. The KG node
optimises for how it reads; the CAS keeps it findable (#398).

The tokens are fragile in a specific way that no existing check catches. They
are written into a *column*, and the file is regenerated wholesale by
`culturebotai-claw/scripts/build_mim_ingredient_sssom.py` followed by
`publish_sssom.py`. That publisher refuses to promote when the **row count**
would drop — which is exactly the wrong invariant here, because rebuilding
`other` without CAS support changes no row count at all. The whole 1,733-token
population can vanish through a green pipeline.

So this asserts the property directly against the published artifact: if a
record has a CAS and its row is symmetric, the row carries the token. It fails
loudly on a rebuild by a builder that lacks the fix, rather than letting the
loss reach the graph.

Deliberately NOT asserted:

* a fixed count. Merges and regroundings legitimately move rows, and a hard
  1,733 would fail for reasons unrelated to CAS loss.
* anything about asymmetric rows. A CAS there is dropped by kg-microbe and
  would wrongly imply the broader parent is purchasable under the child's
  number, so its absence is correct, and the test pins that too.
"""
from __future__ import annotations

import csv
from pathlib import Path

import pytest
import yaml

ROOT = Path(__file__).resolve().parent.parent
SSSOM = ROOT / "mappings" / "ingredient_mappings.sssom.tsv"
MAPPED = ROOT / "data" / "curated" / "mapped_ingredients.yaml"
SYMMETRIC = {"skos:exactMatch", "skos:closeMatch"}


def _cas_for(rec: dict) -> str | None:
    """The CAS a lab would order by — supplied form wins over the denoted one."""
    for sf in rec.get("supplied_form") or []:
        if (sf or {}).get("cas_rn") and str(sf["cas_rn"]).strip():
            return str(sf["cas_rn"]).strip()
    rn = str((rec.get("chemical_properties") or {}).get("cas_rn") or "").strip()
    return rn or None


@pytest.fixture(scope="module")
def rows() -> list[dict]:
    text = [l for l in SSSOM.read_text(encoding="utf-8").splitlines(keepends=True)
            if not l.startswith("#")]
    return list(csv.DictReader(text, delimiter="\t"))


@pytest.fixture(scope="module")
def records() -> dict[str, dict]:
    data = yaml.safe_load(MAPPED.read_text(encoding="utf-8")) or {}
    return {str(r.get("preferred_term")): r for r in data.get("ingredients", [])}


def _tokens(row: dict) -> set[str]:
    return {p.strip().lower() for p in (row.get("other") or "").split("|") if p.strip()}


def test_symmetric_rows_carry_their_records_cas(rows, records):
    """Every symmetric row whose record has a CAS must publish it in `other`."""
    missing = []
    for row in rows:
        if row["predicate_id"] not in SYMMETRIC:
            continue
        rec = records.get(row["subject_label"])
        if rec is None:
            continue
        cas = _cas_for(rec)
        if cas and f"cas:{cas}".lower() not in _tokens(row):
            missing.append((row["subject_label"], cas, row["object_id"]))

    assert not missing, (
        f"{len(missing)} symmetric row(s) lost the CAS token from `other`, so the "
        f"orderable number no longer reaches KGX as a synonym (#403).\n"
        f"The likeliest cause is a rebuild by a builder without the CAS fix — "
        f"publish_sssom.py guards on row count, which does not move when a column "
        f"is rebuilt. Re-run scripts/publish_cas_as_synonym.py --apply to restore, "
        f"and check culturebotai-claw has the #403 builder change.\n"
        f"First few: {missing[:5]}")


def test_every_symmetric_row_resolves_to_a_record(rows, records):
    """Close the gate's own escape hatch.

    The check above looks each row's record up by `subject_label` and skips
    when there is no match — which would let a row quietly stop being checked
    rather than fail, exactly when something upstream renamed subjects or left
    a row behind a merge. All 2,802 symmetric rows resolve today, so this
    costs nothing now and turns that silent skip into a visible failure later.
    """
    orphans = [(r["subject_id"], r["subject_label"], r["object_id"])
               for r in rows
               if r["predicate_id"] in SYMMETRIC
               and r["subject_label"] not in records]
    assert not orphans, (
        f"{len(orphans)} symmetric row(s) name a subject_label that matches no "
        f"record, so the CAS check silently skips them: {orphans[:5]}")


def test_no_cas_tokens_on_asymmetric_rows(rows):
    """kg-microbe drops `other` on narrow/broadMatch — a CAS there is a claim
    that the broader parent is purchasable under the child's number."""
    stray = [(r["subject_label"], r["object_id"], r["predicate_id"])
             for r in rows
             if r["predicate_id"] not in SYMMETRIC
             and any(t.startswith("cas:") for t in _tokens(r))]
    assert not stray, (
        f"{len(stray)} asymmetric row(s) carry a CAS in `other`: {stray[:5]}. "
        f"kg-microbe does not merge `other` into the parent entity for these, so "
        f"the token is dead weight — and if it were merged it would assert the "
        f"broader term is orderable under this record's number.")


def test_the_population_is_not_silently_empty(rows):
    """A floor, not a fixed count: curation moves rows, but a collapse to near
    zero means the column was rebuilt without CAS support rather than curated."""
    n = sum(1 for r in rows if any(t.startswith("cas:") for t in _tokens(r)))
    assert n > 1000, (
        f"only {n} row(s) carry a CAS token; ~1,700 is the curated population. "
        f"This is the shape of a wholesale rebuild dropping the column, not of "
        f"incremental curation.")
