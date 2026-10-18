# `data/ingredients/mapped/D-Serine.yaml`

## Verdict

Needs curation, with a major role-evidence issue. The exact active
`CHEBI:16523` identity, structure fields, 0/0 occurrence count, and final SSSOM
CAS alias pass, but `AMINO_ACID_SOURCE` is asserted only from provisional
CHEBI-ancestry evidence and needs direct media-use support or removal.

## Identity

- Reviewed record: `data/ingredients/mapped/D-Serine.yaml`.
- Current identifier and grounding: `identifier: CHEBI:16523`,
  `ontology_mapping.ontology_id: CHEBI:16523`,
  `ontology_label: D-serine`, `ontology_source: CHEBI`,
  `mapping_quality: EXACT_MATCH`, and `mapping_status: MAPPED`.
- Live OLS lookup by `CHEBI:16523` returns active `CHEBI:16523` labelled
  `D-serine` with formula `C3H7NO3` and matching InChI/SMILES strings.
- A hidden/ignored-inclusive exact `^identifier:` search under
  `data/ingredients` found only this record using `CHEBI:16523` as its primary
  identifier.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/D-Proline.yaml data/ingredients/mapped/D-Raffinose_Pentahydrate.yaml data/ingredients/mapped/D-Ribose.yaml data/ingredients/mapped/D-Saccharic_Acid_Potassium_Salt.yaml data/ingredients/mapped/D-Serine.yaml`:
  passed; 5 files scanned and 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/D-Proline.yaml data/ingredients/mapped/D-Ribose.yaml data/ingredients/mapped/D-Serine.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed for the three CHEBI-primary exact records in this batch.
- `uv run --frozen python scripts/aggregate_records.py --ingredients-dir data/ingredients --output-dir /tmp/mim_qc_roundtrip.wqYt47`
  followed by
  `uv run --frozen python scripts/verify_roundtrip.py --original-dir data/curated --aggregated-dir /tmp/mim_qc_roundtrip.wqYt47`:
  passed before this read-only report batch; both curated collection files had
  0 data differences and only expected scratch `generation_date` metadata
  differences.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K before this read-only report
  batch. Rule B4 was skipped because the sibling kg-microbe ontology transforms
  were absent.

## Evidence

- The record's formula, InChI, SMILES, and CAS RN agree with active
  `CHEBI:16523`.
- The hidden/ignored-inclusive membership search found no
  `CHEBI:16523` rows in `mappings/culturemech_recipe_membership.tsv`, matching
  the record's 0/0 `occurrence_statistics`.
- `mappings/ingredient_mappings_row_review_manifest.tsv` confirms the OAK/OLS
  review row with no mapping action required.
- The final SSSOM row publishes `MIM:D-Serine skos:exactMatch CHEBI:16523` and
  carries only `CAS:312-84-5` in `other`.
- The `AMINO_ACID_SOURCE` facet is supported only by
  `COMPUTATIONAL_PREDICTION` from CHEBI ancestry and its own `curator_note`
  calls it provisional.

## Completeness

- No parent mappings, supplied-form assertions, components, source occurrences,
  or additional synonyms are asserted, so there are no unsupported secondary
  claims beyond the provisional nutritional role.
- The aggregate record in `data/curated/mapped_ingredients.yaml` matches the
  per-record YAML for this reviewed entry.

## Recommended Edits

- In `data/ingredients/mapped/D-Serine.yaml`, either replace the computational
  `AMINO_ACID_SOURCE` evidence with direct CultureBotHT or source-backed
  media-role evidence for this ingredient, or remove the role facet; then rerun
  strict validation and the final SSSOM build.
