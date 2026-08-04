

# Slot: identifier 


_Primary key for the record. For mapped ingredients this is the ontology CURIE (e.g. `CHEBI:26710`, `FOODON:3311109`, `cas:247167-54-0`, `kgmicrobe.compound:aburamycin_a`); for unmapped ingredients it is a generated `UNMAPPED_NNNN` placeholder. The nested `ontology_mapping.ontology_id` carries the same value for mapped records (and is absent for unmapped records)._





URI: [mediaingredientmech:identifier](https://w3id.org/mediaingredientmech/identifier)
Alias: identifier

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [IngredientRecord](IngredientRecord.md) | Core record for a media ingredient with ontology mapping, synonyms, and curat... |  no  |






## Properties

* Range: [String](String.md)

* Required: True




## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/mediaingredientmech




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | mediaingredientmech:identifier |
| native | mediaingredientmech:identifier |




## LinkML Source

<details>
```yaml
name: identifier
description: Primary key for the record. For mapped ingredients this is the ontology
  CURIE (e.g. `CHEBI:26710`, `FOODON:3311109`, `cas:247167-54-0`, `kgmicrobe.compound:aburamycin_a`);
  for unmapped ingredients it is a generated `UNMAPPED_NNNN` placeholder. The nested
  `ontology_mapping.ontology_id` carries the same value for mapped records (and is
  absent for unmapped records).
from_schema: https://w3id.org/mediaingredientmech
rank: 1000
identifier: true
alias: identifier
owner: IngredientRecord
domain_of:
- IngredientRecord
range: string
required: true

```
</details>