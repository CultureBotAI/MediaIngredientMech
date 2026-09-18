# `data/ingredients/mapped/Clindamycin.yaml`

## Verdict

Needs curation; major. The MicrobeDecoder clindamycin import is exactly
grounded to active `CHEBI:3745`, and its formula, InChI, SMILES, 104-count
MicrobeDecoder source occurrence, zero CultureMech membership, SSSOM row, and
aggregate copy agree. The active `RAW_TEXT` synonym is not an exact
`CHEBI:3745` synonym: it resolves in PubChem to CID 29029, while PubChem's
clindamycin record is CID 446598 with a different InChIKey.

## Identity

- Reviewed record: `data/ingredients/mapped/Clindamycin.yaml`.
- Identifier and grounding: `identifier: CHEBI:3745`,
  `ontology_mapping.ontology_id: CHEBI:3745`,
  `ontology_label: clindamycin`, `ontology_source: CHEBI`,
  `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Live OLS lookup by `CHEBI:3745` returns active `CHEBI:3745` labelled
  `clindamycin` with formula `C18H33ClN2O5S` and the same InChI, SMILES, and
  molecular weight stored in `chemical_properties`.
- PubChem lookup by `clindamycin` returns CID 446598 with the same standard
  InChI and InChIKey `KDLRVYVGXIQJDK-AWPVFWJPSA-N`.
- OLS exact search for the record's recovered
  `methyl 7-chloro-6,7,8-trideoxy-6-({[(2S,4R)-1-methyl-4-propylpyrrolidin-2-yl]carbonyl}amino)-1-thio-D-glycero-alpha-D-galacto-octopyranoside`
  synonym returns no ChEBI result. PubChem resolves that exact string to CID
  29029, whose InChIKey is `KDLRVYVGXIQJDK-NOWPCOIGSA-N`, not the clindamycin
  InChIKey.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Clarithromycin.yaml data/ingredients/mapped/Clavulanic_Acid.yaml data/ingredients/mapped/Clindamycin.yaml data/ingredients/mapped/Clofazimine.yaml data/ingredients/mapped/Clotrimazole.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Clarithromycin.yaml data/ingredients/mapped/Clavulanic_Acid.yaml data/ingredients/mapped/Clindamycin.yaml data/ingredients/mapped/Clofazimine.yaml data/ingredients/mapped/Clotrimazole.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed for all five CHEBI-scoped records in this batch.
- `uv run --frozen python scripts/aggregate_records.py --ingredients-dir data/ingredients --output-dir /tmp/mim_qc_roundtrip.wqYt47`
  followed by
  `uv run --frozen python scripts/verify_roundtrip.py --original-dir data/curated --aggregated-dir /tmp/mim_qc_roundtrip.wqYt47`:
  passed before this read-only report batch; both curated collection files had
  0 data differences and only the expected scratch `generation_date` metadata
  differences.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K before this read-only report
  batch. Rule B4 was skipped because the sibling kg-microbe ontology transforms
  were absent.

## Evidence

- Hidden/ignored-inclusive search over `data`, `mappings`, `docs`, and
  `reports` found the active exact `MIM:Clindamycin` SSSOM row, the
  MicrobeDecoder import-review approval, and matching aggregate/docs rows.
- Hidden/ignored-inclusive exact CURIE search under `data/ingredients` found
  `CHEBI:3745` only in this active record.
- Hidden/ignored-inclusive search of `data/custom/microbedecoder` found
  `kgmicrobe.trait:clindamycin` in `BacDive_Antibiotic_resistance` and
  `BacDive_Antibiotic_sensitivity` with count 104, matching the explicit
  `source_occurrences` entry.
- Hidden/ignored-inclusive search of
  `mappings/culturemech_recipe_membership.tsv` found no exact `CHEBI:3745`
  rows, matching the explicit 0/0 media-recipe `occurrence_statistics`.
- The final SSSOM row and docs label index still publish the CID 29029 surface
  form as a searchable `other` synonym for `CHEBI:3745`.
- The record carries no role, component, or environment claims.

## Completeness

- The exact ChEBI identifier, formula, InChI, SMILES, source occurrence, SSSOM
  row, aggregate copy, and docs row are populated and agree.
- The only active data gap is the incorrect `RAW_TEXT` synonym that reaches
  final SSSOM and search outputs.

## Recommended Edits

- Major: in `data/ingredients/mapped/Clindamycin.yaml`, remove the
  CID-29029-specific `RAW_TEXT` synonym or replace it with an exact
  ChEBI/PubChem clindamycin synonym.
- Regenerate synchronized products and rerun strict validation, SSSOM QC,
  aggregate roundtrip, and `git diff --check`.
