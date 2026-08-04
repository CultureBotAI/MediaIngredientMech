# Enum: DatasetTypeEnum 




_Type of dataset or data resource. Canonical UNION of CultureMech's and CommunityMech's enums plus microbial additions. Migration map (old → this): CultureMech values carry over unchanged; CommunityMech GENOME→GENOMICS, METAGENOME→METAGENOMICS, METATRANSCRIPTOME→METATRANSCRIPTOMICS, METAPROTEOME→METAPROTEOMICS (AMPLICON_16S / AMPLICON_ITS / METABOLOMICS / PHENOTYPE / MULTI_OMICS / OTHER are unchanged)._



URI: [mediaingredientmech:DatasetTypeEnum](https://w3id.org/mediaingredientmech/DatasetTypeEnum)

## Permissible Values

| Value | Meaning | Description |
| --- | --- | --- |
| GENOMICS | None | Isolate / single-organism genome data |
| METAGENOMICS | None | Shotgun metagenome sequencing |
| AMPLICON_16S | None | 16S rRNA marker-gene amplicon sequencing |
| AMPLICON_ITS | None | ITS marker-gene amplicon sequencing |
| AMPLICON_OTHER | None | Marker-gene amplicon sequencing other than 16S/ITS (e |
| TRANSCRIPTOMICS | None | Single-organism RNA sequencing / expression |
| METATRANSCRIPTOMICS | None | Community-level RNA sequencing |
| PROTEOMICS | None | Single-organism protein expression profiling |
| METAPROTEOMICS | None | Community-level proteomics |
| METABOLOMICS | None | Metabolite profiling |
| FLUXOMICS | None | Metabolic flux profiling |
| PHENOMICS | None | High-throughput phenotype profiling |
| PHENOTYPE | None | Phenotype / trait measurement collection (e |
| MULTI_OMICS | None | Integrated multi-omics profiling |
| OTHER | None | A dataset type not covered by the above |




## Slots

| Name | Description |
| ---  | --- |
| [dataset_type](dataset_type.md) |  |





## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/mediaingredientmech






## LinkML Source

<details>
```yaml
name: DatasetTypeEnum
description: 'Type of dataset or data resource. Canonical UNION of CultureMech''s
  and CommunityMech''s enums plus microbial additions. Migration map (old → this):
  CultureMech values carry over unchanged; CommunityMech GENOME→GENOMICS, METAGENOME→METAGENOMICS,
  METATRANSCRIPTOME→METATRANSCRIPTOMICS, METAPROTEOME→METAPROTEOMICS (AMPLICON_16S
  / AMPLICON_ITS / METABOLOMICS / PHENOTYPE / MULTI_OMICS / OTHER are unchanged).'
from_schema: https://w3id.org/mediaingredientmech
rank: 1000
permissible_values:
  GENOMICS:
    text: GENOMICS
    description: Isolate / single-organism genome data. (CultureMech GENOMICS; CommunityMech
      GENOME)
  METAGENOMICS:
    text: METAGENOMICS
    description: Shotgun metagenome sequencing. (CommunityMech METAGENOME)
  AMPLICON_16S:
    text: AMPLICON_16S
    description: 16S rRNA marker-gene amplicon sequencing.
  AMPLICON_ITS:
    text: AMPLICON_ITS
    description: ITS marker-gene amplicon sequencing.
  AMPLICON_OTHER:
    text: AMPLICON_OTHER
    description: Marker-gene amplicon sequencing other than 16S/ITS (e.g. 18S, rpoB).
  TRANSCRIPTOMICS:
    text: TRANSCRIPTOMICS
    description: Single-organism RNA sequencing / expression.
  METATRANSCRIPTOMICS:
    text: METATRANSCRIPTOMICS
    description: Community-level RNA sequencing. (CommunityMech METATRANSCRIPTOME)
  PROTEOMICS:
    text: PROTEOMICS
    description: Single-organism protein expression profiling.
  METAPROTEOMICS:
    text: METAPROTEOMICS
    description: Community-level proteomics. (CommunityMech METAPROTEOME)
  METABOLOMICS:
    text: METABOLOMICS
    description: Metabolite profiling.
  FLUXOMICS:
    text: FLUXOMICS
    description: Metabolic flux profiling.
  PHENOMICS:
    text: PHENOMICS
    description: High-throughput phenotype profiling.
  PHENOTYPE:
    text: PHENOTYPE
    description: Phenotype / trait measurement collection (e.g. growth, biochemical).
  MULTI_OMICS:
    text: MULTI_OMICS
    description: Integrated multi-omics profiling.
  OTHER:
    text: OTHER
    description: A dataset type not covered by the above.

```
</details>