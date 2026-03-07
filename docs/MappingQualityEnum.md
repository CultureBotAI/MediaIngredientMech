# Enum: MappingQualityEnum 



URI: [mediaingredientmech:MappingQualityEnum](https://w3id.org/mediaingredientmech/MappingQualityEnum)

## Permissible Values

| Value | Meaning | Description |
| --- | --- | --- |
| EXACT_MATCH | None | Direct exact match to ontology term |
| SYNONYM_MATCH | None | Matches known synonym in ontology |
| CLOSE_MATCH | None | Semantically close but not exact |
| MANUAL_CURATION | None | Manually curated by expert |
| LLM_ASSISTED | None | Mapping suggested by LLM, human-verified |
| PROVISIONAL | None | Tentative mapping needing verification |




## Slots

| Name | Description |
| ---  | --- |
| [mapping_quality](mapping_quality.md) | Quality assessment of this mapping |





## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/mediaingredientmech






## LinkML Source

<details>
```yaml
name: MappingQualityEnum
from_schema: https://w3id.org/mediaingredientmech
rank: 1000
permissible_values:
  EXACT_MATCH:
    text: EXACT_MATCH
    description: Direct exact match to ontology term
  SYNONYM_MATCH:
    text: SYNONYM_MATCH
    description: Matches known synonym in ontology
  CLOSE_MATCH:
    text: CLOSE_MATCH
    description: Semantically close but not exact
  MANUAL_CURATION:
    text: MANUAL_CURATION
    description: Manually curated by expert
  LLM_ASSISTED:
    text: LLM_ASSISTED
    description: Mapping suggested by LLM, human-verified
  PROVISIONAL:
    text: PROVISIONAL
    description: Tentative mapping needing verification

```
</details>