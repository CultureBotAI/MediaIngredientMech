

# Slot: parent_ingredient 


_Reference to parent ingredient in hierarchy (MediaIngredientMech:XXXXXX). Used for variants: purity levels (tap/distilled/double-distilled water), hydrates (CaCl2·2H2O vs CaCl2), stereoisomers (D-glucose vs L-glucose). Enables queries like "find all media using any form of water"._





URI: [mediaingredientmech:parent_ingredient](https://w3id.org/mediaingredientmech/parent_ingredient)
Alias: parent_ingredient

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [IngredientRecord](IngredientRecord.md) | Core record for a media ingredient with ontology mapping, synonyms, and curat... |  no  |






## Properties

* Range: [String](String.md)

* Regex pattern: `^MediaIngredientMech:[0-9]{6}$`




## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/mediaingredientmech




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | mediaingredientmech:parent_ingredient |
| native | mediaingredientmech:parent_ingredient |




## LinkML Source

<details>
```yaml
name: parent_ingredient
description: 'Reference to parent ingredient in hierarchy (MediaIngredientMech:XXXXXX).
  Used for variants: purity levels (tap/distilled/double-distilled water), hydrates
  (CaCl2·2H2O vs CaCl2), stereoisomers (D-glucose vs L-glucose). Enables queries like
  "find all media using any form of water".'
from_schema: https://w3id.org/mediaingredientmech
rank: 1000
alias: parent_ingredient
owner: IngredientRecord
domain_of:
- IngredientRecord
range: string
pattern: ^MediaIngredientMech:[0-9]{6}$

```
</details>