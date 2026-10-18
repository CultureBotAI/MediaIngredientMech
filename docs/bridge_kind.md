

# Slot: bridge_kind 


_Set on chemistry edges only: what the supplied form becomes, or a protonation/tautomer step between species. Each kind fixes the allowed predicate_id and the bases that must verify (MAPPING_SEMANTICS.md section 7). Chemistry edges are taxon-independent._





URI: [mediaingredientmech:bridge_kind](https://w3id.org/mediaingredientmech/bridge_kind)
Alias: bridge_kind

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [CausalEdge](CausalEdge.md) | An evidence-backed directed relationship between two local node_ids |  no  |






## Properties

* Range: [BridgeKindEnum](BridgeKindEnum.md)




## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/mediaingredientmech




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | mediaingredientmech:bridge_kind |
| native | mediaingredientmech:bridge_kind |




## LinkML Source

<details>
```yaml
name: bridge_kind
description: 'Set on chemistry edges only: what the supplied form becomes, or a protonation/tautomer
  step between species. Each kind fixes the allowed predicate_id and the bases that
  must verify (MAPPING_SEMANTICS.md section 7). Chemistry edges are taxon-independent.'
from_schema: https://w3id.org/mediaingredientmech
rank: 1000
alias: bridge_kind
owner: CausalEdge
domain_of:
- CausalEdge
range: BridgeKindEnum

```
</details>