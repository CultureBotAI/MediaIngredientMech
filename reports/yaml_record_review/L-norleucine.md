# `data/ingredients/mapped/L-norleucine.yaml`

## Verdict

Pass. The MicrobeDecoder exact-label promotion to active CHEBI:18347, ChEBI
structure, empty synonym payload, source occurrence count, and final SSSOM row
are consistent.

## Identity

- Reviewed record: `data/ingredients/mapped/L-norleucine.yaml`.
- Identifier and grounding: `identifier: CHEBI:18347` with
  `ontology_mapping.ontology_id: CHEBI:18347`, label `L-norleucine`, source
  `CHEBI`, `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Chemical properties: molecular formula `C6H13NO2`, InChI, SMILES, and
  molecular weight from ChEBI plus PubChem.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/L-lysine_Hcl.yaml data/ingredients/mapped/L-lyxose.yaml data/ingredients/mapped/L-malate.yaml data/ingredients/mapped/L-methionine.yaml data/ingredients/mapped/L-norleucine.yaml`:
  exited 0 for the 5-file batch and wrote zero ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/L-lysine_Hcl.yaml data/ingredients/mapped/L-lyxose.yaml data/ingredients/mapped/L-malate.yaml data/ingredients/mapped/L-methionine.yaml data/ingredients/mapped/L-norleucine.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  exited 0 for the 5 ChEBI records.

## Evidence

- EBI OLS4 resolves `CHEBI:18347` as active `L-norleucine` and lists CAS
  `327-57-1`.
- PubChem resolves `L-norleucine` to CID `21236` with formula `C6H13NO2` and
  the same InChI as the YAML record.
- The MicrobeDecoder import grounded `kgmicrobe.trait:l_norleucine` by exact
  OLS label match and records one `BacDive_Metabolite_utilization` source
  occurrence; the later `review-ingredients` event promoted the held mapping
  back to `MAPPED`.
- The final SSSOM publishes one `skos:exactMatch` row to `CHEBI:18347` with an
  empty `other` field, so no unreviewed synonyms are exported.
- The hidden and ignored-inclusive search over `data`, `mappings`, `reports`,
  `docs`, `src`, and `tests` found the current YAML, aggregate copy,
  MicrobeDecoder source rows, final SSSOM row, and docs projections.

## Completeness

- The active ChEBI identity, structure, source occurrence count, empty synonym
  list, aggregate copy, and final SSSOM row are present and consistent.
- The empty CultureMech `occurrence_statistics` count is expected for this
  MicrobeDecoder-only import because its evidence is captured under
  `source_occurrences`.

## Recommended Edits

- None.
