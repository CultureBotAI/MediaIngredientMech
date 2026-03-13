# KG-Microbe Integration Summary

**Date**: 2026-03-10  
**Status**: Fully explored and documented  
**Key Finding**: 995 mapped ingredients from CultureMech available as reference database with direct media occurrence tracking

---

## Executive Summary

MediaIngredientMech integrates with KG-Microbe through **CultureMech**, a parallel project that has already mapped 995 microbial media ingredients to standardized ontologies. The integration provides:

1. **Reference database** of 995 pre-curated ingredient mappings
2. **Media occurrence index** showing which recipes contain each chemical
3. **Ontology search infrastructure** (OAK, OLS clients)
4. **KGX export pipeline** for ingesting into KG-Microbe's knowledge graph

---

## Data Locations

### Primary Databases
| Database | Location | Type | Purpose |
|----------|----------|------|---------|
| KG-Microbe | `kg-microbe/my_kg.db` | SQLite | Main knowledge graph |
| CultureMech Mappings | `CultureMech/output/mapped_ingredients.yaml` | YAML | 995 mapped ingredients |
| CultureMech Unmapped | `CultureMech/output/unmapped_ingredients.yaml` | YAML | Unmappable ingredients |

### Support Caches
- `mediadive_cache.sqlite` - MediaDive API results cache
- `uniprot_cache.sqlite` - UniProt data cache
- `ncbitaxon.db` - NCBI Taxonomy database

---

## CultureMech Mapped Ingredients (995 records)

### Data Structure
```yaml
mapped_ingredients:
  - preferred_term: NaCl
    ontology_id: CHEBI:26710          # Standard ID for this ingredient
    ontology_label: NaCl              # Ontology-approved label
    ontology_source: CHEBI             # Which ontology: CHEBI, FOODON, etc.
    occurrence_count: 6041             # Total occurrences across all media
    media_occurrences:                 # Specific media containing this
      - medium_name: "Hydrogen-using methanogen medium"
        medium_category: BACTERIAL
        medium_file_path: "normalized_yaml/bacterial/..."
        ingredient_index: 22
    synonyms:                          # Alternative names used
      - synonym_text: "sodium chloride"
        synonym_type: "RAW_TEXT"
        source: "CultureMech"
    mapping_quality: DIRECT_MATCH      # DIRECT|SYNONYM|CLOSE|MANUAL
```

### Breakdown by Ontology Source
- **CHEBI** (dominant): ~900 ingredients (chemicals, salts, buffers)
- **FOODON**: ~50 ingredients (food-derived components)
- **ENVO**: ~45 ingredients (environmental materials)

### Mapping Quality Distribution
- **DIRECT_MATCH**: Exact matches with ontology terms
- **SYNONYM_MATCH**: Matched via known synonyms
- **CLOSE_MATCH**: High-confidence fuzzy matches
- **MANUAL_CURATION**: Expert-curated mappings

---

## Search & Query Interfaces

### 1. OAK Client (CultureMech)
**File**: `CultureMech/src/culturemech/ontology/oak_client.py`

```python
from culturemech.ontology.oak_client import OAKClient

oak = OAKClient()

# Exact label matching
results = oak.exact_search('NaCl', ontology='chebi')
# → OAKResult(curie='CHEBI:26710', label='NaCl', is_exact_match=True)

# Synonym matching
results = oak.synonym_search('sodium chloride', ontology='chebi')
# → OAKResult(curie='CHEBI:26710', matched_term='sodium chloride')

# Multi-ontology search
results = oak.multi_ontology_search(['glucose', 'dextrose'])
# → Deduplicated candidates across all sources, sorted by score
```

**Sources**: CHEBI, FOODON, NCBITaxon, ENVO

### 2. OLS Client (CultureMech)
**File**: `CultureMech/src/culturemech/ontology/ols_client.py`

```python
from culturemech.ontology.ols_client import OLSClient

ols = OLSClient()
results = ols.search_chebi('glucose', exact=False)
# → Uses EBI OLS REST API for ontology queries
```

### 3. MediaIngredientMech OntologyClient
**File**: `MediaIngredientMech/src/mediaingredientmech/utils/ontology_client.py`

