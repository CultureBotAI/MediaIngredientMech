# Enum: CausalNodeTypeEnum 




_TraitMech's vocabulary, CellStructureMech's STRUCTURE, and MIM's anchor INGREDIENT. No TAXON: organisms are organism_scope and protein_examples taxa._



URI: [mediaingredientmech:CausalNodeTypeEnum](https://w3id.org/mediaingredientmech/CausalNodeTypeEnum)

## Permissible Values

| Value | Meaning | Description |
| --- | --- | --- |
| INGREDIENT | None | This record as supplied; exactly one per graph; grounding equals the record i... |
| CHEMICAL | None | Any other chemical entity (active species, metabolite, cofactor form, another... |
| GENE_OR_PROTEIN | None | A taxon-agnostic protein family, function-defined protein or complex |
| MOLECULAR_FUNCTION | None | An activity or reaction: EC, RHEA, GO molecular function, and ProteinTraitsMe... |
| BIOLOGICAL_PROCESS | None | A biological process (GO BP), including ProteinTraitsMech FUNC_PATHWAY record... |
| PATHWAY | None | A PathwayMech record |
| STRUCTURE | None | A CellStructureMech record or GO cellular component |
| CELLULAR_LOCALIZATION | None | A location with no CellStructureMech record |
| ORGANELLE | None | A cellular organelle or microbial subcellular structure |
| TRAIT | None | A TraitMech class record (never an OBJECT_PROPERTY record such as METPO:20000... |
| QUALITY | None | An attribute, including a ProteinTraitsMech requirement trait (COFACTOR_REQ_*... |
| CAPACITY | None | A metabolic or functional capacity, such as reducing power or energy charge, ... |
| STATE | None | A bioenergetic or molecular state of the cell (e |
| RNA | None | A functional RNA molecule or RNA-containing causal entity |
| GENETIC_ELEMENT | None | A non-protein mobile or chromosomal genetic element such as a plasmid or prop... |
| ENVIRONMENTAL_FACTOR | None | An environmental exposure or condition |
| EXPERIMENTAL_FACTOR | None | An assay, perturbation, or experimental condition |




## Slots

| Name | Description |
| ---  | --- |
| [node_type](node_type.md) |  |





## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/mediaingredientmech






## LinkML Source

<details>
```yaml
name: CausalNodeTypeEnum
description: 'TraitMech''s vocabulary, CellStructureMech''s STRUCTURE, and MIM''s
  anchor INGREDIENT. No TAXON: organisms are organism_scope and protein_examples taxa.'
from_schema: https://w3id.org/mediaingredientmech
rank: 1000
permissible_values:
  INGREDIENT:
    text: INGREDIENT
    description: This record as supplied; exactly one per graph; grounding equals
      the record identifier.
  CHEMICAL:
    text: CHEMICAL
    description: Any other chemical entity (active species, metabolite, cofactor form,
      another MIM record).
  GENE_OR_PROTEIN:
    text: GENE_OR_PROTEIN
    description: A taxon-agnostic protein family, function-defined protein or complex.
  MOLECULAR_FUNCTION:
    text: MOLECULAR_FUNCTION
    description: 'An activity or reaction: EC, RHEA, GO molecular function, and ProteinTraitsMech
      FUNC_TRANSPORT records (TCDB families as transport functions).'
  BIOLOGICAL_PROCESS:
    text: BIOLOGICAL_PROCESS
    description: A biological process (GO BP), including ProteinTraitsMech FUNC_PATHWAY
      records.
  PATHWAY:
    text: PATHWAY
    description: A PathwayMech record.
  STRUCTURE:
    text: STRUCTURE
    description: A CellStructureMech record or GO cellular component.
  CELLULAR_LOCALIZATION:
    text: CELLULAR_LOCALIZATION
    description: A location with no CellStructureMech record.
  ORGANELLE:
    text: ORGANELLE
    description: A cellular organelle or microbial subcellular structure.
  TRAIT:
    text: TRAIT
    description: A TraitMech class record (never an OBJECT_PROPERTY record such as
      METPO:2000020).
  QUALITY:
    text: QUALITY
    description: An attribute, including a ProteinTraitsMech requirement trait (COFACTOR_REQ_*).
  CAPACITY:
    text: CAPACITY
    description: A metabolic or functional capacity, such as reducing power or energy
      charge, that is neither a single chemical species nor a process.
  STATE:
    text: STATE
    description: A bioenergetic or molecular state of the cell (e.g. proton motive
      force), as distinct from the process that establishes it.
  RNA:
    text: RNA
    description: A functional RNA molecule or RNA-containing causal entity.
  GENETIC_ELEMENT:
    text: GENETIC_ELEMENT
    description: A non-protein mobile or chromosomal genetic element such as a plasmid
      or prophage.
  ENVIRONMENTAL_FACTOR:
    text: ENVIRONMENTAL_FACTOR
    description: An environmental exposure or condition.
  EXPERIMENTAL_FACTOR:
    text: EXPERIMENTAL_FACTOR
    description: An assay, perturbation, or experimental condition.

```
</details>