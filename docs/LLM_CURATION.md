# LLM-Assisted Curation Guide

Use Claude API to get intelligent ontology mapping suggestions with reasoning for unmapped ingredients.

## Overview

The LLM-assisted curation tool uses Claude to:
1. Analyze ingredient names and context
2. Suggest the most appropriate ontology mapping (CHEBI, FOODON, or ENVO)
3. Provide confidence scores and reasoning
4. Validate suggestions against actual ontologies
5. Auto-accept high-confidence matches or present for review

**Benefits:**
- **Intelligent suggestions** - Claude understands chemical notation, biological materials, and context
- **Reasoning provided** - Know why each mapping was suggested
- **Validation** - All suggestions verified against actual ontology databases
- **Time savings** - Auto-accept high-confidence matches
- **Full audit trail** - All LLM usage tracked with model ID

## Setup

### 1. Install Anthropic SDK

```bash
pip install anthropic
```

### 2. Get API Key

Get your API key from: https://console.anthropic.com/

### 3. Set Environment Variable

```bash
export ANTHROPIC_API_KEY=your-api-key-here
```

**Make it permanent (add to ~/.bashrc or ~/.zshrc):**
```bash
echo 'export ANTHROPIC_API_KEY=your-api-key-here' >> ~/.bashrc
source ~/.bashrc
```

## Usage

### Basic Command

```bash
python scripts/llm_curate_unmapped.py
```

This will:
- Load all unmapped ingredients
- Process them one by one
- Get LLM suggestions
- Present for review and acceptance

### With Options

```bash
python scripts/llm_curate_unmapped.py \
  --category SIMPLE_CHEMICAL \
  --auto-accept-threshold 0.9 \
  --curator marcin \
  --limit 10
```

### All Options

| Option | Default | Description |
|--------|---------|-------------|
| `--data-path PATH` | `data/curated/unmapped_ingredients.yaml` | Path to unmapped ingredients |
| `--category CATEGORY` | All | Filter by category (SIMPLE_CHEMICAL, etc.) |
| `--auto-accept-threshold FLOAT` | 0.9 | Auto-accept if confidence ≥ threshold |
| `--model MODEL` | `claude-sonnet-4-20250514` | Claude model to use |
| `--curator NAME` | `llm_curator` | Curator name for audit trail |
| `--dry-run` | False | Test mode (no changes saved) |
| `--limit N` | None | Process only N ingredients |

## Example Session

```bash
$ python scripts/llm_curate_unmapped.py --category SIMPLE_CHEMICAL --limit 5

┌────────────────────────────────────┐
│ LLM-Assisted Curation Tool         │
│ Uses Claude API to suggest         │
│ ontology mappings with reasoning   │
└────────────────────────────────────┘

Processing 5 ingredients

─── Ingredient 1/5 ───

┌─ Unmapped Ingredient ──────────────┐
│ Name: MgSO4•7H2O                   │
│ ID: UNMAPPED_0003                  │
│ Occurrences: 29 across 29 media    │
└────────────────────────────────────┘

Normalized: MgSO4 (stripped_hydrate)
Category: SIMPLE_CHEMICAL

Consulting LLM for mapping suggestion...

LLM Suggestion

Ontology ID     CHEBI:32599
Label           magnesium sulfate
Source          CHEBI
Confidence      0.95
Status          ✓ Validated
Reasoning       Hydrate form of magnesium sulfate. Maps to base
                chemical in CHEBI per curation guidelines.
Alt. queries    magnesium sulfate, MgSO4, magnesium sulphate


High-confidence suggestion (0.95 ≥ 0.9)

Auto-accept this mapping? [Y/n]: y

✓ Mapped to CHEBI:32599 (magnesium sulfate)
Added 'MgSO4•7H2O' as synonym

─── Ingredient 2/5 ───
...
```

## How It Works

### 1. Contextual Prompting

The LLM receives:
- Ingredient name
- Normalized name (if applicable)
- Category (SIMPLE_CHEMICAL, etc.)
- Synonyms
- Occurrence count
- Normalization rules applied

**Example context:**
```
Ingredient name: MgSO4•7H2O
Category: SIMPLE_CHEMICAL
Occurrences: 29
Normalized name: MgSO4
Normalization applied: stripped_hydrate
```

### 2. LLM Analysis

