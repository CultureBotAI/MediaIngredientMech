"""Tests for MediaIngredientMech environmental_context schema enhancement.

Validates:
- EnvironmentContext class with ENVO terms and relevance qualifiers
- EnvironmentRelevanceEnum values
- environmental_context field on MappedIngredient
- ENVO CURIE pattern validation
- Backward compatibility (ingredients without environmental_context)
- Test YAML data files load and validate correctly
"""

import re
from pathlib import Path

import pytest
import yaml

MAPPED_SCHEMA_PATH = (
    Path(__file__).parent.parent
    / "src"
    / "mediaingredientmech"
    / "schema"
    / "mapped_ingredients_schema.yaml"
)
TEST_DATA_DIR = Path(__file__).parent / "data" / "test_environmental_context"


def load_mapped_schema():
    """Load the mapped_ingredients schema YAML."""
    with open(MAPPED_SCHEMA_PATH, encoding="utf-8") as f:
        return yaml.safe_load(f)


class TestEnvironmentContextSchemaDefinition:
    """Test that EnvironmentContext class is properly defined in the schema."""

    def setup_method(self):
        self.schema = load_mapped_schema()
        self.classes = self.schema["classes"]
        self.enums = self.schema["enums"]

    def test_environment_context_class_exists(self):
        assert "EnvironmentContext" in self.classes

    def test_environment_context_has_required_environment_term(self):
        attrs = self.classes["EnvironmentContext"]["attributes"]
        assert "environment_term" in attrs
        assert attrs["environment_term"]["required"] is True
        assert attrs["environment_term"]["range"] == "string"

    def test_environment_term_has_envo_pattern(self):
        attrs = self.classes["EnvironmentContext"]["attributes"]
        pattern = attrs["environment_term"]["pattern"]
        assert pattern == "^ENVO:\\d{7,8}$"

    def test_environment_context_has_required_relevance(self):
        attrs = self.classes["EnvironmentContext"]["attributes"]
        assert "relevance" in attrs
        assert attrs["relevance"]["required"] is True
        assert attrs["relevance"]["range"] == "EnvironmentRelevanceEnum"

    def test_environment_context_has_optional_label(self):
        attrs = self.classes["EnvironmentContext"]["attributes"]
        assert "environment_label" in attrs
        assert attrs["environment_label"]["required"] is False

    def test_environment_context_has_optional_notes(self):
        attrs = self.classes["EnvironmentContext"]["attributes"]
        assert "notes" in attrs
        assert attrs["notes"]["required"] is False


class TestEnvironmentRelevanceEnum:
    """Test EnvironmentRelevanceEnum definition and values."""

    def setup_method(self):
        self.schema = load_mapped_schema()
        self.enum = self.schema["enums"]["EnvironmentRelevanceEnum"]

    def test_enum_exists(self):
        assert "EnvironmentRelevanceEnum" in self.schema["enums"]

    def test_has_all_expected_values(self):
        values = set(self.enum["permissible_values"].keys())
        expected = {
            "NATURAL_SOURCE",
            "REQUIRED_FOR_ORGANISM",
            "SELECTIVE_AGENT",
            "ENVIRONMENT_MIMIC",
            "COMMONLY_USED",
        }
        assert values == expected

    def test_all_values_have_descriptions(self):
        for val_name, val_def in self.enum["permissible_values"].items():
            assert val_def.get("description"), (
                f"EnvironmentRelevanceEnum.{val_name} missing description"
            )


class TestMappedIngredientEnvironmentalContext:
    """Test that environmental_context field is properly added to MappedIngredient."""

    def setup_method(self):
        self.schema = load_mapped_schema()
        self.attrs = self.schema["classes"]["MappedIngredient"]["attributes"]

    def test_field_exists(self):
        assert "environmental_context" in self.attrs

    def test_field_is_optional(self):
        assert self.attrs["environmental_context"]["required"] is False

    def test_field_is_multivalued(self):
        assert self.attrs["environmental_context"]["multivalued"] is True

    def test_field_range_is_environment_context(self):
        assert self.attrs["environmental_context"]["range"] == "EnvironmentContext"

    def test_field_is_inlined_as_list(self):
        assert self.attrs["environmental_context"]["inlined_as_list"] is True


