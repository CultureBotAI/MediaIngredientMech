# Curation Guide

Step-by-step guide for curating media ingredient ontology mappings in MediaIngredientMech.

## Prerequisites

- MediaIngredientMech installed (`just install`)
- Data imported from CultureMech (`just import-data`)
- Familiarity with CHEBI and FOODON ontologies

## Curation Workflow Overview

```
Import Data -> Snapshot -> Curate -> Validate -> Report -> Export
```

1. Import ingredients from CultureMech
2. Create a snapshot before making changes
3. Curate unmapped ingredients using the interactive CLI
4. Validate all mappings against the schema and ontology
5. Generate a progress report
6. Export validated mappings back to CultureMech

## Using the Interactive CLI

Launch the curation CLI:

```bash
just curate
```

This runs `scripts/curate_unmapped.py`, which presents unmapped ingredients sorted by occurrence count (most frequent first). For each ingredient, you can:

- **Map** it to a CHEBI or FOODON term
- **Skip** it to come back later
- **Mark** it as NEEDS_EXPERT or AMBIGUOUS
- **Add synonyms** from raw text variants
- **Add notes** for context

### Example Session

```
=== Ingredient 1/136: "yeast extract" (occurs in 847 media) ===
Synonyms found: Yeast Extract, YEAST EXTRACT, yeast-extract

Suggested mappings:
  1. CHEBI:27150  yeast extract  (confidence: 0.95)
  2. FOODON:03301439  yeast extract  (confidence: 0.90)

Action [map/skip/expert/ambiguous/notes/quit]: map
Select mapping [1-2]: 1
Quality [EXACT_MATCH/CLOSE_MATCH/SYNONYM_MATCH]: EXACT_MATCH
LLM assisted? [y/n]: n

Mapped "yeast extract" -> CHEBI:27150 (EXACT_MATCH)
```

## Mapping Quality Standards

Choose the appropriate quality rating for each mapping:

| Quality | When to Use | Example |
|---------|------------|---------|
| EXACT_MATCH | Ingredient name matches ontology term label exactly | "sodium chloride" -> CHEBI:26710 "sodium chloride" |
| SYNONYM_MATCH | Ingredient matches a known synonym in the ontology | "NaCl" -> CHEBI:26710 (synonym of sodium chloride) |
| CLOSE_MATCH | Semantically close but not an exact or synonym match | "peptone" -> CHEBI:73329 (closest available term) |
| MANUAL_CURATION | Expert curator made a judgment call | Complex ingredients requiring domain expertise |
| LLM_ASSISTED | LLM suggested the mapping, human verified it | Any mapping where LLM provided the candidate |
| PROVISIONAL | Tentative mapping that needs further verification | Uncertain mappings flagged for later review |

### Decision Tree

```
Is the ingredient name identical to the ontology label?
  YES -> EXACT_MATCH
  NO -> Is it a known synonym in the ontology?
    YES -> SYNONYM_MATCH
    NO -> Is the meaning clearly the same concept?
      YES -> CLOSE_MATCH
      NO -> Was expert judgment required?
        YES -> MANUAL_CURATION
        NO -> Mark as PROVISIONAL or AMBIGUOUS
```

## When to Use NEEDS_EXPERT vs AMBIGUOUS

### NEEDS_EXPERT

Use when the ingredient requires specialized knowledge to map correctly:

- Complex chemical mixtures (e.g., "trace element solution SL-10")
- Domain-specific formulations (e.g., "Wolfe's vitamin solution")
- Ingredients where the correct ontology term is unclear without expertise
- Cases where multiple ontologies could apply

### AMBIGUOUS

Use when the ingredient text itself is unclear or has multiple interpretations:

- Vague names (e.g., "extract", "salt", "acid")
- Ingredients that could refer to different substances depending on context
- Abbreviated or truncated names that lack specificity
- Names with spelling errors that could map to different terms

### Comparison

| Scenario | Status | Reason |
|----------|--------|--------|
| "Wolfe's mineral elixir" | NEEDS_EXPERT | Known formulation, needs expert to identify components |
| "extract" | AMBIGUOUS | Could be yeast extract, meat extract, plant extract, etc. |
| "SL-7 trace elements" | NEEDS_EXPERT | Specific formulation requiring domain knowledge |
| "salt" | AMBIGUOUS | Could be NaCl, any mineral salt, or a salt mixture |

## LLM-Assisted Curation

When using LLM assistance for mapping suggestions:

