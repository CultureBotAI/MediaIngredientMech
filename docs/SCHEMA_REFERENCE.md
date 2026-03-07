# Schema Reference

Complete reference for the MediaIngredientMech LinkML schema. The schema defines structured data classes for media ingredient ontology mappings with curation audit trails.

**Schema source**: `src/mediaingredientmech/schema/mediaingredientmech.yaml`

**Schema ID**: `https://w3id.org/mediaingredientmech`

## Classes

### IngredientCollection

Root container for all ingredient records. This is the tree root class.

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `generation_date` | datetime | No | Timestamp when this collection was generated |
| `total_count` | integer | No | Total number of ingredient records |
| `mapped_count` | integer | No | Number of mapped ingredients |
| `unmapped_count` | integer | No | Number of unmapped ingredients |
| `ingredients` | IngredientRecord[] | No | List of all ingredient records |

Example:

```yaml
generation_date: "2026-03-06T10:00:00"
total_count: 1131
mapped_count: 995
unmapped_count: 136
ingredients:
  - identifier: CHEBI:26710
    preferred_term: sodium chloride
    mapping_status: MAPPED
    # ...
```

### IngredientRecord

Core record for a media ingredient. Represents either a mapped ingredient (with `ontology_mapping`) or unmapped ingredient (needs curation).

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `identifier` | string (ID) | Yes | Unique identifier. Ontology ID for mapped (e.g., `CHEBI:26710`) or placeholder for unmapped (e.g., `UNMAPPED_001`) |
| `preferred_term` | string | Yes | Canonical name for this ingredient |
| `ontology_mapping` | OntologyMapping | No | Ontology term mapping |
| `synonyms` | IngredientSynonym[] | No | Alternative names and raw text variants |
| `mapping_status` | MappingStatusEnum | Yes | Current mapping status |
| `occurrence_statistics` | OccurrenceStats | No | Usage statistics across media recipes |
| `curation_history` | CurationEvent[] | No | Audit trail of all curation actions |
| `notes` | string | No | Free-text curation notes |

Example (mapped ingredient):

```yaml
identifier: CHEBI:26710
preferred_term: sodium chloride
mapping_status: MAPPED
ontology_mapping:
  ontology_id: CHEBI:26710
  ontology_label: sodium chloride
  ontology_source: CHEBI
  mapping_quality: EXACT_MATCH
synonyms:
  - synonym_text: NaCl
    synonym_type: ABBREVIATION
  - synonym_text: "table salt"
    synonym_type: COMMON_NAME
```

Example (unmapped ingredient):

```yaml
identifier: UNMAPPED_042
preferred_term: trace element solution SL-10
mapping_status: NEEDS_EXPERT
notes: "Complex formulation, requires domain expert to decompose"
```

### OntologyMapping

Mapping to an ontology term (CHEBI, FOODON, etc.).

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `ontology_id` | string | Yes | Ontology term ID in CURIE format. Must match pattern `^[A-Z]+:[0-9]+$` |
| `ontology_label` | string | Yes | Human-readable label for the term |
| `ontology_source` | OntologySourceEnum | Yes | Source ontology |
| `mapping_quality` | MappingQualityEnum | Yes | Quality assessment of this mapping |
| `evidence` | MappingEvidence[] | No | Evidence supporting this mapping |

Example:

```yaml
ontology_id: CHEBI:26710
ontology_label: sodium chloride
ontology_source: CHEBI
mapping_quality: EXACT_MATCH
evidence:
  - evidence_type: DATABASE_MATCH
    source: OLS
    confidence_score: 1.0
```

### Validation Rules for `ontology_id`

The `ontology_id` field must be a valid CURIE matching `^[A-Z]+:[0-9]+$`:

| Valid | Invalid |
|-------|---------|
| `CHEBI:26710` | `chebi:26710` (lowercase prefix) |
| `FOODON:03301439` | `CHEBI_26710` (underscore instead of colon) |
| `NCIT:C919` | (would be invalid since C is not a digit) |