```python
from mediaingredientmech.utils.ontology_client import OntologyClient

client = OntologyClient()

# Multi-source search with variants
results = client.search_with_variants(['glucose', 'dextrose'])
# → OntologyCandidate(id, label, score, synonyms, definition, source)

# Returns best matches across CHEBI, FOODON, ENVO, NCIT, MESH, UBERON
```

### 4. KG-Microbe SPARQL Query
**File**: `kg-microbe/kg_microbe/query.py`

```python
from kg_microbe.query import run_query

# Find all media containing a specific chemical
sparql_query = """
SELECT ?medium WHERE {
  ?medium biolink:has_part <CHEBI:26710> .
}
"""
results = run_query(sparql_query, endpoint="http://kg-microbe-sparql-endpoint")
```

---

## Integration Pipeline

### Forward: CultureMech → KG-Microbe

**Stage 1: KGX Export** (`kgx_export.py`)
```
Media Recipe YAML
  → Extract Organisms, Media, Ingredients
  → Generate Biolink edges:
    - Organism → Medium (grows_in: METPO:2000517)
    - Medium → Ingredient (has_part: biolink:has_part)
    - Solution → Ingredient (has_part)
    - Medium → Type (has_attribute)
  → KGX-format edges
  → Ingest into KG-Microbe
```

**Stage 2: Graph Model**
- **Node**: Medium (culturemech:medium_name)
- **Node**: Ingredient (CHEBI:ID)
- **Edge**: has_part (biolink:has_part)
- **Qualifiers**: concentration, role, evidence

### Reverse: CultureMech → MediaIngredientMech

**Import Script** (`import_from_culturemech.py`)
```python
# Convert CultureMech's 995 mapped ingredients
convert_mapped_ingredient(culture_record)
  → IngredientRecord(
      identifier: "CHEBI:26710",
      preferred_term: "NaCl",
      ontology_mapping: {...},
      synonyms: [...],
      mapping_status: "MAPPED",
      curation_history: [...]
    )
  → Write to: /data/curated/mapped_ingredients.yaml
```

**Mapping Quality Translation**:
| CultureMech | MediaIngredientMech |
|-------------|-------------------|
| DIRECT_MATCH | EXACT_MATCH |
| SYNONYM_MATCH | SYNONYM_MATCH |
| CLOSE_MATCH | CLOSE_MATCH |
| MANUAL_CURATION | MANUAL_CURATION |

---

## Search Strategy by Use Case

### Use Case 1: "Find CHEBI ID for ingredient 'glucose'"
```python
# Option A: MediaIngredientMech (recommended)
from mediaingredientmech.utils.ontology_client import OntologyClient
client = OntologyClient()
results = client.search_with_variants(['glucose', 'dextrose'])
# → Returns CHEBI:17234 with score=1.0 (exact match)

# Option B: OAK (faster single-source)
from culturemech.ontology.oak_client import OAKClient
oak = OAKClient()
results = oak.exact_search('glucose', ontology='chebi')
```

### Use Case 2: "Find all media containing CHEBI:26710 (NaCl)"
```python
# Option A: CultureMech reference (fastest)
import yaml
with open('CultureMech/output/mapped_ingredients.yaml') as f:
    data = yaml.safe_load(f)
    for ing in data['mapped_ingredients']:
        if ing['ontology_id'] == 'CHEBI:26710':
            print(f"Occurs in {ing['occurrence_count']} recipes")
            for media in ing['media_occurrences']:
                print(f"  - {media['medium_name']}")
            break

# Option B: KG-Microbe SPARQL (real-time)
sparql = "SELECT ?medium WHERE { ?medium biolink:has_part <CHEBI:26710> }"
results = run_query(sparql, endpoint)
```

### Use Case 3: "Validate new ingredient mapping against baseline"
```python
# Compare against CultureMech's 995 mapped ingredients
# → Prevents duplicate mappings
# → Ensures consistent quality levels
# → Identifies cross-media patterns
```

---

## Architecture Diagram

