# Unmapped Ingredients for Claude Code Curation

**Total:** 13 ingredients
**Category filter:** UNKNOWN

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


## Ingredient 1: UNMAPPED_0074

**Name:** Iron Stock
**Category:** UNKNOWN
**Occurrences:** 1 across 1 media
**Synonyms:** Iron Stock


## Ingredient 2: UNMAPPED_0075

**Name:** Boron Stock
**Category:** UNKNOWN
**Occurrences:** 1 across 1 media
**Synonyms:** Boron Stock


## Ingredient 3: UNMAPPED_0076

**Name:** Bold Trace Stock
**Category:** UNKNOWN
**Occurrences:** 1 across 1 media
**Synonyms:** Bold Trace Stock


## Ingredient 4: UNMAPPED_0079

**Name:** Beef extract
**Category:** UNKNOWN
**Occurrences:** 1 across 1 media
**Synonyms:** Beef extract(Sigma B-4888)


## Ingredient 5: UNMAPPED_0090

**Name:** Trizma Base pH
**Category:** UNKNOWN
**Occurrences:** 1 across 1 media
**Synonyms:** Trizma Base pH 8.2


## Ingredient 6: UNMAPPED_0091

**Name:** A+ Trace Components
**Category:** UNKNOWN
**Occurrences:** 1 across 1 media
**Synonyms:** A+ Trace Components (sterilize before adding)


## Ingredient 7: UNMAPPED_0096

**Name:** Barley grains
**Category:** UNKNOWN
**Occurrences:** 1 across 1 media
**Synonyms:** Barley grains(add after dH2O)


## Ingredient 8: UNMAPPED_0098

**Name:** Sphagnum extract
**Category:** UNKNOWN
**Occurrences:** 1 across 1 media
**Synonyms:** Sphagnum extract


## Ingredient 9: UNMAPPED_0099

**Name:** Organic Peat
**Category:** UNKNOWN
**Occurrences:** 1 across 1 media
**Synonyms:** Organic Peat


## Ingredient 10: UNMAPPED_0100

**Name:** Malt extract
**Category:** UNKNOWN
**Occurrences:** 1 across 1 media
**Synonyms:** Malt extract(Sigma M-0383)


## Ingredient 11: UNMAPPED_0104

**Name:** Barley grains autoclaved
**Category:** UNKNOWN
**Occurrences:** 1 across 1 media
**Synonyms:** Barley grains autoclaved


## Ingredient 12: UNMAPPED_0105

**Name:** Liver extract infusion
**Category:** UNKNOWN
**Occurrences:** 1 across 1 media
**Synonyms:** Liver extract infusion


## Ingredient 13: UNMAPPED_0110

**Name:** Minor Nutrients
**Category:** UNKNOWN
**Occurrences:** 1 across 1 media
**Synonyms:** Minor Nutrients


---

## Summary

After reviewing all ingredients, provide a summary:
- Total suggested mappings
- High confidence (≥0.9) mappings
- Medium confidence (0.7-0.89) mappings
- Low confidence or unmappable items
- Any patterns or insights noticed