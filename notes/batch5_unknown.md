# Unmapped Ingredients for Claude Code Curation

**Total:** 15 ingredients
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


## Ingredient 1: UNMAPPED_0022

**Name:** Tryptone
**Category:** UNKNOWN
**Occurrences:** 6 across 6 media
**Synonyms:** Tryptone (Sigma T 9410), Tryptone(CAS: 91079-40-2), Tryptone(Sigma T 9410)


## Ingredient 2: UNMAPPED_0025

**Name:** Yeast extract
**Category:** UNKNOWN
**Occurrences:** 5 across 5 media
**Synonyms:** Yeast extract(Bacto, Difco), Yeast extract(CAS: 8013-01-2)


## Ingredient 3: UNMAPPED_0038

**Name:** Glucose
**Category:** UNKNOWN
**Occurrences:** 3 across 3 media
**Synonyms:** Glucose(BACTO-dextrose or Sigma D 9634)


## Ingredient 4: UNMAPPED_0042

**Name:** Sodium Thiosulfate Pentahydrate
**Category:** UNKNOWN
**Occurrences:** 3 across 3 media
**Normalized:** Sodium Thiosulfate Penta (rules: stripped_hydrate)
**Search variants:** Sodium Thiosulfate Pentahydrate, Sodium Thiosulfate Penta
**Synonyms:** Sodium Thiosulfate Pentahydrate (agar media only,sterile)(Baker 3946)


## Ingredient 5: UNMAPPED_0044

**Name:** Sodium acetate
**Category:** UNKNOWN
**Occurrences:** 3 across 3 media
**Synonyms:** Sodium acetate(Fisher BP 333)


## Ingredient 6: UNMAPPED_0049

**Name:** Ca
**Category:** UNKNOWN
**Occurrences:** 3 across 3 media
**Synonyms:** Ca(NO3)2•4H2O(CAS: 13477-34-4)


## Ingredient 7: UNMAPPED_0052

**Name:** Glycylglycine
**Category:** UNKNOWN
**Occurrences:** 2 across 2 media
**Synonyms:** Glycylglycine(CAS: 556-50-3)


## Ingredient 8: UNMAPPED_0053

**Name:** Ferric Ammonium Citrate
**Category:** UNKNOWN
**Occurrences:** 2 across 2 media
**Synonyms:** Ferric Ammonium Citrate


## Ingredient 9: UNMAPPED_0058

**Name:** Pea
**Category:** UNKNOWN
**Occurrences:** 2 across 2 media
**Synonyms:** Pea, Pea(add after dH2O)


## Ingredient 10: UNMAPPED_0065

**Name:** Tricine
**Category:** UNKNOWN
**Occurrences:** 2 across 2 media
**Synonyms:** Tricine (adjust to pH 8)(Sigma T-5816-256), Tricine(Sigma T-5816-256)


## Ingredient 11: UNMAPPED_0069

**Name:** Proteose Peptone
**Category:** UNKNOWN
**Occurrences:** 2 across 2 media
**Synonyms:** Proteose Peptone(BD 211684)


## Ingredient 12: UNMAPPED_0074

**Name:** Iron Stock
**Category:** UNKNOWN
**Occurrences:** 1 across 1 media
**Synonyms:** Iron Stock


## Ingredient 13: UNMAPPED_0075

**Name:** Boron Stock
**Category:** UNKNOWN
**Occurrences:** 1 across 1 media
**Synonyms:** Boron Stock


## Ingredient 14: UNMAPPED_0076

**Name:** Bold Trace Stock
**Category:** UNKNOWN
**Occurrences:** 1 across 1 media
**Synonyms:** Bold Trace Stock


## Ingredient 15: UNMAPPED_0077

**Name:** Sodium Metasilicate
**Category:** UNKNOWN
**Occurrences:** 1 across 1 media
**Synonyms:** Sodium Metasilicate


---

## Summary

After reviewing all ingredients, provide a summary:
- Total suggested mappings
- High confidence (≥0.9) mappings
- Medium confidence (0.7-0.89) mappings
- Low confidence or unmappable items
- Any patterns or insights noticed