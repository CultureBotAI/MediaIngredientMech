"""Identity corrections must survive refreshes from older occurrence tables."""

import pytest

from mediaingredientmech.utils.culturemech_occurrences import mim_identifier_for_occurrence


@pytest.mark.parametrize(
    ("label", "old_id", "expected"),
    [
        ("NaNO", "NCIT:C54713", "CHEBI:63005"),
        ("Sodium phosphate dibasic", "CHEBI:37583", "CHEBI:34683"),
        ("Sodium dihydrogen phosphate", "CHEBI:37583", "CHEBI:37585"),
        (
            "0.5 M Nitrilotriacetic acid, disodium salt",
            "CHEBI:132766",
            "kgmicrobe.ingredient:05_m_nitrilotriacetic_acid_disodium_salt",
        ),
        ("Nitrilotriacetic acid, trisodium salt", "CHEBI:132766", "CHEBI:132766"),
        ("Artificial Sea Salt", "MICRO:0001647", "kgmicrobe.ingredient:artificial_sea_salt"),
        ("Unrelated ingredient", "CHEBI:37583", "CHEBI:37583"),
    ],
)
def test_correct_source_label_without_rewriting_whole_identifier_group(label, old_id, expected):
    assert (
        mim_identifier_for_occurrence({"preferred_term": label, "resolved_identifier": old_id})
        == expected
    )
