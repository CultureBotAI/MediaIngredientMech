# Individual YAML Records Implementation

## Overview

Successfully implemented individual YAML file generation for all 1,131 ingredients, transitioning from collection-based to DisMech-style individual file structure.

**Status:** ✅ Complete and validated

## What Was Implemented

### 1. Schema Updates

**File:** `src/mediaingredientmech/schema/mediaingredientmech.yaml`

- Added `tree_root: true` to `IngredientRecord` class
- Maintains backward compatibility with `IngredientCollection` as tree_root
- Both individual files and collection files now supported by schema

### 2. Export Script

**File:** `scripts/export_individual_records.py`

**Functionality:**
- Exports collection YAMLs to individual ingredient files
- One file per ingredient (1,131 total: 995 mapped + 136 unmapped)
- Filename sanitization based on `preferred_term`
- Handles filename collisions (191 detected, resolved with _2, _3 suffixes)
- Directory structure: `data/ingredients/mapped/` and `data/ingredients/unmapped/`

**Usage:**
```bash
python scripts/export_individual_records.py
python scripts/export_individual_records.py --dry-run
python scripts/export_individual_records.py --input-dir data/curated --output-dir data/ingredients
```

**Examples:**
- "sodium chloride" → `Sodium_chloride.yaml`
- "D-glucose" → `D-glucose.yaml`
- "NaCl (99%)" → `NaCl_99.yaml`

### 3. Aggregation Script

**File:** `scripts/aggregate_records.py`

**Functionality:**
- Aggregates individual files back to collection format
- Reverse operation of export script
- Adds metadata: generation_date, total_count, mapped_count, unmapped_count
- Optional validation during aggregation
- Output: `data/collections/mapped_ingredients.yaml` and `unmapped_ingredients.yaml`

**Usage:**
```bash
python scripts/aggregate_records.py
python scripts/aggregate_records.py --validate
python scripts/aggregate_records.py --ingredients-dir data/ingredients --output-dir data/collections
```

### 4. Updated Validation Script

**File:** `scripts/validate_all.py` (updated)

**New features:**
- `--mode` option: `collection`, `individual`, or `both` (default: both)
- `--ingredients-dir` option for individual file directory
- Validates both collection files and individual ingredient files
- Scans directories recursively for YAML files

**Usage:**
```bash
python scripts/validate_all.py --mode both          # Validate both formats
python scripts/validate_all.py --mode individual    # Only individual files
python scripts/validate_all.py --mode collection    # Only collection files
```

### 5. Round-Trip Verification Script

**File:** `scripts/verify_roundtrip.py` (new)

**Functionality:**
- Verifies data integrity between original and aggregated collections
- Compares ingredient records after export → individual → aggregate workflow
- Handles duplicate identifiers correctly (sorts by identifier + preferred_term)
- Reports differences and metadata changes

**Usage:**
```bash
python scripts/verify_roundtrip.py
python scripts/verify_roundtrip.py --original-dir data/curated --aggregated-dir data/collections
```

### 6. Updated Justfile Commands

**New commands:**
```makefile
just export-individual          # Export collections to individual files
just aggregate-collections      # Aggregate individual files to collections
just validate-individual        # Validate individual files only
just sync-individual            # Full workflow: export → validate → aggregate
```

**Updated commands:**
```makefile
just validate-all              # Now validates both formats (--mode both)
```

## Directory Structure

```
MediaIngredientMech/
├── data/
│   ├── curated/                          # Original collection files (unchanged)
│   │   ├── mapped_ingredients.yaml       # 995 records
│   │   └── unmapped_ingredients.yaml     # 136 records
│   ├── ingredients/                      # NEW: Individual ingredient files
│   │   ├── mapped/                       # 995 individual YAML files
│   │   │   ├── Nacl.yaml
│   │   │   ├── Glucose.yaml
│   │   │   ├── Sodium_chloride.yaml
│   │   │   └── ... (992 more)
│   │   └── unmapped/                     # 136 individual YAML files
│   │       ├── A_Trace_Components.yaml
│   │       ├── Empty.yaml
│   │       └── ... (134 more)
│   └── collections/                      # NEW: Aggregated collections
│       ├── mapped_ingredients.yaml       # Aggregated from individual files
│       └── unmapped_ingredients.yaml     # Aggregated from individual files
├── scripts/
│   ├── export_individual_records.py      # NEW
│   ├── aggregate_records.py              # NEW
│   ├── verify_roundtrip.py               # NEW
│   └── validate_all.py                   # UPDATED
└── src/mediaingredientmech/schema/
    └── mediaingredientmech.yaml          # UPDATED (tree_root on IngredientRecord)
```

## Verification Results

### File Counts
- ✅ Mapped files: 995
- ✅ Unmapped files: 136
- ✅ Total files: 1,131

### Validation
- ✅ All 1,131 individual files pass schema validation
- ✅ 0 errors
- ✅ 1,131 warnings (expected - optional fields)
- ✅ Aggregated collections pass validation

