# Enum: CausalGraphScopeEnum 




_Fleet scope disposition (TraitMech, CellStructureMech values)._



URI: [mediaingredientmech:CausalGraphScopeEnum](https://w3id.org/mediaingredientmech/CausalGraphScopeEnum)

## Permissible Values

| Value | Meaning | Description |
| --- | --- | --- |
| MECHANISTIC | None | A source-backed biological mechanism that passed the qc-causal-graphs scope g... |
| NONMECHANISTIC | None | Reviewed; no cellular mechanism to model (e |
| REVIEW_NEEDED | None | Proposed or incomplete; awaits an explicit scope decision |




## Slots

| Name | Description |
| ---  | --- |
| [scope_status](scope_status.md) | Curator disposition |





## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/mediaingredientmech






## LinkML Source

<details>
```yaml
name: CausalGraphScopeEnum
description: Fleet scope disposition (TraitMech, CellStructureMech values).
from_schema: https://w3id.org/mediaingredientmech
rank: 1000
permissible_values:
  MECHANISTIC:
    text: MECHANISTIC
    description: A source-backed biological mechanism that passed the qc-causal-graphs
      scope gate.
  NONMECHANISTIC:
    text: NONMECHANISTIC
    description: Reviewed; no cellular mechanism to model (e.g. SPECIATION). Explained
      in scope_notes.
  REVIEW_NEEDED:
    text: REVIEW_NEEDED
    description: Proposed or incomplete; awaits an explicit scope decision.

```
</details>