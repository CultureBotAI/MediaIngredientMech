# Claude Code Curation - Quick Start

Use me (Claude Code) directly for curation - no API costs, no setup!

## One-Time Setup

None! Just use the scripts.

## Quick Workflow

### 1. Prepare a Batch (30 seconds)

```bash
python scripts/prepare_for_claude_curation.py \
  --category SIMPLE_CHEMICAL \
  --limit 20 \
  --output notes/batch1.md
```

### 2. Ask Claude Code for Suggestions (2-3 minutes)

In your conversation with me, say:

```
Please analyze notes/batch1.md and suggest ontology mappings.
Provide in YAML format for apply_claude_suggestions.py.
```

I'll respond with:

```yaml
suggestions:
  - identifier: UNMAPPED_0003
    name: MgSO4•7H2O
    ontology_id: CHEBI:32599
    ontology_label: magnesium sulfate
    ontology_source: CHEBI
    confidence: 0.95
    quality: EXACT_MATCH
    reasoning: "Hydrate form maps to base chemical."
  # ... more
```

### 3. Save My Response (10 seconds)

Say:

```
Please save these suggestions to notes/batch1_suggestions.yaml
```

### 4. Apply Suggestions (30 seconds)

```bash
python scripts/apply_claude_suggestions.py \
  --suggestions notes/batch1_suggestions.yaml \
  --curator your_name
```

### 5. Validate (10 seconds)

```bash
just validate-all
```

**Done!** 20 ingredients curated in ~5 minutes.

## Full Example

```bash
# Prepare 3 batches
python scripts/prepare_for_claude_curation.py \
  --category SIMPLE_CHEMICAL --limit 20 --output notes/batch1.md

python scripts/prepare_for_claude_curation.py \
  --category UNKNOWN --limit 15 --output notes/batch2.md

python scripts/prepare_for_claude_curation.py \
  --category COMPLEX_MIXTURE --limit 10 --output notes/batch3.md

# For each batch:
# 1. Ask Claude Code: "Analyze notes/batchN.md and suggest mappings in YAML"
# 2. Save: "Save to notes/batchN_suggestions.yaml"
# 3. Apply: python scripts/apply_claude_suggestions.py --suggestions notes/batchN_suggestions.yaml

# Validate all
just validate-all
```

**Time:** ~20 minutes for 45 ingredients

**Cost:** $0 (free!)

## Tips

- **Batch size:** 10-20 per batch (easy to review)
- **Ask questions:** Discuss uncertain mappings with me
- **Iterative:** Don't accept all suggestions blindly
- **Validate often:** Run `just validate-all` after each batch

## See Full Guide

For detailed instructions: [CLAUDE_CODE_CURATION.md](../docs/CLAUDE_CODE_CURATION.md)
