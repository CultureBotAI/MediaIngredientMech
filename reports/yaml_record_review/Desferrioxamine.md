# `data/ingredients/mapped/Desferrioxamine.yaml`

## Verdict

Pass. The MicrobeDecoder import exact-matches active `CHEBI:50453`
desferrioxamine, carries three BacDive sensitivity source mentions, asserts no
unsupported roles or structure fields, and exports an empty final SSSOM synonym
payload.

## Identity

- Reviewed record: `data/ingredients/mapped/Desferrioxamine.yaml`.
- Identifier and grounding: `identifier: CHEBI:50453` with
  `ontology_mapping.ontology_id: CHEBI:50453`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, and `mapping_status: MAPPED`.
- Local OAK resolves `CHEBI:50453` to active `desferrioxamine`; the term has no
  formula, InChI, or SMILES in the local ChEBI metadata, so this sparse record
  correctly leaves `chemical_properties` empty.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Delta-Undecalactone.yaml data/ingredients/mapped/Deoxycholic_Acid.yaml data/ingredients/mapped/Deoxyribonucleic_Acid_From_Herring_Sperm.yaml data/ingredients/mapped/Dermcidin.yaml data/ingredients/mapped/Desferrioxamine.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Delta-Undecalactone.yaml data/ingredients/mapped/Deoxycholic_Acid.yaml data/ingredients/mapped/Deoxyribonucleic_Acid_From_Herring_Sperm.yaml data/ingredients/mapped/Dermcidin.yaml data/ingredients/mapped/Desferrioxamine.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed all 5 records.
- `uv run --frozen runoak -i sqlite:obo:chebi term-metadata CHEBI:171846 CHEBI:28834 CHEBI:50453`:
  returned the active canonical label and ChEBI metadata for `CHEBI:50453`.
- `uv run --frozen python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml`:
  passed; all id-label pairs corresponded, with only full-corpus plausibility
  warnings.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 was skipped because
  the sibling kg-microbe ontology transforms were absent.

## Evidence

- `mappings/microbedecoder_auto_mapped_review.tsv` records the
  `Desferrioxamine.yaml` auto-mapping as approved after a local OAK label
  check.
- The hidden/ignored-inclusive exact search over active `data/ingredients`,
  `data/curated`, `mappings`, `docs/data`, `src`, `scripts`, and `tests`
  found no second active per-record YAML or stale parent-mapping row for
  `CHEBI:50453`.
- The same hidden/ignored-inclusive search found no
  `mappings/culturemech_recipe_membership.tsv` row for `CHEBI:50453`,
  matching `occurrence_statistics.total_occurrences: 0` and `media_count: 0`.
- The record is retained through `source_occurrences` from MicrobeDecoder:
  three `BacDive_Antibiotic_sensitivity` mentions.
- The final `mappings/ingredient_mappings.sssom.tsv` row maps
  `MIM:Desferrioxamine` to `CHEBI:50453` with `skos:exactMatch`, canonical
  object label `desferrioxamine`, CHEBI object source, and empty `other`.

## Completeness

- The ChEBI exact identity, MicrobeDecoder source occurrence, curation history,
  and empty final SSSOM payload are populated.
- Synonyms, mixture components, ingredient roles, supplied forms,
  environmental contexts, and chemical properties are correctly empty for this
  sparse MicrobeDecoder import.
- The aggregate copy in `data/curated/mapped_ingredients.yaml` and the
  per-record YAML agree.

## Recommended Edits

- None.
