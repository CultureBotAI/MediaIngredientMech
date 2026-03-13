---
name: map-media-ingredients
description: Map media ingredient names to ontology terms (CHEBI/FOODON/ENVO) using exact, normalized, and fuzzy matching strategies
category: workflow
requires_database: false
requires_internet: true
version: 1.0.0
---

# Media Ingredient Ontology Mapping

## Overview

**Purpose**: Map microbial growth media ingredient names to authoritative ontology terms for semantic integration and knowledge graph construction.

**Why**: Ensures consistency across datasets, enables semantic queries, links to external knowledge bases (KG-Microbe, CHEBI, FOODON, ENVO), and supports cross-study analysis.

**Scope**: Chemical compounds (salts, organics), biological materials (extracts, peptones), environmental samples (soil, seawater).

## When to Use This Skill

Use this skill when:
- Adding new ingredients to MediaIngredientMech database
- Curating unmapped ingredients from media formulations
- Validating existing ontology mappings
- Integrating media data with KG-Microbe knowledge graph
- Normalizing chemical names with hydrates, catalog codes, or incomplete formulas
- Deciding which ontology (CHEBI vs FOODON vs ENVO) to use

## Ontology Selection Guide

| Ingredient Type | Primary Ontology | Examples | When to Use |
|----------------|------------------|----------|-------------|
| Simple chemicals | CHEBI | NaCl, glucose, MgSO4•7H2O, K2HPO4 | Pure chemical compounds, salts, ions |
| Biological materials | FOODON | yeast extract, peptone, tryptone, beef extract | Biological preparations, food-derived |
| Environmental samples | ENVO | soil extract, seawater, sediment | Natural environmental materials |
| Complex mixtures | May be unmappable | "Vitamin solution A", "Trace metals" | Often too generic for specific mapping |

**Ontology priority order**: CHEBI → FOODON → ENVO

Try the most specific ontology first. If no match, try broader ontologies.

## Chemical Normalization Rules

Many ingredient names require normalization before ontology matching. The `chemical_normalizer.py` utility handles common patterns:

### 1. Hydrate Notation Stripping

**Pattern**: Remove hydration notation (•, ·, .) and water count
- `MgSO4•7H2O` → `MgSO4` → search as "magnesium sulfate"
- `CaCl2·2H2O` → `CaCl2` → search as "calcium chloride"
- `FeSO4.7H2O` → `FeSO4` → search as "ferrous sulfate"
- `Na2HPO4 dihydrate` → `Na2HPO4` → search as "disodium phosphate"

**Synonym preservation**: Original hydrate form is saved as synonym with type `HYDRATE_FORM`

### 2. Incomplete Formula Correction

**Pattern**: Add missing atoms to common incomplete formulas
- `K2HPO` → `K2HPO4` → "dipotassium phosphate"
- `Na2HPO` → `Na2HPO4` → "disodium phosphate"
- `NaHPO` → `NaH2PO4` → "sodium dihydrogen phosphate"

**Synonym preservation**: Incomplete form saved as `INCOMPLETE_FORMULA` synonym

### 3. Catalog Number Removal

**Pattern**: Strip supplier/catalog information
- `NaCl (Fisher S271-500)` → `NaCl` → "sodium chloride"
- `Glucose (Sigma G7021)` → `Glucose` → "glucose"
- `Agar (BD 214010)` → `Agar` → "agar"

**Synonym preservation**: Catalog variant saved as `CATALOG_VARIANT` synonym

### 4. Abbreviation Expansion

**Pattern**: Expand common abbreviations to full names
- `dH2O` → `distilled water` → "water"
- `NaOAc` → `sodium acetate`
- `KOAc` → `potassium acetate`

### 5. Formula to Common Name

**Built-in mappings** for common chemical formulas:
```python
FORMULA_TO_NAME = {
    'NaCl': 'sodium chloride',
    'MgSO4': 'magnesium sulfate',
    'CaCl2': 'calcium chloride',
    'KCl': 'potassium chloride',
    'K2HPO4': 'dipotassium phosphate',
    # ... 40+ common chemicals
}
```

## Matching Strategies

### Level 1: Exact Match

Direct string match with ontology labels (case-insensitive).

