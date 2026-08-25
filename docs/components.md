

# Slot: components


_A has-part decomposition for a STOCK_SOLUTION, DEFINED_MEDIUM, or UNDEFINED_MIXTURE: the list of component ingredients (with concentration where known). This is ingredient/mixture partonomy, not an identity mapping, a complete culturing recipe, or the parent/child variant hierarchy. It may transcribe a combination label. Populate only from verifiable evidence; omit the slot when no constituent is known. When present, component_assertion records how the decomposition was made and its evidence._





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
description: 'A has-part decomposition for a STOCK_SOLUTION, DEFINED_MEDIUM, or UNDEFINED_MIXTURE:
  the list of component ingredients (with concentration where known). This is ingredient/mixture
  partonomy, not an identity mapping, a complete culturing recipe, or the parent/child
  variant hierarchy. It may transcribe a combination label. Populate only from verifiable
  evidence; omit the slot when no constituent is known. When present, component_assertion
  records how the decomposition was made and its evidence.'
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