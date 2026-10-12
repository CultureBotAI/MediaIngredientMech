

# Slot: uniprot_id 



URI: [mediaingredientmech:uniprot_id](https://w3id.org/mediaingredientmech/uniprot_id)
Alias: uniprot_id

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ProteinExample](ProteinExample.md) | A source-backed UniProt protein paired with the organism in which its role in... |  no  |






## Properties

* Range: [String](String.md)

* Required: True

* Regex pattern: `^UniProtKB:(?:[OPQ][0-9][A-Z0-9]{3}[0-9]|[A-NR-Z][0-9](?:[A-Z][A-Z0-9]{2}[0-9]){1,2})$`




## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/mediaingredientmech




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | mediaingredientmech:uniprot_id |
| native | mediaingredientmech:uniprot_id |




## LinkML Source

<details>
```yaml
name: uniprot_id
from_schema: https://w3id.org/mediaingredientmech
rank: 1000
alias: uniprot_id
owner: ProteinExample
domain_of:
- ProteinExample
range: string
required: true
pattern: ^UniProtKB:(?:[OPQ][0-9][A-Z0-9]{3}[0-9]|[A-NR-Z][0-9](?:[A-Z][A-Z0-9]{2}[0-9]){1,2})$

```
</details>