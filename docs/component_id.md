

# Slot: component_id 


_Semantic CURIE for the component (e.g. CHEBI:..., MICRO:..., or cas:...). It is not unconditionally a foreign key to one MIM row: reference_scope states whether the CURIE is represented in MIM or deliberately external. Omit only when reference_scope is UNMAPPED._





URI: [mediaingredientmech:component_id](https://w3id.org/mediaingredientmech/component_id)
Alias: component_id

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [StockComponent](StockComponent.md) | One constituent in an IngredientRecord |  no  |






## Properties

* Range: [String](String.md)

* Regex pattern: `^[A-Za-z][A-Za-z0-9.]*:[A-Za-z0-9][A-Za-z0-9._~-]*$`




## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/mediaingredientmech




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | mediaingredientmech:component_id |
| native | mediaingredientmech:component_id |




## LinkML Source

<details>
```yaml
name: component_id
description: 'Semantic CURIE for the component (e.g. CHEBI:..., MICRO:..., or cas:...).
  It is not unconditionally a foreign key to one MIM row: reference_scope states whether
  the CURIE is represented in MIM or deliberately external. Omit only when reference_scope
  is UNMAPPED.'
from_schema: https://w3id.org/mediaingredientmech
rank: 1000
alias: component_id
owner: StockComponent
domain_of:
- StockComponent
range: string
pattern: ^[A-Za-z][A-Za-z0-9.]*:[A-Za-z0-9][A-Za-z0-9._~-]*$

```
</details>