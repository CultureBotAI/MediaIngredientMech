

# Slot: source_columns


_The upstream columns the count was aggregated over, verbatim (e.g. `BacDive_Metabolite_utilization|Bergey_substrate`), so the number stays interpretable without the original extract._





URI: [mediaingredientmech:source_columns](https://w3id.org/mediaingredientmech/source_columns)
Alias: source_columns

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [SourceOccurrence](SourceOccurrence.md) | An occurrence count attributed to a specific upstream source, with the source... |  no  |






## Properties

* Range: [String](String.md)




## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/mediaingredientmech




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | mediaingredientmech:source_columns |
| native | mediaingredientmech:source_columns |




## LinkML Source

<details>
```yaml
name: source_columns
description: The upstream columns the count was aggregated over, verbatim (e.g. `BacDive_Metabolite_utilization|Bergey_substrate`),
  so the number stays interpretable without the original extract.
from_schema: https://w3id.org/mediaingredientmech
rank: 1000
alias: source_columns
owner: SourceOccurrence
domain_of:
- SourceOccurrence
range: string

```
</details>