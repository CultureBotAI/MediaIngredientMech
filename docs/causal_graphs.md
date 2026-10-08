

# Slot: causal_graphs 


_Evidence-backed mechanism graphs explaining how this ingredient, as supplied, acts on cultured microbes. Fleet graph_list shape (TraitMech, CellStructureMech), so kg-microbe-graph coverage and structure audits read it with default field names. Each graph has exactly one INGREDIENT node grounded to this record's identifier; every other chemical the cell meets is a separate CHEMICAL node reached through typed chemistry edges (CausalEdge.bridge_kind). A graph links to another record, in MIM or a sibling Mech, only through a node grounding equal to that record's identifier. Graphs never change identifier, ontology_mapping or components and never produce SSSOM rows (MAPPING_SEMANTICS.md section 7). This schema validates structure only; the planned offline semantic gate must verify anchors, bridges, evidence and scope before record curation._





URI: [mediaingredientmech:causal_graphs](https://w3id.org/mediaingredientmech/causal_graphs)
Alias: causal_graphs

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [IngredientRecord](IngredientRecord.md) | Core record for a media ingredient with ontology mapping, synonyms, and curat... |  no  |






## Properties

* Range: [CausalGraph](CausalGraph.md)

* Multivalued: True




## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/mediaingredientmech




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | mediaingredientmech:causal_graphs |
| native | mediaingredientmech:causal_graphs |




## LinkML Source

<details>
```yaml
name: causal_graphs
description: Evidence-backed mechanism graphs explaining how this ingredient, as supplied,
  acts on cultured microbes. Fleet graph_list shape (TraitMech, CellStructureMech),
  so kg-microbe-graph coverage and structure audits read it with default field names.
  Each graph has exactly one INGREDIENT node grounded to this record's identifier;
  every other chemical the cell meets is a separate CHEMICAL node reached through
  typed chemistry edges (CausalEdge.bridge_kind). A graph links to another record,
  in MIM or a sibling Mech, only through a node grounding equal to that record's identifier.
  Graphs never change identifier, ontology_mapping or components and never produce
  SSSOM rows (MAPPING_SEMANTICS.md section 7). This schema validates structure only;
  the planned offline semantic gate must verify anchors, bridges, evidence and scope
  before record curation.
from_schema: https://w3id.org/mediaingredientmech
rank: 1000
alias: causal_graphs
owner: IngredientRecord
domain_of:
- IngredientRecord
range: CausalGraph
multivalued: true
inlined: true
inlined_as_list: true

```
</details>