# Good Merge Examples Catalog

**Purpose:** Reference examples of valid merges for training and validation

**Source:** Pattern analysis of 211 merge clusters (163 good merges = 77.3%)

---

## Pattern 1: Case Variation (50 clusters)

**Definition:** Identical names differing only in capitalization

**Confidence:** 100% safe

### Examples

#### Example 1: Folic acid
```yaml
representative: "Folic acid"
merged:
  - "folic acid"
  - "Folic Acid"
```
**Why safe:** Exact match when normalized to lowercase

---

#### Example 2: Resazurin
```yaml
representative: "Resazurin"
merged:
  - "resazurin"
```
**Why safe:** Chemical names are case-insensitive

---

#### Example 3: Ethanol
```yaml
representative: "Ethanol"
merged:
  - "ethanol"
```
**Why safe:** Common chemical, case variation only

---

#### Example 4: Pyridoxine hydrochloride
```yaml
representative: "Pyridoxine hydrochloride"
merged:
  - "Pyridoxine Hydrochloride"
```
**Why safe:** Title case vs sentence case

---

#### Example 5: Sulfur
```yaml
representative: "Sulfur"
merged:
  - "sulfur"
```
**Why safe:** Element name, case-insensitive

---

### More Examples (45 additional)

- Thiamine ⬅ thiamine
- Riboflavin ⬅ riboflavin
- Pyridoxal ⬅ pyridoxal
- Pantothenic acid ⬅ pantothenic acid
- Lipoic acid ⬅ lipoic acid
- Cobalamin ⬅ cobalamin
- Ascorbic acid ⬅ ascorbic acid
- Phylloquinone ⬅ phylloquinone
- Menaquinone ⬅ menaquinone
- Tocopherol ⬅ tocopherol

---

## Pattern 2: Chemical Synonyms (113 clusters)

**Definition:** Different names for the same chemical entity, verified by shared CHEBI ID

**Confidence:** 90% safe (requires verification)

### Sub-pattern 2a: Formula + Systematic Name

#### Example 1: NaCl
```yaml
representative: "NaCl"
CHEBI: "CHEBI:26710"
merged:
  - "sodium chloride"     # Systematic name
  - "NaCL"                # Typo variant
  - "Sodium Chloride"     # Title case
  - "Sodium chloride"     # Sentence case
```
**Why safe:**
- Same CHEBI ID
- NaCl is standard chemical formula
- "sodium chloride" is IUPAC systematic name
- All are true synonyms

---

#### Example 2: KH2PO4
```yaml
representative: "KH2PO4"
CHEBI: "CHEBI:63036"
merged:
  - "Monopotassium phosphate"   # Systematic name
  - "Potassium Phosphate"       # Common name
  - "Monopotassium Phosphate"   # Title case
```
**Why safe:**
- Same CHEBI ID
- Formula matches composition
- All refer to same salt

---

#### Example 3: H3BO3
```yaml
representative: "H3BO3"
CHEBI: "CHEBI:33118"
merged:
  - "Boric Acid"
  - "Boric acid"
```
**Why safe:**
- Chemical formula + common name
- Same CHEBI ID
- Case variations

---

#### Example 4: Na2MoO4
```yaml
representative: "Na2MoO4"
CHEBI: "CHEBI:75218"
merged:
  - "Sodium molybdate"
  - "sodium molybdate"
```
**Why safe:**
- Formula + systematic name
- Same composition

---

### Sub-pattern 2b: Hydrated Salts (with caution)

#### Example 5: CaCl2 x 2 H2O
```yaml
representative: "CaCl2 x 2 H2O"
CHEBI: "CHEBI:3312"
merged:
  - "Calcium chloride dihydrate"  # Systematic name
  - "CaCl2x2H2O"                  # Spacing variant
  - "CaCl2 x2H2O"                 # Spacing variant
  - "CaCl22H2O"                   # No spaces
  - "Calcium chloride"            # ⚠️ May be ambiguous
  - "Calcium Chloride"            # Case variant
  - "CaCl2·2H2O"                  # Unicode dot
```
**Why merged (with caution):**
- All share CHEBI:3312 (dihydrate form)
- "Calcium chloride" often implies dihydrate in practice
- **Note:** Technically "Calcium chloride" could be anhydrous
- **Better approach:** Verify all source media actually used dihydrate

---

### Sub-pattern 2c: Water Variants

#### Example 6: Distilled water
```yaml
representative: "Distilled water"
CHEBI: "CHEBI:15377" (water)
merged:
  - "demineralized water"      # Similar purity
  - "tap water"                # ⚠️ Lower purity
  - "Distilled water "         # Trailing space
  - "Water"                    # Generic
  - "water"                    # Lowercase
  - "H2O"                      # Formula
  - "Demineralized water"      # Title case
  - "Distilled Water"          # Title case
  - "distilled water"          # Lowercase
  - "Double distilled water"   # ⚠️ Higher purity
  - "Tap water"                # ⚠️ Lower purity
```
**Why merged (CONTROVERSIAL):**
- All share CHEBI:15377 (water)
- **Issues:**
  - Tap water contains minerals
  - Double distilled is higher purity
  - These distinctions may matter for media
