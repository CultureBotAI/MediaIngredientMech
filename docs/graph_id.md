

# Slot: graph_id 



URI: [mediaingredientmech:graph_id](https://w3id.org/mediaingredientmech/graph_id)
Alias: graph_id

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [CausalGraph](CausalGraph.md) | A directed, evidence-backed mechanism graph for one ingredient |  no  |






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
| self | mediaingredientmech:graph_id |
| native | mediaingredientmech:graph_id |




## LinkML Source

<details>
```yaml
name: graph_id
from_schema: https://w3id.org/mediaingredientmech
rank: 1000
identifier: true
alias: graph_id
owner: CausalGraph
domain_of:
- CausalGraph
range: string
required: true
pattern: ^[a-z][a-z0-9_]*$

```
</details>