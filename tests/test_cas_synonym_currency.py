"""Preserve legacy CAS transport and separately verified node annotations.

The eleven #762 identities deliberately transport CAS as KGX node xref,
outside SSSOM synonyms. Only the exact subject/target/CAS triples captured
by the committed KG-Microbe runtime audit can use that route. Other rows
retain the original #403 `other`-column contract below.

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

So this asserts the property against the published artifact and the bounded
node-xref audit: a symmetric row with a CAS must retain a verified transport
route. An unrelated row cannot inherit a reviewed annotation allowance.

Deliberately NOT asserted:

* a fixed count. Merges and regroundings legitimately move rows, and a hard
  1,733 would fail for reasons unrelated to CAS loss.
* anything about asymmetric rows. A CAS there is dropped by kg-microbe and
  would wrongly imply the broader parent is purchasable under the child's
  number, so its absence is correct, and the test pins that too.
"""

from __future__ import annotations

import csv
import json
from pathlib import Path

import pytest
import yaml

ROOT = Path(__file__).resolve().parent.parent
SSSOM = ROOT / "mappings" / "ingredient_mappings.sssom.tsv"
MAPPED = ROOT / "data" / "curated" / "mapped_ingredients.yaml"
SYMMETRIC = {"skos:exactMatch", "skos:closeMatch"}
ANNOTATION_AUDIT = ROOT / (
    "reports/sssom_completion_20260921/mapping_review/"
    "identity-review-20260924/kgmicrobe-cas-transport.json"
)


@pytest.fixture(scope="module")
def annotation_routes():
    """Load exact triples whose separate node-xref transport was verified."""
    audit = json.loads(ANNOTATION_AUDIT.read_text())
    result = set()
    for item in audit["annotations"]:
        assert "cas:" + item["cas_rn"] in item["node_xrefs"]
        result.add((item["subject_id"], item["object_id"], item["cas_rn"]))
    return result


def _has_verified_node_xref(row, cas, annotation_routes):
    return (
        row["predicate_id"] == "skos:exactMatch"
        and (row["subject_id"], row["object_id"], cas) in annotation_routes
    )


def _cas_for(rec: dict) -> str | None:
    """The CAS a lab would order by — supplied form wins over the denoted one."""
    for sf in rec.get("supplied_form") or []:
        if (sf or {}).get("cas_rn") and str(sf["cas_rn"]).strip():
            return str(sf["cas_rn"]).strip()
    rn = str((rec.get("chemical_properties") or {}).get("cas_rn") or "").strip()
    return rn or None


@pytest.fixture(scope="module")
def rows() -> list[dict]:
    text = [
        line
        for line in SSSOM.read_text(encoding="utf-8").splitlines(keepends=True)
        if not line.startswith("#")
    ]
    return list(csv.DictReader(text, delimiter="\t"))


@pytest.fixture(scope="module")
def records() -> dict[str, dict]:
    data = yaml.safe_load(MAPPED.read_text(encoding="utf-8")) or {}
    return {str(r.get("preferred_term")): r for r in data.get("ingredients", [])}


def _tokens(row: dict) -> set[str]:
    return {p.strip().lower() for p in (row.get("other") or "").split("|") if p.strip()}


def test_symmetric_rows_carry_their_records_cas(rows, records, annotation_routes):
    """Every symmetric row must retain CAS through a verified output route."""
    missing = []
    for row in rows:
        if row["predicate_id"] not in SYMMETRIC:
            continue
        rec = records.get(row["subject_label"])
        if rec is None:
            continue
        cas = _cas_for(rec)
        if (
            cas
            and f"cas:{cas}".lower() not in _tokens(row)
            and not _has_verified_node_xref(row, cas, annotation_routes)
        ):
            missing.append((row["subject_label"], cas, row["object_id"]))

    assert not missing, (
        f"{len(missing)} symmetric row(s) have no CAS token in `other` and no "
        f"verified node-xref transport (#403, #762).\n"
        f"Check the source-specific publication route; a row-count gate cannot "
        f"detect a lost annotation. Do not restore historical or invalid CAS.\n"
        f"First few: {missing[:5]}"
    )


