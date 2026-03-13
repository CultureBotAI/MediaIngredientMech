# Unmapped Ingredients Curation Guide

Systematic workflow for curating unmapped media ingredients using chemical name normalization.

## Quick Start

```bash
# 1. Analyze unmapped ingredients
python scripts/analyze_unmapped.py

# 2. Start batch curation (simple chemicals first)
python scripts/batch_curate_unmapped.py \
  --category SIMPLE_CHEMICAL \
  --auto-normalize \
  --curator your_name

# 3. Check progress
cat notes/curation_decisions.csv
```

## Current Status

- **Total ingredients:** 1,107
- **Mapped:** 995 (89.9%)
- **Unmapped:** 112 (10.1%)

**Target:** Map 40-50 simple chemicals → 94-95% total coverage

## Tools

### 1. analyze_unmapped.py

Categorizes all unmapped ingredients and generates a prioritized curation list.

```bash
python scripts/analyze_unmapped.py [--verbose]
```

**Outputs:**
- `notes/unmapped_analysis.md` - Prioritized list (by mappability score)
- `data/ingredients/unmapped/*.yaml` - Category-specific files

**Categories:**
- **SIMPLE_CHEMICAL** (40%) - Chemicals with notation issues (hydrates, catalog numbers, incomplete formulas)
- **COMPLEX_MIXTURE** (30%) - Vitamin/metal solutions, media compositions
- **UNKNOWN** (22%) - Needs manual review
- **ENVIRONMENTAL** (5%) - Soil, seawater samples
- **PLACEHOLDER** (2%) - "See source for composition"
- **INCOMPLETE** (1%) - Generic terms like "Vitamin B"

### 2. batch_curate_unmapped.py

Batch curation with auto-normalization and multi-variant search.

```bash
python scripts/batch_curate_unmapped.py [OPTIONS]
```

**Key options:**
- `--category CATEGORY` - Filter by category
- `--auto-normalize` - Enable auto-normalization and high-confidence auto-accept
- `--min-confidence 0.9` - Minimum score for auto-accept (0.0-1.0)
- `--resume PATH` - Resume from progress file
- `--export-csv PATH` - Export decisions to CSV
- `--curator NAME` - Your name for audit trail
- `--sources LIST` - Ontology sources (CHEBI,FOODON,ENVO)

**Interactive actions:**
- `a` - Accept mapping (select candidate + quality rating)
- `s` - Skip
- `e` - Mark NEEDS_EXPERT
- `x` - Mark AMBIGUOUS
- `r` - Re-search with custom query
- `q` - Quit and save

### 3. curate_unmapped.py (Enhanced)

Interactive curation with full terminal UI (now shows normalization info).

```bash
python scripts/curate_unmapped.py --curator your_name
```

**When to use:**
- Need full context (synonyms, occurrence stats)
- Want to add notes/synonyms during curation
- Prefer rich UI

## Chemical Name Normalization

The normalization system automatically handles common notation issues:

### Normalization Rules

| Issue | Example | Normalized | Search Variants |
|-------|---------|------------|-----------------|
| Hydrate notation | `MgSO4•7H2O` | `MgSO4` | MgSO4•7H2O, MgSO4, magnesium sulfate |
| Incomplete formula | `K2HPO` | `K2HPO4` | K2HPO, K2HPO4, dipotassium phosphate |
| Catalog number | `NaCl (Fisher S271-500)` | `NaCl` | NaCl, sodium chloride |
| Abbreviation | `dH2O` | `dH2O` | dH2O, distilled water |

### How It Works

1. **Strip catalog info**: Remove `(Fisher X)`, `(Sigma Y)`, `(CAS: Z)`
2. **Strip hydrates**: Remove `•nH2O`, `.nH2O`, `·nH2O`
3. **Fix incomplete**: `NaNO` → `NaNO3`, `MgCO` → `MgCO3`
4. **Generate variants**:
   - Original name
   - Normalized name
   - Formula → common name (e.g., NaCl → sodium chloride)
   - Abbreviation → expanded (e.g., EDTA → ethylenediaminetetraacetic acid)
5. **Preserve original form**: When normalization is applied, the original form is automatically added as a synonym with appropriate type:
   - `HYDRATE_FORM` - For hydrate notation (e.g., `MgSO4•7H2O`)
   - `CATALOG_VARIANT` - For catalog/supplier codes (e.g., `NaCl (Fisher S271-500)`)
   - `INCOMPLETE_FORMULA` - For incomplete formulas (e.g., `K2HPO`)
   - `ALTERNATE_FORM` - For other chemical form variations

All variants are searched and results deduplicated.

## Recommended Workflow

### Phase 1: Simple Chemicals (High Priority)

**Goal:** Map 40-45 simple chemicals to CHEBI

```bash
# Analyze first
python scripts/analyze_unmapped.py

# Review top candidates
head -30 notes/unmapped_analysis.md

# Batch curate with auto-normalize
python scripts/batch_curate_unmapped.py \
  --category SIMPLE_CHEMICAL \
  --auto-normalize \
  --min-confidence 0.9 \
  --curator marcin
```

**Expected results:**
- Hydrates: `MgSO4•7H2O` → CHEBI:32599 (magnesium sulfate)
- Incomplete formulas: `K2HPO` → CHEBI:63036 (dipotassium phosphate)
- Catalog variants: `NaCl (Fisher S271-500)` → CHEBI:26710 (sodium chloride)
- Abbreviations: `dH2O` → CHEBI:15377 (water)

### Phase 2: Unknown Category (Medium Priority)

**Goal:** Map 10-15 items that need manual review

```bash
python scripts/batch_curate_unmapped.py \
  --category UNKNOWN \
  --curator marcin
```

