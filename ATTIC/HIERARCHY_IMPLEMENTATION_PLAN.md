# Ingredient Hierarchy & Merge System - REFINED PLAN
**Based on Real Data Analysis - 2026-03-14**

## Key Findings from Data Analysis

### Discovered Patterns

**1. True Duplicates (219 groups, ~500+ ingredients)**:
- Simple naming variations: "NaCl" vs "Sodium chloride" vs "sodium chloride"
- Case differences: "Agar" vs "agar"
- Spacing variations: "MgSO4x7H2O" vs "MgSO4 x 7 H2O"
- **Action**: These SHOULD be merged

**2. Variant Families (51 families, 224 ingredients)**:
- Hydrates: MgSO4·7H2O vs MgSO4·4H2O vs MgSO4 (anhydrous)
- Stereoisomers: D-biotin vs L-biotin vs biotin
- Different hydration numbers: NiCl2·6H2O vs NiCl2·2H2O vs NiCl2·5H2O
- **Action**: Keep separate, build hierarchy
- **Insight**: They share common roles (MINERAL, BUFFER) → validates role inheritance

**3. Special Cases Requiring Review**:
- **Agar variants** (23 types!): "Marine agar 2216", "R2A agar", "Corn meal agar"
  - All mapped to CHEBI:2509 (agar)
  - But these are DIFFERENT media, not duplicates
  - **Action**: These should NOT be merged, might need different CHEBI IDs

### Statistics
- **BASE_CHEMICAL**: 785 ingredients (79%)
- **HYDRATE**: 136 ingredients (14%)
- **STEREOISOMER**: 57 ingredients (6%)
- **SALT**: 17 ingredients (2%)

## Refined Implementation Strategy

### Priority 1: Merge True Duplicates (Immediate Value)

**Scope**: 219 duplicate groups affecting ~500 ingredients

**Merge Rules**:
1. ✅ Merge if same CHEBI ID + same variant type
2. ✅ Merge case/spacing variations
3. ✅ Combine synonyms, occurrence counts
4. ✅ Preserve all curation history
5. ❌ Do NOT merge different hydrates (·7H2O vs ·2H2O)
6. ❌ Do NOT merge stereoisomers (D- vs L-)

**Benefits**:
- Cleaner data (995 → ~500 unique chemicals)
- Combined occurrence statistics (more accurate)
- Better search/browse experience

**Risk**: Low (conservative matching)

### Priority 2: Build Variant Hierarchies (High Scientific Value)

**Scope**: 51 variant families with 224 ingredients

**Hierarchy Structure**:
```yaml
# Example: Magnesium sulfate family
- id: MediaIngredientMech:000118
  ontology_id: CHEBI:31795
  preferred_term: MgSO4·7H2O
  parent_ingredient: MediaIngredientMech:PARENT_MgSO4  # Base chemical
  variant_type: HYDRATE
  role_inheritance: true  # Inherits MINERAL role

- id: MediaIngredientMech:PARENT_MgSO4
  ontology_id: CHEBI:PARENT  # Or use most common form's CHEBI
  preferred_term: Magnesium sulfate (base)
  child_ingredients:
    - MediaIngredientMech:000118  # ·7H2O
    - MediaIngredientMech:000380  # ·4H2O
  variant_type: BASE_CHEMICAL
  media_roles:
    - role: MINERAL
      confidence: 1.0
```

**Implementation**:
1. Identify base chemical (most common form or anhydrous)
2. Link variants to parent
3. Enable role inheritance
4. Allow variant-specific role overrides

**Benefits**:
- Scientific accuracy (preserves chemical variants)
- Role inheritance reduces manual curation
- Enables queries: "all forms of glucose"

### Priority 3: Special Case Handling (Requires Expert Review)

**Agar Problem**: 23 different agar types all mapped to CHEBI:2509
- **Marine agar 2216** (defined medium)
- **R2A agar** (defined medium)
- **Corn meal agar** (defined medium)
- **Plain agar** (solidifying agent)

**Options**:
1. **Option A**: Create hierarchy with "agar" as parent, specific agars as children
2. **Option B**: Remap specific agars to different ontology terms (e.g., FOODON for corn meal)
3. **Option C**: Keep as duplicates, mark as "defined media" vs "ingredient"

**Recommendation**: Needs domain expert input

### Phase A: Schema Extensions (Refined)

