

# Slot: identifier


_Semantic identifier for the record and its LinkML identifier slot, but not a guaranteed unique document address: reviewed duplicate families may share a CURIE. For mapped ingredients this is the primary ontology, registry, or local identity (e.g. `CHEBI:26710`, `cas:247167-54-0`, `kgmicrobe.compound:aburamycin_a`); for unmapped ingredients it is a generated `UNMAPPED_NNNN` placeholder. The nested `ontology_mapping.ontology_id` is a grounding target: it equals `identifier` when the identifier itself names the grounded ontology term, but registry or local identities may legitimately differ from the ontology target at any evidence-backed mapping quality._





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
description: 'Semantic identifier for the record and its LinkML identifier slot, but
  not a guaranteed unique document address: reviewed duplicate families may share
  a CURIE. For mapped ingredients this is the primary ontology, registry, or local
  identity (e.g. `CHEBI:26710`, `cas:247167-54-0`, `kgmicrobe.compound:aburamycin_a`);
  for unmapped ingredients it is a generated `UNMAPPED_NNNN` placeholder. The nested
  `ontology_mapping.ontology_id` is a grounding target: it equals `identifier` when
  the identifier itself names the grounded ontology term, but registry or local
  identities may legitimately differ from the ontology target at any evidence-backed
  mapping quality.'
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