### MappingEvidence

Evidence supporting an ontology mapping.

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `evidence_type` | EvidenceTypeEnum | Yes | Type of evidence |
| `source` | string | No | Source of evidence (database name, curator name) |
| `confidence_score` | float | No | Confidence score from 0.0 to 1.0 |
| `notes` | string | No | Additional context |

Example:

```yaml
evidence_type: LLM_SUGGESTION
source: "claude-sonnet-4-5"
confidence_score: 0.92
notes: "High confidence match based on chemical name similarity"
```

### IngredientSynonym

Alternative name or raw text variant for an ingredient.

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `synonym_text` | string | Yes | The synonym text |
| `synonym_type` | SynonymTypeEnum | No | Type of synonym |
| `source` | string | No | Where this synonym came from |
| `occurrence_count` | integer | No | Number of times this variant appears |

Example:

```yaml
synonym_text: NaCl
synonym_type: ABBREVIATION
source: CultureMech
occurrence_count: 312
```

### OccurrenceStats

Statistics about ingredient usage across media recipes.

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `total_occurrences` | integer | Yes | Total number of occurrences across all media |
| `media_count` | integer | Yes | Number of unique media containing this ingredient |
| `sample_media` | string[] | No | Sample media names for reference |
| `concentration_range` | string | No | Observed concentration range (if available) |

Example:

```yaml
total_occurrences: 847
media_count: 847
sample_media:
  - "Luria-Bertani Medium"
  - "Tryptic Soy Broth"
concentration_range: "0.5-10 g/L"
```

### CurationEvent

Audit trail entry for a curation action. Every change to an ingredient record should produce a CurationEvent.

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `timestamp` | datetime | Yes | When this action occurred |
| `curator` | string | Yes | Who performed this action (username or "system") |
| `action` | CurationActionEnum | Yes | Type of curation action |
| `changes` | string | No | Description of what changed |
| `previous_status` | MappingStatusEnum | No | Status before this action |
| `new_status` | MappingStatusEnum | No | Status after this action |
| `llm_assisted` | boolean | No | Whether LLM assistance was used |
| `llm_model` | string | No | LLM model identifier (if `llm_assisted` is true) |
| `notes` | string | No | Additional context for this action |

Example:

```yaml
timestamp: "2026-03-06T10:30:00"
curator: jsmith
action: MAPPED
changes: "Added CHEBI mapping for sodium chloride"
previous_status: UNMAPPED
new_status: MAPPED
llm_assisted: true
llm_model: "claude-sonnet-4-5"
notes: "Verified LLM suggestion against OLS"
```

## Enums

### MappingStatusEnum

Tracks the current mapping state of an ingredient record.

| Value | Description | Typical Next States |
|-------|-------------|-------------------|
| `MAPPED` | Has valid ontology mapping | REJECTED (if found incorrect) |
| `UNMAPPED` | No ontology mapping exists | IN_PROGRESS, NEEDS_EXPERT, AMBIGUOUS, MAPPED |
| `PENDING_REVIEW` | Suggested mapping awaiting review | MAPPED, REJECTED |
| `IN_PROGRESS` | Currently being curated | MAPPED, NEEDS_EXPERT, AMBIGUOUS |
| `NEEDS_EXPERT` | Requires expert domain knowledge | MAPPED, AMBIGUOUS |
| `AMBIGUOUS` | Multiple possible interpretations | MAPPED, NEEDS_EXPERT, REJECTED |
| `REJECTED` | Determined to be invalid or duplicate | (terminal state) |

### MappingQualityEnum

Quality assessment of an ontology mapping.

| Value | Description | Typical Confidence |
|-------|-------------|-------------------|
| `EXACT_MATCH` | Direct exact match to ontology term label | 1.0 |
| `SYNONYM_MATCH` | Matches known synonym in ontology | 0.9-1.0 |
| `CLOSE_MATCH` | Semantically close but not exact | 0.7-0.9 |
| `MANUAL_CURATION` | Manually curated by expert | Varies |
| `LLM_ASSISTED` | Mapping suggested by LLM, human-verified | 0.7-0.95 |
| `PROVISIONAL` | Tentative mapping needing verification | <0.7 |

