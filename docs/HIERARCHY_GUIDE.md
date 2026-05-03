# Ingredient Hierarchy Guide

**Version:** 1.0
**Date:** 2026-03-14
**Purpose:** How to use ingredient hierarchies in MediaIngredientMech

---

## Table of Contents

1. [Overview](#overview)
2. [Hierarchy Schema](#hierarchy-schema)
3. [Water Hierarchy Example](#water-hierarchy-example)
4. [Query Utilities](#query-utilities)
5. [Creating Hierarchies](#creating-hierarchies)
6. [Validation](#validation)
7. [Best Practices](#best-practices)
8. [Use Cases](#use-cases)

---

## Overview

MediaIngredientMech supports **parent-child hierarchies** for organizing ingredient variants:

- **Purity levels:** Tap water → Distilled water → Double distilled water
- **Hydrates:** CaCl₂ (anhydrous) → CaCl₂·2H₂O (dihydrate)
- **Stereoisomers:** Glucose (base) → D-glucose → L-glucose

**Benefits:**
- ✅ **Preserves distinctions:** All variants remain separate records
- ✅ **Enables queries:** "Find all media using any form of water"
- ✅ **Documents relationships:** Explicit parent-child links
- ✅ **Supports role inheritance:** Children auto-get parent's roles
- ✅ **Prevents bad merges:** Different variants stay distinct

---

## Hierarchy Schema

### Fields (IngredientRecord)

All hierarchy fields are **optional** (backward compatible):

**1. `parent_ingredient`** (string)
- Reference to parent in hierarchy (MediaIngredientMech:XXXXXX)
- Used by child variants
- Example: Distilled water → parent: Water (base)

**2. `child_ingredients`** (string[])
- List of child ingredient IDs
- Used by parent records
- Example: Water (base) → children: [Tap, Distilled, Double distilled]

**3. `variant_type`** (VariantTypeEnum)
- Classification of variant relationship
- Indicates why distinct from parent/siblings
- Values: BASE_CHEMICAL, PURIFIED, ULTRA_PURIFIED, TAP, HYDRATE, STEREOISOMER, etc.

**4. `variant_notes`** (string)
- Human-readable distinction from parent/siblings
- Example: "Higher purity (10x) than standard distilled water"

**5. `role_inheritance`** (boolean)
- If true, inherits `media_roles` from parent
- Allows variant-specific role overrides

### VariantTypeEnum Values

- **BASE_CHEMICAL** - Parent form (Water base, Glucose base)
- **PURIFIED** - Standard purified (Distilled water)
- **ULTRA_PURIFIED** - Higher purity (Double distilled water)
- **TAP** - Impure tap water
- **DEMINERALIZED** - Ion exchange purified
- **HYDRATE** - Hydrated form (CaCl₂·2H₂O vs CaCl₂)
- **STEREOISOMER** - Different stereochemistry (D-glucose vs L-glucose)
- **SALT** - Different counterion
- **ANHYDROUS** - Water-free form

---

## Water Hierarchy Example

The water purity hierarchy demonstrates all hierarchy features:

```yaml
# PARENT: Water (base)
id: MediaIngredientMech:001108
identifier: CHEBI:15377
preferred_term: Water (base)
variant_type: BASE_CHEMICAL
child_ingredients:
  - MediaIngredientMech:000260  # Tap water
  - MediaIngredientMech:000472  # Demineralized water
  - MediaIngredientMech:000114  # Distilled water
  - MediaIngredientMech:000268  # Double distilled water
media_roles:
  - role: SOLVENT
    confidence: 1.0

# CHILD: Distilled water
id: MediaIngredientMech:000114
preferred_term: Distilled water
parent_ingredient: MediaIngredientMech:001108
variant_type: PURIFIED
variant_notes: |
  Single thermal distillation process.
  Standard laboratory water (<1 µS/cm conductivity).
  Baseline pure water for media preparation.
role_inheritance: true  # Inherits SOLVENT role from parent
```

**Hierarchy tree:**
```
Water (base) [BASE_CHEMICAL]
├─ Tap water [TAP]
├─ Demineralized water [DEMINERALIZED]
├─ Distilled water [PURIFIED]
└─ Double distilled water [ULTRA_PURIFIED]
```

---

## Query Utilities

Use `hierarchy_utils.py` functions to navigate hierarchies:

### 1. Get Parent

```python
from mediaingredientmech.utils.hierarchy_utils import get_parent

parent = get_parent('MediaIngredientMech:000114', all_records)
# Returns: Water (base) record
```

### 2. Get Children

```python
from mediaingredientmech.utils.hierarchy_utils import get_children

children = get_children('MediaIngredientMech:001108', all_records)
# Returns: [Tap water, Demineralized, Distilled, Double distilled]
```

### 3. Get All Variants (Family)

```python
from mediaingredientmech.utils.hierarchy_utils import get_all_variants

# Query from any variant in family
variants = get_all_variants('MediaIngredientMech:000114', all_records)
# Returns: [Water (base), Tap water, Demineralized, Distilled, Double distilled]
```

**Use case:** "Find all media using any form of water"
1. Get all variants of water
2. Query media using any variant ID

### 4. Get Siblings

```python
from mediaingredientmech.utils.hierarchy_utils import get_siblings

siblings = get_siblings('MediaIngredientMech:000114', all_records)
# Returns: [Tap water, Demineralized, Double distilled] (excludes Distilled)
```

### 5. Get Inherited Roles

```python
from mediaingredientmech.utils.hierarchy_utils import get_inherited_roles

roles = get_inherited_roles('MediaIngredientMech:000114', all_records)
# Returns: [{'role': 'SOLVENT', 'confidence': 1.0}] (from parent)
```

### 6. Get Hierarchy Summary

```python
from mediaingredientmech.utils.hierarchy_utils import get_hierarchy_summary

summary = get_hierarchy_summary('MediaIngredientMech:000114', all_records)
# Returns comprehensive dict with parent, siblings, roles, etc.
```

**Example output:**
```python
{
    'id': 'MediaIngredientMech:000114',
    'preferred_term': 'Distilled water',
    'role': 'child',
    'variant_type': 'PURIFIED',
    'role_inheritance': True,
    'parent': {
        'id': 'MediaIngredientMech:001108',
        'preferred_term': 'Water (base)',
        'variant_type': 'BASE_CHEMICAL'
    },
    'sibling_count': 3,
    'siblings': [
        {'id': '...', 'preferred_term': 'Tap water', 'variant_type': 'TAP'},
        ...
    ],
    'inherited_roles': ['SOLVENT']
}
```

### 7. Get Hierarchy Tree String

```python
from mediaingredientmech.utils.hierarchy_utils import get_hierarchy_tree_string

tree = get_hierarchy_tree_string('MediaIngredientMech:001108', all_records)
print(tree)
```

**Output:**
```
Water (base) [BASE_CHEMICAL]
├─ Tap water [TAP]
├─ Demineralized water [DEMINERALIZED]
├─ Distilled water [PURIFIED]
└─ Double distilled water [ULTRA_PURIFIED]
```

---

## Creating Hierarchies

### Manual Creation

**Step 1: Create parent record**
```yaml
id: MediaIngredientMech:NEW_ID
preferred_term: Glucose (base)
variant_type: BASE_CHEMICAL
child_ingredients:
  - MediaIngredientMech:CHILD1_ID
  - MediaIngredientMech:CHILD2_ID
media_roles:
  - role: CARBON_SOURCE
    confidence: 1.0
```

**Step 2: Link children**
```yaml
id: MediaIngredientMech:CHILD1_ID
preferred_term: D-glucose
parent_ingredient: MediaIngredientMech:NEW_ID
variant_type: STEREOISOMER
variant_notes: "D-form (dextrose), naturally occurring"
role_inheritance: true
```

**Step 3: Validate**
```python
from mediaingredientmech.utils.hierarchy_validator import validate_hierarchy

is_valid, errors = validate_hierarchy(record, all_records)
if not is_valid:
    print(f"Validation failed: {errors}")
```

### Automated Creation

Use builder scripts (see `scripts/build_water_hierarchy.py` as template):

```python
# Create parent
parent = create_parent_record(...)
curator.records.append(parent)

# Link children
for child_idx in child_indices:
    link_child_to_parent(curator.records[child_idx], parent_id, variant_type, notes)

# Validate
results = validate_all_hierarchies(curator.records)

# Save
curator.save()
```

---

## Validation

Use `hierarchy_validator.py` to ensure integrity:

### Validation Checks

1. **Parent exists:** `parent_ingredient` ID must exist in dataset
2. **No circular refs:** A→B→A loops are prevented
3. **Bidirectional links:** Parent lists child, child references parent
4. **Variant type matches:** BASE_CHEMICAL has children, others have parent

### Validation Functions

```python
from mediaingredientmech.utils.hierarchy_validator import (
    validate_hierarchy,
    validate_all_hierarchies,
    get_hierarchy_statistics,
)

# Validate single record
is_valid, errors = validate_hierarchy(record, all_records)

# Validate all records
results = validate_all_hierarchies(all_records)
invalid = {id: errs for id, errs in results.items() if errs}

# Get statistics
stats = get_hierarchy_statistics(all_records)
# Returns: parent_count, leaf_count, orphan_count, variant_types
```

---

## Best Practices

### 1. When to Use Hierarchy

**✅ Use hierarchy for:**
- Purity variants (tap/distilled/double distilled water)
- Hydration states (CaCl₂ vs CaCl₂·2H₂O vs CaCl₂·6H₂O)
- Stereoisomers (D-glucose vs L-glucose)
- Salt forms (sodium phosphate vs potassium phosphate)

**❌ Don't use hierarchy for:**
- True duplicates (merge instead: "NaCl" + "sodium chloride" → merge)
- Unrelated chemicals (use separate records)
- Complex media (use `ingredient_type: DEFINED_MEDIUM`)

### 2. Variant Notes Best Practices

**Good variant notes:**
```yaml
variant_notes: |
  Higher purity than standard distilled (<0.1 µS/cm vs <1 µS/cm).
  10x purer, used for trace-metal sensitive work.
```

**Bad variant notes:**
```yaml
variant_notes: "purer"  # Too vague
```

**Template:**
```yaml
variant_notes: |
  [Process/composition difference]
  [Quantitative distinction if applicable]
  [Use cases / when to use this variant]
```

### 3. Role Inheritance

**Always set `role_inheritance: true` on children** if they share parent's basic function:

```yaml
# Parent: Water (base)
media_roles:
  - role: SOLVENT  # All water is a solvent

# Child: Tap water
role_inheritance: true  # Inherits SOLVENT
media_roles:  # Can add variant-specific roles
  - role: MINERAL_SOURCE  # Tap water provides trace minerals
    confidence: 0.5
    notes: "Contains Ca, Mg from municipal supply"
```

### 4. Validation Always

**After creating/modifying hierarchy:**
```python
# Validate
results = validate_all_hierarchies(curator.records)

# Check for errors
invalid = {id: errs for id, errs in results.items() if errs}
if invalid:
    print("Validation failed!")
    for id, errors in invalid.items():
        print(f"{id}: {errors}")
else:
    print("✓ Hierarchy valid")
    curator.save()
```

---

## Use Cases

### Use Case 1: Find All Media Using Any Water

**Problem:** Need to find all media using water, regardless of purity level

**Solution:**
```python
# Get all water variants
water_parent_id = 'MediaIngredientMech:001108'
all_water = get_all_variants(water_parent_id, all_records)
water_ids = {w['id'] for w in all_water}

# Query media containing any water variant
media_with_water = [
    m for m in media_records
    if any(ing_id in water_ids for ing_id in m['ingredients'])
]
```

### Use Case 2: Check Purity Requirements

**Problem:** Recipe specifies "distilled water" - can I use tap water?

**Solution:**
```python
# Get sibling water variants
siblings = get_siblings('MediaIngredientMech:000114', all_records)

# Check variant types
for s in siblings:
    print(f"{s['preferred_term']}: {s['variant_type']}")
    print(f"  Notes: {s.get('variant_notes', 'N/A')}")

# Decision: No - tap water is TAP type (impure), distilled is PURIFIED
```

### Use Case 3: Role Resolution

**Problem:** What roles does double distilled water have?

**Solution:**
```python
roles = get_inherited_roles('MediaIngredientMech:000268', all_records)
# Returns: [{'role': 'SOLVENT', ...}] from parent

# Plus any variant-specific roles
summary = get_hierarchy_summary('MediaIngredientMech:000268', all_records)
print(f"Inherited: {summary['inherited_roles']}")
# Inherited: ['SOLVENT']
```

### Use Case 4: Document Variant Relationships

**Problem:** Why is double distilled separate from distilled?

**Solution:**
```python
summary = get_hierarchy_summary('MediaIngredientMech:000268', all_records)

print(f"Variant type: {summary['variant_type']}")  # ULTRA_PURIFIED
print(f"Parent: {summary['parent']['preferred_term']}")  # Water (base)

record = next(r for r in all_records if r['id'] == 'MediaIngredientMech:000268')
print(f"Why distinct: {record['variant_notes']}")
# "Higher purity (10x) than standard distilled..."
```

---

## Migration Guide

### Existing Data Without Hierarchy

Existing records work unchanged - hierarchy fields are optional:

```yaml
# Before hierarchy (still valid)
id: MediaIngredientMech:000114
preferred_term: Distilled water
# No hierarchy fields

# After hierarchy (backward compatible)
id: MediaIngredientMech:000114
preferred_term: Distilled water
parent_ingredient: MediaIngredientMech:001108  # NEW
variant_type: PURIFIED  # NEW
role_inheritance: true  # NEW
```

### Adding Hierarchy to Existing Records

Use builder scripts:
1. Create parent record
2. Update children with `parent_ingredient`, `variant_type`, `variant_notes`
3. Update parent with `child_ingredients` list
4. Validate
5. Save

**See:** `scripts/build_water_hierarchy.py` for complete example

---

## API Reference

### hierarchy_utils.py

- `get_parent(id, records)` → parent record
- `get_children(id, records)` → list of child records
- `get_all_variants(id, records)` → parent + all children
- `get_siblings(id, records)` → sibling records (excludes self)
- `get_inherited_roles(id, records)` → resolved roles
- `get_hierarchy_tree_string(id, records)` → tree visualization
- `get_hierarchy_summary(id, records)` → comprehensive dict

### hierarchy_validator.py

- `validate_parent_exists(record, records)` → (bool, error)
- `validate_no_circular_refs(record, records)` → (bool, error)
- `validate_children_reference_parent(record, records)` → (bool, error)
- `validate_variant_type_matches(record)` → (bool, error)
- `validate_hierarchy(record, records)` → (bool, [errors])
- `validate_all_hierarchies(records)` → {id: [errors]}
- `get_hierarchy_statistics(records)` → stats dict

---

## Examples

### Water Hierarchy (Built)

**Status:** ✅ Complete (MediaIngredientMech:001108)

**Structure:**
- Parent: Water (base)
- Children: Tap, Demineralized, Distilled, Double distilled

**Files:**
- Builder: `scripts/build_water_hierarchy.py`
- Guide: `docs/WATER_VARIANT_CURATION.md`

### Future Hierarchies

**Candidates:**
- **Glucose family:** D-glucose, L-glucose, α-D-glucose, β-D-glucose
- **Calcium chloride hydrates:** CaCl₂, CaCl₂·2H₂O, CaCl₂·6H₂O
- **Biotin stereoisomers:** D-biotin, L-biotin

---

## Troubleshooting

### Problem: Validation fails "Parent does not exist"

**Cause:** `parent_ingredient` ID not in dataset

**Solution:** Check ID typo, ensure parent created first

### Problem: Circular reference detected

**Cause:** A→B→C→A loop

**Solution:** Remove loop, restructure hierarchy

### Problem: Child not in parent's child_ingredients

**Cause:** Bidirectional link broken

**Solution:** Add child ID to parent's `child_ingredients` list

### Problem: Role inheritance not working

**Cause:** `role_inheritance: false` or not set

**Solution:** Set `role_inheritance: true` on child record

---

## Related Documentation

- **Schema:** `src/mediaingredientmech/schema/mediaingredientmech.yaml`
- **Water Example:** `docs/WATER_VARIANT_CURATION.md`
- **Purity Detection:** `docs/MERGE_CURATION_GUIDE.md` (Pattern 5)
- **Merge Blocking:** `PURITY_VALIDATION_IMPLEMENTATION.md`

---

**Last Updated:** 2026-03-14
**Status:** Production ready, water hierarchy implemented
