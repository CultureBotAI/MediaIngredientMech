# MediaIngredientMech Schema

LinkML schema for curating media ingredient ontology mappings with LLM assistance tracking. Provides structured workflow for mapping ingredients to CHEBI/FOODON terms with full audit trails.

URI: https://w3id.org/mediaingredientmech

Name: mediaingredientmech-schema



## Classes

| Class | Description |
| --- | --- |
| [CellularMetabolicRoleAssignment](CellularMetabolicRoleAssignment.md) | Assignment of a cellular-metabolic facet role (what the ingredient does insid... |
| [ChemicalProperties](ChemicalProperties.md) | Chemical structure and properties for CHEBI-mapped ingredients |
| [CommunityOrganismRoleAssignment](CommunityOrganismRoleAssignment.md) | Assignment of an organism-in-community role with supporting evidence (e |
| [CurationEvent](CurationEvent.md) | Audit trail entry for a curation action |
| [Dataset](Dataset.md) | A reference to a publicly available dataset (omics, sequence, phenotype) rele... |
| [Discussion](Discussion.md) | A thread-like record of an open question, controversy, curation todo, emergin... |
| [EnvironmentContext](EnvironmentContext.md) | Environmental context annotation for an ingredient |
| [IngredientCollection](IngredientCollection.md) | Root container for all ingredient records |
| [IngredientRecord](IngredientRecord.md) | Core record for a media ingredient with ontology mapping, synonyms, and curat... |
| [IngredientSynonym](IngredientSynonym.md) | Alternative name or raw text variant for an ingredient |
| [MappingEvidence](MappingEvidence.md) | Evidence for an ontology mapping |
| [NutritionalRoleAssignment](NutritionalRoleAssignment.md) | Assignment of a nutritional facet role (what element or macronutrient the ing... |
| [OccurrenceStats](OccurrenceStats.md) | Statistics about ingredient usage across media |
| [OntologyMapping](OntologyMapping.md) | Mapping to an ontology term (CHEBI, FOODON, etc |
| [PhysicochemicalRoleAssignment](PhysicochemicalRoleAssignment.md) | Assignment of a physicochemical facet role (the chemical or physical function... |
| [ProposedExperiment](ProposedExperiment.md) | A lightweight, domain-neutral sketch of an experiment or analysis that could ... |
| [RoleCitation](RoleCitation.md) | Citation supporting a role assignment (DOI, publication, database reference) |
| [StockComponent](StockComponent.md) | One constituent of a stock solution or defined medium recipe — a component in... |
| [SupportingReference](SupportingReference.md) | A lightweight literature/database citation supporting a Discussion or Dataset |



## Slots

| Slot | Description |
| --- | --- |
| [accession](accession.md) | Repository accession or CURIE, e |
| [action](action.md) | Type of curation action |
| [approach](approach.md) | Method/assay in brief (e |
| [attaches_to](attaches_to.md) | Hash-anchor pointers into the sections/nodes this discussion concerns: `<sect... |
| [cas_rn](cas_rn.md) | Chemical Abstracts Service Registry Number (CAS-RN) in format XXX-XX-X or XXX... |
| [category](category.md) | Categorization label for partitioned unmapped collections (e |
| [cellular_metabolic_roles](cellular_metabolic_roles.md) | Role of this ingredient inside/on the cultured microbe (e |
| [changes](changes.md) | Description of what changed |
| [chemical_properties](chemical_properties.md) | Chemical structure and properties (for CHEBI-mapped ingredients only) |
| [child_ingredients](child_ingredients.md) | List of child ingredient `identifier`s in the variant hierarchy |
| [community_organism_roles](community_organism_roles.md) | Role(s) this organism plays in a microbial community (e |
| [component_id](component_id.md) | Identifier of the component when mapped to an ontology/registry term (e |
| [component_name](component_name.md) | Component ingredient name as listed in the recipe (e |
| [components](components.md) | Recipe-level decomposition for a STOCK_SOLUTION or DEFINED_MEDIUM: the list o... |
| [concentration_range](concentration_range.md) | Observed concentration range (if available) |
| [concentration_unit](concentration_unit.md) | Unit for concentration_value (e |
| [concentration_value](concentration_value.md) | Amount/concentration of the component, kept as a string to preserve the sourc... |
| [conditions](conditions.md) | Experimental conditions / groups represented |
| [confidence](confidence.md) | Confidence score for this role assignment (0 |
| [confidence_score](confidence_score.md) | Confidence score (0 |
| [count](count.md) | Record count for this categorized partition |
| [culturemech_medium_name](culturemech_medium_name.md) | Cross-reference to CultureMech medium name if this is a defined medium |
| [curation_history](curation_history.md) | Audit trail of all curation actions |
| [curator](curator.md) | Who performed this action (username or system) |
| [curator_note](curator_note.md) | Curator's explanation of why this supports the role assignment |
| [data_source](data_source.md) | Source of chemical properties (e |
| [dataset_type](dataset_type.md) |  |
| [datasets](datasets.md) | Public datasets (omics/sequence/phenotype) relevant to this ingredient |
| [decision_criterion](decision_criterion.md) | The observation that would settle the question |
| [description](description.md) |  |
| [discussion_id](discussion_id.md) | Stable local identifier for this discussion thread |
| [discussions](discussions.md) | Open questions, knowledge gaps, controversies, and curation todos attached to... |
| [doi](doi.md) | Digital Object Identifier (e |
| [environment_label](environment_label.md) | Canonical ENVO label for environment_term |
| [environment_term](environment_term.md) | ENVO term CURIE (e |
| [environmental_context](environmental_context.md) | Environmental contexts where this ingredient is relevant |
| [evidence](evidence.md) | Evidence supporting this mapping |
| [evidence_source](evidence_source.md) | How the snippet was obtained (e |
| [evidence_type](evidence_type.md) | Type of evidence |
| [excerpt](excerpt.md) | Relevant excerpt or quote from the source |
| [experiment_id](experiment_id.md) | Stable local id (optional; for cross-reference) |
| [explanation](explanation.md) | Curator (or LLM)'s rationale connecting the snippet to the |
| [findings](findings.md) | Brief note on what the dataset shows relevant to this record |
| [generation_date](generation_date.md) | Timestamp when this collection was generated |
| [identifier](identifier.md) | Primary key for the record |
| [inchi](inchi.md) | IUPAC International Chemical Identifier |
| [ingredient_type](ingredient_type.md) | Classification of entry type: single chemical ingredient vs complex defined m... |
| [ingredients](ingredients.md) | List of all ingredient records |
| [kg_microbe_node_id](kg_microbe_node_id.md) | KG-Microbe node ID for this ingredient when found in the KG exactly |
| [kind](kind.md) |  |
| [llm_assisted](llm_assisted.md) | Whether LLM assistance was used |
| [llm_model](llm_model.md) | LLM model identifier (if llm_assisted=true) |
| [mapped_count](mapped_count.md) | Number of mapped ingredients |
| [mapping_quality](mapping_quality.md) | Quality assessment of this mapping |
| [mapping_status](mapping_status.md) | Current mapping status |
| [match_level](match_level.md) | Technical method used to find this mapping |
| [media_count](media_count.md) | Number of unique media containing this ingredient |
| [merged](merged.md) | List of record `identifier`s merged into this representative |
| [metabolic_context](metabolic_context.md) | Pathway or metabolic context (e |
| [model_systems](model_systems.md) | Systems to use (e |
| [molecular_formula](molecular_formula.md) | Molecular formula (e |
| [molecular_weight](molecular_weight.md) | Molecular weight in g/mol |
| [name](name.md) |  |
| [new_status](new_status.md) | Status after this action |
| [notes](notes.md) | Free-text curation notes |
| [nutritional_roles](nutritional_roles.md) | What element or macronutrient this ingredient supplies to the medium (e |
| [occurrence_count](occurrence_count.md) | Number of times this variant appears |
| [occurrence_statistics](occurrence_statistics.md) | Usage statistics across media recipes |
| [ontology_id](ontology_id.md) | Ontology term ID in CURIE format |
| [ontology_label](ontology_label.md) | Canonical OBO label for ontology_id (e |
| [ontology_mapping](ontology_mapping.md) | Ontology term mapping (CHEBI/FOODON) |
| [ontology_source](ontology_source.md) | Source ontology |
| [organism](organism.md) | Source organism / community label (free text or CURIE) |
| [parent_ingredient](parent_ingredient.md) | Reference to parent ingredient's `identifier` in the variant hierarchy |
| [perturbations](perturbations.md) | Interventions applied (e |
| [physicochemical_roles](physicochemical_roles.md) | Chemical or physical function this ingredient performs in the medium (e |
| [platform](platform.md) | Sequencing/assay platform |
| [pmid](pmid.md) | PubMed ID for MEDLINE citations (e |
| [posed_by](posed_by.md) | Curator or agent that raised the discussion |
| [posed_date](posed_date.md) |  |
| [preferred_term](preferred_term.md) | Canonical name for this ingredient |
| [previous_status](previous_status.md) | Status before this action |
| [prompt](prompt.md) | The open question, gap statement, or todo, in one or two sentences |
| [proposed_experiments](proposed_experiments.md) | Optional sketches of how the gap could be resolved |
| [pubchem_cid](pubchem_cid.md) | PubChem Compound Identifier (CID), stored as a positive integer |
| [publication](publication.md) | Associated publication reference (e |
| [rationale](rationale.md) | Why this matters / what resolving it would change |
| [readouts](readouts.md) | What would be measured |
| [reference](reference.md) | PMID: |
| [reference_text](reference_text.md) | Human-readable citation text |
| [reference_title](reference_title.md) | Title of the cited source (optional; populated by tooling) |
| [reference_type](reference_type.md) | Type of reference (peer-reviewed, database, manual curation, etc |
| [relevance](relevance.md) | Why this ingredient is relevant to the specified environment |
| [repository](repository.md) |  |
| [representative](representative.md) | `identifier` of the representative record if this record has been merged |
| [resolution_note](resolution_note.md) | How it was resolved (when status is RESOLVED) |
| [resolved_date](resolved_date.md) |  |
| [retrieval_date](retrieval_date.md) | When these properties were retrieved |
| [role](role.md) | The community/ecological role of the organism (e |
| [role_inheritance](role_inheritance.md) | If true, inherits the three role facets (nutritional_roles, physicochemical_r... |
| [sample_count](sample_count.md) |  |
| [sample_media](sample_media.md) | Sample media names (for reference) |
| [sample_types](sample_types.md) | Sample/material types represented (free text or term labels) |
| [smiles](smiles.md) | Simplified Molecular Input Line Entry System notation |
| [snippet](snippet.md) | Exact substring quoted from the cited abstract that supports |
| [solution_type](solution_type.md) | Type of solution if this is a stock/pre-mix rather than individual chemical |
| [source](source.md) | Source of evidence (e |
| [status](status.md) |  |
| [supports](supports.md) | How the cited reference relates to the mapping claim |
| [synonym_text](synonym_text.md) | The synonym text |
| [synonym_type](synonym_type.md) | Type of synonym |
| [synonyms](synonyms.md) | Alternative names and raw text variants |
| [timestamp](timestamp.md) | When this action occurred |
| [title](title.md) | Short dataset title |
| [total_count](total_count.md) | Total number of ingredient records |
| [total_occurrences](total_occurrences.md) | Total number of occurrences across all media |
| [unmapped_count](unmapped_count.md) | Number of unmapped ingredients |
| [url](url.md) | Web URL for the reference |
| [variant_notes](variant_notes.md) | Human-readable explanation of variant distinction from parent/siblings |
| [variant_type](variant_type.md) | Classification of variant relationship to parent |
| [would_refute](would_refute.md) | Outcome that would refute it |
| [would_support](would_support.md) | Outcome that would support the hypothesis/assertion |


## Enumerations

| Enumeration | Description |
| --- | --- |
| [CellularMetabolicRoleEnum](CellularMetabolicRoleEnum.md) | Role of the ingredient inside or on the cultured microbe(s) — the compound's ... |
| [CitationTypeEnum](CitationTypeEnum.md) | Type of reference or citation |
| [CommunityOrganismRoleEnum](CommunityOrganismRoleEnum.md) | Role an organism plays in a microbial community (formerly `CellularRoleEnum`;... |
| [CurationActionEnum](CurationActionEnum.md) | Documentation-only reference list of well-known curation action labels |
| [DatasetRepositoryEnum](DatasetRepositoryEnum.md) | Public repository hosting the dataset |
| [DatasetTypeEnum](DatasetTypeEnum.md) | Type of dataset or data resource |
| [DiscussionKindEnum](DiscussionKindEnum.md) | Kind of unresolved / in-progress item captured by a Discussion |
| [DiscussionStatusEnum](DiscussionStatusEnum.md) | Lifecycle status for a Discussion |
| [EnvironmentRelevanceEnum](EnvironmentRelevanceEnum.md) | Describes why an ingredient is relevant to a particular environment |
| [EvidenceSupportEnum](EvidenceSupportEnum.md) | How a cited reference relates to the claim it is attached to |
| [EvidenceTypeEnum](EvidenceTypeEnum.md) |  |
| [IngredientTypeEnum](IngredientTypeEnum.md) | Classification of ingredient entry type |
| [MappingQualityEnum](MappingQualityEnum.md) |  |
| [MappingStatusEnum](MappingStatusEnum.md) |  |
| [MatchLevelEnum](MatchLevelEnum.md) |  |
| [NutritionalRoleEnum](NutritionalRoleEnum.md) | What element or macronutrient an ingredient supplies to the medium |
| [OntologySourceEnum](OntologySourceEnum.md) |  |
| [PhysicochemicalRoleEnum](PhysicochemicalRoleEnum.md) | Chemical or physical function an ingredient performs in the medium, independe... |
| [SolutionTypeEnum](SolutionTypeEnum.md) | Type of solution for mixture ingredients (stock solutions, pre-mixes) |
| [SupportLevelEnum](SupportLevelEnum.md) | How a SupportingReference bears on the claim it is attached to (mirrors the s... |
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
