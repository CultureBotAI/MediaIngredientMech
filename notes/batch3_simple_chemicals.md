# Unmapped Ingredients for Claude Code Curation

**Total:** 12 ingredients
**Category filter:** SIMPLE_CHEMICAL

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


## Ingredient 1: UNMAPPED_0011

**Name:** P-IV Metal Solution
**Category:** SIMPLE_CHEMICAL
**Occurrences:** 16 across 16 media
**Synonyms:** P-IV Metal Solution


## Ingredient 2: UNMAPPED_0046

**Name:** MWC Metal Solution
**Category:** SIMPLE_CHEMICAL
**Occurrences:** 3 across 3 media
**Synonyms:** MWC Metal Solution


## Ingredient 3: UNMAPPED_0056

**Name:** Spir solution
**Category:** SIMPLE_CHEMICAL
**Occurrences:** 2 across 2 media
**Synonyms:** Spir solution 1, Spir solution 2


## Ingredient 4: UNMAPPED_0068

**Name:** DYV Metal Solution
**Category:** SIMPLE_CHEMICAL
**Occurrences:** 2 across 2 media
**Synonyms:** DYV Metal Solution


## Ingredient 5: UNMAPPED_0085

**Name:** Beijerinck's Solution
**Category:** SIMPLE_CHEMICAL
**Occurrences:** 1 across 1 media
**Synonyms:** Beijerinck's Solution


## Ingredient 6: UNMAPPED_0092

**Name:** DAS Macro Solution
**Category:** SIMPLE_CHEMICAL
**Occurrences:** 1 across 1 media
**Synonyms:** DAS Macro Solution


## Ingredient 7: UNMAPPED_0094

**Name:** P-II Metal Solution
**Category:** SIMPLE_CHEMICAL
**Occurrences:** 1 across 1 media
**Synonyms:** P-II Metal Solution


## Ingredient 8: UNMAPPED_0095

**Name:** Chelated Iron Solution
**Category:** SIMPLE_CHEMICAL
**Occurrences:** 1 across 1 media
**Synonyms:** Chelated Iron Solution


## Ingredient 9: UNMAPPED_0101

**Name:** Na2Glycerophosphate•5H2O
**Category:** SIMPLE_CHEMICAL
**Occurrences:** 1 across 1 media
**Normalized:** Na2Glycerophosphate (rules: stripped_hydrate)
**Search variants:** Na2Glycerophosphate•5H2O, Na2Glycerophosphate
**Synonyms:** Na2Glycerophosphate•5H2O(CAS: 13408-09-8)


## Ingredient 10: UNMAPPED_0102

**Name:** CaSO4•2H2Osaturated solution
**Category:** SIMPLE_CHEMICAL
**Occurrences:** 1 across 1 media
**Normalized:** CaSO4saturated solution (rules: stripped_hydrate)
**Search variants:** CaSO4•2H2Osaturated solution, CaSO4saturated solution
**Synonyms:** CaSO4•2H2Osaturated solution (Mallinckroft 4300)


## Ingredient 11: UNMAPPED_0109

**Name:** FE EDTA
**Category:** SIMPLE_CHEMICAL
**Occurrences:** 1 across 1 media
**Synonyms:** FE EDTA


## Ingredient 12: UNMAPPED_0112

**Name:** Chu Stock Solution
**Category:** SIMPLE_CHEMICAL
**Occurrences:** 1 across 1 media
**Synonyms:** Chu Stock Solution


---

## Summary

After reviewing all ingredients, provide a summary:
- Total suggested mappings
- High confidence (≥0.9) mappings
- Medium confidence (0.7-0.89) mappings
- Low confidence or unmappable items
- Any patterns or insights noticed