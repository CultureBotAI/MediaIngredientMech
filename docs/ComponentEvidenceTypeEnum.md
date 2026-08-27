# Enum: ComponentEvidenceTypeEnum 




_Kind of evidence supporting a component decomposition._



URI: [mediaingredientmech:ComponentEvidenceTypeEnum](https://w3id.org/mediaingredientmech/ComponentEvidenceTypeEnum)

## Permissible Values

| Value | Meaning | Description |
| --- | --- | --- |
| SOURCE_LABEL | None | The upstream label explicitly enumerates the constituents |
| CURATED_DATASET | None | A reviewed structured curation table supplies the constituents |
| MANUAL_CURATION | None | A curator established the constituent list and recorded the rationale |
| RECIPE_SOURCE | None | A cited medium or stock-solution recipe supplies the constituents |
| PUBLICATION | None | A publication supplies or directly supports the constituent list |








## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/mediaingredientmech






## LinkML Source

<details>
```yaml
name: ComponentEvidenceTypeEnum
description: Kind of evidence supporting a component decomposition.
from_schema: https://w3id.org/mediaingredientmech
rank: 1000
permissible_values:
  SOURCE_LABEL:
    text: SOURCE_LABEL
    description: The upstream label explicitly enumerates the constituents.
  CURATED_DATASET:
    text: CURATED_DATASET
    description: A reviewed structured curation table supplies the constituents.
  MANUAL_CURATION:
    text: MANUAL_CURATION
    description: A curator established the constituent list and recorded the rationale.
  RECIPE_SOURCE:
    text: RECIPE_SOURCE
    description: A cited medium or stock-solution recipe supplies the constituents.
  PUBLICATION:
    text: PUBLICATION
    description: A publication supplies or directly supports the constituent list.

```
</details>