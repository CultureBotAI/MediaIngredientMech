# Enum: EvidenceSourceEnum 




_Study or data-source type providing a claim's evidence. This is independent of supports, citation identifiers, quotation location, and curation method._



URI: [mediaingredientmech:EvidenceSourceEnum](https://w3id.org/mediaingredientmech/EvidenceSourceEnum)

## Permissible Values

| Value | Meaning | Description |
| --- | --- | --- |
| FIELD_STUDY | None | Observation or measurement made in a natural system |
| MESOCOSM | None | Experiment in a controlled enclosure representing a natural system |
| LABORATORY | None | Controlled laboratory study; use IN_VITRO or IN_VIVO when that distinction is... |
| IN_VITRO | None | Experiment outside an intact organism, such as a culture or biochemical assay |
| IN_VIVO | None | Experiment or observation in an intact living organism |
| COMPUTATIONAL | None | Model, simulation, prediction, or computational analysis providing the cited ... |
| META_ANALYSIS | None | Systematic synthesis or quantitative analysis of results across studies |
| REVIEW | None | Narrative review or expert synthesis of published work |
| REMOTE_SENSING | None | Satellite, aerial, or other remotely sensed observations |
| LONG_TERM_MONITORING | None | Repeated observations from a long-term monitoring programme |
| EXPERT_OPINION | None | Expert judgement or consensus rather than a primary experimental result |
| DATABASE | None | Assertion or observation obtained from a database or curated data resource |
| OTHER | None | A known study or data-source type outside these categories; explain it in not... |




## Slots

| Name | Description |
| ---  | --- |
| [evidence_source](evidence_source.md) | Study or data-source type behind the cited evidence, not the curation method ... |





## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/mediaingredientmech






## LinkML Source

<details>
```yaml
name: EvidenceSourceEnum
description: Study or data-source type providing a claim's evidence. This is independent
  of supports, citation identifiers, quotation location, and curation method.
from_schema: https://w3id.org/mediaingredientmech
rank: 1000
permissible_values:
  FIELD_STUDY:
    text: FIELD_STUDY
    description: Observation or measurement made in a natural system.
  MESOCOSM:
    text: MESOCOSM
    description: Experiment in a controlled enclosure representing a natural system.
  LABORATORY:
    text: LABORATORY
    description: Controlled laboratory study; use IN_VITRO or IN_VIVO when that distinction
      is known.
  IN_VITRO:
    text: IN_VITRO
    description: Experiment outside an intact organism, such as a culture or biochemical
      assay.
  IN_VIVO:
    text: IN_VIVO
    description: Experiment or observation in an intact living organism.
  COMPUTATIONAL:
    text: COMPUTATIONAL
    description: Model, simulation, prediction, or computational analysis providing
      the cited evidence.
  META_ANALYSIS:
    text: META_ANALYSIS
    description: Systematic synthesis or quantitative analysis of results across studies.
  REVIEW:
    text: REVIEW
    description: Narrative review or expert synthesis of published work.
  REMOTE_SENSING:
    text: REMOTE_SENSING
    description: Satellite, aerial, or other remotely sensed observations.
  LONG_TERM_MONITORING:
    text: LONG_TERM_MONITORING
    description: Repeated observations from a long-term monitoring programme.
  EXPERT_OPINION:
    text: EXPERT_OPINION
    description: Expert judgement or consensus rather than a primary experimental
      result.
  DATABASE:
    text: DATABASE
    description: Assertion or observation obtained from a database or curated data
      resource.
  OTHER:
    text: OTHER
    description: A known study or data-source type outside these categories; explain
      it in notes or explanation.

```
</details>