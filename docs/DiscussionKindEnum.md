# Enum: DiscussionKindEnum 




_Kind of unresolved / in-progress item captured by a Discussion. Knowledge gaps are represented as a discussion kind so they reuse the shared pointer, evidence, and lifecycle machinery, while optional proposed experiments capture how a gap could be resolved._



URI: [mediaingredientmech:DiscussionKindEnum](https://w3id.org/mediaingredientmech/DiscussionKindEnum)

## Permissible Values

| Value | Meaning | Description |
| --- | --- | --- |
| OPEN_QUESTION | None | An unresolved scientific question posed by curators or experts |
| KNOWLEDGE_GAP | None | A missing causal, evidentiary, model-system, or measurement assertion whose r... |
| CONTROVERSY | None | A live disagreement or competing interpretation between published positions |
| CURATION_TODO | None | A curation task captured inline (e |
| EMERGING_HYPOTHESIS | None | A recently reported hypothesis under active discussion in the community |
| INTERPRETATION | None | A discussion about how to interpret existing evidence or model an edge |
| HUMAN_MODEL_MISMATCH | None | A gap where evidence exists in one system but its fidelity to the target cont... |




## Slots

| Name | Description |
| ---  | --- |
| [kind](kind.md) |  |





## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/mediaingredientmech






## LinkML Source

<details>
```yaml
name: DiscussionKindEnum
description: Kind of unresolved / in-progress item captured by a Discussion. Knowledge
  gaps are represented as a discussion kind so they reuse the shared pointer, evidence,
  and lifecycle machinery, while optional proposed experiments capture how a gap could
  be resolved.
from_schema: https://w3id.org/mediaingredientmech
rank: 1000
permissible_values:
  OPEN_QUESTION:
    text: OPEN_QUESTION
    description: An unresolved scientific question posed by curators or experts.
  KNOWLEDGE_GAP:
    text: KNOWLEDGE_GAP
    description: A missing causal, evidentiary, model-system, or measurement assertion
      whose resolution would materially improve the record.
  CONTROVERSY:
    text: CONTROVERSY
    description: A live disagreement or competing interpretation between published
      positions.
  CURATION_TODO:
    text: CURATION_TODO
    description: A curation task captured inline (e.g. "ingredient needs CHEBI refinement").
  EMERGING_HYPOTHESIS:
    text: EMERGING_HYPOTHESIS
    description: A recently reported hypothesis under active discussion in the community.
  INTERPRETATION:
    text: INTERPRETATION
    description: A discussion about how to interpret existing evidence or model an
      edge.
  HUMAN_MODEL_MISMATCH:
    text: HUMAN_MODEL_MISMATCH
    description: A gap where evidence exists in one system but its fidelity to the
      target context is uncertain (e.g. an in-vitro/model result whose transfer to
      the in-situ or host-associated setting is unverified).

```
</details>