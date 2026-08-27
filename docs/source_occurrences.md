

# Slot: source_occurrences 


_Prevalence recorded by a NON-media source, kept separate from total_occurrences/media_count so it never inflates the media counts. total_occurrences answers "in how many CultureMech media recipes does this appear", which is legitimately 0 for an ingredient sourced from BacDive traits or Bergey substrates. Recording that alone discarded the abundance signal those sources carry -- the same signal used to rank the candidates worth onboarding -- leaving 386 zero-weight records for anything downstream that weights ingredients by prevalence (#196)._





URI: [mediaingredientmech:source_occurrences](https://w3id.org/mediaingredientmech/source_occurrences)
Alias: source_occurrences

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [OccurrenceStats](OccurrenceStats.md) | Statistics about ingredient usage across media |  no  |






## Properties

* Range: [SourceOccurrence](SourceOccurrence.md)

* Multivalued: True




## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/mediaingredientmech




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | mediaingredientmech:source_occurrences |
| native | mediaingredientmech:source_occurrences |




## LinkML Source

<details>
```yaml
name: source_occurrences
description: Prevalence recorded by a NON-media source, kept separate from total_occurrences/media_count
  so it never inflates the media counts. total_occurrences answers "in how many CultureMech
  media recipes does this appear", which is legitimately 0 for an ingredient sourced
  from BacDive traits or Bergey substrates. Recording that alone discarded the abundance
  signal those sources carry -- the same signal used to rank the candidates worth
  onboarding -- leaving 386 zero-weight records for anything downstream that weights
  ingredients by prevalence (#196).
from_schema: https://w3id.org/mediaingredientmech
rank: 1000
alias: source_occurrences
owner: OccurrenceStats
domain_of:
- OccurrenceStats
range: SourceOccurrence
multivalued: true
inlined: true
inlined_as_list: true

```
</details>