**Using OAK** (Ontology Access Kit):
```python
from oaklib import get_adapter

# Search CHEBI
adapter = get_adapter("sqlite:obo:chebi")
results = adapter.basic_search("sodium chloride")

for entity_id in results:
    label = adapter.label(entity_id)
    print(f"{entity_id}: {label}")
# Output: CHEBI:26710: sodium chloride
```

**Using OntologyClient**:
```python
from mediaingredientmech.utils.ontology_client import OntologyClient

client = OntologyClient()
results = client.search("glucose", sources=["CHEBI"])

for candidate in results:
    print(f"{candidate.ontology_id}: {candidate.label} (score: {candidate.score})")
```

### Level 2: Normalized Match

Apply chemical normalization, then search with all variants.

**Using chemical_normalizer**:
```python
from mediaingredientmech.utils.chemical_normalizer import (
    normalize_chemical_name,
    generate_search_variants
)

# Normalize
result = normalize_chemical_name("MgSO4•7H2O")
print(f"Original: {result.original}")
print(f"Normalized: {result.normalized}")
print(f"Variants: {result.variants}")
# Variants: ['magnesium sulfate', 'MgSO4', 'magnesium sulphate']

# Search with all variants
client = OntologyClient()
matches = client.search_with_variants(result.variants, sources=["CHEBI"])
```

**Multi-variant search** (deduplicates results, keeps best scores):
```python
# Generate comprehensive search variants
variants = generate_search_variants("MgSO4•7H2O")
# Returns: ['MgSO4•7H2O', 'MgSO4', 'magnesium sulfate', 'magnesium sulphate']

# Search with all variants, deduplicate results
results = client.search_with_variants(variants, sources=["CHEBI"], max_results=10)
```

### Level 3: Fuzzy Match

Use fuzzy/lexical search for synonym matching and spelling variations.

**Using OAK fuzzy search**:
```bash
# Lexical search (prefix: l~)
uv run runoak -i sqlite:obo:chebi info "l~magnesium sulphate"

# Search with synonyms
uv run runoak -i sqlite:obo:chebi search "magnesium sulfate"
```

**Using EBI OLS API** (web-based, requires internet):
```bash
# Basic search
curl "https://www.ebi.ac.uk/ols4/api/search?q=magnesium%20sulfate&ontology=chebi"

# Python wrapper
import requests

def ols_search(query, ontology="chebi"):
    url = "https://www.ebi.ac.uk/ols4/api/search"
    params = {"q": query, "ontology": ontology}
    response = requests.get(url, params=params)
    return response.json()

results = ols_search("magnesium sulfate", "chebi")
for doc in results['response']['docs']:
    print(f"{doc['obo_id']}: {doc['label']}")
```

**When to use OLS vs OAK**:
- **OAK** (primary): Faster, works offline, integrated with curation scripts
- **OLS** (secondary): Cross-validation, broader coverage, web-based exploration

### Level 4: Manual Curation

When automated matching fails, manual expert curation is required.

**Use manual curation when**:
- Complex mixtures ("Vitamin solution A", "Trace metal mix")
- Generic/incomplete terms ("See source", "Mineral salts")
- Ambiguous names requiring context
- Novel/proprietary formulations

## KG-Microbe Integration

MediaIngredientMech integrates with **CultureMech** (primary integration point) for KG-Microbe knowledge graph construction.

### Data Flow

```
CultureMech → MediaIngredientMech (curate) → Export back to CultureMech
```

### Import from CultureMech

```bash
# Import ingredients from CultureMech
python scripts/import_from_culturemech.py \
  --culturemech-dir /path/to/CultureMech/data \
  --output data/ingredients
```

### Export to CultureMech

```bash
# Export curated mappings back
python scripts/export_to_culturemech.py \
  --input data/ingredients/mapped \
  --output /path/to/CultureMech/data/ingredients
```

### Check Existing Ingredients

Before creating new mappings, check if ingredient already exists in KG-Microbe:

```python
# Search for existing ingredient entities
# Pattern: mediadive.ingredient:*
# Check media_dive_ingredients in CultureMech data

# If found, use existing ID instead of creating duplicate
```

### Link to Media and Organisms

Ingredients in KG-Microbe are linked via:
- **has_part**: Medium → Ingredient relationships
- **Growth requirements**: Organism → Medium → Ingredients
- **Frequency analysis**: How often ingredient appears across media

## Workflows

### Workflow A: Interactive Single Ingredient

