# Enum: ComponentCompletenessEnum 




_Completeness of a component decomposition relative to its cited source._



URI: [mediaingredientmech:ComponentCompletenessEnum](https://w3id.org/mediaingredientmech/ComponentCompletenessEnum)

## Permissible Values

| Value | Meaning | Description |
| --- | --- | --- |
| COMPLETE | None | The source explicitly establishes that the listed constituents are complete |
| PARTIAL | None | The source explicitly indicates that additional constituents are omitted |
| UNKNOWN | None | The source does not establish whether the list is complete |




## Slots

| Name | Description |
| ---  | --- |
| [completeness](completeness.md) | Whether the cited source establishes a complete constituent list |





## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/mediaingredientmech






## LinkML Source

<details>
```yaml
name: ComponentCompletenessEnum
description: Completeness of a component decomposition relative to its cited source.
from_schema: https://w3id.org/mediaingredientmech
rank: 1000
permissible_values:
  COMPLETE:
    text: COMPLETE
    description: The source explicitly establishes that the listed constituents are
      complete.
  PARTIAL:
    text: PARTIAL
    description: The source explicitly indicates that additional constituents are
      omitted.
  UNKNOWN:
    text: UNKNOWN
    description: The source does not establish whether the list is complete.

```
</details>