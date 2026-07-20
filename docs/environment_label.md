

# Slot: environment_label 


_Canonical ENVO label for environment_term. Verified against the ontology by the id↔label gate; the free/relevance name lives in notes._





URI: [rdfs:label](http://www.w3.org/2000/01/rdf-schema#label)
Alias: environment_label

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [EnvironmentContext](EnvironmentContext.md) | Environmental context annotation for an ingredient |  no  |






## Properties

* Range: [String](String.md)




## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/mediaingredientmech




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | rdfs:label |
| native | mediaingredientmech:environment_label |




## LinkML Source

<details>
```yaml
name: environment_label
description: Canonical ENVO label for environment_term. Verified against the ontology
  by the id↔label gate; the free/relevance name lives in notes.
from_schema: https://w3id.org/mediaingredientmech
rank: 1000
slot_uri: rdfs:label
alias: environment_label
owner: EnvironmentContext
domain_of:
- EnvironmentContext
range: string
required: false

```
</details>