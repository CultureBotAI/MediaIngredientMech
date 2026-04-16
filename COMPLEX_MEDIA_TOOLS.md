# Complex Media Identification & Management - Complete ✅

## Problem Identified

**Issue**: Many entries mapped to single chemical CHEBI terms are actually **complex defined media** (complete recipes), not single ingredients.

**Example**:
- "Oatmeal agar" → Contains oatmeal + agar + other nutrients (complete medium recipe)
- "R2A agar" → Defined medium with ~10 ingredients
- "Marine agar 2216" → ATCC medium formulation

All were incorrectly:
1. Mapped to CHEBI:2509 (pure agar)
2. Merged together with pure "Agar"

## Solution Implemented (4 Steps)

### ✅ Step 1: Schema Extensions

**File**: `src/mediaingredientmech/schema/mediaingredientmech.yaml`

Added two new fields to `IngredientRecord`:

```yaml
ingredient_type:
  range: IngredientTypeEnum
  description: Classification of entry type
  # Values: SINGLE_INGREDIENT, DEFINED_MEDIUM, UNDEFINED_MIXTURE, STOCK_SOLUTION

culturemech_medium_name:
  description: Cross-reference to CultureMech medium name for defined media
```

**IngredientTypeEnum** values:
- **SINGLE_INGREDIENT**: Pure chemical (NaCl, agar, glucose)
- **DEFINED_MEDIUM**: Complete recipe (R2A agar, LB broth, Marine agar 2216)
- **UNDEFINED_MIXTURE**: Unknown composition (yeast extract, peptone)
- **STOCK_SOLUTION**: Pre-mixed defined ingredients (vitamin B12 solution)

---

### ✅ Step 2: Detection & Reclassification Script

**File**: `scripts/identify_complex_media.py`

**Features**:
- **Pattern-based detection**: Identifies complex media using:
  - Medium name patterns (e.g., "X agar", "X broth")
  - Known media names (R2A, LB, Marine agar 2216, etc.)
  - CHEBI:2509 entries with additional terms
- **Confidence scoring**: High (≥0.85), Medium (0.70-0.85), Low
- **Three modes**:
  - `--report-only`: Generate report without changes
  - `--interactive`: Review and approve each reclassification
  - `--auto-reclassify`: Automatically reclassify high-confidence entries

**Usage**:
```bash
# Preview detection
python scripts/identify_complex_media.py --report-only

# Interactive review
python scripts/identify_complex_media.py --interactive

# Auto-reclassify (dry run first!)
python scripts/identify_complex_media.py --auto-reclassify --dry-run
python scripts/identify_complex_media.py --auto-reclassify
```

**Detection Patterns**:
- Agar-based media: "Marine agar", "R2A agar", "Corn meal agar"
- Broth-based media: "LB broth", "Mueller Hinton broth"
- Named media with codes: "Marine agar 2216", "Middlebrook 7H10"
- Base/powder indicators: "agar base", "broth powder"

---

### ✅ Step 3: CultureMech Cross-Reference Tool

**File**: `scripts/cross_reference_culturemech.py`

**Features**:
- **Search CultureMech media database** for matching recipes
- **Match types**: Exact, contains, fuzzy (token overlap)
- **Display ingredient lists** from CultureMech recipes
- **Auto-link**: Update `culturemech_medium_name` field

**Usage**:
```bash
# Search for specific ingredient
python scripts/cross_reference_culturemech.py --ingredient "R2A agar" --show-details

# Cross-reference all complex media
python scripts/cross_reference_culturemech.py --complex-media-only

# Update links (dry run first!)
python scripts/cross_reference_culturemech.py --update-links --dry-run
python scripts/cross_reference_culturemech.py --update-links
```

**Output Example**:
```
┌─────────────────────────┬──────────────────────┬──────────┬─────────────┐
│ MediaIngredientMech     │ CultureMech Medium   │ Match    │ Ingredients │
├─────────────────────────┼──────────────────────┼──────────┼─────────────┤
│ R2A agar                │ R2A Agar             │ exact    │ 10          │
│ Marine agar 2216        │ Marine Agar 2216     │ exact    │ 8           │
│ Oatmeal agar            │ Oatmeal Agar (ISP 3) │ contains │ 5           │
└─────────────────────────┴──────────────────────┴──────────┴─────────────┘
```

---

### ✅ Step 4: Comprehensive Analysis Report

**File**: `scripts/generate_complex_media_report.py`

**Features**:
- **Full analysis** of all ingredients
- **Grouped by CHEBI ID** for easy review
- **Markdown or YAML** output formats
- **Includes recommendations** and action items

**Usage**:
```bash
# Generate Markdown report
python scripts/generate_complex_media_report.py

# Generate YAML report
python scripts/generate_complex_media_report.py --output-format yaml
```

**Report Sections**:
1. Summary statistics
2. High-confidence complex media (by CHEBI ID)
3. Medium-confidence entries
4. Special cases (agar variants, etc.)
5. Recommendations and next steps

---

## ⚠️ Bonus: Unmerge Script (Critical!)

**File**: `scripts/unmerge_complex_media.py`

**Problem Found**: Previous deduplication run incorrectly merged 20 complex media into "Agar":
- Marine agar 2216 → Agar
- R2A agar → Agar
- Oatmeal agar → Agar
- etc.

**Solution**: Unmerge script to fix incorrect merges.

