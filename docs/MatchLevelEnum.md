# Enum: MatchLevelEnum 



URI: [mediaingredientmech:MatchLevelEnum](https://w3id.org/mediaingredientmech/MatchLevelEnum)

## Permissible Values

| Value | Meaning | Description |
| --- | --- | --- |
| EXACT | None | Direct string match with no normalization |
| NORMALIZED | None | Chemical normalization applied (hydrate strip, formula fix, catalog removal) |
| FUZZY | None | Synonym matching or semantic similarity |
| MANUAL | None | Expert or LLM-assisted curation |
| UNMAPPABLE | None | Cannot reliably map to ontology |
| UNKNOWN | None | Match method not recorded or imported from external source |




## Slots

| Name | Description |
| ---  | --- |
| [match_level](match_level.md) | Technical method used to find this mapping |





## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/mediaingredientmech






## LinkML Source

<details>
```yaml
name: MatchLevelEnum
from_schema: https://w3id.org/mediaingredientmech
rank: 1000
permissible_values:
  EXACT:
    text: EXACT
    description: Direct string match with no normalization
  NORMALIZED:
    text: NORMALIZED
    description: Chemical normalization applied (hydrate strip, formula fix, catalog
      removal)
  FUZZY:
    text: FUZZY
    description: Synonym matching or semantic similarity
  MANUAL:
    text: MANUAL
    description: Expert or LLM-assisted curation
  UNMAPPABLE:
    text: UNMAPPABLE
    description: Cannot reliably map to ontology
  UNKNOWN:
    text: UNKNOWN
    description: Match method not recorded or imported from external source

```
</details>