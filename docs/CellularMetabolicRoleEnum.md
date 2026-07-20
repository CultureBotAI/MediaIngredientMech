# Enum: CellularMetabolicRoleEnum 




_Role of the ingredient inside or on the cultured microbe(s) — the compound's metabolic fate or biochemical function at the cell level. One of three orthogonal role facets (with NutritionalRoleEnum and PhysicochemicalRoleEnum). Values in this facet are often organism-conditional (e.g. ELECTRON_DONOR applies only for organisms that oxidize the compound for energy; methanol is an electron donor for methylotrophs but only a carbon source for others)._



URI: [mediaingredientmech:CellularMetabolicRoleEnum](https://w3id.org/mediaingredientmech/CellularMetabolicRoleEnum)

## Permissible Values

| Value | Meaning | Description |
| --- | --- | --- |
| SUBSTRATE | None | Consumed by the organism for biosynthesis, energy, or both (general-purpose s... |
| ELECTRON_DONOR | CHEBI:15022 | Electron donor for chemolithotrophic or heterotrophic energy metabolism (orga... |
| ELECTRON_ACCEPTOR | CHEBI:17654 | Terminal electron acceptor for respiration (e |
| COFACTOR | CHEBI:23357 | Acts as an intracellular enzyme cofactor (contrast with NutritionalRoleEnum |
| PROSTHETIC_GROUP_PRECURSOR | None | Precursor for a covalently-bound cofactor / prosthetic group (e |
| MEMBRANE_COMPONENT | None | Incorporated into cell membranes (e |
| OSMOPROTECTANT | None | Accumulated intracellularly to balance external osmotic stress (e |
| INDUCER | None | Triggers expression of specific genes or pathways when present (e |
| INHIBITOR | CHEBI:35222 | Suppresses growth or a specific pathway (e |
| QUENCHER | None | Absorbs or dissipates a signal (e |








## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/mediaingredientmech






## LinkML Source

<details>
```yaml
name: CellularMetabolicRoleEnum
description: Role of the ingredient inside or on the cultured microbe(s) — the compound's
  metabolic fate or biochemical function at the cell level. One of three orthogonal
  role facets (with NutritionalRoleEnum and PhysicochemicalRoleEnum). Values in this
  facet are often organism-conditional (e.g. ELECTRON_DONOR applies only for organisms
  that oxidize the compound for energy; methanol is an electron donor for methylotrophs
  but only a carbon source for others).
from_schema: https://w3id.org/mediaingredientmech
rank: 1000
permissible_values:
  SUBSTRATE:
    text: SUBSTRATE
    description: Consumed by the organism for biosynthesis, energy, or both (general-purpose
      substrate role).
  ELECTRON_DONOR:
    text: ELECTRON_DONOR
    description: Electron donor for chemolithotrophic or heterotrophic energy metabolism
      (organism-conditional).
    meaning: CHEBI:15022
  ELECTRON_ACCEPTOR:
    text: ELECTRON_ACCEPTOR
    description: Terminal electron acceptor for respiration (e.g., nitrate, oxygen,
      sulfate; organism-conditional).
    meaning: CHEBI:17654
  COFACTOR:
    text: COFACTOR
    description: Acts as an intracellular enzyme cofactor (contrast with NutritionalRoleEnum.COFACTOR_PROVIDER,
      the supply-side role).
    meaning: CHEBI:23357
  PROSTHETIC_GROUP_PRECURSOR:
    text: PROSTHETIC_GROUP_PRECURSOR
    description: Precursor for a covalently-bound cofactor / prosthetic group (e.g.,
      δ-aminolevulinate for heme). Note the mapping below points at the parent role
      `prosthetic group` — CHEBI has no dedicated `prosthetic group precursor` role
      class, so the mapping is a hierarchy pointer, not identity.
    mappings:
    - CHEBI:26348
  MEMBRANE_COMPONENT:
    text: MEMBRANE_COMPONENT
    description: Incorporated into cell membranes (e.g., fatty acids, sterols, isoprenoid
      lipids).
  OSMOPROTECTANT:
    text: OSMOPROTECTANT
    description: 'Accumulated intracellularly to balance external osmotic stress (e.g.,
      glycine betaine, ectoine, trehalose). Organism-conditional — assign only with
      organism-context evidence (e.g., "glycine betaine is imported and accumulated
      as an osmoprotectant by <organism>"). NOTE: shares `mappings: CHEBI:25728 (osmolyte)`
      with PhysicochemicalRoleEnum.OSMOTIC_AGENT. See that value''s description for
      cross-facet guidance.'
    mappings:
    - CHEBI:25728
  INDUCER:
    text: INDUCER
    description: Triggers expression of specific genes or pathways when present (e.g.,
      IPTG, arabinose).
  INHIBITOR:
    text: INHIBITOR
    description: Suppresses growth or a specific pathway (e.g., antibiotics targeting
      cellular processes).
    meaning: CHEBI:35222
  QUENCHER:
    text: QUENCHER
    description: Absorbs or dissipates a signal (e.g., quenches fluorescence, radicals,
      or light).

```
</details>