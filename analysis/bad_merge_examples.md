# Bad Merge Examples Catalog

**Purpose:** Document incorrect merges to prevent future mistakes

**Source:** Pattern analysis of 211 merge clusters (1 bad merge cluster = 0.5%, but affecting 21 records!)

---

## Critical Finding

Only **ONE** bad merge cluster was detected, but it contained **21 incorrectly merged records**, demonstrating how a single bad merge decision can corrupt significant amounts of data.

---

## The Agar Mega-Merge (CRITICAL ERROR)

### Overview

**Representative:** `Agar` (CHEBI:2509)

**Pattern:** complex_media_mixed_with_ingredient

**Confidence:** 0.95 (very high certainty this is wrong)

**Impact:** 21 records merged, 20 of which are complex media recipes

---

### What Went Wrong

The merge logic used **only CHEBI ID matching**, treating all records with CHEBI:2509 (agar) as the same entity. However:

- **"Agar"** = Pure polysaccharide solidifying agent
- **"R2A agar"** = Complete defined medium with 10+ ingredients
- **"Marine agar 2216"** = ATCC reference medium with specific formulation

These are **fundamentally different entities** that happen to share the same CHEBI ID because they all **contain** agar as an ingredient.

---

### The One Correct Merge

```yaml
representative: "Agar"
correctly_merged:
  - "agar"  # ✓ Case variation only
```

**Why correct:** Exact same substance, just lowercase

---

### The 20 Incorrect Merges

#### Category 1: Named ATCC/Reference Media (6 records)

These are standardized, published media formulations with specific codes:

##### 1. Marine agar 2216
```yaml
name: "Marine agar 2216"
CHEBI: "CHEBI:2509"
detection: "Known medium name: Marine agar 2216"
confidence: 0.95
```
**Why wrong:**
- ATCC catalog number 2216
- Contains: peptone, yeast extract, ferric citrate, NaCl, agar, seawater
- Used for marine bacteria isolation
- Distinct formulation ≠ pure agar

**Correct action:** Separate record with ingredient_type: DEFINED_MEDIUM

---

##### 2. R2A agar
```yaml
name: "R2A agar"
CHEBI: "CHEBI:2509"
detection: "Known medium name: R2A agar"
confidence: 0.95
```
**Why wrong:**
- Reasoner's 2A medium
- Contains: yeast extract, proteose peptone, casamino acids, glucose, starch, K2HPO4, MgSO4, pyruvate, agar
- Low-nutrient medium for oligotrophic bacteria
- 10+ ingredients ≠ pure agar

**Correct action:** Separate record, link to ingredient list

---

##### 3. GAM agar
```yaml
name: "GAM agar"
CHEBI: "CHEBI:2509"
detection: "Known medium name: GAM agar"
confidence: 0.95
```
**Why wrong:**
- Gifu Anaerobic Medium
- For anaerobic bacteria culture
- Complex formulation with reducing agents
- Not just agar

---

##### 4. BCYE agar
```yaml
name: "BCYE agar"
CHEBI: "CHEBI:2509"
detection: "Known medium name: BCYE agar"
confidence: 0.95
```
**Why wrong:**
- Buffered Charcoal Yeast Extract agar
- For Legionella isolation
- Contains activated charcoal, L-cysteine, ferric pyrophosphate
- Specialized selective medium

---

##### 5. Brewer anaerobic agar
```yaml
name: "Brewer anaerobic agar"
CHEBI: "CHEBI:2509"
detection: "Known medium name: Brewer anaerobic agar"
confidence: 0.95
```
**Why wrong:**
- For anaerobic culture
- Contains reducing agents
- Not equivalent to pure agar

---

##### 6. Brucella agar
```yaml
name: "Brucella agar"
CHEBI: "CHEBI:2509"
detection: "Known medium name: Brucella agar"
confidence: 0.95
```
**Why wrong:**
- For Brucella spp. culture
- Enriched formulation
- Not pure agar

---

#### Category 2: Middlebrook Media (Mycobacterium culture) (2 records)

##### 7. Middlebrook 7H10 agar
```yaml
name: "Middlebrook 7H10 agar"
CHEBI: "CHEBI:2509"
detection: "Known medium name: Middlebrook 7H10 agar"
confidence: 0.95
```

##### 8. Bacto Middlebrook 7H10 agar
```yaml
name: "Bacto Middlebrook 7H10 agar"
CHEBI: "CHEBI:2509"
detection: "Medium pattern match: (?i)\b(middlebrook|m|r)\s*\d{1,2}(h)?\d{0,2}\b"
confidence: 0.85
```

**Why wrong (both):**
- For Mycobacterium tuberculosis culture
- Contains: malachite green (selective agent), glycerol, oleic acid, albumin, catalase, salts
- Critical for TB diagnosis
- Brand name "Bacto" indicates commercial formulation

---

#### Category 3: Ingredient + Modifier Media (5 records)

These are formulations where agar is combined with one other primary ingredient:

