

# Slot: explains 


_Role assignments on this record that the graph explains, as `<facet>#<ROLE>` hash anchors (mech_shared attaches_to convention), e.g. `nutritional_roles#SULFUR_SOURCE`. Each must name a role present on the record. A pointer only: a role never creates an edge and an edge never creates a role._





URI: [mediaingredientmech:explains](https://w3id.org/mediaingredientmech/explains)
Alias: explains

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [CausalGraph](CausalGraph.md) | A directed, evidence-backed mechanism graph for one ingredient |  no  |






## Properties

* Range: [String](String.md)

* Multivalued: True

* Regex pattern: `^(nutritional_roles|physicochemical_roles|cellular_metabolic_roles)#[A-Z][A-Z0-9_]*$`




## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/mediaingredientmech




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | mediaingredientmech:explains |
| native | mediaingredientmech:explains |




## LinkML Source

<details>
```yaml
name: explains
description: 'Role assignments on this record that the graph explains, as `<facet>#<ROLE>`
  hash anchors (mech_shared attaches_to convention), e.g. `nutritional_roles#SULFUR_SOURCE`.
  Each must name a role present on the record. A pointer only: a role never creates
  an edge and an edge never creates a role.'
from_schema: https://w3id.org/mediaingredientmech
rank: 1000
alias: explains
owner: CausalGraph
domain_of:
- CausalGraph
range: string
multivalued: true
pattern: ^(nutritional_roles|physicochemical_roles|cellular_metabolic_roles)#[A-Z][A-Z0-9_]*$

```
</details>