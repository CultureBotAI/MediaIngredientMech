

# Slot: kg_microbe_node_id 


_KG-Microbe node ID for this ingredient when found in the KG exactly. Populated when the ingredient's CHEBI identifier is present as a named node in the KG-Microbe mediadive graph (i.e., used as an ingredient in at least one KG-Microbe medium solution). Format: CHEBI:XXXXX_





URI: [mediaingredientmech:kg_microbe_node_id](https://w3id.org/mediaingredientmech/kg_microbe_node_id)
Alias: kg_microbe_node_id

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [IngredientRecord](IngredientRecord.md) | Core record for a media ingredient with ontology mapping, synonyms, and curat... |  no  |






## Properties

* Range: [String](String.md)

* Regex pattern: `^CHEBI:[0-9]+$`




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
description: 'KG-Microbe node ID for this ingredient when found in the KG exactly.
  Populated when the ingredient''s CHEBI identifier is present as a named node in
  the KG-Microbe mediadive graph (i.e., used as an ingredient in at least one KG-Microbe
  medium solution). Format: CHEBI:XXXXX'
from_schema: https://w3id.org/mediaingredientmech
rank: 1000
alias: kg_microbe_node_id
owner: IngredientRecord
domain_of:
- IngredientRecord
range: string
required: false
pattern: ^CHEBI:[0-9]+$

```
</details>