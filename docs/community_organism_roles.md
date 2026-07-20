

# Slot: community_organism_roles 


_Role(s) this organism plays in a microbial community (e.g., PRIMARY_DEGRADER, SYNERGIST, COMPETITOR). Formerly `cellular_roles`; renamed to disambiguate from ingredient-level cellular metabolic roles._





URI: [mediaingredientmech:community_organism_roles](https://w3id.org/mediaingredientmech/community_organism_roles)
Alias: community_organism_roles

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [IngredientRecord](IngredientRecord.md) | Core record for a media ingredient with ontology mapping, synonyms, and curat... |  no  |






## Properties

* Range: [CommunityOrganismRoleAssignment](CommunityOrganismRoleAssignment.md)

* Multivalued: True




## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/mediaingredientmech




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | mediaingredientmech:community_organism_roles |
| native | mediaingredientmech:community_organism_roles |




## LinkML Source

<details>
```yaml
name: community_organism_roles
description: Role(s) this organism plays in a microbial community (e.g., PRIMARY_DEGRADER,
  SYNERGIST, COMPETITOR). Formerly `cellular_roles`; renamed to disambiguate from
  ingredient-level cellular metabolic roles.
from_schema: https://w3id.org/mediaingredientmech
rank: 1000
alias: community_organism_roles
owner: IngredientRecord
domain_of:
- IngredientRecord
range: CommunityOrganismRoleAssignment
multivalued: true
inlined: true
inlined_as_list: true

```
</details>