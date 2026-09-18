# `data/ingredients/mapped/5-dehydro-D-gluconate.yaml`

## Verdict

Needs curation, major. The exact `CHEBI:58143` identity, anion chemistry,
microbedecoder occurrence count, SSSOM row, and aggregate copy pass, but a
source label for didehydrogluconate was folded in as a typo and is exported as
an exact synonym of the 5-dehydro-D-gluconate anion.

## Identity

- Reviewed record: `data/ingredients/mapped/5-dehydro-D-gluconate.yaml`.
- Identifier and grounding: `identifier: CHEBI:58143` with
  `ontology_mapping.ontology_id: CHEBI:58143`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, and `mapping_status: MAPPED`.
- The official ChEBI page resolves `CHEBI:58143` to
  `5-dehydro-D-gluconate`, formula `C6H9O7`, charge `-1`, the stored SMILES,
  and the stored InChI.
- Local OAK metadata reports `CHEBI:58143` as the conjugate base of
  5-dehydro-D-gluconic acid, and its formula, mass, SMILES, and InChI match
  the record.
- `ingredient_type: SINGLE_INGREDIENT` is present.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/5-Hydroxyoctanoate.yaml data/ingredients/mapped/5-Keto-D-Gluconic_Acid_Potassium_Salt.yaml data/ingredients/mapped/5-_2-thienyl-pentanoic_Acid.yaml data/ingredients/mapped/5-aminovaleric_Acid.yaml data/ingredients/mapped/5-dehydro-D-gluconate.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run linkml-term-validator validate-data data/ingredients/mapped/5-dehydro-D-gluconate.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.
- `uv run --frozen runoak -i sqlite:obo:chebi aliases CHEBI:15887 CHEBI:180039 CHEBI:17426 CHEBI:58143`:
  returned the official exact and related synonym set for `CHEBI:58143`.
- `uv run --frozen runoak -i sqlite:obo:chebi term-metadata CHEBI:15887 CHEBI:180039 CHEBI:17426 CHEBI:58143`:
  returned the expected ChEBI formula, structure strings, and mass for
  `CHEBI:58143`.
- `uv run --frozen runoak -i sqlite:obo:chebi term-metadata CHEBI:18281` and
  `uv run --frozen runoak -i sqlite:obo:chebi term-metadata CHEBI:11449`:
  confirmed that the corresponding 2,5-didehydro acid and anion are distinct
  from `CHEBI:58143`.

## Evidence

- The active ChEBI term, formula, charge, SMILES, InChI, and exact label support
  the 5-dehydro-D-gluconate anion identity imported from
  `kgmicrobe.trait:5_dehydro_d_gluconate`.
- The source occurrence count is traceable to
  `data/custom/microbedecoder/unmapped_labels.tsv`, where
  `kgmicrobe.trait:5_dehydro_d_gluconate` appears in
  `BacDive_Metabolite_production|BacDive_Metabolite_utilization` with count
  288.
- `5-didehydro-D-gluconate` is not an alias of `CHEBI:58143`, and ChEBI carries
  `CHEBI:11449` as `2,5-didehydro-D-gluconate`, the anion of the distinct
  `CHEBI:18281` acid. The current synonym and curation history assert that the
  `didehydro` source label is only a typo for `dehydro`; that assertion is not
  supported.
- The SSSOM row maps `MIM:5-dehydro-D-gluconate` to `CHEBI:58143` with
  `skos:exactMatch`, but it exports `5-didehydro-D-gluconate` in `other`.
- The hidden/ignored-inclusive search over `data`, `mappings`, `reports`,
  `scripts`, `tests`, and `src` found the active YAML, aggregate copy, SSSOM
  row, source microbedecoder row, the sibling `5-didehydro-D-gluconic_Acid`
  record whose history already supersedes the same `didehydro`-is-a-typo
  hypothesis, and ignored aggregate backups.

## Completeness

- Formula, InChI, SMILES, molecular weight, source occurrence count, and
  `ingredient_type` are populated.
- No CAS, PubChem CID, roles, components, environmental context, or discussion
  entries are required for the reviewed 5-dehydro-D-gluconate record.

## Recommended Edits

- In `data/ingredients/mapped/5-dehydro-D-gluconate.yaml`, remove
  `5-didehydro-D-gluconate` from `synonyms` and replace the
  `MERGED_FROM_UNMAPPED_DUPLICATE` history with a superseding curation event
  that points the source label at a distinct didehydrogluconate identity or
  leaves it unresolved; rebuild `mappings/ingredient_mappings.sssom.tsv` and
  `data/curated/mapped_ingredients.yaml`.
- Re-run `uv run --frozen python scripts/validate_strict.py`,
  `uv run --frozen python scripts/validate_sssom_invariants.py`,
  `uv run --frozen python scripts/validate_component_partonomy.py`, and
  `uv run --frozen python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml`
  after the edit to prove the exact-match `other` value is gone and the
  aggregate products remain consistent.
