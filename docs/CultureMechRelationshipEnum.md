# Enum: CultureMechRelationshipEnum 




_How a MIM record relates to the CultureMech recipe it references_



URI: [mediaingredientmech:CultureMechRelationshipEnum](https://w3id.org/mediaingredientmech/CultureMechRelationshipEnum)

## Permissible Values

| Value | Meaning | Description |
| --- | --- | --- |
| EXACT_FORMULATION | None | The same formulation |
| VARIANT_OF | None | A documented variant of that recipe -- a modification of it rather than a dif... |
| SIMILAR_COMPOSITION | None | Compositionally close but not identical, with the differences recorded in `ev... |
| CANDIDATE_UNVERIFIED | None | A candidate proposed by matching but not yet confirmed by a curator |




## Slots

| Name | Description |
| ---  | --- |
| [relationship](relationship.md) | How this record relates to that recipe |





## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/mediaingredientmech






## LinkML Source

<details>
```yaml
name: CultureMechRelationshipEnum
description: How a MIM record relates to the CultureMech recipe it references
from_schema: https://w3id.org/mediaingredientmech
rank: 1000
permissible_values:
  EXACT_FORMULATION:
    text: EXACT_FORMULATION
    description: The same formulation. Asserted only when composition was compared,
      not when names agree.
  VARIANT_OF:
    text: VARIANT_OF
    description: A documented variant of that recipe -- a modification of it rather
      than a different medium.
  SIMILAR_COMPOSITION:
    text: SIMILAR_COMPOSITION
    description: Compositionally close but not identical, with the differences recorded
      in `evidence`. The honest value when recipes overlap substantially and disagree
      in named ways.
  CANDIDATE_UNVERIFIED:
    text: CANDIDATE_UNVERIFIED
    description: 'A candidate proposed by matching but not yet confirmed by a curator.
      Exists so "not linked" and "linked but unchecked" are different states: absence
      would otherwise conflate a record nobody has looked at with one whose candidate
      was rejected. Never written by an automated matcher into an accepted link.'

```
</details>