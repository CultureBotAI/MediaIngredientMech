# Matching Strategies in Detail (CHEBI merge · name matching · kg-microbe reconciliation)

*Reference for the **merge-ingredients** skill — see [`../skill.md`](../skill.md) for the overview, strategies, decision summary, and best practices.*

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

