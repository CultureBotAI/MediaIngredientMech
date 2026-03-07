# MediaIngredientMech

LLM-assisted curation system for media ingredient ontology mappings.

## Overview

MediaIngredientMech provides a structured workflow for curating media ingredient ontology mappings with full audit trails. It manages 995 mapped and 136 unmapped ingredients aggregated from 10,657 media recipes in [CultureMech](https://github.com/KG-Hub/CultureMech).

**Key Features:**
- Ingredient-centric data model with LinkML schemas
- Interactive CLI for ontology mapping curation
- LLM assistance tracking in curation events
- Comprehensive validation (schema + ontology terms)
- Full audit trail for all curation actions
- YAML-based data storage with version control

## Quick Start

### Installation

```bash
# Clone repository
cd /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/MediaIngredientMech

# Install with dev dependencies
just install

# Generate LinkML dataclasses
just gen-schema
```

### Import Data

```bash
# Import from CultureMech (995 mapped + 136 unmapped = 1,131 total)
just import-data

# Validate imported data
just validate-all
```

### Curate Ingredients

```bash
# Create snapshot before curation
just snapshot

# Launch interactive curation CLI
just curate

# Generate progress report
just report
```

## Architecture

**Data Sources:**
- `CultureMech/output/mapped_ingredients.yaml` → 995 mapped ingredients
- `CultureMech/output/unmapped_ingredients.yaml` → 136 unmapped ingredients

**Schema:**
- `IngredientRecord`: Root class with mapping status, synonyms, curation history
- `OntologyMapping`: CHEBI/FOODON term mappings with quality ratings
- `CurationEvent`: Audit trail with LLM assistance tracking

**Workflow:**
1. Import data from CultureMech
2. Curate unmapped ingredients (sorted by occurrence count)
3. Validate ontology terms via OAK/OLS
4. Record curation events with timestamps
5. Export validated mappings back to CultureMech

## Project Structure

```
MediaIngredientMech/
├── src/mediaingredientmech/
│   ├── schema/              # LinkML schemas
│   ├── curation/            # Core curation logic
│   ├── validation/          # Schema & ontology validators
│   ├── export/              # Report generation
│   └── utils/               # YAML I/O, ontology client
├── data/
│   ├── curated/             # Working data (version controlled)
│   └── snapshots/           # Timestamped backups (excluded from git)
├── scripts/                 # CLI tools
├── tests/                   # Test suite
└── docs/                    # Documentation
```

## Documentation

- [Curation Guide](docs/CURATION_GUIDE.md) - Step-by-step curation workflow
- [Schema Reference](docs/SCHEMA_REFERENCE.md) - Data model documentation
- [Workflows](docs/WORKFLOWS.md) - Common operations and integration

## Development

```bash
# Run tests with coverage
just test-cov

# Format code
just format

# Lint code
just lint

# Run all quality checks
just check
```

## License

CC0-1.0 - Public Domain Dedication
