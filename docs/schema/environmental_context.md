# Environmental Context Schema

The `environmental_context` field on `MappedIngredient` links ingredients to the environments where they are relevant, using [ENVO](https://www.ebi.ac.uk/ols/ontologies/envo) (Environment Ontology) terms and relevance qualifiers.

**Schema file**: `src/mediaingredientmech/schema/mapped_ingredients_schema.yaml`

**GitHub Issue**: [#1 - Environmental context linking](https://github.com/CultureBotAI/MediaIngredientMech/issues/1)

## Why Environmental Context?

Many media ingredients have specific relationships to environments:

- **Humic acid** is naturally found in peatlands
- **NaCl** mimics the salinity of sea water
- **Sodium sulfide** is both found in and required by organisms from hydrothermal vents

Capturing these relationships enables:

1. **Environment-based discovery** - "What ingredients are associated with peatland environments?"
2. **Cross-repository queries** - Link ingredients to CultureMech media recipes and CommunityMech microbial communities via shared ENVO terms
3. **Media design support** - When designing media for a specific environment, find relevant ingredients

## EnvironmentContext Class

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `environment_term` | string | Yes | ENVO term CURIE. Must match `^ENVO:\d{7,8}$` |
| `environment_label` | string | No | Human-readable label for the ENVO term |
| `relevance` | EnvironmentRelevanceEnum | Yes | Why this ingredient is relevant to the environment |
| `notes` | string | No | Additional context about the relationship |

### Field Details

**`environment_term`** (required): An ENVO CURIE identifying the environment. Use the [ENVO Browser](https://www.ebi.ac.uk/ols/ontologies/envo) to find appropriate terms. The pattern requires 7-8 digits after the prefix.

**`environment_label`** (optional but recommended): The official ENVO label for readability. Not validated against ENVO, so keep it accurate.

**`relevance`** (required): A qualifier explaining *why* the ingredient relates to this environment. This is required to ensure annotations are meaningful rather than just tags.

**`notes`** (optional): Free-text for specifics that the enum cannot capture, such as concentrations, conditions, or caveats.

## EnvironmentRelevanceEnum

| Value | Description | Example |
|-------|-------------|---------|
| `NATURAL_SOURCE` | Ingredient is naturally found in or sourced from this environment | Humic acid from peatland |
| `REQUIRED_FOR_ORGANISM` | Required for cultivating organisms from this environment | Sulfide for hydrothermal vent bacteria |
| `SELECTIVE_AGENT` | Selectively promotes organisms from this environment | Elemental sulfur for hot spring thermophiles |
| `ENVIRONMENT_MIMIC` | Helps replicate the chemical conditions of this environment | NaCl at 3.5% mimics sea water |
| `COMMONLY_USED` | Commonly used in media for this environment (empirical) | Yeast extract in soil bacteria media |

### Choosing the Right Relevance

- Use `NATURAL_SOURCE` when the ingredient is a component of the environment itself
- Use `REQUIRED_FOR_ORGANISM` when organisms from that environment need it metabolically
- Use `SELECTIVE_AGENT` when the ingredient differentiates organisms from this environment vs. others
- Use `ENVIRONMENT_MIMIC` when the ingredient recreates environmental chemistry in vitro
- Use `COMMONLY_USED` as a fallback when the association is empirical but the mechanism is unclear

An ingredient can have the **same environment with different relevance values**. For example, sodium sulfide is both `NATURAL_SOURCE` (abundant in vent fluids) and `REQUIRED_FOR_ORGANISM` (electron donor for vent bacteria) for hydrothermal vents.

## MappedIngredient Field

The `environmental_context` field is added to `MappedIngredient`:

| Property | Value |
|----------|-------|
| Range | EnvironmentContext |
| Required | No (backward compatible) |
| Multivalued | Yes |
| Inlined | As list |

Existing ingredients without `environmental_context` remain valid.

## Examples

### Peatland Ingredient (NATURAL_SOURCE)

```yaml
preferred_term: Humic acid
ontology_id: CHEBI:27385
ontology_label: humic acid
ontology_source: CHEBI
mapping_quality: DIRECT_MATCH
environmental_context:
  - environment_term: "ENVO:00000044"
    environment_label: peatland
    relevance: NATURAL_SOURCE
    notes: "Major component of peat organic matter; humic substances make up 30-50% of peat"
  - environment_term: "ENVO:00005773"
    environment_label: peat bog
    relevance: REQUIRED_FOR_ORGANISM
    notes: "Required for cultivation of humic acid-degrading bacteria from Sphagnum bogs"
```

### Marine Ingredient (ENVIRONMENT_MIMIC)

```yaml
preferred_term: NaCl
ontology_id: CHEBI:26710
ontology_label: sodium chloride
ontology_source: CHEBI
mapping_quality: DIRECT_MATCH
environmental_context:
  - environment_term: "ENVO:00002149"
    environment_label: sea water
    relevance: ENVIRONMENT_MIMIC
    notes: "Provides salinity for marine organism cultivation (~3.5% w/v)"
  - environment_term: "ENVO:00002044"
    environment_label: hypersaline lake
    relevance: ENVIRONMENT_MIMIC
    notes: "High concentrations (15-30%) for halophilic organism cultivation"
  - environment_term: "ENVO:00002150"
    environment_label: coastal water
    relevance: ENVIRONMENT_MIMIC
```

### Dual Relevance (same environment, different reasons)

```yaml
preferred_term: Sodium sulfide
ontology_id: CHEBI:29919
ontology_label: sodium sulfide
ontology_source: CHEBI
mapping_quality: DIRECT_MATCH
environmental_context:
  - environment_term: "ENVO:01000030"
    environment_label: hydrothermal vent
    relevance: NATURAL_SOURCE
    notes: "Sulfide is abundant in hydrothermal vent fluids (1-10 mM)"
  - environment_term: "ENVO:01000030"
    environment_label: hydrothermal vent
    relevance: REQUIRED_FOR_ORGANISM
    notes: "Electron donor for chemolithoautotrophic sulfur-oxidizing vent bacteria"
```

### Selective Agent

```yaml
preferred_term: Elemental sulfur
ontology_id: CHEBI:26833
ontology_label: sulfur atom
ontology_source: CHEBI
mapping_quality: SYNONYM_MATCH
environmental_context:
  - environment_term: "ENVO:01000339"
    environment_label: hot spring
    relevance: SELECTIVE_AGENT
    notes: "Selects for sulfur-metabolizing thermophiles from acidic hot springs"
```

### Commonly Used (empirical association)

```yaml
preferred_term: Yeast extract
ontology_id: CHEBI:63120
ontology_label: yeast extract
ontology_source: CHEBI
mapping_quality: DIRECT_MATCH
environmental_context:
  - environment_term: "ENVO:00002982"
    environment_label: soil
    relevance: COMMONLY_USED
  - environment_term: "ENVO:00002149"
    environment_label: sea water
    relevance: COMMONLY_USED
```

### No Environmental Context (backward compatible)

```yaml
preferred_term: Agar
ontology_id: CHEBI:2509
ontology_label: agar
ontology_source: CHEBI
mapping_quality: DIRECT_MATCH
# No environmental_context - this is valid
```

## Common ENVO Terms

### Terrestrial

| ENVO ID | Label | Typical Ingredients |
|---------|-------|-------------------|
| `ENVO:00000044` | peatland | Humic acid, Sphagnum extract |
| `ENVO:00002982` | soil | Soil extract, chitin, cellulose |
| `ENVO:00000134` | permafrost | Low-temperature buffers |

### Marine

| ENVO ID | Label | Typical Ingredients |
|---------|-------|-------------------|
| `ENVO:00002149` | sea water | NaCl, artificial sea water salts |
| `ENVO:01000030` | hydrothermal vent | Sodium sulfide, iron(II) chloride |
| `ENVO:03000003` | marine sediment | Sodium sulfate, acetate |

### Freshwater

| ENVO ID | Label | Typical Ingredients |
|---------|-------|-------------------|
| `ENVO:00000023` | lake | Low-salt mineral medium |
| `ENVO:00000022` | river | Dissolved organic carbon sources |

### Extreme

| ENVO ID | Label | Typical Ingredients |
|---------|-------|-------------------|
| `ENVO:01000339` | hot spring | Thermostable buffer, sulfur compounds |
| `ENVO:00002044` | hypersaline lake | NaCl (>15%), MgCl2 |

### Host-Associated

| ENVO ID | Label | Typical Ingredients |
|---------|-------|-------------------|
| `ENVO:02000065` | rhizosphere | Plant root exudate components |

## Cross-Repository Integration

The `environmental_context` field enables cross-repository queries via shared ENVO term CURIEs:

| Repository | Field | Level | Example |
|-----------|-------|-------|---------|
| **CultureMech** | `source_environment` | Media recipe | "This medium is for peatland organisms" |
| **MediaIngredientMech** | `environmental_context` | Ingredient | "Humic acid comes from peatland" |
| **CommunityMech** | `environment_term` | Community | "This community is from peatland" |

**Shared key**: ENVO term CURIE (e.g., `ENVO:00000044`)

### Example Cross-Repo Query

Find ingredients relevant to peatland environments that appear in media designed for peatland organisms:

1. Query MediaIngredientMech: ingredients where `environmental_context.environment_term = ENVO:00000044`
2. Query CultureMech: media where `source_environment.term.id = ENVO:00000044`
3. Join: ingredients that appear in those media
4. Result: peatland-specific ingredient catalog with usage context

## Python Usage

```python
from src.mediaingredientmech.schema.mapped_ingredients_schema import (
    EnvironmentContext,
    EnvironmentRelevanceEnum,
    MappedIngredient,
)

# Create an environmental context annotation
ctx = EnvironmentContext(
    environment_term="ENVO:00000044",
    relevance="NATURAL_SOURCE",
    environment_label="peatland",
    notes="Major component of peat organic matter",
)

# Attach to an ingredient
ingredient = MappedIngredient(
    preferred_term="Humic acid",
    ontology_id="CHEBI:27385",
    environmental_context=[ctx],
)

# Access
for ec in ingredient.environmental_context:
    print(f"{ec.environment_term} ({ec.environment_label}): {ec.relevance}")
```

## Validation

Run the validation test suite:

```bash
pytest tests/test_environmental_context.py -v
```

This runs 44 tests covering schema definition, enum values, ENVO pattern validation, Python dataclass instantiation, backward compatibility, and YAML test data files.

## Related Documentation

- [Schema Reference](../SCHEMA_REFERENCE.md) - Full schema documentation
- [Curation Guide](../CURATION_GUIDE.md) - How to curate ingredients
