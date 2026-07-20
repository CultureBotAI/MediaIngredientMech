# Enum: SupportLevelEnum 




_How a SupportingReference bears on the claim it is attached to (mirrors the supports semantics already used in the Mech EvidenceItem models)._



URI: [mediaingredientmech:SupportLevelEnum](https://w3id.org/mediaingredientmech/SupportLevelEnum)

## Permissible Values

| Value | Meaning | Description |
| --- | --- | --- |
| SUPPORT | None | The source supports the claim |
| REFUTE | None | The source contradicts the claim |
| PARTIAL | None | The source partially supports the claim or supports it with caveats |
| NO_EVIDENCE | None | The source is relevant context but does not directly bear on the claim |
| WRONG_STATEMENT | None | The cited statement was found to be incorrect (kept for provenance) |








## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/mediaingredientmech






## LinkML Source

<details>
```yaml
name: SupportLevelEnum
description: How a SupportingReference bears on the claim it is attached to (mirrors
  the supports semantics already used in the Mech EvidenceItem models).
from_schema: https://w3id.org/mediaingredientmech
rank: 1000
permissible_values:
  SUPPORT:
    text: SUPPORT
    description: The source supports the claim.
  REFUTE:
    text: REFUTE
    description: The source contradicts the claim.
  PARTIAL:
    text: PARTIAL
    description: The source partially supports the claim or supports it with caveats.
  NO_EVIDENCE:
    text: NO_EVIDENCE
    description: The source is relevant context but does not directly bear on the
      claim.
  WRONG_STATEMENT:
    text: WRONG_STATEMENT
    description: The cited statement was found to be incorrect (kept for provenance).

```
</details>