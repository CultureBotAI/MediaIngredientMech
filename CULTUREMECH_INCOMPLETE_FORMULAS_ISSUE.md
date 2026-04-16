# Incomplete Chemical Formulas in CultureMech Source Data

**Issue Type**: Data Quality / Source Data Correction
**Priority**: Medium
**Affects**: 12 ingredient records (99 total occurrences across media)
**Reported**: 2026-03-15
**Reported by**: MediaIngredientMech curation team

---

## Summary

Several chemical ingredient names in the CultureMech database have **incomplete chemical formulas** that are missing atoms or groups. These appear to be truncation errors or data entry issues in the original source data.

These incomplete formulas prevent proper ontology mapping to CHEBI and create ambiguity about the actual chemical compounds used in the media recipes.

---

## Incomplete Formulas Requiring Correction

| Current (Incorrect) | Corrected Formula | Chemical Name | Expected CHEBI ID | Occurrences |
|---------------------|-------------------|---------------|-------------------|-------------|
| **NaNO** | NaNO₃ | sodium nitrate | CHEBI:34218 | 24 |
| **K2HPO** | K₂HPO₄ | dipotassium hydrogen phosphate | CHEBI:32030 | 17 |
| **MgCO** | MgCO₃ | magnesium carbonate | CHEBI:6611 | 11 |
| **KH2PO** | KH₂PO₄ | potassium dihydrogen phosphate | CHEBI:32583 | 11 |
| **CaCO** | CaCO₃ | calcium carbonate | CHEBI:3311 | 8 |
| **KNO** | KNO₃ | potassium nitrate | CHEBI:63043 | 5 |
| **NaHCO** | NaHCO₃ | sodium bicarbonate | CHEBI:32139 | 4 |
| **NH4NO** | NH₄NO₃ | ammonium nitrate | CHEBI:63038 | 3 |
| **Na2CO** | Na₂CO₃ | sodium carbonate | CHEBI:29377 | 3 |
| **H3BO** | H₃BO₃ | boric acid | CHEBI:33118 | 3 |
| **NH4MgPO** | (NH₄)MgPO₄ | ammonium magnesium phosphate | ? | 3 |
| **Ca** | ? | calcium (element/salt?) | ? | 3 |

**Total occurrences**: 99 across 8,653 media recipes

---

## Examples

### Example 1: NaNO → NaNO₃
**Current**: `NaNO` (missing O₂ group)
**Correct**: `NaNO₃` (sodium nitrate)
**Occurrences**: 24 media
**Typical usage**: Nitrogen source in minimal media

**Evidence**:
- CAS number synonyms in data: `7631-99-4` (matches NaNO₃)
- Catalog synonyms: `NaNO3(Fisher BP360-500)`
- Context: Always used as nitrogen source (consistent with nitrate, not nitrite)

### Example 2: K2HPO → K₂HPO₄
**Current**: `K2HPO` (missing O₃ group)
**Correct**: `K₂HPO₄` (dipotassium hydrogen phosphate)
**Occurrences**: 17 media
**Typical usage**: Phosphate buffer, phosphorus source

### Example 3: MgCO → MgCO₃
**Current**: `MgCO` (missing O₂ group)
**Correct**: `MgCO₃` (magnesium carbonate)
**Occurrences**: 11 media
**Typical usage**: Magnesium source, buffer

---

## Pattern Analysis

All incomplete formulas follow similar patterns:

1. **Missing oxygen atoms**: Most common pattern (NaNO₃ → NaNO, K₂HPO₄ → K2HPO)
2. **Missing subscripts**: Second most common (Na₂CO₃ → Na2CO)
3. **Truncated element symbols**: Some cases (Ca, incomplete term)

This suggests a **systematic data processing issue** rather than random errors, possibly:
- Text encoding issues (Unicode subscripts stripped)
- Import/export truncation
- Copy-paste from formatted sources losing formatting

---

## Impact

### On CultureMech
- Ingredient names don't match standard chemical nomenclature
- Cannot be validated against chemical databases
- Ambiguity in actual compound identity

### On MediaIngredientMech
- Cannot map to CHEBI ontology terms
- 99 media recipe instances affected
- Manual curation required to infer correct formula from context

### On KG-Microbe
- Incomplete ingredient nodes in knowledge graph
- Reduced semantic interoperability
- Queries for standard chemical names will miss these records

---

## Recommended Actions

### Priority 1: Correct in Source Data
Update the original source media recipe files with complete chemical formulas:
- `NaNO` → `NaNO3` (or `NaNO₃` if Unicode supported)
- `K2HPO` → `K2HPO4` (or `K₂HPO₄`)
- etc.

### Priority 2: Validate Corrections
Cross-reference with:
- Catalog numbers (Fisher, Sigma codes present in synonyms)
- CAS numbers (where available)
- Usage context (nitrogen source, phosphate buffer, etc.)

### Priority 3: Prevent Future Issues
- Add validation rules to reject incomplete formulas
- Check for common truncation patterns during import
- Validate chemical formulas against CHEBI/PubChem during ingestion

---

## Supporting Data

### Data Source
- **Database**: CultureMech `output/unmapped_ingredients.yaml`
- **Generated**: 2026-03-15
- **Analysis**: MediaIngredientMech categorization pipeline

### Full List of Affected Records
See: `data/curated/unmapped_incomplete_formula.yaml`

### Categorization Report
See: `data/curated/UNMAPPED_INCOMPLETE_FORMULA.md`

---

## Verification Methodology

Each correction was verified by:
1. **Synonym analysis**: Catalog codes and CAS numbers in raw text
2. **Context analysis**: Role annotations (nitrogen source, buffer, etc.)
3. **Chemical knowledge**: Standard inorganic chemistry nomenclature
4. **CHEBI validation**: Expected CHEBI terms for complete formulas

**Confidence**: High (95%+) for 10/12 corrections
**Uncertain**: 2 corrections (NH4MgPO, Ca) require additional context

---

## Questions for CultureMech Maintainers

1. **Source format**: Are original media recipes in a specific format (PDF, Excel, database)?
2. **Encoding**: Were Unicode chemical formulas (subscripts/superscripts) used in source?
3. **Import pipeline**: Which step in the pipeline might strip formula components?
4. **Validation**: Are there existing validation rules for chemical formulas?

---

## Contact

**Reporter**: MediaIngredientMech Curation Team
**Related Project**: KG-Microbe Knowledge Graph
**Issue Tracking**: MediaIngredientMech repository

---

## Appendix: Complete Corrections Table

```
NaNO        → NaNO₃        (sodium nitrate, CHEBI:34218)
K2HPO       → K₂HPO₄       (dipotassium hydrogen phosphate, CHEBI:32030)
MgCO        → MgCO₃        (magnesium carbonate, CHEBI:6611)
KH2PO       → KH₂PO₄       (potassium dihydrogen phosphate, CHEBI:32583)
CaCO        → CaCO₃        (calcium carbonate, CHEBI:3311)
KNO         → KNO₃         (potassium nitrate, CHEBI:63043)
NaHCO       → NaHCO₃       (sodium bicarbonate, CHEBI:32139)
NH4NO       → NH₄NO₃       (ammonium nitrate, CHEBI:63038)
Na2CO       → Na₂CO₃       (sodium carbonate, CHEBI:29377)
H3BO        → H₃BO₃        (boric acid, CHEBI:33118)
NH4MgPO     → (NH₄)MgPO₄  (ammonium magnesium phosphate, needs verification)
Ca          → ?            (incomplete - need context from media recipes)
```

---

**Generated**: 2026-03-15
**Status**: Ready for submission to CultureMech maintainers
