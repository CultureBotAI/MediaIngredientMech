

# Class: CommunityOrganismRoleAssignment 


_Assignment of an organism-in-community role with supporting evidence (e.g., which member of a consortium plays the PRIMARY_DEGRADER or SYNERGIST role)._





URI: [mediaingredientmech:CommunityOrganismRoleAssignment](https://w3id.org/mediaingredientmech/CommunityOrganismRoleAssignment)





```mermaid
 classDiagram
    class CommunityOrganismRoleAssignment
    click CommunityOrganismRoleAssignment href "../CommunityOrganismRoleAssignment/"
      CommunityOrganismRoleAssignment : confidence
        
      CommunityOrganismRoleAssignment : evidence
        
          
    
        
        
        CommunityOrganismRoleAssignment --> "*" RoleCitation : evidence
        click RoleCitation href "../RoleCitation/"
    

        
      CommunityOrganismRoleAssignment : metabolic_context
        
      CommunityOrganismRoleAssignment : notes
        
      CommunityOrganismRoleAssignment : role
        
          
    
        
        
        CommunityOrganismRoleAssignment --> "1" CommunityOrganismRoleEnum : role
        click CommunityOrganismRoleEnum href "../CommunityOrganismRoleEnum/"
    

        
      
```




<!-- no inheritance hierarchy -->


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [role](role.md) | 1 <br/> [CommunityOrganismRoleEnum](CommunityOrganismRoleEnum.md) | The community/ecological role of the organism (e | direct |
| [metabolic_context](metabolic_context.md) | 0..1 <br/> [String](String.md) | Pathway or metabolic context (e | direct |
| [confidence](confidence.md) | 0..1 <br/> [Float](Float.md) | Confidence score for this role assignment (0 | direct |
| [evidence](evidence.md) | * <br/> [RoleCitation](RoleCitation.md) | Citations and references supporting this role | direct |
| [notes](notes.md) | 0..1 <br/> [String](String.md) | Additional context about this role assignment | direct |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [IngredientRecord](IngredientRecord.md) | [community_organism_roles](community_organism_roles.md) | range | [CommunityOrganismRoleAssignment](CommunityOrganismRoleAssignment.md) |







## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/mediaingredientmech




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | mediaingredientmech:CommunityOrganismRoleAssignment |
| native | mediaingredientmech:CommunityOrganismRoleAssignment |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: CommunityOrganismRoleAssignment
description: Assignment of an organism-in-community role with supporting evidence
  (e.g., which member of a consortium plays the PRIMARY_DEGRADER or SYNERGIST role).
from_schema: https://w3id.org/mediaingredientmech
attributes:
  role:
    name: role
    description: The community/ecological role of the organism (e.g., PRIMARY_DEGRADER,
      SYNERGIST, COMMENSAL, COMPETITOR).
    from_schema: https://w3id.org/mediaingredientmech
    domain_of:
    - RoleAssignment
    - CommunityOrganismRoleAssignment
    - NutritionalRoleAssignment
    - PhysicochemicalRoleAssignment
    - CellularMetabolicRoleAssignment
    range: CommunityOrganismRoleEnum
    required: true
  metabolic_context:
    name: metabolic_context
    description: Pathway or metabolic context (e.g., "denitrification", "aromatic
      degradation")
    from_schema: https://w3id.org/mediaingredientmech
    rank: 1000
    domain_of:
    - CommunityOrganismRoleAssignment
    - CellularMetabolicRoleAssignment
  confidence:
    name: confidence
    description: Confidence score for this role assignment (0.0-1.0)
    from_schema: https://w3id.org/mediaingredientmech
    domain_of:
    - RoleAssignment
    - CommunityOrganismRoleAssignment
    - NutritionalRoleAssignment
    - PhysicochemicalRoleAssignment
    - CellularMetabolicRoleAssignment
    range: float
  evidence:
    name: evidence
    description: Citations and references supporting this role
    from_schema: https://w3id.org/mediaingredientmech
    domain_of:
    - OntologyMapping
    - RoleAssignment
    - CommunityOrganismRoleAssignment
    - NutritionalRoleAssignment
    - PhysicochemicalRoleAssignment
    - CellularMetabolicRoleAssignment
    - Discussion
    - Dataset
    range: RoleCitation
    multivalued: true
    inlined: true
    inlined_as_list: true
  notes:
    name: notes
    description: Additional context about this role assignment
    from_schema: https://w3id.org/mediaingredientmech
    domain_of:
    - IngredientRecord
    - EnvironmentContext
    - MappingEvidence
    - CurationEvent
    - RoleAssignment
    - CommunityOrganismRoleAssignment
    - NutritionalRoleAssignment
    - PhysicochemicalRoleAssignment
    - CellularMetabolicRoleAssignment
    - SupportingReference
    - Discussion
    - Dataset

```
</details>

### Induced

<details>
```yaml
name: CommunityOrganismRoleAssignment
description: Assignment of an organism-in-community role with supporting evidence
  (e.g., which member of a consortium plays the PRIMARY_DEGRADER or SYNERGIST role).
from_schema: https://w3id.org/mediaingredientmech
attributes:
  role:
    name: role
    description: The community/ecological role of the organism (e.g., PRIMARY_DEGRADER,
      SYNERGIST, COMMENSAL, COMPETITOR).
    from_schema: https://w3id.org/mediaingredientmech
    alias: role
    owner: CommunityOrganismRoleAssignment
    domain_of:
    - RoleAssignment
    - CommunityOrganismRoleAssignment
    - NutritionalRoleAssignment
    - PhysicochemicalRoleAssignment
    - CellularMetabolicRoleAssignment
    range: CommunityOrganismRoleEnum
    required: true
  metabolic_context:
    name: metabolic_context
    description: Pathway or metabolic context (e.g., "denitrification", "aromatic
      degradation")
    from_schema: https://w3id.org/mediaingredientmech
    rank: 1000
    alias: metabolic_context
    owner: CommunityOrganismRoleAssignment
    domain_of:
    - CommunityOrganismRoleAssignment
    - CellularMetabolicRoleAssignment
    range: string
  confidence:
    name: confidence
    description: Confidence score for this role assignment (0.0-1.0)
    from_schema: https://w3id.org/mediaingredientmech
    alias: confidence
    owner: CommunityOrganismRoleAssignment
    domain_of:
    - RoleAssignment
    - CommunityOrganismRoleAssignment
    - NutritionalRoleAssignment
    - PhysicochemicalRoleAssignment
    - CellularMetabolicRoleAssignment
    range: float
  evidence:
    name: evidence
    description: Citations and references supporting this role
    from_schema: https://w3id.org/mediaingredientmech
    alias: evidence
    owner: CommunityOrganismRoleAssignment
    domain_of:
    - OntologyMapping
    - RoleAssignment
    - CommunityOrganismRoleAssignment
    - NutritionalRoleAssignment
    - PhysicochemicalRoleAssignment
    - CellularMetabolicRoleAssignment
    - Discussion
    - Dataset
    range: RoleCitation
    multivalued: true
    inlined: true
    inlined_as_list: true
  notes:
    name: notes
    description: Additional context about this role assignment
    from_schema: https://w3id.org/mediaingredientmech
    alias: notes
    owner: CommunityOrganismRoleAssignment
    domain_of:
    - IngredientRecord
    - EnvironmentContext
    - MappingEvidence
    - CurationEvent
    - RoleAssignment
    - CommunityOrganismRoleAssignment
    - NutritionalRoleAssignment
    - PhysicochemicalRoleAssignment
    - CellularMetabolicRoleAssignment
    - SupportingReference
    - Discussion
    - Dataset
    range: string

```
</details>