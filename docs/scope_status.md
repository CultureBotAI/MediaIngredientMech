

# Slot: scope_status 


_Curator disposition. NONMECHANISTIC is a reviewed graph with no cellular mechanism in it (a SPECIATION graph, an indicator dye), explained in scope_notes; never a deferral. Proposed or incomplete graphs are REVIEW_NEEDED. MECHANISTIC only through the qc-causal-graphs scope gate._





URI: [mediaingredientmech:scope_status](https://w3id.org/mediaingredientmech/scope_status)
Alias: scope_status

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [CausalGraph](CausalGraph.md) | A directed, evidence-backed mechanism graph for one ingredient |  no  |






## Properties

* Range: [CausalGraphScopeEnum](CausalGraphScopeEnum.md)

* Required: True




## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/mediaingredientmech




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | mediaingredientmech:scope_status |
| native | mediaingredientmech:scope_status |




## LinkML Source

<details>
```yaml
name: scope_status
description: Curator disposition. NONMECHANISTIC is a reviewed graph with no cellular
  mechanism in it (a SPECIATION graph, an indicator dye), explained in scope_notes;
  never a deferral. Proposed or incomplete graphs are REVIEW_NEEDED. MECHANISTIC only
  through the qc-causal-graphs scope gate.
from_schema: https://w3id.org/mediaingredientmech
rank: 1000
alias: scope_status
owner: CausalGraph
domain_of:
- CausalGraph
range: CausalGraphScopeEnum
required: true

```
</details>