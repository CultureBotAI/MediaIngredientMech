# MediaIngredientMech Merge Curation Guide

**Version:** 1.0
**Date:** 2026-03-14
**Purpose:** Guidelines for safely merging ingredient records

---

## Table of Contents

1. [Overview](#overview)
2. [When to Merge (Safe Patterns)](#when-to-merge-safe-patterns)
3. [When NOT to Merge (Dangerous Patterns)](#when-not-to-merge-dangerous-patterns)
4. [Merge Decision Workflow](#merge-decision-workflow)
5. [Pre-Merge Validation Checklist](#pre-merge-validation-checklist)
6. [Post-Merge Validation](#post-merge-validation)
7. [Historical Incident: Complex Media Conflation](#historical-incident-complex-media-conflation)

---

## Overview

Merging ingredient records consolidates duplicate or variant entries into a single canonical record. This improves data quality by:
- Reducing redundancy
- Combining occurrence statistics
- Unifying synonyms
- Simplifying queries

**However**, incorrect merges can corrupt data by:
- Conflating distinct entities (e.g., complex media with pure chemicals)
- Losing semantic distinctions (e.g., stereoisomers)
- Breaking downstream analyses

This guide states the current decision rules. A March 2026 automated-merge
snapshot is retained in `../ATTIC/` only as non-authoritative history; its
water and hydrate judgments conflict with the current identity contract.

---

## When to Merge (Safe Patterns)

### ✅ Pattern 1: Case Variations

**Rule:** Same name, different capitalization only

**Confidence:** 100% safe

**Examples:**
- `Folic acid` ⬅ `folic acid`, `Folic Acid`
- `Resazurin` ⬅ `resazurin`
- `Ethanol` ⬅ `ethanol`

**Detection:**
```python
normalized = [name.lower().strip() for name in all_names]
if len(set(normalized)) == 1:
    return "SAFE: case_variation"
```

**Action:** Auto-merge ✓

---

### ✅ Pattern 2: Chemical Synonyms

**Rule:** Different names for the same chemical entity (verified by CHEBI ID)

**Confidence:** 90% safe (requires verification)

**Examples:**
- `NaCl` ⬅ `sodium chloride`, `NaCL`, `Sodium Chloride`, `Sodium chloride`
- `KH2PO4` ⬅ `Monopotassium phosphate`, `Potassium Phosphate`
- `H3BO3` ⬅ `Boric Acid`, `Boric acid`

**Verification Required:**
1. ✓ Same CHEBI ID
2. ✓ Names share chemical formula, abbreviation, or systematic name
3. ✓ No complex media detected
4. ✓ Same ingredient_type (if set)

**Detection:**
- Formula variants (one has digits)
- Abbreviations (one much shorter)
- Shared chemical words (phosphate, chloride, etc.)

**Action:** Auto-merge with verification ✓

---

### ✅ Pattern 3: Abbreviations

**Rule:** Full name and abbreviated form

**Confidence:** 95% safe

**Examples:**
- `NaCl` ⬅ `sodium chloride`
- `KH2PO4` ⬅ `potassium dihydrogen phosphate`

**Verification Required:**
1. ✓ Shorter name is recognized abbreviation
2. ✓ Same CHEBI ID
3. ✓ No semantic difference

**Action:** Merge only after identity verification ✓

---

## When NOT to Merge (Dangerous Patterns)

### ❌ Pattern 1: Complex Media with Ingredients

**Rule:** NEVER merge multi-component formulations with their constituent ingredients

**Confidence:** 100% unsafe

**Critical Example from Real Data:**
```
❌ BAD MERGE: "Agar" (CHEBI:2509) ⬅ 21 complex media:
   - BL Agar
   - Brewer anaerobic agar
   - Mueller Hinton II agar
   - R2A agar
   - Marine agar 2216
   - Oatmeal agar
   - Corn meal agar
   - Columbia blood agar base
   ... and 13 more
```

**Why This Is Wrong:**
- "R2A agar" is a complex defined medium with 10+ ingredients
- "Agar" is just the solidifying agent
- Merging loses the recipe composition
- User searching for "R2A agar" won't find it

**Detection:**
```python
from identify_complex_media import detect_complex_medium

is_complex, confidence, reason = detect_complex_medium(name, chebi_id)
if is_complex and confidence >= 0.75:
    return "UNSAFE: complex_media"
```

**Patterns Detected:**
- Known medium names (Marine agar 2216, GAM agar)
- Medium codes (R2A, 7H10, BL)
- CHEBI for base ingredient + additional terms (e.g., "Mueller Hinton II" + agar)

**Action:** Block merge ✗

---

### ❌ Pattern 2: Different ingredient_type

**Rule:** Never merge across ingredient type categories

**Confidence:** 100% unsafe

**Examples:**
```
❌ NAMED_MEDIUM ≠ SINGLE_INGREDIENT
❌ UNDEFINED_MIXTURE ≠ SINGLE_INGREDIENT
```

**Why This Is Wrong:**
- Different types indicate different semantic categories
- Type distinctions are intentional classifications

**Detection:**
```python
types = [r.get("ingredient_type") for r in all_records if r.get("ingredient_type")]
if len(set(types)) > 1:
    return "UNSAFE: inconsistent_types"
```

**Action:** Block merge ✗

---

### ❌ Pattern 3: Stereoisomers and Variants

**Rule:** Related but chemically distinct entities must remain separate records

**Confidence:** 100% unsafe once distinct stereochemistry or material grade is
confirmed; name-based detection still requires review

**Examples:**
```
❌ D-biotin ≠ L-biotin (different stereoisomers)
❌ D-glucose ≠ L-glucose (different stereoisomers)
❌ Tap water ≠ Distilled water ≠ Double distilled water
```

**Why This Is Wrong:**
- Stereoisomers have different biological properties
- Water purity levels affect media composition
- Merging loses important semantic distinctions

**Better Approach:** Preserve each distinct identity and ground it at the most
specific supported ontology or registry level. MIM does not currently encode a
local relationship among these records; see `HIERARCHY_GUIDE.md`.

**Detection:**
- D/L prefixes (stereochemistry)
- Purity qualifiers (distilled, double distilled, ultrapure)
- Variant-indicating terms

**Action:** Block the merge and review identity/grounding ⚠️

---

### ⚠️ Pattern 4: Hydrate Variants

**Rule:** Different hydration states are distinct substances; do not merge them

**Confidence:** 100% unsafe when the hydration states differ; expert review may
still be needed to interpret an ambiguous label

**Examples from Real Data:**
```
⚠️ REVIEW: CaCl2 x 2 H2O ⬅ Calcium chloride dihydrate, CaCl2·2H2O
⚠️ REVIEW: MgSO4 ⬅ MgSO4·7H2O
```

**Why This Needs Review:**
- Different hydration states have different molecular weights
- May affect media preparation calculations
- Some recipes specify exact hydrate form

**Detection:**
```python
hydrate_keywords = ["hydrate", "·", "•", "H2O", "anhydrous"]
if any(kw in name for kw in hydrate_keywords):
    return "NEEDS_REVIEW: hydrate_variant"
```

**Action:** Flag for expert review ⚠️

---

## Merge Decision Workflow

```
┌─────────────────────────────────┐
│ Are both records from same      │
│ ontology source (CHEBI ID)?     │
└────────────┬────────────────────┘
             │ NO → STOP (don't merge)
             ▼ YES
┌─────────────────────────────────┐
│ Do they have same                │
│ ingredient_type (if set)?       │
└────────────┬────────────────────┘
             │ NO → STOP (don't merge)
             ▼ YES
┌─────────────────────────────────┐
│ Run detect_complex_medium()     │
│ on both records                 │
└────────────┬────────────────────┘
             │
             ▼
┌─────────────────────────────────┐
│ Is either complex media         │
│ (confidence >= 0.75)?           │
└────────────┬────────────────────┘
             │ YES → STOP (don't merge)
             ▼ NO
┌─────────────────────────────────┐
│ Check name patterns:            │
│ - Case variation?      → MERGE  │
│ - Chemical synonym?    → MERGE  │
│ - Abbreviation?        → MERGE  │
│ - Hydrate variant?     → REVIEW │
│ - Stereoisomer?        → REVIEW │
│ - Unclear?             → REVIEW │
└─────────────────────────────────┘
```

---

## Pre-Merge Validation Checklist

Before executing any merge operation, verify:

- [ ] **Same CHEBI ID** - Both records reference the same ontology term
- [ ] **Same ingredient_type** - Or both have no type set
- [ ] **Not NAMED_MEDIUM** - Neither is a defined medium
- [ ] **Not complex media** - `detect_complex_medium()` returns False or low confidence
- [ ] **Clear pattern match** - Names fit case/synonym/abbreviation pattern
- [ ] **No expert flag** - Neither has NEEDS_EXPERT status
- [ ] **Merge reason documented** - Clear explanation in curation history

**If ALL checkboxes pass:** Safe to merge ✓
**If ANY checkbox fails:** Do NOT merge ✗

---

## Post-Merge Validation

After executing merge operations:

### 1. Run Integrity Validation
```bash
PYTHONPATH=src python scripts/validate_merge_integrity.py
```

**Expected output:**
```
✓ All representative records exist
✓ All merged records have valid representative
✓ No circular references
✓ Merge integrity PASSED
```

### 2. Verify Representative Selection
- Does the representative record make sense?
- Is it the most common/standard name?
- Are occurrence statistics combined correctly?

### 3. Check Synonym Preservation
- Were all synonyms from merged records preserved?
- No synonym loss during merge?

### 4. Audit Trail Complete
- Merge event in curation_history?
- Timestamp and reason documented?

---

## Historical Incident: Complex Media Conflation

The retired March 2026 pattern-analysis snapshot exposed one useful failure
mode, but its cluster counts and good/bad labels are stale and are not current
merge evidence. The original catalogs live in `../ATTIC/` for provenance.

### Agar cluster

**Representative:** `Agar` (CHEBI:2509)

**Correctly merged:**
- agar (case variation) ✓

**Incorrectly merged (20 complex media):**
- ❌ R2A agar (defined medium, 10+ ingredients)
- ❌ Marine agar 2216 (ATCC medium)
- ❌ Oatmeal agar (cereal + agar formulation)
- ❌ Mueller Hinton II agar (clinical medium)
- ❌ Middlebrook 7H10 agar (TB culture medium)
- ... and 15 more

**Impact:** 95% of this cluster was incorrect, affecting 20 records

**Root Cause:** CHEBI-only matching without complex media detection

**Prevention:** Implement pre-merge validation from this guide

---

## Implementation Notes

### For CHEBIDeduplicator

Update `should_auto_merge()` method in `src/mediaingredientmech/curation/chebi_deduplicator.py`:

```python
def should_auto_merge(self, target_idx: int, source_idx: int) -> tuple[bool, str]:
    """Enhanced with safety checks."""
    target = self.records[target_idx]
    source = self.records[source_idx]

    # Existing CHEBI ID and quality checks...

    # NEW: Check ingredient_type compatibility
    target_type = target.get("ingredient_type")
    source_type = source.get("ingredient_type")

    if target_type and source_type and target_type != source_type:
        return False, f"Different ingredient types: {target_type} vs {source_type}"

    # NEW: Check for complex media
    from identify_complex_media import detect_complex_medium

    target_name = target.get("preferred_term")
    source_name = source.get("preferred_term")
    target_chebi = target.get("ontology_mapping", {}).get("ontology_id", "")
    source_chebi = source.get("ontology_mapping", {}).get("ontology_id", "")

    is_target_complex, conf_t, reason_t = detect_complex_medium(target_name, target_chebi)
    is_source_complex, conf_s, reason_s = detect_complex_medium(source_name, source_chebi)

    if is_target_complex and conf_t >= 0.75:
        return False, f"Target is complex media: {reason_t}"
    if is_source_complex and conf_s >= 0.75:
        return False, f"Source is complex media: {reason_s}"

    # Rest of existing logic...
```

### For Interactive Curation

When manually reviewing merge suggestions:
1. Display this checklist
2. Show complex media detection results
3. Highlight pattern classification
4. Allow curator override with mandatory reason

---

## References

- **Complex Media Detection:** `scripts/identify_complex_media.py`
- **Merge Validation:** `scripts/validate_merge_integrity.py`
- **Retired implementation plan:** `../ATTIC/MERGE_TRACKING_IMPLEMENTATION.md`

---

**Document Status:** Active
**Review Frequency:** After each major merge operation
**Maintainer:** MediaIngredientMech curation team
