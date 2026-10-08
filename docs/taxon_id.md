

# Slot: taxon_id 



URI: [mediaingredientmech:taxon_id](https://w3id.org/mediaingredientmech/taxon_id)
Alias: taxon_id

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ProteinExample](ProteinExample.md) | A source-backed UniProt protein paired with the organism in which its role in... |  no  |






## Properties

* Range: [String](String.md)

* Required: True

* Regex pattern: `^NCBITaxon:[0-9]+$`




## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/mediaingredientmech




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | mediaingredientmech:taxon_id |
| native | mediaingredientmech:taxon_id |




## LinkML Source

<details>
```yaml
name: taxon_id
from_schema: https://w3id.org/mediaingredientmech
rank: 1000
alias: taxon_id
owner: ProteinExample
domain_of:
- ProteinExample
range: string
required: true
pattern: ^NCBITaxon:[0-9]+$

```
</details>