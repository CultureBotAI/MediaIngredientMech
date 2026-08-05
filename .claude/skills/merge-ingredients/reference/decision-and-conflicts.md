# Decision Flow & Conflict Resolution

*Reference for the **merge-ingredients** skill — see [`../SKILL.md`](../SKILL.md) for the overview, strategies, decision summary, and best practices.*

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

**Resolution**: ⚠️ **This is not a merge.** `FeSO4` and `Iron(II) sulfate
heptahydrate` are *different substances* — 151.91 vs 278.01 g/mol — that share a
CHEBI ID only because the hydrate was grounded onto its anhydrous parent. Merging
them destroys the distinction a recipe depends on. (CHEBI:75832 is one of the
records `just report-hydrate-grounding` currently flags.)

Per MAPPING_SEMANTICS.md **Section 3**, split them instead:

1. Keep the anhydrous record on the anhydrous term.
2. Give the hydrate its own identifier — a hydrate-specific ontology term if one
   exists, else `cas:<hydrate CAS>` with a `skos:narrowMatch` to the anhydrous
   parent plus the Rule B1 registry row.
3. `scripts/reground_mapped_record.py` performs the move.

Two records **do** merge when they are the same substance under different names
(`Glycerol`/`glycerol`, `Bacto X`/`Bacto X (Difco)`). A different hydration state
is not that case.

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