**Strategy:**
- Try searching FOODON if biological extracts
- Use re-search (`r`) with alternative queries
- Mark NEEDS_EXPERT if unclear

### Phase 3: Environmental Samples (Low Priority)

**Goal:** Map 3-5 environmental samples to ENVO

```bash
python scripts/batch_curate_unmapped.py \
  --category ENVIRONMENTAL \
  --sources ENVO \
  --curator marcin
```

**Examples:**
- `Pasteurized Seawater` → Search ENVO for "seawater"
- `CR1 Soil` → Search ENVO for "soil"

### Phase 4: Mark Unmappable Items

**Goal:** Categorize items that should stay UNMAPPED

```bash
# Complex mixtures (vitamin solutions, etc.)
python scripts/batch_curate_unmapped.py \
  --category COMPLEX_MIXTURE \
  --curator marcin
# Mark most as AMBIGUOUS or leave UNMAPPED

# Placeholders
# Leave UNMAPPED: "See source for composition"
```

## Quality Ratings

Choose appropriate quality when accepting a mapping:

| Rating | When to Use |
|--------|-------------|
| **EXACT_MATCH** | Name matches ontology label exactly |
| **SYNONYM_MATCH** | Name matches a known synonym in ontology |
| **CLOSE_MATCH** | Semantically equivalent but different text |
| **MANUAL_CURATION** | Curator judgment required |

## Progress Tracking

### Check Status

```bash
# View curation decisions
cat notes/curation_decisions.csv

# Or use interactive tool and press 'p' for progress report
python scripts/curate_unmapped.py
```

### Resume Session

Progress auto-saves after each ingredient:

```bash
python scripts/batch_curate_unmapped.py \
  --resume notes/curation_progress.yaml \
  --curator marcin
```

## Example Session

```bash
$ python scripts/batch_curate_unmapped.py --category SIMPLE_CHEMICAL --auto-normalize

┌─────────────────────────────────────────┐
│ Batch Curation Tool                     │
│ Systematically curate unmapped          │
│ ingredients with auto-normalization     │
└─────────────────────────────────────────┘

Filtered to 45 SIMPLE_CHEMICAL ingredients
Processing 45 unmapped ingredients

─── Ingredient 1/45 ───

┌─── UNMAPPED_0003 ────────────────────────┐
│ Name: MgSO4•7H2O                         │
│ Category: SIMPLE_CHEMICAL                │
│ Occurrences: 29 across 29 media          │
└──────────────────────────────────────────┘

Normalized: MgSO4 (rules: stripped_hydrate)

Ontology Candidates
┏━━━━┳━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━┓
┃ #  ┃ ID          ┃ Label               ┃ Source ┃ Score ┃
┡━━━━╇━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━┩
│ 1  │ CHEBI:32599 │ magnesium sulfate   │ CHEBI  │  0.95 │
│ 2  │ CHEBI:86455 │ magnesium sulfate   │ CHEBI  │  0.93 │
│    │             │ heptahydrate        │        │       │
└────┴─────────────┴─────────────────────┴────────┴───────┘

High-confidence match found:
  MgSO4•7H2O → MgSO4
  → CHEBI:32599 (magnesium sulfate)
  Score: 0.95

Auto-accept this mapping? [Y/n]: y

Mapped to CHEBI:32599 (magnesium sulfate)
Added 'MgSO4•7H2O' as synonym (normalization: stripped_hydrate)
```

## Validation

After curation, validate all mappings:

```bash
# Validate all
just validate-all

# Or manually
linkml-validate \
  --schema src/mediaingredientmech/schema/mediaingredientmech.yaml \
  data/curated/unmapped_ingredients.yaml
```

## Expected Outcomes

**Realistic targets:**
- ✅ 40-45 simple chemicals → CHEBI
- ✅ 3-5 environmental samples → ENVO
- ✅ 30-40 marked as AMBIGUOUS/COMPLEX_MIXTURE
- ✅ Total coverage: 89.9% → 94-95%

**Quality standards:**
- All mappings have quality scores
- Full curation history with normalization rules tracked
- All mappings pass validation

## After Curation

### 1. Generate Report

```bash
python scripts/generate_report.py
```

### 2. Rebuild Documentation

```bash
just build-docs
```

### 3. Regenerate UMAP

```bash
just generate-umap
```

### 4. Commit Changes

```bash
git add data/curated/unmapped_ingredients.yaml notes/
git commit -m "Curate unmapped ingredients with chemical normalization

- Mapped 42 simple chemicals to CHEBI
- Used automated normalization for hydrates, catalog numbers
- Total coverage increased from 89.9% to 94.2%
"
```

## Troubleshooting

### No candidates found

Try:
1. Press `r` to re-search with alternative query
2. Try formula vs. name (or vice versa)
3. Search different ontology (FOODON, ENVO)
4. Check original name for typos

### Ambiguous matches

- Mark `AMBIGUOUS` if multiple equally valid options
- Mark `NEEDS_EXPERT` if requires domain knowledge

### Tool errors

Check:
- Python environment: `poetry install` or `pip install -e .`
- OAK adapters: `pip install oaklib`
- Internet connection (for ontology downloads)
- YAML file valid: `yamllint data/curated/unmapped_ingredients.yaml`

## Tips

1. **Start with high-score items** - Build confidence
2. **Use auto-normalize** - Massive time saver
3. **Don't force mappings** - Better to skip than create bad mapping
4. **Review CSV periodically** - Check for patterns
5. **Take breaks** - Quality degrades with fatigue

## See Also

- [CURATION_GUIDE.md](CURATION_GUIDE.md) - General curation workflow
- [WORKFLOWS.md](WORKFLOWS.md) - Common operations
- [SCHEMA_REFERENCE.md](SCHEMA_REFERENCE.md) - Data model details
