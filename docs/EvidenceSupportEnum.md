# Enum: EvidenceSupportEnum 




_How a cited reference relates to the claim it is attached to_



URI: [mediaingredientmech:EvidenceSupportEnum](https://w3id.org/mediaingredientmech/EvidenceSupportEnum)

## Permissible Values

| Value | Meaning | Description |
| --- | --- | --- |
| SUPPORT | None | Reference substantiates the claim |
| PARTIAL | None | Reference touches adjacent context but does not directly substantiate |
| REFUTE | None | Reference contradicts the claim |
| NO_EVIDENCE | None | Reference cited but no extractable supporting snippet |
| WRONG_STATEMENT | None | Reference is incorrectly cited (placeholder for legacy data; |




## Slots

| Name | Description |
| ---  | --- |
| [supports](supports.md) | How the cited reference relates to the mapping claim |





## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/mediaingredientmech






## LinkML Source

<details>
```yaml
name: EvidenceSupportEnum
description: How a cited reference relates to the claim it is attached to
from_schema: https://w3id.org/mediaingredientmech
rank: 1000
permissible_values:
  SUPPORT:
    text: SUPPORT
    description: Reference substantiates the claim
  PARTIAL:
    text: PARTIAL
    description: Reference touches adjacent context but does not directly substantiate
  REFUTE:
    text: REFUTE
    description: Reference contradicts the claim
  NO_EVIDENCE:
    text: NO_EVIDENCE
    description: Reference cited but no extractable supporting snippet
  WRONG_STATEMENT:
    text: WRONG_STATEMENT
    description: 'Reference is incorrectly cited (placeholder for legacy data;

      flagged for cleanup)

      '

```
</details>