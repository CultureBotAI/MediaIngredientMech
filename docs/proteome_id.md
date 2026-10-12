

# Slot: proteome_id 



URI: [mediaingredientmech:proteome_id](https://w3id.org/mediaingredientmech/proteome_id)
Alias: proteome_id

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ProteinExample](ProteinExample.md) | A source-backed UniProt protein paired with the organism in which its role in... |  no  |






## Properties

* Range: [String](String.md)

* Regex pattern: `^UP[0-9]{9}$`




## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/mediaingredientmech




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | mediaingredientmech:proteome_id |
| native | mediaingredientmech:proteome_id |




## LinkML Source

<details>
```yaml
name: proteome_id
from_schema: https://w3id.org/mediaingredientmech
rank: 1000
alias: proteome_id
owner: ProteinExample
domain_of:
- ProteinExample
range: string
pattern: ^UP[0-9]{9}$

```
</details>