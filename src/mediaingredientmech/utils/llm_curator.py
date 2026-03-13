"""LLM-assisted curation for ingredient ontology mappings.

Uses Claude API to suggest ontology mappings for unmapped ingredients,
with reasoning and confidence scores. All suggestions are validated
against actual ontology databases using OAK.
"""

from __future__ import annotations

import json
import logging
import os
from dataclasses import dataclass
from typing import Optional

logger = logging.getLogger(__name__)


@dataclass
class LLMSuggestion:
    """An LLM-suggested ontology mapping."""

    ontology_id: str
    ontology_label: str
    ontology_source: str
    confidence: float
    reasoning: str
    alternative_queries: list[str]


class LLMCurator:
    """LLM-assisted curation for ingredient mappings."""

    def __init__(
        self,
        model: str = "claude-sonnet-4-20250514",
        api_key: Optional[str] = None,
    ):
        """Initialize LLM curator.

        Args:
            model: Claude model identifier
            api_key: Anthropic API key (defaults to ANTHROPIC_API_KEY env var)
        """
        self.model = model
        self.api_key = api_key or os.environ.get("ANTHROPIC_API_KEY")

        if not self.api_key:
            raise ValueError(
                "ANTHROPIC_API_KEY environment variable not set. "
                "Set it with: export ANTHROPIC_API_KEY=your-api-key"
            )

        try:
            from anthropic import Anthropic
            self.client = Anthropic(api_key=self.api_key)
        except ImportError:
            raise ImportError(
                "anthropic package not installed. "
                "Install with: pip install anthropic"
            )

    def suggest_mapping(
        self,
        ingredient_name: str,
        context: Optional[dict] = None,
    ) -> LLMSuggestion:
        """Get LLM suggestion for ontology mapping.

        Args:
            ingredient_name: The unmapped ingredient name
            context: Optional context (synonyms, occurrences, category, etc.)

        Returns:
            LLMSuggestion with ontology mapping and reasoning
        """
        prompt = self._build_prompt(ingredient_name, context)

        try:
            response = self.client.messages.create(
                model=self.model,
                max_tokens=1024,
                temperature=0,  # Deterministic for consistency
                messages=[
                    {
                        "role": "user",
                        "content": prompt,
                    }
                ],
            )

            # Parse response
            content = response.content[0].text
            suggestion = self._parse_response(content, ingredient_name)

            logger.info(
                f"LLM suggested {suggestion.ontology_id} for '{ingredient_name}' "
                f"with confidence {suggestion.confidence}"
            )

            return suggestion

        except Exception as e:
            logger.error(f"LLM API error: {e}")
            raise

    def _build_prompt(
        self,
        ingredient_name: str,
        context: Optional[dict] = None,
    ) -> str:
        """Build the prompt for LLM mapping suggestion."""
        context = context or {}

        # Extract context
        synonyms = context.get("synonyms", [])
        category = context.get("category", "UNKNOWN")
        occurrences = context.get("occurrences", 0)
        normalized = context.get("normalized", ingredient_name)
        normalization_rules = context.get("normalization_rules", [])

        prompt = f"""You are an expert curator mapping media ingredient names to ontology terms.

**Task:** Suggest the best ontology mapping for the following ingredient.

**Ingredient name:** {ingredient_name}

**Context:**
- Category: {category}
- Occurrences in media: {occurrences}
- Normalized name: {normalized}
"""

        if normalization_rules:
            prompt += f"- Normalization applied: {', '.join(normalization_rules)}\n"

        if synonyms:
            syn_list = ', '.join(synonyms[:5])
            prompt += f"- Known synonyms: {syn_list}\n"

        prompt += """
**Ontology sources (in priority order):**
1. **CHEBI** (Chemical Entities of Biological Interest) - For chemicals, salts, compounds
2. **FOODON** (Food Ontology) - For biological materials, extracts, complex mixtures
3. **ENVO** (Environment Ontology) - For environmental samples (soil, seawater, etc.)

**Guidelines:**
- Simple chemicals (NaCl, MgSO4, glucose) → CHEBI
- Biological extracts (yeast extract, tryptone) → FOODON
- Environmental samples (soil, seawater) → ENVO
- Prefer exact matches over close matches
- Consider normalized form for searching
- Hydrate forms map to base chemical (MgSO4•7H2O → magnesium sulfate)

**Output format (JSON):**
```json
{
  "ontology_id": "CHEBI:XXXXX or FOODON:XXXXXX or ENVO:XXXXXX",
  "ontology_label": "official ontology term label",
  "ontology_source": "CHEBI or FOODON or ENVO",
  "confidence": 0.0-1.0,
  "reasoning": "brief explanation of why this mapping is correct",
  "alternative_queries": ["query1", "query2", "query3"]
}
```

**Confidence scoring:**
- 0.9-1.0: Exact match, unambiguous
- 0.7-0.89: Strong match, minor ambiguity
- 0.5-0.69: Likely match, moderate ambiguity
- 0.0-0.49: Uncertain, needs expert review

**Examples:**

Input: "MgSO4•7H2O"
Output:
```json
{
  "ontology_id": "CHEBI:32599",
  "ontology_label": "magnesium sulfate",
  "ontology_source": "CHEBI",
  "confidence": 0.95,
  "reasoning": "Hydrate form of magnesium sulfate. Maps to base chemical in CHEBI.",
  "alternative_queries": ["magnesium sulfate", "MgSO4", "magnesium sulphate"]
}
```

Input: "yeast extract"
Output:
```json
{
  "ontology_id": "FOODON:03301439",
  "ontology_label": "yeast extract",
  "ontology_source": "FOODON",
  "confidence": 0.95,
  "reasoning": "Biological extract, exact match in FOODON",
  "alternative_queries": ["yeast extract", "Saccharomyces extract"]
}
```

Input: "tryptone"
Output:
```json
{
  "ontology_id": "FOODON:03305413",
  "ontology_label": "tryptone",
  "ontology_source": "FOODON",
  "confidence": 0.90,
  "reasoning": "Enzymatic digest of protein, biological material in FOODON",
  "alternative_queries": ["tryptone", "pancreatic digest of casein"]
}
```

**Now suggest a mapping for the ingredient above. Return ONLY valid JSON, no other text.**
"""

        return prompt

    def _parse_response(
        self,
        response_text: str,
        ingredient_name: str,
    ) -> LLMSuggestion:
        """Parse LLM response into LLMSuggestion."""
        try:
            # Extract JSON from response (may have ```json wrapper)
            text = response_text.strip()
            if "```json" in text:
                text = text.split("```json")[1].split("```")[0]
            elif "```" in text:
                text = text.split("```")[1].split("```")[0]

            data = json.loads(text.strip())

            return LLMSuggestion(
                ontology_id=data["ontology_id"],
                ontology_label=data["ontology_label"],
                ontology_source=data["ontology_source"],
                confidence=float(data["confidence"]),
                reasoning=data["reasoning"],
                alternative_queries=data.get("alternative_queries", []),
            )

        except (json.JSONDecodeError, KeyError) as e:
            logger.error(f"Failed to parse LLM response: {e}")
            logger.error(f"Response text: {response_text}")
            raise ValueError(
                f"Failed to parse LLM response for '{ingredient_name}': {e}"
            )


