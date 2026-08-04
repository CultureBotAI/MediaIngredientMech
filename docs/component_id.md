

# Slot: component_id 


_Identifier of the component when mapped to an ontology/registry term (e.g. CHEBI:..., or a registry CURIE). Omit when the component is unmapped. (No pattern constraint: components may be unmapped.)_





URI: [mediaingredientmech:component_id](https://w3id.org/mediaingredientmech/component_id)
Alias: component_id

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [StockComponent](StockComponent.md) | One constituent of a stock solution or defined medium recipe — a component in... |  no  |






## Properties

* Range: [String](String.md)




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
description: 'Identifier of the component when mapped to an ontology/registry term
  (e.g. CHEBI:..., or a registry CURIE). Omit when the component is unmapped. (No
  pattern constraint: components may be unmapped.)'
from_schema: https://w3id.org/mediaingredientmech
rank: 1000
alias: component_id
owner: StockComponent
domain_of:
- StockComponent
range: string

```
</details>