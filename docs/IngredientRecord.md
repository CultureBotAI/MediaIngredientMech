

# Class: IngredientRecord 


_Core record for a media ingredient with ontology mapping, synonyms, and curation history. Represents either a mapped ingredient (with a primary ontology, registry, or local identity CURIE) or an unmapped ingredient (placeholder identifier, awaits curation). Can serve as root element for individual YAML files or as elements in IngredientCollection._





URI: [mediaingredientmech:IngredientRecord](https://w3id.org/mediaingredientmech/IngredientRecord)





```mermaid
 classDiagram
    class IngredientRecord
    click IngredientRecord href "../IngredientRecord/"
      IngredientRecord : cellular_metabolic_roles
        
          
    
        
        
        IngredientRecord --> "*" CellularMetabolicRoleAssignment : cellular_metabolic_roles
        click CellularMetabolicRoleAssignment href "../CellularMetabolicRoleAssignment/"
    

        
      IngredientRecord : chemical_properties
        
          
    
        
        
        IngredientRecord --> "0..1" ChemicalProperties : chemical_properties
        click ChemicalProperties href "../ChemicalProperties/"
    

        
      IngredientRecord : community_organism_roles
        
          
    
        
        
        IngredientRecord --> "*" CommunityOrganismRoleAssignment : community_organism_roles
        click CommunityOrganismRoleAssignment href "../CommunityOrganismRoleAssignment/"
    

        
      IngredientRecord : component_assertion
        
          
    
        
        
        IngredientRecord --> "0..1" ComponentAssertion : component_assertion
        click ComponentAssertion href "../ComponentAssertion/"
    

        
      IngredientRecord : components
        
          
    
        
        
        IngredientRecord --> "*" StockComponent : components
        click StockComponent href "../StockComponent/"
    

        
      IngredientRecord : culturemech_reference
        
          
    
        
        
        IngredientRecord --> "0..1" CultureMechReference : culturemech_reference
        click CultureMechReference href "../CultureMechReference/"
    

        
      IngredientRecord : curation_history
        
          
    
        
        
        IngredientRecord --> "*" CurationEvent : curation_history
        click CurationEvent href "../CurationEvent/"
    

        
      IngredientRecord : datasets
        
          
    
        
        
        IngredientRecord --> "*" Dataset : datasets
        click Dataset href "../Dataset/"
    

        
      IngredientRecord : discussions
        
          
    
        
        
        IngredientRecord --> "*" Discussion : discussions
        click Discussion href "../Discussion/"
    

        
      IngredientRecord : environmental_context
        
          
    
        
        
        IngredientRecord --> "*" EnvironmentContext : environmental_context
        click EnvironmentContext href "../EnvironmentContext/"
    

        
      IngredientRecord : identifier
        
      IngredientRecord : ingredient_type
        
          
    
        
        
        IngredientRecord --> "0..1" IngredientTypeEnum : ingredient_type
        click IngredientTypeEnum href "../IngredientTypeEnum/"
    

        
      IngredientRecord : kg_microbe_node_id
        
      IngredientRecord : mapping_status
        
          
    
        
        
        IngredientRecord --> "1" MappingStatusEnum : mapping_status
        click MappingStatusEnum href "../MappingStatusEnum/"
    

        
      IngredientRecord : merged
        
      IngredientRecord : notes
        
      IngredientRecord : nutritional_roles
        
          
    
        
        
        IngredientRecord --> "*" NutritionalRoleAssignment : nutritional_roles
        click NutritionalRoleAssignment href "../NutritionalRoleAssignment/"
    

        
      IngredientRecord : occurrence_statistics
        
          
    
        
        
        IngredientRecord --> "0..1" OccurrenceStats : occurrence_statistics
        click OccurrenceStats href "../OccurrenceStats/"
    

        
      IngredientRecord : ontology_mapping
        
          
    
        
        
        IngredientRecord --> "0..1" OntologyMapping : ontology_mapping
        click OntologyMapping href "../OntologyMapping/"
    

        
      IngredientRecord : physicochemical_roles
        
          
    
        
        
        IngredientRecord --> "*" PhysicochemicalRoleAssignment : physicochemical_roles
        click PhysicochemicalRoleAssignment href "../PhysicochemicalRoleAssignment/"
    

        
      IngredientRecord : preferred_term
        
      IngredientRecord : representative
        
      IngredientRecord : solution_type
        
          
    
        
        
        IngredientRecord --> "0..1" SolutionTypeEnum : solution_type
        click SolutionTypeEnum href "../SolutionTypeEnum/"
    

        
      IngredientRecord : supplied_form
        
          
    
        
        
        IngredientRecord --> "*" SuppliedForm : supplied_form
        click SuppliedForm href "../SuppliedForm/"
    

        
      IngredientRecord : synonyms
        
          
    
        
        
        IngredientRecord --> "*" IngredientSynonym : synonyms
        click IngredientSynonym href "../IngredientSynonym/"
    

        
      
```




<!-- no inheritance hierarchy -->


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [identifier](identifier.md) | 1 <br/> [String](String.md) | Semantic identifier for the record and its LinkML identifier slot, but not a ... | direct |
| [preferred_term](preferred_term.md) | 1 <br/> [String](String.md) | Canonical name for this ingredient | direct |
| [ontology_mapping](ontology_mapping.md) | 0..1 <br/> [OntologyMapping](OntologyMapping.md) | Ontology term mapping (CHEBI/FOODON) | direct |
| [synonyms](synonyms.md) | * <br/> [IngredientSynonym](IngredientSynonym.md) | Alternative names and raw text variants | direct |
| [mapping_status](mapping_status.md) | 1 <br/> [MappingStatusEnum](MappingStatusEnum.md) | Current mapping status | direct |
| [occurrence_statistics](occurrence_statistics.md) | 0..1 <br/> [OccurrenceStats](OccurrenceStats.md) | Usage statistics across media recipes | direct |
| [curation_history](curation_history.md) | * <br/> [CurationEvent](CurationEvent.md) | Audit trail of all curation actions | direct |
| [notes](notes.md) | 0..1 <br/> [String](String.md) | Free-text curation notes | direct |
| [community_organism_roles](community_organism_roles.md) | * <br/> [CommunityOrganismRoleAssignment](CommunityOrganismRoleAssignment.md) | Role(s) this organism plays in a microbial community (e | direct |
| [nutritional_roles](nutritional_roles.md) | * <br/> [NutritionalRoleAssignment](NutritionalRoleAssignment.md) | What element or macronutrient this ingredient supplies to the medium (e | direct |
| [physicochemical_roles](physicochemical_roles.md) | * <br/> [PhysicochemicalRoleAssignment](PhysicochemicalRoleAssignment.md) | Chemical or physical function this ingredient performs in the medium (e | direct |
| [cellular_metabolic_roles](cellular_metabolic_roles.md) | * <br/> [CellularMetabolicRoleAssignment](CellularMetabolicRoleAssignment.md) | Role of this ingredient inside/on the cultured microbe (e | direct |
| [solution_type](solution_type.md) | 0..1 <br/> [SolutionTypeEnum](SolutionTypeEnum.md) | Type of solution if this is a stock/pre-mix rather than individual chemical | direct |
| [chemical_properties](chemical_properties.md) | 0..1 <br/> [ChemicalProperties](ChemicalProperties.md) | Chemical structure and properties (for CHEBI-mapped ingredients only) | direct |
| [supplied_form](supplied_form.md) | * <br/> [SuppliedForm](SuppliedForm.md) | The material actually ordered and delivered for this ingredient — the thing o... | direct |
| [representative](representative.md) | 0..1 <br/> [String](String.md) | `identifier` of the representative record if this record has been merged | direct |
| [merged](merged.md) | * <br/> [String](String.md) | List of record `identifier`s merged into this representative | direct |
| [ingredient_type](ingredient_type.md) | 0..1 <br/> [IngredientTypeEnum](IngredientTypeEnum.md) | Classification of entry type: single chemical ingredient vs whole named mediu... | direct |
| [components](components.md) | * <br/> [StockComponent](StockComponent.md) | A has-part decomposition for a STOCK_SOLUTION, NAMED_MEDIUM, or UNDEFINED_MIX... | direct |
| [component_assertion](component_assertion.md) | 0..1 <br/> [ComponentAssertion](ComponentAssertion.md) | Method and structured evidence for the record-level has-part claim carried by... | direct |
| [culturemech_reference](culturemech_reference.md) | 0..1 <br/> [CultureMechReference](CultureMechReference.md) | Typed, stable link to a CultureMech recipe | direct |
| [kg_microbe_node_id](kg_microbe_node_id.md) | 0..1 <br/> [String](String.md) | KG-Microbe node ID for this ingredient when found in the KG exactly | direct |
| [environmental_context](environmental_context.md) | * <br/> [EnvironmentContext](EnvironmentContext.md) | Environmental contexts where this ingredient is relevant | direct |
| [discussions](discussions.md) | * <br/> [Discussion](Discussion.md) | Open questions, knowledge gaps, controversies, and curation todos attached to... | direct |
| [datasets](datasets.md) | * <br/> [Dataset](Dataset.md) | Public datasets (omics/sequence/phenotype) relevant to this ingredient | direct |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [IngredientCollection](IngredientCollection.md) | [ingredients](ingredients.md) | range | [IngredientRecord](IngredientRecord.md) |




## Rules


### 

| Rule Applied | Preconditions | Postconditions | Elseconditions |
|--------------|---------------|----------------|----------------|
| slot_conditions |```{'components': {'value_presence': 'PRESENT'}}``` |```{'component_assertion': {'value_presence': 'PRESENT'}}``` | |



### 

| Rule Applied | Preconditions | Postconditions | Elseconditions |
|--------------|---------------|----------------|----------------|
| slot_conditions |```{'components': {'value_presence': 'PRESENT'}}``` |```{'ingredient_type': {'equals_string_in': ['STOCK_SOLUTION', 'NAMED_MEDIUM', 'UNDEFINED_MIXTURE']}}``` | |







## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/mediaingredientmech




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | mediaingredientmech:IngredientRecord |
| native | mediaingredientmech:IngredientRecord |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: IngredientRecord
description: Core record for a media ingredient with ontology mapping, synonyms, and
  curation history. Represents either a mapped ingredient (with a primary ontology,
  registry, or local identity CURIE) or an unmapped ingredient (placeholder identifier,
  awaits curation). Can serve as root element for individual YAML files or as elements
  in IngredientCollection.
from_schema: https://w3id.org/mediaingredientmech
attributes:
  identifier:
    name: identifier
    description: 'Semantic identifier for the record and its LinkML identifier slot,
      but not a guaranteed unique document address: reviewed duplicate families may
      share a CURIE. For mapped ingredients this is the primary ontology, registry,
      or local identity (e.g. `CHEBI:26710`, `cas:247167-54-0`, `kgmicrobe.compound:aburamycin_a`);
      for unmapped ingredients it is a generated `UNMAPPED_NNNN` placeholder. The
      nested `ontology_mapping.ontology_id` is a grounding target: it equals `identifier`
      when the identifier itself names the grounded ontology term, but registry or
      local identities may legitimately differ from the ontology target at any evidence-backed
      mapping quality.'
    from_schema: https://w3id.org/mediaingredientmech
    rank: 1000
    identifier: true
    domain_of:
    - IngredientRecord
    required: true
  preferred_term:
    name: preferred_term
    description: Canonical name for this ingredient
    from_schema: https://w3id.org/mediaingredientmech
    rank: 1000
    domain_of:
    - IngredientRecord
    required: true
  ontology_mapping:
    name: ontology_mapping
    description: Ontology term mapping (CHEBI/FOODON)
    from_schema: https://w3id.org/mediaingredientmech
    rank: 1000
    domain_of:
    - IngredientRecord
    range: OntologyMapping
    bindings:
    - obligation_level: REQUIRED
      binds_value_of: ontology_id
  synonyms:
    name: synonyms
    description: Alternative names and raw text variants
    from_schema: https://w3id.org/mediaingredientmech
    rank: 1000
    domain_of:
    - IngredientRecord
    range: IngredientSynonym
    multivalued: true
    inlined: true
    inlined_as_list: true
  mapping_status:
    name: mapping_status
    description: Current mapping status
    from_schema: https://w3id.org/mediaingredientmech
    rank: 1000
    domain_of:
    - IngredientRecord
    range: MappingStatusEnum
    required: true
  occurrence_statistics:
    name: occurrence_statistics
    description: Usage statistics across media recipes
    from_schema: https://w3id.org/mediaingredientmech
    rank: 1000
    domain_of:
    - IngredientRecord
    range: OccurrenceStats
  curation_history:
    name: curation_history
    description: Audit trail of all curation actions
    from_schema: https://w3id.org/mediaingredientmech
    rank: 1000
    domain_of:
    - IngredientRecord
    range: CurationEvent
    multivalued: true
    inlined: true
    inlined_as_list: true
  notes:
    name: notes
    description: Free-text curation notes
    from_schema: https://w3id.org/mediaingredientmech
    rank: 1000
    domain_of:
    - IngredientRecord
    - EnvironmentContext
    - MappingEvidence
    - SuppliedForm
    - CurationEvent
    - CommunityOrganismRoleAssignment
    - NutritionalRoleAssignment
    - PhysicochemicalRoleAssignment
    - CellularMetabolicRoleAssignment
    - ComponentAssertion
    - ComponentEvidence
    - SupportingReference
    - Discussion
    - Dataset
  community_organism_roles:
    name: community_organism_roles
    description: Role(s) this organism plays in a microbial community (e.g., PRIMARY_DEGRADER,
      SYNERGIST, COMPETITOR). Formerly `cellular_roles`; renamed to disambiguate from
      ingredient-level cellular metabolic roles.
    from_schema: https://w3id.org/mediaingredientmech
    rank: 1000
    domain_of:
    - IngredientRecord
    range: CommunityOrganismRoleAssignment
    multivalued: true
    inlined: true
    inlined_as_list: true
  nutritional_roles:
    name: nutritional_roles
    description: What element or macronutrient this ingredient supplies to the medium
      (e.g., CARBON_SOURCE, SULFUR_SOURCE, VITAMIN_SOURCE). Facet 1 of 3 orthogonal
      ingredient-role facets — a single ingredient may carry multiple values (e.g.,
      L-cysteine → AMINO_ACID_SOURCE + SULFUR_SOURCE).
    from_schema: https://w3id.org/mediaingredientmech
    rank: 1000
    domain_of:
    - IngredientRecord
    range: NutritionalRoleAssignment
    multivalued: true
    inlined: true
    inlined_as_list: true
  physicochemical_roles:
    name: physicochemical_roles
    description: Chemical or physical function this ingredient performs in the medium
      (e.g., BUFFER, CHELATOR, REDUCING_AGENT). Facet 2 of 3 orthogonal ingredient-role
      facets — independent of what element the ingredient supplies.
    from_schema: https://w3id.org/mediaingredientmech
    rank: 1000
    domain_of:
    - IngredientRecord
    range: PhysicochemicalRoleAssignment
    multivalued: true
    inlined: true
    inlined_as_list: true
  cellular_metabolic_roles:
    name: cellular_metabolic_roles
    description: Role of this ingredient inside/on the cultured microbe (e.g., SUBSTRATE,
      ELECTRON_DONOR, COFACTOR). Facet 3 of 3 orthogonal ingredient-role facets —
      often organism-conditional (e.g., ELECTRON_DONOR applies only for organisms
      that oxidize the compound for energy).
    from_schema: https://w3id.org/mediaingredientmech
    rank: 1000
    domain_of:
    - IngredientRecord
    range: CellularMetabolicRoleAssignment
    multivalued: true
    inlined: true
    inlined_as_list: true
  solution_type:
    name: solution_type
    description: Type of solution if this is a stock/pre-mix rather than individual
      chemical
    from_schema: https://w3id.org/mediaingredientmech
    rank: 1000
    domain_of:
    - IngredientRecord
    range: SolutionTypeEnum
  chemical_properties:
    name: chemical_properties
    description: Chemical structure and properties (for CHEBI-mapped ingredients only)
    from_schema: https://w3id.org/mediaingredientmech
    rank: 1000
    domain_of:
    - IngredientRecord
    range: ChemicalProperties
  supplied_form:
    name: supplied_form
    description: 'The material actually ordered and delivered for this ingredient
      — the thing on the shelf, as distinct from the substance the record denotes.
      Multivalued because one ingredient is legitimately buyable in several forms
      (anhydrous vs a hydrate, free acid vs sodium salt) and a recipe may not say
      which. Keeps procurement detail OUT of the identity: the `identifier` optimises
      for how the node reads in the knowledge graph, and this slot carries what you
      would put on a purchase order.'
    from_schema: https://w3id.org/mediaingredientmech
    rank: 1000
    domain_of:
    - IngredientRecord
    range: SuppliedForm
    multivalued: true
    inlined: true
    inlined_as_list: true
  representative:
    name: representative
    description: '`identifier` of the representative record if this record has been
      merged. Only set when mapping_status is REJECTED due to merge. Points to the
      canonical record representing this ingredient. (No pattern constraint: the merge-tracking
      feature is currently unused — when revived, point at the schema''s canonical
      identifier format.)'
    from_schema: https://w3id.org/mediaingredientmech
    rank: 1000
    domain_of:
    - IngredientRecord
  merged:
    name: merged
    description: 'List of record `identifier`s merged into this representative. Only
      set on records serving as merge targets. Tracks all records consolidated into
      this canonical representation. (No pattern constraint: see `representative`
      above.)'
    from_schema: https://w3id.org/mediaingredientmech
    rank: 1000
    domain_of:
    - IngredientRecord
    multivalued: true
  ingredient_type:
    name: ingredient_type
    description: 'Classification of entry type: single chemical ingredient vs whole
      named medium. SINGLE_INGREDIENT: Pure chemical (NaCl, agar, glucose). NAMED_MEDIUM:
      A complete, named medium formulation/recipe (R2A agar, LB broth) -- "defined"
      = record granularity (a whole named medium), NOT "chemically defined"; undefined
      components are expected. UNDEFINED_MIXTURE: Complex mixture of unknown composition
      (yeast extract, peptone). STOCK_SOLUTION: Pre-mixed solution of defined ingredients.'
    from_schema: https://w3id.org/mediaingredientmech
    rank: 1000
    domain_of:
    - IngredientRecord
    range: IngredientTypeEnum
  components:
    name: components
    description: 'A has-part decomposition for a STOCK_SOLUTION, NAMED_MEDIUM, or
      UNDEFINED_MIXTURE: the list of component ingredients (with concentration where
      known). This is ingredient/mixture partonomy, not an identity mapping, a complete
      culturing recipe, or a relationship among chemical forms. It may transcribe
      a combination label. Populate only from verifiable evidence; omit the slot when
      no constituent is known. When present, component_assertion records how the decomposition
      was made and its evidence.'
    from_schema: https://w3id.org/mediaingredientmech
    rank: 1000
    domain_of:
    - IngredientRecord
    range: StockComponent
    multivalued: true
    inlined: true
    inlined_as_list: true
  component_assertion:
    name: component_assertion
    description: Method and structured evidence for the record-level has-part claim
      carried by components. Required whenever components is non-empty and forbidden
      when components is absent; the corpus-level partonomy validator enforces that
      cross-field invariant.
    from_schema: https://w3id.org/mediaingredientmech
    rank: 1000
    domain_of:
    - IngredientRecord
    range: ComponentAssertion
    inlined: true
  culturemech_reference:
    name: culturemech_reference
    description: Typed, stable link to a CultureMech recipe. Replaces the former `culturemech_medium_name`,
      which held a display string and no relationship semantics, so it could not distinguish
      the same formulation from a variant or a merely similar composition (#447).
      CultureMech remains authoritative for the recipe body and for recipe family/variant
      structure; this records only which recipe a record answers to and how.
    from_schema: https://w3id.org/mediaingredientmech
    rank: 1000
    domain_of:
    - IngredientRecord
    range: CultureMechReference
  kg_microbe_node_id:
    name: kg_microbe_node_id
    description: KG-Microbe node ID for this ingredient when found in the KG exactly.
      Populated when the ingredient is present as a named node in the KG-Microbe mediadive
      graph (i.e. used as an ingredient in at least one KG-Microbe medium solution).
      The node ID is a CURIE using whichever scheme the KG-Microbe graph stores the
      entity under — most often `CHEBI:`, but also `mesh:`, `NCIT:`, `FOODON:`, `ENVO:`,
      or one of the kg-microbe registry prefixes (`kgmicrobe.compound:`, `kgmicrobe.ingredient:`).
    from_schema: https://w3id.org/mediaingredientmech
    rank: 1000
    domain_of:
    - IngredientRecord
    required: false
    pattern: ^[A-Za-z][A-Za-z0-9.]*:[A-Za-z0-9][A-Za-z0-9._~-]*$
  environmental_context:
    name: environmental_context
    description: Environmental contexts where this ingredient is relevant. Each entry
      pairs an ENVO term with a relevance qualifier explaining the association (natural
      source, selective agent, environment mimic, etc.). Enables cross-repository
      environment-driven queries with CommunityMech (`environment_term`) and CultureMech
      (`source_environment`). Optional; ubiquitous ingredients (water, glucose) typically
      have no entries.
    from_schema: https://w3id.org/mediaingredientmech
    rank: 1000
    domain_of:
    - IngredientRecord
    range: EnvironmentContext
    bindings:
    - obligation_level: REQUIRED
      binds_value_of: environment_term
    required: false
    multivalued: true
    inlined: true
    inlined_as_list: true
  discussions:
    name: discussions
    description: Open questions, knowledge gaps, controversies, and curation todos
      attached to this ingredient (shared Discussion supertype; anchor `attaches_to`
      into e.g. `ontology_mapping#<term>`).
    from_schema: https://w3id.org/mediaingredientmech
    rank: 1000
    domain_of:
    - IngredientRecord
    range: Discussion
    multivalued: true
    inlined: true
    inlined_as_list: true
  datasets:
    name: datasets
    description: Public datasets (omics/sequence/phenotype) relevant to this ingredient.
    from_schema: https://w3id.org/mediaingredientmech
    rank: 1000
    domain_of:
    - IngredientRecord
    range: Dataset
    multivalued: true
    inlined: true
    inlined_as_list: true
tree_root: true
rules:
- preconditions:
    slot_conditions:
      components:
        name: components
        value_presence: PRESENT
  postconditions:
    slot_conditions:
      component_assertion:
        name: component_assertion
        value_presence: PRESENT
  bidirectional: true
- preconditions:
    slot_conditions:
      components:
        name: components
        value_presence: PRESENT
  postconditions:
    slot_conditions:
      ingredient_type:
        name: ingredient_type
        equals_string_in:
        - STOCK_SOLUTION
        - NAMED_MEDIUM
        - UNDEFINED_MIXTURE

```
</details>

### Induced

<details>
```yaml
name: IngredientRecord
description: Core record for a media ingredient with ontology mapping, synonyms, and
  curation history. Represents either a mapped ingredient (with a primary ontology,
  registry, or local identity CURIE) or an unmapped ingredient (placeholder identifier,
  awaits curation). Can serve as root element for individual YAML files or as elements
  in IngredientCollection.
from_schema: https://w3id.org/mediaingredientmech
attributes:
  identifier:
    name: identifier
    description: 'Semantic identifier for the record and its LinkML identifier slot,
      but not a guaranteed unique document address: reviewed duplicate families may
      share a CURIE. For mapped ingredients this is the primary ontology, registry,
      or local identity (e.g. `CHEBI:26710`, `cas:247167-54-0`, `kgmicrobe.compound:aburamycin_a`);
      for unmapped ingredients it is a generated `UNMAPPED_NNNN` placeholder. The
      nested `ontology_mapping.ontology_id` is a grounding target: it equals `identifier`
      when the identifier itself names the grounded ontology term, but registry or
      local identities may legitimately differ from the ontology target at any evidence-backed
      mapping quality.'
    from_schema: https://w3id.org/mediaingredientmech
    rank: 1000
    identifier: true
    alias: identifier
    owner: IngredientRecord
    domain_of:
    - IngredientRecord
    range: string
    required: true
  preferred_term:
    name: preferred_term
    description: Canonical name for this ingredient
    from_schema: https://w3id.org/mediaingredientmech
    rank: 1000
    alias: preferred_term
    owner: IngredientRecord
    domain_of:
    - IngredientRecord
    range: string
    required: true
  ontology_mapping:
    name: ontology_mapping
    description: Ontology term mapping (CHEBI/FOODON)
    from_schema: https://w3id.org/mediaingredientmech
    rank: 1000
    alias: ontology_mapping
    owner: IngredientRecord
    domain_of:
    - IngredientRecord
    range: OntologyMapping
    bindings:
    - obligation_level: REQUIRED
      binds_value_of: ontology_id
  synonyms:
    name: synonyms
    description: Alternative names and raw text variants
    from_schema: https://w3id.org/mediaingredientmech
    rank: 1000
    alias: synonyms
    owner: IngredientRecord
    domain_of:
    - IngredientRecord
    range: IngredientSynonym
    multivalued: true
    inlined: true
    inlined_as_list: true
  mapping_status:
    name: mapping_status
    description: Current mapping status
    from_schema: https://w3id.org/mediaingredientmech
    rank: 1000
    alias: mapping_status
    owner: IngredientRecord
    domain_of:
    - IngredientRecord
    range: MappingStatusEnum
    required: true
  occurrence_statistics:
    name: occurrence_statistics
    description: Usage statistics across media recipes
    from_schema: https://w3id.org/mediaingredientmech
    rank: 1000
    alias: occurrence_statistics
    owner: IngredientRecord
    domain_of:
    - IngredientRecord
    range: OccurrenceStats
  curation_history:
    name: curation_history
    description: Audit trail of all curation actions
    from_schema: https://w3id.org/mediaingredientmech
    rank: 1000
    alias: curation_history
    owner: IngredientRecord
    domain_of:
    - IngredientRecord
    range: CurationEvent
    multivalued: true
    inlined: true
    inlined_as_list: true
  notes:
    name: notes
    description: Free-text curation notes
    from_schema: https://w3id.org/mediaingredientmech
    rank: 1000
    alias: notes
    owner: IngredientRecord
    domain_of:
    - IngredientRecord
    - EnvironmentContext
    - MappingEvidence
    - SuppliedForm
    - CurationEvent
    - CommunityOrganismRoleAssignment
    - NutritionalRoleAssignment
    - PhysicochemicalRoleAssignment
    - CellularMetabolicRoleAssignment
    - ComponentAssertion
    - ComponentEvidence
    - SupportingReference
    - Discussion
    - Dataset
    range: string
  community_organism_roles:
    name: community_organism_roles
    description: Role(s) this organism plays in a microbial community (e.g., PRIMARY_DEGRADER,
      SYNERGIST, COMPETITOR). Formerly `cellular_roles`; renamed to disambiguate from
      ingredient-level cellular metabolic roles.
    from_schema: https://w3id.org/mediaingredientmech
    rank: 1000
    alias: community_organism_roles
    owner: IngredientRecord
    domain_of:
    - IngredientRecord
    range: CommunityOrganismRoleAssignment
    multivalued: true
    inlined: true
    inlined_as_list: true
  nutritional_roles:
    name: nutritional_roles
    description: What element or macronutrient this ingredient supplies to the medium
      (e.g., CARBON_SOURCE, SULFUR_SOURCE, VITAMIN_SOURCE). Facet 1 of 3 orthogonal
      ingredient-role facets — a single ingredient may carry multiple values (e.g.,
      L-cysteine → AMINO_ACID_SOURCE + SULFUR_SOURCE).
    from_schema: https://w3id.org/mediaingredientmech
    rank: 1000
    alias: nutritional_roles
    owner: IngredientRecord
    domain_of:
    - IngredientRecord
    range: NutritionalRoleAssignment
    multivalued: true
    inlined: true
    inlined_as_list: true
  physicochemical_roles:
    name: physicochemical_roles
    description: Chemical or physical function this ingredient performs in the medium
      (e.g., BUFFER, CHELATOR, REDUCING_AGENT). Facet 2 of 3 orthogonal ingredient-role
      facets — independent of what element the ingredient supplies.
    from_schema: https://w3id.org/mediaingredientmech
    rank: 1000
    alias: physicochemical_roles
    owner: IngredientRecord
    domain_of:
    - IngredientRecord
    range: PhysicochemicalRoleAssignment
    multivalued: true
    inlined: true
    inlined_as_list: true
  cellular_metabolic_roles:
    name: cellular_metabolic_roles
    description: Role of this ingredient inside/on the cultured microbe (e.g., SUBSTRATE,
      ELECTRON_DONOR, COFACTOR). Facet 3 of 3 orthogonal ingredient-role facets —
      often organism-conditional (e.g., ELECTRON_DONOR applies only for organisms
      that oxidize the compound for energy).
    from_schema: https://w3id.org/mediaingredientmech
    rank: 1000
    alias: cellular_metabolic_roles
    owner: IngredientRecord
    domain_of:
    - IngredientRecord
    range: CellularMetabolicRoleAssignment
    multivalued: true
    inlined: true
    inlined_as_list: true
  solution_type:
    name: solution_type
    description: Type of solution if this is a stock/pre-mix rather than individual
      chemical
    from_schema: https://w3id.org/mediaingredientmech
    rank: 1000
    alias: solution_type
    owner: IngredientRecord
    domain_of:
    - IngredientRecord
    range: SolutionTypeEnum
  chemical_properties:
    name: chemical_properties
    description: Chemical structure and properties (for CHEBI-mapped ingredients only)
    from_schema: https://w3id.org/mediaingredientmech
    rank: 1000
    alias: chemical_properties
    owner: IngredientRecord
    domain_of:
    - IngredientRecord
    range: ChemicalProperties
  supplied_form:
    name: supplied_form
    description: 'The material actually ordered and delivered for this ingredient
      — the thing on the shelf, as distinct from the substance the record denotes.
      Multivalued because one ingredient is legitimately buyable in several forms
      (anhydrous vs a hydrate, free acid vs sodium salt) and a recipe may not say
      which. Keeps procurement detail OUT of the identity: the `identifier` optimises
      for how the node reads in the knowledge graph, and this slot carries what you
      would put on a purchase order.'
    from_schema: https://w3id.org/mediaingredientmech
    rank: 1000
    alias: supplied_form
    owner: IngredientRecord
    domain_of:
    - IngredientRecord
    range: SuppliedForm
    multivalued: true
    inlined: true
    inlined_as_list: true
  representative:
    name: representative
    description: '`identifier` of the representative record if this record has been
      merged. Only set when mapping_status is REJECTED due to merge. Points to the
      canonical record representing this ingredient. (No pattern constraint: the merge-tracking
      feature is currently unused — when revived, point at the schema''s canonical
      identifier format.)'
    from_schema: https://w3id.org/mediaingredientmech
    rank: 1000
    alias: representative
    owner: IngredientRecord
    domain_of:
    - IngredientRecord
    range: string
  merged:
    name: merged
    description: 'List of record `identifier`s merged into this representative. Only
      set on records serving as merge targets. Tracks all records consolidated into
      this canonical representation. (No pattern constraint: see `representative`
      above.)'
    from_schema: https://w3id.org/mediaingredientmech
    rank: 1000
    alias: merged
    owner: IngredientRecord
    domain_of:
    - IngredientRecord
    range: string
    multivalued: true
  ingredient_type:
    name: ingredient_type
    description: 'Classification of entry type: single chemical ingredient vs whole
      named medium. SINGLE_INGREDIENT: Pure chemical (NaCl, agar, glucose). NAMED_MEDIUM:
      A complete, named medium formulation/recipe (R2A agar, LB broth) -- "defined"
      = record granularity (a whole named medium), NOT "chemically defined"; undefined
      components are expected. UNDEFINED_MIXTURE: Complex mixture of unknown composition
      (yeast extract, peptone). STOCK_SOLUTION: Pre-mixed solution of defined ingredients.'
    from_schema: https://w3id.org/mediaingredientmech
    rank: 1000
    alias: ingredient_type
    owner: IngredientRecord
    domain_of:
    - IngredientRecord
    range: IngredientTypeEnum
  components:
    name: components
    description: 'A has-part decomposition for a STOCK_SOLUTION, NAMED_MEDIUM, or
      UNDEFINED_MIXTURE: the list of component ingredients (with concentration where
      known). This is ingredient/mixture partonomy, not an identity mapping, a complete
      culturing recipe, or a relationship among chemical forms. It may transcribe
      a combination label. Populate only from verifiable evidence; omit the slot when
      no constituent is known. When present, component_assertion records how the decomposition
      was made and its evidence.'
    from_schema: https://w3id.org/mediaingredientmech
    rank: 1000
    alias: components
    owner: IngredientRecord
    domain_of:
    - IngredientRecord
    range: StockComponent
    multivalued: true
    inlined: true
    inlined_as_list: true
  component_assertion:
    name: component_assertion
    description: Method and structured evidence for the record-level has-part claim
      carried by components. Required whenever components is non-empty and forbidden
      when components is absent; the corpus-level partonomy validator enforces that
      cross-field invariant.
    from_schema: https://w3id.org/mediaingredientmech
    rank: 1000
    alias: component_assertion
    owner: IngredientRecord
    domain_of:
    - IngredientRecord
    range: ComponentAssertion
    inlined: true
  culturemech_reference:
    name: culturemech_reference
    description: Typed, stable link to a CultureMech recipe. Replaces the former `culturemech_medium_name`,
      which held a display string and no relationship semantics, so it could not distinguish
      the same formulation from a variant or a merely similar composition (#447).
      CultureMech remains authoritative for the recipe body and for recipe family/variant
      structure; this records only which recipe a record answers to and how.
    from_schema: https://w3id.org/mediaingredientmech
    rank: 1000
    alias: culturemech_reference
    owner: IngredientRecord
    domain_of:
    - IngredientRecord
    range: CultureMechReference
  kg_microbe_node_id:
    name: kg_microbe_node_id
    description: KG-Microbe node ID for this ingredient when found in the KG exactly.
      Populated when the ingredient is present as a named node in the KG-Microbe mediadive
      graph (i.e. used as an ingredient in at least one KG-Microbe medium solution).
      The node ID is a CURIE using whichever scheme the KG-Microbe graph stores the
      entity under — most often `CHEBI:`, but also `mesh:`, `NCIT:`, `FOODON:`, `ENVO:`,
      or one of the kg-microbe registry prefixes (`kgmicrobe.compound:`, `kgmicrobe.ingredient:`).
    from_schema: https://w3id.org/mediaingredientmech
    rank: 1000
    alias: kg_microbe_node_id
    owner: IngredientRecord
    domain_of:
    - IngredientRecord
    range: string
    required: false
    pattern: ^[A-Za-z][A-Za-z0-9.]*:[A-Za-z0-9][A-Za-z0-9._~-]*$
  environmental_context:
    name: environmental_context
    description: Environmental contexts where this ingredient is relevant. Each entry
      pairs an ENVO term with a relevance qualifier explaining the association (natural
      source, selective agent, environment mimic, etc.). Enables cross-repository
      environment-driven queries with CommunityMech (`environment_term`) and CultureMech
      (`source_environment`). Optional; ubiquitous ingredients (water, glucose) typically
      have no entries.
    from_schema: https://w3id.org/mediaingredientmech
    rank: 1000
    alias: environmental_context
    owner: IngredientRecord
    domain_of:
    - IngredientRecord
    range: EnvironmentContext
    bindings:
    - obligation_level: REQUIRED
      binds_value_of: environment_term
    required: false
    multivalued: true
    inlined: true
    inlined_as_list: true
  discussions:
    name: discussions
    description: Open questions, knowledge gaps, controversies, and curation todos
      attached to this ingredient (shared Discussion supertype; anchor `attaches_to`
      into e.g. `ontology_mapping#<term>`).
    from_schema: https://w3id.org/mediaingredientmech
    rank: 1000
    alias: discussions
    owner: IngredientRecord
    domain_of:
    - IngredientRecord
    range: Discussion
    multivalued: true
    inlined: true
    inlined_as_list: true
  datasets:
    name: datasets
    description: Public datasets (omics/sequence/phenotype) relevant to this ingredient.
    from_schema: https://w3id.org/mediaingredientmech
    rank: 1000
    alias: datasets
    owner: IngredientRecord
    domain_of:
    - IngredientRecord
    range: Dataset
    multivalued: true
    inlined: true
    inlined_as_list: true
tree_root: true
rules:
- preconditions:
    slot_conditions:
      components:
        name: components
        value_presence: PRESENT
  postconditions:
    slot_conditions:
      component_assertion:
        name: component_assertion
        value_presence: PRESENT
  bidirectional: true
- preconditions:
    slot_conditions:
      components:
        name: components
        value_presence: PRESENT
  postconditions:
    slot_conditions:
      ingredient_type:
        name: ingredient_type
        equals_string_in:
        - STOCK_SOLUTION
        - NAMED_MEDIUM
        - UNDEFINED_MIXTURE

```
</details>