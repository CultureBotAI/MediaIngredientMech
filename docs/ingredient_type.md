

# Slot: ingredient_type 


_Classification of entry type: single chemical ingredient vs whole named medium. SINGLE_INGREDIENT: Pure chemical (NaCl, agar, glucose). NAMED_MEDIUM: A complete, named medium formulation/recipe (R2A agar, LB broth) -- "defined" = record granularity (a whole named medium), NOT "chemically defined"; undefined components are expected. UNDEFINED_MIXTURE: Complex mixture of unknown composition (yeast extract, peptone). STOCK_SOLUTION: Pre-mixed solution of defined ingredients._





URI: [mediaingredientmech:ingredient_type](https://w3id.org/mediaingredientmech/ingredient_type)
Alias: ingredient_type

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [IngredientRecord](IngredientRecord.md) | Core record for a media ingredient with ontology mapping, synonyms, and curat... |  no  |






## Properties

* Range: [IngredientTypeEnum](IngredientTypeEnum.md)




## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/mediaingredientmech




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | mediaingredientmech:ingredient_type |
| native | mediaingredientmech:ingredient_type |




## LinkML Source

<details>
```yaml
name: ingredient_type
description: 'Classification of entry type: single chemical ingredient vs whole named
  medium. SINGLE_INGREDIENT: Pure chemical (NaCl, agar, glucose). NAMED_MEDIUM: A
  complete, named medium formulation/recipe (R2A agar, LB broth) -- "defined" = record
  granularity (a whole named medium), NOT "chemically defined"; undefined components
  are expected. UNDEFINED_MIXTURE: Complex mixture of unknown composition (yeast extract,
  peptone). STOCK_SOLUTION: Pre-mixed solution of defined ingredients.'
from_schema: https://w3id.org/mediaingredientmech
rank: 1000
alias: ingredient_type
owner: IngredientRecord
domain_of:
- IngredientRecord
range: IngredientTypeEnum

```
</details>