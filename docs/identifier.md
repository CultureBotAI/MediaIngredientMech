

# Slot: identifier 


_Unique identifier - either ontology ID (e.g., CHEBI:26710) for mapped ingredients or generated UUID/placeholder (e.g., UNMAPPED_001) for unmapped ingredients_





URI: [mediaingredientmech:identifier](https://w3id.org/mediaingredientmech/identifier)
Alias: identifier

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [IngredientRecord](IngredientRecord.md) | Core record for a media ingredient with ontology mapping, synonyms, and curat... |  no  |






## Properties

* Range: [String](String.md)

* Required: True




## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/mediaingredientmech




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | mediaingredientmech:identifier |
| native | mediaingredientmech:identifier |




## LinkML Source

<details>
```yaml
name: identifier
description: Unique identifier - either ontology ID (e.g., CHEBI:26710) for mapped
  ingredients or generated UUID/placeholder (e.g., UNMAPPED_001) for unmapped ingredients
from_schema: https://w3id.org/mediaingredientmech
rank: 1000
identifier: true
alias: identifier
owner: IngredientRecord
domain_of:
- IngredientRecord
range: string
required: true

```
</details>