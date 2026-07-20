

# Slot: role 



URI: [mediaingredientmech:role](https://w3id.org/mediaingredientmech/role)
Alias: role

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [CellularMetabolicRoleAssignment](CellularMetabolicRoleAssignment.md) | Assignment of a cellular-metabolic facet role (what the ingredient does insid... |  no  |
| [CommunityOrganismRoleAssignment](CommunityOrganismRoleAssignment.md) | Assignment of an organism-in-community role with supporting evidence (e |  no  |
| [RoleAssignment](RoleAssignment.md) | Assignment of a functional role in growth medium formulation with supporting ... |  no  |
| [PhysicochemicalRoleAssignment](PhysicochemicalRoleAssignment.md) | Assignment of a physicochemical facet role (the chemical or physical function... |  no  |
| [NutritionalRoleAssignment](NutritionalRoleAssignment.md) | Assignment of a nutritional facet role (what element or macronutrient the ing... |  no  |






## Properties

* Range: [String](String.md)




## Identifier and Mapping Information







## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | mediaingredientmech:role |
| native | mediaingredientmech:role |




## LinkML Source

<details>
```yaml
name: role
alias: role
domain_of:
- RoleAssignment
- CommunityOrganismRoleAssignment
- NutritionalRoleAssignment
- PhysicochemicalRoleAssignment
- CellularMetabolicRoleAssignment
range: string

```
</details>