

# Slot: curation_history 


_Audit trail of all curation actions_





URI: [mediaingredientmech:curation_history](https://w3id.org/mediaingredientmech/curation_history)
Alias: curation_history

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [IngredientRecord](IngredientRecord.md) | Core record for a media ingredient with ontology mapping, synonyms, and curat... |  no  |






## Properties

* Range: [CurationEvent](CurationEvent.md)

* Multivalued: True




## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/mediaingredientmech




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | mediaingredientmech:curation_history |
| native | mediaingredientmech:curation_history |




## LinkML Source

<details>
```yaml
name: curation_history
description: Audit trail of all curation actions
from_schema: https://w3id.org/mediaingredientmech
rank: 1000
alias: curation_history
owner: IngredientRecord
domain_of:
- IngredientRecord
range: CurationEvent
multivalued: true
inlined: true
inlined_as_list: true

```
</details>