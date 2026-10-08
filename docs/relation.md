

# Slot: relation 


_Directed relation from the containing record or sub-object to the target. Consumers may constrain this string with a local enum through slot_usage on a subclass, without changing the shared module._





URI: [mediaingredientmech:relation](https://w3id.org/mediaingredientmech/relation)
Alias: relation

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
| self | mediaingredientmech:relation |
| native | mediaingredientmech:relation |




## LinkML Source

<details>
```yaml
name: relation
description: Directed relation from the containing record or sub-object to the target.
  Consumers may constrain this string with a local enum through slot_usage on a subclass,
  without changing the shared module.
from_schema: https://w3id.org/mediaingredientmech
rank: 1000
alias: relation
owner: CrossCorpusLink
domain_of:
- CrossCorpusLink
range: string
required: true

```
</details>