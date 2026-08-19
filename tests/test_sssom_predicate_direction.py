"""Pin the asymmetric-predicate direction until both repos change together (#390).

**This test asserts something that is wrong by the SKOS spec, on purpose.**

`MAPPING_SEMANTICS.md` defines `skos:narrowMatch` as *"MIM:X is a kind-of Y (Y is
the broader/parent term)"*. SKOS says the opposite: `skos:narrowMatch` is a
sub-property of `skos:narrower`, so `A narrowMatch B` asserts **B is narrower
than A**. Under the spec, "MIM:X is a kind-of Y" is `skos:broadMatch`.

Nothing is broken today because kg-microbe reads the predicates the same inverted
way MIM writes them (`kg_microbe/utils/chemical_mapping_utils.py`):

    if predicate == "skos:narrowMatch":
        parent_sets.setdefault(subject, set()).add(curie)   # object is the parent
    if predicate == "skos:broadMatch":
        parent_sets.setdefault(curie, set()).add(subject)   # subject is the parent

The two repos agree, both differ from SKOS, and every asymmetric row produces a
correct `biolink:subclass_of` edge.

**So a one-sided fix inverts 141 subclass edges.** Someone reading the spec
against this corpus would reasonably flip MIM to `broadMatch` — and that is
precisely the change that breaks the graph, silently, producing a plausible-
looking result. This test exists to stop that landing alone.

Coordination is tracked in MIM #390 and Knowledge-Graph-Hub/kg-microbe#822. When
both sides are ready, the flip is: MIM re-emits these rows as `broadMatch`,
kg-microbe swaps the two branches above, **and this test is updated in the same
change**. If you are here because it failed, that is the question to answer: is
the kg-microbe half landing too?
"""

import csv
from pathlib import Path

ROOT = Path(__file__).parent.parent
SSSOM = ROOT / "mappings" / "ingredient_mappings.sssom.tsv"

ASYMMETRIC = {"skos:narrowMatch", "skos:broadMatch"}


def _rows():
    with SSSOM.open(encoding="utf-8") as fh:
        return list(csv.DictReader(
            (l for l in fh if not l.startswith("#")), delimiter="\t"))


def test_asymmetric_rows_use_narrowmatch_not_broadmatch():
    """The convention is narrowMatch for "MIM:X is a kind-of Y".

    Not because it is right by SKOS -- it is not -- but because kg-microbe's
    parent-index reads it that way, so the two must move together.
    """
    rows = _rows()
    asym = [r for r in rows if r["predicate_id"] in ASYMMETRIC]
    broad = [r for r in asym if r["predicate_id"] == "skos:broadMatch"]
    assert asym, "no asymmetric rows at all — has the corpus changed shape?"
    assert not broad, (
        f"{len(broad)} skos:broadMatch row(s) found, e.g. "
        f"{[(r['subject_label'], r['object_id']) for r in broad[:3]]}.\n"
        f"MIM's convention is narrowMatch for 'MIM:X is a kind-of Y'. That is "
        f"inverted relative to SKOS, and kg-microbe is inverted the same way, so "
        f"they agree. Emitting broadMatch here makes kg-microbe index the SUBJECT "
        f"as the parent — the edge points the wrong way.\n"
        f"If this is the coordinated flip (#390, kg-microbe#822), update this test "
        f"in the same change and confirm the kg-microbe half is landing too.")


def test_every_asymmetric_subject_has_its_registry_row():
    """Rule B1, restated as a test.

    The parent-index translates `MIM:<slug>` to a kg-microbe primary using the
    sibling registry exactMatch row. Without it the asymmetric row still parses
    but the subject never resolves, so the edge is dropped rather than inverted —
    a different failure, equally silent.
    """
    rows = _rows()
    by_subject = {}
    for r in rows:
        by_subject.setdefault(r["subject_id"], []).append(r)

    missing = []
    for r in rows:
        if r["predicate_id"] not in ASYMMETRIC:
            continue
        subject = r["subject_id"]
        if not subject.startswith("MIM:"):
            continue
        slug = subject[4:].lower()
        ok = any(
            s["predicate_id"] == "skos:exactMatch"
            and s["object_id"].startswith(("kgmicrobe.ingredient:", "kgmicrobe.compound:"))
            and s["object_id"].split(":", 1)[1] == slug
            for s in by_subject[subject]
        )
        if not ok:
            missing.append(subject)
    assert not missing, (
        f"{len(missing)} asymmetric subject(s) lack the registry exactMatch row "
        f"whose object local-part equals the subject slug: {sorted(set(missing))[:5]}. "
        f"Note the local part must match the slug EXACTLY, hyphens included — "
        f"`MIM:Dry_Cow-manure` needs `kgmicrobe.ingredient:dry_cow-manure`, not "
        f"`dry_cow_manure`.")