##### 9. Corn meal agar
```yaml
name: "Corn meal agar"
CHEBI: "CHEBI:2509"
detection: "Known medium name: Corn meal agar"
confidence: 0.95
```
**Why wrong:**
- Corn meal + agar (2-component)
- For fungal morphology studies
- Corn meal provides nutrients

---

##### 10. Oatmeal agar
```yaml
name: "Oatmeal agar"
CHEBI: "CHEBI:2509"
detection: "Known medium name: Oatmeal agar"
confidence: 0.95
```
**Why wrong:**
- Oatmeal + agar
- For Actinomycetes culture
- Oatmeal is nutrient source

---

##### 11. Malt extract agar
```yaml
name: "Malt extract agar"
CHEBI: "CHEBI:2509"
detection: "Known medium name: Malt extract agar"
confidence: 0.95
```
**Why wrong:**
- Malt extract + agar
- For fungi and yeast culture
- Malt extract is complex nutrient

---

##### 12. Glycerol-asparagine agar
```yaml
name: "Glycerol-asparagine agar"
CHEBI: "CHEBI:2509"
detection: "Medium pattern match: (?i)\b(malt extract|glycerol-asparagine|inorganic salts-starch)\s+agar\b"
confidence: 0.95
```
**Why wrong:**
- For Streptomyces culture
- Defined nutrient composition
- Not pure agar

---

##### 13. Inorganic salts-starch agar
```yaml
name: "Inorganic salts-starch agar"
CHEBI: "CHEBI:2509"
detection: "Medium pattern match: (?i)\b(malt extract|glycerol-asparagine|inorganic salts-starch)\s+agar\b"
confidence: 0.95
```
**Why wrong:**
- ISP medium #4
- Minimal defined medium
- Multiple inorganic salts + starch

---

#### Category 4: Blood/Selective Media (1 record)

##### 14. Columbia blood agar base
```yaml
name: "Columbia blood agar base"
CHEBI: "CHEBI:2509"
detection: "Medium pattern match: (?i)\b(blood|chocolate)\s+agar\b"
confidence: 0.95
```
**Why wrong:**
- Base medium for blood agar
- Contains peptones, cornstarch, NaCl
- Used with added sheep blood
- Selective/differential medium

---

#### Category 5: Enrichment Media (1 record)

##### 15. Legionella agar enrichment
```yaml
name: "Legionella agar enrichment"
CHEBI: "CHEBI:2509"
detection: "Medium pattern match: (?i)\blegionella\s+agar\s+enrichment\b"
confidence: 0.95
```
**Why wrong:**
- For Legionella enrichment
- Contains selective agents
- Enrichment formulation ≠ pure agar

---

#### Category 6: Complex/Clinical Media (3 records)

##### 16. Mueller Hinton II agar
```yaml
name: "Mueller Hinton II agar"
CHEBI: "CHEBI:2509"
detection: "CHEBI:2509 (agar) with additional terms: ['mueller', 'hinton', 'ii']"
confidence: 0.95
```
**Why wrong:**
- For antibiotic susceptibility testing
- Standardized composition (beef extract, casein hydrolysate, starch)
- CLSI reference medium
- Not equivalent to pure agar

---

##### 17. Fastidious Anaerobe Agar
```yaml
name: "Fastidious Anaerobe Agar"
CHEBI: "CHEBI:2509"
detection: "Known medium name: Fastidious Anaerobe Agar"
confidence: 0.95
```
**Why wrong:**
- For fastidious anaerobes
- Contains hemin, vitamin K1
- Enriched formulation

---

##### 18. Czapek Dox agar
```yaml
name: "Czapek Dox agar"
CHEBI: "CHEBI:2509"
detection: "Known medium name: Czapek Dox agar"
confidence: 0.95
```
**Why wrong:**
- For fungi culture
- Defined minimal medium
- Contains: NaNO3, K2HPO4, MgSO4, KCl, FeSO4, sucrose, agar

---

#### Category 7: Code-Designated Media (2 records)

##### 19. BL Agar
```yaml
name: "BL Agar"
CHEBI: "CHEBI:2509"
detection: "CHEBI:2509 (agar) with additional terms: ['bl']"
confidence: 0.95
```
**Why wrong:**
- "BL" indicates specific medium code
- Not pure agar

---

##### 20. R agar
```yaml
name: "R agar"
CHEBI: "CHEBI:2509"
detection: "CHEBI:2509 (agar) with additional terms: ['r']"
confidence: 0.95
```
**Why wrong:**
- "R" indicates specific medium type
- Not pure agar

---

## Impact Analysis

### Data Corruption

**Before merge:**
- 21 distinct records
- 1 pure ingredient (agar)
- 20 complex media formulations

**After merge:**
- 1 record labeled "Agar"
- 20 distinct media formulations now inaccessible
- Loss of semantic meaning

### Query Impact

**User searches for "R2A agar":**
- Before: Finds specific formulation ✓
- After: Redirected to generic "Agar" ✗
- Lost context: 10+ ingredient recipe

**User searches for "Marine agar 2216":**
- Before: Finds ATCC 2216 formulation ✓
- After: Redirected to generic "Agar" ✗
- Lost context: Seawater-based medium

