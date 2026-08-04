

# Slot: components 


_Recipe-level decomposition for a STOCK_SOLUTION or DEFINED_MEDIUM: the list of component ingredients (with concentration where known). Lets a named mixture (e.g. a trace-element or vitamin solution) be resolved to its constituents. Populate only from a verifiable recipe source; leave empty when the composition is unknown._





URI: [mediaingredientmech:components](https://w3id.org/mediaingredientmech/components)
Alias: components

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [IngredientRecord](IngredientRecord.md) | Core record for a media ingredient with ontology mapping, synonyms, and curat... |  no  |






## Properties

* Range: [StockComponent](StockComponent.md)

* Multivalued: True




## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/mediaingredientmech




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | mediaingredientmech:components |
| native | mediaingredientmech:components |




## LinkML Source

<details>
```yaml
name: components
description: 'Recipe-level decomposition for a STOCK_SOLUTION or DEFINED_MEDIUM: the
  list of component ingredients (with concentration where known). Lets a named mixture
  (e.g. a trace-element or vitamin solution) be resolved to its constituents. Populate
  only from a verifiable recipe source; leave empty when the composition is unknown.'
from_schema: https://w3id.org/mediaingredientmech
rank: 1000
alias: components
owner: IngredientRecord
domain_of:
- IngredientRecord
range: StockComponent
multivalued: true
inlined: true
inlined_as_list: true

```
</details>