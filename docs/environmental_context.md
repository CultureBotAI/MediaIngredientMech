

# Slot: environmental_context 


_Environmental contexts where this ingredient is relevant. Each entry pairs an ENVO term with a relevance qualifier explaining the association (natural source, selective agent, environment mimic, etc.). Enables cross-repository environment-driven queries with CommunityMech (`environment_term`) and CultureMech (`source_environment`). Optional; ubiquitous ingredients (water, glucose) typically have no entries._





URI: [mediaingredientmech:environmental_context](https://w3id.org/mediaingredientmech/environmental_context)
Alias: environmental_context

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [IngredientRecord](IngredientRecord.md) | Core record for a media ingredient with ontology mapping, synonyms, and curat... |  no  |






## Properties

* Range: [EnvironmentContext](EnvironmentContext.md)

* Multivalued: True




## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/mediaingredientmech




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | mediaingredientmech:environmental_context |
| native | mediaingredientmech:environmental_context |




## LinkML Source

<details>
```yaml
name: environmental_context
description: Environmental contexts where this ingredient is relevant. Each entry
  pairs an ENVO term with a relevance qualifier explaining the association (natural
  source, selective agent, environment mimic, etc.). Enables cross-repository environment-driven
  queries with CommunityMech (`environment_term`) and CultureMech (`source_environment`).
  Optional; ubiquitous ingredients (water, glucose) typically have no entries.
from_schema: https://w3id.org/mediaingredientmech
rank: 1000
alias: environmental_context
owner: IngredientRecord
domain_of:
- IngredientRecord
range: EnvironmentContext
bindings:
- obligation_level: REQUIRED
  binds_value_of: environment_term
required: false
multivalued: true
inlined: true
inlined_as_list: true

```
</details>