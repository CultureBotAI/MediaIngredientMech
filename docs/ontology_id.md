

# Slot: ontology_id 


_Ontology term ID in CURIE format (e.g., CHEBI:26710)_





URI: [mediaingredientmech:ontology_id](https://w3id.org/mediaingredientmech/ontology_id)
Alias: ontology_id

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [OntologyMapping](OntologyMapping.md) | Mapping to an ontology term (CHEBI, FOODON, etc |  no  |






## Properties

* Range: [String](String.md)

* Required: True

* Regex pattern: `^[A-Z]+:[0-9]+$`




## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/mediaingredientmech




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | mediaingredientmech:ontology_id |
| native | mediaingredientmech:ontology_id |




## LinkML Source

<details>
```yaml
name: ontology_id
description: Ontology term ID in CURIE format (e.g., CHEBI:26710)
from_schema: https://w3id.org/mediaingredientmech
rank: 1000
alias: ontology_id
owner: OntologyMapping
domain_of:
- OntologyMapping
range: string
required: true
pattern: ^[A-Z]+:[0-9]+$

```
</details>