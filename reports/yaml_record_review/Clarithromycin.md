# `data/ingredients/mapped/Clarithromycin.yaml`

## Verdict

Needs curation; major. The CultureBotHT clarithromycin record is exactly
grounded to active `CHEBI:3732`; its CAS RN, formula, InChI, SMILES, exact
synonym, zero occurrence count, SSSOM row, and aggregate copy agree. The
material gap is that `SELECTIVE_AGENT` is supported solely by a provisional
name-pattern prediction.

## Identity

- Reviewed record: `data/ingredients/mapped/Clarithromycin.yaml`.
- Identifier and grounding: `identifier: CHEBI:3732`,
  `ontology_mapping.ontology_id: CHEBI:3732`,
  `ontology_label: clarithromycin`, `ontology_source: CHEBI`,
  `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Live OLS lookup by `CHEBI:3732` returns active `CHEBI:3732` labelled
  `clarithromycin` with CAS RN `81103-11-9`, formula `C38H69NO13`, and the same
  InChI and SMILES stored in `chemical_properties`.
- `O(6)-methylerythromycin` is a ChEBI exact synonym for `CHEBI:3732`.

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
  `reports` found the active exact `MIM:Clarithromycin` SSSOM row, the
  OAK/OLS row-review confirmation, and matching aggregate/docs rows.
- Hidden/ignored-inclusive exact CURIE search under `data/ingredients` found
  `CHEBI:3732` only in this active record.
- Hidden/ignored-inclusive search of
  `mappings/culturemech_recipe_membership.tsv` found no exact `CHEBI:3732`
  rows, matching the explicit 0/0 media-recipe `occurrence_statistics`.
- The final SSSOM `other` column contains the exact ChEBI synonym
  `O(6)-methylerythromycin` and the matching `CAS:81103-11-9` value.
- `SELECTIVE_AGENT` has only `COMPUTATIONAL_PREDICTION` evidence from
  `infer_roles_from_name_lists` and is explicitly marked "Provisional role from
  a curated name-pattern rule; review recommended."

## Completeness

- The exact ChEBI identifier, CAS RN, formula, InChI, SMILES, exact synonym,
  SSSOM row, aggregate copy, docs row, and zero occurrence count are populated
  and agree.
- The only consequential gap is the unsupported provisional role.

## Recommended Edits

- Major: in `data/ingredients/mapped/Clarithromycin.yaml`, either replace
  `physicochemical_roles.SELECTIVE_AGENT` with inspected evidence for
  clarithromycin as a selective agent in this media scope, or remove the role.
- Regenerate synchronized products and rerun strict validation, SSSOM QC,
  aggregate roundtrip, and `git diff --check`.
