# Enum: IngredientGraphKindEnum 




_What a graph explains. `typical_roles` lists the role anchors a kind usually explains; qc-causal-graphs warns on an unusual pairing, never rejects it._



URI: [mediaingredientmech:IngredientGraphKindEnum](https://w3id.org/mediaingredientmech/IngredientGraphKindEnum)

## Permissible Values

| Value | Meaning | Description |
| --- | --- | --- |
| ASSIMILATION | None | The active species is taken up and incorporated into biomass or a cellular po... |
| ENERGY_CONSERVATION | None | The species is an electron donor, terminal electron acceptor or energy substr... |
| COFACTOR_FUNCTION | None | The species is, or is converted into, a cofactor or prosthetic group an enzym... |
| REGULATION | None | The species changes gene expression or protein activity without being consume... |
| INHIBITION | None | The species inhibits a target or growth |
| STRESS_PROTECTION | None | The species protects cells against a stress |
| MEDIUM_CONDITIONING | None | The ingredient changes a medium property (pH, redox, osmolarity, metal availa... |
| SPECIATION | None | Chemistry only: what the supplied form becomes (bridge and COMPONENT edges), ... |




## Slots

| Name | Description |
| ---  | --- |
| [graph_kind](graph_kind.md) | What the graph explains (claw graph_facets value) |





## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/mediaingredientmech






## LinkML Source

<details>
```yaml
name: IngredientGraphKindEnum
description: What a graph explains. `typical_roles` lists the role anchors a kind
  usually explains; qc-causal-graphs warns on an unusual pairing, never rejects it.
from_schema: https://w3id.org/mediaingredientmech
rank: 1000
permissible_values:
  ASSIMILATION:
    text: ASSIMILATION
    description: The active species is taken up and incorporated into biomass or a
      cellular pool.
    annotations:
      typical_roles:
        tag: typical_roles
        value: nutritional_roles#CARBON_SOURCE nutritional_roles#NITROGEN_SOURCE nutritional_roles#SULFUR_SOURCE
          nutritional_roles#PHOSPHATE_SOURCE nutritional_roles#IRON_SOURCE nutritional_roles#TRACE_ELEMENT
          nutritional_roles#MINERAL_SOURCE nutritional_roles#AMINO_ACID_SOURCE nutritional_roles#PROTEIN_SOURCE
          nutritional_roles#VITAMIN_SOURCE cellular_metabolic_roles#SUBSTRATE cellular_metabolic_roles#MEMBRANE_COMPONENT
  ENERGY_CONSERVATION:
    text: ENERGY_CONSERVATION
    description: The species is an electron donor, terminal electron acceptor or energy
      substrate.
    annotations:
      typical_roles:
        tag: typical_roles
        value: nutritional_roles#ENERGY_SOURCE nutritional_roles#LIGHT_SOURCE cellular_metabolic_roles#ELECTRON_DONOR
          cellular_metabolic_roles#ELECTRON_ACCEPTOR
  COFACTOR_FUNCTION:
    text: COFACTOR_FUNCTION
    description: The species is, or is converted into, a cofactor or prosthetic group
      an enzyme requires.
    annotations:
      typical_roles:
        tag: typical_roles
        value: nutritional_roles#VITAMIN_SOURCE nutritional_roles#COFACTOR_PROVIDER
          nutritional_roles#TRACE_ELEMENT nutritional_roles#IRON_SOURCE cellular_metabolic_roles#COFACTOR
          cellular_metabolic_roles#PROSTHETIC_GROUP_PRECURSOR
  REGULATION:
    text: REGULATION
    description: The species changes gene expression or protein activity without being
      consumed.
    annotations:
      typical_roles:
        tag: typical_roles
        value: cellular_metabolic_roles#INDUCER cellular_metabolic_roles#QUENCHER
  INHIBITION:
    text: INHIBITION
    description: The species inhibits a target or growth. Link an AntibioticMech or
      NaturalProductMech record by shared grounding instead of re-curating its graph.
    annotations:
      typical_roles:
        tag: typical_roles
        value: cellular_metabolic_roles#INHIBITOR physicochemical_roles#SELECTIVE_AGENT
  STRESS_PROTECTION:
    text: STRESS_PROTECTION
    description: The species protects cells against a stress.
    annotations:
      typical_roles:
        tag: typical_roles
        value: cellular_metabolic_roles#OSMOPROTECTANT
  MEDIUM_CONDITIONING:
    text: MEDIUM_CONDITIONING
    description: The ingredient changes a medium property (pH, redox, osmolarity,
      metal availability, gel state) and through it the culture.
    annotations:
      typical_roles:
        tag: typical_roles
        value: physicochemical_roles#BUFFER physicochemical_roles#CHELATOR physicochemical_roles#REDUCING_AGENT
          physicochemical_roles#OXIDIZING_AGENT physicochemical_roles#OSMOTIC_AGENT
          physicochemical_roles#SOLIDIFYING_AGENT physicochemical_roles#PRECIPITATION_INHIBITOR
          physicochemical_roles#SURFACTANT physicochemical_roles#ANTIFOAM physicochemical_roles#PH_INDICATOR
          physicochemical_roles#REDOX_INDICATOR
  SPECIATION:
    text: SPECIATION
    description: 'Chemistry only: what the supplied form becomes (bridge and COMPONENT
      edges), with the mechanism delegated to the species'' or components'' own MIM
      records. Always NONMECHANISTIC; scope_notes names those records.'

```
</details>