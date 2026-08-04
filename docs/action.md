

# Slot: action 


_Type of curation action. Free-form SCREAMING_SNAKE_CASE label minted by the curation tool that produced this event. CurationActionEnum below documents well-known actions; new tools are free to introduce new labels (live data has 110+ distinct values)._





URI: [mediaingredientmech:action](https://w3id.org/mediaingredientmech/action)
Alias: action

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [CurationEvent](CurationEvent.md) | Audit trail entry for a curation action |  no  |






## Properties

* Range: [String](String.md)

* Required: True

* Regex pattern: `^[A-Z][A-Z0-9]*(_[A-Z0-9]+)*$`




## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/mediaingredientmech




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | mediaingredientmech:action |
| native | mediaingredientmech:action |




## LinkML Source

<details>
```yaml
name: action
description: Type of curation action. Free-form SCREAMING_SNAKE_CASE label minted
  by the curation tool that produced this event. CurationActionEnum below documents
  well-known actions; new tools are free to introduce new labels (live data has 110+
  distinct values).
from_schema: https://w3id.org/mediaingredientmech
rank: 1000
alias: action
owner: CurationEvent
domain_of:
- CurationEvent
range: string
required: true
pattern: ^[A-Z][A-Z0-9]*(_[A-Z0-9]+)*$

```
</details>