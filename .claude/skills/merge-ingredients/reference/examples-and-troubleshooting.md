# Worked Examples & Troubleshooting

*Reference for the **merge-ingredients** skill — see [`../skill.md`](../skill.md) for the overview, strategies, decision summary, and best practices.*

---

## Examples and Scenarios

### Example 1: Simple CHEBI Duplicate

**Initial state**:
```yaml
# Record 1 (idx 5)
preferred_term: "NaCl"
ontology_id: CHEBI:26710
mapping_quality: EXACT_MATCH
occurrences: 6041

# Record 2 (idx 12)
preferred_term: "Sodium chloride"
ontology_id: CHEBI:26710
mapping_quality: SYNONYM_MATCH
occurrences: 150
```

**Action**:
```bash
python scripts/deduplicate_ingredients.py --chebi-only
```

**Result**:
```yaml
# Record 1 (idx 5) - MERGED TARGET
preferred_term: "NaCl"
synonyms:
  - synonym_text: "Sodium chloride"
    synonym_type: EXACT_SYNONYM
    source: merge
ontology_id: CHEBI:26710
mapping_quality: EXACT_MATCH  # Preserved higher quality
occurrences: 6191  # 6041 + 150

# Record 2 (idx 12) - REJECTED
mapping_status: REJECTED
```

### Example 2: Solution Name Matching

**Initial state**:
```yaml
# Record 1
preferred_term: "Trace metal solution"
ontology_id: CHEBI:XXXXX

# Record 2
preferred_term: "Trace elements solution"
ontology_id: CHEBI:YYYYY  # Different CHEBI
```

**Action**:
```bash
python scripts/deduplicate_ingredients.py --include-name-matches --name-match-threshold 0.8
```

**Result**:
```
Potential duplicates found:
- Confidence: 0.85
- Name 1: "Trace metal solution"
- Name 2: "Trace elements solution"
- Action: FLAGGED FOR REVIEW (different CHEBI IDs)
```

**Curator decision**: Review definitions, determine if same or distinct concepts.

### Example 3: KG-Microbe Reconciliation

**Initial state**:
```yaml
# MediaIngredientMech
preferred_term: "FeSO4"
ontology_id: CHEBI:75832
occurrences: 50
```

**Action**:
```bash
python scripts/deduplicate_ingredients.py --search-kg-microbe
```

**Result**:
```
CultureMech matches found:
- MediaIngredientMech: "FeSO4"
- Match type: CHEBI ID
- CultureMech records: 3

Details:
1. CultureMech "FeSO4" → 2000 occurrences in 500 media
2. CultureMech "Iron(II) sulfate" → 150 occurrences in 30 media
3. CultureMech "Ferrous sulfate" → 80 occurrences in 20 media
```

**Insight**: MediaIngredientMech count (50) << CultureMech count (2230 total). Suggests potential import or data alignment issue.

### Example 4: Conflict Resolution

**Initial state**:
```yaml
# Record 1 (idx 10)
preferred_term: "MgSO4"
ontology_id: CHEBI:32599
mapping_quality: SYNONYM_MATCH
occurrences: 100

# Record 2 (idx 25)
preferred_term: "Magnesium sulfate"
ontology_id: CHEBI:32599
mapping_quality: EXACT_MATCH  # Higher quality!
occurrences: 50
```

**Action**:
```bash
python scripts/deduplicate_ingredients.py --dry-run
```

**Result**:
```
FLAGGED FOR REVIEW:
- CHEBI:32599 (2 records)
- Reason: Source has higher quality (EXACT_MATCH > SYNONYM_MATCH), needs review
```

**Resolution**:
1. Manually review both records
2. Determine why source has higher quality
3. Options:
   - Swap target (make idx 25 the target)
   - Keep idx 10 as target but upgrade quality
   - Merge as-is with note

---

## Troubleshooting

### Issue 1: Merge Fails with "Cannot merge with itself"

**Cause**: Target and source indices are the same.

**Fix**: Check duplicate detection logic, ensure distinct indices.

### Issue 2: Validation Fails After Merge

**Cause**: CHEBI duplicates still detected.

**Symptoms**:
```
✗ Validation failed:
  - CHEBI:32599 still has 2 non-REJECTED records
```

**Fix**:
1. Check merge execution: Was dry-run flag used?
2. Verify source marked as REJECTED
3. Re-run deduplication without dry-run

### Issue 3: Name Match False Positives

**Cause**: Threshold too low or pattern mismatch.

**Symptoms**:
```
Flagged as duplicates:
- "Macro solution" vs "Micronutrient solution"
- Confidence: 0.72
```

**Fix**:
1. Increase threshold: `--name-match-threshold 0.85`
2. Review SolutionMatcher patterns
3. Add exclusion rules for known false positives

### Issue 4: KG-Microbe File Not Found

**Cause**: CultureMech path incorrect or file moved.

**Symptoms**:
```
CultureMech file not found: /path/to/culturemech/mapped_ingredients.yaml
```

**Fix**:
```bash
# Find correct path
find ~/Documents -name "mapped_ingredients.yaml" 2>/dev/null

# Update script argument
python scripts/deduplicate_ingredients.py \
  --culturemech-path /correct/path/mapped_ingredients.yaml \
  --search-kg-microbe
```

### Issue 5: Memory Error with Large Dataset

**Cause**: Loading 995 CultureMech records + processing.

**Fix**:
1. Increase memory limit (if container-based)
2. Process in batches:
   ```python
   for batch in chunks(records, 100):
       process_batch(batch)
   ```
3. Use generator-based loading for CultureMech data

---

