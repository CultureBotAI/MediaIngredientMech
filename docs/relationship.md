

# Slot: relationship 


_How this record relates to that recipe. Required because an untyped link cannot distinguish the claims it might be making, which is the defect that motivated this class._





URI: [mediaingredientmech:relationship](https://w3id.org/mediaingredientmech/relationship)
Alias: relationship

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [CultureMechReference](CultureMechReference.md) | A verified link from a MIM record to a CultureMech recipe, carried by stable ... |  no  |






## Properties

* Range: [CultureMechRelationshipEnum](CultureMechRelationshipEnum.md)

* Required: True




## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/mediaingredientmech




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | mediaingredientmech:relationship |
| native | mediaingredientmech:relationship |




## LinkML Source

<details>
```yaml
name: relationship
description: How this record relates to that recipe. Required because an untyped link
  cannot distinguish the claims it might be making, which is the defect that motivated
  this class.
from_schema: https://w3id.org/mediaingredientmech
rank: 1000
alias: relationship
owner: CultureMechReference
domain_of:
- CultureMechReference
range: CultureMechRelationshipEnum
required: true

```
</details>