For one-off ingredient mapping with manual review:

```bash
# Interactive curation with GUI
python scripts/curate_unmapped.py

# Shows:
# - Original name and normalized variants
# - Top candidates from each ontology
# - Context (how many media use this ingredient)
# - Accept, skip, or mark for expert review
```

**Process**:
1. Tool normalizes the name
2. Generates search variants
3. Searches CHEBI, then FOODON, then ENVO
4. Presents top candidates with scores
5. User accepts mapping or marks NEEDS_EXPERT

### Workflow B: Batch Curation

For auto-curable simple chemicals with high confidence:

```bash
# Analyze unmapped ingredients first
python scripts/analyze_unmapped.py

# Batch curate simple chemicals
python scripts/batch_curate_unmapped.py \
  --category SIMPLE_CHEMICAL \
  --auto-normalize \
  --min-confidence 0.9 \
  --dry-run

# Review dry-run results, then apply
python scripts/batch_curate_unmapped.py \
  --category SIMPLE_CHEMICAL \
  --auto-normalize \
  --min-confidence 0.9
```

**Best for**:
- SIMPLE_CHEMICAL category (salts, common organics)
- Ingredients with clear normalization patterns
- High-confidence matches (score ≥ 0.9)

**Features**:
- Auto-normalization with synonym preservation
- Multi-variant search with deduplication
- Dry-run mode for safety
- Automatic provenance tracking

### Workflow C: Claude Code-Assisted Curation

For complex ingredients requiring LLM reasoning (zero-cost, no API):

**Step 1: Prepare batch**
```bash
# Prepare ingredients for Claude Code review
python scripts/prepare_for_claude_curation.py \
  --category UNKNOWN \
  --limit 20 \
  --output notes/batch_001.md
```

This creates a markdown file with:
- Ingredient names with context
- Category and normalization info
- Search variants
- Instructions for Claude Code

**Step 2: Ask Claude Code**
```
Open notes/batch_001.md and ask Claude Code:
"Please analyze these ingredients and suggest ontology mappings"
```

Claude Code will:
- Analyze each ingredient
- Apply normalization patterns
- Search relevant ontologies
- Provide structured suggestions with reasoning
- Output YAML with mappings

**Step 3: Apply suggestions**
```bash
# Apply Claude Code suggestions
python scripts/apply_claude_suggestions.py \
  --suggestions notes/batch_001_suggestions.yaml \
  --validate

# Validation checks:
# - Term exists in specified ontology
# - Confidence score is reasonable
# - Quality level is appropriate
```

**Benefits**:
- Zero-cost (uses Claude Code, no API tokens)
- Full reasoning and audit trail
- Handles ambiguous cases
- Batch processing efficiency

**See**: `docs/CLAUDE_CODE_CURATION.md` for detailed guide

## Examples

### Example 1: Simple Chemical with Hydrate

**Input**: `MgSO4•7H2O`

**Process**:
1. Normalize: Strip hydrate → `MgSO4`
2. Map formula to name: `MgSO4` → `magnesium sulfate`
3. Generate variants: `['MgSO4', 'magnesium sulfate', 'magnesium sulphate']`
4. Search CHEBI: Find `CHEBI:32599` (magnesium sulfate)
5. Accept with quality `EXACT_MATCH`
6. Save original `MgSO4•7H2O` as synonym type `HYDRATE_FORM`

**Result**:
```yaml
ontology_id: CHEBI:32599
ontology_label: magnesium sulfate
ontology_source: CHEBI
quality: EXACT_MATCH
synonyms:
  - name: MgSO4•7H2O
    type: HYDRATE_FORM
```

### Example 2: Incomplete Formula

**Input**: `K2HPO`

**Process**:
1. Normalize: Fix incomplete formula → `K2HPO4`
2. Map to name: `K2HPO4` → `dipotassium phosphate`
3. Search CHEBI: Find `CHEBI:131527`
4. Accept with quality `SYNONYM_MATCH`
5. Save `K2HPO` as synonym type `INCOMPLETE_FORMULA`

### Example 3: Biological Extract

**Input**: `Yeast extract`

**Process**:
1. No chemical normalization needed
2. Search CHEBI: No good match
3. Search FOODON: Find `FOODON:03411448` (yeast extract)
4. Accept with quality `EXACT_MATCH`

