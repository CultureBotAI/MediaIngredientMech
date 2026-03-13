# Synonym Preservation Feature - Implementation Summary

## Overview

Added automatic preservation of original chemical forms as synonyms when normalization is applied during batch curation.

**Problem:** When mapping `MgSO4•7H2O` to CHEBI:32599 (magnesium sulfate), the original hydrate notation was being lost.

**Solution:** Automatically add the original form as a synonym with an appropriate type that indicates what kind of normalization was applied.

## What Was Changed

### 1. Schema Enhancement

Added 4 new synonym types to `SynonymTypeEnum`:

```yaml
# src/mediaingredientmech/schema/mediaingredientmech.yaml

SynonymTypeEnum:
  permissible_values:
    # ... existing types ...
    HYDRATE_FORM:
      description: Chemical with hydrate notation (e.g., MgSO4•7H2O)
    CATALOG_VARIANT:
      description: Name with catalog/supplier code (e.g., NaCl Fisher S271-500)
    INCOMPLETE_FORMULA:
      description: Incomplete chemical formula (e.g., K2HPO instead of K2HPO4)
    ALTERNATE_FORM:
      description: Alternative chemical form (salt, ester, etc.)
```

### 2. Batch Curation Script Enhancement

Modified `scripts/batch_curate_unmapped.py`:

**Added method:**
```python
def _add_original_as_synonym(
    self,
    record: dict,
    original_name: str,
    applied_rules: list[str],
) -> None:
    """Add the original (pre-normalization) name as a synonym."""
```

**Logic:**
- When normalization is applied AND original differs from normalized
- Add original name as a synonym
- Choose appropriate type based on normalization rules:
  - `stripped_hydrate` → `HYDRATE_FORM`
  - `stripped_catalog` → `CATALOG_VARIANT`
  - `fixed_incomplete_formula` → `INCOMPLETE_FORMULA`
  - Other → `ALTERNATE_FORM`
- Set source to `batch_curation_normalization`
- Add notes explaining what normalization was applied

**Integration:**
- Called automatically in `_accept_mapping()` method
- Checks for duplicate synonyms before adding
- Only adds if normalization was actually applied

### 3. User Feedback

The script now displays when a synonym is added:

```
Mapped to CHEBI:32599 (magnesium sulfate)
Added 'MgSO4•7H2O' as synonym (normalization: stripped_hydrate)
```

### 4. Documentation

Updated files:
- `docs/UNMAPPED_CURATION.md` - Added synonym preservation explanation
- `notes/IMPLEMENTATION_SUMMARY.md` - Documented the feature
- `notes/SYNONYM_PRESERVATION_EXAMPLE.md` - Detailed examples
- `notes/SYNONYM_FEATURE_SUMMARY.md` - This file

### 5. Testing

Created `scripts/test_synonym_preservation.py` with comprehensive tests:
- ✅ Hydrate form preservation
- ✅ Catalog variant preservation
- ✅ Incomplete formula preservation
- ✅ Multiple normalization rules
- ✅ Record update logic

**All tests pass.**

## Example Usage

### Before (without synonym preservation)

```yaml
# User curates MgSO4•7H2O
identifier: CHEBI:32599
preferred_term: MgSO4•7H2O
mapping_status: MAPPED
# Original hydrate form is lost!
```

### After (with synonym preservation)

```yaml
# User curates MgSO4•7H2O
identifier: CHEBI:32599
preferred_term: MgSO4•7H2O
synonyms:
  - synonym_text: MgSO4•7H2O
    synonym_type: HYDRATE_FORM
    source: batch_curation_normalization
    notes: "Original form before normalization: stripped_hydrate"
mapping_status: MAPPED
ontology_mapping:
  ontology_id: CHEBI:32599
  ontology_label: magnesium sulfate
```

**Now the ingredient is searchable by:**
- `MgSO4•7H2O` (original form)
- `MgSO4` (normalized form)
- `magnesium sulfate` (common name)
- `CHEBI:32599` (ontology ID)

## Benefits

1. **No data loss** - Original notation always preserved
2. **Better searchability** - Multiple search terms per ingredient
3. **Clear traceability** - Synonym type indicates what normalization was applied
4. **Audit trail** - Complete history of curation decisions
5. **Validation** - All changes comply with schema

## Files Changed

| File | Change Type | Description |
|------|-------------|-------------|
| `src/mediaingredientmech/schema/mediaingredientmech.yaml` | Modified | Added 4 new SynonymTypeEnum values |
| `scripts/batch_curate_unmapped.py` | Modified | Added synonym preservation logic |
| `scripts/test_synonym_preservation.py` | New | Test suite for synonym preservation |
| `docs/UNMAPPED_CURATION.md` | Modified | Documented synonym preservation |
| `notes/IMPLEMENTATION_SUMMARY.md` | Modified | Added feature description |
| `notes/SYNONYM_PRESERVATION_EXAMPLE.md` | New | Detailed examples |
| `notes/SYNONYM_FEATURE_SUMMARY.md` | New | This summary |

## Testing

Run the test suite:
```bash
python scripts/test_synonym_preservation.py
```

Expected output:
```
Testing synonym preservation logic...

Test 1: MgSO4•7H2O
  ✓ Normalized: MgSO4
  ✓ Applied rules: ['stripped_hydrate']
  ✓ Synonym type: HYDRATE_FORM
  ✓ Search variants: MgSO4•7H2O, MgSO4, magnesium sulfate

... (more tests)

✅ All tests passed!
```

## Next Steps

1. **Run analysis:**
   ```bash
   python scripts/analyze_unmapped.py
   ```

2. **Start curation with synonym preservation:**
   ```bash
   python scripts/batch_curate_unmapped.py \
     --category SIMPLE_CHEMICAL \
     --auto-normalize \
     --curator your_name
   ```

3. **Verify synonyms were added:**
   - Check output messages: "Added 'X' as synonym..."
   - Review CSV: `cat notes/curation_decisions.csv`
   - Inspect YAML: `cat data/curated/unmapped_ingredients.yaml`

## Validation

All changes validate against the schema:
```bash
linkml-validate \
  --schema src/mediaingredientmech/schema/mediaingredientmech.yaml \
  data/curated/unmapped_ingredients.yaml
```

The new synonym types are properly defined in the schema and recognized by LinkML validation.

## Impact

**Expected synonym additions during curation:**
- **Hydrate forms:** ~11 ingredients (e.g., `MgSO4•7H2O`, `CaCl2•2H2O`)
- **Catalog variants:** ~2 ingredients (e.g., `NaCl (Fisher S271-500)`)
- **Incomplete formulas:** ~5 ingredients (e.g., `K2HPO`, `NaNO`)
- **Total:** ~18 synonyms automatically preserved

This ensures no notation information is lost while still achieving clean ontology mappings.

## Conclusion

The synonym preservation feature is **fully implemented and tested**. It seamlessly integrates with the existing curation workflow and requires no additional user action—synonyms are automatically added when normalization is applied.

**Status:** ✅ Ready for production use
