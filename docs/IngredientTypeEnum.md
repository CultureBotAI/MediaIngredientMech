# Enum: IngredientTypeEnum 




_Classification of ingredient entry type_



URI: [mediaingredientmech:IngredientTypeEnum](https://w3id.org/mediaingredientmech/IngredientTypeEnum)

## Permissible Values

| Value | Meaning | Description |
| --- | --- | --- |
| SINGLE_INGREDIENT | None | Pure chemical compound or single ingredient (e |
| NAMED_MEDIUM | None | A complete, named medium formulation or recipe with multiple ingredients (e |
| UNDEFINED_MIXTURE | None | Complex mixture of unknown or variable composition (e |
| STOCK_SOLUTION | None | Pre-mixed solution of defined ingredients (e |




## Slots

| Name | Description |
| ---  | --- |
| [ingredient_type](ingredient_type.md) | Classification of entry type: single chemical ingredient vs whole named mediu... |





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
  NAMED_MEDIUM:
    text: NAMED_MEDIUM
    description: 'A complete, named medium formulation or recipe with multiple ingredients
      (e.g., R2A agar, LB broth, Marine agar 2216, Oatmeal agar). Denotes RECORD GRANULARITY
      -- this record is a whole named medium rather than a single ingredient. Complex,
      undefined components (digests, infusions, extracts, sera) are expected and normal
      in these records; the compositional distinction is carried by UNDEFINED_MIXTURE,
      not by this value. Should cross-reference to CultureMech for the full recipe.
      Spelled DEFINED_MEDIUM before #222, which renamed it because "DEFINED" read
      as the microbiology term of art "chemically defined medium" -- see #478 for
      the remaining conflation, that this enum mixes granularity (SINGLE_INGREDIENT
      / NAMED_MEDIUM / STOCK_SOLUTION) with composition (UNDEFINED_MIXTURE).'
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