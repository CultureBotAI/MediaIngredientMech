

# Slot: stoichiometry 


_ION_PART only. Ions released per formula unit; must equal the ChEBI SMILES component count._





URI: [mediaingredientmech:stoichiometry](https://w3id.org/mediaingredientmech/stoichiometry)
Alias: stoichiometry

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [CausalEdge](CausalEdge.md) | An evidence-backed directed relationship between two local node_ids |  no  |






## Properties

* Range: [Integer](Integer.md)

* Minimum Value: 1




## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/mediaingredientmech




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | mediaingredientmech:stoichiometry |
| native | mediaingredientmech:stoichiometry |




## LinkML Source

<details>
```yaml
name: stoichiometry
description: ION_PART only. Ions released per formula unit; must equal the ChEBI SMILES
  component count.
from_schema: https://w3id.org/mediaingredientmech
rank: 1000
alias: stoichiometry
owner: CausalEdge
domain_of:
- CausalEdge
range: integer
minimum_value: 1

```
</details>