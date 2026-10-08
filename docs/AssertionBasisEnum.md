# Enum: AssertionBasisEnum 




_The offline check an edge claims (all run in CI on committed files)._



URI: [mediaingredientmech:AssertionBasisEnum](https://w3id.org/mediaingredientmech/AssertionBasisEnum)

## Permissible Values

| Value | Meaning | Description |
| --- | --- | --- |
| LITERATURE | None | PMID/doi evidence with a verbatim snippet found in references_cache (qc-evide... |
| ONTOLOGY_AXIOM | None | The triple (or a declared sub-property of it) is asserted or entailed in mapp... |
| CHEMICAL_STRUCTURE | None | Recomputed from ChEBI SMILES, formula, charge and InChIKey rows in mappings/o... |
| SIBLING_RECORD | None | The pinned sibling record states the relation for exactly this grounding (map... |
| DATABASE_RECORD | None | A cached database entry (references_cache/UniProtKB_<acc> |
| RECORD_COMPONENT | None | Restates this record's components entry; inherits its component_assertion |
| RECORD_SSSOM | None | Restates this record's own SSSOM row |




## Slots

| Name | Description |
| ---  | --- |
| [assertion_basis](assertion_basis.md) | The offline checks this edge claims; qc-causal-graphs confirms each one |





## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/mediaingredientmech






## LinkML Source

<details>
```yaml
name: AssertionBasisEnum
description: The offline check an edge claims (all run in CI on committed files).
from_schema: https://w3id.org/mediaingredientmech
rank: 1000
permissible_values:
  LITERATURE:
    text: LITERATURE
    description: PMID/doi evidence with a verbatim snippet found in references_cache
      (qc-evidence normalisation).
  ONTOLOGY_AXIOM:
    text: ONTOLOGY_AXIOM
    description: The triple (or a declared sub-property of it) is asserted or entailed
      in mappings/ontology_facts.tsv.
  CHEMICAL_STRUCTURE:
    text: CHEMICAL_STRUCTURE
    description: Recomputed from ChEBI SMILES, formula, charge and InChIKey rows in
      mappings/ontology_facts.tsv.
  SIBLING_RECORD:
    text: SIBLING_RECORD
    description: The pinned sibling record states the relation for exactly this grounding
      (mappings/cross_mech_assertions.jsonl; table in MAPPING_SEMANTICS.md section
      7).
  DATABASE_RECORD:
    text: DATABASE_RECORD
    description: A cached database entry (references_cache/UniProtKB_<acc>.json, Rhea
      directional id) states it.
  RECORD_COMPONENT:
    text: RECORD_COMPONENT
    description: Restates this record's components entry; inherits its component_assertion.
  RECORD_SSSOM:
    text: RECORD_SSSOM
    description: Restates this record's own SSSOM row.

```
</details>