def validate_llm_suggestion(
    suggestion: LLMSuggestion,
    ontology_client,
) -> tuple[bool, Optional[str]]:
    """Validate that the LLM-suggested ontology ID actually exists.

    Args:
        suggestion: The LLM suggestion to validate
        ontology_client: OntologyClient instance for verification

    Returns:
        Tuple of (is_valid, error_message)
    """
    try:
        # Search for the exact ID
        from oaklib import get_adapter

        source = suggestion.ontology_source
        resource_map = {
            "CHEBI": "sqlite:obo:chebi",
            "FOODON": "sqlite:obo:foodon",
            "ENVO": "sqlite:obo:envo",
        }

        resource = resource_map.get(source)
        if not resource:
            return False, f"Unknown ontology source: {source}"

        adapter = get_adapter(resource)

        # Check if term exists
        label = adapter.label(suggestion.ontology_id)
        if not label:
            return False, f"Term {suggestion.ontology_id} not found in {source}"

        # Verify label matches (case-insensitive)
        if label.lower() != suggestion.ontology_label.lower():
            logger.warning(
                f"Label mismatch: LLM suggested '{suggestion.ontology_label}' "
                f"but ontology has '{label}'"
            )
            # Update suggestion with correct label
            suggestion.ontology_label = label

        return True, None

    except Exception as e:
        return False, f"Validation error: {e}"
