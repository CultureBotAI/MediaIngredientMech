# Enum: OntologySourceEnum 



URI: [mediaingredientmech:OntologySourceEnum](https://w3id.org/mediaingredientmech/OntologySourceEnum)

## Permissible Values

| Value | Meaning | Description |
| --- | --- | --- |
| CHEBI | None | Chemical Entities of Biological Interest |
| FOODON | None | Food Ontology |
| NCIT | None | NCI Thesaurus |
| MESH | None | Medical Subject Headings |
| UBERON | None | Uber Anatomy Ontology |
| ENVO | None | Environment Ontology |
| MICRO | None | Microbiology vocabulary |
| BTO | None | BRENDA Tissue Ontology |
| CAS | None | CAS Registry — fallback identity when the ingredient has a CAS number but no ... |
| registry | None | Generic registry-row fallback used when an identity exists in a non-ontology ... |
| kgmicrobe.compound | None | kg-microbe compound registry row (placeholder identity awaiting upgrade to a ... |
| kgmicrobe.ingredient | None | kg-microbe ingredient registry row (placeholder identity awaiting upgrade to ... |




## Slots

| Name | Description |
| ---  | --- |
| [ontology_source](ontology_source.md) | Source ontology |





## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/mediaingredientmech






## LinkML Source

<details>
```yaml
name: OntologySourceEnum
from_schema: https://w3id.org/mediaingredientmech
rank: 1000
permissible_values:
  CHEBI:
    text: CHEBI
    description: Chemical Entities of Biological Interest
  FOODON:
    text: FOODON
    description: Food Ontology
  NCIT:
    text: NCIT
    description: NCI Thesaurus
  MESH:
    text: MESH
    description: Medical Subject Headings
  UBERON:
    text: UBERON
    description: Uber Anatomy Ontology
  ENVO:
    text: ENVO
    description: Environment Ontology
  MICRO:
    text: MICRO
    description: Microbiology vocabulary
  BTO:
    text: BTO
    description: BRENDA Tissue Ontology
  CAS:
    text: CAS
    description: CAS Registry — fallback identity when the ingredient has a CAS number
      but no resolved ontology term (paired with `cas:` prefix CURIEs).
  registry:
    text: registry
    description: Generic registry-row fallback used when an identity exists in a non-ontology
      registry tracked by the SSSOM pipeline.
  kgmicrobe.compound:
    text: kgmicrobe.compound
    description: kg-microbe compound registry row (placeholder identity awaiting upgrade
      to a CHEBI/MESH/etc. term).
  kgmicrobe.ingredient:
    text: kgmicrobe.ingredient
    description: kg-microbe ingredient registry row (placeholder identity awaiting
      upgrade to an ontology term).

```
</details>