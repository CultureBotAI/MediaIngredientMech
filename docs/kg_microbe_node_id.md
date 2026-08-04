

# Slot: kg_microbe_node_id 


_KG-Microbe node ID for this ingredient when found in the KG exactly. Populated when the ingredient is present as a named node in the KG-Microbe mediadive graph (i.e. used as an ingredient in at least one KG-Microbe medium solution). The node ID is a CURIE using whichever scheme the KG-Microbe graph stores the entity under — most often `CHEBI:`, but also `mesh:`, `NCIT:`, `FOODON:`, `ENVO:`, or one of the kg-microbe registry prefixes (`kgmicrobe.compound:`, `kgmicrobe.ingredient:`)._





URI: [mediaingredientmech:kg_microbe_node_id](https://w3id.org/mediaingredientmech/kg_microbe_node_id)
Alias: kg_microbe_node_id

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [IngredientRecord](IngredientRecord.md) | Core record for a media ingredient with ontology mapping, synonyms, and curat... |  no  |






## Properties

* Range: [String](String.md)

* Regex pattern: `^[A-Za-z][A-Za-z0-9.]*:[A-Za-z0-9][A-Za-z0-9._~-]*$`




## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/mediaingredientmech




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | mediaingredientmech:kg_microbe_node_id |
| native | mediaingredientmech:kg_microbe_node_id |




## LinkML Source

<details>
```yaml
name: kg_microbe_node_id
description: KG-Microbe node ID for this ingredient when found in the KG exactly.
  Populated when the ingredient is present as a named node in the KG-Microbe mediadive
  graph (i.e. used as an ingredient in at least one KG-Microbe medium solution). The
  node ID is a CURIE using whichever scheme the KG-Microbe graph stores the entity
  under — most often `CHEBI:`, but also `mesh:`, `NCIT:`, `FOODON:`, `ENVO:`, or one
  of the kg-microbe registry prefixes (`kgmicrobe.compound:`, `kgmicrobe.ingredient:`).
from_schema: https://w3id.org/mediaingredientmech
rank: 1000
alias: kg_microbe_node_id
owner: IngredientRecord
domain_of:
- IngredientRecord
range: string
required: false
pattern: ^[A-Za-z][A-Za-z0-9.]*:[A-Za-z0-9][A-Za-z0-9._~-]*$

```
</details>