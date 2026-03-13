# Claude Code Interactive Curation Guide

Use Claude Code (me!) directly for intelligent ontology mapping suggestions - no API costs, no API keys, fully interactive.

## Overview

Instead of using the Anthropic API, you can use Claude Code interactively to:
1. Analyze unmapped ingredients with full context
2. Suggest appropriate ontology mappings with reasoning
3. Apply accepted suggestions with full audit trail
4. Track all curation decisions with `llm_assisted: true` and `llm_model: claude-code-interactive`

**Benefits:**
- ✅ **Zero cost** - No API charges
- ✅ **No API key needed** - Works immediately
- ✅ **Interactive** - Review and discuss suggestions in real-time
- ✅ **Full reasoning** - Ask questions, get explanations
- ✅ **Flexible** - Accept, reject, or modify any suggestion
- ✅ **Complete audit trail** - All tracked as LLM-assisted

## Workflow

### Step 1: Prepare Ingredients for Analysis

Generate a formatted file with unmapped ingredients:

```bash
python scripts/prepare_for_claude_curation.py \
  --category SIMPLE_CHEMICAL \
  --limit 20 \
  --output notes/unmapped_batch1.md
```

**Options:**
- `--category` - Filter by category (SIMPLE_CHEMICAL, UNKNOWN, etc.)
- `--limit` - Number of ingredients to include
- `--output` - Where to save the formatted file

**Output:** A markdown file (`notes/unmapped_batch1.md`) with:
- Ingredient details (name, category, normalization, synonyms)
- Context for Claude Code
- Instructions for providing suggestions

### Step 2: Get Claude Code Suggestions

**Option A: Interactive conversation**

Simply say:
```
Please analyze the unmapped ingredients in notes/unmapped_batch1.md
and suggest ontology mappings for each one.
```

I'll review each ingredient and provide:
- Ontology ID (e.g., CHEBI:32599)
- Label (e.g., magnesium sulfate)
- Source (CHEBI/FOODON/ENVO)
- Confidence score (0.0-1.0)
- Reasoning
- Quality rating

**Option B: Batch YAML format**

Ask me to provide suggestions in YAML format for easy application:

```
Please analyze notes/unmapped_batch1.md and provide suggestions
in YAML format that can be used with apply_claude_suggestions.py
```

I'll generate:
```yaml
suggestions:
  - identifier: UNMAPPED_0003
    name: MgSO4•7H2O
    ontology_id: CHEBI:32599
    ontology_label: magnesium sulfate
    ontology_source: CHEBI
    confidence: 0.95
    quality: EXACT_MATCH
    reasoning: "Hydrate form of magnesium sulfate. Maps to base chemical in CHEBI."

  - identifier: UNMAPPED_0004
    name: NaNO
    ontology_id: CHEBI:75229
    ontology_label: sodium nitrate
    ontology_source: CHEBI
    confidence: 0.90
    quality: CLOSE_MATCH
    reasoning: "Incomplete formula corrected to NaNO3 (sodium nitrate)."
```

### Step 3: Review Suggestions

Review my suggestions:
- Check reasoning makes sense
- Verify confidence scores
- Ask questions about any uncertain mappings
- Request alternative suggestions if needed

**Example interaction:**
```
User: I'm not sure about the mapping for "Vitamin B" - which B vitamin is it?

Claude: Looking at the context, "Vitamin B" is too generic to map confidently.
I'd recommend:
- Check the original media recipes to see which B vitamin is actually used
- Mark as NEEDS_EXPERT for now
- Or if it appears in yeast extract media, it's likely B-complex (mixed)
```

### Step 4: Save Accepted Suggestions

Save my suggestions to a YAML file:

```yaml
# notes/claude_suggestions_batch1.yaml
suggestions:
  - identifier: UNMAPPED_0003
    name: MgSO4•7H2O
    ontology_id: CHEBI:32599
    ontology_label: magnesium sulfate
    ontology_source: CHEBI
    confidence: 0.95
    quality: EXACT_MATCH
    reasoning: "Hydrate form maps to base chemical."

  # ... more suggestions ...
```

### Step 5: Apply Suggestions

Apply the accepted suggestions to your database:

```bash
python scripts/apply_claude_suggestions.py \
  --suggestions notes/claude_suggestions_batch1.yaml \
  --curator marcin
```

**Options:**
- `--suggestions` - YAML file with suggestions (required)
- `--curator` - Your name for audit trail
- `--skip-validation` - Skip OAK validation (faster but less safe)
- `--dry-run` - Preview without saving

**Output:**
```
Applying Claude Code suggestions...

Loaded 20 suggestions

Application Results
┏━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━┓
┃ Identifier     ┃ Name              ┃ Mapping           ┃ Status    ┃
┡━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━┩
│ UNMAPPED_0003  │ MgSO4•7H2O        │ CHEBI:32599 (ma...│ ✓ Success │
│ UNMAPPED_0004  │ NaNO              │ CHEBI:75229 (so...│ ✓ Success │
│ UNMAPPED_0007  │ CaCl2•2H2O        │ CHEBI:3312 (cal...│ ✓ Success │
└────────────────┴───────────────────┴───────────────────┴───────────┘

Summary:
  Success: 18
  Failed: 2
  Total: 20

✓ Saved 18 mappings to data/curated/unmapped_ingredients.yaml
```

