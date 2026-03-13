# Enum: SynonymTypeEnum 



URI: [mediaingredientmech:SynonymTypeEnum](https://w3id.org/mediaingredientmech/SynonymTypeEnum)

## Permissible Values

| Value | Meaning | Description |
| --- | --- | --- |
| EXACT_SYNONYM | None | Exact alternative name |
| RELATED_SYNONYM | None | Related but not identical |
| RAW_TEXT | None | Raw text from original data |
| ABBREVIATION | None | Abbreviated form |
| COMMON_NAME | None | Common or colloquial name |
| SYSTEMATIC_NAME | None | Systematic chemical name |
| HYDRATE_FORM | None | Chemical with hydrate notation (e |
| CATALOG_VARIANT | None | Name with catalog/supplier code (e |
| INCOMPLETE_FORMULA | None | Incomplete chemical formula (e |
| ALTERNATE_FORM | None | Alternative chemical form (salt, ester, etc |




## Slots

| Name | Description |
| ---  | --- |
| [synonym_type](synonym_type.md) | Type of synonym |





## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/mediaingredientmech






## LinkML Source

<details>
```yaml
name: SynonymTypeEnum
from_schema: https://w3id.org/mediaingredientmech
rank: 1000
permissible_values:
  EXACT_SYNONYM:
    text: EXACT_SYNONYM
    description: Exact alternative name
  RELATED_SYNONYM:
    text: RELATED_SYNONYM
    description: Related but not identical
  RAW_TEXT:
    text: RAW_TEXT
    description: Raw text from original data
  ABBREVIATION:
    text: ABBREVIATION
    description: Abbreviated form
  COMMON_NAME:
    text: COMMON_NAME
    description: Common or colloquial name
  SYSTEMATIC_NAME:
    text: SYSTEMATIC_NAME
    description: Systematic chemical name
  HYDRATE_FORM:
    text: HYDRATE_FORM
    description: Chemical with hydrate notation (e.g., MgSO4•7H2O)
  CATALOG_VARIANT:
    text: CATALOG_VARIANT
    description: Name with catalog/supplier code (e.g., NaCl Fisher S271-500)
  INCOMPLETE_FORMULA:
    text: INCOMPLETE_FORMULA
    description: Incomplete chemical formula (e.g., K2HPO instead of K2HPO4)
  ALTERNATE_FORM:
    text: ALTERNATE_FORM
    description: Alternative chemical form (salt, ester, etc.)

```
</details>