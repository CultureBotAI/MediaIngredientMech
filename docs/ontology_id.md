

# Slot: ontology_id 


_Ontology term ID in CURIE format. Most rows use a standard uppercase-prefix / numeric-local form (e.g. `CHEBI:26710`), but the schema also accepts the lowercase / alphanumeric / dotted prefixes used elsewhere in this project for non-ontology identifiers and kg-microbe registry rows (`cas:247167-54-0`, `mesh:C028805`, `NCIT:C76253`, `kgmicrobe.compound:aburamycin_a`). Local IDs may contain letters, digits, `.`, `_`, `-`, and `~`._





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

* Regex pattern: `^[A-Za-z][A-Za-z0-9.]*:[A-Za-z0-9][A-Za-z0-9._~-]*$`




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
description: Ontology term ID in CURIE format. Most rows use a standard uppercase-prefix
  / numeric-local form (e.g. `CHEBI:26710`), but the schema also accepts the lowercase
  / alphanumeric / dotted prefixes used elsewhere in this project for non-ontology
  identifiers and kg-microbe registry rows (`cas:247167-54-0`, `mesh:C028805`, `NCIT:C76253`,
  `kgmicrobe.compound:aburamycin_a`). Local IDs may contain letters, digits, `.`,
  `_`, `-`, and `~`.
from_schema: https://w3id.org/mediaingredientmech
rank: 1000
alias: ontology_id
owner: OntologyMapping
domain_of:
- OntologyMapping
range: string
required: true
pattern: ^[A-Za-z][A-Za-z0-9.]*:[A-Za-z0-9][A-Za-z0-9._~-]*$

```
</details>