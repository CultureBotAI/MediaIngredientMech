# Enum: SiblingMechEnum 




_Fleet Mechs a node may resolve into; keys match culturebotai-claw fleet.yaml._



URI: [mediaingredientmech:SiblingMechEnum](https://w3id.org/mediaingredientmech/SiblingMechEnum)

## Permissible Values

| Value | Meaning | Description |
| --- | --- | --- |
| MEDIAINGREDIENTMECH | None | MediaIngredientMech (this repository); growth-media ingredient records |
| PROTEINTRAITSMECH | None | ProteinTraitsMech; protein trait records (sequence, structure and function tr... |
| PATHWAYMECH | None | PathwayMech; pathway-level microbial mechanism records |
| CELLSTRUCTUREMECH | None | CellStructureMech; microbial cell structure records |
| TRAITMECH | None | TraitMech; microbial ecophysiological trait records |
| TAXONMECH | None | TaxonMech; microbial taxon records (organism_scope and protein_examples taxa ... |
| ANTIBIOTICMECH | None | AntibioticMech; records of chemical structures with antimicrobial activity |
| NATURALPRODUCTMECH | None | NaturalProductMech; natural product structure records |
| HABITATMECH | None | HabitatMech; microbial habitat and environment records |
| COMMUNITYMECH | None | CommunityMech; microbial community records |




## Slots

| Name | Description |
| ---  | --- |
| [target_mech](target_mech.md) | Owning Mech when a grounding is a record in more than one Mech and the node_t... |





## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/mediaingredientmech






## LinkML Source

<details>
```yaml
name: SiblingMechEnum
description: Fleet Mechs a node may resolve into; keys match culturebotai-claw fleet.yaml.
from_schema: https://w3id.org/mediaingredientmech
rank: 1000
permissible_values:
  MEDIAINGREDIENTMECH:
    text: MEDIAINGREDIENTMECH
    description: MediaIngredientMech (this repository); growth-media ingredient records.
  PROTEINTRAITSMECH:
    text: PROTEINTRAITSMECH
    description: ProteinTraitsMech; protein trait records (sequence, structure and
      function traits, including enzymatic activities and cofactor requirements).
  PATHWAYMECH:
    text: PATHWAYMECH
    description: PathwayMech; pathway-level microbial mechanism records.
  CELLSTRUCTUREMECH:
    text: CELLSTRUCTUREMECH
    description: CellStructureMech; microbial cell structure records.
  TRAITMECH:
    text: TRAITMECH
    description: TraitMech; microbial ecophysiological trait records.
  TAXONMECH:
    text: TAXONMECH
    description: TaxonMech; microbial taxon records (organism_scope and protein_examples
      taxa resolve here).
  ANTIBIOTICMECH:
    text: ANTIBIOTICMECH
    description: AntibioticMech; records of chemical structures with antimicrobial
      activity.
  NATURALPRODUCTMECH:
    text: NATURALPRODUCTMECH
    description: NaturalProductMech; natural product structure records.
  HABITATMECH:
    text: HABITATMECH
    description: HabitatMech; microbial habitat and environment records.
  COMMUNITYMECH:
    text: COMMUNITYMECH
    description: CommunityMech; microbial community records.

```
</details>