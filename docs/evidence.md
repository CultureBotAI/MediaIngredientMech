

# Slot: evidence



URI: [mediaingredientmech:evidence](https://w3id.org/mediaingredientmech/evidence)
Alias: evidence

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [PhysicochemicalRoleAssignment](PhysicochemicalRoleAssignment.md) | Assignment of a physicochemical facet role (the chemical or physical function... |  no  |
| [Discussion](Discussion.md) | A thread-like record of an open question, controversy, curation todo, emergin... |  no  |
| [CellularMetabolicRoleAssignment](CellularMetabolicRoleAssignment.md) | Assignment of a cellular-metabolic facet role (what the ingredient does insid... |  no  |
| [OntologyMapping](OntologyMapping.md) | Mapping to an ontology term (CHEBI, FOODON, etc |  no  |
| [NutritionalRoleAssignment](NutritionalRoleAssignment.md) | Assignment of a nutritional facet role (what element or macronutrient the ing... |  no  |
| [CommunityOrganismRoleAssignment](CommunityOrganismRoleAssignment.md) | Assignment of an organism-in-community role with supporting evidence (e |  no  |
| [Dataset](Dataset.md) | A reference to a publicly available dataset (omics, sequence, phenotype) rele... |  no  |
| [ComponentAssertion](ComponentAssertion.md) | Provenance for one IngredientRecord |  no  |






## Properties

* Range: [String](String.md)




## Identifier and Mapping Information







## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | mediaingredientmech:evidence |
| native | mediaingredientmech:evidence |




## LinkML Source

<details>
```yaml
name: evidence
alias: evidence
domain_of:
- OntologyMapping
- CommunityOrganismRoleAssignment
- NutritionalRoleAssignment
- PhysicochemicalRoleAssignment
- CellularMetabolicRoleAssignment
- ComponentAssertion
- Discussion
- Dataset
range: string

```
</details>