### Step 6: Validate

Validate all mappings:

```bash
just validate-all
```

## Example Session

### 1. Prepare batch

```bash
$ python scripts/prepare_for_claude_curation.py \
    --category SIMPLE_CHEMICAL \
    --limit 10 \
    --output notes/batch1.md

✓ Prepared file: notes/batch1.md

Next steps:
1. Review the file: notes/batch1.md
2. Ask Claude Code to analyze and suggest mappings
3. Use apply_claude_suggestions.py to apply accepted mappings
```

### 2. Ask Claude Code (me!)

**User:**
> Please analyze notes/batch1.md and suggest ontology mappings in YAML format

**Claude Code (me):**
> I'll analyze each ingredient and provide mapping suggestions. Let me read the file first.
>
> [reads file]
>
> Here are my suggestions in YAML format:
>
> ```yaml
> suggestions:
>   - identifier: UNMAPPED_0003
>     name: MgSO4•7H2O
>     ontology_id: CHEBI:32599
>     ontology_label: magnesium sulfate
>     ontology_source: CHEBI
>     confidence: 0.95
>     quality: EXACT_MATCH
>     reasoning: "Hydrate form of magnesium sulfate. Per curation guidelines, hydrates map to base chemical in CHEBI."
>
>   - identifier: UNMAPPED_0004
>     name: NaNO
>     ontology_id: CHEBI:75229
>     ontology_label: sodium nitrate
>     ontology_source: CHEBI
>     confidence: 0.90
>     quality: CLOSE_MATCH
>     reasoning: "Incomplete formula. Full formula is NaNO3 (sodium nitrate). Common media ingredient."
>
>   # ... more suggestions ...
> ```
>
> Would you like me to save this to a file, or would you like to discuss any of these mappings first?

### 3. Review and save

**User:**
> Yes, please save to notes/claude_batch1.yaml

**Claude Code:**
> [saves file]
>
> Saved to notes/claude_batch1.yaml. You can now apply these suggestions with:
>
> ```bash
> python scripts/apply_claude_suggestions.py \
>   --suggestions notes/claude_batch1.yaml \
>   --curator marcin
> ```

### 4. Apply

```bash
$ python scripts/apply_claude_suggestions.py \
    --suggestions notes/claude_batch1.yaml \
    --curator marcin

[applies suggestions with validation]

✓ Saved 10 mappings
```

## Conversation Templates

### Template 1: Simple Batch

```
Please analyze notes/unmapped_batch1.md and suggest CHEBI/FOODON
mappings for each ingredient. Provide in YAML format for
apply_claude_suggestions.py.

For each mapping include:
- Confidence score (0.0-1.0)
- Quality rating (EXACT_MATCH, SYNONYM_MATCH, CLOSE_MATCH, LLM_ASSISTED)
- Brief reasoning
```

### Template 2: Interactive Review

```
Please analyze notes/unmapped_batch1.md and suggest mappings.
For each ingredient, show:
1. Your suggested mapping
2. Confidence and reasoning
3. Alternative options if uncertain

Let's discuss any uncertain ones before I save them.
```

### Template 3: Specific Category

```
Please analyze the SIMPLE_CHEMICAL ingredients in
notes/unmapped_batch1.md and suggest CHEBI mappings.

Focus on:
- Hydrate forms (map to base chemical)
- Incomplete formulas (correct and map)
- Catalog variants (strip and map to base)

High confidence only (≥0.9) please.
```

### Template 4: Unknown Category

```
Please analyze the UNKNOWN ingredients in notes/unmapped_batch1.md.

For each, help determine:
1. Is it a simple chemical (CHEBI), biological material (FOODON), or environmental (ENVO)?
2. What's the correct ontology term?
3. How confident are you?

Flag any that need expert review.
```

## Advantages of Claude Code Approach

### vs. API Approach

| Feature | Claude Code | Anthropic API |
|---------|-------------|---------------|
| **Cost** | Free | ~$0.004/ingredient |
| **Setup** | None | API key required |
| **Interactive** | Yes | No |
| **Reasoning** | Discussion | Pre-formatted |
| **Flexibility** | High | Medium |
| **Batch size** | Any | Limited by $ |

### vs. Manual Approach

| Feature | Claude Code | Manual |
|---------|-------------|--------|
| **Speed** | Fast | Slow |
| **Reasoning** | Provided | Internal |
| **Consistency** | High | Varies |
| **Learning** | Yes | Yes |
| **Coverage** | Same | Same |

## Best Practices

### 1. Batch Size

**Optimal:** 10-20 ingredients per batch
- Small enough to review carefully
- Large enough to be efficient
- Easy to discuss uncertain cases

**Too large (>50):**
- Hard to review all suggestions
- May miss errors
- Overwhelming