class TestEnvoPrefixDefined:
    """Test that the ENVO prefix is properly defined in the schema."""

    def setup_method(self):
        self.schema = load_mapped_schema()

    def test_envo_prefix_exists(self):
        prefixes = self.schema.get("prefixes", {})
        assert "ENVO" in prefixes

    def test_envo_prefix_uri(self):
        prefixes = self.schema["prefixes"]
        assert prefixes["ENVO"] == "http://purl.obolibrary.org/obo/ENVO_"


class TestEnvoTermPattern:
    """Test ENVO CURIE pattern validation."""

    PATTERN = re.compile(r"^ENVO:\d{7,8}$")

    @pytest.mark.parametrize(
        "valid_term",
        [
            "ENVO:00000044",  # peatland (8 digits)
            "ENVO:00002149",  # sea water
            "ENVO:01000030",  # hydrothermal vent
            "ENVO:00002982",  # soil
            "ENVO:0000044",   # 7 digits also valid
            "ENVO:00002044",  # hypersaline lake
            "ENVO:01000339",  # hot spring
            "ENVO:02000065",  # rhizosphere
        ],
    )
    def test_valid_envo_terms(self, valid_term):
        assert self.PATTERN.match(valid_term), f"{valid_term} should match ENVO pattern"

    @pytest.mark.parametrize(
        "invalid_term",
        [
            "ENVO:123",       # too few digits
            "ENVO:123456789", # too many digits (9)
            "CHEBI:12345",    # wrong prefix
            "envo:00000044",  # lowercase
            "ENVO:abcdefgh",  # non-numeric
            "ENVO:",          # no digits
            "",               # empty
            "ENVO00000044",   # missing colon
        ],
    )
    def test_invalid_envo_terms(self, invalid_term):
        assert not self.PATTERN.match(invalid_term), (
            f"{invalid_term} should NOT match ENVO pattern"
        )


class TestDataclassInstantiation:
    """Test that generated Python dataclasses work correctly."""

    def test_environment_context_creation(self):
        from src.mediaingredientmech.schema.mapped_ingredients_schema import (
            EnvironmentContext,
        )

        ctx = EnvironmentContext(
            environment_term="ENVO:00000044",
            relevance="NATURAL_SOURCE",
            environment_label="peatland",
            notes="Major component of peat organic matter",
        )
        assert ctx.environment_term == "ENVO:00000044"
        assert str(ctx.relevance) == "NATURAL_SOURCE"
        assert ctx.environment_label == "peatland"
        assert ctx.notes == "Major component of peat organic matter"

    def test_environment_context_required_fields_only(self):
        from src.mediaingredientmech.schema.mapped_ingredients_schema import (
            EnvironmentContext,
        )

        ctx = EnvironmentContext(
            environment_term="ENVO:00002149",
            relevance="ENVIRONMENT_MIMIC",
        )
        assert ctx.environment_term == "ENVO:00002149"
        assert ctx.environment_label is None
        assert ctx.notes is None

    def test_mapped_ingredient_with_environmental_context(self):
        from src.mediaingredientmech.schema.mapped_ingredients_schema import (
            EnvironmentContext,
            MappedIngredient,
        )

        ctx = EnvironmentContext(
            environment_term="ENVO:00000044",
            relevance="NATURAL_SOURCE",
        )
        ingredient = MappedIngredient(
            preferred_term="Humic acid",
            environmental_context=[ctx],
        )
        assert len(ingredient.environmental_context) == 1
        assert ingredient.environmental_context[0].environment_term == "ENVO:00000044"

    def test_mapped_ingredient_multiple_contexts(self):
        from src.mediaingredientmech.schema.mapped_ingredients_schema import (
            EnvironmentContext,
            MappedIngredient,
        )

        contexts = [
            EnvironmentContext(
                environment_term="ENVO:00002149",
                relevance="ENVIRONMENT_MIMIC",
            ),
            EnvironmentContext(
                environment_term="ENVO:00002044",
                relevance="ENVIRONMENT_MIMIC",
            ),
        ]
        ingredient = MappedIngredient(
            preferred_term="NaCl",
            environmental_context=contexts,
        )
        assert len(ingredient.environmental_context) == 2

    def test_mapped_ingredient_without_environmental_context(self):
        from src.mediaingredientmech.schema.mapped_ingredients_schema import (
            MappedIngredient,
        )

        ingredient = MappedIngredient(preferred_term="Agar")
        assert len(ingredient.environmental_context) == 0

    def test_all_relevance_enum_values(self):
        from src.mediaingredientmech.schema.mapped_ingredients_schema import (
            EnvironmentRelevanceEnum,
        )

        for val in [
            "NATURAL_SOURCE",
            "REQUIRED_FOR_ORGANISM",
            "SELECTIVE_AGENT",
            "ENVIRONMENT_MIMIC",
            "COMMONLY_USED",
        ]:
            assert hasattr(EnvironmentRelevanceEnum, val)


