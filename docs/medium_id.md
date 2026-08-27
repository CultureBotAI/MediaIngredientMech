

# Slot: medium_id 


_The stable CultureMech recipe id. Every recipe in `data/normalized_yaml/` carries one as its first field, and they are unique across all 15877 of them._





URI: [mediaingredientmech:medium_id](https://w3id.org/mediaingredientmech/medium_id)
Alias: medium_id

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [CultureMechReference](CultureMechReference.md) | A verified link from a MIM record to a CultureMech recipe, carried by stable ... |  no  |






## Properties

* Range: [String](String.md)

* Required: True

* Regex pattern: `^CultureMech:[0-9]{6}$`




## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/mediaingredientmech




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | mediaingredientmech:medium_id |
| native | mediaingredientmech:medium_id |




## LinkML Source

<details>
```yaml
name: medium_id
description: The stable CultureMech recipe id. Every recipe in `data/normalized_yaml/`
  carries one as its first field, and they are unique across all 15877 of them.
from_schema: https://w3id.org/mediaingredientmech
rank: 1000
alias: medium_id
owner: CultureMechReference
domain_of:
- CultureMechReference
range: string
required: true
pattern: ^CultureMech:[0-9]{6}$

```
</details>