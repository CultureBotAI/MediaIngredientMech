

# Slot: protein_examples 


_Organism-specific UniProtKB instances of a GENE_OR_PROTEIN node, or proteins that enable a MOLECULAR_FUNCTION node (MIM: TraitMech allows GENE_OR_PROTEIN only; ProteinTraitsMech attaches its examples to EC/RHEA records). Each names the taxon in which its role was established; that taxon resolves to a TaxonMech record._





URI: [mediaingredientmech:protein_examples](https://w3id.org/mediaingredientmech/protein_examples)
Alias: protein_examples

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [CausalNode](CausalNode.md) | A node in an ingredient mechanism graph |  no  |






## Properties

* Range: [ProteinExample](ProteinExample.md)

* Multivalued: True




## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/mediaingredientmech




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | mediaingredientmech:protein_examples |
| native | mediaingredientmech:protein_examples |




## LinkML Source

<details>
```yaml
name: protein_examples
description: 'Organism-specific UniProtKB instances of a GENE_OR_PROTEIN node, or
  proteins that enable a MOLECULAR_FUNCTION node (MIM: TraitMech allows GENE_OR_PROTEIN
  only; ProteinTraitsMech attaches its examples to EC/RHEA records). Each names the
  taxon in which its role was established; that taxon resolves to a TaxonMech record.'
from_schema: https://w3id.org/mediaingredientmech
rank: 1000
alias: protein_examples
owner: CausalNode
domain_of:
- CausalNode
range: ProteinExample
multivalued: true
inlined: true
inlined_as_list: true

```
</details>