class TestYamlDataFiles:
    """Test that YAML data files load and conform to schema expectations."""

    def _load_data(self, filename):
        with open(TEST_DATA_DIR / filename, encoding="utf-8") as f:
            return yaml.safe_load(f)

    def test_single_environment_loads(self):
        data = self._load_data("test_ingredient_with_environment.yaml")
        ingredient = data["mapped_ingredients"][0]
        assert ingredient["preferred_term"] == "Humic acid"
        ctx = ingredient["environmental_context"][0]
        assert ctx["environment_term"] == "ENVO:00000044"
        assert ctx["relevance"] == "NATURAL_SOURCE"
        assert ctx["environment_label"] == "peatland"

    def test_multiple_environments_loads(self):
        data = self._load_data("test_ingredient_multiple_environments.yaml")
        ingredient = data["mapped_ingredients"][0]
        assert ingredient["preferred_term"] == "NaCl"
        assert len(ingredient["environmental_context"]) == 3
        relevances = [ctx["relevance"] for ctx in ingredient["environmental_context"]]
        assert all(r == "ENVIRONMENT_MIMIC" for r in relevances)

    def test_no_environment_loads(self):
        data = self._load_data("test_ingredient_no_environment.yaml")
        ingredient = data["mapped_ingredients"][0]
        assert ingredient["preferred_term"] == "Agar"
        assert "environmental_context" not in ingredient

    def test_dual_relevance_loads(self):
        data = self._load_data("test_ingredient_dual_relevance.yaml")
        ingredient = data["mapped_ingredients"][0]
        assert ingredient["preferred_term"] == "Sodium sulfide"
        contexts = ingredient["environmental_context"]
        assert len(contexts) == 2
        # Same environment, different relevance
        assert contexts[0]["environment_term"] == contexts[1]["environment_term"]
        assert contexts[0]["relevance"] != contexts[1]["relevance"]
        relevances = {ctx["relevance"] for ctx in contexts}
        assert relevances == {"NATURAL_SOURCE", "REQUIRED_FOR_ORGANISM"}

    def test_all_relevance_types_covered(self):
        data = self._load_data("test_ingredient_all_relevance_types.yaml")
        all_relevances = set()
        for ingredient in data["mapped_ingredients"]:
            for ctx in ingredient.get("environmental_context", []):
                all_relevances.add(ctx["relevance"])
        expected = {
            "NATURAL_SOURCE",
            "REQUIRED_FOR_ORGANISM",
            "SELECTIVE_AGENT",
            "ENVIRONMENT_MIMIC",
            "COMMONLY_USED",
        }
        assert all_relevances == expected

    def test_all_envo_terms_valid_pattern(self):
        """Verify all ENVO terms in test data match the pattern."""
        pattern = re.compile(r"^ENVO:\d{7,8}$")
        for yaml_file in TEST_DATA_DIR.glob("*.yaml"):
            data = yaml.safe_load(yaml_file.read_text())
            for ingredient in data.get("mapped_ingredients", []):
                for ctx in ingredient.get("environmental_context", []):
                    term = ctx["environment_term"]
                    assert pattern.match(term), (
                        f"Invalid ENVO term '{term}' in {yaml_file.name}"
                    )