**Why FOODON?** Yeast extract is a biological preparation, not a pure chemical compound.

### Example 4: Environmental Sample

**Input**: `Soil extract`

**Process**:
1. Search CHEBI: No match
2. Search FOODON: No specific match
3. Search ENVO: Find `ENVO:02000034` (soil extract)
4. Accept with quality `EXACT_MATCH`

### Example 5: Complex Mixture (Unmappable)

**Input**: `Vitamin solution A (per source)`

**Process**:
1. Categorize as `COMPLEX_MIXTURE`
2. Search fails: Too generic, composition varies
3. Mark as **unmappable** with status `NEEDS_EXPERT`
4. Rationale: Composition not specified, varies by source

**Best practice**: Document in notes that this should reference source formulation.

## Quality Guidelines

Curation quality levels indicate match confidence:

| Quality Level | Meaning | When to Use |
|--------------|---------|-------------|
| `EXACT_MATCH` | String matches ontology label exactly | "glucose" → "glucose" (CHEBI:17234) |
| `SYNONYM_MATCH` | Matches known synonym in ontology | "sulphate" in ontology synonyms |
| `CLOSE_MATCH` | Semantically equivalent, different phrasing | "dipotassium phosphate" ≈ "potassium phosphate dibasic" |
| `MANUAL_CURATION` | Expert judgment required | Ambiguous terms, complex matches |
| `LLM_ASSISTED` | Claude Code or LLM suggested mapping | Used in Claude Code workflow |
| `NEEDS_EXPERT` | Requires domain expert review | Novel compounds, unclear mappings |

**Provenance tracking**: All mappings record curator (automated/manual/LLM), timestamp, and reasoning.

## Categorization System

Unmapped ingredients are categorized to prioritize curation effort:

| Category | Description | Mappability | Strategy |
|----------|-------------|-------------|----------|
| `SIMPLE_CHEMICAL` | Salts, common organics | High (80-100) | Batch curation |
| `COMPLEX_MIXTURE` | Vitamin/metal solutions | Low (10-30) | Often unmappable |
| `ENVIRONMENTAL` | Soil, seawater | Medium (50-70) | Try ENVO |
| `INCOMPLETE` | Generic terms | Low (20-40) | Manual review |
| `PLACEHOLDER` | "See source" | Very low (0-10) | Leave unmapped |
| `UNKNOWN` | Uncategorized | Medium (40-60) | Claude Code-assisted |

**Use**: `scripts/analyze_unmapped.py` generates category assignments and mappability scores.

## Troubleshooting

### No Matches Found

**Problem**: Search returns no results

**Solutions**:
1. Try normalized variants: Use `generate_search_variants()`
2. Check spelling: Common vs British English (sulfate vs sulphate)
3. Try alternative ontologies: CHEBI → FOODON → ENVO
4. Use fuzzy search: OAK `l~` prefix or OLS API
5. Search formula instead of name: "MgSO4" instead of "magnesium sulfate"

### Too Many Matches

**Problem**: Search returns many low-quality matches

**Solutions**:
1. Use more specific term: "D-glucose" instead of "glucose"
2. Include chemical context: "potassium phosphate dibasic" instead of "potassium phosphate"
3. Filter by score: Only consider matches with score ≥ 0.7
4. Use exact match first: Try `basic_search()` before fuzzy search

### Ambiguous Results

**Problem**: Multiple equally good matches

**Solutions**:
1. Check ontology definitions: Read term descriptions
2. Consider biological context: What organisms/media use this?
3. Use most specific term: Species-level over genus-level
4. Mark `NEEDS_EXPERT` if truly ambiguous

### Complex Mixture

**Problem**: Ingredient is a mixture of unknown composition

**Solutions**:
1. Check if composition is defined elsewhere in dataset
2. Search for mixture as a whole (e.g., "Hoagland solution")
3. If composition unknown, mark as **unmappable**
4. Document in notes: "Composition varies by source"

## Best Practices

### DO:

✅ **Normalize before searching**: Always try chemical normalization patterns first

✅ **Try multiple ontologies**: CHEBI → FOODON → ENVO

✅ **Use most specific term**: "D-glucose" > "glucose" > "sugar"

✅ **Record provenance**: Document curator, timestamp, reasoning

✅ **Preserve original forms**: Save hydrates, catalogs as synonyms

