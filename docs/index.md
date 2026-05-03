# MediaIngredientMech Schema

LinkML schema for curating media ingredient ontology mappings with LLM assistance tracking. Provides structured workflow for mapping ingredients to CHEBI/FOODON terms with full audit trails.

URI: https://w3id.org/mediaingredientmech

Name: mediaingredientmech-schema



## Classes

| Class | Description |
| --- | --- |
| [CellularRoleAssignment](CellularRoleAssignment.md) | Assignment of a cellular/metabolic role in organism metabolism with supportin... |
| [ChemicalProperties](ChemicalProperties.md) | Chemical structure and properties for CHEBI-mapped ingredients |
| [CurationEvent](CurationEvent.md) | Audit trail entry for a curation action |
| [IngredientCollection](IngredientCollection.md) | Root container for all ingredient records |
| [IngredientRecord](IngredientRecord.md) | Core record for a media ingredient with ontology mapping, synonyms, and curat... |
| [IngredientSynonym](IngredientSynonym.md) | Alternative name or raw text variant for an ingredient |
| [MappingEvidence](MappingEvidence.md) | Evidence for an ontology mapping |
| [OccurrenceStats](OccurrenceStats.md) | Statistics about ingredient usage across media |
| [OntologyMapping](OntologyMapping.md) | Mapping to an ontology term (CHEBI, FOODON, etc |
| [RoleAssignment](RoleAssignment.md) | Assignment of a functional role in growth medium formulation with supporting ... |
| [RoleCitation](RoleCitation.md) | Citation supporting a role assignment (DOI, publication, database reference) |



## Slots

| Slot | Description |
| --- | --- |
| [action](action.md) | Type of curation action |
| [cas_rn](cas_rn.md) | Chemical Abstracts Service Registry Number (CAS-RN) in format XXX-XX-X or XXX... |
| [cellular_roles](cellular_roles.md) | Cellular/metabolic roles in organism metabolism (e |
| [changes](changes.md) | Description of what changed |
| [chemical_properties](chemical_properties.md) | Chemical structure and properties (for CHEBI-mapped ingredients only) |
| [child_ingredients](child_ingredients.md) | List of child ingredient IDs in hierarchy |
| [concentration_range](concentration_range.md) | Observed concentration range (if available) |
| [confidence](confidence.md) | Confidence score for this role assignment (0 |
| [confidence_score](confidence_score.md) | Confidence score (0 |
| [culturemech_medium_name](culturemech_medium_name.md) | Cross-reference to CultureMech medium name if this is a defined medium |
| [curation_history](curation_history.md) | Audit trail of all curation actions |
| [curator](curator.md) | Who performed this action (username or system) |
| [curator_note](curator_note.md) | Curator's explanation of why this supports the role assignment |
| [data_source](data_source.md) | Source of chemical properties (e |
| [doi](doi.md) | Digital Object Identifier (e |
| [evidence](evidence.md) | Evidence supporting this mapping |
| [evidence_type](evidence_type.md) | Type of evidence |
| [excerpt](excerpt.md) | Relevant excerpt or quote from the source |
| [explanation](explanation.md) | Curator (or LLM)'s rationale connecting the snippet to the |
| [generation_date](generation_date.md) | Timestamp when this collection was generated |
| [inchi](inchi.md) | IUPAC International Chemical Identifier |
| [ingredient_type](ingredient_type.md) | Classification of entry type: single chemical ingredient vs complex defined m... |
| [ingredients](ingredients.md) | List of all ingredient records |
| [kg_microbe_node_id](kg_microbe_node_id.md) | KG-Microbe node ID for this ingredient when found in the KG exactly |
| [llm_assisted](llm_assisted.md) | Whether LLM assistance was used |
| [llm_model](llm_model.md) | LLM model identifier (if llm_assisted=true) |
| [mapped_count](mapped_count.md) | Number of mapped ingredients |
| [mapping_quality](mapping_quality.md) | Quality assessment of this mapping |
| [mapping_status](mapping_status.md) | Current mapping status |
| [match_level](match_level.md) | Technical method used to find this mapping |
| [media_count](media_count.md) | Number of unique media containing this ingredient |
| [media_roles](media_roles.md) | Functional roles in growth medium formulation (e |
| [merged](merged.md) | List of MediaIngredientMech IDs merged into this representative |
| [metabolic_context](metabolic_context.md) | Pathway or metabolic context (e |
| [molecular_formula](molecular_formula.md) | Molecular formula (e |
| [molecular_weight](molecular_weight.md) | Molecular weight in g/mol |
| [new_status](new_status.md) | Status after this action |
| [notes](notes.md) | Free-text curation notes |
| [occurrence_count](occurrence_count.md) | Number of times this variant appears |
| [occurrence_statistics](occurrence_statistics.md) | Usage statistics across media recipes |
| [ontology_id](ontology_id.md) | Unique ontology identifier - either ontology ID (e |
| [ontology_label](ontology_label.md) | Human-readable label for the term |
| [ontology_mapping](ontology_mapping.md) | Ontology term mapping (CHEBI/FOODON) |
| [ontology_source](ontology_source.md) | Source ontology |
| [parent_ingredient](parent_ingredient.md) | Reference to parent ingredient in hierarchy (MediaIngredientMech:XXXXXX) |
| [pmid](pmid.md) | PubMed ID for MEDLINE citations (e |
| [preferred_term](preferred_term.md) | Canonical name for this ingredient |
| [previous_status](previous_status.md) | Status before this action |
| [reference_text](reference_text.md) | Human-readable citation text |
| [reference_type](reference_type.md) | Type of reference (peer-reviewed, database, manual curation, etc |
| [representative](representative.md) | ID of the representative record if this record has been merged |
| [retrieval_date](retrieval_date.md) | When these properties were retrieved |
| [role](role.md) | The functional role (e |
| [role_inheritance](role_inheritance.md) | If true, inherits media_roles from parent ingredient |
| [sample_media](sample_media.md) | Sample media names (for reference) |
| [smiles](smiles.md) | Simplified Molecular Input Line Entry System notation |
| [snippet](snippet.md) | Exact substring quoted from the cited abstract that supports |
| [solution_type](solution_type.md) | Type of solution if this is a stock/pre-mix rather than individual chemical |
| [source](source.md) | Source of evidence (e |
| [supports](supports.md) | How the cited reference relates to the mapping claim |
| [synonym_text](synonym_text.md) | The synonym text |
| [synonym_type](synonym_type.md) | Type of synonym |
| [synonyms](synonyms.md) | Alternative names and raw text variants |
| [timestamp](timestamp.md) | When this action occurred |
| [total_count](total_count.md) | Total number of ingredient records |
| [total_occurrences](total_occurrences.md) | Total number of occurrences across all media |
| [unmapped_count](unmapped_count.md) | Number of unmapped ingredients |
| [url](url.md) | Web URL for the reference |
| [variant_notes](variant_notes.md) | Human-readable explanation of variant distinction from parent/siblings |
| [variant_type](variant_type.md) | Classification of variant relationship to parent |


## Enumerations

| Enumeration | Description |
| --- | --- |
| [CellularRoleEnum](CellularRoleEnum.md) | Cellular and metabolic roles in microbial communities |
| [CitationTypeEnum](CitationTypeEnum.md) | Type of reference or citation |
| [CurationActionEnum](CurationActionEnum.md) |  |
| [EvidenceSupportEnum](EvidenceSupportEnum.md) | How a cited reference relates to the claim it is attached to |
| [EvidenceTypeEnum](EvidenceTypeEnum.md) |  |
| [IngredientRoleEnum](IngredientRoleEnum.md) | Functional roles of ingredients in growth medium formulation |
| [IngredientTypeEnum](IngredientTypeEnum.md) | Classification of ingredient entry type |
| [MappingQualityEnum](MappingQualityEnum.md) |  |
| [MappingStatusEnum](MappingStatusEnum.md) |  |
| [MatchLevelEnum](MatchLevelEnum.md) |  |
| [OntologySourceEnum](OntologySourceEnum.md) |  |
| [SolutionTypeEnum](SolutionTypeEnum.md) | Type of solution for mixture ingredients (stock solutions, pre-mixes) |
| [SynonymTypeEnum](SynonymTypeEnum.md) |  |
| [VariantTypeEnum](VariantTypeEnum.md) | Classification of ingredient variant in hierarchy |


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
