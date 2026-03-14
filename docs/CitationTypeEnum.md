# Enum: CitationTypeEnum 




_Type of reference or citation_



URI: [mediaingredientmech:CitationTypeEnum](https://w3id.org/mediaingredientmech/CitationTypeEnum)

## Permissible Values

| Value | Meaning | Description |
| --- | --- | --- |
| PEER_REVIEWED_PUBLICATION | None | Peer-reviewed journal article or conference paper |
| PREPRINT | None | Preprint or non-peer-reviewed manuscript |
| DATABASE_ENTRY | None | Reference to database record or entry |
| TECHNICAL_REPORT | None | Technical report, manual, or documentation |
| MANUAL_CURATION | None | Expert manual curation without specific publication |
| COMPUTATIONAL_PREDICTION | None | Computational inference or prediction |




## Slots

| Name | Description |
| ---  | --- |
| [reference_type](reference_type.md) | Type of reference (peer-reviewed, database, manual curation, etc |





## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/mediaingredientmech






## LinkML Source

<details>
```yaml
name: CitationTypeEnum
description: Type of reference or citation
from_schema: https://w3id.org/mediaingredientmech
rank: 1000
permissible_values:
  PEER_REVIEWED_PUBLICATION:
    text: PEER_REVIEWED_PUBLICATION
    description: Peer-reviewed journal article or conference paper
  PREPRINT:
    text: PREPRINT
    description: Preprint or non-peer-reviewed manuscript
  DATABASE_ENTRY:
    text: DATABASE_ENTRY
    description: Reference to database record or entry
  TECHNICAL_REPORT:
    text: TECHNICAL_REPORT
    description: Technical report, manual, or documentation
  MANUAL_CURATION:
    text: MANUAL_CURATION
    description: Expert manual curation without specific publication
  COMPUTATIONAL_PREDICTION:
    text: COMPUTATIONAL_PREDICTION
    description: Computational inference or prediction

```
</details>