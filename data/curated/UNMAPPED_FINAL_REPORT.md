# Unmapped Ingredients - Final Report
**Date**: 2026-03-15
**Total Unmapped**: 90 ingredients (after mapping 11 high-priority ingredients)

---

## Summary by Category

| Category | Count | Status | Action Required |
|----------|-------|--------|-----------------|
| **INCOMPLETE_FORMULA** | 12 | ⚠️ Source Issue | Report to CultureMech for correction |
| **COMPLEX_MEDIA** | 61 | ✅ Intentional | Mark as intentionally unmappable |
| **PLACEHOLDER** | 7 | ✅ Reference | Mark as reference-only (not real ingredients) |
| **ALREADY_MAPPED** | 3 | 🔧 Cleanup | Remove from unmapped (encoding duplicates) |
| **OTHER** | 7 | 🔍 Review | 5 mappable, 2 need expert review |

**Total**: 90 ingredients

---

## Category Details

### 1. INCOMPLETE_FORMULA (12 ingredients) ⚠️

**Issue**: Malformed chemical formulas in CultureMech source data

**Top 5 by Occurrence**:
1. NaNO (24 occ) → should be NaNO₃ (CHEBI:34218)
2. K2HPO (17 occ) → should be K₂HPO₄ (CHEBI:32030)
3. MgCO (11 occ) → should be MgCO₃ (CHEBI:6611)
4. KH2PO (11 occ) → should be KH₂PO₄ (CHEBI:32583)
5. CaCO (8 occ) → should be CaCO₃ (CHEBI:3311)

**Full List**:
| Ingredient | Occ | Correct Formula | Expected CHEBI ID |
|------------|-----|-----------------|-------------------|
| NaNO | 24 | NaNO₃ | CHEBI:34218 |
| K2HPO | 17 | K₂HPO₄ | CHEBI:32030 |
| MgCO | 11 | MgCO₃ | CHEBI:6611 |
| KH2PO | 11 | KH₂PO₄ | CHEBI:32583 |
| CaCO | 8 | CaCO₃ | CHEBI:3311 |
| KNO | 5 | KNO₃ | CHEBI:63043 |
| NaHCO | 4 | NaHCO₃ | CHEBI:32139 |
| NH4NO | 3 | NH₄NO₃ | CHEBI:63038 |
| Na2CO | 3 | Na₂CO₃ | CHEBI:29377 |
| NH4MgPO | 3 | (NH₄)MgPO₄ | ? |
| H3BO | 3 | H₃BO₃ | CHEBI:33118 |
| Ca | 3 | ? (incomplete) | ? |

**Action Required**:
- Report to CultureMech maintainers for source data correction
- Keep in unmapped with notes about source issue
- Do NOT map in MediaIngredientMech (preserve source accuracy)

---

### 2. COMPLEX_MEDIA (61 ingredients) ✅

**Status**: Intentionally unmappable (complex mixtures, named media, solutions)

**Top 10 by Occurrence**:
1. Vitamin B (23 occ) - vitamin solution
2. Pasteurized Seawater (19 occ) - environmental sample
3. Biotin Vitamin Solution (18 occ) - vitamin solution
4. P-IV Metal Solution (16 occ) - trace metal solution
5. Soilwater: GR+ Medium (15 occ) - environmental medium
6. Seawater (12 occ) - environmental sample
7. Thiamine Vitamin Solution (12 occ) - vitamin solution
8. Vitamin mix (11 occ) - vitamin solution
9. F/2 Medium (7 occ) - named medium
10. Trace Metals Solution (7 occ) - trace metal solution

**Subcategories**:
- **Named Media/Solutions** (23): BG-11 variants, Bold variants, F/2 Medium, etc.
- **Environmental Samples** (10): Seawater, Pasteurized Seawater, Soilwater, etc.
- **Vitamin Solutions** (12): Vitamin B, Biotin Solution, Thiamine Solution, etc.
- **Metal Solutions** (8): P-IV Metal Solution, Trace Metals Solution, Iron Stock, etc.
- **Other Complex** (8): Enrichment solutions, buffer stocks, etc.

**Action Required**:
- Mark as intentionally unmappable
- Update status or add notes to indicate complex mixture
- Keep for traceability

---

### 3. PLACEHOLDER (7 ingredients) ✅

**Status**: Reference markers, not real ingredients

**List**:
1. See source for composition (4917 occ) - reference marker
2. Full composition available at source database (196 occ) - reference marker
3. Original amount: (NH4)2HPO4(Fisher A686) (4 occ) - catalog note
4. Original amount: (NH4)2SO4(Fisher A 702) (1 occ) - catalog note
5. [Merged 63 duplicates: 5.0, 1.0, 5.0, 1.0] (1 occ) - merge artifact
6. [Merged 10 duplicates: 2.0, 1.0] (1 occ) - merge artifact
7. [Merged 2 duplicates: 5.0, 20.0] (1 occ) - merge artifact

**Action Required**:
- Mark as placeholders
- Add notes explaining they're reference markers
- Keep for traceability but don't curate

---

### 4. ALREADY_MAPPED (3 ingredients) 🔧

**Status**: Encoding duplicates of already mapped ingredients

