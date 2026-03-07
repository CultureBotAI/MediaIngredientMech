# MediaIngredientMech Schema

LinkML schema for curating media ingredient ontology mappings with LLM assistance tracking. Provides structured workflow for mapping ingredients to CHEBI/FOODON terms with full audit trails.

URI: https://w3id.org/mediaingredientmech

Name: mediaingredientmech-schema



## Classes

| Class | Description |
| --- | --- |
| [CurationEvent](CurationEvent.md) | Audit trail entry for a curation action |
| [IngredientCollection](IngredientCollection.md) | Root container for all ingredient records |
| [IngredientRecord](IngredientRecord.md) | Core record for a media ingredient with ontology mapping, synonyms, and curat... |
| [IngredientSynonym](IngredientSynonym.md) | Alternative name or raw text variant for an ingredient |
| [MappingEvidence](MappingEvidence.md) | Evidence for an ontology mapping |
| [OccurrenceStats](OccurrenceStats.md) | Statistics about ingredient usage across media |
| [OntologyMapping](OntologyMapping.md) | Mapping to an ontology term (CHEBI, FOODON, etc |



## Slots

| Slot | Description |
| --- | --- |
| [action](action.md) | Type of curation action |
| [changes](changes.md) | Description of what changed |
| [concentration_range](concentration_range.md) | Observed concentration range (if available) |
| [confidence_score](confidence_score.md) | Confidence score (0 |
| [curation_history](curation_history.md) | Audit trail of all curation actions |
| [curator](curator.md) | Who performed this action (username or system) |
| [evidence](evidence.md) | Evidence supporting this mapping |
| [evidence_type](evidence_type.md) | Type of evidence |
| [generation_date](generation_date.md) | Timestamp when this collection was generated |
| [identifier](identifier.md) | Unique identifier - either ontology ID (e |
| [ingredients](ingredients.md) | List of all ingredient records |
| [llm_assisted](llm_assisted.md) | Whether LLM assistance was used |
| [llm_model](llm_model.md) | LLM model identifier (if llm_assisted=true) |
| [mapped_count](mapped_count.md) | Number of mapped ingredients |
| [mapping_quality](mapping_quality.md) | Quality assessment of this mapping |
| [mapping_status](mapping_status.md) | Current mapping status |
| [media_count](media_count.md) | Number of unique media containing this ingredient |
| [new_status](new_status.md) | Status after this action |
| [notes](notes.md) | Free-text curation notes |
| [occurrence_count](occurrence_count.md) | Number of times this variant appears |
| [occurrence_statistics](occurrence_statistics.md) | Usage statistics across media recipes |
| [ontology_id](ontology_id.md) | Ontology term ID in CURIE format (e |
| [ontology_label](ontology_label.md) | Human-readable label for the term |
| [ontology_mapping](ontology_mapping.md) | Ontology term mapping (CHEBI/FOODON) |
| [ontology_source](ontology_source.md) | Source ontology |
| [preferred_term](preferred_term.md) | Canonical name for this ingredient |
| [previous_status](previous_status.md) | Status before this action |
| [sample_media](sample_media.md) | Sample media names (for reference) |
| [source](source.md) | Source of evidence (e |
| [synonym_text](synonym_text.md) | The synonym text |
| [synonym_type](synonym_type.md) | Type of synonym |
| [synonyms](synonyms.md) | Alternative names and raw text variants |
| [timestamp](timestamp.md) | When this action occurred |
| [total_count](total_count.md) | Total number of ingredient records |
| [total_occurrences](total_occurrences.md) | Total number of occurrences across all media |
| [unmapped_count](unmapped_count.md) | Number of unmapped ingredients |


## Enumerations

| Enumeration | Description |
| --- | --- |
| [CurationActionEnum](CurationActionEnum.md) |  |
| [EvidenceTypeEnum](EvidenceTypeEnum.md) |  |
| [MappingQualityEnum](MappingQualityEnum.md) |  |
| [MappingStatusEnum](MappingStatusEnum.md) |  |
| [OntologySourceEnum](OntologySourceEnum.md) |  |
| [SynonymTypeEnum](SynonymTypeEnum.md) |  |


## Types

| Type | Description |
| --- | --- |
| [Boolean](Boolean.md) | A binary (true or false) value |
| [Curie](Curie.md) | a compact URI |
| [Date](Date.md) | a date (year, month and day) in an idealized calendar |
| [DateOrDatetime](DateOrDatetime.md) | Either a date or a datetime |
| [Datetime](Datetime.md) | The combination of a date and time |
| [Decimal](Decimal.md) | A real number with arbitrary precision that conforms to the xsd:decimal speci... |
| [Double](Double.md) | A real number that conforms to the xsd:double specification |
| [Float](Float.md) | A real number that conforms to the xsd:float specification |
| [Integer](Integer.md) | An integer |
| [Jsonpath](Jsonpath.md) | A string encoding a JSON Path |
| [Jsonpointer](Jsonpointer.md) | A string encoding a JSON Pointer |
| [Ncname](Ncname.md) | Prefix part of CURIE |
| [Nodeidentifier](Nodeidentifier.md) | A URI, CURIE or BNODE that represents a node in a model |
| [Objectidentifier](Objectidentifier.md) | A URI or CURIE that represents an object in the model |
| [Sparqlpath](Sparqlpath.md) | A string encoding a SPARQL Property Path |
| [String](String.md) | A character string |
| [Time](Time.md) | A time object represents a (local) time of day, independent of any particular... |
| [Uri](Uri.md) | a complete URI |
| [Uriorcurie](Uriorcurie.md) | a URI or a CURIE |


## Subsets

| Subset | Description |
| --- | --- |
