# Enum: CommunityOrganismRoleEnum 




_Role an organism plays in a microbial community (formerly `CellularRoleEnum`; renamed 2026-07-19 to disambiguate from cell-level metabolic roles of ingredients — these values describe organisms, not ingredients)._



URI: [mediaingredientmech:CommunityOrganismRoleEnum](https://w3id.org/mediaingredientmech/CommunityOrganismRoleEnum)

## Permissible Values

| Value | Meaning | Description |
| --- | --- | --- |
| PRIMARY_DEGRADER | None | Main organism degrading target compound(s) |
| REDUCTIVE_DEGRADER | None | Degrades compounds via reductive pathways (e |
| OXIDATIVE_DEGRADER | None | Degrades compounds via oxidative pathways |
| BIOTRANSFORMER | None | Transforms compound without complete degradation |
| SYNERGIST | None | Enhances degradation by another organism |
| BRIDGE_ORGANISM | None | Converts intermediates between community members |
| ELECTRON_SHUTTLE | None | Mediates electron transfer between organisms or redox species |
| DETOXIFIER | None | Removes or neutralizes toxic compounds |
| COMMENSAL | None | Benefits from community without clear contribution |
| COMPETITOR | None | Competes for nutrients or ecological niche |








## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/mediaingredientmech






## LinkML Source

<details>
```yaml
name: CommunityOrganismRoleEnum
description: Role an organism plays in a microbial community (formerly `CellularRoleEnum`;
  renamed 2026-07-19 to disambiguate from cell-level metabolic roles of ingredients
  — these values describe organisms, not ingredients).
from_schema: https://w3id.org/mediaingredientmech
rank: 1000
permissible_values:
  PRIMARY_DEGRADER:
    text: PRIMARY_DEGRADER
    description: Main organism degrading target compound(s)
  REDUCTIVE_DEGRADER:
    text: REDUCTIVE_DEGRADER
    description: Degrades compounds via reductive pathways (e.g., reductive dechlorination)
  OXIDATIVE_DEGRADER:
    text: OXIDATIVE_DEGRADER
    description: Degrades compounds via oxidative pathways
  BIOTRANSFORMER:
    text: BIOTRANSFORMER
    description: Transforms compound without complete degradation
  SYNERGIST:
    text: SYNERGIST
    description: Enhances degradation by another organism
  BRIDGE_ORGANISM:
    text: BRIDGE_ORGANISM
    description: Converts intermediates between community members
  ELECTRON_SHUTTLE:
    text: ELECTRON_SHUTTLE
    description: Mediates electron transfer between organisms or redox species
  DETOXIFIER:
    text: DETOXIFIER
    description: Removes or neutralizes toxic compounds
  COMMENSAL:
    text: COMMENSAL
    description: Benefits from community without clear contribution
  COMPETITOR:
    text: COMPETITOR
    description: Competes for nutrients or ecological niche

```
</details>