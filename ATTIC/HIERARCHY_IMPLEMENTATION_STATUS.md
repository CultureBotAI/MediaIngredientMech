# Hierarchy System Implementation - Status

**Date:** 2026-03-14
**Status:** IN PROGRESS
**Goal:** Add parent-child relationships for ingredient variants (water purity levels, hydrates, stereoisomers)

---

## Implementation Plan

### Phase 1: Schema Extensions ✓ (Next)

**File:** `src/mediaingredientmech/schema/mediaingredientmech.yaml`

**Add fields:**
```yaml
classes:
  IngredientRecord:
    attributes:
      # ... existing fields ...

      # NEW: Hierarchy fields
      parent_ingredient:
        range: string
        description: >
          Reference to parent ingredient in hierarchy (MediaIngredientMech:XXXXXX).
          Used for variants: purity levels (tap/distilled), hydrates, stereoisomers.
        required: false

      child_ingredients:
        range: string
        multivalued: true
        description: >
          List of child ingredient IDs in hierarchy.
          Parent record contains all children (e.g., Water → Tap water, Distilled water).
        required: false

      variant_type:
        range: VariantTypeEnum
        description: >
          Classification of variant relationship to parent.
          Indicates why this ingredient is distinct from parent.
        required: false

      variant_notes:
        range: string
        description: >
          Human-readable explanation of variant distinction.
          Example: "Higher purity (10x) than standard distilled water"
        required: false

      role_inheritance:
        range: boolean
        description: >
          If true, inherits media_roles from parent ingredient.
          Allows child to override with specific roles.
        required: false

# NEW: Variant type enumeration
enums:
  VariantTypeEnum:
    description: >
      Types of ingredient variants in hierarchy.
    permissible_values:
      BASE_CHEMICAL:
        description: Parent/base form of chemical
      HYDRATE:
        description: Hydrated form (e.g., CaCl2·2H2O vs CaCl2)
      STEREOISOMER:
        description: Different stereochemistry (e.g., D-glucose vs L-glucose)
      PURIFIED:
        description: Standard purified form (e.g., distilled water)
      ULTRA_PURIFIED:
        description: Higher purity variant (e.g., double distilled)
      TAP:
        description: Impure tap water variant
      DEMINERALIZED:
        description: Demineralized/deionized variant
      SALT:
        description: Salt form of compound
      ANHYDROUS:
        description: Water-free form
```

### Phase 2: Validation Logic

**File:** `src/mediaingredientmech/validation/hierarchy_validator.py` (NEW)

**Functions:**
- `validate_parent_exists()` - Ensure parent_ingredient ID exists
- `validate_no_circular_refs()` - Prevent A→B→A loops
- `validate_children_reference_parent()` - Ensure bidirectional links
- `validate_variant_type_matches()` - Check variant_type makes sense

### Phase 3: Hierarchy Builder Tool

**File:** `scripts/build_water_hierarchy.py` (NEW)

**Purpose:** Apply hierarchy to water variants as test case

**Actions:**
1. Create parent "Water (base)" record
2. Link existing water variants as children:
   - Tap water (variant_type: TAP)
   - Demineralized water (variant_type: DEMINERALIZED)
   - Distilled water (variant_type: PURIFIED)
   - Double distilled water (variant_type: ULTRA_PURIFIED)
3. Set role_inheritance: true on all children
4. Validate bidirectional links

### Phase 4: Query Utilities

**File:** `src/mediaingredientmech/utils/hierarchy_utils.py` (NEW)

**Functions:**
- `get_all_variants(ingredient_id)` - Get parent + all children
- `get_parent(ingredient_id)` - Navigate up hierarchy
- `get_children(ingredient_id)` - Navigate down hierarchy
- `get_inherited_roles(ingredient_id)` - Resolve role inheritance

### Phase 5: Documentation

**Files:**
- `docs/HIERARCHY_GUIDE.md` - How to use hierarchy
- Update `docs/WATER_VARIANT_CURATION.md` - Show hierarchy in action

---

## Current Status

✅ **Completed:**
- Water variant curation rules documented
- Water variants curated and quality-adjusted:
  - Distilled water (7 → 1 merge, EXACT_MATCH)
  - Double distilled (CLOSE_MATCH, higher purity)
  - Tap water (CLOSE_MATCH, impure)
  - Demineralized (CLOSE_MATCH, NEEDS_EXPERT)

⏳ **In Progress:**
- Schema extensions (Phase 1)

🔜 **Next Steps:**
1. Add hierarchy fields to schema
2. Create validation logic
3. Build water hierarchy as proof of concept
4. Test queries
5. Document usage

---

## Water Hierarchy Design (Test Case)

```yaml
# PARENT: Water (base concept)
- id: MediaIngredientMech:001108  # NEW ID
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
  notes: >
    Parent concept for all water purity variants.
    Children inherit SOLVENT role but may have specific use restrictions.

# CHILD: Tap water
- id: MediaIngredientMech:000260
  preferred_term: Tap water
  parent_ingredient: MediaIngredientMech:001108
  variant_type: TAP
  variant_notes: >
    Municipal water supply. Contains chlorine (0.2-4 ppm) and minerals.
    NOT suitable for trace-metal work or chlorine-sensitive organisms.
  role_inheritance: true

# CHILD: Demineralized water
- id: MediaIngredientMech:000472
  preferred_term: Demineralized water
  parent_ingredient: MediaIngredientMech:001108
  variant_type: DEMINERALIZED
  variant_notes: >
    Ion exchange process, low mineral content.
    May be equivalent to distilled in microbiology practice (needs review).
  role_inheritance: true

# CHILD: Distilled water
- id: MediaIngredientMech:000114
  preferred_term: Distilled water
  parent_ingredient: MediaIngredientMech:001108
  variant_type: PURIFIED
  variant_notes: >
    Single distillation, <1 µS/cm conductivity.
    Standard laboratory water for media preparation.
  role_inheritance: true

# CHILD: Double distilled water
- id: MediaIngredientMech:000268
  preferred_term: Double distilled water
  parent_ingredient: MediaIngredientMech:001108
  variant_type: ULTRA_PURIFIED
  variant_notes: >
    Double distillation, <0.1 µS/cm conductivity (10x purer than standard).
    For trace-metal sensitive work and ultra-pure applications.
  role_inheritance: true
```

---

## Benefits

1. **Preserves distinctions:** All purity levels remain separate
2. **Enables queries:** "Find all media using any water" → query parent
3. **Documents relationships:** Explicit parent-child links
4. **Supports role inheritance:** Children auto-get SOLVENT role
5. **Prevents bad merges:** Purity detection still blocks inappropriate merges
6. **Scientific accuracy:** Maintains biological relevance

---

## Timeline

- **Phase 1 (Schema):** 30 min
- **Phase 2 (Validation):** 30 min
- **Phase 3 (Builder):** 45 min
- **Phase 4 (Queries):** 30 min
- **Phase 5 (Docs):** 15 min

**Total:** ~2.5 hours

---

**Next:** Implement Phase 1 (Schema Extensions)
