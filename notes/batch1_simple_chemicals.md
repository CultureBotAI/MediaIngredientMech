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


## Ingredient 1: UNMAPPED_0003

**Name:** MgSO4•7H2O
**Category:** SIMPLE_CHEMICAL
**Occurrences:** 29 across 29 media
**Normalized:** MgSO4 (rules: stripped_hydrate)
**Search variants:** MgSO4•7H2O, MgSO4, magnesium sulfate
**Synonyms:** MgSO4•7H2O (Sigma 230391), MgSO4•7H2O(CAS: 10034-99-8), MgSO4•7H2O(Sigma 230391)


## Ingredient 2: UNMAPPED_0004

**Name:** NaNO
**Category:** SIMPLE_CHEMICAL
**Occurrences:** 24 across 24 media
**Normalized:** NaNO3 (rules: fixed_incomplete_formula)
**Search variants:** NaNO, NaNO3, sodium nitrate
**Synonyms:** NaNO3(CAS: 7631-99-4), NaNO3(Fisher BP360-500), NaNO3(autoclave before adding)(Fisher BP360-500)


## Ingredient 3: UNMAPPED_0006

**Name:** dH2O
**Category:** SIMPLE_CHEMICAL
**Occurrences:** 22 across 22 media
**Synonyms:** dH2O


## Ingredient 4: UNMAPPED_0007

**Name:** CaCl2•2H2O
**Category:** SIMPLE_CHEMICAL
**Occurrences:** 22 across 22 media
**Normalized:** CaCl2 (rules: stripped_hydrate)
**Search variants:** CaCl2•2H2O, CaCl2, calcium chloride
**Synonyms:** CaCl2•2H2O (Sigma C-3881), CaCl2•2H2O(CAS: 10035-04-8), CaCl2•2H2O(Sigma C-3881)


## Ingredient 5: UNMAPPED_0010

**Name:** K2HPO
**Category:** SIMPLE_CHEMICAL
**Occurrences:** 17 across 17 media
**Normalized:** K2HPO4 (rules: fixed_incomplete_formula)
**Search variants:** K2HPO, K2HPO4, dipotassium phosphate
**Synonyms:** K2HPO4(Sigma P 3786)


## Ingredient 6: UNMAPPED_0011

**Name:** P-IV Metal Solution
**Category:** SIMPLE_CHEMICAL
**Occurrences:** 16 across 16 media
**Synonyms:** P-IV Metal Solution


## Ingredient 7: UNMAPPED_0015

**Name:** NaCl
**Category:** SIMPLE_CHEMICAL
**Occurrences:** 13 across 13 media
**Synonyms:** NaCl (Fisher S271-500), NaCl(Fisher S271-500)


## Ingredient 8: UNMAPPED_0016

**Name:** Na2SiO3•9H2O
**Category:** SIMPLE_CHEMICAL
**Occurrences:** 11 across 11 media
**Normalized:** Na2SiO3 (rules: stripped_hydrate)
**Search variants:** Na2SiO3•9H2O, Na2SiO3
**Synonyms:** Na2SiO3•9H2O(CAS: 13517-24-3), Na2SiO3•9H2O(Sigma 307815)


## Ingredient 9: UNMAPPED_0017

**Name:** MgCO
**Category:** SIMPLE_CHEMICAL
**Occurrences:** 11 across 11 media
**Normalized:** MgCO3 (rules: fixed_incomplete_formula)
**Search variants:** MgCO, MgCO3
**Synonyms:** MgCO3(MCIB CB486)


## Ingredient 10: UNMAPPED_0018

**Name:** KH2PO
**Category:** SIMPLE_CHEMICAL
**Occurrences:** 11 across 11 media
**Normalized:** KH2PO4 (rules: fixed_incomplete_formula)
**Search variants:** KH2PO, KH2PO4, monopotassium phosphate
**Synonyms:** KH2PO4(Sigma P 0662)


## Ingredient 11: UNMAPPED_0020

**Name:** KCl
**Category:** SIMPLE_CHEMICAL
**Occurrences:** 10 across 10 media
**Synonyms:** KCl (Fisher P 217), KCl(CAS: 7447-40-7), KCl(CAS:7447-40-7)


## Ingredient 12: UNMAPPED_0021

**Name:** CaCO
**Category:** SIMPLE_CHEMICAL
**Occurrences:** 9 across 9 media
**Normalized:** CaCO3 (rules: fixed_incomplete_formula)
**Search variants:** CaCO, CaCO3
**Synonyms:** CaCO3(Fisher C 64), CaCO3(optional) (Fisher C 64), CaCO3(optional)(Fisher C 64)


## Ingredient 13: UNMAPPED_0026

**Name:** KNO
**Category:** SIMPLE_CHEMICAL
**Occurrences:** 5 across 5 media
**Synonyms:** KNO3(Baker 3190)


## Ingredient 14: UNMAPPED_0028

**Name:** NaH2PO4•H2O
**Category:** SIMPLE_CHEMICAL
**Occurrences:** 4 across 4 media
**Synonyms:** NaH2PO4•H2O(MCIB 742)


## Ingredient 15: UNMAPPED_0030

**Name:** Na2glycerophosphate•5H2O
**Category:** SIMPLE_CHEMICAL
**Occurrences:** 4 across 4 media
**Normalized:** Na2glycerophosphate (rules: stripped_hydrate)
**Search variants:** Na2glycerophosphate•5H2O, Na2glycerophosphate
**Synonyms:** Na2glycerophosphate•5H2O(CAS: 13408-09-8), Na2glycerophosphate•5H2O(CAS:  13408-09-8)


## Ingredient 16: UNMAPPED_0032

**Name:** sterile dH2O
**Category:** SIMPLE_CHEMICAL
**Occurrences:** 4 across 4 media
**Synonyms:** sterile dH2O


## Ingredient 17: UNMAPPED_0034

**Name:** NH4Cl
**Category:** SIMPLE_CHEMICAL
**Occurrences:** 4 across 4 media
**Synonyms:** NH4Cl(CAS: 12125-02-9), NH4Cl(Fisher A 649-500)


## Ingredient 18: UNMAPPED_0035

**Name:** NaHCO
**Category:** SIMPLE_CHEMICAL
**Occurrences:** 4 across 4 media
**Synonyms:** NaHCO3(Fisher S 233)


## Ingredient 19: UNMAPPED_0036

**Name:** Original amount: (NH4)2HPO4(Fisher A686)
**Category:** SIMPLE_CHEMICAL
**Occurrences:** 4 across 4 media
**Normalized:** Original amount: (NH4)2HPO4 (rules: stripped_catalog)
**Search variants:** Original amount: (NH4)2HPO4(Fisher A686), Original amount: (NH4)2HPO4
**Synonyms:** (NH4)2HPO4(Fisher A686)


## Ingredient 20: UNMAPPED_0037

**Name:** NH4NO
**Category:** SIMPLE_CHEMICAL
**Occurrences:** 3 across 3 media
**Synonyms:** NH4NO3(CAS: 6484-52-2)


---

## Summary

After reviewing all ingredients, provide a summary:
- Total suggested mappings
- High confidence (≥0.9) mappings
- Medium confidence (0.7-0.89) mappings
- Low confidence or unmappable items
- Any patterns or insights noticed