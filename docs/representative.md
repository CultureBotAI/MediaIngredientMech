

# Slot: representative 


_`identifier` of the representative record if this record has been merged. Only set when mapping_status is REJECTED due to merge. Points to the canonical record representing this ingredient. (No pattern constraint: the merge-tracking feature is currently unused — when revived, point at the schema's canonical identifier format.)_





URI: [mediaingredientmech:representative](https://w3id.org/mediaingredientmech/representative)
Alias: representative

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [IngredientRecord](IngredientRecord.md) | Core record for a media ingredient with ontology mapping, synonyms, and curat... |  no  |






## Properties

* Range: [String](String.md)




## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/mediaingredientmech




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | mediaingredientmech:representative |
| native | mediaingredientmech:representative |




## LinkML Source

<details>
```yaml
name: representative
description: '`identifier` of the representative record if this record has been merged.
  Only set when mapping_status is REJECTED due to merge. Points to the canonical record
  representing this ingredient. (No pattern constraint: the merge-tracking feature
  is currently unused — when revived, point at the schema''s canonical identifier
  format.)'
from_schema: https://w3id.org/mediaingredientmech
rank: 1000
alias: representative
owner: IngredientRecord
domain_of:
- IngredientRecord
range: string

```
</details>