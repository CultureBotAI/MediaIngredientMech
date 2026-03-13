# Unmapped Ingredients for Claude Code Curation

**Total:** 20 ingredients
**Category filter:** COMPLEX_MIXTURE

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


## Ingredient 1: UNMAPPED_0012

**Name:** Soilwater: GR+ Medium
**Category:** COMPLEX_MIXTURE
**Occurrences:** 15 across 15 media
**Synonyms:** Soilwater: GR+ Medium


## Ingredient 2: UNMAPPED_0023

**Name:** Bristol Medium
**Category:** COMPLEX_MIXTURE
**Occurrences:** 6 across 6 media
**Synonyms:** Bristol Medium


## Ingredient 3: UNMAPPED_0024

**Name:** Erdschreiber's Medium
**Category:** COMPLEX_MIXTURE
**Occurrences:** 5 across 5 media
**Synonyms:** Erdschreiber's Medium


## Ingredient 4: UNMAPPED_0029

**Name:** Trace Metals Solution
**Category:** COMPLEX_MIXTURE
**Occurrences:** 4 across 4 media
**Synonyms:** Trace Metals Solution


## Ingredient 5: UNMAPPED_0031

**Name:** Enrichment Solution for Seawater Medium
**Category:** COMPLEX_MIXTURE
**Occurrences:** 4 across 4 media
**Synonyms:** Enrichment Solution for Seawater Medium


## Ingredient 6: UNMAPPED_0033

**Name:** F/2 Medium
**Category:** COMPLEX_MIXTURE
**Occurrences:** 4 across 4 media
**Synonyms:** F/2 Medium


## Ingredient 7: UNMAPPED_0051

**Name:** Bold 1NV Medium
**Category:** COMPLEX_MIXTURE
**Occurrences:** 2 across 2 media
**Synonyms:** Bold 1NV Medium


## Ingredient 8: UNMAPPED_0054

**Name:** BG-11 Trace Metals Solution
**Category:** COMPLEX_MIXTURE
**Occurrences:** 2 across 2 media
**Synonyms:** BG-11 Trace Metals Solution


## Ingredient 9: UNMAPPED_0055

**Name:** Soil+Seawater Medium
**Category:** COMPLEX_MIXTURE
**Occurrences:** 2 across 2 media
**Synonyms:** Soil+Seawater Medium


## Ingredient 10: UNMAPPED_0059

**Name:** DAS Vitamin Cocktail
**Category:** COMPLEX_MIXTURE
**Occurrences:** 2 across 2 media
**Synonyms:** DAS Vitamin Cocktail


## Ingredient 11: UNMAPPED_0061

**Name:** BG-11 Medium
**Category:** COMPLEX_MIXTURE
**Occurrences:** 2 across 2 media
**Synonyms:** BG-11 Medium


## Ingredient 12: UNMAPPED_0062

**Name:** Enriched Seawater Medium
**Category:** COMPLEX_MIXTURE
**Occurrences:** 2 across 2 media
**Synonyms:** Enriched Seawater Medium


## Ingredient 13: UNMAPPED_0063

**Name:** Waris Medium
**Category:** COMPLEX_MIXTURE
**Occurrences:** 2 across 2 media
**Synonyms:** Waris Medium


## Ingredient 14: UNMAPPED_0064

**Name:** Euglena Medium
**Category:** COMPLEX_MIXTURE
**Occurrences:** 2 across 2 media
**Synonyms:** Euglena Medium


## Ingredient 15: UNMAPPED_0066

**Name:** WC Trace Elements Solution
**Category:** COMPLEX_MIXTURE
**Occurrences:** 2 across 2 media
**Synonyms:** WC Trace Elements Solution


## Ingredient 16: UNMAPPED_0067

**Name:** Supplemented Seawater
**Category:** COMPLEX_MIXTURE
**Occurrences:** 2 across 2 media
**Synonyms:** Supplemented Seawater


## Ingredient 17: UNMAPPED_0070

**Name:** Allen Medium
**Category:** COMPLEX_MIXTURE
**Occurrences:** 1 across 1 media
**Synonyms:** Allen Medium


## Ingredient 18: UNMAPPED_0072

**Name:** Volvox Medium
**Category:** COMPLEX_MIXTURE
**Occurrences:** 1 across 1 media
**Synonyms:** Volvox Medium


## Ingredient 19: UNMAPPED_0078

**Name:** Soilwater: GR- Medium
**Category:** COMPLEX_MIXTURE
**Occurrences:** 1 across 1 media
**Synonyms:** Soilwater: GR- Medium


## Ingredient 20: UNMAPPED_0083

**Name:** DYIII Medium
**Category:** COMPLEX_MIXTURE
**Occurrences:** 1 across 1 media
**Synonyms:** DYIII Medium


---

## Summary

After reviewing all ingredients, provide a summary:
- Total suggested mappings
- High confidence (≥0.9) mappings
- Medium confidence (0.7-0.89) mappings
- Low confidence or unmappable items
- Any patterns or insights noticed