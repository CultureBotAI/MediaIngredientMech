# Deduplication Script · Curation-Workflow Integration · Validation

*Reference for the **merge-ingredients** skill — see [`../skill.md`](../skill.md) for the overview, strategies, decision summary, and best practices.*

---

## Using the Deduplication Script

### Basic Usage

**Dry run (preview only)**:
```bash
python scripts/deduplicate_ingredients.py --dry-run
```

**CHEBI ID deduplication only**:
```bash
python scripts/deduplicate_ingredients.py --chebi-only
```

**Full deduplication (CHEBI + name matching)**:
```bash
python scripts/deduplicate_ingredients.py --include-name-matches
```

**With KG-Microbe search**:
```bash
python scripts/deduplicate_ingredients.py --search-kg-microbe
```

**Execute merges (no dry run)**:
```bash
python scripts/deduplicate_ingredients.py  # Removes --dry-run flag
```

### Advanced Options

**Custom thresholds**:
```bash
# Auto-merge confidence threshold
python scripts/deduplicate_ingredients.py --auto-merge-threshold 0.95

# Name matching threshold
python scripts/deduplicate_ingredients.py --name-match-threshold 0.85
```

**Custom data paths**:
```bash
python scripts/deduplicate_ingredients.py \
  --data-path data/custom/ingredients.yaml \
  --culturemech-path /path/to/culturemech/mapped_ingredients.yaml
```

### Output Interpretation

**Phase 1: CHEBI ID Deduplication**:
- Green panel: Successful merges executed
- Yellow panel: Records flagged for manual review
- Table: Shows merged records and their sources

**Phase 2: Name-Based Matching**:
- Blue panel: Potential duplicates found
- Table: Confidence scores and paired names
- Note: Requires manual review before merging

**Phase 3: KG-Microbe Reconciliation**:
- Magenta panel: CultureMech matches found
- Table: Sample matches with match types
- Statistics: CultureMech baseline summary

**Summary**:
- Initial vs final record count
- Reduction percentage
- Validation results

---

## Integration with Curation Workflow

### Interactive Curation Hook

**During curation** (`curate_unmapped.py`):
1. After accepting a mapping, check for duplicates
2. If duplicate CHEBI ID detected, prompt to merge
3. Show duplicate record details
4. Curator confirms or defers merge

**Example flow**:
```
[Curator maps ingredient to CHEBI:26710]
→ System detects existing record with CHEBI:26710
→ Prompt: "Merge with existing record 'NaCl'? [y/n]"
→ If yes: Merge immediately, continue curation
→ If no: Flag for later review
```

### Batch Curation Integration

**After batch mapping** (e.g., applying Claude suggestions):
1. Run deduplication script
2. Review flagged records
3. Execute merges
4. Re-run validation

**Workflow**:
```bash
# Apply batch suggestions
python scripts/apply_claude_suggestions.py batch1_suggestions.yaml

# Deduplicate
python scripts/deduplicate_ingredients.py --dry-run
python scripts/deduplicate_ingredients.py  # Execute

# Validate
python scripts/validate_mappings.py
```

### Periodic Maintenance

**Monthly/quarterly**:
1. Run full deduplication
2. Search KG-Microbe for new matches
3. Review flagged records
4. Update memory with patterns

**Checklist**:
- [ ] CHEBI ID duplicates resolved
- [ ] High-confidence name matches reviewed
- [ ] KG-Microbe reconciliation complete
- [ ] Validation passing
- [ ] Documentation updated

---

## Validation and Quality Checks

### Pre-Merge Validation

**Checks**:
1. **No circular dependencies**: A→B and B→A merges
2. **CHEBI ID exists**: Verify in ontology via OAK
3. **No data loss**: All synonyms preserved
4. **Occurrence totals**: Stats sum correctly

**Example**:
```python
# Before merge
validate_chebi_exists(target.ontology_id)
validate_no_cycles(target_idx, source_idx)
validate_synonym_preservation(target, source)
```

### Post-Merge Validation

**Checks**:
1. **Count reduction**: Record count decreased as expected
2. **No CHEBI duplicates**: validate_no_chebi_duplicates() passes
3. **REJECTED records**: All marked correctly
4. **Synonym uniqueness**: No duplicate synonyms in merged record

**Example**:
```python
is_valid, errors = chebi_dedup.validate_no_chebi_duplicates()
assert is_valid, f"Validation failed: {errors}"
```

### Audit Trail Validation

**Check curation_history**:
- Merge event recorded with timestamp
- Source indices documented
- Curator/action logged

**Example history entry**:
```yaml
curation_history:
  - timestamp: '2026-03-11T10:30:00Z'
    curator: deduplicate_ingredients
    action: MERGED
    changes: "Merged from indices [12, 45] - same CHEBI ID"
    previous_status: MAPPED
    new_status: MAPPED
    notes: "Auto-merge: same CHEBI + same quality"
```

---


---

## Best Practices

### 1. Always Start with Dry Run

**Why**: Preview changes before executing.

```bash
# Step 1: Dry run
python scripts/deduplicate_ingredients.py --dry-run

# Step 2: Review output

# Step 3: Execute if satisfied
python scripts/deduplicate_ingredients.py
```

### 2. CHEBI First, Names Second

**Order**:
1. Resolve CHEBI duplicates (high confidence)
2. Review name-based matches (requires judgment)
3. Search KG-Microbe (exploratory)

**Rationale**: CHEBI duplicates are non-negotiable. Name matches may require domain knowledge.

### 3. Validate After Every Merge

**Check**:
```bash
# Run deduplication
python scripts/deduplicate_ingredients.py

# Validate
python scripts/validate_mappings.py

# Check counts
python -c "
import yaml
data = yaml.safe_load(open('data/curated/unmapped_ingredients.yaml'))
print(f'Total: {data[\"total_count\"]}')
print(f'Mapped: {data[\"mapped_count\"]}')
print(f'Unmapped: {data[\"unmapped_count\"]}')
"
```

### 4. Document Flagged Records

**Create review log**:
```yaml
# data/curation/flagged_duplicates.yaml
flagged_duplicates:
  - chebi_id: CHEBI:32599
    records: [10, 25]
    reason: "Source has higher quality, needs review"
    reviewed_by: null
    resolution: null
  - chebi_id: CHEBI:26710
    records: [5, 12, 30]
    reason: "Three records with same CHEBI, conflicting evidence"
    reviewed_by: "curator_alice"
    resolution: "Merged 12→5, 30→5 after quality verification"
```

### 5. Preserve Original Terms

**Use synonyms liberally**:
- Add all variant names as synonyms
- Tag with source and type
- Include occurrence_count if available

**Example**:
```yaml
synonyms:
  - synonym_text: "MgSO4•7H2O"
    synonym_type: HYDRATE_FORM
    source: merge
    occurrence_count: 29
  - synonym_text: "Magnesium sulfate heptahydrate"
    synonym_type: EXACT_SYNONYM
    source: merge
    occurrence_count: 15
```

### 6. Periodic KG-Microbe Sync

**Monthly workflow**:
1. Export MediaIngredientMech to KGX format
2. Compare with CultureMech baseline
3. Identify discrepancies
4. Import missing high-frequency ingredients

```bash
# Export to KGX
python scripts/kgx_export.py

# Compare
python scripts/compare_with_culturemech.py

# Import missing
python scripts/import_from_culturemech.py --filter high-frequency
```

---
