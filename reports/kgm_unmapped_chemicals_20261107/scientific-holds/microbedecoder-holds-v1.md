# MicrobeDecoder compound triage

All10 current compound IDs remain source-scoped unresolved, covering225 source assertions. No mapping, release or role approval is added. Current policy lineage: [KG-Microbe PR1220](https://github.com/Knowledge-Graph-Hub/kg-microbe/pull/1220).

| Source ID | Label | Observations | Decision / reason |
|---|---|---:|---|
| `kgmicrobe.compound:pyg` | PYG | 114 | A source-scoped culture-medium acronym, not one chemical or a universally fixed recipe; do not globally map114 observations to MICRO0001573 or infer component-specific utilization. |
| `kgmicrobe.compound:h2_co2` | H2+CO2 | 98 | Joint gas-substrate condition; retain each original assertion without inventing a universal gas ratio, complete medium, or independent H2-only/CO2-only consumption. |
| `kgmicrobe.compound:cyclopentanol_co2` | cyclopentanol+CO2 | 3 | Combined alcohol/CO2 condition. A complete formulation or independent consumption of each constituent does not follow from the combined source expression. |
| `kgmicrobe.compound:pygs` | PYGS | 3 | For the three pinned raw records the prior source review supports peptone-yeast extract-glucose-starch broth naming, while amounts and complete preparation remain unknown; no global exact identity or component-specific consumption is approved. |
| `kgmicrobe.compound:peptones` | peptones | 2 | Unspecified protein-digest material; current MIM Peptone/MICRO0000178 does not establish mammalian origin for these two observations. Keep source identity unresolved; a broader classification needs an explicit nonidentity route. |
| `kgmicrobe.compound:3_methylacetate` | 3-methylacetate | 1 | Actual minor-product literal is present in raw prose and structured field; chemical identity unresolved. No guessed mercaptopropionate or other replacement, no importer-fragment assertion. Separate narrow MIM notes/history correction proposed. |
| `kgmicrobe.compound:cmc_py_horse_serum` | CMC + PY + horse serum | 1 | Source combines separate cooked-meat-carbohydrate and peptone-yeast-extract culture contexts with horse serum; not carboxymethylcellulose and not one proven mixture. Existing MIM AMBIGUOUS/no-mapping correction agrees. |
| `kgmicrobe.compound:microbedecoder_unresolved_26e1775f721e16c42822b09a5ccf52e5e4e16485be4484cd446043b4ad1112ce` | sugar | 1 | An explicitly approved record-scoped unresolved identity, not permission to use generic NCIT:C71939. Preserve the two source-record nodes separately, with their original citations and no cross-record merge. |
| `kgmicrobe.compound:microbedecoder_unresolved_e70afedebc63b126613fa7f69e55fcb21b4c504a87bb1c495f57f34a7bb811b2` | sugar | 1 | An explicitly approved record-scoped unresolved identity, not permission to use generic NCIT:C71939. Preserve the two source-record nodes separately, with their original citations and no cross-record merge. |
| `kgmicrobe.compound:mono_and_disaccharides` | mono- and disaccharides | 1 | A coordinated substrate-class group, not one chemical, named medium or demonstrated physical mixture. Retain class-scope source assertion without picking individual sugars. |

The two sugar rows are distinct source records1200 and6810 and retain separate identifiers. Exact record hashes, citations, predicates, MIM owner hashes and all225 source-scoped policy rows are in the JSON ledger. Current source raw-file SHA256 is `0c6ff730a108720a5d6972400f2bccf2eca8621713b62736abdf5df0fb188c95`.

This reconciles the existing source-scope decisions and current MIM state. It does not claim a new primary-paper review of every phenotype or approve MIM component, type or role assertions. The3-methylacetate active-provenance explanation is separately proposed for correction; identity stays unresolved.
