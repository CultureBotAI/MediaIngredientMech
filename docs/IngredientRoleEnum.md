# Enum: IngredientRoleEnum 




_Functional roles of ingredients in growth medium formulation_



URI: [mediaingredientmech:IngredientRoleEnum](https://w3id.org/mediaingredientmech/IngredientRoleEnum)

## Permissible Values

| Value | Meaning | Description |
| --- | --- | --- |
| CARBON_SOURCE | None | Provides organic carbon for biosynthesis and energy |
| NITROGEN_SOURCE | None | Provides nitrogen for amino acids, nucleotides, etc |
| MINERAL | None | Inorganic mineral nutrient (e |
| TRACE_ELEMENT | None | Micronutrient required in trace amounts (e |
| BUFFER | None | pH buffering agent to maintain stable pH |
| VITAMIN_SOURCE | None | Provides vitamins or vitamin precursors |
| SALT | None | Provides ionic strength and osmotic balance |
| PROTEIN_SOURCE | None | Provides peptides, proteins, or amino acids |
| AMINO_ACID_SOURCE | None | Provides specific amino acids |
| SOLIDIFYING_AGENT | None | Gelling agent for solid media (e |
| ENERGY_SOURCE | None | Primary energy substrate for chemotrophs |
| ELECTRON_ACCEPTOR | None | Terminal electron acceptor for respiration (e |
| ELECTRON_DONOR | None | Electron donor for chemolithotrophs |
| COFACTOR_PROVIDER | None | Provides enzyme cofactors or prosthetic groups |




## Slots

| Name | Description |
| ---  | --- |
| [role](role.md) | The functional role (e |





## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/mediaingredientmech






## LinkML Source

<details>
```yaml
name: IngredientRoleEnum
description: Functional roles of ingredients in growth medium formulation
from_schema: https://w3id.org/mediaingredientmech
rank: 1000
permissible_values:
  CARBON_SOURCE:
    text: CARBON_SOURCE
    description: Provides organic carbon for biosynthesis and energy
  NITROGEN_SOURCE:
    text: NITROGEN_SOURCE
    description: Provides nitrogen for amino acids, nucleotides, etc.
  MINERAL:
    text: MINERAL
    description: Inorganic mineral nutrient (e.g., phosphate, sulfate, magnesium)
  TRACE_ELEMENT:
    text: TRACE_ELEMENT
    description: Micronutrient required in trace amounts (e.g., iron, zinc, cobalt)
  BUFFER:
    text: BUFFER
    description: pH buffering agent to maintain stable pH
  VITAMIN_SOURCE:
    text: VITAMIN_SOURCE
    description: Provides vitamins or vitamin precursors
  SALT:
    text: SALT
    description: Provides ionic strength and osmotic balance
  PROTEIN_SOURCE:
    text: PROTEIN_SOURCE
    description: Provides peptides, proteins, or amino acids
  AMINO_ACID_SOURCE:
    text: AMINO_ACID_SOURCE
    description: Provides specific amino acids
  SOLIDIFYING_AGENT:
    text: SOLIDIFYING_AGENT
    description: Gelling agent for solid media (e.g., agar)
  ENERGY_SOURCE:
    text: ENERGY_SOURCE
    description: Primary energy substrate for chemotrophs
  ELECTRON_ACCEPTOR:
    text: ELECTRON_ACCEPTOR
    description: Terminal electron acceptor for respiration (e.g., nitrate, oxygen)
  ELECTRON_DONOR:
    text: ELECTRON_DONOR
    description: Electron donor for chemolithotrophs
  COFACTOR_PROVIDER:
    text: COFACTOR_PROVIDER
    description: Provides enzyme cofactors or prosthetic groups

```
</details>