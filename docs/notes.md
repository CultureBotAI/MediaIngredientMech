

# Slot: notes 



URI: [mediaingredientmech:notes](https://w3id.org/mediaingredientmech/notes)
Alias: notes

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [EnvironmentContext](EnvironmentContext.md) | Environmental context annotation for an ingredient |  no  |
| [NutritionalRoleAssignment](NutritionalRoleAssignment.md) | Assignment of a nutritional facet role (what element or macronutrient the ing... |  no  |
| [CommunityOrganismRoleAssignment](CommunityOrganismRoleAssignment.md) | Assignment of an organism-in-community role with supporting evidence (e |  no  |
| [IngredientRecord](IngredientRecord.md) | Core record for a media ingredient with ontology mapping, synonyms, and curat... |  no  |
| [SupportingReference](SupportingReference.md) | A lightweight literature/database citation supporting a Discussion or Dataset |  no  |
| [Discussion](Discussion.md) | A thread-like record of an open question, controversy, curation todo, emergin... |  no  |
| [CurationEvent](CurationEvent.md) | Audit trail entry for a curation action |  no  |
| [MappingEvidence](MappingEvidence.md) | Evidence for an ontology mapping |  no  |
| [PhysicochemicalRoleAssignment](PhysicochemicalRoleAssignment.md) | Assignment of a physicochemical facet role (the chemical or physical function... |  no  |
| [CellularMetabolicRoleAssignment](CellularMetabolicRoleAssignment.md) | Assignment of a cellular-metabolic facet role (what the ingredient does insid... |  no  |
| [Dataset](Dataset.md) | A reference to a publicly available dataset (omics, sequence, phenotype) rele... |  no  |






## Properties

* Range: [String](String.md)




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
- EnvironmentContext
- MappingEvidence
- CurationEvent
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