```yaml
# Add to IngredientRecord
attributes:
  parent_ingredient:
    range: string
    description: MediaIngredientMech ID of parent ingredient (base chemical)
    pattern: "^MediaIngredientMech:\\d{6}$"

  child_ingredients:
    range: string
    multivalued: true
    description: MediaIngredientMech IDs of child variant ingredients

  variant_type:
    range: VariantTypeEnum
    description: Chemical variant classification

  role_inheritance:
    range: boolean
    description: Whether roles are inherited from parent (default true for variants)

  merge_history:
    range: MergeEvent
    multivalued: true
    description: History of ingredients merged into this record

# New class for merge tracking
MergeEvent:
  description: Record of ingredient merge operation
  attributes:
    timestamp:
      range: datetime
      required: true
    merged_from:
      range: string
      required: true
      description: MediaIngredientMech ID of merged ingredient
    reason:
      description: Why these were merged (duplicate, synonym, etc.)
    curator:
      description: Who performed the merge

# New enum
VariantTypeEnum:
  permissible_values:
    BASE_CHEMICAL:
      description: Base form or most common variant
    HYDRATE:
      description: Hydrated crystalline form (·nH2O)
    ANHYDROUS:
      description: Explicitly anhydrous (water-free) form
    SALT:
      description: Salt form (HCl, Na+, K+ salts)
    STEREOISOMER:
      description: Specific stereoisomer (D/L, R/S, +/-)
    IONIZED_FORM:
      description: Ionization state (acetate vs acetic acid)
```

### Implementation Phases (Revised)

**Phase A1: Schema + Merge Detection (Week 1)**
- Add schema fields
- Implement conservative merge detector
- Generate merge proposals (don't auto-merge)

**Phase A2: Manual Merge Review (Week 1)**
- Review top 50 duplicate groups
- Identify any false positives
- Create merge exception list

**Phase A3: Execute Merges (Week 2)**
- Script to merge approved duplicates
- Preserve full audit trail
- Update occurrence counts
- 995 ingredients → ~500 unique chemicals

**Phase B1: Hierarchy Detection (Week 2)**
- Detect parent-child relationships
- Propose hierarchies for 51 variant families
- Generate review report

**Phase B2: Manual Hierarchy Review (Week 3)**
- Review proposed hierarchies
- Identify base chemicals
- Assign role inheritance flags

**Phase B3: Build Hierarchies (Week 3)**
- Apply approved hierarchies
- Test role inheritance
- Update documentation

**Phase C: Special Cases (Week 4)**
- Expert review of agar variants
- Review other ambiguous cases
- Document curation decisions

## Validation & Rollback

**Pre-merge validation**:
```python
def validate_merge(target, sources):
    """Validate merge before execution."""
    # Check same CHEBI ID
    assert all(s.chebi_id == target.chebi_id for s in sources)

    # Check same variant type
    target_variant = detect_variant_type(target.name)
    assert all(detect_variant_type(s.name) == target_variant for s in sources)

    # Check no conflicting roles
    all_roles = [s.media_roles for s in sources if s.media_roles]
    if all_roles:
        assert compatible_roles(all_roles)

    # Preview merge
    print_merge_preview(target, sources)
    return True
```

**Rollback mechanism**:
- Keep backup of pre-merge state
- Store merge_history in records
- Script to "unmerge" if needed

## Success Metrics

**Merge Phase**:
- [ ] Reduce ingredient count: 995 → ~500 unique
- [ ] Zero false positive merges
- [ ] All merged records have complete occurrence data
- [ ] Full audit trail preserved

**Hierarchy Phase**:
- [ ] 51 variant families with parent-child links
- [ ] Role inheritance working for 80%+ of variants
- [ ] Documentation of base chemicals vs variants

**Quality**:
- [ ] Expert review sign-off on agar variants
- [ ] Zero data loss
- [ ] Improved search/browse experience

## Tools & Scripts

**Created**:
- [x] `scripts/analyze_duplicates_and_variants.py` - Analysis tool
- [x] `analysis/duplicates_and_variants.yaml` - Findings report

**To Create**:
- [ ] `scripts/merge_duplicates.py` - Execute approved merges
- [ ] `scripts/build_hierarchies.py` - Build parent-child links
- [ ] `scripts/validate_hierarchy.py` - Check hierarchy consistency
- [ ] `.claude/skills/merge-ingredients/skill.md` - Interactive merge tool

## Next Steps

1. **Review this plan** - Adjust based on domain expertise
2. **Prioritize phases** - Merge first, hierarchy second, or both?
3. **Get expert input** - Especially for agar variants
4. **Start Phase A1** - Schema extensions + merge detection

## Questions for Domain Expert

1. **Agar variants**: Should "R2A agar" be separate from "agar"?
2. **Hydrate preferences**: Is MgSO4·7H2O preferred over MgSO4?
3. **Role inheritance**: Any exceptions to role inheritance for variants?
4. **Stereoisomer handling**: D-glucose vs glucose - which is parent?
