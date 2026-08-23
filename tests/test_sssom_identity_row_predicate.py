"""Rule D: a row pointing at the record's own identifier must be exactMatch (#438).

448 published rows said `skos:closeMatch` to the record's own `identifier` --
"this record is similar to itself". The same `mapping_quality` produced both
predicates (`EXACT_MATCH` split 1597/38, `CAS_RN_LOOKUP` 1/39), while all 142
`NARROW_MATCH` identity rows were correctly `exactMatch`, because their
narrowness describes the ontology parent rather than the record's identity.

Fixed upstream in culturebotai-claw's builder; Rule D is the assertion that it
stays fixed, since the builder lives in another repo and only this file is
gated by MIM's CI.
"""

from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
_SPEC = importlib.util.spec_from_file_location(
    "validate_sssom_invariants", ROOT / "scripts" / "validate_sssom_invariants.py"
)
validator = importlib.util.module_from_spec(_SPEC)
sys.modules[_SPEC.name] = validator
_SPEC.loader.exec_module(validator)


def rows():
    _, _, parsed = validator._read_sssom(validator.DEFAULT_SSSOM)
    return parsed


def test_the_published_set_has_no_identity_row_that_is_not_exact_match():
    violations = list(validator.evaluate_rule_d(rows()))

    assert not violations, (
        f"{len(violations)} row(s) publish a non-exactMatch predicate against the "
        f"record's own identifier. First: {violations[0][2] if violations else ''}")


def test_rule_d_fires_on_a_synthetic_violation():
    """The gate must fail as well as pass."""
    subject = next(r["subject_id"] for r in rows() if r["subject_id"].startswith("MIM:"))
    identifier = validator.record_identifier(subject)
    assert identifier, "fixture subject must resolve to a record"

    bad = [{"subject_id": subject, "predicate_id": "skos:closeMatch",
            "object_id": identifier, "object_label": "x"}]

    assert len(list(validator.evaluate_rule_d(bad))) == 1


def test_rule_d_ignores_a_row_pointing_at_a_different_term():
    subject = next(r["subject_id"] for r in rows() if r["subject_id"].startswith("MIM:"))
    fine = [{"subject_id": subject, "predicate_id": "skos:closeMatch",
             "object_id": "CHEBI:99999999", "object_label": "x"}]

    assert list(validator.evaluate_rule_d(fine)) == []


def test_every_published_subject_resolves_to_a_record_file():
    """`_yaml_path_for_subject` used to take the raw slug, so all 19 `~HEX`
    subjects resolved to nothing -- silently disabling Rule A's registry tier
    for them, and Rule D entirely."""
    unresolved = sorted({
        r["subject_id"] for r in rows()
        if r["subject_id"].startswith("MIM:")
        and not validator._yaml_path_for_subject(r["subject_id"]).exists()
    })

    assert not unresolved, f"{len(unresolved)} unresolvable: {unresolved[:5]}"


def test_escaped_subjects_resolve_to_their_unescaped_filenames():
    escaped = sorted({r["subject_id"] for r in rows() if "~" in r["subject_id"]})

    assert escaped, "fixture: the published set carries ~HEX subjects"
    for subject in escaped:
        path = validator._yaml_path_for_subject(subject)
        assert path.exists(), f"{subject} -> {path.name}"
        assert "~" not in path.stem, (
            f"{subject} resolved to a literal-stem path rather than the real file")
