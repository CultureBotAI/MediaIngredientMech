

# Class: RoleAssignment 


_Assignment of a functional role in growth medium formulation with supporting evidence_





URI: [mediaingredientmech:RoleAssignment](https://w3id.org/mediaingredientmech/RoleAssignment)





```mermaid
 classDiagram
    class RoleAssignment
    click RoleAssignment href "../RoleAssignment/"
      RoleAssignment : confidence
        
          
    
        
        
        RoleAssignment --> "0..1" Float : confidence
        click Float href "../http://www.w3.org/2001/XMLSchema#float/"
    

        
      RoleAssignment : evidence
        
          
    
        
        
        RoleAssignment --> "*" RoleCitation : evidence
        click RoleCitation href "../RoleCitation/"
    

        
      RoleAssignment : notes
        
          
    
        
        
        RoleAssignment --> "0..1" String : notes
        click String href "../http://www.w3.org/2001/XMLSchema#string/"
    

        
      RoleAssignment : role
        
          
    
        
        
        RoleAssignment --> "1" IngredientRoleEnum : role
        click IngredientRoleEnum href "../IngredientRoleEnum/"
    

        
      
```




<!-- no inheritance hierarchy -->


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [role](role.md) | 1 <br/> [IngredientRoleEnum](IngredientRoleEnum.md) | The functional role (e | direct |
| [confidence](confidence.md) | 0..1 <br/> [xsd:float](http://www.w3.org/2001/XMLSchema#float) | Confidence score for this role assignment (0 | direct |
| [evidence](evidence.md) | * <br/> [RoleCitation](RoleCitation.md) | Citations and references supporting this role | direct |
| [notes](notes.md) | 0..1 <br/> [xsd:string](http://www.w3.org/2001/XMLSchema#string) | Additional context about this role assignment | direct |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [IngredientRecord](IngredientRecord.md) | [media_roles](media_roles.md) | range | [RoleAssignment](RoleAssignment.md) |







## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/mediaingredientmech




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | mediaingredientmech:RoleAssignment |
| native | mediaingredientmech:RoleAssignment |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: RoleAssignment
description: Assignment of a functional role in growth medium formulation with supporting
  evidence
from_schema: https://w3id.org/mediaingredientmech
attributes:
  role:
    name: role
    description: The functional role (e.g., NITROGEN_SOURCE, BUFFER, MINERAL)
    from_schema: https://w3id.org/mediaingredientmech
    rank: 1000
    domain_of:
    - RoleAssignment
    - CellularRoleAssignment
    range: IngredientRoleEnum
    required: true
  confidence:
    name: confidence
    description: Confidence score for this role assignment (0.0-1.0)
    from_schema: https://w3id.org/mediaingredientmech
    rank: 1000
    domain_of:
    - RoleAssignment
    - CellularRoleAssignment
    range: float
  evidence:
    name: evidence
    description: Citations and references supporting this role
    from_schema: https://w3id.org/mediaingredientmech
    domain_of:
    - OntologyMapping
    - RoleAssignment
    - CellularRoleAssignment
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
    - MappingEvidence
    - CurationEvent
    - RoleAssignment
    - CellularRoleAssignment

```
</details>

### Induced

<details>
```yaml
name: RoleAssignment
description: Assignment of a functional role in growth medium formulation with supporting
  evidence
from_schema: https://w3id.org/mediaingredientmech
attributes:
  role:
    name: role
    description: The functional role (e.g., NITROGEN_SOURCE, BUFFER, MINERAL)
    from_schema: https://w3id.org/mediaingredientmech
    rank: 1000
    alias: role
    owner: RoleAssignment
    domain_of:
    - RoleAssignment
    - CellularRoleAssignment
    range: IngredientRoleEnum
    required: true
  confidence:
    name: confidence
    description: Confidence score for this role assignment (0.0-1.0)
    from_schema: https://w3id.org/mediaingredientmech
    rank: 1000
    alias: confidence
    owner: RoleAssignment
    domain_of:
    - RoleAssignment
    - CellularRoleAssignment
    range: float
  evidence:
    name: evidence
    description: Citations and references supporting this role
    from_schema: https://w3id.org/mediaingredientmech
    alias: evidence
    owner: RoleAssignment
    domain_of:
    - OntologyMapping
    - RoleAssignment
    - CellularRoleAssignment
    range: RoleCitation
    multivalued: true
    inlined: true
    inlined_as_list: true
  notes:
    name: notes
    description: Additional context about this role assignment
    from_schema: https://w3id.org/mediaingredientmech
    alias: notes
    owner: RoleAssignment
    domain_of:
    - IngredientRecord
    - MappingEvidence
    - CurationEvent
    - RoleAssignment
    - CellularRoleAssignment
    range: string

```
</details>