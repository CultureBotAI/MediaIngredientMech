# Enum: NutritionalRoleEnum 




_What element or macronutrient an ingredient supplies to the medium. One of three orthogonal role facets (with PhysicochemicalRoleEnum and CellularMetabolicRoleEnum). A single ingredient may carry multiple nutritional roles (e.g. L-cysteine supplies both amino-acid and sulfur)._



URI: [mediaingredientmech:NutritionalRoleEnum](https://w3id.org/mediaingredientmech/NutritionalRoleEnum)

## Permissible Values

| Value | Meaning | Description |
| --- | --- | --- |
| CARBON_SOURCE | None | Provides organic carbon for biosynthesis and energy |
| NITROGEN_SOURCE | None | Provides nitrogen for amino acids, nucleotides, and other biomass components |
| SULFUR_SOURCE | None | Provides sulfur (typically for cysteine, methionine, Fe-S clusters) |
| PHOSPHATE_SOURCE | None | Provides phosphate for nucleotides, phospholipids, and energy carriers |
| IRON_SOURCE | None | Provides iron (typically for cytochromes, Fe-S clusters, and other metallopro... |
| TRACE_ELEMENT | None | Provides a micronutrient required in trace amounts (e |
| VITAMIN_SOURCE | CHEBI:33229 | Provides vitamins or vitamin precursors |
| AMINO_ACID_SOURCE | None | Provides one or more specific amino acids as building blocks |
| PROTEIN_SOURCE | None | Provides peptides, proteins, or complex amino-acid mixtures (e |
| COFACTOR_PROVIDER | None | Supplies enzyme cofactors or prosthetic groups to the medium (the compound ac... |
| ENERGY_SOURCE | None | Primary energy substrate for chemotrophic growth |
| LIGHT_SOURCE | None | Radiant-energy source for phototrophic growth |








## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/mediaingredientmech






## LinkML Source

<details>
```yaml
name: NutritionalRoleEnum
description: What element or macronutrient an ingredient supplies to the medium. One
  of three orthogonal role facets (with PhysicochemicalRoleEnum and CellularMetabolicRoleEnum).
  A single ingredient may carry multiple nutritional roles (e.g. L-cysteine supplies
  both amino-acid and sulfur).
from_schema: https://w3id.org/mediaingredientmech
rank: 1000
permissible_values:
  CARBON_SOURCE:
    text: CARBON_SOURCE
    description: Provides organic carbon for biosynthesis and energy.
    mappings:
    - METPO:2000006
  NITROGEN_SOURCE:
    text: NITROGEN_SOURCE
    description: Provides nitrogen for amino acids, nucleotides, and other biomass
      components.
    mappings:
    - METPO:2000014
  SULFUR_SOURCE:
    text: SULFUR_SOURCE
    description: Provides sulfur (typically for cysteine, methionine, Fe-S clusters).
    mappings:
    - METPO:2000020
  PHOSPHATE_SOURCE:
    text: PHOSPHATE_SOURCE
    description: Provides phosphate for nucleotides, phospholipids, and energy carriers.
  IRON_SOURCE:
    text: IRON_SOURCE
    description: Provides iron (typically for cytochromes, Fe-S clusters, and other
      metalloproteins).
  TRACE_ELEMENT:
    text: TRACE_ELEMENT
    description: Provides a micronutrient required in trace amounts (e.g., zinc, cobalt,
      manganese, molybdenum).
  VITAMIN_SOURCE:
    text: VITAMIN_SOURCE
    description: Provides vitamins or vitamin precursors.
    meaning: CHEBI:33229
  AMINO_ACID_SOURCE:
    text: AMINO_ACID_SOURCE
    description: Provides one or more specific amino acids as building blocks.
    mappings:
    - CHEBI:33709
  PROTEIN_SOURCE:
    text: PROTEIN_SOURCE
    description: Provides peptides, proteins, or complex amino-acid mixtures (e.g.,
      yeast extract, peptone, tryptone).
    mappings:
    - CHEBI:36080
  COFACTOR_PROVIDER:
    text: COFACTOR_PROVIDER
    description: Supplies enzyme cofactors or prosthetic groups to the medium (the
      compound acts as a source; contrast with CellularMetabolicRoleEnum.COFACTOR,
      which is the intracellular role).
    mappings:
    - CHEBI:23357
  ENERGY_SOURCE:
    text: ENERGY_SOURCE
    description: Primary energy substrate for chemotrophic growth.
    mappings:
    - METPO:2000010
  LIGHT_SOURCE:
    text: LIGHT_SOURCE
    description: Radiant-energy source for phototrophic growth. No CHEBI or METPO
      term yet describes a radiant-energy *supply* role (METPO:1000656 is the organism
      metabolic-mode `photoautotrophic`, not a supply-side role); METPO submission
      pending.

```
</details>