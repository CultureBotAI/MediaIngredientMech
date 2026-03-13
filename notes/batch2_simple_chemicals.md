# Unmapped Ingredients for Claude Code Curation

**Total:** 20 ingredients
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


## Ingredient 2: UNMAPPED_0039

**Name:** Citric Acid•H2O
**Category:** SIMPLE_CHEMICAL
**Occurrences:** 3 across 3 media
**Synonyms:** Citric Acid•H2O(Fisher A 104)


## Ingredient 3: UNMAPPED_0040

**Name:** Na2EDTA•2H2O
**Category:** SIMPLE_CHEMICAL
**Occurrences:** 3 across 3 media
**Normalized:** Na2EDTA (rules: stripped_hydrate)
**Search variants:** Na2EDTA•2H2O, Na2EDTA
**Synonyms:** Na2EDTA•2H2O(Sigma ED255)


## Ingredient 4: UNMAPPED_0041

**Name:** Na2CO
**Category:** SIMPLE_CHEMICAL
**Occurrences:** 3 across 3 media
**Synonyms:** Na2CO3(Baker 3604)


## Ingredient 5: UNMAPPED_0043

**Name:** NH4MgPO
**Category:** SIMPLE_CHEMICAL
**Occurrences:** 3 across 3 media
**Synonyms:** NH4MgPO4(Sigma 529354)


## Ingredient 6: UNMAPPED_0045

**Name:** MES
**Category:** SIMPLE_CHEMICAL
**Occurrences:** 3 across 3 media
**Synonyms:** MES(CAS: 1266615-59-1), MES(CAS: 7365-45-9)


## Ingredient 7: UNMAPPED_0046

**Name:** MWC Metal Solution
**Category:** SIMPLE_CHEMICAL
**Occurrences:** 3 across 3 media
**Synonyms:** MWC Metal Solution


## Ingredient 8: UNMAPPED_0047

**Name:** H3BO
**Category:** SIMPLE_CHEMICAL
**Occurrences:** 3 across 3 media
**Synonyms:** H3BO3(Baker 0084)


## Ingredient 9: UNMAPPED_0048

**Name:** CaSO4•2H2O
**Category:** SIMPLE_CHEMICAL
**Occurrences:** 3 across 3 media
**Normalized:** CaSO4 (rules: stripped_hydrate)
**Search variants:** CaSO4•2H2O, CaSO4, calcium sulfate
**Synonyms:** CaSO4•2H2O(Mallinckroft 4300)


## Ingredient 10: UNMAPPED_0056

**Name:** Spir solution
**Category:** SIMPLE_CHEMICAL
**Occurrences:** 2 across 2 media
**Synonyms:** Spir solution 1, Spir solution 2


## Ingredient 11: UNMAPPED_0057

**Name:** HEPES buffer
**Category:** SIMPLE_CHEMICAL
**Occurrences:** 2 across 2 media
**Synonyms:** HEPES buffer(CAS: 7365-45-9), HEPES buffer(Sigma H-3375)


## Ingredient 12: UNMAPPED_0060

**Name:** Na2HPO4•7H2O
**Category:** SIMPLE_CHEMICAL
**Occurrences:** 2 across 2 media
**Normalized:** Na2HPO4 (rules: stripped_hydrate)
**Search variants:** Na2HPO4•7H2O, Na2HPO4
**Synonyms:** Na2HPO4•7H2O(Sigma S-9390), Na2HPO4•7H2O(autoclave before adding) (Sigma S-9390)


## Ingredient 13: UNMAPPED_0068

**Name:** DYV Metal Solution
**Category:** SIMPLE_CHEMICAL
**Occurrences:** 2 across 2 media
**Synonyms:** DYV Metal Solution


## Ingredient 14: UNMAPPED_0073

**Name:** EDTA Stock
**Category:** SIMPLE_CHEMICAL
**Occurrences:** 1 across 1 media
**Synonyms:** EDTA Stock


## Ingredient 15: UNMAPPED_0080

**Name:** TES buffer
**Category:** SIMPLE_CHEMICAL
**Occurrences:** 1 across 1 media
**Synonyms:** TES buffer(Sigma T 1375)


## Ingredient 16: UNMAPPED_0081

**Name:** Na2Glycerophosphate.5H2O
**Category:** SIMPLE_CHEMICAL
**Occurrences:** 1 across 1 media
**Normalized:** Na2Glycerophosphate (rules: stripped_hydrate)
**Search variants:** Na2Glycerophosphate.5H2O, Na2Glycerophosphate
**Synonyms:** Na2Glycerophosphate.5H2O(CAS:  13408-09-8)


## Ingredient 17: UNMAPPED_0082

**Name:** Original amount: (NH4)2SO4(Fisher A 702)
**Category:** SIMPLE_CHEMICAL
**Occurrences:** 1 across 1 media
**Normalized:** Original amount: (NH4)2SO4 (rules: stripped_catalog)
**Search variants:** Original amount: (NH4)2SO4(Fisher A 702), Original amount: (NH4)2SO4
**Synonyms:** (NH4)2SO4(Fisher A 702)


## Ingredient 18: UNMAPPED_0084

**Name:** Sterile dH2O
**Category:** SIMPLE_CHEMICAL
**Occurrences:** 1 across 1 media
**Synonyms:** Sterile dH2O


## Ingredient 19: UNMAPPED_0085

**Name:** Beijerinck's Solution
**Category:** SIMPLE_CHEMICAL
**Occurrences:** 1 across 1 media
**Synonyms:** Beijerinck's Solution


## Ingredient 20: UNMAPPED_0092

**Name:** DAS Macro Solution
**Category:** SIMPLE_CHEMICAL
**Occurrences:** 1 across 1 media
**Synonyms:** DAS Macro Solution


---

## Summary

After reviewing all ingredients, provide a summary:
- Total suggested mappings
- High confidence (≥0.9) mappings
- Medium confidence (0.7-0.89) mappings
- Low confidence or unmappable items
- Any patterns or insights noticed