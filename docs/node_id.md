

# Slot: node_id 



URI: [mediaingredientmech:node_id](https://w3id.org/mediaingredientmech/node_id)
Alias: node_id

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [CausalNode](CausalNode.md) | A node in an ingredient mechanism graph |  no  |






## Properties

* Range: [String](String.md)

* Required: True

* Regex pattern: `^[a-z][a-z0-9_]*$`




## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/mediaingredientmech




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | mediaingredientmech:node_id |
| native | mediaingredientmech:node_id |




## LinkML Source

<details>
```yaml
name: node_id
from_schema: https://w3id.org/mediaingredientmech
rank: 1000
identifier: true
alias: node_id
owner: CausalNode
domain_of:
- CausalNode
range: string
required: true
pattern: ^[a-z][a-z0-9_]*$

```
</details>