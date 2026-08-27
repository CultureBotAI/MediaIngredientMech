

# Slot: culturemech_reference 


_Typed, stable link to a CultureMech recipe. Replaces the former `culturemech_medium_name`, which held a display string and no relationship semantics, so it could not distinguish the same formulation from a variant or a merely similar composition (#447). CultureMech remains authoritative for the recipe body and for recipe family/variant structure; this records only which recipe a record answers to and how._





URI: [mediaingredientmech:culturemech_reference](https://w3id.org/mediaingredientmech/culturemech_reference)
Alias: culturemech_reference

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [IngredientRecord](IngredientRecord.md) | Core record for a media ingredient with ontology mapping, synonyms, and curat... |  no  |






## Properties

* Range: [CultureMechReference](CultureMechReference.md)




## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/mediaingredientmech




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | mediaingredientmech:culturemech_reference |
| native | mediaingredientmech:culturemech_reference |




## LinkML Source

<details>
```yaml
name: culturemech_reference
description: Typed, stable link to a CultureMech recipe. Replaces the former `culturemech_medium_name`,
  which held a display string and no relationship semantics, so it could not distinguish
  the same formulation from a variant or a merely similar composition (#447). CultureMech
  remains authoritative for the recipe body and for recipe family/variant structure;
  this records only which recipe a record answers to and how.
from_schema: https://w3id.org/mediaingredientmech
rank: 1000
alias: culturemech_reference
owner: IngredientRecord
domain_of:
- IngredientRecord
range: CultureMechReference

```
</details>