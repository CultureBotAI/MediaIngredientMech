# `data/ingredients/mapped/Cinoxacin.yaml`

## Verdict

Pass. The MicrobeDecoder cinoxacin import is exactly grounded to active
`CHEBI:3716`; its formula, InChI, SMILES, one-count MicrobeDecoder source
occurrence, SSSOM row, zero CultureMech membership, and aggregate copy agree.

## Identity

- Reviewed record: `data/ingredients/mapped/Cinoxacin.yaml`.
- Identifier and grounding: `identifier: CHEBI:3716`,
  `ontology_mapping.ontology_id: CHEBI:3716`,
  `ontology_label: cinoxacin`, `ontology_source: CHEBI`,
  `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Live exact OLS lookup for `cinoxacin` returns one active `CHEBI:3716` term
  labelled `cinoxacin`.
- PubChem lookup by `cinoxacin` returns CID 2762, formula `C12H10N2O5`, and the
  same standard InChI stored in `chemical_properties`.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Cinoxacin.yaml data/ingredients/mapped/Ciprofloxacin.yaml data/ingredients/mapped/Ciprofloxacin_Hydrochloride.yaml data/ingredients/mapped/Cis-aconitate.yaml data/ingredients/mapped/Cisplatin.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Cinoxacin.yaml data/ingredients/mapped/Ciprofloxacin.yaml data/ingredients/mapped/Ciprofloxacin_Hydrochloride.yaml data/ingredients/mapped/Cis-aconitate.yaml data/ingredients/mapped/Cisplatin.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
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
  `reports` found the active exact `MIM:Cinoxacin` SSSOM row, the
  MicrobeDecoder import-review approval, and matching aggregate/docs rows.
- Hidden/ignored-inclusive exact CURIE search under `data/ingredients` found
  `CHEBI:3716` only in this active record.
- Hidden/ignored-inclusive search of `data/custom/microbedecoder` found
  `kgmicrobe.trait:cinoxacin` in `BacDive_Antibiotic_sensitivity` with count 1,
  matching the explicit `source_occurrences` entry.
- Hidden/ignored-inclusive search of
  `mappings/culturemech_recipe_membership.tsv` found no exact `CHEBI:3716`
  rows, matching the explicit 0/0 media-recipe `occurrence_statistics`.
- The record carries no role, component, or environment claims.

## Completeness

- The exact ChEBI identifier, formula, InChI, SMILES, source occurrence, SSSOM
  row, aggregate copy, and docs row are populated and agree.

## Recommended Edits

- None for this record.
