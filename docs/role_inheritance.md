

# Slot: role_inheritance 


_If true, inherits the three role facets (nutritional_roles, physicochemical_roles, cellular_metabolic_roles) from the parent ingredient. Allows child variants to automatically get parent's roles while enabling variant-specific role overrides or restrictions._





URI: [mediaingredientmech:role_inheritance](https://w3id.org/mediaingredientmech/role_inheritance)
Alias: role_inheritance

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [IngredientRecord](IngredientRecord.md) | Core record for a media ingredient with ontology mapping, synonyms, and curat... |  no  |






## Properties

* Range: [Boolean](Boolean.md)




## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/mediaingredientmech




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | mediaingredientmech:role_inheritance |
| native | mediaingredientmech:role_inheritance |




## LinkML Source

<details>
```yaml
name: role_inheritance
description: If true, inherits the three role facets (nutritional_roles, physicochemical_roles,
  cellular_metabolic_roles) from the parent ingredient. Allows child variants to automatically
  get parent's roles while enabling variant-specific role overrides or restrictions.
from_schema: https://w3id.org/mediaingredientmech
rank: 1000
alias: role_inheritance
owner: IngredientRecord
domain_of:
- IngredientRecord
range: boolean

```
</details>