### OntologySourceEnum

Supported source ontologies.

| Value | Full Name | Prefix URI |
|-------|-----------|------------|
| `CHEBI` | Chemical Entities of Biological Interest | `http://purl.obolibrary.org/obo/CHEBI_` |
| `FOODON` | Food Ontology | `http://purl.obolibrary.org/obo/FOODON_` |
| `NCIT` | NCI Thesaurus | `http://purl.obolibrary.org/obo/NCIT_` |
| `MESH` | Medical Subject Headings | `http://id.nlm.nih.gov/mesh/` |
| `UBERON` | Uber Anatomy Ontology | `http://purl.obolibrary.org/obo/UBERON_` |
| `ENVO` | Environment Ontology | `http://purl.obolibrary.org/obo/ENVO_` |

### CurationActionEnum

Types of curation actions recorded in the audit trail.

| Value | Description | Creates History Entry |
|-------|-------------|----------------------|
| `CREATED` | Record created | Yes - initial record |
| `IMPORTED` | Imported from external source | Yes - with source info |
| `MAPPED` | Ontology mapping added | Yes - with mapping details |
| `SYNONYM_ADDED` | Synonym added | Yes |
| `VALIDATED` | Mapping validated | Yes - confirms correctness |
| `CORRECTED` | Mapping or data corrected | Yes - with before/after |
| `MERGED` | Merged with another record | Yes - with merge source |
| `STATUS_CHANGED` | Mapping status changed | Yes - with old/new status |
| `ANNOTATED` | Notes or metadata added | Yes |

### SynonymTypeEnum

Types of synonyms for an ingredient.

| Value | Description | Example |
|-------|-------------|---------|
| `EXACT_SYNONYM` | Exact alternative name | "table salt" for sodium chloride |
| `RELATED_SYNONYM` | Related but not identical | "saline" for sodium chloride |
| `RAW_TEXT` | Raw text from original data | "NaCl (5g/L)" |
| `ABBREVIATION` | Abbreviated form | "NaCl" |
| `COMMON_NAME` | Common or colloquial name | "table salt" |
| `SYSTEMATIC_NAME` | Systematic chemical name | "sodium chloride" |

### EvidenceTypeEnum

Types of evidence supporting a mapping.

| Value | Description | Example Source |
|-------|-------------|--------------|
| `DATABASE_MATCH` | Direct match in ontology database | OLS, OAK |
| `CURATOR_JUDGMENT` | Expert curator decision | Curator username |
| `LLM_SUGGESTION` | LLM-generated suggestion | Model identifier |
| `LITERATURE` | Based on literature evidence | PubMed ID |
| `TEXT_SIMILARITY` | Based on text similarity metrics | Algorithm name |
| `CROSS_REFERENCE` | Cross-reference to other database | Database name |

## Prefix Definitions

The schema uses these CURIE prefixes:

| Prefix | URI |
|--------|-----|
| `linkml` | `https://w3id.org/linkml/` |
| `mediaingredientmech` | `https://w3id.org/mediaingredientmech/` |
| `CHEBI` | `http://purl.obolibrary.org/obo/CHEBI_` |
| `FOODON` | `http://purl.obolibrary.org/obo/FOODON_` |
| `NCIT` | `http://purl.obolibrary.org/obo/NCIT_` |
| `MESH` | `http://id.nlm.nih.gov/mesh/` |
| `UBERON` | `http://purl.obolibrary.org/obo/UBERON_` |
| `ENVO` | `http://purl.obolibrary.org/obo/ENVO_` |

## Related Documentation

- [Curation Guide](CURATION_GUIDE.md) - How to curate ingredients using this schema
- [Workflows](WORKFLOWS.md) - Common operations and CultureMech integration