1. **Record it**: Always set `llm_assisted: true` on the CurationEvent
2. **Record the model**: Set `llm_model` to the model identifier (e.g., "claude-sonnet-4-5")
3. **Verify**: Never accept LLM suggestions without human verification
4. **Quality rating**: Use `LLM_ASSISTED` as the mapping quality when the LLM provided the candidate
5. **Evidence**: Add a MappingEvidence entry with `evidence_type: LLM_SUGGESTION`

### Best Practices

- Use LLM suggestions as a starting point, not a final answer
- Cross-reference LLM suggestions against OLS (Ontology Lookup Service) or OAK
- For high-confidence LLM matches (>0.9), verify the ontology term exists and is not obsolete
- For lower-confidence matches, search the ontology manually before accepting
- Document the LLM's reasoning in the evidence notes field

### Example Curation Event with LLM Assistance

```yaml
curation_history:
  - timestamp: "2026-03-06T10:30:00"
    curator: "jsmith"
    action: MAPPED
    changes: "Added CHEBI mapping based on LLM suggestion"
    previous_status: UNMAPPED
    new_status: MAPPED
    llm_assisted: true
    llm_model: "claude-sonnet-4-5"
    notes: "LLM suggested CHEBI:27150 with 0.95 confidence, verified in OLS"
```

## Complete Example: Unmapped to Mapped

This example walks through curating "yeast extract" from unmapped to fully mapped.

### Step 1: Create a Snapshot

```bash
just snapshot
# Output: Snapshot created: data/snapshots/20260306_103000
```

### Step 2: Launch Curation

```bash
just curate
```

### Step 3: Review the Ingredient

The CLI shows the ingredient details:
- Name: "yeast extract"
- Occurrences: 847 media recipes
- Raw text variants: "Yeast Extract", "YEAST EXTRACT", "yeast-extract"

### Step 4: Select a Mapping

Choose CHEBI:27150 (yeast extract) as an EXACT_MATCH.

### Step 5: Add Synonyms

The raw text variants are automatically added as synonyms with type RAW_TEXT.

### Step 6: Validate

```bash
just validate-all
# Output: Validated 1,131 records. 0 errors, 0 warnings.
```

### Step 7: Check Progress

```bash
just report
# Output: Mapped: 996/1131 (88.1%), Unmapped: 135
```

### Resulting Record

```yaml
identifier: CHEBI:27150
preferred_term: yeast extract
mapping_status: MAPPED
ontology_mapping:
  ontology_id: CHEBI:27150
  ontology_label: yeast extract
  ontology_source: CHEBI
  mapping_quality: EXACT_MATCH
  evidence:
    - evidence_type: DATABASE_MATCH
      source: OLS
      confidence_score: 0.95
      notes: "Direct match in CHEBI"
synonyms:
  - synonym_text: "Yeast Extract"
    synonym_type: RAW_TEXT
    source: CultureMech
    occurrence_count: 500
  - synonym_text: "YEAST EXTRACT"
    synonym_type: RAW_TEXT
    source: CultureMech
    occurrence_count: 200
  - synonym_text: "yeast-extract"
    synonym_type: RAW_TEXT
    source: CultureMech
    occurrence_count: 147
occurrence_statistics:
  total_occurrences: 847
  media_count: 847
  sample_media:
    - "Luria-Bertani Medium"
    - "Tryptic Soy Broth"
curation_history:
  - timestamp: "2026-03-06T10:30:00"
    curator: "jsmith"
    action: MAPPED
    changes: "Mapped to CHEBI:27150 yeast extract"
    previous_status: UNMAPPED
    new_status: MAPPED
    llm_assisted: false
    notes: "Exact match confirmed in OLS"
```

## Tips

- **Curate by frequency**: The CLI sorts by occurrence count. Mapping the most frequent ingredients first maximizes impact.
- **Batch similar ingredients**: If you see related ingredients (e.g., "NaCl", "sodium chloride", "salt (NaCl)"), curate them together and add cross-references as synonyms.
- **Use snapshots liberally**: Create a snapshot before each curation session. They are cheap and provide easy rollback.
- **Validate often**: Run `just validate-all` after each batch of changes to catch errors early.
- **Add notes**: When in doubt, add notes explaining your reasoning. Future curators will thank you.

## Related Documentation

- [Schema Reference](SCHEMA_REFERENCE.md) - Detailed class and field documentation
- [Workflows](WORKFLOWS.md) - Common operations and CultureMech integration
