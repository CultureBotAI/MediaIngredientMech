

# Slot: mim_id 


_Permanent opaque record identifier from the append-only MIM registry. Preserved through name, filename, mapping and status changes; never reused._





URI: [mediaingredientmech:mim_id](https://w3id.org/mediaingredientmech/mim_id)
Alias: mim_id

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [IngredientRecord](IngredientRecord.md) | Core record for a media ingredient with ontology mapping, synonyms, and curat... |  no  |






## Properties

* Range: [String](String.md)

* Required: True

* Regex pattern: `^MIM:(?!0000000)[0-9]{7}(?![\s\S])`




## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/mediaingredientmech




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | mediaingredientmech:mim_id |
| native | mediaingredientmech:mim_id |




## LinkML Source

<details>
```yaml
name: mim_id
description: Permanent opaque record identifier from the append-only MIM registry.
  Preserved through name, filename, mapping and status changes; never reused.
from_schema: https://w3id.org/mediaingredientmech
rank: 1000
identifier: true
alias: mim_id
owner: IngredientRecord
domain_of:
- IngredientRecord
range: string
required: true
pattern: ^MIM:(?!0000000)[0-9]{7}(?![\s\S])

```
</details>