### Round-Trip Integrity
- ✅ Export → Individual → Aggregate verified
- ✅ Data integrity maintained
- ✅ Only metadata (generation_date) differs as expected
- ✅ Handles duplicate identifiers correctly

### Existing Tests
- ✅ All 139 existing tests pass
- ✅ No breaking changes to existing functionality

## Individual File Format

Each individual YAML file contains a single `IngredientRecord` at the root level (no collection wrapper):

```yaml
identifier: CHEBI:26710
preferred_term: NaCl
ontology_mapping:
  ontology_id: CHEBI:26710
  ontology_label: NaCl
  ontology_source: CHEBI
  mapping_quality: EXACT_MATCH
  evidence:
  - evidence_type: DATABASE_MATCH
    source: CultureMech
    notes: Imported from CultureMech pipeline, quality=DIRECT_MATCH
synonyms:
- synonym_text: Role: Mineral source; Properties: Defined component
  synonym_type: RAW_TEXT
  source: CultureMech
mapping_status: MAPPED
occurrence_statistics:
  total_occurrences: 6041
  media_count: 50
curation_history:
- timestamp: '2026-03-06T09:44:18.947386+00:00'
  curator: import_from_culturemech
  action: IMPORTED
  changes: Initial import from CultureMech pipeline
  new_status: MAPPED
  llm_assisted: false
```

## Benefits Achieved

### Version Control
- ✅ File-level version control (each ingredient = separate commit)
- ✅ Easier code review (changes isolated to single files)
- ✅ Clear audit trail per ingredient

### Curation Workflow
- ✅ Parallel curation workflows (no merge conflicts)
- ✅ File-level locking possible
- ✅ Easier to track changes per ingredient

### DisMech Methodology Compliance
- ✅ Flat file structure within categories
- ✅ Name-based filenames (sanitized preferred_term)
- ✅ Individual records as tree_root
- ✅ Similar to DisMech disorder files

### Backward Compatibility
- ✅ Original collection files unchanged
- ✅ Collection format still supported
- ✅ Existing tools work with collections
- ✅ All existing tests pass

## Known Issues and Notes

### Filename Collisions
- 191 filename collisions detected (ingredients with same/similar preferred terms)
- Resolved with numeric suffixes (_2, _3, etc.)
- Examples: "glucose" → "Glucose.yaml", "Glucose_2.yaml"

### Duplicate Identifiers
- Some ingredients share the same CHEBI ID but have different preferred terms
- Example: 5 records with CHEBI:115156 (Na2-fumarate, Sodium Fumarate, Na-fumarate, Disodium Fumarate)
- This is a data quality issue in the original data, not a bug in the implementation
- Round-trip verification handles this correctly

### Performance
- Export: ~2 seconds for 1,131 files
- Aggregate: ~1 second for 1,131 files
- Validation: ~30 seconds for 1,131 individual files (without OAK)

## Workflow Examples

### Export and Validate
```bash
# Export collections to individual files
just export-individual

# Validate individual files
just validate-individual

# Verify counts
ls -1 data/ingredients/mapped/*.yaml | wc -l    # Should be 995
ls -1 data/ingredients/unmapped/*.yaml | wc -l  # Should be 136
```

### Aggregate and Verify
```bash
# Aggregate individual files to collections
just aggregate-collections

# Verify round-trip integrity
python scripts/verify_roundtrip.py

# Validate aggregated collections
just validate-all
```

### Full Workflow
```bash
# Complete workflow in one command
just sync-individual

# This runs:
# 1. Export collections → individual files
# 2. Validate individual files
# 3. Aggregate individual files → collections
```

## Future Enhancements (Optional)

### Potential Improvements
- [ ] Add `--format json` option to export/aggregate scripts
- [ ] Create individual file index for faster lookups
- [ ] Add `--category` filter to scripts (mapped/unmapped only)
- [ ] Implement incremental export (only changed records)
- [ ] Add file-level metadata headers (e.g., last_modified)

### Integration with Curation Workflow
- [ ] Update `curate_unmapped.py` to work directly with individual files
- [ ] Add file renaming when preferred_term changes during curation
- [ ] Implement file-level locking for concurrent curation
- [ ] Create curation dashboard showing per-file status

## References

### DisMech Patterns
Based on patterns from:
- `/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/CultureMech/dismech/kb/disorders/`
- File naming: `Alzheimers_Disease.yaml`, `Asthma.yaml`, etc.
- Flat directory structure within categories
- Individual records as tree_root

### Related Files
- Plan document: See plan mode transcript
- Schema: `src/mediaingredientmech/schema/mediaingredientmech.yaml`
- Original collections: `data/curated/*.yaml`
- Individual files: `data/ingredients/{mapped,unmapped}/*.yaml`

---

**Implementation Date:** 2026-03-06
**Total Files Generated:** 1,131 (995 mapped + 136 unmapped)
**Validation Status:** ✅ All tests pass
**Round-Trip Integrity:** ✅ Verified
