# Enum: EvidenceTypeEnum 



URI: [mediaingredientmech:EvidenceTypeEnum](https://w3id.org/mediaingredientmech/EvidenceTypeEnum)

## Permissible Values

| Value | Meaning | Description |
| --- | --- | --- |
| DATABASE_MATCH | None | Direct match in ontology database |
| CURATOR_JUDGMENT | None | Expert curator decision |
| LLM_SUGGESTION | None | LLM-generated suggestion |
| LITERATURE | None | Based on literature evidence |
| TEXT_SIMILARITY | None | Based on text similarity metrics |
| CROSS_REFERENCE | None | Cross-reference to other database |




## Slots

| Name | Description |
| ---  | --- |
| [evidence_type](evidence_type.md) | Type of evidence |





## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/mediaingredientmech






## LinkML Source

<details>
```yaml
name: EvidenceTypeEnum
from_schema: https://w3id.org/mediaingredientmech
rank: 1000
permissible_values:
  DATABASE_MATCH:
    text: DATABASE_MATCH
    description: Direct match in ontology database
  CURATOR_JUDGMENT:
    text: CURATOR_JUDGMENT
    description: Expert curator decision
  LLM_SUGGESTION:
    text: LLM_SUGGESTION
    description: LLM-generated suggestion
  LITERATURE:
    text: LITERATURE
    description: Based on literature evidence
  TEXT_SIMILARITY:
    text: TEXT_SIMILARITY
    description: Based on text similarity metrics
  CROSS_REFERENCE:
    text: CROSS_REFERENCE
    description: Cross-reference to other database

```
</details>