Claude analyzes the ingredient and suggests:
- **Ontology ID** (e.g., CHEBI:32599)
- **Label** (e.g., "magnesium sulfate")
- **Source** (CHEBI, FOODON, or ENVO)
- **Confidence** (0.0-1.0)
- **Reasoning** (why this mapping is correct)
- **Alternative queries** (for manual verification)

### 3. Validation

Before presenting to curator:
- Verifies the ontology ID actually exists
- Checks the label matches
- Confirms it's in the correct ontology

**If validation fails:**
- Warning shown to curator
- Option to search manually
- Can still accept if curator agrees

### 4. Auto-Accept or Review

**High confidence (≥0.9) + validated:**
- Suggests auto-accept
- Shows mapping and reasoning
- Curator confirms with Y/n

**Lower confidence or failed validation:**
- Presents for review
- Options: Accept / Skip / Manual search / Quit

### 5. Recording

All accepted mappings track:
```yaml
ontology_mapping:
  ontology_id: CHEBI:32599
  ontology_label: magnesium sulfate
  mapping_quality: LLM_ASSISTED
  evidence:
    - evidence_type: LLM_SUGGESTION
      source: llm_curator
      confidence_score: 0.95
      notes: "LLM reasoning: Hydrate form of magnesium sulfate..."

curation_history:
  - action: MAPPED
    llm_assisted: true
    llm_model: claude-sonnet-4-20250514
```

## Confidence Scoring

The LLM assigns confidence based on:

| Range | Meaning | Action |
|-------|---------|--------|
| 0.9-1.0 | Exact match, unambiguous | Auto-accept (if enabled) |
| 0.7-0.89 | Strong match, minor ambiguity | Review recommended |
| 0.5-0.69 | Likely match, moderate ambiguity | Careful review |
| 0.0-0.49 | Uncertain, needs expert | Manual verification |

**Examples:**
- `MgSO4•7H2O` → CHEBI:32599 (magnesium sulfate): **0.95** - Exact chemistry, clear mapping
- `yeast extract` → FOODON:03301439: **0.95** - Exact match in FOODON
- `tryptone` → FOODON:03305413: **0.90** - Common biological material, well-known
- `Vitamin B` → Uncertain: **0.40** - Too generic, which B vitamin?

## Ontology Selection

Claude follows priority rules:

1. **CHEBI** (Chemical Entities of Biological Interest)
   - Simple chemicals: NaCl, glucose, ethanol
   - Salts and compounds: MgSO4, CaCl2
   - Organic molecules: amino acids, sugars

2. **FOODON** (Food Ontology)
   - Biological materials: yeast extract, tryptone
   - Complex mixtures: peptone, malt extract
   - Food-derived ingredients

3. **ENVO** (Environment Ontology)
   - Environmental samples: soil, seawater
   - Natural materials: sediment, groundwater

**Special cases:**
- Hydrates → base chemical in CHEBI (`MgSO4•7H2O` → `magnesium sulfate`)
- Catalog variants → base chemical (`NaCl (Fisher S271-500)` → `sodium chloride`)
- Biological extracts → FOODON, not CHEBI

## Interactive Actions

When presented with an LLM suggestion:

### Actions

- **`a`** - Accept the LLM suggestion
  - Choose quality rating (usually LLM_ASSISTED)
  - Mapping saved with full LLM tracking

- **`s`** - Skip to next ingredient
  - No changes made
  - Can return to it later

- **`m`** - Manual search
  - Ignore LLM suggestion
  - Search ontologies yourself
  - Useful if LLM missed something

- **`q`** - Quit and save
  - Saves all accepted mappings
  - Can resume later

## Dry Run Mode

Test LLM suggestions without making changes:

```bash
python scripts/llm_curate_unmapped.py \
  --dry-run \
  --limit 10
```

**Useful for:**
- Testing confidence thresholds
- Reviewing LLM quality
- Training/learning the tool
- Checking API connectivity

## Cost Estimation

**Claude Sonnet 4 pricing (as of 2025):**
- Input: ~$3 per million tokens
- Output: ~$15 per million tokens

**Per ingredient:**
- Input: ~500 tokens (prompt + context)
- Output: ~200 tokens (JSON response)
- **Cost: ~$0.004 per ingredient**

**For 100 ingredients:**
- Total cost: ~$0.40
- Time saved: ~2-3 hours vs manual curation

**ROI:** Highly cost-effective for large batches.

