from __future__ import annotations

import csv
import importlib.util
import io
import sys
from pathlib import Path

SCRIPT = Path(__file__).parent.parent / "scripts" / "publish_cas_as_synonym.py"
SPEC = importlib.util.spec_from_file_location("publish_cas_as_synonym", SCRIPT)
mod = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = mod
SPEC.loader.exec_module(mod)

FIELDS = [
    "subject_id",
    "subject_label",
    "predicate_id",
    "object_id",
    "object_label",
    "object_source",
    "mapping_justification",
    "source",
    "mapping_date",
    "confidence",
    "comment",
    "other",
    "validation_method",
]


def _sssom_text(*rows: dict[str, str]) -> str:
    out = io.StringIO()
    out.write('# mapping_set_id: "https://example.org/mim"\n')
    writer = csv.DictWriter(
        out,
        fieldnames=FIELDS,
        delimiter="\t",
        lineterminator="\n",
    )
    writer.writeheader()
    writer.writerows(rows)
    return out.getvalue()


def _row(other: str, predicate: str = "skos:exactMatch") -> dict[str, str]:
    return {
        "subject_id": "MIM:Bromocresol_Purple",
        "subject_label": "Bromocresol purple",
        "predicate_id": predicate,
        "object_id": "CHEBI:86154",
        "object_label": "bromocresol purple",
        "object_source": "obo:chebi.owl",
        "mapping_justification": "semapv:LexicalMatching",
        "source": "MIM:CultureMech",
        "mapping_date": "2026-08-27",
        "confidence": "0.99",
        "comment": "",
        "other": other,
        "validation_method": "OAK+OLS:chebi",
    }


def _rows(text: str) -> list[dict[str, str]]:
    return list(
        csv.DictReader(
            [line for line in text.splitlines() if not line.startswith("#")],
            delimiter="\t",
        )
    )


def test_quoted_other_cas_is_counted_as_already_present():
    other = "|".join(
        [
            "3,3-bis(3-bromo-4-hydroxy-5-methylphenyl)",
            'bromocresol purple"',
            "CAS:115-40-2",
        ]
    )

    out, stats = mod.publish_cas_rows(
        _sssom_text(_row(other)),
        {
            "Bromocresol purple": {
                "chemical_properties": {"cas_rn": "115-40-2"},
            }
        },
    )

    rows = _rows(out)
    assert stats == mod.PublishStats(already=1)
    assert rows[0]["other"].split("|").count("CAS:115-40-2") == 1
    assert out.startswith('# mapping_set_id: "https://example.org/mim"\n')


def test_missing_cas_is_appended_through_tsv_writer():
    out, stats = mod.publish_cas_rows(
        _sssom_text(_row('bromocresol, purple|quoted "token"')),
        {
            "Bromocresol purple": {
                "chemical_properties": {"cas_rn": "115-40-2"},
            }
        },
    )

    rows = _rows(out)
    assert stats == mod.PublishStats(added=1)
    assert rows[0]["other"].split("|")[-1] == "CAS:115-40-2"


def test_asymmetric_rows_stay_untouched():
    before = _sssom_text(_row("known", predicate="skos:narrowMatch"))

    out, stats = mod.publish_cas_rows(
        before,
        {
            "Bromocresol purple": {
                "chemical_properties": {"cas_rn": "115-40-2"},
            }
        },
    )

    assert out == before
    assert stats == mod.PublishStats(skipped_asym=1)
