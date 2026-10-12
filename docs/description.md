

# Slot: description 



URI: [mediaingredientmech:description](https://w3id.org/mediaingredientmech/description)
Alias: description

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ProposedExperiment](ProposedExperiment.md) | A lightweight, domain-neutral sketch of an experiment or analysis that could ... |  no  |
| [CausalEdge](CausalEdge.md) | An evidence-backed directed relationship between two local node_ids |  no  |
| [CausalGraph](CausalGraph.md) | A directed, evidence-backed mechanism graph for one ingredient |  no  |
| [CausalNode](CausalNode.md) | A node in an ingredient mechanism graph |  no  |
| [Dataset](Dataset.md) | A reference to a publicly available dataset (omics, sequence, phenotype) rele... |  no  |






## Properties

* Range: [String](String.md)




## Identifier and Mapping Information







## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | mediaingredientmech:description |
| native | mediaingredientmech:description |




## LinkML Source

<details>
```yaml
name: description
alias: description
domain_of:
- CausalGraph
- CausalNode
- CausalEdge
- ProposedExperiment
- Dataset
range: string

```
</details>