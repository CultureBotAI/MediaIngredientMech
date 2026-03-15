# MediaIngredientMech Merge Pattern Analysis

**Analysis Date:** /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/MediaIngredientMech

## Summary Statistics

- **Total merge clusters:** 211
- **Total merged records:** 498

### Classifications

- ✅ **GOOD_MERGE:** 163 (77.3%)
- ❌ **BAD_MERGE:** 1 (0.5%)
- ⚠️ **NEEDS_REVIEW:** 47 (22.3%)

### Patterns Detected

- **chemical_synonym:** 113
- **case_variation:** 50
- **unclear:** 42
- **hydrate_variant:** 5
- **complex_media_mixed_with_ingredient:** 1

---

## Good Merges (Safe Patterns)

### Pattern: chemical_synonym

**Count:** 113 clusters

**Examples:**

- **NaCl** ← ['sodium chloride', 'NaCL', 'Sodium Chloride', 'Sodium chloride']
  - *Reason:* NaCl / sodium chloride: possible abbreviation
- **Distilled water** ← ['demineralized water', 'tap water', 'Distilled water ', 'Water', 'water', 'H2O', 'Demineralized water', 'Distilled Water', 'distilled water', 'Double distilled water', 'Tap water']
  - *Reason:* Distilled water / demineralized water: shared words {'water'}
- **CaCl2 x 2 H2O** ← ['Calcium chloride dihydrate', 'CaCl2x2H2O', 'CaCl2 x2H2O', 'CaCl22H2O', 'Calcium chloride', 'Calcium Chloride', 'CaCl2·2H2O']
  - *Reason:* CaCl2 x 2 H2O / Calcium chloride dihydrate: chemical formula variants
- **KH2PO4** ← ['Monopotassium phosphate', 'Potassium Phosphate', 'Monopotassium Phosphate']
  - *Reason:* KH2PO4 / Monopotassium phosphate: possible abbreviation
- **H3BO3** ← ['Boric Acid', 'Boric acid']
  - *Reason:* H3BO3 / Boric Acid: chemical formula variants
  - *...and 108 more*

### Pattern: case_variation

**Count:** 50 clusters

**Examples:**

- **Folic acid** ← ['folic acid', 'Folic Acid']
  - *Reason:* All names are case variations: ['Folic acid', 'folic acid', 'Folic Acid']
- **Pyridoxine hydrochloride** ← ['Pyridoxine Hydrochloride']
  - *Reason:* All names are case variations: ['Pyridoxine hydrochloride', 'Pyridoxine Hydrochloride']
- **Resazurin** ← ['resazurin']
  - *Reason:* All names are case variations: ['Resazurin', 'resazurin']
- **Sulfur** ← ['sulfur']
  - *Reason:* All names are case variations: ['Sulfur', 'sulfur']
- **Ethanol** ← ['ethanol']
  - *Reason:* All names are case variations: ['Ethanol', 'ethanol']
  - *...and 45 more*


---

## Bad Merges (Dangerous Patterns)

**Count:** 1 clusters

### 1. Agar

- **Merged records:** 21
- **Pattern:** complex_media_mixed_with_ingredient
- **Confidence:** 0.95

**Merged names:**

- BL Agar
- Brewer anaerobic agar
- Mueller Hinton II agar
- GAM agar
- Legionella agar enrichment
- Malt extract agar
- Columbia blood agar base
- Glycerol-asparagine agar
- Fastidious Anaerobe Agar
- Oatmeal agar
- BCYE agar
- Middlebrook 7H10 agar
- Brucella agar
- Czapek Dox agar
- R agar
- Inorganic salts-starch agar
- R2A agar
- Corn meal agar
- Bacto Middlebrook 7H10 agar
- Marine agar 2216
- agar

**Issues:**

