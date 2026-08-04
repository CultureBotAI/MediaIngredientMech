

# Slot: nutritional_roles 


_What element or macronutrient this ingredient supplies to the medium (e.g., CARBON_SOURCE, SULFUR_SOURCE, VITAMIN_SOURCE). Facet 1 of 3 orthogonal ingredient-role facets — a single ingredient may carry multiple values (e.g., L-cysteine → AMINO_ACID_SOURCE + SULFUR_SOURCE)._





URI: [mediaingredientmech:nutritional_roles](https://w3id.org/mediaingredientmech/nutritional_roles)
Alias: nutritional_roles

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [IngredientRecord](IngredientRecord.md) | Core record for a media ingredient with ontology mapping, synonyms, and curat... |  no  |






## Properties

* Range: [NutritionalRoleAssignment](NutritionalRoleAssignment.md)

* Multivalued: True




## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/mediaingredientmech




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | mediaingredientmech:nutritional_roles |
| native | mediaingredientmech:nutritional_roles |




## LinkML Source

<details>
```yaml
name: nutritional_roles
description: What element or macronutrient this ingredient supplies to the medium
  (e.g., CARBON_SOURCE, SULFUR_SOURCE, VITAMIN_SOURCE). Facet 1 of 3 orthogonal ingredient-role
  facets — a single ingredient may carry multiple values (e.g., L-cysteine → AMINO_ACID_SOURCE
  + SULFUR_SOURCE).
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

```
</details>