## Best Practices

### 1. Start with Simple Chemicals

```bash
python scripts/llm_curate_unmapped.py \
  --category SIMPLE_CHEMICAL \
  --auto-accept-threshold 0.9
```

LLM excels at simple chemicals. High auto-accept rate.

### 2. Review Complex Mixtures Carefully

```bash
python scripts/llm_curate_unmapped.py \
  --category COMPLEX_MIXTURE \
  --auto-accept-threshold 0.95  # Higher threshold
```

Complex mixtures need more scrutiny. Raise threshold or review all.

### 3. Use Dry Run First

```bash
python scripts/llm_curate_unmapped.py \
  --dry-run \
  --limit 20
```

Review LLM quality before committing changes.

### 4. Batch by Category

Process in phases:
1. SIMPLE_CHEMICAL (high success rate)
2. UNKNOWN (medium success rate)
3. COMPLEX_MIXTURE (careful review needed)

### 5. Validate After Curation

```bash
just validate-all
```

Ensure all LLM-suggested mappings pass schema validation.

## Troubleshooting

### API Key Not Set

```
Error: ANTHROPIC_API_KEY environment variable not set
```

**Fix:**
```bash
export ANTHROPIC_API_KEY=your-key-here
```

### API Key Invalid

```
LLM error: Invalid API key
```

**Fix:**
- Check key is correct
- Verify at https://console.anthropic.com/
- Regenerate if needed

### Validation Failures

```
✗ Validation failed: Term CHEBI:XXXXX not found
```

**Possible causes:**
- LLM hallucinated an ID
- Ontology database outdated
- Typo in ID

**Action:**
- Use manual search (`m`)
- Report if consistent issue

### Rate Limits

If you hit rate limits, the tool will show an error.

**Solutions:**
- Add delay between requests (feature to add)
- Use `--limit` to process in smaller batches
- Upgrade API tier if needed

## Comparison: LLM vs Manual vs Batch

| Feature | LLM-Assisted | Manual | Batch (Auto-Normalize) |
|---------|--------------|--------|------------------------|
| **Speed** | Fast | Slow | Very Fast |
| **Accuracy** | High | Highest | Medium-High |
| **Reasoning** | Provided | Manual | None |
| **Cost** | ~$0.004/item | Free | Free |
| **Best for** | Complex cases | Expert review | Simple chemicals |
| **Auto-accept** | Yes (0.9+) | N/A | Yes (0.9+) |

**Recommendation:**
- **Simple chemicals** → Batch tool (free, fast)
- **Medium complexity** → LLM-assisted (reasoning helps)
- **Complex/ambiguous** → Manual (expert judgment)
- **Large batches** → LLM with auto-accept

## Example: Full Workflow

```bash
# 1. Analyze unmapped ingredients
python scripts/analyze_unmapped.py

# 2. Curate simple chemicals with batch tool (free, fast)
python scripts/batch_curate_unmapped.py \
  --category SIMPLE_CHEMICAL \
  --auto-normalize \
  --curator marcin

# 3. Use LLM for remaining unknowns (intelligent suggestions)
python scripts/llm_curate_unmapped.py \
  --category UNKNOWN \
  --auto-accept-threshold 0.85 \
  --curator marcin

# 4. Manual review for complex mixtures
python scripts/curate_unmapped.py \
  --curator marcin

# 5. Validate all
just validate-all
```

## Audit Trail

Every LLM-assisted mapping is fully tracked:

```yaml
curation_history:
  - timestamp: "2026-03-09T..."
    curator: llm_curator
    action: MAPPED
    changes: "Mapped to CHEBI:32599 (magnesium sulfate)"
    previous_status: UNMAPPED
    new_status: MAPPED
    llm_assisted: true
    llm_model: claude-sonnet-4-20250514
    notes: "LLM reasoning: Hydrate form of magnesium sulfate. Maps to base chemical in CHEBI per curation guidelines."
```

**Queryable:**
- Which mappings used LLM?
- What was the LLM's reasoning?
- What model was used?
- What confidence score?

## See Also

- [UNMAPPED_CURATION.md](UNMAPPED_CURATION.md) - General unmapped curation workflow
- [CURATION_GUIDE.md](CURATION_GUIDE.md) - Manual curation guide
- [Anthropic API Documentation](https://docs.anthropic.com/) - Claude API reference
