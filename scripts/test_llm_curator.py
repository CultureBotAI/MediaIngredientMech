#!/usr/bin/env python3
"""Test LLM curator functionality (without API calls)."""

import sys
from pathlib import Path

# Add src to path
_project_root = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(_project_root / "src"))


def test_llm_suggestion_structure():
    """Test LLMSuggestion dataclass."""
    from mediaingredientmech.utils.llm_curator import LLMSuggestion

    suggestion = LLMSuggestion(
        ontology_id="CHEBI:32599",
        ontology_label="magnesium sulfate",
        ontology_source="CHEBI",
        confidence=0.95,
        reasoning="Hydrate form maps to base chemical",
        alternative_queries=["magnesium sulfate", "MgSO4"],
    )

    assert suggestion.ontology_id == "CHEBI:32599"
    assert suggestion.confidence == 0.95
    assert len(suggestion.alternative_queries) == 2

    print("✓ LLMSuggestion structure correct")


def test_prompt_building():
    """Test prompt construction (without API call)."""
    from mediaingredientmech.utils.llm_curator import LLMCurator

    # Mock curator (will fail on API calls, but we just test prompt building)
    try:
        curator = LLMCurator(api_key="fake-key-for-testing")

        context = {
            "synonyms": ["MgSO4•7H2O (Sigma 230391)"],
            "category": "SIMPLE_CHEMICAL",
            "occurrences": 29,
            "normalized": "MgSO4",
            "normalization_rules": ["stripped_hydrate"],
        }

        prompt = curator._build_prompt("MgSO4•7H2O", context)

        # Check prompt contains key elements
        assert "MgSO4•7H2O" in prompt
        assert "SIMPLE_CHEMICAL" in prompt
        assert "Occurrences in media: 29" in prompt
        assert "Normalized name: MgSO4" in prompt
        assert "stripped_hydrate" in prompt
        assert "CHEBI" in prompt
        assert "FOODON" in prompt
        assert "JSON" in prompt

        print("✓ Prompt building works correctly")
        print(f"\nPrompt length: {len(prompt)} characters")

    except ImportError as e:
        print(f"⚠ Skipping prompt test: {e}")
        print("  Install with: pip install anthropic")


def test_response_parsing():
    """Test parsing LLM responses."""
    from mediaingredientmech.utils.llm_curator import LLMCurator

    try:
        curator = LLMCurator(api_key="fake-key-for-testing")

        # Test valid JSON response
        response_text = """```json
{
  "ontology_id": "CHEBI:32599",
  "ontology_label": "magnesium sulfate",
  "ontology_source": "CHEBI",
  "confidence": 0.95,
  "reasoning": "Hydrate form of magnesium sulfate",
  "alternative_queries": ["magnesium sulfate", "MgSO4"]
}
```"""

        suggestion = curator._parse_response(response_text, "MgSO4•7H2O")

        assert suggestion.ontology_id == "CHEBI:32599"
        assert suggestion.ontology_label == "magnesium sulfate"
        assert suggestion.ontology_source == "CHEBI"
        assert suggestion.confidence == 0.95
        assert len(suggestion.alternative_queries) == 2

        print("✓ Response parsing works correctly")

        # Test JSON without markdown wrapper
        response_text2 = """{
  "ontology_id": "FOODON:03301439",
  "ontology_label": "yeast extract",
  "ontology_source": "FOODON",
  "confidence": 0.90,
  "reasoning": "Biological extract",
  "alternative_queries": ["yeast extract"]
}"""

        suggestion2 = curator._parse_response(response_text2, "yeast extract")
        assert suggestion2.ontology_id == "FOODON:03301439"

        print("✓ Response parsing handles plain JSON")

    except ImportError as e:
        print(f"⚠ Skipping parsing test: {e}")


def test_integration_structure():
    """Test that all components integrate correctly."""
    print("\nIntegration structure test:")

    # Check imports
    try:
        from mediaingredientmech.utils.llm_curator import (
            LLMCurator,
            LLMSuggestion,
            validate_llm_suggestion,
        )
        from mediaingredientmech.utils.chemical_normalizer import (
            normalize_chemical_name,
        )
        from mediaingredientmech.utils.ontology_client import OntologyClient
        from mediaingredientmech.curation.ingredient_curator import (
            IngredientCurator,
        )

        print("✓ All imports successful")

        # Check workflow structure
        norm_result = normalize_chemical_name("MgSO4•7H2O")
        print(f"✓ Normalization: {norm_result.normalized}")

        context = {
            "normalized": norm_result.normalized,
            "normalization_rules": norm_result.applied_rules,
            "category": "SIMPLE_CHEMICAL",
        }
        print(f"✓ Context building: {len(context)} fields")

        # Mock suggestion
        suggestion = LLMSuggestion(
            ontology_id="CHEBI:32599",
            ontology_label="magnesium sulfate",
            ontology_source="CHEBI",
            confidence=0.95,
            reasoning="Test",
            alternative_queries=[],
        )
        print(f"✓ Suggestion structure: {suggestion.ontology_id}")

        print("\n✅ All integration components work together")

    except Exception as e:
        print(f"❌ Integration test failed: {e}")
        return 1

    return 0


if __name__ == "__main__":
    print("Testing LLM Curator (without API calls)...\n")

    try:
        test_llm_suggestion_structure()
        test_prompt_building()
        test_response_parsing()
        exit_code = test_integration_structure()

        print("\n" + "=" * 50)
        print("Note: These tests verify structure only.")
        print("To test actual LLM API calls, set ANTHROPIC_API_KEY")
        print("and run: python scripts/llm_curate_unmapped.py --dry-run --limit 1")
        print("=" * 50)

        sys.exit(exit_code)

    except Exception as e:
        print(f"\n❌ Test suite failed: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