✅ **Validate mappings**: Check that term exists and definition matches

✅ **Check KG-Microbe first**: Reuse existing ingredient entities

### DON'T:

❌ **Force mappings for complex mixtures**: "Vitamin solution" is often unmappable

❌ **Use generic terms when specific exists**: Don't use "salt" when you have "NaCl"

❌ **Skip normalization for chemicals**: Always normalize hydrates, formulas

❌ **Ignore synonym preservation**: Original forms provide valuable context

❌ **Guess at low confidence**: Mark `NEEDS_EXPERT` instead of poor-quality mapping

❌ **Create duplicates**: Check existing ingredients before creating new ones

## Related Tools and Documentation

### Curation Scripts

- `scripts/analyze_unmapped.py` - Categorize and prioritize ingredients
- `scripts/batch_curate_unmapped.py` - Batch workflow for simple chemicals
- `scripts/curate_unmapped.py` - Interactive single-ingredient curation
- `scripts/prepare_for_claude_curation.py` - Prepare batches for Claude Code
- `scripts/apply_claude_suggestions.py` - Apply Claude Code suggestions
- `scripts/import_from_culturemech.py` - Import from CultureMech
- `scripts/export_to_culturemech.py` - Export to CultureMech

### Core Utilities

- `src/mediaingredientmech/utils/chemical_normalizer.py` - Normalization logic
- `src/mediaingredientmech/utils/ontology_client.py` - OAK integration
- `src/mediaingredientmech/utils/curator.py` - Curation state management

### Documentation

- `docs/UNMAPPED_CURATION.md` - General curation guide
- `docs/CLAUDE_CODE_CURATION.md` - Claude Code workflow guide
- `README.md` - Project overview and setup

### Related Skills

- `search-ingredients-hierarchical.md` (MicroGrowAgents) - Hierarchical ingredient search patterns
- `dismech-terms/SKILL.md` (DisMech) - Ontology term curation patterns

## Implementation References

### Chemical Normalizer

```python
# Core normalization function
from mediaingredientmech.utils.chemical_normalizer import normalize_chemical_name

result = normalize_chemical_name("MgSO4•7H2O")
# Returns: NormalizationResult with original, normalized, variants, applied_rules

# Generate comprehensive search variants
from mediaingredientmech.utils.chemical_normalizer import generate_search_variants

variants = generate_search_variants("CaCl2·2H2O")
# Returns: ['CaCl2·2H2O', 'CaCl2', 'calcium chloride', 'calcium chloride dihydrate']
```

### Ontology Client

```python
from mediaingredientmech.utils.ontology_client import OntologyClient

client = OntologyClient()

# Simple search
results = client.search("glucose", sources=["CHEBI"])

# Multi-variant search with deduplication
variants = ["magnesium sulfate", "MgSO4", "magnesium sulphate"]
results = client.search_with_variants(variants, sources=["CHEBI"], max_results=10)

# Validate term exists
exists = client.validate_term("CHEBI:32599")
```

### Curator

```python
from mediaingredientmech.utils.curator import UnmappedCurator

curator = UnmappedCurator("data/ingredients/unmapped")

# Accept mapping
curator.accept_mapping(
    ingredient_name="MgSO4•7H2O",
    ontology_id="CHEBI:32599",
    ontology_label="magnesium sulfate",
    ontology_source="CHEBI",
    quality="EXACT_MATCH"
)

# Mark as needs expert review
curator.mark_needs_expert(
    ingredient_name="Vitamin solution A",
    notes="Composition not specified"
)
```

## Summary

This skill provides comprehensive guidance for mapping media ingredient names to ontology terms using:

- **Chemical normalization**: Handle hydrates, formulas, catalogs, abbreviations
- **Ontology selection**: CHEBI (chemicals), FOODON (biologicals), ENVO (environmental)
- **Multiple matching levels**: Exact → Normalized → Fuzzy → Manual
- **Three workflows**: Interactive, Batch, Claude Code-assisted
- **KG-Microbe integration**: Bidirectional data flow with CultureMech
- **Quality tracking**: Six quality levels with full provenance
- **Synonym preservation**: Maintain original chemical forms as typed synonyms

**Key principle**: Use the simplest matching strategy that works. Start with exact match, escalate to normalized/fuzzy only when needed, and mark for expert review when automated approaches fail.
