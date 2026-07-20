

# Class: CellularMetabolicRoleAssignment 


_Assignment of a cellular-metabolic facet role (what the ingredient does inside or to the cultured microbe) with supporting evidence. Assignments in this facet are often organism-conditional (e.g., ELECTRON_DONOR applies only for organisms that oxidize the compound for energy); capture that in `metabolic_context`._





URI: [mediaingredientmech:CellularMetabolicRoleAssignment](https://w3id.org/mediaingredientmech/CellularMetabolicRoleAssignment)





```mermaid
 classDiagram
    class CellularMetabolicRoleAssignment
    click CellularMetabolicRoleAssignment href "../CellularMetabolicRoleAssignment/"
      CellularMetabolicRoleAssignment : confidence
        
      CellularMetabolicRoleAssignment : evidence
        
          
    
        
        
        CellularMetabolicRoleAssignment --> "*" RoleCitation : evidence
        click RoleCitation href "../RoleCitation/"
    

        
      CellularMetabolicRoleAssignment : metabolic_context
        
      CellularMetabolicRoleAssignment : notes
        
      CellularMetabolicRoleAssignment : role
        
          
    
        
        
        CellularMetabolicRoleAssignment --> "1" CellularMetabolicRoleEnum : role
        click CellularMetabolicRoleEnum href "../CellularMetabolicRoleEnum/"
    

        
      
```




<!-- no inheritance hierarchy -->


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [role](role.md) | 1 <br/> [CellularMetabolicRoleEnum](CellularMetabolicRoleEnum.md) | The cellular-metabolic role (e | direct |
| [metabolic_context](metabolic_context.md) | 0..1 <br/> [String](String.md) | Pathway or organism context that scopes this assignment (e | direct |
| [confidence](confidence.md) | 0..1 <br/> [Float](Float.md) | Confidence score for this role assignment (0 | direct |
| [evidence](evidence.md) | * <br/> [RoleCitation](RoleCitation.md) | Citations and references supporting this role | direct |
| [notes](notes.md) | 0..1 <br/> [String](String.md) | Additional context about this role assignment | direct |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [IngredientRecord](IngredientRecord.md) | [cellular_metabolic_roles](cellular_metabolic_roles.md) | range | [CellularMetabolicRoleAssignment](CellularMetabolicRoleAssignment.md) |







## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/mediaingredientmech




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | mediaingredientmech:CellularMetabolicRoleAssignment |
| native | mediaingredientmech:CellularMetabolicRoleAssignment |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: CellularMetabolicRoleAssignment
description: Assignment of a cellular-metabolic facet role (what the ingredient does
  inside or to the cultured microbe) with supporting evidence. Assignments in this
  facet are often organism-conditional (e.g., ELECTRON_DONOR applies only for organisms
  that oxidize the compound for energy); capture that in `metabolic_context`.
from_schema: https://w3id.org/mediaingredientmech
attributes:
  role:
    name: role
    description: The cellular-metabolic role (e.g., SUBSTRATE, ELECTRON_DONOR, COFACTOR).
    from_schema: https://w3id.org/mediaingredientmech
    domain_of:
    - RoleAssignment
    - CommunityOrganismRoleAssignment
    - NutritionalRoleAssignment
    - PhysicochemicalRoleAssignment
    - CellularMetabolicRoleAssignment
    range: CellularMetabolicRoleEnum
    required: true
  metabolic_context:
    name: metabolic_context
    description: Pathway or organism context that scopes this assignment (e.g., "methanol
      → ELECTRON_DONOR in methylotrophs only", "sulfate → ELECTRON_ACCEPTOR under
      anaerobic sulfate reduction"). Important when a role only holds for a subset
      of organisms or conditions.
    from_schema: https://w3id.org/mediaingredientmech
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
name: CellularMetabolicRoleAssignment
description: Assignment of a cellular-metabolic facet role (what the ingredient does
  inside or to the cultured microbe) with supporting evidence. Assignments in this
  facet are often organism-conditional (e.g., ELECTRON_DONOR applies only for organisms
  that oxidize the compound for energy); capture that in `metabolic_context`.
from_schema: https://w3id.org/mediaingredientmech
attributes:
  role:
    name: role
    description: The cellular-metabolic role (e.g., SUBSTRATE, ELECTRON_DONOR, COFACTOR).
    from_schema: https://w3id.org/mediaingredientmech
    alias: role
    owner: CellularMetabolicRoleAssignment
    domain_of:
    - RoleAssignment
    - CommunityOrganismRoleAssignment
    - NutritionalRoleAssignment
    - PhysicochemicalRoleAssignment
    - CellularMetabolicRoleAssignment
    range: CellularMetabolicRoleEnum
    required: true
  metabolic_context:
    name: metabolic_context
    description: Pathway or organism context that scopes this assignment (e.g., "methanol
      → ELECTRON_DONOR in methylotrophs only", "sulfate → ELECTRON_ACCEPTOR under
      anaerobic sulfate reduction"). Important when a role only holds for a subset
      of organisms or conditions.
    from_schema: https://w3id.org/mediaingredientmech
    alias: metabolic_context
    owner: CellularMetabolicRoleAssignment
    domain_of:
    - CommunityOrganismRoleAssignment
    - CellularMetabolicRoleAssignment
    range: string
  confidence:
    name: confidence
    description: Confidence score for this role assignment (0.0-1.0)
    from_schema: https://w3id.org/mediaingredientmech
    alias: confidence
    owner: CellularMetabolicRoleAssignment
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
    owner: CellularMetabolicRoleAssignment
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
    owner: CellularMetabolicRoleAssignment
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