# Enum: CurationActionEnum 




_Documentation-only reference list of well-known curation action labels. The `action` slot on CurationEvent has range `string` constrained by a SCREAMING_SNAKE_CASE pattern, not membership in this enum — curation tools mint new labels freely (live data has 117 distinct values as of 2026-05-12). The 25 labels below cover the 9 baseline operation verbs plus the most frequent automated/classification/merge labels observed in live data (together >93% of all curation events). New tools should reuse one of these names when applicable rather than inventing a near-duplicate._



URI: [mediaingredientmech:CurationActionEnum](https://w3id.org/mediaingredientmech/CurationActionEnum)

## Permissible Values

| Value | Meaning | Description |
| --- | --- | --- |
| CREATED | None | Record minted by a curator or import tool |
| IMPORTED | None | Record imported from an external source |
| MAPPED | None | Ontology mapping added or replaced |
| ANNOTATED | None | Notes or freeform metadata added |
| CORRECTED | None | Mapping or data corrected (in response to a review finding) |
| MERGED | None | Record merged with another record |
| STATUS_CHANGED | None | `mapping_status` field changed |
| VALIDATED | None | Mapping validated against ontology or reference data |
| SYNONYM_ADDED | None | Single synonym added (cf |
| AUTO_CLASSIFY_INGREDIENT_TYPE | None | Automated `ingredient_type` classification (single chemical, defined medium, ... |
| AUTO_BACKFILL_CHEBI_CHEMISTRY | None | Automated backfill of molecular formula / SMILES / InChI from ChEBI |
| AUTO_BACKFILL_PUBCHEM_CHEMISTRY | None | Automated backfill of chemical properties from PubChem |
| ADDED_SYNONYMS | None | Batch synonym add (multiple synonyms in one event) |
| ADDED_CAS_RN | None | CAS Registry Number added to a record |
| CAS_RN_ADDED | None | Legacy alias for ADDED_CAS_RN emitted by older tooling |
| CREATED_AS_UNMAPPED | None | Record minted in the UNMAPPED state, awaiting ontology lookup |
| CREATED_FROM_CULTUREBOTHT | None | Record imported from the CultureBot HT pipeline |
| CREATED_FROM_CAS_LOOKUP | None | Record created after resolving an unmapped name via CAS lookup |
| CREATED_FROM_CAS_FALLBACK | None | Record created with a `cas:` fallback identity when no ontology term was foun... |
| CREATED_FROM_KGM_PLACEHOLDER | None | Record created from a kg-microbe placeholder ingredient row |
| CLASSIFIED_UNDEFINED_MIXTURE | None | Classified as an undefined mixture (yeast extract, peptone,  |
| CLASSIFIED_STOCK_SOLUTION | None | Classified as a stock solution / premix |
| CLASSIFIED_DEFINED_MEDIUM | None | Classified as a complete defined-medium recipe |
| MERGED_FROM_DUPLICATES | None | Duplicate records consolidated into this representative |
| BACKFILL_PARENT_CHEBI | None | `parent_ingredient` populated by lookup against CHEBI hierarchy |








## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/mediaingredientmech






## LinkML Source

<details>
```yaml
name: CurationActionEnum
description: Documentation-only reference list of well-known curation action labels.
  The `action` slot on CurationEvent has range `string` constrained by a SCREAMING_SNAKE_CASE
  pattern, not membership in this enum — curation tools mint new labels freely (live
  data has 117 distinct values as of 2026-05-12). The 25 labels below cover the 9
  baseline operation verbs plus the most frequent automated/classification/merge labels
  observed in live data (together >93% of all curation events). New tools should reuse
  one of these names when applicable rather than inventing a near-duplicate.
from_schema: https://w3id.org/mediaingredientmech
rank: 1000
permissible_values:
  CREATED:
    text: CREATED
    description: Record minted by a curator or import tool.
  IMPORTED:
    text: IMPORTED
    description: Record imported from an external source.
  MAPPED:
    text: MAPPED
    description: Ontology mapping added or replaced.
  ANNOTATED:
    text: ANNOTATED
    description: Notes or freeform metadata added.
  CORRECTED:
    text: CORRECTED
    description: Mapping or data corrected (in response to a review finding).
  MERGED:
    text: MERGED
    description: Record merged with another record.
  STATUS_CHANGED:
    text: STATUS_CHANGED
    description: '`mapping_status` field changed.'
  VALIDATED:
    text: VALIDATED
    description: Mapping validated against ontology or reference data.
  SYNONYM_ADDED:
    text: SYNONYM_ADDED
    description: Single synonym added (cf. plural ADDED_SYNONYMS for batch).
  AUTO_CLASSIFY_INGREDIENT_TYPE:
    text: AUTO_CLASSIFY_INGREDIENT_TYPE
    description: Automated `ingredient_type` classification (single chemical, defined
      medium, mixture, stock).
  AUTO_BACKFILL_CHEBI_CHEMISTRY:
    text: AUTO_BACKFILL_CHEBI_CHEMISTRY
    description: Automated backfill of molecular formula / SMILES / InChI from ChEBI.
  AUTO_BACKFILL_PUBCHEM_CHEMISTRY:
    text: AUTO_BACKFILL_PUBCHEM_CHEMISTRY
    description: Automated backfill of chemical properties from PubChem.
  ADDED_SYNONYMS:
    text: ADDED_SYNONYMS
    description: Batch synonym add (multiple synonyms in one event).
  ADDED_CAS_RN:
    text: ADDED_CAS_RN
    description: CAS Registry Number added to a record.
  CAS_RN_ADDED:
    text: CAS_RN_ADDED
    description: Legacy alias for ADDED_CAS_RN emitted by older tooling. Prefer ADDED_CAS_RN
      in new code.
  CREATED_AS_UNMAPPED:
    text: CREATED_AS_UNMAPPED
    description: Record minted in the UNMAPPED state, awaiting ontology lookup.
  CREATED_FROM_CULTUREBOTHT:
    text: CREATED_FROM_CULTUREBOTHT
    description: Record imported from the CultureBot HT pipeline.
  CREATED_FROM_CAS_LOOKUP:
    text: CREATED_FROM_CAS_LOOKUP
    description: Record created after resolving an unmapped name via CAS lookup.
  CREATED_FROM_CAS_FALLBACK:
    text: CREATED_FROM_CAS_FALLBACK
    description: Record created with a `cas:` fallback identity when no ontology term
      was found.
  CREATED_FROM_KGM_PLACEHOLDER:
    text: CREATED_FROM_KGM_PLACEHOLDER
    description: Record created from a kg-microbe placeholder ingredient row.
  CLASSIFIED_UNDEFINED_MIXTURE:
    text: CLASSIFIED_UNDEFINED_MIXTURE
    description: Classified as an undefined mixture (yeast extract, peptone, ...).
  CLASSIFIED_STOCK_SOLUTION:
    text: CLASSIFIED_STOCK_SOLUTION
    description: Classified as a stock solution / premix.
  CLASSIFIED_DEFINED_MEDIUM:
    text: CLASSIFIED_DEFINED_MEDIUM
    description: Classified as a complete defined-medium recipe.
  MERGED_FROM_DUPLICATES:
    text: MERGED_FROM_DUPLICATES
    description: Duplicate records consolidated into this representative.
  BACKFILL_PARENT_CHEBI:
    text: BACKFILL_PARENT_CHEBI
    description: '`parent_ingredient` populated by lookup against CHEBI hierarchy.'

```
</details>