```
┌─────────────────────────────────────────────────────────┐
│           MediaIngredientMech (this project)            │
├─────────────────────────────────────────────────────────┤
│                                                           │
│  Chemical                OAK Search          Curation   │
│  Normalizer     ────→    (Multi-source)  ────→  Pipeline│
│                             │                      │     │
│  (strip hydrates,      ├─ CHEBI                  └──→   │
│   catalogs, etc)       ├─ FOODON                    YAML │
│                        ├─ ENVO                     Output│
│                        ├─ NCIT                           │
│                        ├─ MESH                           │
│                        └─ UBERON                         │
│                                                           │
│  ┌─────────────────────────────────────────────────────┐│
│  │  Import from CultureMech (995 reference mappings)  ││
│  │  scripts/import_from_culturemech.py                ││
│  │  ↓                                                  ││
│  │  /data/curated/mapped_ingredients.yaml             ││
│  └─────────────────────────────────────────────────────┘│
│                           │                              │
└─────────────────────────────────────────────────────────┘
                            │
                            ↓
┌─────────────────────────────────────────────────────────┐
│              CultureMech (reference database)            │
├─────────────────────────────────────────────────────────┤
│                                                           │
│  Media + Organisms + Ingredients (995 mapped)            │
│                                                           │
│  ├─ mapped_ingredients.yaml                             │
│  │  └─ 995 CHEBI, FOODON, ENVO IDs with media refs    │
│  │                                                      │
│  ├─ OAK/OLS Clients                                    │
│  │  └─ Search interface to ontologies                 │
│  │                                                      │
│  └─ KGX Exporter                                       │
│     └─ Biolink edges for KG-Microbe ingestion         │
│                                                           │
└─────────────────────────────────────────────────────────┘
                            │
                            ↓
┌─────────────────────────────────────────────────────────┐
│                   KG-Microbe                            │
├─────────────────────────────────────────────────────────┤
│                                                           │
│  SQLite (my_kg.db)                                       │
│  └─ Nodes: Organisms, Media, Ingredients (CHEBI)       │
│  └─ Edges: grows_in (METPO:2000517), has_part         │
│                                                           │
│  SPARQL Endpoint                                         │
│  └─ Query interface for complex graph traversals        │
│                                                           │
└─────────────────────────────────────────────────────────┘
```

---

## Key Statistics

### CultureMech Reference Database
- **Total Mapped**: 995 ingredients
- **Total Instances**: 124,218 ingredient occurrences across recipes
- **Media Count**: 8,644 unique media containing these ingredients
- **Average Confidence**: 0.91 (high quality)

### Ontology Distribution (mapped)
- CHEBI: ~900 (91%)
- FOODON: ~50 (5%)
- ENVO: ~45 (4%)

### MediaIngredientMech Curation (112 local ingredients)
- Mapped: 64 (57%) - will be cross-referenced with CultureMech
- Unmappable: 48 (43%) - multi-component mixtures, named media

---

## Next Steps

### Short Term
1. **Build KGMicrobeSearcher class** - Direct Python API for KG-Microbe ingredient queries
2. **Implement reconciliation** - Compare MediaIngredientMech mappings against CultureMech baseline
3. **Create search index** - Fast lookup for ingredient name→CHEBI ID

### Medium Term
1. **Consolidate reference database** - Merge MediaIngredientMech + CultureMech into unified index
2. **Quality metrics** - Track consistency between separate curation efforts
3. **API layer** - REST endpoint for programmatic ingredient search

### Long Term
1. **Bidirectional sync** - Keep MediaIngredientMech and CultureMech aligned
2. **KG expansion** - Ingest curated mappings back into KG-Microbe
3. **Cross-validation** - Leverage kg-microbe's media composition data for quality assurance

---

## File Reference Guide

| Purpose | Path | Type |
|---------|------|------|
| **Import from CultureMech** | `scripts/import_from_culturemech.py` | Python |
| **Ontology Client** | `src/mediaingredientmech/utils/ontology_client.py` | Python |
| **CultureMech OAK** | `../CultureMech/src/culturemech/ontology/oak_client.py` | Python |
| **CultureMech OLS** | `../CultureMech/src/culturemech/ontology/ols_client.py` | Python |
| **KGX Export** | `../CultureMech/src/culturemech/export/kgx_export.py` | Python |
| **KG-Microbe Query** | `../kg-microbe/kg_microbe/query.py` | Python |
| **Mapped Ingredients** | `../CultureMech/output/mapped_ingredients.yaml` | YAML |
| **Curation Schema** | `src/mediaingredientmech/schema/mediaingredientmech.yaml` | YAML |

---

**Document Version**: 1.0  
**Last Updated**: 2026-03-10  
**Status**: Complete and ready for integration work
