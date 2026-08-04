# Enum: MappingQualityEnum 



URI: [mediaingredientmech:MappingQualityEnum](https://w3id.org/mediaingredientmech/MappingQualityEnum)

## Permissible Values

| Value | Meaning | Description |
| --- | --- | --- |
| EXACT_MATCH | None | Direct exact match to ontology term |
| SYNONYM_MATCH | None | Matches known synonym in ontology |
| CLOSE_MATCH | None | Semantically close but not exact |
| MANUAL_CURATION | None | Manually curated by expert |
| LLM_ASSISTED | None | Mapping suggested by LLM, human-verified |
| PROVISIONAL | None | Tentative mapping needing verification |
| NARROW_MATCH | None | Ontology term is narrower than the ingredient (more specific) |
| BROAD_MATCH | None | Ontology term is broader than the ingredient (less specific) |
| LEXICAL_MATCH | None | Lexical (string-level) match without semantic verification — typically a toke... |
| CAS_RN_LOOKUP | None | Mapping resolved via CAS Registry Number lookup rather than ontology label/sy... |
| FALLBACK_REGISTRY | None | Identity assigned via a registry-row fallback (`registry:` or `kgmicrobe |
| PLACEHOLDER | None | Mapping is a placeholder pending real curation (e |




## Slots

| Name | Description |
| ---  | --- |
| [mapping_quality](mapping_quality.md) | Quality assessment of this mapping |





## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/mediaingredientmech






## LinkML Source

<details>
```yaml
name: MappingQualityEnum
from_schema: https://w3id.org/mediaingredientmech
rank: 1000
permissible_values:
  EXACT_MATCH:
    text: EXACT_MATCH
    description: Direct exact match to ontology term
  SYNONYM_MATCH:
    text: SYNONYM_MATCH
    description: Matches known synonym in ontology
  CLOSE_MATCH:
    text: CLOSE_MATCH
    description: Semantically close but not exact
  MANUAL_CURATION:
    text: MANUAL_CURATION
    description: Manually curated by expert
  LLM_ASSISTED:
    text: LLM_ASSISTED
    description: Mapping suggested by LLM, human-verified
  PROVISIONAL:
    text: PROVISIONAL
    description: Tentative mapping needing verification
  NARROW_MATCH:
    text: NARROW_MATCH
    description: Ontology term is narrower than the ingredient (more specific). Used
      when the ingredient name covers a class and the chosen term covers one instance/subtype
      of that class.
  BROAD_MATCH:
    text: BROAD_MATCH
    description: Ontology term is broader than the ingredient (less specific).
  LEXICAL_MATCH:
    text: LEXICAL_MATCH
    description: Lexical (string-level) match without semantic verification — typically
      a token-overlap or normalized-name match.
  CAS_RN_LOOKUP:
    text: CAS_RN_LOOKUP
    description: Mapping resolved via CAS Registry Number lookup rather than ontology
      label/synonym match.
  FALLBACK_REGISTRY:
    text: FALLBACK_REGISTRY
    description: Identity assigned via a registry-row fallback (`registry:` or `kgmicrobe.compound:`
      / `kgmicrobe.ingredient:`) when no direct ontology term is available.
  PLACEHOLDER:
    text: PLACEHOLDER
    description: Mapping is a placeholder pending real curation (e.g. minted kg-microbe
      ingredient row, awaiting upgrade to CHEBI/FOODON/etc.).

```
</details>