**List**:
1. Na2Glycerophosphate.5H2O (1 occ) → mapped as Na2glycerophosphate•5H2O (CHEBI:131871)
2. Sterile dH2O (1 occ) → mapped as sterile dH2O (CHEBI:15377)
3. Na2Glycerophosphate•5H2O (1 occ) → mapped as Na2glycerophosphate•5H2O (CHEBI:131871)

**Action Required**:
- Remove from unmapped_ingredients.yaml
- These are encoding variants (• vs . vs different case) of already mapped ingredients
- Clean up to avoid confusion

---

### 5. OTHER (7 ingredients) 🔍

**Status**: Need individual review - mostly mappable

**Mappable to CHEBI/FOODON** (5 ingredients):
1. **Tricine** (2 occ) → CHEBI:16325 (buffer, exact match)
2. **Sodium Metasilicate** (1 occ) → CHEBI:86314 (exact match)
3. **TES buffer** (1 occ) → CHEBI:9330 (exact match)
4. **Barley grains** (1 occ) → FOODON term for barley grain
5. **Barley grains autoclaved** (1 occ) → FOODON term for barley grain (autoclaved variant)

**Need Expert Review** (2 ingredients):
6. **Trizma Base pH** (1 occ) → Unclear (Tris base + pH adjustment? Generic?)
7. **FE EDTA** (1 occ) → Iron-EDTA complex (may be generic chelate solution)

**Action Required**:
- Map the 5 clearly mappable ingredients
- Expert review for the 2 ambiguous ones

---

## Current Progress

### Mapping Progress
- **Starting unmapped**: 101 ingredients
- **Mapped this session**: 11 ingredients
  - dH2O → CHEBI:15377
  - sterile dH2O → CHEBI:15377
  - NaH2PO4•H2O → CHEBI:37586
  - Na2glycerophosphate•5H2O → CHEBI:131871
  - Citric Acid•H2O → CHEBI:35804
  - Organic Peat → ENVO:00005774
  - Natural sea-salt → FOODON:03316427
  - Liver extract infusion → FOODON:03301154
  - Glycylglycine → CHEBI:73998
  - Na2HPO4•7H2O → CHEBI:34702
  - Pea → FOODON:00002753
- **Current unmapped**: 90 ingredients
- **Total mapped**: 1015 ingredients

### Breakdown
- **Truly unmappable**: 68 (61 complex media + 7 placeholders)
- **Source issues**: 12 (incomplete formulas)
- **Encoding duplicates**: 3 (should be removed)
- **Mappable**: 7 (need curation)

---

## Next Steps

### Immediate (5 minutes)
1. ✅ **Categorize unmapped** → COMPLETE
2. ⏭️ **Remove encoding duplicates** (3 ingredients from ALREADY_MAPPED)
   - Clean up unmapped_ingredients.yaml
   - Reduce unmapped count to 87

### Short-term (30 minutes)
3. ⏭️ **Map remaining mappable ingredients** (7 from OTHER)
   - Tricine, Sodium Metasilicate, TES buffer
   - Barley grains variants
   - Expert review for Trizma Base pH and FE EDTA
   - Expected: 87 → ~82 unmapped

### Medium-term (1 hour)
4. ⏭️ **Mark complex media as intentionally unmappable** (61 ingredients)
   - Update status or add category field
   - Document why unmappable

5. ⏭️ **Mark placeholders as reference-only** (7 ingredients)
   - Add notes explaining they're not real ingredients

### Long-term (2 hours)
6. ⏭️ **Create CultureMech issue for incomplete formulas** (12 ingredients)
   - List all incomplete formulas with corrections
   - Provide expected CHEBI IDs
   - Submit to CultureMech maintainers

---

## Expected Final State

After completing all steps:
- **Mapped ingredients**: 1015 → ~1020 (+5 from OTHER)
- **Truly unmapped**: 82 ingredients
  - 61 complex media (intentionally unmappable)
  - 12 incomplete formulas (waiting for source fix)
  - 7 placeholders (reference-only)
  - 2 expert review (ambiguous)
- **Unmapped with clear status**: 100%

---

## Files Generated

### Category YAML Files
- `unmapped_placeholder.yaml` (7 ingredients)
- `unmapped_complex_media.yaml` (61 ingredients)
- `unmapped_incomplete_formula.yaml` (12 ingredients)
- `unmapped_already_mapped.yaml` (3 ingredients)
- `unmapped_other.yaml` (7 ingredients)

### Markdown Reports
- `UNMAPPED_CATEGORIES_SUMMARY.md` - Overview by category
- `UNMAPPED_PLACEHOLDER.md` - Placeholder details
- `UNMAPPED_COMPLEX_MEDIA.md` - Complex media details
- `UNMAPPED_INCOMPLETE_FORMULA.md` - Incomplete formulas with corrections
- `UNMAPPED_ALREADY_MAPPED.md` - Encoding duplicates to remove
- `UNMAPPED_OTHER.md` - Mappable ingredients needing review
- `UNMAPPED_FINAL_REPORT.md` - This comprehensive report

---

**Report Date**: 2026-03-15
**Status**: ✅ Categorization Complete
**Next**: Remove encoding duplicates, map remaining 7 ingredients
