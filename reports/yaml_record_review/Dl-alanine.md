# `data/ingredients/mapped/Dl-alanine.yaml`

## Verdict

Pass. The MicrobeDecoder identity exact-matches active `NCIT:C61731`
`DL-Alanine`, OLS resolves the NCIT class with the expected racemic DL-alanine
definition and synonyms, and the final SSSOM row publishes only the exact NCIT
mapping with no noisy `other` payload.

## Identity

- Reviewed record: `data/ingredients/mapped/Dl-alanine.yaml`.
- Identifier and grounding: `identifier: NCIT:C61731` with
  `ontology_mapping.ontology_id: NCIT:C61731`, source `NCIT`,
  `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and 7
  MicrobeDecoder source occurrences.
- OLS resolves `NCIT:C61731` to active `DL-Alanine`, with `DL-Alanine` as an
  exact synonym and a definition for the racemic alanine mixture.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Dl-alanine.yaml data/ingredients/mapped/Dl-alpha-lipoic_Acid.yaml data/ingredients/mapped/Dl-aspartic_Acid.yaml data/ingredients/mapped/Dl-carnitine.yaml data/ingredients/mapped/Dl-dithiothreitol.yaml`:
  exited 0 for the 5-file batch.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Dl-alanine.yaml data/ingredients/mapped/Dl-alpha-lipoic_Acid.yaml data/ingredients/mapped/Dl-aspartic_Acid.yaml data/ingredients/mapped/Dl-carnitine.yaml data/ingredients/mapped/Dl-dithiothreitol.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  exited 0 for all 5 records.
- `uv run --frozen runoak -i sqlite:obo:ncit term-metadata NCIT:C61731`:
  exited 0 but returned no local metadata; the OLS search for
  `NCIT:C61731` returned one current NCIT term for `DL-Alanine`.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 was skipped because
  the sibling kg-microbe ontology transforms were absent.
- `uv run --frozen python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml`:
  passed; all id-label pairs corresponded, with only full-corpus plausibility
  warnings.

## Evidence

- `data/curated/mapped_ingredients.yaml` contains the same maintained record
  body as the per-record YAML.
- The hidden/ignored-inclusive exact search over `data/ingredients`,
  `mappings`, and `docs/data` found the active per-record YAML, generated
  aggregate/docs rows, the MicrobeDecoder promotion review row, and the final
  SSSOM row.
- The focused hidden/ignored-inclusive search over `data/ingredients` for
  `NCIT:C61731` found only `data/ingredients/mapped/Dl-alanine.yaml`.
- `mappings/microbedecoder_auto_mapped_review.tsv` records this NCIT lexical
  match as `APPROVED`.
- The final `mappings/ingredient_mappings.sssom.tsv` row maps
  `MIM:Dl-alanine` to `NCIT:C61731` with `skos:exactMatch`, object label
  `DL-Alanine`, NCIT object source, and no `other` tokens.

## Completeness

- The MicrobeDecoder source occurrence is populated.
- Chemical structure, supplied forms, mixture components, nutritional roles,
  physicochemical roles, biological roles, and environmental contexts are
  correctly empty for this NCIT-backed exact match.

## Recommended Edits

- None.
