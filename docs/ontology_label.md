

# Slot: ontology_label 


_Canonical OBO label for ontology_id (e.g. "sodium chloride" for CHEBI:26710). The id↔label gate verifies this equals the ontology's canonical label; abbreviations/formulas/free names (e.g. "NaCl") belong in preferred_term / synonyms, not here._





URI: [rdfs:label](http://www.w3.org/2000/01/rdf-schema#label)
Alias: ontology_label

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [OntologyMapping](OntologyMapping.md) | Mapping to an ontology term (CHEBI, FOODON, etc |  no  |






## Properties

### Type and Range

| Property | Value |
| --- | --- |
| Range | [String](String.md) |
| Domain Of | [OntologyMapping](OntologyMapping.md) |
| Slot URI | [rdfs:label](http://www.w3.org/2000/01/rdf-schema#label) |

### Cardinality and Requirements

| Property | Value |
| --- | --- |
| Required | Yes |
### Slot Characteristics

| Property | Value |
| --- | --- |
| Owner | [OntologyMapping](OntologyMapping.md) |












## Identifier and Mapping Information





### Schema Source


* from schema: https://w3id.org/mediaingredientmech




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | rdfs:label |
| native | mediaingredientmech:ontology_label |




## LinkML Source

<details>
```yaml
name: ontology_label
description: Canonical OBO label for ontology_id (e.g. "sodium chloride" for CHEBI:26710).
  The id↔label gate verifies this equals the ontology's canonical label; abbreviations/formulas/free
  names (e.g. "NaCl") belong in preferred_term / synonyms, not here.
from_schema: https://w3id.org/mediaingredientmech
rank: 1000
slot_uri: rdfs:label
alias: ontology_label
owner: OntologyMapping
domain_of:
- OntologyMapping
range: string
required: true

```
</details>