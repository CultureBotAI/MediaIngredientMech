# Enum: ProteinGroundingStatusEnum 




_Review disposition for a node without an exact CURIE._



URI: [mediaingredientmech:ProteinGroundingStatusEnum](https://w3id.org/mediaingredientmech/ProteinGroundingStatusEnum)

## Permissible Values

| Value | Meaning | Description |
| --- | --- | --- |
| REVIEWED_LABEL_ONLY | None | The evidence supports the label, but no exact family, function or complex ter... |




## Slots

| Name | Description |
| ---  | --- |
| [grounding_status](grounding_status.md) |  |





## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/mediaingredientmech






## LinkML Source

<details>
```yaml
name: ProteinGroundingStatusEnum
description: Review disposition for a node without an exact CURIE.
from_schema: https://w3id.org/mediaingredientmech
rank: 1000
permissible_values:
  REVIEWED_LABEL_ONLY:
    text: REVIEWED_LABEL_ONLY
    description: The evidence supports the label, but no exact family, function or
      complex term can be asserted without overclaiming.

```
</details>