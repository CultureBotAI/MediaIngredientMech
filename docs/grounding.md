

# Slot: grounding 


_CURIE for the node; for a sibling-Mech record, that record's identifier, which is the only way a graph links out of the record. MIM: the local part admits `~` (five MIM identifiers use it); organism, strain, genome and protein-instance prefixes are refused (genome firewall)._





URI: [mediaingredientmech:grounding](https://w3id.org/mediaingredientmech/grounding)
Alias: grounding

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [CausalNode](CausalNode.md) | A node in an ingredient mechanism graph |  no  |






## Properties

* Range: [String](String.md)

* Regex pattern: `^(?!(?:UniProtKB|NCBITaxon|ncbi\.assembly|kgmicrobe\.strain|insdc|RefSeq|GenBank|ENA|biosample|bioproject|img\.taxon|patric|gtdb):)[A-Za-z][A-Za-z0-9._-]*:[A-Za-z0-9._~-]+$`




## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/mediaingredientmech




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | mediaingredientmech:grounding |
| native | mediaingredientmech:grounding |




## LinkML Source

<details>
```yaml
name: grounding
description: 'CURIE for the node; for a sibling-Mech record, that record''s identifier,
  which is the only way a graph links out of the record. MIM: the local part admits
  `~` (five MIM identifiers use it); organism, strain, genome and protein-instance
  prefixes are refused (genome firewall).'
from_schema: https://w3id.org/mediaingredientmech
rank: 1000
alias: grounding
owner: CausalNode
domain_of:
- CausalNode
range: string
pattern: ^(?!(?:UniProtKB|NCBITaxon|ncbi\.assembly|kgmicrobe\.strain|insdc|RefSeq|GenBank|ENA|biosample|bioproject|img\.taxon|patric|gtdb):)[A-Za-z][A-Za-z0-9._-]*:[A-Za-z0-9._~-]+$

```
</details>