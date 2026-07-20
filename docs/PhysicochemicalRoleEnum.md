# Enum: PhysicochemicalRoleEnum 




_Chemical or physical function an ingredient performs in the medium, independent of what element it supplies. One of three orthogonal role facets (with NutritionalRoleEnum and CellularMetabolicRoleEnum)._



URI: [mediaingredientmech:PhysicochemicalRoleEnum](https://w3id.org/mediaingredientmech/PhysicochemicalRoleEnum)

## Permissible Values

| Value | Meaning | Description |
| --- | --- | --- |
| BUFFER | CHEBI:35225 | Maintains stable pH via a conjugate acid–base system |
| SOLIDIFYING_AGENT | None | Gelling agent for solid or semi-solid media (e |
| CHELATOR | CHEBI:38161 | Sequesters metal ions to control availability, toxicity, or precipitation (e |
| SURFACTANT | CHEBI:35195 | Reduces surface tension for emulsification, solubilization, or membrane perme... |
| REDUCING_AGENT | CHEBI:63247 | Lowers the redox potential of the medium (e |
| OXIDIZING_AGENT | CHEBI:63248 | Raises the redox potential of the medium |
| PH_INDICATOR | CHEBI:50407 | Colorimetric acid–base indicator dye (e |
| REDOX_INDICATOR | None | Colorimetric indicator of redox potential (e |
| SELECTIVE_AGENT | None | Antimicrobial or otherwise selective agent used to enrich for or against part... |
| ANTIFOAM | CHEBI:77973 | Suppresses foaming in aerated or vigorously mixed cultures (e |
| OSMOTIC_AGENT | None | Contributes primarily to the osmotic strength of the medium (e |
| PRECIPITATION_INHIBITOR | None | Prevents precipitation of otherwise poorly-soluble medium components (e |








## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/mediaingredientmech






## LinkML Source

<details>
```yaml
name: PhysicochemicalRoleEnum
description: Chemical or physical function an ingredient performs in the medium, independent
  of what element it supplies. One of three orthogonal role facets (with NutritionalRoleEnum
  and CellularMetabolicRoleEnum).
from_schema: https://w3id.org/mediaingredientmech
rank: 1000
permissible_values:
  BUFFER:
    text: BUFFER
    description: Maintains stable pH via a conjugate acid–base system.
    meaning: CHEBI:35225
  SOLIDIFYING_AGENT:
    text: SOLIDIFYING_AGENT
    description: Gelling agent for solid or semi-solid media (e.g., agar, gellan gum,
      silica gel).
  CHELATOR:
    text: CHELATOR
    description: Sequesters metal ions to control availability, toxicity, or precipitation
      (e.g., EDTA, NTA, citrate).
    meaning: CHEBI:38161
  SURFACTANT:
    text: SURFACTANT
    description: Reduces surface tension for emulsification, solubilization, or membrane
      permeabilization (e.g., Tween, Triton X-100).
    meaning: CHEBI:35195
    mappings:
    - CHEBI:63046
  REDUCING_AGENT:
    text: REDUCING_AGENT
    description: Lowers the redox potential of the medium (e.g., sodium sulfide, cysteine,
      thioglycolate, dithiothreitol).
    meaning: CHEBI:63247
  OXIDIZING_AGENT:
    text: OXIDIZING_AGENT
    description: Raises the redox potential of the medium.
    meaning: CHEBI:63248
  PH_INDICATOR:
    text: PH_INDICATOR
    description: Colorimetric acid–base indicator dye (e.g., phenol red, bromothymol
      blue).
    meaning: CHEBI:50407
  REDOX_INDICATOR:
    text: REDOX_INDICATOR
    description: Colorimetric indicator of redox potential (e.g., resazurin turns
      pink under mildly oxidizing conditions).
    mappings:
    - CHEBI:47867
  SELECTIVE_AGENT:
    text: SELECTIVE_AGENT
    description: Antimicrobial or otherwise selective agent used to enrich for or
      against particular organisms (e.g., antibiotics, bile salts, high salt, azide).
    mappings:
    - CHEBI:33281
    - CHEBI:33282
    - CHEBI:35718
  ANTIFOAM:
    text: ANTIFOAM
    description: Suppresses foaming in aerated or vigorously mixed cultures (e.g.,
      silicone antifoam, polypropylene glycol).
    meaning: CHEBI:77973
  OSMOTIC_AGENT:
    text: OSMOTIC_AGENT
    description: Contributes primarily to the osmotic strength of the medium (e.g.,
      NaCl at high concentration, sucrose, glycerol as osmolyte).
    mappings:
    - CHEBI:25728
  PRECIPITATION_INHIBITOR:
    text: PRECIPITATION_INHIBITOR
    description: Prevents precipitation of otherwise poorly-soluble medium components
      (e.g., citrate keeping iron soluble at neutral pH).

```
</details>