# Enum: SolutionTypeEnum 




_Type of solution for mixture ingredients (stock solutions, pre-mixes)_



URI: [mediaingredientmech:SolutionTypeEnum](https://w3id.org/mediaingredientmech/SolutionTypeEnum)

## Permissible Values

| Value | Meaning | Description |
| --- | --- | --- |
| VITAMIN_MIX | None | Pre-mixed vitamin solution (e |
| TRACE_METAL_MIX | None | Pre-mixed trace element or metal solution |
| AMINO_ACID_MIX | None | Pre-mixed amino acid solution |
| BUFFER_SOLUTION | None | Pre-prepared buffer solution (e |
| CARBON_SOURCE_MIX | None | Pre-mixed carbon source solution |
| MINERAL_STOCK | None | Concentrated mineral stock solution |
| COFACTOR_MIX | None | Pre-mixed cofactor or enzyme supplement solution |
| COMPLEX_UNDEFINED | None | Complex undefined mixture (e |
| OTHER | None | Other type of pre-mixed solution |




## Slots

| Name | Description |
| ---  | --- |
| [solution_type](solution_type.md) | Type of solution if this is a stock/pre-mix rather than individual chemical |





## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/mediaingredientmech






## LinkML Source

<details>
```yaml
name: SolutionTypeEnum
description: Type of solution for mixture ingredients (stock solutions, pre-mixes)
from_schema: https://w3id.org/mediaingredientmech
rank: 1000
permissible_values:
  VITAMIN_MIX:
    text: VITAMIN_MIX
    description: Pre-mixed vitamin solution (e.g., vitamin B12 solution, biotin mix)
  TRACE_METAL_MIX:
    text: TRACE_METAL_MIX
    description: Pre-mixed trace element or metal solution
  AMINO_ACID_MIX:
    text: AMINO_ACID_MIX
    description: Pre-mixed amino acid solution
  BUFFER_SOLUTION:
    text: BUFFER_SOLUTION
    description: Pre-prepared buffer solution (e.g., phosphate buffer, HEPES buffer)
  CARBON_SOURCE_MIX:
    text: CARBON_SOURCE_MIX
    description: Pre-mixed carbon source solution
  MINERAL_STOCK:
    text: MINERAL_STOCK
    description: Concentrated mineral stock solution
  COFACTOR_MIX:
    text: COFACTOR_MIX
    description: Pre-mixed cofactor or enzyme supplement solution
  COMPLEX_UNDEFINED:
    text: COMPLEX_UNDEFINED
    description: Complex undefined mixture (e.g., yeast extract, peptone)
  OTHER:
    text: OTHER
    description: Other type of pre-mixed solution

```
</details>