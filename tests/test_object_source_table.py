"""One object_source table, and a lookup that refuses to guess (#385, #386).

There were three: eleven prefixes in `reconcile_sssom`, eight in
`promote_resolved_unmapped`, three registry prefixes in `reground_mapped_record`.
The promotion table was missing `cas`, `kgmicrobe.compound` and
`kgmicrobe.ingredient` -- 682 of the 2,999 published rows -- and every writer
looked the value up with `.get(prefix, "")`, so promoting to one of those wrote
an empty `object_source` and nothing raised. Rule C catches the result; nothing
stopped it being written.
"""

from __future__ import annotations

import csv
from pathlib import Path

import pytest

from mediaingredientmech.utils.object_source import (
    OBJECT_SOURCE,
    UnknownObjectSource,
    object_source_for,
    prefix_of,
)

SSSOM = Path(__file__).parent.parent / "mappings" / "ingredient_mappings.sssom.tsv"


@pytest.mark.parametrize(
    "curie,expected",
    [
        ("CHEBI:17234", "obo:chebi.owl"),
        ("cas:50-99-7", "registry:cas"),
        ("kgmicrobe.compound:x", "kgm:compound"),
        ("kgmicrobe.ingredient:x", "kgm:ingredient"),
        ("mesh:C000709627", "registry:mesh"),
        ("MICRO:0000455", "obo:micro.owl"),
    ],
)
def test_it_resolves_every_published_shape(curie, expected):
    assert object_source_for(curie) == expected


def test_a_bare_prefix_works_too():
    assert object_source_for("CHEBI") == "obo:chebi.owl"


@pytest.mark.parametrize("curie", ["mesh:C1", "MESH:C1", "MeSH:C1"])
def test_prefix_matching_is_case_insensitive(curie):
    """`mesh:` is lowercase in the corpus while OBO CURIEs are upper."""
    assert object_source_for(curie) == "registry:mesh"


def test_an_undeclared_prefix_raises_rather_than_returning_empty():
    """The #386 defect, refused at the point of writing."""
    with pytest.raises(UnknownObjectSource) as excinfo:
        object_source_for("GO:0008150")
    assert "GO" in str(excinfo.value)
    assert "object_source" in str(excinfo.value)


def test_prefix_of_handles_both_forms():
    assert prefix_of("CHEBI:17234") == "CHEBI"
    assert prefix_of("CHEBI") == "CHEBI"


def test_the_table_covers_every_prefix_the_corpus_actually_publishes():
    """The check that would have caught #385 when the tables diverged."""
    with SSSOM.open(encoding="utf-8") as handle:
        rows = [line for line in handle if not line.startswith("#")]
    published = {r["object_id"].split(":", 1)[0] for r in csv.DictReader(rows, delimiter="\t")}
    missing = sorted(p for p in published if p.upper() not in {k.upper() for k in OBJECT_SOURCE})
    assert not missing, f"published prefixes with no declared object_source: {missing}"


def test_every_published_row_agrees_with_the_table():
    """Ties the table to the artifact, not just to itself."""
    with SSSOM.open(encoding="utf-8") as handle:
        rows = [line for line in handle if not line.startswith("#")]
    wrong = [
        (r["subject_id"], r["object_id"], r["object_source"])
        for r in csv.DictReader(rows, delimiter="\t")
        if r["object_source"] != object_source_for(r["object_id"])
    ]
    assert not wrong, f"{len(wrong)} rows disagree with the table, e.g. {wrong[:3]}"


@pytest.mark.parametrize(
    "script",
    [
        "reconcile_sssom.py",
        "promote_resolved_unmapped.py",
        "move_mapped_out_of_unmapped_collection.py",
        "create_records_from_groundings.py",
        "reground_mapped_record.py",
        "promote_microbedecoder_reviewed.py",
    ],
)
def test_no_writer_keeps_a_silent_empty_lookup(script):
    """`.get(prefix, "")` is the shape that published the blank cells."""
    source = (Path(__file__).parent.parent / "scripts" / script).read_text(encoding="utf-8")
    for bad in ('OBJECT_SOURCE.get(', 'REGISTRY_SOURCE.get('):
        for line in source.splitlines():
            if bad in line and '""' in line:
                pytest.fail(f"{script} still falls back to an empty object_source: {line.strip()}")


def test_promotable_is_not_derived_from_the_shared_table():
    """Sharing the fuller table must not silently widen promotion policy."""
    import importlib.util

    path = Path(__file__).parent.parent / "scripts" / "promote_resolved_unmapped.py"
    source = path.read_text(encoding="utf-8")
    assert "PROMOTABLE = frozenset(OBJECT_SOURCE)" not in source
    assert "cas" not in source.split("PROMOTABLE = frozenset(")[1].split(")")[0]
