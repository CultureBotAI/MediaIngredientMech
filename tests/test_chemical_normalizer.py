import pytest

from mediaingredientmech.utils.chemical_normalizer import (
    normalize_chemical_name,
    strip_hydrate_notation,
)


@pytest.mark.parametrize(
    ("name", "expected"),
    [
        ("Glucose monohydrate", "Glucose"),
        ("Calcium chloride dihydrate", "Calcium chloride"),
        ("Sodium acetate trihydrate", "Sodium acetate"),
        ("Manganese chloride tetrahydrate", "Manganese chloride"),
        ("Copper sulfate pentahydrate", "Copper sulfate"),
        ("Cobalt chloride hexahydrate", "Cobalt chloride"),
        ("Sodium phosphate dibasic heptahydrate", "Sodium phosphate dibasic"),
        ("Nickel sulfate nonahydrate", "Nickel sulfate"),
        ("Magnesium chloride dodecahydrate", "Magnesium chloride"),
        ("Cadmium chloride hemipentahydrate", "Cadmium chloride"),
        ("Sodium chloride hydrate", "Sodium chloride"),
    ],
)
def test_strip_hydrate_notation_strips_complete_hydrate_words(name, expected):
    assert strip_hydrate_notation(name) == (expected, True)


@pytest.mark.parametrize(
    "name",
    [
        "b-Mannan borohydrate reduced carob seed",
        "Sodium hydroxide",
        "Carbohydrate mix",
        "Tetrahydrofuran",
        "Dihydrogen phosphate",
        "L-Ornithine monochlorohydrate",
    ],
)
def test_strip_hydrate_notation_ignores_non_hydrate_suffixes(name):
    assert strip_hydrate_notation(name) == (name, False)


def test_normalize_chemical_name_uses_complete_hydrate_word():
    result = normalize_chemical_name("Copper sulfate pentahydrate")

    assert result.normalized == "Copper sulfate"
    assert "Copper sulfate" in result.variants
    assert "Copper sulfate penta" not in result.variants
