# Water Variant Curation Guide

**Version:** 1.0
**Date:** 2026-03-14
**Purpose:** Decision rules for curating water purity variants
**Scope:** All H₂O-related ingredients (plain water, distilled, tap, demineralized, etc.)

---

## Table of Contents

1. [Overview](#overview)
2. [Water Variants in Dataset](#water-variants-in-dataset)
3. [Purity Hierarchy](#purity-hierarchy)
4. [Merge Decision Rules](#merge-decision-rules)
5. [Type-Specific Guidelines](#type-specific-guidelines)
6. [Integration with Purity Detection](#integration-with-purity-detection)
7. [Real Data Examples](#real-data-examples)
8. [Preparing for Hierarchy Implementation](#preparing-for-hierarchy-implementation)

---

## Overview

Water is the most common media ingredient (4000+ occurrences) but appears in multiple purity variants with **different biological effects**:

- **Tap water** contains minerals, chlorine → affects sensitive organisms
- **Distilled water** is purified → standard laboratory reagent
- **Double distilled water** is ultra-pure → for trace-metal sensitive work
- **Demineralized water** has minerals removed → similar to distilled but different process

**Key principle:** Different purity levels = different ingredients (keep separate, do NOT merge)

**Why this matters:**
- Halophiles require specific trace minerals (Mg²⁺, Ca²⁺, K⁺)
- Chlorine in tap water inhibits many bacteria
- Trace metal contamination affects metal-sensitive organisms
- Reproducibility requires consistent purity levels

---

## Water Variants in Dataset

### Current Inventory (215 total water-related ingredients)

**Pure Water Variants (12 ingredients):**
- Distilled water (MAPPED, 4018 occurrences)
- Double distilled water (MAPPED, 46 occurrences)
- Demineralized water (UNMAPPED, 2 variants)
- Tap water (UNMAPPED, 2 variants)
- Plain "water", "H2O", "Water" (case variants)
- Sterile variants: "sterile dH2O", "Sterile dH2O"

**Hydrate Compounds (203 ingredients):**
- Chemical salts with water of crystallization
- Examples: CaCl₂·2H₂O, MgSO₄·7H₂O, NiCl₂·6H₂O
- **Note:** These are NOT water variants, they are hydrated salts
- Keep separate from water curation (different chemical entities)

---

## Purity Hierarchy

Water variants form a **purity gradient** from impure → ultrapure:

```
┌─────────────────────────────────────────────────────┐
│ PURITY GRADIENT (Increasing purity →)              │
└─────────────────────────────────────────────────────┘

1. TAP WATER (Most impure)
   - Contains: Cl₂, minerals (Ca, Mg), variable composition
   - Purity: Variable (city-dependent)
   - Use cases: Non-critical washing, routine media

2. DEMINERALIZED WATER
   - Contains: Low minerals, may have organics
   - Purity: ~1-10 µS/cm conductivity
   - Process: Ion exchange
   - Use cases: General laboratory use

3. DISTILLED WATER (Standard)
   - Contains: Minimal impurities
   - Purity: <1 µS/cm conductivity
   - Process: Single distillation
   - Use cases: Standard media preparation
   - **CURRENT BASELINE**: CHEBI:15377, 4018 occurrences

4. DOUBLE DISTILLED WATER (High purity)
   - Contains: Trace-level impurities only
   - Purity: <0.1 µS/cm conductivity
   - Process: Double distillation
   - Use cases: Trace-metal sensitive work, spectroscopy
   - **CURRENT DATA**: 46 occurrences

5. ULTRAPURE WATER (Highest purity)
   - Contains: Near-zero impurities
   - Purity: 0.055 µS/cm (18.2 MΩ·cm)
   - Process: RO + EDI + UV + filtration
   - Examples: Milli-Q, HPLC-grade
   - **CURRENT DATA**: Not found in dataset
```

---

## Merge Decision Rules

### ✅ SAFE TO MERGE (Same purity level)

**Rule:** Merge if **exact same purity level** + only case/synonym differences

**Examples:**

```yaml
# Case variations → MERGE
"Distilled water" ← "distilled water" ← "Distilled Water"
"Tap water" ← "tap water"
"Water" ← "water"

# Synonym variations → MERGE
"Distilled water" ← "dH2O" (standard abbreviation)
"Double distilled water" ← "ddH2O" (standard abbreviation)

# Sterile variants → MERGE (if same purity)
"Distilled water" ← "sterile dH2O" (sterility is preparation detail, not purity)
```

**Detection:**
```python
normalized = [name.lower().strip() for name in all_names]
if len(set(normalized)) == 1:
    return "SAFE: case_variation"
```

---

### ❌ NEVER MERGE (Different purity levels)

**Rule:** **Never merge** different purity levels, even if same CHEBI ID

**Examples:**

```yaml
# Different purity → DO NOT MERGE
❌ Tap water ≠ Distilled water
   - Tap: Cl₂ + minerals, variable
   - Distilled: purified, standardized

❌ Distilled water ≠ Double distilled water
   - Distilled: <1 µS/cm
   - Double distilled: <0.1 µS/cm (10x purer)

❌ Demineralized water ≠ Distilled water
   - Demineralized: ion exchange process
   - Distilled: thermal process
   - Different trace contaminant profiles
```

**Why wrong:**
- Different biological effects (chlorine inhibition, mineral requirements)
- Different trace metal content (critical for metal-sensitive organisms)
- Different reproducibility guarantees
- Merging loses critical media composition information

**Prevention:**
```python
from mediaingredientmech.utils.purity_detector import detect_purity_concerns

target_concern, target_conf, _ = detect_purity_concerns(target)
source_concern, source_conf, _ = detect_purity_concerns(source)

# Block if purity mismatch
if target_concern != source_concern:
    return False, "Purity mismatch: different water purity levels"
```

---

### ⚠️ REVIEW CAREFULLY (Sterile variants)

**Rule:** Sterility is a **preparation detail**, not a purity level

**Decision:**
- If sterile + same purity → **MERGE** (sterility doesn't change chemical composition)
- If sterile + different purity → **DO NOT MERGE** (purity takes precedence)

**Examples:**

```yaml
# Sterile + same purity → MERGE
✓ "Distilled water" ← "sterile dH2O"
  - Both are distilled water
  - Sterility is autoclave/filtration step (doesn't change H₂O purity)

# Sterile + different purity → DO NOT MERGE
❌ "Sterile dH2O" ≠ "Sterile tap water"
  - Different purity levels (distilled vs tap)
  - Sterility doesn't override purity difference
```

**Curation note:**
- Document sterility in `notes` field: "Autoclaved before use"
- Do NOT create separate records for sterile variants if purity is same
- Sterility is a **procedure**, not an ingredient property

---

### ⚠️ SPECIAL CASE: Demineralized Water

**Status:** Needs verification before merging

**Current data:**
- 2 demineralized water variants (case variations)
- NOT currently mapped to CHEBI:15377

**Decision matrix:**

| Scenario | Action | Rationale |
|----------|--------|-----------|
| Demineralized used as synonym for distilled | **MERGE** with distilled | If authors use interchangeably |
| Demineralized is distinct process | **KEEP SEPARATE** | Different trace contaminant profile |
| Unclear from context | **MARK AS NEEDS_EXPERT** | Requires domain knowledge |

**Recommended approach:**
1. Check source papers: How is "demineralized" used?
2. If used interchangeably with "distilled" → merge
3. If explicitly distinguished from "distilled" → keep separate
4. If unclear → mark `NEEDS_EXPERT` with note: "Verify if demineralized = distilled in this dataset"

**Technical distinction:**
- **Demineralized:** Ion exchange (removes ionic contaminants)
- **Distilled:** Thermal distillation (removes all volatiles + non-volatiles)
- **Practical difference:** Distilled may have lower organic content
- **Microbiology practice:** Often used interchangeably

---

## Type-Specific Guidelines

### 1. Plain "Water" / "H₂O"

**Variants found:**
- "Water" (capitalized)
- "water" (lowercase)
- "H2O" (various capitalizations)

**Rule:** Merge case variations **only**

**Mapping:**
- Map to CHEBI:15377 (water)
- Quality: `EXACT_MATCH`
- Confidence: 1.0

**Issue:** Unspecified purity level

**Curation notes:**
```yaml
mapping_quality: EXACT_MATCH
evidence:
  - notes: |
      Plain "water" without purity qualifier.
      Assumed to be distilled water (laboratory standard).
      If context suggests tap water, flag for review.
```

**Action:**
- Default assumption: **distilled water** (laboratory standard)
- If source explicitly mentions "tap", "from faucet", etc. → create separate "Tap water" record
- Document assumption in evidence notes

---

### 2. Distilled Water / dH₂O

**Variants found (8 total):**
- "Distilled water" (4018 occurrences) ← PRIMARY
- "distilled water" (lowercase)
- "dH2O" (abbreviation)
- "Distilled Water" (capitalized)
- "sterile dH2O"
- "Sterile dH2O"

**Rule:** Merge all into "Distilled water" (most common form)

**Mapping:**
- Map to CHEBI:15377
- Quality: `EXACT_MATCH`
- Confidence: 1.0

**Merge target:** "Distilled water" (ID: MediaIngredientMech:000114)

**Evidence notes:**
```yaml
preferred_term: Distilled water
synonyms:
  - text: dH2O
    source: abbreviation
  - text: distilled water
    source: case_variation
  - text: sterile dH2O
    source: preparation_variant
mapping_quality: EXACT_MATCH
evidence:
  - notes: |
      Standard laboratory distilled water.
      Single distillation, <1 µS/cm conductivity.
      "Sterile" variants merged (sterility is preparation, not purity).
```

**Action:**
✓ Merge all 8 variants → single "Distilled water" record
✓ Preserve all synonyms
✓ Sum occurrence counts

---

### 3. Double Distilled Water / ddH₂O

**Variants found:**
- "Double distilled water" (46 occurrences)

**Rule:** Keep SEPARATE from "Distilled water"

**Mapping:**
- Map to CHEBI:15377 (same CHEBI as distilled, but different purity)
- Quality: `CLOSE_MATCH` ← **NOT EXACT_MATCH** (purity difference)
- Confidence: 0.85

**Why CLOSE_MATCH?**
- Double distilled is **more pure** than single distilled
- Different use cases (trace-metal sensitive work)
- Should NOT merge with standard distilled water
- Purity detection will flag this

**Evidence notes:**
```yaml
preferred_term: Double distilled water
synonyms:
  - text: ddH2O
    source: abbreviation
mapping_quality: CLOSE_MATCH  # NOT EXACT_MATCH
evidence:
  - confidence_score: 0.85
    notes: |
      Double distilled water (ddH2O) = two distillation cycles.
      Higher purity than standard distilled (<0.1 µS/cm vs <1 µS/cm).
      CLOSE_MATCH instead of EXACT_MATCH to prevent merging with
      single-distilled water. Used for trace-metal sensitive work.
```

**Purity detection:**
```python
has_concern, conf, reason = detect_purity_concerns(record)
# Returns: (False, 0.0, "No concerns") - double distilled is pure
# But comparison with "distilled water" will NOT flag mismatch
# (both are pure, just different purity levels)
```

**Future hierarchy:**
```yaml
Water (CHEBI:15377)
├── Tap water (impure)
├── Demineralized water
├── Distilled water (standard) ← BASE LEVEL
└── Double distilled water (higher purity) ← REFINED VARIANT
```

---

### 4. Tap Water

**Variants found (2):**
- "Tap water"
- "tap water"

**Rule:** Merge case variations, keep SEPARATE from all other water

**Mapping:**
- Map to CHEBI:15377 (water)
- Quality: `CLOSE_MATCH` ← **NOT EXACT_MATCH** (impure)
- Confidence: 0.70

**Why CLOSE_MATCH?**
- Contains chlorine, minerals, variable composition
- NOT pure water (impure variant)
- Purity detection will flag this as concern

**Evidence notes:**
```yaml
preferred_term: Tap water
synonyms:
  - text: tap water
    source: case_variation
mapping_quality: CLOSE_MATCH  # NOT EXACT_MATCH
evidence:
  - confidence_score: 0.70
    notes: |
      Tap water = municipal water supply.
      Contains chlorine (0.2-4 ppm), minerals (Ca, Mg), variable composition.
      NOT suitable for trace-metal work or chlorine-sensitive organisms.
      CLOSE_MATCH to prevent merging with distilled water.
      Use only for non-critical applications.
```

**Purity detection:**
```python
has_concern, conf, reason = detect_purity_concerns(record)
# Returns: (True, 0.85, "environmental source + CLOSE_MATCH")
# Will block merge with distilled water ✓
```

---

### 5. Demineralized Water

**Variants found (2):**
- "Demineralized water"
- "demineralized water"

**Rule:** Merge case variations, **REVIEW** before merging with distilled

**Current status:** UNMAPPED

**Recommended mapping:**
- Map to CHEBI:15377 (water)
- Quality: `CLOSE_MATCH` ← **Initially, until verified**
- Confidence: 0.75

**Evidence notes (draft):**
```yaml
preferred_term: Demineralized water
synonyms:
  - text: demineralized water
    source: case_variation
  - text: deionized water  # If verified equivalent
    source: process_synonym
mapping_quality: CLOSE_MATCH  # Until verified = distilled
mapping_status: NEEDS_EXPERT  # Requires domain review
evidence:
  - confidence_score: 0.75
    notes: |
      Demineralized water = ion exchange process.
      May be equivalent to distilled water in this dataset.
      NEEDS REVIEW: Check source papers to verify if used
      interchangeably with "distilled water".

      If equivalent → change to EXACT_MATCH and merge with distilled.
      If distinct → keep CLOSE_MATCH and separate.
```

**Action required:**
1. Search source papers for "demineralized" usage
2. If interchangeable with "distilled" → merge
3. If distinct → keep separate with CLOSE_MATCH
4. Document decision in curation_history

---

### 6. Seawater Variants

**Variants found:**
- "Seawater"
- "Enriched Seawater Medium"
- "Supplemented Seawater"
- "Soil+Seawater Medium"

**Rule:** These are **complex media**, NOT water variants

**Action:**
- Do NOT merge with water
- Map to ENVO ontology (environmental samples)
- Mark as `COMPLEX_MIXTURE` or `ENVIRONMENTAL`

**Rationale:**
- Seawater = complex mixture (salts, organics, variable composition)
- Not a purity variant of H₂O
- Different ingredient category entirely

---

## Integration with Purity Detection

The new `purity_detector.py` automatically identifies water purity variants:

### Detection Examples

**1. Tap water (detected as impure):**
```python
from mediaingredientmech.utils.purity_detector import detect_purity_concerns

record = {
    'preferred_term': 'Tap water',
    'ontology_mapping': {
        'mapping_quality': 'CLOSE_MATCH',
        'evidence': [{
            'notes': 'Contains chlorine, minerals, variable composition'
        }]
    }
}

has_concern, conf, reason = detect_purity_concerns(record)
# Returns: (True, 0.85, "environmental source + trace components")
```

**2. Distilled water (detected as pure):**
```python
record = {
    'preferred_term': 'Distilled water',
    'ontology_mapping': {
        'mapping_quality': 'EXACT_MATCH',
        'evidence': [{
            'notes': 'Purified H2O'
        }]
    }
}

has_concern, conf, reason = detect_purity_concerns(record)
# Returns: (False, 0.0, "No purity concerns detected")
```

**3. Merge blocking (tap + distilled):**
```python
from mediaingredientmech.curation.chebi_deduplicator import CHEBIDeduplicator

deduplicator = CHEBIDeduplicator(curator)

should_merge, reason = deduplicator.should_auto_merge(
    target_idx=tap_water_idx,
    source_idx=distilled_water_idx
)
# Returns: (False, "Purity mismatch: target has concerns (environmental source), source is pure")
```

### Curation Workflow Integration

When curating water variants, the purity detection system will:

1. ✅ **Allow** merging case/synonym variants (same purity)
   - "Distilled water" + "dH2O" → MERGE
   - "Tap water" + "tap water" → MERGE

2. ❌ **Block** merging different purity levels
   - "Tap water" + "Distilled water" → BLOCKED
   - "Distilled water" + "Double distilled water" → BLOCKED

3. ⚠️ **Flag** for review if uncertain
   - "Demineralized water" + "Distilled water" → FLAG (needs expert review)

---

## Real Data Examples

### Example 1: Distilled Water (MAPPED)

**Current state:**
```yaml
id: MediaIngredientMech:000114
identifier: CHEBI:15377
preferred_term: Distilled water
mapping_status: MAPPED
occurrence_statistics:
  total_occurrences: 4018
  distinct_sources: 150
ontology_mapping:
  ontology_id: CHEBI:15377
  ontology_label: water
  ontology_source: CHEBI
  mapping_quality: EXACT_MATCH
  evidence:
    - confidence_score: 1.0
      notes: Standard laboratory distilled water
```

**Proposed action:**
- ✓ Merge 7 other distilled water variants into this record
- ✓ Add synonyms: dH2O, sterile dH2O
- ✓ Keep EXACT_MATCH quality
- ✓ Update occurrence counts

---

### Example 2: Double Distilled Water (MAPPED)

**Current state:**
```yaml
preferred_term: Double distilled water
mapping_status: MAPPED
occurrence_statistics:
  total_occurrences: 46
  distinct_sources: 8
ontology_mapping:
  ontology_id: CHEBI:15377
  mapping_quality: EXACT_MATCH  # ← Should be CLOSE_MATCH
```

**Proposed changes:**
```yaml
# CHANGE quality to prevent merging with single distilled
mapping_quality: CLOSE_MATCH  # Changed from EXACT_MATCH
evidence:
  - confidence_score: 0.85
    notes: |
      Double distilled water (ddH2O) = higher purity than standard distilled.
      <0.1 µS/cm vs <1 µS/cm conductivity.
      Used for trace-metal sensitive work.
      CLOSE_MATCH prevents merging with single-distilled water.
```

**Rationale:**
- Prevents automatic merge with "Distilled water" (different purity)
- Preserves scientific distinction (10x purity difference)
- Enables future hierarchy (refined variant of distilled)

---

### Example 3: Tap Water (UNMAPPED)

**Current state:**
```yaml
preferred_term: Tap water
mapping_status: UNMAPPED
occurrence_statistics:
  total_occurrences: unknown
```

**Proposed mapping:**
```yaml
id: MediaIngredientMech:NEW_ID
identifier: CHEBI:15377
preferred_term: Tap water
mapping_status: MAPPED
synonyms:
  - text: tap water
    source: case_variation
occurrence_statistics:
  total_occurrences: TBD
  distinct_sources: TBD
ontology_mapping:
  ontology_id: CHEBI:15377
  ontology_label: water
  ontology_source: CHEBI
  mapping_quality: CLOSE_MATCH  # NOT EXACT_MATCH (impure)
  evidence:
    - confidence_score: 0.70
      notes: |
        Tap water = municipal water supply.
        Contains chlorine (0.2-4 ppm), minerals (Ca²⁺, Mg²⁺), variable composition.
        Lower confidence due to impurity - not pure H₂O.
        NOT suitable for trace-metal work or chlorine-sensitive organisms.
curation_history:
  - timestamp: 2026-03-14T12:00:00Z
    curator: claude_code
    action: accept_mapping
    notes: Mapped with CLOSE_MATCH to prevent merging with distilled water
```

---

## Hierarchy Implementation ✅

The water hierarchy system is now **fully implemented and active**:

### Implemented Hierarchy

```yaml
# PARENT: Water (base concept)
- id: MediaIngredientMech:PARENT_WATER
  identifier: CHEBI:15377
  preferred_term: Water (base)
  variant_type: BASE_CHEMICAL
  child_ingredients:
    - MediaIngredientMech:TAP_WATER
    - MediaIngredientMech:DEMIN_WATER
    - MediaIngredientMech:000114  # Distilled water
    - MediaIngredientMech:DOUBLE_DIST_WATER
  media_roles:
    - role: SOLVENT
      confidence: 1.0

# CHILD: Tap water (impure)
- id: MediaIngredientMech:TAP_WATER
  identifier: CHEBI:15377
  preferred_term: Tap water
  parent_ingredient: MediaIngredientMech:PARENT_WATER
  variant_type: TAP
  variant_notes: "Municipal water supply, contains chlorine and minerals"
  role_inheritance: true

# CHILD: Demineralized water
- id: MediaIngredientMech:DEMIN_WATER
  identifier: CHEBI:15377
  preferred_term: Demineralized water
  parent_ingredient: MediaIngredientMech:PARENT_WATER
  variant_type: DEMINERALIZED
  variant_notes: "Ion exchange process, low mineral content"
  role_inheritance: true

# CHILD: Distilled water (standard)
- id: MediaIngredientMech:000114
  identifier: CHEBI:15377
  preferred_term: Distilled water
  parent_ingredient: MediaIngredientMech:PARENT_WATER
  variant_type: PURIFIED
  variant_notes: "Single distillation, <1 µS/cm conductivity"
  role_inheritance: true

# CHILD: Double distilled water (higher purity)
- id: MediaIngredientMech:DOUBLE_DIST_WATER
  identifier: CHEBI:15377
  preferred_term: Double distilled water
  parent_ingredient: MediaIngredientMech:PARENT_WATER
  variant_type: ULTRA_PURIFIED
  variant_notes: "Double distillation, <0.1 µS/cm conductivity, trace-metal work"
  role_inheritance: true
```

### Using the Hierarchy

**Get all water variants:**
```python
from mediaingredientmech.utils.hierarchy_utils import get_all_variants

all_water = get_all_variants('MediaIngredientMech:001108', all_records)
# Returns: [Water (base), Tap water, Demineralized, Distilled, Double distilled]
```

**Navigate from child to parent:**
```python
from mediaingredientmech.utils.hierarchy_utils import get_parent

parent = get_parent('MediaIngredientMech:000114', all_records)
# Returns: Water (base) record
```

**Get siblings:**
```python
from mediaingredientmech.utils.hierarchy_utils import get_siblings

siblings = get_siblings('MediaIngredientMech:000114', all_records)
# Returns: [Tap water, Demineralized, Double distilled]
```

**Visualize tree:**
```python
from mediaingredientmech.utils.hierarchy_utils import get_hierarchy_tree_string

tree = get_hierarchy_tree_string('MediaIngredientMech:001108', all_records)
print(tree)
# Output:
# Water (base) [BASE_CHEMICAL]
# ├─ Tap water [TAP]
# ├─ Demineralized water [DEMINERALIZED]
# ├─ Distilled water [PURIFIED]
# └─ Double distilled water [ULTRA_PURIFIED]
```

### Hierarchy Benefits

1. **Query flexibility:**
   - "Find all media using any water" → query parent, get all variants
   - "Find media using tap water specifically" → query child directly

2. **Role inheritance:**
   - All water variants inherit SOLVENT role from parent
   - Can override with variant-specific roles

3. **Purity relationships:**
   - Explicit parent-child links preserve distinctions
   - Prevents inappropriate merging (purity detection still active)
   - Enables purity-based queries

4. **Scientific accuracy:**
   - Maintains all distinctions (no data loss)
   - Documents relationships (parent-child links)
   - Supports reproducibility (variant notes explain differences)

---

## Summary: Quick Decision Matrix

| Water Type | Merge with others? | CHEBI | Quality | Confidence | Action |
|------------|-------------------|-------|---------|------------|--------|
| **Plain "water"** | ✓ Case only | 15377 | EXACT_MATCH | 1.0 | Assume distilled |
| **Distilled water** | ✓ Case + dH2O | 15377 | EXACT_MATCH | 1.0 | Primary baseline |
| **Double distilled** | ❌ Keep separate | 15377 | CLOSE_MATCH | 0.85 | Higher purity |
| **Tap water** | ❌ Keep separate | 15377 | CLOSE_MATCH | 0.70 | Impure (Cl₂, minerals) |
| **Demineralized** | ⚠️ Review first | 15377 | CLOSE_MATCH | 0.75 | Verify = distilled? |
| **Sterile dH2O** | ✓ Merge w/ distilled | 15377 | EXACT_MATCH | 1.0 | Sterile = procedure |
| **Seawater** | ❌ Different category | ENVO | CLOSE_MATCH | varies | Complex mixture |

---

## Next Steps

### Immediate Actions (Manual Curation)

1. **Merge distilled water variants** (8 variants → 1)
   - Target: "Distilled water" (MediaIngredientMech:000114)
   - Merge: case variations, dH2O, sterile variants
   - Sum occurrences, preserve synonyms

2. **Map tap water** (UNMAPPED → MAPPED)
   - Use CLOSE_MATCH quality
   - Document impurity (chlorine, minerals)
   - Block merge with distilled via purity detection

3. **Review demineralized water**
   - Check source papers for usage context
   - Decide: merge with distilled OR keep separate
   - Document decision rationale

4. **Downgrade double distilled quality**
   - Change: EXACT_MATCH → CLOSE_MATCH
   - Reason: Prevent merge with single distilled
   - Document higher purity level

### Future Enhancements (Automated)

1. **Implement hierarchy system** (Option A)
   - Add parent_ingredient, child_ingredients fields
   - Create water hierarchy (base → variants)
   - Enable role inheritance

2. **Create water curation script** (Option B)
   - Interactive tool for water variant review
   - Auto-suggest merge/separate decisions
   - Apply purity detection automatically

3. **Expand to other purity hierarchies**
   - Glucose variants (D/L, α/β)
   - Salt purity grades (reagent/technical/analytical)
   - Peptone grades (crude/purified)

---

## References

- **Purity Detection:** `src/mediaingredientmech/utils/purity_detector.py`
- **Merge Validation:** `src/mediaingredientmech/curation/chebi_deduplicator.py`
- **Merge Guide:** `docs/MERGE_CURATION_GUIDE.md`
- **Hierarchy Plan:** `HIERARCHY_IMPLEMENTATION_PLAN.md`
- **Data:** `data/curated/mapped_ingredients.yaml`, `data/curated/unmapped_ingredients.yaml`

---

**Last Updated:** 2026-03-14
**Status:** Ready for implementation
**Next:** Execute immediate actions, then implement hierarchy system
