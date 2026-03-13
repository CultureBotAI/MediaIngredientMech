# Merge Ingredients Skill

**Purpose**: Comprehensive guide for deduplicating and merging ingredient records in MediaIngredientMech

**Target users**: Curators, data maintainers, Claude Code agents

---

## Table of Contents

1. [Overview](#overview)
2. [Deduplication Strategies](#deduplication-strategies)
3. [CHEBI ID Merging (Primary Rule)](#chebi-id-merging-primary-rule)
4. [Name-Based Matching](#name-based-matching)
5. [KG-Microbe Reconciliation](#kg-microbe-reconciliation)
6. [Merge Decision Matrix](#merge-decision-matrix)
7. [Conflict Resolution](#conflict-resolution)
8. [Using the Deduplication Script](#using-the-deduplication-script)
9. [Integration with Curation Workflow](#integration-with-curation-workflow)
10. [Validation and Quality Checks](#validation-and-quality-checks)
11. [Examples and Scenarios](#examples-and-scenarios)
12. [Troubleshooting](#troubleshooting)
13. [Best Practices](#best-practices)
14. [API Reference](#api-reference)
15. [Advanced Usage](#advanced-usage)

---

## Overview

MediaIngredientMech maintains a non-redundant collection of ingredient records. Deduplication ensures:

- **No duplicate CHEBI IDs**: Multiple records mapping to the same ontology term must be merged
- **Consolidated solutions/buffers**: Similar named preparations are identified and consolidated
- **KG-Microbe alignment**: Reconciliation with CultureMech's 995 baseline ingredients
- **Data integrity**: All synonyms, occurrence statistics, and curation history preserved

**Key principles**:
- Primary merge rule: Same CHEBI ID → MUST merge
- Secondary matching: High-confidence name similarity for solutions/buffers/stocks
- Audit trail: All merges recorded in curation_history
- Quality preservation: Choose highest quality mapping as target

---

## Deduplication Strategies

### 1. CHEBI ID-Based Deduplication (Primary)

**Rule**: Records sharing the same CHEBI ID MUST be merged.

**Why**: Same CHEBI ID means identical chemical entity. Multiple records create:
- Inconsistent occurrence counts
- Split media associations
- Redundant curation effort

**Example**:
```yaml
# Record 1
preferred_term: "MgSO4"
ontology_mapping:
  ontology_id: CHEBI:32599
  ontology_label: "magnesium sulfate"

# Record 2
preferred_term: "Magnesium sulfate"
ontology_mapping:
  ontology_id: CHEBI:32599
  ontology_label: "magnesium sulfate"

# Result: Merge into single record, preserve both names as synonyms
```

### 2. Name-Based Matching (Secondary)

**Rule**: High-confidence name similarity (≥0.9) for solution/buffer/stock types.

**Why**: These ingredients often have:
- Variable naming conventions
- Type suffixes that differ ("solution" vs "stock")
- Concentration variations that should be consolidated

**Example**:
```yaml
# Record 1
preferred_term: "Trace metal solution"

# Record 2
preferred_term: "Trace elements solution"

# Result: Flag for review (high similarity but not identical)
```

### 3. KG-Microbe Reconciliation (Exploratory)

**Rule**: Search CultureMech baseline (995 ingredients) for potential matches.

**Why**: Identify:
- Ingredients already mapped in KG-Microbe
- Alternative names used in other media collections
- Potential imports to expand coverage

---

## CHEBI ID Merging (Primary Rule)

### Detection Algorithm

```python
# Pseudo-code
for each record:
    if record.ontology_mapping.ontology_id starts with "CHEBI:":
        group records by CHEBI ID

for each CHEBI ID with 2+ records:
    choose_merge_target()
    merge_sources_into_target()
```

### Target Selection Criteria

**Priority order**:
1. **Highest mapping quality**
   - EXACT_MATCH > SYNONYM_MATCH > CLOSE_MATCH > MANUAL_CURATION > LLM_ASSISTED > PROVISIONAL
2. **Highest occurrence count**
   - More widely used ingredient preserved as preferred_term
3. **Lowest index (oldest record)**
   - First imported record preferred as tiebreaker

**Example ranking**:
```
Record A: EXACT_MATCH, 100 occurrences → Score (5, 100, -0)
Record B: SYNONYM_MATCH, 150 occurrences → Score (4, 150, -1)
Record C: EXACT_MATCH, 80 occurrences → Score (5, 80, -2)

Winner: Record A (highest quality, even with fewer occurrences than B)
```

### Merge Process

**Steps**:
1. **Add source preferred_term as synonym to target**
   - Type: EXACT_SYNONYM
   - Source: "merge"
2. **Merge all synonyms from source to target**
   - Skip duplicates (normalized text comparison)
   - Preserve synonym metadata (type, source, occurrence_count)
3. **Combine occurrence statistics**
   - Add total_occurrences
   - Add media_count
   - Merge sample_media lists (deduplicate)
4. **Mark source as REJECTED**
   - Status: REJECTED
   - Preserves audit trail
5. **Rebuild search indices**

**Example merge**:
```yaml
# Before merge
Target (idx 5):
  preferred_term: "NaCl"
  ontology_id: CHEBI:26710
  occurrence_statistics:
    total_occurrences: 6041
    media_count: 1500

Source (idx 12):
  preferred_term: "Sodium chloride"
  ontology_id: CHEBI:26710
  occurrence_statistics:
    total_occurrences: 150
    media_count: 50

# After merge
Target (idx 5):
  preferred_term: "NaCl"
  synonyms:
    - synonym_text: "Sodium chloride"
      synonym_type: EXACT_SYNONYM
      source: merge
  ontology_id: CHEBI:26710
  occurrence_statistics:
    total_occurrences: 6191  # 6041 + 150
    media_count: 1550  # 1500 + 50

Source (idx 12):
  mapping_status: REJECTED  # Marked for filtering
```

### Auto-Merge Conditions

**Automatic merging (no confirmation needed)**:
- Same CHEBI ID + same mapping_quality
- Same CHEBI ID + target has higher quality
- Same CHEBI ID + source has PROVISIONAL quality

**Flag for review**:
- Same CHEBI ID but conflicting evidence (different sources, different confidence)
- One record has NEEDS_EXPERT status
- Source has higher quality than target (suggests curation error)

---

## Name-Based Matching

### Solution/Buffer/Stock Detection

**Patterns recognized**:
```python
PATTERNS = {
    'solution': r'(.+?)\s+solution$',
    'buffer': r'(.+?)\s+buffer$',
    'stock': r'(.+?)\s+stock(?:\s+solution)?$',
    'trace': r'trace\s+(elements?|metals?|solution)$',
    'macro': r'macro\s+(solution|nutrients?)$',
    'micro': r'micronutrients?\s+solution$',
    'vitamin': r'vitamin\s+(solution|mix|mixture)$',
    'mineral': r'mineral\s+(solution|mix|mixture)$',
}
```

**Base name extraction**:
```
"Trace metal solution" → "Trace metal"
"Macro solution" → "Macro"
"Vitamin mix" → "Vitamin"
"KH2PO4 buffer" → "KH2PO4"
```

### Confidence Scoring

**Scoring levels**:
- **1.0**: Exact normalized base name match + same type
- **0.9**: Same base chemical + same type category (solution/buffer/stock interchangeable)
- **0.8**: Same base chemical + different but compatible types
- **0.7**: Similar base name (token overlap > 0.8)
- **<0.7**: Token-based similarity (scaled)

**Examples**:
```
"Trace metal solution" vs "Trace metal buffer" → 0.9 (same base, compatible types)
"Trace metal solution" vs "Trace elements solution" → 0.7 (high token overlap)
"Macro solution" vs "Micronutrient solution" → 0.2 (low similarity)
```

### Concentration Normalization

**Unit normalization**:
```python
"10 mM KCl solution" → "10 mm kcl solution"
"1% NaCl buffer" → "1 pct nacl buffer"
"5 µM FeCl3" → "5 um fecl3"
"10x stock solution" → "10x stock solution"
```

**Purpose**: Ensure concentration variations don't prevent matching when appropriate.

---

## KG-Microbe Reconciliation

### CultureMech Data Structure

**Source**: `/CultureMech/output/mapped_ingredients.yaml` (995 mapped ingredients)

**Fields**:
```yaml
- preferred_term: "NaCl"
  ontology_id: CHEBI:26710
  ontology_label: "NaCl"
  ontology_source: CHEBI
  occurrence_count: 6041
  media_occurrences:
    - medium_name: "..."
      medium_category: BACTERIAL
      ingredient_index: 0
```

### Search Methods

**1. CHEBI ID search**:
```python
kg_searcher.search_by_chebi_id("CHEBI:26710")
# Returns all CultureMech records with this CHEBI ID
```

**2. Name-based search**:
```python
kg_searcher.search_by_name("sodium chloride", threshold=0.8)
# Returns [(record, score), ...] sorted by similarity
```

**3. Combined search**:
```python
kg_searcher.find_matches(ingredient_record)
# Returns {'chebi_matches': [...], 'name_matches': [...]}
```

### Use Cases

**1. Verify mapping consistency**:
- Check if MediaIngredientMech mapping matches CultureMech
- Identify discrepancies for expert review

**2. Import additional ingredients**:
- Find CultureMech ingredients not yet in MediaIngredientMech
- Bulk import common chemicals

**3. Media occurrence tracking**:
- Understand which media use each ingredient
- Prioritize curation based on usage frequency

---

## Merge Decision Matrix

### Decision Flow

```
┌─────────────────────────────────────┐
│ Check: Same CHEBI ID?               │
└─────────────┬───────────────────────┘
              │
         ┌────┴────┐
         │   YES   │
         └────┬────┘
              │
         ┌────▼────────────────────────────────┐
         │ Check: Same quality OR               │
         │        Target higher quality?        │
         └────┬────────────────────────────────┘
              │
         ┌────┴────┐
         │   YES   │───► AUTO-MERGE
         └────┬────┘
              │
              │ NO
              ▼
         FLAG FOR REVIEW
              │
              │
         ┌────┴────────────────────────────────┐
         │ Check: High name similarity (≥0.9)? │
         └────┬────────────────────────────────┘
              │
         ┌────┴────┐
         │   YES   │
         └────┬────┘
              │
         ┌────▼────────────────────────────────┐
         │ Check: Solution/buffer/stock type?  │
         └────┬────────────────────────────────┘
              │
         ┌────┴────┐
         │   YES   │───► FLAG FOR MANUAL REVIEW
         └─────────┘
```

### Auto-Merge Scenarios

| Condition | Action | Reason |
|-----------|--------|--------|
| Same CHEBI + same quality | MERGE | Identical mapping, safe to consolidate |
| Same CHEBI + target higher quality | MERGE | Higher quality target is authoritative |
| Exact normalized name (1.0) + same source | MERGE | Perfect string match, no ambiguity |

### Flag for Review

| Condition | Action | Reason |
|-----------|--------|--------|
| Same CHEBI + conflicting evidence | REVIEW | Different sources suggest uncertainty |
| Same CHEBI + one is NEEDS_EXPERT | REVIEW | Expert review required |
| Name similarity 0.7-0.9 | REVIEW | High but not perfect confidence |
| Different ontology sources | REVIEW | May represent different concepts |

### Never Merge

| Condition | Reason |
|-----------|--------|
| Different CHEBI IDs | Different chemical entities |
| Name similarity < 0.7 | Insufficient confidence |
| One record is REJECTED | Already merged/invalid |

---

## Conflict Resolution

### Scenario 1: Quality Conflict

**Problem**: Source has higher quality than target

**Example**:
```yaml
Target: SYNONYM_MATCH, 100 occurrences
Source: EXACT_MATCH, 50 occurrences
```

**Resolution**:
1. Flag for manual review
2. Curator decides: swap target or keep as-is
3. Document decision in curation_history

### Scenario 2: Evidence Conflict

**Problem**: Same CHEBI ID but different confidence scores

**Example**:
```yaml
Target: confidence_score: 0.98, evidence_type: CURATOR_JUDGMENT
Source: confidence_score: 0.75, evidence_type: LLM_SUGGESTION
```

**Resolution**:
1. Preserve highest confidence evidence
2. Merge other evidence as secondary
3. Note conflict in merge event

### Scenario 3: Name Mismatch

**Problem**: Same CHEBI ID but very different preferred_terms

**Example**:
```yaml
Target: "FeSO4"
Source: "Iron(II) sulfate heptahydrate"
CHEBI ID: CHEBI:75832 (both)
```

**Resolution**:
1. Keep target preferred_term (higher quality/occurrence)
2. Add source preferred_term as EXACT_SYNONYM
3. Note hydrate form in synonym metadata

### Scenario 4: NEEDS_EXPERT Status

**Problem**: One record flagged NEEDS_EXPERT

**Resolution**:
1. NEVER auto-merge
2. Flag for expert review before merging
3. Expert may:
   - Resolve mapping uncertainty
   - Approve merge with notes
   - Keep separate if truly distinct

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

## API Reference

### CHEBIDeduplicator

**Initialization**:
```python
from mediaingredientmech.curation.chebi_deduplicator import CHEBIDeduplicator
from mediaingredientmech.curation.ingredient_curator import IngredientCurator

curator = IngredientCurator(data_path="data/curated/unmapped_ingredients.yaml")
curator.load()

dedup = CHEBIDeduplicator(curator)
```

**Methods**:

#### `find_chebi_duplicates() -> dict[str, list[int]]`
Group record indices by shared CHEBI ID.

**Returns**: Dict mapping CHEBI ID to list of record indices (2+ records only).

**Example**:
```python
duplicates = dedup.find_chebi_duplicates()
# {'CHEBI:26710': [5, 12, 30], 'CHEBI:32599': [10, 25]}
```

#### `choose_merge_target(duplicate_group: list[int]) -> int`
Select best record as merge target.

**Args**:
- `duplicate_group`: List of record indices with same CHEBI ID

**Returns**: Index of merge target (highest quality, most occurrences).

**Example**:
```python
target = dedup.choose_merge_target([5, 12, 30])
# 5 (highest quality or most occurrences)
```

#### `should_auto_merge(target_idx: int, source_idx: int) -> tuple[bool, str]`
Determine if records should auto-merge.

**Args**:
- `target_idx`: Merge target record index
- `source_idx`: Source record index

**Returns**: Tuple of (should_merge, reason).

**Example**:
```python
can_merge, reason = dedup.should_auto_merge(5, 12)
# (True, "Same CHEBI ID + same quality (EXACT_MATCH)")
```

#### `merge_duplicates(dry_run: bool = True, auto_merge: bool = False) -> dict`
Find and merge all CHEBI duplicates.

**Args**:
- `dry_run`: Preview only, don't execute merges
- `auto_merge`: Automatically merge records passing auto-merge criteria

**Returns**: Dict with keys:
- `merged`: List of (target_idx, source_indices, chebi_id) tuples
- `flagged`: List of (chebi_id, indices, reason) tuples
- `total_removed`: Count of records marked REJECTED

**Example**:
```python
results = dedup.merge_duplicates(dry_run=False, auto_merge=True)
# {'merged': [(5, [12, 30], 'CHEBI:26710')], 'flagged': [], 'total_removed': 2}
```

#### `validate_no_chebi_duplicates() -> tuple[bool, list[str]]`
Validate no CHEBI duplicates remain.

**Returns**: Tuple of (is_valid, error_messages).

**Example**:
```python
is_valid, errors = dedup.validate_no_chebi_duplicates()
if not is_valid:
    print("Errors:", errors)
```

### SolutionMatcher

**Initialization**:
```python
from mediaingredientmech.curation.solution_matcher import SolutionMatcher

matcher = SolutionMatcher()
```

**Methods**:

#### `detect_type(name: str) -> str`
Detect ingredient type based on name patterns.

**Returns**: SOLUTION, BUFFER, STOCK, TRACE_METAL, MACRO, MICRO, VITAMIN, MINERAL, or CHEMICAL.

**Example**:
```python
matcher.detect_type("Trace metal solution")  # "TRACE_METAL"
matcher.detect_type("KH2PO4 buffer")  # "BUFFER"
matcher.detect_type("NaCl")  # "CHEMICAL"
```

#### `extract_base_name(name: str) -> str`
Extract base chemical name by stripping type suffix.

**Example**:
```python
matcher.extract_base_name("Trace metal solution")  # "Trace metal"
matcher.extract_base_name("KH2PO4 buffer")  # "KH2PO4"
```

#### `match_confidence(name1: str, name2: str) -> float`
Calculate similarity confidence for two names.

**Returns**: Score 0.0-1.0.

**Example**:
```python
matcher.match_confidence("Trace metal solution", "Trace metal buffer")  # 0.9
matcher.match_confidence("Macro solution", "Micronutrient solution")  # 0.2
```

#### `find_solution_duplicates(records: list[dict], threshold: float = 0.9) -> list[tuple[int, int, float]]`
Find potential duplicate solution/buffer/stock records.

**Returns**: List of (idx1, idx2, confidence) tuples.

**Example**:
```python
duplicates = matcher.find_solution_duplicates(curator.records, threshold=0.85)
# [(10, 25, 0.95), (15, 32, 0.87)]
```

### KGMicrobeSearcher

**Initialization**:
```python
from mediaingredientmech.utils.kg_microbe_searcher import KGMicrobeSearcher
from pathlib import Path

searcher = KGMicrobeSearcher(
    Path("/path/to/CultureMech/output/mapped_ingredients.yaml")
)
```

**Methods**:

#### `search_by_chebi_id(chebi_id: str) -> list[dict]`
Find CultureMech records with matching CHEBI ID.

**Example**:
```python
matches = searcher.search_by_chebi_id("CHEBI:26710")
# [{'preferred_term': 'NaCl', 'ontology_id': 'CHEBI:26710', ...}]
```

#### `search_by_name(name: str, threshold: float = 0.8) -> list[tuple[dict, float]]`
Fuzzy name search with similarity scores.

**Example**:
```python
matches = searcher.search_by_name("sodium chloride", threshold=0.7)
# [({'preferred_term': 'NaCl', ...}, 0.9), ...]
```

#### `find_matches(ingredient_record: dict) -> dict`
Find all potential matches for an ingredient record.

**Returns**: Dict with 'chebi_matches' and 'name_matches'.

**Example**:
```python
matches = searcher.find_matches(curator.records[5])
# {'chebi_matches': [...], 'name_matches': [...]}
```

#### `get_statistics() -> dict`
Get statistics about CultureMech data.

**Example**:
```python
stats = searcher.get_statistics()
# {'total_records': 995, 'unique_chebi_ids': 823, 'source_breakdown': {...}}
```

---

## Advanced Usage

### Custom Merge Logic

**Extend CHEBIDeduplicator**:
```python
class CustomDeduplicator(CHEBIDeduplicator):
    def choose_merge_target(self, duplicate_group: list[int]) -> int:
        # Custom logic: prefer records with more synonyms
        def score(idx):
            record = self.curator.records[idx]
            synonym_count = len(record.get('synonyms', []) or [])
            return (synonym_count, super().score_record(idx))

        return max(duplicate_group, key=score)
```

### Batch Processing

**Process multiple files**:
```python
import glob
from pathlib import Path

for file_path in glob.glob("data/batches/*.yaml"):
    curator = IngredientCurator(data_path=Path(file_path))
    curator.load()

    dedup = CHEBIDeduplicator(curator)
    results = dedup.merge_duplicates(dry_run=False)

    if results['merged']:
        curator.save()
        print(f"Processed {file_path}: {results['total_removed']} merged")
```

### Integration with CI/CD

**Pre-commit hook**:
```bash
#!/bin/bash
# .git/hooks/pre-commit

# Run deduplication check
python scripts/deduplicate_ingredients.py --dry-run > /tmp/dedup_check.txt

# Check for duplicates
if grep -q "Merged groups: [1-9]" /tmp/dedup_check.txt; then
    echo "ERROR: CHEBI duplicates detected. Run deduplication before committing."
    cat /tmp/dedup_check.txt
    exit 1
fi
```

### Automated Reconciliation

**Nightly sync**:
```python
import schedule
import time

def daily_reconciliation():
    # Run deduplication
    os.system("python scripts/deduplicate_ingredients.py")

    # Search KG-Microbe
    os.system("python scripts/deduplicate_ingredients.py --search-kg-microbe")

    # Send report
    send_email_report()

schedule.every().day.at("02:00").do(daily_reconciliation)

while True:
    schedule.run_pending()
    time.sleep(3600)
```

---

## Summary

This skill provides comprehensive deduplication capabilities for MediaIngredientMech:

**Key components**:
1. **CHEBIDeduplicator**: Primary merge rule (same CHEBI ID)
2. **SolutionMatcher**: Secondary matching (solution/buffer/stock names)
3. **KGMicrobeSearcher**: Reconciliation with CultureMech baseline
4. **deduplicate_ingredients.py**: Standalone script for automated workflow

**Usage pattern**:
1. Start with dry run
2. Review flagged records
3. Execute CHEBI merges
4. Manually review name matches
5. Validate results
6. Save and document

**Integration**:
- Interactive curation workflow
- Batch processing scripts
- Periodic maintenance tasks
- CI/CD validation hooks

For questions or issues, consult the troubleshooting section or review the API reference.
