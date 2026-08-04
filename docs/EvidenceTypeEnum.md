# Enum: EvidenceTypeEnum 



URI: [mediaingredientmech:EvidenceTypeEnum](https://w3id.org/mediaingredientmech/EvidenceTypeEnum)

## Permissible Values

| Value | Meaning | Description |
| --- | --- | --- |
| DATABASE_MATCH | None | Direct match in ontology database |
| CURATOR_JUDGMENT | None | Expert curator decision |
| LLM_SUGGESTION | None | LLM-generated suggestion |
| LITERATURE | None | Based on literature evidence |
| TEXT_SIMILARITY | None | Based on text similarity metrics |
| CROSS_REFERENCE | None | Cross-reference to other database |
| LEXICAL_MATCH | None | Lexical (token-overlap / normalized-name) match against an ontology label or ... |
| CAS_RN_CROSS_REFERENCE | None | Identity established via CAS Registry Number cross-reference rather than onto... |
| MANUAL_CURATION | None | Manually curated evidence supplied by a human reviewer (distinct from CURATOR... |
| MANUAL_REVIEW | None | Identity confirmed during a manual review pass |
| CURATOR_CONFIRMED_SYNONYM | None | Curator confirmed a synonym match found by tooling |




## Slots

| Name | Description |
| ---  | --- |
| [evidence_type](evidence_type.md) | Type of evidence |





## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/mediaingredientmech






## LinkML Source

<details>
```yaml
name: EvidenceTypeEnum
from_schema: https://w3id.org/mediaingredientmech
rank: 1000
permissible_values:
  DATABASE_MATCH:
    text: DATABASE_MATCH
    description: Direct match in ontology database
  CURATOR_JUDGMENT:
    text: CURATOR_JUDGMENT
    description: Expert curator decision
  LLM_SUGGESTION:
    text: LLM_SUGGESTION
    description: LLM-generated suggestion
  LITERATURE:
    text: LITERATURE
    description: Based on literature evidence
  TEXT_SIMILARITY:
    text: TEXT_SIMILARITY
    description: Based on text similarity metrics
  CROSS_REFERENCE:
    text: CROSS_REFERENCE
    description: Cross-reference to other database
  LEXICAL_MATCH:
    text: LEXICAL_MATCH
    description: Lexical (token-overlap / normalized-name) match against an ontology
      label or synonym.
  CAS_RN_CROSS_REFERENCE:
    text: CAS_RN_CROSS_REFERENCE
    description: Identity established via CAS Registry Number cross-reference rather
      than ontology label match.
  MANUAL_CURATION:
    text: MANUAL_CURATION
    description: Manually curated evidence supplied by a human reviewer (distinct
      from CURATOR_JUDGMENT, which records the decision rather than the source of
      evidence).
  MANUAL_REVIEW:
    text: MANUAL_REVIEW
    description: Identity confirmed during a manual review pass.
  CURATOR_CONFIRMED_SYNONYM:
    text: CURATOR_CONFIRMED_SYNONYM
    description: Curator confirmed a synonym match found by tooling.

```
</details>