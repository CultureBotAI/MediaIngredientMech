# Decision Flow & Conflict Resolution

*Reference for the **merge-ingredients** skill — see [`../skill.md`](../skill.md) for the overview, strategies, decision summary, and best practices.*

---

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

