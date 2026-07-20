# Enum: DatasetRepositoryEnum 




_Public repository hosting the dataset. Superset of CommunityMech's enum (all values preserved) plus common additions; CultureMech datasets have no repository field today and migrate with repository unset / OTHER._



URI: [mediaingredientmech:DatasetRepositoryEnum](https://w3id.org/mediaingredientmech/DatasetRepositoryEnum)

## Permissible Values

| Value | Meaning | Description |
| --- | --- | --- |
| NCBI_SRA | None | NCBI Sequence Read Archive |
| NCBI_BIOPROJECT | None | NCBI BioProject |
| NCBI_GEO | None | NCBI Gene Expression Omnibus |
| NCBI_ASSEMBLY | None | NCBI Assembly (genome assemblies) |
| ENA | None | European Nucleotide Archive |
| ARRAYEXPRESS | None | EBI ArrayExpress / BioStudies |
| MGNIFY | None | EBI MGnify metagenomics resource |
| JGI_GOLD | None | JGI Genomes OnLine Database |
| JGI_IMG | None | JGI Integrated Microbial Genomes & Microbiomes |
| NMDC | None | National Microbiome Data Collaborative |
| METABOLOMICS_WORKBENCH | None | NIH Metabolomics Workbench |
| METABOLIGHTS | None | EBI MetaboLights metabolomics repository |
| MASSIVE | None | MassIVE mass-spectrometry repository |
| GNPS | None | Global Natural Products Social Molecular Networking |
| PRIDE | None | EBI PRIDE proteomics repository |
| DBGAP | None | NCBI database of Genotypes and Phenotypes |
| GTEX | None | Genotype-Tissue Expression project |
| FIGSHARE | None | Figshare general-purpose research data archive |
| ZENODO | None | Zenodo general-purpose research data archive |
| BIOMODELS | None | EBI BioModels repository of computational models |
| KBASE | None | DOE Systems Biology Knowledgebase (KBase) |
| OTHER | None | A repository not covered by the above |




## Slots

| Name | Description |
| ---  | --- |
| [repository](repository.md) |  |





## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/mediaingredientmech






## LinkML Source

<details>
```yaml
name: DatasetRepositoryEnum
description: Public repository hosting the dataset. Superset of CommunityMech's enum
  (all values preserved) plus common additions; CultureMech datasets have no repository
  field today and migrate with repository unset / OTHER.
from_schema: https://w3id.org/mediaingredientmech
rank: 1000
permissible_values:
  NCBI_SRA:
    text: NCBI_SRA
    description: NCBI Sequence Read Archive.
  NCBI_BIOPROJECT:
    text: NCBI_BIOPROJECT
    description: NCBI BioProject.
  NCBI_GEO:
    text: NCBI_GEO
    description: NCBI Gene Expression Omnibus.
  NCBI_ASSEMBLY:
    text: NCBI_ASSEMBLY
    description: NCBI Assembly (genome assemblies).
  ENA:
    text: ENA
    description: European Nucleotide Archive.
  ARRAYEXPRESS:
    text: ARRAYEXPRESS
    description: EBI ArrayExpress / BioStudies.
  MGNIFY:
    text: MGNIFY
    description: EBI MGnify metagenomics resource.
  JGI_GOLD:
    text: JGI_GOLD
    description: JGI Genomes OnLine Database.
  JGI_IMG:
    text: JGI_IMG
    description: JGI Integrated Microbial Genomes & Microbiomes.
  NMDC:
    text: NMDC
    description: National Microbiome Data Collaborative.
  METABOLOMICS_WORKBENCH:
    text: METABOLOMICS_WORKBENCH
    description: NIH Metabolomics Workbench.
  METABOLIGHTS:
    text: METABOLIGHTS
    description: EBI MetaboLights metabolomics repository.
  MASSIVE:
    text: MASSIVE
    description: MassIVE mass-spectrometry repository.
  GNPS:
    text: GNPS
    description: Global Natural Products Social Molecular Networking.
  PRIDE:
    text: PRIDE
    description: EBI PRIDE proteomics repository.
  DBGAP:
    text: DBGAP
    description: NCBI database of Genotypes and Phenotypes.
  GTEX:
    text: GTEX
    description: Genotype-Tissue Expression project.
  FIGSHARE:
    text: FIGSHARE
    description: Figshare general-purpose research data archive.
  ZENODO:
    text: ZENODO
    description: Zenodo general-purpose research data archive.
  BIOMODELS:
    text: BIOMODELS
    description: EBI BioModels repository of computational models.
  KBASE:
    text: KBASE
    description: DOE Systems Biology Knowledgebase (KBase).
  OTHER:
    text: OTHER
    description: A repository not covered by the above.

```
</details>