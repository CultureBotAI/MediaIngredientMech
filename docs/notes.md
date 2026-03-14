

# Slot: notes 



URI: [mediaingredientmech:notes](https://w3id.org/mediaingredientmech/notes)
Alias: notes

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [RoleAssignment](RoleAssignment.md) | Assignment of a functional role in growth medium formulation with supporting ... |  no  |
| [MappingEvidence](MappingEvidence.md) | Evidence for an ontology mapping |  no  |
| [CellularRoleAssignment](CellularRoleAssignment.md) | Assignment of a cellular/metabolic role in organism metabolism with supportin... |  no  |
| [IngredientRecord](IngredientRecord.md) | Core record for a media ingredient with ontology mapping, synonyms, and curat... |  no  |
| [CurationEvent](CurationEvent.md) | Audit trail entry for a curation action |  no  |






## Properties

* Range: [xsd:string](http://www.w3.org/2001/XMLSchema#string)




## Identifier and Mapping Information







## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | mediaingredientmech:notes |
| native | mediaingredientmech:notes |




## LinkML Source

<details>
```yaml
name: notes
alias: notes
domain_of:
- IngredientRecord
- MappingEvidence
- CurationEvent
- RoleAssignment
- CellularRoleAssignment
range: string

```
</details>