# Enum: ComponentMethodEnum 




_Method used to derive an IngredientRecord.components has-part list._



URI: [mediaingredientmech:ComponentMethodEnum](https://w3id.org/mediaingredientmech/ComponentMethodEnum)

## Permissible Values

| Value | Meaning | Description |
| --- | --- | --- |
| LABEL_ENUMERATION | None | Constituents were transcribed from a source label that explicitly enumerates ... |
| ABBREVIATION_EXPANSION | None | A curator expanded an abbreviation or named blend using a reviewed curation o... |
| CURATED_INTERPRETATION | None | A curator established the constituent list from reviewed evidence that is nei... |
| RECIPE_TRANSCRIPTION | None | Constituents and quantities were transcribed from a cited verified recipe |




## Slots

| Name | Description |
| ---  | --- |
| [method](method.md) | Method used to derive the constituent list |





## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/mediaingredientmech






## LinkML Source

<details>
```yaml
name: ComponentMethodEnum
description: Method used to derive an IngredientRecord.components has-part list.
from_schema: https://w3id.org/mediaingredientmech
rank: 1000
permissible_values:
  LABEL_ENUMERATION:
    text: LABEL_ENUMERATION
    description: Constituents were transcribed from a source label that explicitly
      enumerates them.
  ABBREVIATION_EXPANSION:
    text: ABBREVIATION_EXPANSION
    description: A curator expanded an abbreviation or named blend using a reviewed
      curation or research artifact; the parts are not all spelled out by the source
      label.
  CURATED_INTERPRETATION:
    text: CURATED_INTERPRETATION
    description: A curator established the constituent list from reviewed evidence
      that is neither a literal label enumeration nor a direct recipe transcription.
  RECIPE_TRANSCRIPTION:
    text: RECIPE_TRANSCRIPTION
    description: Constituents and quantities were transcribed from a cited verified
      recipe.

```
</details>