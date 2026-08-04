# Onboarding assessment: kg-microbe `microbedecoder` unmapped labels

**Date:** 2026-08-03
**Branch:** `feat/onboard-microbedecoder-unmapped`
**Source:** `kg-microbe/data/transformed/microbedecoder/unmapped_labels.tsv`
**Staged copy:** `data/custom/microbedecoder/unmapped_labels.tsv` (5,224 rows + header)
**Derived product:** `data/custom/microbedecoder/ingredient_candidates.tsv` (1,023 rows)

## What this source is

A dump of labels that the kg-microbe `microbedecoder` transform could **not** map to an
ontology term. Each row is a distinct free-text label plus the placeholder CURIE
microbedecoder minted for it, the biolink category it guessed, the BacDive/Bergey/FAPROTAX
source column(s) it came from, and an occurrence count across the graph.

Columns: `placeholder_curie | category | label | source_columns | occurrences`.

The header-level `category` is coarse and **understates** the ingredient content — only 73
rows are tagged `biolink:ChemicalEntity`, but a much larger set of chemicals is hiding inside
rows tagged `biolink:PhenotypicQuality` (metabolite-utilization / antibiotic assays). You have
to classify by `source_columns`, not by `category`, to find the ingredients.

## Header category (as-shipped, misleading)

| category | rows | placeholder prefix |
|---|---|---|
| biolink:PhenotypicQuality | 5,061 | kgmicrobe.trait |
| biolink:BiologicalProcess | 90 | kgmicrobe.pathway |
| biolink:ChemicalEntity | 73 | kgmicrobe.compound |

## Real breakdown by source column (unique rows)

| bucket | rows | is it an ingredient? |
|---|---|---|
| **Chemicals / substrates** (Metabolite_utilization, Metabolite_production, bergey substrates + end-products) | 885 | **yes** — carbon sources, sugars, acids, media blends |
| **Antibiotics** (Antibiotic_sensitivity / _resistance) | 146 | **yes** — chemical compounds |
| Environment / host / food (Isolation_category_1/2/3) | 347 | **no** — ENVO/host/food context, not a media ingredient |
| Enzyme activity | 120 | mostly no — enzyme names, not ingredients |
| Numeric / measurement / other phenotype (cell length/width, temp, pH, salt, colony size, incubation, gram stain, oxygen, motility, shape…) | 3,636 | no |
| Metabolic-function pathways (FAPROTAX / bergey type_of_metabolism) | 90 | no — biological processes |

## Headline answer: how many chemicals / ingredients?

**~1,023 distinct chemical/ingredient candidate labels** (885 substrate/metabolite + 146
antibiotic, minus 8 pure-noise labels like `1`, `2`, `%(w/v)`, `Not reported`).

Cross-referencing those 1,023 labels (case-insensitive) against MIM's existing 7,010 known
ingredient names + synonyms:

- **347 already known to MIM** (exact label/synonym match) — e.g. acetate, acetone, adenine,
  2-propanol, 4-hydroxybenzoate, 5-fluorouracil. Onboarding these mostly means attaching the
  microbedecoder occurrence evidence, not new curation.
- **676 net-new candidate labels** not currently in MIM — the actual net curation load.

These are conservative exact-match numbers; fuzzy/normalized matching (hydrate forms, `D-`
prefixes, catalog codes) will move more of the 676 into the "already known" column.

## Caveats the curator must handle

1. **Environment / food / host leakage.** As flagged, the isolation-category rows (347) are
   ENVO/host/food terms (`#Environmental`, `#Host`, `#Soil`, `#Marine`, `#Feces (Stool)`,
   `#Food production`, `#Herbaceous plants`). They are *not* media ingredients and should be
   routed to environmental grounding (ENVO/FOODON), not the ingredient pipeline.
2. **Media-name blends, not single chemicals.** Several `ChemicalEntity` rows are whole media
   or undefined mixtures: `PYG`, `BHI`, `PYGS`, `TYGVS`, `trypticase-glucose-yeast extract`,
   `modified cooked meat medium`, `Fastidious Anaerobe Broth with meat granules`,
   `glucose + yeast extract`. These need decomposition or a "complex medium" mapping, not a
   single CHEBI term.
3. **Label-quality noise.** Malformed splits from CSV parsing appear in the antibiotic column
   (`0129 (2`, `4-Diamino-6`, `7-di-iso-propylpteridine phosphate)` — one antibiotic name torn
   across three rows). Numeric-only labels (`1`,`2`,`3`,`4`) and unit fragments (`%(w/v)`) must
   be dropped. Filter before minting placeholders.
4. **Label variants inflate counts.** `glucose` / `D-glucose`, `fructose` / `D-fructose`,
   `mannose` / `D-mannose` are separate rows; normalization will collapse them.

## Recommended next steps (not done in this pass)

1. Route `ingredient_candidates.tsv` `already_in_mim=no` rows (676) through the
   `map-media-ingredients` skill (exact → normalized → fuzzy → manual).
2. Send the 347 isolation-category rows to environmental/ENVO grounding, out of the ingredient
   scope.
3. Decompose the ~15 media-name blends or map them as complex media.
4. For genuine residual, mint `kgmicrobe.compound:` placeholders via `manage-identifiers`,
   mirroring how microbedecoder already prefixes them.

## Reproduce

```bash
f=data/custom/microbedecoder/unmapped_labels.tsv
# chemical/ingredient candidate count
awk -F'\t' 'NR>1 && ($4 ~ /Metabolite_utilization|Metabolite_production|substrates|end_products|Antibiotic/) \
  && !($3 ~ /^[0-9]+([.,][0-9]+)?$/ || $3 ~ /^%/ || $3=="Not reported"){print tolower($3)}' $f | sort -u | wc -l
```
