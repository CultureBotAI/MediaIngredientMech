

# Slot: category 


_Categorization label for partitioned unmapped collections (e.g. PLACEHOLDER, COMPLEX_MEDIA, INCOMPLETE_FORMULA, OTHER, ALREADY_MAPPED). Set by scripts/categorize_unmapped.py; absent on the canonical mapped_ingredients.yaml / unmapped_ingredients.yaml._





URI: [mediaingredientmech:category](https://w3id.org/mediaingredientmech/category)
Alias: category

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [IngredientCollection](IngredientCollection.md) | Root container for all ingredient records |  no  |






## Properties

* Range: [String](String.md)




## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/mediaingredientmech




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | mediaingredientmech:category |
| native | mediaingredientmech:category |




## LinkML Source

<details>
```yaml
name: category
description: Categorization label for partitioned unmapped collections (e.g. PLACEHOLDER,
  COMPLEX_MEDIA, INCOMPLETE_FORMULA, OTHER, ALREADY_MAPPED). Set by scripts/categorize_unmapped.py;
  absent on the canonical mapped_ingredients.yaml / unmapped_ingredients.yaml.
from_schema: https://w3id.org/mediaingredientmech
rank: 1000
alias: category
owner: IngredientCollection
domain_of:
- IngredientCollection
range: string

```
</details>