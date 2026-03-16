# Unmapped Ingredients - Curation Priority List

**Generated**: 2026-03-15
**Total Unmapped**: 101 ingredients
**Need Curation**: 39 ingredients

---

## Categories

### 1. MAPPABLE - High Priority (11 ingredients)
These can be mapped to CHEBI/FOODON with curation effort:

| Ingredient | Occurrences | Expected Mapping | Notes |
|------------|-------------|------------------|-------|
| dH2O | 22 | CHEBI:15377 (water) | Distilled water abbreviation |
| sterile dH2O | 4 | CHEBI:15377 (water) | Same as dH2O |
| NaH2PO4•H2O | 4 | CHEBI:37586 | Sodium dihydrogen phosphate monohydrate |
| Na2glycerophosphate•5H2O | 4 | CHEBI:131871 | Disodium glycerophosphate pentahydrate |
| Citric Acid•H2O | 3 | CHEBI:35804 | Citric acid monohydrate |
| Water (base) | ? | CHEBI:15377 (water) | Already archived, needs review |
| Soil extract | ? | ENVO term | Environmental sample |
| Natural sea-salt | ? | CHEBI/FOODON | Possibly FOODON:03316427 |
| Peat | ? | ENVO:00005774 | Peat soil |
| Sphagnum extract | ? | Complex | May be unmappable |
| Liver extract infusion | ? | FOODON | Complex biological extract |

### 2. INCOMPLETE FORMULAS - Needs Source Fix (15 ingredients)
These are malformed chemical formulas that should be corrected in CultureMech source data:

| Ingredient | Occurrences | Should Be | CHEBI ID |
|------------|-------------|-----------|----------|
| NaNO | 24 | NaNO₃ | CHEBI:34218 |
| K2HPO | 17 | K₂HPO₄ | CHEBI:32030 |
| MgCO | 11 | MgCO₃ | CHEBI:6611 |
| KH2PO | 11 | KH₂PO₄ | CHEBI:32583 |
| CaCO | 8 | CaCO₃ | CHEBI:3311 |
| KNO | 5 | KNO₃ | CHEBI:63043 |
| NaHCO | 4 | NaHCO₃ | CHEBI:32139 |
| NH4NO | 3 | NH₄NO₃ | CHEBI:63038 |
| Na2CO | 3 | Na₂CO₃ | CHEBI:29377 |
| Ca | 2 | ? | Incomplete |
| K | 2 | ? | Incomplete |
| Mg | 2 | ? | Incomplete |
| Na | 2 | ? | Incomplete |
| Fe | 1 | ? | Incomplete |
| Zn | 1 | ? | Incomplete |

**Action**: Report these to CultureMech for source data correction

### 3. COMPLEX MEDIA - Intentionally Unmapped (58 ingredients)
These are complex mixtures, named media, or solutions that cannot be mapped to simple chemicals:

**Named Media/Solutions** (23):
- Vitamin B, Biotin Vitamin Solution, Thiamine Vitamin Solution
- P-IV Metal Solution, Trace Metals Solution
- F/2 Medium, Bristol Medium, Erdschreiber's Medium
- BG-11 variants, Bold variants, etc.

**Environmental Samples** (10):
- Pasteurized Seawater, Seawater
- CR1 Soil, Green House Soil, Organic Peat
- Soilwater: GR+ Medium, etc.

**Complex Biological** (8):
- Tryptone, Yeast extract, Malt extract
- Proteose Peptone, Beef extract
- Barley grains, Pea

**Buffer/Solution Stocks** (17):
- Enrichment Solution for Seawater Medium
- Chelated Iron Solution, EDTA Stock
- Phosphate Buffer Stock Solution
- Various trace element solutions

### 4. PLACEHOLDERS - Reference Only (4 ingredients)
These are not real ingredients:

| Ingredient | Occurrences | Notes |
|------------|-------------|-------|
| See source for composition | 4917 | Placeholder |
| Full composition available at source database | 196 | Placeholder |
| Original amount: (NH4)2HPO4(Fisher A686) | 4 | Catalog note |
| Original amount: (NH4)2SO4(Fisher A 702) | 1 | Catalog note |

---

## Curation Strategy

### Phase 1: Map the Mappable (11 ingredients) ✨
**Effort**: 1-2 hours
**Tools**: `map-media-ingredients` skill, OAK client, ChEBI search

**Approach**:
1. Use abbreviation expansion (dH2O → distilled water)
2. Search ChEBI for exact chemical matches
3. Validate with chemical properties
4. Add to mapped_ingredients.yaml

### Phase 2: Document Incomplete Formulas (15 ingredients) 📝
**Effort**: 30 minutes
**Action**: Create GitHub issue for CultureMech with list

**Approach**:
1. List all incomplete formulas with corrections
2. Report to CultureMech maintainers
3. Keep in unmapped with notes about source issue

### Phase 3: Mark Complex Media (58 ingredients) 🏷️
**Effort**: 15 minutes
**Action**: Update status to indicate intentionally unmapped

**Approach**:
1. Change status or add notes
2. Mark as "COMPLEX_MIXTURE" or similar
3. Document why they're unmappable

### Phase 4: Archive Placeholders (4 ingredients) 📦
**Effort**: 5 minutes
**Action**: Mark as placeholders

**Approach**:
1. Add notes explaining they're reference markers
2. Keep for traceability but don't curate

---

## Expected Results

After curation:
- **Mapped**: +11 ingredients (move to mapped)
- **Documented incomplete**: 15 (keep in unmapped with notes)
- **Marked complex**: 58 (keep in unmapped with category)
- **Placeholders**: 4 (keep for reference)

**Final state**:
- Mapped ingredients: 1004 → **1015** (+11)
- Truly unmapped: 39 → **28** (-11)
- Unmapped with notes: **77** (58 complex + 15 incomplete + 4 placeholders)

---

## Next Actions

1. **Start with high-value mappable ingredients**:
   ```bash
   # Use the map-media-ingredients skill
   /map-media-ingredients
   ```

2. **For each mappable ingredient**:
   - Expand abbreviations
   - Search ChEBI/FOODON
   - Validate ontology match
   - Accept mapping with evidence

3. **Create CultureMech issue** for incomplete formulas

4. **Update unmapped categories** for complex media and placeholders

---

**Ready to start curation!** 🚀

Priority order:
1. dH2O (22 occ) - easy win
2. NaH2PO4•H2O (4 occ) - straightforward
3. Na2glycerophosphate•5H2O (4 occ) - specific chemical
4. sterile dH2O (4 occ) - same as dH2O
5. Citric Acid•H2O (3 occ) - common chemical
