# MediaIngredientMech

LLM-assisted curation system for media ingredient ontology mappings.

## Overview

MediaIngredientMech provides a structured workflow for curating media ingredient ontology mappings with full audit trails. It manages the ingredient records aggregated from media recipes in [CultureMech](https://github.com/CultureBotAI/CultureMech). The documentation build regenerates the [current mapping inventory](data/curated/ALL_INGREDIENTS.md), avoiding counts here that quickly become stale.

**Design stance — practically oriented.** An ingredient record denotes a specific
chemical someone can **order**. Where sources disagree about which form a recipe
means, MIM picks one by convention (preferring the term that carries the
commercial CAS) rather than splitting the record or retreating to a generic
term — while keeping every raw form as a resolvable synonym. See
[`MAPPING_SEMANTICS.md`](MAPPING_SEMANTICS.md) Section 3.

**Key Features:**
- Ingredient-centric data model with LinkML schemas
- Environmental context linking via ENVO ontology terms
- Interactive CLI for ontology mapping curation
- LLM assistance tracking in curation events
- Comprehensive validation (schema + ontology terms)
- Full audit trail for all curation actions
- YAML-based data storage with version control
- Cross-repository integration with CultureMech and CommunityMech

## Quick Start

### Installation

```bash
# Clone repository
git clone https://github.com/CultureBotAI/MediaIngredientMech.git
cd MediaIngredientMech

# Install with dev dependencies
just install

# Generate LinkML dataclasses
just gen-schema
```

### Use the Curated Corpus

```bash
# Validate the tracked curated records
just validate-all
```

The four former CultureMech collection writers are retired and fail closed
because they overwrote MIM-owned curation with lossy or incomplete aggregate
projections. Until the
replacement contracts in [#447](https://github.com/CultureBotAI/MediaIngredientMech/issues/447)
and [#449](https://github.com/CultureBotAI/MediaIngredientMech/issues/449) are
implemented, review upstream changes and apply scoped curated updates rather
than regenerating `data/curated/`.

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
- Tracked MIM ingredient collections and per-record YAML are the authoritative
  curated surfaces
- CultureMech aggregates are partial diagnostic inputs, not evidence of
  upstream absence and not overwrite-ready MIM records

**Schema:**
- `IngredientRecord`: Root class with mapping status, synonyms, curation history
- `OntologyMapping`: CHEBI/FOODON term mappings with quality ratings
- `CurationEvent`: Audit trail with LLM assistance tracking
- `EnvironmentContext`: ENVO-based environmental linking with relevance qualifiers
- `MappedIngredient`: Aggregated ingredient with environmental context annotations

**Workflow:**
1. Review upstream changes against the tracked MIM corpus
2. Apply scoped, provenance-recorded curation updates
3. Curate unmapped ingredients (sorted by occurrence count)
4. Validate ontology terms via OAK/OLS
5. Publish validated MIM artifacts and coordinate scoped downstream updates

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

## Mapping Semantics

See [MAPPING_SEMANTICS.md](MAPPING_SEMANTICS.md) for predicate semantics (`skos:exactMatch` / `skos:closeMatch` / `skos:narrowMatch` / `skos:broadMatch`), the registry/identity row pattern pairing `MIM:<slug>` with `kgmicrobe.{ingredient,compound}:<slug>`, common mistakes by Rule id, and the curator workflow when CI rejects a row in `mappings/ingredient_mappings.sssom.tsv`.

## Documentation

- [Curation Guide](docs/CURATION_GUIDE.md) - Step-by-step curation workflow
- [Role Curation Workflow](docs/ROLE_CURATION_WORKFLOW.md) - Media ingredient role assignment workflow
- [Schema Reference](docs/SCHEMA_REFERENCE.md) - Data model documentation
- [Environmental Context](docs/schema/environmental_context.md) - ENVO-based environmental linking
- [Workflows](docs/WORKFLOWS.md) - Common operations and integration
- [Mapping Semantics](MAPPING_SEMANTICS.md) - SSSOM predicate semantics and registry/identity row pattern

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

## Deep Research Provider Triage

The provider workflow mirrors public DisMech while targeting ingredient
curation. `identity_mapping` emphasizes exact salts, hydrates, mixtures,
formulations, CAS-RN provenance, and ontology semantics; `functional_roles`
emphasizes context-specific roles in culture media.

```bash
just deep-research-providers
just deep-research-providers functional_roles
just deep-research-provider claude_code identity_mapping
just research-ingredient falcon mapped yeast_extract --dry-run
```

The command ranks providers separately for discovery, synthesis, and
verification, including credential/CLI availability, cost, speed, and source
coverage. Research reports remain proposals until their exact identity and
evidence are validated.

## License

CC0-1.0 - Public Domain Dedication
