# Enum: MappingStatusEnum 



URI: [mediaingredientmech:MappingStatusEnum](https://w3id.org/mediaingredientmech/MappingStatusEnum)

## Permissible Values

| Value | Meaning | Description |
| --- | --- | --- |
| MAPPED | None | Has valid ontology mapping |
| UNMAPPED | None | No ontology mapping exists |
| PENDING_REVIEW | None | Suggested mapping awaiting review |
| IN_PROGRESS | None | Currently being curated |
| NEEDS_EXPERT | None | Requires expert domain knowledge |
| AMBIGUOUS | None | Multiple possible interpretations |
| REJECTED | None | Determined to be invalid or duplicate |




## Slots

| Name | Description |
| ---  | --- |
| [mapping_status](mapping_status.md) | Current mapping status |
| [previous_status](previous_status.md) | Status before this action |
| [new_status](new_status.md) | Status after this action |





## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/mediaingredientmech






## LinkML Source

<details>
```yaml
name: MappingStatusEnum
from_schema: https://w3id.org/mediaingredientmech
rank: 1000
permissible_values:
  MAPPED:
    text: MAPPED
    description: Has valid ontology mapping
  UNMAPPED:
    text: UNMAPPED
    description: No ontology mapping exists
  PENDING_REVIEW:
    text: PENDING_REVIEW
    description: Suggested mapping awaiting review
  IN_PROGRESS:
    text: IN_PROGRESS
    description: Currently being curated
  NEEDS_EXPERT:
    text: NEEDS_EXPERT
    description: Requires expert domain knowledge
  AMBIGUOUS:
    text: AMBIGUOUS
    description: Multiple possible interpretations
  REJECTED:
    text: REJECTED
    description: Determined to be invalid or duplicate

```
</details>