### 2. Category-Based Batches

Process by category for better context:

```bash
# Batch 1: Simple chemicals (high success rate)
python scripts/prepare_for_claude_curation.py \
  --category SIMPLE_CHEMICAL \
  --limit 20 \
  --output notes/batch1_simple.md

# Batch 2: Unknown (medium complexity)
python scripts/prepare_for_claude_curation.py \
  --category UNKNOWN \
  --limit 15 \
  --output notes/batch2_unknown.md

# Batch 3: Complex mixtures (careful review)
python scripts/prepare_for_claude_curation.py \
  --category COMPLEX_MIXTURE \
  --limit 10 \
  --output notes/batch3_complex.md
```

### 3. Validation

Always validate after applying:

```bash
# Validate schema compliance
just validate-all

# Check mapping quality
python scripts/generate_report.py
```

### 4. Iterative Refinement

Don't accept all suggestions blindly:

1. Review my reasoning
2. Question uncertain mappings
3. Request alternatives
4. Discuss edge cases
5. Only save what you're confident in

### 5. Documentation

Keep a log of decisions:

```markdown
# Curation Log - Batch 1

Date: 2026-03-09
Curator: marcin
Category: SIMPLE_CHEMICAL
Suggestions: 20
Accepted: 18
Rejected: 2

Notes:
- Rejected "Vitamin B" - too generic, marked NEEDS_EXPERT
- Rejected "P-IV Metal Solution" - complex mixture, left UNMAPPED
- All hydrate forms mapped successfully
```

## Comparison: Three Curation Modes

### Mode 1: Fully Automated (Batch Tool)

**Use for:** Simple chemicals with clear normalization

```bash
python scripts/batch_curate_unmapped.py \
  --category SIMPLE_CHEMICAL \
  --auto-normalize \
  --min-confidence 0.9
```

**Pros:** Free, fast, no interaction needed
**Cons:** Limited reasoning, may miss edge cases

### Mode 2: Claude Code Assisted (This Guide)

**Use for:** Medium complexity, benefit from reasoning

```bash
# 1. Prepare
python scripts/prepare_for_claude_curation.py --limit 20

# 2. Ask Claude Code for suggestions (interactive)
# 3. Review and save to YAML
# 4. Apply
python scripts/apply_claude_suggestions.py --suggestions file.yaml
```

**Pros:** Free, reasoning provided, interactive discussion
**Cons:** Requires more interaction than batch

### Mode 3: Fully Manual

**Use for:** Complex, ambiguous, expert review needed

```bash
python scripts/curate_unmapped.py --curator marcin
```

**Pros:** Full control, deep review
**Cons:** Slowest, no automated reasoning

## Recommended Workflow

For the 112 unmapped ingredients:

```bash
# 1. Analyze all
python scripts/analyze_unmapped.py

# 2. Batch tool → Simple chemicals (45 items, ~10 min)
python scripts/batch_curate_unmapped.py \
  --category SIMPLE_CHEMICAL \
  --auto-normalize

# 3. Claude Code → Unknown (25 items, ~30 min)
python scripts/prepare_for_claude_curation.py \
  --category UNKNOWN \
  --output notes/unknown_batch.md

# Ask Claude Code for suggestions
# Apply with apply_claude_suggestions.py

# 4. Manual → Complex mixtures (34 items, ~45 min)
python scripts/curate_unmapped.py

# Total time: ~1.5 hours for all 112
# vs. ~4-5 hours all-manual
```

## Audit Trail

All Claude Code-assisted mappings are tracked:

```yaml
ontology_mapping:
  ontology_id: CHEBI:32599
  ontology_label: magnesium sulfate
  mapping_quality: EXACT_MATCH
  evidence:
    - evidence_type: LLM_SUGGESTION
      source: claude_code
      confidence_score: 0.95
      notes: "Claude Code reasoning: Hydrate form maps to base chemical."

curation_history:
  - timestamp: "2026-03-09T..."
    curator: marcin
    action: MAPPED
    llm_assisted: true
    llm_model: claude-code-interactive
    notes: "Claude Code reasoning: Hydrate form maps to base chemical."
```

**Queryable for:**
- Which mappings used Claude Code
- What reasoning was provided
- Confidence scores
- Quality analysis

## Tips

1. **Be specific in requests** - "Please analyze batch1.md and suggest CHEBI mappings with confidence ≥0.9"

2. **Ask for reasoning** - "Explain why you chose FOODON over CHEBI for this ingredient"

3. **Request alternatives** - "What other ontology terms could work for this?"

4. **Iterate** - "That seems wrong, can you reconsider?"

5. **Save incrementally** - Apply batches of 10-20, validate, then continue

6. **Document decisions** - Keep notes on why certain mappings were accepted/rejected

## See Also

- [UNMAPPED_CURATION.md](UNMAPPED_CURATION.md) - Overview of all curation tools
- [CURATION_GUIDE.md](CURATION_GUIDE.md) - General curation workflow
- [LLM_CURATION.md](LLM_CURATION.md) - API-based LLM curation (if you prefer)