def test_verified_annotation_routes_still_match_current_rows(rows, records, annotation_routes):
    """The bounded alternative cannot hide a changed target or corrected CAS."""
    actual = set()
    for row in rows:
        rec = records.get(row["subject_label"])
        if rec and _has_verified_node_xref(row, _cas_for(rec), annotation_routes):
            assert rec["identifier"] == row["object_id"]
            actual.add((row["subject_id"], row["object_id"], _cas_for(rec)))
    assert actual == annotation_routes


@pytest.mark.parametrize("change", ["subject_id", "object_id", "predicate_id", "cas"])
def test_annotation_route_cannot_approve_an_unreviewed_triple(change, annotation_routes):
    """One changed component must lose the narrowly reviewed transport allowance."""
    row = {
        "subject_id": "MIM:Acriflavine",
        "object_id": "NCIT:C76253",
        "predicate_id": "skos:exactMatch",
    }
    cas = "65589-70-0"
    assert _has_verified_node_xref(row, cas, annotation_routes)
    if change == "cas":
        cas = "8048-52-0"
    else:
        row[change] = "unreviewed:value"
    assert not _has_verified_node_xref(row, cas, annotation_routes)


def test_every_symmetric_row_resolves_to_a_record(rows, records):
    """Close the gate's own escape hatch.

    The check above looks each row's record up by `subject_label` and skips
    when there is no match — which would let a row quietly stop being checked
    rather than fail, exactly when something upstream renamed subjects or left
    a row behind a merge. All 2,802 symmetric rows resolve today, so this
    costs nothing now and turns that silent skip into a visible failure later.
    """
    orphans = [
        (r["subject_id"], r["subject_label"], r["object_id"])
        for r in rows
        if r["predicate_id"] in SYMMETRIC and r["subject_label"] not in records
    ]
    assert not orphans, (
        f"{len(orphans)} symmetric row(s) name a subject_label that matches no "
        f"record, so the CAS check silently skips them: {orphans[:5]}"
    )


def test_no_cas_tokens_on_asymmetric_rows(rows):
    """kg-microbe drops `other` on narrow/broadMatch — a CAS there is a claim
    that the broader parent is purchasable under the child's number."""
    stray = [
        (r["subject_label"], r["object_id"], r["predicate_id"])
        for r in rows
        if r["predicate_id"] not in SYMMETRIC and any(t.startswith("cas:") for t in _tokens(r))
    ]
    assert not stray, (
        f"{len(stray)} asymmetric row(s) carry a CAS in `other`: {stray[:5]}. "
        f"kg-microbe does not merge `other` into the parent entity for these, so "
        f"the token is dead weight — and if it were merged it would assert the "
        f"broader term is orderable under this record's number."
    )


def test_the_population_is_not_silently_empty(rows):
    """A floor, not a fixed count: curation moves rows, but a collapse to near
    zero means the column was rebuilt without CAS support rather than curated."""
    n = sum(1 for r in rows if any(t.startswith("cas:") for t in _tokens(r)))
    assert n > 1000, (
        f"only {n} row(s) carry a CAS token; ~1,700 is the curated population. "
        f"This is the shape of a wholesale rebuild dropping the column, not of "
        f"incremental curation."
    )


def test_no_row_publishes_a_cas_its_record_does_not_carry(rows, records):
    """The reverse direction, which was unguarded (#501).

    `test_symmetric_rows_carry_their_records_cas` checks that a record's CAS
    REACHES `other`. Nothing checked that a CAS in `other` still corresponds to
    the record. So adding was guarded, correcting was guarded (the old value
    fails the equality check), and REMOVING was not -- the row is simply skipped
    as "no CAS on record".

    Removal is the case where the published value is most likely to be wrong
    rather than merely stale. #500 removed 20 CAS numbers that named a hydrate's
    ANHYDROUS parent, and all 20 kept publishing to KGX until this was added.

    `_cas_for` is deliberately reused rather than reading `chemical_properties`
    directly: a `supplied_form` CAS is the number a lab orders by and is
    legitimate even when the denoted form carries none. Reading the wrong field
    strips D-lyxose's real value.
    """
    orphans = []
    for row in rows:
        record = records.get(row.get("subject_label", ""))
        if record is None:
            continue
        expected = _cas_for(record)
        for token in _tokens(row):
            if token.startswith("cas:") and token[4:] != (expected or "").lower():
                orphans.append((row.get("subject_label"), token, expected))

    assert not orphans, (
        f"{len(orphans)} row(s) publish a CAS the record does not carry, which "
        f"reaches KGX as a synonym: {orphans[:4]}"
    )
