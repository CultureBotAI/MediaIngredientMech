# Enum: IngredientTypeEnum 




_Classification of ingredient entry type_



URI: [mediaingredientmech:IngredientTypeEnum](https://w3id.org/mediaingredientmech/IngredientTypeEnum)

## Permissible Values

| Value | Meaning | Description |
| --- | --- | --- |
| SINGLE_INGREDIENT | None | Pure chemical compound or single ingredient (e |
| DEFINED_MEDIUM | None | Complete medium formulation or recipe with multiple ingredients (e |
| UNDEFINED_MIXTURE | None | Complex mixture of unknown or variable composition (e |
| STOCK_SOLUTION | None | Pre-mixed solution of defined ingredients (e |




## Slots

| Name | Description |
| ---  | --- |
| [ingredient_type](ingredient_type.md) | Classification of entry type: single chemical ingredient vs complex defined m... |





## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/mediaingredientmech






## LinkML Source

<details>
```yaml
name: IngredientTypeEnum
description: Classification of ingredient entry type
from_schema: https://w3id.org/mediaingredientmech
rank: 1000
permissible_values:
  SINGLE_INGREDIENT:
    text: SINGLE_INGREDIENT
    description: Pure chemical compound or single ingredient (e.g., NaCl, agar, glucose,
      water). Can be mapped to chemical ontologies like CHEBI.
  DEFINED_MEDIUM:
    text: DEFINED_MEDIUM
    description: Complete medium formulation or recipe with multiple ingredients (e.g.,
      R2A agar, LB broth, Marine agar 2216, Oatmeal agar). Should cross-reference
      to CultureMech for full recipe.
  UNDEFINED_MIXTURE:
    text: UNDEFINED_MIXTURE
    description: Complex mixture of unknown or variable composition (e.g., yeast extract,
      peptone, soil extract). Components not fully characterized.
  STOCK_SOLUTION:
    text: STOCK_SOLUTION
    description: Pre-mixed solution of defined ingredients (e.g., vitamin B12 solution,
      trace metal mix). Components known but premixed for convenience.

```
</details>