- Complex media detected in 20 record(s)
-   • merged[0]: BL Agar - CHEBI:2509 (agar) with additional terms: ['bl']
-   • merged[1]: Brewer anaerobic agar - Known medium name: Brewer anaerobic agar
-   • merged[2]: Mueller Hinton II agar - CHEBI:2509 (agar) with additional terms: ['mueller', 'hinton', 'ii']
-   • merged[3]: GAM agar - Known medium name: GAM agar
-   • merged[4]: Legionella agar enrichment - Medium pattern match: (?i)\blegionella\s+agar\s+enrichment\b
-   • merged[5]: Malt extract agar - Known medium name: Malt extract agar
-   • merged[6]: Columbia blood agar base - Medium pattern match: (?i)\b(blood|chocolate)\s+agar\b
-   • merged[7]: Glycerol-asparagine agar - Medium pattern match: (?i)\b(malt extract|glycerol-asparagine|inorganic salts-starch)\s+agar\b
-   • merged[8]: Fastidious Anaerobe Agar - Known medium name: Fastidious Anaerobe Agar
-   • merged[9]: Oatmeal agar - Known medium name: Oatmeal agar
-   • merged[10]: BCYE agar - Known medium name: BCYE agar
-   • merged[11]: Middlebrook 7H10 agar - Known medium name: Middlebrook 7H10 agar
-   • merged[12]: Brucella agar - Known medium name: Brucella agar
-   • merged[13]: Czapek Dox agar - Known medium name: Czapek Dox agar
-   • merged[14]: R agar - CHEBI:2509 (agar) with additional terms: ['r']
-   • merged[15]: Inorganic salts-starch agar - Medium pattern match: (?i)\b(malt extract|glycerol-asparagine|inorganic salts-starch)\s+agar\b
-   • merged[16]: R2A agar - Known medium name: R2A agar
-   • merged[17]: Corn meal agar - Known medium name: Corn meal agar
-   • merged[18]: Bacto Middlebrook 7H10 agar - Medium pattern match: (?i)\b(middlebrook|m|r)\s*\d{1,2}(h)?\d{0,2}\b
-   • merged[19]: Marine agar 2216 - Known medium name: Marine agar 2216


---

## Needs Review

**Count:** 47 clusters

### Pattern: unclear

**Count:** 42 clusters

**Examples (first 3):**

- **Biotin** ← ['D-biotin', 'd-Biotin', 'biotin', 'D-Biotin', 'D(+)-Biotin', 'Biotine', 'D-(+)-biotin']
  - *Issues:* Unable to determine if merge is valid
- **Nicotinic acid** ← ['niacin', 'Nicotinic Acid', 'Niacin']
  - *Issues:* Unable to determine if merge is valid
- **Riboflavin** ← ['riboflavin', 'Riboflavine']
  - *Issues:* Unable to determine if merge is valid
  - *...and 39 more*

### Pattern: hydrate_variant

**Count:** 5 clusters

**Examples (first 3):**

- **Thiamine HCl** ← ['thiamine-HCl', 'thiamine hydrochloride', 'Thiamine dihydrochloride', 'Thiamine·HCl', 'Thiamin-HCl', 'Thiamine hydrochloride', 'Thiamine-HCl']
  - *Issues:* Hydrate forms might benefit from hierarchy instead of merge
- **Na-acetate** ← ['Na-Acetate', 'Na Acetate', 'Sodium acetate·3H2O', '1 M Sodium acetate', 'Sodium Acetate', 'sodium acetate', 'Na acetate', 'Sodium acetate']
  - *Issues:* Hydrate forms might benefit from hierarchy instead of merge
- **Pyridoxine-HCl** ← ['pyridoxine-HCl', 'pyridoxamine-HCl', 'Pyridoxine·HCl', 'Pyridoxamine-HCl', 'Pyridoxamine hydrochloride', 'Pyridoxine HCl']
  - *Issues:* Hydrate forms might benefit from hierarchy instead of merge
  - *...and 2 more*


---

## Recommendations

### Pre-Merge Validation Rules

Based on this analysis, implement these safety checks before merging:

1. **Complex Media Detection**
   - Run `detect_complex_medium()` on all records
   - Block merge if confidence >= 0.75
   - Rationale: Prevents recipes from merging into ingredients

2. **Ingredient Type Consistency**
   - Verify all records have same `ingredient_type`
   - Block merge if types differ
   - Rationale: Different types indicate different semantic categories

3. **Pattern Matching**
   - Prefer merges with clear patterns (case, synonym, abbreviation)
   - Flag unclear patterns for manual review
   - Rationale: Ambiguous merges risk data corruption

4. **Hydrate Handling**
   - Consider hierarchy instead of merge for hydrate variants
   - Flag for expert review
   - Rationale: Different hydration states may have different properties

### Implementation in CHEBIDeduplicator

Update `should_auto_merge()` method to include:

```python
# Check ingredient_type
if target_type != source_type:
    return False, 'Different ingredient types'

# Check complex media
is_complex, conf, reason = detect_complex_medium(name, chebi)
if is_complex and conf >= 0.75:
    return False, f'Complex media: {reason}'
```
