# Enum: VariantTypeEnum 




_Classification of ingredient variant in hierarchy. Indicates the type of relationship to parent ingredient._



URI: [mediaingredientmech:VariantTypeEnum](https://w3id.org/mediaingredientmech/VariantTypeEnum)

## Permissible Values

| Value | Meaning | Description |
| --- | --- | --- |
| BASE_CHEMICAL | None | Parent/base form of chemical in hierarchy |
| HYDRATE | None | Hydrated crystalline form of compound |
| STEREOISOMER | None | Different spatial arrangement of atoms (stereochemistry) |
| PURIFIED | None | Standard purified/distilled form |
| ULTRA_PURIFIED | None | Higher purity variant than standard purified form |
| TAP | None | Impure tap water variant containing chlorine and minerals |
| DEMINERALIZED | None | Demineralized/deionized variant (ion exchange process) |
| SALT | None | Salt form of compound (different counterion) |
| ANHYDROUS | None | Water-free (anhydrous) form of compound |




## Slots

| Name | Description |
| ---  | --- |
| [variant_type](variant_type.md) | Classification of variant relationship to parent |





## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/mediaingredientmech






## LinkML Source

<details>
```yaml
name: VariantTypeEnum
description: Classification of ingredient variant in hierarchy. Indicates the type
  of relationship to parent ingredient.
from_schema: https://w3id.org/mediaingredientmech
rank: 1000
permissible_values:
  BASE_CHEMICAL:
    text: BASE_CHEMICAL
    description: 'Parent/base form of chemical in hierarchy. Example: Water (base)
      as parent of tap/distilled/double-distilled variants.'
  HYDRATE:
    text: HYDRATE
    description: 'Hydrated crystalline form of compound. Example: CaCl2·2H2O vs CaCl2
      (anhydrous).'
  STEREOISOMER:
    text: STEREOISOMER
    description: 'Different spatial arrangement of atoms (stereochemistry). Example:
      D-glucose vs L-glucose, D-biotin vs L-biotin.'
  PURIFIED:
    text: PURIFIED
    description: 'Standard purified/distilled form. Example: Distilled water (<1 µS/cm
      conductivity).'
  ULTRA_PURIFIED:
    text: ULTRA_PURIFIED
    description: 'Higher purity variant than standard purified form. Example: Double
      distilled water (<0.1 µS/cm, 10x purer than distilled).'
  TAP:
    text: TAP
    description: 'Impure tap water variant containing chlorine and minerals. Example:
      Tap water (municipal water supply).'
  DEMINERALIZED:
    text: DEMINERALIZED
    description: 'Demineralized/deionized variant (ion exchange process). Example:
      Demineralized water, DI water.'
  SALT:
    text: SALT
    description: 'Salt form of compound (different counterion). Example: Sodium phosphate
      vs potassium phosphate.'
  ANHYDROUS:
    text: ANHYDROUS
    description: 'Water-free (anhydrous) form of compound. Example: CaCl2 (anhydrous)
      vs CaCl2·2H2O (dihydrate).'

```
</details>