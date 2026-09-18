# `data/ingredients/mapped/L-lyxose.yaml`

## Verdict

Pass with minor issues. The MicrobeDecoder exact-label promotion to active
CHEBI:62320, source occurrence count, empty synonym payload, and final SSSOM
row are consistent; the record simply missed the later
`SINGLE_INGREDIENT`/chemistry backfill.

## Identity

- Reviewed record: `data/ingredients/mapped/L-lyxose.yaml`.
- Identifier and grounding: `identifier: CHEBI:62320` with
  `ontology_mapping.ontology_id: CHEBI:62320`, label `L-lyxose`, source
  `CHEBI`, `mapping_quality: EXACT_MATCH`, and `mapping_status: MAPPED`.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/L-lysine_Hcl.yaml data/ingredients/mapped/L-lyxose.yaml data/ingredients/mapped/L-malate.yaml data/ingredients/mapped/L-methionine.yaml data/ingredients/mapped/L-norleucine.yaml`:
  exited 0 for the 5-file batch and wrote zero ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/L-lysine_Hcl.yaml data/ingredients/mapped/L-lyxose.yaml data/ingredients/mapped/L-malate.yaml data/ingredients/mapped/L-methionine.yaml data/ingredients/mapped/L-norleucine.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  exited 0 for the 5 ChEBI records.

## Evidence

- EBI OLS4 resolves `CHEBI:62320` as active `L-lyxose`.
- PubChem resolves `L-lyxose` to CID `644176` with formula `C5H10O5`.
- The MicrobeDecoder import grounded `kgmicrobe.trait:l_lyxose` by exact OLS
  label match and records two `BacDive_Metabolite_utilization` source
  occurrences; the later `review-ingredients` event promoted the held mapping
  back to `MAPPED`.
- The final SSSOM publishes one `skos:exactMatch` row to `CHEBI:62320` with an
  empty `other` field, so no unreviewed synonyms are exported.
- The hidden and ignored-inclusive search over `data`, `mappings`, `reports`,
  `docs`, `src`, and `tests` found the current YAML, aggregate copy,
  MicrobeDecoder source rows, final SSSOM row, and docs projections.
- Minor: unlike adjacent MicrobeDecoder ChEBI imports with structural
  definitions, this record has no `ingredient_type` or `chemical_properties`
  backfill. Its identity and final SSSOM row still pass, but the ChEBI
  single-ingredient classification is incomplete.

## Completeness

- The active ChEBI identity, source occurrence count, empty synonym list,
  aggregate copy, and final SSSOM row are present and consistent.
- The empty CultureMech `occurrence_statistics` count is expected for this
  MicrobeDecoder-only import because its evidence is captured under
  `source_occurrences`.

## Recommended Edits

- Minor: classify `data/ingredients/mapped/L-lyxose.yaml` as
  `SINGLE_INGREDIENT` and backfill the CHEBI/PubChem structure the next time
  this record is touched, then sync the aggregate copy.
