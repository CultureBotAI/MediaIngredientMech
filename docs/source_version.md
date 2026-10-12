

# Slot: source_version 


_Pinned commit or release of the target corpus that was checked. Optional for compatibility with existing NaturalProductMech links; consumers should require a full immutable version for newly added links._





URI: [mediaingredientmech:source_version](https://w3id.org/mediaingredientmech/source_version)
Alias: source_version

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [CrossCorpusLink](CrossCorpusLink.md) | A directed link from the containing record or sub-object to a record in anoth... |  no  |






## Properties

* Range: [String](String.md)




## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/mediaingredientmech




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | mediaingredientmech:source_version |
| native | mediaingredientmech:source_version |




## LinkML Source

<details>
```yaml
name: source_version
description: Pinned commit or release of the target corpus that was checked. Optional
  for compatibility with existing NaturalProductMech links; consumers should require
  a full immutable version for newly added links.
from_schema: https://w3id.org/mediaingredientmech
rank: 1000
alias: source_version
owner: CrossCorpusLink
domain_of:
- CrossCorpusLink
range: string

```
</details>