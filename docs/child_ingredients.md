

# Slot: child_ingredients 


_List of child ingredient `identifier`s in the variant hierarchy. Parent record contains all children (e.g. Water → Tap water, Distilled water). Used to navigate hierarchy and query all variants. (No pattern constraint: see `parent_ingredient` above.)_





URI: [mediaingredientmech:child_ingredients](https://w3id.org/mediaingredientmech/child_ingredients)
Alias: child_ingredients

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [IngredientRecord](IngredientRecord.md) | Core record for a media ingredient with ontology mapping, synonyms, and curat... |  no  |






## Properties

* Range: [String](String.md)

* Multivalued: True




## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/mediaingredientmech




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | mediaingredientmech:child_ingredients |
| native | mediaingredientmech:child_ingredients |




## LinkML Source

<details>
```yaml
name: child_ingredients
description: 'List of child ingredient `identifier`s in the variant hierarchy. Parent
  record contains all children (e.g. Water → Tap water, Distilled water). Used to
  navigate hierarchy and query all variants. (No pattern constraint: see `parent_ingredient`
  above.)'
from_schema: https://w3id.org/mediaingredientmech
rank: 1000
alias: child_ingredients
owner: IngredientRecord
domain_of:
- IngredientRecord
range: string
multivalued: true

```
</details>