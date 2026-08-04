# Enum: EnvironmentRelevanceEnum 




_Describes why an ingredient is relevant to a particular environment. Mirrors the enum in mapped_ingredients_schema.yaml._



URI: [mediaingredientmech:EnvironmentRelevanceEnum](https://w3id.org/mediaingredientmech/EnvironmentRelevanceEnum)

## Permissible Values

| Value | Meaning | Description |
| --- | --- | --- |
| NATURAL_SOURCE | None | Ingredient is naturally found in or sourced from this environment |
| REQUIRED_FOR_ORGANISM | None | Required for cultivating organisms from this environment |
| SELECTIVE_AGENT | None | Selectively promotes growth of organisms from this environment |
| ENVIRONMENT_MIMIC | None | Helps replicate the chemical conditions of this environment in vitro |
| COMMONLY_USED | None | Commonly used in media targeting organisms from this environment |




## Slots

| Name | Description |
| ---  | --- |
| [relevance](relevance.md) | Why this ingredient is relevant to the specified environment |





## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/mediaingredientmech






## LinkML Source

<details>
```yaml
name: EnvironmentRelevanceEnum
description: Describes why an ingredient is relevant to a particular environment.
  Mirrors the enum in mapped_ingredients_schema.yaml.
from_schema: https://w3id.org/mediaingredientmech
rank: 1000
permissible_values:
  NATURAL_SOURCE:
    text: NATURAL_SOURCE
    description: Ingredient is naturally found in or sourced from this environment
  REQUIRED_FOR_ORGANISM:
    text: REQUIRED_FOR_ORGANISM
    description: Required for cultivating organisms from this environment
  SELECTIVE_AGENT:
    text: SELECTIVE_AGENT
    description: Selectively promotes growth of organisms from this environment
  ENVIRONMENT_MIMIC:
    text: ENVIRONMENT_MIMIC
    description: Helps replicate the chemical conditions of this environment in vitro
  COMMONLY_USED:
    text: COMMONLY_USED
    description: Commonly used in media targeting organisms from this environment

```
</details>