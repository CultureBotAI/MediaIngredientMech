

# Slot: organism_scope 


_The one NCBITaxon in which the biological edges hold (a TaxonMech record where one exists). Every organism-specific source the graph cites (protein_examples taxa, PathwayMech taxa) must lie on its lineage. Omit only for a taxon-agnostic graph; such a graph cannot be MECHANISTIC if it cites organism-specific evidence. Strains and genome assemblies are reached through TaxonMech, never copied here._





URI: [mediaingredientmech:organism_scope](https://w3id.org/mediaingredientmech/organism_scope)
Alias: organism_scope

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [CausalGraph](CausalGraph.md) | A directed, evidence-backed mechanism graph for one ingredient |  no  |






## Properties

* Range: [String](String.md)

* Regex pattern: `^NCBITaxon:[1-9][0-9]*$`




## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/mediaingredientmech




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | mediaingredientmech:organism_scope |
| native | mediaingredientmech:organism_scope |




## LinkML Source

<details>
```yaml
name: organism_scope
description: The one NCBITaxon in which the biological edges hold (a TaxonMech record
  where one exists). Every organism-specific source the graph cites (protein_examples
  taxa, PathwayMech taxa) must lie on its lineage. Omit only for a taxon-agnostic
  graph; such a graph cannot be MECHANISTIC if it cites organism-specific evidence.
  Strains and genome assemblies are reached through TaxonMech, never copied here.
from_schema: https://w3id.org/mediaingredientmech
rank: 1000
alias: organism_scope
owner: CausalGraph
domain_of:
- CausalGraph
range: string
pattern: ^NCBITaxon:[1-9][0-9]*$

```
</details>