- **Better approach:** Use hierarchy with purity levels

---

### Sub-pattern 2d: Multiple Formula Notations

#### Example 7: MgSO4·7H2O
```yaml
representative: "MgSO4·7H2O"
CHEBI: "CHEBI:31795"
merged:
  - "MgSO4.7H2O"              # Period instead of dot
  - "Magnesium sulfate heptahydrate"
  - "Magnesium sulfate 7-hydrate"
```
**Why safe:**
- Same CHEBI ID
- Different notations for same compound
- Unicode vs ASCII dot

---

### Sub-pattern 2e: Common Name + Systematic Name

#### Example 8: Vitamin B12
```yaml
representative: "Vitamin B12"
CHEBI: "CHEBI:176843"
merged:
  - "Cyanocobalamin"          # Chemical name
  - "cobalamin"               # Generic term
```
**Why safe:**
- Vitamin B12 is common name for cyanocobalamin
- Same CHEBI ID confirms equivalence

---

#### Example 9: Vitamin B1
```yaml
representative: "Thiamine"
CHEBI: "CHEBI:18385"
merged:
  - "Thiamine hydrochloride"  # Salt form
  - "Vitamin B1"              # Common name
```
**Why safe:**
- B1 = thiamine (standard equivalence)
- Hydrochloride is common salt form

---

### More Chemical Synonym Examples (100+ additional)

**Salts:**
- Na2HPO4 ⬅ Disodium phosphate, Sodium phosphate dibasic
- (NH4)2SO4 ⬅ Ammonium sulfate
- FeSO4 ⬅ Ferrous sulfate, Iron(II) sulfate
- CuSO4 ⬅ Copper sulfate, Copper(II) sulfate
- ZnSO4 ⬅ Zinc sulfate

**Acids:**
- H2SO4 ⬅ Sulfuric acid
- HCl ⬅ Hydrochloric acid
- CH3COOH ⬅ Acetic acid
- C6H8O7 ⬅ Citric acid

**Vitamins:**
- Vitamin C ⬅ Ascorbic acid, L-ascorbic acid
- Vitamin K1 ⬅ Phylloquinone
- Vitamin E ⬅ α-tocopherol

**Sugars:**
- Glucose ⬅ D-glucose, Dextrose
- Fructose ⬅ D-fructose
- Sucrose ⬅ Table sugar

---

## Pattern Recognition Guide

### How to Verify a Chemical Synonym Merge

1. **Check CHEBI ID match** ✓ Required
2. **Verify name relationship:**
   - Formula + systematic name? ✓ Safe
   - Abbreviation + full name? ✓ Safe
   - Common + systematic name? ✓ Safe
   - Hydrate variants? ⚠️ Caution
   - Purity variants? ⚠️ Consider hierarchy
3. **Check for semantic differences:**
   - Stereoisomers (D/L)? ⚠️ Different compounds
   - Purity levels? ⚠️ May matter
   - Hydration state specified? ⚠️ May matter
4. **Verify no complex media:** Use `detect_complex_medium()` ✓

### Green Flags (Safe to Merge)

- ✓ One is chemical formula, other is systematic name
- ✓ One is abbreviation, matches full name
- ✓ All share same CHEBI ID
- ✓ No complex media detected
- ✓ No stereochemistry differences
- ✓ Same ingredient_type (if set)

### Yellow Flags (Needs Review)

- ⚠️ Hydrate variants (may need hierarchy)
- ⚠️ Purity qualifiers (tap/distilled/ultra-pure)
- ⚠️ Generic + specific forms
- ⚠️ Multiple salt forms

### Red Flags (Do NOT Merge)

- ❌ Different CHEBI IDs
- ❌ Complex media detected
- ❌ Stereoisomer differences (D/L prefix)
- ❌ Different ingredient_type
- ❌ One is recipe, other is ingredient

---

## Statistics

**Total Good Merges:** 163 clusters (77.3%)

**By Pattern:**
- Chemical synonyms: 113 (69.3%)
- Case variations: 50 (30.7%)

**By Merge Count:**
- 2-3 merged records: 85 clusters (52.1%)
- 4-7 merged records: 52 clusters (31.9%)
- 8+ merged records: 26 clusters (16.0%)

**Largest Merge:**
- Distilled water: 11 merged records (includes tap water, H2O, double distilled - CONTROVERSIAL)

---

## Usage

**For Training:**
- Show curators these examples during onboarding
- Use as reference when uncertain about merge decisions
- Practice pattern recognition with real data

**For Validation:**
- Compare new merges against these patterns
- Flag deviations for review
- Update catalog with new validated patterns

**For Testing:**
- Use these as test cases for merge logic
- Verify automated merges match expected results
- Regression testing after code changes

---

**Last Updated:** 2026-03-14
**Source:** `analysis/merge_pattern_analysis.yaml`
