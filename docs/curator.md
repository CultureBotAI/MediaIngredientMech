

# Slot: curator 


_Who performed this action (username or system)_





URI: [mediaingredientmech:curator](https://w3id.org/mediaingredientmech/curator)
Alias: curator

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [CurationEvent](CurationEvent.md) | Audit trail entry for a curation action |  no  |






## Properties

* Range: [xsd:string](http://www.w3.org/2001/XMLSchema#string)

* Required: True




## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/mediaingredientmech




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | mediaingredientmech:curator |
| native | mediaingredientmech:curator |




## LinkML Source

<details>
```yaml
name: curator
description: Who performed this action (username or system)
from_schema: https://w3id.org/mediaingredientmech
rank: 1000
alias: curator
owner: CurationEvent
domain_of:
- CurationEvent
range: string
required: true

```
</details>