# Unmapped Ingredients for Claude Code Curation

**Total:** 5 ingredients
**Category filter:** ENVIRONMENTAL

## Instructions for Claude Code

For each ingredient below, suggest the most appropriate ontology mapping:

1. **Ontology selection:**
   - CHEBI - Simple chemicals, salts, compounds
   - FOODON - Biological materials, extracts, complex mixtures
   - ENVO - Environmental samples (soil, seawater, etc.)

2. **For each ingredient provide:**
   - Ontology ID (e.g., CHEBI:32599)
   - Ontology label (e.g., magnesium sulfate)
   - Ontology source (CHEBI/FOODON/ENVO)
   - Confidence (0.0-1.0)
   - Reasoning (why this mapping is correct)
   - Quality rating (EXACT_MATCH, SYNONYM_MATCH, CLOSE_MATCH, or LLM_ASSISTED)

3. **Special cases:**
   - Hydrates → base chemical (MgSO4•7H2O → magnesium sulfate)
   - Catalog variants → base chemical (NaCl (Fisher X) → sodium chloride)
   - Incomplete formulas → corrected (K2HPO → dipotassium phosphate)
   - Complex mixtures → may be UNMAPPABLE if no appropriate term exists

4. **Format your response as:**
   ```
   Ingredient X: IDENTIFIER
   Suggested mapping: ONTOLOGY_ID (label)
   Source: ONTOLOGY_SOURCE
   Confidence: 0.XX
   Quality: QUALITY_RATING
   Reasoning: [explanation]
   ```

---


## Ingredient 1: UNMAPPED_0008

**Name:** Pasteurized Seawater
**Category:** ENVIRONMENTAL
**Occurrences:** 19 across 19 media
**Synonyms:** Pasteurized Seawater


## Ingredient 2: UNMAPPED_0014

**Name:** CR1 Soil
**Category:** ENVIRONMENTAL
**Occurrences:** 14 across 14 media
**Synonyms:** CR1 Soil


## Ingredient 3: UNMAPPED_0019

**Name:** Green House Soil
**Category:** ENVIRONMENTAL
**Occurrences:** 11 across 11 media
**Synonyms:** Green House Soil


## Ingredient 4: UNMAPPED_0027

**Name:** Seawater
**Category:** ENVIRONMENTAL
**Occurrences:** 4 across 4 media
**Synonyms:** Seawater (30 ppt), Seawater(non-sterilized)


## Ingredient 5: UNMAPPED_0071

**Name:** Vermont Soil
**Category:** ENVIRONMENTAL
**Occurrences:** 1 across 1 media
**Synonyms:** Vermont Soil


---

## Summary

After reviewing all ingredients, provide a summary:
- Total suggested mappings
- High confidence (≥0.9) mappings
- Medium confidence (0.7-0.89) mappings
- Low confidence or unmappable items
- Any patterns or insights noticed