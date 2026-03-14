

# Slot: doi 


_Digital Object Identifier (e.g., 10.1128/jb.00123-15)_





URI: [mediaingredientmech:doi](https://w3id.org/mediaingredientmech/doi)
Alias: doi

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [RoleCitation](RoleCitation.md) | Citation supporting a role assignment (DOI, publication, database reference) |  no  |






## Properties

* Range: [xsd:string](http://www.w3.org/2001/XMLSchema#string)

* Regex pattern: `^10\.\d{4,}/[-._;()/:A-Za-z0-9]+$`




## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/mediaingredientmech




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | mediaingredientmech:doi |
| native | mediaingredientmech:doi |




## LinkML Source

<details>
```yaml
name: doi
description: Digital Object Identifier (e.g., 10.1128/jb.00123-15)
from_schema: https://w3id.org/mediaingredientmech
rank: 1000
alias: doi
owner: RoleCitation
domain_of:
- RoleCitation
range: string
pattern: ^10\.\d{4,}/[-._;()/:A-Za-z0-9]+$

```
</details>