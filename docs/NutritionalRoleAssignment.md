

# Class: NutritionalRoleAssignment 


_Assignment of a nutritional facet role (what element or macronutrient the ingredient supplies) with supporting evidence._





URI: [mediaingredientmech:NutritionalRoleAssignment](https://w3id.org/mediaingredientmech/NutritionalRoleAssignment)





```mermaid
 classDiagram
    class NutritionalRoleAssignment
    click NutritionalRoleAssignment href "../NutritionalRoleAssignment/"
      NutritionalRoleAssignment : confidence
        
      NutritionalRoleAssignment : evidence
        
          
    
        
        
        NutritionalRoleAssignment --> "*" RoleCitation : evidence
        click RoleCitation href "../RoleCitation/"
    

        
      NutritionalRoleAssignment : notes
        
      NutritionalRoleAssignment : role
        
          
    
        
        
        NutritionalRoleAssignment --> "1" NutritionalRoleEnum : role
        click NutritionalRoleEnum href "../NutritionalRoleEnum/"
    

        
      
```




<!-- no inheritance hierarchy -->


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [role](role.md) | 1 <br/> [NutritionalRoleEnum](NutritionalRoleEnum.md) | The nutritional role (e | direct |
| [confidence](confidence.md) | 0..1 <br/> [Float](Float.md) | Confidence score for this role assignment (0 | direct |
| [evidence](evidence.md) | * <br/> [RoleCitation](RoleCitation.md) | Citations and references supporting this role | direct |
| [notes](notes.md) | 0..1 <br/> [String](String.md) | Additional context about this role assignment | direct |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [IngredientRecord](IngredientRecord.md) | [nutritional_roles](nutritional_roles.md) | range | [NutritionalRoleAssignment](NutritionalRoleAssignment.md) |







## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/mediaingredientmech




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | mediaingredientmech:NutritionalRoleAssignment |
| native | mediaingredientmech:NutritionalRoleAssignment |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: NutritionalRoleAssignment
description: Assignment of a nutritional facet role (what element or macronutrient
  the ingredient supplies) with supporting evidence.
from_schema: https://w3id.org/mediaingredientmech
attributes:
  role:
    name: role
    description: The nutritional role (e.g., CARBON_SOURCE, SULFUR_SOURCE, VITAMIN_SOURCE).
    from_schema: https://w3id.org/mediaingredientmech
    domain_of:
    - RoleAssignment
    - CommunityOrganismRoleAssignment
    - NutritionalRoleAssignment
    - PhysicochemicalRoleAssignment
    - CellularMetabolicRoleAssignment
    range: NutritionalRoleEnum
    required: true
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
name: NutritionalRoleAssignment
description: Assignment of a nutritional facet role (what element or macronutrient
  the ingredient supplies) with supporting evidence.
from_schema: https://w3id.org/mediaingredientmech
attributes:
  role:
    name: role
    description: The nutritional role (e.g., CARBON_SOURCE, SULFUR_SOURCE, VITAMIN_SOURCE).
    from_schema: https://w3id.org/mediaingredientmech
    alias: role
    owner: NutritionalRoleAssignment
    domain_of:
    - RoleAssignment
    - CommunityOrganismRoleAssignment
    - NutritionalRoleAssignment
    - PhysicochemicalRoleAssignment
    - CellularMetabolicRoleAssignment
    range: NutritionalRoleEnum
    required: true
  confidence:
    name: confidence
    description: Confidence score for this role assignment (0.0-1.0)
    from_schema: https://w3id.org/mediaingredientmech
    alias: confidence
    owner: NutritionalRoleAssignment
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
    owner: NutritionalRoleAssignment
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
    owner: NutritionalRoleAssignment
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