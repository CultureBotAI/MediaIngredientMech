

# Slot: merged 


_List of MediaIngredientMech IDs merged into this representative. Only set on records serving as merge targets. Tracks all records consolidated into this canonical representation._





URI: [mediaingredientmech:merged](https://w3id.org/mediaingredientmech/merged)
Alias: merged

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [IngredientRecord](IngredientRecord.md) | Core record for a media ingredient with ontology mapping, synonyms, and curat... |  no  |






## Properties

* Range: [String](String.md)

* Multivalued: True

* Regex pattern: `^MediaIngredientMech:[0-9]{6}$`




## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/mediaingredientmech




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | mediaingredientmech:merged |
| native | mediaingredientmech:merged |




## LinkML Source

<details>
```yaml
name: merged
description: List of MediaIngredientMech IDs merged into this representative. Only
  set on records serving as merge targets. Tracks all records consolidated into this
  canonical representation.
from_schema: https://w3id.org/mediaingredientmech
rank: 1000
alias: merged
owner: IngredientRecord
domain_of:
- IngredientRecord
range: string
multivalued: true
pattern: ^MediaIngredientMech:[0-9]{6}$

```
</details>