**Features**:
- **Detects incorrectly merged complex media**
- **Unmerges** and restores to UNMAPPED status
- **Sets ingredient_type** to DEFINED_MEDIUM
- **Preserves audit trail** with curation events

**Usage**:
```bash
# Preview incorrectly merged entries
python scripts/unmerge_complex_media.py --dry-run

# Interactive unmerge
python scripts/unmerge_complex_media.py --interactive

# Auto-unmerge all (dry run first!)
python scripts/unmerge_complex_media.py --auto-unmerge --dry-run
python scripts/unmerge_complex_media.py --auto-unmerge
```

**Current Findings** (dry run):
```
Found 20 Incorrectly Merged Complex Media

┌────────────────────────────┬──────────────────┬────────────┐
│ Complex Medium (Merged)    │ → Representative │ Confidence │
├────────────────────────────┼──────────────────┼────────────┤
│ Marine agar 2216           │ Agar             │ 0.95       │
│ R2A agar                   │ Agar             │ 0.95       │
│ Oatmeal agar               │ Agar             │ 0.95       │
│ Corn meal agar             │ Agar             │ 0.95       │
│ ... (16 more)              │                  │            │
└────────────────────────────┴──────────────────┴────────────┘
```

---

## Recommended Workflow

### Phase 1: Fix Incorrect Merges (URGENT)
```bash
# 1. Review incorrectly merged entries
python scripts/unmerge_complex_media.py --dry-run

# 2. Unmerge them
python scripts/unmerge_complex_media.py --auto-unmerge

# 3. Validate integrity
PYTHONPATH=src python scripts/validate_merge_integrity.py
```

### Phase 2: Identify & Classify Complex Media
```bash
# 1. Generate comprehensive report
python scripts/generate_complex_media_report.py

# 2. Review report
less analysis/complex_media_report.md

# 3. Reclassify complex media
python scripts/identify_complex_media.py --auto-reclassify --dry-run
python scripts/identify_complex_media.py --auto-reclassify
```

### Phase 3: Cross-Reference CultureMech
```bash
# 1. Find CultureMech matches
python scripts/cross_reference_culturemech.py --complex-media-only

# 2. Update links
python scripts/cross_reference_culturemech.py --update-links
```

### Phase 4: Update Merge Policies
**Prevent future incorrect merges**:

Edit `src/mediaingredientmech/curation/chebi_deduplicator.py`:

```python
def should_auto_merge(self, target_idx: int, source_idx: int) -> tuple[bool, str]:
    # ... existing code ...

    # NEW: Check for complex media
    from identify_complex_media import detect_complex_medium

    target_name = target.get("preferred_term")
    source_name = source.get("preferred_term")

    # Check if either is complex medium
    is_target_complex, conf_t, _ = detect_complex_medium(target_name, target_chebi)
    is_source_complex, conf_s, _ = detect_complex_medium(source_name, source_chebi)

    if is_target_complex or is_source_complex:
        return False, "One or both entries appear to be complex media"

    # ... rest of existing logic ...
```

---

## Files Created

### Scripts (5 total)
1. `scripts/identify_complex_media.py` - Detection & reclassification
2. `scripts/cross_reference_culturemech.py` - CultureMech integration
3. `scripts/generate_complex_media_report.py` - Analysis reports
4. `scripts/unmerge_complex_media.py` - Fix incorrect merges
5. `scripts/validate_merge_integrity.py` - Validation (from earlier)

### Reports
1. `analysis/complex_media_report.md` - Generated analysis

### Schema Updates
1. `src/mediaingredientmech/schema/mediaingredientmech.yaml` - Added fields
2. `src/mediaingredientmech/datamodel/mediaingredientmech.py` - Regenerated

---

## Current Data Status

### Problem Data (before fixes):
- **20 complex media** incorrectly merged into "Agar"
- **~211 CHEBI IDs** with "duplicates" (many are complex media)
- **Unknown number** of other complex media misclassified

### After Running Recommended Workflow:
- ✅ Complex media unmerged and properly classified
- ✅ `ingredient_type` field set for all entries
- ✅ Cross-references to CultureMech established
- ✅ Future merges protected by improved policies
- ✅ Clear distinction: single ingredients vs complex media

---

## Scientific Impact

### Before
- **Incorrect**: "Oatmeal agar" = "Agar" (chemically false)
- **Loss of information**: Recipe details hidden
- **Search problems**: Can't find specific media formulations
- **Knowledge graph errors**: Wrong relationships

### After
- **Correct**: "Oatmeal agar" is DEFINED_MEDIUM (contains multiple ingredients)
- **Preserved information**: Links to CultureMech recipes
- **Better search**: Can find media by formulation type
- **Accurate KG**: Proper relationships (medium → contains → agar)

---

## Next Steps (Optional Enhancements)

1. **Build ingredient hierarchy** for complex media:
   ```yaml
   - name: "Oatmeal agar"
     ingredient_type: DEFINED_MEDIUM
     contains_ingredients:
       - CHEBI:2509  # agar
       - FOODON:XXXX # oatmeal
       - ...
   ```

2. **Create medium recipe database** linking to CultureMech

3. **Add validation rule**: Block merging if names suggest different formulations

4. **Export to KG-Microbe**: Use proper medium → ingredient relationships

---

**Implementation Date**: 2026-03-14
**Status**: ✅ ALL 4 STEPS COMPLETE
**Tools Ready**: 5 scripts, full documentation
**Action Required**: Run Phase 1 to fix incorrect merges