### Knowledge Graph Impact

**Relationships lost:**
- medium → contains → multiple ingredients
- medium → used_for → specific organism types
- medium → source → ATCC catalog

**Only relationship preserved:**
- all media → contains → agar (already implicit)

---

## Root Cause Analysis

### Primary Cause: CHEBI ID-Only Matching

The merge logic assumed:
```
Same CHEBI ID → Same entity → Safe to merge
```

**Flaw:** This is true for pure chemicals but FALSE for complex media.

### Why CHEBI Assigns Same ID

CHEBI:2509 represents the **chemical agar**, not the media formulations. The media contain agar but are not agar.

**Analogy:**
- ✓ "Water" + "H2O" → Same CHEBI → Safe merge
- ✗ "Water" + "Seawater" → Both contain H2O → NOT safe merge

### Missing Validation

The merge needed to check:
1. ✓ Same CHEBI ID
2. ✗ No complex media detection (NOT IMPLEMENTED)
3. ✗ Same ingredient_type (NOT CHECKED)
4. ✗ Pattern verification (NOT IMPLEMENTED)

---

## Prevention Strategies

### Strategy 1: Complex Media Detection

**Implement:**
```python
from identify_complex_media import detect_complex_medium

is_complex, confidence, reason = detect_complex_medium(name, chebi_id)
if is_complex and confidence >= 0.75:
    block_merge()
```

**This would have prevented:** All 20 bad merges

---

### Strategy 2: ingredient_type Field

**Implement:**
```python
if target_type == "SINGLE_INGREDIENT" and source_type == "DEFINED_MEDIUM":
    block_merge()
```

**This would have prevented:** All 20 bad merges (if types were set)

---

### Strategy 3: Pattern-Based Warnings

**Implement:**
```python
# Warning if name contains medium indicators
medium_indicators = ["agar base", "medium", "broth"]
if any(ind in name.lower() for ind in medium_indicators):
    flag_for_review()
```

**This would have flagged:** ~15 of 20 for manual review

---

### Strategy 4: Occurrence-Based Review

**Implement:**
```python
# Flag if merging high-occurrence records
if target_occurrences > 100 or source_occurrences > 100:
    require_manual_approval()
```

**This would have flagged:** High-use media like Marine agar 2216

---

## Lessons Learned

### Lesson 1: Shared ID ≠ Same Entity

**Insight:** Two records can share an ontology ID because:
- They are the same entity (merge OK)
- One contains the other (merge NOT OK)
- They share a component (merge NOT OK)

**Action:** Always verify semantic equivalence

---

### Lesson 2: Single Bad Cluster = Large Impact

**Insight:**
- Only 1 of 211 clusters was bad (0.5%)
- But contained 21 records (4.2% of merged data)
- High-connectivity clusters amplify errors

**Action:** Extra scrutiny for large merge clusters

---

### Lesson 3: Domain Knowledge Matters

**Insight:**
- "Marine agar 2216" is well-known to microbiologists
- "R2A agar" is standard low-nutrient medium
- Algorithm didn't recognize these

**Action:** Incorporate domain knowledge via:
- Known medium name lists
- Pattern matching (ATCC codes, medium numbers)
- Expert review for ambiguous cases

---

## Recommendations

### Immediate Actions

1. **Implement complex media detection** in `should_auto_merge()`
2. **Add ingredient_type checking** to merge validation
3. **Create known medium name list** for detection
4. **Flag large merges** (5+ records) for review

### Long-Term Actions

1. **Build medium hierarchy** (medium → ingredients relationship)
2. **Separate ingredient vs medium records** (different record types)
3. **Create medium formulation records** (recipe storage)
4. **Link media to CultureMech** (cross-reference)

---

## Validation Checklist

Before any merge, verify:

- [ ] Same CHEBI ID ✓
- [ ] No complex media detected (conf < 0.75) ✗ FAILED
- [ ] Same ingredient_type ✗ NOT CHECKED
- [ ] Clear pattern match ✗ FAILED
- [ ] < 5 records in cluster OR manual review ✗ FAILED (21 records!)

**Result:** This merge should have been blocked or flagged for review

---

## Testing

Use these 20 examples as **negative test cases**:

```python
def test_agar_complex_media_should_not_merge():
    """Verify complex media are not merged into pure agar."""
    complex_media = [
        "R2A agar",
        "Marine agar 2216",
        "Oatmeal agar",
        # ... all 20
    ]

    for medium_name in complex_media:
        is_complex, conf, _ = detect_complex_medium(medium_name, "CHEBI:2509")
        assert is_complex and conf >= 0.75, f"{medium_name} should be detected as complex media"

        should_merge, _ = deduplicator.should_auto_merge(
            target="Agar",
            source=medium_name
        )
        assert not should_merge, f"{medium_name} should NOT merge with Agar"
```

---

**Status:** CRITICAL - Must prevent recurrence
**Last Updated:** 2026-03-14
**Source:** `analysis/merge_pattern_analysis.yaml`
