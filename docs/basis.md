

# Slot: basis 


_How the relation was established, for example SAME_INCHIKEY for an exact chemical-structure join. A match on a protein or reaction must not be presented as sufficient evidence for a stronger relation._





URI: [mediaingredientmech:basis](https://w3id.org/mediaingredientmech/basis)
Alias: basis

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [CrossCorpusLink](CrossCorpusLink.md) | A directed link from the containing record or sub-object to a record in anoth... |  no  |






## Properties

* Range: [String](String.md)

* Required: True




## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/mediaingredientmech




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | mediaingredientmech:basis |
| native | mediaingredientmech:basis |




## LinkML Source

<details>
```yaml
name: basis
description: How the relation was established, for example SAME_INCHIKEY for an exact
  chemical-structure join. A match on a protein or reaction must not be presented
  as sufficient evidence for a stronger relation.
from_schema: https://w3id.org/mediaingredientmech
rank: 1000
alias: basis
owner: CrossCorpusLink
domain_of:
- CrossCorpusLink
range: string
required: true

```
</details>