

# Slot: cas_rn 


_Chemical Abstracts Service Registry Number (CAS-RN) in format XXX-XX-X or XXXX-XX-X. Primary chemical identifier used in regulatory and commercial contexts. Retrieved from CultureBotHT/MicroMediaParam mappings or external databases._





URI: [mediaingredientmech:cas_rn](https://w3id.org/mediaingredientmech/cas_rn)
Alias: cas_rn

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ChemicalProperties](ChemicalProperties.md) | Chemical structure and properties for CHEBI-mapped ingredients |  no  |






## Properties

* Range: [String](String.md)

* Regex pattern: `^\d+-\d+-\d+$`




## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/mediaingredientmech




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | mediaingredientmech:cas_rn |
| native | mediaingredientmech:cas_rn |




## LinkML Source

<details>
```yaml
name: cas_rn
description: Chemical Abstracts Service Registry Number (CAS-RN) in format XXX-XX-X
  or XXXX-XX-X. Primary chemical identifier used in regulatory and commercial contexts.
  Retrieved from CultureBotHT/MicroMediaParam mappings or external databases.
from_schema: https://w3id.org/mediaingredientmech
rank: 1000
alias: cas_rn
owner: ChemicalProperties
domain_of:
- ChemicalProperties
range: string
pattern: ^\d+-\d+-\d+$

```
</details>